<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/openxr-loading-screens-in-unreal-engine?application_version=5.7 -->

# OpenXR Loading Screens

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
8. OpenXR Loading Screens

# OpenXR Loading Screens

Learn how to use a texture as a loading screen to ease transitions between levels in XR experiences.

![OpenXR Loading Screens](https://dev.epicgames.com/community/api/documentation/image/f2d6cb79-8e4d-4f2d-9942-4195cd3320b5?resizing_type=fill&width=1920&height=335)

 On this page

For apps targeting head-mounted displays (HMDs), you can use a texture as a loading screen to ease transitions between levels. At the end of this guide, you will be familiar with the Blueprint nodes used for loading screens and will know how to use them within your project.

## Set Loading Screen Node

The loading screen must be defined before you can display it in the HMD.

On the **Set Loading Screen** node, you can select the texture that you want to use for the loading screen from the **Texture** pin's Select Asset dropdown.

Then, change the **Offset** vector to specify the texture's position relative to the position of the HMD.

![Set Loading Screen Blueprint Node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f24d6c1e-bcf1-4577-9bcb-f5fc7a4f1dbf/01-set-loading-screen_ue5.png)


Media playback through [Media Framework](/documentation/en-us/unreal-engine/media-framework-in-unreal-engine) is not currently supported with Loading Screens in XR.

## Show and Hide Loading Screen Nodes

Once the Set Loading Screen node has been created, connect its output pin to the **Show Loading Screen** node's execution pin to display it in the HMD.

When you want the loading screen to no longer display, you can connect it to the **Hide Loading Screen** node's execution pin.

![Show Loading Screen and Hide Loading Screen Blueprint Nodes](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/649c4d5f-55d2-40a9-be2b-2a2de755dd7f/02-show-hide-screen_ue5.png)


Sometimes it's necessary to add a short delay, using the Delay node, after the Show Loading Screen to ensure the loading screen is visible before the next operation.

## Using Loading Screen Nodes

In the following example, a map is loaded using [Level Streaming](/documentation/en-us/unreal-engine/level-streaming-in-unreal-engine) as the map transition.

Follow these general steps to add a loading screen to your project:

1. In the Unreal Editor, open your Map in the Level Editor.
2. Click **Blueprints > Open Level** **Blueprint**.

   ![Open Level Blueprint in the Editor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/da5c57a7-fe9e-47e0-87d9-ac8e41d21e35/03-open-level-blueprint_ue5.png)
3. In the Event Graph, add the following nodes:

   * Delay
   * Set Loading Screen
   * Show Loading Screen
   * Load Stream Level
   * Hide Loading Screen![Level Blueprint with all the listed nodes added](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3664ea3d-5d12-42b6-95c1-82e0679dc64f/04-event-begin-play_ue5.png)
4. Connect the output pin from the **Event BeginPlay** node to the input of the **Set Loading Screen** node.
5. On the **Set Loading Screen** node:
   1. Select a texture from the **Texture** dropdown.
   2. Set the **Scale** 2D vector to **(1.0, 1.0)** — a nonzero value — to see the texture.
   3. Set the **Offset** 3D vector for the loading screen to **(1.0, 0.0, 0.5)**. The loading screen should appear in front of you within the HMD, but this position can be different depending on your headset.![Level Blueprint where the Event BeginPlay node is connected as an input to the Set Loading Screen node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/29714431-fdba-4098-9a18-b9ceb696fab5/05-scale-offset_ue5.png)
6. Connect the output pin of the **Set Loading Screen** node to the input of the **Show Loading Screen** node.

   ![Level Blueprint where the Set Loading Screen node is connected as an input to the Show Loading Screen node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d6c790ef-7209-429e-badb-d83097a71630/06-connect-loading-screen_ue5.png)
7. Connect the output of the **Show Loading Screen** node to the input of the **Delay** node. The delay node will set a specific time duration for the loading screen to display.
8. Set the **Delay** node's **Duration** parameter to **3.0** seconds to make the loading screen display for at least three seconds when you launch the app.

   ![Level Blueprint where the Show Loading Screen node is connected as an input to the Delay node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/01a6a144-f923-43af-813b-d3e3f4c61730/07-add-delay_ue5.png)
9. Connect the output pin from the **Delay** node to the input of the **Load Stream Level** node.
10. On the **Load Stream Level** node:

    1. Set the **Level Name** parameter to a different Level in your project.
    2. Enable **Make Visible After Load**.
    3. Enable **Should Block on Load**.![Level Blueprint where the Delay node is connected as an input to the Load Stream Level node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f3a82a90-d5c5-44fe-b76e-6b32cb660cb9/08-enable-load_ue5.png)
11. Connect the output pin of the **Load Stream Level** node to the input of the **Hide Loading Screen** node. Placing the Hide Loading Screen node after the Load Stream Level node ensures that the Level has finished loading before being displayed.

    ![Level Blueprint where the Load Stream Level node is connected as an input to the Hide Loading Screen node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/efbd33f9-d458-455f-8ea9-b260d661fbb7/09-add-hide-loading_ue5.png)
12. Launch the Level on your HMD to see the loading screen appear as the Level changes.

You can also call Hide Loading Screen from Event BeginPlay in the Level Blueprint for the Level you're loading next to ensure the loading screen isn't hidden until the Level has finished loading. You won't need to enable Should Block on Load in the Load Stream Level node when using this method. |

* [xr](https://dev.epicgames.com/community/search?query=xr)
* [vr](https://dev.epicgames.com/community/search?query=vr)
* [openxr](https://dev.epicgames.com/community/search?query=openxr)
* [splash screens](https://dev.epicgames.com/community/search?query=splash%20screens)
* [loading screens](https://dev.epicgames.com/community/search?query=loading%20screens)
* [ar/vr/xr](https://dev.epicgames.com/community/search?query=ar%2Fvr%2Fxr)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Set Loading Screen Node](/documentation/en-us/unreal-engine/openxr-loading-screens-in-unreal-engine?application_version=5.7#setloadingscreennode)
* [Show and Hide Loading Screen Nodes](/documentation/en-us/unreal-engine/openxr-loading-screens-in-unreal-engine?application_version=5.7#showandhideloadingscreennodes)
* [Using Loading Screen Nodes](/documentation/en-us/unreal-engine/openxr-loading-screens-in-unreal-engine?application_version=5.7#usingloadingscreennodes)

Related documents

[Developing for Head-Mounted Experiences with OpenXR

![Developing for Head-Mounted Experiences with OpenXR](https://dev.epicgames.com/community/api/documentation/image/e82d4ae1-3113-44c3-9863-528e2ca53a85?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/developing-for-head-mounted-experiences-with-openxr-in-unreal-engine)
