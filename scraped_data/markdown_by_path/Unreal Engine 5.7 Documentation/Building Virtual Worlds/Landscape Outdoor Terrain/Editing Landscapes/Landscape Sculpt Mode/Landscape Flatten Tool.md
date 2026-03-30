<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-flatten-tool-in-unreal-engine?application_version=5.7 -->

# Landscape Flatten Tool

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
9. Landscape Flatten Tool

# Landscape Flatten Tool

This is an overview of the Flatten painting tool.

![Landscape Flatten Tool](https://dev.epicgames.com/community/api/documentation/image/e5447115-08b5-4a44-b6b6-02a7404b1d09?resizing_type=fill&width=1920&height=335)

 On this page

The **Flatten** tool pushes or pulls all other parts of the heightmap to the level that is currently under the mouse when activated. This can raise or lower the surrounding
heightmap values to be the same value.

## Using the Flatten Tool

In this example, the Flatten tool is being used in the middle of the hillside to flatten out areas at the point where the mouse click was initiated. As long as the mouse is held down, the height value
that was detected is used along any surface to raise or lower (depending on your tool settings) to that height.

Use the following controls to sculpt your Landscape heightmap:

| Controls | Operation |
| --- | --- |
| **Left Mouse Button** | Flattens or levels by both raising and lowering or individually raising and lowering the heightmap. |

![Before Flattening](https://dev.epicgames.com/community/api/documentation/image/253f09d8-01a7-4217-a22a-c9ef177d615d?resizing_type=fit&width=1920&height=1080)

![After Flattening](https://dev.epicgames.com/community/api/documentation/image/25eb1273-3852-4942-98e1-af2a8686a11a?resizing_type=fit&width=1920&height=1080)

Before Flattening

After Flattening

The brush strength determines the amount of Flattening that can happen when using the Flatten tool.

## Tool Settings

|  |  |
| --- | --- |
| [Flatten Tool](https://dev.epicgames.com/community/api/documentation/image/09f48b82-f352-4c39-97d7-659d80f35efe?resizing_type=fit) | [Flatten Tool Properties](https://dev.epicgames.com/community/api/documentation/image/2b75ff61-d26d-4422-a90c-225dbc0bde84?resizing_type=fit) |

| Property | Description |
| --- | --- |
| **Flatten Target** | Sets the target height toward which to flatten. |
| **Tool Strength** | Controls how much smoothing occurs with each brush stroke has. |
| **Flatten Mode** | Determines whether the tool will raise or lower the heightmap section under the brush.   * **Both**: Raises and lowers values to the current height value when the mouse click is activated. * **Raise**: Raises values that are lower than the currently selected height when the mouse click is activated. Any values above this clicked point will be left unchanged. * **Lower**: Lower values that are higher than the currently selected height when the mouse click is activated. Any values lower than this clicked point will be left unchanged. |
| **Use Slope Flatten** | If checked, flattens along the Landscape's existing slope instead of flattening toward a horizontal plane. |
| **Pick Value Per Apply** | If checked, constantly selects new values to flatten toward, instead of only using the first clicked point. |
| Advanced |  |
| --- | --- |
| **Show Preview Grid** | When Flatten Target is enabled, you can enable this option to show a preview grid for the flatten target height. |
| **Terrace Interval** | Sets the height of the Terrace interval for Terrace Flatten mode. |
| **Terrace Smoothing** | Sets the smoothing value for Terrace Flatten mode |

* [landscape](https://dev.epicgames.com/community/search?query=landscape)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Using the Flatten Tool](/documentation/en-us/unreal-engine/landscape-flatten-tool-in-unreal-engine?application_version=5.7#using-the-flatten-tool)
* [Tool Settings](/documentation/en-us/unreal-engine/landscape-flatten-tool-in-unreal-engine?application_version=5.7#tool-settings)
