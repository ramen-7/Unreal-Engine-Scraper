<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprint-class-assets-in-unreal-engine?application_version=5.7 -->

# Blueprint Class

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
5. [Blueprints Visual Scripting](/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine "Blueprints Visual Scripting")
6. [Specialized Blueprint Node Groups](/documentation/en-us/unreal-engine/specialized-blueprint-visual-scripting-node-groups-in-unreal-engine "Specialized Blueprint Node Groups")
7. [Types of Blueprints](/documentation/en-us/unreal-engine/types-of-blueprints-in-unreal-engine "Types of Blueprints")
8. Blueprint Class

# Blueprint Class

These define a new class or type of Actor which can then be placed as instances that behave like any other type of Actor.

![Blueprint Class](https://dev.epicgames.com/community/api/documentation/image/bd914bd2-52e6-4926-844b-ed56b093a736?resizing_type=fill&width=1920&height=335)

 On this page

A **Blueprint Class**, often shortened as **Blueprint**, is an asset that allows content creators to easily add functionality on top of existing gameplay classes.
Blueprints are created inside of Unreal Editor visually, instead of by typing code, and saved as assets in a content package.
These essentially define a new class or type of Actor which can then be placed into maps as instances that behave like any other type of Actor.

## Parent Classes

There are several different types of Blueprints that you can create, however before doing so you will need to specify the **Parent Class** in which the Blueprint will be based.
Selecting a Parent Class allows you to inherit properties from the Parent to use in the Blueprint you are creating.

Below are the most common Parent Classes used when creating a new Blueprint:

| Class Type | Description |
| --- | --- |
| **Actor** | An Actor is an object that can be placed or spawned in the world. |
| **Pawn** | A Pawn is an Actor that can be "possessed" and receive input from a Controller. |
| **Character** | A Character is a Pawn that includes the ability to walk, run, jump, and more. |
| **PlayerController** | A Player Controller is an Actor responsible for controlling a Pawn used by the player. |
| **Game Mode** | A Game Mode defines the game being played, its rules, scoring, and other faces of the game type. |

While the above are the most common, all existing classes can be used as the Parent Class for a new Blueprint (even other Blueprint Classes).

For example, say you created an **Actor Blueprint** called *Animals* and in it provided some script that all animals share such as *Hunger*, *Thirst*, *Energy*, or whatever script you wanted. Then you created another Blueprint called *Dogs* and selected your *Animals* Blueprint Class as the Parent Class; you can then provide specific functionality that applies to only dogs within the *Dogs* Blueprint such as *Play Fetch* or *Roll Over* while inheriting the functionality that all animals share from the *Animals* Blueprint.

Depending upon the method used to [create a Blueprint Class](/documentation/en-us/unreal-engine/creating-blueprint-classes-in-unreal-engine), a Parent Class may already be assigned upon creation.

## Working with Blueprint Classes

Refer to the sections below for information on working with **Blueprint Classes**:

[![Blueprint Editor Blueprint Class UI](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4c6d77cf-cfc2-480e-838d-90710f2b2128/class_blueprint_test_image.png)

Blueprint Editor Blueprint Class UI

A breakdown of the UI elements of the Blueprint Editor when working on Blueprint Classes.](/documentation/en-us/unreal-engine/blueprints-visual-scripting-user-interface-for-blueprint-classes-in-unreal-engine)
[![Creating Blueprint Classes](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f166d576-dc1a-4703-a916-aecf3941249d/placeholder_topic.png)

Creating Blueprint Classes

A how-to guide on ways to create new Blueprint classes](/documentation/en-us/unreal-engine/creating-blueprint-classes-in-unreal-engine)
[![Blueprint Editor Reference](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6522008c-d13e-46b2-b539-c4c6a16880af/macro_blueprint.png)

Blueprint Editor Reference

The Blueprint Editor Reference page outlines the Blueprint Editor's Interface elements and its basic usage instructions.](/documentation/en-us/unreal-engine/user-interface-reference-for-the-blueprints-visual-scripting-editor-in-unreal-engine)

## Data-Only Blueprint

A **Data-Only Blueprint** is a Blueprint Class that contains only the code (in the form of node graphs), variables, and components
inherited from its parent. These allow those inherited properties to be tweaked and modified, but no new elements can be added.
These are essentially a replacement for archetypes and can be used to allow designers to tweak properties or set items with variations.

Data-Only Blueprint are edited in a compact property editor, but can also be "converted" to full Blueprints by simply adding code,
variables, or components using the full **Blueprint Editor**.

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [class blueprints](https://dev.epicgames.com/community/search?query=class%20blueprints)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Parent Classes](/documentation/en-us/unreal-engine/blueprint-class-assets-in-unreal-engine?application_version=5.7#parentclasses)
* [Working with Blueprint Classes](/documentation/en-us/unreal-engine/blueprint-class-assets-in-unreal-engine?application_version=5.7#workingwithblueprintclasses)
* [Data-Only Blueprint](/documentation/en-us/unreal-engine/blueprint-class-assets-in-unreal-engine?application_version=5.7#data-onlyblueprint)
