<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/paper-2d-sprite-collision-in-unreal-engine?application_version=5.7 -->

# Sprite Collision

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
5. [Animating Characters and Objects](/documentation/en-us/unreal-engine/animating-characters-and-objects-in-unreal-engine "Animating Characters and Objects")
6. [Paper 2D](/documentation/en-us/unreal-engine/paper-2d-overview-in-unreal-engine "Paper 2D")
7. [Paper 2D Sprites](/documentation/en-us/unreal-engine/how-to-import-and-use-paper-2d-sprites-in-unreal-engine "Paper 2D Sprites")
8. Sprite Collision

# Sprite Collision

Displays and allows editing of the Sprite Collision shapes.

![Sprite Collision](https://dev.epicgames.com/community/api/documentation/image/1aec1f38-c466-4f96-a90d-3b2ee42c7e80?resizing_type=fill&width=1920&height=335)

 On this page

Just like other types of geometry, such as Static Meshes, Skeletal Meshes, etc., **Sprites** can define shapes that are used to calculate collisions with other geometry in the world.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7288e4a7-b080-43a8-a1b3-5fdc19c7b270/collision_shape.png)

## Collision Domain

The method used for calculating collision is defined using the **Sprite Collision Domain** property. There are three
different settings:

| Collision Type | Description |
| --- | --- |
| **None** | No collision geometry is generated; use this for purely decorative sprites. |
| **Use 2D Physics** | This is an *experimental* option to generate collision geometry for use with Box2D. See [2D Collision](/documentation/en-us/unreal-engine/paper-2d-sprite-collision-in-unreal-engine#2dcollision) for more information on the current limitations. |
| **Use 3D Physics** | Collision geometry will be generated for use with PhysX. The 2D collision geometry defined in the sprite will be extruded using the Collision Thickness units deep in the perpendicular axis to make 3D collision geometry. |

## Collision Geometry

The **Geometry Type** setting on collision geometry specifies the type of calculation to use for generating the collision
geometry. The following settings are available:

| Type | Description |
| --- | --- |
| **Source Bounding Box** | Uses the bounding box of the [Source Region](/documentation/en-us/unreal-engine/how-to-import-and-use-paper-2d-sprites-in-unreal-engine) for the Sprite. |
| **Tight Bounding Box** | Generates a tightened bounding box that excludes any fully transparent areas of the Sprite. This results in better collision in most cases. |
| **Shrink Wwrapped** | (*Experimental*) Generates complex geoemetry the conforms to the opaque areas of the Sprite. This results in the most realistic collision, but the added geometry could result in a performance hit. |
| **Fully Custom** | Enables you to specify the geometry used interactively in the viewport. |
| **Diced** | Split up into smaller squares, including only no-empty ones in the final geometry. |

The **Edit Collision** mode displays the collision geometry and lets you adjust it in the viewport, automatically setting the mode to fully custom.

The toolbar buttons can be used to add additional polygons or snap vertices to the pixel grid. New vertices can be added by selecting an edge and **Shift+clicking** and selected vertices can be deleted by pressing **Delete**.

## 2D Collision

There is an initial **experimental** integration of Box2D 2.3.1 and various associated changes to enable 2D physics in the engine. This is a totally unsupported and undocumented prototype, exercise great caution and do not use in production. The current build only includes precompiled libraries of Box2D for Win32 and Win64, so 2D collision will not work on other platforms. Collision detection and response is automatic when the 2D domain is selected in a sprite, but queries like point traces must be separately enabled in the Physics project settings (bEnable2DPhysics option).

The integration supports collision detection and response (including Unreal collision channels/filtering), rigid body simulation, and ray casts. Non-zero extent queries, sweep tests, and overlap tests are not implemented yet. Things like CharacterMovementComponent and MoveComponent with bSweep=true rely on these sorts of queries and do not work correctly yet.

The long term integration strategy is to make it a first class citizen, where the same techniques and knowledge used in 3D scenes will directly apply to 2D scenes; for example, there'll only be one Overlap event, not a separate 2D and 3D one. 3D raycasts are already implemented for Box2D and you can both trace 'in-plane' (gameplay traces within the 2D 'world') or 'perpendicular to plane' (things like the Touch input trace to determine the object under your finger / mouse cursor), providing a proper hit result location and normal as well.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Collision Domain](/documentation/en-us/unreal-engine/paper-2d-sprite-collision-in-unreal-engine?application_version=5.7#collisiondomain)
* [Collision Geometry](/documentation/en-us/unreal-engine/paper-2d-sprite-collision-in-unreal-engine?application_version=5.7#collisiongeometry)
* [2D Collision](/documentation/en-us/unreal-engine/paper-2d-sprite-collision-in-unreal-engine?application_version=5.7#2dcollision)
