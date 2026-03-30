<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/rift-command-reference-in-unreal-engine?application_version=5.7 -->

# Rift Command Reference

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
8. [Developing for Oculus](/documentation/en-us/unreal-engine/developing-for-oculus-in-unreal-engine "Developing for Oculus")
9. [Oculus Rift](/documentation/en-us/unreal-engine/oculus-rift-in-unreal-engine "Oculus Rift")
10. Rift Command Reference

# Rift Command Reference

Information on the various commands you can use with the Rift.

![Rift Command Reference](https://dev.epicgames.com/community/api/documentation/image/9ae6522e-f344-4f9c-bbff-1337fa9525f9?resizing_type=fill&width=1920&height=335)

Below you will find various INI and Console commands that can be used to adjust the way UE4 and the Oculus Rift interact with one another.

| Command | Description |
| --- | --- |
| **vr.oculus.bHQBuffer** | Enable or disable using floating point texture format for the eye layer. |
| **vr.oculus.bHQBuffer** | Enable or disable using multiple mipmap levels for the eye layer. |
| **vr.oculus.bUpdateOnRenderThread** | Enables or disables updating on the render thread. |
| **vr.oculus.Debug.bShowStats** | Enable or disable rendering of stats. |
| **vr.oculus.Debug.CaptureCubemap** | Captures a cubemap for Oculus Home. Optional arguments (default is zero for all numeric arguments) :xoff= -X axis offset from the origin yoff= -Y axis offset zoff=-Z axis offsetyaw= -- the direction to look into (roll and pitch is fixed to zero) gearvr -- Generate a GearVR format cubemap (height of the captured cubemap will be 1024 instead of 2048 pixels). |
| **vr.oculus.Debug.EnforceHeadTracking** | Set to on to enforce head tracking even when not in stereo mode. |
| **vr.oculus.Debug.FCP** | Shows or overrides the current far clipping plane. |
| **vr.oculus.Debug.IPD** | Shows or changes the current interpupillary distance in meters. |
| **vr.oculus.Debug.NCP** | Shows or overrides the current near clipping plane. |
| **vr.oculus.Debug.Reset** | Resets various stereo rendering parameters back to the original setting. |
| **vr.oculus.Debug.Show** | Shows the current value of various stereo rendering parameters. |
| **vr.oculus.PixelDensity** | Pixel density sets the render target texture size as a factor of recommended texture size. Since this may be slighly larger than the native resolution, setting PixelDensity to 1.0 is usually not the same as setting r.ScreenPercentage to 100 |
| **vr.oculus.PixelDensity.adaptive** | Enable or disable adaptive pixel density. |
| **vr.oculus.PixelDensity.max** | Maximum pixel density when adaptive pixel density is enabled. |
| **vr.oculus.PixelDensity.min** | Minimum pixel density when adaptive pixel density is enabled. |
| **vr.oculus.ShowGlobalMenu** | Opens the global menu. |
| **vr.oculus.ShowQuitMenu** | Opens the quit menu. |
| **vr.oculus.Stress.CPU** | Initiates a CPU stress test. Usage: vr.oculus.Stress.CPU [PerFrameTime [TotalTimeLimit]] |
| **vr.oculus.Stress.GPU** | Initiates a GPU stress test. Usage: vr.oculus.Stress.GPU [LoadMultiplier [TimeLimit]] |
| **vr.oculus.Stress.PD** | Initiates a pixel density stress test wher pixel density is changed every frame for TotalTimeLimit seconds. Usage: vr.oculus.Stress.PD [TotalTimeLimit] |
| **vr.oculus.Stress.Reset** | Resets the stress tester and stops all currently running stress tests. Usage: vr.oculus.Stress.Reset |

* [vr](https://dev.epicgames.com/community/search?query=vr)
* [platform](https://dev.epicgames.com/community/search?query=platform)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)
