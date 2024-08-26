---
title: "CephFS Code Walkthrough: Kernel Client Overview"
date: 2022-05-24
updated: 2022-05-25
tags:
categories:
- "视频总结"
subtitle: tech
---


The question was about the comment in the function `self atomic open` which said "if the file or sim link is non-existent, the vfs3 tries". The questioner wanted to know if VFS keeps retrying and what's the idea behind that.

Answer: The comment appears to be outdated and may not be correct. When a file is non-existent, VFS doesn't really retry; it just returns at that point. The calling convention for atomic open has changed, and this comment is likely no longer accurate. If an atomic open is called under very specific circumstances (like not having a cached entry for something or having a negative entry), it allows instantiating an entry if needed. It also handles situations where there might have been changes on the MDS that the client wasn't aware of. In such cases, if it turns out the file does exist and no create operation is being performed, an open call will be issued to the NBS, and the entry can be instantiated accordingly.