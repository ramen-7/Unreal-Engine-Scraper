<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/frame-pacing-for-mobile-devices-in-unreal-engine?application_version=5.7 -->

# Frame Pacing for Mobile Devices

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
6. [Debugging and Optimization for Mobile](/documentation/en-us/unreal-engine/debugging-and-optimization-for-mobile-in-unreal-engine "Debugging and Optimization for Mobile")
7. Frame Pacing for Mobile Devices

# Frame Pacing for Mobile Devices

Enabling and customizing frame pacing for mobile devices

![Frame Pacing for Mobile Devices](https://dev.epicgames.com/community/api/documentation/image/caea1177-80ee-4339-9d63-a7be2c9e7d0c?resizing_type=fill&width=1920&height=335)

 On this page

**Frame Pacing** is a system that restricts an application to rendering frames at a lower framerate than a device's native refresh rate. This enables the application to prioritize consistency and stability in rendering, providing for a smoother user experience compared with letting the framerate run uncapped. **In Unreal Engine (UE),** frame pacing can be set on a per-device basis using the **Device Profiles** contained in your project's configs.

## Swappy Frame Pacing for Android

Unreal Engine integrates the [Swappy frame pacing library](https://developer.android.com/games/sdk/frame-pacing) from the **Android Game SDK**. This is an alternative to the legacy UE frame pacer that is used for all other hardware, and it is enabled by default in UE 5.2 and newer.

Android hardware normally uses a frame buffer to display past frames when late frame submissions are detected, which prevents screen tearing. However, games' renderers are often unaware of this process and out of synch with it, causing them to get ahead of the displayed frame. This causes the display time for frames to vary wildly and creates significant input latency with touchscreen controls, as stalls will usually occur after input has been sampled. Swappy is an Android-specific frame pacing solution designed to stabilize this behavior by enabling a game's render cycle and Android devices' refresh cycle to communicate more effectively.

### Enabling or Disabling Swappy

We recommend using Swappy over the legacy frame pacer. If you need to disable Swappy and use the legacy frame pacer instead, add a `UseSwappyForFramePacing=0` to the Android profiles you would like to use it. You can add it to `Android_Default` to activate it for all Android devices.

## Editing Frame Pacing Settings in Device Profiles

Frame pacing can be controlled through CVars in the `DeviceProfiles.ini` file containing your desired devices.

* For iOS devices, you can add device profiles under `[/Script/IOSRuntimeSettings.IOSRuntimeSettings]`
* For Android devices, you can add device profiles under `[/Script/AndroidRuntimeSettings.AndroidRuntimeSettings]`

The parameters that control frame pacing are as follows:

| Parameter | Usage | Description |
| --- | --- | --- |
| `FrameRateLock = [value]` | `FrameRateLock=True` | If set to true, allows any frame pacing. |
| `bEnableDynamicMaxFPS = [value]` | `bEnableDynamicMaxFPS=True` | If set to true, allows 120Hz on iOS devices. This has no effect on Android devices, which only need to call `r.setframepace`. |
| `r.setframepace [value]` | `r.setframepace 60` | Sets the refresh rate directly to the value provided. |
| `a.UseSwappyForFramePacing = [value]` | `a.UseSwappyForFramePacing=1` | Set to 1 by default. Setting this value to 0 will disable Google's Swappy frame pacing solution and use the standard UE frame pacer instead. Swappy uses the same CVars as the UE frame pacer. |

## Controlling Frame Pacing in C++

To control frame pacing in C++, you can call static functions from the `FPlatformRHIFramePacer` interface. Frame pace is passed as a 32-bit integer when used as a parameter in these functions.

`FPlatformRHIFramePacer::SupportsFramePace` checks whether the specified frame pace is compatible with the current device's refresh rate. `FPlatformRHIFramePacer::SetFramePace` sets the pace to a specified integer value, and `FPlatformRHIFramePacer::GetFramePace` returns the current frame pace.

* [performance](https://dev.epicgames.com/community/search?query=performance)
* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [optimization](https://dev.epicgames.com/community/search?query=optimization)
* [mobile](https://dev.epicgames.com/community/search?query=mobile)
* [ios](https://dev.epicgames.com/community/search?query=ios)
* [android](https://dev.epicgames.com/community/search?query=android)
* [swappy](https://dev.epicgames.com/community/search?query=swappy)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Swappy Frame Pacing for Android](/documentation/en-us/unreal-engine/frame-pacing-for-mobile-devices-in-unreal-engine?application_version=5.7#swappyframepacingforandroid)
* [Enabling or Disabling Swappy](/documentation/en-us/unreal-engine/frame-pacing-for-mobile-devices-in-unreal-engine?application_version=5.7#enablingordisablingswappy)
* [Editing Frame Pacing Settings in Device Profiles](/documentation/en-us/unreal-engine/frame-pacing-for-mobile-devices-in-unreal-engine?application_version=5.7#editingframepacingsettingsindeviceprofiles)
* [Controlling Frame Pacing in C++](/documentation/en-us/unreal-engine/frame-pacing-for-mobile-devices-in-unreal-engine?application_version=5.7#controllingframepacinginc++)

Related documents

[Configuration Files

![Configuration Files](https://dev.epicgames.com/community/api/documentation/image/13593a96-0a11-4ff0-9062-ff267596caea?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/configuration-files-in-unreal-engine)
