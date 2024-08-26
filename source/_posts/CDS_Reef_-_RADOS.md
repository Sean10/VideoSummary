---
title: "CDS Reef: RADOS"
date: 2022-04-22
updated: 2022-04-23
tags:
categories:
- "视频总结"
subtitle: tech
---


1. **Configuration Profiles**: PR link provided for implementation of configuration profiles on a pool level, aimed at reef but backportable to quincy.
2. **Automatic Key Rotation**: Outstanding PR exists, with work done for quincy enabling backporting, close to completion for reef.
3. **Balancer Improvements**: Work on the workload or primary balancer focusing on balancing read requests based on pool workloads, with refactored capacity balancer code for clarity and future maintainability.
4. **Autoscaler Checks and Balances**: Addition of "dash bulk" flag in quincy to manage pgs effectively, and "no auto scale global" flag to turn off the autoscaler globally. Addressing recent issues where autoscaler actions impact cluster performance.
5. **OSD Map Trimming**: Case identified where millions of OSD maps remain untrimmed due to a trigger in map generation. To be discussed further post understanding the issue.
6. **Partial Stripe Breeds**: Implementation of partial stripes to efficiently read subsets of data without accessing every OSD, beneficial for CPU load reduction especially for small reads in large objects.
7. **Testing Improvements and Board Cleanup**: Discussing testing coverage improvement, particularly for stretch mode, netsplit subsuite, and logical skill testing at larger scales. Also, addressing upgrade test coverage, tracking test improvements, reducing raiders suite run time, and cleanup/deprecation tasks including legacy watches and mdr module usage.