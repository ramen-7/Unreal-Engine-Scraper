<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/android-support-for-unreal-engine?application_version=5.7 -->

# Android Support

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
6. Android Support

# Android Support

Learn how to build projects for Android devices.

![Android Support](https://dev.epicgames.com/community/api/documentation/image/072649ed-3c72-4d62-ac63-33cb4cd323ae?resizing_type=fill&width=1920&height=335)

 On this page

**Unreal Engine** supports publishing to **Android** mobile devices and has several features to help in publishing to the **Google Play Store**. This section contains guides for setting up your Android development environment, how to use Android features and services, and how to prepare your game to ship.

## Current SDK Requirements

Since August 31, 2024, Google Play Store requires apps to target Android 14, which requires API level 34. To publish new apps on the Google Play Store, you must update to UE 5.4.4 or newer for target SDK 34 support. Apps built with previous versions of UE will no longer submit successfully.    
  
For more information, see the [Android documentation on Google Play's target API level requirement](https://developer.android.com/google/play/requirements/target-sdk).

* Current UE Version: 5.7
* Android Studio Version: Koala 2024.1.2 Patch 1 September 17, 2024
* Android SDK:

  + Recommended: SDK 35
  + Minimum for compilation: SDK 34
  + Default target SDK for shipping on devices: 34
  + Minimum install SDK level: 26

    Different stores have their own target SDK minimum requirements, which may differ from that mentioned above.
* NDK Version:  r27c
* Build-tools: 35.0.1
* Java runtime: OpenJDK 21.0.3 2024-04-16
* AGDE v23.2.91+ required for [AGDE debugging](https://dev.epicgames.com/documentation/en-us/unreal-engine/debugging-unreal-engine-projects-for-android-in-visual-studio-with-the-agde-plugin).

## Current Device Compatibility

The current version of Unreal Engine supports Android devices meeting the following specifications:

* Android 8 or higher
* 64-bit Arm-based CPU
* UE 5.6 supports both 4KB and 16KB page sizes
* Compatible GPUs

  + Mali T8xx, G68, G71, G72, G76, G77, G78, or G7xx series
  + Adreno 5xx, 6xx or 7xx series
  + PowerVR GM9xxx series
  + Samsung Xclipse 9xx series
* Compatible Graphics APIs

  + OpenGL ES 3.2
  + Vulkan 1.1 on Android 10 or later devices with compatible drivers

## Getting Started

* [![Setting Up Android SDK and NDK](https://dev.epicgames.com/community/api/documentation/image/2fd2e991-7ccc-431a-8cc3-7332751f1eaf?resizing_type=fit&width=640&height=640)

  Setting Up Android SDK and NDK

  Install Android Studio and automatically add SDK components.](https://dev.epicgames.com/documentation/en-us/unreal-engine/set-up-android-sdk-ndk-and-android-studio-using-turnkey-for-unreal-engine)
* [![Android Quick Start](https://dev.epicgames.com/community/api/documentation/image/d55e57e0-e56e-4986-9738-e9bb12654de7?resizing_type=fit&width=640&height=640)

  Android Quick Start

  Setting up for development for the Android platform.](https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-unreal-engine-projects-for-android-development)
* [![Advanced Android SDK Setup](https://dev.epicgames.com/community/api/documentation/image/c62b5bf4-eed8-4064-ad64-005d08040dfe?resizing_type=fit&width=640&height=640)

  Advanced Android SDK Setup

  Advanced setup and troubleshooting guide for using Android SDK with Unreal Engine.](https://dev.epicgames.com/documentation/en-us/unreal-engine/advanced-setup-and-troubleshooting-guide-for-using-android-sdk)
* [![Setting Up Your Android Device For Development](https://dev.epicgames.com/community/api/documentation/image/d7f2181e-b292-406a-9817-7e0575c69c6a?resizing_type=fit&width=640&height=640)

  Setting Up Your Android Device For Development

  Going over how to set your Android devices up for Unreal Engine development.](https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-your-android-device-for-developing-applications-in-unreal-engine)

## Development Guides

* [![Using Google Play Achievements](https://dev.epicgames.com/community/api/documentation/image/2ae9ac48-92cd-4de3-af30-6b626f23d51a?resizing_type=fit&width=640&height=640)

  Using Google Play Achievements

  Using Google Play Achievements to increase player engagement.](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-google-play-achievements-in-unreal-engine-projects)
* [![Using Ad Mob In-Game Ads on Android](https://dev.epicgames.com/community/api/documentation/image/f4905a7e-e2a0-4aa8-89c4-b4986962e6ee?resizing_type=fit&width=640&height=640)

  Using Ad Mob In-Game Ads on Android

  Using the AdMob in-game advertisement system on Android.](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-ad-mob-for-in-game-ads-on-android-with-unreal-engine)
* [![Android Manifest Control](https://dev.epicgames.com/community/api/documentation/image/666319ac-cc22-42f7-842f-e811689f92c5?resizing_type=fit&width=640&height=640)

  Android Manifest Control

  Setting up and using the Android Mainfest file.](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-use-android-manifest-control-in-unreal-engine-projects)
* [![Using In-App Purchases on Android](https://dev.epicgames.com/community/api/documentation/image/4c7892d8-bd4a-4fa3-b2ea-16cf9c0ec2d9?resizing_type=fit&width=640&height=640)

  Using In-App Purchases on Android

  Using in-app purchases to offer additional paid content for your Android game.](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-use-inapp-purchases-in-unreal-engine-projects-on-android)
* [![Using Google Play Services Leaderboards](https://dev.epicgames.com/community/api/documentation/image/3022b1ff-89cb-4874-834d-0d06c3c1a751?resizing_type=fit&width=640&height=640)

  Using Google Play Services Leaderboards

  Using leaderboards in your game.](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-google-play-services-leaderboards-in-unreal-engine-projects)
* [![Android Virtual Keyboard](https://dev.epicgames.com/community/api/documentation/image/2f216800-06e6-44b7-8e87-25a0518ac0b4?resizing_type=fit&width=640&height=640)

  Android Virtual Keyboard

  Going over setting up the Android Virtual Keyboard.](https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-android-virtual-keyboard-in-unreal-engine-projects)
* [![Android Development Reference](https://dev.epicgames.com/community/api/documentation/image/e7322649-727f-4941-bb16-6e38628c28d5?resizing_type=fit&width=640&height=640)

  Android Development Reference

  How to install different Android SDKs, set environment variables, and work with texture formats.](https://dev.epicgames.com/documentation/en-us/unreal-engine/android-development-basics-for-unreal-engine)
* [![Android Vulkan Mobile Renderer](https://dev.epicgames.com/community/api/documentation/image/6a8216c8-8d28-488f-bdc7-556a22da0581?resizing_type=fit&width=640&height=640)

  Android Vulkan Mobile Renderer

  Information about Vulkan compatibility and how to use the Vulkan mobile renderer in Android projects](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-android-vulkan-mobile-renderer-in-unreal-engine)
* [![Setting up Android Launch Screens](https://dev.epicgames.com/community/api/documentation/image/2487d09f-02da-42b1-8e4c-34f5972d1479?resizing_type=fit&width=640&height=640)

  Setting up Android Launch Screens

  Overview of setting up optional custom Android Launch screens for Android projects.](https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-android-launch-screens-in-unreal-engine)

## Packaging and Publishing

* [![Signing Projects for Release](https://dev.epicgames.com/community/api/documentation/image/cb04daff-3a18-4fa7-ad37-67a08384bf45?resizing_type=fit&width=640&height=640)

  Signing Projects for Release

  Getting your project ready for Release to the Google Play store.](https://dev.epicgames.com/documentation/en-us/unreal-engine/signing-android-projects-for-release-on-the-google-play-store-with-unreal-engine)
* [![Google Play Asset Delivery Reference](https://dev.epicgames.com/community/api/documentation/image/31173a14-36da-4e8f-8905-c9cdf5099d3a?resizing_type=fit&width=640&height=640)

  Google Play Asset Delivery Reference

  API reference and implementation guidelines for the GooglePAD API](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-google-play-asset-delivery-in-unreal-engine)
* [![Packaging Android Projects](https://dev.epicgames.com/community/api/documentation/image/52e0dbba-2fd8-493b-ad29-9c57745a46e5?resizing_type=fit&width=640&height=640)

  Packaging Android Projects

  Taking a look at packaging your final Android project.](https://dev.epicgames.com/documentation/en-us/unreal-engine/packaging-android-projects-in-unreal-engine)
* [![Android Configuration Rules System](https://dev.epicgames.com/community/api/documentation/image/1061e916-9265-4dc4-b14d-e6ddace337df?resizing_type=fit&width=640&height=640)

  Android Configuration Rules System

  Taking a look at using the Android Configuration Rules System in your UE projects.](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-android-configuration-rules-system-in-unreal-engine)
* [![Customizing Device Profiles and Scalability for Android](https://dev.epicgames.com/community/api/documentation/image/8f8c02ee-58e2-4cf1-b632-2139dd9796ce?resizing_type=fit&width=640&height=640)

  Customizing Device Profiles and Scalability for Android

  A reference for device profile rules and scalability settings.](https://dev.epicgames.com/documentation/en-us/unreal-engine/customizing-device-profiles-and-scalability-in-unreal-engine-projects-for-android)

## Debugging

* [![Debugging Android Projects](https://dev.epicgames.com/community/api/documentation/image/d3da9b5e-958c-46be-ad96-d0df6775ee5a?resizing_type=fit&width=640&height=640)

  Debugging Android Projects

  How to debug your Android project in Android Studio](https://dev.epicgames.com/documentation/en-us/unreal-engine/debugging-unreal-engine-projects-for-android-using-android-studio)
* [![Debugging with AGDE in Visual Studio](https://dev.epicgames.com/community/api/documentation/image/88f47d18-7c40-4420-8205-030981a3f2ca?resizing_type=fit&width=640&height=640)

  Debugging with AGDE in Visual Studio

  Use AGDE to debug Android projects in Visual Studio](https://dev.epicgames.com/documentation/en-us/unreal-engine/debugging-unreal-engine-projects-for-android-in-visual-studio-with-the-agde-plugin)
* [![Android File Server](https://dev.epicgames.com/community/api/documentation/image/80ed6a66-fb5c-4eff-a5cc-c7cbdffb8d3f?resizing_type=fit&width=640&height=640)

  Android File Server

  Use Android File Server as a substitute for ADB for pushing and editing files for Unreal Engine projects.](https://dev.epicgames.com/documentation/en-us/unreal-engine/android-file-server-for-unreal-engine)
* [![Android Emulator](https://dev.epicgames.com/community/api/documentation/image/f3611255-3fea-4c01-b480-7a96d748f5e4?resizing_type=fit&width=640&height=640)

  Android Emulator

  Use the Android Emulator to launch a virtual device, then test your Unreal Engine apps on it.](https://dev.epicgames.com/documentation/en-us/unreal-engine/debugging-unreal-engine-projects-with-virtual-devices-using-the-android-emulator)

## Optimization

* [![Creating Bundled PSO Caches for Android](https://dev.epicgames.com/community/api/documentation/image/37b0a716-855a-491a-b149-e8427f03cdc6?resizing_type=fit&width=640&height=640)

  Creating Bundled PSO Caches for Android

  Step-by-step walkthrough for creating a bundled PSO cache for an Android device.](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-bundled-pso-caches-for-android-in-unreal-engine)
* [![Unreal Insights on Android Devices](https://dev.epicgames.com/community/api/documentation/image/4941c26c-47bb-45c5-8cbf-de8d5f6c861a?resizing_type=fit&width=640&height=640)

  Unreal Insights on Android Devices

  Step-by-step guide for attaching the Unreal Insights profiler to an Android application running on a test device.](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-use-unreal-insights-to-profile-android-games-for-unreal-engine)
* [![Reducing Android Binary Size](https://dev.epicgames.com/community/api/documentation/image/a3401fb8-b434-4257-90a4-3d62ae32417d?resizing_type=fit&width=640&height=640)

  Reducing Android Binary Size

  Learn about options for decreasing the size of your project's binary files on Android.](https://dev.epicgames.com/documentation/en-us/unreal-engine/reducing-android-binary-size-in-unreal-engine-projects)

* [mobile](https://dev.epicgames.com/community/search?query=mobile)
* [android](https://dev.epicgames.com/community/search?query=android)
* [platform](https://dev.epicgames.com/community/search?query=platform)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Current SDK Requirements](/documentation/en-us/unreal-engine/android-support-for-unreal-engine?application_version=5.7#current-sdk-requirements)
* [Current Device Compatibility](/documentation/en-us/unreal-engine/android-support-for-unreal-engine?application_version=5.7#current-device-compatibility)
* [Getting Started](/documentation/en-us/unreal-engine/android-support-for-unreal-engine?application_version=5.7#getting-started)
* [Development Guides](/documentation/en-us/unreal-engine/android-support-for-unreal-engine?application_version=5.7#development-guides)
* [Packaging and Publishing](/documentation/en-us/unreal-engine/android-support-for-unreal-engine?application_version=5.7#packaging-and-publishing)
* [Debugging](/documentation/en-us/unreal-engine/android-support-for-unreal-engine?application_version=5.7#debugging)
* [Optimization](/documentation/en-us/unreal-engine/android-support-for-unreal-engine?application_version=5.7#optimization)
