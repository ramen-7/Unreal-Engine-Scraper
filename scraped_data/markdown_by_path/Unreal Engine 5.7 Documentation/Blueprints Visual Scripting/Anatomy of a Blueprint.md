<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/anatomy-of-a-blueprint-in-unreal-engine?application_version=5.7 -->

# Anatomy of a Blueprint

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
6. Anatomy of a Blueprint

# Anatomy of a Blueprint

The User Guide is the go-to source to learn the different parts of Blueprints and nodes that are available to use within Blueprint graphs.

![Anatomy of a Blueprint](https://dev.epicgames.com/community/api/documentation/image/92c76619-4bb5-40e2-b215-35d144079f4a?resizing_type=fill&width=1920&height=335)

 On this page

## Blueprint Classes

A **Blueprint Class**, often shortened as **Blueprint**, is an asset that allows content creators to easily add functionality on top of existing gameplay classes.
Blueprints are created inside of Unreal Editor visually, instead of by typing code, and saved as assets in a content package.
These essentially define a new class or type of Actor which can then be placed into maps as instances that behave like any other type of Actor.

## Components

**Blueprints** do not always need to contain scripted behavior. For example, a lightpost in your level may not be interactive, and would just need a mesh to represent the post and a light.
Using **Components** to build up reusable Blueprints would accelerate your level design process. Of course, you could then work with those Components in a graph to allow your players
to interact with the lights or have a time-of-day system adjust them accordingly.

## Graphs

**Graphs** contain the design-time and game-time behavior of your Blueprints. The **Construction Script** runs following the Components list when an instance of a Blueprint Class is created,
enabling you to dynamically adjust the look and feel of the new Object or Actor.

The **EventGraph** of a Blueprint contains a node graph that uses events and function calls to perform actions in response to gameplay events associated with the Blueprint. This is used to add functionality that is common to all instances of a Blueprint. This is where interactivity and dynamic responses are setup. For example, a light Blueprint could respond to a damage event by turning off its `LightComponent` and changing the material used by its mesh. This would automatically provide this behavior to all instances of the light Blueprint.

[![EventGraph](images/static/document_list/empty_thumbnail.svg)

EventGraph

Uses events and function calls to perform actions in response to Blueprint events.](/documentation/en-us/unreal-engine/event-graph-in-unreal-engine)
[![Graphs](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/392f92e4-0ecd-419d-88e2-b3600b85e054/graph_topic.png)

Graphs

Node graph that uses events and function calls to perform actions in response to events associated with the Blueprint.](/documentation/en-us/unreal-engine/graphs-in-unreal-engine)

## Organizing and Reusing Script

As you create more script in your Blueprints, you may find there are certain sections of script you frequently reuse. **Functions** and **Macros** both enable you to reuse sections of script,
although each method has different strengths and use cases.
For more on the key differences between Functions and Macros, see the [Blueprint Best Practices guide](/documentation/en-us/unreal-engine/blueprint-best-practices-in-unreal-engine).

You can also collapse sections of your Graph into nested Graphs for organization.

[![Function Calls](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0785b1a6-efb4-458d-ade0-ca990d8c637c/functions.png)

Function Calls

Nodes that execute both code-defined and user-defined functions of a target Actor or Object.](/documentation/en-us/unreal-engine/function-calls-in-unreal-engine)



[![Using Macro Libraries](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c7652bfb-b642-4f92-8369-33585a04ed49/placeholder_topic.png)

Using Macro Libraries

Macros inside a Macro Library are used to increase the health and scale of an Actor.](/documentation/en-us/unreal-engine/using-macro-libraries-in-unreal-engine)

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [programming](https://dev.epicgames.com/community/search?query=programming)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Blueprint Classes](/documentation/en-us/unreal-engine/anatomy-of-a-blueprint-in-unreal-engine?application_version=5.7#blueprintclasses)
* [Components](/documentation/en-us/unreal-engine/anatomy-of-a-blueprint-in-unreal-engine?application_version=5.7#components)
* [Graphs](/documentation/en-us/unreal-engine/anatomy-of-a-blueprint-in-unreal-engine?application_version=5.7#graphs)
* [Organizing and Reusing Script](/documentation/en-us/unreal-engine/anatomy-of-a-blueprint-in-unreal-engine?application_version=5.7#organizingandreusingscript)
