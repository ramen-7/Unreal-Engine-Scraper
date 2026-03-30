<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/switchboard-quick-start-for-unreal-engine?application_version=5.7 -->

# Switchboard Quick Start

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
5. [Working with Media](/documentation/en-us/unreal-engine/working-with-media-in-unreal-engine "Working with Media")
6. [Communicating with Media Components](/documentation/en-us/unreal-engine/communicating-with-media-components-from-unreal-engine "Communicating with Media Components")
7. [Switchboard](/documentation/en-us/unreal-engine/switchboard-in-unreal-engine "Switchboard")
8. Switchboard Quick Start

# Switchboard Quick Start

Learn how to add Switchboard to your project and connect to multiple devices remotely.

![Switchboard Quick Start](https://dev.epicgames.com/community/api/documentation/image/95b096d0-1de4-4737-bd23-ee17209be28a?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

The instructions on this page provide a step-by-step guide to getting started with Switchboard. By the end of this tutorial, you'll know how to set up Switchboard to connect to multiple devices.

## Prerequisites

You must have the following set up before completing the next steps:

* The **Switchboard** plugin enabled. After you've added the plugin and restarted the engine, Switchboard and SwitchboardListener options appear in the Toolbar.

  [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/37dd45df-4eba-4f4e-9e63-cdc268b62ac8/00-enable-plugin_ue5.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/37dd45df-4eba-4f4e-9e63-cdc268b62ac8/00-enable-plugin_ue5.png)

  Click image to expand
* Dependencies installed. In the main menu, choose **Edit > Editor Preferences > Plugins > Switchboard** and click **Install Dependencies**.

  [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/30d45d85-6983-4d8a-9551-fa05456fc29d/01-switchboard-dependencies_ue5.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/30d45d85-6983-4d8a-9551-fa05456fc29d/01-switchboard-dependencies_ue5.png)

  Click image to expand
* (Optional) If you're using Windows as your OS, you can choose to install a desktop shortcut for Switchboard. In the main menu, choose **Edit > Project Settings > Plugins > Switchboard** and click **Add Shortcut**.

  [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d84524cb-fc4b-4873-8910-0bf6e10e3055/02-add-shortcuts_ue5.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d84524cb-fc4b-4873-8910-0bf6e10e3055/02-add-shortcuts_ue5.png)

  Click image to expand
* If you built the engine from source, you will need to build **SwitchboardListener** separately. You can either build the project in Visual Studio or run the following command in the root directory of the engine source code: `Engine\Binaries\DotNET\UnrealBuildTool.exe Win64 Development SwitchboardListener`.

## Step 1 - Launching Switchboard Listener

On each device you want to connect to Switchboard, you will need to launch SwitchboardListener. In the Toolbar, select **Switchboard Options > Launch Switchboard Listener**, which launches the listener on the local machine with the default address 0.0.0.0:2980, or the address you specified for **Listener Commandline Arguments** in **Editor Preferences**.

![Launch Switchboard Listener](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bfb582eb-92fe-48e1-b050-016a8e6b17ae/launch-switchboard-listener.png)

The listener minimizes its window automatically on start to avoid issues with nDisplay devices. You can find the application in your OS's taskbar.

![Switchboard Listener application](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/63f2bb27-773b-49ce-b1ba-63ba665179ef/04-switchboard-listener_ue5.png)

You can also select **Launch Switchboard Listener on Login** which launches the listener on the local machine every time you log into the computer.

## Step 2 - Launching Switchboard

There are multiple ways to launch Switchboard:

1. Opening a project in Unreal Editor, and selecting **Launch Switchboard** from the Toolbar.

   ![Launch Switchboard from Unreal Editor Toolbar](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f4ae83ff-a202-4a31-9839-c488a293a3bb/05-swithchboard-icon_ue5.png)
2. Using the desktop shortcut, if you installed it on your computer. Refer to Switchboard Prerequisites for steps on installing this shortcut.
3. Running **Engine\Plugins\VirtualProduction\Switchboard\Source\Switchboard\Switchboard.bat**.

The **Add New Switchboard Configuration** window appears when Switchboard is launched for the first time. You can either fill out the fields and select **OK**, or select **Cancel** and update them later in the Switchboard Settings. Both options open Switchboard in a window.

![Add new Switchboard Configuration](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/68aeb580-5fea-4fb1-ae37-1a8335f47bf0/add-new-switchboard-configuration.png)

Switchboard Configuration Parameters:

| Parameter | Description |
| --- | --- |
| Name | The name you want to use to identify your Switchboard project. |
| uProject | The local path to the uProject you want to control via Switchboard. |
| Engine Dir | The local path to the engine directory of the engine you want to use. It is possible to either specify a path to an engine you have built from source or an installed engine release. Example: "C:\Program Files\Epic Games\UE\_5.00\Engine" |
| Perforce | Enable this checkbox to use Perforce as your source repository. |
| P4 Project Path | The depot path to the directory containing the uproject file specified above. |
| P4 Engine Path | The depot path to the engine directory specified above. May be omitted if you don't plan on building the engine from source. |
| Workspace Name | The name of the locally available perforce workspace that has the uproject directory mapped. |

## Step 3 - Adding a Device in Switchboard

Switchboard supports several types of devices. These devices are implemented as plugins for Switchboard. Refer to [Switchboard Settings](/documentation/en-us/unreal-engine/switchboard-settings-reference-for-unreal-engine) for the list of device plugins available by default, and steps on how to create your own device plugin.

The following example shows how to add an Unreal Device in

1. In Switchboard, select **Add Device > Unreal** to open the **Add Unreal Device** window.

   ![Add Unreal Device in Switchboard](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0e03b9cb-7b4e-4100-a6ff-6aff0b87d048/add-unreal-device-switchboard.png)
2. In the Add Unreal Device window, assign a Name to the machine running Unreal Engine and the IP Address of the computer. Select **OK**. The device is added to the list of Unreal Devices in Switchboard.

   ![Add Unreal Device window](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ffaf355e-b1c7-41f7-b44f-c6bacc1bc0cd/add-unreal-device-window.jpg)

You can also change the IP address and name of the device after it has been added.

1. Click **Connect to listener** to connect to the SwitchboardListener application running on the remote machine. The status icon turns blue when the device is connected.

   ![Connect to Switchboard Listener](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/06856361-4655-48a4-b962-96d2486c62f5/connect-to-switchboard-listener.png)
2. Click **Start Unreal** to launch an instance of the Unreal Editor on the remote machine.

   ![Start Unreal instance remotely](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/04503b07-5e3c-4d48-a223-73dd637341ba/start-unreal.png)
3. The status icon on the left turns either orange or green when the Unreal instance launches.

   * The green status indicates that the Unreal instance is connected through OSC so you can use Take Recorder from Switchboard.
   * The orange status indicates that it is not connected through OSC.![Example of orange status](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cb2d036d-c0d2-43e6-ab2c-bb98e2f9f139/orange-status-example.png)
4. Click **Stop Unreal** to close the Unreal Editor on the remote machine.

   ![Stop Unreal instance remotely](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/31f9b204-7f35-4552-b917-96dfbcff2578/stop-unreal.png)

## Step 4 - On Your Own

This quick start showed you how to start Switchboard and SwitchboardListener, connect to remote devices, and control them from Switchboard. Refer to [Switchboard Settings Reference](/documentation/en-us/unreal-engine/switchboard-settings-reference-for-unreal-engine) for a complete list of options you can modify in Switchboard. Learn more about the following features to use in your project:

* Sync and build your project and engine remotely.
* Record a take remotely from Switchboard.
* Launch and monitor your nDisplay cluster.

* [beta](https://dev.epicgames.com/community/search?query=beta)
* [vfx](https://dev.epicgames.com/community/search?query=vfx)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisites](/documentation/en-us/unreal-engine/switchboard-quick-start-for-unreal-engine?application_version=5.7#prerequisites)
* [Step 1 - Launching Switchboard Listener](/documentation/en-us/unreal-engine/switchboard-quick-start-for-unreal-engine?application_version=5.7#step1-launchingswitchboardlistener)
* [Step 2 - Launching Switchboard](/documentation/en-us/unreal-engine/switchboard-quick-start-for-unreal-engine?application_version=5.7#step2-launchingswitchboard)
* [Step 3 - Adding a Device in Switchboard](/documentation/en-us/unreal-engine/switchboard-quick-start-for-unreal-engine?application_version=5.7#step3-addingadeviceinswitchboard)
* [Step 4 - On Your Own](/documentation/en-us/unreal-engine/switchboard-quick-start-for-unreal-engine?application_version=5.7#step4-onyourown)
