<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-erosion-tool-in-unreal-engine?application_version=5.7 -->

# Landscape Erosion Tool

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
9. Landscape Erosion Tool

# Landscape Erosion Tool

This is an overview of the Erosion painting tool.

![Landscape Erosion Tool](https://dev.epicgames.com/community/api/documentation/image/10a2f1c2-5e71-4f2f-976a-55e016500c31?resizing_type=fill&width=1920&height=335)

 On this page

The **Erosion** tool uses a thermal erosion simulation to adjust the height of the Landscape heightmap. This simulates the transfer of soil from higher elevations to lower elevations by natural forces. The
larger the difference in elevation, the more erosion will occur. This tool also applies a noise effect on top of the erosion, if desired, to provide a more natural random appearance.

## Using the Erosion Tool

In the example above, the Erosion tool is being used on the front and back sides of the mountain face. On the front side, the incline is not as steep, so the surface is not eroded as quickly with the
settings being used. However, on the back side, the incline is much steeper and erodes much more quickly.

Use the following controls to sculpt with Erosion for your Landscape heightmap:

| Controls | Operation |
| --- | --- |
| **Left Mouse Button** | Applies erosion values that raises, lowers, or does both to the heightmap. |

![Before](https://dev.epicgames.com/community/api/documentation/image/658faee4-9676-4976-b02b-62b7c4738d22?resizing_type=fit&width=1920&height=1080)

![After](https://dev.epicgames.com/community/api/documentation/image/a71396dd-95f0-4b89-a117-b9e988a59720?resizing_type=fit&width=1920&height=1080)

Before

After

In the example above, Erosion is used to smooth out the more jagged regions of a hill that is being sculpted using the Sculpt tool and an alpha brush. Erosion uses noise painted onto the hillside to raise or lower the surface giving it variations in different heights based on the strength and various property values that are used.

## Tool Settings

|  |  |
| --- | --- |
| [Erosion Tool](https://dev.epicgames.com/community/api/documentation/image/f44af721-effa-4c78-b2df-228b085ee687?resizing_type=fit) | [Erosion Tool Properties](https://dev.epicgames.com/community/api/documentation/image/3f59aaa0-a82c-44b8-892e-6ef1a5f7a584?resizing_type=fit) |

| Property | Description |
| --- | --- |
| **Tool Strength** | Controls how much effect each brush stroke has. |
| **Combined Layers Operation** | Uses the combined result of all underlying Edit Layers, when checked. |
| **Threshold** | The minimum height difference necessary for the erosion effects to be applied. Smaller values will result in more erosion being applied. |
| **Surface Thickness** | The thickness of the surface for the layer weight erosion effect. |
| **Iterations** | The number of iterations performed. Larger values result in more levels of erosion. |
| **Noise Mode** | Whether to apply noise to raise or lower the heightmap, or do both:   * **Both**: Raises and lowers values for all erosion effects applied to the heightmap. * **Raise**: Applies erosion effects that result in raising the heightmap. * **Lower**: Applies erosion effects that result in lowering the heightmap. |
| **Noise Scale** | The size of the noise filter used. The noise filter is related to position and scale, which means if you do not change **Noise Scale**, the same filter is applied to the same position many times. |
| **Use Layer Hardness** | Determines whether the tool should take into account the layer's hardness parameter. |

* [landscape](https://dev.epicgames.com/community/search?query=landscape)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Using the Erosion Tool](/documentation/en-us/unreal-engine/landscape-erosion-tool-in-unreal-engine?application_version=5.7#using-the-erosion-tool)
* [Tool Settings](/documentation/en-us/unreal-engine/landscape-erosion-tool-in-unreal-engine?application_version=5.7#tool-settings)
