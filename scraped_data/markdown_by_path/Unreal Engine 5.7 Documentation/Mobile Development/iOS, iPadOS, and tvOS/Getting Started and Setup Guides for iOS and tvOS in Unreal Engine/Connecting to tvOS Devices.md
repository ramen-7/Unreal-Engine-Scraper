<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/connecting-to-tvos-devices-in-unreal-engine?application_version=5.7 -->

# Connecting to tvOS Devices

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
8. Connecting to tvOS Devices

# Connecting to tvOS Devices

Set up your testing and debugging pipeline for tvOS connecting over a local area network.

![Connecting to tvOS Devices](https://dev.epicgames.com/community/api/documentation/image/a94c2732-51ea-4bad-96a9-78361162fc7b?resizing_type=fill&width=1920&height=335)

 On this page

**AppleTV** devices use similar methods for launching and debugging projects in Xcode as iOS devices. However, because recent tvOS devices do not have a USB port, you need to use your local area network to access them instead. This page will show you how to set up a tvOS device so that you can connect to it using either Unreal Editor's **Device Manager** or Xcode.

## Connecting a tvOS Device

Ideally, both Unreal Editor's Device Manager and Xcode should recognize your tvOS device automatically over the local area network. Follow this checklist to ensure that it is visible to your computer:

1. Make sure your tvOS device is connected to your local network with an Ethernet cable. While it is possible to connect to an Apple TV with WiFi, Ethernet connections are more stable and reliable.
2. In Unreal Editor, from the main menu, select **Window** > **Developer Tools** > **Device Manager**.
3. In the Device Manager window, verify that your tvOS device is visible.
4. If your tvOS device is not visible, click **Connect to IP**, then type in the IP address of the Apple TV.

Once your Apple TV is visible in the Device Manager, you can follow the same workflows for [launching and debugging projects](/documentation/en-us/unreal-engine/debugging-ios-projects-with-xcode-in-unreal-engine) as iOS devices.

* [testing](https://dev.epicgames.com/community/search?query=testing)
* [debugging](https://dev.epicgames.com/community/search?query=debugging)
* [tvos](https://dev.epicgames.com/community/search?query=tvos)
* [xcode](https://dev.epicgames.com/community/search?query=xcode)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Connecting a tvOS Device](/documentation/en-us/unreal-engine/connecting-to-tvos-devices-in-unreal-engine?application_version=5.7#connectingatvosdevice)
