---
issue: 3
date: 2023-11-26
---

## 文章

### 2023 开发者生态系统现状（[原文](https://www.jetbrains.com/zh-cn/lp/devecosystem-2023/)）

JetBrains 年货来了。我节选部分我觉得很有趣的分享一下，但其实整份报告都很有意思。

#### AI 辅助开发

![](http://img.ameow.xyz/202311251609026.png)

给 AI 提问，然后用 AI 回复作为“Ground Truth”来跟我沟通的同事真的很多，以至于我对这一种现象产生了一定反感——先不论 AI 回复的对错，程序员丧失了通过搜索引擎，阅读官方文档、优质博客等对信息进行核实，深入了解的这一个能力，就很可悲。

我个人目前使用 AI 最多的场景是生成代码/注释/文档，AI 不是代替我进行思考，而是帮我节省打字的劳动和时间。我觉得这也是 Copilot 命名的来由：AI 只是一个副驾驶，人类才是思考、决策的机长。我使用 Copilot 的时候主要的责任就是通过上下文代码或注释引导 Copilot 生成我想要的代码，review 它生成的代码并适当修改。

#### 2023 年，但是 Java 8

![](http://img.ameow.xyz/202311261710415.png)

她一定不知道为什么中国人为什么都在 Java 8。

#### 薪酬

![](http://img.ameow.xyz/202311251626687.png)

美国的薪资大约是中国大陆的五倍，中国大陆和巴西、墨西哥相等，但比印度、非洲等略高，但也在倒数的行列了。

#### 彩蛋

![](http://img.ameow.xyz/202311251618530.png)

也太给 JetBrains 面子了，近几个版本的稳定性实在太差了，总是在重建索引，我都快要 vscode 启动了。

### Diving into Conflict-Free Replicated Data Types(CRDTs) （[原文](https://redis.com/blog/diving-into-crdts/)）

笔记、协作软件经常提到的 CRDT，原来也是 Redis 跨副本同步的核心技术之一。这篇官方博客讲述了 CRDT 在 Redis 中的应用。

### 类原生体验的 vs code（[原文](https://posts.cv/td/brSPuD65bN5NT3aASQL1)）

一个把 vscode 调整成类原生观感的配置。配置文件见：

[/\* ---- settings.json ---- \*/{ "workbench.colorTheme": "Default Light Moder - Pastebin.com](https://pastebin.com/4pEe3RHb)

## 项目

### [MyServers](https://github.com/my-servers)

一个 App 监控管理你所有的服务器和服务端应用。这是一款监控管理 App，可以扩展各种服务端插件，十分灵活。

之前我考虑过，我理想中一个 homelab 控制中心的需求：

- 批量控制开关机
- 批量在线状况监控、性能监控
- docker/lxc 的集中统一管理
- 快速通过反代上线新服务
- 统一通知收集、告警
- 定期维护提醒
- 跳板机
- 支持多种品牌特定的操作（群晖、威联通、pve）

这个项目基本能满足我的需求，不过在设计上跟我的预想有一点区别：它控制的每一台服务器都是一个服务端，手机作为客户端连接到每个服务端上实现管理；我希望的设计是有一个中心化的服务端，在每台服务器上安装一个 agent，通过 agent 进行控制。

### [uber-go/nilaway](https://github.com/uber-go/nilaway)

一个检测 Go 代码中可能出现空指针问题的静态检查工具。目前还在开发阶段，暂时还没有结合进 golangci-lint。

### [kamilsk/godownloader](https://github.com/kamilsk/godownloader)

[goreleaser/godownloader](https://github.com/goreleaser/godownloader) 的继续开发版本。可以生成一个 shell 脚本，从 GitHub Release 下载二进制并安装到指定目录。很多程序会提供一个 shell 脚本，通过一条命令就能下载这个脚本并安装程序到指定目录，该项目就是用来生成这样的脚本。

## 工具

### onemodel

官网链接：[OneModel - A Diagramming Tool for Software Engineers](https://www.onemodel.app/)

一个面向软件开发者的画图工具。我觉得最大的亮点是预定义了很多常用的中间件、服务（例如 Redis，AWS S3）等的图标，以及尽可能减少在排版上的麻烦。图标方面，可以选择图标的单个和多个，同时还支持容器框（Container，用来标识系统边界等），可以画出看起来很 decent 的系统设计图。排版方面，连线只用选择从 A 到 B，会自动生成连线，拐角等会自动处理。

贴一个我自己画的图作为 demo。

![](http://img.ameow.xyz/202311251555415.png)

## 想法

### 重新审视需求：从 AirPower 到 MagSafe 的启示

苹果有一个很出名的流产产品：AirPower，可以在一块无线充电板上随意放置两三个设备，线圈自动跟踪。这个产品流产之后，苹果推出了 MagSafe 系统 ，然后 belkin 做了一个三项充电器，配合上 iOS 的 standby 功能，算是作为 AirPower 更好的替代。

事实上，三项充电器其实在工程上更容易实现，也更加健壮，也能实现 AirPower 的大多数功能：多个设备同时无线充电。在技术上解决不了的时候，与其在技术上死磕，不如往回走一步，看看是否需求不合理了。在这里，三个设备同时平放在一块板上并自动跟踪其实是一个比较弱的需求；如果有一个可以盲放的机制，同时能让多个设备准确定位（MagSafe），其实就能满足用户的充电需求。

很多技术在做需求的时候喜欢死磕，想好的解决方案；但是如果往回想一下，是不是产品的需求不合理，达到用户的需求可以有别的实现方式，会是一个很好的启发。

## 关于

> 这是猫鱼周刊的第 3 期，本系列每周日更新，主要内容为每周收集内容的分享，发布在
>
> 博客：[阿猫的博客-猫鱼周刊](https://ameow.xyz/categories/weekly)
> 掘金(beta)：[猫鱼周刊 - 3verest 的专栏 - 掘金](https://juejin.cn/column/7302415204927012918)
> 邮件订阅：[猫鱼周刊](https://quaily.com/ameow)
> Discord：[猫兄的和谐号高铁](https://discord.gg/5G5Nbtuz)
> 私信：[leslieleung@pm.me](mailto:leslieleung@pm.me)
