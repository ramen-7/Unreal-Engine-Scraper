<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/niagara-lightweight-emitters-overview?application_version=5.7 -->

# Niagara Lightweight Emitters Overview

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
5. [Creating Visual Effects](/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine "Creating Visual Effects")
6. [Niagara Lightweight Emitters](/documentation/en-us/unreal-engine/niagara-lightweight-emitters "Niagara Lightweight Emitters")
7. Niagara Lightweight Emitters Overview

# Niagara Lightweight Emitters Overview

Overview of Niagara's Lightweight Emitters.

![Niagara Lightweight Emitters Overview](https://dev.epicgames.com/community/api/documentation/image/a41cf50f-b16f-4370-a7ec-e5283007963c?resizing_type=fill&width=1920&height=335)

 On this page

## Overview

Unreal Engine 5.4 introduces Niagara **lightweight emitters**. These emitters, also called **stateless emitters**, are optimized to minimize (and in some cases eliminate) the use of tick during the simulation.

In addition, lightweight emitters don’t need to be compiled, which results in a faster workflow and the amount of emitters in a system will have less impact on performance. This means that in most cases a stateless emitter will be significantly more performant than stateful (traditional) emitter.

You add a stateless emitter inside a Niagara System by right clicking inside the System Overview window and selecting **Add stateless emitter** from the menu. Niagara Systems can have both types of emitters working concurrently, but a pure stateless system will be the most performant.

## Improved Performance and Faster Development

The primary motivation for introducing stateless emitters was to reduce Niagara’s memory and CPU cost, and to accelerate development time for VFX artists.

To achieve this, stateless emitters do the following:

* **Reduce Game Thread tick cost** if the Niagara System is fully stateless.
* **Remove the concurrent tick cost** per stateless emitter.
* **Reduce Render Thread cost** when the Niagara System is fully stateless.
* **Reduce memory cost**, as there are no scripts or particle information in memory.
* Removes **performance impact** of **emitter count** and **particle instance count**.
* **Reduce** (and sometimes remove) the need for **compilation**.

## Stateless Emitter Trade-offs

To achieve improved performance, stateless emitters are fixed-function and only have access to the following modules:

* Acceleration Force
* Add Velocity
* Curl Noise / Noise Vector Field
* Drag
* Gravity Force
* Initialize Particle
* Initial Mesh Orientation
* Rotate Around Point
* Scale Color
* Scale Mesh Size
* Scale Mesh Size By Speed
* Scale Sprite Size
* Scale Sprite Size By Speed
* Shape Location
* Solve Velocities And Forces
* Sprite Rotation Rate
* Sub UV Animation

You can adjust the settings for each of the available modules, but cannot create custom modules, scratchpads, or use dynamic inputs. The current feature-set can be expanded via C++ and you can convert a stateless emitter to a stateful, or vice versa, inside your Niagara System.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Overview](/documentation/en-us/unreal-engine/niagara-lightweight-emitters-overview?application_version=5.7#overview)
* [Improved Performance and Faster Development](/documentation/en-us/unreal-engine/niagara-lightweight-emitters-overview?application_version=5.7#improvedperformanceandfasterdevelopment)
* [Stateless Emitter Trade-offs](/documentation/en-us/unreal-engine/niagara-lightweight-emitters-overview?application_version=5.7#statelessemittertrade-offs)
