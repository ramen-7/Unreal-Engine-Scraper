<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine?application_version=5.7 -->

# Unreal Insights

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
6. Unreal Insights

# Unreal Insights

Profile your project's performance with Unreal Insights.

![Unreal Insights](https://dev.epicgames.com/community/api/documentation/image/815f5238-e1b3-404d-81fc-b892d427d6db?resizing_type=fill&width=1920&height=335)

 On this page

**Unreal Insights** is a telemetry capture and analysis suite that can capture events from your project at high data rates. Unreal Insights helps you identify areas of data that might require optimization.

The major components of Unreal Insights are:

* **Trace events**, which contain `EventName` and `FieldName` parameters to define an event and specify a field that the event should include.
* The **Unreal Trace Server**, which records and saves traces from the application.
* **Unreal Insights**, which analyzes and visualizes the data.

![insights-diagram](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6c9ad598-f1ce-4512-af15-793356bc7e85/insightsdiagram.jpg)

Visualization of the major components of the Unreal Insights framework.

Trace sessions are self-describing, and compatible with different engine release versions. They are stored in `.utrace` files. Any companion data that is generated is stored in `.ucache` files located within the same directory as your trace files.

## Setting Up Unreal Insights

### Launch From Editor

To start Unreal Insights from the **Unreal Editor**, navigate to the **Trace/Insights Status Bar Widget** located in the bottom toolbar of the Editor.

![insights-widget](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a1f9d0c0-c124-44de-aa4a-a71b2ed88ce3/insightswidget.png)

When you run a Trace to profile your project data, you can choose from multiple workflow options that vary depending on your Unreal Engine Build and Operating System. For more information about these workflow options, see the following pages:

* [Trace](/documentation/en-us/unreal-engine/trace-in-unreal-engine-5)
* [Trace Quick Start Guide](/documentation/en-us/unreal-engine/trace-quick-start-guide-in-unreal-engine)

### Launch a prebuild of Unreal Insights

If you installed a binary version of Unreal Engine you should have a compiled version of Unreal Insights located in the following directory:

```
Engine\Binaries[Platform]\UnrealInsights[.exe] 	
Copy full snippet
```

### Build From Source

If you don't have a binary version of the engine installed, or you want to compile Unreal Insights from source, you can use the following options:

* **Using an Integrated Development Enviroment (IDE)**. Find the UnrealInsights target located in the Programs folder.
* **From the command prompt**. In your engine installation folder build Unreal Insights using the Unreal Build Tool:

On Windows:

```
Engine/Build/BatchFiles/RunUBT.bat UnrealInsights Win64 Development
Copy full snippet
```

On Linux or Mac:

```
./Engine/Build/BatchFiles/RunUBT.sh UnrealInsights [Linux|Mac] Development
Copy full snippet
```

## Trace

**Trace** is a structured logging framework for tracing instrumentation events from a running process. The **Unreal Trace Server** runs in the background as a single server instance and can be shared between multiple projects or branches. It is an optimized program that has minimal impact on performance and does not include a User Interface.

The **Trace Server** is launched automatically by a separate server process executable, `UnrealTraceServer.exe`, which is located in the `Engine/Binaries/Win64` directory folder.

The **Trace Server** has two components:

* The **Trace Recorder** listens on port 1981 for incoming trace connections and records the live trace stream.
* The **Trace Store** stores the recorded traces as files in a folder. It watches this folder for changes and exposes the list of available traces to Unreal Insights UI.

The **Trace Server** stores configuration and log files in:

* Windows: `%LOCALAPPDATA%/UnrealEngine/Common/UnrealTrace`
* MacOS: `~/UnrealEngine/UnrealTrace`
* Linux: `~/UnrealEngine/UnrealTrace`

The default `Store` folder is created here.

For additional documentation see the following pages:

* [Trace](/documentation/en-us/unreal-engine/trace-in-unreal-engine-5)
* [Trace Quick Start Guide](/documentation/en-us/unreal-engine/trace-quick-start-guide-in-unreal-engine)
* [Trace Developer Guide](/documentation/en-us/unreal-engine/developer-guide-to-tracing-in-unreal-engine)

### Shut Down Trace Server

The server can be shut down using the "kill" command:

`> UnrealTraceServer kill`

### Configuring the Unreal Trace Server

You can configure the Unreal Trace Server to add additional directories to scan for trace files like the download folder or the profiling directory of a specific project. In Unreal Insights, you can control these settings to:

* Set the trace store directory. This is the location where new traces are saved.

  [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6ded5fdd-2c3d-48e2-aff1-693c96c72d4e/settracedirectory.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6ded5fdd-2c3d-48e2-aff1-693c96c72d4e/settracedirectory.png)
* Set additional trace directories and additional sources for trace files, for example, your user Download folder.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dadddbe0-ede2-487f-ac09-bf70befbe72a/colorfilter.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dadddbe0-ede2-487f-ac09-bf70befbe72a/colorfilter.png)

