<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/networking-insights-in-unreal-engine?application_version=5.7 -->

# Networking Insights

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
5. [Testing and Optimizing Your Content](/documentation/en-us/unreal-engine/testing-and-optimizing-your-content "Testing and Optimizing Your Content")
6. [Unreal Insights](/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine "Unreal Insights")
7. Networking Insights

# Networking Insights

Overview of Networking Insights, the network performance profiling tool

![Networking Insights](https://dev.epicgames.com/community/api/documentation/image/405d28c6-d59e-46b3-b9cf-50d44be7fd96?resizing_type=fill&width=1920&height=335)

 On this page

**Networking Insights** is a telemetry capture and analysis tool you can use to analyze, optimize, and debug network traffic. Networking Insights is part of the **Unreal Insights** suite of tools.

Users can record trace information to visualize network behavior with the following features:

* **Packet Overview** panel visualizes packet timelines (and sizes) being transmitted or received during a game.
* **Packet Content** panel reveals packet's content, such as replicated objects, properties, and remote function calls.
* **Connection Selections** panel controls information display based on game instance, connection, and connection mode.
* **Net Stats** panel shows trace events for selected packets, including statistics about the total, maximum, and average exclusive (or inclusive) packet sizes.
* **Net Stats Counters** panel displays the stats counters recorded for the replication system.

## Setup

In order to use Networking Insights, you must first ensure that [Unreal Insights](/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine) is running.

## Using Networking Insights

To analyze data start your client game instances with the following command-line option:

```
	-trace=net -NetTrace=<VERBOSITY> [-tracehost=localhost]
Copy full snippet
```

These command-line options specify different settings for Networking Insights. The `-trace` command-line option specifies which categories Unreal Insights should trace. Specifying `-trace=net` tells Unreal Insights to start Networking Insights and trace the networking category. The `-NetTrace` command-line option specifies the verbosity of Networking Insights recordings. Set verbosity to a value of greater than zero. For example, if a game instance starts with `-NetTrace=1`, Unreal Insights collects and reports network trace data for analysis by opening the session in Unreal Insights. The editor runs its own data store for trace data, which means that you need to specify the tracehost in order to collect network trace data while running in the editor. To specify the tracehost, use: `-NetTrace=1 -trace=net -tracehost=localhost`

## Networking Insights Window

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/63e8672a-c007-4b02-9157-1199d69dcfba/insights-panels.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/63e8672a-c007-4b02-9157-1199d69dcfba/insights-panels.png)

The Networking Insights window features multiple panels providing various functionality.

The Networking Insights window is where you'll find networking session data, including:

1. **Packet Overview** panel visualizes packet timelines (and sizes) being transmitted or received during a game.
2. **Packet Content** panel reveals packet's content, such as replicated objects, properties, and remote function calls.
3. **Connection Selections** panel controls information display based on game instance, connection, and connection mode.
4. **Net Stats** panel shows trace events for selected packets, including statistics about the total, maximum, and average exclusive (or inclusive) packet sizes.
5. **Net Stats Counters** panel tracks stats associated to a particular frame or packet.

For additional commands, tips, and information on other Unreal Insights windows , refer to the [Reference](/documentation/en-us/unreal-engine/unreal-insights-reference-in-unreal-engine-5) documentation.

### Packet Overview Panel

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7019d480-0caf-4c99-bbcd-e25069dc01a8/packet-overview.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7019d480-0caf-4c99-bbcd-e25069dc01a8/packet-overview.png)

The Packet Overview panel displays a bar graph that shows the size (in bits) for every packet received or transmitted. This is useful for identifying large packets that need further investigation. Left-click the bar to select a packet.

Hovering over a packet displays its information. This information includes:

* Packet Index
* Sequence Number
* Content Size in bits
* Total Size in bytes, with unused bits
* A timestamp for when the packet was sent or received
* The packet's current status (delivered or undelivered)
* The connection state in which the packet was received
* Engine frame number of when the packet was sent or received

