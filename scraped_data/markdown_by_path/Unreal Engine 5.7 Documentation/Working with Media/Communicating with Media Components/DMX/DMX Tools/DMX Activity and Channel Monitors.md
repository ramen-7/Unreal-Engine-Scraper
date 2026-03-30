<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/dmx-activity-and-channel-monitors-in-unreal-engine?application_version=5.7 -->

# DMX Activity and Channel Monitors

1. ![Epic Games](https://edc-cdn.net/assets/images/logo-epic.svg)[Developer](/)
2. [Documentation](/documentation/ "Documentation")
3. Unreal Engine
   * [Unreal Engine](/documentation/en-us/unreal-engine)
   * [Fortnite](/documentation/en-us/fortnite)
   * [Twinmotion](/documentation/en-us/twinmotion)
   * [MetaHuman](/documentation/en-us/metahuman)
   * [RealityScan](/documentation/en-us/realityscan)
   * [RealityScan Mobile](/documentation/en-us/realityscan-mobile)
   * [Fab](/documentation/en-us/fab)
4. [Unreal Engine 5.7 Documentation](/documentation/en-us/unreal-engine/unreal-engine-5-7-documentation "Unreal Engine 5.7 Documentation")
5. [Working with Media](/documentation/en-us/unreal-engine/working-with-media-in-unreal-engine "Working with Media")
6. [Communicating with Media Components](/documentation/en-us/unreal-engine/communicating-with-media-components-from-unreal-engine "Communicating with Media Components")
7. [DMX](/documentation/en-us/unreal-engine/dmx-in-unreal-engine "DMX")
8. [DMX Tools](/documentation/en-us/unreal-engine/dmx-tools-in-unreal-engine "DMX Tools")
9. DMX Activity and Channel Monitors

# DMX Activity and Channel Monitors

Use the DMX Activity and Channel Monitors to track your DMX installations.

![DMX Activity and Channel Monitors](https://dev.epicgames.com/community/api/documentation/image/a26abde4-657e-4b59-892f-98e4cfd57b7d?resizing_type=fill&width=1920&height=335)

 On this page

# Introduction

The **DMX Monitors** are tools to visualize DMX input and output.

# Accessing the DMX Monitors

DMX Monitors are available from the DMX Toolbar menu.

![The DMX monitors in the DMX Toolbar menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c5bf62ee-bf2e-446d-b386-9b9971683994/dmx-monitors-dropdown.png)

A Channel Monitor is also available in the DMX Library's Fixture Patch Editor. It monitors DMX Input only.

![The DMX Monitor in the Fixture Patch Editor.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cfcd30e0-a62c-4034-8466-b8850ff5713e/dmx-fixture-monitor.png)

# Channel Monitor

The monitor displays information when Unreal Engine receives data for the specified universe.

A selection widget provides you with a way to pick which universe to monitor.

![Selecting a universe to monitor with the DMX universe selection widget.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/263f9ee6-ecc8-4f10-bee3-f33ced690be1/dmx-universe-selection.png)

| **Property** | **Description** |
| --- | --- |
| **Monitor All Ports** | If selected, all Input or Output Ports are monitored. |
| **Source** | Select a source to monitor, either all **Inputs** or all **Outputs** when you select **Monitor All Ports**, otherwise you can select a specific Input or Output Port. |
| **Local Universe** | Specifies the local Universe monitored. |
| **Clear DMX Buffers** | Clears all DMX Buffers. This empties the buffers, it does not send zero or default values. |

# Activity Monitor

The **DMX Activity Monitor** is a debugging tool for visualizing DMX input and output across many universes. The activity monitor displays any non-zero DMX value received across the universes it monitors.

![the DMX Activity Monitor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/99ffed4d-1df5-4db9-96bd-7eaa966d8ee3/dmx-activity-monitor.png)

| **Property** | **Description** |
| --- | --- |
| **Monitor All Ports** | If selected, all Input or Output Ports are monitored. |
| **Source** | Select a source to monitor, either all **Inputs** or all **Outputs** when you select **Monitor All Ports**, otherwise you can select a specific Input or Output Port. |
| **Universes** | Selects the range of Universes monitored |
| **Clear DMX Buffers** | Clears all DMX Buffers. This empties the buffers, it does not send zero or default values. |

* [dmx](https://dev.epicgames.com/community/search?query=dmx)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Introduction](/documentation/en-us/unreal-engine/dmx-activity-and-channel-monitors-in-unreal-engine?application_version=5.7#introduction)
* [Accessing the DMX Monitors](/documentation/en-us/unreal-engine/dmx-activity-and-channel-monitors-in-unreal-engine?application_version=5.7#accessingthedmxmonitors)
* [Channel Monitor](/documentation/en-us/unreal-engine/dmx-activity-and-channel-monitors-in-unreal-engine?application_version=5.7#channelmonitor)
* [Activity Monitor](/documentation/en-us/unreal-engine/dmx-activity-and-channel-monitors-in-unreal-engine?application_version=5.7#activitymonitor)
