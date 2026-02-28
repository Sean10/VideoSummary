"""
Kiro CLI Invoker Module
Drop-in alternative to claude_invoker, using kiro-cli as the backend.

Usage:
    # 直接替换 claude_invoker 使用
    from .kiro_invoker import invoke_kiro as invoke_claude
    from .kiro_invoker import invoke_skill, invoke_skill_single
"""
import os
import re
import subprocess
import json
import logging
import time
from pathlib import Path
from typing import Dict, Any, List, Optional
import yaml

from .jsonl_handler import (
    jsonl_reader,
    jsonl_writer,
    create_error_entry,
    create_success_entry,
    is_error_entry,
    split_batches,
)

logger = logging.getLogger(__name__)

# Default timeout for Kiro CLI (300 seconds)
DEFAULT_TIMEOUT = 300

# Resolve the skills directory relative to this package
_PACKAGE_DIR = Path(__file__).resolve().parent.parent
_DEFAULT_SKILLS_DIR = str(_PACKAGE_DIR / "skills")


# ---------------------------------------------------------------------------
# 共享工具函数 (与 claude_invoker 保持一致的接口)
# ---------------------------------------------------------------------------

# 直接复用 claude_invoker 中与 CLI 无关的纯逻辑函数
from .claude_invoker import (
    _extract_json_from_response,
    load_skill,
    load_skill_with_version,
    substitute_variables,
    build_skill_prompt,
    _resolve_skills_dir,
)


# ---------------------------------------------------------------------------
# 核心调用: invoke_kiro
# ---------------------------------------------------------------------------

