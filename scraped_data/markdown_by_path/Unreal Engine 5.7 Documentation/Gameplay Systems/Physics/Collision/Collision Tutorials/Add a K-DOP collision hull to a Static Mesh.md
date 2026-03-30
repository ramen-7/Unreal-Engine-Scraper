<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/add-a-k-dop-collision-hull-to-a-static-mesh-in-unreal-engine?application_version=5.7 -->

# Add a K-DOP collision hull to a Static Mesh

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
7. [Collision](/documentation/en-us/unreal-engine/collision-in-unreal-engine "Collision")
8. [Collision Tutorials](/documentation/en-us/unreal-engine/collision-tutorials-in-unreal-engine "Collision Tutorials")
9. Add a K-DOP collision hull to a Static Mesh

# Add a K-DOP collision hull to a Static Mesh

Content guide to creating and setting up collision geometry.

![Add a K-DOP collision hull to a Static Mesh](https://dev.epicgames.com/community/api/documentation/image/9a0138c4-6add-4f5a-aa36-cfdc41f2b247?resizing_type=fill&width=1920&height=335)

 On this page

### Steps

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b2daad4b-624d-41b4-bef1-613c1b297249/colref_collisionmenu_kdop.png)

There are a series of menu options in the **Static Mesh Editor** under the **Collision** menu entry, named *##DOP*, these are the **K-DOP** simple collision generators. **K-DOP** is a type of bounding volume, which stands for *K discrete oriented polytope* (where K is the number of axis aligned planes). Basically it takes K axis-aligned planes and pushes them as close to the mesh as it can. The resulting shape is used as a collision hull. In the **Static Mesh Editor** K can be:

* **10** - Box with 4 edges beveled - you can choose X- Y- or Z-aligned edges.
* **18** - Box with all edges beveled.
* **26** - Box with all edges and corners beveled.

See below for an example. This tool is quite handy for packages full of pipes, pillars, and railings:

![kdop_sizes.jpg](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c0943730-fdad-4c5e-8dc3-cdc7cff298fa/kdop_sizes.jpg)

* [collision](https://dev.epicgames.com/community/search?query=collision)
* [physics](https://dev.epicgames.com/community/search?query=physics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/add-a-k-dop-collision-hull-to-a-static-mesh-in-unreal-engine?application_version=5.7#steps)
