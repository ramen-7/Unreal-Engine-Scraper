<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-collision-guide-in-unreal-engine?application_version=5.7 -->

# Landscape Collision Guide

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
7. Landscape Collision Guide

# Landscape Collision Guide

Collision settings for Landscape.

![Landscape Collision Guide](https://dev.epicgames.com/community/api/documentation/image/e1eafe54-7b3a-4870-aa8e-56578b4632e4?resizing_type=fill&width=1920&height=335)

 On this page

## Landscape Collision

The Unreal Engine 5 (UE5) Landscape system enables you to specify the detail level of the geometry used for both simple and complex collisions for the entire Landscape as a whole or on a per-Component basis. In the following sections, we will go over how to use the system as well as any relevant information you must know before using this in your UE5 projects.

For this example, we are using the Content Examples project, specifically the Landscapes map, that can be found in the **Learn** tab of the UE5 Launcher.

### Collision Mip Level

If you select any Landscape Actor that has been placed in a level and go to the **Details** panel, under the **Collision** section you will find two settings called **Collision Mip Level** and **Simple Collision Mip Level**.

|  |  |
| --- | --- |
| **Collision Mip Level** | The Collision Mip Level sets the complexity of the **Complex** collision that is used for the Landscape. Setting Collision Mip Level to **0**, the default, will give you a very accurate Landscape collision at the expense of memory. Setting this value to **5**, the maximum setting, will make the Landscape collision cheaper, but the accuracy of the collision will suffer. Drag the slider to adjust the Collision Mip Level from 0 to 5 Drag the slider to adjust the Collision Mip Level from 0 to 5 Drag the slider to adjust the Collision Mip Level from 0 to 5 Drag the slider to adjust the Collision Mip Level from 0 to 5  **Drag the slider to adjust the Collision Mip Level from 0 to 5** |
| **Simple Collision Mip Level** | The Simple Collision Mip Level sets the complexity of the **Simple** collision that is used for the Landscape. Setting Simple Collision Mip Level to **0**, the default, will give you a very accurate Landscape collision at the expense of memory. Setting this value to **5**, the maximum setting, will make the Landscape collision cheaper, but the accuracy of the collision will suffer. Drag the slider to adjust the Simple Collision Mip Level from 0 to 5 Drag the slider to adjust the Simple Collision Mip Level from 0 to 5 Drag the slider to adjust the Simple Collision Mip Level from 0 to 5 Drag the slider to adjust the Simple Collision Mip Level from 0 to 5  **Drag the slider to adjust the Simple Collision Mip Level from 0 to 5** |

### Viewing Collision Mip Level

You can visualize the Landscape collision geometry using the Playeer Collision Viewmode. To enable this view mode, go to the **View Mode** menu in the Editor viewport toolbar and select either **Player Collision** or **Visibility Collision**.

[![Collision Visualization](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3dfb2fe2-8733-4cce-abb0-e9328237a652/13-collision-visualization.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3dfb2fe2-8733-4cce-abb0-e9328237a652/13-collision-visualization.png)

Click image for full size.

|  |  |
| --- | --- |
| **Player Collision** | The **Player Collision** view mode displays the Simple Collision Mip Level. Collision Mip Level Player Collision |
| **Visibility Collision** | The **Visibility Collision** view mode displays the Collision Mip Level. Collision Mip Level Visibility Collision |

### Adjusting the Landscape Collision Mip Level

To set the complexity for both simple and complex Landscape collision you will need to do the following:

1. Select your Landscape Terrain in the Editor viewport. In the **Details** panel, expand the **Collision** section.

   [![Details Panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b524ebe8-0618-45ac-b9cc-7b71f8856cca/16-lsc-collision.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b524ebe8-0618-45ac-b9cc-7b71f8856cca/16-lsc-collision.png)

   Click for full image.
2. Under the **Collision** section, find the **Collision Mip Level** option. Set the value from **0** to **5** and then press the **Enter** key to apply the change. The gray collision mesh in the level updates automatically to reflect the changes.

   ![Collision Mip Level 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/eab40592-99f5-48ff-9612-2345daedba93/17-collision-mip-level-0.png "Collision Mip Level 0")

   ![Collision Mip Level 5](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1ce22ac6-1ab7-4659-be31-dca6f9a9dff9/18-collision-mip-level-5.png "Collision Mip Level 5")

   Collision Mip Level 0

   Collision Mip Level 5

### Mixing Collision Mip Level Options

You can set the complexity of both the simple and complex Landscape collision meshes to provide a better balance between performance and accuracy. To set the simple and complex collision levels independently in your project you will need to do the following:

1. Select your Landscape and in the **Details** panel and expand the **Collision** section.

   [![Details Panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4906addb-a212-4ee8-b747-e63d918e4063/19-lsc-collision-01.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4906addb-a212-4ee8-b747-e63d918e4063/19-lsc-collision-01.png)

   Click for full image.
2. Set the **Collision Mip Level** to a value of **0** and **Simple Collision Mip Level** to a value of **2**.

   [![Details Panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/93cc19bb-6874-45e6-b39f-132b3c540b82/20-lsc-collision-04.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/93cc19bb-6874-45e6-b39f-132b3c540b82/20-lsc-collision-04.png)

   Click for full image.

In the following image comparison, you can see what happens to the Landscape collision when the Collision Mip Level and Simple Collision Mip Level are set to different values.

![Player Collision|Simple Collision Mip Level = 2](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f95fb924-902a-4f9d-b057-e2969b63dd3b/21-simple-collision-mip-level-2.png "Player Collision Simple Collision Mip Level 2")

![Visibility Collision|Collision Mip Level = 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/80502a7c-536d-4c4d-859c-e9c60858abc2/22-collision-mip-level-0.png "Visibility Collision Collision Mip Level 0")

Player Collision|Simple Collision Mip Level = 2

Visibility Collision|Collision Mip Level = 0



For most cases, you will want to leave the **Collision Mip Level** at 0 and then use 1 or 2 for the **Simple Collision Mip Level**. Using any higher numbers will start to show inaccuracies between the player and collision.

### Setting Collision Mip Level Per Landscape Components

You can set the Collision Mip Level collision for individual Landscape Components which enables you to reduce the Landscape collision complexity even further in non-playable areas of the level.

To set the Collision Mip Level for an individual component in your project, you will need to do the following:

1. From the **Modes** dropdown, click on the Landscape option and make sure the **Manage** tab is selected.

   [![Modes Panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e0a699ae-e711-4b89-98e9-a2cff01c1a58/23-landscape-cc-1.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e0a699ae-e711-4b89-98e9-a2cff01c1a58/23-landscape-cc-1.png)

   Click for full image.

   [![Landscape Panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/390357e8-2227-4510-8f01-08affdff0b2f/24-select.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/390357e8-2227-4510-8f01-08affdff0b2f/24-select.png)

   Click for full image.
2. Select a few Landscape components by clicking on them with the **Left Mouse Button**. The selected Landscape Components are highlighted in red.

   [![Select a few Landscape components](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/baa08444-d4d8-4ce2-883f-a0b4656a5c2c/25-select-cc.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/baa08444-d4d8-4ce2-883f-a0b4656a5c2c/25-select-cc.png)

   Click for full image.
3. In the **Details** panel, expand the **Landscape Component** section and change both the **Collision Mip Level** and **Simple Collision Mip Level** to **5**.

   [![Details Panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/735ac615-f898-4a42-b91c-b9df2d377e3e/26-collision-mip-level-cc.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/735ac615-f898-4a42-b91c-b9df2d377e3e/26-collision-mip-level-cc.png)

   Click for full image.
4. In the Landscape **Manage** section under **Tool Settings**, press the **Clear Component Selection** button to deselect any currently selected Landscape components.

   [![Clear Selected Component](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/78c8b43e-e8a3-4817-9cb3-c1b6a399d02a/27-clear-selected-comps.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/78c8b43e-e8a3-4817-9cb3-c1b6a399d02a/27-clear-selected-comps.png)

   Click for full image.
5. Select a few more Landscape components and this time set both Collision Mip levels to a value of 2.

   [![Landscape Component](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e116619c-4e4b-4237-8b32-b588be3a7410/28-landscape-component-cc.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e116619c-4e4b-4237-8b32-b588be3a7410/28-landscape-component-cc.png)

   Click for full image.

In the following image, the Collision Mip level for each of the four outlined Landscape Component has been set to a different level.

[![Collision Mip level](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/40310b65-c6e6-439e-90dc-2f827e4805f5/29-collision-cc.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/40310b65-c6e6-439e-90dc-2f827e4805f5/29-collision-cc.png)

Click for full image.

| Number | Collision Mip Level |
| --- | --- |
| 1 | 3 |
| 2 | 4 |
| 3 | 5 |
| 4 | 2 |

* [materials](https://dev.epicgames.com/community/search?query=materials)
* [landscape](https://dev.epicgames.com/community/search?query=landscape)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Landscape Collision](/documentation/en-us/unreal-engine/landscape-collision-guide-in-unreal-engine?application_version=5.7#landscapecollision)
* [Collision Mip Level](/documentation/en-us/unreal-engine/landscape-collision-guide-in-unreal-engine?application_version=5.7#collisionmiplevel)
* [Viewing Collision Mip Level](/documentation/en-us/unreal-engine/landscape-collision-guide-in-unreal-engine?application_version=5.7#viewingcollisionmiplevel)
* [Adjusting the Landscape Collision Mip Level](/documentation/en-us/unreal-engine/landscape-collision-guide-in-unreal-engine?application_version=5.7#adjustingthelandscapecollisionmiplevel)
* [Mixing Collision Mip Level Options](/documentation/en-us/unreal-engine/landscape-collision-guide-in-unreal-engine?application_version=5.7#mixingcollisionmipleveloptions)
* [Setting Collision Mip Level Per Landscape Components](/documentation/en-us/unreal-engine/landscape-collision-guide-in-unreal-engine?application_version=5.7#settingcollisionmiplevelperlandscapecomponents)
