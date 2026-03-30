<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/optimizing-and-debugging-projects-for-realtime-rendering-in-unreal-engine?application_version=5.7 -->

# Optimizing and Debugging Projects for Real-Time Rendering

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
6. Optimizing and Debugging Projects for Real-Time Rendering

# Optimizing and Debugging Projects for Real-Time Rendering

Concepts and approaches to optimizing and debugging your projects for real-time rendering with features and tools available in Unreal Engine.

![Optimizing and Debugging Projects for Real-Time Rendering](https://dev.epicgames.com/community/api/documentation/image/b0beab43-1106-4c68-a38e-a28eb7ce1cb9?resizing_type=fill&width=1920&height=335)

 On this page

Optimizing a project is not always a straightforward task and getting the maximum performance can be challenging because it can, at times, be where milliseconds matter most.

## Getting Started Optimizing Your Project

There are multiple places you can start looking to improve performance by optimizing your project. This can start with improving content creation workflows, performing profiling captures to know where time is being spent to render each frame, and using built-in editor tools.

Unreal Engine already does a lot of heavy-lifting to optimize your project for performance without needing to set up anything. But, that doesn't mean that these built-in systems can't be adjusted to fit your project's needs more closely.

The guide below will help you get started in identifying common performance issues and where to look for them. You'll also learn about some of the tools available in the editor that you can use to optimize and improve performance.

* [![Guidelines for Optimizing Rendering for Real-Time](https://dev.epicgames.com/community/api/documentation/image/efba6f9a-f38b-43e8-b224-e327d33bbb1f?resizing_type=fit&width=640&height=640)

  Guidelines for Optimizing Rendering for Real-Time

  Optimization and development best practices for real-time rendering.](https://dev.epicgames.com/documentation/en-us/unreal-engine/guidelines-for-optimizing-rendering-for-real-time-in-unreal-engine)

## Rendering Pipeline Optimization

The choice of some optimizations can directly affect the rendering pipeline that Unreal Engine uses. They can improve performance for the project in general or may be well-suited for a specific platform you want to develop for.

For example, Unreal Engine offers multiple rendering paths with a Deferred path (default) and a Forward renderer. For platforms like VR and Mobile, the Forward Renderer can improve performance but it does not support all rendering features of the engine.

In other cases, changes to the rendering pipeline can improve performance by rendering at a lower resolution and upscaling rather than rendering at native resolution, all while maintaining the same visual fidelity as the native resolution.

* [![Forward Shading Renderer](https://dev.epicgames.com/community/api/documentation/image/0967d838-66ed-4576-b3fa-5ca6ab177e4c?resizing_type=fit&width=640&height=640)

  Forward Shading Renderer

  Describes the advantages of using the Forward Shading Renderer.](https://dev.epicgames.com/documentation/en-us/unreal-engine/forward-shading-renderer-in-unreal-engine)

* [![Screen Percentage with Temporal Upscale](https://dev.epicgames.com/community/api/documentation/image/c5b61559-f54e-44c7-8b6a-24a611df6e52?resizing_type=fit&width=640&height=640)

  Screen Percentage with Temporal Upscale

  An overview of using Screen Percentage with Temporal Upsampling.](https://dev.epicgames.com/documentation/en-us/unreal-engine/screen-percentage-with-temporal-upscale-in-unreal-engine)

* [![Dynamic Resolution](https://dev.epicgames.com/community/api/documentation/image/e87ee41d-9332-4608-8e31-2cd596d88795?resizing_type=fit&width=640&height=640)

  Dynamic Resolution

  A method of dynamically adjusting the screen percentage to improve performance.](https://dev.epicgames.com/documentation/en-us/unreal-engine/dynamic-resolution-in-unreal-engine)

## Configuration Files and Scalability Optimizations

Through console commands and configuration files, you can set properties that scales your project for the type of experience or platform your application is developed for.

Console commands are used to call and set specific properties. These can be used in configuration files and scalability settings to improve quality and performance of the rendered image for development of the project or for the final shipped product. Configuration files can store these callable scalability settings to automatically set them for the project, and they can even be platform-specific.

For example, a configuration file can be set up which has multiple scalability options for a user to select from to make the application run better on lower end hardware, or the configuration file can store presets that are designed for specific platforms to use that best optimize the application to run on it.

* [![Configuration Files](https://dev.epicgames.com/community/api/documentation/image/13593a96-0a11-4ff0-9062-ff267596caea?resizing_type=fit&width=640&height=640)

  Configuration Files

  Initial settings for configuring gameplay or engine behavior on startup.](https://dev.epicgames.com/documentation/en-us/unreal-engine/configuration-files-in-unreal-engine)

* [![Command-Line Arguments Reference](https://dev.epicgames.com/community/api/documentation/image/97949d3a-b203-41b1-aed0-6b4431582ac3?resizing_type=fit&width=640&height=640)

  Command-Line Arguments Reference

  List of command-line arguments available for Unreal Engine.](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-command-line-arguments-reference)

* [![Anti-Aliasing and Upscaling](https://dev.epicgames.com/community/api/documentation/image/06b9f74b-4559-4b11-8faf-96895f744ef4?resizing_type=fit&width=640&height=640)

  Anti-Aliasing and Upscaling

  A high level overview of the Anti Aliasing options available in Unreal Engine.](https://dev.epicgames.com/documentation/en-us/unreal-engine/anti-aliasing-and-upscaling-in-unreal-engine)



* [![Ray Tracing Performance Guide](https://dev.epicgames.com/community/api/documentation/image/ed719ec3-6a76-4f64-a0a7-7323eed6e5c0?resizing_type=fit&width=640&height=640)

  Ray Tracing Performance Guide

  A selection of topics for improving performance of ray tracing features in your projects.](https://dev.epicgames.com/documentation/en-us/unreal-engine/ray-tracing-performance-guide-in-unreal-engine)

* [![Hardware Ray Tracing Tips and Tricks](https://dev.epicgames.com/community/api/documentation/image/84aee19c-30aa-4592-a75c-c51dfc0acae7?resizing_type=fit&width=640&height=640)

  Hardware Ray Tracing Tips and Tricks

  A collection of topics to aid with development of projects using hardware ray tracing features.](https://dev.epicgames.com/documentation/en-us/unreal-engine/hardware-ray-tracing-tips-and-tricks-in-unreal-engine)

* [![Scalability and The Developer](https://dev.epicgames.com/community/api/documentation/image/21f4a732-a429-4da3-b1d0-fe4502e4f6fc?resizing_type=fit&width=640&height=640)

  Scalability and The Developer

  An overview of Scalability options and considerations for content creators, testers, programmers, and managers.](https://dev.epicgames.com/documentation/en-us/unreal-engine/scalability-and-the-developer-for-unreal-engine)

* [![Scalability Reference](https://dev.epicgames.com/community/api/documentation/image/60a2b054-bfd8-4a8f-8c42-5dec09ed435c?resizing_type=fit&width=640&height=640)

  Scalability Reference

  Scalability options, properties, and console variables.](https://dev.epicgames.com/documentation/en-us/unreal-engine/scalability-reference-for-unreal-engine)

* [![Stat Commands](https://dev.epicgames.com/community/api/documentation/image/7c67beac-f13f-4011-baf0-d84de1ca37d3?resizing_type=fit&width=640&height=640)

  Stat Commands

  Console commands specific to displaying game statistics](https://dev.epicgames.com/documentation/en-us/unreal-engine/stat-commands-in-unreal-engine)

## Asset Optimization

Optimization of assets in your project starts with the workflows you choose when developing the project. Sometimes this can mean creating those assets in ways that work best with Unreal Engine's tools. Other times, the built-in editor tools can do this work for you.

For example, manually creating level of detail (LOD) meshes for every object can be a time-consuming process. Unreal Engine provides its own automatic tool to generate LODs for your meshes. You can even configure the properties for how LODs are generated manually or let it perform the task automatically.

The built-in tools and systems below can help you to improve performance during development of your project.



* [![Nanite Virtualized Geometry Overview](https://dev.epicgames.com/community/api/documentation/image/c41aa30e-443f-4d9f-804e-e32e504e6c3e?resizing_type=fit&width=640&height=640)

  Nanite Virtualized Geometry Overview

  Learn about Nanite's virtualized geometry system and how it achieves pixel scale detail and high object counts.](https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine)

* [![Visibility and Occlusion Culling](https://dev.epicgames.com/community/api/documentation/image/7199121f-8621-4e5c-b61f-b2e258f6c240?resizing_type=fit&width=640&height=640)

  Visibility and Occlusion Culling

  An overview of available visibility and occlusion culling methods.](https://dev.epicgames.com/documentation/en-us/unreal-engine/visibility-and-occlusion-culling-in-unreal-engine)

* [![Texture Streaming](https://dev.epicgames.com/community/api/documentation/image/81eacd37-2ec4-461c-9fad-3a37d5c1b941?resizing_type=fit&width=640&height=640)

  Texture Streaming

  System for loading and unloading textures into and out of memory during gameplay.](https://dev.epicgames.com/documentation/en-us/unreal-engine/texture-streaming-in-unreal-engine)

* [![Creating and Using LODs](https://dev.epicgames.com/community/api/documentation/image/99df6603-d902-4426-a657-cf791bae74e3?resizing_type=fit&width=640&height=640)

  Creating and Using LODs

  How To Create and Use LODs.](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-and-using-lods-in-unreal-engine)

* [![Setting Up Per-Platform LODs](https://dev.epicgames.com/community/api/documentation/image/dae9cf2f-f3fa-4ea1-a1d1-f1807ba7276b?resizing_type=fit&width=640&height=640)

  Setting Up Per-Platform LODs

  How to set up LOD's on a per-platform basis.](https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-per-platform-lods)

* [![Static Mesh Automatic LOD Generation](https://dev.epicgames.com/community/api/documentation/image/70757c9d-3ebc-4f81-9e9d-185ae7c36223?resizing_type=fit&width=640&height=640)

  Static Mesh Automatic LOD Generation

  How To use the Automatic LOD Generation system in UE5.](https://dev.epicgames.com/documentation/en-us/unreal-engine/static-mesh-automatic-lod-generation-in-unreal-engine)

* [![Proxy Geometry Tool](https://dev.epicgames.com/community/api/documentation/image/6276c847-d412-4548-a584-94d4aed09e40?resizing_type=fit&width=640&height=640)

  Proxy Geometry Tool

  The Proxy Geometry tool set was developed as a way to increase your Unreal Engine 4 (UE4) projects performance while keeping the visual quality of your project uneffected.](https://dev.epicgames.com/documentation/en-us/unreal-engine/proxy-geometry-tool-in-unreal-engine)

## Debugging and Profiling Tools

Unreal Engine provides its own debugging and profiling tools and offers plugins for some external applications. These tools are useful for inspecting and identifying areas to improve performance.

For example, using the visualization modes of the Level Editor can visually identify costs of materials currently being rendered on screen. Profiling tools for the CPU and GPU can capture individual frames and breakdown millisecond cost of what is being rendered. With this type of information, you can see what is taking the longest to render in a single frame. By investigating high-cost line items, it may be possible to optimize those elements further.

The tools below will help you debug and profile elements of your project to look for performance optimization opportunities.

* [![Using RenderDoc with Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/a8aaf804-4197-432a-91f8-838c1841b110?resizing_type=fit&width=640&height=640)

  Using RenderDoc with Unreal Engine

  RenderDoc is a standalone open-source graphics debugger that you can use to perform single-frame captures and inspect them.](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-renderdoc-with-unreal-engine)

* [![Unreal Insights](https://dev.epicgames.com/community/api/documentation/image/b6bb65f0-31be-40d7-8592-c8e0dedb4909?resizing_type=fit&width=640&height=640)

  Unreal Insights

  Profile your project's performance with Unreal Insights.](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine)

* [![GPUDump Viewer Tool](https://dev.epicgames.com/community/api/documentation/image/8a947670-2805-4fb6-8546-6085421875dd?resizing_type=fit&width=640&height=640)

  GPUDump Viewer Tool

  A multi-platform command that dumps intermediary RDG textures and buffers to disk for investigating and debugging rendering issues.](https://dev.epicgames.com/documentation/en-us/unreal-engine/gpudump-viewer-tool-in-unreal-engine)

* [![Render Resource Viewer](https://dev.epicgames.com/community/api/documentation/image/f9e71730-361b-4269-ad08-339d857a457f?resizing_type=fit&width=640&height=640)

  Render Resource Viewer

  A tool to assist in identifying resources and their assets allocated to GPU memory.](https://dev.epicgames.com/documentation/en-us/unreal-engine/render-resource-viewer-in-unreal-engine)

* [![Primitive Debugger](https://dev.epicgames.com/community/api/documentation/image/8f8d0942-65b0-454b-8d9d-775e4225e87a?resizing_type=fit&width=640&height=640)

  Primitive Debugger

  This is a runtime-only tool to view information about primitives being rendered in the game client.](https://dev.epicgames.com/documentation/en-us/unreal-engine/primitive-debugger-in-unreal-engine)

## Other Topics



* [![Dealing with a GPU Crash](https://dev.epicgames.com/community/api/documentation/image/cebe7a8b-0645-435f-9aea-a22de532be8c?resizing_type=fit&width=640&height=640)

  Dealing with a GPU Crash

  An overview of investigating, resolving, and reporting GPU Crashes in Unreal Engine.](https://dev.epicgames.com/documentation/en-us/unreal-engine/dealing-with-a-gpu-crash-when-using-unreal-engine)

### Additional Epic-Created Resources

* [Unreal Performance Optimization Learning Path](https://dev.epicgames.com/community/learning/paths/Rkk/unreal-engine-unreal-performance-optimization-learning-path)

* [performance](https://dev.epicgames.com/community/search?query=performance)
* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [optimization](https://dev.epicgames.com/community/search?query=optimization)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Getting Started Optimizing Your Project](/documentation/en-us/unreal-engine/optimizing-and-debugging-projects-for-realtime-rendering-in-unreal-engine?application_version=5.7#getting-started-optimizing-your-project)
* [Rendering Pipeline Optimization](/documentation/en-us/unreal-engine/optimizing-and-debugging-projects-for-realtime-rendering-in-unreal-engine?application_version=5.7#rendering-pipeline-optimization)
* [Configuration Files and Scalability Optimizations](/documentation/en-us/unreal-engine/optimizing-and-debugging-projects-for-realtime-rendering-in-unreal-engine?application_version=5.7#configuration-files-and-scalability-optimizations)
* [Asset Optimization](/documentation/en-us/unreal-engine/optimizing-and-debugging-projects-for-realtime-rendering-in-unreal-engine?application_version=5.7#asset-optimization)
* [Debugging and Profiling Tools](/documentation/en-us/unreal-engine/optimizing-and-debugging-projects-for-realtime-rendering-in-unreal-engine?application_version=5.7#debugging-and-profiling-tools)
* [Other Topics](/documentation/en-us/unreal-engine/optimizing-and-debugging-projects-for-realtime-rendering-in-unreal-engine?application_version=5.7#other-topics)
* [Additional Epic-Created Resources](/documentation/en-us/unreal-engine/optimizing-and-debugging-projects-for-realtime-rendering-in-unreal-engine?application_version=5.7#additionalepic-createdresources)
