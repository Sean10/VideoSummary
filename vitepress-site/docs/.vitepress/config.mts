import { defineConfig } from 'vitepress'
import { getSidebar } from './sidebar.mjs'

export default defineConfig({
  title: 'Ceph 视频总结',
  description: 'Ceph YouTube 频道视频总结知识库',
  lang: 'zh-CN',
  base: '/VideoSummary/',

  lastUpdated: true,
  ignoreDeadLinks: true,

  head: [
    ['meta', { name: 'theme-color', content: '#3F51B5' }],
  ],

  themeConfig: {
    // Material Indigo color scheme
    siteTitle: 'Ceph 视频总结',

    nav: [
      { text: '首页', link: '/' },
      {
        text: '按年份浏览',
        items: [
          { text: '2026', link: '/posts/2026/' },
          { text: '2025', link: '/posts/2025/' },
          { text: '2024', link: '/posts/2024/' },
          { text: '2023', link: '/posts/2023/' },
          { text: '2022', link: '/posts/2022/' },
          { text: '2021', link: '/posts/2021/' },
          { text: '2020', link: '/posts/2020/' },
          { text: '2019', link: '/posts/2019/' },
          { text: '2018', link: '/posts/2018/' },
          { text: '2017', link: '/posts/2017/' },
          { text: '2016', link: '/posts/2016/' },
          { text: '2015', link: '/posts/2015/' },
          { text: '2014', link: '/posts/2014/' },
        ]
      },
      { text: '季度报告', link: '/quarterly/' },
      { text: '按标签', link: '/tags/' },
    ],

    sidebar: getSidebar(),

    search: {
      provider: 'local',
      options: {
        detailedView: true,
      }
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/Sean10/VideoSummary' }
    ],

    editLink: {
      pattern: 'https://github.com/Sean10/VideoSummary/edit/master/source/_posts/:path',
      text: '在 GitHub 上编辑此页'
    },

    footer: {
      message: 'Ceph YouTube 频道视频总结知识库',
      copyright: `© 2014-${new Date().getFullYear()} sean10`
    },

    docFooter: {
      prev: '上一篇',
      next: '下一篇'
    },

    lastUpdated: {
      text: '最后更新于',
      formatOptions: {
        dateStyle: 'full',
        timeStyle: 'short'
      }
    },

    outline: {
      label: '页面导航'
    },

    returnToTopLabel: '回到顶部',
    sidebarMenuLabel: '菜单',
    darkModeSwitchLabel: '主题',
    lightModeSwitchTitle: '切换到浅色模式',
    darkModeSwitchTitle: '切换到深色模式',
  },

  vite: {
    ssr: {
      noExternal: [],
    },
  },
})
