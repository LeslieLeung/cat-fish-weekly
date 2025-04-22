---
issue: 1
date: 2022-12-18
---

其实想写 newsletter 很久了，每周都会阅读、收藏很多文章，但“收集->整理->输出“这个流程最多只走到了整理——把所有文章往 Cubox 里一扔，最多打个标签就草草结束了。从这期开始，我尝试每一周都消化一下上一周往收藏夹里扔的内容，分享一些有趣的文章、网站，发表一些自己的评论，也会分享一些这周遇到的优秀开源项目。我的周刊只会分享一些我在冲浪中遇到的有趣的内容，不会像一些其他周刊一样照搬 GitHub Trending 或者追时下一些热门的内容。

我觉得写作最大的难度是素材的收集，而 [Cubox](https://cubox.pro/) 就能很好地帮我完成这个工作。我创建了一个叫【最近一周】的智能文件夹，规则就是【7 天内】收藏的链接。在平时冲浪时，遇到好的文章，只需要点一下浏览器右上角的收藏快捷方式即可。

![](http://img.ameow.xyz/202212181616889.png)

## 文章

### Golang int 类型的最大最小值（[原文](https://gosamples.dev/int-min-max/)）

以前学 C++ 的时候，老师说过可以把一些值初始化成 `INT_MAX` 之类的值。在 Golang 中也有类似的用法，他在 math 包里面。值得注意的是并没有 `MinUintX` ， 因为 unsigned 的最小值就是 0。具体枚举可以看 math 包的[文档](https://pkg.go.dev/math#pkg-constants) 。

话说比起包文档，这篇文章这种带有 example 的方式更加简单易懂，更适合作为 cheatsheet 使用。

### Golang 结构体对齐（[原文](https://medium.com/@sebassegros/golang-dealing-with-maligned-structs-9b77bacf4b97)）

最近在使用 [golangci-lint](https://github.com/golangci/golangci-lint) 来改善自己代码的质量，在屎山勘探的时候发现它给我标了一个这样的错：

> `warning: struct of size 40 could be 32 (maligned)`

当时有点懵逼，这个报错让人完全摸不着头脑，为什么一个结构体可以变小？看了这篇文章马上想起了“结构体对齐”这个知识点。CPU 是按 字长 （word size）去访问内存的，在 64 位上，字长为 8 字节。因此如果字段和其类型排布不合理，就会浪费大量字节在填充（padding）上。

不过这种极致优化能节省的内存感觉也不多，甚至比起代码的可读性来说可能是值得牺牲的。感觉现代可能已经很少去注重这些极致的优化。之前看过一个视频讲以前的游戏如何在内存极小的机器上运行起来，只能说现在计算机性能的提升让很多原来的奇技淫巧（例如算法和内存上的优化）变得不再重要。

### Golang 中的 context（[原文](https://go.dev/blog/context)）

之前一直以为这个 context 一个从入口一路带到最后一层调用的一个键值对。而事实上它跟并发控制有关，有超时、取消等功能。目前来说还是有点一知半解，但简单来说，context 只适合携带请求相关的参数，而不能作为传值的方式。另一篇[文章](https://medium.com/@cep21/how-to-correctly-use-context-context-in-go-1-7-8f2c0fafdf39) 提到，"Inform, not control."。

这个话题较为复杂，下期文章精读可能会介绍一下这方面的内容，敬请期待。

### 进程间通信（[原文](https://www.jianshu.com/p/c1015f5ffa74)）

和朋友讨论到各种语言的协程通信方式，发现其实 kotlin 和 golang 的协程都有相似的地方，其实这相似性就来源于进程间通信。基础知识永不过期呀！

## 项目

### [direnv](https://direnv.net/) - 自动加载环境变量

一个在进入和退出目录时自动加载目录下 `.envrc` 中的环境变量的工具。配合其他 CLI 工具（例如 Make）可能会有奇效。

### [just](https://just.systems/man/zh/) - 提供一种保存和运行项目特有命令的便捷方式

简化版的 Make，支持任意语言编写配方。

### [Coolify](https://docs.coollabs.io/coolify/) - 自建 Heroku

可以自建的 all in one 解决方案，能够快捷创建应用、数据库等。有点像自建版的 [leancloud](https://www.leancloud.cn/)。

### [MessAuto](https://github.com/LeeeSe/MessAuto) - macOS 自动提取验证码并复制粘贴回车

MessAuto 是一款 macOS 平台  **自动提取**  短信验证码并  **粘贴回车**  的软件，百分百由 Rust 开发，适用于任何 APP。

但是现在该 APP 没有签名，用起来略有顾虑，粘贴回车的方式感觉也略微不优雅，先观望观望。

> 这是猫鱼周刊的第 1 期，本系列每周日更新，主要内容为每周收集内容的分享，同时发布在
>
> 博客：[阿猫的博客-猫鱼周刊](https://ameow.xyz/categories/weekly)
> 掘金(beta)：[猫鱼周刊 - 3verest 的专栏 - 掘金](https://juejin.cn/column/7302415204927012918)
> 邮件订阅：[猫鱼周刊](https://quaily.com/ameow)
> Discord：[猫兄的和谐号高铁](https://discord.gg/5G5Nbtuz)
> 私信：[leslieleung@pm.me](mailto:leslieleung@pm.me)
