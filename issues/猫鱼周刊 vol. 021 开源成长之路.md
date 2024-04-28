---
issue: 22
date: 2024-04-28
intro: 猫鱼周刊第22期，分享了关于开源成长之路、SEO入门指南，工具网站有LLM Price Check、Revezone和TinySnap，以及对程序员面试为何变为八股的思考。
---

## 关于本刊

> 这是猫鱼周刊的第 22 期，本系列每周日更新，主要内容为每周收集内容的分享，同时发布在
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

### 我的开源成长之路

[原文链接](https://tw93.fun/2024-01-12/open.html)

Tw93 大佬的分享。他的作品 Pake 和妙言我都使用过，也 RSS 订阅了他的潮流周刊。这个分享从他的开源经历、对开源的理解、怎么做好开源和开源给他带来了什么几个角度出发。

其实国内的开源氛围一直很一般，我身边的同事基本没有开源贡献过，甚至没有 GitHub 账号；国内互联网大厂的开源项目和贡献远没有 FAANG 多；中文项目很多假开源（核心代码/模型不开源），很多 markdown 项目。

我在毕业之后渐渐开始在 GitHub 活跃，有做自己的项目，偶尔也会给在用的一些项目提 issue 或者 pr，我觉得过程中是学到了很多东西的。当你还在初学阶段的时候，也许你帮不上什么忙，可以提一下 issue，帮助开发者改进项目；当你渐渐入门，有编写/修改大项目的能力，可以去试着写代码提 pr，又或者写自己的小工具/项目。

关于开源，我自己的 Slogan 是 “Code for fun, and for ever.” 。一是希望写代码能给我带来无穷的乐趣，二是希望这是一个长远的事情，并非为了眼前工作赚钱，而是一生的乐趣。

### SEO 入门指南

[原文链接](https://ahrefs.com/seo)

ahref 公司出的一个 SEO 指南，包含了一系列文章，比较简单的介绍了 SEO 的一些基础知识。具体的内容我也还没读完，但是它每篇文章都不长，适合入门读。语言有中文可选。

## 项目

### lobehub/lobe-vidol

[![lobehub/lobe-vidol - GitHub](https://gh-card.dev/repos/lobehub/lobe-vidol.svg?fullname=)](https://github.com/lobehub/lobe-vidol)

LobeHub 团队出品的一个可以跟虚拟人聊天，甚至跟 3D 模型互动的工具。项目还很新，可以关注下。

![image.png](https://img.ameow.xyz/202404272359430.png)

### danvergara/morphos

[![danvergara/morphos - GitHub](https://gh-card.dev/repos/danvergara/morphos.svg?fullname=)](https://github.com/danvergara/morphos)

一个可自建的文件格式转换服务。这类功能有很多在线服务，但是有隐私泄露风险，自建和本地都是更好的选择。

### stonith404/pingvin-share

[![stonith404/pingvin-share - GitHub](https://gh-card.dev/repos/stonith404/pingvin-share.svg?fullname=)](https://github.com/stonith404/pingvin-share)

一个可自建的文件分享服务。可以调整分享链接的过期时间、密码和最大访问次数。

![image.png](https://img.ameow.xyz/202404280007723.png)

## 工具/网站

### LLM Price Check

[网站链接](https://llmpricecheck.com/)

一个用来对比 LLM 价格的网站，同时也展示了上下文长度供参考，也提供了一个计算器来计算成本。

![](https://img.ameow.xyz/202404272339122.png)

### Revezone

[网站链接](https://revezone.com)

一个聚合了 [Tldraw](https://www.tldraw.com/) 和 [Excalidraw](https://excalidraw.com/) 的网站。特点是可以保存多个文件，而且可以通过 tab 切换。

![](https://img.ameow.xyz/202404272309447.png)

另外，如果你对画图工具感兴趣，可以看一下周刊第 10 期对常见画图工具的横评，这是[链接](https://ameow.xyz/archives/weekly-010#%E5%9C%A8%E7%BA%BF%E7%94%BB%E5%9B%BE%E5%B9%B3%E5%8F%B0)。

### TinySnap

[链接](https://chromewebstore.google.com/detail/tinysnap-production-ready/ijobkfpianooemebecnbaafnjndhbdcl)

这是一个网页截图的 chrome 插件，可以制作干净、带边框的漂亮截图。从本期开始，周刊工具/网站栏目的截图就开始用这个工具来制作，

## 想法

### 为什么程序员面试会变成八股？

这张图源自一个做校招指导的人的朋友圈，看完特别想表达一下我的意见。

![image.png](https://img.ameow.xyz/202404272346391.png)

当做面试官的一批人发现可以通过指导校招盈利，于是他们营造焦虑，贩卖相关的课程，写八股，并且在实际面试上就考核八股，然后又通过知识星球、内推等方式获利，并且通过人脉拉拢更多人来搞八股，形成闭环。

而毕业生，还没毕业就被割了韭菜，成为别人利益链条中的一环。当花了钱、背了八股进入大厂拿到亮眼的工资后，这些人又转过头来变成八股的考官和卖课的人，继续割下一代的韭菜，如此恶性循环。

我个人是比较反感八股的，你可以说我是因为没背好八股、没进到大厂所以对八股心生怨恨，也可以说我嫉妒通过校招指导赚到钱的人，但我对我的真才实学问心无愧。在日常工作中，一口流利的八股并不能帮助你设计更好的方案或者排查出疑难的 bug，只有坚实的基础和良好的直觉，能让你迅速定位到问题，通过搜索引擎或其他工具，快速并精准地完成工作。

## 最后

本周刊已在 [GitHub](https://github.com/LeslieLeung/cat-fish-weekly) 开源，欢迎 star。同时，如果你有好的内容，也欢迎[投稿](https://github.com/LeslieLeung/cat-fish-weekly/issues/new?assignees=LeslieLeung&labels=&projects=&template=recommendations.md)。

另外，我建了一个体验反馈问卷，有别的意见也可以在这里[反馈](https://wj.qq.com/s2/14419451/42b1/)，或者加入交流群反馈。

彩蛋：前十名填写问卷的朋友可以获得一个小红包，金额不大，聊表心意。

![421714234147_.pic.jpg](https://img.ameow.xyz/202404280009981.jpg)
