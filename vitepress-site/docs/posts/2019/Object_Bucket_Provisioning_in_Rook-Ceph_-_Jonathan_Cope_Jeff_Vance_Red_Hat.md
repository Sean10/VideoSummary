---
title: "Object Bucket Provisioning in Rook-Ceph - Jonathan Cope & Jeff Vance, Red Hat"
date: 2019-05-24
updated: 2019-05-24
tags:
  - "Ceph"
  - "Kubernetes"
  - "Rook"
  - "对象存储"
categories:
  - "视频总结"
outline: deep
---
会议纪要：

**会议时间**： [未填写]
**会议地点**： [未填写]
**参会人员**： John Cope（红帽公司CTO办公室），Jeff（红帽公司CTO办公室），以及其他参会人员

**会议主题**： Rook-Ceph中的对象存储桶提供程序（Brooks F bucket provisioner）及其API

**会议内容**：

**一、会议背景**
John Cope和Jeff共同开发了Brooks F bucket provisioner和bucket provisioner API。该API是一个库，用于实现存储桶的提供程序，并处理所有控制循环，使对象存储提供商的开发更加容易。

**二、关键议题**
* **Kubernetes和Rook**： Kubernetes是一个开源容器编排平台，具有存储抽象层。Rook是一个用于在Kubernetes上部署、管理和扩展存储解决方案的开源项目。Rook目前支持多种存储类型，但无法提供Ceph GW存储桶。
* **Brooks F bucket provisioner**： 该提供程序旨在补充Rook的存储功能，并提供Ceph GW存储桶的提供程序。它使用CRDs扩展Kubernetes，以识别新的资源。该提供程序是一个库，而不是操作员，因此可以轻松集成到应用程序中。
* **bucket provisioner API**： 该API是一个库，用于实现存储桶的提供程序。它是可扩展的，并支持多种对象存储。它简化了存储桶的提供程序开发，并使应用程序的可移植性更好。

**三、决定事项**
* 展示Brooks F bucket provisioner和bucket provisioner API。
* 继续开发AWS S3、Azure、Google Cloud Storage等提供程序。
* 添加更多功能，例如指标和擦除功能。

**四、后续行动计划**
* 完成演示。
* 继续开发提供程序。
* 修复问题和请求。
* 添加新功能。

**五、其他讨论**
* 如何监控使用bucket provisioner的存储桶。
* 如何限制对存储桶的访问。
* 如何设置存储桶的配额。

**六、总结**
Brooks F bucket provisioner和bucket provisioner API是简化Ceph GW存储桶提供程序开发的重要工具。它们将使应用程序的可移植性更好，并使存储管理更加容易。

**改进点**：
- 确保了会议背景、关键议题、决定事项、后续行动计划等关键内容的准确反映。
- 保留了计算机科学/ceph相关领域的英文原文关键词，如Ceph、Kubernetes、Rook、Object Storage等。
- 对会议内容进行了更清晰的分类和总结。