When configured with additional watch folders, multiple traces, and their corresponding trace file origin will be displayed with the associated color

* The Unreal Trace Server can store settings persistently while your computer is shut down or restarted.

As of UE 5.3, the Unreal Trace Server is enabled for all desktop platforms. This deprecates the store which was hosted in Unreal Insights for Linux and Mac.

Follow the steps below to Configure the Unreal Trace Server.

1. Open Unreal Insights. This will start the Unreal Trace Server, if not already running, on Windows, Mac, or Linux
2. Click on the **Manage store settings** dropdown button then modify the default store directory by clicking the "Set Trace Store directory" button. When starting a new trace the file will be stored in this directory.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e944af6f-12de-4aea-8f2c-a1153b5e8fab/managestoresettings.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e944af6f-12de-4aea-8f2c-a1153b5e8fab/managestoresettings.png)
3. The old trace store directory is automatically added to watch folders.
4. You can add one or more watch folders by clicking the **Add directory** button. If the new folder contains trace files they will appear in the session list with an icon colored by a unique color.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1876d5ca-9d13-47f6-ac30-7540e8081748/adddirectory.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1876d5ca-9d13-47f6-ac30-7540e8081748/adddirectory.png)

## Unreal Insights Session Browser

The Unreal Insights [Session Browser](/documentation/en-us/unreal-engine/unreal-insights-session-browser-for-unreal-engine) is an interface to observe trace data. To launch the browser, navigate to the bottom toolbar, and click **Trace** > **Insights** > **Unreal Insights** (**Session Browser**.)

### Trace Store

The **Trace Store** is an interface for you to observe and manage all of your stored Trace Sessions. The recorded traces are stored as files in a folder and Unreal Insights watches this folder for any data changes and then exposes the list of available traces to Unreal Insights UI.

![session-browser](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bf11d388-91d0-495e-86ce-d490cea1bf3c/sessionbrowser.png)

For more information, see the [Session Browser](/documentation/en-us/unreal-engine/unreal-insights-session-browser-for-unreal-engine) page.

### Connection Tab

The connection tab provides an interface to connect to a running game or editor with a trace server. It features multiple options to change your connection settings.

![connection-tab](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f1956e7b-0acf-4a2e-8104-5e69c1a8e47a/connectiontab.png)

For more information, see the [Session Browser](/documentation/en-us/unreal-engine/unreal-insights-session-browser-for-unreal-engine) page.

### Load a Trace for Analysis

There are multiple options to choose to load a Trace for Analysis. You can:

* Double-click any trace session in the Unreal Insights Browser.
* Select a trace session and click **Open Trace**.
* Search for `.utrace` files in other locations by using the **Open Trace** drop-down arrow.
* Start an analysis of a respective trace file immediately, drag and drop a .utrace file from Explorer over the Unreal Insights window.

![trace-drop-down-menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/552595ec-5ce3-43ff-992a-0e099db0d9f2/tracedropdown.png)

For more information, see the [Session Browser](/documentation/en-us/unreal-engine/unreal-insights-session-browser-for-unreal-engine) page.

### Live Connect

If a live Trace session connects to the tool, it also appears in the list. Live sessions display the word **LIVE** in the status column and update in real-time while you analyze them. Otherwise, they are identical to pre-recorded sessions.

