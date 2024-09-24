import json
import os
import asyncio
from asyncio import Semaphore
from .utils import call_openai_api

async def generate_quarterly_summary(quarter, post_titles, semaphore):
    async with semaphore:
        summaries = []
        for post_title in post_titles:
            with open(os.path.join("source/_posts", post_title), 'r', encoding='utf-8') as f:
                summaries.append(f.read())
        
        combined_summary = "\n\n".join(summaries)
        
        prompt = f"""作为专业的存储领域分布式存储Ceph的研发人员，请对以下{quarter}季度的会议总结进行综合分析，生成一份季度总结报告。
        
        请包含以下内容：
        1. 本季度Ceph社区的主要活动和重点议题
        2. 技术发展和创新亮点
        3. 重要的决策和里程碑
        4. 社区贡献和合作情况
        5. 下一季度的展望和计划

        以下是本季度的会议总结：

        {combined_summary[:4000]}  # 限制字数以避免超过token限制

        请以Markdown格式输出季度总结报告，包含适当的标题和分段。
        """

        messages = [
            {"role": "system", "content": "You are a helpful assistant that generates quarterly summary reports for Ceph community."},
            {"role": "user", "content": prompt}
        ]

        try:
            completion = await call_openai_api(
                client.chat.completions.create,
                model="THUDM/glm-4-9b-chat",
                messages=messages,
                temperature=0.7,
                max_tokens=4096
            )
            return completion.choices[0].message.content
        except Exception as e:
            print(f"生成季度总结报告时出错: {e}")
            return None

async def process_quarterly_summaries():
    with open("post_classification_by_quarter.json", "r", encoding="utf-8") as f:
        quarterly_reports = json.load(f)
    
    semaphore = Semaphore(15)  # 限制并发请求数
    
    for quarter, post_titles in quarterly_reports.items():
        summary = await generate_quarterly_summary(quarter, post_titles, semaphore)
        if summary:
            output_file = f"source/_posts/{quarter}_Ceph社区季度总结.md"
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(f"""---
title: "{quarter} Ceph社区季度总结"
date: {quarter[:4]}-{int(quarter[5])*3}-01
updated: {quarter[:4]}-{int(quarter[5])*3}-01
categories:
- "季度总结"
tags:
- Ceph
- 社区动态
- 技术发展
subtitle: quarterly-summary
---

{summary}
""")
            print(f"已生成季度总结报告: {output_file}")