def invoke_kiro(
    prompt: str,
    input_file: Optional[str] = None,
    output_file: Optional[str] = None,
    timeout: int = DEFAULT_TIMEOUT,
    model: str = None,
    agent: str = None,
    extra_args: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    通过 subprocess 调用 kiro-cli chat 的非交互模式。

    等价于:
        kiro-cli chat --trust-all-tools --no-interactive "prompt"

    Args:
        prompt: 发送给 Kiro 的提示词
        input_file: 可选，让 Kiro 读取的输入文件路径
        output_file: 可选，让 Kiro 写入的输出文件路径
        timeout: 超时秒数 (默认 300)
        model: 可选的模型覆盖 (--model)
        agent: 可选的 agent 名称 (--agent)
        extra_args: 额外的 CLI 参数列表

    Returns:
        {'success': True, 'output': str} 或 {'success': False, 'error': str}
    """
    full_prompt = prompt

    if input_file:
        full_prompt += f"\n\n请读取并处理以下文件的内容: {input_file}"
    if output_file:
        full_prompt += f"\n\n请将结果写入文件: {output_file}"

    cmd = [
        "kiro-cli", "chat",
        "--trust-all-tools",
        "--no-interactive",
        full_prompt,
    ]

    if model:
        cmd.extend(["--model", model])
    if agent:
        cmd.extend(["--agent", agent])
    if extra_args:
        cmd.extend(extra_args)

    logger.info("Invoking Kiro CLI...")
    logger.debug(f"Command: {' '.join(cmd)}")

    try:
        import signal

        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=os.getcwd(),
            preexec_fn=(
                lambda: signal.signal(signal.SIGPIPE, signal.SIG_DFL)
                if hasattr(signal, "SIGPIPE")
                else None
            ),
        )

        try:
            stdout_data, stderr_data = process.communicate(timeout=timeout)
        except subprocess.TimeoutExpired:
            process.kill()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
            logger.error(f"Kiro CLI timeout after {timeout}s")
            return {"success": False, "error": f"Timeout after {timeout} seconds"}

        if process.returncode != 0:
            error_msg = stderr_data.strip() or f"Exit code: {process.returncode}"
            logger.error(f"Kiro CLI error: {error_msg}")
            return {"success": False, "error": error_msg}

        logger.info(f"Kiro CLI response: {len(stdout_data)} chars")
        return {"success": True, "output": stdout_data}

    except FileNotFoundError:
        logger.error("kiro-cli not found. Install it first: https://kiro.dev")
        return {"success": False, "error": "kiro-cli not found in PATH"}
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return {"success": False, "error": str(e)}


# 提供与 claude_invoker.invoke_claude 相同名称的别名，方便直接替换
invoke_claude = invoke_kiro


# ---------------------------------------------------------------------------
# Skill 调用 (批量)
# ---------------------------------------------------------------------------

def _process_one_batch(
    batch_idx: int,
    batch: List[Dict[str, Any]],
    base_prompt: str,
    timeout: int,
    max_retries: int,
    total_batches: int,
) -> List[Dict[str, Any]]:
    """处理单个 batch，带重试。返回该 batch 的结果列表。"""
    logger.info(f"Processing batch {batch_idx + 1}/{total_batches} ({len(batch)} items)")

    batch_content = "\n\n".join(
        f"Item {i+1}:\n{json.dumps(item, ensure_ascii=False)}"
        for i, item in enumerate(batch)
    )

    full_prompt = (
        f"{base_prompt}\n\n"
        f"请处理以下数据，每条数据生成一个结果：\n\n"
        f"{batch_content}\n\n"
        f'请返回JSONL格式的结果，每行一个结果，格式如下：\n'
        f'{{"id": "item_id", "status": "success", "result": {{...}}}}\n'
        f'或\n'
        f'{{"id": "item_id", "status": "error", "error": "错误信息"}}'
    )

    for attempt in range(max_retries):
        response = invoke_kiro(prompt=full_prompt, timeout=timeout)

        if response["success"]:
            try:
                parsed = _extract_json_from_response(response["output"])
                batch_results = [r for r in parsed if "id" in r]
                if batch_results:
                    return batch_results
                logger.warning(f"No valid JSON in response (attempt {attempt + 1})")
            except Exception as e:
                logger.error(f"Error parsing response: {e}")
        else:
            logger.warning(f"Attempt {attempt + 1} failed: {response.get('error')}")
            time.sleep(2)

    # 所有重试都失败，为 batch 中每条数据生成错误条目
    return [
        create_error_entry(item.get("id", "unknown"), "All retries exhausted")
        for item in batch
    ]


def invoke_skill(
    skill_name: str,
    input_data: List[Dict[str, Any]],
    output_file: Optional[str] = None,
    variables: Dict[str, Any] = None,
    skills_dir: str = None,
    batch_size: int = 100,
    timeout: int = DEFAULT_TIMEOUT,
    max_retries: int = 3,
    max_workers: int = 1,
) -> Dict[str, Any]:
    """
    调用 skill 批量处理数据 (通过 kiro-cli)。

    Args:
        max_workers: 并发进程数。1 = 串行 (默认)，>1 = 同时跑多个 kiro-cli。
                     例如 max_workers=4 表示最多同时 4 个 CLI 进程。
    """
    from concurrent.futures import ThreadPoolExecutor, as_completed

    if skills_dir is None:
        skills_dir = _resolve_skills_dir()

    skill = load_skill(skill_name, skills_dir)

    # 合并变量
    skill_vars = {}
    if "variables" in skill:
        for var in skill["variables"]:
            var_name = var["name"]
            if variables and var_name in variables:
                skill_vars[var_name] = variables[var_name]
            else:
                skill_vars[var_name] = var.get("default", "")
    if variables:
        skill_vars.update(variables)

    base_prompt = build_skill_prompt(skill, skill_vars)
    batches = split_batches(input_data, batch_size)
    total_batches = len(batches)

    results: List[Dict[str, Any]] = []
    total_processed = 0
    total_errors = 0

    effective_workers = min(max_workers, total_batches) if max_workers > 1 else 1
    logger.info(f"Running {total_batches} batches with max_workers={effective_workers}")

    if effective_workers <= 1:
        # 串行路径 (向后兼容)
        for batch_idx, batch in enumerate(batches):
            batch_results = _process_one_batch(
                batch_idx, batch, base_prompt, timeout, max_retries, total_batches
            )
            for r in batch_results:
                results.append(r)
                if is_error_entry(r):
                    total_errors += 1
                else:
                    total_processed += 1
    else:
        # 并发路径
        with ThreadPoolExecutor(max_workers=effective_workers) as executor:
            future_to_idx = {
                executor.submit(
                    _process_one_batch,
                    idx, batch, base_prompt, timeout, max_retries, total_batches
                ): idx
                for idx, batch in enumerate(batches)
            }
            for future in as_completed(future_to_idx):
                batch_idx = future_to_idx[future]
                try:
                    batch_results = future.result()
                except Exception as e:
                    logger.error(f"Batch {batch_idx} raised exception: {e}")
                    batch_results = [
                        create_error_entry(
                            item.get("id", "unknown"), str(e)
                        )
                        for item in batches[batch_idx]
                    ]
                for r in batch_results:
                    results.append(r)
                    if is_error_entry(r):
                        total_errors += 1
                    else:
                        total_processed += 1

    if output_file is not None:
        jsonl_writer(output_file, results)

    return {
        "success": total_errors == 0,
        "processed": total_processed,
        "errors": total_errors,
        "total": len(input_data),
    }


# ---------------------------------------------------------------------------
# Skill 调用 (单条)
# ---------------------------------------------------------------------------

def invoke_skill_single(
    skill_name: str,
    input_item: Dict[str, Any],
    variables: Dict[str, Any] = None,
    skills_dir: str = None,
    timeout: int = DEFAULT_TIMEOUT,
) -> Dict[str, Any]:
    """
    调用 skill 处理单条数据 (通过 kiro-cli)。

    接口与 claude_invoker.invoke_skill_single 完全一致。
    """
    if skills_dir is None:
        skills_dir = _resolve_skills_dir()

    skill = load_skill(skill_name, skills_dir)

    skill_vars = {}
    if "variables" in skill:
        for var in skill["variables"]:
            var_name = var["name"]
            if variables and var_name in variables:
                skill_vars[var_name] = variables[var_name]
            else:
                skill_vars[var_name] = var.get("default", "")
    if variables:
        skill_vars.update(variables)

    base_prompt = build_skill_prompt(skill, skill_vars)
    item_content = json.dumps(input_item, ensure_ascii=False)

    full_prompt = (
        f"{base_prompt}\n\n"
        f"请处理以下数据:\n\n"
        f"{item_content}\n\n"
        f'请返回JSON格式的结果:\n'
        f'{{"id": "item_id", "status": "success", "result": {{...}}}}'
    )

    response = invoke_kiro(prompt=full_prompt, timeout=timeout)

    if not response["success"]:
        return create_error_entry(
            input_item.get("id", "unknown"),
            response.get("error", "Unknown error"),
        )

    parsed = _extract_json_from_response(response["output"])
    if parsed:
        return parsed[0]

    return create_error_entry(
        input_item.get("id", "unknown"),
        f"Failed to parse response: {response['output'][:200]}",
    )
