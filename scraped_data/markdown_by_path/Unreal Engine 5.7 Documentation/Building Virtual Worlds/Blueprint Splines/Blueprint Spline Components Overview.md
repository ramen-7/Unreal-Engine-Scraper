<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprint-spline-components-overview-in-unreal-engine?application_version=5.7 -->

# Blueprint Spline Components Overview

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
6. [Blueprint Splines](/documentation/en-us/unreal-engine/blueprint-splines-in-unreal-engine "Blueprint Splines")
7. Blueprint Spline Components Overview

# Blueprint Spline Components Overview

An overview of how to use the Blueprint Spline Components and Blueprint Spline Mesh Components.

![Blueprint Spline Components Overview](https://dev.epicgames.com/community/api/documentation/image/90c0dedc-1023-4d31-8743-13c556ed4e73?resizing_type=fill&width=1920&height=335)

At their core, a **Blueprint Spline Component** is just a path for you to define and use positional data. You can use it to move **Actors** (or other **Components**) around the world, or place a series of **Actors** (or other **Components**) along the spline. They are fully editable in the Blueprint Viewport and in the Level Editor, with the ability to add/remove/duplicate Spline Points, change their tangent types, and even animate them on tick. Further, they are also editable using the **Blueprint Construction Script**, taking in edits made in the Blueprint Viewport or Level Editor, and modifying them further.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4d1b2a33-d9b0-40a4-b69e-7c0a214fae51/bpsc_1.png)

**Blueprint Spline Mesh Components** have a completely different use case. These deform a single **Static Mesh** along a two point spline. You cannot add more Spline Points to a Blueprint Spline Mesh Component, but the two points are completely controllable through Blueprints.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/92d68743-95b5-43db-980a-f6bff03d0a9f/bpsmc_1.png)

While their use cases are very different, they share the same procedures for adding them to a Blueprint, and use the same editing tools.

* [splines](https://dev.epicgames.com/community/search?query=splines)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)
