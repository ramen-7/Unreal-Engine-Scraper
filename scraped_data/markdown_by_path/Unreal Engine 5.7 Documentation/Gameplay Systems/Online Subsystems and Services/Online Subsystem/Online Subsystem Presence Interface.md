<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-presence-interface-in-unreal-engine?application_version=5.7 -->

# Online Subsystem Presence Interface

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
7. [Online Subsystem](/documentation/en-us/unreal-engine/online-subsystem-in-unreal-engine "Online Subsystem")
8. Online Subsystem Presence Interface

# Online Subsystem Presence Interface

Overview of the presence interface.

![Online Subsystem Presence Interface](https://dev.epicgames.com/community/api/documentation/image/c102c1f7-4dc5-4f36-b933-b6b3771e4c4c?resizing_type=fill&width=1920&height=335)

 On this page

When logged into an online service, users can often see information about their friends and other users they've met online, such as whether these users are online, what they're doing, if they're available to join matches, and so on.
The **Presence Interface** provides the Online Subsystem with access to these features.

## Presence Status

Most online services recognize several basic presence states for each user, such as "online", "offline", and "away", as well as game-specific states like "In the lobby" or "Playing a match on (Map)".
However, these settings are not always visible, or may be visible to some users but not others, due to service-specific privacy policies and account settings.
The Online Subsystem does not interact with these policies or settings, but the information that it retrieves will be affected by them.

### Defining Presence

The [FOnlineUserPresence](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineSubsystem/Interfaces/FOnlineUserPresence?application_version=5.5) class contains all information related to a user's presence.
In addition to basic information like whether or not the user is currently online, and whether or not the user is playing a game, the user's presence (using the [FOnlineUserPresenceStatus](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineSubsystem/Interfaces/FOnlineUserPresenceStatus?application_version=5.5) class) stores more in-depth information.
This generally includes a localized string for display, an enumerated value (of type [EOnlinePresenceState](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineSubsystem/Interfaces/EOnlinePresenceState__Type?application_version=5.5)) to describe the user's basic state, and a set of key-value pairs to hold any game-specific custom data, which can be used when building the exact presence display message.

### Retrieving Information About Other Users

The basic flow for collecting presence information about a specific user begins with making a request to the online service through `QueryPresence`, specifying that user by `FUniqueNetId`.
Once that operation finishes, the provided `FOnPresenceTaskCompleteDelegate` will be called, indicating the user and whether the request succeeded or failed.
If successful, the local presence information cache will contain up-to-date presence information, which is available through the `GetCachedPresence` function.

Some online services proactively notify the Online Subsystem about user presence.
On these services, although you don't actually have to call `QueryPresence` or wait for its delegate, the usual code flow should remain unchanged so that it will work across multiple services.

### Setting a User's Presence

The `SetPresence` function sets the presence status of a local user through the online service.
This is an asynchronous call due to the need to verify the new status with the online service, and a delegate of type `FOnPresenceTaskCompleteDelegate` will be called upon completion.
Presence status itself is described by the `FOnlineUserPresenceStatus` class.

* [programming](https://dev.epicgames.com/community/search?query=programming)
* [online subsystem](https://dev.epicgames.com/community/search?query=online%20subsystem)
* [presence](https://dev.epicgames.com/community/search?query=presence)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Presence Status](/documentation/en-us/unreal-engine/online-subsystem-presence-interface-in-unreal-engine?application_version=5.7#presence-status)
* [Defining Presence](/documentation/en-us/unreal-engine/online-subsystem-presence-interface-in-unreal-engine?application_version=5.7#defining-presence)
* [Retrieving Information About Other Users](/documentation/en-us/unreal-engine/online-subsystem-presence-interface-in-unreal-engine?application_version=5.7#retrieving-information-about-other-users)
* [Setting a User's Presence](/documentation/en-us/unreal-engine/online-subsystem-presence-interface-in-unreal-engine?application_version=5.7#setting-a-user-s-presence)