![live-connect](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/91a0b2f2-1608-4a75-bb4c-74708045cef4/liveconnect.png)

The tool can connect to multiple sessions at the same time, and it automatically records data for all of them as the data streams in. To analyze these sessions in real-time, load them from the list the same way you load pre-recorded sessions.

For more information, see the [Session Browser](/documentation/en-us/unreal-engine/unreal-insights-session-browser-for-unreal-engine) page.

## Insights Menu

When viewing a session in Unreal Insights, you can select Menu in the upper-left corner of the window to access the menu.

In the menu, you can access several functions, including the following:

* **Import Table** - Import a `.csv` or `.tsv` file into an Insights table.
* **Session Browser** - Opens the Unreal Insights Session Browser window.
* **Open Trace File** - Opens a specified trace file for analysis.
* **Auto Open Live Trace** - If enabled, analysis starts automatically for each new live trace session, replacing the current analysis session.

## Timing Insights Window

The **Timing Insights** window collects performance data. It displays the data for **CPU** and **GPU** tracks. These tracks feature multiple sub-menus to help you sort and visualize the various processing tasks and the amount of time your project spends on executing them.

![timing-insights-window](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/aed2ff0a-2cf8-4eaa-8c0e-442c8bdaff52/timinginsightswindow.jpg)

The Timing Insights window features the Frames panel (1), the Timing panel filters (2), the Timing panel (3), the Log panel (4),Timers and Counters tabs (5) and the Callers and Callees panels (6).

See the [Timing Insights](/documentation/en-us/unreal-engine/timing-insights-in-unreal-engine-5)

## Memory Insights

The **Memory Insights** component allows you to investigate memory usage and call stack tracing in your project.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9b607fbe-84a8-40b2-b141-566546a4d2e2/memoryinsightswindow.jpg)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9b607fbe-84a8-40b2-b141-566546a4d2e2/memoryinsightswindow.jpg)

Memory Insights traces events for every allocation, reallocation, or free event that occurs during runtime, then reconstructs that memory usage pattern during analysis.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2b27f40d-03fc-4c09-a9a4-0f810c1bde3f/allocationtable.jpg)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2b27f40d-03fc-4c09-a9a4-0f810c1bde3f/allocationtable.jpg)

See the [Memory Insights](/documentation/en-us/unreal-engine/memory-insights-in-unreal-engine) documentation for instructions on how to set up, trace, query, and sort your data.

## Networking Insights

Unreal Insights includes **Networking Insights** to analyze, optimize and debug network traffic.

Refer to the [Networking Insights](/documentation/en-us/unreal-engine/networking-insights-in-unreal-engine) for additional documentation.

## Slate Insights

**Slate Insights** extends Unreal Insights to help developers improve the performance of their UI. it provides tools to identify the root cause of a specific Slate and UMG update.

See [Slate Insights](/documentation/en-us/unreal-engine/slate-insights-in-unreal-engine) for additional documentation.

## Asset Loading Insights

**Asset Loading Insights** provides a way to profile the amount of time it takes to load a project's assets into UnrealEngine. Asset Loading Insights is based on the data traced from the AssetLoadTime trace channel.

This profiling tool is useful in several ways, including the following:

* Viewing details about data sets per asset type.
* Assessing the load order of packages
* Determining if AsyncLoading is respecting package priorities as expected.
* Filtering the Asset Loading tracks.

## Cooking Insights

**Unreal Cooking Insights** allows you to gather and display information about the way packages are cooked in your project. Long cooking times can significantly affect the productivity of teams that are working on larger projects. By displaying the time it takes to cook each package, you can observe which packages to focus your investigation into optimizing.
See [Cooking Insights](/documentation/en-us/unreal-engine/unreal-cooking-insights-in-unreal-engine-5) for additional documentation.

## Reference

To get the most out of the many features that ship with **Unreal Insights**, You can customize your project's output with macros and command-line options.

Refer to the [Reference](/documentation/en-us/unreal-engine/unreal-insights-reference-in-unreal-engine-5) for additional documentation.

## Topics

