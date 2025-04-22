---
intro: 本期猫鱼周刊内容包括55年前象征性的System/360主机终端、UV业余电台在通信时的注意事项以及大海捞针问题中文大模型首批结果公布。此外，介绍了最近的项目和一些工具/网站。
issue: 20
date: 2024-04-14
---

## 关于本刊

> 这是猫鱼周刊的第 20 期，本系列每周日更新，主要内容为每周收集内容的分享，同时发布在
>
> 博客：[阿猫的博客-猫鱼周刊](https://ameow.xyz/categories/weekly)
>
> RSS：[猫鱼周刊](https://ameow.xyz/feed/categories/weekly.xml)
>
> 邮件订阅：[猫鱼周刊](https://quaily.com/ameow)
>
> 微信公众号：[猫兄的和谐号列车](http://img.ameow.xyz/202401141448662.png)
>
> 私信：[leslieleung@pm.me](mailto:leslieleung@pm.me)

上周清明假期咕了一周，这周的内容相应可能多一点点，而且不再围着 LLM 讲了，也聊点别的。祝各位 Bon Appétit。

## 文章

### 55 年前象征性的 System/360 主机终端

[原文地址](https://www.righto.com/2019/04/iconic-consoles-of-ibm-system360.html)

![image.png](https://img.ameow.xyz/202404141930422.png)

第一眼看到这张照片，我还以为这是科幻电影里的场景。作为一个科幻电影迷，这个设计在 2024 年还是让我觉得很有未来感。再往下看到一排排灯泡、按键、旋钮组成的终端时，我真的觉得很酷。

回到技术上，那个时候庞大的终端主要是把寄存器、存储等等的每一个 bit 都展示出来，并且通过旋钮和按钮来操作里面的内容，是最底层的展示方式。这有点像现在的一些 LLM 应用，很多用户并不关心编排、知识库、RAG、embedding 这些东西，他们只关系 AI 能不能在某项工作上帮到他们实现出媲美人类的性能（以及免费使用，x）。LLM 的落地，更多还是要像大型机走向 PC 一样，以更加实用、易用的方式带给用户。

### 浅谈 UV 业余电台在（应急）通信时的注意事项

[原文地址](https://blog.mfwt.top/index.php/archives/222/)

其实是想介绍这个博客。国内业余无线电圈子比较小，相对应的博客更少。之前在 v2 一篇博客交换贴上偶然遇到的博客，内容基本上围绕无线电来讲，也有一些网络、折腾方面的内容。值得一看。

### 超长文本无损能力压测！中文大模型“大海捞针”首批结果公布

[原文地址](https://mp.weixin.qq.com/s/QgoRf2LB-7vc3vTFOHJkpw)

大海捞针（Needle in a Haystack, NIAH）问题最早由 [Greg Kamradt](https://github.com/gkamradt/LLMTest_NeedleInAHaystack) 提出，是一种给 LLM 压测的方式。虽然 LLM 一般都能处理很长的 context，但是在极端情况内，模型并不是一定能准确召回内容。该测试步骤如下：

- 将一个事实或语句（needle，针）放到很长的一段文本（haystack，干草垛）里。
- 让模型召回该语句
- 重复测试模型的长度和针放置的位置

从结果来看，GPT 4 Turbo 显然不是很擅长大海捞针，一定程度上可以说这个 context window 有点“假”。这篇文章对比的是中文大模型，在多语言方面，Claude 3 家族应该是目前最强，见 [Introducing the next generation of Claude \\ Anthropic](https://www.anthropic.com/news/claude-3-family)，基本上达到 100 %。

当然了，我觉得普通人沉迷对比各种模型是没什么意义的，这应该是一些学术机构去做的事情，通过科学地设置 benchmark，持续去对比各种模型的参数，长短处，给应用提供参考就行了。

## 项目

### LeslieLeung/dify-connector

[![LeslieLeung/dify-connector - GitHub](https://gh-card.dev/repos/LeslieLeung/dify-connector.svg?fullname=)](https://github.com/LeslieLeung/dify-connector)

先毛遂自荐一下我最近在做的一个新项目。

dify-connector 是一个将 [Dify](https://github.com/langgenius/dify) 发布到各种 IM 平台的工具。

特性：

- 将 Dify 应用发布到各种 IM 平台(Discord, 钉钉等)
  - ✅Discord
  - ✅ 钉钉
  - (计划中) Telegram
  - 更多...(欢迎 PR)
- (计划中) 管理控制台，用于管理 IM 频道和 Dify 应用
- (计划中) 为 Dify 应用提供内容审查 API

Coze 我觉得很实用的一个功能是能够把编排的应用发布到豆包、飞书等，这是 LLM 最简单的落地方式。不是所有人都有兴趣和对应的知识来编排，但是至少会乐意尝试别人编排好的应用。但是我更喜欢（或者说更早接触到） dify ，因此想把这个功能带给 dify 。

我对 dify 的理解是，dify 这个平台是个 agent 编排平台，是 LLM 工程师用的，不是最终用户使用的。最终用户是用基于 dify 的 api 再开发出来的东西。我认为发布到 IM 属于最后触达最终用户这一步，所以抽出来做比较合适。

### nicoxiang/geektime-downloader

[![nicoxiang/geektime-downloader - GitHub](https://gh-card.dev/repos/nicoxiang/geektime-downloader.svg?fullname=)](https://github.com/nicoxiang/geektime-downloader)

可以用来归档在极客时间购买的课程。虽然我知道这类软件很大一部分用途是用于盗版，我个人的用途是把在极客时间上购买的课程下载下来，防止因为不可抗力因素无法再访问课程资源。下载下来的内容也可以离线观看了，体验更好。

### wangshusen/RecommenderSystem

[![wangshusen/RecommenderSystem - GitHub](https://gh-card.dev/repos/wangshusen/RecommenderSystem.svg?fullname=)](https://github.com/wangshusen/RecommenderSystem)

工业界的推荐系统。作者是小红书的推荐算法工程师，这个项目很系统地介绍了推荐系统，当作 crash course 看，能快速掌握一些推荐系统里的专有名词，对用户行为、召回这些有个粗略的概念。

### drawdb-io/drawdb

[![drawdb-io/drawdb - GitHub](https://gh-card.dev/repos/drawdb-io/drawdb.svg?fullname=)](https://github.com/drawdb-io/drawdb)

有点像之前介绍的 [dbdiagram.io](https://dbdiagram.io/home) 的开源版本。UI 有点像借用了 [draw.io](https://draw.io/)。是一个可视化设计数据库的利器。

## 工具/网站

### 开源协议选择

[Choose an open source license | Choose a License](https://choosealicense.com/)

我愿称之为“赛博选妃”。一般来说，比较常见的有 MIT 和 GNU GPLv3 这些，我自己常用 GNU GPLv3。如果你不懂什么是开源协议，建议花点时间了解一下。根据之前的一些判例，我国是支持开源协议的。

### 提示工程指南

[提示工程指南 | Prompt Engineering Guide](https://www.promptingguide.ai/zh)

我之前很推荐另一个：[Prompt Engineering Guide](https://learnprompting.org/docs/intro)，但是它有很多文章都没完成，而且看起来很多文章都很久没更新了，有些内容都过时了。

这个网站提供很多种语言，建议阅读能力尚可的朋友看英文版，中文版的有很多新文章还没有翻译。

## 最后

本周刊已在 [GitHub](https://github.com/LeslieLeung/cat-fish-weekly) 开源，欢迎 star。同时，如果你有好的内容，也欢迎[投稿](https://github.com/LeslieLeung/cat-fish-weekly/issues/new?assignees=LeslieLeung&labels=&projects=&template=recommendations.md)。

另外，我建了一个体验反馈问卷，有别的意见也可以在这里[反馈](https://wj.qq.com/s2/14419451/42b1/)，或者加入交流群反馈。

![image.png](https://img.ameow.xyz/202404142018514.png)
