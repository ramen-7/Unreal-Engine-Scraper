<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/developing-for-oculus-in-unreal-engine?application_version=5.7 -->

# Developing for Oculus

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
8. Developing for Oculus

# Developing for Oculus

How you can develop for Oculus devices in Unreal Engine.

![Developing for Oculus](https://dev.epicgames.com/community/api/documentation/image/e785ad16-3289-48eb-9255-1ac718ae3e6f?resizing_type=fill&width=1920&height=335)

 On this page

The OculusVR plugin has been deprecated in Unreal Engine 5.1. You should use the OpenXR plugin instead.

[Oculus](https://www.oculus.com/) is a [head-mounted virtual reality](/documentation/en-us/unreal-engine/developing-for-head-mounted-experiences-with-openxr-in-unreal-engine) platform from [Meta](https://about.facebook.com/meta/) that is supported in Unreal Engine. This page describes how Oculus is supported in Unreal Engine, and how to set up your environment to develop with Oculus. Refer to [Supported XR Devices](/documentation/en-us/unreal-engine/supported-xr-devices-in-unreal-engine) for the full list of which Oculus devices Unreal Engine supports.

Currently, you can develop for Oculus devices with either the **OpenXR** plugin or the **Oculus VR** plugin:

* When you develop with the OpenXR plugin, your application can run on any device that supports the OpenXR APIs.
* When you develop with the Oculus VR plugin, your application can use Oculus-specific features that aren't currently included in the **Oculus OpenXR** extension plugin.

Refer to the [Developing with OpenXR APIs](/documentation/en-us/unreal-engine/developing-for-oculus-in-unreal-engine#developingwithopenxrapis) and [Developing with Oculus APIs](/documentation/en-us/unreal-engine/developing-for-oculus-in-unreal-engine#developingwithoculusapis) sections below for more details.

## Developing with OpenXR APIs

To develop for Oculus using OpenXR in Unreal Engine you must set up the following:

* Updated hardware and software. Refer to [Oculus' System and Hardware Requirements](https://developer.oculus.com/documentation/mobilesdk/latest/concepts/mobile-reqs#mobile-reqs)
* [Oculus app](https://www.oculus.com/setup/)
* Oculus Runtime v33.0 or later
* [OpenXR Runtime for Oculus](/documentation/en-us/unreal-engine/openxr-prerequisites-in-unreal-engine)
* **OpenXR** plugin enabled in your project
* (Oculus Quest only) **Oculus OpenXR** plugin enabled in your project

Once you're set up for developing with OpenXR, you can use the OpenXR APIs to develop for not only Oculus devices but any device that supports the OpenXR APIs. Refer to [Developing for Head-Mounted Experiences with OpenXR](/documentation/en-us/unreal-engine/developing-for-head-mounted-experiences-with-openxr-in-unreal-engine) for more details.

## Developing with Oculus APIs

To develop for Oculus using the Oculus-specific APIs in Unreal Engine you must set up the following:

* Updated hardware and software. Refer to [Oculus' System and Hardware Requirements](https://developer.oculus.com/documentation/mobilesdk/latest/concepts/mobile-reqs#mobile-reqs)
* [Oculus app](https://www.oculus.com/setup/)
* Oculus Runtime v33.0 or later
* **Oculus VR** plugin enabled in your project

Once you're set up for developing with the Oculus VR plugin, you can use Oculus-specific features that aren't available in the OpenXR APIs yet. The following features are currently available only in the Oculus VR plugin for Oculus devices:

* [Hand tracking with Oculus Quest](/documentation/en-us/unreal-engine/making-interactive-xr-experiences-in-unreal-engine#oculusquest)
* [Fixed Foveated Rendering](/documentation/en-us/unreal-engine/xr-performance-features-in-unreal-engine#variablerateshadingandfixedfoveatedrendering)

## Getting Started with Development

After setting up your project with the **OpenXR** or **Oculus VR** plugins, follow these guides to get started developing for Oculus devices.

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

## Auto Instancing on Oculus

A **draw call** is the RHI command to draw an object. **Auto-Instancing** is a feature that automatically combines multiple draw calls into one instanced draw call. An **instanced draw call** is a way for the graphics API to draw multiple instances of similar objects that have varying attributes. These can be any attributes that relate to the rendering of a mesh: position, orientation, color, and so on. This page contains more details about auto-instancing on Oculus Quest.

[![Auto Instancing on Oculus](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/159fe1ba-b6f1-440f-a9c3-a106eb16ed47/placeholder_topic.png)

Auto Instancing on Oculus

Debugging auto-instancing in UE4 for Oculus Quest](/documentation/en-us/unreal-engine/auto-instancing-on-oculus-in-unreal-engine)

## Troubleshooting and Profiling

The following guides show how to profile your XR application and what to consider when you need to improve performance.

* [XR Performance and Profiling in Unreal Engine](/documentation/en-us/unreal-engine/xr-performance-and-profiling-in-unreal-engine)
* [Testing and Optimizing Your Content in Unreal Engine](/documentation/en-us/unreal-engine/testing-and-optimizing-your-content)
* Oculus's page on [Optimization Tools](https://developer.oculus.com/documentation/unreal/ts-book-tools)

If you experience issues with your Oculus headset, visit the [Oculus Support Center](https://support.oculus.com/) for troubleshooting help.

* [vr](https://dev.epicgames.com/community/search?query=vr)
* [platform](https://dev.epicgames.com/community/search?query=platform)
* [openxr](https://dev.epicgames.com/community/search?query=openxr)
* [oculus](https://dev.epicgames.com/community/search?query=oculus)
* [ar/vr/xr](https://dev.epicgames.com/community/search?query=ar%2Fvr%2Fxr)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Developing with OpenXR APIs](/documentation/en-us/unreal-engine/developing-for-oculus-in-unreal-engine?application_version=5.7#developingwithopenxrapis)
* [Developing with Oculus APIs](/documentation/en-us/unreal-engine/developing-for-oculus-in-unreal-engine?application_version=5.7#developingwithoculusapis)
* [Getting Started with Development](/documentation/en-us/unreal-engine/developing-for-oculus-in-unreal-engine?application_version=5.7#gettingstartedwithdevelopment)
* [Auto Instancing on Oculus](/documentation/en-us/unreal-engine/developing-for-oculus-in-unreal-engine?application_version=5.7#autoinstancingonoculus)
* [Troubleshooting and Profiling](/documentation/en-us/unreal-engine/developing-for-oculus-in-unreal-engine?application_version=5.7#troubleshootingandprofiling)
