<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/introduction-to-blueprints-visual-scripting-in-unreal-engine?application_version=5.7 -->

# Introduction to Blueprints

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
6. Introduction to Blueprints

# Introduction to Blueprints

Introduction to visual scripting with Blueprints.

![Introduction to Blueprints](https://dev.epicgames.com/community/api/documentation/image/c5ce1cf3-e0eb-46d2-99ca-5bc3f058f3e5?resizing_type=fill&width=1920&height=335)

 On this page

The **Blueprint Visual Scripting** system in Unreal Engine is a visual programming language that uses a node-based interface to create gameplay elements. The node-based workflow provides designers with a wide range of scripting concepts and tools that are generally only available to programmers. In addition, Blueprint-specific markup available in Unreal Engine's C++ implementation provides programmers with a way to create baseline systems that designers can extend.

As with many common scripting languages, you can use the system to define object-oriented (OO) classes or objects in the engine. The system, along with the objects you define, are often referred to as just "Blueprints".

### Prerequisite Knowledge

We recommend understanding the following topics before continuing with the page:

* [Unreal Engine Terminology](/documentation/en-us/unreal-engine/unreal-engine-terminology)
* [Levels in Unreal Engine](/documentation/en-us/unreal-engine/levels-in-unreal-engine)

## How Do Blueprints Work?

Blueprints work by using graphs of nodes for various purposes, such as object construction, individual functions, and general gameplay events. You can create gameplay elements by connecting nodes of events, functions, and variables with wires.

## Commonly Used Blueprint Types

The most common Blueprint types are **Level Blueprints** and **Blueprint Classes**.

For a full list of types, see [Types of Blueprints](/documentation/en-us/unreal-engine/types-of-blueprints-in-unreal-engine).

## Level Blueprint

A Level Blueprint contains logic for level-specific events within maps. Each level has a Level Blueprint, which can:

* Reference and manipulate actors within the level
* Control cinematics using [level sequence actors](/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview)
* Manage level streaming

A Level Blueprint can also interact with Blueprint Classes placed in the level, such as reading variables and triggering custom events. To learn more, see [Level Blueprints](/documentation/en-us/unreal-engine/level-blueprint-in-unreal-engine).

## Blueprint Class

A Blueprint Class defines a new class or type of actor that you can place into maps as instances. Editing a Blueprint Class used throughout a project will update every instance of it.

Blueprint Classes are ideal for making interactive assets such as doors, switches, collectible items, and destructible scenery. To learn more, see [Blueprint Class](/documentation/en-us/unreal-engine/blueprint-class-assets-in-unreal-engine).

## What Else Can Blueprints Do?

The following topics are a few examples you can accomplish with the Blueprint system.

## Create Customizable Prefabs with Construction Scripts

![Construction Script](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/51bdfc25-2f94-42a2-9e56-7009f08cd0ff/construction-script-ue5.png)

The [Construction Script](/documentation/en-us/unreal-engine/construction-script-in-unreal-engine) is a type of graph within a Blueprint Class that executes when an actor is placed or updated in the editor, but not during gameplay. It helps create customizable props that improve environment artists' workflows. For example, a light fixture that automatically updates its material to match the color and brightness of its point light component or a Blueprint that randomly scatters foliage meshes over an area.

In the [Content Examples](/documentation/en-us/unreal-engine/content-examples-sample-project-for-unreal-engine) maps, the demo rooms that contain each example (pictured above) are a single Blueprint made up of many components. The Blueprint's Construction Script creates and arranges the various static meshes and lights according to parameters exposed in the Blueprint's **Details** panel. With each Content Example map, we can drop in the demo room Blueprint, set values for the length, height, and number of rooms to generate, and have a complete set of rooms ready in moments.

## Create A Playable Game Character

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cf68e43f-d2ba-4aee-b1e4-8da70d33e2d0/game_characters.png)

[Pawns](/documentation/en-us/unreal-engine/pawn-in-unreal-engine), a type of Blueprint Class, are the physical representation of actors players can control. With a pawn class, you can assemble every element you need to create a playable [Character](/documentation/en-us/unreal-engine/characters-in-unreal-engine). You can manipulate [camera](/documentation/en-us/unreal-engine/cameras-in-unreal-engine) behavior, set up input events for mouse, controller, and touch screens, and create an animation Blueprint asset for handling skeletal mesh animations.

A character Blueprint contains a character component that has much of the behavior needed for moving around, jumping, swimming, and falling built-in. To finalize the setup, you must add some input events in accordance with how you want players to control your character.

To learn more, see [Setting Up Character Movement](/documentation/en-us/unreal-engine/setting-up-character-movement).

## Create A HUD

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fcd31caa-085f-46e0-803d-3f56b9e2552b/create_huds.png)

You can use Blueprints to create a game's HUD (heads-up display). The setup is similar to Blueprint Classes in that it can contain event sequences and variables but is assigned to your project's GameMode asset instead of directly to a level.

