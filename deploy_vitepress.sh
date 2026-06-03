#!/bin/bash
# VitePress 构建 + 部署脚本
# 接在 youtube_subtitle_summary 的内容生成流程之后运行
#
# 用法:
#   1) 单独运行 (已有新文章在 source/_posts/):  ./deploy_vitepress.sh
#   2) 完整流程 (拉取+生成+部署):                ./update_vitepress.sh
#   3) 仅构建不部署:                             ./deploy_vitepress.sh --no-deploy

set -e

# 加载 nvm (确保 npm/node 可用)
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
VITEPRESS_DIR="$PROJECT_DIR/vitepress-site"
DOCS_DIR="$VITEPRESS_DIR/docs"

SKIP_DEPLOY=false
if [[ "$1" == "--no-deploy" ]]; then
    SKIP_DEPLOY=true
fi

echo "=== VitePress 部署流程 ==="
echo "项目目录: $PROJECT_DIR"
echo ""

# 1. 同步新文章到 VitePress 目录
echo "--- [1/4] 同步文章到 VitePress ---"
python3 "$VITEPRESS_DIR/migrate.py"

# 2. 修复内部链接 (年度/季度总结中的旧 Hexo 链接)
echo "--- [2/4] 修复内部链接 ---"
python3 "$VITEPRESS_DIR/fix_links.py"

# 3. 修正日期 (混合策略: 标题日期优先, YouTube 上传日期兜底)
echo "--- [3/4] 修正文章日期 ---"
python3 "$VITEPRESS_DIR/fix_dates_hybrid.py"

# 4. 构建
echo "--- [4/4] 构建 VitePress ---"
cd "$VITEPRESS_DIR"
npm run build

DIST_DIR="$DOCS_DIR/.vitepress/dist"
DIST_SIZE=$(du -sh "$DIST_DIR" | cut -f1)
echo ""
echo "=== 构建完成 ==="
echo "输出目录: $DIST_DIR"
echo "体积: $DIST_SIZE"
echo ""

# 5. 部署到 gh-pages
if [[ "$SKIP_DEPLOY" == "true" ]]; then
    echo "跳过部署 (--no-deploy)"
    exit 0
fi

echo "--- 部署到 gh-pages ---"

# 创建临时目录, 拷贝 dist 内容
TMPDIR=$(mktemp -d)
cp -r "$DIST_DIR"/* "$TMPDIR"/

# 初始化 git 并推送
cd "$TMPDIR"
git init
git add -A
git commit -m "VitePress deploy $(date +%Y-%m-%d\ %H:%M:%S)"
git push -f git@github.com:Sean10/VideoSummary.git master:gh-pages

# 清理
cd "$PROJECT_DIR"
rm -rf "$TMPDIR"

echo ""
echo "=== 部署完成 ==="
echo "站点地址: https://sean10.github.io/VideoSummary/"
