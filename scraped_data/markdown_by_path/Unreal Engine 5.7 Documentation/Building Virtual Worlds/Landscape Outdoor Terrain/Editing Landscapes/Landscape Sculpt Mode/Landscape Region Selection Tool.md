<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-region-selection-tool-in-unreal-engine?application_version=5.7 -->

# Landscape Region Selection Tool

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
5. [Building Virtual Worlds](/documentation/en-us/unreal-engine/building-virtual-worlds-in-unreal-engine "Building Virtual Worlds")
6. [Landscape Outdoor Terrain](/documentation/en-us/unreal-engine/landscape-outdoor-terrain-in-unreal-engine "Landscape Outdoor Terrain")
7. [Editing Landscapes](/documentation/en-us/unreal-engine/editing-landscapes-in-unreal-engine "Editing Landscapes")
8. [Landscape Sculpt Mode](/documentation/en-us/unreal-engine/landscape-sculpt-mode-in-unreal-engine "Landscape Sculpt Mode")
9. Landscape Region Selection Tool

# Landscape Region Selection Tool

This is an overview of the Region Selection tool.

![Landscape Region Selection Tool](https://dev.epicgames.com/community/api/documentation/image/9096cd01-11dd-4bf3-a226-9585b14d687f?resizing_type=fill&width=1920&height=335)

 On this page

The **Region Selection** tool selects regions of the Landscape using the current brush settings and the tool strength to be used to fit a Landscape [gizmo](/documentation/en-us/unreal-engine/landscape-copy-tool-in-unreal-engine) to a
specific area or to act as a mask for copying data to, or pasting data from, a gizmo.

## Using the Region Selection Tool

In this example, the Region Selection tool has been used to paint an area of the Landscape using the default positive method, then switching to the negative mask method that enables you to paint areas that
don't want to include, and finally showing the Use Region As Mask section that captures the entirety of a Landscape component that is painted rather than just areas within it.

Use the following controls to paint areas that can be used for selection by doing the following:

| **Controls** | **Operation** |
| --- | --- |
| **Left Mouse Button** | Adds to the selected region. |
| **Shift + Left Mouse Button** | Removes from the selected region. |

![Without Selection](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2d6a6dc8-e0fc-42cf-8937-9daabd70fee5/01-without-selection.png "Without Selection")

![With Selection](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b9251b8f-fab9-4fb7-a7c3-ebb32512d12d/02-with-selection.png "With Selection")

Without Selection

With Selection

In this example, an area has been painted for selection that can then be used for masking layers or with the Copy/Paste tool.

## Tool Settings

|  |  |
| --- | --- |
| Landscape Select button | Selection tool properties |

| **Property** | **Description** |
| --- | --- |
| **Clear Region Selection** | Clears the current selected region(s). |
| **Tool Strength** | Controls how much effect each brush stroke has. |
| **Use Region as Mask** | When checked, the region selection acts as a mask with the active area being comprised of the selected region. |
| Region Selection |  |
| **Negative Mask** | When checked, and when **Use Region as Mask** is also checked, the region selection acts as a mask, but the active area is comprised of the unselected region. |
| Region Mask Negative Selection |  |

* [landscape](https://dev.epicgames.com/community/search?query=landscape)
* [region](https://dev.epicgames.com/community/search?query=region)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Using the Region Selection Tool](/documentation/en-us/unreal-engine/landscape-region-selection-tool-in-unreal-engine?application_version=5.7#usingtheregionselectiontool)
* [Tool Settings](/documentation/en-us/unreal-engine/landscape-region-selection-tool-in-unreal-engine?application_version=5.7#toolsettings)
