<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-bundled-pso-caches-for-android-in-unreal-engine?application_version=5.7 -->

# Creating Bundled PSO Caches for Android

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
7. [Optimization Guides for Android in Unreal Engine](/documentation/en-us/unreal-engine/optimization-guides-for-android-in-unreal-engine "Optimization Guides for Android in Unreal Engine")
8. Creating Bundled PSO Caches for Android

# Creating Bundled PSO Caches for Android

Step-by-step walkthrough for creating a bundled PSO cache for an Android device.

![Creating Bundled PSO Caches for Android](https://dev.epicgames.com/community/api/documentation/image/d1065e72-01c0-4e2a-a11c-7170c8917a8d?resizing_type=fill&width=1920&height=335)

 On this page

[PSO Caching](https://dev.epicgames.com/documentation/en-us/unreal-engine/optimizing-rendering-with-pso-caches-in-unreal-engine) creates and stores the most commonly-used Pipeline State Object data for your app in advance to improve rendering performance, most especially to reduce hitches while running your application. This guide provides a walkthrough of implementing PSO Caching in an Android project in Unreal Engine (UE).

This page provides instructions for the Bundled PSO caching method, which is the legacy, manual PSO caching system used in UE versions 5.2 and earlier. We recommend using the PSO precaching system from 5.3 and newer if it is viable for your project. See the [documentation for PSO Precaching](testing-and-optimizing-your-content\pso-caches\pso-precaching) for more details.

## Required Setup

To follow this guide, you need the following:

* An Unreal Engine project that is set up for [Android as a target platform](https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-unreal-engine-projects-for-android-development).
* The version of [Android SDK and NDK](https://dev.epicgames.com/documentation/en-us/unreal-engine/advanced-setup-and-troubleshooting-guide-for-using-android-sdk) compatible with your current version of Unreal Engine.
* A compatible Android testing device with [developer mode and USB debugging](https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-your-android-device-for-developing-applications-in-unreal-engine) enabled.

To learn more about which Android devices are compatible with your version of Unreal Engine, see [Android Development Requirements](sharing-and-releasing-projects/android/development-requirements)

## Set Up Project Settings for PSO Caching

To configure your project settings to support PSO caching, follow these steps:

1. Open your project in Unreal Editor.
2. Open **Edit** > **Project Settings**.
3. Navigate to **Project** > **Packaging** and make sure **Share Material Shader Code** and **Shared Material Native Libraries** are both enabled.
4. In the next step you need to edit config files manually. Close Unreal Editor to avoid conflicts between your manual edits and the Project Settings.
5. Open your project's `Config/Android` folder, then open `AndroidEngine.ini`. Add the following settings:

   C++

   ```
   |  |  |
   | --- | --- |
   |  | [DevOptions.Shaders] |
   |  | NeedsShaderStableKeys=true |
   ```

   [DevOptions.Shaders]
   NeedsShaderStableKeys=true

   Copy full snippet(2 lines long)

## Run Your Game and Gather PSOs

Now that your project settings are PSO cache-compatible, run a build of your project with the `-logPSO` command line enabled.

1. Make sure your testing device is connected to your computer.
2. Open your project in Unreal Editor.
3. Click **Platforms** > **Project Launcher**.
4. In the Project Launcher, click **+ Add** > **Create Custom Profile** to make a new launch profile.

   [![In the Project Launcher, the user selects the Add button and clicks Create Custom Profile.](https://dev.epicgames.com/community/api/documentation/image/a7f2a44c-bcdc-4205-b90f-fe5bacebf5b4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a7f2a44c-bcdc-4205-b90f-fe5bacebf5b4?resizing_type=fit)
5. Re-name your profile **PSO Caching - ETC2**.
6. In the dropdown next to **How would you like to cook your content?**, click **Cook by the Book**.
7. Choose **Android\_ETC2** as your target platform.

   [![In the Project Launcher, Cook by the Book is the cook setting, and Android_ETC2 is the target platform.](https://dev.epicgames.com/community/api/documentation/image/64063572-d3fb-4b1b-9871-1fe29c19b5d5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/64063572-d3fb-4b1b-9871-1fe29c19b5d5?resizing_type=fit)
8. Under **Deploy**, choose your mobile device as the target device and set the **Variant** to **Android\_ETC2**.
9. Under the **Launch** category, add the `-logPSO` command to **Additional Command Line Parameters**.

   [![The -logPSO command is added to Additional Command Line Parameters](https://dev.epicgames.com/community/api/documentation/image/96c973f1-3aef-4f09-8343-61e298567514?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/96c973f1-3aef-4f09-8343-61e298567514?resizing_type=fit)

   You can use **Android File Server (AFS)** to add the `-logPSO` command to the `UECommandLine.txt` file to an existing build on your device. For more details, see the [documentation for AFS](https://dev.epicgames.com/documentation/en-us/unreal-engine/android-file-server-for-unreal-engine).
10. Launch your profile. UE builds and packages the project, then deploys it to your device.
11. Play through your game. The Output Log displays a message anytime your game logs a new PSO.

When you do future PSO gathering sessions, you can re-use the profile you created from this section.

### Tips for Gathering PSOs

The more PSOs you gather, the longer your game's startup time will be when you package the final app, as all your PSOs have to be loaded before users can start playing. Therefore, we advise gathering PSOs specifically in locations you know are commonly used and have noticeable stuttering, as PSO caches for these locations provide the most benefit to users’ experience.

Anytime a location significantly changes, previously-gathered PSOs for that location will become outdated. Therefore, make sure to gather PSOs frequently throughout production.

## Retrieve Gathered PSO Data From Your Device

After logging your PSOs, you need to retrieve the data from your testing device and incorporate it into a new build. To retrieve your PSO data, follow these steps:

1. Unplug your testing device from your computer and close your game.

   If you try to close your game from the Project Launcher, your device might not save the PSO data it logged.
2. Close your project and re-connect your testing device to your computer.
3. Pull the PSOs from the following directory:

   `Internal Storage/Android/Data/[package name of project]/files/UnrealGame/[project name]/Saved/CollectedPSOs`

   You can pull the CollectedPSOs directory's contents using any of the following methods:

   * Run the following command using Android File Server (AFS): `UnrealAndroidFileTool -p [package name] -k [security token] pull ^saved/CollectedPSOs [destination path]`
   * Connect your device to your computer and use your computer's file system to browse to the location of the PSOs.
4. Copy the `.UPIPELINECACHE` file to your computer in a location that is easily accessible. This example uses a folder in in the project's directory called `Import/PSOFiles`.

## Build Final PSO Cache Data and Add It To Your Project

To incorporate your PSO cache into a build, follow these steps:

1. Open your project folder and locate Saved/Cooked/Android\_ETC2/[Project Name]/Metadata/PipelineCaches. Copy the files in this folder into Import/PSOFiles.
2. Open your command line tool and navigate to the install directory for the engine version you are using for your project, then locate the Engine/Binaries/Win64 folder. For example: C:/Program FIles/Epic Games/UE\_5.2/Engine/Binaries/Win64.
3. Run the following command line:

   C++

   ```
   UnrealEditor-Cmd.exe "YourProjectPath.uproject" -run=ShaderPipelineCacheTools expand C:\PSOfiles\*.rec.upipelinecache C:\PSOfiles\*.shk C:\PSOfiles\"Alias Name"_"Project Name"_"Used Graphics API".spc
   ```

   UnrealEditor-Cmd.exe &quot;YourProjectPath.uproject&quot; -run=ShaderPipelineCacheTools expand C:\PSOfiles\\*.rec.upipelinecache C:\PSOfiles\\*.shk C:\PSOfiles\&quot;Alias Name&quot;\_&quot;Project Name&quot;\_&quot;Used Graphics API&quot;.spc

   Copy full snippet(1 line long)
4. After the command line runs successfully, the Import/PSOFiles directory should contain a new PKCS #7 certificate file. Copy it to your project's Build/Android/PipelineCaches folder.
5. Rebuild and launch your game again. The new build includes the final PSO cache data.

## Result

On launch, you should also see a log stating how many PSOs were loaded. When you run your game, any rendering stutters from locations you gathered PSOs from should be addressed.

* [optimization](https://dev.epicgames.com/community/search?query=optimization)
* [mobile](https://dev.epicgames.com/community/search?query=mobile)
* [android](https://dev.epicgames.com/community/search?query=android)
* [psos](https://dev.epicgames.com/community/search?query=psos)
* [pso caching](https://dev.epicgames.com/community/search?query=pso%20caching)
* [rendering optimization](https://dev.epicgames.com/community/search?query=rendering%20optimization)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Required Setup](/documentation/en-us/unreal-engine/creating-bundled-pso-caches-for-android-in-unreal-engine?application_version=5.7#required-setup)
* [Set Up Project Settings for PSO Caching](/documentation/en-us/unreal-engine/creating-bundled-pso-caches-for-android-in-unreal-engine?application_version=5.7#set-up-project-settings-for-pso-caching)
* [Run Your Game and Gather PSOs](/documentation/en-us/unreal-engine/creating-bundled-pso-caches-for-android-in-unreal-engine?application_version=5.7#run-your-game-and-gather-ps-os)
* [Tips for Gathering PSOs](/documentation/en-us/unreal-engine/creating-bundled-pso-caches-for-android-in-unreal-engine?application_version=5.7#tips-for-gathering-ps-os)
* [Retrieve Gathered PSO Data From Your Device](/documentation/en-us/unreal-engine/creating-bundled-pso-caches-for-android-in-unreal-engine?application_version=5.7#retrieve-gathered-pso-data-from-your-device)
* [Build Final PSO Cache Data and Add It To Your Project](/documentation/en-us/unreal-engine/creating-bundled-pso-caches-for-android-in-unreal-engine?application_version=5.7#build-final-pso-cache-data-and-add-it-to-your-project)
* [Result](/documentation/en-us/unreal-engine/creating-bundled-pso-caches-for-android-in-unreal-engine?application_version=5.7#result)

Related documents

[Android File Server

![Android File Server](https://dev.epicgames.com/community/api/documentation/image/80ed6a66-fb5c-4eff-a5cc-c7cbdffb8d3f?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/android-file-server-for-unreal-engine)

[PSO Caches

![PSO Caches](https://dev.epicgames.com/community/api/documentation/image/40416f3d-94c4-433a-b8e4-663a33bd2270?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/optimizing-rendering-with-pso-caches-in-unreal-engine)

[Creating a Bundled PSO Cache

![Creating a Bundled PSO Cache](https://dev.epicgames.com/community/api/documentation/image/cf0dcaca-042f-423f-9df9-238d4870e9d7?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/manually-creating-bundled-pso-caches-in-unreal-engine)
