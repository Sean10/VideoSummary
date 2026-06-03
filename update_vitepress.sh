#!/bin/bash
# 完整工作流: 拉取视频 → 生成总结 → VitePress 构建 → 部署 gh-pages
# 替代原来的 update.sh (Hexo → VitePress)

set -e

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "========================================="
echo "  Ceph 视频总结 - 完整更新流程 (VitePress)"
echo "========================================="
echo ""

# === 阶段 1: 内容生成 (沿用原有 youtube_subtitle_summary 流程) ===
echo "=== 阶段 1: 内容生成 ==="
cd "$PROJECT_DIR/youtube_subtitle_summary"
source venv/bin/activate
source env.sh
pip3 install --upgrade yt-dlp

echo "--- 拉取新视频数据 ---"
python run.py --fetch
python run.py --fetch-diff

echo "--- Claude 处理生成总结 ---"
python run.py --claude-process --backend claude -v
rsync -av temp_posts/* ../source/_posts/

echo "--- 更新季度/年度总结 ---"
python run.py --claude-quarterly --backend claude --summary-workers 4 --timeout 600 -v
python run.py --claude-yearly --backend claude --summary-workers 4 --timeout 900 -v

deactivate
cd "$PROJECT_DIR"

# === 阶段 2: VitePress 构建 + 部署 ===
echo ""
echo "=== 阶段 2: VitePress 构建 + 部署 ==="
bash "$PROJECT_DIR/deploy_vitepress.sh"
