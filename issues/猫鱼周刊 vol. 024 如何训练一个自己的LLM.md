---
issue: 25
date: 2024-05-19
intro: 猫鱼周刊第 25 期介绍了几篇文章和一些项目、工具和网站，包括粤语 Qwen/LMM 微调教程、LLM 原理解释、离线使用 Git、Apple Watch 表盘、LLM 越狱、没时间睡觉了、自建信息聚合、Copy Book、docker run 转 compose等。
---

## 关于本刊

> 这是猫鱼周刊的第 25 期，本系列每周日更新，主要内容为每周收集内容的分享，同时发布在
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

### 可能是全网第一个粤语 Qwen/从零开始的 LLM 微调教程

[原文链接](https://blog.stv.lol/archives/88/)

在还在用 BERT 的时代，要做 finetune 除了要构建数据集，还要写一大堆训练代码。现在完全不一样了，通过现成的脚本，只要准备好数据就可以进行微调了。从这篇文章看来，现在微调一个 LLM 主要有以下几个步骤：

- 准备好数据集，处理成 [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)的格式，当然了这一步多多少少还是要写一点清洗的代码。
- 租用 GPU，搭建环境。[Autodl](https://www.gpuhub.com) 或者一些主流的云服务厂商都有提供租用 GPU 的服务，最好提前了解下你想微调的模型有多少参数，对应需要多大的显存去运行，首先应该满足显存需求，然后才是训练速度。关于训练速度，常见显卡的训练速度可以参考[这个网站](https://tensordock.com/benchmarks)。
- 微调。这一步就是执行脚本，调参这些。如果对里面的学习率、训练轮数、梯度、损失之类的名词觉得陌生，可以去看看吴恩达的这个[教程](https://www.youtube.com/playlist?list=PLkDaE6sCZn6FNC6YRfRQc_FbeQrF8BwGI)。

### 不用数学，解释 LLM 的原理

[原文链接](https://blog.miguelgrinberg.com/post/how-llms-work-explained-without-math)

一篇非常好的入门文章，解释清楚了 token、LM、上下文窗口、幻觉等等的概念。我觉得对我来说比较新鲜的是 `temperature`, `top_p`, `top_k`, `num_tokens` 的实际意义。这几个参数叫 `hyperparameter`，一般叫超参，又或者叫玄学参数，因为没法确定改变这几个参数对具体的输出有什么具体的影响。

这篇科普文章主要目的是把 LLM 的原理解释清楚，它不是魔术，它也没有“思维”。作者认为 LLM 是实用的，但是在使用中一定要注意验证输出是否符合事实。这跟我之前在 [vol. 010](https://ameow.xyz/archives/weekly-010) 中的想法大致相同。

### 离线使用 Git

[原文链接](https://www.gibbard.me/using_git_offline/)

Git 是一个分布式版本管理系统，我们平常通过 GitHub 或者私有的 GitLab 等来与其他人进行协作。但其实 Git 可以不通过网络使用，可以使用 U 盘、硬盘甚至 CD、DVD 这样的介质来进行协作。操作非常简单，只需要把 remote 设成一个路径即可（某种程度上，可以说 URL，因为平常我们是通过 `ssh` 或 `http` 协议来访问 remote。

这篇文章属于是有点冷知识型，但是算得是软件工程中“抽象”的范例。管你具体是什么介质，它都是一个 remote，只要你的介质有对应的实现，就可以正常使用 Git 的其他功能。优雅，太优雅了！

### Apple Watch Terminal 风格表盘

[原文链接](https://anotherdayu.com/2024/5755/)

![image.png](https://img.ameow.xyz/202405191725837.png)

命令行风格的 Apple Watch 表盘。这个其实早就在小红书之类的上面见过，但是以前的项目基本都过时了，作者重新折腾了一个。总体来说还是很 fancy 的，就是不知道会不会很费电？

## 项目

### LLM 越狱

[![elder-plinius/L1B3RT45 - GitHub](https://gh-card.dev/repos/elder-plinius/L1B3RT45.svg)](https://github.com/elder-plinius/L1B3RT45)

[项目地址](https://github.com/elder-plinius/L1B3RT45)

所谓的“越狱”就是指通过一些 prompt 欺骗 LLM，来绕过内容过滤器等。具体可以看看[这个网站](https://learnprompting.org/docs/prompt_hacking/intro)。

### 没时间睡觉了

[![JadyXuan/NTTS - GitHub](https://gh-card.dev/repos/JadyXuan/NTTS.svg)](https://github.com/JadyXuan/NTTS)

[项目地址](https://github.com/JadyXuan/NTTS)

华为发布会 `time.sleep(6)` 事件的整活，看的时候还只有去掉输出中的 `time.sleep` 的功能，现在又加了一个解决 `确定性时延` 的功能，遥遥领先！

### 自建信息聚合

[![glanceapp/glance - GitHub](https://gh-card.dev/repos/glanceapp/glance.svg)](https://github.com/glanceapp/glance)

[项目地址](https://github.com/glanceapp/glance)

![image.png](https://img.ameow.xyz/202405191740414.png)

可以把 RSS 源、HN、Youtube、股票、日历等等信息聚合在一个面板上。

## 工具/网站

### Copy Book —— 常见网站文案

[网站链接](https://copybook.me/)

![image.png](https://img.ameow.xyz/202405191743473.png)

产品经理福音。如果你不知道网站上一些常用的提示语该怎么写，可以直接从这里复制。

可惜网站不提供 i18n 翻译，不然可以减少很多不规范的产品文案翻译。

### docker run 转 compose

[网站链接](https://www.composerize.com/)

![image.png](https://img.ameow.xyz/202405191746900.png)

在 [dockge](https://github.com/louislam/dockge) 中，有个很有意思的功能就是，拿一条 `docker run`，会帮你转成 compose 文件，来启动。这个网站提供了一个独立的这个功能。

总的来说，用 `docker compose` 比直接 `docker run` 要更方便，就算只有一个 pod，用 compose 能把命令中开放端口、挂载路径、环境变量等落到文件中，在更新版本时，只用改一下文件中的镜像版本，重启即可。在之前，我的方式是 `history` 一下找回之前的参数，太麻烦了。

## 最后

本周刊已在 [GitHub](https://github.com/LeslieLeung/cat-fish-weekly) 开源，欢迎 star。同时，如果你有好的内容，也欢迎[投稿](https://github.com/LeslieLeung/cat-fish-weekly/issues/new?assignees=LeslieLeung&labels=&projects=&template=recommendations.md)。

另外，我建了一个交流群，欢迎入群讨论或反馈。

![461716112263_.pic.jpg](https://img.ameow.xyz/202405191751641.jpg)