The reported size of each packet is before compression, so the actual data on the wire may be smaller than what the report shows.

Dropped packets are displayed in red. To select multiple packets, click to select an inital packet, then hold the **Shift** key and click other packets. You can highlight an event in the Packet View, to help you see how many bits that specific event is using in the packet. This makes it possible to quickly see how much bandwidth an event is using relative to other data.

You can choose to highlight either:

* The aggregated bitcount for all instances of the event; or
* The maximum bitcount used by a single event.

### Packet Content Panel

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6856b77b-6178-4867-97f8-0187c41f7e64/packet-contents.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6856b77b-6178-4867-97f8-0187c41f7e64/packet-contents.png)

The packet content panel displaying bunches of data contained in a packet. This includes information about replicated objects and properties.

The Packet Content panel displays the actual content of the currently selected packet. The packet's content displays as a hierarchical event graph starting with bit zero of the packet on the left side. This is the main tool to investigate the data contents in each packet down to the property level.

Packets consist of multiple levels of information. Level 0 is at the top of the Packet Content panel and displays the bunches contained in a packet. Each bunch is named after the channel it belongs to. If the reported bunch has its debug name set when reported, the `debugname` is used instead of the `channelname` to provide additional context. In the example in the image above, this consists of: `PacketHeader`, `Actor ChannelId:28`, and `Actor ChannelId:4`.

The second level typically displays replicated objects contained in the bunch. If the event has an assigned NetId (NetGUID), the ID is displayed also. Traced events display `NetId:NN` until the event is assigned a NetId. In the example in the image above, one of the replicated objects is `LyraAbilitySystemComponent` with `NetId:22`.

Events further down the event hierarchy display replicated properties and RPCs, including how many bits they wrote. In the example image above, one of these RPCs is `NetMulticast_InvokeGameplayCueExecuted_FromSpec` consisting of `1301` bits.

Hovering over an event displays all of the event's information.

The panel features controls to find a packet, or to find events belonging to a specific NetId.

#### Filtering

You can filter packet contents by NetId and event type in combination. This is useful to highlight specific events for a specific instance.

To filter by `NetId`, check the box next to **By NetId:** in the packet contents panel, then enter the `NetId` you want to filter by in the text box.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/12c220ea-8009-4a51-ad3c-dc02c084c2c2/filter-by-netid.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/12c220ea-8009-4a51-ad3c-dc02c084c2c2/filter-by-netid.png)

To filter by packet type, check the box next to **By Type:** in the packet contents panel, then select a packet type within the packet contents panel. The text box next to the filter **By Type:** box will populate with the type of packet content you chose. You can further filter by selecting **Highlight**, which highlights any packets that match your filter criteria.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8638a82e-d615-43bf-9970-7d75140efd1d/filter-by-type.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8638a82e-d615-43bf-9970-7d75140efd1d/filter-by-type.png)

You can navigate the Packet Content Panel and Packet Overview Panel using your keyboard. The up and down arrow keys will move between levels. The left and right arrow keys will move between events on the same level. If you hold the CTRL or CMD key and press the left or right arrow keys, you will move between packets.

### Connection Selection Panel

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a4de7087-f1d2-43da-9cb5-196ed0cd5be8/connection-selection.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a4de7087-f1d2-43da-9cb5-196ed0cd5be8/connection-selection.png)

The connection dropdown lists located at the top of the Packet Overview panel. This example shows Player 0's connection in a client game instance to a localhost server instance with incoming data selected.

The top of the Packet Overview panel has controls that let users select the data to display.

Three dropdown lists are available in the Connection Selection panel:

