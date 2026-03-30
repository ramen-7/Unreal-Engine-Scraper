<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-targeting-system-in-unreal-engine?application_version=5.7 -->

# Gameplay Targeting System

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
6. Gameplay Targeting System

# Gameplay Targeting System

An overview of the Gameplay Targeting System plugin framework in Unreal Engine.

![Gameplay Targeting System](https://dev.epicgames.com/community/api/documentation/image/1df87364-03b6-431a-9c75-e95fe72bc9c6?resizing_type=fill&width=1920&height=335)

 On this page

# Gameplay Targeting System

The [Gameplay Targeting System](/documentation/en-us/unreal-engine/gameplay-targeting-system-in-unreal-engine) is a way to create data-driven targeting requests. It expands on the [Gameplay Ability System Plugin](/documentation/en-us/unreal-engine/gameplay-ability-system-for-unreal-engine), but could be used outside of the feature.

You can enable the Targeting System from the Editor by navigating to **Edit** > **Plugins** > **Gameplay** > **Gameplay Abilities** > **Targeting System**.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2f2bff20-11f3-4f34-88f4-124d8f31bf2d/enableplugin.png)

Setting up the Targeting System Plugin.

### Data and Design

The Targeting System uses a **Targeting Preset**. This Targeting Preset is a data asset that defines a set of **Targeting Tasks** that are run from top to bottom for an executed targeting request.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9fbef684-a4d8-483a-a0b4-71992492dc70/targetingpreset.png)

The TP\_Knockback\_Pistol is a targeting preset set up with a Trace targeting task and Filter by the Actor class targeting task.

A feature of targeting presets is that each task supports inline property editing. You can define reusable targeting tasks and presets that set up how the tasks behave without defining a `UAsset` for each one.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/34494f59-1d49-4ef8-a9e6-6079edb2fa60/targettraceselect.png)

Between the two images above, the Trace Types and the Required Actor Classes are different. This is done in the same targeting preset without having to pick different targeting tasks.

##### TargetingTask

A [**Targeting Task**](/documentation/en-us/unreal-engine/gameplay-targeting-system-reference-in-unreal-engine#targetingtask) is a small unit operation meant to perform a desired action. Targeting Tasks can be generally thought about in 3 categories, [Selection](/documentation/en-us/unreal-engine/gameplay-targeting-system-reference-in-unreal-engine#selection), [Filtering](/documentation/en-us/unreal-engine/gameplay-targeting-system-reference-in-unreal-engine#filtering),and [Sorting](/documentation/en-us/unreal-engine/gameplay-targeting-system-reference-in-unreal-engine#sorting).

Targeting tasks have Blueprint support. Depending on how you engineered your tasks, it can be as simple as setting up [Class default properties](/documentation/en-us/unreal-engine/blueprint-editor-defaults-tab) to handling [Blueprint callable events](/documentation/en-us/unreal-engine/exposing-gameplay-elements-to-blueprints-visual-scripting-in-unreal-engine).

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7efa7e6a-09d1-464a-b64c-0a7eafb2ee40/tasktypes.png)

Example: The **Knockback Pistol Trace** task is set up with two overridable events to calculate the source location and the direction of the trace. In this example, if you look at the Blueprint code you'll see it gets the pawn and calls a function to get the camera location and camera direction.

##### Immediate Targeting Requests

[Immediate Targeting Requests](/documentation/en-us/unreal-engine/gameplay-targeting-system-reference-in-unreal-engine#targetingimmediatetaskdata) are performed by calling the `UTargetingSubsystem::ExecuteTargetingRequest` function. The Targeting Request is based on a `UTargetingPreset` Object and is executed immediately, therefore blocking the Game Thread until it is completed.

##### Async Targeting Requests

[Async Targeting Requests](/documentation/en-us/unreal-engine/gameplay-targeting-system-reference-in-unreal-engine#targetingasynctaskdata) are performed by calling the `UTargetingSubsystem::StartAsyncTargetingRequest` function. The Targeting request is based on a `UTargetingPreset` Object and starts immediately, however, it may not block the Game Thread until it is completed.

These requests are useful when a Targeting Task may need to wait for a slow operation (for example, waiting for the server to authenticate a target) or for a gameplay event to occur before targeting can be completed.

All Targeting Tasks defined in the GameplayTargetingSystem Plugin will provide implementations for both Immediate and Asynchronous targeting requests, however, the game code is not enforced to implement both if the game does not use the async functionality.

##### Async Action - Perform Targeting / Perform Filtering

**UAsyncAction\_PerformTargeting** provides generic Blueprint support for starting an Async Targeting Request or Filtering Action.

## Debugging

For a complete list of debug console commands and descriptions, see the [Gameplay Targeting Debugging](/documentation/en-us/unreal-engine/gameplay-targeting-system-debugging-in-unreal-engine) documentation.

## Developer Reference

For an in-depth Engineering reference guide, see the [Gameplay Targeting Plugin Reference](/documentation/en-us/unreal-engine/gameplay-targeting-system-reference-in-unreal-engine) documentation.

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [programming](https://dev.epicgames.com/community/search?query=programming)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Gameplay Targeting System](/documentation/en-us/unreal-engine/gameplay-targeting-system-in-unreal-engine?application_version=5.7#gameplaytargetingsystem)
* [Data and Design](/documentation/en-us/unreal-engine/gameplay-targeting-system-in-unreal-engine?application_version=5.7#dataanddesign)
* [TargetingTask](/documentation/en-us/unreal-engine/gameplay-targeting-system-in-unreal-engine?application_version=5.7#targetingtask)
* [Immediate Targeting Requests](/documentation/en-us/unreal-engine/gameplay-targeting-system-in-unreal-engine?application_version=5.7#immediatetargetingrequests)
* [Async Targeting Requests](/documentation/en-us/unreal-engine/gameplay-targeting-system-in-unreal-engine?application_version=5.7#asynctargetingrequests)
* [Async Action - Perform Targeting / Perform Filtering](/documentation/en-us/unreal-engine/gameplay-targeting-system-in-unreal-engine?application_version=5.7#asyncaction-performtargeting/performfiltering)
* [Debugging](/documentation/en-us/unreal-engine/gameplay-targeting-system-in-unreal-engine?application_version=5.7#debugging)
* [Developer Reference](/documentation/en-us/unreal-engine/gameplay-targeting-system-in-unreal-engine?application_version=5.7#developerreference)
