<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/iris-filtering-in-unreal-engine?application_version=5.7 -->

# Filtering

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
7. [Iris Replication System](/documentation/en-us/unreal-engine/iris-replication-system-in-unreal-engine "Iris Replication System")
8. [Components of Iris](/documentation/en-us/unreal-engine/components-of-iris-in-unreal-engine "Components of Iris")
9. Filtering

# Filtering

Filter object replication to certain network connections with Iris.

![Filtering](https://dev.epicgames.com/community/api/documentation/image/bbb03528-28f9-45b4-bdfb-bbacb9d4f75e?resizing_type=fill&width=1920&height=335)

Learn to use this **Experimental** feature, but use caution when shipping with it.

###### Prerequisite topics

In order to understand and use the content on this page, make sure you are familiar with the following topics:

* [Introduction to Iris](/documentation/en-us/unreal-engine/introduction-to-iris-in-unreal-engine)

 On this page

The **Iris Filtering System** determines what objects are replicated to which connections. There might be actors or objects in your game that you only want replicated to certain connections. To save time and bandwidth, the filtering system filters which connections an actor or object can replicate. The filtering system supports four different filtering types:

* [Owner](https://dev.epicgames.com/documentation/en-us/unreal-engine/iris-filtering-in-unreal-engine#owner): Object replicates to the same connections as its owner.
* [Connection](https://dev.epicgames.com/documentation/en-us/unreal-engine/iris-filtering-in-unreal-engine#connection): Object replicates to specified, allowed connections and does not replicate to specified, disallowed connections.
* [Group](https://dev.epicgames.com/documentation/en-us/unreal-engine/iris-filtering-in-unreal-engine#group): Object replicates to the same connections as all other objects in its group.
* [Dynamic](https://dev.epicgames.com/documentation/en-us/unreal-engine/iris-filtering-in-unreal-engine#dynamic): Object replicates based on custom, dynamic filtering.

## Owner

Actors with the `bOnlyRelevantToOwner` flag set to `true` automatically enable owner filtering. You can also enable owner filtering for standalone objects other than actors.

### Set Owner Filters For Objects

To enable owner filtering for objects other than actors, follow these steps:

1. Include the necessary Iris files in order to access required Iris functionality.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | #if UE_WITH_IRIS |
   |  | #include "Net/Iris/ReplicationSystem/ReplicationSystemUtil.h" |
   |  | #include "Iris/ReplicationSystem/ReplicationSystem.h" |
   |  | #include "Net/Iris/ReplicationSystem/ActorReplicationBridge.h" |
   |  | #include "Net/Iris/ReplicationSystem/Filtering/NetObjectFilter.h" |
   |  | #endif UE_WITH_IRIS |
   ```

   #if UE\_WITH\_IRIS
   #include &quot;Net/Iris/ReplicationSystem/ReplicationSystemUtil.h&quot;
   #include &quot;Iris/ReplicationSystem/ReplicationSystem.h&quot;
   #include &quot;Net/Iris/ReplicationSystem/ActorReplicationBridge.h&quot;
   #include &quot;Net/Iris/ReplicationSystem/Filtering/NetObjectFilter.h&quot;
   #endif UE\_WITH\_IRIS

   Copy full snippet(6 lines long)
2. In your gameplay code, retrieve the replication system and replication bridge for your replicated object.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // The actor for which you want to control filtering |
   |  | AActor* RepActorPtr; |
   |  |  |
   |  | UReplicationSystem* ReplicationSystem = UE::Net::FReplicationSystemUtil::GetReplicationSystem(RepActorPtr); |
   |  | UActorReplicationBridge* ReplicationBridge = UE::Net::FReplicationSystemUtil::GetActorReplicationBridge(RepActorPtr); |
   ```

   // The actor for which you want to control filtering
   AActor\* RepActorPtr;
   UReplicationSystem\* ReplicationSystem = UE::Net::FReplicationSystemUtil::GetReplicationSystem(RepActorPtr);
   UActorReplicationBridge\* ReplicationBridge = UE::Net::FReplicationSystemUtil::GetActorReplicationBridge(RepActorPtr);

   Copy full snippet(5 lines long)
3. Retrieve the `FNetRefHandle` for your replicated object. Iris uses this identifier to locate your object within the replication system.

   C++

   ```
   UE::Net::FNetRefHandle RepActorNetRefHandle = ReplicationBridge->GetReplicatedRefHandle(RepActorPtr);
   ```

   UE::Net::FNetRefHandle RepActorNetRefHandle = ReplicationBridge-&gt;GetReplicatedRefHandle(RepActorPtr);

   Copy full snippet(1 line long)
4. Set the owner filter handle for your replicated object.

   C++

   ```
   ReplicationSystem->SetFilter(RepActorNetHandle, UE::Net::ToOwnerFilterHandle);
   ```

   ReplicationSystem-&gt;SetFilter(RepActorNetHandle, UE::Net::ToOwnerFilterHandle);

   Copy full snippet(1 line long)

You should assign the owner filter just after an object's owner is assigned.

### Clear All Filters

To clear all filters on a replicated object, first follow Step 1 and 2 from [Set Owner Filters for Objects](https://dev.epicgames.com/documentation/en-us/unreal-engine/iris-filtering-in-unreal-engine), then set the filter to use the following special filter handle:

C++

```
#if UE_WITH_IRIS
	#include "Net/Iris/ReplicationSystem/ReplicationSystemUtil.h"
	#include "Iris/ReplicationSystem/ReplicationSystem.h"
	#include "Net/Iris/ReplicationSystem/ActorReplicationBridge.h"
	#include "Net/Iris/ReplicationSystem/Filtering/NetObjectFilter.h"
	#endif UE_WITH_IRIS

	UReplicationSystem* ReplicationSystem = UE::Net::FReplicationSystemUtil::GetReplicationSystem(RepActorPtr);
	UActorReplicationBridge* ReplicationBridge = UE::Net::FReplicationSystemUtil::GetActorReplicationBridge(RepActorPtr);
```

Expand code  Copy full snippet(14 lines long)

## Connection

You can set the connections an object replicates to by specifying connection IDs. We advise using this option when:

* The allowed connections for the object in question are static, and…
* Only a few objects are affected if the connection IDs change for some reason.

If a large number of objects might be affected, consider using group filtering instead. Connection filtering enables you to add either allowed or disallowed connections to an object.

### Set Connection Filters

To add allowed connections:

1. Set the bits for all connections for which the object is allowed to be replicated
2. Initialize the connection with a maximum number of allowed connections before setting the connection filter.

   C++

   ```
   #if UE_WITH_IRIS
            #include "Net/Iris/ReplicationSystem/ReplicationSystemUtil.h"
            #include "Iris/ReplicationSystem/ReplicationSystem.h"
            #include "Net/Iris/ReplicationSystem/ActorReplicationBridge.h"
            #include "Net/Iris/ReplicationSystem/Filtering/NetObjectFilter.h"
            #endif UE_WITH_IRIS
   		
            UReplicationSystem* ReplicationSystem = UE::Net::FReplicationSystemUtil::GetReplicationSystem(RepActorPtr);
            UActorReplicationBridge* ReplicationBridge = UE::Net::FReplicationSystemUtil::GetActorReplicationBridge(RepActorPtr);
   		
   ```

   Expand code  Copy full snippet(22 lines long)

Similar logic applies to add disallowed connections. Instead of using the `ENetFilterStatus::Allow`, use the `ENetFilterStatus::Disallow` value. In this case, the provided connections are disallowed connections for the object to replicate to.

### Clear Connection Filters

Connection filtering for an object is cleared differently than owner filters. To clear connection filters for an object, set a disallowed connection filter, but specify no provided connections to disallow:

C++

```
#if UE_WITH_IRIS
	#include "Net/Iris/ReplicationSystem/ReplicationSystemUtil.h"
	#include "Iris/ReplicationSystem/ReplicationSystem.h"
	#include "Net/Iris/ReplicationSystem/ActorReplicationBridge.h"
	#include "Net/Iris/ReplicationSystem/Filtering/NetObjectFilter.h"
	#endif UE_WITH_IRIS

	UReplicationSystem* ReplicationSystem = UE::Net::FReplicationSystemUtil::GetReplicationSystem(RepActorPtr);
	UActorReplicationBridge* ReplicationBridge = UE::Net::FReplicationSystemUtil::GetActorReplicationBridge(RepActorPtr);
```

Expand code  Copy full snippet(15 lines long)

## Group

Iris includes an API for creating groups and managing the objects those groups contain. You can also use groups as a filtering mechanism. This is a flexible way of changing which connections a set of objects can replicate to without requiring you to manually keep track of which objects belong to which groups. Example use cases include filtering based on:

* Team
* Squad
* Streaming Level

An object can belong to more than one group. You must add groups to the filtering system for it to consider them for replication. Once you add them, you can modify which connections members of the group are allowed to replicate. You can set groups as allowed or disallowed for replication to:

* A single connection
* A set of connections
* All connections

### Create a Group

To create a filter group, call the `CreateGroup` function, which returns a unique group handle:

C++

```
|  |  |
| --- | --- |
|  | #if UE_WITH_IRIS |
|  | #include "Net/Iris/ReplicationSystem/ReplicationSystemUtil.h" |
|  | #include "Iris/ReplicationSystem/ReplicationSystem.h" |
|  | #endif UE_WITH_IRIS |
|  |  |
|  | UReplicationSystem* ReplicationSystem = UE::Net::FReplicationSystemUtil::GetReplicationSystem(RepActorPtr); |
|  | UE::Net::FNetObjectGroupHandle GroupHandle = ReplicationSystem->CreateGroup(); |
```

#if UE\_WITH\_IRIS
#include "Net/Iris/ReplicationSystem/ReplicationSystemUtil.h"
#include "Iris/ReplicationSystem/ReplicationSystem.h"
#endif UE\_WITH\_IRIS
UReplicationSystem\* ReplicationSystem = UE::Net::FReplicationSystemUtil::GetReplicationSystem(RepActorPtr);
UE::Net::FNetObjectGroupHandle GroupHandle = ReplicationSystem->CreateGroup();

Copy full snippet(7 lines long)

### Add Group Filter

You must add the group filter to the filtering system before setting the filter status and adding objects:

C++

```
|  |  |
| --- | --- |
|  | #if UE_WITH_IRIS |
|  | #include "Iris/ReplicationSystem/ReplicationSystem.h" |
|  | #endif UE_WITH_IRIS |
|  |  |
|  | // Add a valid FNetObjectGroupHandle |
|  | ReplicationSystem->AddGroupFilter(GroupHandle); |
```

#if UE\_WITH\_IRIS
#include "Iris/ReplicationSystem/ReplicationSystem.h"
#endif UE\_WITH\_IRIS
// Add a valid FNetObjectGroupHandle
ReplicationSystem->AddGroupFilter(GroupHandle);

Copy full snippet(6 lines long)

### Set Group Filtering

Once you create a group and add the group filter to the replication system, you can set the group filtering. In this example, any object belonging to the group with handle `GroupHandle` is allowed to replicate only to the connection with ID `SpecialConnectionId`:

C++

```
|  |  |
| --- | --- |
|  | #if UE_WITH_IRIS |
|  | #include "Iris/ReplicationSystem/ReplicationSystem.h" |
|  | #include "Net/Iris/ReplicationSystem/Filtering/NetObjectFilter.h" |
|  | #endif UE_WITH_IRIS |
|  |  |
|  | // With a valid FNetObjectGroupHandle and uint32 connection id |
|  | ReplicationSystem->SetGroupFilterStatus(GroupHandle, SpecialConnectionId, UE::Net::ENetFilterStatus::Allow); |
```

#if UE\_WITH\_IRIS
#include "Iris/ReplicationSystem/ReplicationSystem.h"
#include "Net/Iris/ReplicationSystem/Filtering/NetObjectFilter.h"
#endif UE\_WITH\_IRIS
// With a valid FNetObjectGroupHandle and uint32 connection id
ReplicationSystem->SetGroupFilterStatus(GroupHandle, SpecialConnectionId, UE::Net::ENetFilterStatus::Allow);

Copy full snippet(7 lines long)

### Add Object to Group

You can now add your desired object to the group:

C++

```
|  |  |
| --- | --- |
|  | #if UE_WITH_IRIS |
|  | #include "Net/Iris/ReplicationSystem/ActorReplicationBridge.h" |
|  | #include "Iris/ReplicationSystem/ReplicationSystem.h" |
|  | #endif UE_WITH_IRIS |
|  |  |
|  | UE::Net::FNetRefHandle RepActorNetRefHandle = ReplicationBridge->GetReplicatedRefHandle(RepActorPtr); |
|  |  |
|  | // With a valid FNetObjectGroupHandle and FNetHandle |
|  | ReplicationSystem->AddToGroup(GroupHandle, RepActorNetRefHandle); |
```

#if UE\_WITH\_IRIS
#include "Net/Iris/ReplicationSystem/ActorReplicationBridge.h"
#include "Iris/ReplicationSystem/ReplicationSystem.h"
#endif UE\_WITH\_IRIS
UE::Net::FNetRefHandle RepActorNetRefHandle = ReplicationBridge->GetReplicatedRefHandle(RepActorPtr);
// With a valid FNetObjectGroupHandle and FNetHandle
ReplicationSystem->AddToGroup(GroupHandle, RepActorNetRefHandle);

Copy full snippet(9 lines long)

## Dynamic

Iris’s filtering system can also implement custom, dynamic filtering with a `UNetObjectFilter`-derived class. Dynamic filters can restrict objects from replicating based on custom logic. Dynamic filters are applied after connection and group filters. This means that a dynamic filter cannot enable replication for an object that has already been filtered out by connection or group filters. An object can only have one dynamic filter set at a time.

Dynamic filters always run on an object, whereas connection and group filtering only run when the system is informed of changes. This is due to the fact that a dynamic filter can be implemented in any way, so there is no way for the system to know whether the dynamic filter needs to run or not. There are situations where a dynamic filter provides the best solution. If you modify groups often, such as moving actors between groups or changing which connections the group may be replicated to, a dynamic filter may provide the best solution.

You should only set a dynamic filter for an object as a last resort. This adds significant CPU overhead versus connection and group filters.

UE provides a few dynamic filters in the directory `..\Engine\Source\Runtime\Experimental\Iris\Core\Public\Iris\ReplicationSystem\Filtering\`:

* `UFilterOutNetObjectFilter`: Disallow replication of any objects added to it.
* `UNetObjectConnectionFilter`: Pre-poll filter that supports per-connection filtering for dependent objects.
* `UNetObjectGridFilter`: Divide the game world into cells and only replicate objects in cells near the player’s view.

To use a custom dynamic filter, you must implement the `UNetObjectFilter` interface and it must be configured with filter definitions in order to be used at runtime.

### Create a Dynamic Filter

To use a custom, dynamic filter, implement the `UNetObjectFilter` interface and configure its filter definitions to use the filter at runtime. The base class your custom filter must inherit from is located at the following file path:

* `..\Engine\Source\Runtime\Experimental\Iris\Core\Public\Iris\ReplicationSystem\Filtering\NetObjectFilter.h`

A minimal, working example of a custom, dynamic filter is provided in:

* `..\Engine\Source\Runtime\Experimental\Iris\Core\Public\Iris\ReplicationSystem\Filtering\NopNetObjectFilter.h`

### Dynamic Filter Configuration

Below is the syntax for engine configuration to use a custom dynamic filter:

C++

```
|  |  |
| --- | --- |
|  | [/Script/IrisCore.NetObjectFilterDefinitions] |
|  | +NetObjectFilterDefinitions=(FilterName=<FILTER_NAME>, ClassName=/Script/<PROJECT_NAME>.<FILTER_NAME>, ConfigClassName=/Script/<PROJECT_NAME>.<FILTER_NAME>Config) |
```

[/Script/IrisCore.NetObjectFilterDefinitions]
+NetObjectFilterDefinitions=(FilterName=<FILTER\_NAME>, ClassName=/Script/<PROJECT\_NAME>.<FILTER\_NAME>, ConfigClassName=/Script/<PROJECT\_NAME>.<FILTER\_NAME>Config)

Copy full snippet(2 lines long)

For example, a custom, dynamic filter named `MyCustomFilter` in a project named `MyProject` is configured as follows in the engine configuration hierarchy, such as your project’s `DefaultEngine.ini` file:

C++

```
|  |  |
| --- | --- |
|  | [/Script/IrisCore.NetObjectFilterDefinitions] |
|  | +NetObjectFilterDefinitions=(FilterName=MyCustomFilter, ClassName=/Script/MyProject.MyCustomFilter, ConfigClassName=/Script/MyProject.MyCustomFilterConfig) |
```

[/Script/IrisCore.NetObjectFilterDefinitions]
+NetObjectFilterDefinitions=(FilterName=MyCustomFilter, ClassName=/Script/MyProject.MyCustomFilter, ConfigClassName=/Script/MyProject.MyCustomFilterConfig)

Copy full snippet(2 lines long)

Once your filter is registered with Iris, you can configure your filter as follows in an engine configuration file such as your project’s `DefaultEngine.ini` file:

C++

```
|  |  |
| --- | --- |
|  | [/Script/MyProject.MyCustomFilterConfig] |
|  | MyCustomFilterVar=100 |
```

[/Script/MyProject.MyCustomFilterConfig]
MyCustomFilterVar=100

Copy full snippet(2 lines long)

### Assign Object to Dynamic Filter

To assign a dynamic filter to a replicated object, use the following:

C++

```
|  |  |
| --- | --- |
|  | const UE::Net::FNetObjectFilterHandle FilterHandle = ReplicationSystem->GetFilterHandle(FName("<FILTER_NAME>")); |
|  | if (FilterHandle != UE::Net::InvalidNetObjectFilterHandle) |
|  | { |
|  | const bool bSuccess = ReplicationSystem->SetFilter(ObjectNetHandle, FilterHandle); |
|  | } |
```

const UE::Net::FNetObjectFilterHandle FilterHandle = ReplicationSystem->GetFilterHandle(FName("<FILTER\_NAME>"));
if (FilterHandle != UE::Net::InvalidNetObjectFilterHandle)
{
const bool bSuccess = ReplicationSystem->SetFilter(ObjectNetHandle, FilterHandle);
}

Copy full snippet(5 lines long)

### Remove Dynamic Filter

Dynamic filters are removed in the same way as owner filters. To remove any filter, see the [Clear All Filters](https://dev.epicgames.com/documentation/en-us/unreal-engine/iris-filtering-in-unreal-engine) section of this page.

* [experimental](https://dev.epicgames.com/community/search?query=experimental)
* [multiplayer](https://dev.epicgames.com/community/search?query=multiplayer)
* [networking](https://dev.epicgames.com/community/search?query=networking)
* [iris](https://dev.epicgames.com/community/search?query=iris)
* [filtering](https://dev.epicgames.com/community/search?query=filtering)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Owner](/documentation/en-us/unreal-engine/iris-filtering-in-unreal-engine?application_version=5.7#owner)
* [Set Owner Filters For Objects](/documentation/en-us/unreal-engine/iris-filtering-in-unreal-engine?application_version=5.7#set-owner-filters-for-objects)
* [Clear All Filters](/documentation/en-us/unreal-engine/iris-filtering-in-unreal-engine?application_version=5.7#clear-all-filters)
* [Connection](/documentation/en-us/unreal-engine/iris-filtering-in-unreal-engine?application_version=5.7#connection)
* [Set Connection Filters](/documentation/en-us/unreal-engine/iris-filtering-in-unreal-engine?application_version=5.7#set-connection-filters)
* [Clear Connection Filters](/documentation/en-us/unreal-engine/iris-filtering-in-unreal-engine?application_version=5.7#clear-connection-filters)
* [Group](/documentation/en-us/unreal-engine/iris-filtering-in-unreal-engine?application_version=5.7#group)
* [Create a Group](/documentation/en-us/unreal-engine/iris-filtering-in-unreal-engine?application_version=5.7#create-a-group)
* [Add Group Filter](/documentation/en-us/unreal-engine/iris-filtering-in-unreal-engine?application_version=5.7#add-group-filter)
* [Set Group Filtering](/documentation/en-us/unreal-engine/iris-filtering-in-unreal-engine?application_version=5.7#set-group-filtering)
* [Add Object to Group](/documentation/en-us/unreal-engine/iris-filtering-in-unreal-engine?application_version=5.7#add-object-to-group)
* [Dynamic](/documentation/en-us/unreal-engine/iris-filtering-in-unreal-engine?application_version=5.7#dynamic)
* [Create a Dynamic Filter](/documentation/en-us/unreal-engine/iris-filtering-in-unreal-engine?application_version=5.7#create-a-dynamic-filter)
* [Dynamic Filter Configuration](/documentation/en-us/unreal-engine/iris-filtering-in-unreal-engine?application_version=5.7#dynamic-filter-configuration)
* [Assign Object to Dynamic Filter](/documentation/en-us/unreal-engine/iris-filtering-in-unreal-engine?application_version=5.7#assign-object-to-dynamic-filter)
* [Remove Dynamic Filter](/documentation/en-us/unreal-engine/iris-filtering-in-unreal-engine?application_version=5.7#remove-dynamic-filter)
