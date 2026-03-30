<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/developing-for-head-mounted-experiences-with-openxr-in-unreal-engine?application_version=5.7 -->

# Developing for Head-Mounted Experiences with OpenXR

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
7. Developing for Head-Mounted Experiences with OpenXR

# Developing for Head-Mounted Experiences with OpenXR

Develop on head-mounted AR and VR devices with OpenXR in Unreal Engine.

![Developing for Head-Mounted Experiences with OpenXR](https://dev.epicgames.com/community/api/documentation/image/a897c6b9-cf6f-4ab4-b637-d097c91c197b?resizing_type=fill&width=1920&height=335)

 On this page

[OpenXR](https://www.khronos.org/openxr) is a royalty-free, open standard that provides high-performance access to XR platforms and devices. Epic Games is one of the founding members of the OpenXR Working Group, along with the Khronos Group and industry partners. This multi-company group is working to solve XR fragmentation with a cross-platform standard.

With OpenXR, you can create an immersive experience in Unreal Engine that can run on any system that supports the OpenXR APIs. Currently, OpenXR in Unreal Engine only supports head-mounted devices. To develop XR projects for handheld devices, refer to [Developing for Handheld Augmented Reality Experiences](/documentation/en-us/unreal-engine/developing-for-handheld-augmented-reality-experiences-in-unreal-engine).

![The openxr logo](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/536d9929-ac6b-4327-8804-e781fe655722/openxr_logo.png)

OpenXR and the OpenXR logo are trademarks of the Khronos Group Inc.

This page contains links to documentation about the devices supported by OpenXR and how to develop for head-mounted devices with OpenXR in Unreal Engine.

## OpenXR Runtimes

Each platform has an OpenXR runtime, which is the implementation of the OpenXR APIs for that platform. This page describes all the supported OpenXR runtimes and how to set up your projects to work with them.

[![OpenXR Runtime](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d89d2991-5c95-4061-974a-76b7dfa4cf4f/placeholder_topic.png)

OpenXR Runtime

Learn how to install the OpenXR runtime and set up your projects for OpenXR.](/documentation/en-us/unreal-engine/openxr-prerequisites-in-unreal-engine)

### Plugin Priority

Your Unreal Engine project can ship with the following plugins enabled: OpenXR, Oculus, SteamVR, and Windows Mixed Reality. When you launch your app, the list of plugins is checked in order of the plugin's priority from highest to lowest. The first plugin in the list, whose runtime the app can connect to, is selected.

The following is the current order of plugin priority in Unreal Engine, from highest to lowest:

* Oculus
* OpenXR
* Windows Mixed Reality
* SteamVR

## Extending OpenXR in Unreal Engine

The OpenXR plugin in Unreal Engine supports extension plugins so you can add functionality to OpenXR without relying on engine releases. There are OpenXR extension plugins included in the engine release.

The plugins currently available in Unreal Engine to extend the OpenXR plugin include:

* OpenXRHandTracking
* OpenXREyeTracker
* XRVisualization
* OpenXRMsftHandInteraction
* HP Motion Controller
* OpenXRViveTracker
* XRScribe

You can also install extension plugins from [Fab](https://www.fab.com/) or make your own.

## Supported Platforms

Unreal Engine 5 supports OpenXR devices on Windows and Android.
For device specific features provided through [OpenXR Vendor Extensions](https://registry.khronos.org/OpenXR/specs/1.0/extprocess.html), device vendors are responsible for development and support. You can find vendor plugins for XR devices on Fab.

### Internally validated devices using the native OpenXR Plugin

* Meta Quest 2/3 (PC and Android)
* HTC Vive
* Valve Index

### Externally validated devices

Epic does not guarantee or provide support for device specific features using the following platforms.

* [Meta Quest](https://developers.meta.com/horizon/downloads/package/unreal-engine-5-integration/)
* [Windows Mixed Reality](https://www.fab.com/listings/8c00dec5-60fa-4b23-b861-98ee885419ce)
* [Varjo](https://www.fab.com/listings/aac38f51-491b-4b92-95bf-8ce04311a2ff)
* [Pico](https://www.fab.com/listings/a7eb0f28-d7f1-4b30-8d2d-49d12eeb1d62)
* [Magic Leap](https://developer-docs.magicleap.cloud/docs/guides/unreal/unreal-overview/)

* [xr](https://dev.epicgames.com/community/search?query=xr)
* [steamvr](https://dev.epicgames.com/community/search?query=steamvr)
* [openxr](https://dev.epicgames.com/community/search?query=openxr)
* [oculus](https://dev.epicgames.com/community/search?query=oculus)
* [windows mixed reality](https://dev.epicgames.com/community/search?query=windows%20mixed%20reality)
* [ar/vr/xr](https://dev.epicgames.com/community/search?query=ar%2Fvr%2Fxr)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [OpenXR Runtimes](/documentation/en-us/unreal-engine/developing-for-head-mounted-experiences-with-openxr-in-unreal-engine?application_version=5.7#openxrruntimes)
* [Plugin Priority](/documentation/en-us/unreal-engine/developing-for-head-mounted-experiences-with-openxr-in-unreal-engine?application_version=5.7#pluginpriority)
* [Extending OpenXR in Unreal Engine](/documentation/en-us/unreal-engine/developing-for-head-mounted-experiences-with-openxr-in-unreal-engine?application_version=5.7#extendingopenxrinunrealengine)
* [Supported Platforms](/documentation/en-us/unreal-engine/developing-for-head-mounted-experiences-with-openxr-in-unreal-engine?application_version=5.7#supportedplatforms)
* [Internally validated devices using the native OpenXR Plugin](/documentation/en-us/unreal-engine/developing-for-head-mounted-experiences-with-openxr-in-unreal-engine?application_version=5.7#internallyvalidateddevicesusingthenativeopenxrplugin)
* [Externally validated devices](/documentation/en-us/unreal-engine/developing-for-head-mounted-experiences-with-openxr-in-unreal-engine?application_version=5.7#externallyvalidateddevices)
