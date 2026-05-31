"""Tests for claude_invoker module."""
import json
import os
import subprocess
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

from libylt2summary.claude_invoker import (
    load_skill,
    substitute_variables,
    build_skill_prompt,
    invoke_claude,
    invoke_skill,
    invoke_skill_single,
    _resolve_skills_dir,
    _extract_json_from_response,
)


SKILLS_DIR = str(Path(__file__).resolve().parent.parent / "skills")


class TestResolveSkillsDir:
    def test_returns_absolute_path(self):
        result = _resolve_skills_dir()
        assert os.path.isabs(result)
        assert result.endswith("skills")


class TestExtractJsonFromResponse:
    def test_plain_jsonl(self):
        text = '{"id": "1", "status": "success", "result": {}}\n{"id": "2", "status": "error", "error": "fail"}'
        result = _extract_json_from_response(text)
        assert len(result) == 2
        assert result[0]["id"] == "1"

    def test_fenced_json(self):
        text = 'Here is the result:\n```json\n{"id": "1", "status": "success", "result": {"summary": "test"}}\n```\n'
        result = _extract_json_from_response(text)
        assert len(result) == 1
        assert result[0]["id"] == "1"

    def test_fenced_jsonl(self):
        text = '```jsonl\n{"id": "1", "status": "success"}\n{"id": "2", "status": "success"}\n```'
        result = _extract_json_from_response(text)
        assert len(result) == 2

    def test_mixed_text_and_json(self):
        text = 'Processing complete.\n{"id": "1", "status": "success", "result": {}}\nDone.'
        result = _extract_json_from_response(text)
        assert len(result) == 1

    def test_single_json_object(self):
        text = '{"id": "1", "status": "success", "result": {"summary": "hello"}}'
        result = _extract_json_from_response(text)
        assert len(result) == 1

    def test_json_array_fallback(self):
        text = '[{"id": "1"}, {"id": "2"}]'
        result = _extract_json_from_response(text)
        assert len(result) == 2

    def test_no_json(self):
        text = "This is just plain text with no JSON."
        result = _extract_json_from_response(text)
        assert result == []

    def test_empty_input(self):
        assert _extract_json_from_response("") == []


class TestLoadSkill:
    def test_loads_summarize_skill(self):
        skill = load_skill("summarize", SKILLS_DIR)
        assert skill["name"] == "summarize"
        assert skill["version"] == "1.0.0"
        assert "system_prompt" in skill
        assert "input_schema" in skill
        assert "output_schema" in skill

    def test_loads_all_skills(self):
        for skill_name in ["summarize", "translate", "reflect", "classify"]:
            skill = load_skill(skill_name, SKILLS_DIR)
            assert skill["name"] == skill_name

    def test_nonexistent_skill(self):
        with pytest.raises(FileNotFoundError):
            load_skill("nonexistent_skill", SKILLS_DIR)

    def test_default_skills_dir(self):
        skill = load_skill("summarize")
        assert skill["name"] == "summarize"


class TestSubstituteVariables:
    def test_single_variable(self):
        result = substitute_variables("Hello {{name}}", {"name": "World"})
        assert result == "Hello World"

    def test_multiple_variables(self):
        result = substitute_variables(
            "{{greeting}} {{name}}!",
            {"greeting": "Hi", "name": "Ceph"}
        )
        assert result == "Hi Ceph!"

    def test_missing_variable_unchanged(self):
        result = substitute_variables("Hello {{name}}", {})
        assert result == "Hello {{name}}"

    def test_list_value(self):
        result = substitute_variables("Keywords: {{kw}}", {"kw": ["a", "b", "c"]})
        assert result == "Keywords: a\nb\nc"


class TestBuildSkillPrompt:
    def test_builds_with_variables(self):
        skill = {
            "system_prompt": "You are a {{role}} expert.",
            "variables": [{"name": "role", "default": "storage"}]
        }
        result = build_skill_prompt(skill, {"role": "Ceph"})
        assert "Ceph" in result
        assert "{{role}}" not in result

    def test_builds_without_variables(self):
        skill = {"system_prompt": "You are an expert."}
        result = build_skill_prompt(skill)
        assert result == "You are an expert."


