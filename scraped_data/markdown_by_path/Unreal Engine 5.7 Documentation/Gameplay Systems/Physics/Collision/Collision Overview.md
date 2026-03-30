<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/collision-in-unreal-engine---overview?application_version=5.7 -->

# Collision Overview

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
8. Collision Overview

# Collision Overview

An overview of how Collision and Collision Responses operate in Unreal Engine.

![Collision Overview](https://dev.epicgames.com/community/api/documentation/image/b4aff67d-a60f-4706-b034-b73662b2d481?resizing_type=fill&width=1920&height=335)

 On this page

**Collision Responses** and **Trace Responses** form the basis for how Unreal Engine 4 handles collision and ray casting during run time. Every object that can collide gets an **Object Type** and a series of responses that define how it interacts with all other object types. When a collision or overlap event occurs, both (or all) objects involved can be set to affect or be affected by blocking, overlapping, or ignoring each other.

**Trace Responses** work basically the same way, except the trace (ray cast) itself can be defined as one of the Trace Response types, thusly allowing Actors to either block it or ignore it based on *their* Trace Responses.

## Interactions

There are a few rules to keep in mind with how collisions are handled:

* **Blocking** will naturally occur between two (or more) Actors set to Block. However, **Simulation Generates Hit Events** needs to be enabled to execute **Event Hit**, which is used in Blueprints, Destructible Actors, Triggers, etc...
* Setting Actors to **Overlap** will often look like they **Ignore** each other, and without **Generate Overlap Events**, they are essentially the same.
* For two or more simulating objects to block each other, they both need to be set to block their respective object types.
* For two or more simulating objects: if one is set to overlap an object, and the second object is set to block the other, the overlap will occur but not the block.
* Overlap events **can** be generated even if an object **Blocks** another, especially if traveling at high speeds.
  + It is not recommended for an object to have both collision and overlap events. Though possible, there is much that needs manual handling.
* If one object is set to ignore and the other is set to overlap, no overlap events will be fired.

For purposes of testing levels and looking around your worlds:

* The default **Play In Editor** camera is a pawn. Thusly can be blocked by anything set to block pawns.
* The **Simulate in Editor** camera, before possessing anything, is **not** a pawn. It can freely clip through everything and will not create any collision or overlap events.

## Common Collision Interaction Examples

These interactions assume that all the objects have **Collision Enabled** set to **Collision Enabled** so they are set to fully collide with everything. If collision is disabled, it is as if **ignore** has been set for all **Collision Responses**.

For the following section, this will be the setup used to explain what is happening:

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1c7f22c6-c2ca-4d30-9a56-eefeb61f1219/col_setup.png)

The sphere is a **PhysicsBody** and the box is **WorldDynamic**, and by changing their collision settings we can get a number of behaviors.

### Collision

By setting both of their collision settings to block each other, you get a collision, great for having objects interact with each other:

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9c194183-3ea3-480d-9c45-87b0c7f9aa7a/col_collidenoevent.png)

| Sphere Collision Setup | Wall Collision Setup |
| --- | --- |
|  |  |
| In this case, the sphere is a **PhysicsBody** and it is set to `block` **WorldDynamic** (which is what the wall is). | The wall is a **WorldDynamic** and is set to `block` **PhysicsBody** Actors (which is what the sphere is). |

In this case, the sphere and the wall will simply collide; no further notifications of the collision will take place.

### Collision and Simulation Generates Hit Events

Just collision is useful and in general, the bare minimum for physics interactions, but if you want something to **report** it has collided so a Blueprint or section of code can be triggered:

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3a708e18-e166-4d3d-9f2c-3a14b5c2f8d1/col_collideevent.png)

| Sphere Collision Setup | Wall Collision Setup |
| --- | --- |
|  |  |
| As in the example above, the sphere is a **PhysicsBody** and it is set to `block` **WorldDynamic** (which is what the wall is). However, the sphere has also enabled **Simulation Generates Hit Events** so it will trigger an event for itself whenever it collides with something. | The wall is a **WorldDynamic** and is set to `block` **PhysicsBody** Actors (which is what the sphere is). Since the wall is not set to **Simulation Generates Hit Events**, it will not generate an event for itself. |

