<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/trace-quick-start-guide-in-unreal-engine?application_version=5.7 -->

# Unreal Insights Trace Quick Start Guide

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
7. [Trace](/documentation/en-us/unreal-engine/trace-in-unreal-engine-5 "Trace")
8. Unreal Insights Trace Quick Start Guide

# Unreal Insights Trace Quick Start Guide

Get started with using Unreal Insights by following the setup steps below.

![Unreal Insights Trace Quick Start Guide](https://dev.epicgames.com/community/api/documentation/image/774ba2a1-1ece-4041-9df9-d2111c9e778b?resizing_type=fill&width=1920&height=335)

 On this page

## Setting Up Unreal Insights

When building **Unreal Insights** you will have multiple options available.

#### Option 1: Launch Unreal Insights from the Explorer

Check if you already have a prebuilt copy of Unreal Insights with your engine by navigating to `Engine\Binaries\Win64\UnrealInsights.exe`

![unreal-insights-executable-in-binaries-folder](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/85c1aaba-e857-4bc2-9019-598239bddd32/binaryexe.png)

#### Option 2: Build from Visual Studio

You can build Unreal Insights from your **Program**'s directory in your **Solution Explorer**.

![build-from-visual-studio](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7d8864e4-53f1-4723-90b7-78ed0b08afe6/visualbuild.png)

#### Option 3: From the Command Prompt

Navigate to **Start** > **Command Prompt**, then build Unreal Insights from your command directory.

```
		cd C:\MyEngineInstallLocation\

		Engine\Build\BatchFiles\RunUBT.bat UnrealInsights Win64 Development

Copy full snippet
```

#### Option 4: From the Editor

Start Unreal Insights from the **Unreal Editor** by navigating to **Tools** > **Unreal Insights** > **Run Unreal Insights**. Insights will attempt to compile automatically.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bdb7d5fb-8f3e-49d3-8fc3-61e6f0235920/runinsightseditor.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bdb7d5fb-8f3e-49d3-8fc3-61e6f0235920/runinsightseditor.png)

When running a Trace to profile your project data, you have multiple workflow options available depending on your Unreal Engine build and operating system.

## Default Tracing Workflow (Win64, Binary Launcher)

#### 1. Run Unreal Insights:

Navigate to your `Engine\Binaries\Win64` folder and double-click `UnrealInsights.exe`.

![unreal-insights-executable-in-binaries-folder](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6db621c9-91c9-4a07-a92c-8cc1ffd26559/binaryexe.png)

#### 2. Insights Session Browser:

When you launch the **Unreal Insights Session Browser**, you will notice that there are currently no live sessions available.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3f5913da-e244-4b2e-8314-e2182f4020b7/insightssessionbrowser.png)

#### 3. Run Your Game Project:

Launch the **Command Prompt** from your operating system and run the Lyra Game Sample.

```
	cd C:\MyEngineInstallLocation\

	Samples\Games\Lyra\Binaries\Win64\LyraGame.exe

Copy full snippet
```



If you have downloaded a sample of Lyra from the Epic Games Launcher, you can run Lyra from the default path `UnrealProjects\Lyra\Lyra.uproject`.

#### 4. Live Insights Session Browser:

Navigate back to the Unreal Insights Session Browser and observe that a new session has appeared with the "LIVE" status, indicating it is currently recording.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4a66a7d2-7a8b-4e65-982e-096338177e62/livesession.png)

#### 5. Check Your Trace Status:

