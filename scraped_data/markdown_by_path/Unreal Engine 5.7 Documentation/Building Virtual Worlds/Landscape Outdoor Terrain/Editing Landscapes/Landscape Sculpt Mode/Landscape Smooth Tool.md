<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-smooth-tool-in-unreal-engine?application_version=5.7 -->

# Landscape Smooth Tool

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
9. Landscape Smooth Tool

# Landscape Smooth Tool

This is an overview of the Smooth painting tool.

![Landscape Smooth Tool](https://dev.epicgames.com/community/api/documentation/image/4adbf390-e117-4c17-8e49-3a281ee043b7?resizing_type=fill&width=1920&height=335)

 On this page

The **Smooth** tool will soften the heightmaps painted values to give your Landscape a smoother flow and appearance by getting rid of jagged artifacts that can sometimes happen after using the Sculpting or Erosion tools.

## Using the Smooth Tool

In this example, the Smooth tool is used to soften some of the harder edge artifacts that can happen when using the various Landscape tools.

Use the following controls to sculpt your Landscape heightmap:

| **Controls** | **Operation** |
| --- | --- |
| **Left Mouse Button** | Smoothens and softens the heightmap or selected layer's weight. |

![Before Smoothing](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/41c71c1a-58e9-4288-94c9-d248b88b3109/01-before-smoothing.png "Before Smoothing")

![After Smoothing](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/58b09cba-9614-4542-8994-8923f8d2d68a/02-after-smoothing.png "After Smoothing")

Before Smoothing

After Smoothing

The Brush Strength determines the amount of smoothing that can happen when using the Smooth tool.

## Tool Settings

|  |  |
| --- | --- |
| Landscape Smooth Button | Smooth Tool Properties |

| **Property** | **Description** |
| --- | --- |
| **Tool Strength** | Controls how much smoothing occurs with each brush stroke. |
| **Filter Kernel Scale** | Sets the scale multiplier for the smoothing filter kernel for the radius that smoothing will be performed over. Higher values smooth out bigger details, while lower values only smooth out smaller details. |
| **Detail Smooth** | If checked, performs a detail-preserving smoothing using the specified detail-smoothing value. Larger-detail smoothing values remove more details, while smaller values preserve more details. |

* [landscape](https://dev.epicgames.com/community/search?query=landscape)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Using the Smooth Tool](/documentation/en-us/unreal-engine/landscape-smooth-tool-in-unreal-engine?application_version=5.7#usingthesmoothtool)
* [Tool Settings](/documentation/en-us/unreal-engine/landscape-smooth-tool-in-unreal-engine?application_version=5.7#toolsettings)
