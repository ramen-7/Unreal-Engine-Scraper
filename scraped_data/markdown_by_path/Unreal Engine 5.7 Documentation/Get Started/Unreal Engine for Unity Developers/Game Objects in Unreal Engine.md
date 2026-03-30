<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/game-objects-in-unreal-engine?application_version=5.7 -->

# Game Objects in Unreal Engine

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
7. Game Objects in Unreal Engine

# Game Objects in Unreal Engine

Learn about the fundamental gameplay types.

![Game Objects in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/c13027bd-c6a2-4a3d-b835-46a7f19ccf98?resizing_type=fill&width=1920&height=335)

 On this page

## Comparing GameObjects to UObjects and Actors

In Unity, **GameObjects** represent programmable in-game objects. A GameObject does not do much by itself; it acts as a container for **Components**, such as Light and Mesh, that provide specific functionalities. Every GameObject has a Transform component attached to represent position and orientation in the world.

In Unreal Engine (UE), **UObjects** represent programmable objects in your game's world. The UObject class functions as a shared base class for most classes in UE. This approach supports the [Unreal Engine Reflection System](https://dev.epicgames.com/documentation/en-us/unreal-engine/reflection-system-in-unreal-engine), which provides automatic garbage collection and other benefits.

[Actor](https://dev.epicgames.com/documentation/en-us/unreal-engine/actors-in-unreal-engine), a subclass of UObject, is a close equivalent to Unity's GameObject. Actors support UE's [Component System](https://dev.epicgames.com/documentation/en-us/unreal-engine/game-objects-in-unreal-engine#comparing-component-systems) and transforms (USceneComponent) so you can place them in the world. However, a key difference compared to Unity is you can extend an Actor's functionality directly rather than relying on Components exclusively.

If your object implementation doesn't require the additional functionality of one of UObject's subclasses, you can extend UObject directly for a lighter-weight implementation. See [Objects](https://dev.epicgames.com/documentation/en-us/unreal-engine/objects-in-unreal-engine) for more detailed information on UObjects.

## Comparing Component Systems

Similar to Unity, UE has a Component system you can use to attach reusable functionality to your game objects. You can create your own Components from scratch or by extending one of the many provided with UE. Before you do, it is worth understanding the following core Component types:

* **Actor Component** - The base Component type that attaches to an Actor. Actor Components do not have transforms, so they do not have a physical location in the world. They are useful for abstract behaviors, such as inventory or attribute management.
* **Scene Component** - A type of Actor Component that adds a transform for world positioning. Scene Components do not have visual representations, so they are suitable for non-visual location-based behaviors, such as physical forces, cameras, or audio.
* **Primitive Component** - A type of Scene Component that adds visual and physical representation. They are suitable for rendering visual elements and collision volumes.

In Unity, you can create complex GameObjects with a parent-child relationship. For example, a parent object can have multiple child objects with their own meshes, colliders, or behaviors.

In UE, you can build Actors with a similar hierarchy by using Components instead of child Actors to reduce performance and memory costs.

For more detailed information on UE's Component system, see [Components](https://dev.epicgames.com/documentation/en-us/unreal-engine/actors-in-unreal-engine).

## Comparing Update() and Tick()

In Unity, Component updates are primarily driven by `Update()` and `FixedUpdate()` in MonoBehaviour.

In UE, Actors use `Tick()` (enabled by default), and Components optionally use `TickComponent()` (disabled by default).

By default, ticking happens once per frame. You can specify another ticking interval by assigning a tick group, such as `TG_DuringPhysics`. You can also specify a tick dependency to prevent ticks until another specified tick function is completed.

For more detailed information, see the following resources:

* [Actor Lifecycle](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-actor-lifecycle?application_version=5.5)
* [Actor Ticking](https://dev.epicgames.com/documentation/en-us/unreal-engine/actor-ticking-in-unreal-engine)
* [Component Ticking](https://dev.epicgames.com/documentation/en-us/unreal-engine/components-in-unreal-engine)

## Gameplay Framework

**Unreal Engine's Gameplay Framework** is a collection of classes, including Actors and Components, that provide you with a modular foundation upon which to build your gameplay experiences.

If you compare implementing gameplay in Unity to using UE's Gameplay Framework, there are more differences than similarities. As such, we recommend you review the [Gameplay Framework section](https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-framework-in-unreal-engine) to learn more about how the concepts covered in this document fit into the framework. Additionally, the sections below cover some important framework classes at a high level.

### Important UObject Subclasses

* [Level](https://dev.epicgames.com/documentation/en-us/unreal-engine/levels-in-unreal-engine) - Contains a set of game objects that make up a level in your game. Levels are similar to Scenes in Unity.
* [Data Asset](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-assets-in-unreal-engine?application_version=5.5) - Used to define assets that store data for your game. Data Assets are similar to ScriptableObjects in Unity.

### Important Actor Subclasses

* [Pawn](https://dev.epicgames.com/documentation/en-us/unreal-engine/pawn-in-unreal-engine) - Acts as an "agent" within the world. A Controller can possess a Pawn to take control of it.

  + [Character](https://dev.epicgames.com/documentation/en-us/unreal-engine/characters-in-unreal-engine) - A type of Pawn that represents a humanoid-style character and provides basic movement and collision functionality.
* [Controller](https://dev.epicgames.com/documentation/en-us/unreal-engine/controllers-in-unreal-engine) - Responsible for directing Pawns after possessing them.

  + [PlayerController](https://dev.epicgames.com/documentation/en-us/unreal-engine/player-controllers-in-unreal-engine) - Used to provide a local human player control of a Pawn.
  + [AIController](https://dev.epicgames.com/documentation/en-us/unreal-engine/ai-controllers-in-unreal-engine) - Used to control a Pawn with artificial intelligence.
* [Game Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/game-mode-and-game-state-in-unreal-engine) - A manager Actor that defines and sets up your game.
* [Game State](https://dev.epicgames.com/documentation/en-us/unreal-engine/game-mode-and-game-state-in-unreal-engine) - Contains the game's state information.

  + **Player State** - Contains a player's state information. The Game State tracks all Player States within an array.

* [gameplay](https://dev.epicgames.com/community/search?query=gameplay)
* [unity](https://dev.epicgames.com/community/search?query=unity)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Comparing GameObjects to UObjects and Actors](/documentation/en-us/unreal-engine/game-objects-in-unreal-engine?application_version=5.7#comparing-game-objects-to-u-objects-and-actors)
* [Comparing Component Systems](/documentation/en-us/unreal-engine/game-objects-in-unreal-engine?application_version=5.7#comparing-component-systems)
* [Comparing Update() and Tick()](/documentation/en-us/unreal-engine/game-objects-in-unreal-engine?application_version=5.7#comparing-update-and-tick)
* [Gameplay Framework](/documentation/en-us/unreal-engine/game-objects-in-unreal-engine?application_version=5.7#gameplay-framework)
* [Important UObject Subclasses](/documentation/en-us/unreal-engine/game-objects-in-unreal-engine?application_version=5.7#important-u-object-subclasses)
* [Important Actor Subclasses](/documentation/en-us/unreal-engine/game-objects-in-unreal-engine?application_version=5.7#important-actor-subclasses)
