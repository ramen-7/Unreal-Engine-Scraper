<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/develping-for-windows-mixed-reality-in-unreal-engine?application_version=5.7 -->

# Developing for Windows Mixed Reality

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
8. Developing for Windows Mixed Reality

# Developing for Windows Mixed Reality

How you can develop for Windows Mixed Reality VR devices in Unreal Engine

![Developing for Windows Mixed Reality](https://dev.epicgames.com/community/api/documentation/image/1a5439d5-36f4-44d2-a07d-3594e55c988a?resizing_type=fill&width=1920&height=335)

 On this page

[Windows Mixed Reality](https://www.microsoft.com/en-us/mixed-reality/windows-mixed-reality) is a [head-mounted virtual reality](/documentation/en-us/unreal-engine/developing-for-head-mounted-experiences-with-openxr-in-unreal-engine) platform from [Microsoft](https://www.microsoft.com) that is supported in Unreal Engine through the OpenXR APIs. This page describes how Windows Mixed Reality is supported in Unreal Engine, and how to set up your environment to develop with Windows Mixed Reality. Refer to [Supported XR Devices](/documentation/en-us/unreal-engine/supported-xr-devices-in-unreal-engine) for the full list of which devices Unreal Engine supports.

To develop Unreal Engine projects for Windows Mixed Reality VR devices you should use the **OpenXR** plugin and the **[Microsoft OpenXR](https://www.fab.com/listings/8c00dec5-60fa-4b23-b861-98ee885419ce)** plugin.

Refer to the [Developing with OpenXR APIs](/documentation/en-us/unreal-engine/develping-for-windows-mixed-reality-in-unreal-engine#developingwithopenxrapis) and [Developing with Windows Mixed Reality APIs](/documentation/en-us/unreal-engine/develping-for-windows-mixed-reality-in-unreal-engine#developingwithwindowsmixedrealityapis) sections below for more details.

## Developing with OpenXR APIs

To develop for Windows Mixed Reality VR devices using OpenXR in Unreal Engine you must set up the following:

* Updated hardware and software. Refer to Microsoft's [Installation checklist](https://docs.microsoft.com/windows/mixed-reality/develop/install-the-tools).
* [OpenXR Runtime for Windows Mixed Reality](/documentation/en-us/unreal-engine/openxr-prerequisites-in-unreal-engine).
* **OpenXR** plugin enabled in your project.
* [Microsoft OpenXR](https://www.fab.com/listings/8c00dec5-60fa-4b23-b861-98ee885419ce) plugin installed from [Fab](https://www.fab.com) and enabled.

Once you're set up for developing with OpenXR, you can use the OpenXR APIs to develop for not only Windows Mixed Reality VR devices but any device that supports the OpenXR APIs. Refer to [Developing for Head-Mounted Experiences with OpenXR](/documentation/en-us/unreal-engine/developing-for-head-mounted-experiences-with-openxr-in-unreal-engine) for more details.

## Developing with Windows Mixed Reality APIs

To develop for Windows Mixed Reality VR devices using Windows Mixed Reality APIs in Unreal Engine you must set up the following:

* Updated hardware and software. Refer to Microsoft's [Installation checklist](https://docs.microsoft.com/windows/mixed-reality/develop/install-the-tools)
* **Windows Mixed Reality** plugin enabled in your project.

Once you're set up for developing with the Windows Mixed Reality plugin, you can use the Windows Mixed Reality APIs to create experiences for your Windows Mixed Reality VR devices.

## Getting Started with Development

After setting up your project with the OpenXR or Windows Mixed Reality plugin, follow these guides to get started developing for XR.

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

## Profiling

The following guides show how to profile your XR application and what to consider when you need to improve performance.

* [XR Performance and Profiling in Unreal Engine](/documentation/en-us/unreal-engine/xr-performance-and-profiling-in-unreal-engine)
* [Testing and Optimizing Your Content in Unreal Engine](/documentation/en-us/unreal-engine/testing-and-optimizing-your-content)
* Microsoft's documentation on [Profiling with Unreal Insights](https://docs.microsoft.com/windows/mixed-reality/develop/unreal/unreal-insights)

* [vr](https://dev.epicgames.com/community/search?query=vr)
* [platform](https://dev.epicgames.com/community/search?query=platform)
* [openxr](https://dev.epicgames.com/community/search?query=openxr)
* [windows mixed reality](https://dev.epicgames.com/community/search?query=windows%20mixed%20reality)
* [desktop](https://dev.epicgames.com/community/search?query=desktop)
* [ar/vr/xr](https://dev.epicgames.com/community/search?query=ar%2Fvr%2Fxr)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Developing with OpenXR APIs](/documentation/en-us/unreal-engine/develping-for-windows-mixed-reality-in-unreal-engine?application_version=5.7#developingwithopenxrapis)
* [Developing with Windows Mixed Reality APIs](/documentation/en-us/unreal-engine/develping-for-windows-mixed-reality-in-unreal-engine?application_version=5.7#developingwithwindowsmixedrealityapis)
* [Getting Started with Development](/documentation/en-us/unreal-engine/develping-for-windows-mixed-reality-in-unreal-engine?application_version=5.7#gettingstartedwithdevelopment)
* [Profiling](/documentation/en-us/unreal-engine/develping-for-windows-mixed-reality-in-unreal-engine?application_version=5.7#profiling)