With the sphere set to **Simulation Generates Hit Events**, the sphere will tell itself that it has had a collision. It will fire off events such as **ReceiveHit** or **OnComponentHit** in the sphere's Blueprint. Now if the box had an event for collision, it would not fire because it will never notify itself it has happened.

Further, an object that is reporting rigid collisions will report them all and spam reports when it is just sitting on something, so it is best to be careful to filter what it is colliding within its Blueprint or in code.

### Overlap and Ignore

For all intents and purposes, **Overlap** and **Ignore** work exactly the same **assuming Generate Overlap Events** is disabled. In this case, the sphere is set to overlap or ignore the box:

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3c26a177-6f71-46d1-ac2f-b21e01cb66f2/col_ignore.png)

| Sphere Collision Setup | Wall Collision Setup |
| --- | --- |
|  |  |
| Here the sphere is set to `overlap` **WorldDynamic** Actors (like our wall), but it does not have **Generate Overlap Events** enabled. As far as the sphere is concerned, it has not collided or overlapped anything, effectively it has ignored the wall. | The wall is a **WorldDynamic** and is set to `block` **PhysicsBody** Actors (which is what the sphere is). As stated above, both Actors need to be set to block each other's respective object types. If they do not, they will not collide. |

Or:

| Sphere Collision Setup | Wall Collision Setup |
| --- | --- |
|  |  |
| Here the sphere is set to `ignore` **WorldDynamic** Actors (like our wall), and it will pass through the wall. | The wall is a **WorldDynamic** and is set to `block` **PhysicsBody** Actors (which is what the sphere is). As stated above, both Actors need to be set to block each other's respective object types. If they do not, they will not collide. |

### Overlap and Generate Overlap Events

Unlike collisions that can fire every frame, the overlap events are **ReceiveBeginOverlap** and **ReceiveEndOverlap**, which only fire in those specific cases.

For an overlap to occur, both Actors need to enable **Generate Overlap Events**. This is for performance. In the case where both the Sphere and the Box want overlaps when we move either the Sphere or the Box, we do an overlap query to see if we need to fire any events.

If the Box doesn't want overlaps then when it moves we will not do an overlap query. But now we could be overlapping with the Sphere, and so the Sphere would need to tick and check for overlaps each frame in case someone moved into them.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ad3d2476-2cb5-48d9-a548-2380df6f7e78/col_overlapevent.png)

| Sphere Collision Setup | Wall Collision Setup |
| --- | --- |
|  |  |
| Here the sphere is set to `overlap` **WorldDynamic** Actors (like our wall), and it will generate an event for itself when it does overlap something. | The wall is a **WorldDynamic** and is set to `block` **PhysicsBody** Actors (which is what the sphere is). As stated above, both Actors need to be set to block each other's respective object types. If they do not, they will not collide. But, an **Overlap** does occur here, and events for the sphere and box are fired. |

* [collision](https://dev.epicgames.com/community/search?query=collision)
* [physics](https://dev.epicgames.com/community/search?query=physics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Interactions](/documentation/en-us/unreal-engine/collision-in-unreal-engine---overview?application_version=5.7#interactions)
* [Common Collision Interaction Examples](/documentation/en-us/unreal-engine/collision-in-unreal-engine---overview?application_version=5.7#commoncollisioninteractionexamples)
* [Collision](/documentation/en-us/unreal-engine/collision-in-unreal-engine---overview?application_version=5.7#collision)
* [Collision and Simulation Generates Hit Events](/documentation/en-us/unreal-engine/collision-in-unreal-engine---overview?application_version=5.7#collisionandsimulationgenerateshitevents)
* [Overlap and Ignore](/documentation/en-us/unreal-engine/collision-in-unreal-engine---overview?application_version=5.7#overlapandignore)
* [Overlap and Generate Overlap Events](/documentation/en-us/unreal-engine/collision-in-unreal-engine---overview?application_version=5.7#overlapandgenerateoverlapevents)