[![Session Browser](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5284fe62-97df-443f-928c-efd5cda5a541/placeholder_topic.png)

Session Browser

Browse trace sessions to analyze with Unreal Insights.](/documentation/en-us/unreal-engine/unreal-insights-session-browser-for-unreal-engine)
[![Trace Control Tab](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d2773b75-43f3-46b0-9764-c6ce06cb992b/placeholder_topic.png)

Trace Control Tab

Use the Trace Control tab to start and control traces for running sessions of a project.](/documentation/en-us/unreal-engine/using-the-trace-control-tab-in-unreal-insights-for-unreal-engine)
[![Timing Insights](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f5e85a23-1676-4e99-87f9-1ad66fd622cd/placeholder_topic.png)

Timing Insights

An Overview of the Timing Insights Window in Unreal Insights.](/documentation/en-us/unreal-engine/timing-insights-in-unreal-engine-5)
[![Trace](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b528e378-9b54-40a1-923b-cbd5108f8274/diagram.png)

Trace

An overview of the Trace logging framework in Unreal Insights.](/documentation/en-us/unreal-engine/trace-in-unreal-engine-5)
[![Memory Insights](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a700b12e-7175-4957-b788-33d8a71e4b06/memoryinsights.png)

Memory Insights

An Overview of Memory Insights](/documentation/en-us/unreal-engine/memory-insights-in-unreal-engine)
[![Networking Insights](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8a38da4c-279c-40ab-9da3-96ea0f727a18/placeholder_topic.png)

Networking Insights

Overview of Networking Insights, the network performance profiling tool](/documentation/en-us/unreal-engine/networking-insights-in-unreal-engine)
[![Slate Insights](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/740b1d21-c247-4861-928e-bd165861da53/placeholder_topic.png)

Slate Insights

Overview of Slate Insights, an extension of Unreal Insights that helps users debug Slate and Unreal Motion Graphics (UMG).](/documentation/en-us/unreal-engine/slate-insights-in-unreal-engine)
[![Unreal Insights Reference](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e2199bdc-1be1-49a6-8aba-8b70a4c8d388/placeholder_topic.png)

Unreal Insights Reference

Unreal Insights reference covering input shortcuts, macros, and command-line options](/documentation/en-us/unreal-engine/unreal-insights-reference-in-unreal-engine-5)

* [optimization](https://dev.epicgames.com/community/search?query=optimization)
* [insights](https://dev.epicgames.com/community/search?query=insights)
* [profiling](https://dev.epicgames.com/community/search?query=profiling)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Setting Up Unreal Insights](/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine?application_version=5.7#settingupunrealinsights)
* [Launch From Editor](/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine?application_version=5.7#launchfromeditor)
* [Launch a prebuild of Unreal Insights](/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine?application_version=5.7#launchaprebuildofunrealinsights)
* [Build From Source](/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine?application_version=5.7#buildfromsource)
* [Trace](/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine?application_version=5.7#trace)
* [Shut Down Trace Server](/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine?application_version=5.7#shutdowntraceserver)
* [Configuring the Unreal Trace Server](/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine?application_version=5.7#configuringtheunrealtraceserver)
* [Unreal Insights Session Browser](/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine?application_version=5.7#unrealinsightssessionbrowser)
* [Trace Store](/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine?application_version=5.7#tracestore)
* [Connection Tab](/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine?application_version=5.7#connectiontab)
* [Load a Trace for Analysis](/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine?application_version=5.7#loadatraceforanalysis)
* [Live Connect](/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine?application_version=5.7#liveconnect)
* [Insights Menu](/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine?application_version=5.7#insightsmenu)
* [Timing Insights Window](/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine?application_version=5.7#timinginsightswindow)
* [Memory Insights](/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine?application_version=5.7#memoryinsights)
* [Networking Insights](/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine?application_version=5.7#networkinginsights)
* [Slate Insights](/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine?application_version=5.7#slateinsights)
* [Asset Loading Insights](/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine?application_version=5.7#assetloadinginsights)
* [Cooking Insights](/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine?application_version=5.7#cookinginsights)
* [Reference](/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine?application_version=5.7#reference)
* [Topics](/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine?application_version=5.7#topics)
