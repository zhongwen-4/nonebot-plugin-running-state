<div align="center">
<a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
<br>
<p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-running-state

_✨ 一个获取服务器状态的插件 ✨_

![GitHub Tag](https://img.shields.io/github/v/tag/zhongwen-4/nonebot-plugin-running-state)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/zhongwen-4/nonebot-plugin-running-state/pypi-publish.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/zhongwen-4/nonebot-plugin-running-state)
![PyPI - Version](https://img.shields.io/pypi/v/nonebot-plugin-running-state?logo=python)
![Static Badge](https://img.shields.io/badge/python-3.10%2B-brightgreen?logo=python)

<a href="https://11.onebot.dev">
    <img alt="Static Badge" src="https://img.shields.io/badge/OneBot-V11-%23EEE685?style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABABAMAAABYR2ztAAAAIVBMVEUAAAAAAAADAwMHBwceHh4UFBQNDQ0ZGRkoKCgvLy8iIiLWSdWYAAAAAXRSTlMAQObYZgAAAQVJREFUSMftlM0RgjAQhV+0ATYK6i1Xb+iMd0qgBEqgBEuwBOxU2QDKsjvojQPvkJ/ZL5sXkgWrFirK4MibYUdE3OR2nEpuKz1/q8CdNxNQgthZCXYVLjyoDQftaKuniHHWRnPh2GCUetR2/9HsMAXyUT4/3UHwtQT2AggSCGKeSAsFnxBIOuAggdh3AKTL7pDuCyABcMb0aQP7aM4AnAbc/wHwA5D2wDHTTe56gIIOUA/4YYV2e1sg713PXdZJAuncdZMAGkAukU9OAn40O849+0ornPwT93rphWF0mgAbauUrEOthlX8Zu7P5A6kZyKCJy75hhw1Mgr9RAUvX7A3csGqZegEdniCx30c3agAAAABJRU5ErkJggg==">
</a>
<a target="_blank" href="https://qm.qq.com/cgi-bin/qm/qr?k=Uw7I6zuHfpRfXlwddRqDbyE10MZnB4iB&jump_from=webapi&authKey=tp4LiunKcl44e+1gKEag50kyemidx/xV5a9aqdXkn9t9C9bvj18bdd2EBciZmVBt">
    <img alt="Static Badge" src="https://img.shields.io/badge/QQ%E7%BE%A4-814190174-%23EEE685?style=flat-square&logo=tencentqq">
</a>
</div>

## 📖 介绍

状态插件，用于获取机器人和服务器的当前状态。

> [!WARNING]
> 这个插件只在Lagrange协议端上测试过，其他协议端可能会出现KeyError错误？

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-running-state

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-running-state
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-running-state
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-running-state
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-running-state
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_running_state"]

</details>

## 🎉 使用
### 指令表
| 指令 | 权限 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| 状态 | 所有人都可以用 | 否 | 群聊和私聊都可以 | 记得加前缀哦 |
