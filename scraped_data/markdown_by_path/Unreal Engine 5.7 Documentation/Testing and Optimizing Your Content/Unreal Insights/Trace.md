<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/trace-in-unreal-engine-5?application_version=5.7 -->

# Trace

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
7. Trace

# Trace

An overview of the Trace logging framework in Unreal Insights.

![Trace](https://dev.epicgames.com/community/api/documentation/image/1a8df367-be77-4f98-bfd6-6c79fd9c3abe?resizing_type=fill&width=1920&height=335)

 On this page

**Trace** is a structured logging framework for tracing instrumentation events from a running process. The modules **TraceLog** and **TraceAnalysis** are the principal modules that constitute the framework.
The **Unreal Trace Server** runs in the background as a single server instance and can be shared between multiple projects or branches. It is an optimized program that has minimal impact on performance and does not include a user interface.

The Trace Server launches automatically by a separate server process, `UnrealTraceServer.exe`, which is located in the `Engine/Binaries/Win64` directory folder.

[![insights-major-components-diagram](https://dev.epicgames.com/community/api/documentation/image/68c9bfb7-53a6-4103-812b-4b800ddc3aee?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/68c9bfb7-53a6-4103-812b-4b800ddc3aee?resizing_type=fit)

The Trace Server has two components:

* The **Trace Recorder** listens on port 1981 for incoming trace connections and records the live trace stream.
* The **Trace Store** stores the recorded traces as files in a folder. It watches this folder for changes and exposes the list of available traces to Unreal Insights UI.

An example of the path to the trace folder is:

C++

```
C:/Users/<user>/AppData/Local/UnrealEngine/Common/UnrealTrace/Store/001/
```

C:/Users/<user>/AppData/Local/UnrealEngine/Common/UnrealTrace/Store/001/

Copy full snippet(1 line long)

## Unreal Trace Server

Unreal Editor builds automatically launch the `UnrealTraceServer.exe`, when you make a connection from the Unreal Trace session browser. The Unreal Trace Server runs in the background as a single server instance and can be shared between multiple projects and branches.

[![trace-executable](https://dev.epicgames.com/community/api/documentation/image/35d0f92b-b520-4f70-a0fa-b723afe91304?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/35d0f92b-b520-4f70-a0fa-b723afe91304?resizing_type=fit)

You can shut down Unreal Trace Server by accessing your system's Task Manager, and navigating to the Processes tab.

[![task-manager](https://dev.epicgames.com/community/api/documentation/image/cb96addd-1279-4cd7-a410-bdc3524e1bc2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cb96addd-1279-4cd7-a410-bdc3524e1bc2?resizing_type=fit)

Unreal Trace Server runs in the background as a single instance that does not need to be terminated in order to launch a new version. It can receive and record data from multiple sources simultaneously.

Currently, we only support Unreal Trace Server for one user per machine. If multiple users are logged in simultaneously, then traces will be stored in the first user's trace directory, therefore leaving them inaccessible to other users.

## Trace Insights Widget

The **Trace Insights Widget** provides a way to control and manage your **Trace Data** using an Editor interface. You can access the **Trace Insights Widget** from the Editorby navigating to the bottom toolbar and clicking the **Trace** button.

[![Trace Button](https://dev.epicgames.com/community/api/documentation/image/7052ff6c-a02f-46e9-a6eb-7c27e1ee3905?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7052ff6c-a02f-46e9-a6eb-7c27e1ee3905?resizing_type=fit)

The follows sections describe settings within each category of the Trace menu.

### Trace Data

The **Trace Data** category contains settings on data channels, Trace bookmarks, Trace screenshots, and more.

[![Trace Data](https://dev.epicgames.com/community/api/documentation/image/d356fef9-0e03-4efe-aca4-087411ae0e4a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d356fef9-0e03-4efe-aca4-087411ae0e4a?resizing_type=fit)

#### Channels

Trace is capable of recording large amounts of data. You can choose which type of data to record by using **Trace Channels**.

Channels control the data rate when tracing. Each event type is tied to one or more channels. If the required channels are not enabled then the event will not be emitted to the trace stream.

[![Trace Channels](https://dev.epicgames.com/community/api/documentation/image/ebb6e42a-ac35-4b6d-b6a6-a20ee3595a4b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ebb6e42a-ac35-4b6d-b6a6-a20ee3595a4b?resizing_type=fit)

**Channel presets** group channels together to provide scenario-based entry points.

| Channel | Description |
| --- | --- |
| **Animation** | Animation Insights Plugin. |
| **AssetLoadTime** | Contains named CPU timers for `UObject::Serialize`. |
| **AssetMetadata** | Asset Names and Class Names as metadata for memory allocations. Requires **Metadata** channel. Used by **Memalloc** channel. |
| **Audio** | Audio Insights Plugin. |
| **AudioMixer** | AudioMixer Insights Plugin. |
| **Bookmark** | Low-frequency markers to signify important transitions. Bookmarks provide a quick overview of features such as level loading or engine boot phases. |
| **Callstack** | Callstack descriptions. Allows allocations to be associated with callstacks. |
| **ContextSwitch** | Trace context switch events. On Windows, game or editor runtime should be run as administrator. |
| **Cook** | Displays named CPU timers specific to cooking. This requires the CPU channel to be enabled. Cook will add the both the `CookByTheBook` and `SaveCookedPackage` CPU timing events. |
| **Counters** | Generic counters. Traces float and integer values over time. Counters Trace API. It enables the CSV Profiler Trace. |
| **Cpu** | Named CPU timers. Additional timers can be added by enabling the Stat Named Events channel from the Insights Widget or using the `-statnamedevents` command line argument. |
| **File** | File I/O trace channel that contains Open, ReOpen, Read, Write, Close events. |
| **Frame** | Game and Rendering frames. |
| **Gpu** | Named GPU timers. Based on GpuProfiler data. |
| **LoadTime** | Asset Loading Insights trace channel. Only works for runtime loading from the pak/iostore. |
| **Log** | Logs Messages. |
| **MemAlloc** | Memory allocations. Uses Module and Callstack. |
| **MemTag** | Memory tag statistics. Traces snapshots of memory usage per tag at regular rate. Relies on LLM subsystem for tracing. Implies "-llm". Available after `Init()`. |
| **Messaging** | UDP Messaging plugin. |
| **Metadata** | Support for generic metadata scopes. |
| **Module** | Module loading information. |
| **Net** | Networking trace channel. |
| **Niagara** | Niagara Plugin. |
| **Object** | GameplayInsights/RewindDebugger plugin. `UObject` classes, worlds, instances, and events. |
| **Physics** | [Chaos Visual Debugger](https://dev.epicgames.com/documentation/en-us/unreal-engine/chaos-visual-debugger-in-unreal-engine). |
| **RDG** | RDG Insights Plugin. |
| **RHICommands** | CPU or GPU named timers for RHI commands. |
| **RenderCommands** | CPU or GPU named timers for commands executed on the rendering thread. |
| **SaveTime** | Named CPU timers specific to package saving. |
| **Screenshot** | Captures screenshots triggered with `Trace.Screenshot` console command or using the `TRACE_SCREENSHOT()` API. |
| **Slate** | Slate Insights Plugin. |
| **StackSampling** | Trace stack sampling events based on Event Tracing for Windows (ETW). |
| **Stats** | Stats counters. Based on the Stats system. |
| **Task** | Task Graph trace channel. |
| **VisualLogger** | Visual Logger starts recording to file. |

The following channels are enabled by default:

* Bookmark
* Cpu
* Frame
* Gpu
* Log
* Region
* Screenshot

The MemAlloc, MemTag, and Module channels are grey because they must be run from the command the prompt. See [From the Command Prompt](https://dev.epicgames.com/documentation/en-us/unreal-engine/trace-in-unreal-engine-5)

You can define your own presets using config files added to the `[Trace.ChannelPresets]` category. See the [Trace Developer Guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/developer-guide-to-tracing-in-unreal-engine) for documentation.

#### Trace Screenshot

**Trace Screenshot** takes a picture of your project's viewport during that frame and sends it to the trace. By default, Trace Screenshot is enabled from the channel panel.   
  
You can take a Trace Screenshot in two ways:

* In the bottom toolbar, click **Trace >** **Trace Screenshot**.

  [![Trace Screenshot](https://dev.epicgames.com/community/api/documentation/image/d2c1826d-cca4-4cc2-977a-0587338564e6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d2c1826d-cca4-4cc2-977a-0587338564e6?resizing_type=fit)
* In the console, enter the command `trace.screenshot`.

When using Trace Screenshot, the Timing Insights timeline displays a vertical line that contains a name generated based on the current timestamp, using the date and time of your screenshot.

[![trace-screenshot](https://dev.epicgames.com/community/api/documentation/image/5b655993-9594-4ce6-acce-5e770b771b75?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5b655993-9594-4ce6-acce-5e770b771b75?resizing_type=fit)

#### Trace Bookmark

**Trace Bookmark** emits a `TRACE_BOOKMARK()` event with the given string name. When used from the Editor, both the screenshot and bookmark events will generate a name based on the current timestamp using the format of date and time.  
  
You can set a Trace Bookmark in two ways:

* In the bottom toolbar, click **Trace > Trace Bookmark**.

  [![Trace Bookmark](https://dev.epicgames.com/community/api/documentation/image/70347ac8-262b-475c-bea4-382ae874b6b7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/70347ac8-262b-475c-bea4-382ae874b6b7?resizing_type=fit)
* In the console, enter the command `trace.bookmark`.

Bookmarks and screenshots are visible in the **Timing Insights** tab. You can find them in the **markers track** docked on the top toolbar, underneath the **ruler track**. Bookmarks are available in the **Log** view.

[![trace-bookmark](https://dev.epicgames.com/community/api/documentation/image/647f856e-a772-423c-b370-02003b8e6e50?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/647f856e-a772-423c-b370-02003b8e6e50?resizing_type=fit)

[![log-window](https://dev.epicgames.com/community/api/documentation/image/d5d9d94e-7914-466b-814b-9509336a11db?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d5d9d94e-7914-466b-814b-9509336a11db?resizing_type=fit)

#### Stat Named Events

**Stat Named Events** provide additional profiling metrics. You can enable or disable them by clicking the **State Named Events** checkbox.

[![stat-named-events](https://dev.epicgames.com/community/api/documentation/image/4958e11a-6525-4ee0-9998-31863e02fe25?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4958e11a-6525-4ee0-9998-31863e02fe25?resizing_type=fit)

### Trace Destination

In the **Trace Destination** category, you can choose where to store your trace data.

[![Trace Destination](https://dev.epicgames.com/community/api/documentation/image/3fb02c95-b3b8-47ae-88c2-cb30a1110a15?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3fb02c95-b3b8-47ae-88c2-cb30a1110a15?resizing_type=fit)

| Option | Description |
| --- | --- |
| **Trace Store** | Writes the trace data to a file in its managed trace store directory. |
| **File** | Writes trace data directly to the specified file. |

### Tracing

The **Tracing** category contains settings for starting and stopping a recording, and saving Trace Snapshots.

[![Tracing](https://dev.epicgames.com/community/api/documentation/image/54bb62f6-da4f-4733-87b0-43c5eff7d186?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/54bb62f6-da4f-4733-87b0-43c5eff7d186?resizing_type=fit)

#### Start and Stop Recording

| Option | Description |
| --- | --- |
| **Start Trace** | Starts a trace to the selected trace destination. You can start a trace from the Trace Insights widget by clicking the **Start Trace** button. |
| **Stop Trace** | When a Trace is started, the Start Trace UI icon displays in red. You can stop the trace from recording by clicking the **Stop Trace** button. |

#### Save Trace Snapshot

There are two ways to save a **Trace Snapshot**:

* In the bottom toolbar, click the **Save Trace Snapshot** button.

  [![save-snapshot-button](https://dev.epicgames.com/community/api/documentation/image/2c6f9238-64b1-4c57-85e2-13d8ad0564dc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2c6f9238-64b1-4c57-85e2-13d8ad0564dc?resizing_type=fit)
* In the bottom toolbar, click **Trace** **>** **Save Trace Snapshot**.

  [![Save Trace Snapshot](https://dev.epicgames.com/community/api/documentation/image/63e6e88d-6842-452b-bbb9-e9204099fcdc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/63e6e88d-6842-452b-bbb9-e9204099fcdc?resizing_type=fit)

### Options

The **Options** category controls automation, such as automatically opening Unreal Insights or destination folders.

[![Options](https://dev.epicgames.com/community/api/documentation/image/87bf2244-a899-42e4-9648-37b63d6d6d5a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/87bf2244-a899-42e4-9648-37b63d6d6d5a?resizing_type=fit)

| Option | Description |
| --- | --- |
| **Open Live Session on Trace Start** | When tracing is started, the live session automatically opens in Unreal Insights.  This option only applies when Tracing in the Trace Store. |
| **Open Insights after Trace** | When tracing is stopped or a snapshot is saved, the recorded session automatically opens in Unreal Insights. |
| **Shown in Explorer after Trace** | When tracing is stopped or a snapshot is saved, the folder containing the recorded session automatically opens. |

### Locations

The **Locations** category controls where traces (saved to File and the Trace Server) are stored.

[![Locations](https://dev.epicgames.com/community/api/documentation/image/ce94db35-eb28-4816-8eb2-6bdded63f6a3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ce94db35-eb28-4816-8eb2-6bdded63f6a3?resizing_type=fit)

| Option | Description |
| --- | --- |
| **Open Trace Store Directory** | The location where traces saved to the Trace Server are stored. |
| **Open Profiling Directory** | Opens the profiling directory of the current project. This is the location where traces to the file are stored. |

### Insights

The **Insights** category contains settings that open Unreal Insights, live sessions, and recorded files.

[![Insights](https://dev.epicgames.com/community/api/documentation/image/a6cce4c3-2da2-461c-bb6d-4b559d2b00e6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a6cce4c3-2da2-461c-bb6d-4b559d2b00e6?resizing_type=fit)

| Option | Description |
| --- | --- |
| **Unreal Insights**(**Session Browser**) | Launches the Unreal Insights Session Browser. |
| **Open Live Session** | Opens the current live session. This is only possible when tracing to the store. |
| **Recent Traces** | Opens the latest traces recorded to the trace store or as a file. |

## Trace Status

You can check information about your **Connection**, **Memory Used**, **Important Events cache**, **Sent** data, **Enabled** and **Available** Trace channels by using the console command `Trace.Status`.

[![trace-status](https://dev.epicgames.com/community/api/documentation/image/9ad1cc36-29b9-4107-80d7-fe51d1d1b675?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9ad1cc36-29b9-4107-80d7-fe51d1d1b675?resizing_type=fit)

## Run Insights From the Command Prompt

To run Unreal Insights from the Command Prompt, follow these steps:

1. Navigate to your `Engine\Binaries\Win64` folder and double-click `UnrealInsights.exe`.

   [![unreal-insights-executable-in-binaries-folder](https://dev.epicgames.com/community/api/documentation/image/5b618536-1e69-4eed-9a40-f358b21347ee?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5b618536-1e69-4eed-9a40-f358b21347ee?resizing_type=fit)
2. Launch the **Command Prompt** from your operating system and run your project. In the following example, replace the installation path and project name with your own:

   C++

   ```
   |  |  |
   | --- | --- |
   |  | cd C:\[MyEngineInstallLocation]\ |
   |  | Samples\Games\Binaries\Win64\[YourProject].exe |
   ```

   cd C:\[MyEngineInstallLocation]\
   Samples\Games\Binaries\Win64\[YourProject].exe

   Copy full snippet(2 lines long)

## Tail Tracing

**Tail Tracing** tracks events over the last few seconds (depending on the buffer size). Therefore, any machines that may be able to display a lead-up.

The default size of the buffer is 4MB, however if you wish to modify or deactivate it, you can do so by entering using the console command `-tracetailmb=X`.

Setting **X** to **0 MB** will deactivate it and other values will change the buffer size accordingly.

## Late Connect

**Important events** are cached on the Unreal Engine client side, then sent to late-connecting machines during connection. Therefore, one-time events (Important Events) won't be missed before you can make a connection.

Insights can instruct remote running Unreal Engine instances to connect to the remote trace servers from its local UI instance without needing to involve the local machine.

Late connect can be initiated by navigating to **Unreal Insights** **>** **Connect**, or from the Editor console by entering any of the following commands or arguments:

* `"trace.send [ip]" / "trace.start [filename]"`
* `-trace.start [file] [channelSet] -tracehost=[ip]`
* `-tracefile = [filepath]`

Unreal Insights has a file-based caching system that makes it possible for the application to attach additional information to a trace. This can be used to retrieve previously calculated results faster, or store data that would otherwise be lost such as symbols. The cache is stored in a `.ucache` file next to the trace file.

## Trace User Guide

You can use different workflows to run traces in Unreal Insights. See the [Trace User Guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/trace-quick-start-guide-in-unreal-engine) for documentation.

## Trace Developer Guide

You can develop your own traces in Unreal Insights. See the [Trace Developer Guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/developer-guide-to-tracing-in-unreal-engine) for documentation.

* [optimization](https://dev.epicgames.com/community/search?query=optimization)
* [insights](https://dev.epicgames.com/community/search?query=insights)
* [profiling](https://dev.epicgames.com/community/search?query=profiling)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Unreal Trace Server](/documentation/en-us/unreal-engine/trace-in-unreal-engine-5?application_version=5.7#unreal-trace-server)
* [Trace Insights Widget](/documentation/en-us/unreal-engine/trace-in-unreal-engine-5?application_version=5.7#trace-insights-widget)
* [Trace Data](/documentation/en-us/unreal-engine/trace-in-unreal-engine-5?application_version=5.7#channels)
* [Channels](/documentation/en-us/unreal-engine/trace-in-unreal-engine-5?application_version=5.7#channels)
* [Trace Screenshot](/documentation/en-us/unreal-engine/trace-in-unreal-engine-5?application_version=5.7#trace-screenshot)
* [Trace Bookmark](/documentation/en-us/unreal-engine/trace-in-unreal-engine-5?application_version=5.7#trace-bookmark)
* [Stat Named Events](/documentation/en-us/unreal-engine/trace-in-unreal-engine-5?application_version=5.7#stat-named-events)
* [Trace Destination](/documentation/en-us/unreal-engine/trace-in-unreal-engine-5?application_version=5.7#trace-destination)
* [Tracing](/documentation/en-us/unreal-engine/trace-in-unreal-engine-5?application_version=5.7#tracing)
* [Start and Stop Recording](/documentation/en-us/unreal-engine/trace-in-unreal-engine-5?application_version=5.7#startandstoprecording)
* [Save Trace Snapshot](/documentation/en-us/unreal-engine/trace-in-unreal-engine-5?application_version=5.7#save-trace-snapshot)
* [Options](/documentation/en-us/unreal-engine/trace-in-unreal-engine-5?application_version=5.7#options)
* [Locations](/documentation/en-us/unreal-engine/trace-in-unreal-engine-5?application_version=5.7#locations)
* [Insights](/documentation/en-us/unreal-engine/trace-in-unreal-engine-5?application_version=5.7#insights)
* [Trace Status](/documentation/en-us/unreal-engine/trace-in-unreal-engine-5?application_version=5.7#trace-status)
* [Run Insights From the Command Prompt](/documentation/en-us/unreal-engine/trace-in-unreal-engine-5?application_version=5.7#run-insights-from-the-command-prompt)
* [Tail Tracing](/documentation/en-us/unreal-engine/trace-in-unreal-engine-5?application_version=5.7#tail-tracing)
* [Late Connect](/documentation/en-us/unreal-engine/trace-in-unreal-engine-5?application_version=5.7#late-connect)
* [Trace User Guide](/documentation/en-us/unreal-engine/trace-in-unreal-engine-5?application_version=5.7#trace-user-guide)
* [Trace Developer Guide](/documentation/en-us/unreal-engine/trace-in-unreal-engine-5?application_version=5.7#trace-developer-guide)
