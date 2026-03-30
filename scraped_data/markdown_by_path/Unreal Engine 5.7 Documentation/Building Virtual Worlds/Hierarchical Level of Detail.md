<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/hierarchical-level-of-detail-in-unreal-engine?application_version=5.7 -->

# Hierarchical Level of Detail

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
6. Hierarchical Level of Detail

# Hierarchical Level of Detail

Information on the Hierarchical Level of Detail system in Unreal Engine

![Hierarchical Level of Detail](https://dev.epicgames.com/community/api/documentation/image/b62bef23-ab1a-4981-a118-f13d9606a03f?resizing_type=fill&width=1920&height=335)

A complex level in Unreal Engine contains hundreds of detailed Static Mesh assets that combine together to build a virtual world. With this level of detail, it can become difficult to load a multi-kilometer level all at once.

The Hierarchical Level of Detail (HLOD) system can be used to organize multiple Static Mesh Actors and combine them into a single proxy mesh and Material at long view distances. This helps reduce the number of Actors that need to be rendered for the scene, which reduces the number draw calls per frame and increases performance. This is especially useful when working with large open worlds.

[![Building Hierarchical Level of Detail Meshes](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5bb58d5e-7301-4ff9-9524-0f685a9503e9/topic-image.png)

Building Hierarchical Level of Detail Meshes

This how to covers how to generate the HLOD meshes for your HLOD enabled Unreal Engine 5 project.](/documentation/en-us/unreal-engine/building-hierarchical-level-of-detail-meshes-in-unreal-engine)
[![Hierarchical Level of Detail Overview](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8ab37834-6703-4668-8c9d-17396aa8e835/hlod_overview_topic.png)

Hierarchical Level of Detail Overview

Overview of the Hierarchical Level of Detail system in Unreal Engine 4](/documentation/en-us/unreal-engine/hierarchical-level-of-detail-overview-in-unreal-engine)
[![Hierarchical Level of Detail Outliner](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6235ae87-0af3-4e3c-ba55-f7980db3a348/topic-image.png)

Hierarchical Level of Detail Outliner

A reference page for the interface elements and properties found in the Hierarchical LOD Outliner.](/documentation/en-us/unreal-engine/hierarchical-level-of-detail-outliner-in-unreal-engine)

* [hlod](https://dev.epicgames.com/community/search?query=hlod)
* [building virtual worlds](https://dev.epicgames.com/community/search?query=building%20virtual%20worlds)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)
