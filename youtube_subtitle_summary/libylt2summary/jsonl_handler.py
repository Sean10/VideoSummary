"""
JSONL Handler Module
Provides utilities for reading, writing, and processing JSONL files
"""
import json
import logging
from typing import List, Dict, Any, Iterator, Optional
from pathlib import Path

logger = logging.getLogger(__name__)


def jsonl_reader(file_path: str, encoding: str = 'utf-8') -> List[Dict[str, Any]]:
    """
    Read a JSONL file and return a list of dictionaries.

    Args:
        file_path: Path to the JSONL file
        encoding: File encoding (default: utf-8)

    Returns:
        List of dictionaries, one per line

    Raises:
        FileNotFoundError: If file doesn't exist
    """
    results = []
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(path, 'r', encoding=encoding) as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:  # Skip empty lines
                continue
            try:
                results.append(json.loads(line))
            except json.JSONDecodeError as e:
                logger.warning(f"Skipping malformed JSON at line {line_num}: {e}")
                continue

    return results


def jsonl_reader_iter(file_path: str, encoding: str = 'utf-8') -> Iterator[Dict[str, Any]]:
    """
    Iterate over JSONL file line by line (memory efficient for large files).

    Args:
        file_path: Path to the JSONL file
        encoding: File encoding (default: utf-8)

    Yields:
        Dictionary for each valid JSON line
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(path, 'r', encoding=encoding) as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError as e:
                logger.warning(f"Skipping malformed JSON at line {line_num}: {e}")
                continue


def jsonl_writer(
    file_path: str,
    data: List[Dict[str, Any]],
    encoding: str = 'utf-8',
    append: bool = False
) -> int:
    """
    Write a list of dictionaries to a JSONL file.

    Args:
        file_path: Path to the output JSONL file
        data: List of dictionaries to write
        encoding: File encoding (default: utf-8)
        append: If True, append to existing file (default: False)

    Returns:
        Number of records written
    """
    mode = 'a' if append else 'w'
    count = 0

    with open(file_path, mode, encoding=encoding) as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')
            count += 1

    logger.info(f"Wrote {count} records to {file_path}")
    return count


def jsonl_append(file_path: str, item: Dict[str, Any], encoding: str = 'utf-8') -> None:
    """
    Append a single record to a JSONL file.

    Args:
        file_path: Path to the JSONL file
        item: Dictionary to append
        encoding: File encoding (default: utf-8)
    """
    with open(file_path, 'a', encoding=encoding) as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')


def split_batches(
    data: List[Dict[str, Any]],
    batch_size: int = 100
) -> List[List[Dict[str, Any]]]:
    """
    Split a list of items into batches.

    Args:
        data: List of items to split
        batch_size: Number of items per batch

    Returns:
        List of batches
    """
    batches = []
    for i in range(0, len(data), batch_size):
        batch = data[i:i + batch_size]
        batches.append(batch)

    logger.info(f"Split {len(data)} items into {len(batches)} batches of size {batch_size}")
    return batches


def create_batches_with_metadata(
    data: List[Dict[str, Any]],
    batch_size: int = 100
) -> List[Dict[str, Any]]:
    """
    Create batches with metadata (batch_id, total_batches, batch_size).

    Args:
        data: List of items to batch
        batch_size: Number of items per batch

    Returns:
        List of batch dictionaries with metadata
    """
    batches = []
    total_batches = (len(data) + batch_size - 1) // batch_size

    for i in range(0, len(data), batch_size):
        batch_data = data[i:i + batch_size]
        batch_id = i // batch_size

        batches.append({
            'batch_id': batch_id,
            'total_batches': total_batches,
            'batch_size': len(batch_data),
            'data': batch_data
        })

    return batches


def create_error_entry(entry_id: str, error_message: str) -> Dict[str, Any]:
    """
    Create a standardized error entry for JSONL output.

    Args:
        entry_id: Identifier for the failed entry
        error_message: Description of the error

    Returns:
        Error entry dictionary
    """
    return {
        'id': entry_id,
        'status': 'error',
        'error': error_message
    }


def create_success_entry(entry_id: str, result: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create a standardized success entry for JSONL output.

    Args:
        entry_id: Identifier for the entry
        result: The result data

    Returns:
        Success entry dictionary
    """
    return {
        'id': entry_id,
        'status': 'success',
        'result': result
    }


def is_error_entry(entry: Dict[str, Any]) -> bool:
    """
    Check if a JSONL entry represents an error.

    Args:
        entry: Dictionary to check

    Returns:
        True if entry has status: error
    """
    return entry.get('status') == 'error'


def is_success_entry(entry: Dict[str, Any]) -> bool:
    """
    Check if a JSONL entry represents a success.

    Args:
        entry: Dictionary to check

    Returns:
        True if entry has status: success
    """
    return entry.get('status') == 'success'
