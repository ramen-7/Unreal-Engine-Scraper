<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/launching-unreal-engine-projects-on-devices?application_version=5.7 -->

# Launching to Devices

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
6. [Packaging and Cooking Games](/documentation/en-us/unreal-engine/packaging-and-cooking-games-in-unreal-engine "Packaging and Cooking Games")
7. Launching to Devices

# Launching to Devices

One-click deploying your project to devices like iOS and Android for testing

![Launching to Devices](https://dev.epicgames.com/community/api/documentation/image/39b5de85-6e7b-4dac-aeb4-ca0d9cc4d7a9?resizing_type=fill&width=1920&height=335)

 On this page

In the Main toolbar of the Unreal Editor, there is a button labeled **Platforms**, with a drop-down menu.

![Platforms drop-dawn menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/13d1d969-44bc-4274-ab77-2a2ab6f39d90/launching-platforms-drop-down.png "Platforms drop-dawn menu")

In the drop-down menu, you will see a list of possible platforms you can launch the current Level on.
Generally, you would not need Windows or Mac, as you can use the **Play** button for that without needing to cook your data.
This page will primarily cover the information you need for launching on mobile platforms.

For Android, there will be multiple selections. See the [**Android Texture Formats**](/documentation/en-us/unreal-engine/android-development-basics-for-unreal-engine#androidtextureformats) page for more information.

If you have multiple devices for a particular platform, you can choose between them here. Clicking on the platform (and device), the Editor will start to cook the Level, install the data on the device, and run the Level on the device.

This method will only install the current Level on the device for fast iteration, and switching between Levels is unsupported with this method. If you want to have all of your Levels installed to the device at once, see the  documentation.

### Generic UnrealGame App

If you are making a content-only project, the executable that runs for One-Click Deploy is actually the generic "UnrealGame" game (since it can be used with any content-only project).
When it runs on a device, the icon that gets installed is just labeled as UnrealGame. However, when you package a game, the name of your project is used in the final packaged build.
When you install the packaged build, the icon will have your name (as well as your icons if you updated the default icons).

## Advanced Mode (UnrealFrontend)

There is an additional tool for performing advanced building, cooking, deploying, packaging, and launching options. It is called **Unreal Frontend** and is located in the following locations depending on your platform:

| Platform | Location |
| --- | --- |
| PC | [ENGINE INSTALL LOCATION]\Engine\Binaries\Win64\UnrealFrontend.exe |
| Mac | [ENGINE INSTALL LOCATION]\Engine\Binaries\Mac\UnrealFrontend.app |

This tool will let you only cook certain maps, change the commandline, or even run your game without precooking all the data (called "Cook on the Fly" mode).
These are advanced tools - for more information, see **[Unreal Frontend](/documentation/en-us/unreal-engine/using-the-unreal-frontend-tool)**.

* [packaging](https://dev.epicgames.com/community/search?query=packaging)
* [launching](https://dev.epicgames.com/community/search?query=launching)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Generic UnrealGame App](/documentation/en-us/unreal-engine/launching-unreal-engine-projects-on-devices?application_version=5.7#genericunrealgameapp)
* [Advanced Mode (UnrealFrontend)](/documentation/en-us/unreal-engine/launching-unreal-engine-projects-on-devices?application_version=5.7#advancedmode(unrealfrontend))
