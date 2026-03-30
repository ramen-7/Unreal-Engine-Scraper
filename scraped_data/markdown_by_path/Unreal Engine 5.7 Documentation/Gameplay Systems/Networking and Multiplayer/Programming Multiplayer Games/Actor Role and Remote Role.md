<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/actor-role-and-remote-role-in-unreal-engine?application_version=5.7 -->

# Actor Role and Remote Role

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
8. Actor Role and Remote Role

# Actor Role and Remote Role

Determine how much control this game instance has over an actor.

![Actor Role and Remote Role](https://dev.epicgames.com/community/api/documentation/image/a953f5dc-7fb6-4816-9c58-44586eb5f191?resizing_type=fill&width=1920&height=335)

 On this page

In networked gameplay, an actor's **role** and **remote role** determine which machine has the authority to change the actor's state and perform remote procedure calls. These properties help you answer the following questions about an actor in your multiplayer game:

* Is this actor replicated or not?
* Who has authority over this actor?
* What is the replication role for this actor?

Actor role and remote role are not the same as ownership! For more information, see [Actors and their Owning Connections](https://dev.epicgames.com/documentation/en-us/unreal-engine/actor-owner-and-owning-connection-in-unreal-engine?application_version=5.5).

## View an Actor's Role and Remote Role

You can see the current role and remote role of an actor in the Unreal Editor's Details panel:

[![Sample Role and Remote Role](https://dev.epicgames.com/community/api/documentation/image/e91b5836-c582-4347-b229-810ce17e5c06?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e91b5836-c582-4347-b229-810ce17e5c06?resizing_type=fit)

Sample Role and Remote Role

An actor's role and remote role can also be obtained in C++ or Blueprints.

### Get Actor's Role

To determine how much control the local machine has over this actor, call [AActor::GetLocalRole](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/GetLocalRole?application_version=5.5):

C++

```
|  |  |
| --- | --- |
|  | AMyActor* MyActor; |
|  | ... |
|  | // Once you have a valid Actor pointer... |
|  | const ENetRole LocalRole = MyActor->GetLocalRole(); |
|  | // LocalRole contains the Actor's Role |
|  | ... |
```

AMyActor\* MyActor;
...
// Once you have a valid Actor pointer...
const ENetRole LocalRole = MyActor->GetLocalRole();
// LocalRole contains the Actor's Role
...

Copy full snippet(6 lines long)

### Get Actor's Remote Role

To determine how much control a remote machine has over this actor, call [AActor::GetRemoteRole](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/GetRemoteRole?application_version=5.5):

C++

```
|  |  |
| --- | --- |
|  | AMyActor* MyActor; |
|  | ... |
|  | // Once you have a valid Actor pointer... |
|  | const ENetRole RemoteRole = MyActor->GetRemoteRole(); |
|  | // RemoteRole contains the Actor's RemoteRole |
|  | ... |
```

AMyActor\* MyActor;
...
// Once you have a valid Actor pointer...
const ENetRole RemoteRole = MyActor->GetRemoteRole();
// RemoteRole contains the Actor's RemoteRole
...

Copy full snippet(6 lines long)

## Actor Role States

Actor role and remote role are represented by a state of the `ENetRole` enumeration class (defined in `EngineTypes.h`). The following table lists and describes these states:

| Net Role State | Description |
| --- | --- |
| `ROLE_None` | No role. This actor is not replicated. |
| `ROLE_SimulatedProxy` | Simulated proxy of this actor. This actor simulates the true state but has no authority to change the state or call remote functions. |
| `ROLE_AutonomousProxy` | Autonomous proxy of this actor. This actor simulates the true state and has the authority to change the state and call remote functions. |
| `ROLE_Authority` | Authoritative control of this actor. This actor holds the true state for networking and has the authority to change the state and call functions. This actor is also in charge of keeping track of property changes and replicating them to connected clients. |

## Matrix of Roles for Client-Server

Unreal Engine uses the client-server model for networking. As a result, the server always has authority over replicated actors. This means that only the server should ever see `ROLE_Authority` for replicated actors. Non-replicated actors can have a local role of `ROLE_Authority` on clients and a remote role of `ROLE_None`.

The following table provides a matrix of local role and remote role, whether a server or client is witnessing this role combination, and a description of what this combination means:

| Local Role | Remote Role | Server or Client | Description |
| --- | --- | --- | --- |
| `ROLE_Authority` | `ROLE_AutonomousProxy` | Server | This actor pawn is controlled by one of the connected clients. |
| `ROLE_AutonomousProxy` | `ROLE_Authority` | Client | This actor pawn is controlled by this connected client. |
| `ROLE_SimulatedProxy` | `ROLE_Authority` | Client | This actor pawn is controlled by one of the other connected clients.  Replicated actors that are not controlled by any client can also have this role combination. |
| `ROLE_Authority` | `ROLE_None` | Client | This is a non-replicated actor. |

## Actor Replication Simulation

Servers do not replicate all actors every update because that would take too much bandwidth and CPU resources. Instead, the server replicates actors at the frequency specified on the [AActor::NetUpdateFrequency](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor?application_version=5.5) property. This means that some time passes on the client between actor updates. This could result in actors with a character movement component looking choppy and sporadic. To compensate for this, the client simulates character movement between updates.

For more information about replication simulation and character movement, see [Networked Movement in the Character Movement Component](https://dev.epicgames.com/documentation/en-us/unreal-engine/understanding-networked-movement-in-the-character-movement-component-for-unreal-engine?application_version=5.5) documentation.

## Role and Remote Role Reference

### Functions

| Name | Description |
| --- | --- |
| [CopyRemoteRoleFrom](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/CopyRemoteRoleFrom?application_version=5.5) | Copy remote role from another actor and add this actor to the list of network actors if necessary. |
| [ExchangeNetRoles](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/ExchangeNetRoles?application_version=5.5) | Swap role and remote role if on client. |
| [GetLocalRole](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/GetLocalRole?application_version=5.5) | Return how much control the local machine has over this actor. |
| [GetRemoteRole](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/GetRemoteRole?application_version=5.5) | Return how much control the remote machine has over this actor. |
| [GetRolePropertyName](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/GetRolePropertyName?application_version=5.5) | Get the property name for role. |
| [GetTearOff](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/GetTearOff?application_version=5.5) | If true, this actor is no longer replicated to new clients and is "torn off" (becomes `ENetRole::ROLE_Authority`) on clients to which it was being replicated. |
| [PostNetReceiveRole](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/PostNetReceiveRole?application_version=5.5) | Called immediately after a new role is received from the remote machine. |
| [SetRemoteRoleForBackwardsCompat](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/SetRemoteRoleForBackwardsCompat?application_version=5.5) | Used in the constructor of classes that must set the remote role for backwards compatibility purposes. |
| [SetRole](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/SetRole?application_version=5.5) | Set the value of role without causing other side effects to this instance. |
| [SwapRoles](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/SwapRoles?application_version=5.5) | Swap the role and remote role for this actor.  Use caution and only call this function if you understand the side effects. |

### Properties

| Name | Description |
| --- | --- |
| [bExchangedRoles](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/bExchangedRoles?application_version=5.5) | Whether role and remote role have been exchanged on the client. |

* [programming](https://dev.epicgames.com/community/search?query=programming)
* [networking](https://dev.epicgames.com/community/search?query=networking)
* [role](https://dev.epicgames.com/community/search?query=role)
* [remote role](https://dev.epicgames.com/community/search?query=remote%20role)
* [simulated](https://dev.epicgames.com/community/search?query=simulated)
* [autonomous](https://dev.epicgames.com/community/search?query=autonomous)
* [authority](https://dev.epicgames.com/community/search?query=authority)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [View an Actor's Role and Remote Role](/documentation/en-us/unreal-engine/actor-role-and-remote-role-in-unreal-engine?application_version=5.7#view-an-actor-s-role-and-remote-role)
* [Get Actor's Role](/documentation/en-us/unreal-engine/actor-role-and-remote-role-in-unreal-engine?application_version=5.7#get-actor-s-role)
* [Get Actor's Remote Role](/documentation/en-us/unreal-engine/actor-role-and-remote-role-in-unreal-engine?application_version=5.7#get-actor-s-remote-role)
* [Actor Role States](/documentation/en-us/unreal-engine/actor-role-and-remote-role-in-unreal-engine?application_version=5.7#actor-role-states)
* [Matrix of Roles for Client-Server](/documentation/en-us/unreal-engine/actor-role-and-remote-role-in-unreal-engine?application_version=5.7#matrix-of-roles-for-client-server)
* [Actor Replication Simulation](/documentation/en-us/unreal-engine/actor-role-and-remote-role-in-unreal-engine?application_version=5.7#actor-replication-simulation)
* [Role and Remote Role Reference](/documentation/en-us/unreal-engine/actor-role-and-remote-role-in-unreal-engine?application_version=5.7#role-and-remote-role-reference)
* [Functions](/documentation/en-us/unreal-engine/actor-role-and-remote-role-in-unreal-engine?application_version=5.7#functions)
* [Properties](/documentation/en-us/unreal-engine/actor-role-and-remote-role-in-unreal-engine?application_version=5.7#properties)
