<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-mobile-deferred-shading-mode-in-unreal-engine?application_version=5.7 -->

# Mobile Deferred Shading Mode

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
5. [Mobile Development](/documentation/en-us/unreal-engine/getting-started-with-mobile-development-in-unreal-engine "Mobile Development")
6. [Mobile Rendering Features](/documentation/en-us/unreal-engine/rendering-features-for-mobile-games-in-unreal-engine "Mobile Rendering Features")
7. Mobile Deferred Shading Mode

# Mobile Deferred Shading Mode

Use deferred shading in Mobile games for more efficient dynamic lighting and improved quality.

![Mobile Deferred Shading Mode](https://dev.epicgames.com/community/api/documentation/image/6fcaf187-b054-447b-a760-fb680bf9c4aa?resizing_type=fill&width=1920&height=335)

 On this page

While **forward shading** processes geometry and lighting at draw time, **deferred shading** separates them into two separate passes. This separates the computation of lighting from the computation of geometry, and provides more efficient implementation for materials and advanced lighting features.

The **mobile deferred shading model** provides these benefits, but also takes advantage of tile-based GPUs to reduce the performance impact on system memory and CPU. This provides better rendering quality and better performance on mobile devices that support tile memory.

This page provides the following information:

* An overview of the benefits and limitations of mobile deferred shading.
* Information on which devices are compatible with the mobile deferred shading model.
* Instructions on how to configure mobile deferred shading for your project.

## How to Enable the Mobile Deferred Shading Mode

To enable mobile deferred shading:

1. Open your **Project Settings.**
2. Navigate to **Engine - Rendering** > **Mobile**.
3. Click the dropdown for **Mobile Shading** and set it to **Deferred Shading**, then restart the editor.

   ![The dropdown for Mobile Shading in the Rendering > Mobile section.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e59192f4-39d0-4d49-be4d-1d6680b2b18b/mobileshadingdropdown.png)

When you build your project for mobile devices, they will use the mobile deferred shading model.

## Overview

Deferred shading splits the rendering process into two passes:

1. A *geometry pass* that handles BaseColor, Metallic, and Roughness parameters and stores them in a temporary buffer, usually called **GBuffer**.
2. A *lighting pass* that reads the material attributes from GBuffer, computes lighting for it, then writes shaded pixels into the framebuffer.

Meanwhile, forward shading computes material interactions with lights and shadows at draw time. This means that materials must include light and shadow code alongside all other parameters. Deferred shading can omit this information and use simpler shaders and materials that take less time to compile.

Because deferred shading does not need to bind shadow and reflection textures, it also requires less graphics state management for each draw call, which provides better performance on CPU. This means the **Render Hardware Interface (****RHI)** thread does less work, which in turn frees up big cores for other threads, which causes fewer conflicts among available threads.

Deferred shading separates the processing and memory costs of lighting from the costs of rendering geometry, which makes debugging and optimization for lighting more flexible.

### Mobile Deferred Shading

To achieve deferred shading efficiently on mobile devices, the mobile deferred shading model puts GBuffer in tile memory inside the GPU, meaning that the GBuffer is never stored in system memory. It also does not allocate memory when a device supports the `LAZILY_ALLOCATED` memory type. Devices that support memoryless render target use less memory with mobile deferred shading, but devices that don't support them will allocate system memory for GBuffer and use slightly more memory.

### Example of Performance Improvements

The Material below uses a simple color and roughness input. With mobile forward rendering, it uses 147 instructions and 2 samplers. With mobile deferred, it uses only 34 instructions and 0 samplers, as it no longer needs to include lighting and shading instructions. This results in reduced framerate hitches and overall lower memory use.

![Comparison of a basic material using mobile forward and mobile deferred shading modes](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8b2883c3-cd45-46d8-9f60-471cee76a3df/forward_deferred_comparison.png)

Left: A basic material using simple color and roughness inputs. Top-Right: Statistics for this material using Mobile Forward. Bottom-Right: Statistics for this material using Mobile Forward.

## Guidelines for Using Mobile Deferred Shading and Mobile Forward Shading

Mobile deferred shading is preferable when:

* Your target devices use tile-based mobile GPUs.
* Your game does not use pre-computed lighting.
* You need advanced lighting features not offered by forward shading.
* You need to improve performance and save memory for complex lighting.

Typical examples of projects that fit the above profile are games with large outdoor environments and heavy dependence on dynamic lighting. Most devices that Unreal Engine supports fulfill the hardware requirements for deferred shading, and the performance benefits for deferred shading are significant. Therefore, we advise using mobile deferred shading for most mobile projects in UE. However, the forward shading model is still preferable if you primarily use pre-computed lighting, and it provides benefits when using local lights or a large number of reflection captures.

## Supported Rendering Features for Mobile Deferred Shading

This section lists rendering features that the Mobile Deferred shading mode supports which are not available in the Mobile Forward shading mode.

### Lighting Features

The Mobile Deferred shading mode provides the following lighting features:

* Light Functions
* Light Profiles
* IES Light Profiles
* Lit decals
* Increased local light rendering efficiency

### Rendering Limitations

#### Pre-Computed Lighting and Shading Model Limitations

If your project uses pre-computed lighting, deferred shading only provides DefaultLit and Unlit shading models. If your project uses pre-computed lighting, we strongly advise that you use forward shading instead of deferred shading.

#### Translucency Passes

Translucency is available in the deferred shading mode, but translucency passes always use forward shading. Make sure translucent materials such as glass or water have their **Lighting Mode** set to **Surface ForwardShading**.

#### Multi-Sample Anti-Aliasing (MSAA)

Deferred rendering can not support **Multi-Sample Anti-Aliasing (****MSAA)** due to the amount of space it would need in GBuffer. It also would have a more resource-intensive shading pass due to the need to shade each sample rather than each pixel.

#### Lit Decal Limitations

**Lit decals** are not supported with static lighting in deferred mode, as it would require an additional buffer for decals. This is not feasible on mobile devices due to memory constraints. However, **emissive** decals work fine with static lighting.

#### Other Decal Limitations

Because of space limitations in GBuffer, decals use octahedron encoding for normals to reduce their size. This encoding makes it impossible to blend or modify normals in GBuffer. However, you can fully overwrite them instead.

#### Shading Model Limitations

Supporting multiple shading models at the same time is very expensive with mobile deferred shading. Therefore, you should limit your use of complex shading models only to objects that need them.

## Device Compatibility

Unreal Engine supports Mobile Deferred shading on all platforms that use the Mobile renderer, including PC platforms, iOS, Android Vulkan, and Android GLES. The following sections provide details on how each family of devices uses its Tile Memory to support this shading mode, and on the limitations of certain devices.

### Tile Memory Usage

Each mobile platform has different ways to perform shading in tile memory.

* iOS uses a functionality similar to `framebuffer_fetch` to access GBuffer on tile memory.
* Android Vulkan uses Vulkan's sub-passes.
* Android GLES requires extensions, and there is no universal method for all GPUs.
* Mali and PowerVR use PLS extensions.
* Adreno GPUs use the `framebuffer_fetch` extension.

Other GPUs use an immediate-mode renderer, so these tile memory techniques do not apply. In these cases, GBuffer is allocated as a regular texture in system memory and may not provide memory benefits.

### Hardware Limitations

Mali Devices running Android Vulkan have strict limitations on color and input attachments:

* 16 bytes or 128-bit per-pixel in GBuffer
* Can only use up to 4 input attachments.
* Can only fetch up to 3 color attachments and 1 depth attachment during the lighting pass.

The Mobile Deferred shading mode adopts these limitations by default to ensure consistency across all devices. To remove these limitations, set the `MobileUsesExtendedGBuffer` parameter in your `*Engine.ini` file to `true`. The mobile deferred shading mode will then expand GBuffer to use the full capabilities of the user's device.

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [lighting](https://dev.epicgames.com/community/search?query=lighting)
* [mobile](https://dev.epicgames.com/community/search?query=mobile)
* [shading model](https://dev.epicgames.com/community/search?query=shading%20model)
* [mobile shading model](https://dev.epicgames.com/community/search?query=mobile%20shading%20model)
* [mobile rendering](https://dev.epicgames.com/community/search?query=mobile%20rendering)
* [deferred renderer](https://dev.epicgames.com/community/search?query=deferred%20renderer)
* [deferred shading](https://dev.epicgames.com/community/search?query=deferred%20shading)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [How to Enable the Mobile Deferred Shading Mode](/documentation/en-us/unreal-engine/using-the-mobile-deferred-shading-mode-in-unreal-engine?application_version=5.7#howtoenablethemobiledeferredshadingmode)
* [Overview](/documentation/en-us/unreal-engine/using-the-mobile-deferred-shading-mode-in-unreal-engine?application_version=5.7#overview)
* [Mobile Deferred Shading](/documentation/en-us/unreal-engine/using-the-mobile-deferred-shading-mode-in-unreal-engine?application_version=5.7#mobiledeferredshading)
* [Example of Performance Improvements](/documentation/en-us/unreal-engine/using-the-mobile-deferred-shading-mode-in-unreal-engine?application_version=5.7#exampleofperformanceimprovements)
* [Guidelines for Using Mobile Deferred Shading and Mobile Forward Shading](/documentation/en-us/unreal-engine/using-the-mobile-deferred-shading-mode-in-unreal-engine?application_version=5.7#guidelinesforusingmobiledeferredshadingandmobileforwardshading)
* [Supported Rendering Features for Mobile Deferred Shading](/documentation/en-us/unreal-engine/using-the-mobile-deferred-shading-mode-in-unreal-engine?application_version=5.7#supportedrenderingfeaturesformobiledeferredshading)
* [Lighting Features](/documentation/en-us/unreal-engine/using-the-mobile-deferred-shading-mode-in-unreal-engine?application_version=5.7#lightingfeatures)
* [Rendering Limitations](/documentation/en-us/unreal-engine/using-the-mobile-deferred-shading-mode-in-unreal-engine?application_version=5.7#renderinglimitations)
* [Pre-Computed Lighting and Shading Model Limitations](/documentation/en-us/unreal-engine/using-the-mobile-deferred-shading-mode-in-unreal-engine?application_version=5.7#pre-computedlightingandshadingmodellimitations)
* [Translucency Passes](/documentation/en-us/unreal-engine/using-the-mobile-deferred-shading-mode-in-unreal-engine?application_version=5.7#translucencypasses)
* [Multi-Sample Anti-Aliasing (MSAA)](/documentation/en-us/unreal-engine/using-the-mobile-deferred-shading-mode-in-unreal-engine?application_version=5.7#multi-sampleanti-aliasing(msaa))
* [Lit Decal Limitations](/documentation/en-us/unreal-engine/using-the-mobile-deferred-shading-mode-in-unreal-engine?application_version=5.7#litdecallimitations)
* [Other Decal Limitations](/documentation/en-us/unreal-engine/using-the-mobile-deferred-shading-mode-in-unreal-engine?application_version=5.7#otherdecallimitations)
* [Shading Model Limitations](/documentation/en-us/unreal-engine/using-the-mobile-deferred-shading-mode-in-unreal-engine?application_version=5.7#shadingmodellimitations)
* [Device Compatibility](/documentation/en-us/unreal-engine/using-the-mobile-deferred-shading-mode-in-unreal-engine?application_version=5.7#devicecompatibility)
* [Tile Memory Usage](/documentation/en-us/unreal-engine/using-the-mobile-deferred-shading-mode-in-unreal-engine?application_version=5.7#tilememoryusage)
* [Hardware Limitations](/documentation/en-us/unreal-engine/using-the-mobile-deferred-shading-mode-in-unreal-engine?application_version=5.7#hardwarelimitations)
