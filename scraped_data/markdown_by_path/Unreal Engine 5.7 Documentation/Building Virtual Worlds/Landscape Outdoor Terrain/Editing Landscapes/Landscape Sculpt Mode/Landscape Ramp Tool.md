<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-ramp-tool-in-unreal-engine?application_version=5.7 -->

# Landscape Ramp Tool

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
9. Landscape Ramp Tool

# Landscape Ramp Tool

This is an overview of the Ramp painting tool.

![Landscape Ramp Tool](https://dev.epicgames.com/community/api/documentation/image/e078505b-725d-466f-a9f7-cd68fecc36dc?resizing_type=fill&width=1920&height=335)

 On this page

The **Ramp** tool enables you to select two locations on your Landscape and create a flat ramp between the two points, with a falloff you specify for the sides.

## Using the Ramp Tool

1. In the Landscape toolbar, in the **Sculpt** tab, select the **Ramp** tool.

   ![Ramp Selection](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fafea5c2-2b54-44b9-b4fa-ce1ac8febc4b/01-ramp-selection.png)
2. In the viewport, **Left-click** and drag or simply Left-click in two different places on your Landscape to mark the beginning and end points of the ramp.

   ![Beginning And End Points Of The Ramp](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cc6903ee-3544-4043-8448-01861795ad3a/02-beginning-and-end-points-of-the-ramp.png)


   If you change your mind about adding a ramp after starting to set the beginning and end points, you can click **Reset** to clear them.
3. Select either marker and adjust its position. In this case, it has been moved along the Z-axis above the Landscape surface.

   ![Moved Ramp](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c33ccf61-9461-4d44-95dd-c67ad092b8af/03-moved-ramp.png)
4. When you are satisfied with the position, click the **Add Ramp** button in the Tool Settings to create the ramp.

   ![Add Ramp](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3987cb63-ec73-4df1-a425-daaed22d996e/04-add-ramp.png)

   Now you have a ramp that has been sculpted into your heightmap.

   ![Ramp](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e3899948-530e-43a9-8cfc-d54cfc55ac3b/05-ramp.png)

## Tool Settings

|  |  |
| --- | --- |
| Ramp Tool | Ramp Tool Properties |

| **Property** | **Description** |
| --- | --- |
| **Ramp Width** | Sets the width of the ramp. |
| **Side Falloff** | Sets the edge falloff on the sides of the ramp where it merges inot the rest of the landscape. This falloff gives a softness to the edge flow on these sides. A setting of **0** means no falloff; a setting of **1** means all falloff and no flat surface for the ramp. |

* [landscape](https://dev.epicgames.com/community/search?query=landscape)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Using the Ramp Tool](/documentation/en-us/unreal-engine/landscape-ramp-tool-in-unreal-engine?application_version=5.7#usingtheramptool)
* [Tool Settings](/documentation/en-us/unreal-engine/landscape-ramp-tool-in-unreal-engine?application_version=5.7#toolsettings)
