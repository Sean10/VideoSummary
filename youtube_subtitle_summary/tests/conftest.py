"""
Test configuration - add the parent package to sys.path so we can import
submodules directly without triggering __init__.py's full eager imports.
"""
import sys
from pathlib import Path

# Allow direct submodule imports (e.g. libylt2summary.jsonl_handler)
# without loading the entire package which pulls in heavy deps like yt_dlp
pkg_dir = str(Path(__file__).resolve().parent.parent)
if pkg_dir not in sys.path:
    sys.path.insert(0, pkg_dir)
