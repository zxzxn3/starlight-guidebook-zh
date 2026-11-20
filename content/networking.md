---
id: networking
title: 网络连接
group: 岗位
order: 52
source: ServerInfo/Guidebook/Engineering/Networking.xml
---

# 网络连接

空间站设备需要彼此通讯，例如空气警报连接通风口、洗涤器和传感器，气闸彼此联动。

连接系统分为 Link 和 List。可用多用工具或网络配置器操作，按 <kbd>AltActivateItemInHand</kbd> 切换模式，或悬停设备后按 <kbd>AltActivateItemInWorld</kbd>。

<entity id="Multitool"></entity>
<entity id="NetworkConfigurator"></entity>

部分连接需要权限，例如连接空气警报需要大气权限，连接气闸需要该气闸权限。

## Link 系统

Link 用于明确连接两台设备，例如把一扇门连到另一扇门或按钮。

<entity id="AirlockExternal"></entity>
<entity id="AirlockEngineering"></entity>
<entity id="BlastDoor"></entity>
<entity id="SignalButton"></entity>

设备端口分输入和输出。悬停端口可查看信号触发条件或收到信号后的行为。

## List 系统

List 把多台设备连接到一台主设备，例如把多个大气设备连接到空气警报。

<entity id="AirAlarm"></entity>
<entity id="GasVentPump"></entity>
<entity id="GasVentScrubber"></entity>
<entity id="AirSensor"></entity>
<entity id="Firelock"></entity>

对设备按 <kbd>Use</kbd> 可把其地址保存到工具。再对主设备按 <kbd>Use</kbd> 打开界面：

- **Set**：用工具中的列表覆盖当前列表。
- **Add**：加入当前列表。
- **Clear**：清除全部连接。
- **Copy**：复制当前列表到工具。
- **Show**：显示主设备与所有连接设备之间的连线。

对工具按 <kbd>Use</kbd> 或按 <kbd>ActivateItemInHand</kbd> 可查看并清除已保存设备。