In Lyra, press the tilde (`) twice to open the console, then type in the command:

```
	Trace.Status
Copy full snippet
```

![checking-the-trace-status](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/afe75a12-11be-4315-863c-56ffe42d3f7b/tracestatus.png)

The channels **Gpu**, **Bookmark**, **Frame**, **Cpu**, and **Log** are enabled by default.

If Unreal Insights is already running before starting your project, then Unreal Insights will connect to the local trace server automatically and the default trace channels will be enabled.

#### 6. Open Your Trace Session:

Navigate back to the Unreal Insights Session Browser, then double-click your `.utrace` file to open it for analysis in a new Unreal **Timing Insights** window.

To open a Trace file, you can drag and drop your `.utrace` file from the explorer onto the Unreal Insights Session Browser. Alternatively, you can open a .utrace file from a specific folder by clicking the **Arrow** button next to **Open Trace**, and selecting **Open File** from the drop-down menu.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/737ad03d-3b6e-4e50-8334-435248e04e4a/opentrace.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/737ad03d-3b6e-4e50-8334-435248e04e4a/opentrace.png)

Opening a trace launches a new instance of Unreal Insights. Timing Insights is the default component opened and provides you the capability to interact with a trace session to see how much time your project spends on various tasks.

Refer to the [Timing Insights](/documentation/en-us/unreal-engine/timing-insights-in-unreal-engine-5) documentation for more information on how to view your data for analysis.

### Advanced Controls of Tracing

Unreal Insights provides several Trace commands for you to control how your data is profiled.

* `Trace.SnapshotFile <filename>`: This writes a snapshot of the current in-memory trace buffer to a file. If you are already tracing actively, it does not interrupt the active trace, but instead records a second trace file in parallel just for this snapshot.
* `Trace.Bookmark <name>`: This emits a Bookmark event with the given string name. Bookmarks appear in Timing Insights as a vertical line at the time the Bookmark was recorded. Previously this was available through the API only as `TRACE_BOOKMARK()`.
* `Trace.Screenshot <Name> <bIncludeUI>`: As mentioned above, you can run this console command to generate a vertical line and optionally include the UI by specifying true or false for a screenshot in Timing Insights.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7e0a8976-82c0-4e34-8de5-42e8752ae52c/mysavedscreenshot.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7e0a8976-82c0-4e34-8de5-42e8752ae52c/mysavedscreenshot.png)

You may want to have visibility on specific trace channels like CPU or GPU profiling data, or to disable tracing a channel. Refer to the [Trace](/documentation/en-us/unreal-engine/trace-in-unreal-engine-5) and [Reference](/documentation/en-us/unreal-engine/unreal-insights-reference-in-unreal-engine-5) documentation for additional information on Trace commands.

## Late Connect

There may be instances where you forget to run the `UnrealInsights.exe` before launching your project, or perhaps you have discovered a situation you want to record without initially tracing from the beginning. You can **Late Connect** to Unreal Insights by following the steps below.

Before continuing, check the **Unreal Insights Session Browser** to ensure a live session is not already running. You can stop the connection by entering the console command:

```
	Trace.Stop
Copy full snippet
```

1. **Build**, **Cook**, or **Run** your project as you normally would.
2. Open **Unreal Insights**.
3. Click **Connection** to open the Connection tab. Confirm your desired connection settings, then click **Connect.**

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bb733cdf-2b7e-424b-abec-3088fc2bff8c/lateconnection.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bb733cdf-2b7e-424b-abec-3088fc2bff8c/lateconnection.png)

After a successful connection, click the **Trace Store** tab. A new LIVE session will appear in the Session list.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9f6cca5a-cf9b-4ce2-8125-cec2b4c54b04/livelateconnect.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9f6cca5a-cf9b-4ce2-8125-cec2b4c54b04/livelateconnect.png)

* [optimization](https://dev.epicgames.com/community/search?query=optimization)
* [insights](https://dev.epicgames.com/community/search?query=insights)
* [profiling](https://dev.epicgames.com/community/search?query=profiling)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Setting Up Unreal Insights](/documentation/en-us/unreal-engine/trace-quick-start-guide-in-unreal-engine?application_version=5.7#settingupunrealinsights)
* [Option 1: Launch Unreal Insights from the Explorer](/documentation/en-us/unreal-engine/trace-quick-start-guide-in-unreal-engine?application_version=5.7#option1:launchunrealinsightsfromtheexplorer)
* [Option 2: Build from Visual Studio](/documentation/en-us/unreal-engine/trace-quick-start-guide-in-unreal-engine?application_version=5.7#option2:buildfromvisualstudio)
* [Option 3: From the Command Prompt](/documentation/en-us/unreal-engine/trace-quick-start-guide-in-unreal-engine?application_version=5.7#option3:fromthecommandprompt)
* [Option 4: From the Editor](/documentation/en-us/unreal-engine/trace-quick-start-guide-in-unreal-engine?application_version=5.7#option4:fromtheeditor)
* [Default Tracing Workflow (Win64, Binary Launcher)](/documentation/en-us/unreal-engine/trace-quick-start-guide-in-unreal-engine?application_version=5.7#defaulttracingworkflow(win64,binarylauncher))
* [1. Run Unreal Insights:](/documentation/en-us/unreal-engine/trace-quick-start-guide-in-unreal-engine?application_version=5.7#1rununrealinsights:)
* [2. Insights Session Browser:](/documentation/en-us/unreal-engine/trace-quick-start-guide-in-unreal-engine?application_version=5.7#2insightssessionbrowser:)
* [3. Run Your Game Project:](/documentation/en-us/unreal-engine/trace-quick-start-guide-in-unreal-engine?application_version=5.7#3runyourgameproject:)
* [4. Live Insights Session Browser:](/documentation/en-us/unreal-engine/trace-quick-start-guide-in-unreal-engine?application_version=5.7#4liveinsightssessionbrowser:)
* [5. Check Your Trace Status:](/documentation/en-us/unreal-engine/trace-quick-start-guide-in-unreal-engine?application_version=5.7#5checkyourtracestatus:)
* [6. Open Your Trace Session:](/documentation/en-us/unreal-engine/trace-quick-start-guide-in-unreal-engine?application_version=5.7#6openyourtracesession:)
* [Advanced Controls of Tracing](/documentation/en-us/unreal-engine/trace-quick-start-guide-in-unreal-engine?application_version=5.7#advancedcontrolsoftracing)
* [Late Connect](/documentation/en-us/unreal-engine/trace-quick-start-guide-in-unreal-engine?application_version=5.7#lateconnect)
