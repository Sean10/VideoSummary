/**
 * Sidebar: each year path shows its own articles expanded,
 * other years collapsed to just the year label.
 */
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const __dirname = path.dirname(fileURLToPath(import.meta.url))
const docsDir = path.resolve(__dirname, '..')

function extractTitle(content, filename) {
  const fmMatch = content.match(/^---\n([\s\S]*?)\n---/)
  if (fmMatch) {
    const titleMatch = fmMatch[1].match(/^title:\s*["']?(.+?)["']?\s*$/m)
    if (titleMatch) {
      let title = titleMatch[1].trim()
      if ((title.startsWith('"') && title.endsWith('"')) ||
          (title.startsWith("'") && title.endsWith("'"))) {
        title = title.slice(1, -1)
      }
      return title
    }
  }
  return filename.replace('.md', '').replace(/_/g, ' ').replace(/-/g, ' ')
}

function extractDate(content, filename) {
  const fmMatch = content.match(/^---\n([\s\S]*?)\n---/)
  if (fmMatch) {
    const dateMatch = fmMatch[1].match(/^date:\s*(.+?)\s*$/m)
    if (dateMatch) return dateMatch[1].trim()
  }
  const dateFromName = filename.match(/(\d{4}-\d{2}-\d{2})/)
  return dateFromName ? dateFromName[1] : null
}

function getArticleItems(dirPath, linkPrefix) {
  if (!fs.existsSync(dirPath)) return []
  const files = fs.readdirSync(dirPath).filter(f => f.endsWith('.md') && f !== 'index.md')
  const items = files.map(f => {
    const content = fs.readFileSync(path.join(dirPath, f), 'utf-8')
    return {
      text: extractTitle(content, f),
      link: `${linkPrefix}${f}`,
      _date: extractDate(content, f),
    }
  })
  // Sort by date descending
  items.sort((a, b) => {
    if (!a._date && !b._date) return 0
    if (!a._date) return 1
    if (!b._date) return -1
    return b._date.localeCompare(a._date)
  })
  return items.map(({ _date, ...rest }) => rest)
}

export function getSidebar() {
  const sidebar = {}
  const postsDir = path.join(docsDir, 'posts')
  if (!fs.existsSync(postsDir)) return sidebar

  const years = fs.readdirSync(postsDir)
    .filter(d => fs.statSync(path.join(postsDir, d)).isDirectory())
    .sort((a, b) => b.localeCompare(a))

  // For each year, build a path-specific sidebar:
  //   - Current year: EXPANDED with all article items
  //   - Other years: COLLAPSED stubs (just year label + link)
  for (const activeYear of years) {
    const yearGroups = years.map(year => {
      if (year === activeYear) {
        // Expand this year — list all articles
        const items = getArticleItems(path.join(postsDir, year), `/posts/${year}/`)
        return {
          text: `${year} 年 (${items.length} 篇)`,
          collapsed: false,
          items,
        }
      } else {
        // Collapse other years — just a link, no children
        return {
          text: `${year} 年`,
          link: `/posts/${year}/`,
          collapsed: true,
          items: [],
        }
      }
    })

    sidebar[`/posts/${activeYear}/`] = [
      {
        text: '按年份浏览',
        collapsed: false,
        items: yearGroups,
      }
    ]
  }

  // === Quarterly reports sidebar ===
  const quarterlyDir = path.join(docsDir, 'quarterly')
  if (fs.existsSync(quarterlyDir)) {
    const items = getArticleItems(quarterlyDir, '/quarterly/')
    items.sort((a, b) => b.text.localeCompare(a.text))

    sidebar['/quarterly/'] = [
      {
        text: `季度报告 (${items.length} 篇)`,
        collapsed: false,
        items,
      }
    ]
  }

  // === Home page sidebar ===
  sidebar['/'] = [
    {
      text: '快速导航',
      collapsed: false,
      items: [
        { text: '季度报告汇总', link: '/quarterly/' },
      ]
    }
  ]

  return sidebar
}
