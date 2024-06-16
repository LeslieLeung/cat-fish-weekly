---
issue: 29
date: 2024-06-16
intro: 这是猫鱼周刊的第 29 期，内容涵盖了关于扫街摄影、自建服务清单、软件工程设计文档的技巧、SmokePing和awesome-cloudflare项目介绍以及LLM排行榜和Linux镜像源的工具和网站推荐。
---

## 关于本刊

> 这是猫鱼周刊的第 29 期，本系列每周日更新，主要内容为每周收集内容的分享，同时发布在
>
> 博客：[阿猫的博客-猫鱼周刊](https://ameow.xyz/categories/weekly)
>
> RSS：[猫鱼周刊](https://ameow.xyz/feed/categories/weekly.xml)
>
> 邮件订阅：[猫鱼周刊](https://quail.ink/ameow)
>
> 微信公众号：[猫兄的和谐号列车](http://img.ameow.xyz/202401141448662.png)
>
> 私信：[leslieleung@pm.me](mailto:leslieleung@pm.me)

![](https://img.ameow.xyz/202406160012067.jpeg)

最近解锁了一个新爱好：扫街。这张照片摄于深圳南头古城，就是一条城中村中的商业街，有不少卖文创的店。路过一家店的时候看到店门口这个很有意思的布景：一张简单的木椅，背后是一丛绣球花。

买了相机之后总想出去多拍拍照片，发现扫街是最适合 i 人（猫）的拍照方式，不需要像拍人像一样流连于各种交流群、约模特，就挑任意一个时间（最好还是白天，有人活动、光线也好），背起相机出门就可以拍。也没什么特别的技巧，就是拿着相机慢慢逛，跟各种美好偶遇。

## 文章

### 那些常住在我 Homelab 的服务

[原文链接](https://chi.miantiao.me/posts/homelab-services/)

作者整理了一些常用（长用？）的自建服务，如果你对自建服务感兴趣，这应该是一个不错的列表。

话说我也玩自建好几年了，部署过好多服务，平时在周刊里也介绍过很多，最终留下来长期用的其实不多（其实这跟 App 差不多）。在部署的众多服务里面，用得最频繁的只有一个，我自己写的通知服务 [Heimdallr](https://github.com/LeslieLeung/heimdallr)。不得不说，切合自己需求写的东西才是最实用的。如果大家想看，我有空也整理一篇我的自建服务清单。（欢迎留言评论）

### 如何写一份高可读性的软件工程设计文档

[原文链接](https://mp.weixin.qq.com/s/-qXlbPt25-8aZAtCCxh1MQ)

在 [vol. 026](https://ameow.xyz/archives/weekly-026#X-Y-Problem) 我分享过陈皓的一篇讲 X-Y 问题的文章，在最后我提到，在写文档的时候先写目的和背景，能有助于更好地考虑问题。

> 写技术方案时先写背景和目的。我知道很多技术同僚不擅长也不喜欢写文档，但是习惯了开头先写背景和目的，能够帮助你主动地去完成“退一步”的过程，站在一个更高的角度去审视当前的问题和你拟提出的方案。

这期分享的文章算是对上期的一个补充（才翻出来之前收藏的这篇）。根据文章的内容，再加上一些我自己的理解，我简单总结了一些要点：

- 确定受众：根据你的受众，往文档里添加适量的背景信息，决定内容的详略（例如向更大的受众，则要添加更多背景信息，更多讲述设计思路而不是具体实现/贴代码）。
- 使用模板：用一个相对完整、规范的结构来帮助你思考和行文。
- 使用简洁、准确的语言：正确使用专业术语，不要用复杂的句式，精简段落，使用 Bullet Point、图标等帮助表达，控制篇幅。
- 注意排版：使用统一的格式，会让文档不显得杂乱。使用分级标题等。

另外，我想再提出几个雷点：

- 大段贴官方文档原文或翻译：应该简练地概括，再附上链接。
- 大段贴代码：没人想看你的代码！如果有需要，可以用伪代码来辅助表达，或者只贴关键的片段。
- 没有结构、流水账：就像写任何一篇文章一样，你的文章是你想法的映射，混乱的结构体现的是你对整件事情也没有清晰的了解。

## 项目

### SmokePing

[![oetiker/SmokePing - GitHub](https://gh-card.dev/repos/oetiker/SmokePing.svg)](https://github.com/oetiker/SmokePing)
[项目地址](https://github.com/oetiker/SmokePing)

用于监控宽带连通性和延迟的工具，可以用来诊断网络问题。

### awesome-cloudflare

[![zhuima/awesome-cloudflare - GitHub](https://gh-card.dev/repos/zhuima/awesome-cloudflare.svg)](https://github.com/zhuima/awesome-cloudflare)
[项目地址](https://github.com/zhuima/awesome-cloudflare)

又一个 awesome 列表项目，这次是“赛博菩萨” Cloudflare 上可以搭的一些项目/工具等。不过我还是提倡不要滥用，薅羊毛别把羊薅秃了，等下大家都薅不成了。

## 工具/网站

### LLM 排行榜

[网站链接](https://livebench.ai)

![image.png](https://img.ameow.xyz/202406160100585.png)

一个公正客观的 LLM 评测。它通过以下方式保证公正客观：

- 每个月发布新的问题集，并且从最新的数据集中构建问题（保证所有 LLM 都没有见过对应的语料和问题）
- 每个问题都有可验证、客观的事实结果，对于难的问题也可以准确和自动地评分而不需要 LLM 裁判（之前有 LLM 给自家的模型打高分）

之前我也介绍过几个类似的排行榜，具体可以看[这里](https://ameow.xyz/docs/aigc/llm/leaderboards)。

### LinuxMirrors

[网站链接](https://linuxmirrors.cn/)

运行一个命令就可以给 Linux 系统换源，还挺实用（不用每次去手动改）。

```bash
bash <(curl -sSL https://linuxmirrors.cn/main.sh)
```

## 最后

本周刊已在 [GitHub](https://github.com/LeslieLeung/cat-fish-weekly) 开源，欢迎 star。同时，如果你有好的内容，也欢迎[投稿](https://github.com/LeslieLeung/cat-fish-weekly/issues/new?assignees=LeslieLeung&labels=&projects=&template=recommendations.md)。如果你觉得周刊的内容不错，可以分享给你的朋友，让更多人了解到好的内容，对我也是一种认可和鼓励。（或许你也可以通过[爱发电](https://afdian.net/a/3verest)请我喝杯咖啡）

另外，我建了一个交流群，欢迎入群讨论或反馈，可以通过文章头部的联系邮箱私信我获得入群方式。
