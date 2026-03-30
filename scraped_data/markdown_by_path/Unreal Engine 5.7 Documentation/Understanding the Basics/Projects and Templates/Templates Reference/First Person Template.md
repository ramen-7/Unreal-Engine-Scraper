<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/first-person-template-in-unreal-engine?application_version=5.7 -->

# First Person Template

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
4. First Person Template

# First Person Template

An introduction to the First Person game template in Unreal Engine.

![First Person Template](https://dev.epicgames.com/community/api/documentation/image/bb6c2c22-1bd7-48d2-ae8b-c52244dee448?resizing_type=fill&width=1920&height=335)

 On this page

When you create a new project, Unreal Engine gives you a list of templates you can choose from. These templates contain some ready-to-use assets, such as level geometry, a character you can control, and simple character animations. Many tutorials use one of these templates as a starting point.

In a **First Person** game, the player sees the game from the viewpoint of the character they are playing as. Some first-person games show parts of the character models, like the character's arms or a weapon. This is different from a [third-person game](https://dev.epicgames.com/documentation/en-us/unreal-engine/third-person-template-in-unreal-engine), where you see the action from a point that's behind and slightly above the character.

## Creating a First Person Project

Launching Unreal Engine opens the **Project Browser** window, where you can choose to open an existing Unreal project or create something new. To create a first-person project, select the **Games** category on the left, and then select the **First Person** template.

[![Creating a new first-person project in Unreal Engine 5.](https://dev.epicgames.com/community/api/documentation/image/debd6ed0-878f-4c94-95e8-19763c0e3195?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/debd6ed0-878f-4c94-95e8-19763c0e3195?resizing_type=fit)

Creating a new first-person project in Unreal Engine 5.

There are several additional settings you can configure for your **First Person** project. You can configure the following settings:

| Setting | Description |
| --- | --- |
| **Target Platform** | Select the kind of platform your project is intended for:   * **Desktop** * **Mobile** |
| **Quality Preset** | Select the maximum quality level, based on which platform your project targets. We recommend that you choose:   * **Maximum**, if you are developing your project for a computer or game console. * **Scalable**, if you are developing your project for mobile devices. |
| **Variant** | The variant of the template you want to use. Variants add additional assets to the project. For more about variants, see the Template Variants section of this page. |

After following these steps, the project includes a basic level with a first-person character you can control using the keyboard and mouse.

To try out the level, click **Play** in the Main Toolbar. Use the **WASD** keys to move your character, and look around by moving the mouse.

## Template Variants

The First Person template includes a set of variants to choose from located in the **Variants** dropdown menu. Variants give you a way to build select gameplay styles faster. The First Person template includes a variant with no additional content (**None**) and variants for **Arena Shooter** and **Survival Horror** gameplay.

[![The Variants dropdown menu](https://dev.epicgames.com/community/api/documentation/image/38cf47c0-e22d-41d7-b02f-f6d849faf672?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/38cf47c0-e22d-41d7-b02f-f6d849faf672?resizing_type=fit)

| Variant Name | Description |
| --- | --- |
| **None** | A basic template with the following contents:   * A playable first-person character that can move. * A level with basic geometry such as ramps and platforms. |
| **Arena Shooter** | A template of a first person shooter game with the follow contents:   * A playable first-person character that can move. * A level with basic geometry such as ramps and platforms. * Multiple guns that the player can pick up and use to fire projectiles. * Enemies that move around the level and can be shot by the player. * Pads that cause the character to jump. * A UI that shows a crosshair, a score, and weapon ammo. |
| **Survival Horror** | A template of a first person survival horror game with the follow contents:   * A playable first-person character that can move. * A dark level with lights, ramps, platforms, and automatic doors. * A sprint function and stamina bar for the character. |

For a deeper dive into the features of these variants, see [Game Template Variants](https://dev.epicgames.com/documentation/en-us/unreal-engine/variants-in-game-templates).

### Arena Shooter Variant

The **Arena Shooter** variant includes a confined level with multiple levels, weapon pickups, and AI opponents.

[![In-game screenshot of the Arena Shooter variant](https://dev.epicgames.com/community/api/documentation/image/34bf0882-0074-4769-add1-0f00762d5c03?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/34bf0882-0074-4769-add1-0f00762d5c03?resizing_type=fit)

#### Weapons

In the Arena Shooter variant, the player character can walk over weapon pickup spots to pick up different weapons: a grenade launcher, a pistol, and arifle.

The `Content/Weapons` folder contains the assets for the different gun types.

The blueprints for the weapons and the weapon pickups are in the `Content/Variant_Shooter/Blueprints/Pickups` folder. There is a weapon base class (**BPWeaponBase**), which has been used to create classes for the grenade launcher, pistol, and rifle.

Projectiles are spawned on left-click and apply a physics impulse to any physics-enabled actor they collide with in the level. You can see how this logic was implemented in the **BP\_FirstPersonProjectile** Blueprint located in the `Content/Variant_Shooter/Blueprints/Pickups/Projectiles` folder.

There are animations for the character mesh that correspond to each of the weapons in the `Content/Variant_Shooter/Anims` folder.

#### Enemies

The Arena Shooter variant includes enemies that walk around the level, searching for and shooting at the player. The player and the enemies can all be shot and killed. The blueprints for the enemy are in the `Content/Variant_Shooter/Blueprints/AI` folder, along with [State Trees](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-state-tree-in-unreal-engine), [Environment Queries](https://dev.epicgames.com/documentation/en-us/unreal-engine/environment-query-system-overview-in-unreal-engine), and a [Behavior Tree](https://dev.epicgames.com/documentation/en-us/unreal-engine/behavior-tree-in-unreal-engine---user-guide) Blackboard asset.

#### UI

The Arena Shooter variant has a UI that includes a crosshair, the player's number of kills and number of deaths, and the ammo count for the player's current weapon. The blueprints and assets for the UI are in the `Content/Variant_Shooter/UI` folder.

### Survival Horror Variant

The **Survival Horror** variant features pre-configured lighting and mood setup for a low-light, high-contrast atmosphere.

[![In-game screenshot of the Survival Horror variant](https://dev.epicgames.com/community/api/documentation/image/588ddd76-6040-4a94-ad2c-7187be7ea1a9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/588ddd76-6040-4a94-ad2c-7187be7ea1a9?resizing_type=fit)

#### Lights

The level in the Survival Horror variant is dark and includes a series of lights in different colors to set the tone and to help the player navigate. The blueprint and assets for the lights are in the `Content/Variant_Shooter/Blueprints/Light` folder.

#### Sprint Mechanic

The player character in the Survival Horror variant is able to sprint when the player holds down the sprint button (**Shift** on keyboard, **Left shoulder** or **left thumbstick button** on gamepad). The player character has a stamina bar that depletes when sprinting, and when it is fully depleted, the character stops sprinting.

The logic for the sprint mechanic is included in the horror player character blueprint (**BP\_FP\_Horror**) in the `Content/Variant_Horror/Blueprints` folder, and in the `Content/Variant_Horror/Input` folder.

#### UI

The UI assets for the stamina bar are in the `Content/Variant_Horror/UI` folder.

## Template Contents

All the variants of the First Person template include some basic elements for a first-person experience. The following section details these elements and where to find them in the **Content Browser**.

### Blueprints

The **None** variant of the First Person template include Blueprints for the following assets:

* Player character
* Game mode
* Player controller
* Camera manager

These Blueprints are located in the `Content/FirstPerson/Blueprints` folder. The event graph in each Blueprint includes comments and annotations about what the different node groups do and the logic behind the implementation.

The **Arena Shooter** variant uses the player character, player controller, and game mode in the `Content/Variant_Shooter/Blueprints/FirstPerson` folder.

The **Survival Horror** variant uses the player character and game mode in the `Content/Variant_Horror/Blueprints` folder.

### First Person Character

The first person character includes a full body mesh that is rendered in the first person camera using [First Person Rendering](https://dev.epicgames.com/documentation/en-us/unreal-engine/first-person-rendering). The mesh is visible to the player when they point the camera down, and when the character is moving or holding a gun. The mesh does not render in other camera views.

Assets for the player character are located in the `Content/Characters/Mannequins` folder. Here, you can find the skeletal mesh, materials, textures, animations, and rigs for the character.

### Level

The assets that make up the level geometry for all variants (static meshes, materials, and textures) are located in the `Content/LevelPrototyping` folder.

In the **None** variant of the First Person template, the level, **Lvl\_FirstPerson**, is located in the `Content/FirstPerson` folder.

In the **Arena Shooter** variant, the level, **Lvl\_Shooter**, is located in the `Content/Variant_Shooter` folder. This level includes ramps, platforms, jump pads, enemies, and weapon pickups.

In the **Survival Horror** variant, the level, **Lvl\_Horror**, is located in the `Content/Variant_Horror` folder. This level contains ramps, platforms, automatic doors, and lights.

## Improving your Project

Now that you have a playable level, you can start to import content and make changes to the game. The easiest way to add more content to your level is to drag it in from the **Content Browser**.

For more in-depth instructions on how to populate your Level, see [Level Designer Quick Start](https://dev.epicgames.com/documentation/en-us/unreal-engine/level-designer-quick-start-in-unreal-engine).

## What's Next?

Now that you've gone through the basics of creating a first-person experience, here are some other things you can try:

* Populate your level with content and props from [Quixel Bridge](https://dev.epicgames.com/documentation/en-us/unreal-engine/quixel-bridge-plugin-for-unreal-engine). You can build a variety of indoor and outdoor environments.
* Add some visual effects to your game, like motion blur or vignette, by using [post-processing](https://dev.epicgames.com/documentation/en-us/unreal-engine/post-process-effects-in-unreal-engine).
* For the Arena Shooter variant, [import and configure](https://dev.epicgames.com/documentation/en-us/unreal-engine/fbx-skeletal-mesh-pipeline-in-unreal-engine) a different model for your gun, or choose a different weapon entirely. You can download premade Assets from [Fab](https://www.fab.com) or create your own.
* Create or modify the in-game heads-up display (HUD) with [Unreal Motion Graphics (UMG)](https://dev.epicgames.com/documentation/en-us/unreal-engine/umg-editor-reference-for-unreal-engine) to display information such as player health and ammo count.
* Add or build upon existing AI characters using [State Trees](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-state-tree-in-unreal-engine) and [Behavior Trees](https://dev.epicgames.com/documentation/en-us/unreal-engine/behavior-trees-in-unreal-engine).

**er**: A template of a first person shooter game with the following contents:

* [templates](https://dev.epicgames.com/community/search?query=templates)
* [first person](https://dev.epicgames.com/community/search?query=first%20person)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Creating a First Person Project](/documentation/en-us/unreal-engine/first-person-template-in-unreal-engine?application_version=5.7#creating-a-first-person-project)
* [Template Variants](/documentation/en-us/unreal-engine/first-person-template-in-unreal-engine?application_version=5.7#templatevariants)
* [Arena Shooter Variant](/documentation/en-us/unreal-engine/first-person-template-in-unreal-engine?application_version=5.7#arenashootervariant)
* [Weapons](/documentation/en-us/unreal-engine/first-person-template-in-unreal-engine?application_version=5.7#weapons)
* [Enemies](/documentation/en-us/unreal-engine/first-person-template-in-unreal-engine?application_version=5.7#enemies)
* [UI](/documentation/en-us/unreal-engine/first-person-template-in-unreal-engine?application_version=5.7#ui)
* [Survival Horror Variant](/documentation/en-us/unreal-engine/first-person-template-in-unreal-engine?application_version=5.7#survivalhorrorvariant)
* [Lights](/documentation/en-us/unreal-engine/first-person-template-in-unreal-engine?application_version=5.7#lights)
* [Sprint Mechanic](/documentation/en-us/unreal-engine/first-person-template-in-unreal-engine?application_version=5.7#sprintmechanic)
* [UI](/documentation/en-us/unreal-engine/first-person-template-in-unreal-engine?application_version=5.7#ui-2)
* [Template Contents](/documentation/en-us/unreal-engine/first-person-template-in-unreal-engine?application_version=5.7#template-contents)
* [Blueprints](/documentation/en-us/unreal-engine/first-person-template-in-unreal-engine?application_version=5.7#blueprints)
* [First Person Character](/documentation/en-us/unreal-engine/first-person-template-in-unreal-engine?application_version=5.7#first-person-character)
* [Level](/documentation/en-us/unreal-engine/first-person-template-in-unreal-engine?application_version=5.7#level)
* [Improving your Project](/documentation/en-us/unreal-engine/first-person-template-in-unreal-engine?application_version=5.7#improving-your-project)
* [What's Next?](/documentation/en-us/unreal-engine/first-person-template-in-unreal-engine?application_version=5.7#what-s-next)
