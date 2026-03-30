<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/dataflow-overview?application_version=5.7 -->

# Dataflow Overview

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
7. [Physics Tools](/documentation/en-us/unreal-engine/physics-tools "Physics Tools")
8. [Dataflow Graph](/documentation/en-us/unreal-engine/dataflow-graph "Dataflow Graph")
9. Dataflow Overview

# Dataflow Overview

Overview of the Dataflow graph system in Unreal Engine.

![Dataflow Overview](https://dev.epicgames.com/community/api/documentation/image/d4fcf00e-84f6-45ee-be45-7f6babdc38f3?resizing_type=fill&width=1920&height=335)

 On this page

## Introduction

![Dataflow graph system](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/63404a48-5fb8-458b-a05b-1a11427143ea/dataflow-system-benefits.png)

The **Dataflow Graph** system is a **node-based procedural asset generation environment** inside the Unreal Engine editor.

Dataflow exists as an asset in the **Content Browser** and contains a node graph that produces a specific asset after it is evaluated.

Dataflow is implemented as a **dependency-based node graph** where changes to a node trigger reevaluation of its downstream dependencies. Each node in the graph is designed to take one or more inputs, process the data, and produce one or more outputs, which are then passed to the next dependent node.

## System Benefits

![Captain Roux](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/03e682d9-d7e5-4645-9858-09254eb0cb49/roux-talisman-bridge.jpg)

Dataflow was created to **improve iteration times** when creating certain asset types in the engine. The same Dataflow graph can be **used by multiple assets** and the graph itself can produce different results depending on the inputs given by the source asset.

Dataflow is a **general-purpose system** that can be adapted to various physics asset types, such as **Chaos Cloth**, **Chaos Flesh**, and **Geometry Collection fracturing**.

Dataflow is also **designed to be extensible** by developers using C++. Developers can further adapt the system to accommodate their specific needs.

## Dataflow vs traditional workflows in Unreal Engine

![Workflow differences](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fb64a46c-7c1e-466f-83b8-fdd998a994ab/dataflow-workflow.png)

The Dataflow Graph system differs from traditional workflows in the following ways:

**Traditional workflow**:

* **Generally destructive workflow**: When creating the asset, the changes are permanent and cannot be easily reversed. This increases iteration time and limits exploration.
* **Manual workflow**: The developer has to go through the workflow manually to produce different assets of the same type.

**Dataflow workflow**:

* **Procedural, non-destructive workflow**: The Dataflow nodes can be modified inside the graph and the results are reflected instantly. All of the steps in the graph can be reverted or skipped if desired.
* **Automatic workflow**: The Developer can automate the workflow to process thousands of assets automatically.
* **Modular workflow**: The same Dataflow graph can be used with multiple assets, each providing different inputs and generating different results.
* **Flexible workflow**: Developers can easily connect and disconnect different nodes to apply different effects and can see the results instantly.

## Extensible and Battle Tested

![Lego Fortnite](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6daf4fb7-d801-40bd-ba78-0f8754f7d217/lego-fortnite.png)

The Dataflow Graph system was **designed with extensibility** in mind. Developers can create **custom Dataflow nodes with C++** to extend the system. Dataflow can also be used to fully automate creation of specific types of assets, such as clothing simulation and Geometry Collection fracturing.

Dataflow was designed for and tested in Lego Fortnite. The system has been tested in production and will continue to improve in future versions of Unreal Engine.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Introduction](/documentation/en-us/unreal-engine/dataflow-overview?application_version=5.7#introduction)
* [System Benefits](/documentation/en-us/unreal-engine/dataflow-overview?application_version=5.7#systembenefits)
* [Dataflow vs traditional workflows in Unreal Engine](/documentation/en-us/unreal-engine/dataflow-overview?application_version=5.7#dataflowvstraditionalworkflowsinunrealengine)
* [Extensible and Battle Tested](/documentation/en-us/unreal-engine/dataflow-overview?application_version=5.7#extensibleandbattletested)
