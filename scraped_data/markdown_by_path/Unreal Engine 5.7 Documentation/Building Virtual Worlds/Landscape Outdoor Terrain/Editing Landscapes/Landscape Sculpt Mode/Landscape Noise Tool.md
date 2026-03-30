<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-noise-tool-in-unreal-engine?application_version=5.7 -->

# Landscape Noise Tool

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
9. Landscape Noise Tool

# Landscape Noise Tool

This is an overview of the Noise painting tool.

![Landscape Noise Tool](https://dev.epicgames.com/community/api/documentation/image/d9244ffd-8971-40a2-826c-09e43b904adb?resizing_type=fill&width=1920&height=335)

 On this page

The **Noise** tool applies a noise filter to produce variations in the surface of the Landscape heightmap.

## Using the Noise Tool

In this example, the Noise tool is used to paint on the Landscape, similarly to how Sculpt would be used. Variations are painted around the area that raise and lower the heightmap based
on the tool settings. This enables you to paint grand or subtle variations into your Landscape.

Use the left mouse button control to sculpt with Noise for your Landscape heightmap:

| Controls | Operation |
| --- | --- |
| **Left Mouse Button** | Heightens or increases the heightmap or selected layer's weight. |

![Before](https://dev.epicgames.com/community/api/documentation/image/d3f76316-9cbd-41c3-9575-938adb6316d5?resizing_type=fit&width=1920&height=1080)

![After](https://dev.epicgames.com/community/api/documentation/image/e5947f11-3c9c-48a6-93cd-7a28c099744f?resizing_type=fit&width=1920&height=1080)

Before

After

In this example, Noise has been painted onto the smooth Landscape surface giving it variations in different heights based on the strength and property values used.

## Tool Settings

|  |  |
| --- | --- |
| [Noise Tool](https://dev.epicgames.com/community/api/documentation/image/f38b83e4-9bac-43db-996d-c620b0ddad2b?resizing_type=fit) | [Noise Tool Properties](https://dev.epicgames.com/community/api/documentation/image/81739b0a-0e95-46b3-b0ae-876511db1f20?resizing_type=fit) |

| Property | Description |
| --- | --- |
| **Tool Strength** | Controls how much effect each brush stroke has. |
| **Noise Mode** | Determines whether to apply: all noise effects, only the noise effects that result in raising the heightmap, or only the noise effects that result in lowering the heightmap.   * **Both**: Raises and lowers values (for painted values of Noise) to the heightmap when the mouse click is activated. * **Add**: Raises values (when painting Noise to the heightmap) when the mouse click is activated. * **Sub**: Lowers values (when painting Noise to the heightmap) when the mouse click is activated. |
| **Noise Scale** | The size of the perlin noise filter used. The noise filter is related to position and scale, which means if you do not change **Noise Scale**, the same filter is applied to the same position many times. |

The brush strength determines the amount of raising or lowering that can happen when using the Noise tool.

* [landscape](https://dev.epicgames.com/community/search?query=landscape)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Using the Noise Tool](/documentation/en-us/unreal-engine/landscape-noise-tool-in-unreal-engine?application_version=5.7#using-the-noise-tool)
* [Tool Settings](/documentation/en-us/unreal-engine/landscape-noise-tool-in-unreal-engine?application_version=5.7#tool-settings)
