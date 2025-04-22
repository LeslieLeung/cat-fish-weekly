---
issue: 10
date: 2024-01-21
---

- [关于本刊](#%E5%85%B3%E4%BA%8E%E6%9C%AC%E5%88%8A)
- [文章](#%E6%96%87%E7%AB%A0)
  - [Go 1.22 新特性](#Go%201.22%20%E6%96%B0%E7%89%B9%E6%80%A7)
  - [Go 1.22 新特性前瞻](#Go%201.22%20%E6%96%B0%E7%89%B9%E6%80%A7%E5%89%8D%E7%9E%BB)
  - [Go 1.22 Release Notes(Draft)](<#Go%201.22%20Release%20Notes(Draft)>)
  - [技术写作学习路线](#%E6%8A%80%E6%9C%AF%E5%86%99%E4%BD%9C%E5%AD%A6%E4%B9%A0%E8%B7%AF%E7%BA%BF)
  - [我们是怎么丢失了 54K star 的](#%E6%88%91%E4%BB%AC%E6%98%AF%E6%80%8E%E4%B9%88%E4%B8%A2%E5%A4%B1%E4%BA%86%2054K%20star%20%E7%9A%84)
- [项目](#%E9%A1%B9%E7%9B%AE)
  - [Portkey-AI/gateway](#Portkey-AI/gateway)
  - [bloomberg/memray](#bloomberg/memray)
- [工具/网站](#%E5%B7%A5%E5%85%B7/%E7%BD%91%E7%AB%99)
  - [PHP 沙箱](#PHP%20%E6%B2%99%E7%AE%B1)
  - [几个 PaaS 平台](#%E5%87%A0%E4%B8%AA%20PaaS%20%E5%B9%B3%E5%8F%B0)
- [想法](#%E6%83%B3%E6%B3%95)
  - [马太效应与先发优势](#%E9%A9%AC%E5%A4%AA%E6%95%88%E5%BA%94%E4%B8%8E%E5%85%88%E5%8F%91%E4%BC%98%E5%8A%BF)

## 关于本刊

> 这是猫鱼周刊的第 10 期，本系列每周日更新，主要内容为每周收集内容的分享，同时发布在
>
> 博客：[阿猫的博客-猫鱼周刊](https://ameow.xyz/categories/weekly)
> RSS：[猫鱼周刊](https://ameow.xyz/feed/categories/weekly.xml)
> 邮件订阅：[猫鱼周刊](https://quaily.com/ameow)
> 微信公众号：[猫兄的和谐号列车](http://img.ameow.xyz/202401141448662.png)
> Discord：[猫兄的和谐号高铁](https://discord.gg/5G5Nbtuz)
> 私信：[leslieleung@pm.me](mailto:leslieleung@pm.me)

## 文章

### Go 1.22 新特性

[原文链接](https://medium.com/@yuseferi/new-features-that-you-should-expect-in-go-1-22-91ae3ec0da95)

Go 1.22 预计将于 2024 年 2 月份正式发布。Go 的 for loop 一直有个坑，如果在 for 循环中使用循环变量，会出现在多个协程中引用了同一个变量的 bug，这个是大家都很关心的特性。

（这个 bug 如下）

```go
// go 1.21
values := []int{1, 2, 3, 4, 5}
for _, val := range values {
    go func() {
    fmt.Printf("%d ", val)
    }()
}
// Result : 5 5 5 5 5

// go 1.22
values := []int{1, 2, 3, 4, 5}
for _, val := range values {
    go func() {
    fmt.Printf("%d ", val)
    }()
}
// Result: 5 3 4 1 2
```

### Go 1.22 新特性前瞻

[原文链接](https://tonybai.com/2023/12/25/go-1-22-foresight/)

一篇中文的博客，与第一篇英文的侧重点各有不同。

### Go 1.22 Release Notes(Draft)

[原文链接](https://tip.golang.org/doc/go1.22)

官方的 Release Note，应该是最全的 1.22 新特性以及变化。

### 技术写作学习路线

[原文链接](https://roadmap.sh/technical-writer)

![](http://img.ameow.xyz/202401211702381.png)

之前就介绍过 [roadmap](https://roadmap.sh/)这个网站，上面有一系列常见职业/岗位的学习路线。最近发现上新了一个技术写作的路线。

### 我们是怎么丢失了 54K star 的

[原文链接](https://httpie.io/blog/stardust)

HTTPie 项目因为作者不小心把仓库设成了 private 导致丢失了所有的 star，这件事情发生在 2022 年了，当时这篇文章也传得很火。文章里提出了几个教训来避免这类事情发生：

- 改进 UI/UX 设计
- 不要使用硬删除
- 不要太天真地信任 GitHub 与开发者的关系

对于 HTTPie 团队，结局不是特别好，GitHub 的态度一般，没有帮他们恢复（作者认为 GitHub 完全是有能力做到的，因为他们给自己恢复过，后来也给别的团队恢复过），只发了一条[推文](https://twitter.com/github/status/1493329046708670475)。

这件事情的后续也比较有意思。首先是这个项目现在（2024 年 1 月）已经恢复到 30K star 了，说明社区的力量还是很强大的；其次是 GitHub 真的修改了他们的 UI，使得现在删除前能更好知道自己的操作有什么具体的影响；最后是另外一个被删除的团队的 star 得到了 GitHub 的恢复。

![](https://img.ameow.xyz/202401211733871.png)

## 项目

### Portkey-AI/gateway

[![Portkey-AI/gateway - GitHub](https://gh-card.dev/repos/Portkey-AI/gateway.svg?fullname=)](https://github.com/Portkey-AI/gateway)

一个 AI 网关，类似 one-api，都支持通过 OpenAI 的接口对接到不同 AI 服务。区别是支持负载均衡、回落和自动重试，比起 one-api 要更加稳定。

### bloomberg/memray

[![bloomberg/memray - GitHub](https://gh-card.dev/repos/bloomberg/memray.svg?fullname=)](https://github.com/bloomberg/memray)

![](http://img.ameow.xyz/202401211726162.png)

一个 Python 的内存分析工具，可以分析出火焰图等等，帮助优化内存占用。

## 工具/网站

### PHP 沙箱

网站链接：[PHP Sandbox - Execute PHP code online through your browser](https://onlinephp.io/)

![](https://img.ameow.xyz/202401211742925.png)

之前一期我提到过一些在线的代码运行网站，最近又找到一个可以“对比多个 PHP 版本间运行差异”的，可以勾选多个 PHP 版本，同时运行，对比他们的差异。PHP 8 之后等于的判断与之前的版本有比较大的差别，在这个网站上就能方便地上手试试了。

### 几个 PaaS 平台

- [Zeabur - Deploying your service with one click](https://zeabur.com?referralCode=LeslieLeung)
- [Sealos: 专为云原生开发打造的以 K8s 为内核的云操作系统](https://sealos.run/)
- [Cloud Application Hosting for Developers | Render](https://render.com/)

几个对 Hobby 级别开发者非常友好的 PaaS 平台（类似 Vercel），都支持多种语言或基于容器部署。他们的部署流程和特性都很类似：

- （Zeabur）根据 Dockerfile 构建或从公共仓库选取镜像
- 使用镜像部署
- 提供修改环境变量、日志查看等功能
- 提供二级域名或自定义域名（使用 CNAME）
- 按照实际使用 CPU 和内存等资源收费，提供一定免费额度

## 想法

### 马太效应与先发优势

马太效应典出《马太福音》，原文为：

> **凡有的，还要加给他，叫他有余；凡没有的，连他所有的也要夺去。**

1968 年，美国社会学家罗伯特·莫顿提出这个术语用以概括一种社会心理现象：“相对于那些不知名的研究者，声名显赫的科学家通常得到更多的声望，即使他们的成就是相似的，同样地，在同一个项目上，声誉通常给予那些已经出名的研究者，例如，一个奖项几乎总是授予最资深的研究者，即使所有工作都是一个研究生完成的。”

在 LLM 领域，OpenAI 的 GPT 不一定是性能最好的，但是却是最出圈的。由于它的先发优势，大家谈起 LLM 、AI 等等都会先想起 ChatGPT；同时，在别的公司推出自己的 LLM 产品后，由于 OpenAI 的生态已经有完善的 SDK 等，其他公司的产品也或多或少将自己的 API 向 OpenAI 靠近；或就是有开发者做了兼容其他 LLM，但使用 OpenAI 接口格式的网关。
