---
id: mixing-and-filtering
title: 混合与过滤
group: 岗位
order: 75
source: ServerInfo/Guidebook/Engineering/MixingAndFiltering.xml
---

# 混合与过滤

<entity id="GasMixer"></entity>
<entity id="GasFilter"></entity>

## 气体混合器

混合器有两个输入和一个输出，按比例混合气体。缺少任一输入时不会输出错误比例；如果输入压力不足，仍可生成混合气，但输出压力会低于设定值。

体积式混合器按压力而非摩尔数工作，输入温度不同会改变最终摩尔比。摩尔式混合器则严格按用户比例混合，不受温度影响，但某输入不足时会变慢。

<entity id="GasMixer" caption="体积式混合器"></entity>
<entity id="GasMolarMixer" caption="摩尔式混合器"></entity>

## 气体过滤器

<entity id="GasFilter"></entity>

过滤器把目标气体从混合物中分离。任一输出堵塞时，整个过滤器会停止。可用于清除废气和把纯气送入回收管网。
