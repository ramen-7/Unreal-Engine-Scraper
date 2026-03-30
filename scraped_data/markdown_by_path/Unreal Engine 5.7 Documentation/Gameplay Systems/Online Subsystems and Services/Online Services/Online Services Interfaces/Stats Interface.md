<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/stats-interface-in-unreal-engine?application_version=5.7 -->

# Stats Interface

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
9. Stats Interface

# Stats Interface

Upload stats and data to online services and complete stats queries.

![Stats Interface](https://dev.epicgames.com/community/api/documentation/image/5cc4a0ec-192f-4c16-8806-423bf2a1dd73?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

The **Online Services Stats Interface** is used to upload stats and data to online services and complete stats queries. Stats Interface functionality is also used by other interfaces that rely on user gameplay statistics such as the Online Services' Achievements and Leaderboards Interfaces.

## API Overview

The following table provides a high-level description of the functions included in the Stats Interface.

| Function | Description |
| --- | --- |
| **Update** |  |
| [UpdateStats](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IStats/UpdateStats?application_version=5.5) | Upload stats to the platform |
| **Query** |  |
| [QueryStats](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IStats/QueryStats?application_version=5.5) | Query the stats of a user and cache the result in the interface. |
| [BatchQueryStats](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IStats/BatchQueryStats?application_version=5.5) | Query the stats of a group of users and cache the results in the interface. |
| **Get** |  |
| [GetCachedStats](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IStats/GetCachedStats?application_version=5.5) | Retrieve the cached user stats stored after a call to QueryStats or BatchQueryStats. |
| **Event Listening** |  |
| [OnStatsUpdated](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IStats/OnStatsUpdated?application_version=5.5) | An event will fire as a result of changes to user stats. |

## Configuration

You can use the Stats Interface with either a corresponding platform backend or a `StatsNull` implementation. To use the Stats Interface, you must first configure the Stats Interface in your `DefaultEngine.ini` file:

C++

DefaultEngine.ini

```
|  |  |
| --- | --- |
|  | [OnlineServices.Stats] |
|  | +StatDefinitions=(Name=<STAT_NAME>, Id=<ID_NUMBER>, ModifyMethod=<METHOD>, DefaultValue="<TYPE>:<DEFAULT_VALUE>") |
```

[OnlineServices.Stats]
+StatDefinitions=(Name=<STAT\_NAME>, Id=<ID\_NUMBER>, ModifyMethod=<METHOD>, DefaultValue="<TYPE>:<DEFAULT\_VALUE>")

Copy full snippet(2 lines long)

**Stat Definitions** consist of the following fields:

* `Name`: The name of the stat.

  + This is the name that will be used to update and query stats with `UpdateStats` and `QueryStats` respectively.
* `Id`: The ID of the stat.

  + This is the corresponding configured stat ID in the platform portal.
* `ModifyMethod`: Method prescribing how the stat will be updated.

  + For non-`StatsNull` implementations, the Modify Method is configured in the platform portal.
  + The Modify Method is used by the Achievements Interface on all implementations when using Title Managed achievements to determine whether an achievement meets the prescribed unlock rules.
* `DefaultValue`: The type and default value of the stat.

  + This prescribes the initial value of the stat.

To unlock achievements and update leaderboards with stats, you must specify corresponding stats in the Achievements and Leaderboards config sections of `DefaultEngine.ini`.

### Configuration Example

Here is a configuration example for the Online Services Stats interface:

C++

DefaultEngine.ini

```
|  |  |
| --- | --- |
|  | [OnlineServices.Stats] |
|  | +StatDefinitions=(Name=Stat_Use_Largest, Id=0, ModifyMethod=Largest, DefaultValue="Int64:0") |
|  | +StatDefinitions=(Name=Stat_Use_Smallest, Id=1, ModifyMethod=Smallest, DefaultValue="Int64:999") |
|  | +StatDefinitions=(Name=Stat_Use_Set, Id=2, ModifyMethod=Set, DefaultValue="Int64:0") |
|  | +StatDefinitions=(Name=Stat_Use_Sum, Id=3, ModifyMethod=Sum, DefaultValue="Int64:0") |
|  | +StatDefinitions=(Name=Stat_Type_Bool, Id=4, ModifyMethod=Set, DefaultValue="Bool:True") |
|  | +StatDefinitions=(Name=Stat_Type_Double, Id=5, ModifyMethod=Smallest, DefaultValue="Double:9999.999") |
```

[OnlineServices.Stats]
+StatDefinitions=(Name=Stat\_Use\_Largest, Id=0, ModifyMethod=Largest, DefaultValue="Int64:0")
+StatDefinitions=(Name=Stat\_Use\_Smallest, Id=1, ModifyMethod=Smallest, DefaultValue="Int64:999")
+StatDefinitions=(Name=Stat\_Use\_Set, Id=2, ModifyMethod=Set, DefaultValue="Int64:0")
+StatDefinitions=(Name=Stat\_Use\_Sum, Id=3, ModifyMethod=Sum, DefaultValue="Int64:0")
+StatDefinitions=(Name=Stat\_Type\_Bool, Id=4, ModifyMethod=Set, DefaultValue="Bool:True")
+StatDefinitions=(Name=Stat\_Type\_Double, Id=5, ModifyMethod=Smallest, DefaultValue="Double:9999.999")

Copy full snippet(7 lines long)

## Examples

This section contains a variety of code examples that guide you on how to:

* [Query Stats](https://dev.epicgames.com/documentation/en-us/unreal-engine/stats-interface-in-unreal-engine?application_version=5.5)
* [Get Cached Stats](https://dev.epicgames.com/documentation/en-us/unreal-engine/stats-interface-in-unreal-engine?application_version=5.5)
* [Listen for an event](https://dev.epicgames.com/documentation/en-us/unreal-engine/stats-interface-in-unreal-engine?application_version=5.5)
* [Execute a Console Command](https://dev.epicgames.com/documentation/en-us/unreal-engine/stats-interface-in-unreal-engine?application_version=5.5)

### Query Stats

C++

```
UE::Online::IOnlineServicesPtr OnlineServices = UE::Online::GetServices();
UE::Online::IStatsPtr Stats = OnlineServices->GetStatsInterface();

UE::Online::FQueryStats::Params Params;
Params.LocalAccountId = LocalAccountId;
Params.TargetAccountId = TargetAccountId;
Params.StatNames = {"StatA", "StatB"};

// See Note below Walkthrough for more information about this OnComplete call
Stats->QueryStats(MoveTemp(Params)).OnComplete([](const UE::Online::TOnlineResult<FQueryStats>& Result)
```

Expand code  Copy full snippet(20 lines long)

#### Walkthrough

1. Use the default online services by calling `GetServices` with no parameters specified:

   C++

   ```
   UE::Online::IOnlineServicesPtr OnlineServices = UE::Online::GetServices();
   ```

   UE::Online::IOnlineServicesPtr OnlineServices = UE::Online::GetServices();

   Copy full snippet(1 line long)
2. Access the Stats Interface for the default online services:

   C++

   ```
   UE::Online::IStatsPtr Stats = OnlineServices->GetStatsInterface();
   ```

   UE::Online::IStatsPtr Stats = OnlineServices-&gt;GetStatsInterface();

   Copy full snippet(1 line long)
3. Instantiate the parameters necessary to query the `StatNames` of the `TargetAccountId`:

   C++

   ```
   |  |  |
   | --- | --- |
   |  | UE::Online::FQueryStats::Params Params; |
   |  | Params.LocalAccountId = LocalAccountId; |
   |  | Params.TargetAccountId = TargetAccountId; |
   |  | Params.StatNames = {"StatA", "StatB"}; |
   ```

   UE::Online::FQueryStats::Params Params;
   Params.LocalAccountId = LocalAccountId;
   Params.TargetAccountId = TargetAccountId;
   Params.StatNames = {&quot;StatA&quot;, &quot;StatB&quot;};

   Copy full snippet(4 lines long)
4. Handle the `QueryStats.OnComplete` callback by processing the error or the queried stats:

   C++

   ```
   Stats->QueryStats(MoveTemp(Params)).OnComplete([](const UE::Online::TOnlineResult<FQueryStats>& Result)
        {
            if (Result.IsError())
            {
                const UE::Online::FOnlineError OnlineError = Result.GetErrorValue();
                // Process OnlineError
                return;
            }
            const UE::Online::FQueryStats::Result QueriedStats = Result.GetOkValue();
            // Process QueriedStats
   ```

   Expand code  Copy full snippet(11 lines long)

To bind to a member function, always prefer to use a UObject-derived class or a class that inherits from `TSharedFromThis` and use

C++

```
.OnComplete(this, &MyClass::OnQueryStatsComplete)
```

.OnComplete(this, &MyClass::OnQueryStatsComplete)

Copy full snippet(1 line long)

This automatically selects `CreateUObject`, `CreateThreadSafeSP`, or `CreateSP`. The safest delegate creation call will be used. For more information, refer to the [Callback Format](programming-and-scripting/online/online-services/overview#CallbackFormat) section of the Online Services Overview page.

### Get Cached Stats

C++

```
UE::Online::IOnlineServicesPtr OnlineServices = UE::Online::GetServices();
UE::Online::IStatsPtr Stats = OnlineServices->GetStatsInterface();

UE::Online::TOnlineResult<FGetCachedStats> CachedStats = Stats->GetCachedStats({});
if (CachedStats.IsError())
{
	UE::Online::FOnlineError OnlineError = CachedStats.GetErrorValue();
	// Process OnlineError
	return;
}
```

Expand code  Copy full snippet(13 lines long)

#### Walkthrough

1. Use the default online services by calling `GetServices` with no parameters specified and access the Stats Interface:

   C++

   ```
   |  |  |
   | --- | --- |
   |  | UE::Online::IOnlineServicesPtr OnlineServices = UE::Online::GetServices(); |
   |  | UE::Online::IStatsPtr Stats = OnlineServices->GetStatsInterface(); |
   ```

   UE::Online::IOnlineServicesPtr OnlineServices = UE::Online::GetServices();
   UE::Online::IStatsPtr Stats = OnlineServices-&gt;GetStatsInterface();

   Copy full snippet(2 lines long)
2. Retrieve the cached stats through the Stats Interface with `Stats->GetCachedStats`:

   C++

   ```
   UE::Online::TOnlineResult<UE::Online::FGetCachedStats> CachedStats = Stats->GetCachedStats({});
   ```

   UE::Online::TOnlineResult&lt;UE::Online::FGetCachedStats&gt; CachedStats = Stats-&gt;GetCachedStats({});

   Copy full snippet(1 line long)
3. Handle the `CachedStats` by processing the error or the cached stats data:

   C++

   ```
   |  |  |
   | --- | --- |
   |  | if (CachedStats.IsError()) |
   |  | { |
   |  | UE::Online::FOnlineError OnlineError = CachedStats.GetErrorValue(); |
   |  | // Process OnlineError |
   |  | return; |
   |  |  |
   |  | } |
   |  | UE::Online::FGetCachedStats::Result& CachedStatsData = CachedStats.GetOkValue(); |
   |  | // Process CachedStatsData |
   ```

   if (CachedStats.IsError())
   {
   UE::Online::FOnlineError OnlineError = CachedStats.GetErrorValue();
   // Process OnlineError
   return;
   }
   UE::Online::FGetCachedStats::Result&amp; CachedStatsData = CachedStats.GetOkValue();
   // Process CachedStatsData

   Copy full snippet(9 lines long)

### Listen for an Event

Event listening is handled differently than synchronous and asynchronous functions. An `FOnlineEventDelegateHandle` is created to handle the result of the `OnStatsUpdated` event, then `Unbind` must be called in your shutdown code to ensure proper destruction.

#### Walkthrough

1. Declare an event handle in your class for the Stat interface.

   C++

   ```
   UE::Online::FOnlineEventDelegateHandle StatEventHandle;
   ```

   UE::Online::FOnlineEventDelegateHandle StatEventHandle;

   Copy full snippet(1 line long)
2. In your init code, initialize the default online services, access the Stats interface, and process the stats when an event happens.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | UE::Online::IOnlineServicesPtr OnlineServices = UE::Online::GetServices(); |
   |  | UE::Online::IStatsPtr Stats = OnlineServices->GetStatsInterface(); |
   |  | StatEventHandle = Stats->OnStatsUpdated().Add([](const UE::Online::FStatsUpdated& StatsUpdated) |
   |  | { |
   |  | // custom logic inside this lambda |
   |  | }); |
   ```

   UE::Online::IOnlineServicesPtr OnlineServices = UE::Online::GetServices();
   UE::Online::IStatsPtr Stats = OnlineServices-&gt;GetStatsInterface();
   StatEventHandle = Stats-&gt;OnStatsUpdated().Add([](const UE::Online::FStatsUpdated&amp; StatsUpdated)
   {
   // custom logic inside this lambda
   });

   Copy full snippet(6 lines long)
3. Ensure that you unbind the event handler in your shutdown code.

   C++

   ```
   StatEventHandle.Unbind();
   ```

   StatEventHandle.Unbind();

   Copy full snippet(1 line long)

### Execute a Console Command

For the general command-line syntax to run an async interface with a console command, refer to the [Online Services Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-online-services-in-unreal-engine?application_version=5.5) documentation.

#### Example

To run the `QueryStats` function, execute the following console command:

C++

```
OnlineServices Index=0 Stats QueryStats 0 0 ["StatA", "StatB"]
```

OnlineServices Index=0 Stats QueryStats 0 0 ["StatA", "StatB"]

Copy full snippet(1 line long)

This command calls `QueryStats` from the Stats Interface with the default online services for the zeroth local user. In particular, the above command queries the default online services for `StatA` and `StatB` of this user.

## Reset Stats Data

During development and testing, the `ResetStats` function resets all provided player stats for the current title. Although policies vary across online services, you should not expect this function to work outside a testing environment. Be sure to remove any code that uses `ResetStats` from shipping builds, or use compile-time logic to mask the code like this:

C++

```
|  |  |
| --- | --- |
|  | #if !UE_BUILD_SHIPPING |
|  | // Code block with call to ResetStats |
|  | #endif |
```

#if !UE\_BUILD\_SHIPPING
// Code block with call to ResetStats
#endif

Copy full snippet(3 lines long)

## More Information

### Header File

Consult the `Stats.h` header file directly for more information as needed. The Stats Interface header file `Stats.h` is located in the directory:

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
* [achievements](https://dev.epicgames.com/community/search?query=achievements)
* [leaderboards](https://dev.epicgames.com/community/search?query=leaderboards)
* [multiplayer](https://dev.epicgames.com/community/search?query=multiplayer)
* [online services](https://dev.epicgames.com/community/search?query=online%20services)
* [stats](https://dev.epicgames.com/community/search?query=stats)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [API Overview](/documentation/en-us/unreal-engine/stats-interface-in-unreal-engine?application_version=5.7#api-overview)
* [Configuration](/documentation/en-us/unreal-engine/stats-interface-in-unreal-engine?application_version=5.7#configuration)
* [Configuration Example](/documentation/en-us/unreal-engine/stats-interface-in-unreal-engine?application_version=5.7#configuration-example)
* [Examples](/documentation/en-us/unreal-engine/stats-interface-in-unreal-engine?application_version=5.7#examples)
* [Query Stats](/documentation/en-us/unreal-engine/stats-interface-in-unreal-engine?application_version=5.7#query-stats)
* [Walkthrough](/documentation/en-us/unreal-engine/stats-interface-in-unreal-engine?application_version=5.7#walkthrough)
* [Get Cached Stats](/documentation/en-us/unreal-engine/stats-interface-in-unreal-engine?application_version=5.7#get-cached-stats)
* [Walkthrough](/documentation/en-us/unreal-engine/stats-interface-in-unreal-engine?application_version=5.7#walkthrough)
* [Listen for an Event](/documentation/en-us/unreal-engine/stats-interface-in-unreal-engine?application_version=5.7#listen-for-an-event)
* [Walkthrough](/documentation/en-us/unreal-engine/stats-interface-in-unreal-engine?application_version=5.7#walkthrough)
* [Execute a Console Command](/documentation/en-us/unreal-engine/stats-interface-in-unreal-engine?application_version=5.7#execute-a-console-command)
* [Example](/documentation/en-us/unreal-engine/stats-interface-in-unreal-engine?application_version=5.7#example)
* [Reset Stats Data](/documentation/en-us/unreal-engine/stats-interface-in-unreal-engine?application_version=5.7#reset-stats-data)
* [More Information](/documentation/en-us/unreal-engine/stats-interface-in-unreal-engine?application_version=5.7#more-information)
* [Header File](/documentation/en-us/unreal-engine/stats-interface-in-unreal-engine?application_version=5.7#header-file)
* [Function Parameters and Return Types](/documentation/en-us/unreal-engine/stats-interface-in-unreal-engine?application_version=5.7#function-parameters-and-return-types)
