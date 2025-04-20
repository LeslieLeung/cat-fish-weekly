---
issue: 9
date: 2024-01-14
---

- [关于本刊](#%E5%85%B3%E4%BA%8E%E6%9C%AC%E5%88%8A)
- [头条](#%E5%A4%B4%E6%9D%A1)
- [文章](#%E6%96%87%E7%AB%A0)
  - [12 要素 App （12 Factors App）](#12%20%E8%A6%81%E7%B4%A0%20App%20%EF%BC%8812%20Factors%20App%EF%BC%89)
- [项目](#%E9%A1%B9%E7%9B%AE)
  - [message-pusher](#message-pusher)
  - [novu](#novu)
  - [ntfy](#ntfy)
  - [bark](#bark)
  - [heimdallr](#heimdallr)
  - [linkwarden](#linkwarden)
- [工具/网站](#%E5%B7%A5%E5%85%B7/%E7%BD%91%E7%AB%99)
  - [最佳平替](#%E6%9C%80%E4%BD%B3%E5%B9%B3%E6%9B%BF)
  - [mdnice](#mdnice)
- [想法](#%E6%83%B3%E6%B3%95)
  - [大流量高日活的网站](#%E5%A4%A7%E6%B5%81%E9%87%8F%E9%AB%98%E6%97%A5%E6%B4%BB%E7%9A%84%E7%BD%91%E7%AB%99)
- [加餐](#%E5%8A%A0%E9%A4%90)

## 关于本刊

> 这是猫鱼周刊的第 9 期，本系列每周日更新，主要内容为每周收集内容的分享，同时发布在
>
> 博客：[阿猫的博客-猫鱼周刊](https://ameow.xyz/categories/weekly)
> RSS：[猫鱼周刊](https://ameow.xyz/feed/categories/weekly.xml)
> 邮件订阅：[猫鱼周刊](https://quaily.com/ameow)
> 微信公众号：[猫兄的和谐号列车](http://img.ameow.xyz/202401141448662.png)
> Discord：[猫兄的和谐号高铁](https://discord.gg/5G5Nbtuz)
> 私信：[leslieleung@pm.me](mailto:leslieleung@pm.me)

## 头条

我自己的通知服务 [heimdallr](https://github.com/LeslieLeung/heimdallr)最近在进行一次比较大的重构，目的是让其符合 12 要素 App 以及支持多个通知渠道配置等，因此也调研了很多热门的通知服务和他们的实现。这期基本围绕通知服务展开。

## 文章

### 12 要素 App （12 Factors App）

[原文链接](https://12factor.net/) | [中文翻译](https://12factor.net/zh_cn/)

这篇文章是在思考我的通知聚合服务的配置文件要如何改版，在查阅使用环境变量作为配置的实践时找到的。阅读下来之后发现，这就是现在很多开源项目在遵循的“最佳实践”。这套实践适用于任意语言和后端服务（数据库、消息队列、缓存等）开发的应用程序。

虽然我觉得文章的内容非常“现代”，但其实文章最后一次更新已经是 2017 年，看来好的工程师一定是有前瞻性的。（文章的中文翻译有些许别扭，如果有能力，建议还是阅读英文原文）

## 项目

### message-pusher

[![songquanpeng/message-pusher - GitHub](https://gh-card.dev/repos/songquanpeng/message-pusher.svg?fullname=)](https://github.com/songquanpeng/message-pusher)

one-api 的作者做的消息推送聚合服务，后端使用 Go，因此非常轻量。通知方式方面支持国内常见的 IM（QQ、企业微信、飞书、钉钉、Bark、TG、Discord 等），也支持聚合一次推送到多个渠道的功能。

### novu

[![novuhq/novu - GitHub](https://gh-card.dev/repos/novuhq/novu.svg?fullname=)](https://github.com/novuhq/novu)

通知聚合服务。不过通知方式主要是支持的国外的服务，国外服务商的短信/电话基本是打不进国内的。

### ntfy

[![binwiederhier/ntfy - GitHub](https://gh-card.dev/repos/binwiederhier/ntfy.svg?fullname=)](https://github.com/binwiederhier/ntfy)

一个通知推送服务。特点是客户端支持 iOS/Android，甚至还支持桌面端，应该是支持自建的方案里面支持最全的一个。

### bark

[![Finb/bark-server - GitHub](https://gh-card.dev/repos/Finb/bark-server.svg?fullname=)](https://github.com/Finb/bark-server)

也是通知推送服务，应该是 iOS 平台上体验最好的一个，我自用已经两三年了。缺点是只支持 iOS，甚至不支持 macOS。

### heimdallr

[![LeslieLeung/heimdallr - GitHub](https://gh-card.dev/repos/LeslieLeung/heimdallr.svg?fullname=)](https://github.com/LeslieLeung/heimdallr)

一个我自己做的通知聚合服务。我对通知推送服务的理解是它最好是一个轻量且可靠的服务，最好运行成本特别低，甚至零成本。因此它不但支持常见的 Docker 部署，还支持部署到腾讯云、阿里云等的云函数上。同时，它的通知路由跟 Bark 的几乎一样，使得所有支持 Bark 的第三方服务基本都可以无缝切换成 heimdallr。

### linkwarden

[![linkwarden/linkwarden - GitHub](https://gh-card.dev/repos/linkwarden/linkwarden.svg?fullname=)](https://github.com/linkwarden/linkwarden)

一个开源可自建的书签管理、归档应用，可以作为 Cubox 的自建替代。

## 工具/网站

### 最佳平替

网站链接：[最佳平替 - 用更低价的搜索词购物](https://www.pingti.xyz/)

![](http://img.ameow.xyz/202401141527666.png)

属于“找个乐子”类型，不过目前网站日活很高。

### mdnice

网站链接：[墨滴 | 看颜值的文章社区](https://mdnice.com/)

基本上是 markdown 文章转微信公众号发布最好的方案了。

微信不支持发送带有外链（a 标签）的内容，只能通过纯文本分享 URL，这个工具带有外链转脚注的功能，能够不花时间重新排版就能得到可以发布的内容。

网站有开源，因此如果不想看广告也可以自己部署一份。

## 想法

### 大流量高日活的网站

上周我在即刻发表过一个疑惑：是要重视内容质量还是重视推广/宣传。我发现我其实是误解了当时图中 hook 的意义，hook 不只是简单的宣传，是指内容引起观众的注意，并吸引观众点击的意思。近期有很多例子可以佐证这个道理：

- 最佳平替：命中了“平替”、“消费降级”的关键词，虽然不具有非常强的实用价值，但是很吸引人，能引起人好奇。
- “失业产品经理”做的 IP 站：命中了“失业”、“产品经理”、“GPT”的关键词，会让人好奇这几个组合能碰撞出怎么样的火花。
- 网页空调、风扇：猎奇心理，打开的网页只是一个动画，点击开关之后有空调滴的一生。

这些网站的内容从技术上来说都没什么特别，内容也不是什么特别有实用价值或者说“营养”，但是单纯利用了好奇心，不用打磨内容，只需要一个好的 hook 就可以获得大量的流量。

还有一种网站也可以达到很高的流量和日活，同时又不需要花时间创作内容，就是导航/消息聚合站。这种站最大的特色是，如果你做得比较全，用户粘性实际上是比较高的（在我自己搭建 dashy 作为自己的导航之前，我一直使用一个叫 marstab 的自定义导航页，用了大概一两年）；其次，不需要自己创造内容，只要维护好消息源，就会有用户不停地把你的网站作为入口去看其他的内容，如果筛选的内容优质，其实也做了很有意义的事情（又顺便赚到了钱）。

## 加餐

我的博客里一直有一个【收藏夹】的专栏，我希望是把一些我见过的好网站/文章按照专题的方式进行分享。之前一直没找到比较好的载体，直到现在找到了 linkwarden 这个项目，它可以建公开的 collection。以下是两个试水的 collection。

- Git 专题：[All About Git](https://link.niuma.dev/public/collections/4)
- 在线开发工具专题：[Online Dev Tools](https://link.niuma.dev/public/collections/1)
