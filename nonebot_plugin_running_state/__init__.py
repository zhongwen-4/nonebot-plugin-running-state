from nonebot import on_command, require, get_driver, get_adapters, on_message, get_bots
import platform, psutil, time, json,  asyncio
from typing import Any
from nonebot import __version__

require("nonebot_plugin_localstore")
import nonebot_plugin_localstore as localstore
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, MessageSegment, Message
from nonebot.adapters import Bot as adapter_bot
from nonebot.plugin import PluginMetadata
__plugin_meta__ = PluginMetadata(

    name="运行状态",
    description="基于 NoneBot和Lagrange.OneBot 的运行状态插件",
    usage= "发送['状态', '系统状态', 'zt', 'status'] 其中一个即可获取",
    type="application",
    homepage="https://github.com/zhongwen-4/nonebot-plugin-running-state",
    supported_adapters={"~onebot.v11"}

)

path = localstore.get_plugin_data_dir()
path= f"{path}/data.json"
driver = get_driver()
state = on_command("状态", aliases= {"系统状态", "zt", "status"})
get_msg = on_message()


def jw(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def jr(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


@driver.on_bot_connect
async def on_bot_connect(bot: Bot):
    data = jr(path)
    data["bot_connect"]= time.time()
    jw(path, data)


@driver.on_startup
async def on_startup():
    try:
        data = jr(path)
        data["bot_startup"]= time.time()
        jw(path, data)
    except FileNotFoundError:
        data = {}
        data["bot_startup"]= time.time()
        jw(path, data)
        

def get_time(t):
    total_seconds = int(round(t))
    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    if t < 60:
        return f"{seconds:02}秒"
    if t < 3600:
        return f"{minutes:02}分{seconds:02}秒"
    if t < 86400:
        return f"{hours:02}时{minutes:02}分{seconds:02}秒"
    else:
        return f"{days:02}天{hours:02}时{minutes:02}分{seconds:02}秒"
    

@get_msg.handle()
async def get_msg_handle(event: GroupMessageEvent):
    data = jr(path)
    if "get_msg" not in data:
        data["get_msg"] = 1
        jw(path, data)
    
    else:
        data["get_msg"] += 1
        jw(path, data)
    
    await get_msg.finish()


@adapter_bot.on_calling_api
async def handle_api_call(bot: adapter_bot, api: str, data: dict[str, Any]):

    if api == "send_msg":
        date = jr(path)
        if "send_msg" not in date:
            date["send_msg"] = 1
            jw(path, date)
        else:
            date["send_msg"] += 1
            jw(path, date)


@driver.on_shutdown
async def do_something():
    data = jr(path)
    if "get_msg" and "send_msg" in data:
        del data["get_msg"]
        del data["send_msg"]
        jw(path, data)


@state.handle()
async def state_handle(bot: Bot, event: GroupMessageEvent):

    # t = time.time()    # 这个东西是输出耗时的必要变量，一般做调试用

    data = jr(path)
    msg_list = Message()
    pid_info = Message()
    await state.send("骚等, 系统状态加载中...")

    platform_info = platform.platform()    # 获取系统信息

    cpu_count_logical = psutil.cpu_count(logical=True) # 获取CPU逻辑核心数
    cpu_count_physical = psutil.cpu_count(logical=False) # 获取CPU物理核心数

    cpu_usage_percent = psutil.cpu_percent() # 获取CPU使用率
    await asyncio.sleep(1)
    cpu_usage_percent = psutil.cpu_percent()

    pids = len(psutil.pids())    # 获取进程数量
    msg_list += MessageSegment.text("----CPU信息----\n")
    msg_list += MessageSegment.text(f"逻辑核心数: {cpu_count_logical}\n物理核心数: {cpu_count_physical}\n使用率: {cpu_usage_percent}%\n已使用进程数: {pids}\n\n")

    mem_info = psutil.virtual_memory()    # 获取内存信息
    total_memory = mem_info.total    # 获取内存总大小
    available_memory = mem_info.available    # 获取内存剩余大小
    mem_usage_percent = mem_info.percent    # 获取内存使用率
    msg_list += MessageSegment.text("----内存信息----\n")
    msg_list += MessageSegment.text(f"总内存: {total_memory / (1024 ** 3):.2f} GB\n剩余内存: {available_memory / (1024 ** 3):.2f} GB\n使用率: {mem_usage_percent}%\n\n")

    net_io = psutil.net_io_counters()    # 获取网络信息
    net_sent = net_io.bytes_sent    # 获取发送流量
    bytes_recv = net_io.bytes_recv    # 获取接收流量
    packets_sent = net_io.packets_sent    # 获取发送包数
    packets_recv = net_io.packets_recv    # 获取接收包数
    msg_list += MessageSegment.text("----网络信息----\n")
    msg_list += MessageSegment.text(f"发送流量: {net_sent / (1024 ** 2):.2f} MB\n接收流量: {bytes_recv / (1024 ** 2):.2f} MB\n发送包数: {packets_sent}\n接收包数: {packets_recv}\n\n")

    disk_partitions = psutil.disk_partitions()    # 获取磁盘信息
    msg_list += MessageSegment.text("----磁盘信息----\n")

    if platform.system() == "Windows": # 如果是Windows系统
        if len(disk_partitions) <= 2:    # 如果磁盘数量小于等于2
            for partition in disk_partitions:
                msg_list += MessageSegment.text(f"盘符: {partition.mountpoint}\n")
                msg_list += MessageSegment.text(f"文件系统类型{partition.fstype}\n")
                if partition.opts:
                    msg_list += MessageSegment.text(f"文件系统选项{partition.opts}\n")
                disk_usage = psutil.disk_usage(partition.mountpoint)
                msg_list += MessageSegment.text(f"总大小: {disk_usage.total / (1024 ** 3):.2f} GB\n已使用: {disk_usage.used / (1024 ** 3):.2f} GB\n剩余: {disk_usage.free / (1024 ** 3):.2f} GB\n使用率: {disk_usage.percent}%\n\n")

        else:
            disk_usage = psutil.disk_usage("/")
            msg_list += MessageSegment.text(f"总大小: {disk_usage.total / (1024 ** 3):.2f} GB\n已使用: {disk_usage.used / (1024 ** 3):.2f} GB\n剩余: {disk_usage.free / (1024 ** 3):.2f} GB\n使用率: {disk_usage.percent}%\n\n")

    if platform.system() == "Linux":    # 如果是Linux系统
        disk_usage = psutil.disk_usage("/")
        msg_list += MessageSegment.text(f"总大小: {disk_usage.total / (1024 ** 3):.2f} GB\n已使用: {disk_usage.used / (1024 ** 3):.2f} GB\n剩余: {disk_usage.free / (1024 ** 3):.2f} GB\n使用率: {disk_usage.percent}%\n\n")

    boot_time = psutil.boot_time()    # 获取系统启动时间
    boot_time = time.time() - int(boot_time)   # 计算系统运行时间
    boot_time = get_time(boot_time)
    bot_connect = time.time() - data["bot_connect"]    # 计算bot连接时长
    bot_connect = get_time(bot_connect)
    bot_startup = time.time() - data["bot_startup"]    # 计算实例启动时长
    bot_startup = get_time(bot_startup)
    msg_list += MessageSegment.text(f"----系统信息----\n")
    msg_list += MessageSegment.text(f"系统启动时间: {boot_time} \nbot连接时长: {bot_connect} \n实例启动时长: {bot_startup} \n系统名称: {platform_info}\n\n")

    app = await bot.get_version_info()    # 获取协议端的版本信息
    ver = app["app_version"]
    app_name = app["app_name"]
    nt_protocol = app["nt_protocol"]
    python_version = platform.python_version()    # 获取python版本
    env = driver.config.driver    # 获取驱动器信息
    adapter = get_adapters()    # 获取适配器信息
    adapter = [i for i in adapter]    # 鉴于可能存在多个适配器, 直接返回列表
    msg_list += MessageSegment.text(f"----运行环境----\nPython版本: {python_version}\n驱动器信息: {env}\n适配器信息: {adapter}\nNoneBot版本号: {__version__}\n协议端名称: {app_name}\n协议端版本号: {ver}\n使用协议: {nt_protocol}\n\n")
    user_info = await bot.get_group_member_info(group_id= event.group_id, user_id= event.user_id)

    a = []
    for i in psutil.process_iter():
        pinfo = i.as_dict(attrs = ['pid', 'name', 'memory_percent', 'cpu_percent'])
        a.append(pinfo)
    b = sorted(a, key = lambda i:i['memory_percent'], reverse = True)

    pid_info += MessageSegment.text("----进程信息----\n")
    for i in b[:10]:
        pid_info += MessageSegment.text(f"PID: {i['pid']}\n进程名: {i['name']}\nCPU使用率: {i['cpu_percent']}%\n内存使用率: {i['memory_percent']:.2f}%\n-----------------\n")

    try:
        a = data["get_msg"]
        b = data["send_msg"]
    except KeyError:
        a = 0
        b = 0

    bots = get_bots()
    bots = [i for i in bots]
    msg_list += MessageSegment.text(f"----Bot----\n收: {a}条\n发: {b}条\n在线账号共: {len(bots)}个\n账号列表: {bots}")

    for i in bots:
        name = await bot.call_api("get_stranger_info", user_id = i)
        nickname = name["nickname"]
        level = name["level"]
        age = name["age"]
        msg_list += MessageSegment.text(f"\n账号昵称: {nickname}\n账号等级: {level}\n账号年龄: {age}")

    msg = [
        MessageSegment.node_custom(
        user_id= user_info["user_id"],
        nickname= user_info["nickname"],
        content= msg_list
        ),
        MessageSegment.node_custom(
        user_id= user_info["user_id"],
        nickname= user_info["nickname"],
        content= pid_info
        )
    ]
    
    res_id = await bot.call_api("send_forward_msg", messages= Message(msg))
    await state.send(Message(MessageSegment.forward(res_id)))

    #todo 以下内容是输出耗时用的
    # t = time.time() -t
    # await state.finish(f"耗时: {t:.2f}s")