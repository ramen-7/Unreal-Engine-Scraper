<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/target-point-actors-in-unreal-engine?application_version=5.7 -->

# Target Point Actors

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
5. [Understanding the Basics](/documentation/en-us/unreal-engine/understanding-the-basics-of-unreal-engine "Understanding the Basics")
6. [Actors and Geometry](/documentation/en-us/unreal-engine/actors-and-geometry-in-unreal-engine "Actors and Geometry")
7. [Actors Reference](/documentation/en-us/unreal-engine/unreal-engine-actors-reference "Actors Reference")
8. Target Point Actors

# Target Point Actors

Guide to creating and using Target Actors.

![Target Point Actors](https://dev.epicgames.com/community/api/documentation/image/9bd852bb-3bf3-456f-bb59-f5ede71d4ffe?resizing_type=fill&width=1920&height=335)

 On this page

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/17d55e62-dfe1-4279-b95b-24448bd91a2e/target_point_actors.png)

When creating worlds for games you sometimes need the ability to place and spawn items in the world for the player to interact with. **Target Point Actors** do just this; they give you a generic point in the world that you can spawn items from. If you are familiar with other 3D applications like 3Ds Max or Maya, Target Point Actors are very similar to dummy Actors that you find in those programs.

## Placing Target Point Actors

Target Point Actors can be found in the **Modes** panel under the **All Classes** category. To add one to the world, simply select it from the **Modes** panel and then drag it into the world.

## Using Target Points

Target Point Actors can be used for all kinds of things inside Unreal Engine 4. Here is a list of some of the things that you can use Target Point Actors for.

* Look-at targets for cameras during cinematic sequences.
* Path points for AI agents.
* Spawn point for a VFX.
* Spawn points for items like health and item pickups.
* Visual cue for where an item is placed / should be placed in the world.

Here is an example showing how a Target Point Actor was used as in a Blueprint to serve as a spawn point.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6299b413-38d9-48ec-84c3-a60ef8bbd1dc/target_point_as_spawn.png)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Placing Target Point Actors](/documentation/en-us/unreal-engine/target-point-actors-in-unreal-engine?application_version=5.7#placingtargetpointactors)
* [Using Target Points](/documentation/en-us/unreal-engine/target-point-actors-in-unreal-engine?application_version=5.7#usingtargetpoints)
