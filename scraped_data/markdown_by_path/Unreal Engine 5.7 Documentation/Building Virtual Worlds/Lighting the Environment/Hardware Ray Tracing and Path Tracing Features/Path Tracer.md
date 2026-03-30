<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7 -->

# Path Tracer

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
7. [Hardware Ray Tracing and Path Tracing Features](/documentation/en-us/unreal-engine/ray-tracing-and-path-tracing-features-in-unreal-engine "Hardware Ray Tracing and Path Tracing Features")
8. Path Tracer

# Path Tracer

Learn about the Path Tracer and how you can use it to render high quality images for final shots and ground truth comparisons against the real-time rendered scenes.

![Path Tracer](https://dev.epicgames.com/community/api/documentation/image/4ce8aa40-6ca7-4d99-ae16-a37f540b4ab1?resizing_type=fill&width=1920&height=335)

 On this page

The Path Tracer is a progressive, hardware-accelerated rendering mode that mitigates the disadvantages of real-time features with physically correct and compromise-free global illumination, reflection and refraction of materials, and more. It shares the ray tracing architecture built into Unreal Engine, with minimal to no additional setup required to achieve clean, photoreal renders.

[![](https://dev.epicgames.com/community/api/documentation/image/82da1beb-7afe-44db-a844-7e9983195679?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/82da1beb-7afe-44db-a844-7e9983195679?resizing_type=fit)

"Virtual tour in Unreal Engine" by ARCHVYZ. Design by Toledano Architects.

The Path Tracer uses the same ray-tracing architecture as other ray-tracing features, such as [Real-Time Ray Tracing](https://dev.epicgames.com/documentation/en-us/unreal-engine/hardware-ray-tracing-in-unreal-engine) and [GPU Lightmass](https://dev.epicgames.com/documentation/en-us/unreal-engine/gpu-lightmass-global-illumination-in-unreal-engine), making it ideal for [ground truth comparisons](https://dev.epicgames.com/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine) and production renders. The Path Tracer only uses geometry and material present in the scene to render its unbiased result, and does not share the same ray-tracing code that has been developed to work well for real-time rendering.

## Benefits of the Path Tracer

The Path Tracer provides the following benefits when compared to other rendering modes:

* The ability to generate high-quality photorealistic renders with physically accurate results.
* Minimal or no additional setup required to achieve comparable results to other offline renderers.
* Reduces the feature gap of comparable real time features. For example, materials seen in reflections and refractions are rendered without limitations, such as having global illumination and path-traced shadows present.
* Full integration with Sequencer and Movie Render Queue to support Film / TV quality render outputs.

## Path-Traced Examples

The following scenes are examples of the high-quality renders achieved using the Path Tracer.

[![](https://dev.epicgames.com/community/api/documentation/image/f778c3d5-9e95-4139-817b-299558004cf9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f778c3d5-9e95-4139-817b-299558004cf9?resizing_type=fit)

"Virtual tour in Unreal Engine" by ARCHVYZ. Design by Toledano Architects.

## Enabling the Path Tracer in Your Project

The Path Tracer requires [Hardware Ray Tracing](https://dev.epicgames.com/documentation/en-us/unreal-engine/hardware-ray-tracing-in-unreal-engine) to be enabled for the project. The following system requirements must be met and these settings must be enabled.

System Requirements:

* Operating System: **Windows 10 1809 or later**
* GPU: **NVIDIA RTX and DXR driver-enabled GTX series graphics cards**

Project Settings:

[![Path Tracer Project Settings](https://dev.epicgames.com/community/api/documentation/image/6dfaaeee-2022-4de7-8d1a-bdc54e2b8c39?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6dfaaeee-2022-4de7-8d1a-bdc54e2b8c39?resizing_type=fit)

* Platforms > Windows > Targeted RHIs > Default RHI: **DirectX 12**
* Engine > Rendering > Hardware Ray Tracing: Enable **Path Tracing**
* Engine > Rendering > Hardware Ray Tracing: Enable **Support Hardware Ray Tracing**
* Engine > Rendering > Hardware Ray Tracing: Enable **Path Tracing**

  Unreal Engine 5 introduced settings that control the creation of path tracer specific shader permutations for materials. Projects which do not plan to use the path tracer at all can disable this setting to reduce shader compilation time.
* Engine > Rendering > Optimizations: Enable **Support Compute Skin Cache**

When Support Hardware Ray Tracing is enabled for the project, a pop-up window asks you to enable **Support Compute Skin Cache** if it is not already enabled. This is required to support hardware ray tracing and path tracing features.

Restart the engine for changes to take effect.

## Using the Path Tracer in the Level Editor

Enable the Path Tracer view in the Level Viewport by using the **View Modes** dropdown menu to select **Path Tracing**.

[![Level Viewport View Mode for Path Tracing](https://dev.epicgames.com/community/api/documentation/image/4f812c58-7d30-4bbf-9925-e5131ef400bb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4f812c58-7d30-4bbf-9925-e5131ef400bb?resizing_type=fit)

When enabled, the renderer progressively accumulates samples from the current view by continuously adding samples while the camera is not moving. When the target sample count is reached, the frame will be denoised (if denoising is enabled in the Post Process Setting) to remove any remaining noise present in the render.

In most cases, when the scene changes the samples are invalidated and the process starts again. Moving the camera, changing views, updating or changing materials on an object, and moving or adding objects to the scene will all result in the scene's samples being invalidated.

The Path Tracer can be used interactively and will quickly start to display pixels with shaded color as samples accumulate. The amount of time it takes to render largely depends on the complexity of the scene and the materials being sampled. Outdoor scenes tend to render more quickly as rays can escape with fewer and faster bounces. Interior scenes, especially those with materials with albedos close to 1.0, cause light paths to be longer and will therefore result in a longer render time.

## Using the Path Tracer with Movie Render Queue

This section goes into details about using the Movie Render Queue to generate a path-traced rendered output. For general usage and workflow information, see [Movie Render Queue](https://dev.epicgames.com/documentation/en-us/unreal-engine/movie-render-pipeline-in-unreal-engine#movie-render-queue) before proceeding.

The **Movie Render Queue** (or MRQ) is useful for production pipelines when producing high-quality rendered outputs. When combined with the Path Tracer, it allows for substantially higher quality renders than could be achieved otherwise.

The **Path Tracer** module enables the Path Tracer to be used to output rendered frames and it provides some settings specific to its rendering path.

[![Movie Render Queue Path Tracer Module Settings](https://dev.epicgames.com/community/api/documentation/image/30f14f14-64f6-40c3-97f6-2bd22574ba06?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/30f14f14-64f6-40c3-97f6-2bd22574ba06?resizing_type=fit)

**Post Process Volumes** placed in the Level also control specific path tracing functionality, such as the maximum number of ray bounces, support for emissive materials, and exposure.

MRQ also contains other settings modules that provide additional controls and options for achieving higher-quality renders.

* The [High Resolution](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine)  module provides settings to render frames as separate tiles that can be combined to render higher single frame resolutions than would otherwise be possible. Individual tiles can use up to the largest resolution supported by your graphics card (for example, 7680x4320 for RTX 3080 cards).
* The [Anti-aliasing](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine) module provides specific settings to adjust the sample counts per pixel and for better motion blur quality. This module provides warm-up times that can be required for level-loading and visual effects to render the scene accurately.

  + **Temporal Sample Count** interpolates several rendered frames at slightly offset instances in time, improving motion blur quality. This accumulation of samples happens after denoising occurs, helping stabilize residual artifacts from individual spatial passes. However, if **Reference Motion Blur** is enabled, all temporal samples will be taken before denoising. In this case, we recommend leaving Spatial Samples at 1 and driving all sampling through Temporal samples to maximize motion blur quality.
  + **Spatial Sample Count** sets the number of samples per pixel to use per temporal sample. Increasing the samples per pixel, decreases noise present in each render pass while increasing the time needed to render each frame. The Post Process Volume samples per pixel setting is ignored when using MRQ.
  + The total number of samples taken per pixel is the product of the spatial and temporal sample counts. Spreading the samples across both spatial and temporal can produce better results in some cases. For example, if you want to use 16 samples per pixel, you could apply 4 samples to spatial and 4 to temporal, or 16 to spatial and 1 to temporal, or 1 to spatial and 16 to temporal. Which is best depends mainly on the quality of motion blur desired. For stills, we recommend using all spatial samples (1 temporal) and for animations, we recommend using 1 spatial sample with many temporal samples with reference motion blur turned on.
* The [Console Variables](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine) module enables you to add any console variables that are relevant to your rendered frames. This includes overrides for quality, or toggling of some settings that would be relevant to the Path Tracer.
* The [Output](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-rendering-image-quality-settings-in-unreal-engine) module provides settings to configure the output directory, file name, image resolution, and the start / end frames you want to render.

### Path Tracer Post Process Volume Settings

Placed Post Process Volumes in the Level provide configurable properties for the Path Tracer. These include settings for the maximum number of light bounces, samples per pixel, anti-aliasing quality (or Filter Width), and more.

Settings for the Path Tracer can be found in the Post Process Volume Details panel under the **PathTracing** category.

[![Path Tracer Post Process Volume Settings](https://dev.epicgames.com/community/api/documentation/image/d04117cb-781a-4a47-b6e5-709968b2f634?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d04117cb-781a-4a47-b6e5-709968b2f634?resizing_type=fit)

Path Tracer Post Process Volume Settings

| Property | Description |
| --- | --- |
| **Max. Bounces** | Sets the maximum possible number of light bounces rays should travel before being terminated. |
| **Samples Per Pixel** | Sets the number of samples used per pixel for convergence. A higher number of samples reduces noise of the rendered image. |
| **Max Path Intensity** | Sets the maximum exposure allowed for path tracing in order to reduce [firefly artifacts](https://en.wikipedia.org/wiki/Fireflies_computer_graphics) from occurring. Adjusting the exposure to a higher value than the scene's exposure helps mitigate these artifacts.  (See the [Additional Information](https://dev.epicgames.com/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine#additional-information) section of this page for more details and an example of this type of artifact). |
| **Emissive Materials** | Should materials with Emissive Color set contribute to the lighting of the scene? When disabled, such colors will still be visible to camera rays, but will not emit light into the scene. This can be used to quickly decide if some contributions are double-counted such as with light fixtures that have modelled geo but are also represented by local light sources. For more fine-grained control, a **PathTracingRayTypeSwitch** node can be used inside the material. |
| **Reference Depth of Field** | Enables reference-quality depth of field, which replaces the post-process effect. This mode can correctly handle translucent surfaces, volumetrics and hair geometry. |
| **Reference Atmosphere** | Enables path tracing in the atmosphere instead of baking the Sky Atmosphere contribution into the skylight. Any Sky Light component present in the scene is automatically ignored when this setting is enabled.  Refer to the [Reference Atmosphere](https://dev.epicgames.com/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine#reference-atmosphere) section of this page. |
| **Denoiser** | This toggle uses the currently loaded denoiser plugin on the last sample to remove noise from the rendered output. By default, the NNE Denoiser plugin is used. This toggle has no effect on the rendered output if the denoiser plugin is not enabled. |
| **Lighting Components** | This section contains a number of checkboxes which can be used to limit the calculation of certain light paths, enabling selective output of the image. This can be used to decompose the image into multiple passes which will be guaranteed to add back up to the beauty later on. Indirect Emissive is slightly special in that it controls bounce lighting for emissive materials.  You might want to turn off this property to prevent double-counting illumination of surfaces that are also represented by actual light sources, or to reduce noise from small emitters.  For example, having an emissive material representing a small light bulb while also using a point or spot light source to illuminate the area would be double-counted in this case. |

### Rendering Lighting Components with MRQ

The Path Tracer can output individual lighting component renders (such as diffuse and specular) through callable Blueprint events with the Movie Render Queue.

To do this, you'll want to make an **Actor Blueprint** that contains a **Post Process Volume**. Set the volume to be **Infinite Extent (Unbound)** and give it a high **Priority** to ensure it's always chosen over any other post process volumes in the scene.

[![Post Process Volume Setting - Priority and Unbound](https://dev.epicgames.com/community/api/documentation/image/f951195d-89c2-4183-a6ae-ef58bb393ce9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f951195d-89c2-4183-a6ae-ef58bb393ce9?resizing_type=fit)

The purpose of this Post Process Volume is to set the desired Lighting Component Configuration through custom events in a Blueprint. These custom events can be executed through a Movie Pipeline Configuration File by using a **Start Console Command Track** and calling each event using the syntax `Ke * [Custom Event Name]`.

In the example below, the custom event named **RenderSpecular** is called by the Movie Pipeline Configuration with the console command `Ke * RenderSpecular`.

[![MRQ Lighting Pass Settings - Star Console Command](https://dev.epicgames.com/community/api/documentation/image/21517002-e799-4bbd-9010-07fe6d9ac034?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/21517002-e799-4bbd-9010-07fe6d9ac034?resizing_type=fit)

This process makes it easier to set up unique Lighting Component configurations depending on the needs of the project.

To run out multiple Lighting Component Renders, the shot must be called multiple times in MRQ — once for each desired pass configuration. Each item in the queue would need to reference a different Movie Pipeline Configuration, each of which calls a different custom event for setting up the Lighting Component (like the example below).

This setup requires the render to run multiple times, but keep in mind that the Path Tracer does have early outs, so there isn't a direct linear scale on render times while rendering multiple lighting component configurations.

[![MRQ Lighting Component Renders](https://dev.epicgames.com/community/api/documentation/image/f09d61ba-59df-428c-8bdc-eb60dfa3bc9a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f09d61ba-59df-428c-8bdc-eb60dfa3bc9a?resizing_type=fit)

In the Blueprint you created, you'll want to set up the following events:

|  |  |  |
| --- | --- | --- |
| [Ray Component Split](https://dev.epicgames.com/community/api/documentation/image/2500edfd-9b72-4e98-bfef-03dc55da6e8f?resizing_type=fit) | [Ray Path Split](https://dev.epicgames.com/community/api/documentation/image/41e61cee-0e60-4737-ab9b-b296eac8b71f?resizing_type=fit) | [Path Component Split](https://dev.epicgames.com/community/api/documentation/image/b72bb897-7445-45d2-a571-e1438060b584?resizing_type=fit) |
| Ray Component Split | Ray Path Split | Path Component Split |
| Click image for full size. | Click image for full size. | Click image for full size. |

## Limitations of the Path Tracer

The following are some of the current limitations of path tracing in Unreal Engine.

* **Bright Materials slow down interior renders**

  + Materials which have an albedo value close to 1.0, such as a bright white color, cause rendering of frames to take longer than needed because the Path Tracer needs to simulate the path of lights with many bounces. Interior scenes are especially susceptible to this because light rays can take longer to escape the environment before being terminated.

    The Path Tracer employs the Russian Roulette technique to terminate rays that aren't likely to contribute to the scene sooner. Rays that continuously bounce through the scene are less likely to happen because they are terminated by the Russian Roulette technique when possible. When a material's albedo uses a value close to 1.0, termination of the ray path is less likely to happen, and contributes to longer render times for the frame.
  + Materials that reflect all incoming light are rare in the real world, and these tend to have a washed out appearance to their surface. For this reason, it is recommended that you keep the Base Color below 0.8 for all diffuse materials.
* **Dynamic Scene Elements**

  + The Path Tracer works by having the renderer accumulate samples over time. This is ideal for static scenes and less so for dynamic scenes that include elements such as moving lights, animated skinned meshes, and visual effects. These types of elements do not invalidate path tracing in the editor and appear as blurred, or streaking artifacts in the frame. This only appears when working in the editor and is remedied by using the Movie Render Queue to render out final elements.

    Capturing a high resolution screenshot (see below) at a resolution different from the viewport is another way to work around this issue because it takes all samples without letting the engine tick time forward.
* **Path Tracing Material Quality Switch Nodes**

  + Optimizing materials for path tracing features by reducing their complexity using the **PathTracingQualitySwitch** node reduces complexity or workarounds used in standard materials. Since runtime is not a concern, compromises to the material are not needed. Using these nodes helps provide a compromise-free result without duplicating the material.
* **Ray Tracing Material Quality Switch Nodes**

  + Optimizing material for ray tracing features by reducing their complexity using the **Ray Tracing Quality Switch** node helps reduce their costs at runtime. This allows Unreal Engine's ray tracing features to use a simpler material compared to the deferred renderer.

    Since the Path Tracer is intended for high quality output, it uses the **Normal** port of these Switch nodes, despite being based on ray tracing. To control the behavior of materials specifically for the Path Tracer, use the **PathTracingQualitySwitch** node instead.
* **HDRIBackdrop is not compatible with the Path Tracer**

  + The current implementation of the HDRIBackdrop component leads to double-counted illumination in the Path Tracer and disables importance sampling of the HDRI lighting. It is recommended to use a Sky Light with a specified texture and setting the path tracer console variable `r.PathTracing.VisibleLights 2` to make the backdrop appear.

  This does not provide a shadow-catching ground plane.

## Supported Features of the Path Tracer

The limitations of the Path Tracer are either limitations of the current implementation or features that aren't planned for support. This list of features intends to give you an idea of what is currently supported with this current release. It is not a comprehensive list of all supported features / properties of the engine.

The Path Tracer shares the same code used with [Real-Time Ray Tracing](https://dev.epicgames.com/documentation/en-us/unreal-engine/hardware-ray-tracing-in-unreal-engine) features of Unreal Engine. In general, if a feature is supported by real-time ray tracing then it should be supported by the Path Tracer.

| Feature Name | Supported? | Additional Notes |
| --- | --- | --- |
| Geometry Types |  |  |
| **Nanite** | Yes | The Fallback Mesh is used for Nanite-enabled meshes by default. Lower the **Fallback Relative Error** parameter in the Static Mesh Editor to use more of the source mesh's triangles. (Experimental) Initial support for native path tracing of Nanite meshes is enabled when setting the console variable `r.RayTracing.Nanite.Mode 1`. This preserves all detail while using significantly less GPU memory than zero-error fallback meshes. |
| **Skinned Meshes** | Yes | Animations do not invalidate the path tracer, which can cause blurring, or streaking, to be visible in the viewport. Movie Render Queue should be used to output final images. |
| **World Position Offset-driven Animation** | Yes | **Evaluate World Position Offset** should be enabled on individual scene Actors. They do not invalidate the Path Tracer, which can cause blurring, or streaking, to be visible in the viewport. Movie Render Queue should be used to output final images. |
| **Hair Strands** | Yes | Hair Strand support is still considered experimental as it can require many resources to build efficient acceleration structures. The console variable `r.HairStrands.RaytracingProceduralSplits` can be used to balance between rendering performance and acceleration structure build performance (memory usage). The default value of 4 emphasizes rendering performance, but heavy grooms can lead to instability. If you experience GPU timeouts, try lowering this value to or reduce the number of hair segments in the groom. |
| **Landscape** | Yes |  |
| **Spline Meshes** | Yes |  |
| **Instanced Static Mesh** | Yes |  |
| **Hierarchical Instanced Static Mesh** | Yes |  |
| **Water Geometry** | Yes | This must be enabled by the console variable `r.RayTracing.Geometry.Water 1`. |
| Visual Effects |  |  |
| --- | --- | --- |
| **Niagara Particle Systems** | Yes | Particle systems do not invalidate the Path Tracer, causing blur / streaking to be visible in the viewport. Movie Render Queue should be used to output final images. |
| Light Types |  |  |
| --- | --- | --- |
| **Directional Light** | Yes |  |
| **Sky Light** | Yes | * Currently Sky Light capture is only visible when **Real Time Capture** is enabled.    + To improve render quality, increase the resolution of the Sky Light capture to be higher than used for real-time capture.   + If the illumination is coming from Sky Atmosphere and Volumetric Clouds, consider hiding any redundant skyboxes by making them invisible to ray tracing.   + For the best quality, enable **Reference Atmosphere** mode from the post process settings under the Path Tracer settings section. * When not using Real Time Capture mode, a sky box / sphere is expected to have sky representation. Its material must have the flag **Is Sky** enabled in the material's settings, otherwise its illumination will be double-counted against the skylighting — and is likely to produce noise since it won't be importance sampled. * Sky box / sphere shapes should also **not** cast shadows because they can occlude contributions from the Sky Light and Directional Light. |
| **Point Light** | Yes |  |
| **Spot Light** | Yes |  |
| **Rect Light** | Yes |  |
| Lighting Features/Properties |  |  |
| --- | --- | --- |
| **Emissive Materials** | Yes | Emissive parts that are small can introduce a lot of noise to the rendered scene. They can also cause double-counted lighting if the emissive parts have a light associated with them. Use the **Emissive Materials** checkbox in the Post Process Volume settings to disable them, or use the console variable `r.PathTracing.EnableEmissive 0`. |
| **Sky Atmosphere** | Yes | Requires a Sky Light in the scene which has **Real Time Capture** enabled on the component. Or, enabling the Post Process Volume setting **Reference Atmosphere**, which path traces the atmosphere instead of baking the Sky Atmosphere contribution into the Sky Light. Any Sky Light present in the scene is automatically ignored when this setting is enabled.  Refer to the [Fog and Atmosphere](https://dev.epicgames.com/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine#fog-and-atmosphere-volumetrics) section of this page. |
| **Volumetric Clouds** | Partially | Similar to Sky Atmosphere, this will either be captured by a skylight, or be represented natively when using **Reference Atmosphere** mode in the post process settings under Path Tracer Settings section. |
| **Exponential Height Fog** | Yes | Requires **Volumetric Fog** setting to be enabled. Not all controls are supported since some have non-physical meaning.  Refer to the [Fog and Atmosphere](https://dev.epicgames.com/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine#fog-and-atmosphere-volumetrics) section of this page. |
| **Volumetric Fog** | Yes | Must be enabled the on Exponential Height Fog component.  Refer to the [Fog and Atmosphere](https://dev.epicgames.com/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine#fog-and-atmosphere-volumetrics) section of this page. |
| **IES Profiles** | Yes |  |
| **Light Functions** | Yes | Also supports colored light functions when `r.PathTracing.LightFunctionColor` is enabled. |
| Post Processing |  |  |
| --- | --- | --- |
| **Depth of Field** | Yes | The path tracer renders its own depth pass rather than using the one generated by the rasterizer. This results in a more accurate match between the depth and RGB color results, improving post-processing passes that rely on depth. This does not affect the Reference Depth of Field option you can enable in the post process volume settings. |
| **Motion Blur** | Partially | The most accurate results can be obtained with Movie Render Queue when **Reference Motion Blur** is enabled on the **Path Tracing** module. This option enables more accurate motion blur with higher performance cost to get smooth results.  In this mode, no post-process vector blur is applied, and denoising is applied after all spatial and temporal sample accumulation. Higher temporal samples should be applied to increase quality. Be aware of the tick resolution limitations in Sequencer when using very high temporal sample counts. |
| Material Shading Models |  |  |
| --- | --- | --- |
| **Unlit** | Yes |  |
| **Default Lit** | Yes |  |
| **Subsurface** | Yes |  |
| **Preintegrated Skin** | Yes | Renders identically to the subsurface shading model. |
| **Alpha Holdout** | Yes |  |
| **Clear Coat** | Yes |  |
| **Subsurface Profile** | Yes | Requires a subsurface profile with **Burley** subsurface scattering enabled. |
| **Two Sided Foliage** | Yes |  |
| **Hair** | Yes | Support for this shading model is still considered **experimental** and has not yet been calibrated against the behavior of the **Lit** Shading Model. |
| **Cloth** | Yes |  |
| **Eye** | Yes |  |
| **SingleLayerWater** | Yes | Added experimental support for this shading model. Since the raster implementation is heavily dependent on post-processing, a close match is not currently possible. |
| **Thin Translucent** | Yes |  |
| **From Material Expression** | Yes |  |
| Material Features |  |  |
| --- | --- | --- |
| **Substrate Materials** | Yes | Initial support is implemented. [Substrate](https://dev.epicgames.com/documentation/en-us/unreal-engine/substrate-materials-in-unreal-engine?application_version=5.5) is experimental and still actively being developed. |
| **Sparse Volume Textures** | Partially | Initial support has been added. For information on setting up and using them, see [Sparse Volume Textures](https://dev.epicgames.com/documentation/en-us/unreal-engine/sparse-volume-textures-in-unreal-engine). |
| **Heterogeneous Volumes** | Partially | Initial support added. Sky Atmosphere not yet supported. For more information, see [Heterogeneous Volumes](https://dev.epicgames.com/documentation/en-us/unreal-engine/heterogeneous-volumes-in-unreal-engine). |
| **Colored Shadows** | Yes | Can be achieved with the **Thin Translucent** or solid glass.  See the [Glass Rendering with the Path Tracer](https://dev.epicgames.com/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine#glass-rendering-with-the-path-tracer) and [Color Absorption](https://dev.epicgames.com/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine#color-absorption) sections of this page. |
| **Translucent Shadows** | Yes |  |
| **Refraction** | Yes |  |
| **Decals** | Yes | Both DecalActors and Mesh decals are supported. |
| **Anisotropy** | Yes |  |
| System Support |  |  |
| --- | --- | --- |
| **Multiple GPU** | Yes | Requires a GPU that supports NVIDIA NvLink / SLI.  Refer to [Enabling Rendering using Multiple GPUs](https://dev.epicgames.com/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine#enabling-support-for-multiple-gp-us) section of this page. |
| **Sequencer Movie Render Queue** | Yes |  |
| **Orthographic Camera** | Yes |  |
| **Per Instance Custom Data** | Yes |  |
| **Per Instance Random Data** | Yes |  |

## Additional Information

The Path Tracing mode works differently than some other rendering methods within Unreal Engine. This means that something that works well for real-time rendering may not work best for path-traced rendering. The following sections describe some of these inconsistencies and common issues as well as the steps you can take to improve your results with the Path Tracer.

### Reducing Firefly Artifacts

The Path Tracer simulates light by randomly tracing rays according to material properties. When bright areas of the scene have a low probability of being discovered, the resulting samples can become excessively bright, creating specs of light (or fireflies) that appear and disappear within the frame. Path tracing attempts to minimize the most common sources of these effects, but they can still occur in some scenarios.

When the path-traced result is combined with bloom post processing passes, the resulting pixels can be particularly noticeable because of how they appear and disappear, or become brighter and dimmer.

The Post Process Setting **Max Path Intensity** controls the maximum intensity used in the rendered path-traced scene. 
The default values clamps fireflies fairly aggressively and should not need to be changed in most cases. Increasing the value will result in more accurate renders at the expense of more noise, while reducing the value can clamp even more aggressively at the expense of some energy loss. Note that the value here is relative to the current exposure, so can be kept constant in all cases.

### Denoising Options

When rendering frames with the path tracer interactively through the viewport, [Movie Render Graph](https://dev.epicgames.com/documentation/en-us/unreal-engine/movie-render-pipeline-in-unreal-engine#movie-render-graph), or with [Movie Render Queue](https://dev.epicgames.com/documentation/en-us/unreal-engine/movie-render-pipeline-in-unreal-engine#movie-render-queue) which will all have a bit of noise present in the frame. One way of reducing noise is by using a denoising algorithm to stabilize the end results, producing cleaner images with less noise.

The path tracer enables denoising through the **Post Process Volume** settings when **Denoiser** is enabled under the **Path Tracing** section.

There are two plugins available by default:

* **[NNE Denoise](https://dev.epicgames.com/documentation/en-us/unreal-engine/nne-denoiser-in-unreal-engine)** is the default implementation. It is based on the same network as Intel's Open Image Denoise but runs it on the GPU for improved performance. This is the default and recommended option.
* **NFOR** **Denoiser** is a denoiser optimized for animation rendering. It takes into account neighboring frames and can produce more stable results than the default denoiser when rendering animation sequences through Movie Render Queue.

In addition, there is also support for the following third-party denoising libraries:

* [Intel's Open Image Denoise](https://www.openimagedenoise.org/) library is a CPU-based denoiser that removes noise from the last sample taken and improves the quality of long-running frames. This produces identical results to the built-in NNE Denoiser.
* [NVIDIA Optix AI-Accelerated Denoiser](https://developer.nvidia.com/optix-denoiser) library is a GPU-accelerated artificial intelligence trained on tens of thousands of images to reduce visual noise, while providing faster denoising times. This may produce different results to the default denoiser; however it requires a NVidia GPU.

This is an comparative example with and without denoising applied to the frame:

![Without Denoising Applied](https://dev.epicgames.com/community/api/documentation/image/3ba6a2e1-8c0a-4ea7-98e1-cfdc867b59db?resizing_type=fit&width=1920&height=1080)

![With Denoising Applied](https://dev.epicgames.com/community/api/documentation/image/439415eb-9396-493e-9de8-773a567db441?resizing_type=fit&width=1920&height=1080)

Without Denoising Applied

With Denoising Applied

#### NNE Denoiser

The NNEDenoiser plugin is enabled by default.

This denoiser is a generic denoiser plugin with which arbitrary neural denoiser networks can be imported and run on different NNE runtimes. It comes with different versions of Intel's Open Image Denoiser (fast, balanced and high quality, each with and without alpha) that can run on either CPU or GPU. The default is set to the balanced preset with alpha that runs on GPU, providing interactive denoising at decent quality.

For more information on how to change the preset or add and enable your own neural denoiser, see [NNE Denoiser](https://dev.epicgames.com/documentation/en-us/unreal-engine/nne-denoiser-in-unreal-engine).

#### Open Image Denoise Plugin

This denoiser runs on the CPU and is not designed for interactive denoising, but rather to help improve the quality of long-running frames. This denoiser does not guarantee temporal consistency in all cases and may require a high number of samples per pixel for stable output. Temporal stability can be improved when using Movie Render Queue to increase the **Temporal Sample Count** in the **Anti-Aliasing** module settings.

#### Optix Denoise Plugin

This plugin is experimental

The **OptixDenoise** plugin must be enabled for your project from the **Plugins** browser.

This denoiser uses GPU-accelerated artificial intelligence to reduce visual noise, while providing faster denoising times. The denoiser also contains a temporal component which tries to reduce flickering in denoised animations.

When multiple plugins are enabled for your project, you must use console variables to choose which denoiser is used when **Denoiser** is enabled in the Post Process Volume settings. You can use the console variable `r.PathTracing.SpatialDenoiser.Type` to select whether spatial (0, default) or temporal (1) denoising is used. Set `r.PathTracing.Denoiser.Name` (for example, to `NNEDenoiser` (default) or `OIDN`) to select which denoiser is used when spatial denoising is enabled. Set `r.PathTracing.TemporalDenoiser.Name` (for example, to `NFOR` (default), `NNEDenoiser` or `OptiX`) to select which denoiser is used when temporal denoising is enabled.

### Skylighting with the Path Tracer

Skylighting is handled in two ways: using a traditional skybox with an applied sky material, or using the **Real Time Capture** mode of the Sky Light to capture the sky, atmosphere, and clouds in the scene.

|  |  |
| --- | --- |
|  |  |
| Skybox Mesh | Sky Light Real Time Capture |

Using a skybox to represent the sky requires a couple of things to be set up on the mesh and in the material for it to work well with the Path Tracer. First, the sky material must have the flag **Is Sky** enabled in the Material's **Details** panel settings. This ensures that the illumination of the skybox material won't be counted twice when the Sky Light is present in the scene. It also potentially reduces the amount of noise that can occur if the skybox were to in fact be counted twice.

[![Material setting Is Sky flag](https://dev.epicgames.com/community/api/documentation/image/c7cb5a17-b6cb-491c-b4c2-b51f27706ad2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c7cb5a17-b6cb-491c-b4c2-b51f27706ad2?resizing_type=fit)

In the Level, select the skybox Actor and use the **Details** panel to disable **Cast Shadows** to prevent the mesh from occluding contributions from the Sky Light and Directional Light in the scene.

[![Disable Shadows on SkyBox Mesh](https://dev.epicgames.com/community/api/documentation/image/d1c8f4fc-ad28-44aa-91d7-15880f3b4820?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d1c8f4fc-ad28-44aa-91d7-15880f3b4820?resizing_type=fit)

Alternatively, lighting contributions from the [Sky Atmosphere](https://dev.epicgames.com/documentation/en-us/unreal-engine/sky-atmosphere-component-in-unreal-engine) and [Volumetric Clouds](https://dev.epicgames.com/documentation/en-us/unreal-engine/volumetric-cloud-component-in-unreal-engine) systems can be captured by enabling **Real Time Capture** mode on the Sky Light. Because of this limitation for capturing skyboxes, Sky Atmosphere, and Volumetric Clouds for skylighting representation, their resolutions are dependent on the Sky Light **Cubemap Resolution**.

|  |  |
| --- | --- |
|  |  |
| Sky Light Cubemap Resolution: 128 (Default) | Sky Light Cubemap Resolution: 512 |

### Fog and Atmosphere Volumetrics

The Path Tracer supports volumetrics from Sky Atmosphere and Exponential Height Fog components.

#### Reference Atmosphere

When **Reference Atmosphere** is enabled in the Post Process Volume settings, the Sky Atmosphere lighting is computed volumetrically, giving more realistic results. While in this mode, any Sky Light in the scene is automatically ignored as the sky lighting is only influenced by local and Directional Light sources. The path tracer represents the planet as a very large sphere so that the correct shadowing is present, and so that the ground color is properly reflected in the bounced lighting onto the sky from all directions.

![Path-traced scene without Reference Atmosphere](https://dev.epicgames.com/community/api/documentation/image/fa5b570f-acb2-45e4-a943-036f7e40a2b1?resizing_type=fit&width=1920&height=1080)

![Path-traced scene with Reference Atmosphere](https://dev.epicgames.com/community/api/documentation/image/55353a91-fbb7-45e2-a43b-f4685520c857?resizing_type=fit&width=1920&height=1080)

Path-traced scene without Reference Atmosphere

Path-traced scene with Reference Atmosphere

Additional notes for using Reference Atmosphere:

* To use the **Sky Atmosphere** as intended, adjust its **Transform Mode** setting to **Planet Top at Component Transform**, and move the component down below your scene so that the planet's ground plane does not interfere with your scene.
* Volumetric Cloud components are now supported starting in Unreal Engine 5.6. By default, an approximate form of multiple scattering is used to ensure compatibility with the rasterization pipeline and to improve performance. True multiple scattering in clouds can be enabled using `r.PathTracing.CloudMultipleScatterMode 2` although this can substantially increase the rendering time. The default value of 1 uses the parameters configured in the Volumetric Advanced Output node in the cloud material.
* It is recommended that any skybox geometry be disabled when using reference atmosphere mode, unless they are scaled beyond the size of the planetary atmosphere (in which case they can be used to represent the moon, stars or other objects existing beyond the planet’s atmosphere. To hide the skybox only for the path tracer, the simplest is to mark the mesh as invisible to raytracing.
* Clouds will only cast shadows on geometry if this is enabled in the distant light representing the sun.

#### Volumetric Fog

Fog is supported when using an Exponential Height Fog component that has Volumetric Fog enabled.

[![](https://dev.epicgames.com/community/api/documentation/image/4fd33c90-bb70-49d1-90e6-5b17055cdb61?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4fd33c90-bb70-49d1-90e6-5b17055cdb61?resizing_type=fit)

Not all controls are supported as some of the parameters have non-physical meaning.The primary parameters supported are:

* Fog Density and Fog Height Falloff
* Scattering Distribution
* Albedo
* Extinction Scale
* View Distance

  + This used to limit the region of influence of the height fog since infinite extents can lead to long rendering times.

### Rendering of Heterogeneous Volumes

Heterogeneous volumes are rendered using either the Niagara Fluids plugin or by instancing Heterogeneous Volume actors in the scene that use a [Sparse Volume Texture](https://dev.epicgames.com/documentation/en-us/unreal-engine/sparse-volume-textures-in-unreal-engine) material.

[![Example of a path-traced heterogeneous volume generated from a Niagara fluids particle system.](https://dev.epicgames.com/community/api/documentation/image/f883541f-bc76-4955-91af-caada933b8cf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f883541f-bc76-4955-91af-caada933b8cf?resizing_type=fit)

For more information on rendering heterogeneous volumes with the path tracer, see [Heterogenous Volumes](https://dev.epicgames.com/documentation/en-us/unreal-engine/heterogeneous-volumes-in-unreal-engine) and [Sparse Volume Textures](https://dev.epicgames.com/documentation/en-us/unreal-engine/sparse-volume-textures-in-unreal-engine).

### Direct Visibility of Light Sources

Non-punctual light sources, such as Point Lights with a source radius, Rect Lights, and Sky Lights are not visible to direct camera rays by default. The exception to this is Sky Lights with **Real Time Capture** enabled.

Skylighting paired with skybox geometry and static, or specified, cubemaps are not typically seen by camera rays. This can be modified by setting the console variable `r.PathTracing.VisibleLights 1`.

All light sources are visible in reflections and refractions regardless of if the visible lights console variable is enabled. This ensures that they are seen by all possible ray paths. However, in some cases, this might cause unexpected behavior. For example, a Rect Light placed directly behind a glass window will be visible and will block the view through the window, which is only the case for true refraction, when the index of refraction is not equal to 1.

### Glass Rendering with the Path Tracer

#### Basic Glass Material

The basic material setup for glass in the path tracer depends on a few factors. The first decision which must be made is if the mesh to be shaded has been modeled with thickness or not. We will first look at the solid (or "thick") case first. In this case, we want to use the following settings on the material:

* Shading Model: Default Lit
* Blending Mode: Translucent
* Lighting Mode: Surface Forward Shading (to enable access to all shader parameters)
* Refraction Method: Index of Refraction

With this basic configuration in place, we can now make portions of the material refract light by setting Opacity to 0. You may think of the Opacity parameter as blending between the "Default Lit" shading model (which includes diffuse and specular) and a purely refractive shading model (representing clear glass). By default the refraction amount is automatically derived from the specular color. For finer grained control, you may plug a value into the "Index of Refraction" slot in the material to override this and control reflectivity independently from the ray bending effect of IOR. Here is an example of the simplest possible glass material:

[![Example of a basic glass material.](https://dev.epicgames.com/community/api/documentation/image/30171623-0d6b-4634-9dc0-88ecfbe09895?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/30171623-0d6b-4634-9dc0-88ecfbe09895?resizing_type=fit)

Click image for full size.

Let's now examine how we can achieve greater control over the glass shading by controlling the fresnel effect and refraction with independent IORs. Instead of using Specular which can only produce a SpecularColor of up to 0.08 (which corresponds to an IOR of roughly 1.8), we will drive specular color more directly by setting Metallic to 1.0 which lets SpecularColor=BaseColor. Then, we make use of the [formula](https://en.wikipedia.org/wiki/Fresnel_equations#Normal_incidence) **SpecularColor=((IOR-1)/(IOR+1))^2** to compute the appropriate SpecularColor given an Index of Refraction value. Here is an example material:

[![Example of glass material with more control.](https://dev.epicgames.com/community/api/documentation/image/f4b2224a-8bb7-486c-88a6-d698871bfde9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f4b2224a-8bb7-486c-88a6-d698871bfde9?resizing_type=fit)

Here is an example of the independent control of Specularity vs. Refraction:

![Drag the slider to see specularity changes to the glass material. Specular values are from 0 to 1.0 in 0.1 increments. These changes are equal to IOR values between 1.0 to 1.789.](https://dev.epicgames.com/community/api/documentation/image/a965e050-a498-4805-9a86-77ffdd836baf?resizing_type=fit&width=1920&height=1080)![Drag the slider to see specularity changes to the glass material. Specular values are from 0 to 1.0 in 0.1 increments. These changes are equal to IOR values between 1.0 to 1.789.](https://dev.epicgames.com/community/api/documentation/image/785cb3df-a559-4b35-9d02-1e0454c1e212?resizing_type=fit&width=1920&height=1080)![Drag the slider to see specularity changes to the glass material. Specular values are from 0 to 1.0 in 0.1 increments. These changes are equal to IOR values between 1.0 to 1.789.](https://dev.epicgames.com/community/api/documentation/image/316fa770-40cc-4033-ab4d-10d40da39aa5?resizing_type=fit&width=1920&height=1080)![Drag the slider to see specularity changes to the glass material. Specular values are from 0 to 1.0 in 0.1 increments. These changes are equal to IOR values between 1.0 to 1.789.](https://dev.epicgames.com/community/api/documentation/image/b56e39d9-31a3-46ae-b7a6-68de8009287c?resizing_type=fit&width=1920&height=1080)![Drag the slider to see specularity changes to the glass material. Specular values are from 0 to 1.0 in 0.1 increments. These changes are equal to IOR values between 1.0 to 1.789.](https://dev.epicgames.com/community/api/documentation/image/868ad768-548f-46dc-aaa8-febe756fc15c?resizing_type=fit&width=1920&height=1080)![Drag the slider to see specularity changes to the glass material. Specular values are from 0 to 1.0 in 0.1 increments. These changes are equal to IOR values between 1.0 to 1.789.](https://dev.epicgames.com/community/api/documentation/image/e85aa2b8-6bf5-44f5-80f9-daabc27ed525?resizing_type=fit&width=1920&height=1080)![Drag the slider to see specularity changes to the glass material. Specular values are from 0 to 1.0 in 0.1 increments. These changes are equal to IOR values between 1.0 to 1.789.](https://dev.epicgames.com/community/api/documentation/image/debb2b8c-ee67-4033-bbdd-0f5d30276627?resizing_type=fit&width=1920&height=1080)![Drag the slider to see specularity changes to the glass material. Specular values are from 0 to 1.0 in 0.1 increments. These changes are equal to IOR values between 1.0 to 1.789.](https://dev.epicgames.com/community/api/documentation/image/fccbdcec-76a3-4028-8601-6649821673a0?resizing_type=fit&width=1920&height=1080)![Drag the slider to see specularity changes to the glass material. Specular values are from 0 to 1.0 in 0.1 increments. These changes are equal to IOR values between 1.0 to 1.789.](https://dev.epicgames.com/community/api/documentation/image/5cfb836a-0d60-427a-a42a-0f1e9f7493fe?resizing_type=fit&width=1920&height=1080)![Drag the slider to see specularity changes to the glass material. Specular values are from 0 to 1.0 in 0.1 increments. These changes are equal to IOR values between 1.0 to 1.789.](https://dev.epicgames.com/community/api/documentation/image/1f949945-88f8-4ddb-9092-7656311f28e9?resizing_type=fit&width=1920&height=1080)![Drag the slider to see specularity changes to the glass material. Specular values are from 0 to 1.0 in 0.1 increments. These changes are equal to IOR values between 1.0 to 1.789.](https://dev.epicgames.com/community/api/documentation/image/e3fd4eca-e2c4-4041-a371-0b162d91b371?resizing_type=fit&width=1920&height=1080)

**Drag the slider to see specularity changes to the glass material. Specular values are from 0 to 1.0 in 0.1 increments. These changes are equal to IOR values between 1.0 to 1.789.**

![Drag the slider to see specularity changes to the glass material. Specular values are from 0 to 1.0 in 0.1 increments.](https://dev.epicgames.com/community/api/documentation/image/1f359881-9d07-4701-8919-6b4a9266a889?resizing_type=fit&width=1920&height=1080)![Drag the slider to see specularity changes to the glass material. Specular values are from 0 to 1.0 in 0.1 increments.](https://dev.epicgames.com/community/api/documentation/image/25e96648-a6c0-4594-aaee-ac9c03ebb2d5?resizing_type=fit&width=1920&height=1080)![Drag the slider to see specularity changes to the glass material. Specular values are from 0 to 1.0 in 0.1 increments.](https://dev.epicgames.com/community/api/documentation/image/5cfef889-d50b-4d73-b49a-463e2a3b080b?resizing_type=fit&width=1920&height=1080)![Drag the slider to see specularity changes to the glass material. Specular values are from 0 to 1.0 in 0.1 increments.](https://dev.epicgames.com/community/api/documentation/image/403b8912-4e6b-4f39-8095-4f2be4544c3b?resizing_type=fit&width=1920&height=1080)![Drag the slider to see specularity changes to the glass material. Specular values are from 0 to 1.0 in 0.1 increments.](https://dev.epicgames.com/community/api/documentation/image/1a612a0f-3e81-409b-b57e-77955d8659b4?resizing_type=fit&width=1920&height=1080)![Drag the slider to see specularity changes to the glass material. Specular values are from 0 to 1.0 in 0.1 increments.](https://dev.epicgames.com/community/api/documentation/image/21136fec-ce8d-402f-86aa-32e8d31f3fa8?resizing_type=fit&width=1920&height=1080)![Drag the slider to see specularity changes to the glass material. Specular values are from 0 to 1.0 in 0.1 increments.](https://dev.epicgames.com/community/api/documentation/image/e2214061-b194-4e81-b75f-1d6053299b88?resizing_type=fit&width=1920&height=1080)![Drag the slider to see specularity changes to the glass material. Specular values are from 0 to 1.0 in 0.1 increments.](https://dev.epicgames.com/community/api/documentation/image/df9d073d-1e98-411b-9fc4-bf8de087e404?resizing_type=fit&width=1920&height=1080)![Drag the slider to see specularity changes to the glass material. Specular values are from 0 to 1.0 in 0.1 increments.](https://dev.epicgames.com/community/api/documentation/image/c95cb74c-2df1-4e26-8ce4-56ebf1a9f49d?resizing_type=fit&width=1920&height=1080)![Drag the slider to see specularity changes to the glass material. Specular values are from 0 to 1.0 in 0.1 increments.](https://dev.epicgames.com/community/api/documentation/image/705aca9b-72f0-4a16-a7ef-d5797d5798b4?resizing_type=fit&width=1920&height=1080)![Drag the slider to see specularity changes to the glass material. Specular values are from 0 to 1.0 in 0.1 increments.](https://dev.epicgames.com/community/api/documentation/image/28a6ebd3-3b26-47d5-876d-cfe1d06fdb50?resizing_type=fit&width=1920&height=1080)

**Drag the slider to see specularity changes to the glass material. Specular values are from 0 to 1.0 in 0.1 increments.**

#### Thin Translucency Shading Model

The **Thin Translucency** shading model is useful for achieving physically accurate results when the object does not have any thickness (for instance if a pane of glass is represented with a single flat polygon). The setup for thin glass material is largely the same as above, the only changes to be made are:

* Shading Model: Thin Translucent
* Add a **Thin Translucent Material** node to control the color (see section below on Color Absorption)

All other behavior between solid and thin cases is the same. One important difference however is that in the thin case, the index of refraction does not actually change the direction of the ray when roughness is low. However, it does have a subtle effect on the reflectivity and transmission amounts, as well as controlling the ratio between reflection roughness and transmission roughness. As the Index of Refraction gets closer to 1, the transmission roughness will decrease, while the reflected roughness will stay the same. This effect can be seen by comparing the result to a thin slab of glass using a solid glass material.

In both cases, if the Refraction Method is not set to **Index Of Refraction**, the path tracer will use transparency instead of refraction. Transparency does not count as a scattering event and therefore does not count towards the number of bounces. It also means that the roughness is not applied in these modes.

|  |  |
| --- | --- |
|  |  |
| Solid Glass Material | Thin Translucent Glass Material |
| Click image for full size view. | Click image for full size view. |

#### Color Absorption

Controlling the color of the transmission through the glass (also known as "Beer's law"), can be done by using the **Absorption Medium** material output node in the Material Graph for solid glass materials. This feature is only available for the Path Tracer as it requires tracking the state of the ray color through multiple bounces.

To add this feature to the solid glass examples above, you can add a small additional set of nodes to the material like the material example below.

[![Color Absoprtion material example.](https://dev.epicgames.com/community/api/documentation/image/b163b357-e898-4237-acb4-5783da30d45a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b163b357-e898-4237-acb4-5783da30d45a?resizing_type=fit)

When setting a RGB color, values close to **1** will not demonstrate absorption.

The example material above uses **Transmittance Color** to control the amount of absorption that is happening. The specified color is normalized to be reached after a distance of 100 units. To change this distance, use the following formula `Transmittance Color = Color^(100/Distance)`.

|  |  |  |  |
| --- | --- | --- | --- |
|  |  |  |  |
| Absorption: 0x | Absorption: 1x | Absorption: 10x | Absorption: 100x |

Controlling the absorption through thin glass is done through the "Thin Translucent Output" node. Here, the transmission color is relative to a virtual thickness so the distance control can be simplified to a relative one:

[![Thin translucency with color absoprtion example.](https://dev.epicgames.com/community/api/documentation/image/06b8321b-53bd-4519-9d6d-3ea95d20ca2c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/06b8321b-53bd-4519-9d6d-3ea95d20ca2c?resizing_type=fit)

#### Energy Conservation

The Unreal Engine 5 implementation of Energy Conservation is used to reduce the energy loss in the specular lobe of metals and glass materials.

You can turn on Energy Conservation from the Project Settings under the Engine > Rendering > Materials section.

To preserve backwards compatibility this feature is currently disabled by default. In a future release of the engine, this feature is expected to be enabled by default.

![Energy Conservation: Disabled](https://dev.epicgames.com/community/api/documentation/image/3963536b-e6be-4dcc-967f-e0bcb078ac48?resizing_type=fit&width=1920&height=1080)

![Energy Conservation: Enabled](https://dev.epicgames.com/community/api/documentation/image/0b49c368-2f3d-40d1-99bb-0f379ca68299?resizing_type=fit&width=1920&height=1080)

Energy Conservation: Disabled

Energy Conservation: Enabled

#### Approximate Caustics

The Path Tracer uses approximate caustic paths to help reduce noise, especially in cases where a glass or metal surface has lower roughness values. For these types of materials, the reflective caustics can produce various patterns and can take up an impractical amount of time, or samples, to converge for a noise-free image.

For example, these images were taken sequentially during the rendering and sample accumulation process with the final image being the finished and denoised result.

[![Examples of Approximate Caustics.](https://dev.epicgames.com/community/api/documentation/image/70eba8d8-3847-48e3-812f-bd6443ccce4a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/70eba8d8-3847-48e3-812f-bd6443ccce4a?resizing_type=fit)

Click image for full size.

Because caustics generally take a long time to converge to a noise-free result, the Path Tracer reduces image noise by approximating the caustics that would be present in the image using the console command `r.PathTracing.ApproximateCaustics 1`. This variable is enabled by default.

![Approximate Caustics: Disabled](https://dev.epicgames.com/community/api/documentation/image/a8a173e4-7e3e-456c-b0cb-03c4c2f28f61?resizing_type=fit&width=1920&height=1080)

![Approximate Caustics: Enabled](https://dev.epicgames.com/community/api/documentation/image/910323d4-3480-426c-991a-d247c5aa2039?resizing_type=fit&width=1920&height=1080)

Approximate Caustics: Disabled

Approximate Caustics: Enabled

Another element to consider is the difference between refractive caustics and approximate caustics. By using the denoiser, it is possible to preview how the caustics would appear given enough time to converge, whereas the approximate caustics gives a production-ready image in much shorter time.

![Refractive Caustics | Approximate Caustics: Disabled](https://dev.epicgames.com/community/api/documentation/image/7a4872e7-fec4-4897-8f28-73a7afc36ca0?resizing_type=fit&width=1920&height=1080)

![Refractive Caustics | Approximate Caustics: Enabled](https://dev.epicgames.com/community/api/documentation/image/249349a6-4b85-4fc8-863e-786cacc2473c?resizing_type=fit&width=1920&height=1080)

Refractive Caustics | Approximate Caustics: Disabled

Refractive Caustics | Approximate Caustics: Enabled

### Rough Light Transmission and Reflections

The Path Tracer is unique in that it allows for the rendering of rough transmission in addition to rough reflection — and in the case of the Path Tracer, these shader parameters are coupled together.

In the examples below, the roughness value of the glass material varies to demonstrate the approximate caustics, roughness of the reflection, and the effect it has on the translucent shadow being cast.

![Drag the slider to see the glass material change from no roughness to some roughness. Roughness values are from 0 to 0.2](https://dev.epicgames.com/community/api/documentation/image/5642e846-498a-4c0c-a69b-fac297d50c8f?resizing_type=fit&width=1920&height=1080)![Drag the slider to see the glass material change from no roughness to some roughness. Roughness values are from 0 to 0.2](https://dev.epicgames.com/community/api/documentation/image/c87eabaf-39b0-4d8a-b4e2-388461bf0bdd?resizing_type=fit&width=1920&height=1080)![Drag the slider to see the glass material change from no roughness to some roughness. Roughness values are from 0 to 0.2](https://dev.epicgames.com/community/api/documentation/image/c5a9560c-2962-4dd8-9b80-e9ca2d939372?resizing_type=fit&width=1920&height=1080)![Drag the slider to see the glass material change from no roughness to some roughness. Roughness values are from 0 to 0.2](https://dev.epicgames.com/community/api/documentation/image/23a17549-3e97-44a6-a17c-7008ecae5626?resizing_type=fit&width=1920&height=1080)![Drag the slider to see the glass material change from no roughness to some roughness. Roughness values are from 0 to 0.2](https://dev.epicgames.com/community/api/documentation/image/b0cb68ef-7c53-4042-908a-ce77a9b15864?resizing_type=fit&width=1920&height=1080)![Drag the slider to see the glass material change from no roughness to some roughness. Roughness values are from 0 to 0.2](https://dev.epicgames.com/community/api/documentation/image/2c4d5a12-cb11-47b3-a590-fb255cecd397?resizing_type=fit&width=1920&height=1080)

**Drag the slider to see the glass material change from no roughness to some roughness. Roughness values are from 0 to 0.2**

### Ray Type Switch Material Node

The **Path Tracing Ray Type Switch** node can be used to replace material information for shadows, indirect specular, volume, and diffuse rays.

[![Path Tracer Ray Type Switch Material Node](https://dev.epicgames.com/community/api/documentation/image/ea38833c-6b00-40f1-88a6-dafe73117495?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ea38833c-6b00-40f1-88a6-dafe73117495?resizing_type=fit)

| Input Options | Description |
| --- | --- |
| **Main** | Used for camera rays, or non-path traced shading. |
| **Shadow** | Used by the path tracer on shadow rays, and only applies for materials using non-opaque blend modes. |
| **IndirectDiffuse** | Used by the path tracer on indirect diffuse rays replacing their color. |
| **IndirectSpecular** | Used by the path tracer on indirect specular rays replacing their color. |
| **IndirectVolume** | Used by the path tracer on indirect volume rays replacing their color. |

The example scene below shows two materials set up using the Path Tracing Ray Type Switch node: an opaque and a translucent material. The opaque material is applied to the sphere and shows the indirect specular reflecting the material as blue and the indirect lighting around the red sphere is now green. And, the translucent checkerboard material replaces its shadow with a masked texture sample.

[![Example scene using ray type switch on various materials.](https://dev.epicgames.com/community/api/documentation/image/965a3412-39cf-4c0d-b87f-0d27b80076bb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/965a3412-39cf-4c0d-b87f-0d27b80076bb?resizing_type=fit)

|  |  |
| --- | --- |
|  |  |
| Opaque material replacing indirect specular and indirect diffuse. | Translucent material replacing shadow cast by material. |

### Post Process Material Buffers

Post-process material buffers include additional outputs for use with the path tracer. These buffers are accessible through the **Path Tracing Buffer Texture** material expression. This node provides data for radiance, denoised radiance, albedo, normal, and variance. Use the Details panel to select the type of buffer you want to apply to the node in your material graph.

[![Path Tracer Buffer Texture Material Expression](https://dev.epicgames.com/community/api/documentation/image/b9601972-fbaf-423b-b568-65d11decfe93?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b9601972-fbaf-423b-b568-65d11decfe93?resizing_type=fit)

| Property | Description |
| --- | --- |
| **Radiance** | The raw radiance. |
| **Denoised Radiance** | Stores the denoised radiance if denoising is turned on in the post processing settings for the path tracer, and completes for the current frame, otherwise it is black. |
| **Albedo** | Average albedo at the current sample count. |
| **Normal** | Average normal at the current sample count. |
| **Variance** | Path tracing variance stored as standard derivation. Variance can be per channel variance or variance of luminance, albedo, and normal based on the path tracing configuration. Hooking up this buffer incurs additional cost. |

### DBuffer Decal Material Expressions

DBuffer material expressions are useful in setting up decal materials that provide a wider response than just translucent and alpha composite blend modes. These nodes read texture data from the DBuffer directly into the material graph, providing customizable flexibility for your decal materials, such as recreating an approximation of legacy behavior or more complex lighting interactions.

For more information about using these expressions in materials, see the “DBuffer Material Expressions” section of [Decal Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/decal-materials-in-unreal-engine).

## Useful Console Variables

The following are some useful console variables to have enabled when using the Path Tracer.

| Console Variable | Description |
| --- | --- |
| `r.PathTracing.VisibleLights` | Makes all lights visible to camera rays. This is disabled by default to match the raster-based modes of the engine, but it can be useful to understand how lights are modeled and to spot cases where lights are overlapping. Setting this to 2 will make only the Skylight visible |
| `r.PathTracing.ProgressDisplay` | This adds a small progress bar to the view that displays progress toward the configured samples per pixel. The progress bar will automatically be hidden when accumulation is completed. It does not affect renders with Movie Render Queue and is safe to leave on all the time. This is enabled by default. |
| `r.PathTracing.Denoiser` | This option can be used to quickly toggle the denoiser on and off (assuming the current sample accumulation is complete). Unlike the Post Process Volume setting, changing this will not cause accumulation to restart and can be useful for quickly comparing the rendered frame with and without denoising enabled. |
| `r.PathTracing.HeterogeneousVolumes` | This option enables the usage of heterogeneous volume rendering with the path tracer. For more usage information of heterogeneous volumes and the path tracer, see [Heterogeneous Volumes](https://dev.epicgames.com/documentation/en-us/unreal-engine/heterogeneous-volumes-in-unreal-engine). |

## Frequently Asked Questions

### Capturing a Converged Path-Traced Image using HighResShot

Use the console variable `r.HighResScreenshotDelay` equal to the currently active **Samples Per Pixel** in your scene. A good way to validate that the correct output is being captured is to leave `r.PathTracing.ProgressDisplay` set to 1. If the progress bar is not present in the captured image, sample accumulation is complete.

### Enabling the Path Tracer at Runtime

The Path Tracer can be invoked at runtime on supported hardware and platforms using the **Enable Path Tracing** Blueprint node.

[![Blueprint node to enable path tracer at runtime.](https://dev.epicgames.com/community/api/documentation/image/260de8aa-64c6-487c-a1d1-3ae9b60a3b22?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/260de8aa-64c6-487c-a1d1-3ae9b60a3b22?resizing_type=fit)

### Avoiding Timeout Delays on Windows for "D3D Device Removed Crashes"

Windows tries to maintain system responsiveness by limiting the amount of time a GPU kernel can take. For a resource intensive process, such as brute force path tracing, this limit can be hit more frequently, particularly on lower end GPUs or when light simulation becomes too complex to finish in a reasonable time.

The engine exposes a few console variables to control the amount of work performed at once, though these variables can reduce overall performance if set incorrectly. It's recommended to keep watch on overall performance with the `stat gpu` command.

* `r.PathTracing.DispatchSize` controls the maximum width and height in pixels for the path-traced render. If this value is lower than your viewport or image resolution, the render may take place in several steps, which increases the amount of times Windows can verify that the GPU is still responsive. The default is 2048.
* `r.PathTracing.FlushDispatch` controls how frequently to flush the command list during the path tracing process. Setting this to 1 gives Windows more chances to verify the GPU is still responsive. By default, this is set to 2.

In extreme cases, it may be difficult to maintain good performance while avoiding crashes. In such cases, it is possible to change the Windows Timeout limit itself. See [How to Fix a GPU Driver Crash](https://dev.epicgames.com/documentation/en-us/unreal-engine/dealing-with-a-gpu-crash-when-using-unreal-engine).

For scenes containing hair, it is possible for acceleration structure (BLAS) timeouts to occur. In this case, try lowering the value of `r.HairStrands.RaytracingProceduralSplits` to **1** or **2**.

### Instances Disappearing in the Path-Traced View

The default culling implementation for Hardware Ray Tracing can be overly aggressive in the context of path tracing, since ray tracing is also used for camera visibility. If instances appear to be missing when switching to the Path Tracer view, try setting `r.RayTracing.Geometry.InstancedStaticMeshes.Culling` to **0**.

### Using Path Tracer with Nanite-Enabled Meshes

There is experimental support for native path tracing of Nanite-enabled meshes which can be enabled with `r.RayTracing.Nanite.Mode 1`. This mode uses the Nanite streaming system to prepare ray-traced meshes on-the-fly, preserving much more detail than is possible for Fallback Meshes.

The path tracer also supports the Nanite-enabled meshes Fallback Mesh for representation. The Fallback Mesh uses a percentage of the source mesh's triangles for representation but leads to Nanite-enabled meshes having lower detail in the scene. Increase the Fallback Mesh's detail in the Static Mesh Editor by adjusting the **Fallback Triangle Percent** and **Fallback Relative Error** parameters.

For more information on configuring these settings, see the [Fallback Mesh section of the Nanite documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.5#fallback-mesh).

### Enabling Support for Multiple GPUs

Requires Windows 10 version 2004 or newer to use multiple GPUs.

Computing lighting with multiple GPUs (mGPU) is supported through NVIDIA's Scalable Link Interface (SLI) technology that links multiple NVIDIA GPUs together. This improves the amount of processing power that is needed to render scenes using core Hardware Ray Tracing features, such as the Path Tracer and GPU Lightmass.

Enable support for multiple GPU configurations by:

* Connecting GPUs with NVLink bridges and enabling SLI in the NVIDIA Control Panel.
* Pass the command line argument `-MaxGPUCount=N`, where N is the number of GPUs available. For example, `-MaxGPUCount=2`.
* With the editor open, use the console variable `r.PathTracing.MultiGPU 1` to enable multi-GPU support. You can also add this console variable to your **DefaultEngine.ini** file located in **[Unreal Engine Root]/Engine/Config** under the `[/Script/Engine.RendererSettings]`.

Once the editor opens, you can check the **Output Log** to confirm that multi-GPU mode has been enabled. Look for `LogD3D12RHI: Enabling multi-GPU with 2 nodes`.

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [lighting](https://dev.epicgames.com/community/search?query=lighting)
* [path tracer](https://dev.epicgames.com/community/search?query=path%20tracer)
* [automotive](https://dev.epicgames.com/community/search?query=automotive)
* [architecture](https://dev.epicgames.com/community/search?query=architecture)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Benefits of the Path Tracer](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#benefits-of-the-path-tracer)
* [Path-Traced Examples](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#path-traced-examples)
* [Enabling the Path Tracer in Your Project](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#enabling-the-path-tracer-in-your-project)
* [Using the Path Tracer in the Level Editor](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#using-the-path-tracer-in-the-level-editor)
* [Using the Path Tracer with Movie Render Queue](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#using-the-path-tracer-with-movie-render-queue)
* [Path Tracer Post Process Volume Settings](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#path-tracer-post-process-volume-settings)
* [Rendering Lighting Components with MRQ](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#rendering-lighting-components-with-mrq)
* [Limitations of the Path Tracer](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#limitations-of-the-path-tracer)
* [Supported Features of the Path Tracer](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#supported-features-of-the-path-tracer)
* [Additional Information](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#additional-information)
* [Reducing Firefly Artifacts](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#reducing-firefly-artifacts)
* [Denoising Options](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#denoising-options)
* [NNE Denoiser](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#nne-denoiser)
* [Open Image Denoise Plugin](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#open-image-denoise-plugin)
* [Optix Denoise Plugin](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#optix-denoise-plugin)
* [Skylighting with the Path Tracer](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#skylighting-with-the-path-tracer)
* [Fog and Atmosphere Volumetrics](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#fog-and-atmosphere-volumetrics)
* [Reference Atmosphere](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#reference-atmosphere)
* [Volumetric Fog](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#volumetric-fog)
* [Rendering of Heterogeneous Volumes](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#rendering-of-heterogeneous-volumes)
* [Direct Visibility of Light Sources](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#direct-visibility-of-light-sources)
* [Glass Rendering with the Path Tracer](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#glass-rendering-with-the-path-tracer)
* [Basic Glass Material](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#basic-glass-material)
* [Thin Translucency Shading Model](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#thin-translucency-shading-model)
* [Color Absorption](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#color-absorption)
* [Energy Conservation](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#energy-conservation)
* [Approximate Caustics](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#approximate-caustics)
* [Rough Light Transmission and Reflections](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#rough-light-transmission-and-reflections)
* [Ray Type Switch Material Node](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#ray-type-switch-material-node)
* [Post Process Material Buffers](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#post-process-material-buffers)
* [DBuffer Decal Material Expressions](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#d-buffer-decal-material-expressions)
* [Useful Console Variables](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#useful-console-variables)
* [Frequently Asked Questions](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#frequently-asked-questions)
* [Capturing a Converged Path-Traced Image using HighResShot](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#capturing-a-converged-path-traced-image-using-high-res-shot)
* [Enabling the Path Tracer at Runtime](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#enabling-the-path-tracer-at-runtime)
* [Avoiding Timeout Delays on Windows for "D3D Device Removed Crashes"](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#avoiding-timeout-delays-on-windows-for-d3-d-device-removed-crashes)
* [Instances Disappearing in the Path-Traced View](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#instances-disappearing-in-the-path-traced-view)
* [Using Path Tracer with Nanite-Enabled Meshes](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#using-path-tracer-with-nanite-enabled-meshes)
* [Enabling Support for Multiple GPUs](/documentation/en-us/unreal-engine/path-tracer-in-unreal-engine?application_version=5.7#enabling-support-for-multiple-gp-us)
