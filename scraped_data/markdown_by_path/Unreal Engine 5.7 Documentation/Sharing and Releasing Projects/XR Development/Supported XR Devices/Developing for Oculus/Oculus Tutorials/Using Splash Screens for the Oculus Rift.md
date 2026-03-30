<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-splash-screens-for-the-oculus-rift-in-unreal-engine?application_version=5.7 -->

# Using Splash Screens for the Oculus Rift

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
7. [Supported XR Devices](/documentation/en-us/unreal-engine/supported-xr-devices-in-unreal-engine "Supported XR Devices")
8. [Developing for Oculus](/documentation/en-us/unreal-engine/developing-for-oculus-in-unreal-engine "Developing for Oculus")
9. [Oculus Tutorials](/documentation/en-us/unreal-engine/oculus-how-to-in-unreal-engine "Oculus Tutorials")
10. Using Splash Screens for the Oculus Rift

# Using Splash Screens for the Oculus Rift

Setting up splash screens when loading levels on VR

![Using Splash Screens for the Oculus Rift](https://dev.epicgames.com/community/api/documentation/image/2f795372-19cc-4860-b7d9-598dce18122c?resizing_type=fill&width=1920&height=335)

###### Prerequisite topics

In order to understand and use the content on this page, make sure you are familiar with the following topics:

* [Using Motion Controllers](/documentation/en-us/unreal-engine/using-motion-controllers-in-unreal-engine)

 On this page

Skill\_family: Tutorial Level 1
Version: 5.0
Parent: sharing-and-releasing-projects/xr-development/supported-xr-platforms/developing-for-oculus/OculusHowTo
Order: 2
tags: Oculus
prereq: sharing-and-releasing-projects/xr-development/supported-xr-platforms/developing-for-steamvr/HowTo/StandingCamera
prereq: sharing-and-releasing-projects/xr-development/making-interactive-xr-experiences/using-motion-controllers
prereq: sharing-and-releasing-projects/xr-development/supported-xr-platforms/developing-for-oculus/OculusHowTo/GuardianSystem

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/52051557-4708-4639-8bd4-0da5a93ab8e9/htsplashscreen_hero_image.png)

Whenever you are changing levels in your UE VR project, the user could experience some framerate issues due to the massive amount of data that is being unloaded and loaded. To help avoid this issue and mask any frame rate issues that might arise when loading a new level you can display a Splash screen or movie to the user. In the following tutorial we will go over how to setup and call a splash screen in your UE projects.

## Steps

\* For this How - To you will need to download, unzip and import the two files contained in the following zip file, **[Oculus Splash Screen Source Files](https://d1iv7db44yhgxn.cloudfront.net/documentation/attachments/9d51a798-a51d-4935-b567-ed49a72cdb1f/oclussplashscreensourcecontent.zip)**

1. Open up your VRPawn and go to the **Event Graph**. Right-click inside the Event Graph and search for and add the following Blueprint nodes:

   * Event Begin Play
   * Set Tracking Origin
   * Enable Auto Loading Splash Screen
   * Add Loading Splash Screen
   * Hide Splash Screen

     [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e6d26719-f7e5-4a53-8fb8-314b50d14b5c/htsplashscreen_00.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e6d26719-f7e5-4a53-8fb8-314b50d14b5c/htsplashscreen_00.png)

     Click for full image.
2. Since we want the Splash screen to be called each time a level is loaded, we will want first to make sure that we enable the autoloading of Splash screen and then set what we want to use as the Splash screen. Finally, we will want to hide the Splash Screen so that we can call it when we need it later. Now set up the nodes in your VRPawn Event Graph to match the following image:

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/03df692d-fd73-4b5b-af5d-8c608d257b72/htsplashscreen_01.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/03df692d-fd73-4b5b-af5d-8c608d257b72/htsplashscreen_01.png)

   Click for full image.

   Make sure that you check the **Auto Show Enabled** property on the **Enable Auto Loading Splash Screen** so that the Splash screen will be automatically called each time a level is loaded.
3. In the **Add Loading Splash Screen** node, there is a **Texture** input which controls what Texture or Movie will be displayed when this is node is called. Set the Texture used to be the **T\_UE4\_Logo\_00** or any other Texture of your choosing.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/911d7af7-5a01-4215-82d6-e9b0ed389483/htsplashscreen_02.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/911d7af7-5a01-4215-82d6-e9b0ed389483/htsplashscreen_02.png)

   Click for full image.

   When selecting a Texture to be used as a Splash image, it is best to set the Texture compression setting to **UserInterface2D** and also to enable the **Never Stream** option to make sure you will see the highest quality version of your Splash screen.
4. Now connect the following three nodes to the VRPawn Event graph so that we can show and hide the Splash screen. When completed your setup should match the following image:

   * Motion Controller (L)Trigger
   * Show Loading Splash Screen
   * Hide Loading Splash Screen

     [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3693cc7a-4789-4597-a6c2-55cfd00b7014/htsplashscreen_03.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3693cc7a-4789-4597-a6c2-55cfd00b7014/htsplashscreen_03.png)

     Click for full image.

     While you can display Splash screen in this manner, you will want to add this functionality a level Blueprint so that when the level is loaded, the Splash screen will be displayed until the level is done with loading.
5. After that has been completed and you VRPawn Blueprint looks like the following image, put on your HMD grab your Touch controllers and stand in the middle of your VR interaction area.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7b09833f-c916-453d-b5de-bcc3ae3363cf/htsplashscreen_04.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7b09833f-c916-453d-b5de-bcc3ae3363cf/htsplashscreen_04.png)

   Click for full image.

## End Result

Now when you squeeze the left trigger on the Touch, your scene should go black, and the Texture of the UE logo or the image you selected will be displayed. Releasing the left trigger on the Touch will bring you back the level back into view like in the following video.

## UE Project Downloads

Below you will find a link to where you can download the UE project that was used to create this example.

* [**Oculus Rift Splash Screens Example Project**](https://epicgames.box.com/s/1rirqbohl7inchgnssznuam7ylalrzk4)

* [oculus](https://dev.epicgames.com/community/search?query=oculus)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/using-splash-screens-for-the-oculus-rift-in-unreal-engine?application_version=5.7#steps)
* [End Result](/documentation/en-us/unreal-engine/using-splash-screens-for-the-oculus-rift-in-unreal-engine?application_version=5.7#endresult)
* [UE Project Downloads](/documentation/en-us/unreal-engine/using-splash-screens-for-the-oculus-rift-in-unreal-engine?application_version=5.7#ueprojectdownloads)
