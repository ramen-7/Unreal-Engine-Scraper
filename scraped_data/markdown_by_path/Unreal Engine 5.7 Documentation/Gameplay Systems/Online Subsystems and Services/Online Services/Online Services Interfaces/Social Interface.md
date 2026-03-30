<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/social-interface-in-unreal-engine?application_version=5.7 -->

# Social Interface

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
6. [Online Subsystems and Services](/documentation/en-us/unreal-engine/online-subsystems-and-services-in-unreal-engine "Online Subsystems and Services")
7. [Online Services](/documentation/en-us/unreal-engine/online-services-in-unreal-engine "Online Services")
8. [Online Services Interfaces](/documentation/en-us/unreal-engine/online-services-interfaces-in-unreal-engine "Online Services Interfaces")
9. Social Interface

# Social Interface

Manage relationships with friends and blocked users.

![Social Interface](https://dev.epicgames.com/community/api/documentation/image/1fcee29a-511c-4538-869e-9b3802a2c0a6?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

The **Online Services Social Interface** manages relationships between users. This includes:

* Retrieving and viewing a player's friends list.
* Sending friend invites.
* Accepting/Rejecting friend invites.
* Viewing a list of blocked players.
* Blocking other players.

## API Overview

### Functions

The following table provides a high-level overview of the functions provided by the social interface:

| Function | Description |
| --- | --- |
| **View** |  |
| [QueryFriends](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/ISocial/QueryFriends?application_version=5.5) | Query the player's friends list. |
| [GetFriends](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/ISocial/GetFriends?application_version=5.5) | Retrieve a friends list cached by `QueryFriends`. |
| **Invite** |  |
| [SendFriendInvite](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/ISocial/SendFriendInvite?application_version=5.5) | Send a friend invite. |
| [AcceptFriendInvite](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/ISocial/AcceptFriendInvite?application_version=5.5) | Accept a friend invite. |
| [RejectFriendInvite](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/ISocial/RejectFriendInvite?application_version=5.5) | Reject a friend invite. |
| **Block** |  |
| [QueryBlockedUsers](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/ISocial/QueryBlockedUsers?application_version=5.5) | Query the blocked users list. |
| [GetBlockedUsers](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/ISocial/GetBlockedUsers?application_version=5.5) | Retrieve blocked users list cached by `QueryBlockedUsers`. |
| [BlockUser](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/ISocial/BlockUser?application_version=5.5) | Block a specified user. |
| **Event Listening** |  |
| [OnRelationshipUpdated](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/ISocial/OnRelationshipUpdated?application_version=5.5) | Event triggered by updating friends list. |

### Primary Struct

The social interface communicates its functionality primarily through the [FFriend](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/FFriend?application_version=5.5) struct in addition to the function specific structs for passing parameters and return values.

#### FFriend

| Member | Type | Description |
| --- | --- | --- |
| `FriendId` | `FAccountId` | Account ID of this friend. |
| `DisplayName` | `FString` | Display the name of this friend. |
| `Nickname` | `FString` | Local nickname for this friend.  Consult the documentation for your platform's online services for availability. |
| `Relationship` | `ERelationship` | Relationship to this friend. |

### Enumerated Classes

The [ERelationship](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/UE__Online__ERelationship?application_version=5.5) enumerated class holds the relationship status between the local user and the online user represented by the `FFriend` struct through which it is accessed.

#### ERelationship

| Value | Description |
| --- | --- |
| `Friend` | Friend |
| `NotFriend` | Not a friend |
| `InviteSent` | Invite sent to a user. |
| `InviteReceived` | Invite received from a user. |
| `Blocked` | Local user has blocked this user. |

## Process Flow

### View Friends

Upon starting your game, the player views which friends are online. To accomplish this, `QueryFriends` caches the player's friends list with the social interface, then `GetFriends` retrieves the previously cached friends list for reading. The player can now view their friends list to decide whether to invite their friends to join a lobby and enter a game session together.

### Invite Friends

After playing with their friends and other online players, the player meets several other players they enjoy playing with. The player decides to send friend invites to two of these online players. `SendFriendInvite` sends a friendship invitation to a single provided player each time it is called. One of the online players sees the invitation and rejects it. The game calls `RejectFriendInvite` to reject the player's invitation.

Meanwhile, the second online player accepts the invitation. A call to `AcceptFriendInvite` accepts the player's invitation. This friendship acceptance triggers an `OnRelationshipUpdated` event for both the player who sent the invitation and the online player who accepted the invitation.

### Block Users

While playing with their new friend, the player meets another online player. This time, the player decides they do not wish to interact with this online player in the future. The player proceeds to block this online player. The player can see the online players they have blocked by querying their blocked list. `QueryBlockedUsers` caches the information in the interface and a subsequent call to `GetBlockedUsers` retrieves the list of blocked players. If the online player in question does not appear in this list, a call to `BlockUser` adds the online player to the player's blocked list.

Depending on your platform, the Invite and Block APIs may bring up a platform dialogue to perform the associated action. Consult the documentation for your particular platform for more information.

## Converting Code from Online Subsystem

The Online Services Social Interface is responsible for all code previously handled by the [Online Subsystem](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-in-unreal-engine) [Friends Interface](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-friends-interface-in-unreal-engine?application_version=5.5).

## More Information

### Header File

Consult the `Social.h` header file directly for more information as needed. The social interface header file `Social.h` is located in the directory:

C++

```
Engine\Plugins\Online\OnlineServices\Source\OnlineServicesInterface\Public\Online
```

Engine\Plugins\Online\OnlineServices\Source\OnlineServicesInterface\Public\Online

Copy full snippet(1 line long)

For instructions on how to obtain the UE source code, see our documentation on [Downloading Unreal Engine Source Code](https://dev.epicgames.com/documentation/en-us/unreal-engine/downloading-source-code-in-unreal-engine).

### Function Parameters and Return Types

See the [Functions](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-online-services-in-unreal-engine?application_version=5.5#functions) section of the Online Services Overview page for an explanation of function parameters and return types, including how to pass parameters and processing the results when functions return.

* [social](https://dev.epicgames.com/community/search?query=social)
* [beta](https://dev.epicgames.com/community/search?query=beta)
* [programming](https://dev.epicgames.com/community/search?query=programming)
* [online services](https://dev.epicgames.com/community/search?query=online%20services)
* [friends](https://dev.epicgames.com/community/search?query=friends)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [API Overview](/documentation/en-us/unreal-engine/social-interface-in-unreal-engine?application_version=5.7#api-overview)
* [Functions](/documentation/en-us/unreal-engine/social-interface-in-unreal-engine?application_version=5.7#functions)
* [Primary Struct](/documentation/en-us/unreal-engine/social-interface-in-unreal-engine?application_version=5.7#primary-struct)
* [FFriend](/documentation/en-us/unreal-engine/social-interface-in-unreal-engine?application_version=5.7#f-friend)
* [Enumerated Classes](/documentation/en-us/unreal-engine/social-interface-in-unreal-engine?application_version=5.7#enumerated-classes)
* [ERelationship](/documentation/en-us/unreal-engine/social-interface-in-unreal-engine?application_version=5.7#e-relationship)
* [Process Flow](/documentation/en-us/unreal-engine/social-interface-in-unreal-engine?application_version=5.7#process-flow)
* [View Friends](/documentation/en-us/unreal-engine/social-interface-in-unreal-engine?application_version=5.7#view-friends)
* [Invite Friends](/documentation/en-us/unreal-engine/social-interface-in-unreal-engine?application_version=5.7#invite-friends)
* [Block Users](/documentation/en-us/unreal-engine/social-interface-in-unreal-engine?application_version=5.7#block-users)
* [Converting Code from Online Subsystem](/documentation/en-us/unreal-engine/social-interface-in-unreal-engine?application_version=5.7#converting-code-from-online-subsystem)
* [More Information](/documentation/en-us/unreal-engine/social-interface-in-unreal-engine?application_version=5.7#more-information)
* [Header File](/documentation/en-us/unreal-engine/social-interface-in-unreal-engine?application_version=5.7#header-file)
* [Function Parameters and Return Types](/documentation/en-us/unreal-engine/social-interface-in-unreal-engine?application_version=5.7#function-parameters-and-return-types)
