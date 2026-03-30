<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/capturing-data-with-chaos-visual-debugger?application_version=5.7 -->

# Capturing Data with Chaos Visual Debugger

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
5. [Gameplay Systems](/documentation/en-us/unreal-engine/gameplay-systems-in-unreal-engine "Gameplay Systems")
6. [Physics](/documentation/en-us/unreal-engine/physics-in-unreal-engine "Physics")
7. [Chaos Visual Debugger](/documentation/en-us/unreal-engine/chaos-visual-debugger-in-unreal-engine "Chaos Visual Debugger")
8. Capturing Data with Chaos Visual Debugger

# Capturing Data with Chaos Visual Debugger

Capture and play back recordings with Chaos Visual Debugger.

![Capturing Data with Chaos Visual Debugger](https://dev.epicgames.com/community/api/documentation/image/d829671a-0bfb-47fe-9916-c11f67dfa982?resizing_type=fill&width=1920&height=335)

 On this page

In the following tutorials, you’ll use **[Chaos Visual Debugger](https://dev.epicgames.com/documentation/en-us/unreal-engine/chaos-visual-debugger-in-unreal-engine)** (**CVD**) to capture and play back recordings for targets on local or remote machines, including:

* Game clients and servers
* Packaged builds
* Play-in-editor sessions

[![CVD Capture City Sample](https://dev.epicgames.com/community/api/documentation/image/97c3aa7c-65a2-4180-bdaf-3cc595369703?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/97c3aa7c-65a2-4180-bdaf-3cc595369703?resizing_type=fit)

## Data Channels

CVD records a considerable amount of data from several systems. The more complex a scene is, the larger the CVD file becomes — which can impact performance. To manage file size, you can opt-out of recording certain data by toggling the **data channels**.

Data channels control which simulation stages or data visualization flags that CVD records.

To toggle data channels, click **Data Channels** in the main toolbar and check the desired channels.

[![Toggle Data Channels](https://dev.epicgames.com/community/api/documentation/image/3a33e243-344b-44af-9250-d54218ee1c69?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3a33e243-344b-44af-9250-d54218ee1c69?resizing_type=fit)

Recording in CVD requires access to the console, such as in the **Test** or **Development** build configurations. When using the Test configuration, the CVD outliner does not display objects’ debug names. For more information on build configurations, see [Packaging Unreal Engine Projects](https://dev.epicgames.com/documentation/en-us/unreal-engine/packaging-your-project).

## Session Targets

CVD describes the application or editor that you intend to record (such as a game client, game server, packaged build, or a PIE session) as a **target**. With the exception of PIE sessions, you can record one or more targets at a time, referred to as **single** or **multiple** sources.

The **Session Target** dropdown menu provides target presets to choose from when preparing to record, but you can also specify a custom target. By default, this menu is set to Local Editor — meaning that if you intend to record a local PIE session, you can leave this as is.

[![Session Targets](https://dev.epicgames.com/community/api/documentation/image/0a319755-1a43-481b-bb68-6e03163c324e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0a319755-1a43-481b-bb68-6e03163c324e?resizing_type=fit)

| Target | Description | Source Amount |
| --- | --- | --- |
| **Local Editor** | Records a local PIE session. | Single |
| **All Remote** | Records all instances that are not the Editor. | Multiple |
| **All Remote Servers** | Records all game servers that are not the Editor. | Multiple |
| **All Remote Clients** | Records all game clients that are not the Editor. | Multiple |
| **All** | Records all available targets. | Multiple |
| **Custom Selection** | Records a custom target or targets. | Single or Multiple |

Recording multiple targets is useful if you are already recording a game server and game client, and need to record an additional client.

## Next Up

* [![Recording to File](https://dev.epicgames.com/community/api/documentation/image/c6586e65-2b47-4ae3-b63c-f187268d22c3?resizing_type=fit&width=640&height=640)

  Recording to File

  Record to file with Chaos Visual Debugger](https://dev.epicgames.com/documentation/en-us/unreal-engine/recording-to-file)

* [![Recording a Live Session](https://dev.epicgames.com/community/api/documentation/image/611a2540-a88b-4a2d-9044-78c3cb86d61d?resizing_type=fit&width=640&height=640)

  Recording a Live Session

  Record a live session with Chaos Visual Debugger](https://dev.epicgames.com/documentation/en-us/unreal-engine/live-debugging-with-chaos-visual-debugger)

* [![Playback in Chaos Visual Debugger](https://dev.epicgames.com/community/api/documentation/image/118531b5-4316-4ac7-a933-abe744980883?resizing_type=fit&width=640&height=640)

  Playback in Chaos Visual Debugger

  Play back recordings in Chaos Visual Debugger.](https://dev.epicgames.com/documentation/en-us/unreal-engine/playback-in-chaos-visual-debugger)

* [chaos visual debugger](https://dev.epicgames.com/community/search?query=chaos%20visual%20debugger)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Data Channels](/documentation/en-us/unreal-engine/capturing-data-with-chaos-visual-debugger?application_version=5.7#datachannels)
* [Session Targets](/documentation/en-us/unreal-engine/capturing-data-with-chaos-visual-debugger?application_version=5.7#sessiontargets)
* [Next Up](/documentation/en-us/unreal-engine/capturing-data-with-chaos-visual-debugger?application_version=5.7#nextup)
