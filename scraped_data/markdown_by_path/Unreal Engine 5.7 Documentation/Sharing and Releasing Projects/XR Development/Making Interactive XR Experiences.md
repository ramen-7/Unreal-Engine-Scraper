<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/making-interactive-xr-experiences-in-unreal-engine?application_version=5.7 -->

# Making Interactive XR Experiences

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
7. Making Interactive XR Experiences

# Making Interactive XR Experiences

Add user input to your AR and VR projects in Unreal Engine

![Making Interactive XR Experiences](https://dev.epicgames.com/community/api/documentation/image/5ef91f6b-ef31-46e3-a083-f1c28a96bb79?resizing_type=fill&width=1920&height=335)

 On this page

There are many different kinds of input for XR, such as hand tracking, motion controllers, and eye tracking. This page contains links to documentation about how to add input to your XR projects.

## Input in OpenXR for Head-Mounted Experiences

The OpenXR runtime uses interaction profiles to support various hardware controllers and provide action bindings for whichever controller is connected. This page explains the concepts of input and controller mapping emulation with OpenXR in Unreal Engine.

## Motion Controllers

Motion Controllers represent the controller or hands used for input with XR devices. Motion Controllers can be accessed through a Motion Controller Component, which is typically attached to your project's Pawn. The Motion Controller Component inherits from the Scene Component, which supports location-based behavior, and moves the Pawn it is attached to based on the tracking data from the hardware. This component provides the functionality to render the Motion Controller and to expose the controller for user interactions defined by the Pawn.

These pages show how to set up motion controllers in your project.

[![Using Motion Controllers](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7bd71c20-b3fa-4d86-8ab6-c1a2648d74e8/placeholder_topic.png)

Using Motion Controllers

Showing you how to pick up and drop objects using Motion Controllers.](/documentation/en-us/unreal-engine/using-motion-controllers-in-unreal-engine)
[![Motion Controller Component Setup](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1ac0248f-e6ae-450d-ab3c-12a5aa5d56bb/placeholder_topic.png)

Motion Controller Component Setup

Information on how to setup Motion Controllers for VR interaction.](/documentation/en-us/unreal-engine/motion-controller-component-setup-in-unreal-engine)

## Hand Tracking

The following sections explain how to get started with using hand tracking for input on each platform that supports it.

### Oculus Quest

Hand tracking on Oculus Quest is available through the **Oculus VR** plugin. Currently, you cannot use hand tracking with an OpenXR project. The APIs for hand tracking on Oculus Quest are provided through an Oculus-custom component. Refer to Oculus's [hand tracking documentation](https://developer.oculus.com/documentation/unreal/unreal-hand-tracking/) for more details on visualizing the user's hands and using them as input.

![Oculus Quest hand tracking](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e0445b44-d61a-477d-a38f-25a6d31d933c/handtracking_smaller.gif)

## Training Streams

Watch these training streams to learn how to add input to your XR projects.





## Next Steps

After setting up input in your XR project, follow these guides to add more functionality to your project and to improve its performance.

[![Creating UI for XR Experiences](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8667f2ba-6a5e-47bf-9b43-fad2b5705419/placeholder_topic.png)

Creating UI for XR Experiences

Design user interfaces for XR experiences in Unreal Engine](/documentation/en-us/unreal-engine/design-user-interfaces-for-xr-experiences-in-unreal-engine)
[![Sharing XR Experiences](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/84b25c36-651b-42eb-b920-c006034e88e6/placeholder_topic.png)

Sharing XR Experiences

Create an immersive experience for multiple users in Unreal Engine](/documentation/en-us/unreal-engine/sharing-xr-experiences-in-unreal-engine)
[![XR Performance and Profiling](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/995da777-cd70-4fc5-9b66-b7c5e11e0b00/placeholder_topic.png)

XR Performance and Profiling

Tools and strategies for profiling your XR projects in Unreal Engine](/documentation/en-us/unreal-engine/xr-performance-and-profiling-in-unreal-engine)

* [xr](https://dev.epicgames.com/community/search?query=xr)
* [input](https://dev.epicgames.com/community/search?query=input)
* [openxr](https://dev.epicgames.com/community/search?query=openxr)
* [hand tracking](https://dev.epicgames.com/community/search?query=hand%20tracking)
* [motion controllers](https://dev.epicgames.com/community/search?query=motion%20controllers)
* [ar/vr/xr](https://dev.epicgames.com/community/search?query=ar%2Fvr%2Fxr)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Input in OpenXR for Head-Mounted Experiences](/documentation/en-us/unreal-engine/making-interactive-xr-experiences-in-unreal-engine?application_version=5.7#inputinopenxrforhead-mountedexperiences)
* [Motion Controllers](/documentation/en-us/unreal-engine/making-interactive-xr-experiences-in-unreal-engine?application_version=5.7#motioncontrollers)
* [Hand Tracking](/documentation/en-us/unreal-engine/making-interactive-xr-experiences-in-unreal-engine?application_version=5.7#handtracking)
* [Oculus Quest](/documentation/en-us/unreal-engine/making-interactive-xr-experiences-in-unreal-engine?application_version=5.7#oculusquest)
* [Training Streams](/documentation/en-us/unreal-engine/making-interactive-xr-experiences-in-unreal-engine?application_version=5.7#trainingstreams)
* [Next Steps](/documentation/en-us/unreal-engine/making-interactive-xr-experiences-in-unreal-engine?application_version=5.7#nextsteps)
