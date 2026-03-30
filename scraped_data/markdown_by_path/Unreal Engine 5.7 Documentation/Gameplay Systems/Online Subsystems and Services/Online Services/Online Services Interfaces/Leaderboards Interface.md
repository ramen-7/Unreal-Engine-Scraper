<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine?application_version=5.7 -->

# Leaderboards Interface

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
9. Leaderboards Interface

# Leaderboards Interface

Display and update leaderboards from within your game.

![Leaderboards Interface](https://dev.epicgames.com/community/api/documentation/image/5fd64063-590b-459c-a5df-66b25e744d1d?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

A **leaderboard** is a list of players ranked by an in-game statistic. Leaderboards encourage competition between players, their friends, and the rest of the world, for the top score in your game. Games can feature multiple modes that award scores. Each of these modes can have its own leaderboard or leaderboards.

Leaderboards can rank entries in the following ways:

* **Ascending**: Lower scores are ranked better than higher scores.

  + The Fortnite wins leaderboard is organized in descending order since more wins is desirable.
* **Descending**: Higher scores are ranked better than lower scores.

  + Lap time leaderboards in racing games are organized in ascending order since faster lap times are more desirable.

The **Online Services Leaderboards Interface** provides developers with tools to display and update leaderboards from within their games. Leaderboard data can be very large since each leaderboard your game supports could have an entry for every user account that has played your game. For this reason, the leaderboards interface retrieves data in chunks. Games that implement the leaderboards interface can request chunks of the leaderboard in different ways as described below in the [Functions](https://dev.epicgames.com/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine?application_version=5.5#functions) section and, in more detail, in the [Read Leaderboard Entries](https://dev.epicgames.com/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine?application_version=5.5) section.

## API Overview

### Functions

The following table provides a high-level overview of the functions provided by the leaderboards interface:

| Function | Description |
| --- | --- |
| [ReadEntriesForUsers](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/ILeaderboards/ReadEntriesForUsers?application_version=5.5) | Read leaderboard entries for specific users. |
| [ReadEntriesAroundRank](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/ILeaderboards/ReadEntriesAroundRank?application_version=5.5) | Read leaderboard entries around a specified rank index. |
| [ReadEntriesAroundUser](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/ILeaderboards/ReadEntriesAroundUser?application_version=5.5) | Read leaderboard entries around the specified user. |

### Primary Struct

The leaderboards interface's functionality is primarily communicated through the [FLeaderboardEntry](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/FLeaderboardEntry?application_version=5.5) struct:

| Member | Type | Description |
| --- | --- | --- |
| `AccountId` | `FAccountId` | Account ID of this leaderboard entry. |
| `Rank` | `int32` | Rank of this account in this leaderboard. |
| `Score` | `int64` | Score of this account in this leaderboard. |

## Configuration

To update a leaderboard score using stats, you must configure the leaderboards interface in the engine configuration files, such as `DefaultEngine.ini`. The leaderboards interface works in conjunction with the [Stats Interface](https://dev.epicgames.com/documentation/en-us/unreal-engine/stats-interface-in-unreal-engine?application_version=5.5) to track stats for leaderboard rankings.

### General Syntax

C++

DefaultEngine.ini

```
|  |  |
| --- | --- |
|  | [OnlineServices.Leaderboards] |
|  | bIsTitleManaged=true |
|  | !LeaderboardDefinitions=ClearDefinitions |
|  | +LeaderboardDefinitions=(Name=<StatName0>, Id=<Id0>, UpdateMethod=[KeepBest | Force], OrderMethod=[Ascending | Descending]) |
|  | +LeaderboardDefinitions=(Name=<StatName1>, Id=<Id1>, UpdateMethod=[KeepBest | Force], OrderMethod=[Ascending | Descending]) |
|  | ... |
```

[OnlineServices.Leaderboards]
bIsTitleManaged=true
!LeaderboardDefinitions=ClearDefinitions
+LeaderboardDefinitions=(Name=<StatName0>, Id=<Id0>, UpdateMethod=[KeepBest | Force], OrderMethod=[Ascending | Descending])
+LeaderboardDefinitions=(Name=<StatName1>, Id=<Id1>, UpdateMethod=[KeepBest | Force], OrderMethod=[Ascending | Descending])
...

Copy full snippet(6 lines long)

In order for leaderboards to update based on stats changes, you must set the `bIsTitleManaged` flag to `true`. This flag configures the client to listen for the Online Services Stats Interface's `FStatsUpdated` event to automatically update leaderboards in response to stats changes. The `bIsTitleManaged` flag's default value is `false`. If you do not set this flag to `true`, leaderboards will not automatically update based on stat changes configured in the leaderboard definitions in `DefaultEngine.ini`.

The following [Leaderboard Definition](https://dev.epicgames.com/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine?application_version=5.5) table explains the syntax for adding a leaderboard definition to an engine configuration file.

#### Leaderboard Definition

| Field | Type | Description |
| --- | --- | --- |
| `Name` | `String` | Name of the stat that determines ranking. This must be the same as the name of a stat configured with the stats interface. |
| `Id` | `int` | ID number to associate with this leaderboard. This is not related to the stats ID from the stats interface. |
| `UpdateMethod` | `KeepBest` or `Force` | The method used to update this leaderboard entry. `KeepBest` keeps the best value for this stat that has been achieved. `Force` updates the leaderboard entry to the latest stat value, regardless of how it changes a player's rank. |
| `OrderMethod` | `Ascending` or `Descending` | Determines whether a lower or higher stat value gives a better ranking. `Ascending` means a lower stat value gives a higher rank. `Descending` means a higher stat value gives a higher rank. |

### Configuration Example

Suppose that you have a simple game with a single leaderboard titled "Total Game Points" tracked by a statistic of the same name configured with the stats interface:

C++

DefaultEngine.ini

```
|  |  |
| --- | --- |
|  | [OnlineServices.Stats] |
|  | !StatDefinitions=ClearDefinitions |
|  | +StatDefinitions=(Name=Total_Game_Points, Id=0, ModifyMethod=Sum) |
|  |  |
|  | [OnlineServices.Leaderboards] |
|  | bIsTitleManaged=true |
|  | !LeaderboardDefinitions=ClearDefinitions |
|  | +LeaderboardDefinitions=(Name=Total_Game_Points, Id=0, UpdateMethod=KeepBest, OrderMethod=Descending) |
```

[OnlineServices.Stats]
!StatDefinitions=ClearDefinitions
+StatDefinitions=(Name=Total\_Game\_Points, Id=0, ModifyMethod=Sum)
[OnlineServices.Leaderboards]
bIsTitleManaged=true
!LeaderboardDefinitions=ClearDefinitions
+LeaderboardDefinitions=(Name=Total\_Game\_Points, Id=0, UpdateMethod=KeepBest, OrderMethod=Descending)

Copy full snippet(8 lines long)

In this configuration, the leaderboard:

* keeps the best score for the `Total_Game_Points` statistic for each player, and
* is organized in descending order, since higher point totals are more desirable.

## Read Leaderboard Entries

There are three different ways to read leaderboard entries with the leaderboards interface. Leaderboard entries can be read in the following ways:

* [For specific users](https://dev.epicgames.com/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine?application_version=5.5)
* [Around a particular rank](https://dev.epicgames.com/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine?application_version=5.5)
* [Around a given user](https://dev.epicgames.com/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine?application_version=5.5)

Below we show a visual representation of what each of these methods retrieves with the "Total Game Points" leaderboard configured in the [configuration example](https://dev.epicgames.com/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine?application_version=5.5) above.

### For Specific Users

Use the `ReadEntriesForUsers` function to retrieve leaderboard entries for specific users. This function takes in a list of user IDs for the individual users whose rank you wish to query.

#### Example

Suppose that you have the leaderboard below titled "Total Game Points" and call `ReadEntriesForUsers` with the following parameters:

C++

```
|  |  |
| --- | --- |
|  | UE::Online::FReadEntriesForUsers::Params Params; |
|  | Params.LocalAccountId = "LLV54WB-3C678QQ"; |
|  | Params.AccountIds = {"9P8H4GQ-HNO5GA4", "3CN9H8E-VNO3G3C", "OHB8RA2-OHSEBSE"}; |
|  | Params.BoardName = TEXT("Total Game Points"); |
```

UE::Online::FReadEntriesForUsers::Params Params;
Params.LocalAccountId = "LLV54WB-3C678QQ";
Params.AccountIds = {"9P8H4GQ-HNO5GA4", "3CN9H8E-VNO3G3C", "OHB8RA2-OHSEBSE"};
Params.BoardName = TEXT("Total Game Points");

Copy full snippet(4 lines long)

If the call returns successfully, you can access the columns marked as retrieved in the returned `TOnlineResult`:

| Total Game Points |  |  |  |
| --- | --- | --- | --- |
| **Account ID** | **Rank** | **Score** | **Retrieved?** |
| 3CN9H8E-VNO3G3C | 1 | 1,901 | Y |
| LLV54WB-3C678QQ | 2 | 151 |  |
| OHB8RA2-OHSEBSE | 3 | 17 | Y |
| 9P8H4GQ-HNO5GA4 | 4 | 3 | Y |
| 9HQGQER-ILASDFH | 5 | 1 |  |

### Around a Particular Rank

Use the `ReadEntriesAroundRank` function to retrieve leaderboard entries around a particular leaderboard rank. This function takes in:

* a rank at which you want to start reading leaderboard entries, and
* a limit for the number of entries to read.

#### Example

Suppose that you have the leaderboard below titled Total Game Points and call `ReadEntriesAroundRank` with the following parameters:

C++

```
|  |  |
| --- | --- |
|  | UE::Online::FReadEntriesAroundRank::Params Params; |
|  | Params.LocalAccountId = "LLV54WB-3C678QQ"; |
|  | Params.Rank = 2; |
|  | Params.Limit = 2; |
|  | Params.BoardName = TEXT("Total Game Points"); |
```

UE::Online::FReadEntriesAroundRank::Params Params;
Params.LocalAccountId = "LLV54WB-3C678QQ";
Params.Rank = 2;
Params.Limit = 2;
Params.BoardName = TEXT("Total Game Points");

Copy full snippet(5 lines long)

If the call returns successfully, you can access the columns marked as retrieved in the returned `TOnlineResult`:

| Total Game Points |  |  |  |
| --- | --- | --- | --- |
| **Account ID** | **Rank** | **Score** | **Retrieved?** |
| 3CN9H8E-VNO3G3C | 1 | 1,901 |  |
| LLV54WB-3C678QQ | 2 | 151 |  |
| OHB8RA2-OHSEBSE | 3 | 17 | Y |
| 9P8H4GQ-HNO5GA4 | 4 | 3 | Y |
| 9HQGQER-ILASDFH | 5 | 1 |  |

From a programming perspective, the rank of the top of a leaderboard is 0, not 1. As a result of this, to retrieve the entry in third place, `ReadEntriesAroundRank` needs to be called with `Params.Rank = 2`.

### Around a Given User

Use the `ReadEntriesAroundUser` function to retrieve leaderboard entries around a particular user. This function takes in:

* the user around which you want to read entries,
* an offset to indicate where to start reading entries, and
* a limit for the total number of entries to read.

The offset can exceed the limit. In this case, the provided user will not be present in the returned array of leaderboard entries. This can be useful when organizing leaderboard entries into pages for viewing.

#### Example

Suppose that you have the leaderboard below titled Total Game Points and call `ReadEntriesAroundUser` with the following parameters:

C++

```
|  |  |
| --- | --- |
|  | UE::Online::FReadEntriesAroundUser::Params Params; |
|  | Params.LocalAccountId = "LLV54WB-3C678QQ"; |
|  | Params.Offset = -1; |
|  | Params.Limit = 3; |
|  | Params.BoardName = TEXT("Total Game Points"); |
```

UE::Online::FReadEntriesAroundUser::Params Params;
Params.LocalAccountId = "LLV54WB-3C678QQ";
Params.Offset = -1;
Params.Limit = 3;
Params.BoardName = TEXT("Total Game Points");

Copy full snippet(5 lines long)

If the call returns successfully, you can access the columns marked as retrieved in the returned `TOnlineResult`:

| Total Game Points |  |  |  |
| --- | --- | --- | --- |
| **Account ID** | **Rank** | **Score** | **Retrieved?** |
| 3CN9H8E-VNO3G3C | 1 | 1,901 | Y |
| LLV54WB-3C678QQ | 2 | 151 | Y |
| OHB8RA2-OHSEBSE | 3 | 17 | Y |
| 9P8H4GQ-HNO5GA4 | 4 | 3 |  |
| 9HQGQER-ILASDFH | 5 | 1 |  |

## More Information

### Header File

Consult the `Leaderboards.h` header file directly for more information as needed. The Leaderboards Interface header file `Leaderboards.h` is located in the directory:

C++

```
UNREAL_ENGINE_ROOT\Engine\Plugins\Online\OnlineServices\Source\OnlineServicesInterface\Public\Online
```

UNREAL\_ENGINE\_ROOT\Engine\Plugins\Online\OnlineServices\Source\OnlineServicesInterface\Public\Online

Copy full snippet(1 line long)

For instructions on how to obtain the UE source code, see our documentation on [Downloading Unreal Engine Source Code](https://dev.epicgames.com/documentation/en-us/unreal-engine/downloading-source-code-in-unreal-engine).

### Function Parameters and Return Types

See the [Functions](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-online-services-in-unreal-engine?application_version=5.5#functions) section of the Online Services Overview page for an explanation of function parameters and return types, including how to pass parameters and processing the results when functions return.

* [beta](https://dev.epicgames.com/community/search?query=beta)
* [programming](https://dev.epicgames.com/community/search?query=programming)
* [leaderboards](https://dev.epicgames.com/community/search?query=leaderboards)
* [online services](https://dev.epicgames.com/community/search?query=online%20services)
* [stats](https://dev.epicgames.com/community/search?query=stats)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [API Overview](/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine?application_version=5.7#api-overview)
* [Functions](/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine?application_version=5.7#functions)
* [Primary Struct](/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine?application_version=5.7#primary-struct)
* [Configuration](/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine?application_version=5.7#configuration)
* [General Syntax](/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine?application_version=5.7#general-syntax)
* [Leaderboard Definition](/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine?application_version=5.7#leaderboard-definition)
* [Configuration Example](/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine?application_version=5.7#configuration-example)
* [Read Leaderboard Entries](/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine?application_version=5.7#read-leaderboard-entries)
* [For Specific Users](/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine?application_version=5.7#for-specific-users)
* [Example](/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine?application_version=5.7#example)
* [Around a Particular Rank](/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine?application_version=5.7#around-a-particular-rank)
* [Example](/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine?application_version=5.7#example)
* [Around a Given User](/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine?application_version=5.7#around-a-given-user)
* [Example](/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine?application_version=5.7#example)
* [More Information](/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine?application_version=5.7#more-information)
* [Header File](/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine?application_version=5.7#header-file)
* [Function Parameters and Return Types](/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine?application_version=5.7#function-parameters-and-return-types)
