"""
Claude Code Invoker Module
Provides utilities to invoke Claude Code CLI via subprocess
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
    is_error_entry
)

logger = logging.getLogger(__name__)

# Default timeout for Claude Code CLI (300 seconds)
DEFAULT_TIMEOUT = 300

# Resolve the skills directory relative to this package
_PACKAGE_DIR = Path(__file__).resolve().parent.parent
_DEFAULT_SKILLS_DIR = str(_PACKAGE_DIR / "skills")


def _resolve_skills_dir() -> str:
    """Return the absolute path to the skills directory."""
    return _DEFAULT_SKILLS_DIR


def _extract_json_from_response(text: str) -> List[Dict[str, Any]]:
    """
    Extract JSON objects from Claude CLI response, handling markdown
    code fences and mixed text output.
    """
    results = []

    # Strip markdown code fences (```json ... ``` or ```jsonl ... ```)
    fence_pattern = r'```(?:json|jsonl)?\s*\n(.*?)```'
    fenced_blocks = re.findall(fence_pattern, text, re.DOTALL)
    if fenced_blocks:
        text_to_parse = '\n'.join(fenced_blocks)
    else:
        text_to_parse = text

    for line in text_to_parse.strip().split('\n'):
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
            if isinstance(obj, dict):
                results.append(obj)
        except json.JSONDecodeError:
            continue

    # Fallback: try parsing the entire text as a single JSON object
    if not results:
        try:
            obj = json.loads(text_to_parse.strip())
            if isinstance(obj, dict):
                results.append(obj)
            elif isinstance(obj, list):
                results.extend(item for item in obj if isinstance(item, dict))
        except json.JSONDecodeError:
            pass

    return results


def load_skill(skill_name: str, skills_dir: str = None) -> Dict[str, Any]:
    """
    Load a skill definition from YAML file.

    Args:
        skill_name: Name of the skill (e.g., "summarize", "translate")
        skills_dir: Directory containing skill YAML files

    Returns:
        Skill definition dictionary

    Raises:
        FileNotFoundError: If skill doesn't exist
        yaml.YAMLError: If YAML is invalid
    """
    if skills_dir is None:
        skills_dir = _resolve_skills_dir()

    skill_path = Path(skills_dir) / skill_name / "skill.yaml"

    if not skill_path.exists():
        raise FileNotFoundError(f"Skill not found: {skill_name} (expected: {skill_path})")

    with open(skill_path, 'r', encoding='utf-8') as f:
        skill = yaml.safe_load(f)

    logger.info(f"Loaded skill: {skill['name']} v{skill['version']}")
    return skill


def load_skill_with_version(skill_name: str, version: str = None, skills_dir: str = None) -> Dict[str, Any]:
    """
    Load a skill with specific version or latest.

    Args:
        skill_name: Name of the skill
        version: Specific version (e.g., "1.2.0") or None for latest
        skills_dir: Directory containing skill YAML files

    Returns:
        Skill definition dictionary
    """
    # For now, just load the skill (versioning to be implemented)
    return load_skill(skill_name, skills_dir)


def substitute_variables(template: str, variables: Dict[str, Any]) -> str:
    """
    Replace {{variable}} placeholders in template with values.

    Args:
        template: Template string with {{variable}} placeholders
        variables: Dictionary of variable values

    Returns:
        Template with variables replaced
    """
    result = template

    # Find all {{variable}} patterns
    pattern = r'\{\{(\w+)\}\}'
    matches = re.findall(pattern, template)

    for var_name in matches:
        if var_name in variables:
            value = variables[var_name]
            # Handle multiline values
            if isinstance(value, list):
                value = '\n'.join(str(v) for v in value)
            result = result.replace(f'{{{{{var_name}}}}}', str(value))
        # If variable not found, leave placeholder unchanged

    return result


def build_skill_prompt(skill: Dict[str, Any], variables: Dict[str, Any] = None) -> str:
    """
    Build the full prompt from a skill definition.

    Args:
        skill: Skill definition dictionary
        variables: Variables to substitute in the prompt

    Returns:
        Full prompt string
    """
    prompt = skill.get('system_prompt', '')

    if variables:
        prompt = substitute_variables(prompt, variables)

    return prompt


def invoke_claude(
    prompt: str,
    input_file: Optional[str] = None,
    output_file: Optional[str] = None,
    timeout: int = DEFAULT_TIMEOUT,
    model: str = None
) -> Dict[str, Any]:
    """
    Invoke Claude Code CLI via subprocess.

    Args:
        prompt: Prompt to send to Claude Code
        input_file: Optional input file path for Claude to read
        output_file: Optional output file path for Claude to write
        timeout: Timeout in seconds (default: 300)
        model: Optional model override

    Returns:
        Dictionary with 'success' boolean and either 'output' or 'error'

    Raises:
        subprocess.TimeoutExpired: If CLI exceeds timeout
        subprocess.CalledProcessError: If CLI returns non-zero exit code
    """
    full_prompt = prompt

    if input_file:
        full_prompt += f"\n\n请读取并处理以下文件的内容: {input_file}"

    if output_file:
        full_prompt += f"\n\n请将结果写入文件: {output_file}"

    cmd = ["claude", "-p", full_prompt, "--output-format", "text"]

    if model:
        cmd.extend(["--model", model])

    logger.info(f"Invoking Claude Code CLI...")

    try:
        import select
        import signal
        
        logger.info(f"Command: {' '.join(cmd)}")
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=os.getcwd(),
            preexec_fn=lambda: signal.signal(signal.SIGPIPE, signal.SIG_DFL) if hasattr(signal, 'SIGPIPE') else None
        )
        
        try:
            stdout_data, stderr_data = process.communicate(timeout=timeout)
        except subprocess.TimeoutExpired:
            process.kill()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
            logger.error(f"Claude Code timeout after {timeout}s")
            return {
                'success': False,
                'error': f"Timeout after {timeout} seconds"
            }
        
        if process.returncode != 0:
            error_msg = stderr_data or f"Exit code: {process.returncode}"
            logger.error(f"Claude Code error: {error_msg}")
            return {
                'success': False,
                'error': error_msg
            }

        logger.info(f"Claude Code response: {len(stdout_data)} chars")

        return {
            'success': True,
            'output': stdout_data
        }

    except FileNotFoundError:
        logger.error("Claude Code CLI not found. Make sure it's installed.")
        return {
            'success': False,
            'error': "Claude Code CLI not found"
        }
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return {
            'success': False,
            'error': str(e)
        }


def _process_one_batch_claude(
    batch_idx: int,
    batch: List[Dict[str, Any]],
    base_prompt: str,
    timeout: int,
    max_retries: int,
    total_batches: int,
) -> List[Dict[str, Any]]:
    """处理单个 batch，带重试。返回该 batch 的结果列表。"""
    logger.info(f"Processing batch {batch_idx + 1}/{total_batches} ({len(batch)} items)")

    batch_content = "\n\n".join([
        f"Item {i+1}:\n{json.dumps(item, ensure_ascii=False)}"
        for i, item in enumerate(batch)
    ])

    full_prompt = f"""{base_prompt}

