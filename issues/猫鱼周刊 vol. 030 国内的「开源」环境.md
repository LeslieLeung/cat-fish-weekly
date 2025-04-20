---
issue: 31
date: 2024-06-30
intro: 猫鱼周刊第31期，内容包括CSDN旗下的GitCode在批量搬运GitHub项目并竞争，希腊将实行六天工作制，还有两个开源项目推荐：opensource-lighthouse和open_source_team。还介绍了The Apple Wiki和endoflife.date这两个网站。
---

## 关于本刊

> 这是猫鱼周刊的第 31 期，本系列每周日更新，主要内容为每周收集内容的分享，同时发布在
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

![DSC00594.jpg](https://img.ameow.xyz/202406301719986.jpg)

摄于深圳沙井清平古墟。烈日下阳光打在纯白色的外墙上，蓝色的天空，和阴影面的墙体以及几个点缀的遮阳篷形成对比，像是壁纸。

沙井的商业化不是很严重，还很大情况下保留了古村落的特点，旧旧的房子，窄窄的街巷，村民聚集在树头或凉亭中吹水。就算是周末去人也不多（除了万景楼很多人在拍照），其他地方都很适合徒步探索。

## 文章

### CSDN 旗下的 GitCode 正在批量搬运 Github 开源项目并为开发者创建主页

[原文链接 1](https://www.landiannews.com/archives/104662.html)
[原文链接 2](https://www.landiannews.com/archives/104677.html)

这是两条前后连续的新闻。tl;dr:

> CSDN 旗下的代码托管平台 GitCode 正在批量搬运 Github 上的开源项目并为开发者创建主页，甚至「贴心」的将原始项目中的 readme 文件中的 Github 地址都替换为 GitCode。与此同时 CSDN 也在批量替换站内文章中提到的 Github 地址，让用户通过搜索引擎进入 CSDN 后也跳转到 GitCode。

> 大量开发者前往 Gitcode 要求删除账号和项目，但要想删除开发者必须使用自己的 Github 账号授权登录 Gitcode 创建账号并完成验证，接管项目后才可以操作包括删除项目。但即便是开发者忍心拿着 Github 账号授权登录了，也只能删除项目内容，Gitcode 仍然会保留项目名和开发者名作为占位符，至少目前是无法彻底删除的。

我自己的项目没被搬运，看来是看不上我的。不过我就这个事情，问了一下 GPT，作为个人开发者，只能从「著作权」和「开源协议」上出发进行维权，但是一般的开源项目并不会申请著作权，开源协议一般也只要求开发源码和保留原作者信息等，不限制发表的平台。当然，在公司层面（例如 GitHub 等）可以提起「不正当竞争」的诉讼，且不说 GitHub 在国内并没有运营实体，上头对 GitHub 的态度有如当年谷歌，说不定什么时候 GitCode 就顺势在国内取代 GitHub 了（就像当年的百度）。

很显然 CSDN 是有备而来，还伙同了华为云。如果你要删除自己被搬运的项目，需要先注册 GitCode 平台，过程不但要手机号认证（相当于实名）、绑定 GitHub 账号（相当于 GitHub 账号也实名了，细思极恐）。另外，在注册的过程中，需要同时同意 GitCode 和华为云的隐私协议。

GitCode 这个平台的存在至少是有以下两个影响：一是恶心了一些真的在做开源的开发者，尤其是国内的开发者（在 GitHub 上活跃开发有意义的项目的中国开发者，在中国技术群体里面真的不多）；二是蒙蔽、至少是恶化了多数中国开发者的信息获取渠道，通过 SEO 优化等方式（CSDN 老强项了）把多数国内开发者引流到一个劣质的平台。

对一个开发者来说，能做的就是不再使用这些恶心平台。在 2013 年的时候，陈皓就在 CoolShell 写过一篇[文章](https://coolshell.cn/articles/9308.html)杯葛（boycott）百度，直到现在，这个弹窗还在 CoolShell 的网站上挂着，如果你从百度进入 CoolShell 就会有弹窗提醒你不要使用百度。虽然我没有陈皓的影响力，但我建议大家不要使用 GitCode 及其他一些 CSDN 名下的产品（它名下竟然还有一些云服务）。

### 希腊即将实施六天工作制

[原文链接](https://greekcitytimes.com/2024/06/20/greece-six-day-work-week/)

标题听起来骇人听闻：欧洲不是不加班吗？事实上，六天工作制是用来解决一些需要连续或 24 小时工作的工种，保护劳动者权益的，并不适用全部的人。这个问题的背景是，一些公司依赖连续的运作（例如工厂流水线），但目前五天工作制使得一些劳动者必须进行「未申报的劳动」（加班）。因此政府开放一些公司去申请实行六天工作制，并且给劳动者开出更高的工资。

但也不是想六天就可以六天，需要满足以下的条件：

- 政府雇员等不属于持续运转的商业会被排除。
- 雇佣者必须提前通知员工，且提前在政府备案。
- 周六班次需要增加 40%薪水，如果是假日，则是 115%。
- 周六班次只能工作 8 个小时，且必须严格记录时间。

P.S. 希腊的每周平均工时为 41，欧盟平均为 37.5，希腊位居欧盟第一。

## 项目

### opensource-lighthouse

[![LeslieLeung/opensource-lighthouse - GitHub](https://gh-card.dev/repos/LeslieLeung/opensource-lighthouse.svg)](https://github.com/LeslieLeung/opensource-lighthouse)
[项目地址](https://github.com/LeslieLeung/opensource-lighthouse)

我最近做了一个新项目，统计了一些国内外「大厂」的开源组织及项目。我有一些愿景：

- 帮助诸位了解在开源社区各家大公司的参与情况，提供一个好项目的整合。
- 促进国内的「大厂」在开源上有更多的投入，贡献更多能做到「主流」且「国际化」的项目。

![CleanShot 2024-06-30 at 17.44.35@2x.png](https://img.ameow.xyz/202406301744736.png)

目前收集了每个公司的项目数、近半年内活跃项目数、总 Star 数，语言 Top 3 等信息，也有每个公司具体的项目和情况。后续可能会增加一些可视化、数据分析等。近期应该也会写一篇文章对此做一些分析和评论，感兴趣可以关注一下。

### open_source_team

[![niezhiyang/open_source_team - GitHub](https://gh-card.dev/repos/niezhiyang/open_source_team.svg)](https://github.com/niezhiyang/open_source_team)

[项目地址](https://github.com/niezhiyang/open_source_team)

我项目灵感的来源。这个项目收集了很多国内团队的开源地址，但是已经一段时间没有更新了。

## 工具/网站

### The Apple Wiki

[网站地址](https://theapplewiki.com)

一个关于苹果公司的 Wiki，收录了很多苹果的软硬件产品。例如苹果有一个域名 `guzzoni.apple.com`，单独来看 `guzzoni` 并不是苹果的产品，但原来它属于 [Siri 协议](https://theapplewiki.com/wiki/Siri_Protocol)的一部分。Guzzoni 是 Siri 创始人的名字，而苹果是收购的 Siri。

### endoflife.date

[网站地址](https://endoflife.date/)

软硬件都是有生命周期的。一般都会经历活跃开发、安全更新、不再支持这么几个阶段。这个网站收集了常见软硬件的生命周期。

![image.png](https://img.ameow.xyz/202406301752173.png)

我发现，一些比较新的语言支持时间都很短，例如 Go 只有一年，Kotlin 只有半年，而 Rust 只有一到两个月。相比之下，Python 有一年左右的「活跃支持」和三年的「安全支持」，Java 甚至有长达十几年的支持。

## 最后

本周刊已在 [GitHub](https://github.com/LeslieLeung/cat-fish-weekly) 开源，欢迎 star。同时，如果你有好的内容，也欢迎[投稿](https://github.com/LeslieLeung/cat-fish-weekly/issues/new?assignees=LeslieLeung&labels=&projects=&template=recommendations.md)。如果你觉得周刊的内容不错，可以分享给你的朋友，让更多人了解到好的内容，对我也是一种认可和鼓励。（或许你也可以通过[爱发电](https://afdian.net/a/3verest)请我喝杯咖啡）

另外，我建了一个交流群，欢迎入群讨论或反馈，可以通过文章头部的联系邮箱私信我获得入群方式。
