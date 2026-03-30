<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/presence-interface-in-unreal-engine?application_version=5.7 -->

# Online Services Presence Interface

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
9. Online Services Presence Interface

# Online Services Presence Interface

Access the presence and joinability status of friends and followers.

![Online Services Presence Interface](https://dev.epicgames.com/community/api/documentation/image/913f73ea-28b8-4253-91e7-1489b021268b?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

When logged into an online service, you may want to look for information about your friends and other users you have met online. For example, on many online services, you can see whether other users are online, what game they are currently playing, if they are available to join matches, and so on. The **Online Services Presence Interface** encompasses all functionality related to platform-specific user states across online services, including querying and updating a user's presence as well as listening for changes.

This document provides an API overview and code examples as well as tips for converting code from the [Online Subsystem Presence Interface](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-presence-interface-in-unreal-engine).

## API Overview

### Functions

The following table provides a high-level description of the functions included in the Presence Interface.

| Function | Description |
| --- | --- |
| **Query** |  |
| [QueryPresence](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IPresence/QueryPresence?application_version=5.5) | Fetch the presence of the user with the supplied `TargetAccountId`. |
| [BatchQueryPresence](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IPresence/BatchQueryPresence?application_version=5.5) | Fetch the presence for every user in the supplied list of `TargetAccountIds`. |
| **Get** |  |
| [GetCachedPresence](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IPresence/GetCachedPresence?application_version=5.5) | Retrieve the presence of the user with the supplied `TargetAccountId` cached in the interface. |
| **Update** |  |
| [UpdatePresence](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IPresence/UpdatePresence?application_version=5.5) | Update the presence of the user. |
| [PartialUpdatePresence](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IPresence/PartialUpdatePresence?application_version=5.5) | Update the presence of the user with only the specified presence settings. |
| **Event Listening** |  |
| [OnPresenceUpdated](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IPresence/OnPresenceUpdated?application_version=5.5) | Event will trigger as a result of updates to a user's presence. |

### Enumeration Classes

The Presence Interface defines three enumeration classes that represent a user's status ([EUserPresenceStatus](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/UE__Online__EUserPresenceStatus?application_version=5.5)), joinability ([EUserPresenceJoinability](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/UE__Online__EUserPresenceJoinabi-?application_version=5.5)), and game status ([EUserPresenceGameStatus](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/UE__Online__EUserPresenceGameSta-?application_version=5.5)). These enumeration classes represent three primary members of the `FUserPresence` struct. For more information, refer to the [Primary Struct](https://dev.epicgames.com/documentation/en-us/unreal-engine/presence-interface-in-unreal-engine?application_version=5.5) section of this page.

#### EUserPresenceStatus

| Enumerator | Description |
| --- | --- |
| `Offline` | User is offline. |
| `Online` | User is online. |
| `Away` | User is away. |
| `ExtendedAway` | User has been away for at least two hours (may be platform dependent). |
| `DoNotDisturb` | User does not want to be disturbed. |
| `Unknown` | Default user presence status. |

#### EUserPresenceJoinability

| Enumerator | Description |
| --- | --- |
| `Public` | Anyone can discover and join this session. |
| `FriendsOnly` | Anyone trying to join must be a friend of a lobby member. |
| `InviteOnly` | Anyone trying to join must be invited first. |
| `Private` | User is not currently accepting invitations. |
| `Unknown` | Default user presence joinability status. |

#### EUserPresenceGameStatus

| Enumerator | Description |
| --- | --- |
| `PlayingThisGame` | User is playing the same game as you. |
| `PlayingOtherGame` | User is playing a different game than you. |
| `Unknown` | Default user presence game status. |

### Primary Struct

#### FUserPresence

The [FUserPresence](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/FUserPresence?application_version=5.5) struct is the primary object in the Presence interface and consists of all necessary information pertaining to a user's presence.

| Member | Type | Description |
| --- | --- | --- |
| `AccountId` | `FAccountId` | User whose presence this is. |
| `Status` | `EUserPresenceStatus` | User presence state. (Default value is `EUserPresenceStatus::Unknown`.) |
| `Joinability` | `EUserPresenceJoinability` | User session state. (Default value is `EUserPresenceJoinability::Unknown`.) |
| `GameStatus` | `EUserPresenceGameStatus` | User game state. (Default value is `EUserPresenceGameStatus::Unknown`.) |
| `StatusString` | `FString` | String representation of user presence state. |
| `RichPresenceString` | `FString` | Game-defined representation of the current game state. |
| `Properties` | `FPresenceProperties` | Session keys. |

The type `FPresenceProperties` is a typedef for `TMap<FString, FPresenceVariant>` where `FPresenceVariant` is an `FString`.

## Examples

We now provide an example demonstrating `UpdatePresence`, `QueryPresence`, and `GetPresence`. `UserA` updates their presence with the default platform services, then `UserB` queries the presence of `UserA` after it has been updated. If the query successfully returns, then `UserB` retrieves the presence of `UserA`.

### Code

C++

UserAPresence.cpp

```
UE::Online::IOnlineServicesPtr OnlineServices = UE::Online::GetServices();
UE::Online::IPresencePtr PresenceInterface = OnlineServices->GetPresenceInterface();

TSharedRef<UE::Online::FUserPresence> Presence = MakeShared<UE::Online::FUserPresence>();
Presence->AccountId = UserA;
Presence->Status = UE::Online::EUserPresenceStatus::Online;
Presence->Joinability = UE::Online::EUserPresenceJoinability::Public;
Presence->RichPresenceString = TEXT("Exploring the Great Citadel");
Presence->Properties.Add(TEXT("advanced_class"), TEXT("advanced_class_assassin"));
```

Expand code  Copy full snippet(26 lines long)

C++

UserBPresence.cpp

```
UE::Online::IOnlineServicesPtr OnlineServices = UE::Online::GetServices();
UE::Online::IPresencePtr PresenceInterface = OnlineServices->GetPresenceInterface();

PresenceInterface->QueryPresence({UserA})
.OnComplete([](const UE::Online::TOnlineResult<UE::Online::FQueryPresence> Result)
{
	if(Result.IsOk())
	{
		// we succeeded - now use GetPresence to actually view the presence object
```

Expand code  Copy full snippet(30 lines long)

### Walkthrough

1. Both users retrieve the default online services by calling `GetServices` with no parameters specified and access the Presence Interface:

   C++

   UserAPresence.cpp and UserBPresence.cpp

   ```
   |  |  |
   | --- | --- |
   |  | UE::Online::IOnlineServicesPtr OnlineServices = UE::Online::GetServices(); |
   |  | UE::Online::IPresencePtr PresenceInterface = OnlineServices->GetPresenceInterface(); |
   ```

   UE::Online::IOnlineServicesPtr OnlineServices = UE::Online::GetServices();
   UE::Online::IPresencePtr PresenceInterface = OnlineServices-&gt;GetPresenceInterface();

   Copy full snippet(2 lines long)
2. `UserA` initializes an `FUserPresence` struct named `Presence`. Notice that we are using two of the aforementioned enumerations provided by the Presence Interface: `EUserPresenceStatus` and `EUserPresenceJoinability`.

   C++

   UserAPresence.cpp

   ```
   |  |  |
   | --- | --- |
   |  | TSharedRef<UE::Online::FUserPresence> Presence = MakeShared<UE::Online::FUserPresence>(); |
   |  | Presence->AccountId = UserA; |
   |  | Presence->Status = UE::Online::EUserPresenceStatus::Online; |
   |  | Presence->Joinability = UE::Online::EUserPresenceJoinability::Public; |
   |  | Presence->RichPresenceString = TEXT("Exploring the Great Citadel"); |
   |  | Presence->Properties.Add(TEXT("advanced_class"), TEXT("advanced_class_assassin")); |
   ```

   TSharedRef&lt;UE::Online::FUserPresence&gt; Presence = MakeShared&lt;UE::Online::FUserPresence&gt;();
   Presence-&gt;AccountId = UserA;
   Presence-&gt;Status = UE::Online::EUserPresenceStatus::Online;
   Presence-&gt;Joinability = UE::Online::EUserPresenceJoinability::Public;
   Presence-&gt;RichPresenceString = TEXT(&quot;Exploring the Great Citadel&quot;);
   Presence-&gt;Properties.Add(TEXT(&quot;advanced\_class&quot;), TEXT(&quot;advanced\_class\_assassin&quot;));

   Copy full snippet(6 lines long)
3. `UserA` initializes an `FUpdatePresence::Params` struct named `Params` with the parameters that will be passed to `UpdatePresence`:

   C++

   UserAPresence.cpp

   ```
   |  |  |
   | --- | --- |
   |  | UE::Online::FUpdatePresence::Params Params; |
   |  | Params.LocalAccountId = AccountId; |
   |  | Params.Presence = Presence; |
   ```

   UE::Online::FUpdatePresence::Params Params;
   Params.LocalAccountId = AccountId;
   Params.Presence = Presence;

   Copy full snippet(3 lines long)
4. `UserA` calls `UpdatePresence` and processes the result with an `OnComplete` callback:

   C++

   UserAPresence.cpp

   ```
   PresenceInterface->UpdatePresence(MoveTemp(Params))
    .OnComplete([](const UE::Online::TOnlineResult<UE::Online::FUpdatePresence> Result)
    {
        if(Result.IsOk())
        {
            // we succeeded - UserB is now clear to query presence
        }
        else
        {
            // we failed - check the error state in Result.GetErrorValue();
   ```

   Expand code  Copy full snippet(12 lines long)
5. `UserB` queries the presence of `UserA`. Inside the queries' `OnComplete` callback, `UserB` first checks to ensure `QueryPresence` returned an "Ok" status. If it did, then `UserB` is safe to retrieve the presence of `UserA` and process the result or error of `GetPresence` accordingly:

   C++

   UserBPresence.cpp

   ```
   PresenceInterface->QueryPresence({UserA})
    .OnComplete([](const UE::Online::TOnlineResult<UE::Online::FQueryPresence> Result)
    {
        if(Result.IsOk())
        {
            // we succeeded - now use GetPresence to actually view the presence object

            UE::Online::TOnlineResult<UE::Online::FGetPresence> GetPresenceResult = PresenceInterface->GetPresence({UserB});
            if(GetPresenceResult.IsOk())
            {
   ```

   Expand code  Copy full snippet(23 lines long)

If all function calls return without error, `UserB` now sees the updated status of `UserA` and `UserB` can choose to make decisions based on this status. For example, `UserB` could access the `GetPresenceResult` to see `UserA` is online and their joinability status is public. Upon setting this status `UserB` could decide to join `UserA` and "Explore the Great Citadel" together.

## Converting Code from Online Subsystem

The [Online Services](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-services-in-unreal-engine) plugins are an updated version of the [Online Subsystem](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-in-unreal-engine) plugins and will exist alongside one another for the foreseeable future. The API functionality of the Online Services Presence Interface maps approximately one-to-one with the API functionality of the Online Subsystem Presence Interface. A few caveats include:

* `SetPresence` was renamed to `UpdatePresence` to better represent the function's asynchronicity.
* `UpdatePresence` and `QueryPresence` are no longer overloaded.
* We recommend using their renamed functions `PartialUpdatePresence` and `BatchQueryPresence` instead.

  + The overloads for `UpdatePresence` and `QueryPresence` were renamed to `PartialUpdatePresence` and `BatchQueryPresence`, respectively.
* `QueryPresence` was given the `bListenToChanges` parameter.

  + This adds a specific user to the `OnPresenceUpdated` event.
  + The parameter is set to true by default.

## More Information

### Header File

Consult the `Presence.h` header file directly for more information as needed. The Presence Interface header file `Presence.h` is located in the directory:

C++

```
Engine\Plugins\Online\OnlineServices\Source\OnlineServicesInterface\Public\Online
```

Engine\Plugins\Online\OnlineServices\Source\OnlineServicesInterface\Public\Online

Copy full snippet(1 line long)

For instructions on how to obtain the UE source code, refer to our documentation on [Downloading Unreal Engine Source Code](https://dev.epicgames.com/documentation/en-us/unreal-engine/downloading-source-code-in-unreal-engine).

### Function Parameters and Return Types

Refer to the [Functions](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-online-services-in-unreal-engine?application_version=5.5#functions) section of the Online Services Overview page for an explanation of function parameters and return types, including how to pass parameters and processing the results when functions return.

* [social](https://dev.epicgames.com/community/search?query=social)
* [beta](https://dev.epicgames.com/community/search?query=beta)
* [programming](https://dev.epicgames.com/community/search?query=programming)
* [presence](https://dev.epicgames.com/community/search?query=presence)
* [multiplayer](https://dev.epicgames.com/community/search?query=multiplayer)
* [online services](https://dev.epicgames.com/community/search?query=online%20services)
* [status](https://dev.epicgames.com/community/search?query=status)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [API Overview](/documentation/en-us/unreal-engine/presence-interface-in-unreal-engine?application_version=5.7#api-overview)
* [Functions](/documentation/en-us/unreal-engine/presence-interface-in-unreal-engine?application_version=5.7#functions)
* [Enumeration Classes](/documentation/en-us/unreal-engine/presence-interface-in-unreal-engine?application_version=5.7#enumeration-classes)
* [EUserPresenceStatus](/documentation/en-us/unreal-engine/presence-interface-in-unreal-engine?application_version=5.7#e-user-presence-status)
* [EUserPresenceJoinability](/documentation/en-us/unreal-engine/presence-interface-in-unreal-engine?application_version=5.7#e-user-presence-joinability)
* [EUserPresenceGameStatus](/documentation/en-us/unreal-engine/presence-interface-in-unreal-engine?application_version=5.7#e-user-presence-game-status)
* [Primary Struct](/documentation/en-us/unreal-engine/presence-interface-in-unreal-engine?application_version=5.7#primary-struct)
* [FUserPresence](/documentation/en-us/unreal-engine/presence-interface-in-unreal-engine?application_version=5.7#f-user-presence)
* [Examples](/documentation/en-us/unreal-engine/presence-interface-in-unreal-engine?application_version=5.7#examples)
* [Code](/documentation/en-us/unreal-engine/presence-interface-in-unreal-engine?application_version=5.7#code)
* [Walkthrough](/documentation/en-us/unreal-engine/presence-interface-in-unreal-engine?application_version=5.7#walkthrough)
* [Converting Code from Online Subsystem](/documentation/en-us/unreal-engine/presence-interface-in-unreal-engine?application_version=5.7#converting-code-from-online-subsystem)
* [More Information](/documentation/en-us/unreal-engine/presence-interface-in-unreal-engine?application_version=5.7#more-information)
* [Header File](/documentation/en-us/unreal-engine/presence-interface-in-unreal-engine?application_version=5.7#header-file)
* [Function Parameters and Return Types](/documentation/en-us/unreal-engine/presence-interface-in-unreal-engine?application_version=5.7#function-parameters-and-return-types)
