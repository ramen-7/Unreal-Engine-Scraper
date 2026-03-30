<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/enemy-characters-in-parrot-for-unreal-engine?application_version=5.7 -->

# Enemy Characters in Parrot

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
8. Enemy Characters in Parrot

# Enemy Characters in Parrot

Project Parrot uses templates for NPC enemies.

![Enemy Characters in Parrot](https://dev.epicgames.com/community/api/documentation/image/b43cb008-8719-49f5-912b-b2773a45f236?resizing_type=fill&width=1920&height=335)

 On this page

## Enemy Characters

In Unreal Engine, NPCs and enemies are generally set up very similarly to the player in that an enemy has a controller and a pawn. In fact, the enemies and the player have some shared functionality in a common base class, `AParrotCharacterBase`. For the Parrot game, the behavior trees are used to control the enemy behavior, so the AI Controller class is used to create our enemy controllers. We will start with the animation blueprint since that setup is shared across enemies.

## The Enemy Animation Blueprints

### Animation Blueprint Templates

For cases where you have multiple skeletal meshes that otherwise share identical needs for animation, you can create what’s called an animation blueprint template (see **[Animation Blueprint Linking](https://dev.epicgames.com/documentation/en-us/unreal-engine/BlueprintAPI/Components/SkeletalMesh/AnimationBlueprintLinking?application_version=5.6)**). In this case, there are four different enemy types - a headless skeleton, a skeleton, sharky, and a boss shark. Because they all share an identical skeleton and animation configuration, one template that implements the animation graph and event graph can be reused for all of them. You can view how this template is set up here:  `Blueprints > Enemy > EnemyBase > ABT_EnemyBase`. It looks very similar to the player’s animation blueprint because a template is set up in nearly the same way as that animation blueprint.

### Animation Blueprints

In this case, all of the implementation is in the template, while the animations themselves are absent since the template does not reference a specific skeleton. Each of the enemies has its own animation blueprint derived from the template, and each one has that skeleton’s animations slotted in the animation graph overrides. You can view an example of this here:  `Blueprints > Enemy > HeadlessSkeleton > ABP_Enemy_HeadlessSkeleton`.

Below, we have selected the appropriate animations for the headless skeleton’s skeletal mesh for each animation state.

[![Image of which animation graph overrides are being used for the headless skeleton.](https://dev.epicgames.com/community/api/documentation/image/4070feba-47d6-40c1-8020-54b893db01ee?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4070feba-47d6-40c1-8020-54b893db01ee?resizing_type=fit)

### The Enemy Pawn

Parrot's enemy characters share a lot of functionality with the player; specifically, hit points and similar functions (such as death). This shared implementation can be seen in `AParrotCharacterBase`. For the enemy-specific implementation, we have a subclass `AParrotEnemyCharacterBase`. This handles all of the implementation of how the patrol system works, how combat works, and more. You can learn more about how combat works in the [Combat in Parrot](https://dev.epicgames.com/documentation/en-us/unreal-engine/combat-in-parrot-for-unreal-engine) documentation.

In this setup, the combat hit and hurt checks are done on the enemy with an implementation on how to trigger volumes in the blueprint base class found here: `Blueprints > Enemy > EnemyBase > BP_EnemyCharacter_Base`.

This implementation is done here instead of handled in the native C++ class because the trigger volumes have to be different for every enemy due to the different shapes, sizes, and complexities of their meshes. This is necessary because a trigger volume that is inherited cannot be modified in the derived class.

### The Enemy AI Controller

As previously mentioned, the enemies are controlled with behavior trees, so there is a base class derived from `AIController` in `AParrotEnemyAIControllerBase`. Here you will see a variety of `BlueprintImplementableEvents` used to send data to the blackboard to be used by the behavior trees.

You can view how the AI Controller passes data into the behavior tree and how it handles detecting player presence in `Blueprints > AI > EnemyBase > BP_EnemyController_Base`.

## Creating AI with Behavior Trees

Unreal Engine offers a powerful and flexible infrastructure to build AI using behavior trees. A Quick Start guide to setup the basic boilerplate with some behaviors can be found in the [Behavior Tree Quick Start Guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/behavior-tree-in-unreal-engine---quick-start-guide). The results from that guide are used as the foundation of the enemy AI and to make alterations to set up the behaviors needed.

We have two behavior tree tasks, **Blueprints > AI > EnemyBase > BTT\_FindNextPatrol** and **Blueprints > AI > EnemyBase > BTT\_AttackPlayer** to provide the basic functionality needed for patrolling and attacking the player. There is one shared blackboard, **Blueprints > AI > EnemyBase > BB\_Enemy\_Base**, since the infrastructure to support all features is present in each enemy. It is up to the behavior tree implementation to decide which functionalities to use to customize the enemy behaviors.

Each of the enemies has a different behavior tree configuration so that each of them behaves in a different way. You can take a look through all four of them at the following locations:

* ****Blueprints> AI > HeadlessSkeleton > BT\_HeadlessSkeleto**n**
* **Blueprints > AI/Skeleton > BT\_Skeleton**
* **Blueprints > AI > Sharky > BT\_Sharky**
* **Blueprints > AI > BossShark > BT\_Boss\_Shark**

## Creating an Authorable Patrolling Waypoint System

For the enemies, Parrot doesn’t want the same patrol functionality that the behavior tree guide demonstrates, which is where the enemy AI randomly selects a navigable point within a radius every 4 seconds. What is wanted is enemies that actively follow a patrol route back and forth, like many other platformer games.

For this, Parrot has created its own system that provides the functionality needed. This consists of the `UParrotEnemyPatrolRigComponent` that can be placed in the scene to author a patrol. It uses class default sub-objects to instantiate a spline. The spline is used to author the patrol waypoints, two trigger volumes (used to trigger AI behavior), and an editor-only visualizer that draws the ordering of waypoints. The ordering of the waypoints allows the direction of the patrol path to be seen at edit time. You can see the details of the C++ implementation in `UParrotEnemyPatrolRigComponent`.

This implementation is a component so that a patrol rig can be attached to any actor in a scene. This allows placing a rig on a moving object and means the patrol will stay correctly placed in local space. For placing a patrol rig that isn’t attached to an existing actor in a scene, we have the `AParrotEnemyPatrolRigActor`, which is an actor you can place anywhere in a scene and it spawns a `UParrotEnemyPatrolRigComponent` as a default sub-object on itself.

This implementation allows selecting an enemy to be spawned at runtime to follow the patrol path. This process uses an Unreal Engine feature called **deferred actor spawning**, which allows spawning an actor in two stages - the first constructs the actor object without performing any `AActor` initialization such as `BeginPlay`. This gives you the opportunity to perform any configuration or setup necessary for the actor to have before it is initialized. After performing this setup, you invoke the second stage to finalize the spawn and initialize the actor. This is done for the patrol rig so that when the enemy actor is spawned, the patrol spline and trigger volumes can be piped into the actor so they can be processed during actor initialization and the patrol sequence can begin automatically.

You can view the code that performs the deferred actor spawn in `UParrotEnemyPatrolRigComponent`. A similar feature exists in blueprint, where you can tag properties on a blueprint actor as **Expose on Spawn**, which allows you to pass arguments into the spawn blueprint node, which are set before the actor’s initialization takes place.

Pictured below, you can see an example of how one of these patrol rigs is set up in **Maps > Level\_1 > Level\_1** with a two point patrol rig, starting at point 0 on the right. This patrol rig is set up to spawn a `BP_EnemyCharacter_Skeleton`.

[![Image of the details tab showing the contents of the Enemy Patrol Rig actor.](https://dev.epicgames.com/community/api/documentation/image/9e49d9f3-1065-46a3-84fc-7df71c4e2c00?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9e49d9f3-1065-46a3-84fc-7df71c4e2c00?resizing_type=fit)

Below, there is a **Show Flag** toggle menu to identify the patrol rig waypoints for easy identification at edit time. Most show flag checkboxes have been selected. You can see details of how this is implemented in an editor-only visualizer component, `UParrotPatrolRigDebugVisualizer`.

[![Image of all the checked boxes for individual show flags (most are checked).](https://dev.epicgames.com/community/api/documentation/image/f94bc54a-f0e9-4ed9-86e1-8966f523e120?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f94bc54a-f0e9-4ed9-86e1-8966f523e120?resizing_type=fit)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Enemy Characters](/documentation/en-us/unreal-engine/enemy-characters-in-parrot-for-unreal-engine?application_version=5.7#enemycharacters)
* [The Enemy Animation Blueprints](/documentation/en-us/unreal-engine/enemy-characters-in-parrot-for-unreal-engine?application_version=5.7#theenemyanimationblueprints)
* [Animation Blueprint Templates](/documentation/en-us/unreal-engine/enemy-characters-in-parrot-for-unreal-engine?application_version=5.7#animationblueprinttemplates)
* [Animation Blueprints](/documentation/en-us/unreal-engine/enemy-characters-in-parrot-for-unreal-engine?application_version=5.7#animationblueprints)
* [The Enemy Pawn](/documentation/en-us/unreal-engine/enemy-characters-in-parrot-for-unreal-engine?application_version=5.7#theenemypawn)
* [The Enemy AI Controller](/documentation/en-us/unreal-engine/enemy-characters-in-parrot-for-unreal-engine?application_version=5.7#theenemyaicontroller)
* [Creating AI with Behavior Trees](/documentation/en-us/unreal-engine/enemy-characters-in-parrot-for-unreal-engine?application_version=5.7#creatingaiwithbehaviortrees)
* [Creating an Authorable Patrolling Waypoint System](/documentation/en-us/unreal-engine/enemy-characters-in-parrot-for-unreal-engine?application_version=5.7#creatinganauthorablepatrollingwaypointsystem)
