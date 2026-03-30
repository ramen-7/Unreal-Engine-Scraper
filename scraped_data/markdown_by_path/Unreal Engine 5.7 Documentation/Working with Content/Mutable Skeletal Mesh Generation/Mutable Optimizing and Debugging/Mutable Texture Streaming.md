<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/mutable-texture-streaming-in-unreal-engine?application_version=5.7 -->

# Mutable Texture Streaming

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
5. [Working with Content](/documentation/en-us/unreal-engine/working-with-content-in-unreal-engine "Working with Content")
6. [Mutable Skeletal Mesh Generation](/documentation/en-us/unreal-engine/mutable-skeletal-mesh-generation-in-unreal-engine "Mutable Skeletal Mesh Generation")
7. [Mutable Optimizing and Debugging](/documentation/en-us/unreal-engine/mutable-optimizing-and-debugging-in-unreal-engine "Mutable Optimizing and Debugging")
8. Mutable Texture Streaming

# Mutable Texture Streaming

An overview of Texture Streaming in Mutable.

![Mutable Texture Streaming](https://dev.epicgames.com/community/api/documentation/image/b096b808-d7bf-4228-806c-3a0a39a6f73a?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

Mutable instances can generate their textures progressively. This has the following impact:

* Objects are ready to render much faster, but at a lower quality.
* Objects use less memory because larger texture mipmaps that are not needed won't be generated and won't use CPU or GPU memory.
* Total object generation time is larger, because some work is repeated for every mipmap update.
* There is a visible transition when texture mipmaps are updated, exactly like with the standard Unreal Engine texture streaming.
* Mutable runtime is busier more often, which may delay the updates of other objects.

The general recommendation (and also the default behavior) is to toggle texture streaming on when in-game and toggle texture streaming off when the player is customizing an object, to prevent texture popping on mipmap updates.

Mutable toggles texture streaming for [States](/documentation/en-us/unreal-engine/using-customizable-states-in-mutable-with-unreal-engine) using the **Texture Compression Strategy** set to **None**. This is a heuristic that assumes that uncompressed textures will only be used in Customizable Object States that prioritize low update latency and popping is not allowed, for example while changing the skin color in a lobby.

Additionally, global Mutable texture streaming can be toggled using the cvar `mutable.EnableMutableProgressiveMipStreaming`.

At runtime it can be controlled with the following method: `UCustomizableObjectSystem::SetProgressiveMipStreamingEnabled(bool bIsEnabled)`.

* [landscape](https://dev.epicgames.com/community/search?query=landscape)
* [beta](https://dev.epicgames.com/community/search?query=beta)
* [working with content](https://dev.epicgames.com/community/search?query=working%20with%20content)
* [skeletal mesh](https://dev.epicgames.com/community/search?query=skeletal%20mesh)
* [mutable](https://dev.epicgames.com/community/search?query=mutable)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)
