---
intro: 这是猫鱼周刊的第16期，分享了为什么年纪越大时间过得越快以及有关个人信息安全的两篇文章，项目方面介绍了几个镜像相关的以及一个AI去除硬字幕的项目，最后分享了我关于学习正则表达式的心得。
issue: 16
date: 2024-03-03
---

## 关于本刊

> 这是猫鱼周刊的第 16 期，本系列每周日更新，主要内容为每周收集内容的分享，同时发布在
>
> 博客：[阿猫的博客-猫鱼周刊](https://ameow.xyz/categories/weekly)
>
> RSS：[猫鱼周刊](https://ameow.xyz/feed/categories/weekly.xml)
>
> 邮件订阅：[猫鱼周刊](https://quail.ink/ameow)
>
> 微信公众号：[猫兄的和谐号列车](http://img.ameow.xyz/202401141448662.png)
>
> Discord：[猫兄的和谐号高铁](https://discord.gg/5G5Nbtuz)
>
> 私信：[leslieleung@pm.me](mailto:leslieleung@pm.me)

## 文章

### 为什么年纪越大时间过得越快？

[原文链接](https://invertedpassion.com/why-time-seems-to-pass-faster-as-we-age/)

年纪越大，剩余寿命越短，却觉得每年过得更快了。作者认为这是进化使得我们的大脑成了一个高效的存储装置。大脑的主要作用是对这个世界构建出一个模型，从而获得生存和繁殖的优势。为了获得这个优势，大脑就沉迷于预测事情的发展。当一件事之前已经发生过，大脑不会再重新储存整件事情，而是增量记录新鲜和惊喜的部分。当我们还是孩子时，世界上所有的事情都是新鲜的，因此大脑进行大量的更新，投入了大量注意力在这些新事情上；当我们长大，新的遭遇变成了老记忆上的一个小补丁。当生活不断重复一样的模式，你对时间的感知就越来越弱。总的来说，你的生活越可预测，你就觉得时间越短暂。

要减缓时间，只能破坏生活的可预测性以及积极地策划惊喜。不过，随着年龄增长，我们越来越抗拒探索和冒险，但这就是让时间变快的原因。要彻底打破可预测性，就必须肉体上或精神上投入一个未知领域。变化越小，时间就流逝得越快。

> 注：文章原文行文较乱，我的概括不一定非常忠实地还原了文章的本意。长话短说，我的理解就是要想生活有意义、有重量感，就要多尝试新鲜的事情，积极打破生活中的循环。

### KYC？别了，谢谢。

[原文链接]([KYC? No, thanks | KYCNOT.me Blog](https://blog.kycnot.me/p/kyc-no-thanks))

KYC（Know Your Customer，或者通俗说身份验证）是一个合规操作，常见于银行、交易所、在线商务、邮件提供商、域名注册商等（在中国大陆，基本上所有在线服务）。

作者认为 KYC 对个人隐私、自由、安全和人格造成了威胁。KYC 本意是满足合规需求以及防止罪案，但很多时候一些小公司没有能力保护好收集的个人信息，造成个人信息在网上被肆意售卖等。同时对监管来说，KYC 也算是一种滥用。

其实关于个人信息安全，类似的事件数不胜数。我有一篇[文章](https://ameow.xyz/archives/chaoxing-incident)表达了对国内高校信息安全的担忧。作为呼应，我的母校在毕业后有一个小程序收集校友信息，明确表示了信息仅存储在校内服务器中。

## 项目

### NoCLin/LightMirrors

[![NoCLin/LightMirrors - GitHub](https://gh-card.dev/repos/NoCLin/LightMirrors.svg?fullname=)](https://github.com/NoCLin/LightMirrors)

一个可以镜像 DockerHub、PyPI、PyTorch 和 NPM 的镜像站服务。

### DaoCloud/public-image-mirror

[![DaoCloud/public-image-mirror - GitHub](https://gh-card.dev/repos/DaoCloud/public-image-mirror.svg?fullname=)](https://github.com/DaoCloud/public-image-mirror)

Docker 的镜像，由 DaoCloud 出品，支持包括 DockerHub、gcr、quay 等等，只需要替换一下 registry 即可使用。

### eryajf/Thanks-Mirror

[![eryajf/Thanks-Mirror - GitHub](https://gh-card.dev/repos/eryajf/Thanks-Mirror.svg?fullname=)](https://github.com/eryajf/Thanks-Mirror)

一个运维开发老哥整理的各个包管理器，系统镜像以及常用软件的好用镜像。

### YaoFANGUK/video-subtitle-remover

[![YaoFANGUK/video-subtitle-remover - GitHub](https://gh-card.dev/repos/YaoFANGUK/video-subtitle-remover.svg?fullname=)](https://github.com/YaoFANGUK/video-subtitle-remover)

Video-subtitle-remover (VSR) 是一款基于 AI 技术，将视频中的硬字幕去除的软件。 主要实现了以下功能：

- **无损分辨率**将视频中的硬字幕去除，生成去除字幕后的文件
- 通过超强 AI 算法模型，对去除字幕文本的区域进行填充（非相邻像素填充与马赛克去除）
- 支持自定义字幕位置，仅去除定义位置中的字幕（传入位置）
- 支持全视频自动去除所有文本（不传入位置）
- 支持多选图片批量去除水印文本

在实际应用场景测试效果还不错，不过可能需要花点时间调整下。AI 相关的论文非常多，但是把论文落地成应用，还开源的，真的很少。

## 工具/网站

### MuscleWiki

[网站链接](https://musclewiki.com/)

![](https://img.ameow.xyz/202403031954247.png)

一个可以根据有的器材和需要训练的肌肉群来推荐健身动作的网站。

![](https://img.ameow.xyz/202403031956626.png)

配有动图和文字讲解动作。（不过还是建议在专业场地找专业人士指导和帮助健身）

## 想法

### 正则表达式怎么学

正则表达式的学习方式很简单粗暴，唯熟手而。

一开始先通读一遍文档，大约知道有什么符号，能做什么。

然后就是枯燥的查文档-改正则的过程，在一大堆复杂的匹配需求中不断练习，直到渐渐不怎么用查文档就能写出正则，再到不怎么用调试就能写出好用的正则。

进阶的话，可以了解一下编译原理里面有一个有限状态机的概念，有很多正则的辅助工具也是通过有限状态机来对正则进行可视化。了解这个后，对正则会有一个新的理解。
