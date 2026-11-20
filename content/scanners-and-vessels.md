---
id: scanners-and-vessels
title: 扫描器与收容容器
group: 异常研究
order: 20
source: ServerInfo/Guidebook/Science/ScannersAndVessels.xml
---

# 异常扫描器

异常扫描器（Anomaly Scanner）用来收集异常信息，通常可以在科研部的储物柜中找到。

<entity id="AnomalyScanner"></entity>

扫描异常会显示严重度、总体稳定性、大致的点数产出、异常对各类粒子的反应，以及距离下一次脉冲的时间。粒子的反应类型可以与异常粒子发射器配合使用，从而操控异常。

# 异常收容容器

异常收容容器（Anomaly Vessel）是一台利用异常产生研究点（Research Points）的设备。先使用异常扫描器扫描异常，再对空容器使用扫描器，即可把最近扫描的异常同步到容器。

<entity id="MachineAnomalyVessel"></entity>

容器每秒产生的点数取决于异常的严重度、稳定性和生命值。这三项数值越高，点数产出越高。

注意：异常一旦进入**超临界（Supercritical）**，与其连接的收容容器会爆炸，并可能破坏空间站和附近设备。
