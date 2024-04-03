---
issue: 11
date: 2024-01-28
---

- [关于本刊](#%E5%85%B3%E4%BA%8E%E6%9C%AC%E5%88%8A)
- [文章](#%E6%96%87%E7%AB%A0)
  - [GitHub Actions 小记](#GitHub%20Actions%20%E5%B0%8F%E8%AE%B0)
  - [混沌工程](#%E6%B7%B7%E6%B2%8C%E5%B7%A5%E7%A8%8B)
  - [Mojo 简介——超快的 Python 超集](#Mojo%20%E7%AE%80%E4%BB%8B%E2%80%94%E2%80%94%E8%B6%85%E5%BF%AB%E7%9A%84%20Python%20%E8%B6%85%E9%9B%86)
- [项目](#%E9%A1%B9%E7%9B%AE)
  - [Bistutu/GoMusic](#Bistutu/GoMusic)
  - [version-fox/vfox](#version-fox/vfox)
  - [eryajf/awesome-ops](#eryajf/awesome-ops)
- [工具/网站](#%E5%B7%A5%E5%85%B7/%E7%BD%91%E7%AB%99)
  - [在线画图平台](#%E5%9C%A8%E7%BA%BF%E7%94%BB%E5%9B%BE%E5%B9%B3%E5%8F%B0)
  - [ReadMedium](#ReadMedium)
- [想法](#%E6%83%B3%E6%B3%95)
  - [LLM 不过是碰巧经历丰富的旅行者](#LLM%20%E4%B8%8D%E8%BF%87%E6%98%AF%E7%A2%B0%E5%B7%A7%E7%BB%8F%E5%8E%86%E4%B8%B0%E5%AF%8C%E7%9A%84%E6%97%85%E8%A1%8C%E8%80%85)

## 关于本刊

> 这是猫鱼周刊的第 11 期，本系列每周日更新，主要内容为每周收集内容的分享，同时发布在
>
> 博客：[阿猫的博客-猫鱼周刊](https://ameow.xyz/categories/weekly)
> RSS：[猫鱼周刊](https://ameow.xyz/feed/categories/weekly.xml)
> 邮件订阅：[猫鱼周刊](https://quail.ink/ameow)
> 微信公众号：[猫兄的和谐号列车](http://img.ameow.xyz/202401141448662.png)
> Discord：[猫兄的和谐号高铁](https://discord.gg/5G5Nbtuz)
> 私信：[leslieleung@pm.me](mailto:leslieleung@pm.me)

## 文章

### GitHub Actions 小记

[原文链接](https://ameow.xyz/archives/github-actions)

GitHub Actions 是一个用来自动化软件开发工作流的工具。它的用途包括但不限于 CI/CD、生成文档、自动发布 Release、操作 Issue 等。它类似于 GitLab CI/CD、Jenkins 等 CI/CD 工具，有丰富的文档和社区支持，很适合用来入门。文章讲述了一个最简单的构建 Go Web 应用并发布 docker 镜像到 DockerHub 的过程。

### 混沌工程

[原文链接](https://en.wikipedia.org/wiki/Chaos_engineering)

混沌工程是指对系统进行试验以增强系统应对复杂条件的信心的一种实践。用大白话说，就是在系统中随机制造故障或混乱（称为混沌实验），来发现系统弱点、提高系统弹性（resilience）、验证容错等等。

混沌工程的历史也比较有趣，原来它最早出现在 1983 年，苹果利用一个随机高速产生 UI 交互事件的程序，模拟一只猴子疯狂敲击键盘、移动和点击鼠标的行为。这个程序被叫做猴子（Monkey）。后来在 Netflix 这一实践被“现代化”和推广，他们有一个工具会在生产环境中到处搞破坏，随机关闭一些实例，来测试系统的弹性。有趣的是，他们的这个工具就叫 ChaosMonkey。

### Mojo 简介——超快的 Python 超集

[原文链接](https://towardsdatascience.com/a-quick-introduction-to-mojo-a-superset-of-python-that-is-super-fast-079c619036a7) | [readmedium](https://readmedium.com/a-quick-introduction-to-mojo-a-superset-of-python-that-is-super-fast-079c619036a7)

Python 被诟病慢已经很久了，主要原因是它被设计成一个弱类型语言，而且是解释执行。而对于机器学习/深度学习来说，计算性能的提升尤为重要。有个叫 Modular 的公司开发了一个名为 Mojo 的语言，它被设计为 Python 的超集（现在还不是，因为有些 Python 的语法它暂时还不支持）。

## 项目

### Bistutu/GoMusic

[![Bistutu/GoMusic - GitHub](https://gh-card.dev/repos/Bistutu/GoMusic.svg?fullname=)](https://github.com/Bistutu/GoMusic)

最近网易云改版，原来可以定义的底部 tab 和资讯模块没了，塞进了一堆臃肿的东西。于是一狠心迁移到 Apple Music 了。这个工具能通过输入网易云歌单 id 提取出一份纯文本的歌单列表，通过 [TunemyMusic](https://www.tunemymusic.com/zh-CN/transfer)就可以转移到 Apple Music 或者 Spotify 了。

> 注意，TuneMyMusic 是一个付费订阅服务，如果你的歌单小于 500 首歌，则不需要付费。如果超过了，就必须最低订阅一个月（约 30 人民币）才能迁移。

### version-fox/vfox

[![version-fox/vfox - GitHub](https://gh-card.dev/repos/version-fox/vfox.svg?fullname=)](https://github.com/version-fox/vfox)

一个跨平台的可以用来切换 SDK 版本的工具，类似 node 的 [nvm](https://github.com/nvm-sh/nvm)。vfox 目前支持 Node、Java、Golang 等等，也可以通过 lua 脚本自定义插件（每个 SDK 可以视为一个插件，通过 lua 脚本实现切换）。

这个项目的出现有些“不合时宜”，毕竟现在 devcontainer 也很方便。我能想到它比较适合的场景是 Mac 用户，内存比较宝贵，所以不适合用 Docker 进行开发。另外，这个对 Go 程序员可能也比较鸡肋，因为 Go 版本基本是向前兼容的，只需要有一个 Go 版本就可以了。

### eryajf/awesome-ops

[![eryajf/awesome-ops - GitHub](https://gh-card.dev/repos/eryajf/awesome-ops.svg?fullname=)](https://github.com/eryajf/awesome-ops)

一个 awesome-list 类型的项目，主题为运维相关，目前在快速成长中。

这个项目比较有意思的点是，它通过每个项目一个 yaml 文件来进行管理，然后通过 GitHub Actions 生成 markdown。之前看过的一些 awesome-list 基本是通过 markdown 对里面的项目进行管理，然后通过 badge 等形式去引入 star 数等数据。这种新方式能够大幅降低维护成本，不需要手动进行排序等等，也能生成出一个漂亮的表格，有静态的 star 数等信息。

## 工具/网站

### 在线画图平台

最近经常有画图的需求，我把最近调研的画图平台/工具简单横评了一下，供大家参考。

| 产品                                        | 是否支持协同       | 是否支持自建       | 是否有图标集                         | 是否免费                           | 特性                                                                                     |
| ------------------------------------------- | ------------------ | ------------------ | ------------------------------------ | ---------------------------------- | ---------------------------------------------------------------------------------------- |
| [draw.io](https://app.diagrams.net/)        | ✅（需要使用网盘） | ✅                 | ✅                                   | ✅                                 |                                                                                          |
| [excalidraw](https://excalidraw.com/)       | ✅                 | ❌（作为组件提供） | ✅（仅手绘风格，需要使用基础图形画） | ✅                                 |                                                                                          |
| [tldraw](https://www.tldraw.com/)           | ✅                 | ❌（作为组件提供） | ❌                                   | ✅                                 |                                                                                          |
| [ProcessOn](https://www.processon.com/)     | ✅                 | ❌                 | ✅                                   | ❌（免费版限制文件数量和协作人数） |                                                                                          |
| [Mermaid Live Editor](https://mermaid.live) | ❌                 | ❌                 | ❌                                   | ✅                                 | mermaid 的在线编辑器，可以导出图片。当然也可以在支持的 markdown 编辑器里直接写 mermaid。 |
| [onemodel](https://www.onemodel.app/)       | ✅（需要付费）     | ❌                 | ✅                                   | ✅（个人使用免费，不限制文件数）   | 仅协作功能需要付费。自带了常见的软件的图标集，自动排版很美观，非常为开发特化的画图工具。 |

### ReadMedium

[网站链接](https://readmedium.com/)

![](https://img.ameow.xyz/202401282216822.png)

主要的两个功能是解锁会员文章和对比翻译。

解锁方式有两种，进入 ReadMedium 然后输入文章地址，或者直接在文章地址`medium.com`前面加上`read`。仅用于学习，如果有财力还是建议付费支持。

对比翻译就是打开文章后在右上角可以让它翻译成对应的语言，一上一下对比翻译。

## 想法

### LLM 不过是碰巧经历丰富的旅行者

现在越来越多人依赖 LLM 查询或解决技术问题，我个人非常反感盲目信任 LLM，不对结果加以验证的行为。

LLM 不过是一个碰巧经历丰富的“旅行者”，并不是某个领域的专家，它“语言模型”的属性决定它的基础逻辑是顺着你的话讲下去（因此当你说它不对，它很可能会说抱歉然后说出一个跟之前完全相反的答案）。它不具有显式的逻辑推理能力，它的逻辑推理能力仅限于“语句通顺”的“隐式”逻辑。因此 LLM 并不适合回答较为专业的问题，尤其是技术问题，容易造成误导。另外软件是会更新的，API 等是会变化的，LLM 会受限于训练时的语料来源而产生偏差（不包含 web 访问插件的情况下）。
