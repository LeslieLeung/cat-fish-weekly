---
intro: 这是猫鱼周刊的第17期，分享了一篇关于硬件入门的文章以及两个有趣的 Docker项目，讲重构的网站，还有一些 PVE 的脚本。最后分享了这周折腾的部分成果。
issue: 17
date: 2024-03-10
---

## 关于本刊

> 这是猫鱼周刊的第 17 期，本系列每周日更新，主要内容为每周收集内容的分享，同时发布在
>
> 博客：[阿猫的博客-猫鱼周刊](https://ameow.xyz/categories/weekly)
>
> RSS：[猫鱼周刊](https://ameow.xyz/feed/categories/weekly.xml)
>
> 邮件订阅：[猫鱼周刊](https://quaily.com/ameow)
>
> 微信公众号：[猫兄的和谐号列车](http://img.ameow.xyz/202401141448662.png)
>
> Discord：[猫兄的和谐号高铁](https://discord.gg/5G5Nbtuz)
>
> 私信：[leslieleung@pm.me](mailto:leslieleung@pm.me)

## 文章

### 如何入门硬件开发？一个软件开发者的边学边做手记

[原文链接](https://sspai.com/post/85507)

从软件开发者角度的硬件入门，讲得比较全，如果对硬件感兴趣可以一看。

不过以我之前学习硬件开发（结果是没学成）的时候的感觉，最大的阻碍还是一些基础原理部分，我在学校里模拟电路和电子电路总共就开了一学期的课，没怎么覆盖硬件部分的内容，课程其实也没学好。这篇文章可以作为一个大概的路线图，但是具体路线还是要自己去补充和摸索。

## 项目

### dockur/windows

[![dockur/windows - GitHub](https://gh-card.dev/repos/dockur/windows.svg?fullname=)](https://github.com/dockur/windows)

在 Docker 里跑的 Windows。

### sickcodes/Docker-OSX

[![sickcodes/Docker-OSX - GitHub](https://gh-card.dev/repos/sickcodes/Docker-OSX.svg?fullname=)](https://github.com/sickcodes/Docker-OSX)

在 Docker 里跑的 macOS。

笑死，在 GitHub trending 上看到这个 Windows 的项目就想起他的孪生兄弟——在 Docker 里跑的 macOS。真是万物归于 Docker！

话说回来，费心思和冒版权风险把这些专有系统搞进 Docker 有什么意义呢？我觉得潜在的用途可能是 CI/CD 和 安全研究，例如需要一个能快速拉起的干净环境、能够同时地的测试多个版本的系统、又或者是运行一些平台的专有工具（macOS 上的 Xcode）。而 Docker 比虚拟机更轻量，更方便部署，

## 工具/网站

### refactoring.guru

[网站地址](https://refactoring.guru)

![](https://img.ameow.xyz/202403101720448.png)

一个介绍重构和设计模式的网站，配有漫画，会用伪代码来讲解，也有针对主流语言给出的范例。可以无聊翻着看，也可以需要的时候拿起来速查。

### Proxmox VE Helper-Scripts

[网站地址](https://tteck.github.io/Proxmox/)

一系列 PVE 的工具脚本，包括安装后的一些维护、创建 LXC、部署软件等。

## 番外

这个星期情绪比较混乱，周末体检的时候又发现身体有点比意料中棘手的问题，因此这期周刊的内容有一些缩水。不过这个星期我花了比较多时间研究一个玩意——OSSHound，输入用户需求，LLM 分析优化关键词，利用 GitHub 工具搜索，返回符合要求的高星项目。我尝试了 Dify 和 Coze 两个平台，分别做英文关键词和中文关键词版本，初步能达到我想要的效果，不过实践中发现以下的问题：

- LLM 的能力差距在这个任务上表现得特别明显，使用 GPT 4 得到的效果非常喜人，GPT 3.5 Turbo 最新的版本偶尔能行，偶尔输出无效结果，字节的云雀最差，经常查到一些奇怪的库上
- 搜中文关键词只能出来中文项目（废话），所以在 GitHub 上还是多用英文搜索，项目的简介和 Readme 也最好用英文写
- 数据污染非常严重，在 GitHub 上搜索很多中文关键词，都会出来那几个思想很危险的宣传库，无奈这些库的 SEO 做得太好了，以至于如果搜到他就说明搜索关键词不对
- LLM 的审核需求非常大，因为你不知道 LLM 会读到一些什么奇怪的东西，说出来什么离经叛道的话，如果需要面向国内服务，那还是尽量加上云厂商的审核服务（阿里云就有）

最后，放一个效果图，这里让它找一个 Jira 的替代，出来的结果跟我自己搜索筛选的基本一致了。

![](https://img.ameow.xyz/202403101823757.png)

由于审核的原因，暂时没办法把这个放出来给大家玩，等我解决审核问题，会再写篇文章讲讲这个编排的思路和实现教程。
