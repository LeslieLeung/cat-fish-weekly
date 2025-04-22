---
issue: 14
date: 2024-02-18
---

- [关于本刊](#%E5%85%B3%E4%BA%8E%E6%9C%AC%E5%88%8A)
- [文章](#%E6%96%87%E7%AB%A0)
  - [函数式编程初探](#%E5%87%BD%E6%95%B0%E5%BC%8F%E7%BC%96%E7%A8%8B%E5%88%9D%E6%8E%A2)
  - [教程：上手泛型](#%E6%95%99%E7%A8%8B%EF%BC%9A%E4%B8%8A%E6%89%8B%E6%B3%9B%E5%9E%8B)
  - [Go 中的函数式编程](#Go%20%E4%B8%AD%E7%9A%84%E5%87%BD%E6%95%B0%E5%BC%8F%E7%BC%96%E7%A8%8B)
  - [Go 函数式编程：从一个 for 循环讲起](#Go%20%E5%87%BD%E6%95%B0%E5%BC%8F%E7%BC%96%E7%A8%8B%EF%BC%9A%E4%BB%8E%E4%B8%80%E4%B8%AA%20for%20%E5%BE%AA%E7%8E%AF%E8%AE%B2%E8%B5%B7)
- [项目](#%E9%A1%B9%E7%9B%AE)
  - [samber/lo](#samber/lo)
  - [IBM/fp-go](#IBM/fp-go)
- [工具/网站](#%E5%B7%A5%E5%85%B7/%E7%BD%91%E7%AB%99)
  - [ffmpeg-online](#ffmpeg-online)
  - [unlimited:waifu2x](#unlimited:waifu2x)
- [最后](#%E6%9C%80%E5%90%8E)

## 关于本刊

> 这是猫鱼周刊的第 14 期，本系列每周日更新，主要内容为每周收集内容的分享，同时发布在
>
> 博客：[阿猫的博客-猫鱼周刊](https://ameow.xyz/categories/weekly)
>
> RSS：[猫鱼周刊](https://ameow.xyz/feed/categories/weekly.xml)
>
> 邮件订阅：[猫鱼周刊](https://quaily.com/ameow)
>
> 微信公众号：[猫兄的和谐号列车](http://img.ameow.xyz/202401141448662.png)
>
> Discord：[猫兄的和谐号高铁](https://discord.gg/5G5Nbtuz)
>
> 私信：[leslieleung@pm.me](mailto:leslieleung@pm.me)

## 文章

### 函数式编程初探

[原文链接](https://www.ruanyifeng.com/blog/2012/04/functional_programming.html)

出自阮一峰老师之笔，一篇概述性的文章，介绍了函数式编程的定义、特点等。

### 教程：上手泛型

[原文链接](https://go.dev/doc/tutorial/generics)

Go 官方的一篇介绍泛型的文章。因为 Go 是一个强类型静态语言，因此要实现类型安全的函数式编程，必须了解一下泛型。（如果愿意在类型安全上多下功夫，也可以用反射实现，可以看陈皓老师的[这篇文章（极客时间付费专栏）](https://time.geekbang.org/column/article/332606)）

### Go 中的函数式编程

[原文链接](https://bitfieldconsulting.com/golang/functional)

一篇讲述在 Go 中使用 MapReduce 方式进行函数式编程的文章。正是它启发了我写了以下这篇文章。

### Go 函数式编程：从一个 for 循环讲起

[原文链接](https://ameow.xyz/archives/go-functional-programming-intro)

函数式编程在大前端中应用比较广，但是在后端中（至少在我工作中）比较少见。诚然，我认为最大的拦路虎是后端的业务逻辑很复杂，业务代码繁重，而且大家习惯于指令式编程的思维，转变到声明式编程，对程序员的心智要求比较高。

我尝试用 Filter 这个函数式编程的一小部分特性，来说明一份代码如何从大家熟知的指令式编程，演化至函数式编程，来实现以下目标：

- 提升代码的可复用性，以及对需求变更、技术变更的快速适应
- 在不需要修改业务逻辑的情况下，利用并发特性，优化 IO 密集场景的性能

## 项目

### samber/lo

[![samber/lo - GitHub](https://gh-card.dev/repos/samber/lo.svg?fullname=)](https://github.com/samber/lo)

一个利用泛型来实现例如 map，filter 等功能的函数式编程框架，发展两年了，星星也非常多。我认为最大的缺点是没有实现 pipeline，只支持 MapFilter 这种。

### IBM/fp-go

[![IBM/fp-go - GitHub](https://gh-card.dev/repos/IBM/fp-go.svg?fullname=)](https://github.com/IBM/fp-go)

另一个函数式编程框架。不过这个相对比较学术派一点，目前也是在积极开发阶段。缺点是没有上一个容易上手，需要多了解一点函数式编程的概念。

## 工具/网站

### ffmpeg-online

网站链接：[ffmpeg-online](https://ffmpeg-online.vercel.app)

![](https://img.ameow.xyz/202402170217679.png)

一个使用 [ffmpeg.wasm](https://github.com/ffmpegwasm/ffmpeg.wasm) 的在线 demo，可以在浏览器上运行 ffmpeg。ffmepg 算是一个我觉得非常适合 wasm 的应用场景，把计算密集的负载放到边缘计算，一来减少了对服务器性能的依赖，二来对隐私也是有利的（数据仅在客户端本地处理），三是消除了依赖安装、环境配置等等问题（对交付非常友好）。

### unlimited:waifu2x

网站链接：[unlimited:waifu2x](https://unlimited.waifu2x.net/)

![](https://img.ameow.xyz/202402170222544.png)

这是另外一个使用 wasm 的例子。[waifu2x](https://github.com/nagadomi/nunif)是一个图像超分算法，利用卷积神经网络来提升图像的分辨率。这里作者把训练出来的模型导出成 onnx 格式，利用 onnx-runtime 来在设备端运算。因此这个 unlimited (wasm) 的版本比服务器端版本多了模型、4x 倍数等等的功能，速度也明显更快。

## 最后

这期周刊撰写的时间还是在春节假期内，所以还是再祝大家新年快乐，工作顺利，生活顺心。

这期的内容略少，且只有两个主题，一个是 Go 和函数式编程，另一个就是 wasm（还是炒的之前存的冷饭）。陪家人的时间比较多，也不想在假期想太多工作相关的事情，好好放松一下，所以就选了一个自己感兴趣的方面做了点研究。
