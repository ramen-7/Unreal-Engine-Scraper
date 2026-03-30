<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/composure?application_version=5.7 -->

# Composure

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
7. [Real-Time Compositing with Composure](/documentation/en-us/unreal-engine/realtime-compositing-with-composure-in-unreal-engine "Real-Time Compositing with Composure")
8. Composure

# Composure

The new Composure plugin renews support for real‑time compositing pipelines in Unreal Engine, and intends to replace the Legacy Composure plugin.

![Composure](https://dev.epicgames.com/community/api/documentation/image/1b433529-c151-4a5d-9f20-66a7b89f1bd4?resizing_type=fill&width=1920&height=335)

Learn to use this **Experimental** feature, but use caution when shipping with it.

 On this page

### Our Motivation

**Composure** provides a viable platform for real-time compositing with both live video input as well as file / image media plates. This fills a critical gap in Unreal Engine's **virtual production** capabilities.

### What is in Scope

Unreal Engine 5.7 reintroduces Composure in Experimental as an updated system for real-time compositing. The new Composure is a layer-based tool with numerous improvements over the legacy system, including:

* Redesigned user experience and streamlined workflow.
* Performant **Shadow and Reflection** integration for live-action footage using **Custom Render Passes**.
* Improved **Keyer**.

The legacy version of Composure remains available, but is no longer maintained and will be phased out going forward.

### Who will Benefit

In general, Composure and real-time compositing will be most applicable to work that uses live-action footage.  Sophisticated **Computer-Generated (CG)**  compositing remains best served by dedicated offline tools such as Nuke and After Effects.  The two most common types of shots that Composure aims to support are:

* Greenscreen / bluescreen foreground footage over a CG (Unreal Engine) background.
* CG (Unreal Engine) foreground elements / characters over live-action background footage.

While final-quality composited shots will be possible, it is more likely that Film/TV productions will initially use Composure for Simulcam-style previewing during production on set, and post-vis for editorial.  Broadcasts (that is, news, sports, etc.) are included as candidates for the new Composure.

### Legacy Composure

While the reintroduced Composure in Unreal Engine 5.7 is technically Experimental, the existing feature set is officially documented and is prioritized to avoid confusion about versions. Going forward, the prior / existing system will be branded as **Legacy Composure**. Documentation for Legacy Composure will not be updated. You can find Legacy Composure in the Unreal Engine 5.6 documentation here:

[Real-Time Compositing with Composure](https://dev.epicgames.com/documentation/en-us/unreal-engine/realtime-compositing-with-composure-in-unreal-engine?application_version=5.5)

The prior / existing Legacy Composure can still be accessed from the **Virtual Production** menu for any user who still relies on it. The old system will likely remain for several releases until the new system takes hold.

[![Legacy-composure-in-dropdown-menu](https://dev.epicgames.com/community/api/documentation/image/5fd81f95-b4c9-40ed-a838-425ed5240d49?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5fd81f95-b4c9-40ed-a838-425ed5240d49?resizing_type=fit)

## Overview

The new **Composure** **plugin** reintroduces support for real‑time compositing pipelines in Unreal Engine, and intends to replace the **Legacy Composure** **plugin**. Its purpose is to simplify workflows for common use cases such as CG-over-video, or a keyed-video in a CG environment. It introduces 3D workflows by projecting footage into the scene, which improves interactions between footage and CG. When compared to Legacy Composure, the new plugin leverages recent engine features with improvements to: scene captures, custom render passes, primitive alpha holdout, material branching per render, and the render dependency graph.

The compositing setup is controlled by the **Composite Actor**. It orchestrates layers (which merge imagery) and passes (which process imagery). It also automatically manages scene captures or lightweight custom render passes as needed, to re‑render parts of the world from the main camera’s point of view.

* **Layers** decide what to merge and how to merge (for example, a main render with holdout masks over a plate). Layers can also register passes to pre-process inputs at various points during rendering.

  + **Main Render Layer**
  + **Plate Layer**
  + **Scene Capture Layer**
  + **Shadow Reflection Catcher Layer**
  + **Single Light Shadow Layer**
  + **Processing Layer**
* **Passes** are small, reusable image processors added on each layer’s secondary input, such as a media texture or a scene capture render.

  + **Centered Scale Pass**
  + **Color Grade Pass**
  + **Color Keyer Pass**
  + **Distortion Pass**
  + **Fast Approximate Anti-Aliasing (FXAA) Pass**
  + **Post-Process Material Pass**
  + **OpenColorIO Pass**
  + **Subpixel Morphological Anti-Aliasing (SMAA) Pass**

[![Simplified-structure-of-layers-&-passes](https://dev.epicgames.com/community/api/documentation/image/98ec19e6-6780-4c46-a0bb-83780d9ac234?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/98ec19e6-6780-4c46-a0bb-83780d9ac234?resizing_type=fit)

Simplified structure of layers & passes. For this initial release, the graph structure remains fairly rigid.

Scene captures are automatically spawned and owned by the Composite Actor on behalf of layers when they require additional renders (for example, a shadow / reflection matte or a custom render of selected actors).

### 3D vs. 2D Workflow

#### 3D with Composite Meshes (Recommended)

A 3D workflow is enabled by using composite meshes on the plate layer. These meshes can act as holdout occluders in the main render, while the projected media contributes to indirect lighting and reflections onto virtual CG objects.

#### 2D Only

Users may skip meshes, and composite scene capture layers in 2D over the main render. This can be useful for simple composite shots but plausible indirect lighting from the plate will be lost.

## Getting Started

1. Add a **Cine Camera Actor** to your level. This camera should mirror the real camera. It will be used as the source of projection for other renders.

   1. Optional: Calibrated lens file component. Follow our [Lens Calibration Quick Start Guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/camera-lens-calibration-quick-start-for-unreal-engine) to match the lens distortion between the physical camera lens and the engine cine camera for accurate compositing and occlusion.
   2. Optional: Live link components for tracking & FIZ data.
2. Open the Composure window, under **Window > Virtual Production > Composure**.
3. Click **Place Composite Actor** to add to your level:

   [![Place-composite-mesh-actor](https://dev.epicgames.com/community/api/documentation/image/c24b254b-dcef-43a8-92a9-02a71a3b8bd3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c24b254b-dcef-43a8-92a9-02a71a3b8bd3?resizing_type=fit)

   1. It should come preconfigured with 3 layers:

      [![Composite-actor-layers](https://dev.epicgames.com/community/api/documentation/image/081a1a66-fe5d-41cb-b166-cb368fe6b652?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/081a1a66-fe5d-41cb-b166-cb368fe6b652?resizing_type=fit)

      1. Main Render Layer: `MainRenderLayer`
      2. Shadow & Reflection Catcher Layer (deselected): `ShadowReflectionLayer`
      3. **Plate Laye****r**: `PlateLayer`
4. Point the **Composite Actor** to your `CineCameraActor`, and update the **Render Resolution** to match your desired output resolution.

   [![Point-the-cine-camera](https://dev.epicgames.com/community/api/documentation/image/3787f0db-7df4-440a-8082-5fd8e8312b39?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3787f0db-7df4-440a-8082-5fd8e8312b39?resizing_type=fit)
5. Select the `PlateLayer` and click **+** to **Place** **Composite Mesh Actor** in your level.

   [![Place-composite-mesh-actor-in-menu](https://dev.epicgames.com/community/api/documentation/image/b144b32e-6d28-43e4-ad17-7f5125379c74?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b144b32e-6d28-43e4-ad17-7f5125379c74?resizing_type=fit)

   1. Right-click the actor and select **Default Lit Masked** material type to catch CG shadows & reflections, and rough keying with alpha-masked edges.
   2. Right-click the actor and select **Default Unlit Alpha Composite** material type for keying plates while preserving good alpha quality (no shadows and reflections).
   3. Optionally update its **Material Type** given your use case, by right-clicking on the added mesh (or with the Material Type option exposed on the Composite Mesh Actor).

      [![Default-lit-and-unlit-options](https://dev.epicgames.com/community/api/documentation/image/689eb7fe-5229-47f4-aad2-2c6ea9e51740?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/689eb7fe-5229-47f4-aad2-2c6ea9e51740?resizing_type=fit)
6. On the `PlateLayer`, update the **Texture** with your live video input.

   1. Note that a (live video) media profile texture can be selected here directly.

      [![Texture-input-menu](https://dev.epicgames.com/community/api/documentation/image/bc79cb98-0cc3-45b1-9ee6-74ecaa0d8776?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bc79cb98-0cc3-45b1-9ee6-74ecaa0d8776?resizing_type=fit)
7. Add a **Hero CG Mesh** into the scene (for example, **SM\_MatPreviewMesh\_01**).
8. Optionally **select** the `ShadowReflectionCatcher` layer, then select the CG actor from which we want to catch shadows & reflections.

   The **Shadow Reflection Catcher** layer is the most expensive layer, since it creates two scene captures. It can be replaced with the much faster **Single Light Shadow** layer to trade quality for performance.

   [![Shadow-reflection-layer-selected](https://dev.epicgames.com/community/api/documentation/image/df8b24c2-559f-41b8-8738-8decc4171751?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/df8b24c2-559f-41b8-8738-8decc4171751?resizing_type=fit)
9. Pilot the cine camera.

   [![Image-of-airplane-icon-in-the-composure-tab](https://dev.epicgames.com/community/api/documentation/image/8adc7ad1-b8a1-45d5-a7c8-4b2c788ed36b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8adc7ad1-b8a1-45d5-a7c8-4b2c788ed36b?resizing_type=fit)

Example resulting composite:

[![Image-of-camera-over-color-bars-background](https://dev.epicgames.com/community/api/documentation/image/723a9027-7db1-43a8-84ae-e94cac4d126b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/723a9027-7db1-43a8-84ae-e94cac4d126b?resizing_type=fit)

## Actors and Components

### Composite Actor

The central compositing orchestrator manages all the compositing logic, ticking, layers, passes, and components.

#### Properties

| Property | Description |
| --- | --- |
| **Enabled** | Whether or not the composite behavior is enabled. This property is serialized and transacted through multi-user. |
| **Render Resolution** | Used for transient scene-capture render target size that layers may create. |
| **Camera** | Reference to the (optionally tracked and calibrated) camera used as a source of projection. Properties are also automatically derived from its lens file, if present. |
| **Enable Screen Space Reflections** | Automatically update the screen space reflections in post-processing, such that the plate is present in reflections. |
| **Overrides View User Flags / View User Flags** | A custom User Flag's value used to alter materials in the composite render pass. Set to one by default such that branching can be used in Lit materials. (See `TestPostVolumeUserFlag` material node.) |
| **Main Render Output** | Setting to control the render’s color space & encoding.   * Default (Tonemapped Final Color Low Dynamic Range (LDR)) * Linear High Dynamic Range (HDR) with Tone Curve * Linear High Dynamic Range (HDR) |
| **Allowed View Modes** | Constrain composite rendering to specific view modes, which can be useful for multi-viewport workflows.   * **Default**: Compositing is allowed on viewports with Lit, Path Tracing or Unknown view modes. * **Media Profile (Unknown)**: Compositing is only allowed with the media profile viewport (default Unknown view mode). * **All View Modes**: Compositing is allowed with all view modes. |

### Composite Mesh Actor & Component

A **Composite Mesh Actor** with its built-in composite mesh component are convenience objects for receiving a video plate in the scene. Its material can be updated with preconfigured options: **Default Lit Masked** or **Default Unlit Alpha Composite**.

[![Material-type-for-the-composite-mesh-actor](https://dev.epicgames.com/community/api/documentation/image/4c637831-1c05-4411-8221-29473f1c73e0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4c637831-1c05-4411-8221-29473f1c73e0?resizing_type=fit)

This actor is only exposed for convenient access to plugin materials: any mesh / material combination can be used as a plate layer composite mesh. 
Material instances can also be created from the default plugin materials to adjust properties such as **Metallic**, **Specular** and **Roughness**.

### Automatically Managed Components

The following components are managed automatically by the **Composite Actor**, and should not require user input except for specific use cases.

|  |  |
| --- | --- |
| **View‑Projection Component** | Writes the camera view‑projection matrix into a **Material Parameter Collection** every frame (4 vectors starting at  `MatrixParameterName`). Targets any  `CameraComponent` or  `CineCameraComponent` via a component reference. |
| **Composite Scene Capture****s** | Wrapper(s) over the standard `USceneCaptureComponent2D` used by the system for captures. Layers obtain and manage these through the **Composite Actor**. |

## Layers

**Layers** sequentially merge textures or render targets based on the specified merge operation for each layer. They operate bottom-up, as shown in the **Composure** window. Here is a description of the Composure table, column by column (starting from the left):undefined

1. **Active**: The active state controls whether the **Composite Actor** is actively rendering. It also enforces the activation of a single composite actor at a time. When joining multi-user, actors are automatically de-activated, and need to be re-activated manually (via a blueprint script). This property is not transacted.
2. **Enabled**: Transacted and serialized enabled state, for each layer or actor.
3. **Solo**: Solo layers allow you to quickly preview a single layer at a time.
4. **Object Name**
5. **Type**: Actor or layer type name.
6. **Operation**: Merge or blend operation with the previous layer.

Merge operators control how each layer or element is combined in the scene composition. There are many options, here are the currently supported merge operations:

|  |  |
| --- | --- |
| **None** | Current layer A previous replaces previous layer B. |
| **Over** | Current layer A over previous layer B: A + B \* (1-a). |
| **Under** | Current layer A under previous layer B: A \* (1-b) + B. |
| **Add** | Current layer A added to previous layer B: A + B. |
| **Subtract** | Previous layer B subtracted from current layer A: A - B. |
| **Multiply** | Current layer A multiplied by previous layer B: A \* B. |
| **Divide** | Current layer A (safely) divided by previous layer B: A / B. |
| **Min** | Per-component minimum between current layer A and previous layer B. |
| **Max** | Per-component maximum between current layer A and previous layer B. |
| **In** | Current layer A masked by the previous layer B's alpha: A \* b. |
| **Mask** | Current layer A's alpha masking the previous layer B: B \* a. |
| **Screen** | Screen advanced blend mode. |
| **Overlay** | Overlay advanced blend mode. |
| **Darken** | Darken advanced blend mode. |
| **Lighten** | Lighten advanced blend mode. |
| **ColorDodge** | Color dodge advanced blend mode. |
| **ColorBurn** | Color burn advanced blend mode. |
| **HardLight** | Hard light advanced blend mode. |
| **SoftLight** | Soft light advanced blend mode. |
| **Difference** | Difference advanced blend mode. |
| **Exclusion** | Exclusion advanced blend mode. |

### Layer Base Class

The **Layer Base Class** exposes default properties such as **Enabled**, **Solo**, **Name**, a merge **Operation** (default **Over**), and an interface for registering **Passes** proxies to send to the render thread.

[![Layer-base-class-and-passes-options](https://dev.epicgames.com/community/api/documentation/image/1023f0a2-7b17-4835-b752-e61a60b28901?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1023f0a2-7b17-4835-b752-e61a60b28901?resizing_type=fit)

### Plate

`UCompositeLayerPlate`: Integrates a 2D texture or media texture as a plate.

#### Properties

| Property | Description |
| --- | --- |
| **Composite Meshes** | Receives the projected plate texture, marked as holdout in the main render, but re-renders separately in a built-in custom render pass.  The separate render is automatically dilated to hide aliasing artifacts under smoothed **Temporal Super Resolution (TSR)** primitive alpha holdout edges. |
| **Texture** | Plate source texture (`Texture2D` or  `MediaTexture`), usually selected from a **Media Profile** video input. |
| **Media Passes** | Passes applied before rendering as a series of pre-processing steps onto the plate.  Media passes will usually host passes such as the **Centered Scale** pass (to counteract overscan) or the **Color Keyer** pass. |
| **Layer Passes** | Passes applied during post-processing, before integration with other layers. |
| **Mode** | **Composite Mesh** mode will sample the built-in custom render pass, while **Texture** mode will sample the processed plate texture directly (see diagrams below). |



[![Example render pipeline with media, scene, and layer passes.](https://dev.epicgames.com/community/api/documentation/image/49228f80-aad2-494d-ba43-624655401a35?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/49228f80-aad2-494d-ba43-624655401a35?resizing_type=fit)

Example render pipeline with media, scene, and layer passes.

For comparison, when the **Texture** mode is enabled on the plate layer, the pipeline changes as follows:

[![The-pipeline-is-changed-since-the-texture-mode-is-applied](https://dev.epicgames.com/community/api/documentation/image/bd980031-b745-4ee9-b84b-698bec82f7ca?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bd980031-b745-4ee9-b84b-698bec82f7ca?resizing_type=fit)

### Scene Capture

`UCompositeLayerSceneCapture`: Renders a subset of actors from a composite, managed scene-capture and merges the result.

[![Scene-capture-options](https://dev.epicgames.com/community/api/documentation/image/39acda26-f736-44a3-b65f-bdee0f954bb7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/39acda26-f736-44a3-b65f-bdee0f954bb7?resizing_type=fit)

#### Properties

| Property | Description |
| --- | --- |
| **Actors** | List of meshes that auto‑drives the capture’s `ShowOnlyComponents`. |
| **Custom Render Pass** | Optionally runs as a **Custom Render Pass** inline with the main renderer. Custom Render Passes are fast, minimal scene captures without lighting and anti-aliasing. |
| **Layer Passes** | Render target processing passes, for example **SMAA** or **FXAA** on an aliased custom render pass.  The **Scene Capture** layer automatically creates a scene capture component on the **Composite Actor**. Its properties can be further adjusted as needed. |

### Single Light Shadow

`UCompositeLayerSingleLightShadow`: Captures a single light (currently Directional) shadow map (Percentage-Closure Filtering (PCF), non‑cascaded) and builds a shadow matte.

[![Single-light-shadow-options](https://dev.epicgames.com/community/api/documentation/image/5ace0015-9cfb-4253-9f26-ebb2190cda40?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5ace0015-9cfb-4253-9f26-ebb2190cda40?resizing_type=fit)

Through its use of custom render passes for depth rendering, this layer is significantly faster than the alternative `UCompositeLayerShadowReflection`, but produces limited/lower quality shadows. Reflections are not included with this layer.

#### Properties

| Property | Description |
| --- | --- |
| **Light** | The reference light, whose exact transform will be used to render a shadow map.  Please make sure the light is aligned to your shadow-casting scene by **piloting the light**. Only directional lights are currently supported. |
| **Orthographic Width** | The desired width (in world units) of the shadow map view (ignored if light is not directional). Reduce size to only contain the shadow casting geometry in view of the light. |
| **Shadow Map Resolution** | Resolution of the shadow map texture. Lower resolutions will cause more blurry shadows, but require a higher shadow bias. |
| **Shadow Strength** | Basic shadow strength multiplier, from 0 to 1. |
| **Shadow Bias** | Shadow bias to avoid shadow acne. Increase until unwanted shadowing disappears (automatically scaled by `r.Shadow.CSMDepthBias` console variable). |
| **Shadow Casting Content** | (optional): List of shadow casting actors to be removed from the main camera view's scene depth. This helps create a cleaner shadow matte preventing aliased dark edges around CG objects. |

### Shadow & Reflection Catcher

`UCompositeLayerShadowReflection`: Produces a shadow / reflection matte to be multiplied on the plate. It uses two captures: one with CG and one without.

#### Properties

| Property | Description |
| --- | --- |
| **Auto-Configure Actors** | Marks the CG as normally visible or as hidden in scene capture, but with shadows / indirect while hidden is enabled. Hidden yields cleaner edges on the multiplicative matte, but loses screen space **Ambient Occlusion (AO)**. |
| **Actors** | List of CG actors from which to catch shadows and reflections. |

#### Current Known Limitations

* Being multiplicative in nature, the reflections currently disappear on colors with zero components.
* Reflections can be incorrectly tinted as they pick up saturated colors in the background.

#### Additional Notes

* With animated skeletal meshes, you may wish to disable `TemporalAA` (manually) on the reflection shadow catcher components hosted on the **Composite Actor**. This can prevent temporal history ghosting with moving shadows.
* This layer is significantly heavier than the Single Light Shadow, but should yield better quality results, despite known limitations.

### Processing

`UCompositeLayerProcessing`: Special layer that does not add a new input, it only processes the output of previous layers.

[![Pipeline-with-a-special-layer](https://dev.epicgames.com/community/api/documentation/image/2037cbca-500d-4c78-8e8a-e879f882c3b5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2037cbca-500d-4c78-8e8a-e879f882c3b5?resizing_type=fit)

For more information, see the next section on [Passes](https://dev.epicgames.com/documentation/en-us/unreal-engine/composure#passes).

One important use case involves two **OpenColorIO (OCIO)** passes to preserve the Unreal Engine’s tonecurve look while forcing the render to be HDR Linear (on the Composite Actor). Without **Academy Color Encoding Specification (ACES 2.0)**, the colors are not perfectly preserved—however, this works well enough in practice.

[![](https://dev.epicgames.com/community/api/documentation/image/055c6083-0633-4d9c-9d35-7dcfc6591cf5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/055c6083-0633-4d9c-9d35-7dcfc6591cf5?resizing_type=fit)

Please refer to the Open Color IO documentation: [Color Management with Open Color IO](https://dev.epicgames.com/documentation/en-us/unreal-engine/color-management-with-opencolorio-in-unreal-engine).

Forcing the main render to HDR Linear can help avoid incorrect blending artifacts, which could manifest as overlight bright colors in alpha gradients.

## Passes

**Passes** are small, reusable image processors added on each layer’s secondary input, such as a media texture or a scene capture render.

#### Color Keyer

`UCompositePassColorKeyer`: Production‑oriented keyer with chroma keying, clean‑plate support, spill removal, optional pre‑denoise, and multiple visualization modes.

#### Key Properties

| Property | Description |
| --- | --- |
| **Screen Type** | Type of screen color (required). The keyer works best against red, green or blue backgrounds. |
| **Key Color** | Static background key color. |
| **C****lean Plate** | Clean plate background for calculating color differences per pixel, instead of the static key color. Resolution must match the composite actor render resolution. |
| **R****ed / Green / Blue Weights** | Weight of the foreground channel contributing to the key matte hardness. |
| **Alpha Threshold** | Keeps any alpha value outside the specified threshold range to zero or one respectively, with linear interpolation in-between. |
| **De-spill Strength** | Strength of the spill reduction, 0.0: none, 1.0: full. |
| **D****e-vignette Strength** | Strength of the vignette removal. Used to improve plate uniformity & remove darker corners. |
| **Preserve Vignette After Key** | When enabled, we undo de-vignetting before outputting the keyed plate. |
| **Denoise Method** | Denoising method applied before the keyer (None, Median3x3). |
| **Visualization** | Visualize the alpha key or fill. |
| **Invert Alpha** | Invert the alpha key. |

### Centered Scale

`UCompositePassCenteredScale`: Scale footage to counteract overscan or uncropped footage with black bars (top / bottom bars are letterboxing, left / right bars are pillarboxing). Properties can be automatically derived from the Composite Actor’s camera component reference.

#### Properties

| Property | Description |
| --- | --- |
| **Scale Mode** | Centered scale calculation mode used to rescale a media texture with black bars into an already constrained aspect ratio viewport.   * **None**: No constraint applied. * **Automatic**: Automatically derive aspect ratio from the parent layer media texture & composite actor camera. * **AspectRatio**: Calculate the scaling factor from source & target aspect ratios. * **Manual**: Manually define the scaling factor. |
| **Source Aspect Ratio** | Source container aspect ratio (or resolution). |
| **Target Aspect Ratio** | Embedded target aspect ratio (or resolution), without black bars. |
| **Scale Factor** | Manual scale factor. |
| **O****verscan Uncrop Mode** | Uncrop calculation mode used to uncrop a viewport cropped in by overscan.   * **None**: No crop applied. * **Automatic**: Automatically derive the overscan crop factor from the parent composite actor camera reference. * **Manual**: Manually define the overscan crop factor. |
| **Overscan** | Manual overscan to uncrop, with values from 0.0 to 1.0 matching the source camera overscan. |

### Color Grade

`UCompositePassColorGrade`: Apply regular Unreal Engine color grading. See tonemapper documentation for color grading controls: [Color Grading and the Filmic Tonemapper](https://dev.epicgames.com/documentation/en-us/unreal-engine/color-grading-and-the-filmic-tonemapper-in-unreal-engine).

### OpenColorIO

`UCompositePassOpenColorIO`: Applies an `OpenColorIO` transform. See our documentation on `OpenColorIO` here: [OpenColorIO Quick Start Guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/opencolorio-quick-start-for-unreal-engine).

### FXAA

`UCompositePassFXAA`: Non-temporal anti-aliasing for CG. Expose Quality (0–5).

### SMAA

`UCompositePassSMAA`: Non-temporal anti-aliasing for CG. Expose Quality (0–5) analogous to `r.fxaa.quality` scale.

### Distortion (UCompositePassDistortion)

`UCompositePassDistortion`: Applies Distort using the lens distortion scene-view extension.

This pass is automatically applied, and only accessible via code or Blueprint. 
Follow our [Lens Calibration Quick Start Guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/camera-lens-calibration-quick-start-for-unreal-engine) to learn more about lens distortion.

* [composure](https://dev.epicgames.com/community/search?query=composure)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Our Motivation](/documentation/en-us/unreal-engine/composure?application_version=5.7#ourmotivation)
* [What is in Scope](/documentation/en-us/unreal-engine/composure?application_version=5.7#whatisinscope)
* [Who will Benefit](/documentation/en-us/unreal-engine/composure?application_version=5.7#whowillbenefit)
* [Legacy Composure](/documentation/en-us/unreal-engine/composure?application_version=5.7#legacycomposure)
* [Overview](/documentation/en-us/unreal-engine/composure?application_version=5.7#overview)
* [3D vs. 2D Workflow](/documentation/en-us/unreal-engine/composure?application_version=5.7#3dvs2dworkflow)
* [3D with Composite Meshes (Recommended)](/documentation/en-us/unreal-engine/composure?application_version=5.7#3dwithcompositemeshes(recommended))
* [2D Only](/documentation/en-us/unreal-engine/composure?application_version=5.7#2donly)
* [Getting Started](/documentation/en-us/unreal-engine/composure?application_version=5.7#getting-started)
* [Actors and Components](/documentation/en-us/unreal-engine/composure?application_version=5.7#actorsandcomponents)
* [Composite Actor](/documentation/en-us/unreal-engine/composure?application_version=5.7#compositeactor)
* [Properties](/documentation/en-us/unreal-engine/composure?application_version=5.7#properties)
* [Composite Mesh Actor & Component](/documentation/en-us/unreal-engine/composure?application_version=5.7#compositemeshactor&component)
* [Automatically Managed Components](/documentation/en-us/unreal-engine/composure?application_version=5.7#automaticallymanagedcomponents)
* [Layers](/documentation/en-us/unreal-engine/composure?application_version=5.7#layers)
* [Layer Base Class](/documentation/en-us/unreal-engine/composure?application_version=5.7#layerbaseclass)
* [Plate](/documentation/en-us/unreal-engine/composure?application_version=5.7#plate)
* [Properties](/documentation/en-us/unreal-engine/composure?application_version=5.7#properties-2)
* [Scene Capture](/documentation/en-us/unreal-engine/composure?application_version=5.7#scenecapture)
* [Properties](/documentation/en-us/unreal-engine/composure?application_version=5.7#properties-3)
* [Single Light Shadow](/documentation/en-us/unreal-engine/composure?application_version=5.7#singlelightshadow)
* [Properties](/documentation/en-us/unreal-engine/composure?application_version=5.7#properties-4)
* [Shadow & Reflection Catcher](/documentation/en-us/unreal-engine/composure?application_version=5.7#shadow&reflectioncatcher)
* [Properties](/documentation/en-us/unreal-engine/composure?application_version=5.7#properties-5)
* [Current Known Limitations](/documentation/en-us/unreal-engine/composure?application_version=5.7#currentknownlimitations)
* [Additional Notes](/documentation/en-us/unreal-engine/composure?application_version=5.7#additionalnotes)
* [Processing](/documentation/en-us/unreal-engine/composure?application_version=5.7#processing)
* [Passes](/documentation/en-us/unreal-engine/composure?application_version=5.7#passes)
* [Color Keyer](/documentation/en-us/unreal-engine/composure?application_version=5.7#colorkeyer)
* [Key Properties](/documentation/en-us/unreal-engine/composure?application_version=5.7#keyproperties)
* [Centered Scale](/documentation/en-us/unreal-engine/composure?application_version=5.7#centeredscale)
* [Properties](/documentation/en-us/unreal-engine/composure?application_version=5.7#properties-6)
* [Color Grade](/documentation/en-us/unreal-engine/composure?application_version=5.7#colorgrade)
* [OpenColorIO](/documentation/en-us/unreal-engine/composure?application_version=5.7#opencolorio)
* [FXAA](/documentation/en-us/unreal-engine/composure?application_version=5.7#fxaa)
* [SMAA](/documentation/en-us/unreal-engine/composure?application_version=5.7#smaa)
* [Distortion (UCompositePassDistortion)](/documentation/en-us/unreal-engine/composure?application_version=5.7#distortion(ucompositepassdistortion))
