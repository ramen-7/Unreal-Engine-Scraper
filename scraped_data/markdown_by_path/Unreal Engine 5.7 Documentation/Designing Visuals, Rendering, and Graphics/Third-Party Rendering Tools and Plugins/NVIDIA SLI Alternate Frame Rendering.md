<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/nvidia-sli-alternative-frame-rendering-in-unreal-engine?application_version=5.7 -->

# NVIDIA SLI Alternate Frame Rendering

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
5. [Designing Visuals, Rendering, and Graphics](/documentation/en-us/unreal-engine/designing-visuals-rendering-and-graphics-with-unreal-engine "Designing Visuals, Rendering, and Graphics")
6. [Third-Party Rendering Tools and Plugins](/documentation/en-us/unreal-engine/third-party-rendering-tools-and-plugins-in-unreal-engine "Third-Party Rendering Tools and Plugins")
7. NVIDIA SLI Alternate Frame Rendering

# NVIDIA SLI Alternate Frame Rendering

Integration of NVIDIA's Alternate Frame Rendering technology that enables support for games using multiple GPUs with SLI.

![NVIDIA SLI Alternate Frame Rendering](https://dev.epicgames.com/community/api/documentation/image/a2fe9025-f4a2-4627-80b6-2e44ef483054?resizing_type=fill&width=1920&height=335)

 On this page

Unreal Engine supports NVIDIA's **Alternate Frame Rendering** (AFR) for packaged games running on NVIDIA SLI configurations. Alternate Frame Rendering works by alternating frames between the linked GPUs. One frame is rendered by GPU 1 with the next frame rendered by GPU 2, before repeating the procress. Using this method, image quality and performance are improved by using multiple GPUs on a single monitor.

Projects that intend to ship with support for Alternate Frame Rendering will need to work directly with NVIDIA to test their games and have it automatically switch over to use this functionality where possible.

For additional details, see NVIDIA documentation on their [SLI modes, specifically Alternate Frame Rendering](https://docs.nvidia.com/gameworks/content/technologies/desktop/sli.htm) here.

## Forcefully Enabling Alternate Frame Rendering

NVIDIA Control Panel allows for some applications to be manually added which support AFR forcibly enabling the SLI rendering mode. Add applications to the NVIDIA Control Panel using the following steps.

1. Open the **NVIDIA Control Panel** from your task tray, and navigate to **Manage 3D Settings**.
2. Click on the **Program Settings** tab. Under **Select a program to cumstomize** use the dropdown to select the program you want to add.
3. Next to **SLI Rendering Mode**, select **Force Alternate Frame Rendering**.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d9fa2579-26e5-43b3-9abb-9711f387272b/afrsetting.jpg)


This feature is not guaranteed to improve the quality or performance of your applications. It is not intended for use with the Unreal Engine Editor, specifically. Should to want this for your developed and released project, you will need to talk with NVIDIA directly to set up this functionality with their drivers.

* [plugins](https://dev.epicgames.com/community/search?query=plugins)
* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [lighting](https://dev.epicgames.com/community/search?query=lighting)
* [nvidia](https://dev.epicgames.com/community/search?query=nvidia)
* [third-party](https://dev.epicgames.com/community/search?query=third-party)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Forcefully Enabling Alternate Frame Rendering](/documentation/en-us/unreal-engine/nvidia-sli-alternative-frame-rendering-in-unreal-engine?application_version=5.7#forcefullyenablingalternateframerendering)
