cd /Users/sean10/Code/VideoSummary/youtube_subtitle_summary
source init/bin/activate
source env.sh
pip3 install --upgrade yt-dlp
python run.py --fetch
python run.py --fetch-diff
python run.py --summarize
python run.py --reflect
rsync -av temp_posts/* ../source/_posts
cd ..
node --max-old-space-size=8192 node_modules/hexo-cli/bin/hexo gen -c 100  -d