<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/colliders-triggers-and-pickups-in-parrot-for-unreal-engine?application_version=5.7 -->

# Colliders, Triggers, and Pickups in Parrot

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
5. [Get Started](/documentation/en-us/unreal-engine/get-started "Get Started")
6. [Unreal Engine for Unity Developers](/documentation/en-us/unreal-engine/unreal-engine-for-unity-developers "Unreal Engine for Unity Developers")
7. [Parrot Game Sample](/documentation/en-us/unreal-engine/parrot-game-sample-for-unreal-engine "Parrot Game Sample")
8. Colliders, Triggers, and Pickups in Parrot

# Colliders, Triggers, and Pickups in Parrot

Collisions and triggers in Project Parrot.

![Colliders, Triggers, and Pickups in Parrot](https://dev.epicgames.com/community/api/documentation/image/1b2e9a52-0920-4c7e-9b74-06e3f5cff07e?resizing_type=fill&width=1920&height=335)

 On this page

## Collision Types

Collision in Unreal Engine is similar to Unity but has some differences that are covered here. If you have used Unity’s layer-based collision detection, the project collision settings should look similar to the collision matrix. You can access this by going to **Edit >** **Project Settings > Collision**. If you expand the **Preset** tab, you can see all of the default preset profiles with a description of what they do.

[![Image of the options on the Engine Collision landing page with descriptions of presets.](https://dev.epicgames.com/community/api/documentation/image/4886bd6a-5e90-4077-8aa0-d11dd454be7c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4886bd6a-5e90-4077-8aa0-d11dd454be7c?resizing_type=fit)

You will notice that Unreal has a few more options when it comes to resolving collisions. These are covered in depth in the [Unreal Engine Collision Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/collision-in-unreal-engine---overview). This level of granularity in collision detection is nice to have and can help your game’s performance. It’s important to understand:

* Channels or individual colliders can be set to Blocking, Overlap, or Ignore.
* A common mistake is not having the Generate Overlap Events checkbox set correctly on your colliders when you need those events.
* Static geometry should be blocking and overlapping but not necessarily generate overlap or hit events since it’s not needed for gameplay.
* Overlap events can be generated even if an object blocks another - particularly when traveling at high speeds. In Unity, this can be a problem if you’re directly modifying the translation instead of a Rigidbody component. Doing so bypasses physics considerations.
* In Unreal, when you call any function that updates an actor’s transform, there are two boolean parameters that dictate how you’d like the actor to move:

  + **Sweep** sets to true triggers overlaps and stops that actor short of the destination if blocked. **Teleport** determines whether or not the physics velocity is preserved.

* Channels can also be used for Traces which are equivalent to Unity’s physics cast (i.e. Raycast, SphereCast etc.). You can pass the channel during your Line Trace function call the same way you would pass the layer mask in a Raycast in Unity.

### Parrot Custom Collision Types

Parrot has a few custom collision object channels setup: **Player**, **Cannonball**, and **Enemy**.

[![Object channel menu options for Player, Cannonball, or Enemy.](https://dev.epicgames.com/community/api/documentation/image/0892f730-306b-4680-9b07-528d0d874edc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0892f730-306b-4680-9b07-528d0d874edc?resizing_type=fit)

By adding these object types, Parrot can control exactly how these object channels interact with trace channels as collision traces occur in the world. A default response is set for what should generally happen - but this can be customized as desired. Parrot also has a few custom trace channel presets: **Player**, **OverlapAllPlayers**, **BlockAllPlayers**, **Cannonball**, and **Enemy**.

[![Image of trace channel presets in Parrot.](https://dev.epicgames.com/community/api/documentation/image/9920dbee-928b-4dc5-825d-a9ce9f563fe9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9920dbee-928b-4dc5-825d-a9ce9f563fe9?resizing_type=fit)

These presets are particularly useful for gameplay triggers. For example, `OverlapAllPlayers` can ignore all other collisions and just respond to collision events with player collision object types. If you look at the collision settings for different meshes in the game, you will see these presets used frequently.

Collision settings can also be customized on a per mesh basis if desired.

### World Bounds

When creating your levels, something to note is the **World Bounds**. This can be set from **World Settings > World**. You can implement a custom damage type for when an actor interacts with these defined world bounds. Parrot bounds use a combination of the **KillZ** world setting and **Out of Bounds** trigger volumes.

[![Image of the KillZ setting.](https://dev.epicgames.com/community/api/documentation/image/4f56c59b-6c19-4d80-be62-8731825a3af8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4f56c59b-6c19-4d80-be62-8731825a3af8?resizing_type=fit)

## Trigger Volumes

Unreal Engine has built-in trigger volume actors (see [Trigger Volume Actors in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/trigger-volume-actors-in-unreal-engine)) that can be used to trigger events. Examples where developers use these in Parrot are **Out Of Bounds** and **Finish Line** trigger volumes. Trigger volumes are often used in conjunction with the level blueprint (see the developer document [Level Blueprints in Parrot](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-level-blueprints-in-parrot)) but do not have to be. Parrot's trigger for Out Of Bounds is a box trigger with a straightforward event graph:

[![Example of out of bounds trigger with image of coast line in game.](https://dev.epicgames.com/community/api/documentation/image/7e3fc1f3-f08b-4b95-9a9a-aa04272e1f2a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7e3fc1f3-f08b-4b95-9a9a-aa04272e1f2a?resizing_type=fit)

[![Image of Blueprints workflow in UE.](https://dev.epicgames.com/community/api/documentation/image/ea50b39c-fd09-413d-9d95-9ca566bc4c88?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ea50b39c-fd09-413d-9d95-9ca566bc4c88?resizing_type=fit)

If you look at the actor’s collision settings in the Details panel, you’ll see the collision channel preset does most of the work here.

[![Image of the Collision presets options.](https://dev.epicgames.com/community/api/documentation/image/3f7859e8-f236-4499-8639-c8e29e4a86fc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3f7859e8-f236-4499-8639-c8e29e4a86fc?resizing_type=fit)

### Power Pickup

Let’s take a look at a practical example of the collision system with Parrot’s powerup pickup implementation. If you open **BP\_PickupBase under Content** **>** **Blueprints** **> Pickups** and look at the viewport you can see the hierarchy which contains the collision component.

[![Image of item in viewport with hierarchy in folders in left nav menu.](https://dev.epicgames.com/community/api/documentation/image/750a9019-bd9d-4e70-bf2e-db3b20fd6988?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/750a9019-bd9d-4e70-bf2e-db3b20fd6988?resizing_type=fit)

The collision settings and the Out of Bounds have a trigger preset that generates overlap events with players:

[![Image of checkbox for Generate Overlap Events option.](https://dev.epicgames.com/community/api/documentation/image/dba6fa04-9642-4fb6-bcea-bd1d8b30a5f6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dba6fa04-9642-4fb6-bcea-bd1d8b30a5f6?resizing_type=fit)

If you look at the Event Graph, you’ll see the `ActorBeginOverlap` event with Other Actor as a parameter. This event works much like `OnCollisionEnter` in Unity. The difference here is that instead of being passed a collider component, you’re given the actor itself.

Parrot casts to check that the actor is a player that has overlapped. Then the `OnPickedUp` event is called. This allows derived blueprint classes to define their own behavior for `OnPickedUp` while the base class handles the actor overlap event itself.

The developers use the base blueprint to handle having all pickups play a sound and spawn some particle effects. The pickup sound and particle effect variables are instance-editable so that they can be set in the class defaults of the derived classes. **Class Defaults** are located in the Blueprint editor at the top by the compile button:

[![Class Defaults option in the menu bar settings.](https://dev.epicgames.com/community/api/documentation/image/4da511f3-2ab3-4d68-b9ab-4cb5f04f01d8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4da511f3-2ab3-4d68-b9ab-4cb5f04f01d8?resizing_type=fit)

An example of changed class defaults can be found with the speed pickup, which uses a Niagra system with green particles (versus the heart pickup that uses pink). Similarly, the pickup mesh itself can be set on derived blueprints. The last step in the overlap logic is to destroy the pickup actor since we don’t want it to persist after a player has collected it.

With only a few nodes, you’re able to create some robust logic that can expand to derived blueprints with ease. All derived blueprints stem from an overlap event tied to the actor.

## Player Character Jumping Off an Enemy

Another great example to look at is the player jumping off of an enemy. The enemy’s capsule collider type is ‘enemy’ and will collide with player object types. Enemies with swords also have a similar overlap event. These are commonly referred to as hit-boxes and are where an attack is effective.

But when a player goes to jump off an enemy, how does Parrot get around this? The solution was to place a hurt-box on the enemies heads. When the player overlaps this hurt-box volume, the player character can then do a series of checks to see if it’s a valid jump based on the location of the character, the location of the hurt-box, and the box extents. If the checks pass, the player can perform their jump and hit the enemy. The heavy lifting is once again done by the collision channels filtering to just the overlaps that Parrot cares about - a player collision object and an enemy on the hurt-box volume.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Collision Types](/documentation/en-us/unreal-engine/colliders-triggers-and-pickups-in-parrot-for-unreal-engine?application_version=5.7#collisiontypes)
* [Parrot Custom Collision Types](/documentation/en-us/unreal-engine/colliders-triggers-and-pickups-in-parrot-for-unreal-engine?application_version=5.7#parrotcustomcollisiontypes)
* [World Bounds](/documentation/en-us/unreal-engine/colliders-triggers-and-pickups-in-parrot-for-unreal-engine?application_version=5.7#worldbounds)
* [Trigger Volumes](/documentation/en-us/unreal-engine/colliders-triggers-and-pickups-in-parrot-for-unreal-engine?application_version=5.7#triggervolumes)
* [Power Pickup](/documentation/en-us/unreal-engine/colliders-triggers-and-pickups-in-parrot-for-unreal-engine?application_version=5.7#powerpickup)
* [Player Character Jumping Off an Enemy](/documentation/en-us/unreal-engine/colliders-triggers-and-pickups-in-parrot-for-unreal-engine?application_version=5.7#playercharacterjumpingoffanenemy)
