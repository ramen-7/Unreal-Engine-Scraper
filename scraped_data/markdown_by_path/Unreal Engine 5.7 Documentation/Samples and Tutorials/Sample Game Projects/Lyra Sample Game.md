<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/lyra-sample-game-in-unreal-engine?application_version=5.7 -->

# Lyra Sample Game

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
7. Lyra Sample Game

# Lyra Sample Game

Explore how to develop projects in UE5 using techniques from the Lyra Sample Game.

![Lyra Sample Game](https://dev.epicgames.com/community/api/documentation/image/52e322d9-ef07-4322-9527-c79ef3e4ddf7?resizing_type=fill&width=1920&height=335)

 On this page

**Lyra** is a learning resource designed as a sample game project to help you understand the frameworks of Unreal Engine 5 (UE5). Its architecture is designed to be modular, including a core system and plugins that are updated regularly along with the development of UE5.

* Cross-Platform compatibility and scalability.
* Online Multiplayer and cross-play support for Epic Online Services and Console Online Subsystems.
* Features a choice between three different Game modes: Elimination (Team Deathmatch), Control (Capture the Control point) and Exploder (a top down party game).
* A customized Gameplay Ability System.
* Niagara FX.
* Unreal Motion Graphics (UMG) widget classes and UI Icons for the project's gameplay concepts including menu settings, controller key sticks, and displays for health, mana, and ammo. These UI features are designed with modularity so you could use their systems in your own game independent of Lyra.
* Optimized, hand-crafted content including locomotion animation assets, sounds, and a weapon system compatible with any Pawn.
* New UE5 Mannequins, Manny, and Quinn. These Mannequins are playable characters that share the same core skeleton hierarchy as MetaHumans, with a compatible animation system.

## Downloading the Lyra Starter Game

To install the Lyra Starter Game sample project, follow these steps:

1. Access the [Lyra Starter Game sample](https://fab.com/s/3fe3f994dd6d) from **Fab** and click **Add to My Library** for the project file to show in the **Epic Games Launcher**.

   1. Alternatively, you can search for the sample project using Fab in Launcher, or the Fab plugin for UE.
2. From the **Epic Games Launcher** go to **Unreal Engine > Library > Fab Library** to access the project.

   Sample projects only appear in **Fab Library** when you have the compatible engine version installed.
3. Click **Create Project** and follow the on-screen instructions to download the sample and start a new project.

To learn more about accessing sample content from Fab, see [Samples and Tutorials](https://dev.epicgames.com/documentation/en-us/unreal-engine/samples-and-tutorials-for-unreal-engine).

## Downloading Lyra for Engine Source Builds

You can download your own source build of Unreal Engine, refer to [Downloading Unreal Engine SourceCode](programming-and-scripting/development-environment-setup/downloading-unreal-engine-source-code).

When you have finished downloading your Unreal Engine source build, you will want to download and install Lyra inside the top level directory of your custom-built engine. After selecting a top level directory, it will create a LyraStarterGame subdirectory, then create a LyraStarterGame.uproject file including the source code and content.

[![lyra-uproject-directory](https://dev.epicgames.com/community/api/documentation/image/ac514aed-b4a0-41d8-8b45-8a2dab5d15e2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ac514aed-b4a0-41d8-8b45-8a2dab5d15e2?resizing_type=fit)

To launch your installed copy of the sample, you can either double click the `.uproject` file or launch the sample directly from the Library tab of the launcher.

[![lyra-sample-from-library-launcher](https://dev.epicgames.com/community/api/documentation/image/f705b0e8-98c7-4562-8ac2-953d97e83d38?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f705b0e8-98c7-4562-8ac2-953d97e83d38?resizing_type=fit)

If you are using a custom-built version of the engine, you can recreate project files and launch Lyra as a project from inside your source code editor such as Visual Studio.

If you right click the `LyraStarterGame.uproject` file you can associate it with a different installed version of the engine if you have multiple copies installed, or generate project files for compiling with a source code editor.

[![uproject-options-list](https://dev.epicgames.com/community/api/documentation/image/e8ebe2be-2b0d-4ccb-9e71-bc9f1b87bab1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e8ebe2be-2b0d-4ccb-9e71-bc9f1b87bab1?resizing_type=fit)

## Playing the Game Sample

When you launch Lyra, the **DefaultEditorOverview** level will be loaded as the **Default Map**. From the Editor, you can click on **Play In Editor**(**PIE**) to launch the default level.

[![play-in-editor-arrow](https://dev.epicgames.com/community/api/documentation/image/e3808222-4097-40bf-a053-81f4a6d04d33?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e3808222-4097-40bf-a053-81f4a6d04d33?resizing_type=fit)

When in PIE, Your Player Controller will take possession of the Lyra Pawn. In the level there are several portals that load into an **Experience**.

[![main-game-select](https://dev.epicgames.com/community/api/documentation/image/7d578996-9ac9-4c2c-8174-67afd4a8b578?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7d578996-9ac9-4c2c-8174-67afd4a8b578?resizing_type=fit)

The table below provides a brief description into each map:

| Game Mode Map | Description | Content File Path |
| --- | --- | --- |
| **Control** | Secure the control points along with your teammates to increase your score and win. | `/ShooterMaps/Maps/L_Convolution_Blockout` |
| **Elimination** | Find and eliminate enough enemies to win in this classic head-to-head team match. | `/ShooterMaps/Maps/L_Expanse` |
| **Front End** | Contains the Main Menu of the Lyra sample game. | `/Game/System/FrontEnd/Maps/L_LyraFrontEnd` |
| **Default Map** | The base example of the user facing map. | `/Game/System/DefaultEditorMap/L_DefaultEditorOverview` |
| **Shooter Gym** | A small test level to test the ShooterCore plugin functionality. | `/ShooterCore/Maps/L_ShooterGym` |
| **Exploder** | Destroy blocks, collect power-ups, and avoid getting exploded in this top-down party game. | `/TopDownArena/Maps/L_TopDownArenaGym` |

The maps for each game mode can be loaded directly in the editor by using **File > Open Level** and navigating to the content file paths listed above.

[![using-the-open-level-window](https://dev.epicgames.com/community/api/documentation/image/2ce6972e-abbd-46ad-b826-1c44e57a99da?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2ce6972e-abbd-46ad-b826-1c44e57a99da?resizing_type=fit)

Most of the maps are located inside game feature plugins. After loading a map like **Expanse** for the first time, the **Editor Viewport** will be empty because it is a **World Partition** map.

[![expanse-world-partition](https://dev.epicgames.com/community/api/documentation/image/6cd8ed19-6080-439a-940e-f7290efe2b0a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6cd8ed19-6080-439a-940e-f7290efe2b0a?resizing_type=fit)

To see the level Actors, select the **world partition grid cells** by clicking and dragging in the bottom right **World Partition** details panel, then right click and select **Load Selected Cells** to load that part of the map.

[![](https://dev.epicgames.com/community/api/documentation/image/47c7b07f-3336-4d2a-850d-edce9a211871?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/47c7b07f-3336-4d2a-850d-edce9a211871?resizing_type=fit)

Using PIE while one of the Game Mode levels is open will load the appropriate game mode as if you had walked into the appropriate portal on the default map.

For more information on Lyra's Game maps and menus, refer to the [A Tour of Lyra](https://dev.epicgames.com/documentation/en-us/unreal-engine/tour-of-lyra-in-unreal-engine) reference page.

## Lyra Framework Systems

Lyra makes use of the **Gameplay Feature Plugins**, this means that the Content folder only contains generic assets and the main lobby, however, the plugins folder contains the different core elements that create the Lyra Starter Game.

[![plugins-content-folder](https://dev.epicgames.com/community/api/documentation/image/c2767406-b05e-4db8-950f-9053e3892775?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c2767406-b05e-4db8-950f-9053e3892775?resizing_type=fit)

When a game experience is chosen inside the lobby, the game will load the plugins that are required. For example, choosing the **Expanse** Team Deathmatch\_ map will load **ShooterCore** for the pawn and mechanics, and **ShooterMaps** for the level.

| Plugin Folder Name | Description |
| --- | --- |
| **Lyra Example Content** | Contains shared materials, such as grids. |
| **Shooter Core Content** | The core elements of the LyraShooterGame experience. This includes gameplay logic for game modes, specific Gameplay Abilities like Dash, and Blueprints for Actors such as teleporters and grenades, Bots, Weapons and User Interface elements. |
| **ShooterMaps Content** | The maps used by the LyraShooterGame (Expanse and Convolution), with associated materials and content. |
| **TopDownArena Content** | The content for the TopDownArena experience, from the map generator to power ups. |

Experiences are defined using a **LyraExperienceDefinition** class. You can access the **Default Gameplay Experience** from the World Settings by navigating to the **Toolbar** > **Window** > **World Settings** > **Game Mode**.

[![world-settings-experience-definition](https://dev.epicgames.com/community/api/documentation/image/ab467ec5-493f-42d3-9a4c-fb4339d5c6b3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ab467ec5-493f-42d3-9a4c-fb4339d5c6b3?resizing_type=fit)

You can think of experiences as a much more advanced version of a GameMode. Multiple Experiences can exist inside a plugin, for example the experiences Team Death Match and Control Points both use the ShooterCore plugins and are derived from the same parent class(**B\_LyraShooterGameVase**, a child class of the LyraExperienceDefinition.)

These classes contain the information that are used in Lyra's input and gameplay mechanics. While other options contain information like the scoring system (based on Elimination for Team Deathmatch and Capture for Control Points)

## Topics

* [![Common User Plugin](https://dev.epicgames.com/community/api/documentation/image/e3bc044f-a5cb-4fc6-8b59-399a92d02220?resizing_type=fit&width=640&height=640)

  Common User Plugin

  The Common User plugin provides a common interface between C++, Blueprint Scripting, and the Online Subsystem(OSS) or other online backends.](https://dev.epicgames.com/documentation/en-us/unreal-engine/common-user-plugin-in-unreal-engine-for-lyra-sample-game)
* [![Abilities in Lyra](https://dev.epicgames.com/community/api/documentation/image/b7b50ae7-3c1c-42bc-8c81-bbfe74cfd98f?resizing_type=fit&width=640&height=640)

  Abilities in Lyra

  An overview of how Lyra uses the Gameplay Ability System for its Gameplay.](https://dev.epicgames.com/documentation/en-us/unreal-engine/abilities-in-lyra-in-unreal-engine)
* [![Animation In Lyra](https://dev.epicgames.com/community/api/documentation/image/95a41baf-0a27-4b6b-ad3d-f82636bda7c6?resizing_type=fit&width=640&height=640)

  Animation In Lyra

  An overview of the Animation System in Lyra](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-in-lyra-sample-game-in-unreal-engine)
* [![Lyra Game Settings](https://dev.epicgames.com/community/api/documentation/image/abce718a-4826-453c-9859-98ba873ca799?resizing_type=fit&width=640&height=640)

  Lyra Game Settings

  An overview of Game Settings for the Lyra Game Sample.](https://dev.epicgames.com/documentation/en-us/unreal-engine/lyra-sample-game-settings-in-unreal-engine)
* [![Geometry Tools in Lyra](https://dev.epicgames.com/community/api/documentation/image/2e3607b6-9293-48fb-909c-2f81fbdeb66f?resizing_type=fit&width=640&height=640)

  Geometry Tools in Lyra

  An overview of how Geometry Tools was used in Lyra to create parametric level level design geometry objects in Blueprints, and the workflows that Level Designers use to build the level with these pieces.](https://dev.epicgames.com/documentation/en-us/unreal-engine/lyra-geometry-tools-in-unreal-engine)
* [![Lyra Input Settings](https://dev.epicgames.com/community/api/documentation/image/abb46b05-d4aa-4797-85b3-50a228b29f0b?resizing_type=fit&width=640&height=640)

  Lyra Input Settings

  An overview of how Lyra uses its Input Settings system to solve many common input configuration setups.](https://dev.epicgames.com/documentation/en-us/unreal-engine/lyra-input-settings-in-unreal-engine)
* [![Lyra Interaction System](https://dev.epicgames.com/community/api/documentation/image/e3996239-24c9-497b-baa5-1c67dd7758fc?resizing_type=fit&width=640&height=640)

  Lyra Interaction System

  An overview of the Lyra Interaction System for the Lyra Game sample.](https://dev.epicgames.com/documentation/en-us/unreal-engine/lyra-sample-game-interaction-system-in-unreal-engine)
* [![Lyra Inventory and Equipment](https://dev.epicgames.com/community/api/documentation/image/90bf0302-4014-4f34-8130-8b2e11e78ba9?resizing_type=fit&width=640&height=640)

  Lyra Inventory and Equipment

  Explore the Inventory and Equipment systems used in the Lyra Sample Game.](https://dev.epicgames.com/documentation/en-us/unreal-engine/lyra-inventory-and-equipment-in-unreal-engine)
* [![Lyra Scalability and Device Profiles](https://dev.epicgames.com/community/api/documentation/image/8e5f3d25-e506-4a12-945c-a230068985ff?resizing_type=fit&width=640&height=640)

  Lyra Scalability and Device Profiles

  An overview of Scalability and Device Profiles in the Lyra Game Sample.](https://dev.epicgames.com/documentation/en-us/unreal-engine/scalability-and-device-profiles-in-lyra-sample-game-for-unreal-engine)
* [![Tour of Lyra](https://dev.epicgames.com/community/api/documentation/image/9db4f5d2-47c2-4fa7-81e2-a362b144a2f1?resizing_type=fit&width=640&height=640)

  Tour of Lyra

  Reference page of Lyra in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/tour-of-lyra-in-unreal-engine)
* [![Upgrading the Lyra Starter Game to the Latest Engine Release](https://dev.epicgames.com/community/api/documentation/image/3eb5732b-a3fb-488b-aaad-f1d16f716611?resizing_type=fit&width=640&height=640)

  Upgrading the Lyra Starter Game to the Latest Engine Release

  Documents the major changes to Lyra for each engine version and includes information that help you upgrade existing games to take advantage of the newest release of Unreal Engine 5.](https://dev.epicgames.com/documentation/en-us/unreal-engine/upgrading-the-lyra-starter-game-to-the-latest-engine-release-in-unreal-engine)
* [![Using Lyra With Epic Online Services](https://dev.epicgames.com/community/api/documentation/image/335d0c19-aba6-445a-a055-0c0bf499ca12?resizing_type=fit&width=640&height=640)

  Using Lyra With Epic Online Services

  A step-by-step tutorial describing how to use the Lyra sample game for working with Epic Online Services.](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-lyra-with-epic-online-services-in-unreal-engine)

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [audio](https://dev.epicgames.com/community/search?query=audio)
* [programming](https://dev.epicgames.com/community/search?query=programming)
* [ai](https://dev.epicgames.com/community/search?query=ai)
* [lyra](https://dev.epicgames.com/community/search?query=lyra)
* [shootercore](https://dev.epicgames.com/community/search?query=shootercore)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Downloading the Lyra Starter Game](/documentation/en-us/unreal-engine/lyra-sample-game-in-unreal-engine?application_version=5.7#downloading-the-lyra-starter-game)
* [Downloading Lyra for Engine Source Builds](/documentation/en-us/unreal-engine/lyra-sample-game-in-unreal-engine?application_version=5.7#downloading-lyra-for-engine-source-builds)
* [Playing the Game Sample](/documentation/en-us/unreal-engine/lyra-sample-game-in-unreal-engine?application_version=5.7#playing-the-game-sample)
* [Lyra Framework Systems](/documentation/en-us/unreal-engine/lyra-sample-game-in-unreal-engine?application_version=5.7#lyra-framework-systems)
* [Topics](/documentation/en-us/unreal-engine/lyra-sample-game-in-unreal-engine?application_version=5.7#topics)

Related documents

[Samples and Tutorials

![Samples and Tutorials](https://dev.epicgames.com/community/api/documentation/image/f1954fd2-f9a4-4083-bc27-c000b758efb3?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/samples-and-tutorials-for-unreal-engine)
