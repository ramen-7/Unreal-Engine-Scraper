<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/developing-for-handheld-augmented-reality-experiences-in-unreal-engine?application_version=5.7 -->

# Developing for Handheld Augmented Reality Experiences

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
7. Developing for Handheld Augmented Reality Experiences

# Developing for Handheld Augmented Reality Experiences

Develop on handheld AR devices in Unreal Engine

![Developing for Handheld Augmented Reality Experiences](https://dev.epicgames.com/community/api/documentation/image/ee3b5f80-16f8-4ae3-99e9-6f3299a17208?resizing_type=fill&width=1920&height=335)

 On this page

Unreal Engine supports handheld AR development with a unified framework so your applications can target multiple mobile platforms with minimal platform checks. Handheld AR platforms provide a variety of features that you can use in your Unreal Engine projects, such as facial tracking, environment probes, and object occlusion.

Currently, you cannot use OpenXR to develop with handheld AR devices. To develop XR projects with OpenXR, refer to [Developing for Head-Mounted Experiences with OpenXR](/documentation/en-us/unreal-engine/developing-for-head-mounted-experiences-with-openxr-in-unreal-engine).

This page contains links to documentation on how to develop for handheld AR devices in Unreal Engine.

## Getting Started with Handheld AR

Unreal Engine includes a template project for handheld AR. This template provides a simple base for handheld augmented reality projects, which you can modify to suit your project's needs. These pages explain how to use the template and how to get started developing with handheld AR in Unreal Engine.

[![Handheld AR Template Quickstart](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/994215b3-875d-4442-9ffe-a70974d62197/scanningplanes.png)

Handheld AR Template Quickstart

A guide to setting up a project with the Handheld AR Template and preparing your mobile device to test it](/documentation/en-us/unreal-engine/handheld-ar-template-quickstart-in-unreal-engine)
[![Handheld AR Template Technical Reference](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2d2f0da0-b69b-4fcb-8573-9468dbe25b68/placeholder_topic.png)

Handheld AR Template Technical Reference

A reference page for where key features of the Handheld AR Template are implemented and how they function](/documentation/en-us/unreal-engine/handheld-ar-template-technical-reference)

## Supported Platforms

These pages provide information on the platforms and mobile devices that support handheld augmented reality in Unreal Engine and how to deploy your applications to them.

[![Developing for ARCore](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d6e2ad15-379c-43b0-9f99-5bcdcd4010de/placeholder_topic.png)

Developing for ARCore

How you can develop for ARCore-supported devices in Unreal Engine](/documentation/en-us/unreal-engine/developing-for-arcore-in-unreal-engine)
[![Developing for ARKit](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/10b924d7-45ec-454d-bf41-0d8b400e4224/placeholder_topic.png)

Developing for ARKit

How you can develop for ARKit-supported devices in Unreal Engine](/documentation/en-us/unreal-engine/developing-for-arkit-in-unreal-engine)

## Handheld AR Features

The following is a list of handheld AR features you can add to your projects and whether they're supported on the platforms.

| Feature | Description | ARCore Support | ARKit Support |
| --- | --- | --- | --- |
| **Plane Detection** | You can detect vertical or horizontal planes in the real world. Once the planes are detected, you can then place virtual objects in that location so they can appear to be attached to the real-world object, such as on a table top. | Yes | Yes |
| **Object Occlusion** | Real-world objects can occlude your virtual objects, that is, your virtual objects appear to be rendered behind the real-world object. | Yes | Yes |
| **People Occlusion** | Similar to object occlusion, people can occlude virtual objects. | No | Yes |
| **Environment Probe** | You can estimate the intensity and direction of the real-world lighting. You can then apply this light estimation to your virtual objects to blend them with the real world. | Yes | Yes |
| **ARPins** | You can attach your virtual objects to real-world locations with ARPins. You can also save these ARPins to the cloud and share them with other devices so multiple users can view the same content in the same location. | Yes, locally and through the cloud with Cloud Anchors and Azure Spatial Anchors. | Yes, locally and through the cloud with Geo Anchors, Cloud Anchors, and Azure Spatial Anchors. |
| **Augmented Images** | You can provide reference images that your app can detect and augment. | Yes | Yes |
| **Facial Tracking** | You can detect feature points on the user's face for tracking and augmenting. | Yes | Yes, through either the ARKit API or the [Live Link Face app](/documentation/en-us/unreal-engine/recording-face-animation-on-ios-device-in-unreal-engine). |
| **Geotracking** | You can track specific geographic locations using the device's GPS and world tracking based on downloaded images. This feature is dependent on whether images have been collected for the area. | No | Yes, for more details, refer to [Apple's documentation](https://developer.apple.com/documentation/arkit/content_anchors/tracking_geographic_locations_in_ar). |
| **Camera Intrinsics** | You can retrieve information about the device's physical camera, such as focal length and image resolution. | Yes | Yes |

* [xr](https://dev.epicgames.com/community/search?query=xr)
* [mobile](https://dev.epicgames.com/community/search?query=mobile)
* [ar](https://dev.epicgames.com/community/search?query=ar)
* [handheld ar](https://dev.epicgames.com/community/search?query=handheld%20ar)
* [ar/vr/xr](https://dev.epicgames.com/community/search?query=ar%2Fvr%2Fxr)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Getting Started with Handheld AR](/documentation/en-us/unreal-engine/developing-for-handheld-augmented-reality-experiences-in-unreal-engine?application_version=5.7#gettingstartedwithhandheldar)
* [Supported Platforms](/documentation/en-us/unreal-engine/developing-for-handheld-augmented-reality-experiences-in-unreal-engine?application_version=5.7#supportedplatforms)
* [Handheld AR Features](/documentation/en-us/unreal-engine/developing-for-handheld-augmented-reality-experiences-in-unreal-engine?application_version=5.7#handheldarfeatures)
