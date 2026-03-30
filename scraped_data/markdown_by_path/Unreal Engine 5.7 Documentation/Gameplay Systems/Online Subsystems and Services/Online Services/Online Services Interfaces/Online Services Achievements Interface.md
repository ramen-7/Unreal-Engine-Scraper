<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/achievements-interface-in-unreal-engine?application_version=5.7 -->

# Online Services Achievements Interface

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
9. Online Services Achievements Interface

# Online Services Achievements Interface

Read and update player achievements.

![Online Services Achievements Interface](https://dev.epicgames.com/community/api/documentation/image/6fae16b9-6f01-424d-aaf7-330f3c6ac319?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

An **achievement** is a goal or trophy, awarded outside of a game environment, unlocked or rewarded for accomplishing in-game tasks. Achievements give you a way to incentivize, challenge, and reward players. You can use them to:

* Guide players through a game
* Increase a game's replay value
* Support rivalries between players

The **Online Services Achievements Interface** provides you with tools to read achievement definitions as well as read and update the achievement state for players. The achievements interface does not handle the creation, deletion, or modification of achievements. Each online service has its own backend systems to manage these aspects of achievements.

You can set up the following mechanisms to unlock achievements depending on the interface's configuration:

* **Platform-service Managed**: Achievements are automatically unlocked by the platform service when associated stats reach predefined thresholds.
* **Title-managed (automatic)**: Achievements are automatically unlocked by the title when associated stats reach predefined thresholds. See the [Configure Automatic Title-Managed Achievements](https://dev.epicgames.com/documentation/en-us/unreal-engine/achievements-interface-in-unreal-engine?application_version=5.5) section below for more information.
* **Title-managed (manual)**: Achievements are manually unlocked by the title according to title logic and the `UnlockAchievements` function.

The availability of these three options varies depending on the online service implementation/platform that you use. Consult the documentation for your particular online service implementation for more information.

## API Overview

### Functions

The following table provides a high-level overview of the functions provided by the Achievements Interface:

| Function | Definition |
| --- | --- |
| [QueryAchievementDefinitions](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IAchievements/QueryAchievement-?application_version=5.5) | Query all achievement definitions for this title. |
| [GetAchievementIds](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IAchievements/GetAchievementIds?application_version=5.5) | Retrieve the achievement IDs for achievements cached by `QueryAchievementDefinitions`. |
| [GetAchievementDefinition](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IAchievements/GetAchievementDefinition?application_version=5.5) | Retrieve an achievement definition with the provided achievement ID cached by `QueryAchievementDefinitions`. |
| [QueryAchievementStates](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IAchievements/QueryAchievementStates?application_version=5.5) | Query the state of all achievements for the provided player. |
| [GetAchievementState](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IAchievements/GetAchievementState?application_version=5.5) | Retrieve the state of an achievement by ID for the provided player. |
| [UnlockAchievements](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IAchievements/UnlockAchievements?application_version=5.5) | Manually unlock provided achievements. |
| [DisplayAchievementUI](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IAchievements/DisplayAchievementUI?application_version=5.5) | Launch the platform UI for the provided achievement. |
| [OnAchievementStateUpdated](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IAchievements/OnAchievementSta-?application_version=5.5) | Event triggered when a player's achievement state changes. |

### Primary Structs

The achievements interface communicates its functionality primarily through three structs: [FAchievementDefinition](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/FAchievementDefinition?application_version=5.5), [FAchievementStatDefinition](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/FAchievementStatDefinition?application_version=5.5), and [FAchievementState](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/FAchievementState?application_version=5.5), in addition to the function specific structs for passing parameters and return values.

#### FAchievementDefinition

| Member | Type | Description |
| --- | --- | --- |
| `AchievementId` | `FString` | Unique achievement ID. |
| `UnlockedDisplayName` | `FText` | Localized display name of this achievement used once it is unlocked. |
| `UnlockedDescription` | `FText` | Localized description of this achievement used once it is unlocked. |
| `LockedDisplayName` | `FText` | Localized display name of this achievement used while it is locked. |
| `LockedDescription` | `FText` | Localized description of this achievement used while it is locked. |
| `FlavorText` | `FText` | Localized flavor text. |
| `UnlockedIconUrl` | `FString` | URL of the icon for this achievement used once it is unlocked. |
| `LockedIconUrl` | `FString` | URL of the icon for this achievement used while it is locked. |
| `bIsHidden` | `bool` | Whether or not this achievement is hidden until it is unlocked. |
| `StatDefinitions` | `TArray<FAchievementStatDefinition>` | The stats that relate to this achievement. |

#### FAchievementStatDefinition

| Member | Type | Description |
| --- | --- | --- |
| `StatId` | `FString` | Unique ID of the stat. |
| `UnlockThreshold` | `uint32` | Threshold value a user must meet with the associated stat for the achievement to auto unlock. |

#### FAchievementState

| Member | Type | Description |
| --- | --- | --- |
| `AchievementId` | `FString` | Achievement this state relates to. |
| `Progress` | `float` | Progress toward unlocking this achievement as a percentage between 0.0 and 1.0. Any value less than 1.0 means that the achievement is locked. A value of 1.0 means the achievement is unlocked. |
| `UnlockTime` | `FDateTime` | If unlocked, the time this achievement was unlocked. |

## Configure Automatic Title-Managed Achievements

The achievements interface does not require engine configuration when achievements are either platform-service managed or title-managed and manually unlocked. You must configure the engine if your achievement progress is title-managed and you want achievements to automatically unlock when one or more stats reach a predefined threshold.

For automatically-unlocking, title-managed achievements, the achievements interface works in conjunction with the [Stats Interface](https://dev.epicgames.com/documentation/en-us/unreal-engine/stats-interface-in-unreal-engine?application_version=5.5). You must configure the engine for this mechanism to set up unlock rules for achievements and establish conditions based on stats defined with stats interface configuration.

### General Syntax

C++

DefaultEngine.ini

[OnlineServices.Achievements]
bIsTitleManaged=true
!UnlockRules=ClearRules
+UnlockRules=(AchievementId=<AchievementId1>, Conditions=((StatName=<StatName>, UnlockThreshold="<Type>:<Value>"), ...))
+UnlockRules=(AchievementId=<AchievementId2>, Conditions=((StatName=<StatName>, UnlockThreshold="<Type>:<Value>"), ...))
...

Copy full snippet(6 lines long)

For automatically-unlocking, title-managed achievements to update based on stats changes, you must set the `bIsTitleManaged` flag to `true`. This flag configures the client to listen for the Online Services Stats Interface's `FStatsUpdated` event to automatically update achievement state in response to stats changes. The `bIsTitleManaged` flag's default value is `false`. If you do not set this flag to `true`, achievements will not automatically update based on stat changes configured in the achievements definitions in `DefaultEngine.ini`.

The list of `Conditions` within `UnlockRules` contains individual condition pairs. Achievements can depend on one or more stats coupled with an `UnlockThreshold`. An achievement unlocks only after every stat in its associated `Conditions` list has met or exceeded the predefined threshold.

#### Unlock Rules

| Field | Type | Description |
| --- | --- | --- |
| `AchievementId` | `String` | ID of the achievement that this unlock rule is associated with. |
| `Conditions` | `List` | List of conditions under which this achievement unlocks. |

#### Conditions

| Field | Type | Description |
| --- | --- | --- |
| `StatName` | `String` | Name of the stat to associate an unlock threshold for this achievement. |
| `UnlockThreshold` | Colon delimited `Type:Value` pair | A pair of the form `<Type>:<Value>` where `Type` is the type of this stat and `Value` is the threshold value at which this condition is met for this achievement to unlock. |

### Configuration Example

Below is an achievements interface example configuration with two different achievements. The first achievement is dependent on a single stat named `Total_Distance` that records the total distance a player has traveled in meters. The second achievement is dependent on three different stats to unlock: `Distance_Run`, `Distance_Swim`, and `Distance_Cycle`, all measured in meters.

C++

DefaultEngine.ini

```
[OnlineServices.Stats]
	!StatDefinitions=ClearDefinitions
	+StatDefinitions=(Name=Total_Distance, Id=0, ModifyMethod=Sum)
	+StatDefinitions=(Name=Distance_Run, Id=1, ModifyMethod=Sum)
	+StatDefinitions=(Name=Distance_Swim, Id=2, ModifyMethod=Sum)
	+StatDefinitions=(Name=Distance_Cycle, Id=3, ModifyMethod=Sum)

	[OnlineServices.Achievements]
	bIsTitleManaged=true
	!UnlockRules=ClearRules
```

Expand code  Copy full snippet(12 lines long)

## Read

The purpose of the achievements interface is to read achievement definitions and state. Below is a high-level description of the steps involved in reading definitions and state. For code examples, the process of querying and getting information using any Online Services interface is very similar to the example outlined in the [Stats Interface](https://dev.epicgames.com/documentation/en-us/unreal-engine/stats-interface-in-unreal-engine?application_version=5.5) documentation to query and get stats.

### Achievement Definition

The Achievements interface can read the definition of any achievements configured on the platform services by following these steps:

1. [QueryAchievementDefinitions](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IAchievements/QueryAchievement-?application_version=5.5) populates the local interface cache with achievement definitions.
2. [GetAchievementIds](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IAchievements/GetAchievementIds?application_version=5.5) retrieves the list of IDs for the cached achievements from step 1.
3. [GetAchievementDefinition](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IAchievements/GetAchievementDefinition?application_version=5.5) obtains the full definition associated with each ID from step 2.

The [FAchievementDefintion](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/FAchievementDefinition?application_version=5.5) struct represents achievement definitions. For platform service managed achievements, the definition includes the stats associated with the achievement and their unlock thresholds, above which, the achievement automatically unlocks.

### Achievement State

After you query and retrieve a player's achievement definitions as explained in the [Achievement Definition](https://dev.epicgames.com/documentation/en-us/unreal-engine/achievements-interface-in-unreal-engine?application_version=5.5) section, use `QueryAchievementStates` and `GetAchievementState` to read player achievement states:

1. [QueryAchievementStates](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IAchievements/QueryAchievementStates?application_version=5.5) populates the local interface cache with achievement state information.
2. [GetAchievementState](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IAchievements/GetAchievementState?application_version=5.5) retrieves the current progress toward unlocking the achievement if it is still locked, or the unlock time if the achievement is unlocked.

For title managed achievements, the progress is a binary 0.0 (locked) or 1.0 (unlocked). For platform-service managed achievements with stat-based unlock rules, the progress may accurately reflect the current progress toward the achievement as a percentage between 0.0 and 1.0.

## More Information

### Header File

Consult the `Achievements.h` header file directly for more information as needed. The Achievements Interface header file `Achievements.h` is located in the directory:

C++

Engine\Plugins\Online\OnlineServices\Source\OnlineServicesInterface\Public\Online

Copy full snippet(1 line long)

For instructions on how to obtain the UE source code, see our documentation on [Downloading Unreal Engine Source Code](https://dev.epicgames.com/documentation/en-us/unreal-engine/downloading-source-code-in-unreal-engine).

### Function Parameters and Return Types

See the [Functions](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-online-services-in-unreal-engine?application_version=5.5#functions) section of the Online Services Overview page for an explanation of function parameters and return types, including how to pass parameters and processing the results when functions return.

* [beta](https://dev.epicgames.com/community/search?query=beta)
* [programming](https://dev.epicgames.com/community/search?query=programming)
* [achievements](https://dev.epicgames.com/community/search?query=achievements)
* [online services](https://dev.epicgames.com/community/search?query=online%20services)
* [stats](https://dev.epicgames.com/community/search?query=stats)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [API Overview](/documentation/en-us/unreal-engine/achievements-interface-in-unreal-engine?application_version=5.7#api-overview)
* [Functions](/documentation/en-us/unreal-engine/achievements-interface-in-unreal-engine?application_version=5.7#functions)
* [Primary Structs](/documentation/en-us/unreal-engine/achievements-interface-in-unreal-engine?application_version=5.7#primary-structs)
* [FAchievementDefinition](/documentation/en-us/unreal-engine/achievements-interface-in-unreal-engine?application_version=5.7#f-achievement-definition)
* [FAchievementStatDefinition](/documentation/en-us/unreal-engine/achievements-interface-in-unreal-engine?application_version=5.7#f-achievement-stat-definition)
* [FAchievementState](/documentation/en-us/unreal-engine/achievements-interface-in-unreal-engine?application_version=5.7#f-achievement-state)
* [Configure Automatic Title-Managed Achievements](/documentation/en-us/unreal-engine/achievements-interface-in-unreal-engine?application_version=5.7#configure-automatic-title-managed-achievements)
* [General Syntax](/documentation/en-us/unreal-engine/achievements-interface-in-unreal-engine?application_version=5.7#general-syntax)
* [Unlock Rules](/documentation/en-us/unreal-engine/achievements-interface-in-unreal-engine?application_version=5.7#unlock-rules)
* [Conditions](/documentation/en-us/unreal-engine/achievements-interface-in-unreal-engine?application_version=5.7#conditions)
* [Configuration Example](/documentation/en-us/unreal-engine/achievements-interface-in-unreal-engine?application_version=5.7#configuration-example)
* [Read](/documentation/en-us/unreal-engine/achievements-interface-in-unreal-engine?application_version=5.7#read)
* [Achievement Definition](/documentation/en-us/unreal-engine/achievements-interface-in-unreal-engine?application_version=5.7#achievement-definition)
* [Achievement State](/documentation/en-us/unreal-engine/achievements-interface-in-unreal-engine?application_version=5.7#achievement-state)
* [More Information](/documentation/en-us/unreal-engine/achievements-interface-in-unreal-engine?application_version=5.7#more-information)
* [Header File](/documentation/en-us/unreal-engine/achievements-interface-in-unreal-engine?application_version=5.7#header-file)
* [Function Parameters and Return Types](/documentation/en-us/unreal-engine/achievements-interface-in-unreal-engine?application_version=5.7#function-parameters-and-return-types)
