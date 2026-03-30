<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/stack-o-bot-sample-game-in-unreal-engine?application_version=5.7 -->

# Stack O Bot Sample Game

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
5. [Samples and Tutorials](/documentation/en-us/unreal-engine/samples-and-tutorials-for-unreal-engine "Samples and Tutorials")
6. [Sample Game Projects](/documentation/en-us/unreal-engine/sample-game-projects-for-unreal-engine "Sample Game Projects")
7. Stack O Bot Sample Game

# Stack O Bot Sample Game

A breakdown of the Stack O Bot sample game and what features are used to build it.

![Stack O Bot Sample Game](https://dev.epicgames.com/community/api/documentation/image/13f21f41-1891-44fa-a097-4fd443f979fb?resizing_type=fill&width=1920&height=335)

 On this page

**Stack O Bot** is a sample game project made as a learning resource for exploring game development with Unreal Engine. It demonstrates various engine features, including **Procedural Content Generation (PCG)**, **Blueprints**, and **level instances**. The sample project includes in-game developer commentary that discusses design choices and implementation, as well as commented Blueprints and materials.

In Stack O Bot, the player controls a robot character from a third-person perspective and must complete a series of platforming challenges and physics-based puzzles. It supports a wide range of devices, from mobile phones to high-end PCs, and can be controlled using keyboard and mouse, controller, and touchscreen inputs.

This page explains how to open the Stack O Bot sample project, provides an overview of the major features of the project, and links to related documentation for further learning.

## Open The Stack O Bot Project

The Stack O Bot sample described on this page is built using Unreal Engine 5.6. To try the older Stack O Bot sample, download the project for engine versions preceding 5.6.

To open the Stack O Bot sample project, follow these steps:

1. From Fab, go to the [Stack O Bot](https://www.google.com/url?q=https://www.fab.com/listings/b4dfff49-0e7d-4c4b-a6c5-8a0315831c9c&sa=D&source=docs&ust=1754928300614820&usg=AOvVaw35YA7pgZS5sx8t8KVs9sEp) sample, and click **Add to My Library**.

   1. Alternatively, you can search for the sample project from the [Fab plugin](https://dev.epicgames.com/documentation/en-us/unreal-engine/fab-window-in-unreal-engine?application_version=5.3) for Unreal Engine.
2. Go to **Stack O Bot** and click **Create Project**.
3. In the **Epic Games Launcher**, go to **Unreal Engine** > **Library** > **Fab Library**.
4. Enter a name and location for your project.
5. Select **5.6** as the engine version.
6. Click **Create**. The project will open.

To learn more about accessing sample content and the Fab plugin for Unreal Engine, see [Samples and Tutorials](https://dev.epicgames.com/documentation/en-us/unreal-engine/samples-and-tutorials-for-unreal-engine).

### Recommended System Specifications

Stack O Bot is designed to support a wide range of devices, including mobile phones and PC. The content scales across detail levels and is fully mobile-compatible.

The following system specifications are recommended for a PC:

* Windows 10 64-bit version 1909 revision .1350 or higher, or versions 2004 and 20H2 revision .789 or higher

  + Windows 11 is compatible with Unreal Engine 5 and fits in the recommended specs.
* Quad-core Intel or AMD, 2.5 GHz or faster
* 32 GB of system RAM
* 8 GB of VRAM
* DirectX 11 or 12 compatible graphics card

## Navigating The Stack O Bot Project

After you open the Stack O Bot project, the **Lvl\_Empty** map opens by default in the [level editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/level-editor-in-unreal-engine).  The map provides some on-screen information for using this sample project.

Most of the contents of the sample project are located in the `/Content/StackOBot/` folder. The main game map, **Lvl\_StackOBot**, is located in the `/Content/StackOBot/Maps` folder.

To play the game, click the **play** icon in the **Main Toolbar**.

The game starts with a main menu, which is contained in the **Lvl\_MainMenu** map. Click **PLAY** to go to the main game map, **Lvl\_StackOBot**.

[![The Stack O Bot main menu](https://dev.epicgames.com/community/api/documentation/image/3e71170a-6483-48d0-a59a-1252d94e3423?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3e71170a-6483-48d0-a59a-1252d94e3423?resizing_type=fit)

The main game map includes bubble icons that trigger developer commentary when the player gets close. This commentary explains some of the implementation details and design decisions the developers made when making Stack O Bot.

[![A bubble icon in Stack O Bot](https://dev.epicgames.com/community/api/documentation/image/c66a5439-0631-41ec-a9d7-aea8114a3278?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c66a5439-0631-41ec-a9d7-aea8114a3278?resizing_type=fit)

The content of the developer commentary bubbles is located in the `/Content/DevCom` folder.

### Stack O Bot In-Game Controls

To play Stack O Bot, the player can use a keyboard and mouse, controller, or touchscreen controls.

| Action | Keyboard and Mouse | Controller | Touch (see image below) |
| --- | --- | --- | --- |
| Move | W, A, S, D | Left thumbstick | 1 |
| Look | Mouse | Right thumbstick | 2 |
| Jump | Space (press) | Bottom face button (press) | 3 (press) |
| Jetpack | Space (hold) | Bottom face button (hold) | 3 (hold) |
| Grab | E | Right trigger | 4 |
| Pause | Escape or Left Shift | Start button | 5 |

[![Touch controls for Stack O Bot](https://dev.epicgames.com/community/api/documentation/image/813d05cf-0078-4644-a030-bdc86cececdb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/813d05cf-0078-4644-a030-bdc86cececdb?resizing_type=fit)

Touch controls for Stack O Bot

## Stack O Bot Features

This section describes the features used in the Stack O Bot sample project, and the locations of related assets in the project folder.

### Level Introduction

Stack O Bot starts with a level introduction, built as a level sequence using [Sequencer](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview). In the level sequence, three cinematic cameras and a camera cut track are used to move around the level and show various elements of the game map.

The level sequence (**SQ\_Lvl1\_fly**) is located in the `/Content/StackOBot/Maps` folder.

### Customizable Third-Person Character

The Stack O Bot project includes a third-person character that moves, jumps, and can interact with non-player characters (NPCs) and objects. The Blueprint for the character, **BP\_Bot**, combines an [animation graph](https://dev.epicgames.com/documentation/en-us/unreal-engine/graphing-in-animation-blueprints-in-unreal-engine), a [control rig](https://dev.epicgames.com/documentation/en-us/unreal-engine/control-rig-in-unreal-engine), and customizable [materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-materials).

The animation graph is used for animating the character in various states, such as standing, running, or jumping. The control rig is used for contextual animations, such as positioning the character's feet on different surfaces, and for guiding the hand to the button position when pressing buttons. The customizable materials include parameters to change color combinations and facial expressions for the character.

The **BP\_Bot** Blueprint is located in the `/Content/StackOBot/Blueprints/Character` folder, and the character animations and materials are located in the `/Content/StackOBot/Characters/Bot` folder.

### Procedural Content Generation (PCG)

The map in Stack O Bot is created using [Procedural Content Generation (PCG)](https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-content-generation-overview). PCG is used to make many of the assets, including the floating islands, the foliage, the platforms, the hexagonal domes, the fences, and the coin spawners.

The platforms are created by setting a size, using existing tile pieces, and a set of rules to keep the platforms visually consistent. Domes are placed throughout the map, but you can set a level entrance and exit that is left clear of domes.

The fences are created using a PCG system that samples a spline, **PCG\_BP\_FenceSpline**, and applies rules to generate the different parts of the fence, like posts and end caps. The map includes coin spawners, which also use PCG to spawn coins along a spline.

The PCG content is located in the `/Content/StackOBot/Blueprints/PCG` folder.

### Smart UV-Less Materials

The Stack O Bot project uses smart UV-less materials to apply high-quality textures to every  mesh in the map with a concrete, metal, or painted surface, such as the floating platforms, the metal cylinders, and the metal parts of the bio dome structure. Instead of creating [UV channels](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-uv-channels-with-static-meshes-in-unreal-engine) for each section of a mesh, the team added [vertex color](https://dev.epicgames.com/documentation/en-us/unreal-engine/paint-vertex-colors-tool-in-unreal-engine) information to each mesh using [modeling tools](https://dev.epicgames.com/documentation/en-us/unreal-engine/modeling-tools-in-unreal-engine). The smart materials then use the vertex colors to position the texture on each mesh.

### HLOD Generation

The map in Stack O Bot is large with many assets to render, so the project uses the [Hierarchical Level of Detail (HLOD)](https://dev.epicgames.com/documentation/en-us/unreal-engine/hierarchical-level-of-detail-in-unreal-engine) system in Unreal Engine to improve performance when playing the game.

### StateTree NPC Behavior

Stack O Bot includes NPCs that can interact with the player character. The NPCs walk around parts of the map, chase the player if they are nearby, bump into the player to knock them back, and can be destroyed when the player character jumps on their heads. The NPC behavior is controlled using a [StateTree](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-state-tree-in-unreal-engine), which defines the different states that each NPC can be in (such as idle, walking, or dead), and the actions that the NPC should perform in each state.

The StateTree for the NPCs is located in the `/Content/StackOBot/AI/STree_Bug` folder.

### Modular Level Instances

Stack O Bot uses [level instances](https://dev.epicgames.com/documentation/en-us/unreal-engine/level-instancing-in-unreal-engine) to create re-usable modular level segments. For example, there are level instances with variants of the floating islands that you can use to build game maps without having to create unique content for each new area.

Each level instance can be played as a standalone map, or added to a [World Partition](https://dev.epicgames.com/documentation/en-us/unreal-engine/world-partition-in-unreal-engine) map. When placed in another map, each instance has a transform so it can be rotated and positioned.

You can add objects to an instance that are tagged **Main World Only** in the object's details panel. These objects only show up if the instance is played as a standalone map, and not if you use the map as a level instance in a World Partition map. Check the **Main World Only** checkbox on lighting, player starts, and other objects that you don’t want to use in the World Partition map, but do want to use when testing and debugging the level instance as a standalone map.

Level instances are located in the `/Content/StackOBot/Maps/LevelInstances` folder. Level instances that use objects tagged as Main World Only have a `Main World` folder that includes these objects.

### Physics-based Interactions

Stack O Bot uses Unreal Engine's [physics](https://dev.epicgames.com/documentation/en-us/unreal-engine/physics-in-unreal-engine) systems to implement physics objects, interactions, and destruction.

For physics objects like the stackable crates, the player character grabs them using a physics handle. Objects like the bounce pads and fans use physics commands to throw the player in the air. Floating platforms and bridges use a physics constraints setup. Destructible objects, like the roofs and respawning platforms, use a pre-fractured [geometry collection](https://dev.epicgames.com/documentation/en-us/unreal-engine/geometry-collections-user-guide) that the Chaos master field triggers.

The physics objects are located in the `/Content/StackOBot/Blueprints/PhysicsElements` folder.

### Dynamic Camera

Stack O Bot uses a custom [player camera manager](https://dev.epicgames.com/documentation/en-us/unreal-engine/cameras-in-unreal-engine#playercameramanager) (**BP\_CamManager**) to create three distinct camera types:

* A third-person camera that follows behind the player
* A locked third-person perspective designed to show off various elements of the game map from a cinematic angle
* A side-scrolling implementation designed to recreate the style of classic 2D platform games

The third-person camera that follows the player is used throughout most of the main map. When standing on certain moving platforms, the camera switches to the locked third-person perspective. There is one part of the map where the camera switches to the side-scrolling perspective.

The camera manager transitions between all 3 camera types using a Blueprint actor (**BP\_GameCamVolume**), logic in the camera manager, and an interface (**BPI\_CamManager**) to communicate between the manager and the Blueprint actor.

The camera manager and game camera volume Blueprint are located in the `/Content/StackOBot/Blueprints/Camera` folder.

### Gameplay Interactions

Stack O Bot includes an interaction handler [component](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-terminology#component:~:text=of%20that%20class.-,Component,-A%20Component%20is) that is added to any actor that the player character can interact with. This applies to objects like buttons and pressure pads.

Objects that can be grabbed, like the crates, have the **GRAB** actor tab that is checked by the **Grab\_Check** function in **BP\_Bot**. Grabbed objects are updated by the **Grab\_Update** function.

The interaction handler component is located in the `/Content/StackOBot/Blueprints/GameElements` folder. The grab logic is included in the **BP\_Bot** Blueprint, which is located in the `/Content/StackOBot/Blueprints/Character` folder.

### Objective Tracking

Stack O Bot implements an objective system using the [Game Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/game-mode-and-game-state-in-unreal-engine). You can tag interactive actors using the **IsObjective** boolean in the interaction handler blueprint component. When the player interacts with the tagged actor, the objective updates.

The objectives are tracked in the game's [user interface (UI)](https://dev.epicgames.com/documentation/en-us/unreal-engine/user-interfaces-and-huds-in-unreal-engine). The interaction handler sends the object status to the UI and updates the UI as necessary.

Objectives are also visually represented in the map by the **BP\_Portal** actor, which has one light per objective. The lights turn on as the objectives are completed. After all objectives are completed and all lights are lit, the portal becomes active and the trigger collision is enabled. This activation allows the player to complete the map by entering the portal. The interaction handler component manages the logic for the lights and the portal.

The interaction handler component (**BPC\_InteractionHandler**) and the portal blueprint (**BP\_Portal**) are located in the `/Content/StackOBot/Blueprints/GameElements` folder. The user interface asset (**HUD\_InGame**) is located in the `/Content/StackOBot/Blueprints/Framework` folder.

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [physics](https://dev.epicgames.com/community/search?query=physics)
* [level instancing](https://dev.epicgames.com/community/search?query=level%20instancing)
* [programming](https://dev.epicgames.com/community/search?query=programming)
* [mobile](https://dev.epicgames.com/community/search?query=mobile)
* [statetree](https://dev.epicgames.com/community/search?query=statetree)
* [procedural generation](https://dev.epicgames.com/community/search?query=procedural%20generation)
* [fab](https://dev.epicgames.com/community/search?query=fab)
* [learning](https://dev.epicgames.com/community/search?query=learning)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Open The Stack O Bot Project](/documentation/en-us/unreal-engine/stack-o-bot-sample-game-in-unreal-engine?application_version=5.7#openthestackobotproject)
* [Recommended System Specifications](/documentation/en-us/unreal-engine/stack-o-bot-sample-game-in-unreal-engine?application_version=5.7#recommendedsystemspecifications)
* [Navigating The Stack O Bot Project](/documentation/en-us/unreal-engine/stack-o-bot-sample-game-in-unreal-engine?application_version=5.7#navigatingthestackobotproject)
* [Stack O Bot In-Game Controls](/documentation/en-us/unreal-engine/stack-o-bot-sample-game-in-unreal-engine?application_version=5.7#stackobotin-gamecontrols)
* [Stack O Bot Features](/documentation/en-us/unreal-engine/stack-o-bot-sample-game-in-unreal-engine?application_version=5.7#stackobotfeatures)
* [Level Introduction](/documentation/en-us/unreal-engine/stack-o-bot-sample-game-in-unreal-engine?application_version=5.7#levelintroduction)
* [Customizable Third-Person Character](/documentation/en-us/unreal-engine/stack-o-bot-sample-game-in-unreal-engine?application_version=5.7#customizablethird-personcharacter)
* [Procedural Content Generation (PCG)](/documentation/en-us/unreal-engine/stack-o-bot-sample-game-in-unreal-engine?application_version=5.7#proceduralcontentgeneration(pcg))
* [Smart UV-Less Materials](/documentation/en-us/unreal-engine/stack-o-bot-sample-game-in-unreal-engine?application_version=5.7#smartuv-lessmaterials)
* [HLOD Generation](/documentation/en-us/unreal-engine/stack-o-bot-sample-game-in-unreal-engine?application_version=5.7#hlodgeneration)
* [StateTree NPC Behavior](/documentation/en-us/unreal-engine/stack-o-bot-sample-game-in-unreal-engine?application_version=5.7#statetreenpcbehavior)
* [Modular Level Instances](/documentation/en-us/unreal-engine/stack-o-bot-sample-game-in-unreal-engine?application_version=5.7#modularlevelinstances)
* [Physics-based Interactions](/documentation/en-us/unreal-engine/stack-o-bot-sample-game-in-unreal-engine?application_version=5.7#physics-basedinteractions)
* [Dynamic Camera](/documentation/en-us/unreal-engine/stack-o-bot-sample-game-in-unreal-engine?application_version=5.7#dynamiccamera)
* [Gameplay Interactions](/documentation/en-us/unreal-engine/stack-o-bot-sample-game-in-unreal-engine?application_version=5.7#gameplayinteractions)
* [Objective Tracking](/documentation/en-us/unreal-engine/stack-o-bot-sample-game-in-unreal-engine?application_version=5.7#objectivetracking)
