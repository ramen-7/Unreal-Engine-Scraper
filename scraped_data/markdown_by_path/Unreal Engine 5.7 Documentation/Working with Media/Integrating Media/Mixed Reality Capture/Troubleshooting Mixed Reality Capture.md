<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/troubleshooting-mixed-reality-capture-in-unreal-engine?application_version=5.7 -->

# Troubleshooting Mixed Reality Capture

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
5. [Working with Media](/documentation/en-us/unreal-engine/working-with-media-in-unreal-engine "Working with Media")
6. [Integrating Media](/documentation/en-us/unreal-engine/integrating-media-in-unreal-engine "Integrating Media")
7. [Mixed Reality Capture](/documentation/en-us/unreal-engine/mixed-reality-capture-in-unreal-engine "Mixed Reality Capture")
8. Troubleshooting Mixed Reality Capture

# Troubleshooting Mixed Reality Capture

Troubleshooting tips when working with Mixed Reality Capture.

![Troubleshooting Mixed Reality Capture](https://dev.epicgames.com/community/api/documentation/image/8e7aba6c-f9bf-4b32-9a4d-4aeae2a0ed43?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

This page provides troubleshooting information for Mixed Reality Capture (MRC).

## Flickering During Captures

Depending on the resolution of the MR capture target (the default is 1080p), your app may be constrained by its render target pool size. By default, render targets are set to reallocate as needed, which can lead to ping-ponging and flickering as the MR capture targets fight with the stereo render targets. (shown in the video below)

If you see this kind of behavior, you can change the render target resize rule to 'Grow' (in your engine.ini file, set *r.SceneRenderTargetResizeMethod=2*). Making this change should resolve the issue.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/08dd5788-bbb6-4f99-96ef-74c753d0cc06/mr_captureflicker.gif)

## Capture Not Displaying on Spectator Screen

The MRC framework uses the [Virtual Reality Spectator Screen](/documentation/en-us/unreal-engine/virtual-reality-spectator-screen-in-unreal-engine) to display the composited scene. This means the Mixed Reality capture will only be displayed when running in Virtual Reality. If your project also uses the spectator screen, then you need to conditionally guard where you use them. There are MRC methods to help with this:

**Get Mixed Reality Capture Texture**  
Returns the Capture Texture, or a nullptr if there isn't one.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/25e0d3ac-a8d0-43a5-ab6f-bc8f0de5613e/01-get-mixed-reality_ue5.png "01-get-mixed-reality_ue5.png")

**Is Mixed Reality Capture Broadcasting**  
Returns true, if the system is sending the capture texture to the spectator screen.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/269eb38f-f02d-4955-a4db-6d7f57bea11e/02-is-mixed-reality_ue5.png "02-is-mixed-reality_ue5.png")

**Set Mixed Reality Capture Broadcasting**  
Toggles whether the capture system is sending the capture texture to the spectator screen or not.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8494d0fc-f944-4c7a-9db6-594668447424/03-set-mixed-reality_ue5.png "03-set-mixed-reality_ue5.png")

**An Example of Using the MRC Methods**

[![04-bleprint-example_ue5.png](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/92a3dddd-366b-4738-87ab-fe7f0a4f39a2/04-bleprint-example_ue5.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/92a3dddd-366b-4738-87ab-fe7f0a4f39a2/04-bleprint-example_ue5.png)

Click image to expand.

## Controller/Trigger Not Responding During Calibration

If your controller input does not appear to respond during calibration, below are several possible causes.

* **The headset sensor in not covered.** If theheadset's sensor is not covered, the controllers may not be active.
* **The application window needs to have focus.** If theMRCalibration window is not the current active window, the controller actions may not be captured by the calibration program.
* **The Oculus system may not be configured to run from Unknown Sources.** As a part of Beta access, the calibration program is still in active development and has not been reviewed by Oculus.

  ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/98c459c9-2d32-4071-a38b-47fb5003bb80/mr_oculusunknownsourcessetting.png "MR_OculusUnknownSourcesSetting.png")

* [beta](https://dev.epicgames.com/community/search?query=beta)
* [mr](https://dev.epicgames.com/community/search?query=mr)
* [landingpage](https://dev.epicgames.com/community/search?query=landingpage)
* [troubleshooting](https://dev.epicgames.com/community/search?query=troubleshooting)
* [ar/vr/xr](https://dev.epicgames.com/community/search?query=ar%2Fvr%2Fxr)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Flickering During Captures](/documentation/en-us/unreal-engine/troubleshooting-mixed-reality-capture-in-unreal-engine?application_version=5.7#flickeringduringcaptures)
* [Capture Not Displaying on Spectator Screen](/documentation/en-us/unreal-engine/troubleshooting-mixed-reality-capture-in-unreal-engine?application_version=5.7#capturenotdisplayingonspectatorscreen)
* [Controller/Trigger Not Responding During Calibration](/documentation/en-us/unreal-engine/troubleshooting-mixed-reality-capture-in-unreal-engine?application_version=5.7#controller/triggernotrespondingduringcalibration)
