<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/mover-features-and-concepts-in-unreal-engine?application_version=5.7 -->

# Mover Features and Concepts

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
6. [Mover](/documentation/en-us/unreal-engine/mover-in-unreal-engine "Mover")
7. Mover Features and Concepts

# Mover Features and Concepts

Learn about the MoverComponents, movement modes, and more.

![Mover Features and Concepts](https://dev.epicgames.com/community/api/documentation/image/af183acc-e052-4419-ac9a-b9ec2e8db49d?resizing_type=fill&width=1920&height=335)

Learn to use this **Experimental** feature, but use caution when shipping with it.

 On this page

This document covers Mover's features and high-level concepts to help you better understand the plugin.

## MoverComponent

A **MoverComponent** is an actor component that manages movement, acts as a source for state queries, and provides API for influencing movement.

## Movement Mode

A **movement mode** is an object that observes inputs to determine how actors move, such as walking, falling, or climbing. After determining the movement method, the mode attempts to move the character.

There is exactly one mode active at a time.

## Layered Moves

**Layered moves** are objects that represent additional, usually temporary, movement. For example, a constant force repulsing an actor away, a homing force that moves toward an enemy, or even animation-driven root motion.

Layered moves generate a proposed move and rely on the active movement mode to execute it. Multiple layered moves can be active at a time, and they are mixed with other influences. Their lifetime can have a duration or be instantaneous, and they survive through movement mode changes.

## Transitions

**Transitions** are objects that evaluate if an actor should change modes based on the current state. They can be associated with a particular mode and only evaluated when that mode is active, or they can be global and evaluated regardless of mode.

The use of transitions is optional, as there are other available methods of switching modes.

## Default Character Movement Set

The **default character movement set** is a collection of modes and mechanisms intended to behave similarly to the built-in functionality of the **Character Movement Component (CMC)**. It shares some limitations, such as assuming a vertical capsule primitive for all actors.

The default character movement set is included with the Mover plugin as a bridge for devs who are used to CMC.

The methods outlined for this movement set are only one approach to designing movement. If it suits your project, you can replace any or all of it. Other approaches might involve many specialized modes that derive from a single type, but have a high degree of configurability.

## Other Movement Influences

### Movement Modifiers

For events like crouch or stance changes, you can use movement modifiers to adjust the movement simulation’s parameters without producing movement. You can use them to change movement settings in batches, such as max speed and acceleration for crouching.

### Instant Effects

Instant effects cover certain mechanics that instantly change the movement simulation state without consuming any time or relying on a mode to execute the change, such as teleportation or inducing a forced velocity.

### Navigation and Pathfinding

Mover supports navigation through **NavMoverComponent** and a **NavWalking** movement mode in the default movement set. The NavMoverComponent is added to the actor in addition to your Mover component.

Reciprocal Velocity Obstacles (RVO) avoidance is not yet supported.

## Composable Inputs and State

**Inputs**, created by the controlling owner, influence movement simulation steps. This includes things like desired move direction, jumping inputs, or desired pathing info.

**Sync states** are snapshots that describe an actor's movement at a point in time. This includes things like location, orientation, velocity, and movement mode.

Both inputs and sync states can have project-specific struct data attached dynamically. For example, an item granted to a player at runtime might enable input that activates a new movement mode and writes additional state data.

## Shared Settings

You can share **settings** between multiple decoupled movement modes. For example, the maximum walkable slope angle may influence both walking and falling modes. Individual modes declare which settings types they require, and the MoverComponent ensures that both modes use a single instance of that type.

## Backends

You can drive Mover actors with systems other than Network Prediction. For example, physics-based characters use a different backend that interfaces with Chaos' Networked Physics system. You can even create a simple standalone backend for non-networked games to avoid the overhead of other systems.

Mode implementations may also be specialized to execute proposed movements differently. For example, physics-based movement modes only perform setup operations while leaving the actual movement to the physics simulation. This differs from the default modes, which move scene components directly.

* [experimental](https://dev.epicgames.com/community/search?query=experimental)
* [character](https://dev.epicgames.com/community/search?query=character)
* [mover](https://dev.epicgames.com/community/search?query=mover)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [MoverComponent](/documentation/en-us/unreal-engine/mover-features-and-concepts-in-unreal-engine?application_version=5.7#movercomponent)
* [Movement Mode](/documentation/en-us/unreal-engine/mover-features-and-concepts-in-unreal-engine?application_version=5.7#movementmode)
* [Layered Moves](/documentation/en-us/unreal-engine/mover-features-and-concepts-in-unreal-engine?application_version=5.7#layeredmoves)
* [Transitions](/documentation/en-us/unreal-engine/mover-features-and-concepts-in-unreal-engine?application_version=5.7#transitions)
* [Default Character Movement Set](/documentation/en-us/unreal-engine/mover-features-and-concepts-in-unreal-engine?application_version=5.7#defaultcharactermovementset)
* [Other Movement Influences](/documentation/en-us/unreal-engine/mover-features-and-concepts-in-unreal-engine?application_version=5.7#othermovementinfluences)
* [Movement Modifiers](/documentation/en-us/unreal-engine/mover-features-and-concepts-in-unreal-engine?application_version=5.7#movementmodifiers)
* [Instant Effects](/documentation/en-us/unreal-engine/mover-features-and-concepts-in-unreal-engine?application_version=5.7#instanteffects)
* [Navigation and Pathfinding](/documentation/en-us/unreal-engine/mover-features-and-concepts-in-unreal-engine?application_version=5.7#navigationandpathfinding)
* [Composable Inputs and State](/documentation/en-us/unreal-engine/mover-features-and-concepts-in-unreal-engine?application_version=5.7#composableinputsandstate)
* [Shared Settings](/documentation/en-us/unreal-engine/mover-features-and-concepts-in-unreal-engine?application_version=5.7#sharedsettings)
* [Backends](/documentation/en-us/unreal-engine/mover-features-and-concepts-in-unreal-engine?application_version=5.7#backends)
