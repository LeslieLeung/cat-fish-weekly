---
issue: 6
date: 2023-12-17
---

## 文章

### 找出项目中不可达的函数

[原文链接](https://go.dev/blog/deadcode)

Go 官方新出的一个工具，名为 deadcode，可以检测代码中不可达的函数(unreachable functions)。这个对于清理无用代码很有参考意义，因为在 IDE 中只能看到函数是否有被使用，但没法真正区分出代码是否可达。官方给出了一个例子：

```go
package main

import "fmt"

func main() {
    var g Greeter
    g = Helloer{}
    g.Greet()
}

type Greeter interface{ Greet() }

type Helloer struct{}
type Goodbyer struct{}

var _ Greeter = Helloer{}  // Helloer  implements Greeter
var _ Greeter = Goodbyer{} // Goodbyer implements Greeter

func (Helloer) Greet()  { hello() }
func (Goodbyer) Greet() { goodbye() }

func hello()   { fmt.Println("hello") }
func goodbye() { fmt.Println("goodbye") }
```

很明显此处 `goodbye()` 这个函数是不可达的（没有地方能调用这个函数），但是由于 `Goodbyer` 实现了 `Greeter` 接口，因此它需要这个函数。通过 `deadcode` ，可以知道：

```
$ deadcode .
greet.go:23: unreachable func: goodbye
greet.go:20: unreachable func: Goodbyer.Greet
```

因此可以删除 `Goodbyer` 和 `goodbye()` 相关的代码。

这个工具利用了一种叫快速类型分析(Rapid Type Analysis, RTA) 的算法来分辨代码是否可达，具体的原理已经超出了我的能力范围，只能推荐大家去阅读一下[原论文](http://doi.acm.org/10.1145/236337.236371)。

### PHP realpath cache 与 k8s secrets / configmap 更新

[原文链接](https://pracucci.com/php-realpath-cache-and-kubernetes-secrets-configmap-updates.html)

这个是最近踩到的坑：PHP 会缓存文件链接的实际路径。可以理解为 DNS 缓存，缓存了动态链接（域名）到实际文件路径（IP）的映射。而 Kubernetes 在处理 secrets / configmap 更新时，会先创建一个文件夹，然后更改原来的文件夹的动态链接到新的文件夹，最后删除旧文件夹。

因此如果 PHP 缓存了这个映射，会导致程序有一段时间内（配置的 `realpath_cache_ttl`，默认为 2 分钟）访问到了旧的目录，导致读不到文件。

文章提出了四种方法来解决这个问题。第一种是禁用这个缓存，不推荐；第二种是利用 `subPath` 来挂载文件，但其实这种方法就损失了动态更新这一重要特性；第三种是利用 OPCache，可用，但是感觉增加了复杂度；第四种是用 `clearstatcache` 这个函数，包裹正常的文件获取流程。

不得不感慨一下，PHP 感觉真的老了，跟现在最新的技术有点水土不服了。

### k8s 折腾笔记——树莓派集群安装 k3s

[原文链接](https://blog.xianyu.one/2021/11/16/Linux/tutorial/k8s-install/)

最近树莓派 5B 上市了，估计 4B 快要开始降价了，可以开始看一下树莓派集群的搭建了。

## 项目

### 1874.cool —— 个人门户

[![LetTTGACO/1874.cool - GitHub](https://gh-card.dev/repos/LetTTGACO/1874.cool.svg)](https://github.com/LetTTGACO/1874.cool)

[1874's Home](https://1874.cool/)

一个个人门户的网站源码，可以把自己的社交媒体账号、个人简介、作品集等展示在一个地方。

![](http://img.ameow.xyz/202312171626526.png)

### PicList —— 更好的 PicGo

[![Kuingsmile/PicList - GitHub](https://gh-card.dev/repos/Kuingsmile/PicList.svg)](https://github.com/Kuingsmile/PicList)

之前我一直在使用 PicGo，最近关注到图片 EXIF 隐私问题，因此在寻找一款能够在上传时清除 EXIF 信息的 PicGo 替代，找到了它。

## 工具

经常在写代码的时候突然出现“提笔忘字”时刻，例如“诶，两个 order by 到底是怎么排序的呢”，“python 的 tuple 是怎么访问的呢？”。这时候一些合适的在线测试工具就能帮助我们快速搭建起一个测试环境，去快速验证我们的想法。

### SQL 在线测试工具

网站链接：[SQL Fiddle](http://sqlfiddle.com)
开源代码：[GitHub - zzzprojects/sqlfiddle3: New version based on vert.x and docker](https://github.com/zzzprojects/sqlfiddle3)

一个 SQL 在线测试工具，用法是先在左边写好 DDL 和数据，在右边执行查询，另外还可以在下面看到 `EXPLAIN` 的结果。

这个工具也是开源的，看了一下，原本以为会是用软件模拟 SQL，结果发现它支持多种数据库，而且应该是实时会给你创表，在真实的数据库（当然是容器化的）去给你做查询。

![](http://img.ameow.xyz/202312171551729.png)

### webhook 在线测试工具

网站链接：[Webhook.site - Test, process and transform emails and HTTP requests](https://webhook.site)
开源代码：[GitHub - webhooksite/webhook.site: ⚓️ Easily test HTTP webhooks with this handy tool that displays requests instantly.](https://github.com/webhooksite/webhook.site)

一个 webhook 在线测试工具。在做接入第三方 webhook 的时候最痛苦的事情就是，对方的接口文档写得比较含糊，也没有真实的示例 payload 的时候，真是两眼一抓瞎。用上这个工具，将第三方的 webhook 发到这个网站上，就能看到 webhook 的 payload，以及 Header 之类的详细信息。

### 在线代码运行工具

网站链接：[Online IDE - Code Editor, Compiler, Interpreter](https://www.online-ide.com/)

这种应该就比较常见了，输入代码，运行得出结果，有点像竞赛用的 OJ。适合在”提笔忘字“的时候当草稿纸用（当然你也可以在本地搞一个 `test.py`）。

![](http://img.ameow.xyz/202312171600884.png)

### Go Playground

网站链接：[Go Playground - The Go Programming Language](https://go.dev/play/)
开源代码：[GitHub - golang/playground: [mirror] The Go Playground](https://github.com/golang/playground)

这个就很经典了，gophers 常用的分享代码片段的地方。在 stackoverflow、GitHub issue 里经常见到的，如果你遇到了 bug，最好是分享一个最小可用片段，gophers 常用这个工具。

## 想法

### 静态规则 vs GPT 在代码检查中的作用

今年年中的时候，曾经尝试过用 GPT 对代码进行 lint，去发现并修复代码中的 bug 等。试验的结果非常不尽人意，GPT 出现了以下的问题：

- 行号问题：给 ChatGPT 提供一整个代码文件之后，line:char 会出现丢失的情况。猜想是 tokenize 的时候丢失了。如果要解决行号，在每一行开头手动补一个行号即可。char 的问题可能无法解决，只能精确到行，但是作为 lint 来说没有 char 也没什么大问题。
- 输出无用建议：目前经常出现一些没有用的建议或者是对语言的特性不了解、对上下文不了解等，导致模型提出一些无效的建议，需要再加人工去筛选。例如出现某某变量未定义等，通过 prompt 去限制也无改善。
- 上下文受限：当时 GPT 3.5 还不支持 16K context，当输入的代码文件过长，就会出现输出截断等问题。
- 输出格式不稳定：由于 LLM 的不稳定性，不能保证每次输出的结果都是结构化、可处理的。
- 不可重复性：与正常的 lint 相比，使用 ChatGPT 做 lint 不可避免的问题是每次 lint 的结果不一定是一样的。如果第一次 lint 的时候 GPT 指出你有某个问题，尝试修复之后，它不一定还会再报这个问题，导致无法验证是否真的改好了。

这些问题中，有几个是致命的：输出的建议误报率过高，而且不可重复。相反，像 `deadcode`, `nilaway` 这类利用静态规则等去对代码进行分析的静态分析工具反而更加实用。

## 关于

> 这是猫鱼周刊的第 6 期，本系列每周日更新，主要内容为每周收集内容的分享，同时发布在
>
> 博客：[阿猫的博客-猫鱼周刊](https://ameow.xyz/categories/weekly)
> 掘金(beta)：[猫鱼周刊 - 3verest 的专栏 - 掘金](https://juejin.cn/column/7302415204927012918)
> 邮件订阅：[猫鱼周刊](https://quail.ink/ameow)
> Discord：[猫兄的和谐号高铁](https://discord.gg/5G5Nbtuz)
> 私信：[leslieleung@pm.me](mailto:leslieleung@pm.me)
