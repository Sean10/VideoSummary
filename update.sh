cd /Users/sean10/Self_Code/VideoSummary/youtube_subtitle_summary
source venv/bin/activate
source env.sh
pip3 install --upgrade yt-dlp
python run.py --fetch
python run.py --fetch-diff
python run.py --claude-process --backend claude -v
rsync -av temp_posts/* ../source/_posts
cd ..
node --max-old-space-size=8192 node_modules/hexo-cli/bin/hexo gen -c 100  -d