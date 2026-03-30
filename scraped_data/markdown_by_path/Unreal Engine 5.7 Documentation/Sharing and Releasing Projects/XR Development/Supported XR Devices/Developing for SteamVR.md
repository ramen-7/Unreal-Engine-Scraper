<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/developing-for-steamvr-in-unreal-engine?application_version=5.7 -->

# Developing for SteamVR

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
8. Developing for SteamVR

# Developing for SteamVR

How you can develop for SteamVR in Unreal Engine.

![Developing for SteamVR](https://dev.epicgames.com/community/api/documentation/image/499e2e6f-29f9-40b3-8fd7-372c822a60ca?resizing_type=fill&width=1920&height=335)

 On this page

The SteamVR plugin has been deprecated in Unreal Engine 5.1. You should use the OpenXR plugin instead.

[SteamVR](https://www.steamvr.com) is a [head-mounted virtual reality](/documentation/en-us/unreal-engine/developing-for-head-mounted-experiences-with-openxr-in-unreal-engine) platform from [Valve](https://www.valvesoftware.com) that is supported in Unreal Engine through the OpenXR APIs. This page describes how SteamVR is supported in Unreal Engine, and how to set up your environment to develop with SteamVR.

SteamVR supports Vive, Oculus, and Windows Mixed Reality headsets. Refer to [Supported XR Devices](/documentation/en-us/unreal-engine/supported-xr-devices-in-unreal-engine) for the full list of XR devices Unreal Engine supports.

Currently, you can develop for SteamVR with either the OpenXR plugin or the SteamVR plugin:

* When you develop with the OpenXR plugin, your application can run on any device that supports the OpenXR APIs.
* When you develop with the SteamVR plugin, your application can only run on devices that SteamVR supports. Some Unreal Engine features, such as [Live Link XR](/documentation/en-us/unreal-engine/livelinkxr-in-unreal-engine), require the SteamVR plugin to use.

Refer to the [Developing with OpenXR APIs](/documentation/en-us/unreal-engine/developing-for-steamvr-in-unreal-engine#developingwithopenxrapis) and [Developing with SteamVR APIs](/documentation/en-us/unreal-engine/developing-for-steamvr-in-unreal-engine#developingwithsteamvrapis) sections below for more details.

## Developing with OpenXR APIs

To develop with SteamVR using OpenXR in Unreal Engine you must set up the following:

* Updated hardware and software. Refer to your device's system and hardware requirements.
* SteamVR version 1.5.17 or later
* [OpenXR Runtime for SteamVR](/documentation/en-us/unreal-engine/openxr-prerequisites-in-unreal-engine)
* **OpenXR** plugin enabled in your project

Once you're set up for developing with OpenXR, you can use the OpenXR APIs to develop for not only devices that SteamVR supports but any device that supports the OpenXR APIs. Refer to [Developing for Head-Mounted Experiences with OpenXR](/documentation/en-us/unreal-engine/developing-for-head-mounted-experiences-with-openxr-in-unreal-engine) for more details.

## Developing with SteamVR APIs

To develop with the SteamVR plugin you must set up the following:

* Updated hardware and software. Refer to your device's system and hardware requirements.
* SteamVR version 1.5.17 or later
* **SteamVR** plugin enabled in your project

Once you're set up for developing with the SteamVR plugin, you can use the SteamVR APIs to develop for SteamVR-supported devices.

## Getting Started with Development

After setting up your project with the OpenXR or SteamVR plugin, follow these guides to get started developing for XR.

[![Getting Started with XR Development](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4a772df2-26e4-4fd5-a7da-e09f3075f35e/placeholder_topic.png)

Getting Started with XR Development

Set up your project and apply best practices for AR and VR devices with Unreal Engine.](/documentation/en-us/unreal-engine/getting-started-with-xr-development-in-unreal-engine)
[![Making Interactive XR Experiences](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d40682e3-646b-4d1d-ae59-10546012822b/placeholder_topic.png)

Making Interactive XR Experiences

Add user input to your AR and VR projects in Unreal Engine](/documentation/en-us/unreal-engine/making-interactive-xr-experiences-in-unreal-engine)
[![Creating UI for XR Experiences](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8667f2ba-6a5e-47bf-9b43-fad2b5705419/placeholder_topic.png)

Creating UI for XR Experiences

Design user interfaces for XR experiences in Unreal Engine](/documentation/en-us/unreal-engine/design-user-interfaces-for-xr-experiences-in-unreal-engine)
[![XR Performance and Profiling](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/995da777-cd70-4fc5-9b66-b7c5e11e0b00/placeholder_topic.png)

XR Performance and Profiling

Tools and strategies for profiling your XR projects in Unreal Engine](/documentation/en-us/unreal-engine/xr-performance-and-profiling-in-unreal-engine)

## Troubleshooting and Profiling

The following guides show how to profile your XR application and what to consider when you need to improve performance.

* [XR Performance and Profiling in Unreal Engine](/documentation/en-us/unreal-engine/xr-performance-and-profiling-in-unreal-engine)
* [Testing and Optimizing Your Content in Unreal Engine](/documentation/en-us/unreal-engine/testing-and-optimizing-your-content)
* [SteamVR Frame Timing](https://developer.valvesoftware.com/wiki/SteamVR/Frame_Timing)

If you experience issues with your headset, visit [SteamVR Support](https://support.steampowered.com/kb_article.php?ref=8566-SDZC-9326) or [HTC Vive Support](https://www.vive.com/us/support/) for troubleshooting help.

* [vr](https://dev.epicgames.com/community/search?query=vr)
* [platform](https://dev.epicgames.com/community/search?query=platform)
* [steamvr](https://dev.epicgames.com/community/search?query=steamvr)
* [openxr](https://dev.epicgames.com/community/search?query=openxr)
* [desktop vr](https://dev.epicgames.com/community/search?query=desktop%20vr)
* [ar/vr/xr](https://dev.epicgames.com/community/search?query=ar%2Fvr%2Fxr)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Developing with OpenXR APIs](/documentation/en-us/unreal-engine/developing-for-steamvr-in-unreal-engine?application_version=5.7#developingwithopenxrapis)
* [Developing with SteamVR APIs](/documentation/en-us/unreal-engine/developing-for-steamvr-in-unreal-engine?application_version=5.7#developingwithsteamvrapis)
* [Getting Started with Development](/documentation/en-us/unreal-engine/developing-for-steamvr-in-unreal-engine?application_version=5.7#gettingstartedwithdevelopment)
* [Troubleshooting and Profiling](/documentation/en-us/unreal-engine/developing-for-steamvr-in-unreal-engine?application_version=5.7#troubleshootingandprofiling)
