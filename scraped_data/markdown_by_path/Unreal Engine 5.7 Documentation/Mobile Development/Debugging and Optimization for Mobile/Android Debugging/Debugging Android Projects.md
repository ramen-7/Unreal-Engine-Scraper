<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/debugging-unreal-engine-projects-for-android-using-android-studio?application_version=5.7 -->

# Debugging Android Projects

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
7. [Android Debugging](/documentation/en-us/unreal-engine/debugging-for-android-devices-in-unreal-engine "Android Debugging")
8. Debugging Android Projects

# Debugging Android Projects

How to debug your Android project in Android Studio

![Debugging Android Projects](https://dev.epicgames.com/community/api/documentation/image/5f5409f5-1663-4b13-8b65-dd7ebbca52ff?resizing_type=fill&width=1920&height=335)

 On this page

You can use Android Studio to debug the C++ and Java code used in your Unreal Engine (UE) projects. This tutorial will guide you on how to set up Android Studio for this process.

## Reduce Iteration Times

To reduce the build time for Android projects during iteration, you can set your project to avoid bundling `libUnreal.so` in your `.apk` and instead push it to an internal file directory on your device. This skips gradle and avoids reinstalling the `.apk` with every change. To implement this, open your project's `*Engine.ini` and add the following lines to it:

\*Engine.ini

```
|  |  |
| --- | --- |
|  | [[/Script/AndroidRuntimeSettings.AndroidRuntimeSettings] |
|  | bDontBundleLibrariesInAPK=True |

Copy full snippet
```

If you are using Unreal Build Tool directly, you can also pass `-ForceDontBundleLibrariesInAPK=true` to enable this setting.

After you opt in to this setting, it should be enabled for both AGDE and Quick Launch for non-shipping builds. Shipping builds still bundle `libUnreal.so` in your `.apk`.

## Set Up Android Studio

To set up Android Studio to debug a UE project, follow these steps:

1. If you have not already done so, download and install the version of Android Studio that is compatible with your current build of Unreal Engine. Refer to the [Development Requirements](/documentation/404) page for information on which version to use, and the [Android SDK and NDK Setup guide](/documentation/en-us/unreal-engine/advanced-setup-and-troubleshooting-guide-for-using-android-sdk) for information about how to set up your environment.
2. Build the `APK` that you want to debug and then deploy it to your Android device you will be using for debugging.

   [![Package Project via Unreal Engine](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dab003ad-4e53-4d9d-aa72-4a74e042db0f/ue5_1-01-select-package-project.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dab003ad-4e53-4d9d-aa72-4a74e042db0f/ue5_1-01-select-package-project.png)

   Click image for full size.
3. Open the Android Studio Launcher and from the displayed options, then select the **Open an existing Android Studio Project**.

   [![Open an existing Android Studio Project](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7e05fa03-675b-4c15-87e6-66ccc123f583/androiddebugging_01.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7e05fa03-675b-4c15-87e6-66ccc123f583/androiddebugging_01.png)

   Click image for full size.
4. From the **Open File or Project** menu, navigate to **C:\YourProjectName\Intermediate\Android\APK\Gradle** and select the **Gradle** directory, then press the **OK** button.

   ![Navigate to Grandle directory](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/eb9a214a-f0c0-4d26-bd80-f9a2db8cc5dd/androiddebugging_02.png "Navigate to Grandle directory")
5. Once Android Studio is open, go to the **Run Menu** and select the **Edit Configurations** option.

   [![Select the Edit Configurations option](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1eb78786-8967-43c0-87da-07fd6fd8ce94/androiddebugging_03.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1eb78786-8967-43c0-87da-07fd6fd8ce94/androiddebugging_03.png)

   Click image for full size.
6. Click on the **Debugger** tab and set the debug type to **Dual**.

   [![Set Debug Type](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5e30ebba-4e20-443c-8b86-9b97d6c80607/androiddebugging_04.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5e30ebba-4e20-443c-8b86-9b97d6c80607/androiddebugging_04.png)

   Click image for full size.
7. Next, go to the **LLDB Startup Command** tab, press **plus** icon (+) and then input the following line, pressing the **OK** button to complete the process.

   ```
       command script import "C:\PathToYourUE4EngineInstall\Engine\Extras/LLDBDataFormatters\UE4DataFormatters_2ByteChars.py"
   Copy full snippet
   ```



   Note that TEXT("string") should be used instead of L("string") in your C++ code.

   [![Add input to the LLDB Startup Command tab](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ff06e578-f35b-4b80-896e-6b2bbe1b9b4f/androiddebugging_05.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ff06e578-f35b-4b80-896e-6b2bbe1b9b4f/androiddebugging_05.png)

   Click image for full size.

   Make sure to press the **Enter** key or the command will not take.
8. Now, open up any of your project's `.cpp` files and add breakpoints to items you want to debug.

   [![Open CPP file and add breakpoints](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b313bbe8-3230-4e22-8012-1893c1bca4d4/androiddebugging_10.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b313bbe8-3230-4e22-8012-1893c1bca4d4/androiddebugging_10.png)

   Click image for full size.
9. From the main menu, select **Run** > **Debug 'app-app'**.

[![Select Debug 'app-app'](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dc691857-8a06-4dc1-a03e-35ca16ef0b38/androiddebugging_06.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dc691857-8a06-4dc1-a03e-35ca16ef0b38/androiddebugging_06.png)

Click image for full size.

1. When the **Select Deployment Type** windows is displayed, select your device from the list and press the **OK** button.

[![Select your device from the list](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c4804c3b-4f1c-4b10-816b-b8e8881d85a5/androiddebugging_07.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c4804c3b-4f1c-4b10-816b-b8e8881d85a5/androiddebugging_07.png)

Click image for full size.

## End Result

Once you have completed the above steps, wait for the debugger to attach to your Android Device.

[![Wait for the debugger to attach to your Android Device](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/30ccdb5c-36ac-4d6c-ae9a-9ec5ee452af1/androiddebugging_08.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/30ccdb5c-36ac-4d6c-ae9a-9ec5ee452af1/androiddebugging_08.png)

Click image for full size.

Depending on the size of your project, it could take some time for the debugger to attach. This also **does not** install the data on the device if you don't use the **Package data inside APK** option. Doing so will make the redeploying for debugging slower since the APK will be larger. Another option is to first do a **Launch** on in the editor before using Android Studio for debugging to install the current level on the device. Alternatively, you can package and install the OBB on the device if you need more than the current level data.

* [development](https://dev.epicgames.com/community/search?query=development)
* [debugging](https://dev.epicgames.com/community/search?query=debugging)
* [programming](https://dev.epicgames.com/community/search?query=programming)
* [android](https://dev.epicgames.com/community/search?query=android)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Reduce Iteration Times](/documentation/en-us/unreal-engine/debugging-unreal-engine-projects-for-android-using-android-studio?application_version=5.7#reduceiterationtimes)
* [Set Up Android Studio](/documentation/en-us/unreal-engine/debugging-unreal-engine-projects-for-android-using-android-studio?application_version=5.7#setupandroidstudio)
* [End Result](/documentation/en-us/unreal-engine/debugging-unreal-engine-projects-for-android-using-android-studio?application_version=5.7#endresult)
