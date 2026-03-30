<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/activating-the-virtual-scouting-legacy-tools?application_version=5.7 -->

# Activating the Virtual Scouting Legacy Tools

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
5. [Building Virtual Worlds](/documentation/en-us/unreal-engine/building-virtual-worlds-in-unreal-engine "Building Virtual Worlds")
6. [Virtual Scouting](/documentation/en-us/unreal-engine/virtual-scouting-in-unreal-engine "Virtual Scouting")
7. [Virtual Scouting Legacy Tools](/documentation/en-us/unreal-engine/virtual-scouting-legacy-tools "Virtual Scouting Legacy Tools")
8. Activating the Virtual Scouting Legacy Tools

# Activating the Virtual Scouting Legacy Tools

Describes how to enable the Virtual Scouting Legacy tools.

![Activating the Virtual Scouting Legacy Tools](https://dev.epicgames.com/community/api/documentation/image/63e9b851-f2be-42d1-aec8-d20f578ffd14?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

The [Virtual Scouting Legacy tools](/documentation/en-us/unreal-engine/virtual-scouting-legacy-tools) described on this page will be sunset and deprecated in a future engine release. We encourage users to move to the [new Virtual Scouting tools](/documentation/en-us/unreal-engine/virtual-scouting-in-unreal-engine). Unused VREditor code and
modules will be fully deprecated in a future engine release.



Virtual Scouting is compatible with the HTC Vive, HTC Vive Pro, Oculus Rift, and Oculus Rift S VR HMDs. See [SteamVR Prerequisites](/documentation/en-us/unreal-engine/steamvr-prerequisites-in-unreal-engine) and [Oculus Prerequisites](/documentation/en-us/unreal-engine/oculus-prerequisites-in-unreal-engine) for connecting your headsets to Unreal Engine.

In this how-to guide, you will configure a project to enable access to the Virtual Scouting tools.

## Steps

1. With your project open, select **Edit** > **Plugins** from the main menu.
2. From the **Plugins** menu, under **Virtual Production**, enable the **Virtual Production Utilities** plugin.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b1bd106b-5128-4d83-a067-1f8a3569930a/virtualproductionutilities_enable.png)
3. Restart the **editor** when prompted.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2cb37754-4bb0-4e33-9caf-7d36ec73ce03/virtualproductionutilities_restart.png)
4. Select **Edit** > **Project Settings** from the main menu.
5. In **Project Settings** > **Plugins** > **Virtual Production Editor** > **Virtual Production**, set the **Virtual Scouting User Interface** to **Virtual Scouting Widget**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b137b7aa-ec9c-406a-8bf0-86db8d8a5b44/virtualscoutingwidget.png)


   If the **Virtual Production Utilities** plugin is enabled, but the **Virtual Scouting User Interface** is not set to **VirtualScoutingWidget**, it may affect **VR Editor** behavior. This will be resolved in a future release.
6. Select **Edit** > **Editor Preferences** from the main menu.
7. In **General** > **VR Mode** > **Motion Controllers**, set the **Interactor Class** to **VirtualScoutingInteractor**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1b8869e0-66e6-4bc9-9289-bccbfa5d09f1/vrmode_interactorclass.png)
8. Select **Edit** > **Editor Preferences** from the main menu.
9. In **Editor Preferences** > **General** > **VR Mode** > **Motion Controllers**, set the **Teleporter Class** to **VirtualScoutingTeleporter**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/460b0eb5-6513-4684-aa81-d5b89b2f776e/vrmode_teleporterclass.png)
10. Select **Edit** > **Editor Preferences** from the main menu.
11. In **Editor Preferences** > **General** > **VR Mode** > **World Movement**, uncheck **Show World Movement Grid** and **Show World Movement Post Process**.

    ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a7c138b3-dbf7-4648-8d02-4c45f61a2379/worldmovement_before.png "worldmovement_before.png")

    ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/05604868-34a1-48b7-9171-a67ec50f0fba/worldmovement_after.png "worldmovement_after.png")
12. Select **Edit** > **Editor Preferences** from the main menu.
13. In **Editor Preferences** > **Level Editor** > **Viewports** > **Grid Snapping**, uncheck **Enable Grid Snapping**, **Enable Rotation Snapping**, and **Enable Scale Snapping**.

    ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c139f3ca-0383-4db4-b042-20c673522ac8/gridsnapping_before.png "gridsnapping_before.png")

    ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cc061bcc-5a78-4f41-8e7f-827e639eb36a/gridsnapping_after.png "gridsnapping_after.png")
14. Enter **VR Mode**.

    ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d98ca68e-9dd0-4715-bf6f-e60026373052/vrmode.png)

## End Result

Once you are in **VR Mode**, pressing the Menu button on your VR controller will make the Virtual Scouting panel appear, giving you access to the various Virtual Scouting tools. For more information about the individual tools, see the [Virtual Scouting Overview](/documentation/en-us/unreal-engine/virtual-scouting-legacy-overview).

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b64a54cd-0d3f-470c-9a8d-4edae3e11823/menus.png)

* [beta](https://dev.epicgames.com/community/search?query=beta)
* [virtual scouting](https://dev.epicgames.com/community/search?query=virtual%20scouting)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/activating-the-virtual-scouting-legacy-tools?application_version=5.7#steps)
* [End Result](/documentation/en-us/unreal-engine/activating-the-virtual-scouting-legacy-tools?application_version=5.7#endresult)
