---
issue: 26
date: 2024-05-26
intro: 这是猫鱼周刊的第 26 期，内容包括正在加速崩塌的中文互联网、UTF、Emoji和连字的基础知识，以及一些项目和工具的介绍。
---

## 关于本刊

> 这是猫鱼周刊的第 26 期，本系列每周日更新，主要内容为每周收集内容的分享，同时发布在
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

## 文章

### 正在加速崩塌的是「中文」，不是互联网

[原文链接](https://blog.est.im/2024/stderr-09)

这是一个“水深火热”议题。最原始的文章是“何加盐”写的一篇名为《中文互联网正在加速崩塌》的文章，由于这篇文章本身已经 404，我对其中数据和观点也不完全认同，感兴趣的读者可以自行搜索查看。其从搜索引擎搜不到过去的信息出发，总结出互联网正在遗忘以前的内容这个观点。

来到这篇文章，作者通过一个数据（Common Crawl 的中文数据量，其是一个采集互联网上内容的项目）证实了从 2019 年开始，数据开始下降。他认为中文互联网的崩溃的原因是长截图的崛起和音视频的统治。同时，由于各个内容网站筑起高墙，实现内部搜索，导致公共的搜索根本无法获得很好的结果。

有几段我比较在意：

> 文本实际上就是人脑活动的压缩，对信息的概括。这是 transformer 架构和语言模型对我的一个巨大启发。这个有损压缩，丢掉的是什么呢？情绪和环境上下文，也就是亲切感。如今的音视频把这一最古老的人类群居基石——聊天拉回现实，放入口袋里那一小块屏幕中，怪不得雷军、周鸿祎这样的老人都出来当网红了。

加速崩塌的实际上是“文本”这个载体，音视频才是人之间最简单的交流方式，“文本”自古就是小众的，现代普及了教育，才增加了识字的比率。曾经的科技水平不发达，传输信息的带宽很低，才发展出以文本为主的交流方式（写信、印刷、电子邮件等等）。如今带宽大大增加，自然音视频这个载体重新占据回互联网的主流。这倒是帮我想明白了一个问题，为什么以视频为载体的教程比以文本为载体的官方教程会有更多人看。

话又说回来，文本是一个信息密度更高的载体（也有人认为是“有损压缩”），也是我比较偏好的信息传递方式。也许这也是我坚持创作博客的原因吧。

> 人们对互联网的期待显然可以分为两种：一种是客观的，工具性质的，严肃话题研究。这就是过去 USENET 和 UGC 的宝藏所在；另一种，人们是为了瞬间的快乐，长时间的归属感，去找认同的。这个时候，互联网提供了多彩的屁股位置选项。过去，没人知道互联网上对方是不是一条狗，现在，没人在乎你是不是沃尔玛购物袋，但是这并不妨碍网上武装直升机们为这事吵得不亦乐乎。

认同。

### UTF、Emoji 和神奇的连字

[原文链接](https://ecnelises.com/2024/05/utf-emoji-ligatures/)

文章介绍了 Unicode、UTF 的几个变种以及 emoji 和连字的一些基础知识。

我觉得字符编码是一个被严重低估的主题。我觉得在大部分国内程序员的认知里，要避免乱码就用 UTF-8，数据库里要存 emoji 就要用 utf8mb4，仅此而已。实际上，作为中文使用者，字符编码确确实实是一个我们需要了解的东西，不像美国人，一个 ASCII 就能解决他们的使用需求。

## 项目

### Bash 的高级语言

[项目链接](https://github.com/Ph0enixKM/Amber)

shell 脚本不好写，以现代眼光来看它有点残缺。Amber 就是一个 Bash 的高级语言，可以用现代的语法去写，然后通过 amber 编译成 shell 脚本。

### 网站统计

[项目链接](https://github.com/Openpanel-dev/openpanel)

![image.png](https://img.ameow.xyz/202405261732504.png)

一个网站统计工具，Google Analytics 的替代，有点像 Umami。目前来说还不能自建，不过看着界面挺简洁。

### 创建自己的 awesome-list

[项目链接](https://github.com/maguowei/starred)

一个可以根据自己的 GitHub star 列表生成 awesome 项目的模板。

### LLM 多合一 SDK

[项目链接](https://github.com/BerriAI/litellm)

一个 Python 的聚合 LLM SDK，可以通过统一的接口调用不同的 LLM 服务。最近它新增了一个类似 [one-api](https://github.com/songquanpeng/one-api) 的代理功能，有[管理面板](https://docs.litellm.ai/docs/hosted)。

## 工具/网站

### Go 代码片段例子

[网站链接](https://gobyexample.com/)

![image.png](https://img.ameow.xyz/202405261750198.png)

写代码的时候会有提笔忘字的现象，尤其是用得不多的时候，例如不熟悉的泛型。这个网站提供了很多这种小例子来帮你快速捡起一些语法或者实现一些功能的片段（例如这个限流的[例子](https://gobyexample.com/rate-limiting)）。

不过，如果你有 Copilot，可以尝试打一行注释让它自动写。

## 最后

本周刊已在 [GitHub](https://github.com/LeslieLeung/cat-fish-weekly) 开源，欢迎 star。同时，如果你有好的内容，也欢迎[投稿](https://github.com/LeslieLeung/cat-fish-weekly/issues/new?assignees=LeslieLeung&labels=&projects=&template=recommendations.md)。如果你觉得周刊的内容不错，可以分享给你的朋友，让更多人了解到好的内容，对我也是一种认可和鼓励。

另外，我建了一个交流群，欢迎入群讨论或反馈。

![471716717243_.pic.jpg](https://img.ameow.xyz/202405261754962.jpg)
