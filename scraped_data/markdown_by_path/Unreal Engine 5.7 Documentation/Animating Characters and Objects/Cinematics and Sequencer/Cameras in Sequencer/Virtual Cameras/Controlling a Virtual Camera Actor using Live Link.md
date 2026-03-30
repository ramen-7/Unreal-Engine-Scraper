<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/controlling-a-virtual-camera-actor-using-live-link-in-unreal-engine?application_version=5.7 -->

# Controlling a Virtual Camera Actor using Live Link

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
8. [Virtual Cameras](/documentation/en-us/unreal-engine/virtual-cameras-in-unreal-engine "Virtual Cameras")
9. Controlling a Virtual Camera Actor using Live Link

# Controlling a Virtual Camera Actor using Live Link

Use the sample Virtual Camera Actor, driven by Live Link, to control a Cine Camera Actor.

![Controlling a Virtual Camera Actor using Live Link](https://dev.epicgames.com/community/api/documentation/image/e2a67d84-eb2e-4a5c-af0d-2d819240ef82?resizing_type=fill&width=1920&height=335)

 On this page

The **Virtual Camera** Actor is a camera placed in your Unreal Engine scene that you can use to stream data from a Live Link-connected device. The Live Link-connected device can be used to view and move around the scene and to set up and record shots. This user guide will show you how to use virtual cameras in your project and the different parts of the Unreal VCam app.

## Required Setup

To use Virtual Cameras, you must set up and configure your Unreal Engine project before setting up and connecting your Live Link-enabled device.

### Unreal Engine Setup

Enable the following plugins from the **Plugins** browser found in the **Edit** menu:

* **VirtualCamera**

  + This plugin enables controlling and viewing of cameras with physical devices.
* **Live Link**

  + This plugin enables streaming of animated data into Unreal Engine. For more information, see [Live Link](https://dev.epicgames.com/documentation/en-us/unreal-engine/live-link-in-unreal-engine).
* **Take Recorder**

  + This is a suite of tools and interfaces designed for recording, reviewing and playing back takes in a virtual production environment. For more information, see [Take Recorder](https://dev.epicgames.com/documentation/en-us/unreal-engine/take-recorder-in-unreal-engine) and [Using Take Recorder](https://dev.epicgames.com/documentation/en-us/unreal-engine/record-gameplay-in-unreal-engine).

Features such as Live Link and Take Recorder with Sequencer are larger topics than this page covers. We suggest spending time familiarizing yourself with these features and their use cases. See their linked documentation above.

### Device Setup

Before you can start, you must have a compatible iOS or Android device, and you must download the **Unreal VCam** app from the [App Store](https://apps.apple.com/us/app/live-link-vcam/id1547309663) or [Google Play Store](https://play.google.com/store/apps/details?id=com.epicgames.live_link_vcam).

**iOS Device System Requirements:**

* iOS 15.0 and later
* iPadOS 15.0 and later
* Support for ArKit

**Android Device System Requirements:**

* Android 24 (Nougat) or higher
* ARCore Support

When you open the app for the first time, you must accept the license agreement to use the app. No further setup is needed at this time.

### Optional Prerequisite for this Guide

The **Meerkat Demo** sample project is a real-time short film developed by Weta Digital and rendered entirely in Unreal Engine. This is a project well-suited to test out some of the capabilities of using virtual cameras in a project. This guide uses the sample project for demonstration for setup and usage in a virtual production environment.

You can download the project from [Fab](https://www.fab.com/listings/5ca1076f-c495-449a-b65a-1ae898ab9d37) or you can download it directly from the Epic Games Launcher in the **Samples** tab.

You can learn more specifics about the sample project by visiting the [Meerkat Demo documentation](samples-and-tutorials/engine-feature-examples/meerkat-example).

## Preparing a Scene for Virtual Cameras

To prepare your project to use a virtual camera setup, you must first prepare your scene in Unreal Engine, and then set up your iOS or Android mobile device to interact with it.

**Unreal Engine scene setup:**

To set up your Unreal Engine scene:

1. Navigate to the **Place Actors** panel, and enter "**VCAM**" into the search field, or select the **Virtual Production** icon.

   For newly created projects, the **Place Actors** panel is not displayed by default in Unreal Engine. If you do not see one, navigate to the **Windows** menu and click on **Place Actors** to open one.
2. Click and drag a **VCam Actor** into the scene.

Immediately upon dragging a VCam Actor into the scene, the viewport changes to automatically pilot the virtual camera. Your viewport should look like the image below.

[![image alt text](https://dev.epicgames.com/community/api/documentation/image/74ec3597-49fb-4883-bf67-fb6476e067c5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/74ec3597-49fb-4883-bf67-fb6476e067c5?resizing_type=fit)

Next, you'll connect your mobile device to the Unreal Editor to drive a virtual camera placed in the scene.

**Mobile device setup:**

To set up your device:

1. Connect your mobile device to the same network the machine running your project is using.
2. In the **Unreal Editor**, click the **Pixel Streaming** dropdown menu in the toolbar. Under the **Signaling Server URLs** section of the menu, you should see at least two IP addresses. Enter the one sharing the same network (for instance 192.x.x.x) as your device into the Unreal VCam app.
3. On your device, open the **Unreal VCam** app. Using the IP address that matches your shared network, enter the IP address into the text field in the app.
4. Click **Connect**.

You may see two Pixel Streaming dropdowns, depending on your current configuration. Virtual Camera does not currently support Pixel Streaming 2. Only refer to the “Pixel Streaming” dropdown and not the “Pixel Streaming 2” dropdown when working with Virtual Camera.

If your scene has a single virtual camera, your mobile device automatically connects to that VCam Actor. However, if you have multiple virtual cameras in the scene, you must select one to connect to. See [Using Multiple Virtual Cameras](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-multiple-virtual-cameras-in-unreal-engine) for more information on setting up and using multiple cameras in your project.

Your mobile device should now be connected to a virtual camera placed in your Unreal Editor scene. You should also have control of the virtual camera from your mobile device, and be able to move around to change the view. You should also have access to the Unreal VCam interface on your mobile device and from the Unreal Editor viewport. The VCam interface contains many controls for managing the look and behavior of virtual cameras in the scene.

[![image alt text](https://dev.epicgames.com/community/api/documentation/image/d005e331-9135-4cd9-97dd-93d14446f1c8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d005e331-9135-4cd9-97dd-93d14446f1c8?resizing_type=fit)

## Controlling Inputs to Virtual Camera Controls

The Enhanced Input feature of Unreal Engine is capable of managing a large number of actions and changing them dynamically. Inputs can change behavior depending on their current state. This means that you can assign more mappable keys than there are buttons for in the user interface. In this case, it's ideal for mapping inputs of hardware devices to virtual camera controls in Unreal Engine through the VCam app.

You can add and configure mapped inputs in two ways:

* In the **Project Settings** under the **VCam Input Settings**
* From the **Details Panel** of the VCam Component under the **Input Profile** section.

For more information on setting up and using Enhanced Inputs, see [Controlling Inputs to Virtual Camera Controls](https://dev.epicgames.com/documentation/en-us/unreal-engine/controlling-inputs-to-virtual-camera-controls-in-unreal-engine).

## Virtual Camera Interface

The Virtual Camera's **Controller Interface** features a range of controls and settings. You can use these settings to modify the look and behavior of a virtual camera in Unreal Engine through an external device. For example, you can use an ARKit-enabled iOS device to make modifications. The ARKit features enable physical position and rotation of your device to move and control the virtual camera's position and rotation in your project in real time.

[![image alt text](https://dev.epicgames.com/community/api/documentation/image/0cc517aa-4657-49a3-aede-850ee95869e2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0cc517aa-4657-49a3-aede-850ee95869e2?resizing_type=fit)

The Virtual Camera Actor includes the following:

1. Camera and Device Information
2. Virtual Camera Settings
3. Unreal VCam App Settings
4. Sequencer and Bookmarks Settings

## Adjusting Settings Dials

The majority of configurable settings within the Unreal VCam app use radial dials. These dials can be located on either side of the interface. They sometimes include an inner and outer dial. To select an option, you can drag your finger along the dial in either direction, and dial in your desired values. Changes made with the dials are reflected in real-time in Unreal Engine.

## Navigating the Virtual Scene with the Unreal VCam App

The Unreal VCam app provides a full range of motion tracking in a physical space using ARKit. ARKit does this by streaming out positional and rotational data live to an Unreal Engine instance with Live Link over a network. With the app, you can drive the 3D camera within the real-time environment and visualize the shot on a supported mobile device.

Additionally, touch screen joysticks provide manual controls for navigating the scene using the Unreal VCam app. Movement using the joysticks is layered on top of any motion tracked movement through ARKit.

[![image alt text](https://dev.epicgames.com/community/api/documentation/image/c2899242-c709-4b23-bcbb-ef8261473901?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c2899242-c709-4b23-bcbb-ef8261473901?resizing_type=fit)

### Moving Around With an ARKit-enabled Device

With an ARKit-enabled device, you can move freely within a space, and that movement translates to the Unreal Engine instance running your project. Your tracked movements include being able to fully tilt, pan, and roll your device, and move around in the space in any direction.

Motion tracked through Live Link happens automatically, and syncs with your 3D camera in Unreal Engine. This means you can set up shots using the app, including previs shots before a shoot, capturing real takes during principal photography, and creating a new shot in post production.

The Unreal VCam app includes settings to scale how movement translates to the 3D scene with motion tracking. To learn about how you can adjust these settings, see [Unreal VCam Virtual Camera Settings](animating-characters-and-objects/Sequencer/Cameras/VirtualCamera/controlling-virtual-camera-actors/unreal-vcam-virtual-camera-settings).

### Moving With Touch Screen Joysticks

You can manually move the Virtual Camera actors in the scene using touch screen joysticks on your Live Link-connected device. You can use the joysticks for directional movement, vertical-only movement, and panning of the camera.

The Unreal VCam app includes settings to adjust the sensitivity and scale of movement in the Live Link-connected device. To learn about how you can adjust these settings, see [Unreal VCam Virtual Camera Settings](animating-characters-and-objects/Sequencer/Cameras/VirtualCamera/controlling-virtual-camera-actors/unreal-vcam-virtual-camera-settings).

## Camera Information

The top-most section of the Virtual Camera actor provides quick reference information for configured camera settings.

[![image alt text](https://dev.epicgames.com/community/api/documentation/image/c21dd5bf-6d24-4072-b958-8b8f8d18b325?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c21dd5bf-6d24-4072-b958-8b8f8d18b325?resizing_type=fit)

In the graphic above, the numbers correspond to the following:

1. Quick reference and action for configured camera settings.
2. Timestamp and film frames per second.
3. Quick Action buttons for toggling Camera Behavior

   * Manual and Tracking Focus
   * Focus Peaking
   * Exposure Zebra Striping
   * Hold Position
   * Local Space Flight Mode
   * Kill Roll

### Quick Access to Virtual Camera Settings and Reference

On either side of the Virtual Camera actor is the configured settings for the camera. Tapping on any of these settings directly opens its adjustable dial within the Unreal VCam app.

[![image alt text](https://dev.epicgames.com/community/api/documentation/image/fe0b90c6-8d6f-45f7-a1fd-a52f632e2959?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fe0b90c6-8d6f-45f7-a1fd-a52f632e2959?resizing_type=fit)

The adjustable settings include:

* Lens Size
* FIlmback Size
* Mask Size
* Toggle Camera UI
* ISO
* Focus Distance
* Iris F-Stop
* Shutter Speed

### Accessing and Sharing the Output Log

You can access and share the Output Log to view detailed information about your Vcam session in order to identify and troubleshoot any potential problems you encounter.

To access the Output Log:

1. In the top-right corner of the Unreal VCam app, tap the **Gear** icon to open the settings.
2. Tap **Application Log** to view the available logs.
3. Tap a log to open the **Log Viewer.** The log marked (Current) is the log for the active session.

[![image alt text](https://dev.epicgames.com/community/api/documentation/image/fceedfe1-10d9-4bbd-980d-7d76cb918cf1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fceedfe1-10d9-4bbd-980d-7d76cb918cf1?resizing_type=fit)

[![image alt text](https://dev.epicgames.com/community/api/documentation/image/a26031e1-cb13-4935-8b70-04da92a6602d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a26031e1-cb13-4935-8b70-04da92a6602d?resizing_type=fit)

[![image alt text](https://dev.epicgames.com/community/api/documentation/image/bee1b9a5-b05e-4837-8922-e020cbbf3309?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bee1b9a5-b05e-4837-8922-e020cbbf3309?resizing_type=fit)

[![image alt text](https://dev.epicgames.com/community/api/documentation/image/fc7b8f36-7ed6-4588-8f75-3347786497bb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fc7b8f36-7ed6-4588-8f75-3347786497bb?resizing_type=fit)

To share the output log, click the **Share** icon in the log to save and send the log.

[![image alt text](https://dev.epicgames.com/community/api/documentation/image/48a2f23e-8668-41de-bc33-e4168117b40d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/48a2f23e-8668-41de-bc33-e4168117b40d?resizing_type=fit)

* [getting started](https://dev.epicgames.com/community/search?query=getting%20started)
* [virtual camera](https://dev.epicgames.com/community/search?query=virtual%20camera)
* [working with media](https://dev.epicgames.com/community/search?query=working%20with%20media)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Required Setup](/documentation/en-us/unreal-engine/controlling-a-virtual-camera-actor-using-live-link-in-unreal-engine?application_version=5.7#required-setup)
* [Unreal Engine Setup](/documentation/en-us/unreal-engine/controlling-a-virtual-camera-actor-using-live-link-in-unreal-engine?application_version=5.7#unreal-engine-setup)
* [Device Setup](/documentation/en-us/unreal-engine/controlling-a-virtual-camera-actor-using-live-link-in-unreal-engine?application_version=5.7#device-setup)
* [Optional Prerequisite for this Guide](/documentation/en-us/unreal-engine/controlling-a-virtual-camera-actor-using-live-link-in-unreal-engine?application_version=5.7#optional-prerequisite-for-this-guide)
* [Preparing a Scene for Virtual Cameras](/documentation/en-us/unreal-engine/controlling-a-virtual-camera-actor-using-live-link-in-unreal-engine?application_version=5.7#preparing-a-scene-for-virtual-cameras)
* [Controlling Inputs to Virtual Camera Controls](/documentation/en-us/unreal-engine/controlling-a-virtual-camera-actor-using-live-link-in-unreal-engine?application_version=5.7#controlling-inputs-to-virtual-camera-controls)
* [Virtual Camera Interface](/documentation/en-us/unreal-engine/controlling-a-virtual-camera-actor-using-live-link-in-unreal-engine?application_version=5.7#virtual-camera-interface)
* [Adjusting Settings Dials](/documentation/en-us/unreal-engine/controlling-a-virtual-camera-actor-using-live-link-in-unreal-engine?application_version=5.7#adjusting-settings-dials)
* [Navigating the Virtual Scene with the Unreal VCam App](/documentation/en-us/unreal-engine/controlling-a-virtual-camera-actor-using-live-link-in-unreal-engine?application_version=5.7#navigating-the-virtual-scene-with-the-unreal-v-cam-app)
* [Moving Around With an ARKit-enabled Device](/documentation/en-us/unreal-engine/controlling-a-virtual-camera-actor-using-live-link-in-unreal-engine?application_version=5.7#moving-around-with-an-ar-kit-enabled-device)
* [Moving With Touch Screen Joysticks](/documentation/en-us/unreal-engine/controlling-a-virtual-camera-actor-using-live-link-in-unreal-engine?application_version=5.7#moving-with-touch-screen-joysticks)
* [Camera Information](/documentation/en-us/unreal-engine/controlling-a-virtual-camera-actor-using-live-link-in-unreal-engine?application_version=5.7#camera-information)
* [Quick Access to Virtual Camera Settings and Reference](/documentation/en-us/unreal-engine/controlling-a-virtual-camera-actor-using-live-link-in-unreal-engine?application_version=5.7#quick-access-to-virtual-camera-settings-and-reference)
* [Accessing and Sharing the Output Log](/documentation/en-us/unreal-engine/controlling-a-virtual-camera-actor-using-live-link-in-unreal-engine?application_version=5.7#accessing-and-sharing-the-output-log)
