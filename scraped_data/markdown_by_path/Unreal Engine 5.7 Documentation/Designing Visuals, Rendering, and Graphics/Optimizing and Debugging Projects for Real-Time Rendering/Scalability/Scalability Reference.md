<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/scalability-reference-for-unreal-engine?application_version=5.7 -->

# Scalability Reference

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
6. [Optimizing and Debugging Projects for Real-Time Rendering](/documentation/en-us/unreal-engine/optimizing-and-debugging-projects-for-realtime-rendering-in-unreal-engine "Optimizing and Debugging Projects for Real-Time Rendering")
7. [Scalability](/documentation/en-us/unreal-engine/scalability-in-unreal-engine "Scalability")
8. Scalability Reference

# Scalability Reference

Scalability options, properties, and console variables.

![Scalability Reference](https://dev.epicgames.com/community/api/documentation/image/ca6f5549-119a-4d57-a421-abecd3c1070d?resizing_type=fill&width=1920&height=335)

 On this page

The Scalability settings provide a way for you to adjust the quality of various features in order to maintain the best performance for your game on different platforms and hardware.

## Scalability Settings

You can access the Scalability settings in the editor through the Viewport **Performance and Scalability** menu. The **Viewport Scalability** settings contain shortcuts to the most commonly-used settings defined in the `BaseScalability.ini` file, while **Material Quality Level** sets the global material quality setting.

[![Viewport Performance and Scalability menu and Scalability Groups window](https://dev.epicgames.com/community/api/documentation/image/a0e95651-99b1-4572-bfa6-935ee3456a88?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a0e95651-99b1-4572-bfa6-935ee3456a88?resizing_type=fit)

## Resolution Scale

Unreal Engine can render a scene in lower resolution and scale the image up to the target resolution. As 2D User interfaces usually cost less performance and suffer more from lower resolution, Unreal Engine does not apply this technique to UI. There is a minor cost for the up-sampling pass, but usually, it is worth the effort.

[![AA resolution scale comparison](https://dev.epicgames.com/community/api/documentation/image/034b25e1-6361-43e1-9f7b-a55d73ff0b11?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/034b25e1-6361-43e1-9f7b-a55d73ff0b11?resizing_type=fit)

Left: 50% no AA, Middle: 50% with AA, Right: 100% (no resolution scale) with AA

Having a softer input image helps the up-sampling step. This means this scalability options benefits from another scalability option: the anti-aliasing quality.

You can access this setting with the **r.ScreenPercentage** console variable. It takes in a value from 10-100 with -1 also equaling 100%.

## View Distance

Objects can be culled based on their distance to the viewer. By default, all objects are not distance culled (desired max draw distance of 0). On top of the designer specified value, there is a global scalability setting that works like a multiplier (**r.ViewDistanceScale**). Here you can see some grass objects (desired max draw distance of 1000):

[![View distance examples](https://dev.epicgames.com/community/api/documentation/image/06c8d50b-2840-4d89-913e-017f75e082fb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/06c8d50b-2840-4d89-913e-017f75e082fb?resizing_type=fit)

left: r.ViewDistanceScale 0.4, middle: r.ViewDistanceScale 0.7, right: r.ViewDistanceScale 1.0 (default)

## Anti-Aliasing

[![AA settings examples](https://dev.epicgames.com/community/api/documentation/image/56a02d1d-d927-4c43-9904-7f2679200d18?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/56a02d1d-d927-4c43-9904-7f2679200d18?resizing_type=fit)

From the left: r.PostProcessAAQuality 0 to 6. The first 3 equal the Low, Medium, High, Epic settings in the Scalability Groups > AA (TSR) settings.

Adjusting the anti-aliasing quality level using the **r.PostProcessAAQuality** console command adjusts the quality of whichever anti-aliasing method you are using (FXAA or temporal AA).

* For either anti-aliasing method, a value of 0 used with **r.PostProcessAAQuality** disables the effect.
* For FXAA, the effect of values 2, 4, and 6, can be seen in the above image; the smoothing of jagged edges becomes better and better.
* Values above 6 have no effect.

For temporal AA, there is a trade off between fill speed of the effect and quality, the higher the value you use:

* *r.PostProcessAAQuality* 2 with temporal AA is fast to settle but jitter caused by the effect will be more pronounced.
* *r.PostProcessAAQuality* 4 settles slower but does not jitter.

## Post Processing - sg.PostProcessQuality

[![Post process quality settings examples](https://dev.epicgames.com/community/api/documentation/image/7690821d-72a7-4310-8d25-5bbc67450210?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7690821d-72a7-4310-8d25-5bbc67450210?resizing_type=fit)

sg.PostProcessQuality set from 0 on the left to 3 on the right.

The **Scalability Groups > Post Processing** option adjusts the quality of the post processing effects in accordance with the settings found in the `BaseScalability.ini` file located in the folder at `[UE_InstallPath]/Engine/Config`. The **Low** setting equates to  *sg.PostProcessQuality* 0  and **Epic** to *sg.PostProcessQuality* 3.

| sg.PostProcessQuality 0 | sg.PostProcessQuality 1 |
| --- | --- |
| Config  ``` r.MotionBlurQuality=0  r.BlurGBuffer=0  r.AmbientOcclusionLevels=0  r.AmbientOcclusionRadiusScale=1.7  r.DepthOfFieldQuality=0 ```  Expand code  Copy full snippet(25 lines long) | Config  ``` r.MotionBlurQuality=3  r.BlurGBuffer=0  r.AmbientOcclusionLevels=1  r.AmbientOcclusionRadiusScale=1.7  r.DepthOfFieldQuality=1 ```  Expand code  Copy full snippet(25 lines long) |
| sg.PostProcessQuality 2 | sg.PostProcessQuality 3 |
| --- | --- |
| Config  ``` r.MotionBlurQuality=3  r.BlurGBuffer=-1  r.AmbientOcclusionLevels=2  r.AmbientOcclusionRadiusScale=1.5  r.DepthOfFieldQuality=2 ```  Expand code  Copy full snippet(25 lines long) | Config  ``` r.MotionBlurQuality=4  r.BlurGBuffer=-1  r.AmbientOcclusionLevels=3  r.AmbientOcclusionRadiusScale=1.0  r.DepthOfFieldQuality=2 ```  Expand code  Copy full snippet(25 lines long) |

## Shadows - sg.ShadowQuality

[![Shadow Quality settings examples](https://dev.epicgames.com/community/api/documentation/image/24635009-a661-40f7-b6cb-6fddfb08e989?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/24635009-a661-40f7-b6cb-6fddfb08e989?resizing_type=fit)

sg.ShadowQuality set from 0 on the left to 3 on the right.

The **Scalability Groups > Shadows** option adjusts the quality of dynamic shadows in accordance with the settings found in the `BaseScalability.ini` file located in the folder at  `[UE_InstallPath]/Engine/Config`. The **Low** setting equates to *sg.ShadowQuality* 0 and **Epic** to *sg.ShadowQuality* 3.

| sg.ShadowQuality 0 | sg.ShadowQuality 1 |
| --- | --- |
| Config  ``` r.LightFunctionQuality=0  r.ShadowQuality=0  r.Shadow.CSM.MaxCascades=1  r.Shadow.MaxResolution=512  r.Shadow.RadiusThreshold=0.06 ```  Expand code  Copy full snippet(13 lines long) | Config  ``` r.LightFunctionQuality=1  r.ShadowQuality=2  r.Shadow.CSM.MaxCascades=1  r.Shadow.MaxResolution=1024  r.Shadow.RadiusThreshold=0.05 ```  Expand code  Copy full snippet(13 lines long) |
| sg.ShadowQuality 2 | sg.ShadowQuality 3 |
| --- | --- |
| Config  ``` r.LightFunctionQuality=1  r.ShadowQuality=5  r.Shadow.CSM.MaxCascades=2  r.Shadow.MaxResolution=1024  r.Shadow.RadiusThreshold=0.04 ```  Expand code  Copy full snippet(13 lines long) | Config  ``` r.LightFunctionQuality=1  r.ShadowQuality=5  r.Shadow.CSM.MaxCascades=4  r.Shadow.MaxResolution=1024  r.Shadow.RadiusThreshold=0.03 ```  Expand code  Copy full snippet(13 lines long) |

## Textures - sg.TextureQuality

A modern rendering engine requires a lot more GPU memory (textures, meshes, GBuffer, depth buffer, shadow maps). Some of those memory usage costs scale with the screen resolution (for example, GBuffer), others with specific quality settings (for example, shadow maps). Another large memory usage cost comes from the textures used (usually compressed and streamed).

You can instruct the streaming system to manage more aggressively (smaller pool size, culling unused textures) or to have less or more detail in the mip level computation. This can have effects on the image quality, how much you can notice texture streaming artifacts, and how smoothly the game runs (updates require expensive memory transfers). The results can vary, depending on the media (for example, a faster or slower hard drive or SSD). Streaming from DVD or Blu-Ray adds much more latency, so avoid those.

The texture quality also affects the texture filtering mode (**r.MaxAnisotropy**). Limiting the anisotropic sample count reduces texture bandwidth, but does not save texture memory.

| sg.TextureQuality 0 | sg.TextureQuality 1 |
| --- | --- |
| Config  ``` |  |  | | --- | --- | |  | r.Streaming.MipBias=2.5 | |  |  | |  | r.MaxAnisotropy=0 | |  |  | |  | r.Streaming.PoolSize=200 | ``` r.Streaming.MipBias=2.5 r.MaxAnisotropy=0 r.Streaming.PoolSize=200 Copy full snippet(5 lines long) | Config  ``` |  |  | | --- | --- | |  | r.Streaming.MipBias=1 | |  |  | |  | r.MaxAnisotropy=2 | |  |  | |  | r.Streaming.PoolSize=400 | ``` r.Streaming.MipBias=1 r.MaxAnisotropy=2 r.Streaming.PoolSize=400 Copy full snippet(5 lines long) |
| sg.TextureQuality 2 | sg.TextureQuality 3 |
| --- | --- |
| Config  ``` |  |  | | --- | --- | |  | r.Streaming.MipBias=0 | |  |  | |  | r.MaxAnisotropy=4 | |  |  | |  | r.Streaming.PoolSize=700 | ``` r.Streaming.MipBias=0 r.MaxAnisotropy=4 r.Streaming.PoolSize=700 Copy full snippet(5 lines long) | Config  ``` |  |  | | --- | --- | |  | r.Streaming.MipBias=0 | |  |  | |  | r.MaxAnisotropy=8 | |  |  | |  | r.Streaming.PoolSize=1000 | ``` r.Streaming.MipBias=0 r.MaxAnisotropy=8 r.Streaming.PoolSize=1000 Copy full snippet(5 lines long) |

The effect of this feature is heavily dependent on your game and hardware. If you do not have many textures, to the point where loading and using the full resolution mip maps does not use all of the memory pool Unreal Engine has devoted to textures, you will not actually see a difference between high and low settings (outside of the change to the Anisotropy settings).

## Effects - sg.EffectsQuality

The **Scalability Groups >  Effects** option adjusts the quality of many different types of effects in accordance with the settings found in the `BaseScalability.ini` file located in the folder at `[UE_InstallPath]/Engine/Config`. The **Low** setting equates to *sg.EffectsQuality* 0 and **Epic** to *sg.EffectsQuality* 3.

| sg.EffectsQuality 0 | sg.EffectsQuality 1 |
| --- | --- |
| Config  ``` r.TranslucencyLightingVolumeDim=24  r.RefractionQuality=0  r.SSR=0  r.SceneColorFormat=3  r.DetailMode=0 ```  Expand code  Copy full snippet(13 lines long) | Config  ``` r.TranslucencyLightingVolumeDim=32  r.RefractionQuality=0  r.SSR=0  r.SceneColorFormat=3  r.DetailMode=1 ```  Expand code  Copy full snippet(13 lines long) |
| sg.EffectsQuality 2 | sg.EffectsQuality 3 |
| --- | --- |
| Config  ``` r.TranslucencyLightingVolumeDim=48  r.RefractionQuality=2  r.SSR=0  r.SceneColorFormat=3  r.DetailMode=1 ```  Expand code  Copy full snippet(13 lines long) | Config  ``` r.TranslucencyLightingVolumeDim=64  r.RefractionQuality=2  r.SSR.Quality=1  r.SceneColorFormat=4  r.DetailMode=2 ```  Expand code  Copy full snippet(13 lines long) |

## Detail Mode

Each placed Actor has a Detail Mode property in the Rendering category. This setting defines the minimum detail level for an Actor to render.

[![Actor Detail Mode property in the Rendering section.](https://dev.epicgames.com/community/api/documentation/image/32912f4f-7948-4271-a4a8-e233008327a0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/32912f4f-7948-4271-a4a8-e233008327a0?resizing_type=fit)

The scalability mode can be changed from the console:

Config

```
r.DetailMode 1
```

r.DetailMode 1

Copy full snippet(1 line long)

The cvar values map to the settings for the Detail Mode property as follows:

* *r.DetailMode* 0 = Low
* *r.DetailMode* 1 = Medium
* *r.DetailMode* 2 =High

[![Detail Mode settings examples](https://dev.epicgames.com/community/api/documentation/image/0a7bf59c-0280-4305-802a-481bfcefc714?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0a7bf59c-0280-4305-802a-481bfcefc714?resizing_type=fit)

It is easy to use this to disable decals, detail objects, lights, or individual particle effects. Make sure to only use this on objects that have no effect on gameplay, otherwise, you will run into problems with network gameplay, save games, or consistency.

## Material Quality Level

[![Material Quality Level in the Viewport Performance and Scalability menu.](https://dev.epicgames.com/community/api/documentation/image/baf571c5-3d7d-4938-8a23-215eda8b8250?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/baf571c5-3d7d-4938-8a23-215eda8b8250?resizing_type=fit)

Materials can use the **Quality Switch** Material Expression node to disable some expensive Material parts that have a minor effect on the final look. To see the effect of this, you need to toggle to the **Low Quality** mode.

[![Blueprint Node layout for Material Quality](https://dev.epicgames.com/community/api/documentation/image/995edda2-a77d-4f91-88df-237117944183?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/995edda2-a77d-4f91-88df-237117944183?resizing_type=fit)

Setting the **Material Quality Level** to Low or High determines which expressions get evaluated for this material (the low or high pin). The default pin fills in either high or low (or both) if they have no inputs. This material contains two reasonably high-cost Perlin noise operations when set to high:

This example is to demonstrate the **Material Switch Node**. The
**Noise** nodes are expensive making them good for this example, but they
should be used sparingly as there are cheaper ways to create this
effect.

[![Material Quality Level settings example](https://dev.epicgames.com/community/api/documentation/image/d22bf5ee-1bb2-4549-b72a-55746c6dac9b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d22bf5ee-1bb2-4549-b72a-55746c6dac9b?resizing_type=fit)

left: Material Quality Level set to low, right: Material Quality Level set to high

[![Material Quality Level shader cost](https://dev.epicgames.com/community/api/documentation/image/d7ed1c14-d96f-4cf7-bc9d-1ac54d440615?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d7ed1c14-d96f-4cf7-bc9d-1ac54d440615?resizing_type=fit)

left: Material Quality Level set to low, right: Material Quality Level set to high. Shader Complexity mode shows that the high quality material is more costly than other shaders, with darker greens meaning more costly shaders.

Using the quality switch causes more shaders to be compiled (shader permutation).

This feature is not for distance LOD as you cannot have two quality levels at the same time. The feature can be used to reduce:

* Shader computations (for example, disable fuzz layer).

  + Use **Shader Complexity** mode (**Alt+8** in the editor) and instruction count to verify your optimization.
* Texture lookups (no detail bump map).
* Memory bandwidth (for example, using fewer textures).

  + You need to profile on actual hardware to verify this.

Most material editor outputs only affect the pixel shader. World position offset and all tessellation outputs affect the other shader types. Pixels shaders only cost a lot if they occupy large portions of the screen (a skybox for example), while other shaders only matter if the object is not culled (inside the view, not hidden behind opaque objects).

## Skeletal Mesh LOD Bias

[![Skeletal mesh LOD bias](https://dev.epicgames.com/community/api/documentation/image/92dcf697-8daf-484b-921b-adfc3102ad85?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/92dcf697-8daf-484b-921b-adfc3102ad85?resizing_type=fit)

Skeletal meshes can have static Level of Details models. Using the console variable **r.SkeletalMeshLODBias**, you can globally bias the LOD level. Depending on the quality of your first or second LOD, it can be a good idea to have this option in the scalability settings. Here you can see the scalability setting on top of the distance dependent LOD.

## Grass and Foliage Scalability

The **Scalability Groups > Foliage** option adjusts how many foliage meshes are rendered at one time in accordance with the settings found in the `BaseScalability.ini` file located in the folder at `[UE_InstallPath]/Engine/Config`. The **Low** setting equates to *FoliageQuality* 0 and **Epic** to *FoliageQuality* 3.

For Foliage Static Meshes to work with the Scalability settings you must
enable the Enable Density Scaling option. You can read more about how
to set this up in the[Foliage Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/foliage-mode-in-unreal-engine) documentation.

| FoliageQuality 0 | FoliageQuality 1 |
| --- | --- |
| Config  ``` |  |  | | --- | --- | |  | [FoliageQuality@0] | |  |  | |  | foliage.DensityScale=0 | |  |  | |  | grass.DensityScale=0 | ``` [FoliageQuality@0] foliage.DensityScale=0 grass.DensityScale=0 Copy full snippet(5 lines long) | Config  ``` |  |  | | --- | --- | |  | [FoliageQuality@1] | |  |  | |  | foliage.DensityScale=0.4 | |  |  | |  | grass.DensityScale=0.4 | ``` [FoliageQuality@1] foliage.DensityScale=0.4 grass.DensityScale=0.4 Copy full snippet(5 lines long) |
| FoliageQuality 2 | FoliageQuality 3 |
| --- | --- |
| Config  ``` |  |  | | --- | --- | |  | [FoliageQuality@2] | |  |  | |  | foliage.DensityScale=0.8 | |  |  | |  | grass.DensityScale=0.8 | ``` [FoliageQuality@2] foliage.DensityScale=0.8 grass.DensityScale=0.8 Copy full snippet(5 lines long) | Config  ``` |  |  | | --- | --- | |  | [FoliageQuality@3] | |  |  | |  | foliage.DensityScale=1.0 | |  |  | |  | grass.DensityScale=1.0 | ``` [FoliageQuality@3] foliage.DensityScale=1.0 grass.DensityScale=1.0 Copy full snippet(5 lines long) |

## Customizing Scalability Settings

You can customize any of the Scalability Settings used in your Unreal Engine project. In the following example we will add and the change the Scalability Settings for the Foliage by doing the following:

* Go to your projects Config folder and create a new `.ini` file called `DefaultScalability.ini`.

  [![Create a new ini file](https://dev.epicgames.com/community/api/documentation/image/22bcfb62-39f5-4096-9ffe-88f2fe7dd420?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/22bcfb62-39f5-4096-9ffe-88f2fe7dd420?resizing_type=fit)
* Open up the newly created `DefaultScalability.ini` file and add the following lines of code to it.

  Config

  ```
  [FoliageQuality@0]
  foliage.DensityScale=.25
  grass.DensityScale=.25

  [FoliageQuality@1]
  foliage.DensityScale=0.50
  grass.DensityScale=0.50

  [FoliageQuality@2]
  foliage.DensityScale=0.75
  ```

  Expand code  Copy full snippet(15 lines long)
* Save the file and now when the Scalability settings for **Foliage** are changed, the amount of Foliage and Landscape Grass Static Meshes that are spawned will be reduced or increased based on which setting was picked.

* [scalability](https://dev.epicgames.com/community/search?query=scalability)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Scalability Settings](/documentation/en-us/unreal-engine/scalability-reference-for-unreal-engine?application_version=5.7#scalabilitysettings)
* [Resolution Scale](/documentation/en-us/unreal-engine/scalability-reference-for-unreal-engine?application_version=5.7#resolutionscale)
* [View Distance](/documentation/en-us/unreal-engine/scalability-reference-for-unreal-engine?application_version=5.7#viewdistance)
* [Anti-Aliasing](/documentation/en-us/unreal-engine/scalability-reference-for-unreal-engine?application_version=5.7#anti-aliasing)
* [Post Processing - sg.PostProcessQuality](/documentation/en-us/unreal-engine/scalability-reference-for-unreal-engine?application_version=5.7#postprocessing-sgpostprocessquality)
* [Shadows - sg.ShadowQuality](/documentation/en-us/unreal-engine/scalability-reference-for-unreal-engine?application_version=5.7#shadows-sgshadowquality)
* [Textures - sg.TextureQuality](/documentation/en-us/unreal-engine/scalability-reference-for-unreal-engine?application_version=5.7#textures-sgtexturequality)
* [Effects - sg.EffectsQuality](/documentation/en-us/unreal-engine/scalability-reference-for-unreal-engine?application_version=5.7#effects-sgeffectsquality)
* [Detail Mode](/documentation/en-us/unreal-engine/scalability-reference-for-unreal-engine?application_version=5.7#detailmode)
* [Material Quality Level](/documentation/en-us/unreal-engine/scalability-reference-for-unreal-engine?application_version=5.7#materialqualitylevel)
* [Skeletal Mesh LOD Bias](/documentation/en-us/unreal-engine/scalability-reference-for-unreal-engine?application_version=5.7#skeletalmeshlodbias)
* [Grass and Foliage Scalability](/documentation/en-us/unreal-engine/scalability-reference-for-unreal-engine?application_version=5.7#grassandfoliagescalability)
* [Customizing Scalability Settings](/documentation/en-us/unreal-engine/scalability-reference-for-unreal-engine?application_version=5.7#customizingscalabilitysettings)
