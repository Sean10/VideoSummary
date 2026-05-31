#!/bin/bash

# Ceph YouTube 视频总结工具 - 快速启动脚本

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

print_header() { echo -e "${BLUE}========================================${NC}\n${BLUE}$1${NC}\n${BLUE}========================================${NC}"; }
print_success() { echo -e "${GREEN}✓ $1${NC}"; }
print_warning() { echo -e "${YELLOW}⚠ $1${NC}"; }
print_error()   { echo -e "${RED}✗ $1${NC}"; }

print_header "Ceph YouTube 视频总结工具"

# 检查依赖
if ! command -v python3 &>/dev/null; then print_error "Python 3 未安装"; exit 1; fi
print_success "Python $(python3 --version | cut -d' ' -f2)"

if ! command -v claude &>/dev/null; then
    print_error "Claude Code CLI 未安装，请运行: npm install -g @anthropic-ai/claude-code"
    exit 1
fi
print_success "Claude Code CLI 已安装"

if ! command -v yt-dlp &>/dev/null; then
    print_warning "yt-dlp 未安装，正在安装..."
    pip install yt-dlp
fi
print_success "yt-dlp 已安装"

if ! python3 -c "import yaml" 2>/dev/null; then
    print_warning "缺失 Python 依赖，正在安装..."
    pip install -r requirements.txt
fi
print_success "Python 依赖已准备就绪"

# 工作流选项
print_header "选择工作流"
echo "1. 完整流程: 下载 → 处理 → 季度/年度总结 → 发布 (推荐)"
echo "2. 仅下载字幕"
echo "3. 仅处理字幕 (字幕 → hexo 文章)"
echo "4. 更新季度/年度总结 (自动检测过期)"
echo "5. 查看所有命令"
echo ""
read -p "请选择 [1-5]: " choice

BACKEND="${BACKEND:-claude}"
WORKERS="${WORKERS:-4}"

case $choice in
    1)
        print_header "完整流程"
        pip install --upgrade yt-dlp -q

        print_header "步骤 1: 下载新增字幕"
        python3 run.py --fetch-diff

        print_header "步骤 2: 处理字幕 → hexo 文章"
        python3 run.py --claude-process --backend "$BACKEND" -v

        print_header "步骤 3: 同步文章"
        rsync -av temp_posts/* ../source/_posts/

        print_header "步骤 4: 更新季度/年度总结"
        python3 run.py --claude-quarterly --backend "$BACKEND" --summary-workers "$WORKERS" --timeout 600 -v
        python3 run.py --claude-yearly    --backend "$BACKEND" --summary-workers "$WORKERS" --timeout 900 -v

        print_header "步骤 5: 生成并发布"
        cd ..
        node --max-old-space-size=8192 node_modules/hexo-cli/bin/hexo gen -c 100 -d
        print_success "完整流程完成！"
        ;;
    2)
        print_header "下载新增字幕"
        pip install --upgrade yt-dlp -q
        python3 run.py --fetch-diff
        print_success "字幕下载完成"
        ;;
    3)
        print_header "处理字幕 → hexo 文章"
        python3 run.py --claude-process --backend "$BACKEND" -v
        rsync -av temp_posts/* ../source/_posts/
        print_success "处理完成，文章已同步到 source/_posts/"
        ;;
    4)
        print_header "更新季度/年度总结（自动检测过期）"
        python3 run.py --claude-quarterly --backend "$BACKEND" --summary-workers "$WORKERS" --timeout 600 -v
        python3 run.py --claude-yearly    --backend "$BACKEND" --summary-workers "$WORKERS" --timeout 900 -v
        print_success "总结更新完成"
        ;;
    5)
        python3 run.py --help
        ;;
    *)
        print_error "无效选择"
        exit 1
        ;;
esac
