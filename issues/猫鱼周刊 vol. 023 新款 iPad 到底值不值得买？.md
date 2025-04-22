---
issue: 24
date: 2024-05-12
intro: 猫鱼周刊的24期，介绍了苹果新发布的iPad和笔，分析了其配置和新交互对艺术创作者的友好程度。同时分享了关于iPad的生产力指南和AI项目失败的原因分析。推荐了两个开源项目和两个实用工具/网站。
---

## 关于本刊

> 这是猫鱼周刊的第 24 期，本系列每周日更新，主要内容为每周收集内容的分享，同时发布在
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

## 本周新鲜事

这周的科技新闻不得不提一下苹果新发布的 iPad 和笔，升级点、新功能这些我就不多赘述了，表达几个我的看法。

- 面上是跳过了 M3 直接到 M4，但实际只有 1TB 和 2TB 版本的有满血 M4，其他是 3+6 的九核残血版，砍了 P 核，不一定打得过 M3。另外，只有 1TB 和 2TB 版本有 16GB 内存。刀法精准，感觉拿了个小改款 M3，名义上叫成 M4，又好卖又不妨碍挤牙膏。
- 还是上面这个配置的事，WWDC 还没开，不清楚苹果在 iOS/iPadOS 搞些什么 AI 方面的东西，所以在不知道有没有什么硬限制（例如到时候 8GB 内存跑不了大参数的模型）之前，建议还是观望下。
- 苹果之前不怎么强调 AI，一直说的是机器学习（Machine Learning），今年提得比较多，也许要发力了。
- 新的笔的新交互对画画的人很友好，几乎成了买新一代 iPad 和笔的决策原因。

另外，iPad Pro 的广告 [Crush!](https://www.youtube.com/watch?v=ntjkwIXWtrc)引起了比较大的争议。苹果一大客户群体是艺术创作者，但是这个广告很大胆地把乐器、画笔油漆、游戏机等等东西放进液压机压碎（据闻是 CG），引起了这些群体的反感。苹果也为此[道歉](https://adage.com/article/digital-marketing-ad-tech-news/apple-apologizes-ipad-pro-crushed-ad-it-missed-mark/2559321)。

![CleanShot 2024-05-11 at 23.39.57@2x.png](https://img.ameow.xyz/202405112340540.png)

回到标题说的，新款 iPad 到底值不值得买？我的决定是不买，尽管这次发布会看得我很心动，但是回到生产力本身，我不从事艺术创作，iPad 于我只是一个娱乐的作用，不需要追新型号。我对 iPad 的展望是，上 macOS，做一个类似微软 Surface 的定位，比 MacBook Air 更便携，同时又有 macOS 的生产力（能写代码，能本地编译调试等等）。当 iPad 能实现这些的那一天，我会毫不犹豫花出这笔钱。

## 文章

### iPad 生产力指南——编程

[原文链接](https://www.omegaxyz.com/2022/06/10/ipad-coding/)

前面说到在考虑买不买新 iPad 的时候，我的一个很大的关注点是“生产力”。这篇文章列举了一些在编程方面的生产力，我简单总结下。iPadOS 上的开发工具大概有几种：

- 文本编辑器（不是 IDE，不能编译或者调试）
- 远程工具（SSH 或者数据库等）
- 远程桌面
- 远程开发（通过连接到远程的开发环境）

事实上，我觉得这些工具很难形成真正有效的“生产力”。缺乏真正的 IDE，开发体验会非常差；远程类的不能脱离网络工作，外出场景非常蹩脚。再者，如果使用远程开发，完全白瞎了 iPad 上那颗 M 芯片，找个老款 iPad 也行。

### AI 项目为什么会失败

[原文链接](https://readmedium.com/why-do-ai-projects-fail-9b07f32ce321)

AI 项目的失败率很高，作者分析有以下原因： AI 没有解决正确的问题、AI 创新差距、AI 无法实现足够好的性能、人们忽视了简单的提升、AI 没有产生足够的价值和道德、偏见、社会危害。

在 [vol. 020](https://ameow.xyz/archives/weekly-020#AI-%E7%B1%BB%E5%B7%A5%E5%85%B7%E5%9C%A8-B-%E7%AB%AF%E7%9A%84%E8%90%BD%E5%9C%B0) 我提到过我的想法，跟这个作者的观点大致相似。有个点我比较在意，那就是人往往对 AI 有很高的期望，希望 AI 解决很大的问题，而忽略了 AI 可以完成的很小的功能。

> 为汽车自动泊车构建人工智能非常困难。但它可以从简单的预测开始，每辆车都可以做到：这个空间够大吗？

### Shamir 秘密共享

[原文链接](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing)

电影里经常有这样的情节：需要发射核弹的时候，要两个人同时将钥匙插进一个机器，同时转动。在密码学领域，有这么一种需求：有一个秘密，由多个人持有解密的密钥，但要需要若干个人同时提供密钥才能解锁。Shamir 秘密共享（Shamir's secret sharing）就是这样一种密码学算法。

## 项目

### Vercel 开源替代

[![Dokploy/dokploy - GitHub](https://gh-card.dev/repos/Dokploy/dokploy.svg)](https://github.com/Dokploy/dokploy)

[项目地址](https://github.com/Dokploy/dokploy)

开源的 Vercel、Netlify 和 Heroku 替代。我一直很喜欢这类 PaaS 平台，一方面是可以白嫖资源来部署自己的服务，另一方面是能 CI/CD 实在是太酷了。我现在最常用的是 [Zeabur](https://zeabur.com/)，这个是国人做的出海项目，说实话也不错。之前也看过可自建的 [Coolify](https://coolify.io/)，不过都比不上 dokploy 给我的第一印象好。

### 运行在 Cloudflare worker 上的网站监控

[![lyc8503/UptimeFlare - GitHub](https://gh-card.dev/repos/lyc8503/UptimeFlare.svg)](https://github.com/lyc8503/UptimeFlare)

[项目地址](https://github.com/lyc8503/UptimeFlare)

说到白嫖资源怎么能不提 Cloudflare 这个赛博菩萨呢。一个利用 CF worker 的网站监控，特点就是资源全白嫖（x。不过这个有个比较大的问题是，如果你的服务器在国内，这个监控的意义不大（网络波动比较多）。

## 工具/网站

### 景深模拟器

[网站链接](https://jherr.github.io/depth-of-field/)

![image.png](https://img.ameow.xyz/202405121936424.png)

一个可以调整物体距离、焦距、光圈、传感器面积的景深模拟器。适合摄影爱好者去理解焦距、光圈和景深的关系。

### iPad 参数大全

[网站链接](http://kylebing.cn/tools/ipad/)

![image.png](https://img.ameow.xyz/202405121939624.png)

我觉得这算是一个比较面向 geek 消费者的参数比较网站。苹果也有一个自家产品的[比较](https://www.apple.com.cn/ipad/compare/)，这个非常面向大众，不提详细的参数，不提同一款 iPad 间不同配置的具体差异（例如 1T 以下版本没有 16G 内存这事）。

## 最后

本周刊已在 [GitHub](https://github.com/LeslieLeung/cat-fish-weekly) 开源，欢迎 star。同时，如果你有好的内容，也欢迎[投稿](https://github.com/LeslieLeung/cat-fish-weekly/issues/new?assignees=LeslieLeung&labels=&projects=&template=recommendations.md)。

另外，我建了一个交流群，欢迎入群讨论或反馈。

![451715517486_.pic.jpg](https://img.ameow.xyz/202405122038249.jpg)
