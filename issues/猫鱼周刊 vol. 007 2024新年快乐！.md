---
issue: 8
date: 2024-01-07
---

- [关于本刊](#%E5%85%B3%E4%BA%8E%E6%9C%AC%E5%88%8A)
- [头条](#%E5%A4%B4%E6%9D%A1)
- [文章](#%E6%96%87%E7%AB%A0)
  - [生成式 AI 在软件开发中的变革性力量](#%E7%94%9F%E6%88%90%E5%BC%8F%20AI%20%E5%9C%A8%E8%BD%AF%E4%BB%B6%E5%BC%80%E5%8F%91%E4%B8%AD%E7%9A%84%E5%8F%98%E9%9D%A9%E6%80%A7%E5%8A%9B%E9%87%8F)
  - [中文大模型基准测评 2023 年度报告](#%E4%B8%AD%E6%96%87%E5%A4%A7%E6%A8%A1%E5%9E%8B%E5%9F%BA%E5%87%86%E6%B5%8B%E8%AF%84%202023%20%E5%B9%B4%E5%BA%A6%E6%8A%A5%E5%91%8A)
  - [「缺省」这个词是如何从英语 "Default" 翻译过来的？](#%E3%80%8C%E7%BC%BA%E7%9C%81%E3%80%8D%E8%BF%99%E4%B8%AA%E8%AF%8D%E6%98%AF%E5%A6%82%E4%BD%95%E4%BB%8E%E8%8B%B1%E8%AF%AD%20%22Default%22%20%E7%BF%BB%E8%AF%91%E8%BF%87%E6%9D%A5%E7%9A%84%EF%BC%9F)
- [项目](#%E9%A1%B9%E7%9B%AE)
  - [review-2023](#review-2023)
  - [cmd-wrapped](#cmd-wrapped)
- [工具/网站](#%E5%B7%A5%E5%85%B7/%E7%BD%91%E7%AB%99)
  - [Say what you see!](#Say%20what%20you%20see!)
  - [FRE 123 技术周刊精选推荐](#FRE%20123%20%E6%8A%80%E6%9C%AF%E5%91%A8%E5%88%8A%E7%B2%BE%E9%80%89%E6%8E%A8%E8%8D%90)
  - [Oh-My-Zsh Git Cheatsheet](#Oh-My-Zsh%20Git%20Cheatsheet)
- [想法](#%E6%83%B3%E6%B3%95)
  - [别急](#%E5%88%AB%E6%80%A5)

## 关于本刊

> 这是猫鱼周刊的第 8 期，本系列每周日更新，主要内容为每周收集内容的分享，同时发布在
>
> 博客：[阿猫的博客-猫鱼周刊](https://ameow.xyz/categories/weekly)
> RSS：[猫鱼周刊](https://ameow.xyz/feed/categories/weekly.xml)
> 邮件订阅：[猫鱼周刊](https://quail.ink/ameow)
> Discord：[猫兄的和谐号高铁](https://discord.gg/5G5Nbtuz)
> 私信：[leslieleung@pm.me](mailto:leslieleung@pm.me)

## 头条

新年快乐！这是猫鱼周刊在 2024 年的第一刊，在这里祝各位新年快乐，工作顺利，生活如意。

## 文章

### 生成式 AI 在软件开发中的变革性力量

[原文链接](https://www.uber.com/blog/the-transformative-power-of-generative-ai)

Uber 在内部搞了一个 Hackathon，让各个团队尝试了一些将生成式 AI 集成进工作流程的方式。

![](http://img.ameow.xyz/202401071949925.png)

他们主要尝试了以下用途：

- 设计文档，审校和风险评估
- 代码和测试生成
  - 解释现有代码
  - 生成 UI 代码
  - 自动化重构和集中迁移
- 自动化修复
  - 评审及优化现有代码
- 测试生成
- 代码调试
- 代码评审（Code Review）
- 错误分类
- 本地化（翻译）
- 知识库

同时，他们也提出生成式 AI 有两个风险，一是输出内容的质量，二是决策的可解释性。

### 中文大模型基准测评 2023 年度报告

[原文链接](https://mp.weixin.qq.com/s/PycSpCCREBgB0tEy3csPKQ)

SuperCLUE 团队出品的国内大模型基准测评，采用了多维度、多视角的综合性测评方案，包含简答题、客观题等，对国内外有代表性的 26 个大模型进行了测评。

![](http://img.ameow.xyz/202401072003473.png)

值得注意的是，这个测评标准，使得大模型的具体表现可以量化。之前一直有很多讨论，说 GPT 某个版本或者从某时间开始变笨了等等，终于有量化的结果来支持这种言论了。

![](http://img.ameow.xyz/202401072007881.png)

### 「缺省」这个词是如何从英语 "Default" 翻译过来的？

[原文链接](https://www.zhihu.com/question/20953160)

我一直觉得 “Default” 翻译成“默认值”是比较合适的，这个回答提供了一个新的角度：预设值（preset value）和缺省/除错/补缺值（default value）。预设和缺省是有区别的，预设指的是预先设置一个值，后面没人设置了，就默认这个值，是事先设置的；而缺省指的是，没有预先设置一个值，让用户填空，用户操作失误没有填或填错了，补上一个值，是事后弥补的。因此预设值和缺省值都是“默认值”。

后面也有很多回答，各有千秋，但是总的来说我比较认同这个高赞答案。

## 项目

### review-2023

[![saveweb/review-2023 - GitHub](https://gh-card.dev/repos/saveweb/review-2023.png)](https://github.com/saveweb/review-2023)

汇总了很多中文博客的 2023 年终总结，看下别人在折腾什么，挺有意思的。

也顺便再发一下我的[年终总结](https://ameow.xyz/archives/2023-wrapup)。

### cmd-wrapped

[![YiNNx/cmd-wrapped - GitHub](https://gh-card.dev/repos/YiNNx/cmd-wrapped.png)](https://github.com/YiNNx/cmd-wrapped)

命令行的年终总结。

（可惜我今年 10 月份的时候丢失了一次数据，不然这个应该很有意义）

![](http://img.ameow.xyz/202401072044244.png)

![](http://img.ameow.xyz/202401072046411.png)

## 工具/网站

### Say what you see!

网站链接：[Say What You See — Google Arts & Culture](https://artsandculture.google.com/experiment/say-what-you-see)

AI 画图提示词训练器（❌），英语学习工具（✅）。

进入关卡，左边会先展示一幅图，你在右边输入对应的描述，然后根据你的描述再生成一张图，通过两张图的相似度（或者也可能是提示词的相似度）判定是否符合。

我遇到的这个关卡就很有意思，里面有两个我稍微思考了一下的单词，一个是田野（field），另一个是作物（crop）。

![](http://img.ameow.xyz/202401072058510.png)

### FRE 123 技术周刊精选推荐

网站链接：[技术周刊精选推荐 - fre123 免费资源共享平台](https://www.fre123.com/weekly/)

很新鲜的体验，将所有优质周刊资源聚合起来了。

### Oh-My-Zsh Git Cheatsheet

网站链接：[Oh-My-Zsh Git Cheat Sheet - Kapeli](https://kapeli.com/cheat_sheets/Oh-My-Zsh_Git.docset/Contents/Resources/Documents/index)

Oh-My-Zsh 自带了很多 git 命令的 alias，我之前一直只会用 `gp` （git push），打字这事，能省则省嘛！

## 想法

### 别急

> 大概意思是：“树熊，身边朋友看起来都挺厉害的，不知道自己什么时候才变得厉害。”
>
> 他讨厌自己现在这么弱，更害怕自己以后也是这么弱。
>
> 我回他：“你可以快一点，但不要更着急。”
>
> 这句话的意思理解起来并不复杂。
>
> 因为“快”是做事节奏，而“急”是一种心态。做事可以快，可心态一旦“上火”，就会燥热，容易生病。

很久以前在不知道哪里摘抄下来的句子，我一直急于变强，出来工作后，又急于赚到大钱。别急，可以多做一点事，光心态上的焦虑并不解决问题。共勉。
