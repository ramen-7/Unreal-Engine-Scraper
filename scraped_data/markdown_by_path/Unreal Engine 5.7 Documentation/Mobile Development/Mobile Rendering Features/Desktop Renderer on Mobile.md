<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-desktop-renderer-on-mobile-in-unreal-engine?application_version=5.7 -->

# Desktop Renderer on Mobile

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
6. [Mobile Rendering Features](/documentation/en-us/unreal-engine/rendering-features-for-mobile-games-in-unreal-engine "Mobile Rendering Features")
7. Desktop Renderer on Mobile

# Desktop Renderer on Mobile

An overview of the Desktop Renderer for Mobile devices.

![Desktop Renderer on Mobile](https://dev.epicgames.com/community/api/documentation/image/5e30b51e-3766-47b1-b876-c8c35bc820ca?resizing_type=fill&width=1920&height=335)

Learn to use this **Experimental** feature, but use caution when shipping with it.

 On this page

Unreal Engine (UE) provides support for both the forward and deferred desktop renderers for iOS devices and Android devices using Vulkan. This uses the same rendering path as PC and console platforms.

The iOS implementation of the desktop renderer is considered Beta in terms of feature readiness. The Android Vulkan implementation is considered experimental.

## How to Enable the Desktop Renderer on Mobile

The sections below provide instructions on how to enable the desktop renderer on iOS and Android.

### iOS/tvOS/iPadOS

To enable the desktop renderer for iOS, follow these steps:

1. Open your **Project Settings**.
2. Navigate to **Platforms** > **iOS** > **Rendering**.
3. Enable **Metal Desktop Renderer**.

### Android Vulkan

To enable the desktop renderer for Android Vulkan, follow these steps:

1. Open your **Project Settings**.
2. navigate to **Platforms** > **Android** > **Build**.
3. Enable **Support Vulkan Desktop [Experimental]**.
4. Set r.Android.DisableVulkanSupport` to 0 to ensure that Android Vulkan is enabled.
5. Set `r.Android.DisableVulkanSM5Support` to `0` to allow the use of Shader Model 5 (SM5).

### Finalize Settings and Configure Desktop Renderer

You must restart the Unreal Editor for your changes to take effect. You can then configure forward and deferred rendering features the same way you would in a desktop application.

## Device Compatibility

The desktop renderer is only available for mobile devices that can use shader model 5 (SM5).

## Benefits

The desktop renderer provides access to high-fidelity rendering consistent with desktops and game consoles.

## Drawbacks

The desktop renderer has a high resource cost compared with the mobile forward and mobile deferred shading paths, and most mobile hardware isn't set up in such a way to run it efficiently.

## When to Use the Desktop Renderer

The desktop renderer is considered beta on iOS and experimental on Android Vulkan. We do not recommend using it for shipped projects, but welcome any feedback if you decide to experiment with it.

* [experimental](https://dev.epicgames.com/community/search?query=experimental)
* [mobile](https://dev.epicgames.com/community/search?query=mobile)
* [mobile rendering](https://dev.epicgames.com/community/search?query=mobile%20rendering)
* [desktop renderer](https://dev.epicgames.com/community/search?query=desktop%20renderer)
* [desktop renderer on mobile](https://dev.epicgames.com/community/search?query=desktop%20renderer%20on%20mobile)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [How to Enable the Desktop Renderer on Mobile](/documentation/en-us/unreal-engine/using-the-desktop-renderer-on-mobile-in-unreal-engine?application_version=5.7#howtoenablethedesktoprendereronmobile)
* [iOS/tvOS/iPadOS](/documentation/en-us/unreal-engine/using-the-desktop-renderer-on-mobile-in-unreal-engine?application_version=5.7#ios/tvos/ipados)
* [Android Vulkan](/documentation/en-us/unreal-engine/using-the-desktop-renderer-on-mobile-in-unreal-engine?application_version=5.7#androidvulkan)
* [Finalize Settings and Configure Desktop Renderer](/documentation/en-us/unreal-engine/using-the-desktop-renderer-on-mobile-in-unreal-engine?application_version=5.7#finalizesettingsandconfiguredesktoprenderer)
* [Device Compatibility](/documentation/en-us/unreal-engine/using-the-desktop-renderer-on-mobile-in-unreal-engine?application_version=5.7#devicecompatibility)
* [Benefits](/documentation/en-us/unreal-engine/using-the-desktop-renderer-on-mobile-in-unreal-engine?application_version=5.7#benefits)
* [Drawbacks](/documentation/en-us/unreal-engine/using-the-desktop-renderer-on-mobile-in-unreal-engine?application_version=5.7#drawbacks)
* [When to Use the Desktop Renderer](/documentation/en-us/unreal-engine/using-the-desktop-renderer-on-mobile-in-unreal-engine?application_version=5.7#whentousethedesktoprenderer)
