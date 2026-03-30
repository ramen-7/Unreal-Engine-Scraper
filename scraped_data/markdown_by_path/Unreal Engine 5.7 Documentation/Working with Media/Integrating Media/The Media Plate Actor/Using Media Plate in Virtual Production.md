<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-media-plate-on-virtual-production-stage-in-unreal-engine?application_version=5.7 -->

# Using Media Plate in Virtual Production

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
5. [Working with Media](/documentation/en-us/unreal-engine/working-with-media-in-unreal-engine "Working with Media")
6. [Integrating Media](/documentation/en-us/unreal-engine/integrating-media-in-unreal-engine "Integrating Media")
7. [The Media Plate Actor](/documentation/en-us/unreal-engine/the-media-plate-actor-in-unreal-engine "The Media Plate Actor")
8. Using Media Plate in Virtual Production

# Using Media Plate in Virtual Production

What to be aware of when using Media Plate in Virtual Production setups

![Using Media Plate in Virtual Production](https://dev.epicgames.com/community/api/documentation/image/b6400114-4e35-4afe-ac71-2d1e1bddaf39?resizing_type=fill&width=1920&height=335)

 On this page

The [Media Plate Actor](/documentation/404) is especially useful in clustered rendering setups with large LED displays, where the Actor maximizes the 2D plate or 360 latlong EXR playback performance and quality. The Media Plate Actor can use EXR tiling and mipmaps to balance load on render nodes and improve per-PC bandwidth limitations.

## VP specifics

* To make use of this maximization, we recommend you use an EXR media format, and select a **Sphere** or **Plane** mesh under the [Mesh settings](/documentation/404). These two meshes use optimized streaming, so the media plate only streams the tiles visible to the camera frustum.
* If you have the Virtual Production Utilities plugin enabled, an extra property becomes available in the [Settings for the Media Plate](/documentation/404):
  + Materials > Create Dynamic Material
    You can create a dynamic material, which has any available parameter within the root Material exposed, so you can configure individual parameters.
* When playing large latlong tiled `.exr` files on LED stages, you can experience increased tile requests at the poles. Increased tile requests typically happen on ceiling nDisplay nodes where the IO requirements can jump past the hardware capabilities, which causes stalls or playback stutters.
  + To prevent stalls and playback stutters, you can set the Media Plate Actor to either automatically increase the MIP levels requested (lower resolution), or cap the Media Plate bandwidth EXR tiles requests. You can change these settings in the [EXR Tiles & Mips settings](/documentation/404).

In a clustered rendering setup using nDisplay, we recommend you try to use multiple PCs to help with bandwidth requirements. The more PCs you have, the fewer visible EXR tiles you will get per render node. Leveraging the support for tiles and mips, this should cut the per-PC input/output (IO) requirements. For high resolution EXR playback, for example simultaneous 8K+ latlongs, we also recommend that you have an SSD / NVMe raid configuration that throughputs at least 7-10 GB/sec on all nDisplay PCs.

* [virtual production](https://dev.epicgames.com/community/search?query=virtual%20production)
* [media plate](https://dev.epicgames.com/community/search?query=media%20plate)
* [playing media](https://dev.epicgames.com/community/search?query=playing%20media)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [VP specifics](/documentation/en-us/unreal-engine/using-media-plate-on-virtual-production-stage-in-unreal-engine?application_version=5.7#vpspecifics)
