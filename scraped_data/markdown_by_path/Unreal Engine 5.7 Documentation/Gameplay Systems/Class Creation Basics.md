<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/class-creation-basics-in-unreal-engine?application_version=5.7 -->

# Class Creation Basics

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
6. Class Creation Basics

# Class Creation Basics

Examples showing how to create classes with Blueprints alone, C++ alone, and a combination of C++ and Blueprints.

![Class Creation Basics](https://dev.epicgames.com/community/api/documentation/image/1e9bd150-1cf4-4e99-a1bd-8a11dfdd3d4a?resizing_type=fill&width=1920&height=335)

 On this page

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d54c61fa-60b4-4a9e-8426-ea6e476374c4/lightswitchactor.png)

These examples show how to create a new class using Blueprints only, C++ code only, and a combination of C++ code and Blueprints. The goal is to create new LightSwitch classes with the same properties and behavior using all three workflows, and then add an instance of each new class to the level, so there are three new LightSwitch Actors.

LightSwitch classes are based directly on the Actor class, since their primary requirement is that they can be placed within the level. They contain a PointLightComponent as the root component, and a SphereComponent that is a child of the PointLightComponent. Each LightSwitch class also has a variable called DesiredIntensity, which is used to set the intensity of the PointLightComponent. Finally, the default behavior of the classes is that when the player enters or leaves the SphereComponent, the PointLightComponent's visibility will be toggled.

## Examples

[![Blueprints Only](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1aa32834-7353-42c1-bfd8-17025af11b0c/bp_only_topic.png)

Blueprints Only

Introductory information for gameplay programmers getting started with Unreal Engine.](/documentation/en-us/unreal-engine/blueprints-only-example)
[![C++ Only](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3de3a2ac-7168-47b1-9fd4-0bec8f0b5c02/code_only_topic.png)

C++ Only

Introductory information for gameplay programmers getting started with Unreal Engine.](/documentation/en-us/unreal-engine/cpp-only-example)
[![C++ and Blueprints](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3883cbb2-d19f-43bf-ba7b-5988fdd50561/both_topic.png)

C++ and Blueprints

Introductory information for gameplay programmers getting started with Unreal Engine.](/documentation/en-us/unreal-engine/cpp-and-blueprints-example)

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [programming](https://dev.epicgames.com/community/search?query=programming)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Examples](/documentation/en-us/unreal-engine/class-creation-basics-in-unreal-engine?application_version=5.7#examples)
