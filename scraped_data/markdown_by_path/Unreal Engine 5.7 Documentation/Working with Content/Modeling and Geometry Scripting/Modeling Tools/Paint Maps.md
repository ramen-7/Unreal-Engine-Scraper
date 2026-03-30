<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/paint-maps-tool-in-unreal-engine?application_version=5.7 -->

# Paint Maps

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
5. [Working with Content](/documentation/en-us/unreal-engine/working-with-content-in-unreal-engine "Working with Content")
6. [Modeling and Geometry Scripting](/documentation/en-us/unreal-engine/modeling-and-geometry-scripting-in-unreal-engine "Modeling and Geometry Scripting")
7. [Modeling Tools](/documentation/en-us/unreal-engine/modeling-tools-in-unreal-engine "Modeling Tools")
8. Paint Maps

# Paint Maps

Overview of painting vertex weight maps for Modeling Mode tools.

![Paint Maps](https://dev.epicgames.com/community/api/documentation/image/3574f302-26ac-41e2-a668-4bfd4960891d?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

The **Paint Maps** tool stores values from 0 to 1 in the vertices of a mesh to create **weight maps**. The range of values determines the strength at which mesh vertices are affected by a selected procedure. You can use the weight maps in other [Modeling Mode](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine) tools to perform operations on specific vertex regions.

![Weight Maps with Offset Tool](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/07904376-9854-4ccf-a360-630cc9b093ca/paint-map-tool.png)

Using a weight map in the Offset tool to define vertices that move along the normal (areas in red) - creating a cobblestone effect.

The following modeling tools support weight maps:

* [Smooth](/documentation/en-us/unreal-engine/smooth-tool-in-unreal-engine)
* [Displace](/documentation/en-us/unreal-engine/displace-tool-in-unreal-engine)
* [Offset](/documentation/en-us/unreal-engine/offset-tool-in-unreal-engine)
* [Paint Vertex Colors](/documentation/404)

The weight maps you create with the Paint Maps tool are not accessible by [materials](/documentation/en-us/unreal-engine/unreal-engine-materials). You can use the Paint Vertex Colors tool to copy over your weight maps, which you can then use for materials and additional workflows.

## Accessing the Tool

You can access the Paint Maps tool from the following:

* The **Attributes** category in **Modeling Mode**. To learn more about Modeling Mode and how to access it, see [Modeling Mode Overview](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine).
* The **Editing Tools** tab in the **Skeleton Editor**. To learn more, see [Skeleton Editing](/documentation/en-us/unreal-engine/skeleton-editing-in-unreal-engine).

![Paint Map Tool Icon](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fc531984-71a1-4687-aed2-14444f97de3a/paint-map-tool-icon.png)

## Using Paint Maps

Before using the Paint Maps tool, you must create a weight map layer in the [Edit Attributes](/documentation/en-us/unreal-engine/modeling-tools-in-unreal-engine#attribs) tool.

The Paint Maps tool works similarly to the other brush-based tools in Modeling Mode. You can interactively paint weight map values onto mesh vertices using a brush and adjust the various brush settings. A mesh can have multiple weight map layers, and you can switch between each layer in a single tool session.



If your brush strength is higher than 0 but your brush strokes are not appearing, the result could indicate you're not hitting a vertex but the area of a triangle. You can increase the resolution of the geometry using the [Remesh](/documentation/en-us/unreal-engine/modeling-tools-in-unreal-engine#meshops) tool. This increase in vertices can help create a continuous painting flow when creating weight maps.

Once you are done using the tool, you can accept or cancel the changes in the [Tool Confirmation](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine#toolsundohistoryandacceptingchanges) panel.

### Settings

| **Brush Action** | **Description** |
| --- | --- |
| **Paint** | Create weight maps through brush strokes. |
| **Flood Fill** | Set the entire mesh to the brush settings. |

| **Brush** | **Description** |
| --- | --- |
| **Size** | Set the size of the brush relative to the mesh's size. |
| **Strength** | Determines what value (0-1) of color is applied with each brush stroke. Higher values create a solid color, while lower values create more opaque colors. |
| **Falloff** | From the center of the brush, determine the strength of the radius. The value of the setting is the percentage of the falloff circle size to brush size. A lower value creates harder edges, and a higher value makes blurred edges. |
| **Specify Radius** | Enable to ignore relative brush size and use explicit world radius. |
| **Radius** | Size of the radius. |

You can switch between the mesh's weight map layers using the **Selected Attribute** property.

## Hotkeys

| **Hotkey** | **Description** |
| --- | --- |
| **Shift + Click** | Blend the color values. Click and hold to continuously blend. |
| **CTRL + Click** | Erase color. Click and hold to continuously erase. |
| **[ or S** | Decreases the brush size by 0.025 with each key press. Holding the Shift key reduces the size by 0.005 for each key press. |
| **] or D** | Increases the brush size by 0.025 with each key press. Holding the Shift key will increase the size by 0.005 for each key press. |
| **F** | Zooms into the location of the brush. |
| **Enter** | Accept tool changes. |
| **ESC** | To cancel the changes and exit the tool. |

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [landscape](https://dev.epicgames.com/community/search?query=landscape)
* [beta](https://dev.epicgames.com/community/search?query=beta)
* [modeling mode](https://dev.epicgames.com/community/search?query=modeling%20mode)
* [modeling tools](https://dev.epicgames.com/community/search?query=modeling%20tools)
* [weight maps](https://dev.epicgames.com/community/search?query=weight%20maps)
* [skeleton editing](https://dev.epicgames.com/community/search?query=skeleton%20editing)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Accessing the Tool](/documentation/en-us/unreal-engine/paint-maps-tool-in-unreal-engine?application_version=5.7#accessingthetool)
* [Using Paint Maps](/documentation/en-us/unreal-engine/paint-maps-tool-in-unreal-engine?application_version=5.7#usingpaintmaps)
* [Settings](/documentation/en-us/unreal-engine/paint-maps-tool-in-unreal-engine?application_version=5.7#settings)
* [Hotkeys](/documentation/en-us/unreal-engine/paint-maps-tool-in-unreal-engine?application_version=5.7#hotkeys)

Related documents

[Modeling Tools

![Modeling Tools](https://dev.epicgames.com/community/api/documentation/image/808c9f39-3e12-44a5-8c91-d19bce2c278b?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/modeling-tools-in-unreal-engine)

[Modeling Mode Overview

![Modeling Mode Overview](https://dev.epicgames.com/community/api/documentation/image/056cb8c8-a8a2-4ba1-b18c-42a01965bcb1?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine)
