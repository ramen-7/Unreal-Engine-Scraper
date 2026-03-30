<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/augmented-reality-overview-in-unreal-engine?application_version=5.7 -->

# Augmented Reality Overview

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
7. [Developing for Handheld Augmented Reality Experiences](/documentation/en-us/unreal-engine/developing-for-handheld-augmented-reality-experiences-in-unreal-engine "Developing for Handheld Augmented Reality Experiences")
8. Augmented Reality Overview

# Augmented Reality Overview

An overview of Epic's Augmented Reality implementation.

![Augmented Reality Overview](https://dev.epicgames.com/community/api/documentation/image/9b4b7574-94b4-4786-8b84-6ee625f84cfe?resizing_type=fill&width=1920&height=335)

 On this page

Augmented reality (AR) is a technology that overlays a computer-generated image on a user's view of the real world, providing a composite view.

The Unreal Engine AR framework provides a rich, unified framework for building augmented reality apps with the Unreal Engine for both iOS and Android handheld platforms. The unified framework provides a single path of development for both platforms, allowing developers to build augmented reality apps for both platforms using a single code path. The **Handheld AR** Blueprint template provides a complete example project demonstrating the augmented reality functionality available in the Unreal Engine.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f218f22f-a1a9-43a5-9d16-6a5e91f1eaf9/ar_introshot.png)

Augmented reality provides user experiences that add 2D or 3D elements to a live view from a device's camera in a way that makes those elements appear to inhabit the real world.

## iOS and Android Release Support

The unified AR framework includes support for basic AR functionality like Alignment, Light Estimation, Pinning, Session State, Trace Results, and Tracking.

However, the augmented reality story for Android and iOS is constantly evolving. As of Unreal Engine 4.23, we now support some of the advanced functionality available in the latest ARCore and ARKit releases.

**ARCore 1.7**

* Augmented Faces
* Augmented Images
* Cloud Anchors
* Vertical Plane Detection

**ARKit 3.0**

* 2D Image Detection
* 3D Object Detection
* Face Tracking
* Persistent Experiences
* Shared Experiences
* People Occlusion\*
* Motion Capture (2D, 3D, LiveLink)\*

\* Unreal Engine 4.23.1 provides beta support for this feature.

Epic Games developer **Joe Graf** has written several informative blogs discussing ARKit functionality in UE4.

