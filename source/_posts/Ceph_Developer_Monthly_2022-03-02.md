---
title: "Ceph Developer Monthly 2022-03-02"
date: 2022-06-03
updated: 2022-06-03
tags:
categories:
- "视频总结"
subtitle: tech
---


1. **Centralized Logging Solutions**:
   - **Graylog**: Has to be configured manually, lacks dynamic log collection.
   - **Elasticsearch and Logstash**: Offer customization and better visualization, but require running beats daemon on every node.
   - **Loki**: Simpler integration with native grafana interface.

2. **Traceability and Observability**:
   - Trace points can help in reducing the overhead of processing logs.
   - Tracing gives the possibility of focusing on specific flows and turning on traces under certain conditions.

3. **Dynamic Filtering and Conditional Tracing**:
   - The idea of conditional tracing based on observed conditions to reduce the volume of logs.
   - Dynamic filtering capabilities like those seen in dtrace for efficient log management and debugging.

4. **Future Work**:
   - Explore integrating dynamic code or scripting into logging and tracing to allow for flexible condition injection.
   - Consider the feasibility and safety of such dynamic capabilities in a C++ environment.

5. **Community Feedback**:
   - Send out emails to both dev list and user list to gather more feedback on centralized logging solutions.
   - Understand different use cases and roles these solutions can serve.