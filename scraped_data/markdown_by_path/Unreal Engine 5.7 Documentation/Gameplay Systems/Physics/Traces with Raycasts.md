<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/traces-with-raycasts-in-unreal-engine?application_version=5.7 -->

# Traces with Raycasts

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
5. [Gameplay Systems](/documentation/en-us/unreal-engine/gameplay-systems-in-unreal-engine "Gameplay Systems")
6. [Physics](/documentation/en-us/unreal-engine/physics-in-unreal-engine "Physics")
7. Traces with Raycasts

# Traces with Raycasts

The landing page for Physics Traces.

![Traces with Raycasts](https://dev.epicgames.com/community/api/documentation/image/5e502f0c-a3da-407c-b442-98e1b5e285b6?resizing_type=fill&width=1920&height=335)

 On this page

There may be instances in your game where you want to determine if the player character is looking at something, and if so, alter the game state in some way (for example, highlight something when a player looks at it). Or maybe you want to determine if an enemy can see the player character, and if so, start shooting or engaging them in some way. You can accomplish both scenarios by using **Traces** (or **Raycasts**) to "shoot" out an invisible ray which will detect geometry between two points and if geometry is hit, return what was hit so that you may then do something with it.

There are different options available when running a Trace. You can run a Trace to check for collision with any Objects where hit Objects are returned, or you can run a Trace by Trace Channel where any Objects hit will return hit information if the Object is set to specifically respond to a specified Trace Channel (which can be set via Collision Settings).

In addition to running traces by Objects or by Trace Channel, you can run your Trace to detect Single hits or Multi hits, where a Single Trace returns a singular hit result and a Multi Trace returns multiple hits resulting from the Trace. With Traces, you can also specify the type of ray that is used: a straight line, a box, a capsule, or a sphere.

## Topics

To learn more about Raycasts using Blueprints, follow the links below:

[![Traces Overview](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/65a218b6-0f69-4bf6-ac57-bae6cd36805b/trace-overview-topic.png)

Traces Overview

Overview of the Unreal Engine 5 tracing system.](/documentation/en-us/unreal-engine/traces-in-unreal-engine---overview)
[![Traces Tutorials](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7af7d5e1-b204-4fc0-b0c5-50adfb5c079e/trace_topic.png)

Traces Tutorials

Guides covering Tracing (Raycasting) in Unreal Engine.](/documentation/en-us/unreal-engine/traces-tutorials-in-unreal-engine)

* [gameplay](https://dev.epicgames.com/community/search?query=gameplay)
* [physics](https://dev.epicgames.com/community/search?query=physics)
* [tracing](https://dev.epicgames.com/community/search?query=tracing)
* [raycast](https://dev.epicgames.com/community/search?query=raycast)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Topics](/documentation/en-us/unreal-engine/traces-with-raycasts-in-unreal-engine?application_version=5.7#topics)