You can set up a HUD to read variables from other Blueprints, display a health bar, update a score value, display objective markers, and more. It is also possible to use the HUD to add hit-boxes for elements like buttons you can click on.

While possible with Blueprint, the [Unreal Motion Graphics](/documentation/en-us/unreal-engine/umg-editor-reference-for-unreal-engine) system is a more designer-friendly way of laying out a UI. The system is based on Blueprint Visual Scripting.

## Blueprint Editors and Graphs

The **Blueprint Editor** is the user interface you use to construct Blueprint elements to build your visual script.

![Blueprint Editor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9cf4ae24-21fb-4dbc-a520-8827758e52f7/blueprint-editor-ue5.png)

The Blueprint Editor's UI changes based on the type of Blueprint chosen. The core feature of most **Blueprint Editors** is the **Event Graph** tab for laying out the network of your Blueprint.

To learn more about the interface, see [Blueprint Editor](/documentation/en-us/unreal-engine/user-interface-reference-for-the-blueprints-visual-scripting-editor-in-unreal-engine).

## Getting Started

You can continue to learn the basics of visual scripting in Unreal Engine with the following pages.

[![Basic Scripting with Blueprints](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/94769a06-72c1-495c-b7f4-b76ce0ce0643/using_interface_topic.png)

Basic Scripting with Blueprints

Get a general overview of the variables and execution flow of the Blueprints visual scripting system.](/documentation/en-us/unreal-engine/basic-scripting-with-blueprints-in-unreal-engine)
[![Blueprints Visual Scripting Overview](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c59ab86f-c134-4021-9b93-80e79d2a6e36/blueprint_topic.png)

Blueprints Visual Scripting Overview

Learn about Unreal Engine's Blueprint Scripting System.](/documentation/en-us/unreal-engine/overview-of-blueprints-visual-scripting-in-unreal-engine)
[![Blueprints Quick Start Guide](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/958201ab-7025-4afc-b577-cb621a268545/quickstart.png)

Blueprints Quick Start Guide

Get up and running by creating your first Blueprint.](/documentation/en-us/unreal-engine/quick-start-guide-for-blueprints-visual-scripting-in-unreal-engine)

## Blueprint Samples and Tutorials

Additional hands-on resources you can use to learn more about the Blueprint system.

* [Sample Projects](/documentation/en-us/unreal-engine/samples-and-tutorials-for-unreal-engine)
* [Blueprint Tutorials](/documentation/en-us/unreal-engine/blueprint-workflows-in-unreal-engine)

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [visual scripting](https://dev.epicgames.com/community/search?query=visual%20scripting)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisite Knowledge](/documentation/en-us/unreal-engine/introduction-to-blueprints-visual-scripting-in-unreal-engine?application_version=5.7#prerequisiteknowledge)
* [How Do Blueprints Work?](/documentation/en-us/unreal-engine/introduction-to-blueprints-visual-scripting-in-unreal-engine?application_version=5.7#howdoblueprintswork?)
* [Commonly Used Blueprint Types](/documentation/en-us/unreal-engine/introduction-to-blueprints-visual-scripting-in-unreal-engine?application_version=5.7#commonlyusedblueprinttypes)
* [Level Blueprint](/documentation/en-us/unreal-engine/introduction-to-blueprints-visual-scripting-in-unreal-engine?application_version=5.7#levelblueprint)
* [Blueprint Class](/documentation/en-us/unreal-engine/introduction-to-blueprints-visual-scripting-in-unreal-engine?application_version=5.7#blueprintclass)
* [What Else Can Blueprints Do?](/documentation/en-us/unreal-engine/introduction-to-blueprints-visual-scripting-in-unreal-engine?application_version=5.7#whatelsecanblueprintsdo?)
* [Create Customizable Prefabs with Construction Scripts](/documentation/en-us/unreal-engine/introduction-to-blueprints-visual-scripting-in-unreal-engine?application_version=5.7#createcustomizableprefabswithconstructionscripts)
* [Create A Playable Game Character](/documentation/en-us/unreal-engine/introduction-to-blueprints-visual-scripting-in-unreal-engine?application_version=5.7#createaplayablegamecharacter)
* [Create A HUD](/documentation/en-us/unreal-engine/introduction-to-blueprints-visual-scripting-in-unreal-engine?application_version=5.7#createahud)
* [Blueprint Editors and Graphs](/documentation/en-us/unreal-engine/introduction-to-blueprints-visual-scripting-in-unreal-engine?application_version=5.7#blueprinteditorsandgraphs)
* [Getting Started](/documentation/en-us/unreal-engine/introduction-to-blueprints-visual-scripting-in-unreal-engine?application_version=5.7#gettingstarted)
* [Blueprint Samples and Tutorials](/documentation/en-us/unreal-engine/introduction-to-blueprints-visual-scripting-in-unreal-engine?application_version=5.7#blueprintsamplesandtutorials)
