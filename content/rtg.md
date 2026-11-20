---
id: rtg
title: 放射性同位素热电发电机（RTG）
group: 岗位
order: 47
source: ServerInfo/Guidebook/Engineering/RTG.xml
---

# 放射性同位素热电发电机（RTG）

<entity id="GeneratorRTG" caption="RTG"></entity>

RTG 利用放射性同位素衰变被动发电，无需维护，适合通讯、AI 和船员监控服务器等必须持续供电的系统。

RTG 固定输出 `GeneratorRTG.PowerSupplier.MaxSupply` W，必须接入 HV [电网](VoltageNetworks)。通常只能通过打捞远征找到。

## 受损 RTG

<entity id="GeneratorRTGDamaged" caption="受损 RTG"></entity>

严重受损后会变为放射性 RTG，发电方式不变但会产生辐射。可把辐射收集器放在附近，把辐射转化为额外电力。
