---
issue: 23
date: 2024-05-05
intro: 猫鱼周刊第23期的文章内容涉及AWS S3桶名的安全性、分号在编程语言中的起源、Llama 3文本生成模型的改进、Raycast插件列表、自建书签App、微软开源的MS-DOS代码和敏感词包等内容。作者还提到了一些关于保护敏感信息、做好监控和告警以及注意成本的建议。
---

## 关于本刊

> 这是猫鱼周刊的第 23 期，本系列每周日更新，主要内容为每周收集内容的分享，同时发布在
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

## 文章

### 云上黑暗森林：打爆云账单，只需要 S3 桶名

[原文链接](https://mp.weixin.qq.com/s/35ScjtPjC1GNGKaSArJhcA)

简单来说，就是 AWS S3 即使是私有桶，也需要为请求次数付费，包括未授权请求（4xx）。作者从中学到的教训是：

- 不要暴露 S3 桶名，即使是私有桶。
- 可以为桶名添加随机后缀以增加安全性。
- 明确指定 S3 区域，避免产生重定向费用。

译者还表达了一些很尖锐的观点，例如厂商监守自盗等。

云服务有很多隐藏的坑，有很多繁杂的收费项，有很多隐晦的计费规则，很可能在账单出来之前你也不会预料到会花这么多钱；同时，云服务也有很多安全风险，例如之前就有博主 CDN 被刷了几万块。我提几个我自己会比较注意的地方：

- 保护好敏感信息。包括要注意实际使用的配置文件不要上传到 GitHub 或其他公共的 git，添加进 `.gitignore` 中（打包 Docker 镜像同理）；遵守 12 因素 App，通过环境变量传递敏感值；定期更换 token 等。
- 做好监控和告警。涉及 CDN、流量等，必须做监控和告警。七牛云有个服务，监控 CDN 流量，变动大的时候短信通知，此外我自己还加了个 webhook，做到强触达。
- 注意成本。如果确定自己要长期、大量使用某个服务，最好购买资源包或者包年包月，或者使用成本计算器（很坑，有些服务商或者服务不提供，AWS 就基本都有）预估按量计费的成本。在使用新的服务时，接下来几天一定要关注成本状况，及时止损。如果是测试用的服务，不用了一定要记得关掉。

### 分号在编程语言中的起源

[原文链接](https://www.ntietz.com/blog/researching-why-we-use-semicolons-as-statement-terminators/)

如果你是计算机专业的学生，你的第一门语言很可能是 C/C++，你的老师第一节课就会告诉你，语句结尾要有分号。等你学编译原理的时候，就会学到在词法分析、语法分析等等步骤中，这个语句终结符的作用。

分号是最常见的语句终结符，但具体为什么要使用分号没有明确的记录。最早使用分号作为语句终结符的是 [ALGOL 58](https://en.wikipedia.org/wiki/ALGOL_58)。作者作出了几个推测：可用，多数键盘上有这个符号；方便，就在手指的默认位置（homerow）；在英语中用法接近，用来分割短句；不容易冲突。

### Llama 3 出言不逊

[原文链接](https://ollama.com/blog/llama-3-is-not-very-censored)

对比 Llama 2，Llama 3 大幅降低了误拒绝率（false refusal）。作者举了几个例子，包括在机场杀时间（Killing time at the airport，在机场消磨时间），写格式化硬盘代码等。Llama 2 会以道德规范为由拒绝提供回答，而 Llama 3 则能理解这些问题，并提供回答。

文本生成模型一直有比较大的争议，包括版权、种族或性别歧视问题，还有一些不可细说的风险。要安全合规地使用，我个人觉得还是要再套一层审核规则。

## 项目

### Raycast 插件列表

[![marekbrze/categorized-raycast-extensions - GitHub](https://gh-card.dev/repos/marekbrze/categorized-raycast-extensions.svg)](https://github.com/marekbrze/categorized-raycast-extensions)

[项目地址](https://github.com/marekbrze/categorized-raycast-extensions)

一个非官方的 Raycast 插件列表。直接在网页里就可以搜索，比官方商店的好用一点。

### 自建书签 App

[![MohamedBassem/hoarder-app - GitHub](https://gh-card.dev/repos/MohamedBassem/hoarder-app.svg)](https://github.com/MohamedBassem/hoarder-app)

[项目地址](https://github.com/MohamedBassem/hoarder-app)

![image.png](https://img.ameow.xyz/202405051726281.png)

一个可自建的 Cubox 替代。我在第一期讲过，我主要使用 Cubox 进行收集，它最大的缺点是数据不好导出，不在自己掌控。中间也找过 LinkWarden 之类的替代，设计、功能等都有些不满意，但这个看起来还不错，过段时间可能会迁移过来。

### MS-DOS

[![microsoft/MS-DOS - GitHub](https://gh-card.dev/repos/microsoft/MS-DOS.svg)](https://github.com/microsoft/MS-DOS)

[项目地址](https://github.com/microsoft/MS-DOS)

这位更是重量级。作为历史资料，微软开源了 MS-DOS v1.25，v2.0 和 v4.0 的代码，而且是以 MIT 协议公开。

主要都是汇编语言，基本看不懂（可能要老一辈才能懂了吧）。但是 v1.25 的代码量其实很少，有点像看 Linux 内核 v0.12 的味道（虽然那个我也没细看过）。

### 敏感词

[![houbb/sensitive-word - GitHub](https://gh-card.dev/repos/houbb/sensitive-word.svg)](https://github.com/houbb/sensitive-word)

[项目地址](https://github.com/houbb/sensitive-word)

一个敏感词包。不过有些可惜，只能作为一个 Java 包使用，不能直接部署成服务，给别的系统使用。

## 工具/网站

本周没有逛到什么特别有意思的工具或者网站，推一下我自己最近做的一个配置工具，能够为我的[通知项目](https://github.com/LeslieLeung/heimdallr)提供配置生成。这个项目的编写也很有意思，是我跟 GitHub Copilot 合作完成的，如果你对开发过程感兴趣，可以看看这篇[文章](https://ameow.xyz/archives/develop-a-frontend-site-with-copilot)。

[网站链接](https://heimdallr-configurator.vercel.app/)

![image.png](https://img.ameow.xyz/202405051721857.png)

## 最后

上周我在周刊和交流群里发了个有奖问卷，一开始是有收到一些有建设性的意见，直到后来应该是有人把链接发到了一些薅羊毛群，涌入了一大堆垃圾数据，整个问卷就废了。主要收到这些意见：

- 丰富内容，增加趣味性（尽量引入一些，但主要还是我信息源内的内容，不保证不会跟其他博主的重复）
- GitHub 链接不可点击（那个图片可以点击跳转，在我的博客上由于图片插件的问题，点击区域在图片右边。对应本期增加了一个项目链接。）

问卷的效果不是很好，后面不搞了。如果有好的意见，可以在对应的开源项目提 issue，或者发邮件给我，又或者在交流群里面讨论。

本周刊已在 [GitHub](https://github.com/LeslieLeung/cat-fish-weekly) 开源，欢迎 star。同时，如果你有好的内容，也欢迎[投稿](https://github.com/LeslieLeung/cat-fish-weekly/issues/new?assignees=LeslieLeung&labels=&projects=&template=recommendations.md)。

另外，我建了一个交流群，欢迎入群讨论或反馈。

![441714902454_.pic.jpg](https://img.ameow.xyz/202405051748021.jpg)


