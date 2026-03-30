<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/ios-ipados-and-tvos-support-for-unreal-engine?application_version=5.7 -->

# iOS, iPadOS, and tvOS

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
6. iOS, iPadOS, and tvOS

# iOS, iPadOS, and tvOS

Learn how to build projects for iOS, iPadOS, and Apple TV.

![iOS, iPadOS, and tvOS](https://dev.epicgames.com/community/api/documentation/image/96e352c4-4fdb-48ba-9665-d687e9c1dca3?resizing_type=fill&width=1920&height=335)

 On this page

**Unreal Engine** supports publishing to **iOS** and **tvOS** devices. Developing for these platforms requires some specialized setup, as a machine running **MacOS** is required to make signed builds for C++ projects in Apple's ecosystem, and you need to use **Xcode** to debug builds on iOS and tvOS devices. This section will provide guides on how to use these tools, how to streamline your workflow if your team primarily uses Windows, and how to make the most of iOS and tvOS's features. Additionally, although iOS and tvOS's workflows are mostly the same, these guides cover the handful of differences between them.

## Getting Started

[![Connecting to tvOS Devices](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/91c50022-ed06-4eab-af0d-eb0fc5a3b0f5/placeholder_topic.png)

Connecting to tvOS Devices

Set up your testing and debugging pipeline for tvOS connecting over a local area network.](/documentation/en-us/unreal-engine/connecting-to-tvos-devices-in-unreal-engine)

## iOS and tvOS for Windows Users

[![Remote Mac Builds](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f785ed7c-26b6-459f-8386-1feacfe33f41/ios_qs_editor_topicimage.png)

Remote Mac Builds

Do part of your compilation on a remote Mac from a Windows machine.](/documentation/en-us/unreal-engine/creating-remote-builds-of-unreal-engine-projects-for-ios)
[![Windows Metal Shader Compiler](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4a46659e-558d-4ca6-a566-ad34a7b64ccc/placeholder_topic.png)

Windows Metal Shader Compiler

Use the Windows Metal Shader Compiler for iOS](/documentation/en-us/unreal-engine/using-the-windows-metal-shader-compiler-for-ios-in-unreal-engine)

## Development Guides

[![Working with iOS Input](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5b26a9f0-2982-4fba-bb6a-e4092914dac9/placeholder_topic.png)

Working with iOS Input

Guidelines for working with external input devices in iOS, tvOS and iPadOS 14 and later](/documentation/en-us/unreal-engine/working-with-ios-input-in-unreal-engine)
[![Localizing plist and NSLocalizedString](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/95b0e1b5-7a5e-4602-830c-5a46f495b3aa/placeholder_topic.png)

Localizing plist and NSLocalizedString

Identify strings in your project code that need to be translated.](/documentation/en-us/unreal-engine/localizing-plist-and-nslocalizedstring-in-an-ios-project-in-unreal-engine)
[![iOS Launch Storyboards](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5e70bc24-ccbe-4c07-87ac-5d958a18514e/ios_qs_editor_topicimage.png)

iOS Launch Storyboards

Setting up launch screen storyboards in your Unreal Engine projects for iOS](/documentation/en-us/unreal-engine/setting-up-ios-launch-storyboards-in-unreal-engine-projects)

## Packaging and Publishing

[![Packaging iOS Projects](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5e312e7b-4ba6-44da-8c57-a73a16f13687/ios_qs_editor_topicimage.png)

Packaging iOS Projects

Learn how to package iOS Projects in Unreal Engine](/documentation/en-us/unreal-engine/packaging-ios-projects-in-unreal-engine)

## Debugging

[![Accessing Logs and Crash Reports on iOS and tvOS](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0d6e328a-b000-4543-af96-4bb617d20883/placeholder_topic.png)

Accessing Logs and Crash Reports on iOS and tvOS

Download and read iOS and tvOS logs and crash reports either directly from device or from TestFlight.](/documentation/en-us/unreal-engine/accessing-logs-and-crash-reports-on-ios-and-tvos-in-unreal-engine)
[![Debugging iOS Projects With Xcode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/59d937f3-6ea7-4c8c-811d-69812942da31/placeholder_topic.png)

Debugging iOS Projects With Xcode

Use Xcode to launch your project on device and debug with break points and LLDB commands.](/documentation/en-us/unreal-engine/debugging-ios-projects-with-xcode-in-unreal-engine)
[![Using Remote Session Plugin for iOS Development](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b9e33229-ef5c-4f27-9216-e4f1ec48f9e9/ios_qs_editor_topicimage.png)

Using Remote Session Plugin for iOS Development

Replicate inputs from an iOS device on your PC for testing.](/documentation/en-us/unreal-engine/using-the-remote-session-plugin-for-ios-development-in-unreal-engine)
[![Using the Xcode iOS Simulator](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cce4c329-d52b-4a8e-b661-20190c4a4772/placeholder_topic.png)

Using the Xcode iOS Simulator

Use Xcode's iOS Simulator to test your project on various iOS devices without using a physical device.](/documentation/en-us/unreal-engine/using-the-xcode-ios-simulator-with-unreal-engine-projects)

## Optimization

[![iOS Packaged Game Size](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/288fb9a4-4534-43a9-b52f-c7d6fddec294/ios_qs_editor_topicimage.png)

iOS Packaged Game Size

Factors that affect the size of a packaged iOS game.](/documentation/en-us/unreal-engine/optimizing-packaged-game-size-for-ios-projects-in-unreal-engine)

* [ios](https://dev.epicgames.com/community/search?query=ios)
* [tvos](https://dev.epicgames.com/community/search?query=tvos)
* [ipados](https://dev.epicgames.com/community/search?query=ipados)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Getting Started](/documentation/en-us/unreal-engine/ios-ipados-and-tvos-support-for-unreal-engine?application_version=5.7#gettingstarted)
* [iOS and tvOS for Windows Users](/documentation/en-us/unreal-engine/ios-ipados-and-tvos-support-for-unreal-engine?application_version=5.7#iosandtvosforwindowsusers)
* [Development Guides](/documentation/en-us/unreal-engine/ios-ipados-and-tvos-support-for-unreal-engine?application_version=5.7#developmentguides)
* [Packaging and Publishing](/documentation/en-us/unreal-engine/ios-ipados-and-tvos-support-for-unreal-engine?application_version=5.7#packagingandpublishing)
* [Debugging](/documentation/en-us/unreal-engine/ios-ipados-and-tvos-support-for-unreal-engine?application_version=5.7#debugging)
* [Optimization](/documentation/en-us/unreal-engine/ios-ipados-and-tvos-support-for-unreal-engine?application_version=5.7#optimization)
