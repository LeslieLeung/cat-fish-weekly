---
issue: 4
date: 2023-12-03
---

## 文章

### 重试——常见重试策略的可交互研究（[原文](https://encore.dev/blog/retries)）

文章介绍了一些常见的重试策略，及其对服务端的影响，包括

- 直接重试
- 有延迟的重试
- 指数退避重试
- 增加随机抖动的重试

到目前为止看起来都是一片正常的技术文章，真正让它超神的是，作者做了一个可交互的组件来让读者直观地感受不同参数的效果。这其实跟以动画形式展示算法运行过程很像，不过我真的很惊奇有人做了一套这样的组件来展示重试策略，实在是泰酷辣！

![](http://img.ameow.xyz/202312031630983.png)

## 不要使用 requirements.txt（[原文](https://quanttype.net/posts/2023-10-31-do-not-use-requirements.txt.html)）

作者认为如果你使用 python 开发后端程序，就不应该再使用用 pip 和 requirements.txt 来管理依赖了，应该使用 poetry。pip 不支持 lock 文件和自动虚拟环境管理。

python 的环境和依赖管理一直是噩梦，经常出现拿到的项目代码因为环境等问题跑不通的问题，因此我最近也转到 poetry 去了。加餐：如果你也是喜欢在 commit 前格式化代码的强迫症，这里还有一篇[文章](https://sam.hooke.me/note/2023/09/poetry-pre-commit-hooks/)介绍怎么把 isort 和 black 集成到 poetry 里。

### 我们买了一颗国产卫星（[视频](https://www.bilibili.com/video/BV1Ec411z7j2)）

无限进步！这个团队真的太燃了。

## 项目

### [msgbyte/tailchat](https://github.com/msgbyte/tailchat)

[![msgbyte/tailchat - GitHub](https://gh-card.dev/repos/msgbyte/tailchat.svg)](https://github.com/msgbyte/tailchat)

一个可自建的 Discord 替代。看起来已经非常可用了，可惜没有 macOS 和 iOS 的原生客户端。

### [jaywcjlove/reference](https://github.com/jaywcjlove/reference)

[![jaywcjlove/reference - GitHub](https://gh-card.dev/repos/jaywcjlove/reference.svg)](https://github.com/jaywcjlove/reference)

一个可自建的 cheatsheet。

我修改精简了一下，做了一个镜像站：[参考.牛马.开发](https://ref.niuma.dev)。

## 工具

### roadmap.sh

官网链接：[Developer Roadmaps - roadmap.sh](https://roadmap.sh/)

关注这个网站很久了，最近发现它新增了一个创建自己的 roadmap 的功能，适合用来规划自己的学习路线，也可以分享学习路线给别人。网站本身有主流的方向的学习路线，例如前后端、移动端、游戏开发等，值得一看。

![](http://img.ameow.xyz/202312031624824.png)

### GitHub 项目可视化

官网链接：[GitHub Next | Visualizing a Codebase](https://githubnext.com/projects/repo-visualization/)

通过将项目结构平铺的方式展示，更加方便地查找项目代码，方便看大型开源项目。网页中提供了一个小测试，通过传统的树形文件夹方式查找 facebook/create-react-app 中 react-dev-utils 的测试用例，我对前端并不熟悉，还是小花了一段时间，但是通过这个可视化的图，不出几秒就找到了。

![](http://img.ameow.xyz/202312031625090.png)

### Regex.ai

官网链接：[Regex.ai - Artificial Intelligence Regular Expression Generator](https://regex.ai/)

一个利用 AI 生成正则表达式的工具，可以输入多行结果以及高亮需要提取的部分，输出正则表达式。

不过体验下来，如果输入的文本中含有特殊字符等好像就不行了，正则其实也不难学，建议还是自己写吧（x）。

## 想法

### 开放世界探索和系统性学习

从高中迈入大学再到进入职场可能会有这么一个感觉：怎么东西怎么都学不完，怎么没办法“系统性”学习一个东西。原因应该是，读书的时候，你学习的路线是别人规划好的，每人都差不多一样，就是考试大纲。到大学甚至工作之后，每个人的路线就差异化了，可能你做后端，他做前端；方向又可以细分，例如应用开发和底层开发等等，每个细分方向需要学习和掌握的知识都不尽相同。如果将所有的知识点看成一棵技能树，那就是在设定上就不可能有人能点满所有的技能（受制于时间和精力），你需要有选择性地横向或纵向拓展。

### 对简体中文开发者社区的失望

这周掘金热榜第二有一篇文章，到发稿时已经有 6.5k 浏览，用一篇文章的篇幅介绍了如何使用 IDEA 的 git GUI 实现以下简单的命令：

```bash
git reset --hard && git push --force
```

我很难理解为什么这样一篇垃圾文章能够冲上热榜，是因为简中程序员对 git 的了解仅限于 pull，commit 和 push？（这可能是真的，在工作中经常碰到三五年经验的程序员，连 cherry-pick 这种操作都没听说过，还在手动挑代码）而且这篇文章毫无深度可言，到最后都没说明白其实这个 GUI 上的操作实现了 git 上的什么东西，知其然不知其所以然。

## 关于

> 这是猫鱼周刊的第 4 期，本系列每周日更新，主要内容为每周收集内容的分享，同时发布在
>
> 博客：[阿猫的博客-猫鱼周刊](https://ameow.xyz/categories/weekly)
> 掘金(beta)：[猫鱼周刊 - 3verest 的专栏 - 掘金](https://juejin.cn/column/7302415204927012918)
> 邮件订阅：[猫鱼周刊](https://quaily.com/ameow)
> Discord：[猫兄的和谐号高铁](https://discord.gg/5G5Nbtuz)
> 私信：[leslieleung@pm.me](mailto:leslieleung@pm.me)
