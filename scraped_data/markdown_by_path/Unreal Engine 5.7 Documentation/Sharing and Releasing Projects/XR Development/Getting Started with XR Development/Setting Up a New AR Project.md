<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-a-new-ar-project-in-unreal-engine?application_version=5.7 -->

# Setting Up a New AR Project

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
5. [Sharing and Releasing Projects](/documentation/en-us/unreal-engine/sharing-and-releasing-projects-for-unreal-engine "Sharing and Releasing Projects")
6. [XR Development](/documentation/en-us/unreal-engine/developing-for-xr-experiences-in-unreal-engine "XR Development")
7. [Getting Started with XR Development](/documentation/en-us/unreal-engine/getting-started-with-xr-development-in-unreal-engine "Getting Started with XR Development")
8. Setting Up a New AR Project

# Setting Up a New AR Project

Learn how to set up a new AR project from a blank template.

![Setting Up a New AR Project](https://dev.epicgames.com/community/api/documentation/image/b1bcaa70-d337-4d5f-b3ee-2a3953816680?resizing_type=fill&width=1920&height=335)

 On this page

This guide shows how to create a new empty project in Unreal Engine and add the necessary Blueprints and configurations to turn it into an AR experience.

If you want to start with an AR project that is set up already, see the following AR templates:

* [Handheld AR Template for iOS and Android](https://dev.epicgames.com/documentation/en-us/unreal-engine/handheld-ar-template-quickstart-in-unreal-engine)

Follow these steps to create a new Unreal Engine project and level with minimal rendering features enabled. Blank projects open with the default level, which includes a Sky Sphere and Atmosphere Fog objects. These objects will persistently overlay everything in AR, so it's useful to start with an empty level when creating an AR experience to control what will be displayed.

1. Launch **Unreal Engine** from the [Epic Games Launcher](https://www.epicgames.com/store/en-US/download).
2. In the **Unreal Project Browser** window, choose **Games**.

   [![Choose Games in the Unreal Project Browser](https://dev.epicgames.com/community/api/documentation/image/6d64fbe4-d2ce-4588-b19b-47841047f7dd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6d64fbe4-d2ce-4588-b19b-47841047f7dd?resizing_type=fit)

   Click image to expand.
3. Select the **Blank Template**.

   [![Select the Blank Template](https://dev.epicgames.com/community/api/documentation/image/842a7347-825c-4e96-83ad-219abf1da87f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/842a7347-825c-4e96-83ad-219abf1da87f?resizing_type=fit)

   Click image to expand.
4. For the **Project Defaults**, choose the following:

   * Blueprint
   * Scalable
   * Raytracing Disabled
   * Mobile
   * No Start Content

     [![Choose Project Defaults](https://dev.epicgames.com/community/api/documentation/image/9a3a19a3-9de4-4ed2-b0a6-e663b75f307b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9a3a19a3-9de4-4ed2-b0a6-e663b75f307b?resizing_type=fit)

     Click image to expand.
5. In the main menu, select **Edit > Plugins**, and in the **Plugins** windows, search for and enable the **AR Utilities** plugin. Click **Restart Now**, and wait for Unreal Engine to restart.

   [![Enable the AR Utilities plugin](https://dev.epicgames.com/community/api/documentation/image/bf7b3b85-3a9a-45ec-b3f8-2db433c83bde?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bf7b3b85-3a9a-45ec-b3f8-2db433c83bde?resizing_type=fit)
6. From the Editor, choose **File > New Level…** and choose **Empty Level**. Make sure to name and save your level. In this example, the level is named **Main**.

   [![Select Empty Level](https://dev.epicgames.com/community/api/documentation/image/b1ce08b4-1931-48a5-8f82-393d3512a432?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b1ce08b4-1931-48a5-8f82-393d3512a432?resizing_type=fit)
7. In the main navigation, choose **Edit > Project Settings.**
8. In the Project Settings window, select **Maps & Modes** under the **Project** section. Set the **Editor Startup Map** and the **Game Default Map** to the new level **Main.**

   [![Project Settings Maps & Modes](https://dev.epicgames.com/community/api/documentation/image/dadf4eef-c917-4cb6-83e0-703a3db36cff?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dadf4eef-c917-4cb6-83e0-703a3db36cff?resizing_type=fit)

   Click image to expand.

## Adding a Pawn and Game Mode

In Unreal Engine, a [pawn](https://dev.epicgames.com/documentation/en-us/unreal-engine/pawn-in-unreal-engine) is the physical representation of the user and defines how the user interacts with the world. The [Game Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/game-mode-and-game-state-in-unreal-engine)
object defines the rules of the experience, such as which pawn object
to use. In order to build a new AR project, you need to set up the pawn
so you can interact with the environment when you run your app.

Follow the steps below to create a Pawn and Game Mode for your AR project.

1. Right-click in the **Content Drawer** and choose **Blueprint Class** from the list. In the **Pick Parent Class** window, select **Pawn**. Name the asset **ARPawn**.

   [![Select Blueprint Class](https://dev.epicgames.com/community/api/documentation/image/72eb0e8b-6752-4f21-95f9-f0ceabef2193?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/72eb0e8b-6752-4f21-95f9-f0ceabef2193?resizing_type=fit)

   [![Pick Actor as parent class](https://dev.epicgames.com/community/api/documentation/image/aa6a120c-33c1-4ea9-9510-4b24f7948660?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/aa6a120c-33c1-4ea9-9510-4b24f7948660?resizing_type=fit)
2. Double-click the **ARPawn** object in the **Content Drawer** to open it in the **Blueprint Editor**. In the Blueprint Editor, choose **Add Component** and search for **Camera**.

   [![Add a Camera component](https://dev.epicgames.com/community/api/documentation/image/1066dc85-5cc2-421d-84b7-71e35b131d73?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1066dc85-5cc2-421d-84b7-71e35b131d73?resizing_type=fit)
3. Make sure the **Camera** component's parent is **DefaultSceneRoot**.

   [![Make sure DefaultSceneRoot is the Camera component's parent](https://dev.epicgames.com/community/api/documentation/image/7bceb098-d307-497e-95f5-f1a47b36458f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7bceb098-d307-497e-95f5-f1a47b36458f?resizing_type=fit)
4. Right-click in the **Content Drawer** and choose **Blueprint Class** from the list. In the **Pick Parent Class** window, select **Game Mode Base**. Name the asset **ARGameMode**.

   [![Select Game Mode Base as the parent class](https://dev.epicgames.com/community/api/documentation/image/0eb67d97-fa6f-4ad7-958c-7290bb4d2a09?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0eb67d97-fa6f-4ad7-958c-7290bb4d2a09?resizing_type=fit)
5. Double-click **ARGameMode** to edit the settings. Set **Default Pawn Class** to **ARPawn**.

   [![Set Default Pawn Class to ARPawn](https://dev.epicgames.com/community/api/documentation/image/30f81e2a-f2f4-4c77-a457-eb9645992113?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/30f81e2a-f2f4-4c77-a457-eb9645992113?resizing_type=fit)

   Click image to expand.
6. In the main navigation, choose **Edit > Project Settings** to open the **Project Settings** window.
7. In the **Project Settings** window under the **Project** section on the left, select **Maps & Modes**.

   1. Set **Default GameMode** to **ARGameMode.**
   2. Set **Default Pawn Class** to **ARPawn**.

   [![Set the Default Game Mode and the Default Pawn Class](https://dev.epicgames.com/community/api/documentation/image/6c612806-8dff-4619-ae58-791c1b2a8427?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6c612806-8dff-4619-ae58-791c1b2a8427?resizing_type=fit)

   Click image to expand.

## Creating an AR Session

The function **Start AR Session** requires an ARSessionConfig object, which defines all the AR-specific capabilities for the project. See [UARSessionConfig](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/AugmentedReality/UARSessionConfig?application_version=5.6) for more information on what each setting is.

Follow the steps below to add the AR session logic to your project.

1. Right-click in the **Content Drawer**. Choose **Miscellaneous > Data Asset** to open the **Pick Data Asset Class** window.

   [![Select Data Asset](https://dev.epicgames.com/community/api/documentation/image/47306ce0-0180-4ee9-a434-aecc133f827e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/47306ce0-0180-4ee9-a434-aecc133f827e?resizing_type=fit)
2. In the **Pick Data Asset Class** window, choose **ARSessionConfig**. Name the data asset **ARSessionConfig**. Open the asset and select **Save** to confirm the default AR options.

   [![Pick ARSessionConfig as the data asset instance](https://dev.epicgames.com/community/api/documentation/image/83b0121d-ee47-4ae7-b71c-190aef74d4a7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/83b0121d-ee47-4ae7-b71c-190aef74d4a7?resizing_type=fit)
3. Double-click the **ARPawn** asset to open it in the **Blueprint Editor**. Add the function **Set Tracking Origin**. Set the **Origin** value to **Floor Level**.

   [![Set Tracking Origin node value set to Floor Level](https://dev.epicgames.com/community/api/documentation/image/973016e3-f034-4025-af51-558c071472c6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/973016e3-f034-4025-af51-558c071472c6?resizing_type=fit)
4. Add the function **Start AR Session**. Set **Session Config** asset to **ARSessionConfig**.

   [![Start AR Session node value set to ARSessionConfig](https://dev.epicgames.com/community/api/documentation/image/005bab3e-810c-4d67-924f-c309c41a97b6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/005bab3e-810c-4d67-924f-c309c41a97b6?resizing_type=fit)
5. Add the function **Stop AR Session**.

   [![Add Stop AR Session node](https://dev.epicgames.com/community/api/documentation/image/34694341-9c57-44f9-b3fd-e94c4359c4d3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/34694341-9c57-44f9-b3fd-e94c4359c4d3?resizing_type=fit)

When you launch your project on your device, you will now be able to
navigate your AR environment. See the documentation for your AR platform
for detailed steps on how to launch your Unreal project on your device.

## On Your Own

In this guide, you learned how to create a new AR project, and add the necessary Blueprints to get started building an AR app.

* [template](https://dev.epicgames.com/community/search?query=template)
* [xr](https://dev.epicgames.com/community/search?query=xr)
* [vr](https://dev.epicgames.com/community/search?query=vr)
* [ar](https://dev.epicgames.com/community/search?query=ar)
* [ar/vr/xr](https://dev.epicgames.com/community/search?query=ar%2Fvr%2Fxr)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Adding a Pawn and Game Mode](/documentation/en-us/unreal-engine/setting-up-a-new-ar-project-in-unreal-engine?application_version=5.7#addingapawnandgamemode)
* [Creating an AR Session](/documentation/en-us/unreal-engine/setting-up-a-new-ar-project-in-unreal-engine?application_version=5.7#creatinganarsession)
* [On Your Own](/documentation/en-us/unreal-engine/setting-up-a-new-ar-project-in-unreal-engine?application_version=5.7#onyourown)