class TestInvokeClaude:
    @patch("libylt2summary.claude_invoker.subprocess.run")
    def test_success(self, mock_run):
        mock_run.return_value = MagicMock(
            returncode=0,
            stdout='{"id": "1", "status": "success"}',
            stderr=""
        )
        result = invoke_claude("test prompt")
        assert result["success"] is True
        assert "output" in result

    @patch("libylt2summary.claude_invoker.subprocess.run")
    def test_nonzero_exit(self, mock_run):
        mock_run.return_value = MagicMock(
            returncode=1,
            stdout="",
            stderr="Error occurred"
        )
        result = invoke_claude("test prompt")
        assert result["success"] is False
        assert "Error occurred" in result["error"]

    @patch("libylt2summary.claude_invoker.subprocess.run")
    def test_timeout(self, mock_run):
        mock_run.side_effect = subprocess.TimeoutExpired("claude", 300)
        result = invoke_claude("test prompt", timeout=300)
        assert result["success"] is False
        assert "Timeout" in result["error"]

    @patch("libylt2summary.claude_invoker.subprocess.run")
    def test_cli_not_found(self, mock_run):
        mock_run.side_effect = FileNotFoundError()
        result = invoke_claude("test prompt")
        assert result["success"] is False
        assert "not found" in result["error"]

    @patch("libylt2summary.claude_invoker.subprocess.run")
    def test_input_file_appended_to_prompt(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0, stdout="ok", stderr="")
        invoke_claude("prompt", input_file="/tmp/input.jsonl")
        call_args = mock_run.call_args
        cmd = call_args[0][0]
        prompt_arg = cmd[cmd.index("-p") + 1]
        assert "/tmp/input.jsonl" in prompt_arg

    @patch("libylt2summary.claude_invoker.subprocess.run")
    def test_model_param(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0, stdout="ok", stderr="")
        invoke_claude("prompt", model="opus")
        cmd = mock_run.call_args[0][0]
        assert "--model" in cmd
        assert "opus" in cmd


class TestInvokeSkill:
    @patch("libylt2summary.claude_invoker.invoke_claude")
    def test_single_item_batch(self, mock_invoke):
        mock_invoke.return_value = {
            "success": True,
            "output": '{"id": "v1", "status": "success", "result": {"summary": "test"}}'
        }
        result = invoke_skill(
            skill_name="summarize",
            input_data=[{"id": "v1", "content": "test"}],
            skills_dir=SKILLS_DIR,
            batch_size=10,
            max_retries=1
        )
        assert result["processed"] == 1
        assert result["errors"] == 0

    @patch("libylt2summary.claude_invoker.invoke_claude")
    def test_writes_output_file(self, mock_invoke, tmp_path):
        mock_invoke.return_value = {
            "success": True,
            "output": '{"id": "v1", "status": "success", "result": {}}'
        }
        out_file = str(tmp_path / "out.jsonl")
        invoke_skill(
            skill_name="summarize",
            input_data=[{"id": "v1", "content": "test"}],
            output_file=out_file,
            skills_dir=SKILLS_DIR,
            batch_size=10,
            max_retries=1
        )
        assert os.path.exists(out_file)

    @patch("libylt2summary.claude_invoker.invoke_claude")
    def test_no_output_file(self, mock_invoke):
        mock_invoke.return_value = {
            "success": True,
            "output": '{"id": "v1", "status": "success", "result": {}}'
        }
        result = invoke_skill(
            skill_name="summarize",
            input_data=[{"id": "v1", "content": "test"}],
            output_file=None,
            skills_dir=SKILLS_DIR,
            batch_size=10,
            max_retries=1
        )
        assert result["processed"] == 1

    @patch("libylt2summary.claude_invoker.invoke_claude")
    def test_cli_failure_produces_error_entries(self, mock_invoke):
        mock_invoke.return_value = {
            "success": False,
            "error": "CLI not found"
        }
        result = invoke_skill(
            skill_name="summarize",
            input_data=[{"id": "v1", "content": "test"}, {"id": "v2", "content": "test2"}],
            skills_dir=SKILLS_DIR,
            batch_size=10,
            max_retries=1
        )
        assert result["errors"] == 2
        assert result["processed"] == 0

    @patch("libylt2summary.claude_invoker.invoke_claude")
    def test_handles_fenced_response(self, mock_invoke):
        mock_invoke.return_value = {
            "success": True,
            "output": '```json\n{"id": "v1", "status": "success", "result": {"summary": "ok"}}\n```'
        }
        result = invoke_skill(
            skill_name="summarize",
            input_data=[{"id": "v1", "content": "test"}],
            skills_dir=SKILLS_DIR,
            batch_size=10,
            max_retries=1
        )
        assert result["processed"] == 1


class TestInvokeSkillSingle:
    @patch("libylt2summary.claude_invoker.invoke_claude")
    def test_returns_result(self, mock_invoke):
        mock_invoke.return_value = {
            "success": True,
            "output": '{"id": "v1", "status": "success", "result": {"summary": "done"}}'
        }
        result = invoke_skill_single(
            skill_name="summarize",
            input_item={"id": "v1", "content": "subtitle text"},
            skills_dir=SKILLS_DIR
        )
        assert result["status"] == "success"

    @patch("libylt2summary.claude_invoker.invoke_claude")
    def test_handles_cli_failure(self, mock_invoke):
        mock_invoke.return_value = {"success": False, "error": "timeout"}
        result = invoke_skill_single(
            skill_name="summarize",
            input_item={"id": "v1", "content": "text"},
            skills_dir=SKILLS_DIR
        )
        assert result["status"] == "error"

    @patch("libylt2summary.claude_invoker.invoke_claude")
    def test_handles_unparseable_response(self, mock_invoke):
        mock_invoke.return_value = {
            "success": True,
            "output": "This is not JSON at all"
        }
        result = invoke_skill_single(
            skill_name="summarize",
            input_item={"id": "v1", "content": "text"},
            skills_dir=SKILLS_DIR
        )
        assert result["status"] == "error"
