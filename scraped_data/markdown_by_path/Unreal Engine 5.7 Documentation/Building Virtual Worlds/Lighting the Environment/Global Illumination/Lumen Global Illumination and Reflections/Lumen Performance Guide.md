<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/lumen-performance-guide-for-unreal-engine?application_version=5.7 -->

# Lumen Performance Guide

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
7. [Global Illumination](/documentation/en-us/unreal-engine/global-illumination-in-unreal-engine "Global Illumination")
8. [Lumen Global Illumination and Reflections](/documentation/en-us/unreal-engine/lumen-global-illumination-and-reflections-in-unreal-engine "Lumen Global Illumination and Reflections")
9. Lumen Performance Guide

# Lumen Performance Guide

Scalability options for Lumen Global Illumination and Reflections.

![Lumen Performance Guide](https://dev.epicgames.com/community/api/documentation/image/7b2b2ae7-a683-42ef-bcf9-3a75997abac4?resizing_type=fill&width=1920&height=335)

 On this page

Lumen targets 30 and 60 frames per second (fps) on consoles with 8ms and 4ms frame budgets at 1080p for global illumination and reflections on opaque and translucent materials, and volumetric fog. The engine uses preconfigured Scalability settings to control Lumen's target FPS. The **Epic** scalability level targets 30 fps. The **High** scalability level targets 60 fps.

Lumen relies on [Temporal Upsampling](https://dev.epicgames.com/documentation/en-us/unreal-engine/dynamic-resolution-in-unreal-engine) with Unreal Engine 5's [Temporal Super Resolution](https://dev.epicgames.com/documentation/en-us/unreal-engine/temporal-super-resolution-in-unreal-engine) (TSR) for 4k output. Lumen and other features use a lower internal resolution (1080p), which gives TSR the best final image quality. Otherwise, rendering these features at 4K natively would need lower quality settings to achieve 30 or 60 fps.

## Scalability Settings

You can find the Scalability settings in the Level Editor under the Viewport **Settings > Engine Scalability Settings**. In-game, control the Scalability settings with GameUserSettings and the graphics settings menus (see the [Lyra](https://dev.epicgames.com/documentation/en-us/unreal-engine/lyra-sample-game-in-unreal-engine) project for an example). Lumen quality is set by the **Global Illumination** and **Reflections** quality groups:

* **Cinematic** scalability level targets [Movie Render Queue](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/MovieRenderPipeline).
* **Epic** scalability level targets a 30 fps console budget.
* **High** scalability level targets a 60 fps console budget.
* **Low** and **Medium** scalability levels disable Lumen features.

[![Engine Scalability Settings](https://dev.epicgames.com/community/api/documentation/image/824259ca-bc5b-4a9a-9f1c-56d4563c2082?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/824259ca-bc5b-4a9a-9f1c-56d4563c2082?resizing_type=fit)

By default, Unreal Engine targets 30 fps on consoles. To target 60 fps, set the **Global Illumination** and **Reflections** quality groups to **High** in the console Device Profiles. These profiles can be found in `[Your Project Name]\Platforms[Console]\Config\` folder. For example, `[Your Project Name]\Platforms\PS5\Config\PS5DeviceProfiles.ini`.

A PlayStation 5 Device Profile targeting 60 fps would look like:

C++

```
|  |  |
| --- | --- |
|  | [PS5 DeviceProfile] |
|  | ; Set Lumen GI and reflection quality to High, targeting 60 fps |
|  | +CVars=sg.GlobalIlluminationQuality=2 |
|  | +CVars=sg.ReflectionQuality=2 |
```

[PS5 DeviceProfile]
; Set Lumen GI and reflection quality to High, targeting 60 fps
+CVars=sg.GlobalIlluminationQuality=2
+CVars=sg.ReflectionQuality=2

Copy full snippet(4 lines long)

## Scaling Down Beyond Lumen

The default **Global Illumination** and **Reflections** quality groups are in `\Engine\Config\BaseScalability.ini`. These settings attempt to keep indirect lighting looking similar between quality levels. This has the added benefit of not needing to redo your lighting per platform while scaling down costs of Lumen.

Medium Quality Level

* For large-scale ambient occlusion, **Distance Field Ambient Occlusion** replaces **Lumen Global Illumination**.
* For small-scale ambient occlusion, **Screen Space Ambient Occlusion** is enabled.

Low Quality Level

* Uses only unshadowed skylight.
* Reduces skylight intensity (`r.SkylightIntensityMultiplier=0.7`) to better match **Medium** quality level since there's no form of skylight shadowing.

### Software Ray Tracing

[Software Ray Tracing](https://dev.epicgames.com/documentation/en-us/unreal-engine/lumen-technical-details-in-unreal-engine#software-ray-tracing) is the fastest tracing method in Lumen and we recommend it for games which cannot afford Hardware Ray Tracing or as a fallback for GPUs which don't support Hardware Ray Tracing.

In this configuration Lumen traces a single merged Global Distance Field. Tracing the global distance field makes tracing independent from the number of instances and their overlap with other instances. It's also a great fit for content with a large amount of overlapping instances.

Global Distance Field update performance is still dependent on the number of instances, but it’s heavily cached which reduces the cost of updates.

Global Distance Field caches movable and static objects separately. It’s important to correctly set up component mobility, as moving static actors will invalidate static cache, which can be very expensive. `r.GlobalDistanceField.Debug.LogModifiedPrimitives` can be used to debug, which static actors are being moved at runtime.

Disable **Affects Distance Field Lighting** in component or set **Distance Field Resolution Scale** to **0** in the static mesh editor in order to remove individual distance field instances from rendering in the distance field scene. Removing less important instances that don't have a major impact on global illumination or reflections can help to optimize Global Distance Field update performance.

### Hardware Ray Tracing

Hardware Ray Tracing provides Lumen with improved quality and we recommend it as a default option on consoles for both 30 fps and 60 fps. It is more expensive than Software Ray Tracing and requires careful scene optimization as it is quite sensitive to large amounts of instance overlaps.

Hardware Ray Tracing requires rebuilding the **Top Level Acceleration Structure** (TLAS) every frame. This cost is proportional to the number of instances you need to include in this acceleration structure. Achieving good performance on next-generation consoles generally means having fewer than 100,000 instances in the **Ray Tracing Scene** after culling. On Microsoft Windows, the number of instances can vary.

Use `Stat SceneRendering` to check how many instances are visible in the ray tracing scene. Look at the **Ray tracing active instances** stat.

[![Stat SceneRendering](https://dev.epicgames.com/community/api/documentation/image/e2022b92-d757-4020-9af9-91a1954f340d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e2022b92-d757-4020-9af9-91a1954f340d?resizing_type=fit)

The ray tracing scene culling settings are the most powerful tool for controlling how many ray tracing instances are in the scene. Ray tracing culling is enabled by default to simplify its setup, but additional changes can be made to the **DefaultEngine.ini** configuration file found in the `[Your Project Name]\Config\` folder.

C++

```
|  |  |
| --- | --- |
|  | [SystemSettings] |
|  | r.RayTracing.Culling=3 |
|  | r.RayTracing.Culling.Radius=15000 |
|  | r.RayTracing.Culling.Angle=0.5 |
```

[SystemSettings]
r.RayTracing.Culling=3
r.RayTracing.Culling.Radius=15000
r.RayTracing.Culling.Angle=0.5

Copy full snippet(4 lines long)

You can remove Individual instances from the ray tracing scene by disabling **Visible In Ray Tracing** on the actor in the level.

See the [Ray Tracing Performance Guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/ray-tracing-performance-guide-in-unreal-engine) for detailed information on Hardware Ray Tracing performance, including performance counters and debug views.

**Far Field** provides aggressive culling without compromising global illumination and reflection distance. After the ray tracing scene radius, all rays use the far field traces to extend global illumination and reflections at a cheaper cost. [Lumen Technical Details](https://dev.epicgames.com/documentation/en-us/unreal-engine/lumen-technical-details-in-unreal-engine) provides information on how to set up Far Field.

Increasing ray tracing scene culling coupled with Far Field helps you to optimize and scale down Lumen Hardware Ray Tracing performance.

Hardware Ray Tracing performance depends on how much the meshes in the scene overlap. Large meshes that overlap the entire scene are a performance issue, such as a skybox. These meshes should have **Visible In Ray Tracing** disabled. You can also save tracing costs on grass meshes, and kit-bashed meshes with multiple layers of intersecting combined meshes.

To keep scenes performant with Hardware Ray Tracing, you must keep overlapping meshes to a reasonable level.

**Hit Lighting for Reflections** provides improved reflection quality. It evaluates materials and lighting at every hit point, but is expensive for games. We don't recommend using it for games unless materials are trivial and optimized with **Ray Tracing Quality Switch** nodes. On consoles, you can limit the number of BVH traversal iterations and terminate long and expensive rays early using `r.Lumen.HardwareRayTracing.MaxIterations`. Terminated rays are treated as fully occluded with zero radiance causing over-occlusion. This setting is useful to finetune performance and avoid performance issues caused by parts of the scene with lots of overlapping geometry.

## Tips

The cost of **Lumen Reflections** can vary depending on how much of the screen has smooth, or low-roughness, materials. These materials need dedicated reflection rays. By default, all pixels with roughness below 0.4 will trace a reflection ray. Pixels with roughness above that get free reflection approximation based on Lumen Global illumination.

### Lumen Reflection Roughness Threshold

You can control the roughness threshold using **Max Roughness To Trace** setting in the **Post Process Volume**. It can be additionally clamped from scalability settings using `r.Lumen.Reflections.MaxRoughnessToTraceClamp`. Pixels with roughness below the set threshold will trace dedicated **Lumen Reflection** rays, and pixels with roughness above this threshold fall back to free rough specular approximation.

Foliage has an independent roughness threshold. Any pixel with materials **Two Sided Foliage** or **Subsurface** shading models are treated as foliage. You can control foliage roughness with `r.Lumen.Reflections.MaxRoughnessToTraceForFoliage`. Pixels requiring dedicated reflection rays can be visualized using **Performance Overview** view mode, which is found in the Level Viewport under the View Modes menu.

[![Lumen Performance View Mode](https://dev.epicgames.com/community/api/documentation/image/ea708de5-517c-4752-9c3d-a7c14bd20de2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ea708de5-517c-4752-9c3d-a7c14bd20de2?resizing_type=fit)

Reflections on foliage are often hard to see. Without compromising quality, it's possible to achieve some significant performance wins by setting the foliage max roughness threshold to 0.

### Replacing Lumen Reflections with Screen Space Reflections

Reflection costs can be more aggressively scaled down by replacing Lumen Reflections with **Screen Space Reflections** (SSR). You can do this by setting `r.Lumen.Reflections.Allow=0`. For example, you can save 1 ms on Xbox Series S by adding the following to the `XSXDeviceProfiles.ini` file.

C++

```
|  |  |
| --- | --- |
|  | [XSX_Lockhart DeviceProfile] |
|  | ; Use SSR in lieu of Lumen reflections for perf |
|  | +CVars=r.Lumen.Reflections.Allow=0 |
```

[XSX\_Lockhart DeviceProfile]
; Use SSR in lieu of Lumen reflections for perf
+CVars=r.Lumen.Reflections.Allow=0

Copy full snippet(3 lines long)

The example below demonstrates how Lumen Global Illumination provides rough specular even when Lumen Reflections is disabled.

[![Example of Lumen GI Specular with Lumen Reflections disabled.](https://dev.epicgames.com/community/api/documentation/image/67528db7-1c42-49f9-9d18-645949ba15fe?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/67528db7-1c42-49f9-9d18-645949ba15fe?resizing_type=fit)

Some performance increase from Lumen Reflections is gained by reusing rays traced for diffuse global illumination. This only provides a speed increase for scenes with many pixels whose roughness is in the range of 0.2–0.4. You can enable this using `r.Lumen.Reflections.RadianceCache=1`.

### Lumen Scene Lighting

**Lumen Scene Lighting** updates the surface cache's direct and indirect lighting, which is used for lighting ray hits both for global illumination and for reflections. Performance depends on the fraction of surface cache updated every frame. Speed up updates can be set separately for direct lighting using `r.LumenScene.DirectLighting.UpdateFactor`, and for indirect lighting, using `r.LumenScene.DirectLighting.MaxLightsPerTile` and `r.LumenScene.Radiosity.UpdateFactor`.

Lumen Scene Lighting selects a small subset of the most important lights per surface cache tile, which makes its performance less sensitive to the total number of lights in the scene. The number of lights per tile can be controlled by `r.LumenScene.DirectLighting.MaxLightsPerTile`.

### Lumen World Space Radiance Cache

Lumen caches distant lighting using a **World Space Radiance Cache**.

Individual probe resolution can be controlled using `r.Lumen.ScreenProbeGather.RadianceCache.ProbeResolution` and `r.Lumen.TranslucencyVolume.RadianceCache.ProbeResolution`. Higher values increase the quality of indirect lighting but are more expensive to update.

The second main performance control is the number of probes to be updated per frame. This can be set using `r.Lumen.ScreenProbeGather.RadianceCache.NumProbesToTraceBudget`and `r.Lumen.TranslucencyVolume.RadianceCache.NumProbesToTraceBudget`. Higher values make lighting more responsive but cost more. Setting this value too low can cause lighting pops during fast camera movements due to Lumen having to slowly catch-up, so at some point in order to scale down further the resolution of a probe grid has also to be reduced using `r.Lumen.ScreenProbeGather.RadianceCache.GridResolution` and `r.Lumen.TranslucencyVolume.GridPixelSize`.

### Lumen Screen Probe Gather

**Screen Probe Gather** is responsible for the final gather by tracing rays from pixels and integrating incoming lighting.

The main performance control here is probe spacing (`r.Lumen.ScreenProbeGather.DownsampleFactor`) and resolution of screen space probes (`r.Lumen.ScreenProbeGather.TracingOctahedronResolution`). Increasing probe spacing will reduce the quality of indirect shadows and blur indirect lighting. Decreasing screen probe resolution will reduce indirect lighting directionality and quality of rough reflections.

Indirect lighting integration can be optionally run at half-resolution using `r.Lumen.ScreenProbeGather.IntegrateDownsampleFactor 2`. This will greatly speedup integration, but can cause extra noise and soften normals, so it’s not enabled by default by any of the default scalability or device presets.

### Profiling Lumen

Lumen is divided into three passes:

* **Lumen Scene Lighting** for evaluating surface cache lighting.
* **Lumen Screen Probe Gather** for evaluating diffuse global illumination and rough reflections, and translucency global illumination.
* **Lumen Reflections** for evaluating dedicated reflection rays on smooth surfaces.

`Stat GPU` displays GPU pass timings, including individual Lumen passes.

[![Stat GPU](https://dev.epicgames.com/community/api/documentation/image/f8514fed-59de-469b-9717-5c71a0fdfcd4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f8514fed-59de-469b-9717-5c71a0fdfcd4?resizing_type=fit)

For a more detailed performance breakdown, use the `ProfileGPU` command. You can also use third-party profiling tools like RenderDoc.

Lumen is using Async Compute, running in parallel with other workloads. In order to measure Lumen individuality, it's recommended to disable it with the console command `r.Lumen.AsyncCompute 0`. See the next section for more details about Async Compute.

## Async Compute

Lumen uses **Async Compute** on consoles. This allows the GPU to overlap Lumen's work with the non-Nanite geometry pass and direct lighting pass. Additionally, Lumen can overlap with the **Lumen Screen Probe Gather** and **Lumen Reflections** passes.

[![Async compute graphics passes](https://dev.epicgames.com/community/api/documentation/image/7f78cb2c-0029-47d6-a6cc-1206ae0894b2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7f78cb2c-0029-47d6-a6cc-1206ae0894b2?resizing_type=fit)

Async Compute is pre-configured for common workloads, but in some cases non-default settings can be faster. One of these cases which we encountered is when the **Lumen Screen Probe Gather** pass can't overlap with the **Lumen Reflections** pass due to large amounts of direct lighting or shadow map work on the graphics queue. In this case, it may be beneficial to run the Lumen entirely as an async compute pass. You can do this by setting the following:

C++

```
|  |  |
| --- | --- |
|  | r.LumenScene.Lighting.AsyncCompute=1 |
|  | r.Lumen.DiffuseIndirect.AsyncCompute=1 |
|  | r.Lumen.Reflections.AsyncCompute=1 |
```

r.LumenScene.Lighting.AsyncCompute=1
r.Lumen.DiffuseIndirect.AsyncCompute=1
r.Lumen.Reflections.AsyncCompute=1

Copy full snippet(3 lines long)

Async Compute makes Lumen overlap with other rendering passes. This makes profiling harder since timings will include not only the cost of Lumen, but also the cost of other workloads which overlap with it. When profiling Lumen individually, disable Async Compute.

## Scalability Reference

The default engine scalability and per-platform device profiles contain individual Lumen settings. These are useful as a reference for important and up-to-date renderer performance scalability settings. Also, they are a good starting point for custom scalability settings. We recommend using the default scalability levels to achieve 30 fps or 60 fps, but also for a consistent look between levels. You can take a look at these scalability settings in either of these files:

C++

```
|  |  |
| --- | --- |
|  | [Engine Root]\Engine\Config\BaseScalability.ini |
|  | [Engine Root]\Platforms\[Console Name]\Base[ConsoleName]DeviceProfile.ini |
```

[Engine Root]\Engine\Config\BaseScalability.ini
[Engine Root]\Platforms\[Console Name]\Base[ConsoleName]DeviceProfile.ini

Copy full snippet(2 lines long)

* [performance](https://dev.epicgames.com/community/search?query=performance)
* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [lighting](https://dev.epicgames.com/community/search?query=lighting)
* [optimization](https://dev.epicgames.com/community/search?query=optimization)
* [global illumination](https://dev.epicgames.com/community/search?query=global%20illumination)
* [lumen](https://dev.epicgames.com/community/search?query=lumen)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Scalability Settings](/documentation/en-us/unreal-engine/lumen-performance-guide-for-unreal-engine?application_version=5.7#scalability-settings)
* [Scaling Down Beyond Lumen](/documentation/en-us/unreal-engine/lumen-performance-guide-for-unreal-engine?application_version=5.7#scaling-down-beyond-lumen)
* [Software Ray Tracing](/documentation/en-us/unreal-engine/lumen-performance-guide-for-unreal-engine?application_version=5.7#software-ray-tracing)
* [Hardware Ray Tracing](/documentation/en-us/unreal-engine/lumen-performance-guide-for-unreal-engine?application_version=5.7#hardware-ray-tracing)
* [Tips](/documentation/en-us/unreal-engine/lumen-performance-guide-for-unreal-engine?application_version=5.7#tips)
* [Lumen Reflection Roughness Threshold](/documentation/en-us/unreal-engine/lumen-performance-guide-for-unreal-engine?application_version=5.7#lumen-reflection-roughness-threshold)
* [Replacing Lumen Reflections with Screen Space Reflections](/documentation/en-us/unreal-engine/lumen-performance-guide-for-unreal-engine?application_version=5.7#replacing-lumen-reflections-with-screen-space-reflections)
* [Lumen Scene Lighting](/documentation/en-us/unreal-engine/lumen-performance-guide-for-unreal-engine?application_version=5.7#surface-cache-tile-updates)
* [Lumen World Space Radiance Cache](/documentation/en-us/unreal-engine/lumen-performance-guide-for-unreal-engine?application_version=5.7#lumenworldspaceradiancecache)
* [Lumen Screen Probe Gather](/documentation/en-us/unreal-engine/lumen-performance-guide-for-unreal-engine?application_version=5.7#lumenscreenprobegather)
* [Profiling Lumen](/documentation/en-us/unreal-engine/lumen-performance-guide-for-unreal-engine?application_version=5.7#profiling-lumen)
* [Async Compute](/documentation/en-us/unreal-engine/lumen-performance-guide-for-unreal-engine?application_version=5.7#async-compute)
* [Scalability Reference](/documentation/en-us/unreal-engine/lumen-performance-guide-for-unreal-engine?application_version=5.7#scalability-reference)
