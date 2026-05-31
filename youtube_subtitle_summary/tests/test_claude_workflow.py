"""Tests for claude_workflow module — integration-level tests with mocked CLI."""
import json
import os
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

from libylt2summary.claude_workflow import (
    prepare_summarize_input,
    run_summarize_workflow,
    prepare_reflect_input,
    run_reflect_workflow,
    run_classify_workflow,
)
from libylt2summary.jsonl_handler import jsonl_writer, jsonl_reader


SKILLS_DIR = str(Path(__file__).resolve().parent.parent / "skills")


@pytest.fixture
def workspace(tmp_path):
    """Create a minimal workspace with subtitles and metadata."""
    subtitles_dir = tmp_path / "subtitles_origin"
    subtitles_dir.mkdir()

    subtitle_file = subtitles_dir / "Test_Video.en.ttml"
    subtitle_file.write_text(
        '<tt><body><div><p begin="00:00:01" end="00:00:05">Hello this is a Ceph meeting</p></div></body></tt>',
        encoding="utf-8"
    )

    meta_file = tmp_path / "videos_meta.jsonl"
    jsonl_writer(str(meta_file), [
        {
            "title": "Test_Video.en.ttml",
            "published_at": "2024-01-15T00:00:00Z",
            "channel": "Ceph",
            "duration": "PT30M"
        }
    ])

    summary_dir = tmp_path / "summary"
    summary_dir.mkdir()

    temp_input = tmp_path / "temp_input"
    temp_input.mkdir()

    return tmp_path


class TestPrepareSummarizeInput:
    def test_prepares_items(self, workspace):
        items = prepare_summarize_input(
            subtitles_dir=str(workspace / "subtitles_origin"),
            videos_meta=str(workspace / "videos_meta.jsonl"),
            output_file=str(workspace / "temp_input" / "summarize_input.jsonl")
        )
        assert len(items) == 1
        assert items[0]["id"] == "Test_Video.en"
        assert "content" in items[0]

    def test_skips_already_summarized(self, workspace):
        summary_file = workspace / "summary" / "Test_Video.en.md"
        summary_file.write_text("existing summary", encoding="utf-8")

        original_cwd = os.getcwd()
        os.chdir(str(workspace))
        try:
            items = prepare_summarize_input(
                subtitles_dir=str(workspace / "subtitles_origin"),
                videos_meta=str(workspace / "videos_meta.jsonl"),
                output_file=str(workspace / "temp_input" / "summarize_input.jsonl")
            )
            assert len(items) == 0
        finally:
            os.chdir(original_cwd)

    def test_empty_subtitles_dir(self, workspace):
        empty_dir = workspace / "empty_subs"
        empty_dir.mkdir()
        items = prepare_summarize_input(
            subtitles_dir=str(empty_dir),
            videos_meta=str(workspace / "videos_meta.jsonl"),
            output_file=str(workspace / "temp_input" / "summarize_input.jsonl")
        )
        assert items == []


class TestRunSummarizeWorkflow:
    @patch("libylt2summary.claude_workflow.invoke_skill")
    def test_end_to_end(self, mock_invoke, workspace):
        input_file = str(workspace / "temp_input" / "summarize_input.jsonl")
        jsonl_writer(input_file, [{"id": "Test_Video.en", "content": "test content"}])

        output_dir = str(workspace / "summary")
        results_file = os.path.join(output_dir, "results.jsonl")

        mock_invoke.return_value = {
            "success": True,
            "processed": 1,
            "errors": 0,
            "total": 1
        }
        jsonl_writer(results_file, [
            {"id": "Test_Video.en", "status": "success", "result": {"summary": "# Meeting Summary\nCeph performance discussed"}}
        ])

        result = run_summarize_workflow(
            input_file=input_file,
            output_dir=output_dir
        )
        assert result["processed"] == 1

        md_file = os.path.join(output_dir, "Test_Video.en.md")
        assert os.path.exists(md_file)

    def test_missing_input_file(self, workspace):
        result = run_summarize_workflow(
            input_file=str(workspace / "nonexistent.jsonl"),
            output_dir=str(workspace / "summary")
        )
        assert result["success"] is False


class TestRunClassifyWorkflow:
    @patch("libylt2summary.claude_workflow.invoke_skill")
    def test_classifies_posts(self, mock_invoke, workspace):
        posts_dir = workspace / "source" / "_posts"
        posts_dir.mkdir(parents=True)
        (posts_dir / "Ceph_OSD_Deep_Dive.md").write_text("content", encoding="utf-8")
        (posts_dir / "CRUSH_Algorithm.md").write_text("content", encoding="utf-8")

        temp_output = "temp_classify_results.jsonl"
        mock_invoke.return_value = {"success": True, "processed": 1, "errors": 0, "total": 1}

        original_cwd = os.getcwd()
        os.chdir(str(workspace))
        try:
            jsonl_writer(temp_output, [
                {"id": "batch_0", "status": "success", "result": {
                    "RADOS 核心": ["Ceph_OSD_Deep_Dive.md", "CRUSH_Algorithm.md"],
                    "技术深度探讨": ["Ceph_OSD_Deep_Dive.md"]
                }}
            ])

            output_file = str(workspace / "classification.json")
            result = run_classify_workflow(
                posts_dir=str(posts_dir),
                output_file=output_file
            )
            assert result["processed"] == 1

            assert os.path.exists(output_file)
            with open(output_file, "r") as f:
                classification = json.load(f)
            assert "RADOS 核心" in classification
        finally:
            os.chdir(original_cwd)
            if os.path.exists(temp_output):
                os.remove(temp_output)
