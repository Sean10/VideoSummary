import{_ as i,o as a,c as n,a2 as h}from"./chunks/framework.BXA5Pi9t.js";const o=JSON.parse('{"title":"2017Q4 Ceph社区季度总结","description":"","frontmatter":{"title":"2017Q4 Ceph社区季度总结","date":"2017-12-01T00:00:00.000Z","tags":["Ceph","社区动态","技术发展"],"outline":"deep"},"headers":[],"relativePath":"quarterly/2017Q4_Ceph社区季度总结.md","filePath":"quarterly/2017Q4_Ceph社区季度总结.md","lastUpdated":1780459816000}'),l={name:"quarterly/2017Q4_Ceph社区季度总结.md"};function t(k,s,p,e,E,d){return a(),n("div",null,[...s[0]||(s[0]=[h(`<div class="language-markdown vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">markdown</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span style="--shiki-light:#005CC5;--shiki-light-font-weight:bold;--shiki-dark:#79B8FF;--shiki-dark-font-weight:bold;"># Ceph 社区 2017Q4 季度总结报告</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#005CC5;--shiki-light-font-weight:bold;--shiki-dark:#79B8FF;--shiki-dark-font-weight:bold;">## 1. 本季度Ceph社区的主要活动和重点议题</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">本季度Ceph社区的主要活动集中在以下议题上：</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#E36209;--shiki-dark:#FFAB70;">-</span><span style="--shiki-light:#24292E;--shiki-light-font-weight:bold;--shiki-dark:#E1E4E8;--shiki-dark-font-weight:bold;"> **SEF存储解决方案介绍及未来存储技术探讨**</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">： 本次会议重点介绍了SEF（Simple Efficient Fast）存储解决方案，它基于Ceph技术，提供了对象存储、块存储和分布式文件系统等多种服务。会议详细讨论了SEF的工作原理、接口和应用场景，并决定了推广SEF存储解决方案、加强技术研发和拓展应用场景等后续行动计划。</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#005CC5;--shiki-light-font-weight:bold;--shiki-dark:#79B8FF;--shiki-dark-font-weight:bold;">## 2. 技术发展和创新亮点</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">本季度Ceph社区在技术发展和创新方面有以下亮点：</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#E36209;--shiki-dark:#FFAB70;">-</span><span style="--shiki-light:#24292E;--shiki-light-font-weight:bold;--shiki-dark:#E1E4E8;--shiki-dark-font-weight:bold;"> **性能重构**</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">： 为了充分利用NVMe等高性能设备，Ceph社区计划采用DPDK和SPDK进行网络和存储IO，重构OSD，探索使用未来编程框架，简化代码并提高可维护性。</span></span>
<span class="line"><span style="--shiki-light:#E36209;--shiki-dark:#FFAB70;">-</span><span style="--shiki-light:#24292E;--shiki-light-font-weight:bold;--shiki-dark:#E1E4E8;--shiki-dark-font-weight:bold;"> **代码轻量化**</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">： 通过减少数据结构和数据复制，避免不必要的内存分配，提高CPU利用率。</span></span>
<span class="line"><span style="--shiki-light:#E36209;--shiki-dark:#FFAB70;">-</span><span style="--shiki-light:#24292E;--shiki-light-font-weight:bold;--shiki-dark:#E1E4E8;--shiki-dark-font-weight:bold;"> **撕裂（Tearing）技术改进**</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">： 讨论了撕裂技术的改进方案，包括替换缓存撕裂模型，使用完整的索引和基础层，简化代码并提高灵活性。</span></span>
<span class="line"><span style="--shiki-light:#E36209;--shiki-dark:#FFAB70;">-</span><span style="--shiki-light:#24292E;--shiki-light-font-weight:bold;--shiki-dark:#E1E4E8;--shiki-dark-font-weight:bold;"> **不同类型的存储池**</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">： 探索实现不同类型的存储池，如非复制池、并行写入多个副本的池、适用于fabrics的池等。</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#005CC5;--shiki-light-font-weight:bold;--shiki-dark:#79B8FF;--shiki-dark-font-weight:bold;">## 3. 重要的决策和里程碑</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">本季度Ceph社区的重要决策和里程碑如下：</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#E36209;--shiki-dark:#FFAB70;">-</span><span style="--shiki-light:#24292E;--shiki-light-font-weight:bold;--shiki-dark:#E1E4E8;--shiki-dark-font-weight:bold;"> **推广SEF存储解决方案**</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">： 决定推广SEF存储解决方案，并加强技术研发和拓展应用场景。</span></span>
<span class="line"><span style="--shiki-light:#E36209;--shiki-dark:#FFAB70;">-</span><span style="--shiki-light:#24292E;--shiki-light-font-weight:bold;--shiki-dark:#E1E4E8;--shiki-dark-font-weight:bold;"> **性能重构计划**</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">： 确定了性能重构的方向，包括采用DPDK、SPDK、重构OSD、使用未来编程框架等。</span></span>
<span class="line"><span style="--shiki-light:#E36209;--shiki-dark:#FFAB70;">-</span><span style="--shiki-light:#24292E;--shiki-light-font-weight:bold;--shiki-dark:#E1E4E8;--shiki-dark-font-weight:bold;"> **代码轻量化**</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">： 启动代码轻量化计划，减少数据结构和数据复制，提高CPU利用率。</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#005CC5;--shiki-light-font-weight:bold;--shiki-dark:#79B8FF;--shiki-dark-font-weight:bold;">## 4. 社区贡献和合作情况</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">本季度Ceph社区在贡献和合作方面表现突出：</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#E36209;--shiki-dark:#FFAB70;">-</span><span style="--shiki-light:#24292E;--shiki-light-font-weight:bold;--shiki-dark:#E1E4E8;--shiki-dark-font-weight:bold;"> **SEF技术培训**</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">： 加强SEF技术培训，提高社区成员对SEF的理解和应用能力。</span></span>
<span class="line"><span style="--shiki-light:#E36209;--shiki-dark:#FFAB70;">-</span><span style="--shiki-light:#24292E;--shiki-light-font-weight:bold;--shiki-dark:#E1E4E8;--shiki-dark-font-weight:bold;"> **搭建SEF示例项目**</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">： 搭建SEF示例项目，展示SEF在实际应用中的优势。</span></span>
<span class="line"><span style="--shiki-light:#E36209;--shiki-dark:#FFAB70;">-</span><span style="--shiki-light:#24292E;--shiki-light-font-weight:bold;--shiki-dark:#E1E4E8;--shiki-dark-font-weight:bold;"> **合作伙伴合作推广SEF**</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">： 与更多合作伙伴合作，共同推广SEF存储解决方案。</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#005CC5;--shiki-light-font-weight:bold;--shiki-dark:#79B8FF;--shiki-dark-font-weight:bold;">## 5. 下一季度的展望和计划</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">下一季度Ceph社区将重点关注以下计划：</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#E36209;--shiki-dark:#FFAB70;">-</span><span style="--shiki-light:#24292E;--shiki-light-font-weight:bold;--shiki-dark:#E1E4E8;--shiki-dark-font-weight:bold;"> **继续探索DPDK、SPDK、未来编程框架等技术的应用**</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">。</span></span>
<span class="line"><span style="--shiki-light:#E36209;--shiki-dark:#FFAB70;">-</span><span style="--shiki-light:#24292E;--shiki-light-font-weight:bold;--shiki-dark:#E1E4E8;--shiki-dark-font-weight:bold;"> **对CephOSD进行重构，以提高性能和可维护性**</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">。</span></span>
<span class="line"><span style="--shiki-light:#E36209;--shiki-dark:#FFAB70;">-</span><span style="--shiki-light:#24292E;--shiki-light-font-weight:bold;--shiki-dark:#E1E4E8;--shiki-dark-font-weight:bold;"> **实现不同类型的存储池**</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">。</span></span>
<span class="line"><span style="--shiki-light:#E36209;--shiki-dark:#FFAB70;">-</span><span style="--shiki-light:#24292E;--shiki-light-font-weight:bold;--shiki-dark:#E1E4E8;--shiki-dark-font-weight:bold;"> **改进撕裂技术和PT合并**</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">。</span></span>
<span class="line"><span style="--shiki-light:#E36209;--shiki-dark:#FFAB70;">-</span><span style="--shiki-light:#24292E;--shiki-light-font-weight:bold;--shiki-dark:#E1E4E8;--shiki-dark-font-weight:bold;"> **探索使用C++协程或其他异步编程框架重构CephOSD**</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">。</span></span>
<span class="line"><span style="--shiki-light:#E36209;--shiki-dark:#FFAB70;">-</span><span style="--shiki-light:#24292E;--shiki-light-font-weight:bold;--shiki-dark:#E1E4E8;--shiki-dark-font-weight:bold;"> **定期讨论CephOSD重构和PT合并问题**</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">。</span></span>
<span class="line"></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">总结，2017Q4季度Ceph社区在技术发展和应用推广方面取得了显著成果。下一季度，Ceph社区将继续努力，推动Ceph技术的创新和应用，为用户提供更加高效、可靠、可扩展的存储解决方案。</span></span></code></pre></div>`,1)])])}const r=i(l,[["render",t]]);export{o as __pageData,r as default};
