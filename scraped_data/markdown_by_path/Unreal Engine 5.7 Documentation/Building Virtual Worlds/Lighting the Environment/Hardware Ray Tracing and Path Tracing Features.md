<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/ray-tracing-and-path-tracing-features-in-unreal-engine?application_version=5.7 -->

# Hardware Ray Tracing and Path Tracing Features

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
5. [Building Virtual Worlds](/documentation/en-us/unreal-engine/building-virtual-worlds-in-unreal-engine "Building Virtual Worlds")
6. [Lighting the Environment](/documentation/en-us/unreal-engine/lighting-the-environment-in-unreal-engine "Lighting the Environment")
7. Hardware Ray Tracing and Path Tracing Features

# Hardware Ray Tracing and Path Tracing Features

Explore topics for setting up and using real-time hardware ray tracing and path tracing to render scenes using ray-traced lighting features.

![Hardware Ray Tracing and Path Tracing Features](https://dev.epicgames.com/community/api/documentation/image/4e481ec0-0f86-45cf-b046-b71d2779adef?resizing_type=fill&width=1920&height=335)

 On this page

Ray Tracing techniques have long been used in film, television, and visualization for rendering photo-realistic images, but often it required powerful computers and time to render individual images (or frames). For architectural visualization, this can often mean hours of rendering. For film and television, it can take many hours or even days to render high-quality image sequences.

Unreal Engine uses its own ray tracing code base that is shared with both its real-time and offline rendering paths. Real-Time Ray Tracing is an optimized path to work in real-time to render scenes, such as interactive experiences or in games. The offline path uses the built-in Path Tracer to generate uncompromised renderings of scenes. It works seamlessly with the [Movie Render Queue](https://dev.epicgames.com/documentation/en-us/unreal-engine/movie-render-pipeline-in-unreal-engine?application_version=5.5#movie-render-queue) to output the highest quality frame renders.

Explore the topics below to learn more about these paths and how you can use them in your own projects.

## Ray Tracing in Unreal Engine

Ray Tracing in Unreal Engine supports two modes:

* A hybrid **Ray Tracer** that couples ray tracing capabilities with traditional raster techniques for real-time rendering.
* A **Path Tracer** for generating high quality, compromise-free rendered results.

## System Requirements

The following system requirements must be met to use Ray Tracing and Path Tracing features of Unreal Engine:

| System Requirements |  |
| --- | --- |
| **Operating System** | * [Windows 10 RS5 (Build 1809) or later](https://support.microsoft.com/en-us/help/4028685/windows-10-get-the-update)  Verify your Windows build by typing **winver** in the Windows search bar. * Vulkan Desktop on Linux and Windows    + For details on what operating system builds are needed, see [Hardware and Software Specifications](https://dev.epicgames.com/documentation/en-us/unreal-engine/hardware-and-software-specifications-for-unreal-engine?application_version=5.5). |
| **GPU** | NVIDIA RTX and some GTX series cards with DXR support using the latest device drivers.  For more information, see NVIDIA's site [here](https://www.nvidia.com/en-us/geforce/news/geforce-gtx-dxr-ray-tracing-available-now). |
| **Unreal Engine Version** | 5.0 and Later |
| **Unreal Engine Rendering Path** | Deferred Path |

## Overviews

* [![Hardware Ray Tracing](https://dev.epicgames.com/community/api/documentation/image/3b1eaa89-6ce3-4a42-b755-c2ce127c6faf?resizing_type=fit&width=640&height=640)

  Hardware Ray Tracing

  An overview of the features that use hardware to render real-time ray traced results.](https://dev.epicgames.com/documentation/en-us/unreal-engine/hardware-ray-tracing-in-unreal-engine)

* [![Path Tracer](https://dev.epicgames.com/community/api/documentation/image/41646628-a38e-4623-83d6-1ca16062ed44?resizing_type=fit&width=640&height=640)

  Path Tracer

  Learn about the Path Tracer and how you can use it to render high quality images for final shots and ground truth comparisons against the real-time rendered scenes.](https://dev.epicgames.com/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine)

## Guides



* [![Hardware Ray Tracing Tips and Tricks](https://dev.epicgames.com/community/api/documentation/image/84aee19c-30aa-4592-a75c-c51dfc0acae7?resizing_type=fit&width=640&height=640)

  Hardware Ray Tracing Tips and Tricks

  A collection of topics to aid with development of projects using hardware ray tracing features.](https://dev.epicgames.com/documentation/en-us/unreal-engine/hardware-ray-tracing-tips-and-tricks-in-unreal-engine)

* [![Rendering High Quality Frames with Movie Render Queue](https://dev.epicgames.com/community/api/documentation/image/cec3f9d9-3ec4-489d-872e-ac96bf416d16?resizing_type=fit&width=640&height=640)

  Rendering High Quality Frames with Movie Render Queue

  A how-to guide for configuring the Unreal Engine Movie Render Queue feature to get high-quality cinematics—particularly when using ray tracing.](https://dev.epicgames.com/documentation/en-us/unreal-engine/rendering-high-quality-frames-with-movie-render-queue-in-unreal-engine)

## Reference

* [![Hardware Ray Tracing and Path Tracer Features Properties](https://dev.epicgames.com/community/api/documentation/image/88d84b27-2311-4589-a892-8675c6809497?resizing_type=fit&width=640&height=640)

  Hardware Ray Tracing and Path Tracer Features Properties

  A listing of all available properties setting for Ray Tracing and Path Tracer features.](https://dev.epicgames.com/documentation/en-us/unreal-engine/ray-tracing-and-path-tracer-features-properties-in-unreal-engine)

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [lighting](https://dev.epicgames.com/community/search?query=lighting)
* [film](https://dev.epicgames.com/community/search?query=film)
* [architectural visualization](https://dev.epicgames.com/community/search?query=architectural%20visualization)
* [ray tracing](https://dev.epicgames.com/community/search?query=ray%20tracing)
* [path tracing](https://dev.epicgames.com/community/search?query=path%20tracing)
* [tv](https://dev.epicgames.com/community/search?query=tv)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Ray Tracing in Unreal Engine](/documentation/en-us/unreal-engine/ray-tracing-and-path-tracing-features-in-unreal-engine?application_version=5.7#ray-tracing-in-unreal-engine)
* [System Requirements](/documentation/en-us/unreal-engine/ray-tracing-and-path-tracing-features-in-unreal-engine?application_version=5.7#system-requirements)
* [Overviews](/documentation/en-us/unreal-engine/ray-tracing-and-path-tracing-features-in-unreal-engine?application_version=5.7#overviews)
* [Guides](/documentation/en-us/unreal-engine/ray-tracing-and-path-tracing-features-in-unreal-engine?application_version=5.7#guides)
* [Reference](/documentation/en-us/unreal-engine/ray-tracing-and-path-tracing-features-in-unreal-engine?application_version=5.7#reference)
