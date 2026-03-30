<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/virtual-cameras-in-unreal-engine?application_version=5.7 -->

# Virtual Cameras

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
5. [Animating Characters and Objects](/documentation/en-us/unreal-engine/animating-characters-and-objects-in-unreal-engine "Animating Characters and Objects")
6. [Cinematics and Sequencer](/documentation/en-us/unreal-engine/cinematics-and-movie-making-in-unreal-engine "Cinematics and Sequencer")
7. [Cameras in Sequencer](/documentation/en-us/unreal-engine/movie-and-cinematic-cameras-in-unreal-engine "Cameras in Sequencer")
8. Virtual Cameras

# Virtual Cameras

Control Cameras inside Unreal Engine by using a modular component system to manipulate and output Camera data.

![Virtual Cameras](https://dev.epicgames.com/community/api/documentation/image/76369613-1439-48dc-bb0b-93b63b49a196?resizing_type=fill&width=1920&height=335)

A **Virtual Camera** drives a **Cine Camera** in **Unreal Engine** by using a modular component system to manipulate camera data and output the final results to a variety of external output devices. In addition, the Virtual Camera system provides its functionality while in the **editor** and during **Play In Editor (PIE)** or **Standalone Game** mode.

The **Virtual Camera Component (VCamComponent)** is the base component that enables building custom virtual cameras in Unreal Engine. With the VCamComponent, a user can drive a Cine Camera inside Unreal Engine by adding custom **Modifiers** and **Output Providers**. The Modifiers manipulate the camera data with custom effects such as filtering, tracking, and auto focus. The Output Providers route the output of the virtual camera to **Composure**, **Media Framework**, editor viewports, or any devices running the **Unreal Remote** app.

In addition, this new architecture includes the following:

* **[Multi-User editing](https://dev.epicgames.com/documentation/en-us/unreal-engine/multi-user-editing-in-unreal-engine)** support for all features.
* The ability to overlay custom UMG controls over the output and interact with them in the editor or on a device.
* Built-in support for input hardware such as controllers and touchscreens.
* Provides the functionality to switch to any custom tracking system with **Live Link**.
* An updated Unreal Remote app with a new UI and improved streaming performance.

For further documentation regarding the virtual camera system, please see the page links below.

* [![Controlling a Virtual Camera Actor using Live Link](https://dev.epicgames.com/community/api/documentation/image/9b360730-53cf-4825-9858-6dd3346e7a96?resizing_type=fit&width=640&height=640)

  Controlling a Virtual Camera Actor using Live Link

  Use the sample Virtual Camera Actor, driven by Live Link, to control a Cine Camera Actor.](https://dev.epicgames.com/documentation/en-us/unreal-engine/controlling-a-virtual-camera-actor-using-live-link-in-unreal-engine)

* [![Unreal VCam Tools and Configuration](https://dev.epicgames.com/community/api/documentation/image/3e77a503-d586-4cf7-a279-09ba789716c3?resizing_type=fit&width=640&height=640)

  Unreal VCam Tools and Configuration

  Tools and configuration options for the Unreal VCam app.](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-vcam-tools-and-configuration-in-unreal-engine)

* [![Unreal VCam Virtual Camera Settings](https://dev.epicgames.com/community/api/documentation/image/f6f8d68e-7ca3-44b2-87f2-113266b0ff51?resizing_type=fit&width=640&height=640)

  Unreal VCam Virtual Camera Settings

  Settings and configuration information for the Unreal VCam app](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-vcam-virtual-camera-settings)

* [![Virtual Camera Multi-User Quick-Start Guide](https://dev.epicgames.com/community/api/documentation/image/159beade-bb62-48b8-a5b6-b70f2ab96515?resizing_type=fit&width=640&height=640)

  Virtual Camera Multi-User Quick-Start Guide

  Use Switchboard to connect multiple users to simultaneously operate Virtual Cameras.](https://dev.epicgames.com/documentation/en-us/unreal-engine/virtual-camera-multiuser-quickstart-guide-in-unreal-engine)

* [![Configuring a Virtual Camera Component](https://dev.epicgames.com/community/api/documentation/image/f5cbf560-cb98-4f2a-ba0e-dc5aa3d03f1d?resizing_type=fit&width=640&height=640)

  Configuring a Virtual Camera Component

  A guide to understanding and configuring a custom virtual camera.](https://dev.epicgames.com/documentation/en-us/unreal-engine/configuring-a-virtual-camera-component-in-unreal-engine)

* [![Controlling Inputs to Virtual Camera Controls](https://dev.epicgames.com/community/api/documentation/image/9fed2b49-2263-49c6-af39-c8dff05d85ea?resizing_type=fit&width=640&height=640)

  Controlling Inputs to Virtual Camera Controls

  How to manage, edit, and configure inputs to virtual camera controls.](https://dev.epicgames.com/documentation/en-us/unreal-engine/controlling-inputs-to-virtual-camera-controls-in-unreal-engine)

* [![Using Multiple Virtual Cameras](https://dev.epicgames.com/community/api/documentation/image/13356286-7df1-40b9-9f49-7dc062e9fcb6?resizing_type=fit&width=640&height=640)

  Using Multiple Virtual Cameras

  How to set up multiple virtual cameras in a virtual production environment.](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-multiple-virtual-cameras-in-unreal-engine)

* [virtual production](https://dev.epicgames.com/community/search?query=virtual%20production)
* [sequencer](https://dev.epicgames.com/community/search?query=sequencer)
* [camera](https://dev.epicgames.com/community/search?query=camera)
* [live link](https://dev.epicgames.com/community/search?query=live%20link)
* [take recorder](https://dev.epicgames.com/community/search?query=take%20recorder)
* [virtual camera](https://dev.epicgames.com/community/search?query=virtual%20camera)
* [ar](https://dev.epicgames.com/community/search?query=ar)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)
