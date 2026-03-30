<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/multi-process-rendering-with-unreal-engine?application_version=5.7 -->

# Multi-Process Rendering

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
7. [Rendering to Multiple Displays with nDisplay](/documentation/en-us/unreal-engine/rendering-to-multiple-displays-with-ndisplay-in-unreal-engine "Rendering to Multiple Displays with nDisplay")
8. Multi-Process Rendering

# Multi-Process Rendering

Learn about multi-process rendering and how it differs from multi-GPU rendering.

![Multi-Process Rendering](https://dev.epicgames.com/community/api/documentation/image/bea1353a-71aa-456d-9c1a-57b74d0f1716?resizing_type=fill&width=1920&height=335)

 On this page

## What is Multi-Process Rendering?

**Multi-Process Rendering** is a method of utilizing the power of multiple GPUs for nDisplay rendering. This approach allows specific viewports to be rendered simultaneously on each GPU. For example, the outer frustum could be rendered on the primary GPU while the inner frustum is rendered on a secondary GPU.

In the vast majority of cases (scene dependent), Multi-Process rendering is more performant than Multi-GPU rendering, which was introduced in 4.27. Multi-Process and Multi-GPU share the same physical hardware configuration, so there is no disadvantage to switching to a Multi-Process workflow. Multi-Process is also the recommended way to render with multiple NVIDIA [ADA Lovelace](https://en.wikipedia.org/wiki/Ada_Lovelace) GPUs, as they do not support NVLink which is recommended for Multi-GPU (mGPU) configurations.

As the name implies, Multi-Process rendering launches two instances, or processes, of Unreal Engine on each render node. The first is a regular nDisplay node. This is also known as the **onscreen node** because it renders out to the LED wall and is visible in Windows when rendering. The second node, which operates as a separate Windows process, is a headless instance that is not directly visible and is referred to as the **offscreen node**.

In the frustum example above, the offscreen node will render the inner frustum on the secondary GPU, sharing it back to the onscreen node as a texture. The onscreen node, which is rendering on the primary GPU, composites the inner frustum over the outer frustum and displays it out to the LED wall.

Multi-Process will only share the final rendered texture between GPUs via CPU/Motherboard. Sharing the rendered texture is more efficient than Multi-GPU, which requires huge bandwidth to share all GPU memory via the NVLink and SLI.

The two methods can be compared in the following table:

![comparison table](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b364c5d8-7201-4823-bfbe-551aa959f759/table.png)

## Technical Prerequisites

* At least **two GPUs**
* **SLI must be disabled** ([see Nvidia documentation](https://www.nvidia.com/content/Control-Panel-Help/vLatest/en-us/index.htm) for configuring SLI)
* If using Nvidia Mosaic, ensure that it is not set to Premium Mosaic, as this enables SLI
* **Disable Intel Hyper-Threading / AMD Simultaneous Multi-Threading.** We recommend doing this to ensure the best performance. Please note that disabling either of these may impact performance for other software you are using. You may experience longer shader compile times.
* The currently supported NVIDIA drivers and control panel settings, including synchronization. This information can be found on our [nDisplay Synchronisation with NVIDIA GPUs page](/documentation/en-us/unreal-engine/synchronization-in-ndisplay-in-unreal-engine).

## Knowledge Prerequisites

* Familiar with the concepts in the [ICVFX quickstart guide](/documentation/en-us/unreal-engine/in-camera-vfx-quick-start-for-unreal-engine), including how to create a new config.

## Additional Topics

[![Getting Started with Multi-Process Rendering](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f05c6127-a1bb-4c57-8b72-f8ea9e222cea/placeholder_topic.png)

Getting Started with Multi-Process Rendering

Learn how to set up multi-process rendering.](/documentation/en-us/unreal-engine/getting-started-with-multi-process-rendering-in-unreal-engine)
[![Converting from mGPU to Multi-Processing Rendering](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4f068c53-49d1-4c0b-bad2-42af152c1fb5/placeholder_topic.png)

Converting from mGPU to Multi-Processing Rendering

Convert an existing multi-GPU config for multi-process rendering.](/documentation/en-us/unreal-engine/converting-from-mgpu-to-multi-process-rendering-in-unreal-engine)

## Useful Links

* [NVIDIA Documentation](https://nvidia.com/content/Control-Panel-Help/vLatest/en-us/index.htm)
* [nDisplay Synchronization with NVIDIA GPUs](/documentation/en-us/unreal-engine/synchronization-in-ndisplay-in-unreal-engine)
* [In-Camera VFX Quick Start](/documentation/en-us/unreal-engine/in-camera-vfx-quick-start-for-unreal-engine)

* [ndisplay](https://dev.epicgames.com/community/search?query=ndisplay)
* [icvfx](https://dev.epicgames.com/community/search?query=icvfx)
* [bronze](https://dev.epicgames.com/community/search?query=bronze)
* [multi-process rendering](https://dev.epicgames.com/community/search?query=multi-process%20rendering)
* [mgpu](https://dev.epicgames.com/community/search?query=mgpu)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [What is Multi-Process Rendering?](/documentation/en-us/unreal-engine/multi-process-rendering-with-unreal-engine?application_version=5.7#whatismulti-processrendering?)
* [Technical Prerequisites](/documentation/en-us/unreal-engine/multi-process-rendering-with-unreal-engine?application_version=5.7#technicalprerequisites)
* [Knowledge Prerequisites](/documentation/en-us/unreal-engine/multi-process-rendering-with-unreal-engine?application_version=5.7#knowledgeprerequisites)
* [Additional Topics](/documentation/en-us/unreal-engine/multi-process-rendering-with-unreal-engine?application_version=5.7#additionaltopics)
* [Useful Links](/documentation/en-us/unreal-engine/multi-process-rendering-with-unreal-engine?application_version=5.7#usefullinks)
