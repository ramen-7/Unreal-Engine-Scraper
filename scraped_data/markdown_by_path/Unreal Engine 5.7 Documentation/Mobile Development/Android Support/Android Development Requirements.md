<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/android-development-requirements-for-unreal-engine?application_version=5.7 -->

# Android Development Requirements

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
6. [Android Support](/documentation/en-us/unreal-engine/android-support-for-unreal-engine "Android Support")
7. Android Development Requirements

# Android Development Requirements

Android development requirements including compatible hardware, software, and SDK information.

![Android Development Requirements](https://dev.epicgames.com/community/api/documentation/image/18e08443-e18f-4ee2-8358-db06715a4163?resizing_type=fill&width=1920&height=335)

 On this page

This page contains the software development kit (SDK) requirements needed to develop Unreal Engine (UE) projects for Android devices, as well as compatible hardware for the current version of UE.

## Current SDK Information

Since August 31, 2024, Google Play Store requires apps to target Android 14, which requires API level 34. To publish new apps on the Google Play Store, you must update to UE 5.4.4 or newer for target SDK 34 support. Apps built with previous versions of UE will no longer submit successfully.    
  
For more information, see the [Android documentation on Google Play's target API level requirement](https://developer.android.com/google/play/requirements/target-sdk).

* Current UE Version: 5.7
* Android Studio Version: Koala 2024.1.2 Patch 1 September 17, 2024
* Android SDK:

  + Recommended: SDK 35
  + Minimum for compilation: SDK 35
  + Default target SDK for shipping on devices: 35
  + Minimum install SDK level: 26

    Different stores have their own target SDK minimum requirements, which may differ from that mentioned above.
* NDK Version:  r27c
* Build-tools: 35.0.1
* Java runtime: OpenJDK 21.0.3 2024-04-16
* AGDE v23.2.91+ required for [AGDE debugging](https://dev.epicgames.com/documentation/en-us/unreal-engine/debugging-unreal-engine-projects-for-android-in-visual-studio-with-the-agde-plugin).

## Current Compatible Devices

UE supports Android devices meeting the following specifications:

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

## Version History

| UE Version | Android Studio Version | Minimum Android SDK Version | Android NDK Version | Notes |
| --- | --- | --- | --- | --- |
| 5.7 | Koala 2024.1.2 Patch 1 September 17, 2024 | Recommended: SDK 35 | NDK r27c |  |
| 5.6 | Koala 2024.1.2 August 29, 2024 | Recommended: SDK 34  Minimum: SDK 34 | NDK r27c | Supports 16kb memory page size. |
| 5.5 | Koala 2024.1.2 August 29, 2024 | Recommended: SDK 34  Minimum: SDK 34 | NDK r25b |  |
| 5.3-5.4 | Flamingo 2022.2.1 Patch 2 May 24, 2023 | Recommended: SDK 33  Minimum: SDK 30 | NDK r25b |  |
| 5.1-5.2 | Android Studio 4.0 | Recommended: SDK 32  Minimum: SDK 30 | NDK r25b | While SDK 30 is the minimum needed to compile on your system, SDK 26 is the minimum SDK you can target for shipping projects on devices. |
| 5.0 | Android Studio 4.0 | SDK 23 | NDK r21e | Minimum SDK version required to use Android File Server (AFS) is 26. |

* [specifications](https://dev.epicgames.com/community/search?query=specifications)
* [android](https://dev.epicgames.com/community/search?query=android)
* [compatibility](https://dev.epicgames.com/community/search?query=compatibility)
* [sdk](https://dev.epicgames.com/community/search?query=sdk)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Current SDK Information](/documentation/en-us/unreal-engine/android-development-requirements-for-unreal-engine?application_version=5.7#current-sdk-information)
* [Current Compatible Devices](/documentation/en-us/unreal-engine/android-development-requirements-for-unreal-engine?application_version=5.7#current-compatible-devices)
* [Version History](/documentation/en-us/unreal-engine/android-development-requirements-for-unreal-engine?application_version=5.7#versionhistory)
