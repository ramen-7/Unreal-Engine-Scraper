<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/developing-for-arkit-in-unreal-engine?application_version=5.7 -->

# Developing for ARKit

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
5. [Sharing and Releasing Projects](/documentation/en-us/unreal-engine/sharing-and-releasing-projects-for-unreal-engine "Sharing and Releasing Projects")
6. [XR Development](/documentation/en-us/unreal-engine/developing-for-xr-experiences-in-unreal-engine "XR Development")
7. [Supported XR Devices](/documentation/en-us/unreal-engine/supported-xr-devices-in-unreal-engine "Supported XR Devices")
8. Developing for ARKit

# Developing for ARKit

How you can develop for ARKit-supported devices in Unreal Engine

![Developing for ARKit](https://dev.epicgames.com/community/api/documentation/image/1eba8c50-17bd-404a-a912-bb6feb9e64e1?resizing_type=fill&width=1920&height=335)

 On this page

[ARKit](https://developer.apple.com/augmented-reality/) is a [handheld augmented reality](/documentation/en-us/unreal-engine/developing-for-handheld-augmented-reality-experiences-in-unreal-engine) platform from [Apple](https://www.apple.com) that is supported in Unreal Engine. This page describes how ARKit is supported in Unreal Engine, and how to set up your environment to develop with ARKit. Refer to [Supported XR Devices](/documentation/en-us/unreal-engine/supported-xr-devices-in-unreal-engine) for the full list of which devices and which SDK versions Unreal Engine supports.

## Developing with the ARKit APIs

To develop for ARKit in Unreal Engine you must set up the following:

* Updated hardware and software. Refer to [iOS Development Requirements](/documentation/en-us/unreal-engine/ios-ipados-and-tvos-support-for-unreal-engine).
* Xcode 12 or later installed.
* iOS 14 or later installed
* A supported, configured, and connected handheld iOS device with an A12 Bionic chip or greater.
* **Apple ARKit** plugin enabled in your project.

Once you're set up for developing with ARKit, you can use the unique ARKit functionality to develop for your iOS devices. Refer to [Handheld AR Features](/documentation/en-us/unreal-engine/developing-for-handheld-augmented-reality-experiences-in-unreal-engine#handheldarfeatures) for what features are supported in Unreal Engine.

## Getting Started with Development

After setting up your project with the Apple ARKit plugin, follow these guides to get started developing for ARKit devices.

[![Handheld AR Template Quickstart](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/994215b3-875d-4442-9ffe-a70974d62197/scanningplanes.png)

Handheld AR Template Quickstart

A guide to setting up a project with the Handheld AR Template and preparing your mobile device to test it](/documentation/en-us/unreal-engine/handheld-ar-template-quickstart-in-unreal-engine)
[![Handheld AR Template Technical Reference](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2d2f0da0-b69b-4fcb-8573-9468dbe25b68/placeholder_topic.png)

Handheld AR Template Technical Reference

A reference page for where key features of the Handheld AR Template are implemented and how they function](/documentation/en-us/unreal-engine/handheld-ar-template-technical-reference)

[![ARPins](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f4720721-68eb-428d-94d8-60b618b132fb/placeholder_topic.png)

ARPins

ARPins are a fixed real-world location in augmented reality (AR) to which you can attach virtual content within Unreal Engine.](/documentation/en-us/unreal-engine/arpins-in-unreal-engine)

## Profiling

The following guides show how to profile your XR application and what to consider when you need to improve performance.

* [XR Performance and Profiling in Unreal Engine](/documentation/en-us/unreal-engine/xr-performance-and-profiling-in-unreal-engine)
* [Testing and Optimizing Your Content in Unreal Engine](/documentation/en-us/unreal-engine/testing-and-optimizing-your-content)
* [Debugging iOS and tvOS Projects](/documentation/404)

## Known Limitations

The following are known limitations of features in ARKit:

* Candidate images for image detection must have unique friendly names. If multiple candidate images share the same friendly name, only the image with the first instance of the friendly name will be recognized.

* [mobile](https://dev.epicgames.com/community/search?query=mobile)
* [ar](https://dev.epicgames.com/community/search?query=ar)
* [ios](https://dev.epicgames.com/community/search?query=ios)
* [handheld ar](https://dev.epicgames.com/community/search?query=handheld%20ar)
* [arkit](https://dev.epicgames.com/community/search?query=arkit)
* [ar/vr/xr](https://dev.epicgames.com/community/search?query=ar%2Fvr%2Fxr)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Developing with the ARKit APIs](/documentation/en-us/unreal-engine/developing-for-arkit-in-unreal-engine?application_version=5.7#developingwiththearkitapis)
* [Getting Started with Development](/documentation/en-us/unreal-engine/developing-for-arkit-in-unreal-engine?application_version=5.7#gettingstartedwithdevelopment)
* [Profiling](/documentation/en-us/unreal-engine/developing-for-arkit-in-unreal-engine?application_version=5.7#profiling)
* [Known Limitations](/documentation/en-us/unreal-engine/developing-for-arkit-in-unreal-engine?application_version=5.7#knownlimitations)
