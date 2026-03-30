<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/pcg-runtime-generation-debugging-in-unreal-engine?application_version=5.7 -->

# PCG Runtime Generation Debugging

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
6. [Procedural Content Generation Framework](/documentation/en-us/unreal-engine/procedural-content-generation-framework-in-unreal-engine "Procedural Content Generation Framework")
7. PCG Runtime Generation Debugging

# PCG Runtime Generation Debugging

An overview of PCG runtime generation debugging tools.

![PCG Runtime Generation Debugging](https://dev.epicgames.com/community/api/documentation/image/71327f04-2e66-44ea-bd54-dea606c98282?resizing_type=fill&width=1920&height=335)

 On this page

## Introduction

When you are creating a project using Unreal Engine's (UE) **procedural content generation** (PCG) features, you have access to debugging features and workflows. This page provides an overview of those tools, to help you improve your work.

## General Tools

This section describes tools useful for improving your PCG projects.

### Screen Overlay

The **screen overlay** provides a high-level overview of what the system is doing. You can use this to validate at a glance that runtime generation is active.

[![PCG screen overlay](https://dev.epicgames.com/community/api/documentation/image/039b2038-a5d3-4f52-863f-64f4b10fd954?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/039b2038-a5d3-4f52-863f-64f4b10fd954?resizing_type=fit)

The PCG screen overlay.

To enable the feature, use the following cvar: `pcg.RuntimeGeneration.EnableDebugOverlay 1`

The data values shown are unfiltered, to give you clean data for each frame.

Considering most projects run at 30 FPS or higher, we recommend capturing a video to study transient behaviors, so you can use the scroll and pause features to review the data for any given frame during the generation process.

UE displays the following data fields after you enable this feature.

| Overlay Data Field | Description |
| --- | --- |
| **Tick time** | Shows game thread time spent inside the runtime generation system during the current frame. |
| **Generate Calls** | Shows how often  `Generate()`  was called on grid cells this frame. |
| **Cleanup Calls** | Shows how often  `Cleanup()`  was called on grid cells this frame. |
| **Num Generating Components** | Shows how many PCG components / cells were  generating this frame. |
| **PA Pool** | Shows the generated results placed on partition actors (PAs) in the level. These are pooled to reduce runtime cost. When the current pool is exhausted, it is doubled in size, an expensive operation you should avoid triggering during gameplay. You can set the initial pool size using the cvar  `pcg.RuntimeGeneration.BasePoolSize` . |
| **VT Preloads** | Shows how many times  `URuntimeVirtualTextureComponent::Preload()`  was called during the current frame to prime virtual textures for use. You can use this to verify the VT setup and VT priming information are set correctly in the level.  You can enable or disable VT preloading using the cvar  `pcg.VirtualTexturePriming.Enable` .  You can visualize VT preloading using the cvar  `pcg.VirtualTexturePriming.DebugDrawTexturePrimingBounds` . |

The screen overlay functions in Editor and Development builds, not Test or Shipping builds.

### Draw Generated Cells

The **draw generated cells** feature shows a visualization of the runtime generation state.

[![Draw generated cells wireframe during PIE](https://dev.epicgames.com/community/api/documentation/image/afa83e3c-532f-4bc2-991a-c3ce932676cc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/afa83e3c-532f-4bc2-991a-c3ce932676cc?resizing_type=fit)

The draw generated cells wireframe during PIE.

To enable the feature, use the following cvar: `pcg.GraphExecution.DebugDrawGeneratedCells 1`

UE shows the following visuals when you enable this feature:

* **Red wireframe sphere**: These are drawn for each generation source, at the smallest generation radius. The fine detail (as in the above screenshot) generates when grid cells are overlapped by the red sphere. In the editor, a label displays near the center of the generation source.
* **Yellow triple-wireframe boxes**: These are drawn around any cell that is currently generating. In the editor, a label displays near the center of the generation cell with the grid size and cell coordinates, which can aid in further inspection and debugging in the graph editor.
* If either the **Generate Landscape Textures** node or the **Generate Grass Maps** node is in use, a single wireframe box is drawn in cells waiting for grass map textures to stream in.

A red sphere is drawn for each generation radius for each grid that has runtime components. Pressing F8 to eject from your character while in PIE and moving to view the wireframe spheres from a different perspective gives better understanding of the procedural generation behavior.

[![Wireframe spheres viewed from a distance after ejecting in PIE.](https://dev.epicgames.com/community/api/documentation/image/6673801f-1aca-40e2-8235-b785497370b3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6673801f-1aca-40e2-8235-b785497370b3?resizing_type=fit)

Generation source wireframe spheres viewed after ejecting from the character in Play in Editor mode.

This visualization serves several tasks and workflows. It helps you to:

* Understand how the system is behaving at a glance.
* Diagnose visual pop issues (for correlating visible pops with generating cells).
* Fine-tune the runtime processing budget pcg.FrameTime (or pcg.EditorFrameTime outside of PIE). To do so, observe whether the generation is happening promptly when the generation radius sphere starts overlapping the cell.

  + If cells generate immediately on overlap, the system is keeping up with the workload.
  + If cells are still generating well within the generation radius, there is a danger of visual pops.

A **visual pop** is a sudden, unintended change in what the player sees—such as a jump, flicker, or snapping transition—that breaks the visual continuity of the scene.

This feature functions in Editor and Development builds. By default it does not function for Test and Shipping builds, but you can enable it by setting `UE_ENABLE_DEBUG_DRAWING` to true in the respective config files.

### Other Console Commands and Variables

| Console Command / Variable | Description |
| --- | --- |
| `pcg.RuntimeGeneration.Refresh` | Cleans up all current grid cells. The system then regenerates them in following ticks. Useful for checking whether an issue is transient (that is, refreshing fixes it) or persistent.Command, emit when needed. |
| `pcg.RuntimeGeneration.Enable` | Controls runtime generation ticking. The current generated state of cells is frozen when disabled. To remove all runtime-generated data, set it to disabled then emit  `pcg.RuntimeGeneration.Refresh` . Enabled by default. |
| `pcg.Cache.Runtime.Enabled` | Controls whether the PCG graph cache is enabled, which caches output data from CPU nodes to avoid later re-executing on the same data. Applies to game worlds. Disabled by default. |
| `pcg.Cache.Editor.Enabled` | Controls whether the PCG graph cache is enabled, which caches output data from CPU nodes to avoid later re-executing on the same data. Applies to editor worlds. Enabled by default. |
| `pcg.Cache.Runtime.MemoryBudgetMB` | Controls how much memory the PCG graph cache is allowed to use in game worlds. When memory usage exceeds this value, old entries are dropped from the cache. Requires an integer value. |
| `pcg.Cache.Editor.MemoryBudgetMB` | Controls how much memory the PCG graph cache is allowed to use in editor worlds. When memory usage exceeds this value, old entries are dropped from the cache. Requires an integer value. |
| `pcg.GPU.FuzzMemory` | Randomly initializes buffer memory before execution in GPU graphs. This helps test if all data is properly written, and helps reproduce undefined behavior bugs which can be hard to isolate, especially when uninitialized data is often 0 by chance. Disabled by default. |
| `pcg.RuntimeGeneration.HideActorsFromOutliner` | Controls whether runtime generation actors are visible in the Outliner. Enabled by default. |
| `pcg.RuntimeGeneration.FramesBeforeFirstGenerate` | Delays runtime generation for the number of ticks you specify. The PCG system waits this duration until beginning to generate, which is useful to provide buffer time for Virtual Textures to populate. Requires an integer value, the default is 0. |
| `pcg.GPU.EnableLandscapeVTSampling` | Enable to use Virtual Textures to obtain landscape height data. This is primarily useful in GPU graphs. Enabled by default. |

## Debugging

This section describes features specifically for debugging your CPU and GPU when working with PCG.

### CPU Debugging

Every node has a **Break In Debugger** setting which, when enabled, triggers breakpoints in CPU debuggers when the node enters any execute phase.

[![Break In Debugger feature in the Details panel.](https://dev.epicgames.com/community/api/documentation/image/04bbe7a9-b2ce-46c7-9351-7239f208c798?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/04bbe7a9-b2ce-46c7-9351-7239f208c798?resizing_type=fit)

Break In Debugger feature in the Details panel.

Requirements:

* You must attach a debugger.
* You must select the component or grid cell of interest in the **Debug Object Tree**. The breakpoint is only active for the currently inspected object.

If the node result is already cached, the node might not execute unless the cache is flushed (for example, by ctrl-clicking the **Force Regen** button in the graph editor toolbar).

### GPU Debugging

Nodes set to execute on GPU expose additional debug settings, as shown in the image below.

[![GPU debug options](https://dev.epicgames.com/community/api/documentation/image/12c1bc45-3423-4eba-872e-44dc3ea8ff25?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/12c1bc45-3423-4eba-872e-44dc3ea8ff25?resizing_type=fit)

GPU debug options

| GPU Debug Setting | Description |
| --- | --- |
| **Dumped Cooked HLSL** | Enable to show the cooked HLSL source before it is passed to Compute Framework to assemble the final kernel. Useful for kernel development. |
| **Dump Data Descriptions** | Enable to dump the description of data flowing through GPU nodes, which PCG uses to determine buffer sizes and thread counts. |
| **Print Shader Debug Values** | Enable to allocate an array of floats initialized with a default value of 0, and expose an API for overwriting these values from the HLSL. After the array values are updated from the GPU kernel, they are printed to the log. See  `WriteDebugValue`  in the Declarations pane of the HLSL Source editor. |
| **Trigger Render Capture** | Enable to trigger a render capture when this node executes while a debug object is selected in the graph editor. Editor-only. Render captures must be enabled (for example,  `-AttachRenderDoc`  or  `-AttachPIX` ). These tools provide a detailed view of the GPU state and the state of the input/output buffers. |

The `pcg.GPU.FuzzMemory` cvar described above under [Other Console Commands and Variables](https://dev.epicgames.com/documentation/en-us/unreal-engine/pcg-runtime-generation-debugging-in-unreal-engine#other-console-commands-and-variables) is useful for debugging. GPU memory allocated each frame can result in values of 0, or similar random contents every frame, which can obscure bugs when either data is not written or uninitialized data is read. Enabling this option can make such bugs obvious and significantly improve reproducibility.

## Profiling

This section describes tools for profiling your CPU and GPU activity.

### CPU Profiling

The **Profiling** pane in the PCG Graph Editor window gives a detailed breakdown of CPU time spent in each node. This does not yet cover GPU execution.

For more detailed profiling, [Unreal Insights](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-insights-in-unreal-engine) is the standard tool. A range of PCG functions are instrumented with profile scopes (including `UPCGSubystem::Tick` which is typically the root for much of the work, and which you can plot as a starting point when opening a trace).

### GPU Profiling

PCG kernels execute in `ComputeFrame_ExecuteBatches`. On some platforms and build configs, each kernel has a scope which gives the kernel name.

For more detailed profiling, select a GPU profiling tool for your platform. Repeatable profiling can be tricky as PCG work produces bursts of activity when generating cells, but does not do predictable work every frame. To help with repeatable profiling, there is a **Profile Kernel Index** setting on GPU-enabled nodes.

[![Profile Kernel Index Setting in the Details panel.](https://dev.epicgames.com/community/api/documentation/image/c5e7accd-bfbf-4908-91b7-8da77a7c7198?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c5e7accd-bfbf-4908-91b7-8da77a7c7198?resizing_type=fit)

Profile Kernel Index Setting in the Details panel.

This index perpetually dispatches a kernel executed by this node every frame, which provides a way to capture a GPU trace using a GPU profiling tool to analyze performance. Some nodes emit multiple kernels from `CreateKernels()`, this setting is an index for this array. Set it to -1 to disable profiling.

Any grid cells will progress up to this kernel and then repeatedly execute each frame, and this can result in a lot of dispatches which might skew performance. You can set `pcg.RuntimeGeneration.NumGeneratingComponents` to limit how many cells can execute simultaneously.

To enable this functionality, enable `PCG_GPU_KERNEL_PROFILING` in PCG.Build.cs.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Introduction](/documentation/en-us/unreal-engine/pcg-runtime-generation-debugging-in-unreal-engine?application_version=5.7#introduction)
* [General Tools](/documentation/en-us/unreal-engine/pcg-runtime-generation-debugging-in-unreal-engine?application_version=5.7#generaltools)
* [Screen Overlay](/documentation/en-us/unreal-engine/pcg-runtime-generation-debugging-in-unreal-engine?application_version=5.7#screenoverlay)
* [Draw Generated Cells](/documentation/en-us/unreal-engine/pcg-runtime-generation-debugging-in-unreal-engine?application_version=5.7#drawgeneratedcells)
* [Other Console Commands and Variables](/documentation/en-us/unreal-engine/pcg-runtime-generation-debugging-in-unreal-engine?application_version=5.7#other-console-commands-and-variables)
* [Debugging](/documentation/en-us/unreal-engine/pcg-runtime-generation-debugging-in-unreal-engine?application_version=5.7#debugging)
* [CPU Debugging](/documentation/en-us/unreal-engine/pcg-runtime-generation-debugging-in-unreal-engine?application_version=5.7#cpudebugging)
* [GPU Debugging](/documentation/en-us/unreal-engine/pcg-runtime-generation-debugging-in-unreal-engine?application_version=5.7#gpudebugging)
* [Profiling](/documentation/en-us/unreal-engine/pcg-runtime-generation-debugging-in-unreal-engine?application_version=5.7#profiling)
* [CPU Profiling](/documentation/en-us/unreal-engine/pcg-runtime-generation-debugging-in-unreal-engine?application_version=5.7#cpuprofiling)
* [GPU Profiling](/documentation/en-us/unreal-engine/pcg-runtime-generation-debugging-in-unreal-engine?application_version=5.7#gpuprofiling)

Related documents

[Build Configurations Reference

![Build Configurations Reference](https://dev.epicgames.com/community/api/documentation/image/12d11fab-41a6-4a29-ad7c-6ad0f2a6d1b7?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/build-configurations-reference-for-unreal-engine)
