<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-xcode-ios-simulator-with-unreal-engine-projects?application_version=5.7 -->

# Using the Xcode iOS Simulator

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
5. [Mobile Development](/documentation/en-us/unreal-engine/getting-started-with-mobile-development-in-unreal-engine "Mobile Development")
6. [Debugging and Optimization for Mobile](/documentation/en-us/unreal-engine/debugging-and-optimization-for-mobile-in-unreal-engine "Debugging and Optimization for Mobile")
7. [iOS and tvOS Debugging and Optimization](/documentation/en-us/unreal-engine/ios-and-tvos-debugging-and-optimization-in-unreal-engine "iOS and tvOS Debugging and Optimization")
8. Using the Xcode iOS Simulator

# Using the Xcode iOS Simulator

Use Xcode's iOS Simulator to test your project on various iOS devices without using a physical device.

![Using the Xcode iOS Simulator](https://dev.epicgames.com/community/api/documentation/image/95c85534-17ee-4010-8469-c955f2373b59?resizing_type=fill&width=1920&height=335)

Learn to use this **Experimental** feature, but use caution when shipping with it.

 On this page

Xcode’s **iOS Simulator** launches a virtual iPhone or iPad device on your Mac’s desktop so you can test apps in a wide variety of environments without needing a large number of physical test devices. This page explains how to launch **Unreal Engine (UE)** projects using the iOS Simulator, either from Xcode or directly from Unreal Editor.

## Prerequisites

To follow this guide, make sure you have the following:

* An Apple Silicon Mac (M1/M2/M3) with Unreal Engine and the required version of Xcode installed. See the [iOS Development Requirements](/documentation/404) page for more information.
  + Xcode must be signed in to your Apple Developer account.
  + Xcode simulators preinstalled. See the [Apple Developer Docs](https://developer.apple.com/documentation/xcode/installing-additional-simulator-runtimes) for more information.
  + Automatic code signing is recommended.
* A UE project set up for Mobile. You can use either the third-person or first-person templates to quickly create a new project to test on.
* An iOS or iPadOS device for initial setup.

See [Debugging in Xcode](/documentation/en-us/unreal-engine/debugging-ios-projects-with-xcode-in-unreal-engine) for more information on setting up these prerequisites.

## Initial Setup in Unreal Editor

Before you can use iOS Simulators, follow these steps to enable the required settings and prepare your project's content:

1. Open Project Settings > Platforms > iOS Settings. Enable the following settings:

   * **Build** > **Enable iOS Simulator Support**
   * **Build** > **Support Apple A8**
2. Restart Unreal Editor to make your changes take effect.

## Use an iOS Simulator in Xcode

To launch your game onto an iOS or iPadOS simulator from Xcode, follow these steps:

1. Xcode can't cook content itself, so you need to use Unreal Editor to run a cook operation before you can launch your app out of Xcode. In Unreal Editor, click **Platforms** > **iOS** > **Cook Content** to cook your project's content for iOS and iPadOS. Alternatively, you can quickly launch onto a physical iOS or iPadOS device.
2. Start **Xcode** and load the project `UE5 (IOS).workspace`.
3. Select the desired **Target** (the name of the project) in the **Xcode scheme** dropdown.

   * For example, **TP\_FirstPerson.**
4. Click **Edit Scheme,** select **Diagnostics** > **Run**, and disable **Metal API Validation**.
5. Click the **launch destinations** dropdown and select a simulator to launch. This is the same dropdown as where you choose an iPhone or a tablet to run on.
6. Press the **Run** button to build your project and launch it on the selected simulator.

## Launch on an iOS Simulator from Unreal Editor (Experimental)

Because support for launching iOS Simulators from the editor is experimental, not all of UE's static libraries have been updated with a iOS Simulator slice.

To launch your game onto an iOS or iPadOS Simulator directly from Unreal Editor, follow these steps:

1. Start up an iOS/iPadOS Simulator from Xcode. Unreal Editor detects the simulator while it's running and adds it as a target device you can launch on in the next step.
2. Click the **Platforms** dropdown, then locate the new **Simulators** section underneath the **Quick Launch** section. Any simulators you are running appear here.

   ![An iPad Mini displayed in the Launch dropdown in Unreal Editor.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3e78e768-e044-4333-b5bd-91bf37158891/launch_editor.png)
3. Once selected, UE creates a simulator-specific build of the app and installs it onto the open simulator.

   ![An iOS simulator displayed on the desktop.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b3cbffe4-4ea9-4994-8655-64ca4d58cf12/simulator_screenshot.png)
4. Select the app in the simulator and it will launch and run.

   ![A user opens their UE app in the iOS simulator.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2de6512f-a063-4cba-9396-3585b595db3d/simulator_working.gif)

## Upgrade Existing Projects to use the iOS Simulator

If you are adding iOS Simulator support to a project that is already compiled and cooked, you may have errors when attempting to compile with iOS Simulator Support enabled due to issues with your shader libraries. To remedy these errors, delete all cooked content for your project after you enable the Enable iOS Simulator Support setting, then launch your project to your iOS device again.

The iOS Simulator needs a different shader library compared to physical devices, so UE projects create two Metal libraries: one standard, and one called Metal-Sim for the Simulator.

## Running Multiple Instances

You can run up to six iOS simulators for your application simultaneously. Running multiple simulators is useful for comparing rendering issues between different versions of iOS. To see which simulators you are currently using, click the **Window** button in the toolbar.

Expect your system to slow down dramatically when running three or more instances of the iOS simulator simultaneously.

* [testing](https://dev.epicgames.com/community/search?query=testing)
* [experimental](https://dev.epicgames.com/community/search?query=experimental)
* [debugging](https://dev.epicgames.com/community/search?query=debugging)
* [ios](https://dev.epicgames.com/community/search?query=ios)
* [ipados](https://dev.epicgames.com/community/search?query=ipados)
* [xcode](https://dev.epicgames.com/community/search?query=xcode)
* [iphone](https://dev.epicgames.com/community/search?query=iphone)
* [ipad](https://dev.epicgames.com/community/search?query=ipad)
* [ios simulator](https://dev.epicgames.com/community/search?query=ios%20simulator)
* [ipad simulator](https://dev.epicgames.com/community/search?query=ipad%20simulator)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisites](/documentation/en-us/unreal-engine/using-the-xcode-ios-simulator-with-unreal-engine-projects?application_version=5.7#prerequisites)
* [Initial Setup in Unreal Editor](/documentation/en-us/unreal-engine/using-the-xcode-ios-simulator-with-unreal-engine-projects?application_version=5.7#initialsetupinunrealeditor)
* [Use an iOS Simulator in Xcode](/documentation/en-us/unreal-engine/using-the-xcode-ios-simulator-with-unreal-engine-projects?application_version=5.7#useaniossimulatorinxcode)
* [Launch on an iOS Simulator from Unreal Editor (Experimental)](/documentation/en-us/unreal-engine/using-the-xcode-ios-simulator-with-unreal-engine-projects?application_version=5.7#launchonaniossimulatorfromunrealeditor(experimental))
* [Upgrade Existing Projects to use the iOS Simulator](/documentation/en-us/unreal-engine/using-the-xcode-ios-simulator-with-unreal-engine-projects?application_version=5.7#upgradeexistingprojectstousetheiossimulator)
* [Running Multiple Instances](/documentation/en-us/unreal-engine/using-the-xcode-ios-simulator-with-unreal-engine-projects?application_version=5.7#runningmultipleinstances)
