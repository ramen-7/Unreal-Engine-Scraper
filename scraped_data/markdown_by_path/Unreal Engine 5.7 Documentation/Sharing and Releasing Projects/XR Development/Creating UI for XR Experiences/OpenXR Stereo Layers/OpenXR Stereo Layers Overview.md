<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/openxr-stero-layers-overview-in-unreal-engine?application_version=5.7 -->

# OpenXR Stereo Layers Overview

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
5. [Sharing and Releasing Projects](/documentation/en-us/unreal-engine/sharing-and-releasing-projects-for-unreal-engine "Sharing and Releasing Projects")
6. [XR Development](/documentation/en-us/unreal-engine/developing-for-xr-experiences-in-unreal-engine "XR Development")
7. [Creating UI for XR Experiences](/documentation/en-us/unreal-engine/design-user-interfaces-for-xr-experiences-in-unreal-engine "Creating UI for XR Experiences")
8. [OpenXR Stereo Layers](/documentation/en-us/unreal-engine/openxr-stero-layers-in-unreal-engine "OpenXR Stereo Layers")
9. OpenXR Stereo Layers Overview

# OpenXR Stereo Layers Overview

Send textures to the HMD in a separate rendering pass from the rest of the project, to display without any post-processing effects.

![OpenXR Stereo Layers Overview](https://dev.epicgames.com/community/api/documentation/image/a7e059b9-6946-430f-94bf-8db31ff7320d?resizing_type=fill&width=1920&height=335)

 On this page

OpenXR Stereo Layers send a separate texture to the head-mounted display (HMD) and re-project the texture in a separate rendering pass than the rest of the project. This can be useful for user interface (UI) elements that you want attached to the HMD without additional effects applied to them, such as post-processing or anti-aliasing.

Stereo Layers are rendered to the HMD, but they do not appear in the **VR Preview** window on your desktop.

This page is an overview of the OpenXR Stereo Layers feature. To learn how to add Stereo Layers to your OpenXR app, see the [OpenXR Stereo Layers Quick Start](/documentation/en-us/unreal-engine/openxr-stereo-layers-quick-start-in-unreal-engine).

## Stereo Layer Types

You can set which space the Stereo Layer's position and rotation are relative to. The following are the available types:

* **Face-Locked**: The Stereo Layer stays in the same place in the HMD view, regardless of its position or rotation.

  ![Texture is relative to the HMD's view](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/173a2ad7-8449-45b5-a38e-03054b2bed15/image_1.gif)
* **Tracker-Locked**: The Stereo Layer position is relative to the real-world tracking space around the player.

  ![Texture is relative to the physical space around the user](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ebf659fd-230d-49cb-827e-fe9636dc14ce/image_2.gif)
* **World-Locked**: The Stereo Layer position is relative to the virtual world space and the object to which it's attached as a Component.

  ![Texture is relative to the virtual object in the scene](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a27e0c11-4cee-4abc-b5ee-2030219f10b5/image_3.gif)

Mixing Face-Locked layer priorities with World-Locked and Tracker-Locked layers by setting the `vr.StereoLayers.bMixLayerPriorities` console variable is not supported.

## Stereo Layer Shape

You can set the shape of the layer by selecting an option from the **Stereo Layer Shape** dropdown.
Stereo Layers support the following shapes:

* Cylinder
* Equirect
* Quad

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/35faedef-e109-41d6-b633-949a4c1b03cb/stereo_layer_shapes.png)


Note: The Quad Layer Shape is supported on all OpenXR runtimes. Other Stereo Layer Shapes may not be supported depending on the OpenXr Runtime you are using.

## Layer Draw Order

Stereo Layers exist outside the virtual world and are drawn based on the **Priority** setting for each layer. The draw order is determined by the following:

* Layers with higher priority are rendered on top of layers with lower priority.
* Face-Locked layers are rendered on top of World-Locked or Tracker-Locked layers regardless of priority.
* When multiple layers have the same priority, those layers are rendered in no-specified order. Use different priorities if you need a specific ordering for the layers.

## Stereo Layer Properties

Stereo Layers have some properties that affect the way in which it is rendered. The following table describes each one of these settings and its effect on the Stereo Layers.

| Setting Name | Description |
| --- | --- |
| **Live Texture** | True, if the Stereo Layer texture needs to update itself every frame (scene capture, video, and so on). |
| **Supports Depth** | True, if the Stereo Layer needs to support depth intersections with the scene geometry, if available on the platform. This option is currently not supported by OpenXR. |
| **No Alpha Channel** | True, if the texture should not use its own alpha channel (1.0 will be substituted). |
| **Texture** | Texture displayed on the Stereo Layer (if stereoscopic textures are supported on the platform, and more than one texture is provided, this will be the right eye). |
| **Quad Preserve Texture Ratio** | True, if the quad should internally set its Y value based on the set texture's dimensions. |
| **Stereo Layer Type** | Specifies how and where the quad is rendered to the screen. |
| **Stereo Layer Shape** | Specifies the shape of the layer. Only the **Quad** layer shape is supported in OpenXR. |
| **Priority** | Render priority among all Stereo Layers; higher priority render on top of lower priority. |
| **Left Texture** | Texture displayed on the Stereo Layer for the left eye, if stereoscopic textures are supported on the platform. |
| **Quad Size** | Size of the rendered Stereo Layer quad. |
| **UVRect** | UV coordinates mapped to the quad face. |
| **Cylinder Radius** | Radial size of the rendered Stereo Layer cylinder. |
| **Cylinder Overly Arc** | Arc angle for the Stereo Layer cylinder. |
| **Cylinder Height** | Height of the Stereo Layer cylinder. |

* [xr](https://dev.epicgames.com/community/search?query=xr)
* [vr](https://dev.epicgames.com/community/search?query=vr)
* [openxr](https://dev.epicgames.com/community/search?query=openxr)
* [stereo layers](https://dev.epicgames.com/community/search?query=stereo%20layers)
* [ar/vr/xr](https://dev.epicgames.com/community/search?query=ar%2Fvr%2Fxr)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Stereo Layer Types](/documentation/en-us/unreal-engine/openxr-stero-layers-overview-in-unreal-engine?application_version=5.7#stereolayertypes)
* [Stereo Layer Shape](/documentation/en-us/unreal-engine/openxr-stero-layers-overview-in-unreal-engine?application_version=5.7#stereolayershape)
* [Layer Draw Order](/documentation/en-us/unreal-engine/openxr-stero-layers-overview-in-unreal-engine?application_version=5.7#layerdraworder)
* [Stereo Layer Properties](/documentation/en-us/unreal-engine/openxr-stero-layers-overview-in-unreal-engine?application_version=5.7#stereolayerproperties)
