---
issue: 21
date: 2024-04-21
intro: 猫鱼周刊第21期，介绍了不同设计的载具和Llama 3的发布，以及文本嵌入测评、项目、工具和网站等内容。AI类工具在B端落地的难题有客观和主观原因。
---

## 关于本刊

> 这是猫鱼周刊的第 21 期，本系列每周日更新，主要内容为每周收集内容的分享，同时发布在
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

## 文章

### N 个轮的载具

[原文链接](http://www.douglas-self.com/MUSEUM/TRANSPORT/nwheelcar/nwheelcar.htm)

说起载具（vehicles），一般人的印象都是 4 个轮的现代汽车，然而历史上存在过很多不同设计的载具，从一个到 72 个不等。这篇文章细数了有历史记录的各种轮子个数的汽车。

![image.png](https://img.ameow.xyz/202404211643458.png)

我觉得比较实用的是一种五个轮的汽车，它在车尾备胎的位置设计了一个可升降的轮，帮助在马路边极窄的地方泊车，或者实现原地 90 度旋转、原地掉头等。

![image.png](https://img.ameow.xyz/202404211650596.png)

### Llama 3：当前最强的公开 LLM

[原文地址](https://ai.meta.com/blog/meta-llama-3/)

Llama 3 的发布不算什么新闻了，我挑几个点说一下：

- 70B 是当前旗舰，比 Claude 3 Sonnet 强，但不如 Claude 3 Opus
- 有一个 400B 的在训练了，对标 Claude 3 Opus
- Llama 3 70B 和 Claude 3 Sonnet 还有很多东西都比 GPT 3.5 强了，GPT 4 也是四面楚歌，Claude 3 Opus 已经吊打 GPT 4
- 开放性是个很大的优势，不仅主流的云服务平台能部署，[ollama](https://github.com/ollama/ollama)几乎是立刻就支持了，而且 7B 在 M1 Pro 上运行很快
- 延伸一下上一点，开放意味着性价比会更高。在 B 端，几个点的性能不如对半砍的成本重要。

### 文本嵌入测评

[原文地址](https://huggingface.co/spaces/mteb/leaderboard)

我在之前的几期介绍过大模型的榜单和测评（benchmark），这期介绍一个关于 embedding 的测评和榜单。

随着 RAG 的兴起，embedding 显得越来越重要。RAG（Retieval Augmented Generation）是一种通过寻找外部知识（Retrieval，召回）来辅助 LLM 生成回答的技术，通过这种技术，可以让 LLM 获得在训练语料以外的知识（例如一些私有的知识库，或在训练截止日期之后发生的事情等），来避免产生幻觉（语句上通顺但不符合事实的回答）。

在构建知识库时，需要对已有的一些文本内容分段、清洗并向量化，将向量存入向量数据库中。在查询时，用户输入先通过相同的模型进行向量化，并送入向量数据库中进行查询，这一步一般使用最近邻算法，取出在语义上最相似的几个片段；如果需要提升准确率，还需要进行重排（rerank），通过一定的算法计算用户输入和片段之间的关联性（这里跟语义相似度有一定的差别）；最后再把这几个片段作为上下文提供给 LLM 来产生回答。

因此可以看出，embedding 对于 RAG 质量有很直接的影响。另外，用于构建知识库的文本通常很多，虽然 OpenAI 的 embedding 也很便宜（$0.13/1M tokens），但自建的 embedding 通常能提供更低的时延和成本。

## 项目

### metowolf/vCards

[![metowolf/vCards - GitHub](https://gh-card.dev/repos/metowolf/vCards.svg?fullname=)](https://github.com/metowolf/vCards)

一个联系人订阅，搞好后短信界面是稍微好一点了。但是还是会有一大堆数不尽的 106 号码。

### jina-ai/reader

[![jina-ai/reader - GitHub](https://gh-card.dev/repos/jina-ai/reader.svg?fullname=)](https://github.com/jina-ai/reader)

能把任意网页转化成 LLM 可读的 Markdown 文档的工具。

## 工具/网站

### 与我协作，让 \<div\> 变成杰作

[网站地址](https://freelance.sunebear.com/)

一个自由职业者的接单落地页，动效非常出色。

![image.png](https://img.ameow.xyz/202404211743886.png)

## 想法

### AI 类工具在 B 端的落地

AI 类工具在 B 端落地很难，简单归纳以下几个原因。

客观原因：

AI 产出的内容质量不达标，达不到业务方的预期。根本原因是 LLM 作为通用的模型，不具备在某一个业务上深入的经验，因此在做一些有深度的工作时，没办法达到很好的结果。

主观原因：

a. 负面偏见。其实 LLM 交付的内容效果“一般”，至少是像模像样，但是匹配不上专业人类的水平，又或者一个或某个 case 不符合预期，造成对其接受度非常低。

b. 职业威胁论。在 AI 能完成“一般”的效果的前提下，其职业稳定性、地位是否会被其动摇。另，原本一天工作量的事情，引入提效后，是否会影响其效率安排（摸鱼）。

## 最后

本周刊已在 [GitHub](https://github.com/LeslieLeung/cat-fish-weekly) 开源，欢迎 star。同时，如果你有好的内容，也欢迎[投稿](https://github.com/LeslieLeung/cat-fish-weekly/issues/new?assignees=LeslieLeung&labels=&projects=&template=recommendations.md)。

另外，我建了一个体验反馈问卷，有别的意见也可以在这里[反馈](https://wj.qq.com/s2/14419451/42b1/)，或者加入交流群反馈。

![](https://img.ameow.xyz/202404211752324.jpg)