* [2D Image Detection in UE4 4.20](https://medium.com/@joe.j.graf/arkit-1-5-image-detection-in-ue4-4-20-4dcbefb7a178)
* [ARKit 2.0 support in UE4 4.20](https://medium.com/@joe.j.graf/arkit-2-0-support-in-ue4-4-20-47d1156d545f)
* [AR Environment Probes in UE4 4.20](https://medium.com/@joe.j.graf/ar-environment-probes-in-ue4-4-20-afda05bcc587)

## Augmented Reality API

The unified AR framework provides a framework to build augmented reality apps with Unreal Engine for both iOS and Android handheld platforms. The unified AR framework provides a new library of C++ and Blueprint functions that allow developers to build augmented reality apps for both platforms using a single code path. These new functions also make working with augmented reality easier. 
More detailed information can be found in the [Unreal Engine API Reference](http://api.unrealengine.com/INT/API/).

The **Handheld AR** Blueprint template provides a complete example project demonstrating the new augmented reality functionality available in Unreal Engine. A good place to start exploring the project and the new augmented reality functions is to open the **Content Browser**, navigate to **Content\HandheldARBP\Blueprints\UI** and open the **BP\_DebugMenu** asset in the **Blueprint Editor**.

## Supported Handheld Platforms

Currently, we support the iOS and Android platforms. Please read through the following pages to learn which devices are supported on each platform.

* [Apple's iOS Device Compatibility Reference](https://developer.apple.com/library/content/documentation/DeviceInformation/Reference/iOSDeviceCompatibility/DeviceCompatibilityMatrix/DeviceCompatibilityMatrix.html)
* [ARCore Supported Devices Overview](https://developers.google.com/ar/discover#supported_devices)

It's worth mentioning that support for handheld iOS and Android devices isn't new to the Unreal Engine, so if you're already working with Unreal Engine and iOS or Android devices, you'll only need a minimal amount of additional configuration to get started with augmented reality in Unreal Engine.

### iOS

For detailed iOS augmented reality prerequisite information, see the [ARKit Prerequisits](/documentation/en-us/unreal-engine/arkit-prerequisites-in-unreal-engine) topic. Additionally, basic configuration of Unreal Engine and iOS devices is covered in the [iOs and tvOS](/documentation/404) section of the Unreal Engine documentation.

### Android

For detailed Android augmented reality prerequisite information, see the [ARCore Prerequisites](/documentation/en-us/unreal-engine/arcore-prerequisites-in-unreal-engine) topic. Basic configuration of Unreal Engine and Android devices is covered in the [Android Quick Start](/documentation/en-us/unreal-engine/setting-up-unreal-engine-projects-for-android-development) section of the Unreal  Engine documentation.

## Getting Started with Unreal AR

Now that you understand some basic information about using Unreal Engine with augmented reality, it's time to get started by running through the [Handheld AR Template Quickstart](/documentation/en-us/unreal-engine/handheld-ar-template-quickstart-in-unreal-engine) tutorial.

* [xr](https://dev.epicgames.com/community/search?query=xr)
* [virtual reality](https://dev.epicgames.com/community/search?query=virtual%20reality)
* [ar](https://dev.epicgames.com/community/search?query=ar)
* [ios](https://dev.epicgames.com/community/search?query=ios)
* [android](https://dev.epicgames.com/community/search?query=android)
* [startingout](https://dev.epicgames.com/community/search?query=startingout)
* [augmented reality](https://dev.epicgames.com/community/search?query=augmented%20reality)
* [mixed reality](https://dev.epicgames.com/community/search?query=mixed%20reality)
* [mobile ar](https://dev.epicgames.com/community/search?query=mobile%20ar)
* [ar/vr/xr](https://dev.epicgames.com/community/search?query=ar%2Fvr%2Fxr)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [iOS and Android Release Support](/documentation/en-us/unreal-engine/augmented-reality-overview-in-unreal-engine?application_version=5.7#iosandandroidreleasesupport)
* [Augmented Reality API](/documentation/en-us/unreal-engine/augmented-reality-overview-in-unreal-engine?application_version=5.7#augmentedrealityapi)
* [Supported Handheld Platforms](/documentation/en-us/unreal-engine/augmented-reality-overview-in-unreal-engine?application_version=5.7#supportedhandheldplatforms)
* [iOS](/documentation/en-us/unreal-engine/augmented-reality-overview-in-unreal-engine?application_version=5.7#ios)
* [Android](/documentation/en-us/unreal-engine/augmented-reality-overview-in-unreal-engine?application_version=5.7#android)
* [Getting Started with Unreal AR](/documentation/en-us/unreal-engine/augmented-reality-overview-in-unreal-engine?application_version=5.7#gettingstartedwithunrealar)

Related documents

[Handheld AR Template Quickstart

![Handheld AR Template Quickstart](https://dev.epicgames.com/community/api/documentation/image/994215b3-875d-4442-9ffe-a70974d62197?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/handheld-ar-template-quickstart-in-unreal-engine)

[ARKit Prerequisites

![ARKit Prerequisites](https://dev.epicgames.com/community/api/documentation/image/58993022-d275-4304-ba38-3d7eafdb62da?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/arkit-prerequisites-in-unreal-engine)

[ARCore Prerequisites

![ARCore Prerequisites](https://dev.epicgames.com/community/api/documentation/image/82f0d2c1-7fa9-44b7-ba72-600153746fa8?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/arcore-prerequisites-in-unreal-engine)
