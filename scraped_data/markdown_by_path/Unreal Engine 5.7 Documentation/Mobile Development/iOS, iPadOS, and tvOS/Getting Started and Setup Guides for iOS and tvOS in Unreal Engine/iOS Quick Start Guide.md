<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-an-unreal-engine-project-for-ios?application_version=5.7 -->

# iOS Quick Start Guide

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
6. [iOS, iPadOS, and tvOS](/documentation/en-us/unreal-engine/ios-ipados-and-tvos-support-for-unreal-engine "iOS, iPadOS, and tvOS")
7. [Getting Started and Setup Guides for iOS and tvOS in Unreal Engine](/documentation/en-us/unreal-engine/getting-started-and-setup-guides-for-ios-and-tvos-in-unreal-engine "Getting Started and Setup Guides for iOS and tvOS in Unreal Engine")
8. iOS Quick Start Guide

# iOS Quick Start Guide

Set up an Unreal Engine project for iOS, tvOS, or iPadOS.

![iOS Quick Start Guide](https://dev.epicgames.com/community/api/documentation/image/a10b6270-181c-4d5c-91d6-8b64b3d90b5a?resizing_type=fill&width=1920&height=335)

 On this page

This quick start guide explains all the steps required to build an **Unreal Engine** project for Apple's iOS, iPadOS, and tvOS platforms. By completing this guide, you will:

* Set up Xcode on your Mac.
* Connect to your device in Xcode.
* Register your device with your Apple Developer account.
* Create a Provisioning Profile and Certificates for your project.
* Configure your project for iOS.
* Build and run your project on an iOS device.

This guide covers creating signed builds for C++ projects. For Blueprint-only projects on Windows, there is an alternate workflow for building iOS projects. Refer to [Packaging iOS Projects](https://dev.epicgames.com/documentation/en-us/unreal-engine/packaging-ios-projects-in-unreal-engine) for more information.

Additionally, while this guide refers to iPhone and iOS as an example, note that the same setup steps are used for tvOS. To connect to a tvOS device, refer to the [Connecting to a tvOS Device](https://dev.epicgames.com/documentation/en-us/unreal-engine/connecting-to-tvos-devices-in-unreal-engine) page.

## 1. Requirements

To build projects for Apple's platforms, you need the following:

* A computer running MacOS with Unreal Engine installed.
* An installation of Xcode that is compatible with your current version of Unreal Engine.
* An Apple Developer Account.
* An iOS device that is compatible with your current version of Unreal Engine.

The following software versions are compatible with the current version of Unreal Engine:

* Current UE Version: 5.6

  + Supported Target SDK versions: iOS 15 or later
  + Recommended macOS and Xcode Versions

    - macOS Sonoma 14.7
    - Xcode 
      16.1
  + Minimum macOS and Xcode Versions

    - macOS Sonoma 14.5
    - Xcode 16

The following iOS hardware versions are compatible with the current version of Unreal Engine:

* iOS 15

  + iPhone 6S or later
  + iPod Touch 7th generation
* iPadOS 15

  + iPad 5th generation or later
  + iPad Air 2 or later
  + iPad Mini 4 or later
  + iPad Pro (all models)
* tvOS 15

  + Apple TV HD
  + Apple TV 4K (first generation)
  + Apple TV 4K (second generation)

Apple A8/A8X-based devices (iPad Air 2, iPad Mini 4 and Apple TV HD) require a project setting for support to be enabled. Some rendering features may be limited on A8/A8X devices.

For software compatibility information about older versions of Unreal Engine, refer to the [iOS and tvOS Development Requirements](https://dev.epicgames.com/documentation/en-us/unreal-engine/ios-ipados-and-tvos-development-requirements-for-unreal-engine?application_version=5.5) page.

## 2. Set Up Xcode

1. If you do not already have Xcode installed on your Mac, download and install it from the App Store. You need to sign in with your Apple ID.

   [![Download Xcode from the App Store](https://dev.epicgames.com/community/api/documentation/image/bbc419dd-bb3b-4a34-b6e4-bf08d0a18026?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bbc419dd-bb3b-4a34-b6e4-bf08d0a18026?resizing_type=fit)
2. Open Xcode. In the toolbar, open **Xcode** > **Settings**.

   [![Open Xcode > Settings](https://dev.epicgames.com/community/api/documentation/image/930ebbac-75cc-4383-b10c-7e03860ad8aa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/930ebbac-75cc-4383-b10c-7e03860ad8aa?resizing_type=fit)
3. Open the **Locations** tab, then verify that the **Command Line Tools** path is set to the current version of Xcode. If this path is not set, you will not be able to open Unreal Editor, as the Metal shader compiler will not be able to find Xcode.

   [![Make sure to set your Command Line Tools path](https://dev.epicgames.com/community/api/documentation/image/14c7a780-5f61-465c-a00c-c4428f4c0c23?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/14c7a780-5f61-465c-a00c-c4428f4c0c23?resizing_type=fit)

## 3. Create a Project

To set up a Mobile project, open Unreal Editor and create a new project with the following specifications:

[![The settings for a new Mobile project](https://dev.epicgames.com/community/api/documentation/image/babcbc96-6937-489f-92f7-014f4577efce?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/babcbc96-6937-489f-92f7-014f4577efce?resizing_type=fit)

Click image for full size.

1. Open **Unreal Editor**. When the **Unreal Project Browser** appears, click **Games**.
2. Configure your project as follows:

   * **Project Template:** Top Down
   * **Target Platform:** Mobile
   * **Quality Preset:** Scalable
   * **Project Name:** MobileTestGame

You can create a project that uses either **Blueprint** or **C++**.

1. Click **Create** to create the project and open it in Unreal Editor.

The above specifications and project name are from the [Creating a Mobile Project](https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-an-unreal-engine-project-for-mobile-platforms) guide. Refer to that page for more details on these specifications.

## 4. Connect Your Device With Xcode and Register it With Your Apple Developer Account

To use your iOS device for testing, you need to connect it to your computer, make sure it is recognized by Xcode, and register it in your Apple Developer Account as a testing device for your apps. The device registration will be used later for creating a Provisioning Profile. Follow these steps to set up your device:

1. Connect your iOS Device to your computer with a USB cable.
2. Open Xcode, then click **Window** > **Devices and Simulators**.
3. Unlock your device to grant Xcode access to it. When you see the **Trust This Device** prompt on your iOS device, tap **Trust**, then provide your passcode. Xcode will fetch debug symbols for the device.
4. Log in to your Apple Developer account at [developer.apple.com](https://developer.apple.com). If you do not have an Apple ID and a developer account, create one.

   While Epic's software is available free of charge, Apple Developer accounts cost a fee of $99 per year. Keep this in mind when registering your account.
5. Once you have logged in, click **Certificates, Identifiers & Profiles**.
6. Click **Devices**, then click **Register a Device**.
7. Fill out the following information about your device:

   * Set the **Platform** to iOS, tvOS, watchOS.
   * Set the **Device Name** to a unique, recognizable name.
   * Look at the information about your device in **Xcode** in **Window** > **Devices and Simulators**. Copy the **Identifier**, then return to the Register a Device page and paste it into the **UUID** field.

   Click **Continue** when you are finished.
8. Double-check that the information about your device is correct. If you input the wrong UUID, you may see the wrong type of device listed. Click **Register** to finish registering your device with your Apple developer account. When registration is complete, click **Done**.

## 5. Provisioning and Signing

The following is a short summary of how to obtain a Code Signing Certificate and Provisioning Profile for your app, which are required to package an iOS project. For fully detailed steps, refer to the [iOS Provisioning guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-ios-tvos-and-ipados-provisioning-profiles-and-signing-certificates-for-unreal-engine-projects).

1. Connect your Apple Developer ID with Xcode in **Xcode** > **Preferences** > **Accounts**.
2. Create an **Identifier** (App ID) for your app. Provide a Bundle Identifier name with the format com.(OrganizationName).(ProjectName). In this example, the Bundle Identifier is com.YourCompany.MobileTestProject.
3. Open your project's Xcode project file, then make sure it has the same Bundle Identifier as you specified for your App ID. Do the same in Unreal Editor in **Project Settings** > **Platforms** > **iOS**.
4. Under **Signing & Capabilities**, enable **Automatically Manage Signing**, then set your **Team** to the name associated with your Apple Developer account. Xcode will automatically generate a code signing certificate. Alternatively, you can create one manually in the **Certificates, Identifiers, and Profiles** section of the Apple Developer Page.
5. Open the Apple Developer page, then open **Certificates, Identifiers, and Profiles**. Create a new **Provisioning Profile** using your Identifier, your registered device, and your signing certificate. Download it to a convenient location, such as a **Provisioning** folder.
6. Go to the Apple [Certificate Authority Page](https://www.apple.com/certificateauthority/) and download the latest [WWDR Intermediate Certificate](https://developer.apple.com/support/expiration/). Open the **Keychain Access** app and drag the certificate into the **System keychain**. This is not necessary to package your project for testing, but it is necessary for shipping.
7. Open your project in Unreal Editor, then open **Project Settings** > **Platforms** > **iOS**. Give the editor a few moments to discover your Provisioning Profile and your Signing Certificate, then select each of them.

## 6. Packaging Your Project

After completing the above sections, click the **Platforms** dropdown, then click **iOS** > **Package Project**. If all of your components are set up correctly, your project will package successfully. You can also use the **Quick Launch** option to launch on your selected device directly.

## Final Result

After following the steps in this guide, you will have an iOS project set up, ready to launch on your test device,

* [c++](https://dev.epicgames.com/community/search?query=c++)
* [mobile](https://dev.epicgames.com/community/search?query=mobile)
* [macos](https://dev.epicgames.com/community/search?query=macos)
* [ios](https://dev.epicgames.com/community/search?query=ios)
* [tvos](https://dev.epicgames.com/community/search?query=tvos)
* [ipados](https://dev.epicgames.com/community/search?query=ipados)
* [xcode](https://dev.epicgames.com/community/search?query=xcode)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [1. Requirements](/documentation/en-us/unreal-engine/setting-up-an-unreal-engine-project-for-ios?application_version=5.7#1-requirements)
* [2. Set Up Xcode](/documentation/en-us/unreal-engine/setting-up-an-unreal-engine-project-for-ios?application_version=5.7#2-set-up-xcode)
* [3. Create a Project](/documentation/en-us/unreal-engine/setting-up-an-unreal-engine-project-for-ios?application_version=5.7#3-create-a-project)
* [4. Connect Your Device With Xcode and Register it With Your Apple Developer Account](/documentation/en-us/unreal-engine/setting-up-an-unreal-engine-project-for-ios?application_version=5.7#4-connect-your-device-with-xcode-and-register-it-with-your-apple-developer-account)
* [5. Provisioning and Signing](/documentation/en-us/unreal-engine/setting-up-an-unreal-engine-project-for-ios?application_version=5.7#5-provisioning-and-signing)
* [6. Packaging Your Project](/documentation/en-us/unreal-engine/setting-up-an-unreal-engine-project-for-ios?application_version=5.7#6-packaging-your-project)
* [Final Result](/documentation/en-us/unreal-engine/setting-up-an-unreal-engine-project-for-ios?application_version=5.7#final-result)
