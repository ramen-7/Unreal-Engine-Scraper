<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/openxr-stereo-layers-quick-start-in-unreal-engine?application_version=5.7 -->

# OpenXR Stereo Layers Quick Start

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
9. OpenXR Stereo Layers Quick Start

# OpenXR Stereo Layers Quick Start

Learn how to add an OpenXR Stereo Layer to your project.

![OpenXR Stereo Layers Quick Start](https://dev.epicgames.com/community/api/documentation/image/824531d5-0475-4bb5-8c0a-4d807990af81?resizing_type=fill&width=1920&height=335)

This page describes how to get started with Stereo Layers in your OpenXR project.

The steps and images on this page use the [VR Template](/documentation/en-us/unreal-engine/vr-template-in-unreal-engine) Project as a starting point. The steps should apply to any project set up for OpenXR.

To add an OpenXR Stereo Layer to your project's Pawn:

1. In the **Content Drawer**, navigate to **Content > VRTemplate > Blueprints** and double-click the **VRPawn** Asset to open it in the **Blueprint Editor**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ae4bd3ab-8e94-4993-9b8c-f115d1d74450/01-select-vr-pawn_ue5.png)
2. In the **Components** panel of the Blueprint Editor, click the **Add Component** button and search for **Stereo Layer**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f21ea716-a521-4901-8601-573101114938/02-add-stereo-layer_ue5.png)
3. Drag the new **Stereo Layer** Component on top of the **Camera** Component to make it a Child Actor of the Camera.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/957ad821-a003-478b-8791-7470b90debeb/03-stereo-layer_ue5.png)
4. Select the Stereo Layer Component from the Components list to open its **Details** panel. Under the **Transform** section, set the **X** value of **Location** to **100**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/abae5b69-942f-452a-b55c-38a952ad9421/04-change-location_ue5.png)
5. Switch to the **Viewport** tab of the Blueprint Editor to see the location of the Stereo Layer relative to the Pawn's Camera.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e1ea1cc5-2a55-49c8-a3d5-46c070aa8d25/05-select-viewport_ue5.png)
6. In the **Details** panel, under the **Stereo Layer** section:

   * Assign a texture to the **Texture** parameter. In this example, the **T\_Grid** texture is used.
   * Set the **Stereo Layer Shape** to **Quad Layer**.![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8d0daef2-829b-44cf-8317-66090e8e4024/06-add-texture_ue5.png)
7. **Compile** the Blueprint and close the Blueprint Editor.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cf604c3c-7060-443e-a002-a1b3b3080f76/07-select-compile-button_ue5.png)
8. Press **Play in VR** to launch your project on the headset and verify that the texture is displayed in front of you and locked to the HMD.

   ![image alt text](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8fad1e46-6550-4407-9e89-a60abd7f066f/image_12.gif)

To change where the Stereo Layer appears, change the Stereo Layer Type parameter. See the [OpenXR Stereo Layers Overview](/documentation/en-us/unreal-engine/openxr-stero-layers-overview-in-unreal-engine) for details on the available options.

* [xr](https://dev.epicgames.com/community/search?query=xr)
* [vr](https://dev.epicgames.com/community/search?query=vr)
* [openxr](https://dev.epicgames.com/community/search?query=openxr)
* [stereo layers](https://dev.epicgames.com/community/search?query=stereo%20layers)
* [ar/vr/xr](https://dev.epicgames.com/community/search?query=ar%2Fvr%2Fxr)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)
