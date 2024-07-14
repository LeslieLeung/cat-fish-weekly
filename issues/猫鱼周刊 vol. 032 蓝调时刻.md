---
issue: 33
date: 2024-07-14
intro: 猫鱼周刊的33期，本期主要介绍了蓝调时刻、LLM 结构化输出、多智能体使用、json_repair项目和火烧云分析网站。
---

## 关于本刊

> 这是猫鱼周刊的第 33 期，本系列每周日更新，主要内容为每周收集内容的分享，同时发布在
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

![](https://img.ameow.xyz/202407141748505.jpg)

深圳前海的蓝调时刻。蓝调时刻指的是在一天中日出之前和日落之后这一短暂的时刻，这时候太阳刚好在地平线之下，整个天空会呈现蓝色。蓝调时刻每天都有，但只有十几分钟到半小时左右，有不少 APP 或网站可以查询，相比火烧云，蓝调时刻算是唾手可得的美好。

## 文章

### LLM 结构化输出

[原文链接](https://ameow.xyz/archives/llm-structural-output)

在几乎除了聊天以外所有的程序调用场景中，我们都希望 LLM 通过某种结构化的方式来输出，便于后续程序处理。在文章中中，采用了一个推书的例子，通过几种方式由简单到复杂地让 LLM 结构化地输出结果。采用的方法尽量不依赖某个平台或模型的特有功能，而是一些通用的方式来实现。

最简单的方式是在 `system` 中添加输出示例，并开启 JSON mode。也可以尝试使用 few-shot，但终结技是把整个 JSON schema 提供给模型，可以实现更加复杂的结构以及使用枚举等。

### 什么时候该用多智能体是不是一定要用多智能体？

[原文链接](https://baoyu.io/blog/ai/when-to-use-multi-agent-systems-or-cot)

「多智能体」可以大致理解为「多个 Prompt」，是一种把复杂任务分割成各个小部分的方式，本质上是软件工程中熟悉的「分而治之」的概念。作者以「直译、反思和意译」的翻译流程为例，展示了通过一个 prompt 和 「多智能体」的方式如何实现。

两种方式的优缺点可以在原文看，我聊聊我的看法。在不考虑实现需求和编程的问题，只考虑模型本身时，对于 4 代（gpt-4、gpt-4o、Claude 3 Opus 等）的模型，可以尝试使用单个 prompt，这类模型对于复杂的指令和任务有较好的效果；而使用 3.5 代（gpt-3.5、Claude 3 Haiku 等）模型时，考虑「多智能体」，保持每个任务足够简单。

> 先用多智能体把流程走通，然后再看看能不能优化成一个 Prompt 多个步骤。

作者提到的这个原则也非常实用。不过以我的经验来说，一开始可以先用「高级」的模型尝试一个 prompt 来解决，验证可行性，然后尝试换成低一点的模型，看看效果如何。但是基本上单个 prompt 的效果都一般，因此需要进入到工作流去编排，就是「多智能体」，到这一步基本上就是先像作者说的那样把任务尽量拆细。补充一个细节就是这时候最好先用「高级」模型把流程跑通，然后再找一些简单的任务（例如翻译等），尝试换成低一点的模型是否影响整体的效果。

当然，使用什么模型，是否采用多智能体是需要根据需求、成本去综合考虑的，在效果敏感、成本不敏感的时候当然无脑 gpt-4o+多智能体，效果不敏感、成本敏感的时候尽量用便宜的模型+简短的 prompt，这些都需要根据实际情况去考虑。

## 项目

### json_repair

[![mangiucugna/json_repair - GitHub](https://gh-card.dev/repos/mangiucugna/json_repair.svg)](https://github.com/mangiucugna/json_repair)
[项目地址](https://github.com/mangiucugna/json_repair)

LLM 的 JSON 输出不一定非常可靠，有时候会抽风生成出不合法的 JSON，导致后续程序无法解析。基本的原理是通过[BNF](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form)来解析 JSON，通过给数组或对象添加未闭合的括号、给字符串添加引号、调整空白或换行等启发式规则，尝试修复 JSON。

## 工具/网站

### 火烧云分析与记录

[网站链接](https://sunsetbot.top/)

![](https://img.ameow.xyz/202407141809450.jpg)

预报火烧云的鲜艳度。跟着预报走，减少扑空的可能性（我就连续扑空了两天，但好在看到了蓝调时刻，也不亏）。

火烧云的预报非常复杂，作者甚至写了一个很详尽的六万字的[文档](https://docs.qq.com/doc/DWHdrTVRPR3RaT0VD)来说明，感兴趣可以细读。

## 最后

本周刊已在 [GitHub](https://github.com/LeslieLeung/cat-fish-weekly) 开源，欢迎 star。同时，如果你有好的内容，也欢迎[投稿](https://github.com/LeslieLeung/cat-fish-weekly/issues/new?assignees=LeslieLeung&labels=&projects=&template=recommendations.md)。如果你觉得周刊的内容不错，可以分享给你的朋友，让更多人了解到好的内容，对我也是一种认可和鼓励。（或许你也可以通过[爱发电](https://afdian.net/a/3verest)请我喝杯咖啡）

另外，我建了一个交流群，欢迎入群讨论或反馈，可以通过文章头部的联系邮箱私信我获得入群方式。
