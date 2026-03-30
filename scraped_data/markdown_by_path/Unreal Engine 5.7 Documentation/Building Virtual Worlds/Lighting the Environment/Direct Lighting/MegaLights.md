<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/megalights-in-unreal-engine?application_version=5.7 -->

# MegaLights

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
7. [Direct Lighting](/documentation/en-us/unreal-engine/features-and-properties-of-lights-in-unreal-engine "Direct Lighting")
8. MegaLights

# MegaLights

A whole new direct lighting path to place many dynamic and shadowed area lights in a scene.

![MegaLights](https://dev.epicgames.com/community/api/documentation/image/56bf9cf2-9e8f-4b91-9f66-ef561377b6c2?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

MegaLights is a whole new direct lighting path in Unreal Engine 5 enabling artists to place orders of magnitudes more dynamic and shadowed area lights than they could ever before.

[![](https://dev.epicgames.com/community/api/documentation/image/35072cc3-e8e6-415f-a2cb-91c263f17cab?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/35072cc3-e8e6-415f-a2cb-91c263f17cab?resizing_type=fit)

MegaLights is designed to support current generation consoles and leverages ray tracing to enable realistic soft shadows from various types of area lights.

[![](https://dev.epicgames.com/community/api/documentation/image/743b1d3c-d38c-4c66-83d9-e25663db762d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/743b1d3c-d38c-4c66-83d9-e25663db762d?resizing_type=fit)

MegaLights not only reduces the cost of dynamic shadowing, it also reduces the cost of unshadowed light evaluation, making it possible to use expensive light sources, such as textured area lights, on consoles.

[![](https://dev.epicgames.com/community/api/documentation/image/f0946efe-b04d-4ad0-956a-4cdf46c9a8e8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f0946efe-b04d-4ad0-956a-4cdf46c9a8e8?resizing_type=fit)

MegaLights also supports [Volumetric Fog](building-virtual-worlds\lighting-and-shadows\environmental-lighting\volumetric-fog).

[![](https://dev.epicgames.com/community/api/documentation/image/13db5e47-c170-4035-b48f-f8fa0b56fb96?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/13db5e47-c170-4035-b48f-f8fa0b56fb96?resizing_type=fit)

## Using MegaLights

You can enable MegaLights for your project from the Project Settings in the **Rendering > Direct Lighting** category. This prompts you to also enable **Support Hardware Ray Tracing**, which is a recommended setting for MegaLights.

[![](https://dev.epicgames.com/community/api/documentation/image/857f4fda-f355-4401-a8de-3e0a1d75345a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/857f4fda-f355-4401-a8de-3e0a1d75345a?resizing_type=fit)

Once enabled, all local lights are handled by the MegaLights system. MegaLights can be disabled per light using **Allow MegaLights** light component property. You can also set the **MegaLights Shadow Method** to select the source of shadowing to either be **Ray Tracing (Default)** or **Virtual Shadow Maps** (VSMs).

[![](https://dev.epicgames.com/community/api/documentation/image/f7a12747-1eb4-4d01-9bc3-04ac238f6f66?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f7a12747-1eb4-4d01-9bc3-04ac238f6f66?resizing_type=fit)

While Virtual Shadow Maps will cast shadows directly from the non-simplified Nanite geometry, it only approximates area shadows. There is CPU, memory and GPU time overhead for VSMs on a per-light basis for preparing shadow map depths in advance.

For a more fine-grained control inside a single project, MegaLights can be enabled or disabled using Post Process Volume settings.

[![](https://dev.epicgames.com/community/api/documentation/image/5c4234bb-0b2e-491b-9558-aed9e22b0d7b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5c4234bb-0b2e-491b-9558-aed9e22b0d7b?resizing_type=fit)

MegaLights can be disabled per scalability level or device profile with `r.MegaLights.Allow 0`.

## Technique Overview

MegaLights is a stochastic direct lighting technique, which solves direct lighting though importance sampling of lights. It traces a fixed number of rays per pixel towards important light sources. If a light source is hit by a ray then that light’s contribution is added to the current pixel.

This approach has a few important implications:

* Direct lighting is handled by a single pass in an unified manner, replacing multiple existing Deferred Renderer shadowing and shading techniques.
* MegaLights not only reduce the cost of shadowing, but also reduce the cost of the shading itself.
* MegaLights has a constant performance overhead, but quality may decrease as lighting complexity increases at a given pixel.

Where Deferred Shading has a constant lighting quality, the GPU cost increases with the number of lights. Whereas, MegaLights have constant performance, but the quality depends on the lighting complexity at a given pixel.

MegaLights replaces the following features:

* Shadow MapsDistance Field Shadows
* Ray Traced Shadows
* Deferred Shading (BRDF and light evaluation)
* Volumetric Fog shadowing and light evaluation
* Virtual Shadow Map projection

  + Virtual Shadow Maps can still be used with MegaLights if selected as the shadow method on the individual light actor’s settings.

By default, MegaLights first traces a short conservative screen space ray in order to pick up tiny details, which may not be available in the simplified Ray Tracing Scene. If such ray goes offscreen, behind an object, or just reaches its max length, then MegaLights continues tracing from the last valid position using Hardware or Software Ray Tracing. MegaLights can also be configured to ray trace a virtual shadow map, but its shadows have additional upfront cost since shadow maps need to be generated per light, while the BVH (Ray Tracing Scene) is generated once for all lights in the scene.

The ray guiding in MegaLights is useful for selecting important light sources and is crucial for sending more samples to lights that are likely to have influence on a given pixel. In turn, ray guiding sends fewer samples towards lights that are to have less influence, like those that are likely occluded. This is an important part of the technique, allowing it to extract the best possible lighting quality out of the fixed per pixel light sample budget. While ray guiding reduces the number of rays sent towards occluded light sources, it still needs to periodically sample those to check whether they became visible in the current frame. With this in mind, you should avoid placing light sources with huge bounds affecting the entire scene.

Finally, all accumulated lighting goes through a denoiser that tries to reconstruct high quality direct lighting from the stochastic and possibly noisy input. As the lighting complexity increases in the scene, the denoiser needs to do more work to account for this. Increased lighting complexity can lead to blurring of the lighting or cause ghosting, which you can avoid by merging smaller light sources into large area lights and carefully narrowing down the bounds of light sources to improve the final lighting quality.

## Lighting Complexity

There’s a limitation of how many important lights can affect a single pixel before it has to rely heavily on the denoiser because there’s a fixed budget and fixed number of samples per pixel, which can cause the denoiser to produce blurry lighting and eventually noise or ghosting in the scene. It continues to be important to optimize light placement by narrowing light attenuation range, and replacing clusters of light sources with a single area light.

To keep MegaLights working well within a scene, it’s best to avoid placing lights inside scene geometry and to optimize a light’s bounds. You can use the console command `r.MegaLights.Debug 1` to visualize where rays are being sent from a selected pixel. You can freeze a selected ray using this console command `r.ShaderPrint.Lock 1`, which allows you to fly around the scene to inspect traced rays.

Additional visualization tools will be made available as MegaLights is developed into a production-ready feature of Unreal Engine.

In the example below, part of the textured rect light is inside the wall and even though it won’t be ever visible, it still needs to be sampled by MegaLights. This can be seen in the visualization, which shows some of the rays being traced into the wall. Ideally textured rect light’s **Source Width** and **Source Height** should be narrowed down, so that light source fills this arch, but doesn’t extend past it.

[![](https://dev.epicgames.com/community/api/documentation/image/f3b6688d-6bc2-42ab-9314-108897ffbd9c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f3b6688d-6bc2-42ab-9314-108897ffbd9c?resizing_type=fit)

To minimize noise avoid placing lights inside geometry, optimize light attenuation range, spotlight cone angles, and rect light barn doors to narrow down the influence of light.

## Ray Tracing Scene

By default, MegaLights uses ray tracing, and shadow quality depends on the quality of Ray Tracing Scene representation. For performance, the Ray Tracing Scene is built using automatically simplified Nanite meshes and has more aggressive culling settings than the main view. This may cause shadow artifacts, leaking, or missing shadows.

Ray Tracing Scene visualizations are a great starting point for investigating shadowing issues. They show the actual scene representation that MegaLights ray-traces against. You can visualize the Ray Tracing Scene using:

* One of the **Ray Tracing Debug** view modes, which is found in the Level Viewport under the View Modes menu. Ray Tracing Debug view modes are also available through console commands: `show RayTracingDebug 1` and `r.RayTracing.DebugVisualizationMode = "World Normal"`.
* **Lumen Overview** view mode, which enables a picture-in-picture visualization where both the Ray Tracing Scene and main view can be seen at the same time. Lumen Overview view mode is also available through the console command `r.Lumen.Visualize 1`.

|  |  |
| --- | --- |
|  |  |
| Scene View | Ray Tracing World Normal Visualization View Mode |

If some shadows are missing or disappearing with distance, it may be due to Ray Tracing Scene culling. You can start adjusting culling by using the console commands under `r.RayTracing.Culling.*`. You’ll want to look at the culling mode, radius, and solid angle variables.

For culling purposes, you can merge smaller objects together using **Ray Tracing Group Id**, so that they are culled together using their merged bounds.

For more detailed information about Ray Tracing Scene culling controls, see the [Ray Tracing Performance Guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/ray-tracing-performance-guide-in-unreal-engine?application_version=5.5).

Ray Tracing Scene is based on automatically simplified Nanite Fallback Meshes. Default settings can sometimes result in fallback meshes that are too low quality for the purposes of shadowing and may require manual adjustment. Follow these steps to do this:

[![](https://dev.epicgames.com/community/api/documentation/image/d59dd3b4-ecaf-4c00-9f37-4d4b79c87f45?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d59dd3b4-ecaf-4c00-9f37-4d4b79c87f45?resizing_type=fit)

1. Open the mesh in the Static Mesh Editor.
2. In the Details panel under **Nanite Setting**, set the **Fallback Target** to **Relative Error**.
3. A new setting is revealed named **Fallback Relative Error**, and you can set its value. Reducing the value increases the number of triangles and fidelity of the Nanite Fallback mesh.
4. Once you’re done, click **Apply Changes** to rebuild the Nanite Fallback Mesh.

For more information about setting up Nanite Fallback Meshes, see [Nanite Virtualized Geometry](designing-visuals-rendering-and-graphics\rendering-optimization\nanite).

Nanite Fallback Mesh triangle count and number of instances included in the Ray Tracing Scene will affect ray tracing BVH build times, used memory, and ray tracing performance. We recommend carefully increasing them according to the available performance and memory budget of your project.

For non real-time rendering, it’s also possible to use `r.RayTracing.Nanite.Mode 1`, which builds the Ray Tracing Scene out of full detail Nanite Meshes. This has a large performance and memory cost and can result in hitches during scene or camera animation when the Nanite LOD cut changes and its BVH needs to be rebuilt.

## Screen Space Traces

MegaLights uses the Ray Tracing Scene when casting shadows for larger geometry detail but leverages screen space traces for smaller scale geometry that may be missing from the simplified Ray Tracing Scene. Screen space traces use Scene Depth and they will hit anything that's visible on the screen. This may cause issues with certain art direction tweaks, like invisible shadow casters which don’t affect Scene Depth and only exist in the Ray Tracing Scene.

For traces that extend past the ray tracing scene coverage (or when the far field representation is too coarse), MegaLights supports distant screen traces. The length of the distant screen traces is defined as a percentage of the screen using `r.MegaLights.DistantScreenTraces.Length`.

## Shadowing Methods

MegaLights exposes two shadowing methods, which can be selected per light using light component’s properties:

* **Ray Tracing** is the default and recommended method. It doesn't add any extra cost per light and can achieve correct area shadows. The downside is that the quality of the shadows depends on the simplified Ray Tracing Scene.
* **Virtual Shadow Maps** traces rays against a [Virtual Shadow Map](building-virtual-worlds\lighting-and-shadows\shadows\virtual-shadow-maps). Virtual Shadow Maps are generated per light using rasterization and can capture full Nanite mesh details. The downside is that it can only approximate area shadows, and it has a significant additional per light cost in terms of memory, CPU, and GPU overhead used to generate shadow depths. This should be used sparingly.

By default, all lights, especially larger area light sources with softer shadows or less important lights, should use Ray Tracing, as softer lights don’t need precise shadow casters. It’s also worth allocating a bit more budget for the Ray Tracing Scene, as higher quality ray tracing representation allows for more lights going through the cheaper ray tracing path.

## Light Functions

Light Functions are supported as long as they are compatible with the [Light Function Atlas](building-virtual-worlds\lighting-and-shadows\features-of-lights\light-functions\#lightfunctionatlas) and if the Light Function atlas is enabled in the project settings.

## Alpha Masking

By default, only Screen Space Traces can correctly handle alpha masked surfaces. It’s possible to enable Alpha Masking support for Ray Tracing using the console command `r.MegaLights.HardwareRayTracing.EvaluateMaterialMode 1`. Enabling this option has a non-trivial performance overhead, so it’s best to avoid alpha masking in content.

## Directional Lights

By default, directional lights are disabled and have to be manually enabled using `r.MegaLights.DirectionalLights 1`. This is due to various limitations, making it more suited towards dim and soft directional lights as moonlight than high quality sharp sun shadows extending to the horizon.

Quality of directional light shadows heavily depends on the ray tracing representation in the distance, which can be challenging due to BVH build and traversal overhead. Some of those issues can be hidden by enabling Far Field.

Strong directional lights can also make indoors noisy by redirecting some samples towards invisible directional light, which doesn’t contribute to the final pixels. It’s possible to work around this by placing post process volumes, which would make directional light dimmer indoors or maybe even disable it.

## Far Field

MegaLights implements [Far Field](https://dev.epicgames.com/documentation/en-us/unreal-engine/ray-tracing-performance-guide-in-unreal-engine?application_version=5.5#far-field) traces, which allow extending shadow ray range past the TLAS culling range with a relatively low overhead by tracing against very simplified and merged HLOD1 meshes.

Far Field traces are enabled by the console variable `r.MegaLights.HardwareRayTracing.FarField` in the DefaultEngine.ini configuration file, and requires the use of World Partition's Hierarchical Level of Detail (HLOD). Far Field requires the use of HLOD1 to be built.

## Lit Translucency and Volumetric Fog

MegaLights integrates with the [Translucency Lighting Volume](https://dev.epicgames.com/documentation/en-us/unreal-engine/lit-translucency-in-unreal-engine) and [Volumetric Fog](https://dev.epicgames.com/documentation/en-us/unreal-engine/volumetric-fog-in-unreal-engine) to stochastically evaluate lighting and shadowing on those volumes.

Shadowing is calculated using a unified froxel volume whose resolution is defined using`r.MegaLights.Volume.GridPixelSize`and `r.MegaLights.Volume.GridSizeZ`. The coverage of the volume is automatically extended based on `r.TranslucencyLightingVolume.OuterDistance` and the View Distance of the active Exponential Height Fog component.

Changing these settings will affect the quality of shadowing on both lit translucency and volumetric fog.

## Forward Shading

Forward shading is currently calculated using the same volume used for lit translucency. In particular, specular lighting is approximated by extracting a single light from spherical harmonics that approximates the overall lighting around the surface.

## Particle Lights

MegaLights supports particle lights but only for those spawned by [Niagara systems](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-niagara-effects-for-unreal-engine) currently. They can also be made shadow casting when handled by MegaLights.

By default, particle lights will only be handled by MegaLights when users enable it explicitly in assets. This behavior can be changed using the console variable `r.MegaLights.SimpleLightMode`, where setting it to 2 makes MegaLights handle all particle lights — shadow casting still needs to be enabled per asset — and setting it to 0 disables particle lights from MegaLights.

To enable MegaLights for a Niagara emitter:

[![Niagara emitter with MegaLights settings.](https://dev.epicgames.com/community/api/documentation/image/a2935c53-1c16-45dd-aab2-07b55b9a337e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a2935c53-1c16-45dd-aab2-07b55b9a337e?resizing_type=fit)

Niagara emitter with MegaLights settings.

1. Select the **Light Renderer** module under the emitter.
2. In the **Details** panel, enable **Allow Mega Lights** and **Mega Lights Cast Shadows**.

   1. Checking the second setting makes the particle lights cast shadows.
   2. Checking the first setting enables MegaLights for the lights spawned.

Since an emitter can spawn a lot of lights, care needs to be taken to avoid having too many strong lights affecting a screen pixel at the same time. Otherwise, quality may degrade noticeably. We recommend keeping the lights small, sparse in space, and only enable shadow casting on a small number of particle lights.

## Scalability

These are the primary controls for scalability of MegaLights:

* `r.MegaLights.DownsampleMode` controls the downsample factor for sampling and tracing.
* `r.MegaLights.NumSamplesPerPixel` controls how many samples and traces are done per pixel.

Scaling lighting quality to that of high-end PCs or offline rendering is still under development, however you can try to use the command `r.MegaLights.DownsampleMode 0` and `r.MegaLights.NumSamplesPerPixel 16` to achieve the best quality.

For scalability of lighting for volumetric fog and hair strands, you can use console variables under `r.megalights.volume.*` to adjust lighting quality for them.

MegaLights doesn’t yet have dedicated support for [Movie Render Queue](animating-characters-and-objects\Sequencer\movie-render-pipeline#movierenderqueue), but good results can be achieved with either using Temporal Super Resolution (TSR) as anti-aliasing method or setting the Temporal Sample Count to around 8, which is able to resolve lighting correctly.

## Performance

When comparing performance it’s important to understand that MegaLights is solving all direct lighting and replaces a variety of Deferred Renderer passes, such as:

* **Shadow Depths:** if using Shadow Maps or Virtual Shadow Maps
* **RenderDeferredLighting::Lights**
* **InjectTranslucencyLightingVolume**
* **VolumetricFog::Shadowed Lights**
* Removes light evaluation from **VolumetricFog::LightScattering**

Factors which impact performance:

* Performance is mostly dependent on the internal rendering resolution.
* Ray Tracing is the second biggest part of MegaLights cost. The cost depends on several factors: the number of instances in the Ray Tracing Scene, their complexity, amount of overlapping instances and amount of dynamic triangles which need to be updated each frame. For in-depth information about optimizing the Ray Tracing Scene, see the [Ray Tracing Performance Guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/ray-tracing-performance-guide-in-unreal-engine?application_version=5.5).
* There’s an additional memory, CPU and GPU overhead for generating shadow map depths per each light, which uses Virtual Shadow Map for shadowing instead of Ray Tracing.
* There’s a small cost for pixels on screen with complex BRDFs and affected by heavy light types (textured Rect Lights).

MegaLights cost is mostly constant, and there isn’t a large difference between unshadowed and shadowed lights, so all lights in the scene can have shadows enabled.

Ideally, MegaLights should be used with [Lumen HWRT](building-virtual-worlds\lighting-and-shadows\global-illumination\lumen\TechOverview\#hardwareraytracing), which allows sharing Ray Tracing Scene overhead and optimizations between both systems.

`Stat GPU` shows GPU timing overview, including the MegaLights pass. In-depth timings can be obtained using built-in `ProfileGPU` or third party profilers.

Unreal Engine uses Async Compute to overlap multiple dispatches from various features. `Stat GPU` and `ProfileGPU` timings will be distorted until you disable Async Compute using the `r.RDG.AsyncCompute 0` console command.

Although MegaLights is fully GPU driven, there’s still some legacy CPU cost per light. If all lights are MegaLights using ray tracing, most of the per light CPU cost can be removed using the console command `r.Visibility.LocalLightPrimitiveInteraction 0`.

## Limitations

General limitations:

* MegaLights is incompatible with the Forward Renderer

Current limitations, which we want to improve:

* There’s a legacy per light CPU overhead tracking primitive interactions, which aren’t needed for MegaLights
* Directional light cloud shadows aren't supported.
* Subsurface scattering thickness estimation isn't supported.
* Water, Clouds, Heterogenous Volumes and Local Volumetrics aren’t supported

## Platform Support

* MegaLights are designed for current gen consoles (such as PlayStation 5, Xbox Series X | S) and PCs with ray tracing capabilities.
* MegaLights do not support mobile, Switch, or previous-generation consoles (such as PlayStation 4 and Xbox One)

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [lighting](https://dev.epicgames.com/community/search?query=lighting)
* [experimental](https://dev.epicgames.com/community/search?query=experimental)
* [lights](https://dev.epicgames.com/community/search?query=lights)
* [megalights](https://dev.epicgames.com/community/search?query=megalights)
* [hardware ray tracing](https://dev.epicgames.com/community/search?query=hardware%20ray%20tracing)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Using MegaLights](/documentation/en-us/unreal-engine/megalights-in-unreal-engine?application_version=5.7#using-mega-lights)
* [Technique Overview](/documentation/en-us/unreal-engine/megalights-in-unreal-engine?application_version=5.7#technique-overview)
* [Lighting Complexity](/documentation/en-us/unreal-engine/megalights-in-unreal-engine?application_version=5.7#lighting-complexity)
* [Ray Tracing Scene](/documentation/en-us/unreal-engine/megalights-in-unreal-engine?application_version=5.7#ray-tracing-scene)
* [Screen Space Traces](/documentation/en-us/unreal-engine/megalights-in-unreal-engine?application_version=5.7#screen-space-traces)
* [Shadowing Methods](/documentation/en-us/unreal-engine/megalights-in-unreal-engine?application_version=5.7#shadowing-methods)
* [Light Functions](/documentation/en-us/unreal-engine/megalights-in-unreal-engine?application_version=5.7#light-functions)
* [Alpha Masking](/documentation/en-us/unreal-engine/megalights-in-unreal-engine?application_version=5.7#alpha-masking)
* [Directional Lights](/documentation/en-us/unreal-engine/megalights-in-unreal-engine?application_version=5.7#directionallights)
* [Far Field](/documentation/en-us/unreal-engine/megalights-in-unreal-engine?application_version=5.7#farfield)
* [Lit Translucency and Volumetric Fog](/documentation/en-us/unreal-engine/megalights-in-unreal-engine?application_version=5.7#littranslucencyandvolumetricfog)
* [Forward Shading](/documentation/en-us/unreal-engine/megalights-in-unreal-engine?application_version=5.7#forwardshading)
* [Particle Lights](/documentation/en-us/unreal-engine/megalights-in-unreal-engine?application_version=5.7#particlelights)
* [Scalability](/documentation/en-us/unreal-engine/megalights-in-unreal-engine?application_version=5.7#scaling-quality-up)
* [Performance](/documentation/en-us/unreal-engine/megalights-in-unreal-engine?application_version=5.7#performance)
* [Limitations](/documentation/en-us/unreal-engine/megalights-in-unreal-engine?application_version=5.7#limitations)
* [Platform Support](/documentation/en-us/unreal-engine/megalights-in-unreal-engine?application_version=5.7#platform-support)
