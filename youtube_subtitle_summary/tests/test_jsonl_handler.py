"""Tests for jsonl_handler module."""
import json
import os
import tempfile
import pytest

from libylt2summary.jsonl_handler import (
    jsonl_reader,
    jsonl_reader_iter,
    jsonl_writer,
    jsonl_append,
    split_batches,
    create_batches_with_metadata,
    create_error_entry,
    create_success_entry,
    is_error_entry,
    is_success_entry,
)


@pytest.fixture
def tmp_jsonl(tmp_path):
    """Create a temporary JSONL file with sample data."""
    file_path = str(tmp_path / "test.jsonl")
    records = [
        {"id": "v1", "title": "Video 1"},
        {"id": "v2", "title": "Video 2"},
        {"id": "v3", "title": "Video 3"},
    ]
    with open(file_path, "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    return file_path, records


class TestJsonlReader:
    def test_reads_all_records(self, tmp_jsonl):
        path, expected = tmp_jsonl
        result = jsonl_reader(path)
        assert result == expected

    def test_skips_empty_lines(self, tmp_path):
        path = str(tmp_path / "empty_lines.jsonl")
        with open(path, "w") as f:
            f.write('{"id": "1"}\n\n\n{"id": "2"}\n')
        result = jsonl_reader(path)
        assert len(result) == 2

    def test_skips_malformed_lines(self, tmp_path):
        path = str(tmp_path / "bad.jsonl")
        with open(path, "w") as f:
            f.write('{"id": "1"}\nnot json\n{"id": "2"}\n')
        result = jsonl_reader(path)
        assert len(result) == 2

    def test_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            jsonl_reader("/nonexistent/file.jsonl")


class TestJsonlReaderIter:
    def test_iterates_records(self, tmp_jsonl):
        path, expected = tmp_jsonl
        result = list(jsonl_reader_iter(path))
        assert result == expected


class TestJsonlWriter:
    def test_writes_records(self, tmp_path):
        path = str(tmp_path / "out.jsonl")
        data = [{"id": "a"}, {"id": "b"}]
        count = jsonl_writer(path, data)
        assert count == 2
        result = jsonl_reader(path)
        assert result == data

    def test_append_mode(self, tmp_path):
        path = str(tmp_path / "append.jsonl")
        jsonl_writer(path, [{"id": "1"}])
        jsonl_writer(path, [{"id": "2"}], append=True)
        result = jsonl_reader(path)
        assert len(result) == 2

    def test_unicode_content(self, tmp_path):
        path = str(tmp_path / "unicode.jsonl")
        data = [{"id": "1", "title": "Ceph 性能调优"}]
        jsonl_writer(path, data)
        result = jsonl_reader(path)
        assert result[0]["title"] == "Ceph 性能调优"


class TestJsonlAppend:
    def test_appends_single_record(self, tmp_path):
        path = str(tmp_path / "single.jsonl")
        jsonl_writer(path, [{"id": "1"}])
        jsonl_append(path, {"id": "2"})
        result = jsonl_reader(path)
        assert len(result) == 2
        assert result[1]["id"] == "2"


class TestSplitBatches:
    def test_splits_evenly(self):
        data = [{"id": str(i)} for i in range(10)]
        batches = split_batches(data, batch_size=5)
        assert len(batches) == 2
        assert len(batches[0]) == 5
        assert len(batches[1]) == 5

    def test_splits_with_remainder(self):
        data = [{"id": str(i)} for i in range(7)]
        batches = split_batches(data, batch_size=3)
        assert len(batches) == 3
        assert len(batches[2]) == 1

    def test_single_batch(self):
        data = [{"id": "1"}, {"id": "2"}]
        batches = split_batches(data, batch_size=100)
        assert len(batches) == 1

    def test_empty_data(self):
        batches = split_batches([], batch_size=10)
        assert batches == []


class TestCreateBatchesWithMetadata:
    def test_metadata_fields(self):
        data = [{"id": str(i)} for i in range(5)]
        batches = create_batches_with_metadata(data, batch_size=3)
        assert len(batches) == 2
        assert batches[0]["batch_id"] == 0
        assert batches[0]["total_batches"] == 2
        assert batches[0]["batch_size"] == 3
        assert len(batches[0]["data"]) == 3
        assert batches[1]["batch_size"] == 2


class TestErrorProtocol:
    def test_create_error_entry(self):
        entry = create_error_entry("vid1", "timeout")
        assert entry == {"id": "vid1", "status": "error", "error": "timeout"}

    def test_create_success_entry(self):
        result = {"summary": "test"}
        entry = create_success_entry("vid1", result)
        assert entry["id"] == "vid1"
        assert entry["status"] == "success"
        assert entry["result"] == result

    def test_is_error_entry(self):
        assert is_error_entry({"status": "error"}) is True
        assert is_error_entry({"status": "success"}) is False
        assert is_error_entry({}) is False

    def test_is_success_entry(self):
        assert is_success_entry({"status": "success"}) is True
        assert is_success_entry({"status": "error"}) is False