| Dropdown List | Description |
| --- | --- |
| **Game Instance** | Displays the created Game Instance for each unique NetDriver observed during a recording session. For example, when using PIE, there are separate instances for the server and each client. |
| **Connection** | This dropdown selects a specific connection, displaying every observed connection during the selected Game Instance's session. |
| **Connection Mode** | This dropdown controls whether to visualize incoming our outgoing data. |

### Net Stats Panel

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/35b8f228-978e-4ffc-9933-03725664487c/net-stats.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/35b8f228-978e-4ffc-9933-03725664487c/net-stats.png)

The Net Stats panel with events grouped by level.

The Net Stats panel lists all trace events for the selected packet range in the Packet Overview panel.

In addition to aggregating data based on a selected range, users can sort the list in ascending or descending order by the values in any active column. Right-click anywhere in the list to change the sort order, or to activate or deactivate columns.
The following columns are available:

* Type
* Level
* Instance Count
* Total Inclusive Size (bits)
* Max Inclusive Size (bits)
* Total Exclusive Size
* Max Exclusive Size

To filter events by name, use the "search net events or groups" field. Users can group according to these event types:

| Group Name | Description |
| --- | --- |
| Level | Creates one group for each level. |
| Flat | Creates a single group. Includes all Net Events. |
| Name | Creates one group for one letter |

Grouping by Level helps users understand their data better because the same name can appear on different levels. The following table describes these levels:

| Level | Description |
| --- | --- |
| **0** | Typically channel information that displays all bunches using the channel name. |
| **1** | Replicated Object (Actor), most events at this level show the serialized object. |
| **2** | Reports events originating from property replication or from RPCs. |
| **3** | Reports events when serializing properties. |
| **4** | Reports additional events when serializing properties, array content, and more. |

The Net Stats panel features a **!0** toggle to filter out event types that have no data in the selected range.

### Net Stats Counters

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bd69eade-4407-4466-bb12-498617b7f0f7/net-stats-counters.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bd69eade-4407-4466-bb12-498617b7f0f7/net-stats-counters.png)

The **Net Stats Counters** panel is where you can view stats counters related to the replication system for the selected packet or range of packets.

There are two different categories of stats:

* **Frame Stats**: Stats counters for the entire frame. This is typically used for reporting stat counters related to networking, for work that is shared between all connections. For example, how many objects are currently being updated on this frame.
* **Packet Stats**: Stats counters related to each specific packet. For example, how many objects were scheduled to be serialized, and how many actually did fit into the packet.

To add information to this panel, use the macros `UE_NET_TRACE_FRAME_STATSCOUNTER` and `UE_NET_TRACE_PACKET_STATSCOUNTER` in your C++ code. Data traced with either of these macros will be displayed in the Net Stats Counters panel.

#### Net Stats Counter Macros

To use the trace stats counter for information associated with the current frame, add `UE_NET_TRACE_FRAME_STATSCOUNTER` to your code. This macro is used as follows:

```
	UE_NET_TRACE_FRAME_STATSCOUNTER(<GAME_INSTANCE_ID>, <STAT_NAME>, <STAT_VALUE>, <NET_TRACE_VERBOSITY>)
Copy full snippet
```

To use the trace stats counter for information associated with the current packet, add `UE_NET_TRACE_PACKET_STATSCOUNTER` to your code. This macro is used as follows:

```
	UE_NET_TRACE_FRAME_STATSCOUNTER(<GAME_INSTANCE_ID>, <CONNECTION_ID>, <STAT_NAME>, <STAT_VALUE>, <NET_TRACE_VERBOSITY>)
Copy full snippet
```

## Example Data

To better understand the data that Networking Insights visualizes, we offer the following examples:

### Replicated Objects

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/936c18d7-0bfc-4b7e-93f3-ae7d45564a19/replicatedobjects.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/936c18d7-0bfc-4b7e-93f3-ae7d45564a19/replicatedobjects.png)

This is the initial replication of a new Actor--ReplicationGraphDebugActor, NetGUID 10.

