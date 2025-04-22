---
issue: 27
date: 2024-06-02
intro: 猫鱼周刊的27期，内容包括文章《X-Y Problem》介绍了一个常见的沟通陷阱, F1车赛的旗语含义和用途, 以及一个可以自建的问卷系统。此外，分享了一个设计的文本转语音模型和一个跨全栈的编程课程。
---

## 关于本刊

> 这是猫鱼周刊的第 27 期，本系列每周日更新，主要内容为每周收集内容的分享，同时发布在
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

![](https://img.ameow.xyz/202406021353005.jpg)

这张照片是在深圳宝安前海演艺公园拍的欢乐港湾的摩天轮，这算是在深圳我最喜欢的地标了。趁着 618 买了 a6700 作为我的第二台相机，准备重拾一下摄影这个老爱好。理想情况下，以后每周周刊都会有一张好看的图片作为点缀。

## 文章

### X-Y Problem

[原文链接](https://coolshell.cn/articles/10804.html)

原文是左耳朵耗子陈皓写于 2013 年的文章，虽然我今天要分享的内容并不是受这篇文章启发，但是我在他这里第一次知道这个概念，因此留个 coolshell 的链接。他的博客虽然不再更新，但是很多内容还是很新鲜的，值得翻阅。

X-Y 问题指的是有人想解决问题 X，他想到一个可能的解决方案 Y，但是他不知道 Y 该怎么做，于是去问别人 Y 该怎么做；在解决过程中，大家在 Y 上耗费了大量时间，才发现原始的问题是 X，而 Y 根本不是解决 X 的合适方案。

X-Y 问题最早由 Eric S. Raymond 在 [How To Ask Questions The Smart Way](http://www.catb.org/~esr/faqs/smart-questions.html) 中提出（[中文版](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way)），主要强调在提问过程中最好把事情的背景阐述清楚。很多时候，这个问题被归类成沟通技巧，但在技术方案设计中，也经常发现有人会犯这个错误。

coolshell 的文章中已经有很多工程实践中的例子，我不再赘述。我想提出一个解决这个问题的好方法：退一步。在你提出一个解决方案，并准备开始调研时，先退一步，先列出问题的背景、方案拟解决的问题，再来想这个方案是否能满足这些具体的需求点，是否把问题复杂化了。在设计中，经常会出现初始的设计不能满足所有的需求，需要给方案打各种补丁的情况。这时候，把现在方向中需要的补丁提炼成一个硬需求清单，回到原点开始重新想，有没有能满足这些需求，又比现在这个方案更优化的方案。

当然了，这个思维路径可能不是一下子就能形成，有一个很简单的方式可以帮助你：写技术方案时先写背景和目的。我知道很多技术同僚不擅长也不喜欢写文档，但是习惯了开头先写背景和目的，能够帮助你主动地去完成“退一步”的过程，站在一个更高的角度去审视当前的问题和你拟提出的方案。

### F1 赛事中的旗语

[原文链接](https://www.autosport.com/f1/news/what-do-the-different-colour-flags-mean-in-f1-everything-to-know-about-the-10-flags/10583727/)

最近刷到一个 F2 摩纳哥站的视频（[B 站链接](https://www.bilibili.com/video/BV1ib421q7Es)），后车选手在隧道中施展了一次闪避避免了事故，很多人讨论说选手的反应真快云云。实际上，在进入隧道时，赛道马修就已经向后车选手发出白色灯光信号（警告车手前方有慢速车辆，可能存在危险）。

![CleanShot 2024-06-02 at 14.30.39@2x.png](https://img.ameow.xyz/202406021431744.png)

车手自身素质确实过硬，但是赛车比赛的安全实际上是由多方保证的，从车手本身、车辆设计再到赛委指挥、赛道马修。赛车在赛道上疾驰，最靠谱的交流方式就是视觉信号，因此赛车比赛设计了多种不同旗语来达成赛道上信息交换的目的。这篇文章普及了各种旗的含义及用途，还挺有意思。

### 绕过证书绑定

[原文链接](https://mas.owasp.org/MASTG/techniques/android/MASTG-TECH-0012/)

道高一尺，魔高一丈。一般大家认为，做了 Certificate Pinning 就能防住抓包了，但实际上还有很多公开的方式可以绕过。

没有百分百的安全。没有单一的完美的安全防护方案，只有通过多种方式组合，才能使进攻难度系数直线上升，直到攻击的成本大于攻击成功的收益。

## 项目

### 为对话场景设计的文本转语音模型

[![2noise/ChatTTS - GitHub](https://gh-card.dev/repos/2noise/ChatTTS.svg)](https://github.com/2noise/ChatTTS)

[项目链接](https://github.com/2noise/ChatTTS)

这个项目这周都刷屏了，效果比之前抖音那些什么悟空的音效都要好。如果你感兴趣，这里有个 [demo](https://huggingface.co/spaces/Dzkaka/ChatTTS) 可以在线生成。

我自己试了一下，英文的效果不怎么好，甚至说有点毛骨悚然，不过中文的效果确实不错。

### 可自建的问卷系统

[![didi/xiaoju-survey - GitHub](https://gh-card.dev/repos/didi/xiaoju-survey.svg)](https://github.com/didi/xiaoju-survey)

[项目链接](https://github.com/didi/xiaoju-survey)

滴滴开源的问卷系统，可以自建。第一次知道滴滴也有做开源。

## 工具/网站

### 深入浅出现代 Web 编程全栈公开课

[网站链接](https://fullstackopen.com/zh/)

一个由赫尔辛基大学（Linus Torvalds 的母校）发起的公开课，主要使用 JS/TS。内容很好，而且有中文翻译。JS/TS 可能是开源社区最喜欢的语言（见[链接](https://octoverse.github.com/2022/top-programming-languages)），用它来开发全栈项目也很适合。

## 最后

本周刊已在 [GitHub](https://github.com/LeslieLeung/cat-fish-weekly) 开源，欢迎 star。同时，如果你有好的内容，也欢迎[投稿](https://github.com/LeslieLeung/cat-fish-weekly/issues/new?assignees=LeslieLeung&labels=&projects=&template=recommendations.md)。如果你觉得周刊的内容不错，可以分享给你的朋友，让更多人了解到好的内容，对我也是一种认可和鼓励。

另外，我建了一个交流群，欢迎入群讨论或反馈。

![481717312140_.pic.jpg](https://img.ameow.xyz/202406021509799.jpg)