请处理以下数据，每条数据生成一个结果：

{batch_content}

请返回JSONL格式的结果，每行一个结果，格式如下：
{{"id": "item_id", "status": "success", "result": {{...}}}}
或
{{"id": "item_id", "status": "error", "error": "错误信息"}}
"""

    for attempt in range(max_retries):
        response = invoke_claude(prompt=full_prompt, timeout=timeout)

        if response['success']:
            try:
                parsed = _extract_json_from_response(response['output'])
                batch_results = [r for r in parsed if 'id' in r]
                if batch_results:
                    return batch_results
                logger.warning(f"No valid JSON found in response (attempt {attempt + 1})")
            except Exception as e:
                logger.error(f"Error parsing response: {e}")
        else:
            logger.warning(f"Attempt {attempt + 1} failed: {response.get('error')}")
            time.sleep(2)

    # 所有重试都失败
    return [
        create_error_entry(item.get('id', 'unknown'), "All retries exhausted")
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
    max_workers: int = 1
) -> Dict[str, Any]:
    """
    Invoke a skill to process input data.

    Args:
        skill_name: Name of the skill to invoke
        input_data: List of input items
        output_file: Path to output JSONL file (None to skip writing)
        variables: Additional variables for prompt substitution
        skills_dir: Directory containing skills (auto-resolved if None)
        batch_size: Items per batch
        timeout: Timeout per batch
        max_retries: Number of retries on failure
        max_workers: 并发进程数。1 = 串行 (默认)，>1 = 同时跑多个 CLI 进程。

    Returns:
        Dictionary with 'success', 'processed', 'errors' counts
    """
    from concurrent.futures import ThreadPoolExecutor, as_completed

    if skills_dir is None:
        skills_dir = _resolve_skills_dir()

    skill = load_skill(skill_name, skills_dir)

    skill_vars = {}
    if 'variables' in skill:
        for var in skill['variables']:
            var_name = var['name']
            if variables and var_name in variables:
                skill_vars[var_name] = variables[var_name]
            else:
                skill_vars[var_name] = var.get('default', '')

    if variables:
        skill_vars.update(variables)

    base_prompt = build_skill_prompt(skill, skill_vars)

    from .jsonl_handler import split_batches
    batches = split_batches(input_data, batch_size)
    total_batches = len(batches)

    results = []
    total_processed = 0
    total_errors = 0

    effective_workers = min(max_workers, total_batches) if max_workers > 1 else 1
    logger.info(f"Running {total_batches} batches with max_workers={effective_workers}")

    if effective_workers <= 1:
        # 串行路径 (向后兼容)
        for batch_idx, batch in enumerate(batches):
            batch_results = _process_one_batch_claude(
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
                    _process_one_batch_claude,
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
                            item.get('id', 'unknown'), str(e)
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
        'success': total_errors == 0,
        'processed': total_processed,
        'errors': total_errors,
        'total': len(input_data)
    }


def invoke_skill_single(
    skill_name: str,
    input_item: Dict[str, Any],
    variables: Dict[str, Any] = None,
    skills_dir: str = None,
    timeout: int = DEFAULT_TIMEOUT
) -> Dict[str, Any]:
    """
    Invoke a skill for a single item without writing to file.

    Args:
        skill_name: Name of the skill
        input_item: Single input item
        variables: Variables for prompt
        skills_dir: Skills directory (auto-resolved if None)
        timeout: Timeout in seconds

    Returns:
        Result dictionary with 'success' and either 'result' or 'error'
    """
    if skills_dir is None:
        skills_dir = _resolve_skills_dir()

    skill = load_skill(skill_name, skills_dir)

    skill_vars = {}
    if 'variables' in skill:
        for var in skill['variables']:
            var_name = var['name']
            if variables and var_name in variables:
                skill_vars[var_name] = variables[var_name]
            else:
                skill_vars[var_name] = var.get('default', '')
    if variables:
        skill_vars.update(variables)

    base_prompt = build_skill_prompt(skill, skill_vars)
    item_content = json.dumps(input_item, ensure_ascii=False)

    full_prompt = f"""{base_prompt}

请处理以下数据:

{item_content}

请返回JSON格式的结果:
{{"id": "item_id", "status": "success", "result": {{...}}}}
"""

    response = invoke_claude(prompt=full_prompt, timeout=timeout)

    if not response['success']:
        return create_error_entry(
            input_item.get('id', 'unknown'),
            response.get('error', 'Unknown error')
        )

    output = response['output']
    parsed = _extract_json_from_response(output)
    if parsed:
        return parsed[0]

    return create_error_entry(
        input_item.get('id', 'unknown'),
        f"Failed to parse response: {output[:200]}"
    )
