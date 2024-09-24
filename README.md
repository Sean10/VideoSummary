# 基于youtube的ceph会议录屏使用GPT进行总结


* [x] 使用youtube-dl下载视频
* [x] 使用GPT总结
* [x] 支持对总结配合字幕进行二次反思, 并输出tag
* [ ] 采集etherpad内容, 辅助总结
    * 已采集
    * 如何让他搜索本地相关文件, 自动化串联.
        * 预计需要个本地索引及向量化搜索能力. 类似continue/cursor的index能力.
        * 原型已完毕
   * 将对应pull request信息采集
      * 原型已有
* [x] 使用GPT分类, 按季度总结

## 使用

[ceph视频总结 \| youtube频道总结](https://sean10.github.io/VideoSummary/)


# 生成过程

# TODO
* 考虑到QoS, 增加token计算
* 或引入langchain重新实现, 以支持引入jina.ai等联动etherpad等
* 使用AI归类, 并打tag, 提供阶段性汇总的总结. 年报或者季度总结都行. 考虑先季度或年度的来(max_tokens限制)

# Features
* 实现检测哪些已下载过, 下次仅下载新出现的视频
* 实现将总结发给gpt, 使其进行分类, 或根据季度进行汇总, 提供汇总的总结.
* 将该工具导出的文档发布到github pages, 以便于查看.

# 使用步骤

```
cd youtube_subtitle_summary
```
1. **下载字幕**
   使用以下命令从指定的 YouTube 频道下载字幕：
   ```bash
   python main.py --fetch
   ```

2. **下载新增字幕**
   使用以下命令下载新增的字幕：
   ```bash
   python main.py --fetch-diff
   ```

3. **处理字幕**
   下载完成后，使用以下命令处理字幕并生成总结：
   ```bash
   python main.py --summarize
   ```

4. **处理新增字幕**
   使用以下命令处理新增的字幕并生成总结：
   ```bash
   python main.py --summarize-diff
   ```

5. **翻译字幕（可选）**
   如果需要翻译某个特定的字幕文件，可以使用以下命令：
   ```bash
   python main.py --translate subtitle_file.en.ttml
   ```

6. **按内容分类文章**
   使用以下命令对文章进行内容分类：
   ```bash
   python main.py --classify-content
   ```

7. **按季度分类文章**
   使用以下命令对文章进行季度分类：
   ```bash
   python main.py --classify-quarter
   ```

8. **添加 Hexo 元数据**
   处理完字幕后，使用以下命令将生成的总结文件添加 Hexo 博客所需的标题元数据：
   ```bash
   python main.py --add-metadata
   ```

9. **反思和改进总结**
   使用以下命令对现有的总结进行反思和改进：
   ```bash
   python main.py --reflect
   ```

10. **生成季度总结报告**
    使用以下命令生成季度总结报告：
    ```bash
    python main.py --quarterly-summary
    ```

11. **部署 Hexo 博客**
    最后，使用以下命令触发 Hexo 部署：
    ```bash
    hexo deploy
    ```

# 常用命令

```
# 清理指定目录下带空格的旧文件
find ./ -type f -name "* *" -exec rm -f "{}" +
```


# 实验命令


```
yt-dlp --write-auto-subs    'https://www.youtube.com/watch?v=bByZZk3DiXU&t=1276s' --skip-download

yt-dlp --print "%(release_date)s;%(id)s;%(title)s;%(webpage_url)s"  https://www.youtube.com/@Cephstorage/videos   > results.txt

yt-dlp --skip-download --write-subs --write-auto-subs  --sub-lang en --sub-format ttml --convert-subs srt --exec before_dl:"sed -e '/^[0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9] --> [0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9]$/d' -e '/^[[:digit:]]\{1,5\}$/d' -e 's/<[^>]*>//g' -e '/^[[:space:]]*$/d' -i '' %(requested_subtitles.:.filepath)#q" 'https://www.youtube.com/watch?v=bByZZk3DiXU&t=1276s'
```

[How to download only subtitles of videos using youtube\-dl \- Super User](https://superuser.com/questions/927523/how-to-download-only-subtitles-of-videos-using-youtube-dl)