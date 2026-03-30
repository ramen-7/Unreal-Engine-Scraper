<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-mirror-tool-in-unreal-engine?application_version=5.7 -->

# Landscape Mirror Tool

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
9. Landscape Mirror Tool

# Landscape Mirror Tool

This is an overview of the Mirror tool.

![Landscape Mirror Tool](https://dev.epicgames.com/community/api/documentation/image/0d91ff7a-f17f-4496-aa1f-647b0b8465b4?resizing_type=fill&width=1920&height=335)

 On this page

The **Mirror** tool enables you to mirror or rotate the existing Landscape heightmap geometry along the X or Y axis.

In this example, the Mirror tool is used to mirror the entire entire Landscape Actor along the Y axis.

## Using the Mirror Tool

1. In the Landscape toolbar, in **Sculpt** tab, select the **Mirror** tool.

   ![Mirror Tool button](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1380bfaf-ea92-420b-a0a4-fdac17474aee/01-mirror-tool-button.png "Mirror Tool button")
2. Use the **Operation** drop-down selection to choose the axis and mirroring method you would like to use for your selected landscape. The directional arrow indicates which side of the landscape geometry will be mirrored on.

   ![Mirror Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bbc968cb-390b-4a10-b580-0a5ec18a54d0/02-mirror-settings.png "Mirror Settings")
3. If necessary, adjust the **Mirror Point** values for the mirror plane or Left-click and drag the directional arrow on mirror plane into the position you want to mirror.

   Only the currently selected **Operation** axis will be used for the **Mirror Point**. For example, if the Operation method is "-X to +X" the X axis is the only active Mirror Point that will be affected.

   ![Setting the Mirror Point](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/85dda869-522c-4e7c-889f-3f200cbcad0e/03-setting-the-mirror-point.png "Setting the Mirror Point")
4. Once you are satisfied with your edits, you can hit the **Apply** button to see the results.

   ![Applying Mirror](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/927ead4a-0234-499b-b9e3-415916811dba/04-applying-mirror.png "Applying Mirror")

   You now have a landscape with mirrored geometry.

### Mirror Smoothing Width

If the edge seams from mirroring your landscape look unnatural or too sharp in contrast after you apply your changes you can use **CTRL + Z** to undo your last action. Then you should adjust the **Smoothing Width** so that these
edge vertices that are merged are softened.

![Smoothing Width Before](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ff0a919d-28f1-4930-8d83-95365abb40f2/05-smoothing-width-before.png "Smoothing Width Before")

![Smoothing Width After](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/eb64dc06-9539-4e6c-9d7b-b385087c067a/06-smoothing-width-after.png "Smoothing Width After")

Smoothing Width Before

Smoothing Width After

In this example, the left image has no smoothing applied after the Landscape is mirrored, whereas the right is using a value of 10 to smooth the mirrored edges and reduce the harshness of the seam.

## Tool Settings

|  |  |
| --- | --- |
| Mirror Tool | Mirror Tool properties |

| **Property** | **Description** |
| --- | --- |
| **Mirror Point** | This sets the location of the mirror plane. This will default to the center of the selected Landscape and in most cases will not normally need to be changed. |
| **Operation** | The type of mirroring operation to perform. For example, -X to +X will copy and flip the -X half of the Landscape onto the +X half. |
| **Recenter** | This button places the mirror plane back at the center of the selected Landscape. |
| **Smoothing Width** | This will set the number of vertices on either side of the mirror plane to smooth over reducing sharp contrasting angles for mirrored sides. |

* [landscape](https://dev.epicgames.com/community/search?query=landscape)
* [region](https://dev.epicgames.com/community/search?query=region)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Using the Mirror Tool](/documentation/en-us/unreal-engine/landscape-mirror-tool-in-unreal-engine?application_version=5.7#usingthemirrortool)
* [Mirror Smoothing Width](/documentation/en-us/unreal-engine/landscape-mirror-tool-in-unreal-engine?application_version=5.7#mirrorsmoothingwidth)
* [Tool Settings](/documentation/en-us/unreal-engine/landscape-mirror-tool-in-unreal-engine?application_version=5.7#toolsettings)
