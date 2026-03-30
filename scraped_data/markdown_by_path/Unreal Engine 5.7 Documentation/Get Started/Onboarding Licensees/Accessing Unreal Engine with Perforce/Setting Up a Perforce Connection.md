<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-a-perforce-connection-with-unreal-engine?application_version=5.7 -->

# Setting Up a Perforce Connection

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
5. [Get Started](/documentation/en-us/unreal-engine/get-started "Get Started")
6. [Onboarding Licensees](/documentation/en-us/unreal-engine/onboarding-licensees-in-unreal-engine "Onboarding Licensees")
7. [Accessing Unreal Engine with Perforce](/documentation/en-us/unreal-engine/accessing-unreal-engine-with-perforce "Accessing Unreal Engine with Perforce")
8. Setting Up a Perforce Connection

# Setting Up a Perforce Connection

Guide to connecting to Epic Games' Perforce server to obtain Unreal Engine builds.

![Setting Up a Perforce Connection](https://dev.epicgames.com/community/api/documentation/image/5039cc60-31c2-4aa2-80dd-39e658b67b07?resizing_type=fill&width=1920&height=335)

 On this page

Using the content of this page requires a custom license support agreement with Epic Games that includes access to the Unreal Engine P4 Perforce depot.

Epic Games makes QA-approved builds of Unreal Engine, as well as other specialized code drops, available to licensees through a Perforce depot that can be accessed externally. This is one of the methods licensees use to first obtain the engine, as well as update to new versions as they are released and it is deemed appropriate by the licensee. This document covers the steps to set up Perforce locally in order to connect to the Epic Games' Unreal Engine depot and sync to a build of the engine.

## Connectivity Policy

Please note that only one authorized user should log into the Perforce account. Multiple users logging into the same account is a violation of the Perforce terms of service.

Epic Games' guidance is for a single user or automation to use the account to sync engine builds to your local Perforce depot, and allow your staff access with their own individual Perforce accounts licensed by your company.

If you don’t already have a Perforce license for your team, it is [free for up to 5 users](https://www.perforce.com/products/helix-core/free-version-control) or you can [explore licensing options](https://www.perforce.com/how-buy).

The complete process for downloading builds or revisions of Unreal Engine from Epic Games' Perforce depot is detailed on the [Downloading Unreal Engine with Perforce](https://dev.epicgames.com/documentation/en-us/unreal-engine/downloading-unreal-engine-with-perforce) page.

## Installation and Configuration

### Setting Up P4V

The P4V client is the current client provided by Perforce. It provides access to versioned files through a graphical interface and also includes tools for merging and visualizing code evolution.

[![](https://dev.epicgames.com/community/api/documentation/image/eab6cfb5-d8aa-479e-8061-a259cb3b6004?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/eab6cfb5-d8aa-479e-8061-a259cb3b6004?resizing_type=fit)

The full P4V installer can be downloaded from the [Perforce Downloads](https://www.perforce.com/downloads) page. Refer to Perforce's [P4V documentation](https://help.perforce.com/helix-core/server-apps/p4v/current/Content/P4V/Home-p4v.html) for instructions on installing and setting up P4V.

Be sure to download the version that applies to your operating system, including 32- or 64-bit.

You must be running a 2017.2 or later version of a Perforce client

### Character Encoding

If you store Unicode files as text in Perforce, it will add in a 0xd to match the local line end; so the Unicode line end 0x0a 0x00 0x0d 0x00 will be converted to 0x0a 0x0d 0x00 0x0d 0x00 and break. However, when it does this, it will leave your local version unchanged (and working). Sync to a previous version and then back to head to see the problem.

Perforce defines UTF-8 as Unicode. UTF-16 is ideal, provided no one accidentally converts to ASCII. Binary also works OK provided you do not miss merging or multiple checkouts.

Unreal Engine will load ASCII or UTF-16 with BOM, provided they are valid files.

### Setting up Perforce for Unreal Engine Distribution

Your team is granted a single account on Epic Games’ Perforce P4 server from which you can download the Unreal Engine source. Follow the instructions below to set up a process for sharing builds with your team.

#### Perform initial setup and import

1. Create your own (local) P4 Server.
2. Create a stream’s depot on that server for importing into, for example: `//UE5`
3. Create a stream for the particular release you are importing from Epic, for example: `//UE5/Release-5.6.0`

   1. Do not add any files to this local stream – you will add them below as a separate step.
4. Create a workspace on the Epic Games Perforce P4 Server (see [Downloading Unreal Engine with Perforce](https://dev.epicgames.com/documentation/en-us/unreal-engine/downloading-unreal-engine-with-perforce)) and sync the data you want.

   1. Set the workspace Root folder to something like: `c:\UE5\release-5.6`
   2. Note the latest changelist you are syncing to (view the history tab in P4V with the stream selected).
5. Create a new connection in P4V to your own Perforce P4 Server.
6. Create a workspace for your new Stream (`//UE5/Release-5.6.0`)
7. Set the root of the workspace to be the same folder as for your workspace on the Epic Games Perforce P4 server (in this example, `c:\UE\release-5.6`).
8. Right click on the root folder and select **Mark for Add**.
9. Go to the pending changelists folder, and submit the changelist.

   1. In the description, note the particular changelist number you synced from the Epic Games server

### Get and Import a New Snapshot from Epic Games

This is a regular process using the workspaces you previously created. It is a modified subset of the steps above, and this workflow assumes you still have your workspaces as previously set up. You will import the latest changes.

1. Connect to the Epic Games Perforce P4 server

   1. Select the workspace you previously created.
   2. Click **Get Latest** to update the files.
   3. Note the latest changelist you synced to.
2. Connect to your local Perforce P4 Server.
3. Select the workspace you previously created.
4. Right click on the root folder and select **Reconcile offline work**.
5. Go to the pending changelists folder, and submit the changelist.

   1. In the description, note the particular changelist number you synced from the Epic Games server.

## Support

### Connection Issues

If you are unable to connect to the Perforce depot for any reason, please contact [developer-access@unrealengine.com](mailto:developer-access@unrealengine.com) or post on [Epic Pro Support](https://epicprosupport.epicgames.com/).

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Connectivity Policy](/documentation/en-us/unreal-engine/setting-up-a-perforce-connection-with-unreal-engine?application_version=5.7#connectivity-policy)
* [Installation and Configuration](/documentation/en-us/unreal-engine/setting-up-a-perforce-connection-with-unreal-engine?application_version=5.7#installation-and-configuration)
* [Setting Up P4V](/documentation/en-us/unreal-engine/setting-up-a-perforce-connection-with-unreal-engine?application_version=5.7#setting-up-p4-v)
* [Character Encoding](/documentation/en-us/unreal-engine/setting-up-a-perforce-connection-with-unreal-engine?application_version=5.7#character-encoding)
* [Setting up Perforce for Unreal Engine Distribution](/documentation/en-us/unreal-engine/setting-up-a-perforce-connection-with-unreal-engine?application_version=5.7#settingupperforceforunrealenginedistribution)
* [Perform initial setup and import](/documentation/en-us/unreal-engine/setting-up-a-perforce-connection-with-unreal-engine?application_version=5.7#performinitialsetupandimport)
* [Get and Import a New Snapshot from Epic Games](/documentation/en-us/unreal-engine/setting-up-a-perforce-connection-with-unreal-engine?application_version=5.7#getandimportanewsnapshotfromepicgames)
* [Support](/documentation/en-us/unreal-engine/setting-up-a-perforce-connection-with-unreal-engine?application_version=5.7#maintenance-and-support)
* [Connection Issues](/documentation/en-us/unreal-engine/setting-up-a-perforce-connection-with-unreal-engine?application_version=5.7#connection-issues)
