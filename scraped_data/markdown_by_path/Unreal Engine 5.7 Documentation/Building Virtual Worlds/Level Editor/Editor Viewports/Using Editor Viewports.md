<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-editor-viewports-in-unreal-engine?application_version=5.7 -->

# Using Editor Viewports

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
6. [Level Editor](/documentation/en-us/unreal-engine/level-editor-in-unreal-engine "Level Editor")
7. [Editor Viewports](/documentation/en-us/unreal-engine/editor-viewports-in-unreal-engine "Editor Viewports")
8. Using Editor Viewports

# Using Editor Viewports

Basic concepts and features of the Viewports in Unreal Editor.

![Using Editor Viewports](https://dev.epicgames.com/community/api/documentation/image/dcc96030-d23a-4825-a23a-4696042e8f91?resizing_type=fill&width=1920&height=335)

 On this page

Operating System 

×Windows

Select an option from the dropdown to see content relevant to it.

The **Viewports** are your window into the worlds you create in Unreal. They can be navigated just as you would in a game, or can be used in a more schematic design sense as you would for an architectural Blueprint. The Unreal Editor viewports contain a variety of tools and visualizers to help you see exactly the data you need.

[![Viewports Topic](https://dev.epicgames.com/community/api/documentation/image/b34724a9-e863-4739-a207-01c32bac9d47?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b34724a9-e863-4739-a207-01c32bac9d47?resizing_type=fit)

Click image for full size.

## Viewport Types

There are two main types of Viewports in Unreal Editor: Perspective and Orthographic. The perspective view is a
3D window into the game world. The Orthographic views - Front, Side, and Top - are 2D Viewports that each look
down one of the main axes (X, Y, or Z).

|  |  |  |  |
| --- | --- | --- | --- |
| [View Perspective](https://dev.epicgames.com/community/api/documentation/image/72f4a04a-27c0-417a-9208-3dd817b8915f?resizing_type=fit) | [View Front](https://dev.epicgames.com/community/api/documentation/image/122afc15-e39a-43d2-bb34-8952ffb2133a?resizing_type=fit) | [View Side](https://dev.epicgames.com/community/api/documentation/image/88924040-3127-424c-85e0-5d0474adde18?resizing_type=fit) | [View Top](https://dev.epicgames.com/community/api/documentation/image/dd1f5ccb-a0e0-4010-8287-8b38f7c33a0b?resizing_type=fit) |
| Perspective (3D) | Front (X-Axis) | Side (Y-Axis) | Top (Z-Axis) |

You can cycle through the types of Viewports by pressing **Alt** and **G**, **H**, **J**, or **K**. These set the
Viewport to be Perspective, Front, Side, or Top, respectively.

## Viewport Layout

By default, you see a single Perspective Viewport when you open Unreal Editor.

[![Viewport](https://dev.epicgames.com/community/api/documentation/image/93559232-4d3e-4382-a528-b077b810f42f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/93559232-4d3e-4382-a528-b077b810f42f?resizing_type=fit)

Click image for full size.

The **Viewport** panel actually contains multiple Viewports, which are laid out in a grid and any of which can be shown
maximized. The default layout is a 4x4 that consists of one of each type of Viewport - Perspective, Top, Front, and Side.

[![Viewport](https://dev.epicgames.com/community/api/documentation/image/7988ebf2-629a-45e7-997a-7e774c5cebfa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7988ebf2-629a-45e7-997a-7e774c5cebfa?resizing_type=fit)

Click image for full size.

The Viewports can be minimized and maximized using the and
buttons located in the top right corner of each Viewport.

## View Modes

The Unreal Editor viewports have a large number of visualization modes to help you see the type of data being processed in your scene, as well as to diagnose any errors or unexpected results. The more common view modes have their own hotkeys, but all can be accessed from the viewport within the **View Mode** menu.

[![Viewmode Menu](https://dev.epicgames.com/community/api/documentation/image/f0b875c4-9e6f-4dde-828c-3a66f34d7cfe?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f0b875c4-9e6f-4dde-828c-3a66f34d7cfe?resizing_type=fit)

Click image for full size.

[![Viewmodes Submenu Button](https://dev.epicgames.com/community/api/documentation/image/eb151b7a-b4f4-463f-84d2-ecd8caadad7b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/eb151b7a-b4f4-463f-84d2-ecd8caadad7b?resizing_type=fit)

Click image for full size.

The most commonly used view modes are shown here:

|  |  |  |
| --- | --- | --- |
| [Viewmode Lit](https://dev.epicgames.com/community/api/documentation/image/93363bec-15e2-49cf-96a8-58b5d63e0b59?resizing_type=fit) | [Viewmode Unlit](https://dev.epicgames.com/community/api/documentation/image/dd342f34-2445-4714-b371-6bb7df11fc66?resizing_type=fit) | [Viewmode Wireframe](https://dev.epicgames.com/community/api/documentation/image/2fda6fbf-1b45-41aa-ab7b-74f511230caf?resizing_type=fit) |
| Lit | Unlit | Wireframe |

See [Viewport Modes](https://dev.epicgames.com/documentation/en-us/unreal-engine/viewport-modes-in-unreal-engine) for a listing and description of all available modes.

## Game View

**Game View** causes the Viewport to display the scene as it would appear in the game. This means that none of the
editor-specific elements - such as the Actor icons - are shown. It gives you an easy way to see just how your level
will look when you run it in the game.

![Drag the slider to toggle Game View.](https://dev.epicgames.com/community/api/documentation/image/5937d1de-46c2-432a-80d0-0814508550b5?resizing_type=fit&width=1920&height=1080)![Drag the slider to toggle Game View.](https://dev.epicgames.com/community/api/documentation/image/35b6eb95-45f7-4007-b6b5-47b12834c022?resizing_type=fit&width=1920&height=1080)

**Drag the slider to toggle Game View.**

To enable Game View, simply press the **G** key (by default) with the Viewport focused or choose the **Game View** option from the
Viewport Options menu:

[![Gamemode Viewport](https://dev.epicgames.com/community/api/documentation/image/74df4105-6c0d-457b-a05e-4e00d69c9109?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/74df4105-6c0d-457b-a05e-4e00d69c9109?resizing_type=fit)

Click image for full size.

## Immersive Mode

Viewports have another state in addition to maximized and minimized that they can be in called **Immersive Mode**. This refers to
Viewport being maximized out to the full extents of the window containing the **Viewport** panel. When you have the Level editor
maximized, this enables you to have your Viewport run in full-screen for a truly *immersive* editing experience!

To enable Immersive Mode, simply press the **F11** key (by default) with the Viewport focused or choose the **Immersive Mode** option
from the Viewport Options menu:

[![Immersive Mode Options](https://dev.epicgames.com/community/api/documentation/image/f10c8dd2-bcca-4238-84d5-1bdc1756592a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f10c8dd2-bcca-4238-84d5-1bdc1756592a?resizing_type=fit)

Click image for full size.

You can restore the Viewport to normal using the same procedure above or by pressing the
button located at the top right of the Viewport when in Immersive Mode.

![Drag the slider to see Immersive Mode in action!](https://dev.epicgames.com/community/api/documentation/image/e858b9d6-1934-4deb-b523-f0978e3cab66?resizing_type=fit&width=1920&height=1080)![Drag the slider to see Immersive Mode in action!](https://dev.epicgames.com/community/api/documentation/image/f215697c-5137-4068-94c0-152d6cd591b4?resizing_type=fit&width=1920&height=1080)![Drag the slider to see Immersive Mode in action!](https://dev.epicgames.com/community/api/documentation/image/83c7358b-a06e-4956-ade3-0c98b5a2bf77?resizing_type=fit&width=1920&height=1080)![Drag the slider to see Immersive Mode in action!](https://dev.epicgames.com/community/api/documentation/image/e8b8f1ed-30fd-4406-85da-c424ac864413?resizing_type=fit&width=1920&height=1080)![Drag the slider to see Immersive Mode in action!](https://dev.epicgames.com/community/api/documentation/image/34744c5b-248f-4de4-b39a-56379d628091?resizing_type=fit&width=1920&height=1080)![Drag the slider to see Immersive Mode in action!](https://dev.epicgames.com/community/api/documentation/image/5c3aec76-a0e1-4afe-bc79-09abd2ff2858?resizing_type=fit&width=1920&height=1080)

**Drag the slider to see Immersive Mode in action!**

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [building virtual worlds](https://dev.epicgames.com/community/search?query=building%20virtual%20worlds)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Viewport Types](/documentation/en-us/unreal-engine/using-editor-viewports-in-unreal-engine?application_version=5.7#viewport-types)
* [Viewport Layout](/documentation/en-us/unreal-engine/using-editor-viewports-in-unreal-engine?application_version=5.7#viewport-layout)
* [View Modes](/documentation/en-us/unreal-engine/using-editor-viewports-in-unreal-engine?application_version=5.7#view-modes)
* [Game View](/documentation/en-us/unreal-engine/using-editor-viewports-in-unreal-engine?application_version=5.7#game-view)
* [Immersive Mode](/documentation/en-us/unreal-engine/using-editor-viewports-in-unreal-engine?application_version=5.7#immersive-mode)
