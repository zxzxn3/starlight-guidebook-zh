---
id: pipenets
title: 管网
group: 岗位
order: 80
source: ServerInfo/Guidebook/Engineering/PipeNetworks.xml
---

# 管网

管网是一组承担共同任务的互联[管道](Pipes)，例如配气网络和废气管网。

<entity id="GasPipeStraight"></entity>
<entity id="GasPipeHalf"></entity>
<entity id="GasPipeBend"></entity>
<entity id="GasPipeTJunction"></entity>
<entity id="GasPipeFourway"></entity>
<entity id="GasPressurePump"></entity>
<entity id="GasVolumePump"></entity>

管网在模拟中被视为一个整体容积。泵改变压力会影响整个管网，而不只旁边一节管道。

泵、混合器、过滤器、阀门和散热器等设备会分隔管网。停泵或断电时不会允许气体通过。
