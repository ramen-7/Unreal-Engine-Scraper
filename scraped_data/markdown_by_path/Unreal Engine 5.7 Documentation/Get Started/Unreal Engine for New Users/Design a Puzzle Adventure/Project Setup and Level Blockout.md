<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine?application_version=5.7 -->

# Project Setup and Level Blockout

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
5. [Get Started](/documentation/en-us/unreal-engine/get-started "Get Started")
6. [Unreal Engine for New Users](/documentation/en-us/unreal-engine/unreal-engine-for-new-users "Unreal Engine for New Users")
7. [Design a Puzzle Adventure](/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine "Design a Puzzle Adventure")
8. Project Setup and Level Blockout

# Project Setup and Level Blockout

Get started planning, designing, and blocking out your puzzle adventure level! Practice using different Viewport modes, transforming objects, and organizing assets in the Outliner.

![Project Setup and Level Blockout](https://dev.epicgames.com/community/api/documentation/image/1e5a0712-c9be-4718-a6cb-e4f6567cde63?resizing_type=fill&width=1920&height=335)

 On this page

In this section of the tutorial series, you’ll get comfortable with the basics of the Unreal Editor, including how to create a new level, place and transform objects, work with different viewport modes, and use the Outliner to stay organized.

You’ll also learn how to block out your ideas using simple shapes while applying level design concepts like scale, verticality, occlusion, contrast, and guiding lines. These are all tools that influence how players move through and experience your level.

By the end, you’ll have a playable space that sets the foundation for the gameplay you’ll create in the next sections of the track.

[![Image-of-the-first-person-level-with-a-ramp-and-wall](https://dev.epicgames.com/community/api/documentation/image/3dcb461a-822d-4f0a-afd1-f1ad9d77639a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3dcb461a-822d-4f0a-afd1-f1ad9d77639a?resizing_type=fit)

### Before You Begin

Ensure you’ve [installed the Epic Games Launcher and Unreal Engine](https://www.epicgames.com/help/en-US/epic-games-store-c-202300000001639/launcher-support-c-202300000001735/how-to-download-the-epic-games-launcher-a202300000012839).

To follow this tutorial, you must understand the basics of Unreal Editor toolbars, panels, and Viewport controls. For more information, refer to the other pages in the [Unreal Engine for New Users](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-for-new-users) documentation before starting this tutorial:

* [Unreal Editor Interface](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-editor-interface)
* [Viewport Controls](https://dev.epicgames.com/documentation/en-us/unreal-engine/viewport-controls-in-unreal-engine)
* [Viewport Toolbar](https://dev.epicgames.com/documentation/en-us/unreal-engine/viewport-toolbar)

## Sketch Your Ideas

Before starting to build in the editor, spend 10-20 minutes writing or sketching your ideas out on paper first. This initial iteration can help you:

* Figure out the basic gameplay beats and concepts in your level.
* See if your gameplay ideas might flow well and fit in scope before investing time building them in the editor.
* Remember your ideas between working sessions.

You can approach this initial design in different ways, such as leading with gameplay mechanics or leading with level design. Choose or combine level design techniques based on the type of game you are creating and personal preference. There is no singular correct approach to game design—it's the result that matters. Games where level design and gameplay support each other are more cohesive and create a more immersive and engaging experience for the player.

One technique, node mapping, involves drawing a simplified, abstract diagram of circles and lines to show the different spaces in the level, what happens in those spaces, and how the player can transition from space to space. Node mapping focuses on gameplay pacing, branching paths, and player choices. One node represents one player action or event. The event can inspire the shape of that space.

This tutorial uses a series of rooms to show you how to implement common gameplay objects like restricting the player with locked doors and keys, creating obstacles that can damage the player, and adding platforms and switches to defeat those obstacles. Here’s how we sketched out this sort of level idea in nodes:

[![Hand-sketch-of-floorplan-and-gameplay-for-each-room](https://dev.epicgames.com/community/api/documentation/image/106a4aca-c5b6-4d4a-b5da-56540f45256e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/106a4aca-c5b6-4d4a-b5da-56540f45256e?resizing_type=fit)

Another technique is to **draw a visual sketch** of a top-down, side, or orthographic view of the level’s actual layout. Here, the focus starts with level design, not gameplay. The shape of the level’s spaces can inspire player actions and events.

Here’s how we first sketched out the room and hallway design for our tutorial level:

[![Floorplan-with-room-descriptions](https://dev.epicgames.com/community/api/documentation/image/7a2e3e5f-95bf-4503-ad2f-af70c6aa50f0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7a2e3e5f-95bf-4503-ad2f-af70c6aa50f0?resizing_type=fit)

You can also design with **player verbs**, or the actions that the player is capable of in your game, like jump, run, hide, grab, craft, shoot, melee, and talk. This shifts your focus from the things in the world to what the player is engaging in. This way of thinking can help boost your level’s engagement, fun, and pacing.

As you design your level’s spaces, think about where you can add opportunities to use those player verbs meaningfully. The verbs can inform the design of the space. For example, if your verb is **jump**, you could add a gap to cross, some platforms, vertical space, or an enemy or hazard to jump over. Vary these verbs from space to space to keep gameplay fresh and well-paced.

No matter what approach you take to design a level and its gameplay, always consider what the player is doing.

## Create Your Project

To get started, create a new project using the First-Person template. Templates include premade assets such as meshes, gameplay objects, and a player character that are useful for expediting level design.

A **mesh** is a 3D model, or the set of polygons that create a 3D model. A **static mesh** is a 3D model used to make an object in your level that can be translated, rotated, and scaled.

If you started with the [Programming Track](https://dev.epicgames.com/documentation/en-us/unreal-engine/code-a-firstperson-adventure-game-in-unreal-engine) tutorial, you can continue using your project in this track.

To create a new first-person project, follow these steps:

1. Open Unreal Editor. In the **Unreal Project Browser**, go to the **Games** project category, and select the **First Person** template.
2. Keep all **Project Defaults**, and select **Arena Shooter** as the **Variant**. Template variants include additional assets and a sample level that corresponds to that gameplay genre.

   [![Screenshot-of-first-person-template-with-blueprint-and-arena-shooter](https://dev.epicgames.com/community/api/documentation/image/4408d010-f4e9-4fad-90fd-ddfec3d06100?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4408d010-f4e9-4fad-90fd-ddfec3d06100?resizing_type=fit)
3. **Name** your project. This tutorial uses `AdventureGame` as the project name.
4. Click **Create** to open your new project in Unreal Editor.

Your project opens with the `Lvl_FirstPerson` sample level open in the viewport.

[![Image-first-person-sample-level](https://dev.epicgames.com/community/api/documentation/image/1ec4f0f6-2e0f-428b-b8d9-21ca405a8c3d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1ec4f0f6-2e0f-428b-b8d9-21ca405a8c3d?resizing_type=fit)

## Start a New Level

To start making this project your own, create a brand-new **level** (sometimes called a **map**), explore its contents, set up how the game starts, and play it for the first time.

When you're working in Unreal Editor, if you run into unexpected behavior (for example, assets or actors not appearing or updating), try restarting the editor. Because Unreal Engine heavily relies on caching, a restart can often resolve these issues.

To create a new level, follow these steps:

1. In Unreal Editor’s menu bar, go to **File**, and select **New Level**.

   [![Create-a-basic-new-level](https://dev.epicgames.com/community/api/documentation/image/17bf6810-cf77-44f4-b0ad-66d66ae26866?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/17bf6810-cf77-44f4-b0ad-66d66ae26866?resizing_type=fit)
2. In the **New Level** window, select **Basic**, and click **Create**. This gets you started with a floor, sky, player spawn, and ambient lighting.

   [![View-of-your-new-level-with-floor-and-sky](https://dev.epicgames.com/community/api/documentation/image/5fd3742c-f29c-402e-891c-8dba92608efe?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5fd3742c-f29c-402e-891c-8dba92608efe?resizing_type=fit)
3. Go to **File > Save Current Level**.
4. Create a folder structure to store the assets you’ll create throughout this tutorial series:

   * In the **Save Level As** window, in the left panel, right-click the **Content** folder and select **New Folder**.
   * Name this folder after your project. This tutorial uses `AdventureGame`.
   * Right-click your new folder and select **New Folder**.
   * Name this folder `Designer` and select it.
5. Enter a name for your level and click **Save**. This tutorial uses `Lvl_Adventure`.

### Explore the Outliner and Details Panels

Look at the **Outliner** to see a list of all objects in your level. These objects are also often called **actors**.

[![Page-tree-showing-lighting-options-for-the-level-adventure](https://dev.epicgames.com/community/api/documentation/image/709466e6-412b-4f9f-9243-5f0cb0c4d0cf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/709466e6-412b-4f9f-9243-5f0cb0c4d0cf?resizing_type=fit)

In the **Lighting** folder, there’s a set of objects that control the background and ambient lighting in your level. To see how each contributes to your level’s look and feel, hover over each and click the eye icon to toggle its visibility in the viewport.

![Gif-to-show-toggling-visibility-in-lighting-folder](https://dev.epicgames.com/community/api/documentation/image/023a7501-4cd1-47bb-8714-a23c5d9f2f9d?resizing_type=fit)

The location of these lighting level objects doesn’t matter, so you can move them out of the way if desired.

The level also contains a floor mesh and a **PlayerStart** spawn point that controls where players start the level.

In the **Outliner**, click the **DirectionalLight**. This light is configured to act as the sun (or moon) that lights your level and casts shadows. In the **Details** panel, you can view and change the light’s properties, such as **Color** or **Intensity**, and see the results update instantly in the viewport.

[![Image-showing-adjustments-to-the-light-source](https://dev.epicgames.com/community/api/documentation/image/74604e49-aee7-49b9-841d-29a045bb8720?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/74604e49-aee7-49b9-841d-29a045bb8720?resizing_type=fit)

If you can’t find an object in the viewport, in the **Outliner**, click that object and press **F** to reposition the viewport to focus on that object.

To learn more about customizing your level’s lighting, see [Lighting the Environment](https://dev.epicgames.com/documentation/en-us/unreal-engine/environmental-light-with-fog-clouds-sky-and-atmosphere-in-unreal-engine).

### Preview Gameplay in the Viewport

The viewport shows a preview of the level. In the Viewport Toolbar, click **Play** to play your level within the viewport. This is often also called **Play-In-Editor** (**PIE**) mode. With PIE mode, you can test how your project functions at runtime from within Unreal Editor (either within a viewport or in a new window).

**Runtime** refers to the period of time when a project is running on its target platform, such as your machine or a console.

When you play the level, you’ll spawn at the location of the PlayerStart.

Then, click the viewport and use **WASD** or **arrow keys** to move around and **Spacebar** to jump.

Look down and you’ll see that your game is using a default first-person player character.

[![Player-looking-down-at-his-own-shadow-on-the-ground](https://dev.epicgames.com/community/api/documentation/image/d063d3c7-3ac6-4230-8dad-8bb08a017b90?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d063d3c7-3ac6-4230-8dad-8bb08a017b90?resizing_type=fit)

Press **Shift+F1** to switch back to your cursor and click **Stop** (or press **Escape**) to quit Play mode.

To play a full, standalone version of your game, click the three dots next to the Play Mode controls and select **Standalone Game** mode. This plays your game in a new window and simulates a finished, exported version of your game, allowing you to test UI menus and load screens, resolution scaling, and mouse input. However, this mode still runs within the editor. To build and run a temporary `.exe` version of your packaged game, select **Quick Launch** mode.

Use this menu to switch back to play-in-viewport mode.

[![Image-of-ellipses-menu](https://dev.epicgames.com/community/api/documentation/image/5b2f6af2-1251-4290-8e9a-1b20cccf76d3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5b2f6af2-1251-4290-8e9a-1b20cccf76d3?resizing_type=fit)

If Unreal Editor is feeling slow on your computer, click the **Performance and Scalability** tools button near the top-right corner of the viewport, go to **Viewport Scalability**, and select a lower quality setting. Or, near the right side of the Viewport Toolbar, click **Lit** to open the **View Mode** menu, and select **Unlit**. This only affects Unreal Editor, not your final project.

[![Viewport-scalability-adjustments-to-increase-responsiveness](https://dev.epicgames.com/community/api/documentation/image/d00f9ef7-1eb0-4b90-aae7-58fb168248a6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d00f9ef7-1eb0-4b90-aae7-58fb168248a6?resizing_type=fit)

### Change the Startup Level

Use Project Settings to change the level that loads when you open your project in Unreal Editor and when playing your finished game.

To change your project’s default starting level, follow these steps:

1. In the editor’s main menu, go to **Edit > Project Settings**.
2. In the **Project** section in the left panel, select **Maps & Modes**.
3. In the Default Maps section, change **Editor Startup Map** and **Game Default Map** to your new level. 
   The editor opens the **Editor Startup Map** when you open your project, and Unreal Engine loads the **Game Default Map** when playing a standalone or packaged `.exe` of your project.

   [![Image-of-adjusting-maps-and-modes-in-project-settings](https://dev.epicgames.com/community/api/documentation/image/aa88222f-08e1-411a-b1a3-3769093d0d11?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/aa88222f-08e1-411a-b1a3-3769093d0d11?resizing_type=fit)
4. Close **Project Settings**.

## Block Out Your Map

Now that you have a concept, a fresh project, and a new level, you can begin designing in Unreal Editor.

Before thinking about finished art and polished details, it’s important to first focus on the layout and playability of your level. This design phase is often called **blockout** (or **grayboxing**) and involves building the rough spaces in your level with simple shapes that represent walls, pathways, and functional obstacles. It’s like sketching with a pencil on a canvas before finalizing it with paint.

Blockout is a tool that helps you quickly iterate and test ideas to decide what is or isn't working in your design. Remember that this isn’t the final product; this process should be fast in order to allow for more time spent on parts of the game that players will actually interact with.

Blocking out your level helps you:

* Start designing gameplay without waiting for a finished art design.
* Catch design issues earlier.
* Experiment and iterate quickly without risking redoing art assets.
* Test scale, sight lines, and gameplay flow without spending time on details that are unnecessary at this stage.

You’re creating the simplest and most navigable version of your level possible, only with the obstacles that support the gameplay. Instead of looks, focus on how the space feels, if it’s fun, and if it supports your gameplay goals. Because you’re using basic shapes, if something isn’t working, you can remove it and try something new.

You can incorporate both layout and artistic design choices into your blockout, as long as they are functional and support the gameplay. Successful games use both types of design elements to create engaging and immersive spaces.

|  | Do Add to Your Blockout | Don't Add to Your Blockout |
| --- | --- | --- |
| **Layout design choices** | * A rectangular block that acts as a fallen beam, restricting passage through a hallway. * Pillars that block line of sight, creating depth, a reveal, or cover for the player. | * A rectangular block that represents a purely decorative bookshelf against the wall. |
| **Artistic design choices** | * A light that acts as a neon sign that draws the player to a certain area or object. | * A light that represents an atmospheric campfire. |

### Determine Your Scale

Before you get too far blocking out your level, it’s important to establish your game’s standard measurements and **scale**. This includes deciding on the size of common structures in your level, such as:

* The height of jumpable objects, climbable objects, cover, corridors, and rooms.
* The size of doors, windows, and corridors.

When tuning your level’s scale, your goal is to make the level consistent, natural, and easily understood. Your blockout also creates the scale for the environment artists.

In Unreal Engine, you’ll work with **centimeter units**, and 100 centimeters equals 1 meter.

#### Make it Feel Natural

The features of the space should feel believable based on the player’s size. However, keep in mind that total realism doesn’t always translate well to games. For example, a 0.8m-wide doorway might feel spacious in real life, but be too cramped in-game or prevent the camera from passing through without clipping. Find the balance between realism and fun that is believable for your type of game.

[![Image-showing-walls-and-platform-for-examining-in-game-scale](https://dev.epicgames.com/community/api/documentation/image/d52a4d5a-6f33-49b0-a2ad-aa38964f5b68?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d52a4d5a-6f33-49b0-a2ad-aa38964f5b68?resizing_type=fit)

Your scale depends on player size, how a space should feel, and what gameplay the space will support. Is the space a cramped, claustrophobic hallway, or an open and airy room? Does it need to fit one player, several players, or an enemy encounter?

As you decide on the scale of your level’s spaces, keep these average measurements in mind

| Level Object | Standard Measurement |
| --- | --- |
| **Human character** | 1.8m tall, jumps 0.5m high |
| **Hallways** | 2-3m wide, 3-4m tall  Third-person cameras require wider hallways to fit a camera. |
| **Doors** | 1 - 1.5m wide, 2m tall |
| **Walls** | 4m tall |

Remember, these are just guidelines. The design and scale of your level should match the needs of your gameplay experience.

#### Make it Easily Understood

The scale of a level’s features should be easily readable and predictable for the player. When the player walks up to an object, they should know at a glance whether it’s meant to be crouched next to for cover, jumped on, climbed, or is impassable.

For example, here’s a short structure that represents a little garden wall as a leading line to guide the player along, but not jump over. It’s 0.6m tall (10cm higher than the player’s jump height).

[![Image-of-a-retaining-wall-just-higher-than-the-players-jump-height](https://dev.epicgames.com/community/api/documentation/image/af1e052b-1c7d-4d67-bb53-5e8f0905a67e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/af1e052b-1c7d-4d67-bb53-5e8f0905a67e?resizing_type=fit)

When the player runs up to this wall, it’s low enough that they’ll think they can jump over it and may feel frustrated when they can’t. Instead, we could replace the wall with a series of tall trellis panels that allow similar visibility as the wall while also communicating to the player that they can’t get through this way.

#### Make it Consistent

To make your level feel believable and support worldbuilding, keep the size of common features consistent throughout the environment.

However, you can introduce some contrast to draw the player’s attention or evoke an emotion. For example, making one door larger than all the others can hint at its importance.

If you have many designers working on a level or project, standardizing measurements prevents inconsistency between assets (which avoids time spent redoing work) and helps create a cohesive experience for the player.

As you design your level, create a player-sized cube or character mesh in each space as a reference of player scale. To add a player static mesh, go to the **Content > Characters > Mannequins > Meshes** folder in the **Content Browser**, and drag a `SKM_Manny_Simple` into the viewport.

Objects appear smaller in third-person view because the camera is further back, so you may need to increase the scale of your spaces compared to a first-person game. A good guideline is to multiply your scale by 1.5 (a 50% increase) when working with a third-person camera.

#### Modular Versus Complete Pieces

When blocking out your spaces, you can build walls, floors, and ceilings from one long mesh or keep duplicating meshes for a more modular design.

This choice depends on preference and the type of space; you could use modular pieces in hallways and boxy rooms, and use larger pieces for oddly-shaped rooms or natural spaces.

Blocking out in modular pieces has the following advantages:

* Many level designers find it faster and more predictable to duplicate modular pieces instead of resizing each piece.
* It can be easier to change one or two modular pieces in your blockout instead of one larger piece.
* You can build a wide variety of spaces while minimizing the number of assets that need to be created by artists.
* Standardized sizes keep everything aligned to the same grid and scale, which helps performance by reducing the number of unique materials and meshes needed.

Using modular design practices, you’ll create a palette of mesh shapes that you can use like building blocks to assemble your level’s spaces. However, these pieces are just a foundation; you can always add unique shapes as needed.

### Add Your First Object

Use the sample assets included with your project to start experimenting with scale and block out your level.

Assets are files you create or import into your project, and they’re stored in the Content Browser. Assets can be 3D meshes, 2D images, sound files, and more.

In Unreal Engine, you work with assets and actors:

* **Assets** are files you create or import into your project, and they’re stored in the Content Browser.
* **Actors** are any object that’s placed in a level.

Often, actors are **instances** of an asset, meaning an individual copy of that asset placed in the world.

To add your first static mesh to the level, follow these steps:

1. In the **Content Browser**’s asset tree, go to the **Content > LevelPrototyping > Meshes** folder.

   [![Image-of-static-mesh-assets-in-the-content-drawer](https://dev.epicgames.com/community/api/documentation/image/21a9bd99-96ca-4c0b-a1ea-bee6298d6cdd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/21a9bd99-96ca-4c0b-a1ea-bee6298d6cdd?resizing_type=fit)
2. Click `SM_Cube` and drag it into the viewport near the PlayerStart. This creates a **Static Mesh Actor** in your level that uses the `SM_Cube` asset.

![Gif-of-dragging-cube-asset-into-level](https://dev.epicgames.com/community/api/documentation/image/530b0e62-7350-4336-8bca-d2b9d9d69a95?resizing_type=fit)

The **Content Browser** asset and level-object instances of that asset have a parent-child relationship. Changes to the parent `SM_Cube` asset affect the mesh in your level, but any changes you make to individual `SM_Cube` object instances in your level won’t affect the `SM_Cube` asset in the **Content Browser**.

This block is 1m x 1m x 1m and has a grid material to help you see its dimensions at a glance. The dark lines on the material create a 1m grid, and the light lines on the floor material create a 0.1m grid. The light lines on vertical surfaces are 0.2m grids.

[![1-meter-cubes-and-floor-grid-lines-for-assessing-scale](https://dev.epicgames.com/community/api/documentation/image/736d36e6-7146-4e4d-bec5-45a6f2181aaa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/736d36e6-7146-4e4d-bec5-45a6f2181aaa?resizing_type=fit)

In Unreal Engine, a **material** is an asset made of 2D textures that changes how the surface of a mesh looks. Materials are what make a mesh look like metal, wood, or just a plain color.

To resize the 1m block into a piece of wall, follow these steps:

1. In the viewport, click the block mesh to select it.
2. In the Viewport Toolbar, click the **Scale** button (or press **R**). The Scale gizmo appears on the block.

   [![Image-of-the-scale-gizmo-on-a-block](https://dev.epicgames.com/community/api/documentation/image/5b7e1843-c4be-444e-9b62-e07bd427bc0d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5b7e1843-c4be-444e-9b62-e07bd427bc0d?resizing_type=fit)
3. Click and drag the gizmo’s handles to make the block thinner, longer, and taller. The thickness of your walls depends on what you are building. A house may have thinner walls, while a fortress has thicker walls. 10–30cm is a good starting point.

Using the Scale property to resize a cube.

When resizing the shape, look at the **Details** panel and notice how its **Scale** properties change. You can also change an object’s location, rotation, and size from the **Details** panel.

To make the shape larger or smaller in multiple dimensions at once, hover over the triangle between the red and blue handles until they are highlighted in yellow, then click and drag.

To scale all three dimensions at once, click and drag the white sphere in the middle of the gizmo.

  To adjust the position of your wall, follow these steps:

1. In the Viewport Toolbar, click the **Translate** button (or press **W**).

   [![Viewport-toolbar-option-for-translate-mode](https://dev.epicgames.com/community/api/documentation/image/c40e10a2-a671-4547-b2b5-2aadd12dc026?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c40e10a2-a671-4547-b2b5-2aadd12dc026?resizing_type=fit)

   [![Image-of-wall-with-scale-gizmo-selected](https://dev.epicgames.com/community/api/documentation/image/0efc5c0f-347b-4f20-85f8-f996e7085ec7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0efc5c0f-347b-4f20-85f8-f996e7085ec7?resizing_type=fit)
2. Click and drag the green or red handles to move the shape in either direction along the floor.

![Showing-a-wall-being-selected-and-moved](https://dev.epicgames.com/community/api/documentation/image/a015e4ef-6cd0-4923-ad91-c674259d3ce5?resizing_type=fit)

To move the shape in two directions at once, hover over the square between the green and red handles until they are highlighted in yellow, then click and drag the shape around the floor.

### Duplicate and Align Objects to Build a Room

You need a few more walls to make a room, so keep going!

To quickly make another wall piece, select your wall mesh, hold the **Alt** key, and use the Translate gizmo to move the mesh. This keeps the original in place and creates a duplicate.

![Using-the-alt-key-to-duplicate-a-wall](https://dev.epicgames.com/community/api/documentation/image/de68ab89-8703-46a2-869a-39e5801e9e97?resizing_type=fit)

Duplicate and move wall pieces around to build your first room. Ensure there’s enough space to add an obstacle in a later module of this tutorial.

Press **Ctrl** to select multiple pieces at once and then press and hold **Alt** while rotating or translating to duplicate the entire selection.

Using the Ctrl and Alt key to duplicate objects.

As you move objects around, notice that they snap along an invisible grid. The grid and grid-snapping tools help you place, align, and scale objects accurately in your level. The grid ensures that everything snaps together neatly and stays consistent in size and position.

![Moving-a-cube-as-it-snaps-to-grid-intesections](https://dev.epicgames.com/community/api/documentation/image/aad4f774-14a4-4903-afa2-b4a52444e8bd?resizing_type=fit)

Man-made spaces adhere to a grid more than natural spaces.

In the Viewport Toolbar, you can use the grid snapping menus to select a different grid size (or snap increment) for translation, rotation, and scale. By default, the grid size for moving objects is 10 units, or 10cm.

[![Image-of-the-selection-tool-in-the-toolbar](https://dev.epicgames.com/community/api/documentation/image/b886ee80-b0bb-41f6-b145-6fe0081de007?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b886ee80-b0bb-41f6-b145-6fe0081de007?resizing_type=fit)

Large snapping increments are great for laying out rooms and walls, and small grid sizes are useful for fine-tuning object placement. For example, change the rotation grid snap to 45° or 90° to make objects align at right angles.

For more information about all snapping options, see the **Snapping Tools & Snap Settings** section in [Viewport Toolbar](https://dev.epicgames.com/documentation/en-us/unreal-engine/viewport-toolbar).

Another way to ensure your objects are lined up is by using a 2D wireframe view. Near the right side of the Viewport Toolbar, click **Perspective** to open the camera options, and select **Top**.

[![Birds-eye-view-of-the-floorplan-walls](https://dev.epicgames.com/community/api/documentation/image/d24e5a7c-c172-43f4-b4c0-466b134b36a2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d24e5a7c-c172-43f4-b4c0-466b134b36a2?resizing_type=fit)

These orthographic-type views default to **Wireframe** view mode, which shows the edges and polygon structure of your level’s geometry. You can also see the grid in this mode. As you block out your level, switch to a **Top** or side view periodically to check the alignment of your meshes. When you’re done, switch back to **Perspective** mode.

Some objects, such as large lights, sky meshes, or trigger volumes, can get in the way when you’re trying to select objects in a 2D wireframe viewport. To hide these objects, use the **Show Flags** menu in the Viewport Toolbar to hide types of objects. Or, use the **Outliner** to hide individual objects.

### Set The Start Point

Now that you have the beginnings of a level, reposition the PlayerStart position to where the player should start from, and make sure they are facing the right direction!

To change the player’s starting location and direction, follow these steps:

1. Click the **PlayerStart** object. Use the **Translate** gizmo to move it to where you want the player to spawn into your first room.
2. Press **Q** on your keyboard to change to **Select** mode and remove the gizmo. The blue arrow on the **PlayerStart** object shows the direction the player faces when the game starts.

   [![Image-of-player-start-icon](https://dev.epicgames.com/community/api/documentation/image/fae55678-1b38-44c8-9221-b61d2d840a24?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fae55678-1b38-44c8-9221-b61d2d840a24?resizing_type=fit)
3. Use the Transform toolbar to switch to the **Rotation** gizmo and rotate it to control where the player faces when they start.

   ![](https://dev.epicgames.com/community/api/documentation/image/51c9131a-ec58-4e9b-89cb-78d987ee6f7d?resizing_type=fit)

### Add a Door

In later parts of this tutorial, you’ll learn to make a blueprint for a key that can be set to different colors, and each color unlocks a matching door. To set up your level for this functionality, add some doors.

To add and resize a `BP_DoorFrame` Blueprint, follow these steps:

1. In your blockout, make space for three different doors.

   [![Plan-view-of-a-room-with-3-doors](https://dev.epicgames.com/community/api/documentation/image/d6e27036-23c0-44df-8e14-bd34c9648025?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d6e27036-23c0-44df-8e14-bd34c9648025?resizing_type=fit)
2. In the **Content Browser**, go to **Content > LevelPrototyping > Interactable > Door**.

   [![Image-of-blueprint-doorframe-asset-in-content-drawer](https://dev.epicgames.com/community/api/documentation/image/abd9237a-d033-4537-b49b-583efd1b4b8c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/abd9237a-d033-4537-b49b-583efd1b4b8c?resizing_type=fit)
3. Drag `BP_DoorFrame` into your level. This object isn’t a plain static mesh like the `SM_Cube`; it’s a blueprint, which is a visual asset with extra features or behaviors scripted into it. In the viewport, you can see it’s surrounded by a trigger volume and has a **Door Size** widget. You’ll learn more about Blueprints in the next module in this tutorial.

   ![Gif-of-dragging-a-door-asset-from-the-content-drawer-into-the-level](https://dev.epicgames.com/community/api/documentation/image/e7a9f0c2-0da8-44fd-818f-72f28c8d3730?resizing_type=fit)
4. Click the **Door Size** widget. This forces the Translation gizmo to be active, but you can use it to resize the door just like you would use the Scale gizmo.

   ![Using-the-door-size-gizmo-to-resize-a-door](https://dev.epicgames.com/community/api/documentation/image/177db322-b9d5-48eb-8c46-a5c45661e85a?resizing_type=fit)
5. Click the door’s mesh and use the Translation gizmo to move the door into one of the gaps in your walls. You may need to adjust the walls or door width to make everything fit together.

   Fine adjustments in top-down wireframe view.
6. Repeat these steps to add two more doors to your room.

   [![Image-of-doors-being-placed-in-walls](https://dev.epicgames.com/community/api/documentation/image/094b2fa0-8ecc-4923-9472-c05e8e90c3fc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/094b2fa0-8ecc-4923-9472-c05e8e90c3fc?resizing_type=fit)

### Build A Hallway

Next, add some traversal space with a hallway that connects your first room with a second one.

There are a few ways we can design a hallway. First, what if we make it straight?

[![View-of-straight-hallway-leading-into-a-room](https://dev.epicgames.com/community/api/documentation/image/94f26472-3113-438a-9669-c4d2eec2b12f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/94f26472-3113-438a-9669-c4d2eec2b12f?resizing_type=fit)

This isn’t very exciting, but could be effective if we want the player to be pressured by ranged attacks as they go down this hallway, or if we want them to anticipate what they see at the end of the hallway. Here’s an example of a straight hallway made more interesting by obstacles the player has to duck under or climb over:

[![Image-of-hallway-with-fallen-column-as-an-obstruction](https://dev.epicgames.com/community/api/documentation/image/9787171f-ab28-42d0-967e-2e8889d97fc8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9787171f-ab28-42d0-967e-2e8889d97fc8?resizing_type=fit)

What about a hallway with a bend?

[![Image-of-hallway-with-a-90-degree-bend](https://dev.epicgames.com/community/api/documentation/image/4cd38050-3121-4b89-b18b-be0c770c52f0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4cd38050-3121-4b89-b18b-be0c770c52f0?resizing_type=fit)

Now there’s some occlusion and a reveal as the player turns the corner. Occlusion is when the player’s line of sight is partly or fully blocked. You can use occlusion to direct the player’s attention within a level. For example, directing attention toward pickups and level progression, or obscuring the visibility of an enemy to facilitate a jumpscare.

What if we add a window in the hallway and the next room?

[![Image-of-hallway-with-90-degree-bend-and-windows](https://dev.epicgames.com/community/api/documentation/image/7d8f8e3c-a7e6-4a7b-9aa1-2b5fcd7a3527?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7d8f8e3c-a7e6-4a7b-9aa1-2b5fcd7a3527?resizing_type=fit)

This makes traversing the hallway a bit more interesting. Showing the player a peek into their destination builds anticipation and shows the reward they’ll get by investing time in that path.

What if we add some verticality? This means adding height differences to your level, such as stairs, hills, platforms, and climbable areas.

Vertical elements can do the following for your gameplay:

* Add variety to your spaces and make traversal and exploration more interesting.
* Give players a tactical advantage (if up high) or disadvantage (if down low).
* Show the player where they are going next (for example, overlooking a vista).
* Control player access (for example, dropping down into a space unable to go back, or only being able to climb up into a space after finding a rope).

To add stairs to your blockout, drag an `SM_Ramp` (in **Content > LevelPrototyping > Meshes**) into your level and resize it. Ensure you test the scale as you go.

[![Image-of-level-with-a-ramp-and-scaled-elements](https://dev.epicgames.com/community/api/documentation/image/ad24b8e6-c013-496f-a54e-9158104e5089?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ad24b8e6-c013-496f-a54e-9158104e5089?resizing_type=fit)

This corridor is curved to add occlusion without being too boxy and is wider to accommodate two different paths, each offering the opportunity for sneaking and using cover. Adding choices like this makes the player feel they have some agency.

## Test Early and Often

Ensure you play your level and check how your metrics and scale are feeling before continuing to build.

Test the player’s sight lines to check that your occlusion is set up properly. A space may look great from the viewport, but playtesting could reveal that the player can see something they shouldn’t, like the other team’s spawn point.

As your level grows and you want to preview one section without starting back at your player’s spawn point, right-click a spot in the viewport and select Play From Here.

[![Accessing-the-right-click-menu-to-play-from-here](https://dev.epicgames.com/community/api/documentation/image/4a6f50a9-da88-4b10-8d5b-73106225da48?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4a6f50a9-da88-4b10-8d5b-73106225da48?resizing_type=fit)

## Add Blocking Volumes

As you playtest your design, you may discover places where the player can jump past geometry and leave or skip the play area. Blocking volumes are level objects that act as an invisible wall to close off unintended areas and keep the player in the level.

However, never use blocking volumes in places where the player expects to move freely, like an open doorway or hallway.

To add a blocking volume to your level, follow these steps:

1. In the main toolbar, click the **Create**button. In this menu, you can create new actors.
2. In the **Create** menu, scroll to **Volumes**, search for `Blocking`, and select **Blocking Volume**.

   [![Blocking-volumes-menu-option](https://dev.epicgames.com/community/api/documentation/image/e8902cef-6555-41ba-a960-1806b47fcb32?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e8902cef-6555-41ba-a960-1806b47fcb32?resizing_type=fit)
3. The editor adds a `BlockingVolume` in the middle of your main viewport.

Once you’re done working on your blocking volumes, you can hide them from view to reduce clutter in your level.

In the example hallway here, blocking volumes prevent the player from jumping out the window or jumping on the roof after climbing up the pillar:

[![Outlines-of-blocking-volumes](https://dev.epicgames.com/community/api/documentation/image/d43f8461-252e-43d9-82bc-c582a406199b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d43f8461-252e-43d9-82bc-c582a406199b?resizing_type=fit)

Blocking volumes can also even out complex collision shapes or detailed geometry, so the player doesn’t get stuck on or bump awkwardly into small edges or holes.

## Organize Objects in the Outliner

As your level grows, so does the list of objects in the Outliner panel. To make the Outliner cleaner and more navigable, organize your objects into folders. You can create folders to group objects by function or location.

To create a Geometry folder with all of your blockout meshes, follow these steps:

1. In the **Outliner** panel, select all of your blockout geometry. (Press **Ctrl** or **Shift** to add to your selection.)

   [![Image-of-outliner-menu-with-all-geometry-selected](https://dev.epicgames.com/community/api/documentation/image/0aba3a14-2c70-41dd-84d6-c362045e3bb0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0aba3a14-2c70-41dd-84d6-c362045e3bb0?resizing_type=fit)
2. Near the top-right corner of the Outliner, click the **Create folder** button.
3. Enter a name for your folder (for example, `Geometry`).

   [![Create-a-new-folder-for-your-geometry](https://dev.epicgames.com/community/api/documentation/image/d6c63292-a0e3-418b-88bf-5a4492633c8e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d6c63292-a0e3-418b-88bf-5a4492633c8e?resizing_type=fit)

As your level grows, you could further organize your project by creating folders of blockout geometry for each region or room in the level.

* You can repeat these steps for a subset of meshes to sort them into a subfolder of the **Geometry** folder.
* Use the visibility toggles in the **Outliner** to hide all objects in a folder

## Add Text Labels

To label a space, obstacle, or gameplay element to come, add a Text Render Actor to your blockout. This text can act as a placeholder or give playtesters context about what’s planned for that space.

To use a Text Render Actor to display a text string in your level, follow these steps:

1. In the main toolbar, click the **Create**button.
2. In the **Create** menu, search for `Text Render`, and select **Text Render Actor**. 
   The editor adds a **TextRenderActor** in the middle of your main viewport.

   [![Text-render-actor-menu-option](https://dev.epicgames.com/community/api/documentation/image/4819f20b-80f7-43c1-ace5-eda134e9d79d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4819f20b-80f7-43c1-ace5-eda134e9d79d?resizing_type=fit)
3. With the actor selected, in its **Details** panel, use the **Text** property to enter the text you want to display in the level.

   [![Text-render-details-menu](https://dev.epicgames.com/community/api/documentation/image/eb45dd9a-927d-403a-a87f-afa07cefa2bf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/eb45dd9a-927d-403a-a87f-afa07cefa2bf?resizing_type=fit)
4. Use **World Size** to make the text larger or smaller, and use **Text Render Color** to change the text color.

   [![World-size-and-text-render-menu-options](https://dev.epicgames.com/community/api/documentation/image/279af0ca-97da-4651-8442-9b89dc9a5ae0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/279af0ca-97da-4651-8442-9b89dc9a5ae0?resizing_type=fit)
5. Rotate and move the text into position. Text Render Actors look best when placed on a wall, floor, or obstacle.

   [![Text-render-actor-placed-on-wall-behind-a-bar](https://dev.epicgames.com/community/api/documentation/image/9e8eea3f-f5bb-4280-bbaf-54048a243ea5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9e8eea3f-f5bb-4280-bbaf-54048a243ea5?resizing_type=fit)
6. Optional: To make a Text Render Actor invisible in-game, in the **Details** panel, in the **Rendering** section, enable **Actor Hidden in Game**.

## Enhance Your Design

You’ve gotten started with your first room and some hallways; now keep building!

To complete the rest of this tutorial, we recommend having the following elements in your blockout:

* Areas that allow the player to collect three different keys and unlock each key’s matching door.
* An area to place a maze of traps that can be disabled with a floor switch.
* An area to traverse a series of moving platforms.
* An area to fight NPC enemies.

Beyond that, use your imagination, experiment, and iterate! That’s the beauty of grayboxing.

As you build, there are a few more design principles to consider:

### Obstacles and Occlusion

Don’t forget to introduce some functional obstacles. For example:

* An object blocking an obvious pathway, forcing the player to find an interesting detour.
* Pillars that block line of sight and add interest.
* Objects that create cover.
* Geometry that teaches the player part of their moveset (such as jumping, crouching, crawling).

Here’s an example of a blocked-out room with some height changes and occlusion:

[![Image-of-a-blocked-out-room-with-ramps-and-columns](https://dev.epicgames.com/community/api/documentation/image/95cc4797-97c1-4a2a-b5c7-2d0db9922ac8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/95cc4797-97c1-4a2a-b5c7-2d0db9922ac8?resizing_type=fit)

### Level Flow and Guiding Lines

Think about the rhythm and pace of the player’s path through your level. Are they naturally guided to the next area? Are there moments of tension and calm? Does the player feel like they have some choice?

Using guiding lines and points of contrast directs the player to areas of interest without them knowing. It makes the world feel intuitive as the player is naturally drawn along or towards these elements.

For example:

* Cables, pipes, fences, railings, and pathways lead the player’s eye along these edges.
* Light sources or contrasting visuals get the player’s attention.
* The view of a landmark or a doorway that frames the next area draws the player in that direction.

When the player enters this room, they are drawn along the wall towards the window, which leads the player towards the exit.

[![View-from-the-end-of-a-hallway-towards-a-room](https://dev.epicgames.com/community/api/documentation/image/3bf5d57b-4b09-4033-99e2-0193042f6a73?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3bf5d57b-4b09-4033-99e2-0193042f6a73?resizing_type=fit)

As you design your spaces, think about how they’ll be traversed. For example, this tutorial creates a hub-and-spoke-style space where the player has to return to the first room after completing certain objectives. Here, the hallways shouldn’t be too long because the player has to pass through them multiple times.

### Shape Language

You can use different shapes to communicate emotion or function to the player, even in the blockout stage of development.

* Rounded corners and curves suggest nature and safety, so these shapes work well in a rest area or healing location.
* Square or boxy areas feel man-made, stable, and orderly.
* Triangular, jagged, or spikey areas feel dangerous. A space like this could silently warn the player that there are traps or enemies nearby.
* A tall or expansive space can evoke power, while claustrophobic and cluttered spaces create tension and discomfort.

For example, a future section in this tutorial designs a trap that damages the player if they fall on it. Players associate spikes with danger, so this design utilizes this shape language to tell the player they should avoid this obstacle:

[![Image-of-a-platform-covered-in-spike-cones](https://dev.epicgames.com/community/api/documentation/image/607d3e17-98d6-4cf4-a15c-e2b5685d4899?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/607d3e17-98d6-4cf4-a15c-e2b5685d4899?resizing_type=fit)

## Blockout Example

Here’s the space that the rest of this tutorial uses. You can match it, or design something entirely your own.

All rooms have a number so the steps in this tutorial can reference a specific room.

[![Image-of-the-full-level-floorplan](https://dev.epicgames.com/community/api/documentation/image/18c1b63d-6317-44b7-875f-5a3638d35f4c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/18c1b63d-6317-44b7-875f-5a3638d35f4c?resizing_type=fit)

The rooms are built to demonstrate increasing complexity:

* Start Room is where the player starts. We also added a small spawn area that leads into the Start Room.
* Room 2 is plain with a basic L-bend in the hallway.
* Room 1 increases the complexity with a curved hallway featuring different paths, occlusion, and height changes.
* Room 3 goes above-and-beyond to demonstrate the full potential of what you could create with the basic shapes included with the first-person template. It adds a level of detail to the floor and walls that influences the game’s art style and helps the artists imagine what can go in that space.

The blockout style in Room 1 and 2 is usually the sort of detail you’re aiming for when level designing.

Hallway 3 and Room 3 also use the meshes from `BP_DoorFrame` that are located in **Content > LevelPrototyping > Interactable > Door > Assets > Meshes.**

[![Image-focusing-on-the-start-room](https://dev.epicgames.com/community/api/documentation/image/1a0ac850-a1e7-4299-8635-23cc37395cba?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1a0ac850-a1e7-4299-8635-23cc37395cba?resizing_type=fit)

[![Image-focusing-on-hallway-1](https://dev.epicgames.com/community/api/documentation/image/47f06dec-bc1e-4dad-87dc-0baf1dd5de87?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/47f06dec-bc1e-4dad-87dc-0baf1dd5de87?resizing_type=fit)

[![Image-focusing-on-hallway-3](https://dev.epicgames.com/community/api/documentation/image/23374388-8320-4759-8849-5d631a55026d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/23374388-8320-4759-8849-5d631a55026d?resizing_type=fit)

### Try the Sample Level

If you’d like to use the sample blockout we created for this tutorial, use the snippet below. This is a text version of all the blockout meshes used to create this example. When you copy and paste this text into the level editor, Unreal Engine turns it into level objects.

Command Line

Start Room

```
Begin Map
   Begin Level
      Begin Actor Class=/Game/LevelPrototyping/Interactable/Door/BP_DoorFrame.BP_DoorFrame_C Name=BP_DoorFrame_C_4 Archetype="/Game/LevelPrototyping/Interactable/Door/BP_DoorFrame.BP_DoorFrame_C'/Game/LevelPrototyping/Interactable/Door/BP_DoorFrame.Default__BP_DoorFrame_C'" ExportPath="/Game/LevelPrototyping/Interactable/Door/BP_DoorFrame.BP_DoorFrame_C'/Temp/Untitled_1.Untitled_1:PersistentLevel.BP_DoorFrame_C_4'"
         Begin Object Class=/Script/Engine.SceneComponent Name="DefaultSceneRoot" Archetype="/Script/Engine.SceneComponent'/Game/LevelPrototyping/Interactable/Door/BP_DoorFrame.BP_DoorFrame_C:DefaultSceneRoot_GEN_VARIABLE'" ExportPath="/Script/Engine.SceneComponent'/Temp/Untitled_1.Untitled_1:PersistentLevel.BP_DoorFrame_C_4.DefaultSceneRoot'"
         End Object
         Begin Object Class=/Script/Engine.BoxComponent Name="Box" Archetype="/Script/Engine.BoxComponent'/Game/LevelPrototyping/Interactable/Door/BP_DoorFrame.BP_DoorFrame_C:Box_GEN_VARIABLE'" ExportPath="/Script/Engine.BoxComponent'/Temp/Untitled_1.Untitled_1:PersistentLevel.BP_DoorFrame_C_4.Box'"
            Begin Object Class=/Script/Engine.BodySetup Name="BodySetup_0" Archetype="/Script/Engine.BodySetup'/Game/LevelPrototyping/Interactable/Door/BP_DoorFrame.BP_DoorFrame_C:Box_GEN_VARIABLE.BodySetup_0'" ExportPath="/Script/Engine.BodySetup'/Temp/Untitled_1.Untitled_1:PersistentLevel.BP_DoorFrame_C_4.Box.BodySetup_0'"
            End Object
         End Object
         Begin Object Class=/Script/Engine.TimelineComponent Name="Door Control" ExportPath="/Script/Engine.TimelineComponent'/Temp/Untitled_1.Untitled_1:PersistentLevel.BP_DoorFrame_C_4.Door Control'"
```

Expand code  Copy full snippet(3318 lines long)

Command Line

Hallway 1, Room 1

```
Begin Map
   Begin Level
      Begin Actor Class=/Script/Engine.ExponentialHeightFog Name=ExponentialHeightFog_0 Archetype="/Script/Engine.ExponentialHeightFog'/Script/Engine.Default__ExponentialHeightFog'" ExportPath="/Script/Engine.ExponentialHeightFog'/Temp/Untitled_1.Untitled_1:PersistentLevel.ExponentialHeightFog_0'"
         Begin Object Class=/Script/Engine.BillboardComponent Name="Sprite" Archetype="/Script/Engine.BillboardComponent'/Script/Engine.Default__ExponentialHeightFog:Sprite'" ExportPath="/Script/Engine.BillboardComponent'/Temp/Untitled_1.Untitled_1:PersistentLevel.ExponentialHeightFog_0.Sprite'"
         End Object
         Begin Object Class=/Script/Engine.ExponentialHeightFogComponent Name="HeightFogComponent0" Archetype="/Script/Engine.ExponentialHeightFogComponent'/Script/Engine.Default__ExponentialHeightFog:HeightFogComponent0'" ExportPath="/Script/Engine.ExponentialHeightFogComponent'/Temp/Untitled_1.Untitled_1:PersistentLevel.ExponentialHeightFog_0.HeightFogComponent0'"
         End Object
         Begin Object Name="Sprite" ExportPath="/Script/Engine.BillboardComponent'/Temp/Untitled_1.Untitled_1:PersistentLevel.ExponentialHeightFog_0.Sprite'"
            AttachParent="HeightFogComponent0"
         End Object
```

Expand code  Copy full snippet(3206 lines long)

C++

Hallway 2, Room 2

```
Begin Map
   Begin Level
      Begin Actor Class=/Script/Engine.StaticMeshActor Name=Floor_90 Archetype="/Script/Engine.StaticMeshActor'/Script/Engine.Default__StaticMeshActor'" ExportPath="/Script/Engine.StaticMeshActor'/Temp/Untitled_1.Untitled_1:PersistentLevel.Floor_90'"
         Begin Object Class=/Script/Engine.StaticMeshComponent Name="StaticMeshComponent0" Archetype="/Script/Engine.StaticMeshComponent'/Script/Engine.Default__StaticMeshActor:StaticMeshComponent0'" ExportPath="/Script/Engine.StaticMeshComponent'/Temp/Untitled_1.Untitled_1:PersistentLevel.Floor_90.StaticMeshComponent0'"
         End Object
         Begin Object Name="StaticMeshComponent0" ExportPath="/Script/Engine.StaticMeshComponent'/Temp/Untitled_1.Untitled_1:PersistentLevel.Floor_90.StaticMeshComponent0'"
            StaticMesh="/Script/Engine.StaticMesh'/Engine/MapTemplates/SM_Template_Map_Floor.SM_Template_Map_Floor'"
            bUseDefaultCollision=False
            StaticMeshDerivedDataKey="STATICMESH_34081786561B425A9523C94540EA599D_359a029847e84730ba516769d0f19427Simplygon_5_5_2156_18f808c3cf724e5a994f57de5c83cc4b_680318F3495BDBDEBE4C11B39CD497CE000000000100000001000000000000000000803F0000803F00000000000000000000344203030300000000"
            MaterialStreamingRelativeBoxes(0)=4294901760
```

Expand code  Copy full snippet(2188 lines long)

C++

Hallway 3, Room 3

```
Begin Map
   Begin Level
      Begin Actor Class=/Script/Engine.StaticMeshActor Name=StaticMeshActor_911 Archetype="/Script/Engine.StaticMeshActor'/Script/Engine.Default__StaticMeshActor'" ExportPath="/Script/Engine.StaticMeshActor'/Game/AdventureGame/deleteme.deleteme:PersistentLevel.StaticMeshActor_911'"
         Begin Object Class=/Script/Engine.StaticMeshComponent Name="StaticMeshComponent0" Archetype="/Script/Engine.StaticMeshComponent'/Script/Engine.Default__StaticMeshActor:StaticMeshComponent0'" ExportPath="/Script/Engine.StaticMeshComponent'/Game/AdventureGame/deleteme.deleteme:PersistentLevel.StaticMeshActor_911.StaticMeshComponent0'"
         End Object
         Begin Object Name="StaticMeshComponent0" ExportPath="/Script/Engine.StaticMeshComponent'/Game/AdventureGame/deleteme.deleteme:PersistentLevel.StaticMeshActor_911.StaticMeshComponent0'"
            StaticMesh="/Script/Engine.StaticMesh'/Game/LevelPrototyping/Meshes/SM_Cylinder.SM_Cylinder'"
            StaticMeshImportVersion=1
            StaticMeshDerivedDataKey="STATICMESH_FD1BFC73B5510AD60DFC65F62C1E933E_228332BAE0224DD294E232B87D83948FQuadricMeshReduction_V2$2e1_6D3AF6A2$2d5FD0$2d469B$2dB0D8$2dB6D9979EE5D2_CONSTRAINED0_100100000000000000000000000100000000000080FFFFFFFFFFFFFFFFFFFFFFFF000000000000803F00000000000000803F0000803F00000000000000003D19FC1626C9B2485E57DB4B8EC731318B8215AE8D46FAD400000000010000000100000000000000010000000100000000000000000000000100000001000000400000000000000001000000000000000000F03F000000000000F03F000000000000F03F0000803F00000000050000004E6F6E65000C00000030000000803FFFFFFFFF0000803FFFFFFFFF0000000000000041000000000000A0420303030000000000000000_RT00_0"
            RelativeLocation=(X=-2790.000000,Y=-1610.000000,Z=-0.499892)
```

Expand code  Copy full snippet(5513 lines long)

To copy this blockout example into an empty level, follow these steps:

1. In a new, **Basic**-type level, delete the **Floor** and **PlayerStart** meshes so you have a level that only contains lighting level objects.
2. Click **Copy Full Snippet**.
3. In Unreal Editor, ensure the viewport or **Outliner** is the active panel (click anywhere in the viewport or Outliner and press **Esc**), and then press **Ctrl + V**.
4. Repeat for all rooms and hallways.

In the Outliner, you’ll see all meshes organized into folders named after each room and hallway.

[![Folder-structure-to-keep-room-files-organized](https://dev.epicgames.com/community/api/documentation/image/0e04e353-8d29-406e-a376-a54feea12a1e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0e04e353-8d29-406e-a376-a54feea12a1e?resizing_type=fit)

The sample level uses naming conventions for many objects in the Outliner. Level prototyping meshes are renamed depending on their use:

* Walls are named `SM_Wall`
* Columns are named `SM_Column` and `SM_QuarterColumn`

If you’d like to use these naming conventions and rename your objects, select a group of meshes in the **Outliner**, right-click your selection, and go to **Edit > Rename Selected Actors**. For more information about working in the Outliner, see the [Outliner](https://dev.epicgames.com/documentation/en-us/unreal-engine/outliner-in-unreal-engine) documentation.

## Next Up

Once you’ve blocked out your level, it’s time to start adding gameplay elements. In the next section, you’ll get an introduction to Blueprint Visual Scripting in Unreal Engine and learn how to build gameplay logic into a blueprint level object.

The next document in this tutorial serries involves the use of Unreal Engine's visual scripting language **Blueprints**. If you are new to Blueprints, and would like a introduction to using Blueprints to program game logic, see the [Blueprints Foundations](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprint-foundations) documentation.

If you are already comfortable with Blueprints, you can proceed to the **Create a Key** tutorial:

* [![Create a Key](https://dev.epicgames.com/community/api/documentation/image/03094522-adf5-4121-863e-16ba0071b20e?resizing_type=fit&width=640&height=640)

  Create a Key

  Using blueprints, learn how to create a key that players can pick up.](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-02-create-a-key-in-unreal-engine)

* [geometry](https://dev.epicgames.com/community/search?query=geometry)
* [blueprint](https://dev.epicgames.com/community/search?query=blueprint)
* [level design](https://dev.epicgames.com/community/search?query=level%20design)
* [beginner](https://dev.epicgames.com/community/search?query=beginner)
* [graybox](https://dev.epicgames.com/community/search?query=graybox)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Before You Begin](/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine?application_version=5.7#beforeyoubegin)
* [Sketch Your Ideas](/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine?application_version=5.7#sketchyourideas)
* [Create Your Project](/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine?application_version=5.7#createyourproject)
* [Start a New Level](/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine?application_version=5.7#startanewlevel)
* [Explore the Outliner and Details Panels](/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine?application_version=5.7#exploretheoutlineranddetailspanels)
* [Preview Gameplay in the Viewport](/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine?application_version=5.7#previewgameplayintheviewport)
* [Change the Startup Level](/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine?application_version=5.7#changethestartuplevel)
* [Block Out Your Map](/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine?application_version=5.7#blockoutyourmap)
* [Determine Your Scale](/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine?application_version=5.7#determineyourscale)
* [Make it Feel Natural](/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine?application_version=5.7#makeitfeelnatural)
* [Make it Easily Understood](/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine?application_version=5.7#makeiteasilyunderstood)
* [Make it Consistent](/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine?application_version=5.7#makeitconsistent)
* [Modular Versus Complete Pieces](/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine?application_version=5.7#modularversuscompletepieces)
* [Add Your First Object](/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine?application_version=5.7#addyourfirstobject)
* [Duplicate and Align Objects to Build a Room](/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine?application_version=5.7#duplicateandalignobjectstobuildaroom)
* [Set The Start Point](/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine?application_version=5.7#setthestartpoint)
* [Add a Door](/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine?application_version=5.7#addadoor)
* [Build A Hallway](/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine?application_version=5.7#buildahallway)
* [Test Early and Often](/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine?application_version=5.7#testearlyandoften)
* [Add Blocking Volumes](/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine?application_version=5.7#addblockingvolumes)
* [Organize Objects in the Outliner](/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine?application_version=5.7#organizeobjectsintheoutliner)
* [Add Text Labels](/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine?application_version=5.7#addtextlabels)
* [Enhance Your Design](/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine?application_version=5.7#enhanceyourdesign)
* [Obstacles and Occlusion](/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine?application_version=5.7#obstaclesandocclusion)
* [Level Flow and Guiding Lines](/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine?application_version=5.7#levelflowandguidinglines)
* [Shape Language](/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine?application_version=5.7#shapelanguage)
* [Blockout Example](/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine?application_version=5.7#blockoutexample)
* [Try the Sample Level](/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine?application_version=5.7#trythesamplelevel)
* [Next Up](/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine?application_version=5.7#nextup)

Related documents

[Code a First-Person Adventure Game

![Code a First-Person Adventure Game](https://dev.epicgames.com/community/api/documentation/image/ffc1a8f8-e7e5-42c0-b4ed-32ce6d3adbbc?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/code-a-firstperson-adventure-game-in-unreal-engine)

[Create a Key

![Create a Key](https://dev.epicgames.com/community/api/documentation/image/03094522-adf5-4121-863e-16ba0071b20e?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/designer-02-create-a-key-in-unreal-engine)

[Blueprint Foundations

![Blueprint Foundations](https://dev.epicgames.com/community/api/documentation/image/d5519c66-d202-42af-bd24-b32ac0bbe537?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/blueprint-foundations)
