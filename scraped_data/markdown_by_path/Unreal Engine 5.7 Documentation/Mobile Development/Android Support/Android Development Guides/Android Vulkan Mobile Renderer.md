<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-android-vulkan-mobile-renderer-in-unreal-engine?application_version=5.7 -->

# Android Vulkan Mobile Renderer

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
5. [Mobile Development](/documentation/en-us/unreal-engine/getting-started-with-mobile-development-in-unreal-engine "Mobile Development")
6. [Android Support](/documentation/en-us/unreal-engine/android-support-for-unreal-engine "Android Support")
7. [Android Development Guides](/documentation/en-us/unreal-engine/developing-guides-for-android-in-unreal-engine "Android Development Guides")
8. Android Vulkan Mobile Renderer

# Android Vulkan Mobile Renderer

Information about Vulkan compatibility and how to use the Vulkan mobile renderer in Android projects

![Android Vulkan Mobile Renderer](https://dev.epicgames.com/community/api/documentation/image/f59593d9-a5f7-4951-9f33-c6a446784193?resizing_type=fill&width=1920&height=335)

 On this page

**Unreal Engine** (UE) has built-in support for the **Vulkan** graphics API. Vulkan is a low-overhead, cross-platform 3D graphics library that gives developers more control over the GPU and lower level CPU usage for their Android base mobile projects. The following document shows how you can enable and use Vulkan in your UE Android projects.

## Vulkan Video Drivers for PC Development

To make sure that you can visualize the rendering options Vulkan has available on your development PC, you will need to make sure you download and install the latest version of video card drivers for your graphics card. Below you will find the minimal driver version you need to use to be able to preview what Vulkan will look like on your development PC.

* [NVIDIA](http://www.nvidia.com/Download/index.aspx): 390.0 or later
* [AMD](https://support.amd.com/en-us/download): 17 or later

## Checking Vulkan Device Compatibility

Determining if your smartphone supports the Vulkan rendering API can be challenging due to the wide range of Android smartphones on the market. To help you quickly find out if your smartphone supports the Vulkan API, it is recommended to install the following program from Google Play Store: [Hardware Caps Viewer for Vulkan](https://play.google.com/store/apps/details).

The Vulkan Hardware Capability Viewer is a client tool aimed at developers needing to gather hardware implementation details for devices that support the new Vulkan Graphics API.

## Supported Vulkan Devices

The following devices have Vulkan-specific profiles available in addition to non-Vulkan profiles:

* Adreno 6xx
* Mali G72
* Mali G76
* Mali G77
* PowerVR GM9xxx
* Samsung XClipse series

If your device uses Android 9 or higher and you have Vulkan enabled as a feature level for your project, it will use the Vulkan-enabled version of these GPU families' device profiles.

Please note that the ability to use the Vulkan API depends on if your mobile carrier has released the Vulkain update for your specific device variant. To find if this support has been pushed to your mobile device, you will need to contact your mobile carrier.

## Building for Vulkan

To build a UE project that has support for the Vulkan API you will need to do the following:

1. Before you begin, make sure that you have your Android smartphone plugged into your development PC via USB and that your Android smartphone has developer mode enabled.
2. Launch the UE Editor and create a new project using the **Games > Blank** template using the following settings:

   * **Blueprint Project** enabled
   * **Mobile** enabled
   * **Maximum Quality** enabled
   * **Starter Content** disabled

   When that is completed, press the **Create** button to create and load the new project.

   [![Creating Project setup](https://dev.epicgames.com/community/api/documentation/image/45c991fc-4c5b-4b00-b197-364be970c63b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/45c991fc-4c5b-4b00-b197-364be970c63b?resizing_type=fit)

   Click image for full view.
3. Once the project has loaded, go to **Edit > Project Settings**, then under **Engine**, go to the **Rendering** section and make sure that **Mobile HDR** has been enabled under **VR**.

   [![Enable Mobile HDR option](https://dev.epicgames.com/community/api/documentation/image/2b043697-e1b2-42c3-bac9-269a3670fa0a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2b043697-e1b2-42c3-bac9-269a3670fa0a?resizing_type=fit)

   Click image for full view.
4. In the **Project Settings**, navigate to the **Platforms**, go to the **Android** section, make sure that the following options are enabled under **Build**:

   * **Support OpenGL ES3.2**
   * **Support Vulkan**

     [![Set Build options](https://dev.epicgames.com/community/api/documentation/image/70556b45-4900-426c-b240-d702a2f3398e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/70556b45-4900-426c-b240-d702a2f3398e?resizing_type=fit)

     Click image for full view.
5. From the menu bar, click on the **Platform** button, go to **Android**, make sure, that **Android(ASTC)** option is selected and click on **Package Project**.

   [![Launch packaging project process](https://dev.epicgames.com/community/api/documentation/image/2cb6b52d-ed55-43ac-be53-6aac57d72a04?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2cb6b52d-ed55-43ac-be53-6aac57d72a04?resizing_type=fit)
6. Select a location for UE to save the Android build and then press the **Select Folder** button to start the packaging process.

   [![Set packaging project folder](https://dev.epicgames.com/community/api/documentation/image/1ef49fcd-e8e5-48d4-88cf-f9cc16356727?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1ef49fcd-e8e5-48d4-88cf-f9cc16356727?resizing_type=fit)
7. When the packaging process has been completed, open up the folder that the packaged build was placed in. Inside this folder, you should see two `BAT` files. Locate the `BAT` file that has the word **Install** in the name and double-click on it to install it to your device.

   [![Launch installation to device](https://dev.epicgames.com/community/api/documentation/image/8ed525fa-3230-486e-a3e0-80b2367167cc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8ed525fa-3230-486e-a3e0-80b2367167cc?resizing_type=fit)
8. Once installed on your device, press on the UE icon that has your project name under it to launch the project on the device.

   [![Example of the project on device](https://dev.epicgames.com/community/api/documentation/image/7d8762ae-2ea2-4f53-966e-e32cdab0fcf3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7d8762ae-2ea2-4f53-966e-e32cdab0fcf3?resizing_type=fit)

   Click image for full view.

## Enabling Vulkan Preview Rendering in Editor

If you have enabled Vulkan in your project as described above, a preview rendering option will appear automatically. On the **Main Toolbar**, click on the **Settings** button and go to the **Preview Rendering Level** option. Select the **Android Vulkan** option to enable the Vulkan preview in the UE Viewport.

[![Set Preview Rendering Level](https://dev.epicgames.com/community/api/documentation/image/09e26a00-9fea-475c-9992-aee8d7fe2ab9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/09e26a00-9fea-475c-9992-aee8d7fe2ab9?resizing_type=fit)

The Viewport should read **Feature Level: Android Vulkan ES31** in the lower-right corner.

After doing this, the Editor will need to recompile the entire shader cache to include the required Vulkan options. Depending on the size of your project and power of your development computer, this process could take anywhere from a few minutes, to an hour or more to complete.

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [mobile](https://dev.epicgames.com/community/search?query=mobile)
* [android](https://dev.epicgames.com/community/search?query=android)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Vulkan Video Drivers for PC Development](/documentation/en-us/unreal-engine/using-the-android-vulkan-mobile-renderer-in-unreal-engine?application_version=5.7#vulkan-video-drivers-for-pc-development)
* [Checking Vulkan Device Compatibility](/documentation/en-us/unreal-engine/using-the-android-vulkan-mobile-renderer-in-unreal-engine?application_version=5.7#checking-vulkan-device-compatibility)
* [Supported Vulkan Devices](/documentation/en-us/unreal-engine/using-the-android-vulkan-mobile-renderer-in-unreal-engine?application_version=5.7#supported-vulkan-devices)
* [Building for Vulkan](/documentation/en-us/unreal-engine/using-the-android-vulkan-mobile-renderer-in-unreal-engine?application_version=5.7#building-for-vulkan)
* [Enabling Vulkan Preview Rendering in Editor](/documentation/en-us/unreal-engine/using-the-android-vulkan-mobile-renderer-in-unreal-engine?application_version=5.7#enabling-vulkan-preview-rendering-in-editor)
