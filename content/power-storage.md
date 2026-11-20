---
id: power-storage
title: 电力储存
group: 岗位
order: 50
source: ServerInfo/Guidebook/Engineering/PowerStorage.xml
---

# 电力储存

由于[电力爬坡](Ramping)，需要储能设备削平功率峰谷并应对赤字。

## SMES

SMES 能储存大量电力并快速释放。

<entity id="SMESBasic"></entity>

向指向 SMES 的电缆端子输入 HV 电力即可充电。SMES 从端子取电，再从下方电缆输出；端子确保输入和输出不会直接连通。

<entity id="CableTerminal"></entity>
<entity id="CableHV" caption="输出"></entity>
<entity id="CableHV" caption="输入"></entity>

标准 SMES 储存 `SMESBasic.Battery.MaxCharge` J，最大输出 `SMESBasic.PowerNetworkBattery.MaxSupply` W。满电后会直接向输出端输电；出现缺口时自动补充。

## 高级 SMES

<entity id="SMESAdvanced"></entity>

高级 SMES 储存 `SMESAdvanced.Battery.MaxCharge` J，最大输出 `SMESAdvanced.PowerNetworkBattery.MaxSupply` W，常用于空间站大型储能阵列，为开局启动或长期赤字争取时间。

它仍会耗尽；没有发电源持续补充时，电池会迅速放电。
