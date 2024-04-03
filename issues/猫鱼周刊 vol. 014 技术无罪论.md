---
intro: 猫鱼周刊的第15期，包括关于Flipper的文章和长期运行树莓派的考虑，还有两个项目和一个用来测试RSS的网站。
issue: 15
date: 2024-02-25
---

- [关于本刊](#%E5%85%B3%E4%BA%8E%E6%9C%AC%E5%88%8A)
- [文章](#%E6%96%87%E7%AB%A0)
  - [拯救 flipper](#%E6%8B%AF%E6%95%91%20flipper)
  - [满月时表现完全不同的代码](#%E6%BB%A1%E6%9C%88%E6%97%B6%E8%A1%A8%E7%8E%B0%E5%AE%8C%E5%85%A8%E4%B8%8D%E5%90%8C%E7%9A%84%E4%BB%A3%E7%A0%81)
  - [长期运行树莓派的一些考虑](#%E9%95%BF%E6%9C%9F%E8%BF%90%E8%A1%8C%E6%A0%91%E8%8E%93%E6%B4%BE%E7%9A%84%E4%B8%80%E4%BA%9B%E8%80%83%E8%99%91)
- [项目](#%E9%A1%B9%E7%9B%AE)
  - [readysettech/readyset](#readysettech/readyset)
  - [google/magika](#google/magika)
- [工具/网站](#%E5%B7%A5%E5%85%B7/%E7%BD%91%E7%AB%99)
  - [Lorem RSS](#Lorem%20RSS)
- [最后](#%E6%9C%80%E5%90%8E)

## 关于本刊

> 这是猫鱼周刊的第 15 期，本系列每周日更新，主要内容为每周收集内容的分享，同时发布在
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

### 拯救 flipper

[原文链接](https://saveflipper.ca/)

Flipper Zero 是一个极客用的多用途工具，长得非常像小孩子的玩具。本质上它就是一块 MCU 加上一块屏幕，几个按钮，以及各种射频硬件和接口。

![](https://img.ameow.xyz/202402251656733.png)

由于它开放的特性，加上拥有齐全的硬件，使得它可以作为偷车的工具（通过复制车辆钥匙的信号等方式，不多赘述）。加拿大政府因此决定禁止此类工具，包括 Flipper Zero，在加拿大市场上售卖。

回到文章，有一群人认为此举对底层的技术有误解，纵容了生产商设计不安全的产品，影响了安全相关研究以及会产生司法资源的浪费。目前已经有很多人签名请愿。

> **技术中立原则**（technological neutrality），又名**菜刀理论**，指科学技术或者工具的发明者或销售者，无法控制科技或工具的使用者如何使用该项科技工具，所以他们也不应为意料之外的工具用途来负责。

技术中立原则由索尼与环球电影制片公司在 1984 年的诉讼中引入。简单而言，索尼开发了一款录像机，可以改变观看的时间，快进快退，以及复制节目进行永久保存。环球电影认为此举属于侵权。最终判索尼罪名不成立，详情可以看[维基百科](https://en.wikipedia.org/wiki/Sony_Corp._of_America_v._Universal_City_Studios,_Inc.)。

2016 年快播案中，被告律师也曾提及技术中立原则，快播 CEO 王欣表示快播本身并不提供播放资源，快播的本意并不在传播淫秽视频，传播者是上传视频者，而公司也有相应的监管措施。最终认定该行为构成传播淫秽物品牟利罪，王欣被判处有期徒刑 3 年 6 个月，并处罚金 100 万元。

### 满月时表现完全不同的代码

[原文链接](https://www.hanselman.com/blog/the-code-worked-differently-when-the-moon-was-full)

一个周期性性能下降的 bug，表现是应用周期性地出现性能恶化。

![](https://img.ameow.xyz/202402251724011.png)

排查发现，在 Windows 95 以及一些 POSIX 平台上，一些以毫秒为单位的时间值使用 32 位表示，因此大约只支持 49.7 天。线程池中一个地方使用了这些 32 位的值，因此每隔固定的一段时间就会因为 bug 出现性能问题。

基于时间的 bug 其实很难排查，甚至通过测试也没法测出来。通过增加单测，mock 时间，可以解决一些问题。但这个例子中的可能真的无从下手。

### 长期运行树莓派的一些考虑

[原文链接](https://www.dzombak.com/blog/2023/12/Considerations-for-a-long-running-Raspberry-Pi.html)

虽然树莓派是玩具级别的硬件，但是作者通过优化 wifi 连接、SD 卡读写等等方式，发展出了一套”高可用“树莓派指南。

## 项目

### readysettech/readyset

[![readysettech/readyset - GitHub](https://gh-card.dev/repos/readysettech/readyset.svg?fullname=)](https://github.com/readysettech/readyset)

一个 MySQL 和 Postgres 的中间件，应用无感知地进行查询缓存。一般来说，对性能关键的查询，都会在应用里做一层查询缓存。这个项目把这个从应用代码里解耦出来，通过代理 SQL 请求来实现缓存。

看起来挺厉害的，但是我感觉增加了部署中的复杂度，也增加了薄弱点。非要选用的话，可能需要自己实现一下访问 readyset 失败时降级到访问数据库的逻辑。

### google/magika

[![google/magika - GitHub](https://gh-card.dev/repos/google/magika.svg?fullname=)](https://github.com/google/magika)

判断文件类型有什么方法？一般来说，通过判断文件名后缀，判断文件 MIME 信息，判断文件头的 magic number，这几种方式就能判断出文件真实的类型。但很显然，要绕过这些检测也非常简单，伪造一下对应检测的信息，再把别的内容隐藏在中间就好了。这也是文件类型检测面临的一个网络安全挑战。

谷歌这个团队提出，通过提取文件首尾和中间的一些字节进行深度学习，分类出文件的类型。这个模型达到了 99%+的准确率和召回率，推理的过程也非常快。

我猜测这个方式可行的原因是，文件的组成是有标准的，例如 [mp4](https://en.wikipedia.org/wiki/MP4_file_format)，因此数据封装的格式是有规律/特征的。通过这个特征来判断，能够有效地区分出文件的格式。如果区分不出来，那就判断文件内容是否人类可读(human readable)，如果是，那就是纯文本，否则就是二进制文件。

## 工具/网站

### Lorem RSS

[网站链接](https://lorem-rss.herokuapp.com/)

一个用来测试 RSS 的网站，可以设置指定的间隔刷新。

## 最后

GitHub TOP 5k 项目的贡献者可领取价值 $200 空投，建议大家到 https://provisions.starknet.io 看一下自己是否符合资格领取，到手可以参考[这篇帖子](https://v2ex.com/t/1017287)卖出换成法币。我自己是领到了 111.1 的大保底，加上卖的比较早，价值大概 230 刀。

同时由于这个事件，近期针对 GitHub 账号的骗局也比较多。由于符合资格者的 ID 相当于是公开了，产生了很多有针对性地骗账号场景（尤其是分配了价值几千美元的 ID）。