Before the bunch containing the new actor, there is a NetGUID bunch containing all of the exported references from the new Actor, including NetGUIDS.

### RPCs

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e33a7ee2-b49c-4dcf-8622-0f0ff7465015/rpcs.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e33a7ee2-b49c-4dcf-8622-0f0ff7465015/rpcs.png)

This is an RPC named ClientAckGoodMove that targets PlayerPawn\_C with NetGUID 14.

GUIDs must be mapped.

### Split Bunches

Event data generated from transmitting a split bunch report with the first part--when receiving a split bunch, parts are reported first, and when all parts are received, events are reported with the final part.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7c9e45ab-b039-4efb-a5aa-b85d4bf67288/splitbunches_1.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7c9e45ab-b039-4efb-a5aa-b85d4bf67288/splitbunches_1.png)

This is a split outgoing bunch. Note that the events in the bunch are larger than the Bunch.

The next few packets look like the following:

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/56383105-d483-483f-b3b0-12574aa26c58/splitbunches_2.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/56383105-d483-483f-b3b0-12574aa26c58/splitbunches_2.png)



Incoming split bunches exhibit the opposite pattern, where events report with the last partial bunch.

### Sub-Objects

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/42d9fab9-1162-4140-bee0-e902922b8ed1/subobjects.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/42d9fab9-1162-4140-bee0-e902922b8ed1/subobjects.png)

This is a SubObject example--note that the second Actor after BotPawn\_C shares the same bunch.

* [performance](https://dev.epicgames.com/community/search?query=performance)
* [optimization](https://dev.epicgames.com/community/search?query=optimization)
* [profiling](https://dev.epicgames.com/community/search?query=profiling)
* [networking insights](https://dev.epicgames.com/community/search?query=networking%20insights)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Setup](/documentation/en-us/unreal-engine/networking-insights-in-unreal-engine?application_version=5.7#setup)
* [Using Networking Insights](/documentation/en-us/unreal-engine/networking-insights-in-unreal-engine?application_version=5.7#usingnetworkinginsights)
* [Networking Insights Window](/documentation/en-us/unreal-engine/networking-insights-in-unreal-engine?application_version=5.7#networkinginsightswindow)
* [Packet Overview Panel](/documentation/en-us/unreal-engine/networking-insights-in-unreal-engine?application_version=5.7#packetoverviewpanel)
* [Packet Content Panel](/documentation/en-us/unreal-engine/networking-insights-in-unreal-engine?application_version=5.7#packetcontentpanel)
* [Filtering](/documentation/en-us/unreal-engine/networking-insights-in-unreal-engine?application_version=5.7#filtering)
* [Connection Selection Panel](/documentation/en-us/unreal-engine/networking-insights-in-unreal-engine?application_version=5.7#connectionselectionpanel)
* [Net Stats Panel](/documentation/en-us/unreal-engine/networking-insights-in-unreal-engine?application_version=5.7#netstatspanel)
* [Net Stats Counters](/documentation/en-us/unreal-engine/networking-insights-in-unreal-engine?application_version=5.7#netstatscounters)
* [Net Stats Counter Macros](/documentation/en-us/unreal-engine/networking-insights-in-unreal-engine?application_version=5.7#netstatscountermacros)
* [Example Data](/documentation/en-us/unreal-engine/networking-insights-in-unreal-engine?application_version=5.7#exampledata)
* [Replicated Objects](/documentation/en-us/unreal-engine/networking-insights-in-unreal-engine?application_version=5.7#replicatedobjects)
* [RPCs](/documentation/en-us/unreal-engine/networking-insights-in-unreal-engine?application_version=5.7#rpcs)
* [Split Bunches](/documentation/en-us/unreal-engine/networking-insights-in-unreal-engine?application_version=5.7#splitbunches)
* [Sub-Objects](/documentation/en-us/unreal-engine/networking-insights-in-unreal-engine?application_version=5.7#sub-objects)
