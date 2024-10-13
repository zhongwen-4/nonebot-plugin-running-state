<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">
## 📖 介绍

状态插件，用于获取机器人和服务器的当前状态。
> [!WARNING]
> 这个插件只在Lagrange协议端上测试过，其他协议端可能会出现KeyError错误？

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-running_state

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-running_state
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-running_state
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-running_state
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-running_state
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_running_state"]

</details>

## 🎉 使用
### 指令表
| 指令 | 权限 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| 状态 | 所有人都可以用 | 否 | 群聊和私聊都可以 | 记得加前缀哦 |