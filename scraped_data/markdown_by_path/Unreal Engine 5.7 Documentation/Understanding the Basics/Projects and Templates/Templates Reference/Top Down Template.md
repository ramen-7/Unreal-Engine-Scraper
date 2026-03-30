<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/top-down-template-in-unreal-engine?application_version=5.7 -->

# Top Down Template

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
5. [Understanding the Basics](/documentation/en-us/unreal-engine/understanding-the-basics-of-unreal-engine "Understanding the Basics")
6. [Projects and Templates](/documentation/en-us/unreal-engine/working-with-projects-and-templates-in-unreal-engine "Projects and Templates")
7. [Templates Reference](/documentation/en-us/unreal-engine/unreal-engine-templates-reference "Templates Reference")
8. Top Down Template

# Top Down Template

An introduction to the Top Down game template in Unreal Engine.

![Top Down Template](https://dev.epicgames.com/community/api/documentation/image/efd6a377-80d2-4042-af14-393257c288ee?resizing_type=fill&width=1920&height=335)

 On this page

When you create a new project, Unreal Engine gives you a list of templates you can choose from. These templates contain some ready-to-use assets, such as level geometry, a character you can control, and simple character animations. Many tutorials use one of these templates as a starting point.

In a Top Down game, the player sees the game from a camera behind and above the character at a greater distance than for a [third-person game](https://dev.epicgames.com/documentation/en-us/unreal-engine/third-person-template-in-unreal-engine). In some types of top-down games, the player controls the character using a mouse or a touchscreen to move the character. In other top down games, the player uses a keyboard or gamepad. In this template, you click and hold the mouse down to move the character in a direction for the basic (non-variant) project.

## Creating a Top Down Project

Launching Unreal Engine opens the Project Browser window, where you can choose to open an existing Unreal project or create something new. To create a top-down game project, select the **Games** category on the left, and then select the **Top Down** template.

[![Creating a new Top Down project in Unreal Engine.](https://dev.epicgames.com/community/api/documentation/image/c1bec625-812c-42ba-aa21-4f8f0226d435?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c1bec625-812c-42ba-aa21-4f8f0226d435?resizing_type=fit)

When the **Top Down** template is selected, there are several additional settings you can configure in the panel on the right side of the project browser window to set up the Top Down project. You can configure the following settings:

| Setting | Description |
| --- | --- |
| **Target Platform** | Select the kind of platform your project is intended for:   * **Desktop** * **Mobile** |
| **Quality Preset** | Select the maximum quality level, based on which platform your project targets:   * **Maximum**, if you are developing your project for a computer or game console. * **Scalable**, if you are developing your project for mobile devices. |
| **Variant** | The variant of the template you want to open. Variants add additional assets to the project. For more about variants, see the Template Variants section of this page. |

After following these steps, the project includes a basic level with a top-down camera and a character you can control.

To try out the level, click **Play** in the **Main Toolbar**. When using the base template, click or hold the **mouse** or **touchscreen** to move the character around the level. Variants use different controls for their gameplay.

## Template Variants

The **Top Down** template includes a set of variants to choose from located in the Variants dropdown menu. Variants give you a way to build different gameplay styles. The Top Down template includes variants for **Strategy** and **Twin Stick** gameplay.

[![The Variant options for the Top Down template.](https://dev.epicgames.com/community/api/documentation/image/b7739bba-0803-4fbe-89d8-62541d9b2af7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b7739bba-0803-4fbe-89d8-62541d9b2af7?resizing_type=fit)

|  |  |
| --- | --- |
| Variant Name | Description |
| **None** | A basic template with the following contents:   * A playable character that can move. * A level with basic geometry such as ramps and platforms. * A cursor effect that plays when the player clicks a spot on the level. |
| **Strategy** | A template of a top-down strategy game with the following contents:   * Multiple characters (units) that can be selected and moved around the level. * A level with basic geometry such as ramps, platforms, and rooms with roofs. * A cursor effect that plays when the player clicks a spot on the level. * A material applied to the roofs that lets the player see into the rooms with roofs. * Cubes that units can have physics interactions with. * A camera that can be moved and zoomed in and out. * A UI that shows how many units are selected. |
| **Twin Stick** | A template of a top-down twin stick shooter game with the following contents:   * A playable character that can move, shoot projectiles, and use bombs. * A level with basic geometry. * AI opponents that approach the player and can be destroyed for points. * A multiplier that grows as the player destroys enemies. * A UI that shows the player's score, multiplier, and number of bombs. |

For a deeper dive into the features of these variants, see [Game Template Variants](https://dev.epicgames.com/documentation/en-us/unreal-engine/variants-in-game-templates).

### Strategy Variant

The **Strategy** variant features an orthographic camera and multiple characters (or units) that can be selected and moved as a group. The units can interact with the cubes while moving, and can stand near automatic doors to open them. Some objects, such as roofs (colored blue) over structures use a special material allowing for the camera to see behind them and what is inside this area.

[![The Strategy variant of the Top Down template.](https://dev.epicgames.com/community/api/documentation/image/576ba78d-2558-4620-b929-e1fbf07a935d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/576ba78d-2558-4620-b929-e1fbf07a935d?resizing_type=fit)

#### Camera

The Strategy variant uses a camera with **Orthographic** projection to create an isometric view of the level. The camera can zoom in and zoom out, and move around using the mouse or keyboard.

The logic for the camera can be found in **BP\_StrategyPlayerController** and **BP\_StrategyPawn**, located in the `Content/Variant_Strategy/Blueprints folder`.

In this Blueprint, you can select the **Camera** component and change settings for its orthographic projection under the **Camera Settings** in the **Details** panel.

[![The Camera Settings in the Details panel.](https://dev.epicgames.com/community/api/documentation/image/6c161622-4a42-4d1f-8d8d-96a47c216ccb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6c161622-4a42-4d1f-8d8d-96a47c216ccb?resizing_type=fit)

To learn more about this projection mode and its settings, see [Orthographic Camera](https://dev.epicgames.com/documentation/en-us/unreal-engine/orthographic-camera-in-unreal-engine).

#### Units

The Strategy variant contains multiple characters, or units, that the player can select and move around the level. When one or more units is selected, the player can click or tap in the level to instruct the units to move to that location.

The units have a few interactions with each other and the level. When one unit gets close to another unit, they both play an animation. If the units are near an automatic door, the door will open. As units move, they can bump into the cubes and have physics interactions, which will bounce off of the units.

The logic for the units movement and interactions can be found in **BP\_StrategyUnit** and **BP\_StrategyPlayerController**, both located in the `Content/Variant_Strategy/Blueprints` folder.

#### Roof Camera Cutout Effect

The effect of having the camera see through an opaque surface in the Strategy variant is done using a masked material. While this effect affects what the camera sees, the material, itself, controls how this happens by taking into account screen position and the camera’s location because it is always set to the same distance from any object’s surface.  This is done using the **M\_Cutout** material located in the `Content/Variant_Strategy` folder.

Because the material is set up using parameters and variables, you can create a Material Instance of M\_Cutout and adjust these to make the masked cutout larger or smaller to suit your gameplay needs. You can also use this material as a basis to build on top of to make it uniquely your own for your own project. When using this material as a Material Instance, adjust the **Strength** variable to make the cutout larger or smaller.

Adjusting the Strength variable

To learn more about materials and material instances to use their variables and parameters, see [Instanced Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/instanced-materials-in-unreal-engine).

#### User Interface

The Strategy variant has a UI element that shows how many units the player has selected. The widget Blueprint for the UI is located in the `Content/Variant_Strategy/UI` folder.

### Twin Stick Variant

The **Twin Stick** variant features a player character that can aim in any direction and fire projectiles and bombs, as well as simple AI opponents that follow the player and can be destroyed. Destroying the enemies gives the player points, and as the player destroys more enemies in succession, they gain a multiplier that applies to the points they gain. The multiplier goes down over time if the player stops destroying enemies.

[![The Twin Stick variant of the Top Down template.](https://dev.epicgames.com/community/api/documentation/image/4b3e5a1e-d1a2-4cc6-818c-569ff02b3c46?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4b3e5a1e-d1a2-4cc6-818c-569ff02b3c46?resizing_type=fit)

#### Projectiles and Bombs

In the Twin Stick variant, the player character can fire projectiles and use bombs that destroy the enemies in the level. Projectiles are fired by pressing the **F** key, clicking the **left mouse button**, or pressing the **right trigger** on a controller. Projectiles are aimed using the **mouse** or the **right thumbstick** on a controller. Bombs appear in the level as spheres, and can be collected when the player character touches them. Bombs can be used by pressing the **G** key, clicking the **right mouse button**, or pressing the **left trigger** on a controller.

When a projectile hits an enemy, a particle effect is spawned. The particle visual effect is created using a [Niagara](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine) system.

The blueprints for the projectiles and bombs are located in the the `Content/Variant_TwinStick/Blueprints` folder. The mesh for projectiles and bombs is located in the `Content/Variant_TwinStick` folder.

#### Enemies

The enemies in the Twin Stick variant spawn from the corners of the play area and move towards the player. When the player character touches an enemy, the player character is pushed back some distance away from the enemy. The player can destroy the enemies by hitting them with projectiles or bombs. When an enemy is hit with a projectile or a bomb, it explodes, which is done using a [Chaos Physics](https://dev.epicgames.com/documentation/en-us/unreal-engine/physics-in-unreal-engine) geometry collection.

The blueprints for the enemies are located in the `Content/Variant_TwinStick/Blueprints/AI` folder, and the meshes are located in the `Content/Variant_TwinStick/Meshes` folder.

#### User Interface

The UI for the Twin Stick variant shows the player's score, the player's current score multiplier, and the number of bombs that the player has. The UI assets are in the `Content/Variant_TwinStick/UI` folder.

## Template Contents

The following section details these contents and where to find them in the **Content Browser**.

### Blueprints

The None variant of the Top Down template include Blueprints for the following assets:

* Player character
* Game mode
* Player controller

These Blueprints are located in the `Content/TopDown/Blueprints` folder.

The Event Graph in each Blueprint includes comments and annotations about what the different node groups do and the logic behind their implementation.

The Strategy variant uses the player character, player controller, and game mode in the `Content/Variant_Strategy/Blueprints` folder.

The Twin Stick variant uses the player character, player controller, and game mode in the `Content/Variant_TwinStick/Blueprints` folder.

### Cursor

The None and Strategy variants have a cursor animation that plays when the player clicks somewhere on the level. The assets for the cursor animation are located in the `Content/Variant_TwinStick/Cursor` and the `Content/Variant_TwinStick/TopDown/Cursor` folders.

### Level

In the None variant of the Top Down template, the level, **Lvl\_TopDown**, is located in the `Content/TopDown` folder. The assets that make up the level geometry (static meshes, materials, and textures) are located in the `Content/LevelPrototyping` folder.

In the Strategy variant, the level, **Lvl\_Strategy**, is located in the `Content/Variant_Strategy` folder. This level includes ramps, platforms, rooms with roofs, physics-enabled cubes, and multiple controllable characters.

In the Twin Stick variant, the level, **Lvl\_TwinStick**, is located in the `Content/Variant_TwinStick` folder. This level includes enemy spawn points,

## Improving your Project

Now that you have a playable level, you can start to import your own content and make changes to the game. Or, you can use the assets provided in the Content Browser with this project to build it out by dragging and dropping these assets into the level and placing them where you want.

For more instructions on how to populate your level, see [Level Designer Quick Start](https://dev.epicgames.com/documentation/en-us/unreal-engine/level-designer-quick-start-in-unreal-engine).

## What's Next?

Now that you've gone through the basics of creating a top-down experience, here are some other things you can try:

* Populate your level with content and props from [Fab](https://dev.epicgames.com/documentation/en-us/unreal-engine/fab-window-in-unreal-engine?application_version=5.3). You can build a variety of indoor and outdoor environments.
* Create or modify the in-game heads-up display (HUD) with [Unreal Motion Graphics (UMG)](https://dev.epicgames.com/documentation/en-us/unreal-engine/umg-editor-reference-for-unreal-engine).
* Use [Niagara](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine) to add or change visual effects in your game.
* Add or build upon existing AI characters using [StateTrees](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-state-tree-in-unreal-engine) or [Behavior Trees](https://dev.epicgames.com/documentation/en-us/unreal-engine/behavior-trees-in-unreal-engine).

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Creating a Top Down Project](/documentation/en-us/unreal-engine/top-down-template-in-unreal-engine?application_version=5.7#creatingatopdownproject)
* [Template Variants](/documentation/en-us/unreal-engine/top-down-template-in-unreal-engine?application_version=5.7#templatevariants)
* [Strategy Variant](/documentation/en-us/unreal-engine/top-down-template-in-unreal-engine?application_version=5.7#strategyvariant)
* [Camera](/documentation/en-us/unreal-engine/top-down-template-in-unreal-engine?application_version=5.7#camera)
* [Units](/documentation/en-us/unreal-engine/top-down-template-in-unreal-engine?application_version=5.7#units)
* [Roof Camera Cutout Effect](/documentation/en-us/unreal-engine/top-down-template-in-unreal-engine?application_version=5.7#roofcameracutouteffect)
* [User Interface](/documentation/en-us/unreal-engine/top-down-template-in-unreal-engine?application_version=5.7#userinterface)
* [Twin Stick Variant](/documentation/en-us/unreal-engine/top-down-template-in-unreal-engine?application_version=5.7#twinstickvariant)
* [Projectiles and Bombs](/documentation/en-us/unreal-engine/top-down-template-in-unreal-engine?application_version=5.7#projectilesandbombs)
* [Enemies](/documentation/en-us/unreal-engine/top-down-template-in-unreal-engine?application_version=5.7#enemies)
* [User Interface](/documentation/en-us/unreal-engine/top-down-template-in-unreal-engine?application_version=5.7#userinterface-2)
* [Template Contents](/documentation/en-us/unreal-engine/top-down-template-in-unreal-engine?application_version=5.7#templatecontents)
* [Blueprints](/documentation/en-us/unreal-engine/top-down-template-in-unreal-engine?application_version=5.7#blueprints)
* [Cursor](/documentation/en-us/unreal-engine/top-down-template-in-unreal-engine?application_version=5.7#cursor)
* [Level](/documentation/en-us/unreal-engine/top-down-template-in-unreal-engine?application_version=5.7#level)
* [Improving your Project](/documentation/en-us/unreal-engine/top-down-template-in-unreal-engine?application_version=5.7#improvingyourproject)
* [What's Next?](/documentation/en-us/unreal-engine/top-down-template-in-unreal-engine?application_version=5.7#what'snext?)
