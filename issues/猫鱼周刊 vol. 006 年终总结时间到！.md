---
issue: 7
date: 2023-12-24
---

## 关于本刊

> 这是猫鱼周刊的第 7 期，本系列每周日更新，主要内容为每周收集内容的分享，同时发布在
>
> 博客：[阿猫的博客-猫鱼周刊](https://ameow.xyz/categories/weekly)
> RSS：[猫鱼周刊](https://ameow.xyz/feed/categories/weekly.xml)
> 邮件订阅：[猫鱼周刊](https://quail.ink/ameow)
> Discord：[猫兄的和谐号高铁](https://discord.gg/5G5Nbtuz)
> 私信：[leslieleung@pm.me](mailto:leslieleung@pm.me)

## 头条

又到年底啦，又到了写年终总结的时间。这是我的[年终总结](https://ameow.xyz/archives/2023-wrapup)，欢迎查看。

## 文章

### Interface 的误区

[原文链接](https://preslav.me/2023/12/15/golang-interfaces-are-not-meant-for-that/)

作者表示接口经常用于达成内聚的目的，并以此来实现替换数据库层进而进行 mock、单测等。但实际上这层不必要的抽象会使代码更加脆弱，也更难阅读和维护。相反，作者认为现代的代码在进入生产后要么只会增加功能，要么整个被替换，而且数据库基本是跟应用绑定的。最后作者提出了一些他的建议：

- 多一层的接口是否是必要的？标准库或第三方包中的接口能否实现同样的功能？
- 你是在写应用还是库？接口更多出现在库而不是应用中。
- 接口必须根据需求自然形成，而非提前设计。
- 减少方法，一个就够了。（？这里不是特别理解）
- 减少参数的数量，尽量使用基本类型，或标准库中的知名类型，减少使用自定义的类型。
- Mock 不是引入接口的理由。
- 问问自己，这个接口会有多少个用例？如果少于三个，最好还是用标准库中的接口。

### Go 项目模板

[原文链接](https://go.dev/blog/gonew)

在今年的 [Go 开发者调查](https://go.dev/blog/survey2023-h2-results)中，调研了几个有关创建新项目的问题。Go 团队最近做了一个新工具，通过 `gonew` 命令来从已有的模板创建新项目。

![](http://img.ameow.xyz/202312241701713.png)

我用我自己的一个 [gin 模板](https://github.com/LeslieLeung/gin-application-template) 体验了一下，如果开发者自己本身就有趁手的项目模板（或者使用社区提供的优质模板），确实是很快就能创建出一个舒服的项目结构。稍微有点不足的是，使用 `gonew` 创建出来的项目，不会自动更改项目文件中的 `import` 路径，因此创建出来的项目并不是马上就能跑通。

### 容器化开发

[原文链接](https://code.visualstudio.com/docs/devcontainers/containers)

最近 Jetbrains 的 IDE 也开始支持 devcontainers 了，vscode 在更早就有了这个功能。容器化开发也许是解决同时开发多个项目时，不同的复杂依赖的问题的一剂良药？

## 项目

### Tensor-Puzzles —— pytorch 练习题

[![srush/Tensor-Puzzles - GitHub](https://gh-card.dev/repos/srush/Tensor-Puzzles.svg)](https://github.com/srush/Tensor-Puzzles)

一些常见的矩阵操作等的 pytorch 练习题。还记得大学的时候写炼丹代码的时候就经常被维度转换等等折磨，如果回到大一大二，也许我会认真刷一遍这个练习题（x）。

### go-sqlmock

[![DATA-DOG/go-sqlmock - GitHub](https://gh-card.dev/repos/DATA-DOG/go-sqlmock.svg)](https://github.com/DATA-DOG/go-sqlmock)

一个通过模拟数据库驱动来测试数据库交互的 mock 工具。可以断言数据库执行了什么语句来进行测试。

## 工具

### GitHub Wrapped —— 生成你的 GitHub 年度报告

网站链接：[GitHub Wrapped](https://www.githubwrapped.io/)

### Sony Playstation 2023 Wrap-up

网站链接：[Wrap-Up 2023 | PlayStation](https://wrapup.playstation.com)

## 想法

### 注册登录体验

一般产品的注册登录有落地页或首页仅展示“登录“，仅展示“去体验”，同时展示“注册”和“登录”这几种，下面分别使用一些例子来详细说明。

- devv.ai：仅展示登录。网站不登录即可使用，因此不需要强调注册。同时，登录弹窗中支持第三方登录（仅谷歌），通过邮箱登录不区分注册/登录行为，第一次登录即为注册。实际上是通过统一了第三方登录和邮箱登录的流程，去除了注册行为，来达到一致。这种方式仅需一步就能到达注册页面，仅需两步就能完成新用户注册（第一步点击登录按钮，第二步发送邮件或跳转第三方登录）。
- cubox.pro：仅展示去体验。网站是需要注册登录才可以使用的，所以点击去体验之后跳转到的是登录页面，注册会比登录深一个层级。这种方式仅需两步就能到达注册页面。
- proton.me：同时展示注册和登录。网站需要注册登录才可以使用，同时还有付费服务。因此注册按钮文案为"Create free account"。

一般好的注册登录体验，在一到两步内就要能到达注册页面。

## 最后

本期的周刊排版有了一些新变化，主要是：

- 关于部分移到了文章顶部，新增了 RSS 链接，去掉了掘金的链接（以后周刊不在掘金发布了）。
- 增加了一个头条的栏目（不一定每期都有），主要会对我最近的好文章进行展示。

最后的最后，祝大家圣诞节快乐，新年快乐。（下周放假，也许停发一周）
