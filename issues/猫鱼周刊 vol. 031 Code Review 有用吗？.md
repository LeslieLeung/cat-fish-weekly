---
issue: 32
date: 2024-07-07
intro: 猫鱼周刊第32期分享了一篇关于DS_store的文章，介绍了它的来源和作用。另外，讨论了Code Review的重要性和最佳实践。还介绍了两个有趣的项目和一个实用的工具网站。此外，分享了一个关于着急写代码的想法。欢迎大家阅读和分享。
---

## 关于本刊

> 这是猫鱼周刊的第 32 期，本系列每周日更新，主要内容为每周收集内容的分享，同时发布在
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

![DSC00646.jpeg](https://img.ameow.xyz/202407071440107.jpeg)

这张照片摄于一个早晨（大概六七点的时候）。很久没在这个时间往外看了，才发现阳光的金色照在云上，加上云的纹理，也是很美的景色。

## 文章

### DS_store 的来源

[原文链接](https://www.arno.org/on-the-origins-of-ds-store)

在把 Mac 上的文件传到 Windows 上时，经常会出现一个 `.DS_Store` 文件。这是一个「没什么用」的文件，在 \*nix 系统上会表现为一个隐藏文件。没想到，它其实是 Finder 的一个历史遗留（也不知道算不算得上是 bug）。在 1999 年时，作者作为 Finder 的技术领导，决定重构当时已经有 8 年历史的代码，把 Finder 分成了前端和后端，这个文件名就是当时定下来的。理论上，只会对文件夹做了显示设置或者更改图标才会创建这个文件，但是一个遗留的 bug 导致现在只要用 Finder 打开一个文件夹几乎就一定会创建这个文件。

说起历史遗留，其实很多操作系统里都有很多上古代码，例如 Windows 里有兼容 DOS 的代码等。这个行业对历史的尊重堪称一绝，今天的 Windows 和 macOS 都还能直接打开软盘。

### Code Review 确实能发现 Bug

[原文链接](https://two-wrongs.com/code-reviews-do-find-bugs.html)

微软在 2015 年发表过一个研究说 CR 中只有 15%的评论实际上是缺陷，作者认为这是一个谬误。有研究表明，CR 只要多花 15% 的时间成本就能多发现 60%的缺陷，但作者认为前提是 CR 遵从了最佳实践。另外，除了发现代码中的缺陷，CR 还有助于团队成员熟悉代码。

实际上，CR 有很多最佳实践，这里有一个[谷歌的实践](https://google.github.io/eng-practices/review/)可供参考。从我的经验来说，作为提交者，我会：

- 向 Reviewer 介绍需求背景，讲解大概的思路，附上必要的文档等
- 保持 commit 的代码量在一两百行内，边界清晰（不夹带私货），有描述性的 commit message
- 代码层面，写好注释，保持好的风格，格式化好等等

而作为 Reviewer，我会：

- 指出可能会产生 bug 的地方，并要求对方修改
- 尽管对方不一定会接受，提出所有自己认为可以优化的地方，包括一些风格上的

在实践中，我发现 CR 的机制经常失效。有以下几种情况：

- 跳过 CR：虽然版本控制系统做了限制，但是有办法可以跳过，就导致有机会贪方便钻空子提交未经审核的代码。
- 草草 CR：迫于「对方比自己资深」、「提了对方也不会改」、「时间安排紧」等原因，只保证功能上能用，不对性能、风格、可维护性等方面进行评估。
- 无效 CR：虽然提了建议，但是作者没有修改就提交了。（这个算是前面的一个混合）

技术债是软件工程的必然副产物，但如果技术债严重，可以说是管理失职。CR 能够帮助解决技术债，但只有自上而下保证 CR 机制的有效，才能防止技术债积累。

## 项目

### ladybird

[![LadybirdBrowser/ladybird - GitHub](https://gh-card.dev/repos/LadybirdBrowser/ladybird.svg)](https://github.com/LadybirdBrowser/ladybird)
[项目地址](https://github.com/LadybirdBrowser/ladybird) | [项目官网](https://ladybird.org/)

一个宣称「真正独立」的浏览器。重点是他们宣称不使用 Blink、WebKit、 Gecko 或其他引擎的代码（这三个背后分别是 Google、苹果和 Mozilla）。不过要等 2026 年夏天才有第一个 alpha 版本，敬请期待。

### pintree

[![Pintree-io/pintree - GitHub](https://gh-card.dev/repos/Pintree-io/pintree.svg)](https://github.com/Pintree-io/pintree)
[项目地址](https://github.com/Pintree-io/pintree) | [演示地址](https://app.pintree.io/)

把书签转换成导航的工具。比起现有的一些链接收藏工具或者导航站，感觉都要更简洁好看。

![image.png](https://img.ameow.xyz/202407071600472.png)

## 工具/网站

### ray.so

[网站链接](https://ray.so)

包含了六个小工具，是 Raycast 官方做的。有两个比较实用，一是制作代码图片，很适合分享在社交媒体；二是图标生成，可以用在 Raycast 或者其他地方，还支持导出 PNG 或 SVG 格式。剩下一些跟 Raycast 平台绑定，如果感兴趣也可以看看。

![image.png](https://img.ameow.xyz/202407071602232.png)

## 想法

### 别心急写代码

发现有的人在遇到问题时会有这么一个思维：「我会一个什么东西，我要把这个套在现在的问题上来解决」，一上来就吭哧吭哧地写代码。

我觉得好的方式是，正如我之前说过的，退一步，分析当前问题关键是什么，寻找对应的最佳解决方案。代码是最简单的东西，花时间计划清楚，再开始写，就不会出现中途发现设计问题需要推翻重做的尴尬，也能帮助你在写的时候思路清晰、不出 bug。

我想把这个问题归咎于「中国式教育」，习惯用固定的解题方式去套问题，容易陷进思维定式，也没法解决一些很新颖或者「老师没讲」的内容。当然这也跟知识的广度有关，当一个人拥有很多解决问题的手段，他就不会着急用手头仅有的一两个方法去试。

## 最后

本周刊已在 [GitHub](https://github.com/LeslieLeung/cat-fish-weekly) 开源，欢迎 star。同时，如果你有好的内容，也欢迎[投稿](https://github.com/LeslieLeung/cat-fish-weekly/issues/new?assignees=LeslieLeung&labels=&projects=&template=recommendations.md)。如果你觉得周刊的内容不错，可以分享给你的朋友，让更多人了解到好的内容，对我也是一种认可和鼓励。（或许你也可以通过[爱发电](https://afdian.net/a/3verest)请我喝杯咖啡）

另外，我建了一个交流群，欢迎入群讨论或反馈，可以通过文章头部的联系邮箱私信我获得入群方式。
