<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/horde-build-automation-tutorial-for-unreal-engine?application_version=5.7 -->

# Horde Build Automation Tutorial

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
5. [Setting Up Your Production Pipeline](/documentation/en-us/unreal-engine/setting-up-your-production-pipeline-in-unreal-engine "Setting Up Your Production Pipeline")
6. [Horde](/documentation/en-us/unreal-engine/horde-in-unreal-engine "Horde")
7. [Horde Tutorials](/documentation/en-us/unreal-engine/horde-tutorials-for-unreal-engine "Horde Tutorials")
8. Horde Build Automation Tutorial

# Horde Build Automation Tutorial

A tutorial for using Horde build authentication with Unreal Engine.

![Horde Build Automation Tutorial](https://dev.epicgames.com/community/api/documentation/image/c060542d-022f-4d21-b0c3-052315c2863a?resizing_type=fill&width=1920&height=335)

 On this page

## Introduction

Horde implements a build automation system using BuildGraph as a scripting language, which supports Windows, Mac, and Linux. It integrates closely with Horde's remote execution capabilities, UnrealGameSync, and other tools in the Unreal Engine ecosystem.

The terms Continuous Integration (CI) and Continuous Delivery (CD) are common monikers for build automation, ensuring that the state of a project is continuously being monitored and that builds are produced regularly.

## Prerequisites

* Horde Server and one or more Horde Agents (see the [Horde Installation Tutorial](/documentation/en-us/unreal-engine/horde-installation-tutorial-for-unreal-engine))
* A configured Perforce server with a stream containing Unreal Engine 5.4 or later.
  + Legacy Perforce branches are not currently supported.
  + Horde may support other revision control systems in the future.

## Setup

1. Locate the `C:\ProgramData\Epic\Horde\Server` folder containing configuration files for the Horde Server.

   * The `C:\ProgramData` folder is hidden by default. You may have to enter it into the Windows Explorer address bar manually.
2. Open the `globals.json` file.

   * This file is one of two main configuration files for the server. The `server.json` file configures settings specific to this machine (such as other servers to communicate with, logging settings, etc.), while the `globals.json` file configures settings shared by all server instances in a multi-machine installation.
   * See [Configuration > Orientation](/documentation/en-us/unreal-engine/horde-orientation-for-unreal-engine) for more information.
   * See [Configuration > Schema > Globals.json](/documentation/en-us/unreal-engine/horde-schema-for-unreal-engine#globals) for detailed information on all settings.
3. Configure your Perforce server in the `perforceClusters` section of the config file.

   * A default configuration is included but commented out - configure the `serverAndPort` and `credentials` entries as appropriate for your deployment.
   * The server will reload any changes to `globals.json` automatically when the file is saved.
   * You may wish to go to the Horde Dashboard (<http://localhost:13340> by default), open the **Server** menu, and select **Status**. This page shows the status of various server subsystems, including the Perforce connection status - which should be confirmed as working.
4. Enable the example project by uncommenting the following lines in `globals.json`:

   ```
        "projects": [
            {
                "id": "ue5",
                "path": "ue5.project.json"
            }
        ]
   Copy full snippet
   ```

   * A project in Horde parlance is typically a game or project, analagous to a stream depot in Perforce. Epic has several streams under the `UE5` project on our internal Horde instance, such as `//UE5/Main`, `//UE5/Release-5.5`, `//UE5/Dev-Main-HordeDemo` and so on.
   * The referenced config file, `ue5.project.json` exists in the same directory and references a stream configured in `ue5-release-5.5.stream.json`. The name of this file is not important for this tutorial.
5. Open the `ue5-release-5.5.stream.json` file and update the `name` property to a stream on your Perforce server. The default is `//UE5/Release-5.5-HordeSync`.

   * You should update the `Project` and `ProjectPath` macros below to reference your project. By default, these are set to build Epic Games' **Lyra** sample.
6. At this point, you should see the **UE5** project listed in the menu bar on the Horde Dashboard. Click on this button and select the stream you configured above.

   * You may need to refresh the dashboard in your web browser for the project to appear.

## Default Jobs

The example `ue5-release-5.5.stream.json` file configures the appearance of its page in the Horde Dashboard, as well as job templates and agent types.

* A **job template** defines a set of parameters that are used to construct a [BuildGraph](https://docs.unrealengine.com/en-US/buildgraph-for-unreal-engine/) command line. Job templates are used to start jobs.
* An **agent type** defines a mapping from agents listed in BuildGraph script to a pool of machines that can execute it and settings for what those machines should sync from Perforce to execute the job.

After enabling the example stream, any agents connected to the server will start syncing Perforce workspaces necessary to support agent types that they match.

The default page for the example stream shows tabs across the top of the page, which can be used to group related job types. There are several predefined jobs on different tabs.

### Incremental

* **Incremental Build** - Builds the editor for your project and uploads editor builds to Horde that can be synced with UnrealGameSync. These jobs are designed to be fast, run frequently during the day, and use incremental workspaces that are not cleaned between runs. This allows them to start quickly and use intermediate artifacts produced on previous runs.

### Packaged Builds

* **Packaged Project Build** - Compiles and cooks a standalone game/client/server build for different target platforms and runs standard tests on it. These jobs run on non-incremental workspaces, restoring them to a pristine state before the job starts.

### Presubmit

* **Presubmit Tests** - Performs a quick editor compilation on a shelved changelist before submitting the change on behalf of the initiating user. The **P4VUtils** tool, which can be enabled through UnrealGameSync, provides extensions to Perforce P4V so you can initiate a presubmit build on a shelf through the UI.

### Utility

* **Installed Engine Build** - Creates an installed engine build similar to that which can be downloaded from the Epic Games Store. With Installed Engine Builds, you can use the engine like an SDK. This is designed for small teams that don't expect to modify the engine heavily.
* **Parameter Demo** - Shows the different types of parameters that can be configured through the Horde Dashboard and how to use them from a corresponding BuildGraph script (`Engine/Build/Graph/Examples/Parameters.xml`).
* **Remote Execution Test** - Tests compilation using UnrealBuildAccelerator. Horde passes settings to jobs through environment variables that allow UnrealBuildTool to connect to the server without any additional configuration.
* **Test Executor** - Runs a mock job with simulated errors or warnings, which is useful for testing connectivity to agents without syncing a Perforce workspace.

## See Also

* [Configuration > Build Automation](/documentation/en-us/unreal-engine/horde-build-automation-for-unreal-engine)

* [horde](https://dev.epicgames.com/community/search?query=horde)
* [bronze](https://dev.epicgames.com/community/search?query=bronze)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Introduction](/documentation/en-us/unreal-engine/horde-build-automation-tutorial-for-unreal-engine?application_version=5.7#introduction)
* [Prerequisites](/documentation/en-us/unreal-engine/horde-build-automation-tutorial-for-unreal-engine?application_version=5.7#prerequisites)
* [Setup](/documentation/en-us/unreal-engine/horde-build-automation-tutorial-for-unreal-engine?application_version=5.7#setup)
* [Default Jobs](/documentation/en-us/unreal-engine/horde-build-automation-tutorial-for-unreal-engine?application_version=5.7#defaultjobs)
* [Incremental](/documentation/en-us/unreal-engine/horde-build-automation-tutorial-for-unreal-engine?application_version=5.7#incremental)
* [Packaged Builds](/documentation/en-us/unreal-engine/horde-build-automation-tutorial-for-unreal-engine?application_version=5.7#packagedbuilds)
* [Presubmit](/documentation/en-us/unreal-engine/horde-build-automation-tutorial-for-unreal-engine?application_version=5.7#presubmit)
* [Utility](/documentation/en-us/unreal-engine/horde-build-automation-tutorial-for-unreal-engine?application_version=5.7#utility)
* [See Also](/documentation/en-us/unreal-engine/horde-build-automation-tutorial-for-unreal-engine?application_version=5.7#seealso)
