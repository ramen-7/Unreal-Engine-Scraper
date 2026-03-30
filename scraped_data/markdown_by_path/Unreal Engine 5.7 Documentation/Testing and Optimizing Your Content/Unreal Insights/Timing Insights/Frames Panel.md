<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-frames-panel-in-unreal-insights-for-unreal-engine?application_version=5.7 -->

# Frames Panel

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
5. [Testing and Optimizing Your Content](/documentation/en-us/unreal-engine/testing-and-optimizing-your-content "Testing and Optimizing Your Content")
6. [Unreal Insights](/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine "Unreal Insights")
7. [Timing Insights](/documentation/en-us/unreal-engine/timing-insights-in-unreal-engine-5 "Timing Insights")
8. Frames Panel

# Frames Panel

View the CPU and GPU time used by your application on a frame-by-frame basis.

![Frames Panel](https://dev.epicgames.com/community/api/documentation/image/fe89825b-341a-4082-85b8-19102aecb0cf?resizing_type=fill&width=1920&height=335)

The **Frames** panel displays the total time taken by each frame using a bar graph format. This is useful for identifying general trends, such as low performance or framerate drops when a level is loaded, an unoptimized scene is visible, or spawning a large number of Actors simultaneously.

![The Frames Panel displayed in Unreal Insights.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/737e1ced-fd1e-43ac-b668-2559377f6bbb/main-image.png)

The frames panel displays the Frames, Timing, Timers, Callers, Callees, Counters, and Log tracks.

Hovering the cursor over a bar causes that frame's index and running time to appear.

![image alt text](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9a759e74-7752-4165-9b6a-1c13c48b72f1/frames-timeline.png)

If you right-click on on the bar, the following **Zoom** context menu options will appear:

![image alt text](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2499386a-ba05-4af0-a83e-7d42f5696230/zoom-options.png)

| **Option** | **Description** |
| --- | --- |
| **Auto Zoom** | Toggles auto zoom, which fits the entire session time range into the frames display window. |
| **Zoom Timing View on Frame Selection** | Toggles whether the timing view is zoomed when a frame is selected. |

These options are also available to edit in the UnrealInsightsSettings.ini file.

* [unreal insights](https://dev.epicgames.com/community/search?query=unreal%20insights)
* [timing insights](https://dev.epicgames.com/community/search?query=timing%20insights)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)
