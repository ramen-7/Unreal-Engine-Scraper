<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/steamvr-command-reference-in-unreal-engine?application_version=5.7 -->

# SteamVR Command Reference

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
8. [Developing for SteamVR](/documentation/en-us/unreal-engine/developing-for-steamvr-in-unreal-engine "Developing for SteamVR")
9. SteamVR Command Reference

# SteamVR Command Reference

Information on the various commands you can use with SteamVR.

![SteamVR Command Reference](https://dev.epicgames.com/community/api/documentation/image/7dccfa27-0bc1-4942-87e3-d4b9e2d0adaa?resizing_type=fill&width=1920&height=335)

Below you will find various Console commands that can be used to adjust the way Unreal Engine and SteamVR interact with one another.

| Command | Description |
| --- | --- |
| **vr.SteamVR.AdaptiveDebugGPUTime** | Added to the the GPU frame timing, in ms, for testing. |
| **vr.SteamVR.AdaptiveGPUTimeThreshold** | Time, in ms, to aim for stabilizing the GPU frame time at. |
| **vr.SteamVR.PixelDensityAdaptiveDebugCycle** | If non-zero, the adaptive pixel density will cycle from max to min pixel density, and then jump to max. |
| **vr.SteamVR.PixelDensityAdaptiveDebugOutput** | If non-zero, the adaptive pixel density will print debugging info to the log. |
| **vr.SteamVR.PixelDensityAdaptivePostProcess** | If non-zero, when the adaptive density changes, we'll disable Temporal Anti-Aliasing (TAA) for a few frames to clear the buffers. |
| **vr.SteamVR.PixelDensityMax** | Maximum pixel density, as a float. |
| **vr.SteamVR.PixelDensityMin** | Minimum pixel density, as a float. |
| **vr.SteamVR.ShowDebug** | If non-zero, will draw debugging info to the canvas. |
| **vr.SteamVR.UsePostPresentHandoff** | Whether or not to use PostPresentHandoff. If true, more GPU time will be available, but this relies on no SceneCaptureComponent2D or WidgetComponents being active in the scene. Otherwise, it will break async re-projection. |
| **vr.SteamVR.UseVisibleAreaMesh** | If non-zero, SteamVR will use the visible area mesh in addition to the hidden area mesh optimization. This may be problematic on beta versions of platforms. |

* [vr](https://dev.epicgames.com/community/search?query=vr)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

Related documents

[Virtual Reality Spectator Screen

![Virtual Reality Spectator Screen](https://dev.epicgames.com/community/api/documentation/image/577d577c-78a8-4a8b-9bf7-bebb6b4217ce?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/virtual-reality-spectator-screen-in-unreal-engine)
