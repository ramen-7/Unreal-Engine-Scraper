<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/actor-relevancy-in-unreal-engine?application_version=5.7 -->

# Actor Relevancy

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
6. [Networking and Multiplayer](/documentation/en-us/unreal-engine/networking-and-multiplayer-in-unreal-engine "Networking and Multiplayer")
7. [Programming Multiplayer Games](/documentation/en-us/unreal-engine/programming-network-multiplayer-games-for-unreal-engine "Programming Multiplayer Games")
8. Actor Relevancy

# Actor Relevancy

Determine whether an actor is currently relevant for replication to a connection.

![Actor Relevancy](https://dev.epicgames.com/community/api/documentation/image/871a9624-27b7-4893-9ff8-78a717a33f16?resizing_type=fill&width=1920&height=335)

 On this page

Unreal Engine levels can be very large. At any time, a player might only see a small fraction of the total number of actors in a level. Most of the actors are not visible or audible, nor do they have a significant effect on the current player. The set of actors the server determines are capable of affecting a client in any significant way are considered **relevant** for this client. The set of relevant actors is determined on a per-client, or, in networking terms, a per-connection basis. Unreal Engine only replicates actors to a client if they are relevant for that client.

The following image comparison showcase a contrived example that uses *distance-based* relevancy. The primary actor (in the middle of the frame) is set to have replicated actors remain relevant if they are within 300 centimeters (3 meters). In the before image, the secondary actor is within 300 cm, and is relevant. This means that the secondary actor is replicated to the primary actor’s connection and is visible. In the after image, the secondary actor has traveled beyond 300 cm from the primary actor; therefore, the actor is no longer relevant to the primary actor, is not replicated to the primary actor’s connection, and is not visible.

![Actor relevant](https://dev.epicgames.com/community/api/documentation/image/f8226a97-92d4-48f0-a3d4-c28254f266cc?resizing_type=fit&width=1920&height=1080)

![Actor not relevant](https://dev.epicgames.com/community/api/documentation/image/395c9fa9-f98a-4bd7-8a76-61be5a142333?resizing_type=fit&width=1920&height=1080)

Actor relevant

Actor not relevant

Dynamically spawned, replicated actors are destroyed on the client when they are no longer relevant. This is why the secondary actor is no longer visible to the primary actor in this case.

## Obtain an Actor’s Relevancy

The network driver determines whether an actor is relevant for a particular connection with a call to [AActor::IsNetRelevantFor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/IsNetRelevantFor?application_version=5.5). This is handled automatically by the network driver.

### Make an Actor Relevant

You can force any actor to be relevant by calling [AActor::ForceNetRelevant](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/ForceNetRelevant?application_version=5.5) in your `AActor`-derived class.

### Override Actor Relevancy

You can customize actor relevancy by overriding the virtual function `AActor::IsNetRelevantFor` in your `AActor`-derived class.

Use caution when overriding `AActor::IsNetRelevantFor`. This may have unintended consequences if you are not familiar with Unreal Engine's replication system.

## How Relevancy is Determined

The virtual function `AActor::IsNetRelevantFor` implements several tests to determine the set of actors that are relevant to a connection.

### Parameters

`AActor::IsNetRelevantFor` uses three parameters to determine whether the calling actor object is relevant:

| Parameter | Description |
| --- | --- |
| `RealViewer` | Client network object controlling the current actor for which relevancy is being checked. This is usually a Player Controller. |
| `ViewTarget` | Actor currently viewed or controlled by `RealViewer`. This is usually a Pawn. |
| `SrcLocation` | Source location of the controlling network object. This is used when distance-based relevancy is enabled. |

### Relevancy Logic

For a given actor and connection, the following tests are performed:

* If at least one of the following conditions hold, then the current actor is relevant for this connection:

  + The current actor is always relevant.
  + The current actor is owned by the current connection’s Pawn.
  + The current actor is owned by the current connection’s Player Controller.
  + The current actor is the current connection’s Pawn.
  + The current connection’s Pawn is the instigator of some action, such as noise or damage.
* If the following conditions hold, then the replication system uses the current actor’s owner’s relevancy to determine whether it is relevant for this connection:

  + The current actor has an owner.
  + The current actor is set to use its owner’s net relevancy.
* If the following conditions hold, then the current actor is not relevant for this connection:

  + The current actor is only relevant to its owner.
  + The current actor does not have an owner.
  + The current actor’s owner is not relevant.
* If the following condition holds, then the system uses the current actor’s base relevancy to determine whether it is relevant for this connection:

  + The current actor is attached to the skeleton of another actor.
* If the following conditions hold, then the current actor is not relevant for this connection:

  + The current actor is hidden.
  + The current actor does not have a root component or the root component does not have collision enabled.

    If the current actor has no root component, then `AActor::IsNetRelevantFor` logs a warning and asks if the actor should be always relevant.
* If the following conditions hold, then the current actor is relevant for this connection:

  + The Game Network Manager ([AGameNetworkManager](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AGameNetworkManager?application_version=5.5)) is set to use distance-based relevancy.
  + The current actor is within the relevancy distance.

This relevancy logic is for the base `AActor` class. Other `AActor`-derived classes may contain different network relevancy logic. For example, the `APawn` and `APlayerController` classes override `AActor::IsNetRelevantFor`. Therefore, they have different conditions for relevancy. See `Pawn.cpp` and `PlayerController.cpp` for more information.

## Customize Relevancy Settings

You can customize network relevancy settings for your `AActor`-derived class in the Replication section of the Unreal Editor Details Panel or in C++.

[![Edit relevancy settings in the Details Panel](https://dev.epicgames.com/community/api/documentation/image/10cc179d-d4fe-4157-8a7b-d3ba6bf31800?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/10cc179d-d4fe-4157-8a7b-d3ba6bf31800?resizing_type=fit)

## Relevancy Reference

The following tables provide functions and properties pertaining to actor relevancy that can be found in the `AActor` class:

### Functions

| Name | Description |
| --- | --- |
| [ForceNetRelevant](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/ForceNetRelevant?application_version=5.5) | Force this actor to be network relevant if it is not already relevant by default. |
| [IsNetRelevantFor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/IsNetRelevantFor?application_version=5.5) | Check if this actor is relevant for a specific network connection. |
| [IsRelevancyOwnerFor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/IsRelevancyOwnerFor?application_version=5.5) | Check if this actor is the owner when performing network relevancy checks for actors marked `bOnlyRelevantToOwner`. |
| [IsReplayRelevantFor](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/IsRelevancyOwnerFor?application_version=5.5) | Check if this actor is relevant for recorded replay. |
| [IsWithinNetRelevancyDistance](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/IsWithinNetRelevancyDistance?application_version=5.5) | Check if the square of the distance between the given source location and this actor’s location is within `NetCullDistanceSquared`. |

### Properties

| Name | Description |
| --- | --- |
| [bAlwaysRelevant](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor?application_version=5.5) | Always relevant for network replication. Overrides `bOnlyRelevantToOwner`. |
| [bNetUseOwnerRelevancy](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor?application_version=5.5) | If this actor has a valid owner, call the owner's `IsNetRelevantFor` and `GetNetPriority`. |
| [bOnlyRelevantToOwner](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/bOnlyRelevantToOwner?application_version=5.5) | If true, this actor is only relevant to its owner. |
| [bRelevantForNetworkReplays](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor?application_version=5.5) | If true, this actor is replicated to network replays. Default true. |
| [NetCullDistanceSquared](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor?application_version=5.5) | Square of the maximum distance from the client’s viewport that this actor is relevant and replicates. |
| [Owner](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor?application_version=5.5) | Owner of this actor. Used for replication with `bNetUseOwnerRelevancy` and `bOnlyRelevantToOwner`. |

* [programming](https://dev.epicgames.com/community/search?query=programming)
* [networking](https://dev.epicgames.com/community/search?query=networking)
* [relevancy](https://dev.epicgames.com/community/search?query=relevancy)
* [isnetrelevantfor](https://dev.epicgames.com/community/search?query=isnetrelevantfor)
* [netculldistance](https://dev.epicgames.com/community/search?query=netculldistance)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Obtain an Actor’s Relevancy](/documentation/en-us/unreal-engine/actor-relevancy-in-unreal-engine?application_version=5.7#obtain-an-actor-s-relevancy)
* [Make an Actor Relevant](/documentation/en-us/unreal-engine/actor-relevancy-in-unreal-engine?application_version=5.7#make-an-actor-relevant)
* [Override Actor Relevancy](/documentation/en-us/unreal-engine/actor-relevancy-in-unreal-engine?application_version=5.7#override-actor-relevancy)
* [How Relevancy is Determined](/documentation/en-us/unreal-engine/actor-relevancy-in-unreal-engine?application_version=5.7#how-relevancy-is-determined)
* [Parameters](/documentation/en-us/unreal-engine/actor-relevancy-in-unreal-engine?application_version=5.7#parameters)
* [Relevancy Logic](/documentation/en-us/unreal-engine/actor-relevancy-in-unreal-engine?application_version=5.7#relevancy-logic)
* [Customize Relevancy Settings](/documentation/en-us/unreal-engine/actor-relevancy-in-unreal-engine?application_version=5.7#customize-relevancy-settings)
* [Relevancy Reference](/documentation/en-us/unreal-engine/actor-relevancy-in-unreal-engine?application_version=5.7#relevancy-reference)
* [Functions](/documentation/en-us/unreal-engine/actor-relevancy-in-unreal-engine?application_version=5.7#functions)
* [Properties](/documentation/en-us/unreal-engine/actor-relevancy-in-unreal-engine?application_version=5.7#properties)
