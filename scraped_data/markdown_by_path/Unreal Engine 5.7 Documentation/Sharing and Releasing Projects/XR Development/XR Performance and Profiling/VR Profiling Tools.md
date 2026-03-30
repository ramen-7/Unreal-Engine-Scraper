<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/vr-profiling-tools-in-unreal-engine?application_version=5.7 -->

# VR Profiling Tools

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
7. [XR Performance and Profiling](/documentation/en-us/unreal-engine/xr-performance-and-profiling-in-unreal-engine "XR Performance and Profiling")
8. VR Profiling Tools

# VR Profiling Tools

Internal and external tools you can use for profiling your Unreal Engine VR project

![VR Profiling Tools](https://dev.epicgames.com/community/api/documentation/image/2b55bd5d-ad1d-465f-8128-d168cdc99307?resizing_type=fill&width=1920&height=335)

 On this page

This page contains information about profilng tools specifically designed for VR projects and devices. For general performance troubleshooting and information, you can use [Unreal Insights](/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine) to gather details about the performance of your project.

## Oculus Performance Head-Up Display

Oculus Performance Head-Up Display is a tool that can be used to display performance information, whether in the editor or a packaged build. This tool will help verify the actual CPU and GPU timings, excluding any throttling done by the application. For an overview of the screens and what the values mean, refer to Oculus' [documentation](https://developer.oculus.com/documentation/native/pc/dg-hud).

In general, you'll want to look at the graphs and values on the **Application Render Timing** screen. These will give you the CPU and GPU timings as the Oculus compositor sees them, and will be more accurate for Draw and GPU timings.

To use Oculus PerfHud with Unreal Engine, you will need to do the following:

1. First, go to `C:\Program Files\Oculus\Support\oculus-diagnostics` and locate the **OculusDebugTool.exe**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e1e0c0e8-11e9-4e38-86fd-71e103ba0f8a/odt_01.png)
2. Double - click on the OculusDebugTool.exe to open it up and set the **Visible HUD** to the **Performance** option.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1d46da52-d7d5-46e4-b5ff-753087e3fea1/odt_02.png)
3. Now launch your project and put your Oculus Rift HMD on and you will see the performance information related to your UE project being displayed on the Rift. To change what type of information is displayed, you will need to change what is input into the Visible HUD option like in the image below.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9ad5cf26-9bd5-45af-bf09-5ae5c6556cdb/oculus_perf_hud.jpg)

## SteamVR Frame Timing Tool

The SteamVR Frame Timing Tool lets you see how your VR project is performing in both the Editor or in a packaged build. This tool will help verify the actual CPU and GPU timings, excluding any throttling done by the application. For an overview of how to open the tool as well as what all of the values relate to, refer to the [Valve Developer Community](https://developer.valvesoftware.com/wiki/SteamVR/Frame_Timing) page. Please note that there is nothing inside of UE that needs to be done in order for the SteamVR Frame Timing tools to work. All of the functionality is provided by the SteamVR Application.

## RenderDoc

RenderDoc is an external tool you can also use for profiling Unreal Engine projects. To use it with Unreal Engine:

1. Download the latest [RenderDoc](https://renderdoc.org/builds).
2. In RenderDoc, configure it to launch your game (e.g. UE5Editor.exe, with appropriate command line arguments).
3. Run `ToggleDrawEvents` from the command line of your app to get human readable events.
4. Press F12 to capture a frame.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Oculus Performance Head-Up Display](/documentation/en-us/unreal-engine/vr-profiling-tools-in-unreal-engine?application_version=5.7#oculusperformancehead-updisplay)
* [SteamVR Frame Timing Tool](/documentation/en-us/unreal-engine/vr-profiling-tools-in-unreal-engine?application_version=5.7#steamvrframetimingtool)
* [RenderDoc](/documentation/en-us/unreal-engine/vr-profiling-tools-in-unreal-engine?application_version=5.7#renderdoc)
