<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/horde-unrealgamesync-tutorial-for-unreal-engine?application_version=5.7 -->

# Horde UnrealGameSync Tutorial

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
8. Horde UnrealGameSync Tutorial

# Horde UnrealGameSync Tutorial

A tutorial on using Horde and UnrealGameSync together for Unreal Engine.

![Horde UnrealGameSync Tutorial](https://dev.epicgames.com/community/api/documentation/image/05246398-7b7a-465e-977a-0cb8586a939d?resizing_type=fill&width=1920&height=335)

 On this page

## Introduction

Projects built with Unreal Engine typically require close collaboration between artists, designers and engineers - especially with technologies such as Blueprint, which allow interop of C++ code and gameplay scripting.

Coordinating these development efforts can be challenging due to the way that different developers interact with the revision control system - engineers may modify code and build their own editor, then submit assets created with those code changes, for example - and artists need to be able to sync and use those same assets in lock-step, without having to navigate a code IDE.

**UnrealGameSync** (often abbreviated as **UGS**) is a tool to provide a unified frontend to developers syncing a project from **Perforce**, providing content creators and engineers with the same view of the repository. Engineers can use it to version their editor correctly for editing assets, and content creators can use it to sync pre-built editor binaries produced by Horde's build automation system. The interface provides an overview of the health of the project and the state of recent CI builds, and acts as a jumping-off point for launching other tools.

Epic Games uses UnrealGameSync for development on all internal projects, such as Fortnite. More information about UnrealGameSync can be [found here](/documentation/en-us/unreal-engine/unreal-game-sync-ugs-for-unreal-engine).

The graphical UnrealGameSync client is only available on Windows. A command line version is available for use on MacOS and Linux.

![UnrealGameSync](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/efb65482-9b1e-42ad-bccc-6b2606f8d810/unrealgamesync-main.png)

## Prerequisites

* Horde Server installation (see the [Horde Installation Tutorial](/documentation/en-us/unreal-engine/horde-installation-tutorial-for-unreal-engine)).

## Installation (Windows)

1. Navigate to the `Tools > Downloads` page on the Horde dashboard.
2. Click the `Download` button to the right of the `UnrealGameSync` item, and run the downloaded installer.
3. After installation, you'll be prompted to configure auto-update settings for UnrealGameSync. Select 'Horde' and enter the path to your Horde server. This will also configure UnrealGameSync to fetch build information and metadata from other users from Horde.

   You can modify this later using the `Options > Application Settings...` dialog inside UnrealGameSync.
4. Select `Open Project...`, and select a project you already have synced locally, or create a new workspace with the project to sync.

## Installation (Mac)

1. Install the [.NET 8 Runtime](https://dotnet.microsoft.com/en-us/download) and [Helix Command Line Tools](https://www.perforce.com/products/helix-core-apps/command-line-client).
2. Open a terminal and run:

   ```
        curl "{{ HORDE_SERVER_URL }}/api/v1/tools/ugs-cmd?action=download" -o ~/ugs.zip
        unzip -eo ~/ugs.zip -d ~/ugs/
        ~/ugs/ugs install
        source ~/.zshrc
   Copy full snippet
   ```
3. Run `ugs -help` for information on available commands.

## Installation (Linux)

1. Install the [.NET 8 Runtime](https://dotnet.microsoft.com/en-us/download) and [Helix Command Line Tools](https://www.perforce.com/products/helix-core-apps/command-line-client).
2. Open a terminal and run:

   ```
        curl "{{ HORDE_SERVER_URL }}/api/v1/tools/ugs-cmd?action=download" -o ~/ugs.zip
        unzip -eo ~/ugs.zip -d ~/ugs/
        ~/ugs/ugs install
        source ~/.bashrc
   Copy full snippet
   ```
3. Run `ugs -help` for information on available commands.

## Server Setup

### Default Perforce Server

* If your whole team uses the same Perforce server, you can configure UGS with a default value by modifying the server's [globals.json](/documentation/en-us/unreal-engine/horde-orientation-for-unreal-engine) file. As long as UGS is configured to use your Horde server, it will query this property on startup.

  ```
        "parameters": {
            "ugs": 
            {
                // Set the default Perforce server for anyone using UGS.
                "defaultPerforceServer": "perforce:1666"
            }
        }
  Copy full snippet
  ```

### Editor Builds

UnrealGameSync was originally created with small teams in mind, where artists would be able to sync and build code code changes locally without any infrastructure (eg. a CI/CD system) set up. While it can still be used in this way, for larger teams it's typically easier to have Horde's build automation system generate editor builds centrally.

UnrealGameSync can query Horde for available editor builds (often referred to aspre-compiled binaries or PCBs). These builds can be stored and discovered on the Horde server automatically. Earlier builds of UnrealGameSync required storing these binaries in a zip file in Perforce; this is no longer necessary.

The example stream configuration referenced from Horde's [build automation](/documentation/en-us/unreal-engine/horde-build-automation-tutorial-for-unreal-engine) tutorial guide includes an **Incremental Build** job template which will compile and upload these binaries using the `Engine/Build/Graph/Examples/BuildEditorAndTools.xml` [BuildGraph](/documentation/en-us/unreal-engine/buildgraph-for-unreal-engine) script.

Once you've built your project's editor on Horde, check the `Options > Sync Precompiled Binaries` option to download them rather than building locally.

### Badges

You can surface information from Horde's build automation system directly in UGS by using the BuildGraph `<Label>` element.

* [horde](https://dev.epicgames.com/community/search?query=horde)
* [bronze](https://dev.epicgames.com/community/search?query=bronze)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Introduction](/documentation/en-us/unreal-engine/horde-unrealgamesync-tutorial-for-unreal-engine?application_version=5.7#introduction)
* [Prerequisites](/documentation/en-us/unreal-engine/horde-unrealgamesync-tutorial-for-unreal-engine?application_version=5.7#prerequisites)
* [Installation (Windows)](/documentation/en-us/unreal-engine/horde-unrealgamesync-tutorial-for-unreal-engine?application_version=5.7#installation(windows))
* [Installation (Mac)](/documentation/en-us/unreal-engine/horde-unrealgamesync-tutorial-for-unreal-engine?application_version=5.7#installation(mac))
* [Installation (Linux)](/documentation/en-us/unreal-engine/horde-unrealgamesync-tutorial-for-unreal-engine?application_version=5.7#installation(linux))
* [Server Setup](/documentation/en-us/unreal-engine/horde-unrealgamesync-tutorial-for-unreal-engine?application_version=5.7#serversetup)
* [Default Perforce Server](/documentation/en-us/unreal-engine/horde-unrealgamesync-tutorial-for-unreal-engine?application_version=5.7#defaultperforceserver)
* [Editor Builds](/documentation/en-us/unreal-engine/horde-unrealgamesync-tutorial-for-unreal-engine?application_version=5.7#editorbuilds)
* [Badges](/documentation/en-us/unreal-engine/horde-unrealgamesync-tutorial-for-unreal-engine?application_version=5.7#badges)
