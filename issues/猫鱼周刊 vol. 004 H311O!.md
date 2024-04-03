---
issue: 5
date: 2023-12-10
---

## 文章

### 2023 H2 Go 开发者调查结果（[原文](https://go.dev/blog/survey2023-h2-results)）

Google 的 Go 团队做的半年度 Go 开发者调查。最近很多组织/公司都在释出年度的调查报告，都挺有意思。

Go 这边的调查总体跟我印象中很符合，一般大家还是用于做后端开发/云原生相关的开发，而且大家也很喜欢用 Go 来做自己的 side project，写起来也觉得很愉悦，今年大家也喜欢用/开发 AI。我比较好奇的是有 9% 的人竟然使用 Go 开发桌面端/GUI 程序，他们是在用什么框架，是写的纯 Go 吗？

### Leet/1337（[原文](https://en.wikipedia.org/wiki/Leet)）

在外网冲浪，经常看到有的人用户名中有有一两个数字，一直没找到这个“不成文”的替换规则。正好在 domainhacks 那里看到 1337 Hack，一番搜索，终于解开了这个好奇已久的谜题。

一个说法是，当时的 hacker （不一定是黑客哈）为了避免 BBS 的关键词检测，而采用的一种用数字+字母混淆单词的拼写方式。这种习惯现在在安全领域依旧很常见。有点类似我们简体中文文化中的火星文、同音字替换、字母替换、拆字等。

## 项目

### [hipstersmoothie/obsidian-plugin-toc](https://github.com/hipstersmoothie/obsidian-plugin-toc)

一个给 obsidian 生成目录（TOC, table of contents）的插件。之前有朋友反馈，周刊缺乏一个目录，不方便查看，这就可以加上了。

### [besscroft/kamera](https://github.com/besscroft/kamera)

一款专供摄影佬使用的记录网站，支持常见的图片格式，可以读取 EXIF 信息，管理维护图片，瀑布流展示查看图片。 兼容 S3 API、支持 CDN 配置。首页精品照片展示，子页分类展示等功能。 基于 Nuxt 3 开发，支持一键部署，无需单独后端。

可以基于 vercel 和 supabase 部署，四舍五入白嫖！

### [go-gost/gost](https://github.com/go-gost/gost)

新科技？插个眼。

### [names-generator.go](https://github.com/moby/moby/blob/master/pkg/namesgenerator/names-generator.go)

新建 docker 容器的时候如果不指定名称就会生成一个由一个形容词+一个人名组成的随机名称，它的生成方式简单粗暴又有趣：一个形容词表，一个人名表（例如 `turing` Alan Turing , `lovelace` Ada Lovelace, `hawking` Stephen Hawking）等，从两个表中随机各拿一个单词出来拼接。特别地，这个生成器不会生成出 `boring_wozniak`。

```go
if name == "boring_wozniak" /* Steve Wozniak is not boring */ {
	goto begin
}
```

## 工具

### domainhacks 域名创意工具

官网链接：[Domainhacks.info](https://domainhacks.info/)

原理应该是通过一系列静态规则对输入的关键词进行处理，得出一系列域名创意。还可以检测域名是否已被注册。有一些还是挺实用的，例如 path hack 和 1337 hack。

![](http://img.ameow.xyz/202312080310876.png)

## 关于

> 这是猫鱼周刊的第 5 期，本系列每周日更新，主要内容为每周收集内容的分享，同时发布在
>
> 博客：[阿猫的博客-猫鱼周刊](https://ameow.xyz/categories/weekly)
> 掘金(beta)：[猫鱼周刊 - 3verest 的专栏 - 掘金](https://juejin.cn/column/7302415204927012918)
> 邮件订阅：[猫鱼周刊](https://quail.ink/ameow)
> Discord：[猫兄的和谐号高铁](https://discord.gg/5G5Nbtuz)
> 私信：[leslieleung@pm.me](mailto:leslieleung@pm.me)
