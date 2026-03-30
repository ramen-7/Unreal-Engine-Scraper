<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/set-up-android-sdk-ndk-and-android-studio-using-turnkey-for-unreal-engine?application_version=5.7 -->

# Setting Up Android SDK and NDK

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
7. [Getting Started and Setup for Android in Unreal Engine](/documentation/en-us/unreal-engine/getting-started-and-setup-for-android-projects-in-unreal-engine "Getting Started and Setup for Android in Unreal Engine")
8. Setting Up Android SDK and NDK

# Setting Up Android SDK and NDK

Install Android Studio and automatically add SDK components.

![Setting Up Android SDK and NDK](https://dev.epicgames.com/community/api/documentation/image/11dd5d2d-b3c5-4946-84a2-3398d0245435?resizing_type=fill&width=1920&height=335)

 On this page

Unreal Engine (UE)uses **Android Studio** and the **Android SDK Command-Line Tools** to download and install the Android SDK components required to develop Android projects.

### Installation Summary

To install Android SDK, follow these steps:

1. Run **Turnkey** to automatically download and install the needed version of Android Studio.
2. Configure the Android Studio installation to download the Android SDK Command-Line Tools.
3. Close Android Studio and let Turnkey continue installing the needed Android SDK components.
4. Reboot your computer.

These steps are explained in further detail in the sections below.

If you do not install Android SDK Command-Line Tools, Turnkey will fail to download Android NDK and other needed components. Make sure you do not miss this step!

### Required Versions

The following are the required software components needed to develop Android projects in Unreal Engine:

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

## Required Setup

To use this installation guide, you must have an installation of Unreal Engine 5.4 or newer. The Android Turnkey installation process is not available in UE 5.3 or earlier. For installation instructions on those versions, see the [Advanced Android Studio Setup Guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/advanced-setup-and-troubleshooting-guide-for-using-android-sdk).

## Run Turnkey to Begin Installing Android Studio

UE uses an **Unreal Automation Tool** script called Turnkey to distribute SDKs throughout teams. Normally, Turnkey requires you to put a platform's SDK installation files in a common location for your team. However, Android Studio is publicly available, therefore Turnkey can automatically download it and begin setup without any extra steps.

For more information about Turnkey, see the Turnkey documentation.

### Run Turnkey From Unreal Editor

To run the Android Turnkey installation process from Unreal Editor, follow these steps:

1. Open **Unreal Editor**.
2. Click **Platforms** > **Android** > **Install SDK**.

### Run Turnkey From a Command Line

To run the Android Turnkey installation process from a command line, follow these steps:

1. Open your command line.
2. Navigate to your Unreal Engine install directory and run the following command:

   Commandline

   C++

   ```
   RunUAT.bat Turnkey -Command=InstallSDK Platform=Android
   ```

   RunUAT.bat Turnkey -Command=InstallSDK Platform=Android

   Copy full snippet(1 line long)

## Set Up Android Studio and Android Command-Line Tools

Regardless of which method you use to run Turnkey, it downloads Android Studio and automatically starts installation. However, before it can continue, you must go through the installation wizard yourself and download the Android SDK Command-Line Tools so that Turnkey can fetch the other components UE needs. To complete installation, follow these steps:

1. When prompted to choose components, leave the default components enabled.
2. When prompted to choose the install directory, use the default directory.

   If you do not use the default install directory, Turnkey will not be able to find files needed in a later step. We strongly recommend keeping the default directory. To target a separate directory, see the [advanced Android Studio setup guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/advanced-setup-and-troubleshooting-guide-for-using-android-sdk).
3. When the installation finishes, open Android Studio.
4. In the **Welcome to Android Studio** dialog, click **More Actions** and click **SDK Manager**.

   [![The location of the SDK Manager shortcut in the Welcome dialog](https://dev.epicgames.com/community/api/documentation/image/0e210e6a-b188-4657-b947-6a8024aae67c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0e210e6a-b188-4657-b947-6a8024aae67c?resizing_type=fit)

This opens the Android Studio Settings menu at Appearance and Behavior > System Settings > Android SDK.

1. Click the **SDK Tools** tab.
2. Check **Android SDK Command-Line Tools (latest)** and then click **Apply**. This downloads the Command-Line tools, which are needed to automatically configure Android Studio for UE.

   [![The Android Settings Menu. The Android SDK section is open, and it is set to the SDK Tools tab with Android SDK Command-Line-Tools checked.](https://dev.epicgames.com/community/api/documentation/image/3f8871c2-d89b-44b1-9bb5-73bcff8bc4d4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3f8871c2-d89b-44b1-9bb5-73bcff8bc4d4?resizing_type=fit)
3. Click **OK** to close the Settings window, then close the Welcome to Android Studio dialog.
4. Close Android Studio and return to either Unreal Editor or your command line.

## Finalize and Verify Your SDK Setup

After you close Android Studio, Turnkey resumes downloading and installing other Android SDK components. Once the process is complete, a prompt appears telling you whether it succeeded.

To finalize the Android SDK installation and make sure it works correctly, follow these steps:

1. Close Unreal Editor or your command line.
2. To finalize your Android environment variables, log out of your machine and then log back in.
3. Open Unreal Editor and click **Platforms** > **Android**. The allowed version and installed version of the SDK should match, and you should not see a button to install or repair Android SDK.

   [![The Platforms dropdown displaying a successful Android SDK installation.](https://dev.epicgames.com/community/api/documentation/image/f20f94db-5041-48da-9b66-64641a911dc4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f20f94db-5041-48da-9b66-64641a911dc4?resizing_type=fit)

## Troubleshooting

If you installed from a fresh system, the above steps should result in a working SDK setup. However, conflicts can arise from old environment variables and installations. For information on how to diagnose and fix specific issues preventing you from setting up Android SDK, see the [advanced Android Studio setup guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/advanced-setup-and-troubleshooting-guide-for-using-android-sdk).

* [android](https://dev.epicgames.com/community/search?query=android)
* [android studio](https://dev.epicgames.com/community/search?query=android%20studio)
* [platform development](https://dev.epicgames.com/community/search?query=platform%20development)
* [android setup](https://dev.epicgames.com/community/search?query=android%20setup)
* [android sdk](https://dev.epicgames.com/community/search?query=android%20sdk)
* [android sdk setup](https://dev.epicgames.com/community/search?query=android%20sdk%20setup)
* [android ndk](https://dev.epicgames.com/community/search?query=android%20ndk)
* [android turnkey](https://dev.epicgames.com/community/search?query=android%20turnkey)
* [android jdk](https://dev.epicgames.com/community/search?query=android%20jdk)
* [android jni](https://dev.epicgames.com/community/search?query=android%20jni)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Installation Summary](/documentation/en-us/unreal-engine/set-up-android-sdk-ndk-and-android-studio-using-turnkey-for-unreal-engine?application_version=5.7#installation-summary)
* [Required Versions](/documentation/en-us/unreal-engine/set-up-android-sdk-ndk-and-android-studio-using-turnkey-for-unreal-engine?application_version=5.7#required-versions)
* [Required Setup](/documentation/en-us/unreal-engine/set-up-android-sdk-ndk-and-android-studio-using-turnkey-for-unreal-engine?application_version=5.7#required-setup)
* [Run Turnkey to Begin Installing Android Studio](/documentation/en-us/unreal-engine/set-up-android-sdk-ndk-and-android-studio-using-turnkey-for-unreal-engine?application_version=5.7#run-turnkey-to-begin-installing-android-studio)
* [Run Turnkey From Unreal Editor](/documentation/en-us/unreal-engine/set-up-android-sdk-ndk-and-android-studio-using-turnkey-for-unreal-engine?application_version=5.7#run-turnkey-from-unreal-editor)
* [Run Turnkey From a Command Line](/documentation/en-us/unreal-engine/set-up-android-sdk-ndk-and-android-studio-using-turnkey-for-unreal-engine?application_version=5.7#run-turnkey-from-a-command-line)
* [Set Up Android Studio and Android Command-Line Tools](/documentation/en-us/unreal-engine/set-up-android-sdk-ndk-and-android-studio-using-turnkey-for-unreal-engine?application_version=5.7#set-up-android-studio-and-android-command-line-tools)
* [Finalize and Verify Your SDK Setup](/documentation/en-us/unreal-engine/set-up-android-sdk-ndk-and-android-studio-using-turnkey-for-unreal-engine?application_version=5.7#finalize-and-verify-your-sdk-setup)
* [Troubleshooting](/documentation/en-us/unreal-engine/set-up-android-sdk-ndk-and-android-studio-using-turnkey-for-unreal-engine?application_version=5.7#troubleshooting)
