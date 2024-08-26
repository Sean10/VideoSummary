

# TODO
* 实现检测哪些已下载过, 下次仅下载新出现的视频
* 实现将总结发给gpt, 使其进行分类, 或根据季度进行汇总, 提供汇总的总结.
* 将该工具导出的文档发布到github pages, 以便于查看.


# 实验命令


```
yt-dlp --write-auto-subs    'https://www.youtube.com/watch?v=bByZZk3DiXU&t=1276s' --skip-download

yt-dlp --print "%(release_date)s;%(id)s;%(title)s;%(webpage_url)s"  https://www.youtube.com/@Cephstorage/videos   > results.txt

yt-dlp --skip-download --write-subs --write-auto-subs  --sub-lang en --sub-format ttml --convert-subs srt --exec before_dl:"sed -e '/^[0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9] --> [0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9]$/d' -e '/^[[:digit:]]\{1,5\}$/d' -e 's/<[^>]*>//g' -e '/^[[:space:]]*$/d' -i '' %(requested_subtitles.:.filepath)#q" 'https://www.youtube.com/watch?v=bByZZk3DiXU&t=1276s'
```

[How to download only subtitles of videos using youtube\-dl \- Super User](https://superuser.com/questions/927523/how-to-download-only-subtitles-of-videos-using-youtube-dl)