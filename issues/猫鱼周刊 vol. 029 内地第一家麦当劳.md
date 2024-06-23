---
issue: 30
date: 2024-06-23
intro: 猫鱼周刊的第30期，内容包括介绍深圳东门老街的麦当劳、剖析JOSE、Kubernetes中CPU的限制和请求、个人使用指南、jieplag项目和全球DNS检测。
---

## 关于本刊

> 这是猫鱼周刊的第 30 期，本系列每周日更新，主要内容为每周收集内容的分享，同时发布在
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

![DSC00437.png](https://img.ameow.xyz/202406231355815.png)

深圳东门老街的麦当劳，据说它是[内地第一家麦当劳餐厅](https://www.mcdonalds.com.cn/index/mcd/mcdonalds-china/mcd-in-china-2)。其实内部装修等都是很标准的麦当劳，餐牌等也很标准（还以为会有一些限定品种，脑洞大开了），唯一特别就是它有三层楼，据说有五百多个座位。这个巨大的发光 M 字几乎成了东门老街的一个地标，不少深圳人都能马上认出来这是东门的麦当劳。

这张照片来得也很巧，那天新买的黑柔滤镜刚到货，就拍到了这个巨大的发光 M 字，黄色和红色的光晕开，很有感觉。这有点像在游戏里刚获得新的道具，然后进入了一个教学关卡，让你试用（白给奖励）的感觉。

## 文章

### 剖析 JOSE

[原文链接](https://github.com/lestrrat-go/jwx/blob/develop/v2/docs/00-anatomy.md)

大家可能都听说过 JWT （JSON Web Token），它是一种身份验证方式，我觉得比较有特色的地方在：

- 它支持有效期以及自定义的验证字段等
- 支持签名，防止内容被篡改
- 服务端可以本地校验 JWT 的有效性，不需要网络请求（除非需要刷新公钥）
- 可以灵活地支持各种加解密算法

然而，JWT 其实只是 JOSE （Javascript Object Signing and Encryption）的一部分，JOSE 实际上由 5 个 RFC 规范组成，包括 JWS（签名）、JWE（加密）、JWK（密钥）、JWA（算法）和 JWT。

回到文章，这个作者做了一个包叫 [JWX](https://github.com/lestrrat-go/jwx)，把 JOSE 的各个部分都做进去了。这个包一开始看云里雾里的，直到看了这个「00-anatomy.md」，才发现原来作者把所有概念串讲了一下。

### 深入了解 Kubernetes 中 CPU 的 limit 和 request

[原文链接](https://www.datadoghq.com/blog/kubernetes-cpu-requests-limits/)

一篇还没读透但是迫不及待想分享的文章。在工作中不时会遇到需要调整部署的项目所需的资源，内存部分还好理解，但是 CPU 的我一直没摸透：假设我需要 0.5 核，系统怎么知道把 0.5 核的资源分配给我呢（不像硬盘或者内存，可以通过寻址划分）。实际上，Kubernetes 是通过划分时间片实现的，一些虚拟机或者 Docker 的实现方式也类似。具体来说，Kubernetes 通过  `CPU requests`  和  `CPU limits`  来管理和分配容器的 CPU 资源。比如，当你请求 0.5 核的 CPU 时，系统会确保你的容器在一定时间内使用到相当于半个 CPU 核心的时间片。

### 个人使用指南

[原文链接](https://futureforum.com/2022/07/15/personal-user-manual/)

文章写于 2022 年，正值远程办公兴起之时。个人使用指南（Personal User Mauals）是一个对自己的背景、价值观和交流风格的简短描述。在团队内部每人都要撰写并且交换自己的个人使用指南，帮助队友更好了解自己。

这个概念挺有意思，即刻上就有这个传统，很多人主页会置顶一条个人简介。感觉这个对沟通还是很有帮助的。

## 项目

### jieplag

[![thu-cs-lab/jieplag - GitHub](https://gh-card.dev/repos/thu-cs-lab/jieplag.svg)](https://github.com/thu-cs-lab/jieplag)
[项目地址](https://github.com/thu-cs-lab/jieplag)

清华大学开源的一个抄袭检测工具，用于检测代码的相似度，支持 C/C++、Rust、Python 等。可以本地运行，也可以作为服务端运行。

其灵感来源于斯坦福大学的 [Moss](https://theory.stanford.edu/~aiken/moss/)，也是一个代码抄袭检测工具，它支持的语言更多、更「传统」一些。

我有一个好奇的地方，OJ（online judge）基本上是高校编程机考的必备了，怎么没把抄袭检测集成进去？

## 工具/网站

### 全球 DNS 检测

[网站链接](https://dnschecked.com)

![image.png](https://img.ameow.xyz/202406231441459.png)

一个检测在全球各地 DNS 解析结果的网站。对一些大型的网站来说，会在全球各地设置不同的 DNS 解析，保证用户获得最佳的体验，当然这个操作也能用来干一些损害用户体验的事情（也叫 DNS 污染）。总之，要对 DNS 解析进行调试，这是一个不错的工具。

## 想法

### 周刊减产了吗

最近的几期，周刊都没有介绍很多内容（指条数），但其实周刊的内容总体还是比较充实，字数维持在 1500 字左右。回顾一下我之前对周刊内容的期望：

> 从这期开始，我尝试每一周都消化一下上一周往收藏夹里扔的内容，分享一些有趣的文章、网站，发表一些自己的评论，也会分享一些这周遇到的优秀开源项目。我的周刊只会分享一些我在冲浪中遇到的有趣的内容，不会像一些其他周刊一样照搬 GitHub Trending 或者追时下一些热门的内容。

> 周刊目前会注重于内容的创作，如果当期内容太少，我不会为了不断更而强行拼凑一些我自己没有认真消化过的内容；如果实在内容太少，那就留到下一周一起再发。
> 不会使用 AI 来辅助创作，包括其实我的整个博客的人类可读内容都不会使用 AI 辅助创作，但可能使用 AI 进行 SEO 优化等。

周刊走到第 30 期了，我觉得这也算是一个里程碑，回顾一下，基本达到了我自己的期望。我不会分享我没认真看过的文章/项目，比起一些「内参」形式的信息收集来说，我的周刊更像个人分享的集合。

最近的几期，你可能会发现以下这些变化：

- 代码相关的内容少了（我近期写的代码其实也不多，在往其他方向努力）
- 生活、趣味向的内容多了（人不可能只有工作吧？）

不管怎么样，周刊确实满足了我的分享欲。如果你对周刊有好的意见和建议，欢迎联系我或者在下面评论。

## 最后

本周刊已在 [GitHub](https://github.com/LeslieLeung/cat-fish-weekly) 开源，欢迎 star。同时，如果你有好的内容，也欢迎[投稿](https://github.com/LeslieLeung/cat-fish-weekly/issues/new?assignees=LeslieLeung&labels=&projects=&template=recommendations.md)。如果你觉得周刊的内容不错，可以分享给你的朋友，让更多人了解到好的内容，对我也是一种认可和鼓励。（或许你也可以通过[爱发电](https://afdian.net/a/3verest)请我喝杯咖啡）

另外，我建了一个交流群，欢迎入群讨论或反馈，可以通过文章头部的联系邮箱私信我获得入群方式。
