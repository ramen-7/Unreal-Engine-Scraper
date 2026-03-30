<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/level-streaming-in-unreal-engine?application_version=5.7 -->

# Level Streaming

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
6. Level Streaming

# Level Streaming

Asynchronously loading and unloading levels during play to decrease memory usage and create seamless worlds.

![Level Streaming](https://dev.epicgames.com/community/api/documentation/image/4fd9365e-45f0-40c0-ba57-a75002d374c8?resizing_type=fill&width=1920&height=335)

 On this page

The Level Streaming feature makes it possible to load and unload map files into memory as well as toggle their visibility during play. This makes it possible to have worlds broken up
into smaller chunks so that only the relevant parts of the world are taking up resources and being rendered at any point. If done properly, this allows for the creation of very
large, seamless games that can make the player feel as if they are playing within a world that dwarfs them in size.

[![Level Streaming Overview](images/static/document_list/empty_thumbnail.svg)

Level Streaming Overview](/documentation/en-us/unreal-engine/level-streaming-overview-in-unreal-engine)
[![Level Streaming Volumes Reference](images/static/document_list/empty_thumbnail.svg)

Level Streaming Volumes Reference](/documentation/en-us/unreal-engine/level-streaming-volumes-reference-in-unreal-engine)
[![Loading and Unloading Levels using Blueprints](images/static/document_list/empty_thumbnail.svg)

Loading and Unloading Levels using Blueprints](/documentation/en-us/unreal-engine/loading-and-unloading-levels-using-blueprints-in-unreal-engine)
[![Loading and Unloading Levels using C++](images/static/document_list/empty_thumbnail.svg)

Loading and Unloading Levels using C++](/documentation/en-us/unreal-engine/loading-and-unloading-levels-using-cplusplus-in-unreal-engine)
[![World Composition](images/static/document_list/empty_thumbnail.svg)

World Composition](/documentation/en-us/unreal-engine/world-composition-in-unreal-engine)
[![Level Streaming using Volumes](images/static/document_list/empty_thumbnail.svg)

Level Streaming using Volumes](/documentation/en-us/unreal-engine/level-streaming-using-volumes-in-unreal-engine)

## World Composition

World Composition is a specific form of level streaming used to create large worlds. Levels are arranged in a planar grid, and streamed in as the player approaches them.

[![World Composition](images/static/document_list/empty_thumbnail.svg)

World Composition](/documentation/en-us/unreal-engine/world-composition-in-unreal-engine)


World Composition is a legacy system used for level streaming. It is recommended to use [World Partition](/documentation/en-us/unreal-engine/world-partition-in-unreal-engine) for level streaming in projects using Unreal Engine 5.0 or later.

* [level streaming](https://dev.epicgames.com/community/search?query=level%20streaming)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [World Composition](/documentation/en-us/unreal-engine/level-streaming-in-unreal-engine?application_version=5.7#worldcomposition)
