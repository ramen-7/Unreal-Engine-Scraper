<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/downloading-unreal-engine-with-perforce?application_version=5.7 -->

# Downloading Unreal Engine with Perforce

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
8. Downloading Unreal Engine with Perforce

# Downloading Unreal Engine with Perforce

Instructions for downloading Unreal Engine source code with Perforce.

![Downloading Unreal Engine with Perforce](https://dev.epicgames.com/community/api/documentation/image/d4747983-e311-40a7-ac8a-2c533c9c75bd?resizing_type=fill&width=1920&height=335)

 On this page

Using the content of this page requires a custom license support agreement with Epic Games that includes access to the Unreal Engine P4 Perforce depot.

## Connecting to the Epic Games P4 Perforce Server

This section is intended for technical administrators connecting directly to the Epic Games P4 Perforce depot, to download the source code into a local depot. It should not be used by developers who need to set up a local build of Unreal Engine. Instead, developers should contact their technical administrator to get access to a local depot holding the Unreal Engine source code.

Connecting to the Epic Games Perforce P4 server requires using the SSL feature, and you must be running a 2017.2 or later version of a Perforce client (P4V, p4, or API). You can take advantage of latency based routing to automatically connect to the closest Perforce regional proxy by using the global DNS name. Alternatively, you can connect directly to a regional proxy to ensure you always connect to the closest one.

If you are running a local proxy, you must connect through a broker instead of using the region proxy servers. You can connect to the global broker using the address below:

`ssl:p4-licensee.epicgames.com:1666`

Port `1667` is also valid, and you can use it for troubleshooting login issues.

1. Install the **P4V Perforce client for Windows**. The client can be downloaded from the [Perforce Downloads](https://www.perforce.com/downloads/helix-visual-client-p4v) page.
2. In the **Open Connection** dialog, enter the following connection info:

   * **Server**: ssl:p4-licensee.epicgames.com:1666

     The address above should automatically direct you to a regional proxy with the best latency based on your geographic location. If, for some reason, you need to connect to a specific regional proxy, you can connect to them using the addresses below:

     + **United States East (Virginia)**: ssl:p4-licensee-east.us.epicgames.com:1666
     + **United States West (Oregon)**: ssl:p4-licensee-west.us.epicgames.com:1666
     + **Asia Pacific Northeast (Tokyo)**: ssl:p4-licensee-northeast.ap.epicgames.com:1666
     + **Europe Central (Frankfurt)**: ssl:p4-licensee-central.eu.epicgames.com:1666
   * **User**: Perforce username provided by Epic Games.
   * **Password**: Set by your technical license administrator in Epic Games’ Okta.
3. Click **OK** to connect to the Perforce P4 Server.

   [![](https://dev.epicgames.com/community/api/documentation/image/bee56b72-197f-413f-a41d-2a3b991daab4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bee56b72-197f-413f-a41d-2a3b991daab4?resizing_type=fit)

   Click the image for full size.
4. When connecting to an endpoint for the first time, you must explicitly trust that endpoint.

   * The Epic Games SSL fingerprint is `B7:8D:23:34:71:4C:04:80:FD:D2:C0:A4:F5:7F:44:5E:D0:1C:D2:86`.
   * P4V will prompt you to trust the new endpoint.
   * Command line p4 uses the p4 trust command: `$ p4 trust -y`.
5. In P4V, choose **Connection > New Workspace** to create a new workspace for the engine. Enter the information below and click **OK** to create the workspace:

   * **Workspace name**: Give your new workspace a name.
   * **Stream**: Click **Browse** and select `//UE5/Release-Latest` from the list of available streams.

   [![Create a new workspace](https://dev.epicgames.com/community/api/documentation/image/765ded13-54ae-4692-a229-20c25c0c5e12?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/765ded13-54ae-4692-a229-20c25c0c5e12?resizing_type=fit)
6. In the **Depot** pane, expand the **Filter Depot** menu and select **Tree Restricted to Workspace View**.

   [![The Filter Depot menu](https://dev.epicgames.com/community/api/documentation/image/1fdf8fdf-6c8f-4679-bae9-26a8029ebf44?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1fdf8fdf-6c8f-4679-bae9-26a8029ebf44?resizing_type=fit)

### Connecting to your Local Perforce Depot

After your technical administrator has downloaded the Unreal Engine source code to a local P4 Perforce depot, the process for developers connecting to the local depot should be mostly the same as described above, except replace steps 2-4 with your local P4 Perforce depot connection and authentication information. Your technical administrator will have the required information for you to access your local depot.

### Download Unreal Engine

Epic Games uses stream names by convention. If you rename the streams for local use, please adjust the instructions below for your local users accordingly.

Epic Games distributes Unreal Engine to licensees using the `//UE5/Release-Latest` stream in the Perforce depot. This contains the entire engine along with several additional projects in the form of example games, samples, and demos. When setting up your local build, you have the option of downloading everything or picking and choosing only the parts you want or need.

To get set up as quickly as possible, we recommend you only download the bare minimum to start with and then download other parts on an as-needed basis. This can dramatically reduce idle time spent waiting for the download to finish. We also provide a `//UE5/Release-Latest-Minimal` stream to help with this.

Because there are a large number of files in the `//UE5/Release-Latest` stream and the total download size is many gigabytes, the download can take a long time when syncing the entire branch.

1. Right-click on the stream you want to download and choose **Get Latest Revision**.

   [![Perforce - Get Latest Revision](https://dev.epicgames.com/community/api/documentation/image/174a489e-104c-443e-b50e-7538c9c49582?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/174a489e-104c-443e-b50e-7538c9c49582?resizing_type=fit)
2. The latest version of all files will be downloaded.

### Migrating an Existing Workspace

To avoid having to force sync your entire workspace when creating a new one on the global replica, users can use `p4 flush` to populate the information based on the files in a local workspace. This procedure will be much faster than a force sync, and allow users to essentially pick up where they left off.

1. Create a new workspace on the global replica, copying the view and root settings from the original workspace.
2. Switch to the new workspace.
3. Issue `p4 flush` command 
   or `p4 sync -k` to populate information on the server.
4. Epic Games ages out old workspaces automatically if they are unused for six months.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Connecting to the Epic Games P4 Perforce Server](/documentation/en-us/unreal-engine/downloading-unreal-engine-with-perforce?application_version=5.7#connectingtotheepicgamesp4perforceserver)
* [Connecting to your Local Perforce Depot](/documentation/en-us/unreal-engine/downloading-unreal-engine-with-perforce?application_version=5.7#connectingtoyourlocalperforcedepot)
* [Download Unreal Engine](/documentation/en-us/unreal-engine/downloading-unreal-engine-with-perforce?application_version=5.7#downloadunrealengine)
* [Migrating an Existing Workspace](/documentation/en-us/unreal-engine/downloading-unreal-engine-with-perforce?application_version=5.7#migrating-an-existing-workspace)
