<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/level-designer-quick-start-in-unreal-engine?application_version=5.7 -->

# Level Designer Quick Start

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
6. Level Designer Quick Start

# Level Designer Quick Start

Get up and running with the basics of the Unreal Editor.

![Level Designer Quick Start](https://dev.epicgames.com/community/api/documentation/image/ede835b9-80e6-484a-904f-74dd89acd001?resizing_type=fill&width=1920&height=335)

###### Prerequisite topics

In order to understand and use the content on this page, make sure you are familiar with the following topics:

* [Installing Unreal Engine](/documentation/en-us/unreal-engine/installing-unreal-engine)
* [Creating a New Project](/documentation/en-us/unreal-engine/creating-a-new-project-in-unreal-engine)

 On this page

Operating System 

×Windows

Select an option from the dropdown to see content relevant to it.

[![Finished](https://dev.epicgames.com/community/api/documentation/image/cd47b4df-de0d-431b-8d02-ec72825caf5b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cd47b4df-de0d-431b-8d02-ec72825caf5b?resizing_type=fit)

At the end of this guide, you'll have a room similar to the one pictured above.

The focus of the Unreal Editor Quick Start Guide is to walk you through the basics of working with Unreal Engine 5.

After going through this tutorial, developers will know the following:

* How to navigate viewports.
* How to create a new level.
* How to place and edit actors in levels.
* How to build and run levels.

## 1. Required Setup

In the **Project Browser**, you can create new projects based off several different template types, or open any previously created projects or samples that you have downloaded. Let's create a new project.

1. After [Installing Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/install-unreal-engine?application_version=5.5) and launching the Unreal Editor, the **Project Browser** appears. **Under New Project Categories**, select a development category. For this quick start, let's create a project from the **Games** category, then click **Next**.

   [![Select Category on Windows.](https://dev.epicgames.com/community/api/documentation/image/7770bea3-b127-4abd-a452-8ae76c4e4728?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7770bea3-b127-4abd-a452-8ae76c4e4728?resizing_type=fit)
2. In the second page of the Project Browser, select the **Blank** template, then click **Next**.

   [![Select the Blank template on Windows](https://dev.epicgames.com/community/api/documentation/image/28b0d6bd-3b33-4617-9c5b-b36a3c7d5394?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/28b0d6bd-3b33-4617-9c5b-b36a3c7d5394?resizing_type=fit)
3. On the final page of the Project Browser, select the **Blueprint** and **With Starter Content** settings, enter a Folder location and Name for your project, then click **Create Project**.

   [![Select Blueprint and With Starter Content on Windows](https://dev.epicgames.com/community/api/documentation/image/1db11af9-1b5e-4ebd-ab2c-7c9563eff9c4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1db11af9-1b5e-4ebd-ab2c-7c9563eff9c4?resizing_type=fit)

## 2. Navigating the Viewport

With the project open and ready to go, the first thing you may notice is the [Viewport](https://dev.epicgames.com/documentation/en-us/unreal-engine/editor-viewports-in-unreal-engine) in the center of the Unreal Editor.

[![Table and chairs](https://dev.epicgames.com/community/api/documentation/image/a2d12865-f1ba-40b0-aec3-f96bf288a7f6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a2d12865-f1ba-40b0-aec3-f96bf288a7f6?resizing_type=fit)

Inside the Viewport is where you will do most of your level construction. The template project that we selected in the previous step includes a small sample [Level](https://dev.epicgames.com/documentation/en-us/unreal-engine/levels-in-unreal-engine) and some assets for us to get started with. Using this little area as a point of reference, take a moment to get used to the [Viewport Camera Controls](https://dev.epicgames.com/documentation/en-us/unreal-engine/viewport-controls-in-unreal-engine) by using the most common methods of navigating the Viewport in Unreal Engine 5.

### Standard Controls

These controls represent the default behavior when clicking and dragging in the viewports with no other keys or buttons pressed. These are also the only controls that can be used to navigate the orthographic viewports.

| Control | Action |
| --- | --- |
| Perspective |  |
| **LMB + Drag** | Moves the camera forward and backward and rotates left and right. |
| **RMB + Drag** | Rotates the viewport camera. |
| **LMB + RMB + Drag** | Moves up and down. |
| Orthographic (Top, Front, Side) |  |
| --- | --- |
| **LMB + Drag** | Creates a marquee selection box. |
| **RMB + Drag** | Pans the viewport camera. |
| **LMB + RMB + Drag** | Zooms the viewport camera in and out. |
| Focusing |  |
| --- | --- |
| **F** | Focuses the camera on the selected object. This is essential to make the most out of tumbling the camera. |

To switch to an [Orthographic View](https://www.youtube.com/watch?v=RoiQOwCg-4Q), click the **Perspective** drop-down then select an Orthographic View Mode.

[![Orthographic views](https://dev.epicgames.com/community/api/documentation/image/f6a87dc5-fb87-4820-b3c5-e85ee6f900ec?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f6a87dc5-fb87-4820-b3c5-e85ee6f900ec?resizing_type=fit)

Click image for full size.

### WASD Fly Controls

All of these controls are only valid in a Perspective viewport, and by default you must hold **RMB** to use the WASD game-style controls.

| Control | Action |
| --- | --- |
| **W** / **Numpad8** / **Up** | Moves the camera forward. |
| **S** / **Numpad2** / **Down** | Moves the camera backward. |
| **A** / **Numpad4** / **Left** | Moves the camera left. |
| **D** / **Numpad6** / **Right** | Moves the camera right. |
| **E** / **Numpad9** / **Page Up** | Moves the camera up. |
| **Q** / **Numpad7** / **Page Dn** | Moves the camera down. |
| **Z** / **Numpad1** | Zooms the camera out (raises FOV). |
| **C** / **Numpad3** | Zooms the camera in (lowers FOV). |

### Orbit, Dolly, and Track

Unreal Editor supports Maya-style pan, orbit, and zoom viewport controls, making it much easier for Maya artists to jump into the tool. If you are unfamiliar, here is a breakdown of the keys:

| Command | Description |
| --- | --- |
| **Alt + LMB + Drag** | Tumbles the viewport around a single pivot or point of interest. |
| **Alt + RMB + Drag** | Dollies (zooms) the camera toward and away from a single pivot or point of interest. |
| **Alt + MMB + Drag** | Tracks the camera left, right, up, and down in the direction of mouse movement. |

The use of the F key is not limited to Maya-style controls. You can always press F to focus on a selected object or group of objects.

## 3. Create a New Level

Next we will create a new [Level](https://dev.epicgames.com/documentation/en-us/unreal-engine/levels-in-unreal-engine) that we will use to build our game environment in. While there are several different ways in which you can create a new Level, we will use the **File Menu** method, which lists level selection options.

1. Inside the Unreal Editor, click the **File Menu** option then select **New Level...**.

   [![Create New Level on Windows](https://dev.epicgames.com/community/api/documentation/image/1a8fef58-2cff-474b-9071-27cfc8d60c56?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1a8fef58-2cff-474b-9071-27cfc8d60c56?resizing_type=fit)
2. This opens the **New Level** dialog window.

   [![New level dialog window on Windows](https://dev.epicgames.com/community/api/documentation/image/bf122a76-ac0c-4622-b57f-9c7096b46759?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bf122a76-ac0c-4622-b57f-9c7096b46759?resizing_type=fit)

   The **Default** level includes some of the commonly-used assets for constructing levels, the **VR-Basic** level includes some assets for constructing levels with the VR Editor, and **Empty Level**
   is a completely blank level with no assets. For the purposes of this
   guide you are going to start from scratch with a completely blank slate.
3. Click the **Empty Level** to select it.

## 4. Placing Actors in the Level

In this step, we will begin placing [Actors](https://dev.epicgames.com/documentation/en-us/unreal-engine/actors-and-geometry-in-unreal-engine) (for example, lights or geometry) into our empty level. We will cover the two most common ways of adding Actors to the level: through [Select Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/select-mode-in-unreal-engine) and through the [Content Browser](https://dev.epicgames.com/documentation/en-us/unreal-engine/content-browser-in-unreal-engine). After completing this step, you will know how to place Actors inside your own levels and can begin manipulating those Actors to create your environment.

1. In the **Place Actors** panel on the left, click the [Geometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine) category and select the **Box**.

   [![Modes panel](https://dev.epicgames.com/community/api/documentation/image/91dad2f6-83da-47c6-a5d4-5e7c33ecffe6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/91dad2f6-83da-47c6-a5d4-5e7c33ecffe6?resizing_type=fit)

   Click image for full size.
2. **Left-click** and drag the **Box** into the **Level Viewport**.

   [![Place box](https://dev.epicgames.com/community/api/documentation/image/3ad201cb-0b8f-4f54-92d3-b6896970d293?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3ad201cb-0b8f-4f54-92d3-b6896970d293?resizing_type=fit)

   Click image for full size.

   When you release the **Left Mouse Button**, the **Box** is added to the level.

   [![Place](https://dev.epicgames.com/community/api/documentation/image/0ebb86b6-2808-4127-af60-f0df85264be5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0ebb86b6-2808-4127-af60-f0df85264be5?resizing_type=fit)
3. In the [Details](https://dev.epicgames.com/documentation/en-us/unreal-engine/level-editor-details-panel-in-unreal-engine) panel (lower-right window of the editor), with the **Box** still selected, set **Location** and **Rotation** all to **0**.
4. Set the **Scale** to **4 x 4 x 0.1**.

   [![Resize floor](https://dev.epicgames.com/community/api/documentation/image/7817a540-3f6b-4059-8a57-47b3cf9031ec?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7817a540-3f6b-4059-8a57-47b3cf9031ec?resizing_type=fit)

   Click image for full size.

   We will use this as the floor on which the player can walk around.
5. In the **Place Actors** panel select the **Lights** tab, then drag-and-drop a **Directional Light** into the level on top of the floor.

   [![Place light](https://dev.epicgames.com/community/api/documentation/image/7e73203e-c2d9-46c4-b7c9-2f09ef7961d5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7e73203e-c2d9-46c4-b7c9-2f09ef7961d5?resizing_type=fit)

   Click image for full size.
6. On the [Translation Tool](https://dev.epicgames.com/documentation/en-us/unreal-engine/editor-viewports-in-unreal-engine), click and drag the Z-Axis (blue) on the gizmo up, away from the surface of the floor.

   [![Move light](https://dev.epicgames.com/community/api/documentation/image/2b12de44-6431-47b0-9bdb-df351ec88203?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2b12de44-6431-47b0-9bdb-df351ec88203?resizing_type=fit)

   If the **Directional Light** becomes unselected, you can re-select it by **Left-clicking** on it in the **Level Viewport**.
7. In the **Place Actors** panel, select the **Visual Effects** tab and drag-and-drop an [Volumetric Cloud](https://dev.epicgames.com/documentation/en-us/unreal-engine/volumetric-cloud-component-in-unreal-engine) into the level.

   [![Place fog](https://dev.epicgames.com/community/api/documentation/image/bff99785-a01a-41c0-8eca-50ef40505260?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bff99785-a01a-41c0-8eca-50ef40505260?resizing_type=fit)

   Click image for full size.

   The **Volumetric Cloud** Actor will add a basic sky to the level and the level will become illuminated instead of dark.
8. In the **Place Actors** panel, select the **Basic** tab and drag-and-drop a [Player Start](https://dev.epicgames.com/documentation/en-us/unreal-engine/player-start-actor-in-unreal-engine) into the level.

   [![Place start](https://dev.epicgames.com/community/api/documentation/image/df6d1db9-22d7-4873-bc27-fbb80888581e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/df6d1db9-22d7-4873-bc27-fbb80888581e?resizing_type=fit)

   Click image for full size.
9. In the **Place Actors** panel, select the **Volumes** tab and drag-and-drop a [Lightmass Importance Volume](https://dev.epicgames.com/documentation/en-us/unreal-engine/lightmass-basics-in-unreal-engine) into the level.

   [![Place volume](https://dev.epicgames.com/community/api/documentation/image/46cfbab8-33bd-4761-9ee8-324c91695b1f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/46cfbab8-33bd-4761-9ee8-324c91695b1f?resizing_type=fit)

   Click image for full size.

   The **Lightmass Importance Volume** is used to control and concentrate lighting and shadowing effects within the volume. When placing the Lightmass Importance Volume in the level, the default size of the volume does not cover our playable area, so we will need to scale it up.
10. Inside the **Level Viewport**, press **R** to switch to the [Scale Tool](https://dev.epicgames.com/documentation/en-us/unreal-engine/viewport-controls-in-unreal-engine#moving-rotating-and-scaling-objects-in-the-level).
11. Click and drag the white box in the center of the **Scale Tool** so that the **Lightmass Importance Volume** encapsulates the floor.

    [![Scale volume](https://dev.epicgames.com/community/api/documentation/image/7ac1037c-1676-4b51-834b-81376163d7d6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7ac1037c-1676-4b51-834b-81376163d7d6?resizing_type=fit)

    Click image for full size.
12. Inside the **Content Browser** under **Content** > **StarterContent** > **Props**, drag-and-drop the **SM\_TableRound** into the level.

    [![Place table](https://dev.epicgames.com/community/api/documentation/image/56b26ad8-cfd1-450a-9bb3-385eae5def95?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/56b26ad8-cfd1-450a-9bb3-385eae5def95?resizing_type=fit)

    Click image for full size.

    Try to place the table in the center of the floor using the **Move Tool** (press **W** if it is not selected).
13. Also under **Content** > **StarterContent** > **Props**, drag-and-drop the **SM\_Chair** into the level.

    [![Add chair](https://dev.epicgames.com/community/api/documentation/image/b50a2c2a-f38a-48dd-b98a-9c16c2231387?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b50a2c2a-f38a-48dd-b98a-9c16c2231387?resizing_type=fit)

    Click image for full size.
14. With the **SM\_Chair** selected inside the **Level Viewport**, press **E** to access the Rotation Tool.

    [![Rotate](https://dev.epicgames.com/community/api/documentation/image/9537b93f-07c3-46ad-9c33-87784aa65bb0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9537b93f-07c3-46ad-9c33-87784aa65bb0?resizing_type=fit)
15. **Left-click** and drag the blue axis arc (the gizmo will update to show degrees) and rotate the chair to face the table.

    [![Rotate](https://dev.epicgames.com/community/api/documentation/image/f10cfd27-10c6-4673-a9aa-4c1d8c9fa025?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f10cfd27-10c6-4673-a9aa-4c1d8c9fa025?resizing_type=fit)
16. Using the placement methods above, create a small scene by adding more Actors from the **Modes Panel** and **Content Browser**.

    [![Place things](https://dev.epicgames.com/community/api/documentation/image/5c89a82f-a80f-4264-bc1c-4d4f6b3e216c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5c89a82f-a80f-4264-bc1c-4d4f6b3e216c?resizing_type=fit)

    Click image for full size.

    Try adding some lights, props, walls and a roof (found under the **Content** > **StarterContent** > **Architecture** folder).

Need help punching out the holes for windows and doors? Check out our video on [Adding Windows & Doors](https://youtu.be/RGxf2SiUBt8).

## 5. Editing Placed Actors

With several different **Actors** placed inside our level, the next step involves [Editing Actor Properties](https://dev.epicgames.com/documentation/en-us/unreal-engine/actor-snapping-in-unreal-engine) that can change the look or the way the Actor functions in the level, giving us a more customized looking level. We will start with editing the properties of our **Directional Light Actor** then shift our focus to applying [Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-materials) to some of the [Static Mesh Actors](https://dev.epicgames.com/documentation/en-us/unreal-engine/static-mesh-actors-in-unreal-engine) that you have placed in your level.

Once you have finished this step, you will have seen where to access and modify the properties of Actors, so that you can begin editing and experimenting with different settings inside your own levels.

1. Select the **Directional Light Actor** by **Left-clicking** on it in the Viewport.

   [![Select the Directional Light](https://dev.epicgames.com/community/api/documentation/image/ed725438-3deb-4ea4-ab17-8a6f44a6e321?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ed725438-3deb-4ea4-ab17-8a6f44a6e321?resizing_type=fit)
2. In the **Details Panel** under the **Light** category, enable **Atmosphere Sun Light**:

   [![Enable sun](https://dev.epicgames.com/community/api/documentation/image/97c8b6b8-48d1-4ed9-9bb9-c5517d02d2cd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/97c8b6b8-48d1-4ed9-9bb9-c5517d02d2cd?resizing_type=fit)

   Click image for full size.

   Depending on the rotation of your Directional Light Actor, the sky color will change. If you rotate the Viewport around, you will see that the sun now aligns with the Directional Light Actor. This is a real time process, so you can rotate the Directional Light Actor (press **E** to switch to **Rotation Mode**) and the sky will change color from night to sunrise, daytime, and sunset.

Next we will change the **Material** on one of your placed **Static Mesh Actors** by first selecting it.

1. With your Actor selected, in the **Details** panel under **Materials**, click the drop-down box under **Element 0**.

   [![Material](https://dev.epicgames.com/community/api/documentation/image/71b6bf54-f0f9-4c1a-b80a-90f91c00eeec?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/71b6bf54-f0f9-4c1a-b80a-90f91c00eeec?resizing_type=fit)

   Click image for full size.
2. In the pop-up window, select the **M\_Brick\_Clay\_New** Material.

   [![Material](https://dev.epicgames.com/community/api/documentation/image/5de7186a-fdfc-4e59-a90f-90b9d98292d4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5de7186a-fdfc-4e59-a90f-90b9d98292d4?resizing_type=fit)

   Click image for full size.
3. All **Actors** in your level have many properties for you to adjust inside the **Details** panel. Explore changing their settings!

   [![Before bake](https://dev.epicgames.com/community/api/documentation/image/47caf1f5-047b-4847-98c2-ce4f23208719?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/47caf1f5-047b-4847-98c2-ce4f23208719?resizing_type=fit)

   Click image for full size.

   Try changing the **Light Color** of your lights, applying more **Materials** or changing the **Scale** of the Actors in your level.

## 6. Running the Build Process

By now you may have noticed the "Preview" labels in the shadows and the light leaking under walls.

[![Before bake](https://dev.epicgames.com/community/api/documentation/image/bf201ae7-87b9-4dd5-bf08-57d31f8ce415?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bf201ae7-87b9-4dd5-bf08-57d31f8ce415?resizing_type=fit)

This is because all the lights in the scene are static and use precomputed, or baked lighting, which has not been calculated yet. The "Preview" text is there to remind you that what you are seeing in the viewport currently is not what you will see in the game.

In this step, we will go through the **Build** process which will build all levels (precompute lighting data and visibility data, generate any navigation networks and update all brush models). We will also take a look at **Light Quality** settings inside of the **Build Options**, which we can use to adjust the quality of our lighting when it is built.

1. From the Main Toolbar, click the down-arrow next to the **Build** option.

   [![Build options button](https://dev.epicgames.com/community/api/documentation/image/dd1b2f77-9368-4278-a1d1-d24d7e2b588e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dd1b2f77-9368-4278-a1d1-d24d7e2b588e?resizing_type=fit)

   Click image for full size.
2. Under **Lighting Quality**, choose the **Production** setting.

   [![Production lighting](https://dev.epicgames.com/community/api/documentation/image/35f7f9f9-fb77-4c7e-906c-973abc4099f9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/35f7f9f9-fb77-4c7e-906c-973abc4099f9?resizing_type=fit)

   Click image for full size.

   This will give us the highest quality lighting but is the slowest in terms of computation time and will increase the time it takes to **Build** the game. Our level is small, so it should not impact us too much, but keep this in mind when you are working on larger levels as you may want to leave it on a mid-low level setting while creating your level and switching it to **Production** in a "final pass" on your level.
3. Wait for the **Build** to complete.

   [![Wait](https://dev.epicgames.com/community/api/documentation/image/24147e48-303f-4e35-8f4b-92b7dd1e611a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/24147e48-303f-4e35-8f4b-92b7dd1e611a?resizing_type=fit)

   You will see the progress in the lower-right corner of the Unreal Editor as seen in the image above. Once the **Build** process is complete, the level lighting will update to give you a better indication of the final result.

   [![Built](https://dev.epicgames.com/community/api/documentation/image/5459bf05-2458-4ae8-959c-55f262953a1b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5459bf05-2458-4ae8-959c-55f262953a1b?resizing_type=fit)
4. From the Main Toolbar, click the **Play** Button to play in the editor.

   [![Play in editor](https://dev.epicgames.com/community/api/documentation/image/98842d1c-7b02-4863-9eeb-eae50c4d4c36?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/98842d1c-7b02-4863-9eeb-eae50c4d4c36?resizing_type=fit)

   Click image for full size.

   Using **WASD** to move and the **Mouse** to turn the camera, you can fly around your level.

## 7. On Your Own!

At this point, you should have created a **Build** of the level lighting and previewed your game with the **Play** in Editor feature. Each of the steps leading up to this point have been aimed at getting you quickly up to speed on how to perform the most common actions when constructing levels inside the Unreal Editor.

Using the methods that were provided during the course of this guide, try to do the following on your own:

[![Update](https://dev.epicgames.com/community/api/documentation/image/1e81d6a7-7802-4385-a9e5-2404b67d806a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1e81d6a7-7802-4385-a9e5-2404b67d806a?resizing_type=fit)

* Change the lighting of the level to a moonlit, night scene.
* Add another room, attached to the first room.

[![Update](https://dev.epicgames.com/community/api/documentation/image/d299bd2c-64a2-4bcd-b434-264d13faeaff?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d299bd2c-64a2-4bcd-b434-264d13faeaff?resizing_type=fit)

[![Update](https://dev.epicgames.com/community/api/documentation/image/2f33a1af-e682-4ad3-8a16-b0275bfcbb68?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2f33a1af-e682-4ad3-8a16-b0275bfcbb68?resizing_type=fit)

* On the attached room, try to make it elevated and join them with stairs.
* Add some bushes, a couch, shelves and a front door.

[![Update](https://dev.epicgames.com/community/api/documentation/image/602f497c-ef03-4fdf-bfd6-c8077809f387?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/602f497c-ef03-4fdf-bfd6-c8077809f387?resizing_type=fit)

* Add different kinds of lights with different colors.
* Use different Materials on some of your Actors.

For more information on the topics covered in this quick start guide, see the [Building Virtual Worlds](https://dev.epicgames.com/documentation/en-us/unreal-engine/building-virtual-worlds-in-unreal-engine).

As for specifics covered in this quick start:

* For more information on the Level Editor, see: [Level Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/level-editor-in-unreal-engine)
* For more information on Viewports, see: [Viewports](https://dev.epicgames.com/documentation/en-us/unreal-engine/editor-viewports-in-unreal-engine)
* For more information on the Editing Modes available in Unreal Editor, 5 see: [Level Editor Modes](https://dev.epicgames.com/documentation/en-us/unreal-engine/level-editor-modes-in-unreal-engine)
* For more information on the Content Browser, see: [Content Browser](https://dev.epicgames.com/documentation/en-us/unreal-engine/content-browser-in-unreal-engine)
* For more information on the Details Panel, see: [Details Panel](https://dev.epicgames.com/documentation/en-us/unreal-engine/level-editor-in-unreal-engine)
* For more information on Building, see: [Lightmass](https://dev.epicgames.com/documentation/en-us/unreal-engine/global-illumination-in-unreal-engine)
* For more information on Lighting, see: [Lighting the Environment](https://dev.epicgames.com/documentation/en-us/unreal-engine/lighting-the-environment-in-unreal-engine)

* [landscape](https://dev.epicgames.com/community/search?query=landscape)
* [building virtual worlds](https://dev.epicgames.com/community/search?query=building%20virtual%20worlds)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [1. Required Setup](/documentation/en-us/unreal-engine/level-designer-quick-start-in-unreal-engine?application_version=5.7#1-required-setup)
* [2. Navigating the Viewport](/documentation/en-us/unreal-engine/level-designer-quick-start-in-unreal-engine?application_version=5.7#2-navigating-the-viewport)
* [Standard Controls](/documentation/en-us/unreal-engine/level-designer-quick-start-in-unreal-engine?application_version=5.7#standard-controls)
* [WASD Fly Controls](/documentation/en-us/unreal-engine/level-designer-quick-start-in-unreal-engine?application_version=5.7#wasd-fly-controls)
* [Orbit, Dolly, and Track](/documentation/en-us/unreal-engine/level-designer-quick-start-in-unreal-engine?application_version=5.7#orbit-dolly-and-track)
* [3. Create a New Level](/documentation/en-us/unreal-engine/level-designer-quick-start-in-unreal-engine?application_version=5.7#3-create-a-new-level)
* [4. Placing Actors in the Level](/documentation/en-us/unreal-engine/level-designer-quick-start-in-unreal-engine?application_version=5.7#4-placing-actors-in-the-level)
* [5. Editing Placed Actors](/documentation/en-us/unreal-engine/level-designer-quick-start-in-unreal-engine?application_version=5.7#5-editing-placed-actors)
* [6. Running the Build Process](/documentation/en-us/unreal-engine/level-designer-quick-start-in-unreal-engine?application_version=5.7#6-running-the-build-process)
* [7. On Your Own!](/documentation/en-us/unreal-engine/level-designer-quick-start-in-unreal-engine?application_version=5.7#7-on-your-own)
