<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-unreal-stage-in-unreal-engine?application_version=5.7 -->

# Getting Started with Unreal Stage

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
6. [Integrating Media](/documentation/en-us/unreal-engine/integrating-media-in-unreal-engine "Integrating Media")
7. [Rendering to Multiple Displays with nDisplay](/documentation/en-us/unreal-engine/rendering-to-multiple-displays-with-ndisplay-in-unreal-engine "Rendering to Multiple Displays with nDisplay")
8. [Unreal Stage App](/documentation/en-us/unreal-engine/unreal-stage-app-for-unreal-engine "Unreal Stage App")
9. Getting Started with Unreal Stage

# Getting Started with Unreal Stage

In this tutorial you will discover the new Unreal Stage app, install it on your device, and connect it to your Unreal Engine project.

![Getting Started with Unreal Stage](https://dev.epicgames.com/community/api/documentation/image/20cf8439-73df-43be-9051-ebc0c1cf74a8?resizing_type=fill&width=1920&height=335)

Learn to use this **Experimental** feature, but use caution when shipping with it.

 On this page

## What is Unreal Stage?

Unreal Stage is an Epic-created app that allows users to utilize a tablet as a wireless control panel for certain features in a physical space. This is particularly useful when these features need to be viewed while adjustments are being made, such as lighting on a film set, but computers are kept away from the stage to make room for physical equipment and set pieces.

Once set up, the simplified interface of Unreal Stage allows anyone to manage these variables autonomously and efficiently, even if they are unfamiliar with Unreal Engine.

This tutorial is most effective if you have experience with nDisplay and some knowledge of Unreal Engine's remote control features. Unreal Stage can be used as the mobile version of the In-Camera VFX feature, which provides an in-Engine desktop version of these controls. A tablet is required for Unreal Stage.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2e3a4e9c-1549-4c9b-8f9b-877ee5167518/stage-1.png)

## Install Unreal Stage

Unreal Stage has been specifically designed for use on tablets. It is not intended for other mobile devices, like cell phones. The app is available to download directly through the Apple App Store and an iPad is recommended, though an Android version is available through GitHub.

### iOS App

Install the Unreal Stage App from the Apple App Store for your iPad:

* [Unreal Stage iOS App](https://apps.apple.com/us/app/unreal-stage/id1611811922)

### Android Support

Unreal Stage is a Flutter-based app that can be deployed and run on Android devices if desired. The source code for the app is available on Github:

* [Unreal Stage Source Code on UE5/Main](https://github.com/EpicGames/UnrealEngine/tree/ue5-main/Engine/Extras/VirtualProduction/EpicStageApp)

Users must be logged in and have their Github account linked to an Epic Games account to access Unreal Engine source code on GitHub. [Click here for instructions on linking your accounts.](https://www.unrealengine.com/ue-on-github)

## Unreal Project Setup

In your Unreal project, ensure the following plugins (File > Plugins) are enabled:

* Epic Stage App
* nDisplay
* Remote Control API
* Remote Control Web Interface

Alternatively, enabling the ICVFX Plugin will also ensure all necessary plugins are enabled. Restart Unreal Engine once all plugins have been enabled.

After your Unreal level has reopened, ensure there is a nDisplay Root Actor in the scene. This is what the app will connect with and control.

* [getting started](https://dev.epicgames.com/community/search?query=getting%20started)
* [experimental](https://dev.epicgames.com/community/search?query=experimental)
* [virtual production](https://dev.epicgames.com/community/search?query=virtual%20production)
* [ndisplay](https://dev.epicgames.com/community/search?query=ndisplay)
* [icvfx](https://dev.epicgames.com/community/search?query=icvfx)
* [virtual sets](https://dev.epicgames.com/community/search?query=virtual%20sets)
* [bronze](https://dev.epicgames.com/community/search?query=bronze)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [What is Unreal Stage?](/documentation/en-us/unreal-engine/getting-started-with-unreal-stage-in-unreal-engine?application_version=5.7#whatisunrealstage?)
* [Install Unreal Stage](/documentation/en-us/unreal-engine/getting-started-with-unreal-stage-in-unreal-engine?application_version=5.7#installunrealstage)
* [iOS App](/documentation/en-us/unreal-engine/getting-started-with-unreal-stage-in-unreal-engine?application_version=5.7#iosapp)
* [Android Support](/documentation/en-us/unreal-engine/getting-started-with-unreal-stage-in-unreal-engine?application_version=5.7#androidsupport)
* [Unreal Project Setup](/documentation/en-us/unreal-engine/getting-started-with-unreal-stage-in-unreal-engine?application_version=5.7#unrealprojectsetup)
