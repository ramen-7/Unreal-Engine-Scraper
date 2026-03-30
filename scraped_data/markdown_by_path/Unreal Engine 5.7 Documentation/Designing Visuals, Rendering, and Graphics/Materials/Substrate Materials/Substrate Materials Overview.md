<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7 -->

# Substrate Materials Overview

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
6. [Materials](/documentation/en-us/unreal-engine/unreal-engine-materials "Materials")
7. [Substrate Materials](/documentation/en-us/unreal-engine/substrate-materials-in-unreal-engine "Substrate Materials")
8. Substrate Materials Overview

# Substrate Materials Overview

An overview of the Substrate Materials framework for principled BSDF-based material authoring.

![Substrate Materials Overview](https://dev.epicgames.com/community/api/documentation/image/d34722cb-1810-4905-8315-df3ea5806735?resizing_type=fill&width=1920&height=335)

 On this page

Substrate is Unreal Engine's approach to authoring materials, which replaces the fixed suite of shading models and blend modes, such as Default Lit and Clear Coat, with a more expressive and modular framework.

Certain abstractions of the non-Substrate (or legacy) material system are done away with by Substrate — it replaces them with measured properties of matter. This creates wider parameter space from which to work and makes it possible to more accurately blend between discrete surface types like metal, glass, and plastic. Substrate also streamlines the process of layering materials, making it easier to represent surfaces like liquid on metal, or a clear coat over subsurface scattering.

Materials in Substrate are conceptualized as "slabs of matter." These slabs are a principled BSDF (bidirectional scattering distribution function) representation, parameterized by physical quantities with well-defined units. Materials are expressed as a graph of slabs on which operations are performed (like mixing and layering). Because of their principled representation, Substrate Materials can be simplified according to the capacity of a platform in order to trade visual quality for performance.

## New Projects

Substrate is enabled by default for any newly created project. **Existing projects** upgrading to UE 5.7 and later will continue to use the non-Substrate path by default, unless their project settings explicitly opt-in for Substrate support.

For these existing projects, you can opt-in to Substrate from the **Project Settings > Rendering** and enable **Substrate materials**, and restart your project for the changes to take effect.

For new projects that have Substrate enabled by default, **Blendable GBuffer** format is used to prioritize speed over visual fidelity. This format can be changed in the project’s rendering settings.

Some template projects, such as Automotive and Architectural, use the **Adaptive GBuffer** by default in order to favor visual fidelity over performance.

For more information on setting up GBuffer format for your project, see the GBuffer Format section of this page.

### Material Editor Conversion

Existing non-Substrate materials will work out-of-the-box but aren't automatically converted to Substrate nodes. For existing non-Substrate, or newly created, materials, they will continue to use the non-Substrate root node parameterization and are converted to Substrate at compile time. This simplifies the project migration, avoids the need for asset modification or resaving, and helps with cooking costs.

To convert a material to Substrate, right-click on the root node and choose **Convert to Substrate**. This automatically creates a **Slab** and connects it to the **Front Material** of the root node and connects the inputs from the non-Substrate root node to the Slab.

Substrate Material Conversion

Follow these guidelines when enabling Substrate in an existing project or migrating to Unreal Engine 5.7 or later versions:

* Opening an existing non-Substrate material in a Substrate-enabled project does not alter the material any longer. It remains compatible with non-Substrate projects.
* Explicitly converted materials are not compatible with non-Substrate projects. The conversion is permanent and cannot be reverted to a non-Substrate material.
* Substrate Materials renders black if Substrate is disabled for the project. This includes any legacy Substrate materials that were created from converted materials. You can manually rewire any converted Substrate material to a legacy-style material but this will not get rid of the Substrate nodes that are now in the material graph.

## GBuffer Format for Visual Fidelity

Substrate supports two different GBuffer formats for storing material data, **Blendable GBuffer** and **Adaptive GBuffer**. These formats come with different tradeoffs regarding speed, memory, and visual fidelity.

### Blendable GBuffer

This format targets *fixed-memory* footprint and *predictable speed* as first principles. Its primary usage is for 60Hz projects. It comes with limited feature sets and is similar to the non-Substrate path.

* Performance is in parity with the non-Substrate path.
* Targets performance-oriented project (60Hz).
* Ensures visual consistency across all platforms.
* No cooking overhead.
* It **does not** force the DBuffer decal technique to be enabled.

### Adaptive GBuffer

This format targets visual fidelity and enables the full potential of Substrate, allowing enriched material complexity.

* Performance cost is higher and depends on the material’s complexity visible on screen.
* Targets visual fidelity, enabling more complex shading behaviors.
* High visual fidelity will depend on the platform.
* Cooking time increases by about 15% compared to the Blendable format. Materials with complex shading behavior will additionally increase cook time.
* It forces the DBuffer decal technique to be **enabled**.
* Additional controls for **Closure Count** and **Bytes Per Pixel** are available from the Project Settings and console variable.

This format is only supported on current-generation consoles Xbox Series X/S, PlayStation 5 and PlayStation 5 Pro, Windows PC (SM6), MacOS (SM6), and Linux (SM6). On other platforms (including SM5 platforms), materials are simplified and the platforms run with **Blendable GBuffer** format.

For known issues using Adaptive GBuffer, see the [Limitations and Known](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine#limitations-and-known-issues) Issues section of this page.

### DBuffer

* **Blendable GBuffer** **format** will continue to support both blendable decal and DBuffer decal. DBuffer decal is enabled by default, but you can opt-out in the project settings.
* Adaptive GBuffer format only supports DBuffer decal. If the project does not use DBuffer decal, the rendering system automatically enables it for platforms that support Adaptive GBuffer format.

When using DBuffer decals, Substrate supports material’s normal read during DBuffer evaluation as an experimental path, which can be enabled with `r.Substrate.DBufferPass`. This allows the DBuffer material to use the material’s normal without any temporal reprojection or depth-based normal reconstruction.

## Optional Project Settings and Console Variables

  Substrate includes these optional project settings and console variables:

[![Substrate Project Settings](https://dev.epicgames.com/community/api/documentation/image/a1f665e0-af41-4cec-bdce-4ae2e81eb0b7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a1f665e0-af41-4cec-bdce-4ae2e81eb0b7?resizing_type=fit)

Substrate Project Settings

| Project Settings | Description |
| --- | --- |
| **Substrate GBuffer Format (Project)** | Select the GBuffer format used for the project:   * **Blendable GBuffer:** Fast but has limited lighting complexity. If selected, all platforms will be forced to use this format. * **Adaptive GBuffer:** Heavier but enables complex lighting behavior per pixel. If selected, only compatible platforms will use this format. Incompatible platforms will use Blendable GBuffer. |
| **Substrate Closure Per Pixel (Project)** | Defines the maximum number of closures that can be evaluated per pixel. If a material contains more closures than this, the material will be iteratively simplified until it fits into the project’s budget. In addition, each platform has its own upper closure count limit, which can be overridden with these settings:   * **Min of Project’s and Platform’s Closure Count:** By default, for a given platform, the max closure count is the minimum between the platform’s count and the project-specified closure count. * **Force Closure Count:** This forces the project specified closure count to be the maximum for all platforms. |
| **Substrate Closure-Per-Pixel Override** | Select how the maximum number of closures evaluated per pixel is defined for each platform:   * **Use Platform Closure Count:** Use the minimum between the platform’s closure count and the project’s closure count on platforms supporting Adaptive GBuffer. * **Force Closure Count:** Force the project’s closure count on all platforms supporting Adaptive GBuffer. |
| **Substrate opaque material rough reflection (Experimental)** | When enabled, rough surfaces coating other materials can blur the lower layers in a physically plausible way.  This feature is experimental. |
| **Substrate translucent material rough refraction** | When enabled, translucent surfaces can generate rough refractions as a function of roughness. Enabling this makes the distortion pass more expensive. |
| **Substrate advanced visualization shaders (Editor / Win64 / DX12 Only)** | Enable advanced Substrate material debug visualization shaders. Base pass shaders can output such advanced data. Only available for Editors built for Win64 and running DX12 graphic API at this time. |
| **Substrate enable material layer support (Experimental)** | Enable Substrate material layering and user interface. Note: This support is one way, the legacy layer materials auto-upgrade and can only be reversed manually after assets are re-saved. |
| Console Variables |  |
| --- | --- |
| `r.Substrate.BytesPerPixel` | Provides a means to specify the storage bytes-per-pixel of a Substrate material before it is automatically simplified. This variable is set to 80 bytes per pixel by default. You can increase it for complex materials with higher storage requirements. Higher values use more memory, and can affect memory bandwidth and other performance characteristics. The relationship of this variable to performance is very dependent on both the content and the platform. You can specify this value on a per-platform basis in the platform.ini configuration file if necessary. |
| `r.Substrate.MaxClosureCount` | Provides a means to fix the number of closure evaluated per pixel. If a material has more closures than this value, the material will be automatically simplified to respect the closure count. |
| `r.Substrate.BlendableGBuffer` | Enable this forces Substrate to convert all materials to the legacy GBuffer using a single Shading Model per pixel. This can be used on lower end platforms to result in better performance for some projects that need it. |

## Substrate's Relationship to Material Layers

Traditional **Material Layering** in Unreal Engine (both [graph-based](https://dev.epicgames.com/documentation/en-us/unreal-engine/layered-materials-in-unreal-engine) and in the [custom layers GUI](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-material-layers-in-unreal-engine)) are based on the concept of parameter blending. Each layer defines a pattern graph of parameters which are blended and fed into the final shading model.

There is nothing preventing material layer-driven parameters from feeding into a Substrate-defined shading model. However, you would need to set this logic up manually using the output of a [Material Attribute](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-attributes-expressions-in-unreal-engine) node in the parent material. A limitation of this approach is that the Material Attributes system has a fixed list of parameters, but there might not be enough slots to feed into a multi-slab setup with Substrate — it might require using pins arbitrarily and unrelated to their true meaning.

Substrate can natively use [parameter blending](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.5), as described later in this page, but there is no way to access that functionality from the Material Layers interface. **Unifying Substrate and Material Layers is a strong area of interest for future development.**

It is important to note that Material Attribute and Material Layers do not operate real layering of matter: it is possible to simulate a clear coat and not possible to have a top layer with colored transmittance above another. They are rather only enabling the blending, or horizontal mixing, of two materials on a surface: not the layering of a slab of matter on top of another one.

## Working with Substrate Materials

Substrate Materials are authored similarly to legacy materials. This section covers the key elements that make up Substrate Materials, including its nodes, blend modes, and details on the types of materials you can create.

### Substrate Material Root Node

Like legacy materials, the **Material Root** node is where Substrate slabs and other Substrate nodes, like operators and building blocks, are fed into through the Front Material.

[![Substrate Material Root Node](https://dev.epicgames.com/community/api/documentation/image/4e9aac2a-0880-4080-8276-652eb5937c01?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4e9aac2a-0880-4080-8276-652eb5937c01?resizing_type=fit)

All Substrate Material graphs must be connected to the **Front Material** input on the root node. This input is the end-point of every Substrate graph.

[![Material Root Node Front Material Input](https://dev.epicgames.com/community/api/documentation/image/2b3f0378-f93e-42f3-a6f9-7eb4708cd46b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2b3f0378-f93e-42f3-a6f9-7eb4708cd46b?resizing_type=fit)

Also, like Legacy materials, you'll use the **Details** panel when the Material Root node is selected to set the **Blend Mode** and other properties that define the look of the material. The material domain and shading model are deducted automatically from the graph.

[![Setting the Substrate Blend Mode](https://dev.epicgames.com/community/api/documentation/image/38dbf688-e12e-4ae5-85da-598e3872a7c0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/38dbf688-e12e-4ae5-85da-598e3872a7c0?resizing_type=fit)

#### Substrate Blend Modes

Substrate uses its own set of [Blend Modes](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.5) to define how the material's color is blended with the background. Legacy material blend modes are limited in how they can mix and blend with one another, thus limiting the types of materials they can create. Substrate offers a broader selection of blend modes that can blend together to create all sorts of materials. This is especially important for achieving physically correct translucent surface shading.

Substrate includes the following Blend Modes:

[![Select a Substrate Blend Mode](https://dev.epicgames.com/community/api/documentation/image/2ca28845-59c9-47e3-bb4b-75765556a0a2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2ca28845-59c9-47e3-bb4b-75765556a0a2?resizing_type=fit)

| Blend Mode | Description |
| --- | --- |
| **Opaque** | Defines a surface through which light neither passes nor penetrates. An opaque surface with coverage of 1. This is the same as the legacy Opaque Blend Mode. |
| **Masked** | Used for materials that need to selectively control visibility in a binary (on / off) fashion. An opaque surface with coverage of 1 or 0. This is the same as the legacy Masked Blend Mode. |
| **Translucent - Grey Transmittance** | A translucent Material with colored surface and coverage, but transmittance reduced to grayscale. This is faster, as it prevents the extra render of post depth-of-field translucency into a modulate pass. This is the fallback Blend Mode for platforms not supporting hardware colored translucency (called dual source color blending). [This is similar to the legacy Translucent Blend Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/lit-translucency-in-unreal-engine). |
| **Additive** | Adds the color of the Material to the color of the background where Final Color = Source Color + Dest color. |
| **Colored Transmittance Only** | Only the transmittance of the Material is used. Surface interactions are reduced to 0. This is the same as the legacy Multiply Blend Mode. |
| **AlphaComposite (Premultiplied Alpha)** | This Blend Mode provides finer control over the Color contribution a material blended additively over the scene and the amount of coverage reducing the scene visibility behind (the coverage of the material can be overridden using the Opacity input of the root node). Works the same as the Legacy Alpha Composite (Premultiplied Alpha) Blend Mode. |
| **AlphaHoldout** | This blend mode holds out the alpha making it possible to punch a hole through objects to reveal the objects behind it. Works the same as the legacy AlphaHoldout Blend Mode. |
| **Translucent - Colored Transmittance** | A fully-featured translucent material with colored surface, coverage, and colored transmittance. This is more expensive when using separate translucency when post depth of field since it will have to render the transmittance component in a separate buffer, similarly to the legacy ThinTranslucent shading model. |

Substrate makes working with translucency more straightforward than traditional materials do — translucent Blend Modes are better defined by their intent. One aspect that remains unchanged between the two is that any translucent Blend Mode must also set a **Lighting Mode** to define how lighting is calculated for its surface. This is important to achieve the correct look for translucent materials.

The vast majority of translucent materials you create will use **Surface Translucency Volume** or **Surface Forward Shading**.

The following Lighting Modes are available to choose from:

| Lighting Modes | Description |
| --- | --- |
| **Volumetric NonDirectional** | Lighting is calculated for a volume without directionality. Use this on particle effects like smoke and dust. This is the cheapest per-pixel lighting method. However, the material normal is not taken into account. |
| **Volumetric Directional** | Lighting is calculated for a volume with directionality so that the normal of the material is taken into account. Note that default particle tangent space is facing the camera, so enable Generate Spherical Particles to get a more useful tangent space. |
| **Volumetric PerVertex NonDirectional** | Same as Volumetric NonDirectional but lighting is only evaluated at vertices so the pixel shader cost is significantly less. Note that lighting still comes from a volume texture, so it is limited in range. Directional Lights become unshadowed in the distance. |
| **Volumetric PerVertex Directional** | Same as Volumetric Directional but lighting is only evaluated at vertices so the pixel shader cost is significantly less. Note that lighting still comes from a volume texture, so it is limited in range. Directional Lights become unshadowed in the distance. |
| **Surface Translucency Volume** | Lighting is calculated for a surface. The light is accumulated in a volume so the result is blurry, and has limited distance but the per-pixel cost is very low. Use this on translucent surfaces like glass and water. Only diffuse lighting is supported. |
| **Surface ForwardShading** | Lighting is calculated for a surface. Use this on translucent surfaces like glass and water. This is implemented with forward shading so specular highlights from local lights are supported, however many deferred-only features are not. This is the most expensive translucency lighting method as each light's contribution is computed per-pixel. |

For some examples of setting up and using translucency in a Substrate Material, see the [Translucency](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.5) section of this page.

### Substrate Slab

The **Substrate Slab** is the elementary building block from which one assembles a Substrate Material. It is designed to be the minimum necessary set of parameters with which the vast majority of material appearances can be achieved. As such, it is the basis of a much more expressive type of appearance authoring.

A slab is a principled representation of a slab of matter that is composed of an **interface** and a **medium**.

[![Composition of a Substrate Slab](https://dev.epicgames.com/community/api/documentation/image/6dbcbb7e-d2ad-4ae5-bac8-88fa21bc80d7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6dbcbb7e-d2ad-4ae5-bac8-88fa21bc80d7?resizing_type=fit)

The composition of a Substrate Slab: The interface (1) and the medium (2).

1. The **interface** is the boundary where light interacts with the material's surface. The properties of the interface are primarily defined by the Roughness, Normal, Diffuse Albedo, F0 and F90 values fed into them.
2. The **medium** is the volume of matter beneath the interface where light is scattered, transmitted, and absorbed. The properties of the medium are primarily defined by the [Mean Free Path](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.5) (or MFP) as well as the Diffuse Albedo inputs.

The Substrate Slab is a modular replacement for the monolithic Material root node in non-Substrate Materials. It is made up of multiple surface attributes, such as Diffuse, Specular, Roughness, Emissive, Cloth, Anisotropy, and many more. All [Substrate BSDF nodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.5) contain properties that are relevant to their named output for the type of material they produce, such as eye, hair, simple clear coat, and so on.

Traditional Materials relied on their Blend Mode to present inputs that can be used. Substrate uses its different BSDF slabs to define the type of material. And because these are not tied directly to Blend Modes any longer they can be layered and mixed to produce varying types of materials.

|  |  |
| --- | --- |
| [Legacy Material Root Node](https://dev.epicgames.com/community/api/documentation/image/86bdace9-df51-4b95-a346-4cde37229391?resizing_type=fit) | [Substrate Slab with Material Root Node](https://dev.epicgames.com/community/api/documentation/image/3236ae8b-992c-4a16-8b7a-73ff8cd44808?resizing_type=fit) |
| Legacy Material Root Node | Substrate Slab and Material Root Node |

The primary **Substrate Slab BSDF** node used includes the following inputs:

| Substrate Slab Inputs | Definition |
| --- | --- |
| **Diffuse Albedo** | Defines the percentage of light reflected as diffuse from a surface. This is similar to the local base color of the medium. The default value is 0.18.  The Diffuse Albedo also represents the Percentage of light that is scattered by the participating medium when the simple volume sub-surface representation is used. |
| **F0** | Defines the color and brightness of the specular highlight where the surface is perpendicular to the camera. For dielectric Materials (plastics and other non-metals), this value is typically in the 0 - 0.08 range. For metallic materials it can range up to 1. Gemstones are in a range up to around 0.16. |
| **F90** | Defines the color of the specular highlight where the surface normal is 90 degrees from the camera. In other words, at grazing angles relative to the camera view. Only hue and saturation are perceived, as brightness is fixed at 1.0 This fades to black as F0 drops below 0.02. |
| **Roughness** | Controls how rough the material is. The roughness of the surface from 0 to 1. At 0 (smooth), roughness is a mirror reflection. At 1 (fully rough), roughness is completely matte or diffuse. When anisotropy is used, the roughness value is used along the tangent axis. |
| **Anisotropy** | Controls the anisotropy direction of the Material (-1: highlight aligned to the bi-tangent, 1: highlight is aligned with the tangent). |
| **Normal** | Take the surface normal as input. The normal is considered tangent or world space according to the space properties on the material root node. This input defines the shading normal per-pixel. |
| **Tangent** | Take a surface tangent as input. The normal is considered tangent or world space according to the space properties on the material root node. This input defines the shading tangent per-pixel. |
| **SSS MFP** | Subsurface scattering Mean Free Path (MFP). This controls the perceived density of the material and influences the absorption and scattering of light by the Material. More precisely, this defines the average distance in centimeters at which a photon interacts with a particle of matter. This distance is controlled per color channel.  The MFP directly interacts with transmittance and the amount of scattered light scattered within a slab:     1. Transmittance: the longer the MFP will be the more light will travel through the slab of matter. For instance, the scene will be more visible through a translucent surface.     1. An MFP equal to the Slab Thickness only lets 36% of the scene color through.    2. Scattering: The longer the MFP will be the less light will scatter towards the camera.    3. An MFP of zero makes the surface look as if it is opaque.   This input is only used when there is not any Subsurface Profile asset assigned to the material root node. |
| **SSS MFP Scale** | This input scales the subsurface scattering mean free path radius of the subsurface profile to a value between 0 and 1. |
| **SSS Phase Anisotropy** | Positive values elongate the phase function along the light direction, causing forward scattering. Negative values elongate the function backward along the light direction, causing back scattering. |
| **Emissive Color** | Controls the emissive color on top of material surfaces. |
| **Second Roughness** | Controls the roughness of a secondary specular lobe. At 0 (smooth), roughness is a mirror reflection. At 1 (fully rough), roughness is completely matte or diffuse.  This input does not influence diffuse roughness. |
| **Second Roughness Weight** | The mix factor between the primary and secondary specular lobe. The first specular using Roughness has a weight of (1 - SecondRoughnessWeight). Values equal to 0 renders the primary lobe only. 0.5 renders a 50% mix of both roughnesses, and 1.0 renders the secondary lobe only. |
| **Fuzz Roughness** | Controls how rough the Fuzz layer is. Fuzz with a roughness of 0 is smooth (shinier) and 1 is fully rough (matte). |
| **Fuzz Amount** | When greater than 0, adds a fuzz-like layer at the interface, causing color retroreflectivity. This controls the amount of fuzz applied on top of a surface layer. Usually used to create fabric materials. |
| **Fuzz Color** | Defines the color of the fuzz layer. |
| **Glint Density** | The logarithm representation of micro facet density on the surface of a material.  Requires `r.Substrate.Glints=1` to be set in the ConsoleVariables.ini configuration file. |
| **Glint UVs** | Controls the position and scale of glints on the surface of a material.  Requires `r.Substrate.Glints=1` to be set in the ConsoleVariables.ini configuration file. |

The Slab's sub-surface behavior is defined by the **Sub-Surface Type** property on the Slab. It defines the scattering model used for the given Slab. It offers an explicit control to achieve the existing legacy behavior, or achieve different looks.

The **Sub-Surface Type** available are:

* **Wrap:** Use a wrap lighting model to emulate light scattering. This is equivalent to the legacy Subsurface shading model.
* **Two-Sided Wrap:** Use a wrap lighting model on both sides of the surface to emulate light scattering. This is equivalent to the legacy Two-Sided Foliage shading model.
* **Diffusion:** Use diffusion model (screen space or raytraced) to update light scattering. When an SSS profile is provided, it is equivalent to the legacy SubSurface Profile shading model. Otherwise, MFP can be controlled directly on the slab.
* **Simple Volume:** Uses a mixture of Beer-Lambert model for the transmittance part and a fitted model for the scattering part.

For vertically layered slabs, only the **Simple Volume** Sub-Surface type is valid. List of Subsurface type support per layer type:

| Bottom Layer | Upper Layers |
| --- | --- |
| None  Simple Volume  Wrap  Two-Sided Wrap  Diffusion | Non  Simple Volume |

Depending on the platform and shading path, the diffusion subsurface type might not be available. In such cases, the system falls back onto a simple non-scattering diffuse model. Diffusion is only supported in deferred path and path-tracing path and on the following platforms: Xbox One, Xbox Series S, Xbox Series X, PlayStation 4 and 5, PC DX11, PC DX12, Linux Vulkan, and Mac OS. Lower-end platforms, like mobile, don't support diffusion models. At the bottom of each Slab node, a tag indicates which scattering model will be used based on the topology. This tag might be different from the one specified by the **Sub-Surface Type** property if this scattering type is not compatible with the topology.

[![](https://dev.epicgames.com/community/api/documentation/image/0936926b-4065-455e-872a-ffd30bb139e6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0936926b-4065-455e-872a-ffd30bb139e6?resizing_type=fit)

### Substrate Material Parameterization

Substrate uses a F0 / Diffuse Albedo parameterization compared to the non-Substrate path, which was using Base Color / Specular / Metalness. This parameterization offers more flexibility while continuing to ensure energy preservation. However, picking the right value for F0 might not be intuitive at first.

As a simple guideline, you can separate materials into two groups:

* **Dielectric materials:** These are materials with a metalness of 0, and they usually have an F0 value between 0.02 and 0.06, in linear space. Gemstones can have an F0 value up to 0.18, in linear space.
* **Conductor materials:** These are materials with a metalness of 1, and they usually have an F0 value beyond 0.5 up to 1, in linear space.

In between these ranges falls semi-conductor materials, which are rarely encountered in the real world.

[![Diagram for plausible ranges for dielectric materials.](https://dev.epicgames.com/community/api/documentation/image/8ca64aa2-f349-4ee1-a15e-e29b19d25eef?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8ca64aa2-f349-4ee1-a15e-e29b19d25eef?resizing_type=fit)

Diagram for plausible ranges for dielectric materials (source Adobe Substance)

Diagram taken from [Adobe Substances](https://www.adobe.com/learn/substance-3d-designer/web/the-pbr-guide-part-2).

  Below is a list of F0 values for common materials:

This list is reproduced from Real-Time Rendering Third Edition by Tomas Akenine-Moller, Eric Haines, and Naty Hoffman.

| Material | F0 Linear | F0 sRGB | Color |
| --- | --- | --- | --- |
| **Water** | 0.02 | 0.15 |  |
| **Plastic / Glass (Low)** | 0.03 | 0.21 |  |
| **Plastic (High)** | 0.05 | 0.24 |  |
| **Glass (High) / Ruby** | 0.08 | 0.31 |  |
| **Diamond** | 0.17 | 0.45 |  |
| **Iron** | 0.56, 0.57, 0.58 | 0.77, 0.78, 0.78 |  |
| **Copper** | 0.95, 0.64, 0.54 | 0.98, 0.82, 0.76 |  |
| **Gold** | 1.00, 0.71, 0.29 | 1.00, 0.86, 0.57 |  |
| **Aluminum** | 0.91, 0.92, 0.92 | 0.96, 0.96, 0.97 |  |
| **Silver** | 0.95, 0.93, 0.88 | 0.98, 0.97, 0.95 |  |

### Material Simplification

Material simplification occurs when one of the following limits is not matched by a material:

* For **Blendable GBuffer** format, if a material has more than one closure.
* For **Adaptive GBuffer** format, if a material has more closures-per-pixel than the project / platform settings, or if the number of bytes-per-pixel is beyond the project settings.

With these parameters in mind, the material is simplified by merging slabs with parameters blending until the requirements are met. The simplification reasons and the details are visible in the Substrate panel (**Window > Substrate**).

[![Substrate stats panel in the Material Editor.](https://dev.epicgames.com/community/api/documentation/image/1a5ca9ab-c75a-4ff4-ad3e-d6c47daf64f5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1a5ca9ab-c75a-4ff4-ad3e-d6c47daf64f5?resizing_type=fit)

Substrate stats panel in the Material Editor.

For projects / platforms using the Blendable GBuffer format, the final material is forced to use a single feature per pixel, corresponding to a legacy Shading Model. These features are (by order of priority):

* Fuzz
* Subsurface Scattering (with or without a Profile)
* Haziness

If several features are enabled at the same time for a given pixel, only the highest priority feature is used. Note that anisotropy can be enabled independently of the other features.

In the example material below, the Substrate material was out of budget and has been simplified accordingly when looking at the Substrate stats panel in the Material Editor.

[![A simplified Substrate material that was out of budget.](https://dev.epicgames.com/community/api/documentation/image/44f829ae-4f4a-4c69-a67f-c6f30bbfaa7d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/44f829ae-4f4a-4c69-a67f-c6f30bbfaa7d?resizing_type=fit)

A simplified Substrate material that was out of budget.

Substrate supports multiple visual features that can be enabled for each Slab (or automatically when using the SubstrateShadingModel expression node). These shading models include:

* F90
* Fuzz
* SSS effects (SSS Profile, Wrapped, Simple Volume)
* Haziness
* Anisotropy
* Specular Profile
* Glints

When using the Blendable GBuffer format, some features are not supported. These include:

* F90
* Diffusion SSS with per-pixel MFP
* Haziness
* Glints

In this case, the feature will be visually missing from the material. Note that Specular LUT is supported but approximated as a view-dependent only effect.

Below is a visual comparison of these features between the two GBuffer formats:

![Adaptive GBuffer Format](https://dev.epicgames.com/community/api/documentation/image/d6633372-8d56-4382-a573-2259a567d300?resizing_type=fit&width=1920&height=1080)

![Blendable GBuffer Format](https://dev.epicgames.com/community/api/documentation/image/e2e1a717-46f8-4d6a-872d-6d64f0cc2af3?resizing_type=fit&width=1920&height=1080)

Adaptive GBuffer Format

Blendable GBuffer Format

For performance reasons, during lighting evaluation, these features are mapped onto complexity sets, corresponding to increasingly higher evaluation cost:

* Simple: default lit material (colored diffuse and specular, roughness)
* Single: F90 color, Fuzz, SSS effects (Profile, Wrapped, and Simple Volume using MFP), Clear Coat.
* Complex: Anisotropy, Specular profile, Eye, and Hair
* Complex Special: Glints

### Substrate Material Nodes

You can use the following types of nodes to author a Substrate material:

| Type of Node | Description |
| --- | --- |
| [BSDFs](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.5) | These nodes represent most types of surfaces, from simple materials to more complex ones like hair, eyes, and water. |
| [Operators](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.5) | These nodes mix and layer multiple Substrate Slab BSDFs to create complex and varied surfaces. |
| [Building Blocks](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.5) | These nodes translate common material types for use with Substrate, like creating a coated layer or the default legacy material shading model of Unreal Engine. |
| [Extras](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.5) | These nodes define a Material Domain for a Substrate Material, and are directly analogous to their legacy Material Domain namesakes. |
| [Helpers](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.5) | These nodes are used to do some conversion within the material, such as mapping transmittance to Mean Free Path for a Substrate Slab. |

#### Substrate BSDF Nodes

Substrate **BSDF** (Bidirectional Scattering Distribution Function) nodes are used to represent most types of surfaces, they control the visual look of materials you author and automatically set their domain and shading model accordingly. The goal is to remove these aspects from being manually set on the material root node through the Details panel.

Substrate includes the following BSDFs:

[![Substrate BSDF Nodes](https://dev.epicgames.com/community/api/documentation/image/f81634eb-c312-4046-9230-9bdff264671a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f81634eb-c312-4046-9230-9bdff264671a?resizing_type=fit)

The Slab BSDF is the primary node for authoring in Substrate and can be layered with other slabs. The other BSDFs are for specialized use cases and must be used on their own without mixing with other BSDFs.

| Substrate BSDF Node | Description |
| --- | --- |
| **Substrate Slab BSDF** | The principled representation of a slab of matter that aggregates multiple components: diffuse, specular, haziness, cloth fuzz, and anisotropy. It can render effects such as opaque subsurface or translucent scattering and translucent transmittance subsurface scattering. |
| **Substrate Eye BSDF** | A BDFS dedicated to rendering eye materials with Substrate. This includes specific inputs for the cornea and iris. |
| **Substrate Hair BSDF** | A BDFS dedicated to rendering hair materials with Substrate. |
| **Substrate Simple Clear Coat** | Provides a simple and fast way to render a material with a clear top coat. This node uses the Substrate Slab BSDF in the background, but simplifies the workflow for clear coat rendering. It is optimized to render legacy Clear Coat materials. |
| **Substrate SingleLayerWater BSDF** | A BSDF dedicated to rendering of a [Single Layer Water](https://dev.epicgames.com/documentation/en-us/unreal-engine/single-layer-water-shading-model-in-unreal-engine) material primarily used with the [Water](https://dev.epicgames.com/documentation/en-us/unreal-engine/water-system-in-unreal-engine) system. |
| **Substrate Unlit BSDF** | A BSDF used to render unlit elements with a colored emissive luminance. This Substrate node replaces legacy grayscale opacity with colored transmittance.  If you need to blend an Unlit Slab, use a regular Substrate Slab with only Emissive Color input being used. Coverage Weight operator can be used. |
| **Substrate Volumetric-Fog-Cloud BSDF** | A BSDF used to represent a participating medium. This node is used to render Volumetric Clouds and Heterogeneous Volumes. |

#### Substrate Operator Nodes

**Substrate Operator** nodes mix or layer multiple [Substrate Slabs](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.5) to create complex and varied surfaces. If the Substrate Slab represents a piece of matter, Operators present ways to combine those pieces.

The following Substrate Operators are available to choose from:

[![Substrate Operator Nodes](https://dev.epicgames.com/community/api/documentation/image/7e8d788a-832e-4b59-8d79-c097c1c71a05?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7e8d788a-832e-4b59-8d79-c097c1c71a05?resizing_type=fit)

Substrate Operators do not work with all [Substrate BSDFs](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.5). Only **Substrate Slab BSDF** and **Substrate Simple Clear Coat** can use these Operator nodes.

| Substrate Operator Node | Description |
| --- | --- |
| **Substrate Coverage Weight** | This operator takes input from a Slab and controls the amount of coverage it has where Weight is the amount of coverage. Reducing the weight reduces the coverage of matter of the slab, meaning you will see through to the matter underneath. The weight is similar to the Opacity input on the root node in the Legacy material. For instance, it can be used to make surfaces translucent when using a translucent blend mode or to reduce the visibility of a clear coat top layer. |
| **Substrate Horizontal Blend** | This operator takes input from two Slabs: a Background and Foreground. The Mix input controls how much these two Slabs mix together using a linear interpolation. This can be used for a soft transition between slabs over a surface. |
| **Substrate Vertical Layer** | This operator takes input from two Slabs: a Top and Bottom layer. Top slab is layered above the Bottom slab, with the bottom layer's appearance influenced by the properties of the top layer. Use the Top Thickness input to control how thick the top layer is over the bottom. This operator is ideal for creating car paints, wood varnishes, and wetness on a surface. |
| **Substrate Add** | This operator takes input from two Slabs and adds them together. The material created is not physically plausible because it creates more outgoing energy from the surface than incoming energy.  This node should be avoided whenever possible. |
| **Substrate Select** | This operator takes input from two Substrate materials paths and selects a single one. Both paths have parameter blending enabled so that, in the end, one and only one Slab material remains.  It can be used to stochastically select Slabs with and without subsurface profiles for instance using Blue noise. It is interesting for performance since it enforces a single Slab as output, so a single closure per pixel will be evaluated during the lighting passes. |

Operator nodes include an option to parameter blend their input slabs into a single slab when toggling on **Use Parameter Blending**. Because Substrate Operators can create complex material appearances by mixing and layering slabs together, their expense at runtime (primarily due to lighting evaluation) can be costly to performance. Parameter blending is an optimization that trades visual accuracy and expensive lighting evaluation for runtime performance and less costly lighting evaluation.

For more information on this parameter blending optimization, see the [Parameter Blending](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.5) section of this page.

##### Substrate Coverage Weight

The **Substrate Coverage Weight** Operator controls the ratio of two slabs in a vertical layering operation. The **Weight** input drives the coverage of this material when layering together with a [Substrate Vertical Layer Operator](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.5) (like the example below). You can also use the operator to achieve translucent surfaces when using alpha-as-coverage or alpha-as-opacity, similar to how the Translucent Blend Mode uses opacity.

[![Substrate Coverage Weight](https://dev.epicgames.com/community/api/documentation/image/95b955c6-75c2-42f1-b9a6-fc6300adcec8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/95b955c6-75c2-42f1-b9a6-fc6300adcec8?resizing_type=fit)

The graph above uses the **Substrate Coverage Weight** Operator, where **Weight** drives the amount of coverage applied over the bottom slab. A weight of 1 is fully opaque, blocking the green textured pattern. 0.5 is 50% transparent, mixing the two materials' colors and showing the texture pattern. 0 is fully transparent and shows only the green textured pattern.

[![Substrate Coverage Weight Examples](https://dev.epicgames.com/community/api/documentation/image/3ad7c097-8643-43f5-86c6-4ef02d402fa7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3ad7c097-8643-43f5-86c6-4ef02d402fa7?resizing_type=fit)

##### Substrate Horizontal Layer

The **Substrate Horizontal Layer** Operator mixes two slabs together, one representing the background and the other the foreground. The **Mix** input controls their mixture ratio using linear interpolation.

[![Substrate Horizontal Blend Node](https://dev.epicgames.com/community/api/documentation/image/5da7c6d5-9675-4eca-95c5-a5ab4452939f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5da7c6d5-9675-4eca-95c5-a5ab4452939f?resizing_type=fit)

The **Background** input is fully visible when it is **0**, and the **Foreground** is fully visible when it equals **1**. When the mix ratio is **0.5**, the slabs are mixed together, and the mix is evaluated per-pixel. The Mix input can use textures to control the mix ratios, like the example below.

[![Substrate Horizontal Blend Example Material](https://dev.epicgames.com/community/api/documentation/image/80ac63c1-40fb-40bb-aff9-b9d127ec5b44?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/80ac63c1-40fb-40bb-aff9-b9d127ec5b44?resizing_type=fit)

##### Substrate Vertical Layer

The **Substrate Vertical Layer** Operator layers the **Top Slab** and **Bottom Slab**. This node takes into account the thickness of the top layer to apply physically correct transmittance and scattering, which is similar to a coating operation, with the top layer covering the bottom layer. The appearance of the Bottom slab is dependent on the properties of the Top slab. If the BSDF passed into the Top input is fully opaque, the bottom slab is not seen at all.undefined

Vertical layering is particularly useful in situations that call for a transparent, or semi-transparent, top coat over an opaque bottom layer. Examples include car paint, varnished wood surfaces, or wetness on a surface, such as puddles of water.

##### Substrate Add

The **Substrate Add** Operator combines two slabs and outputs their result. This operator is not considered physically plausible because it can produce a material where the outgoing energy from the surface exceeds the incoming energy. It is useful when art direction is more important than being physically plausible. However, to maintain physically accurate surfaces, this operator should be avoided.

[![Substrate Add Node Example](https://dev.epicgames.com/community/api/documentation/image/590df50d-7853-4342-8b20-48ee1fb95b1a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/590df50d-7853-4342-8b20-48ee1fb95b1a?resizing_type=fit)

#### Substrate Building Block Nodes

The **Substrate Building Block** nodes are a set of [Material Functions](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-functions-in-unreal-engine) that provide translations for some common use cases. Because these are material functions, you can open and inspect them directly.

The following Substrate Building Blocks are available to choose from:

[![Substrate Building Block Nodes](https://dev.epicgames.com/community/api/documentation/image/e535e213-31d6-4b5d-81e9-4046c8a48175?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e535e213-31d6-4b5d-81e9-4046c8a48175?resizing_type=fit)

| Substrate Building Block Node | Description |
| --- | --- |
| **Substrate Coated Layer** | A material function that creates a coated material made of two slabs layered on each other. It exposes user-friendly parameters to control the coat interface and absorption. |
| **Substrate Standard Surface Opaque** | A material function that creates an uber-shader-like Substrate material with a user-friendly parameterization for opaque surfaces. The parameterization uses industry standard vocabulary and notions. |
| **Substrate Standard Surface Translucent** | A material function that creates an uber-shader-like Substrate material with a user-friendly parameterization for translucent surfaces. The parameterization uses industry standard vocabulary and notions. |
| **Substrate UE4 Default Shading** | A material function that replicates the default shading model with Substrate for diffuse, metallic, and specular parameterization used in non-Substrate Materials. |
| **Substrate UE5 Unlit Shading** | A material function that recreates the UE4 Unlit shading model with Substrate. |

#### Substrate Extras Nodes

The **Substrate Extras** nodes specify the type of material and function it serves, such as setting the Substrate material to be used as a decal or light function. These nodes are directly analogous to non-Substrate Materials that were assigned them as part of their Material Domain.

The following Substrate Extras are available to choose from:

[![Substrate Extras Nodes](https://dev.epicgames.com/community/api/documentation/image/8d584dda-875d-4747-b781-1f98a42cb57e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8d584dda-875d-4747-b781-1f98a42cb57e?resizing_type=fit)

These nodes are monolithic and must be used in isolation. They are not compatible with [Substrate Operators](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.5).

As a good habit, we recommend placing these nodes at the end of the material graph, right before plugging into the **Front Material** input.

| Substrate Extras Node | Description |
| --- | --- |
| **Substrate Convert To Decal** | Any material graph can be used as a decal. This node specifies the material will be converted and used as a Decal material only. |
| **Substrate Light Function** | This node specifies the material will be used as a [Light Function](building-virtual-worlds\lighting-and-shadows\features-of-lights\light-functions) only. It must be used in isolation. |
| **Substrate Post Process** | This node specifies the material will be used as a [Post Process Material](https://dev.epicgames.com/documentation/en-us/unreal-engine/post-process-materials-in-unreal-engine) only. It must be used in isolation. |
| **Substrate UI** | This node specifies the material will be used as a User Interface element only, such as ones designed to be used with [UMG UI Designer](https://dev.epicgames.com/documentation/en-us/unreal-engine/umg-editor-reference-for-unreal-engine). It must be used in isolation. |

For example, when using the **Substrate Convert To Decal** node, any Substrate Material can be used as a decal material applied to Mesh Decals and Decal Actors in the scene.

Extras nodes automatically set the **Material Domain** when connected to the **Front Material** input of the **Material Root** node. Some Extras nodes require the [Blend Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.5) to be changed to support the output.

[![Substrate Convert-to-Decal example](https://dev.epicgames.com/community/api/documentation/image/df32adcf-f49a-4843-92b7-4c9e1887f5ff?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/df32adcf-f49a-4843-92b7-4c9e1887f5ff?resizing_type=fit)

When using the **Substrate Convert To Decal** node, you must set the Blend Mode to **TranslucentGrey Transmittance**, **Colored Transmittance**, **TranslucentColorTransmittance**, or **AlphaComposite (Premultiplied Alpha)**. Otherwise, an error is displayed in the **Stats** panel of the Material Editor.

#### Substrate Helper Nodes

The **Substrate Helper** nodes are a set of nodes and material functions to perform some conversion or achieve something that legacy materials could do.

[![Substrate Helper Nodes](https://dev.epicgames.com/community/api/documentation/image/8eb8758f-e701-434c-9268-e3eca3597a98?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8eb8758f-e701-434c-9268-e3eca3597a98?resizing_type=fit)

| Substrate Helper Node | Description |
| --- | --- |
| **Substrate Flip Flop** | Controls the surface reflectivity based on the view incident angle. It allows interpolations of a normal-facing color (F0) to a grazing-angle color (F90), based on the view angle, and it controls the interpolation speed with the falloff parameter. |
| **Substrate Haziness-To-Secondary-Roughness** | Compute a second specular lob roughness from a base surface roughness and haziness. This parameterization ensures that the haziness makes sense physically and is perceptually easier to author. |
| **Substrate IOR-To-F0** | Convert a dielectric IOR into a F0 value. |
| **Substrate Metalness-To-DiffuseColorF0** | Convert a metalness parameterization (BaseColor / Specular / Metallic) into DiffuseAlbedo / F0 parameterization. |
| **Substrate Rotation-To-Tangent** | Convert a rotation angle into a tangent vector. |
| **Substrate Thin-Film** | Compute the resulting material specular parameters F0 and F90 according to thin film parameters. |
| **Substrate Transmittance-To-MeanFreePath** | Convert a transmittance color corresponding to a Slab of participating media viewed perpendicularly to its surface into a Mean Free Path. This node directly maps to the Slab BSDF SSS MPF Input. |
| **Substrate View-Dependent-Coverage** | Adapts the coverage based on the view-incident angle. This node is useful for mixing a layer whose thickness is large enough to imply a view-dependent effect. For instance, large grains of dust would have greater occlusion at a grazing angle compared to an incident angle. |

### Additional Notes about Substrate Nodes

* **Substrate Decal Materials**

  + Substrate Decals currently use the same features as the legacy Decals blend mode path.
  + Future versions of Substrate Decals look to offer a more robust feature set similar to other features already available with Substrate, like Layer Translucent Slabs for things like water, blood, and goo. For example, having layers that can erode according to thickness like car paint scratches, ground steps, and tire marks.
* **Substrate Shading Models Node**

  + Opening any prior created material once Substrate is enabled for your project automatically converts the material to use its slabs. All existing inputs are fed into a **Substrate Shading Model** node.

  [![Substrate Shading Models Node](https://dev.epicgames.com/community/api/documentation/image/01dfbfa4-8400-4c6c-82ab-372c920a6dd5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/01dfbfa4-8400-4c6c-82ab-372c920a6dd5?resizing_type=fit)

  Avoid manually adding or using this node when creating new Substrate materials.

### Substrate Stats Panel

The **Substrate** stats panel is available in the Material Editor below the Material Graph.

[![Substrate Stats Panel](https://dev.epicgames.com/community/api/documentation/image/af0dfd4b-cbe7-4b5f-9307-ced87ef95e59?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/af0dfd4b-cbe7-4b5f-9307-ced87ef95e59?resizing_type=fit)

The Substrate panel displays stats about the material, topology, its features, and simplification.

[![Substrate Stats Panel](https://dev.epicgames.com/community/api/documentation/image/3433f2a6-0b68-4af9-aea3-b320d306abce?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3433f2a6-0b68-4af9-aea3-b320d306abce?resizing_type=fit)

### Parameter Blending with Operators

Using multiple BSDFs (Bidirectional Scattering Distribution Functions) per pixel slows the rendering process proportionally to their count in the material graph. It is twice as slow to evaluate the lighting for two BSDFs as it is a single one. This is true for both opaque and translucent surfaces.

Operator nodes include a **Use Parameter Blending** checkbox that attempts to optimize the performance and memory footprint of the material while maintaining the appearance of all the mixing and layer operations in the graph. Only the rightmost Operator node before the Material Root node must have the setting enabled. All other nodes in the graph automatically apply parameter blending.

Parameter blending is a good fallback option when the performance of multiple Slabs in a material is a concern. When enabled, two Slabs are merged into a single Slab that needs only a single lighting evaluation. This merge uses a lot less memory than two individual slabs.

[![Substrate Operators Use Parameter Blending checkbox](https://dev.epicgames.com/community/api/documentation/image/3e67edc7-bc9c-49c6-abec-5e4075b98ce1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3e67edc7-bc9c-49c6-abec-5e4075b98ce1?resizing_type=fit)

The example materials below are taken from [Content Examples Substrate Level](https://www.fab.com/listings/4d251261-d98c-48e2-baee-8f4e47c67091) without and with **Use Parameter Blending** enabled.

This material (M\_Substrate\_ShaderBall\_IceRocks) uses two BSDFs. The left is without any blending and the right is using parameter blending.

[![Substrate Parameter Blending Example](https://dev.epicgames.com/community/api/documentation/image/c7c10bdd-aed1-4a0e-9a9c-bc24514ea51e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c7c10bdd-aed1-4a0e-9a9c-bc24514ea51e?resizing_type=fit)

This is a more complex material (M\_Substrate\_ShaderBall\_AnisoOverSSS) that blends four slabs using two Vertical Layer Operators and a single Coverage Weight Operator. The material has a memory cost of 108 bytes per pixel. With Use Parameter Blending enabled, blending on all operators comes down to 28 bytes per pixel. The left material is without any blending and the right uses parameter blending.

[![Substrate Parameter Blending Example](https://dev.epicgames.com/community/api/documentation/image/ae7c3de8-d654-44f8-bbef-3863cc866578?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ae7c3de8-d654-44f8-bbef-3863cc866578?resizing_type=fit)

Aside from Parameter Blending on Operators nodes, you can use one of the following workflows to achieve similar results:

* Blend the DiffuseAlbedo, F0, F90, Roughness, and other attributes manually in the graph. Pass all the attributes into a single Slab connected to the Front Material input. This approach can work well for isolated cases but may become unmanageable for a large library of complex materials.
* Use the graph-based [Layered Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/layered-materials-in-unreal-engine) workflow. Since it employs material functions to reuse work, this can scale better than the first option.

On lower end platforms, such as mobile, the compiler automatically enables parameter blending for the sake of performance. On intermediate platforms, parameter blending is progressively introduced on the bottom layers of a material in order to remain within the target performance and memory constraints.

### Metalness and Specular Response

The parameterization used by Substrate differs from the DefaultLit Shading Model in non-Substrate (or legacy) materials — there is no longer a Metallic input. This parameterization attempts to do away with abstracted values (like metallic and specular) and moves toward physical properties with real-world units.

The reflective properties and specular response of Substrate Materials are defined with three attributes: DiffuseAlbedo, F0, and F90. Substrate enforces energy conservation automatically, ensuring the specular interface and medium do not add any energy. Therefore, the higher F0 gets, the less visible the diffuse contribution will be.

Metalness is emulated using the **Substrate Metalness-To-DiffuseAlbedo-F0** Helper node. It takes BaseColor, Specular, and Metallic values as inputs and converts them to values which map to **Diffuse Albedo** and **F0** on the Substrate Slab.

[![Substrate Metalness-To-DiffuseAlbedo-F0.](https://dev.epicgames.com/community/api/documentation/image/13fd661b-2e38-4741-b472-ea3dd101c0c7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/13fd661b-2e38-4741-b472-ea3dd101c0c7?resizing_type=fit)

It's possible to achieve a wide variety of complex material diffuse and specular response to light using the **EdgeColor** or **F90** inputs. For example, a red sphere with cyan-to-yellow perpendicular-to-tangent specular reflections.

[![Substrate Metalness-to-DiffuseAlbedo-F0 Example](https://dev.epicgames.com/community/api/documentation/image/d7db7b6a-5cbe-487e-95fa-46f555bb9a38?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d7db7b6a-5cbe-487e-95fa-46f555bb9a38?resizing_type=fit)

**Substrate FlipFlop** Helper nodes are useful for achieving normal-based specular colorization. It controls the specular color of F0 and F90 as a function of NoV with adjustable falloff transition.

### Rough Refraction

Substrate supports rough refraction through translucent objects and layered opaque materials with a translucent top layer. The blurriness of the scene background, as well as the distance to the refracted object, is computed from the primary material roughness when you use distortion / refraction as well as the distance to the refracted object.

#### Translucent Rough Refraction

To create a translucent material with rough refraction, set the following properties in the **Details** panel.

* **Blend Mode:** TranslucentColoredTransmittance, TranslucentGreyTransmittance, or ColoredTransmittanceOnly.
* **Refraction Method:** Index of Refraction (IOR), Pixel Normal Offset, or 2D Offset.

Pass values into **Refraction**, **Roughness**, and **SSS MFP**. The graph below produces a simplistic frosted glass result when roughness is greater than 0. A high SSS MFP value is used to create a fully transparent material, while the IOR of 1.514 approximates that of glass.

[![Substrate Translucent Rough Refraction Example Graph.](https://dev.epicgames.com/community/api/documentation/image/e01895c2-0207-4a96-aee9-d4c817ad2e12?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e01895c2-0207-4a96-aee9-d4c817ad2e12?resizing_type=fit)

In the examples below, as the value of Roughness increases (0, 0.2, and 0.6 left to right), objects behind the glass become blurrier.

[![Substrate Translucent Rough Refraction Examples.](https://dev.epicgames.com/community/api/documentation/image/30fef83a-b02f-4740-a4e2-fd601d2dc107?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/30fef83a-b02f-4740-a4e2-fd601d2dc107?resizing_type=fit)

The blurring from rough refraction uses an approximation for accounting for depth behind translucent elements in the scene.

#### Opaque Rough Refraction

Substrate coating layers can blur the layers beneath them based on the roughness and thickness of the top coating layer. This type of refraction is more costly to performance and must be enabled for the project in the Project Settings under the **Engine > Rendering** category. Check the box for **Substrate opaque material rough refraction** to enable this feature.

[![Project Setting for Substrate Opaque Rough Refraction](https://dev.epicgames.com/community/api/documentation/image/0648231e-be80-41d1-9039-b1f6b56d509e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0648231e-be80-41d1-9039-b1f6b56d509e?resizing_type=fit)

The graph below shows an example using opaque material rough refraction using a vertically layered material with a clear coat on top of an opaque checkerboard.

[![Example of using an opaque material rough refractions with Substrate.](https://dev.epicgames.com/community/api/documentation/image/c4ea0a2a-3f13-4926-ba54-220bec2540ec?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c4ea0a2a-3f13-4926-ba54-220bec2540ec?resizing_type=fit)

The **Roughness** and **Thickness** parameters determine the strength of the blur being applied to the bottom material layer. Increasing either value increases how blurred the refraction becomes.

You can see this in the examples below, where the clear coat top layer on the left has a roughness and thickness of 0.1. The example on the right has a roughness of 0.8 and a thickness of 6, causing the bottom layer to become blurred.

[![Substrate Rough Refractions Thickness Examples](https://dev.epicgames.com/community/api/documentation/image/7ae0f9b3-8a26-4d07-9a03-96b05acd43a7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7ae0f9b3-8a26-4d07-9a03-96b05acd43a7?resizing_type=fit)

### Substrate Layer Thickness

The thickness of the bottom layer is implicitly fixed at 0.01 centimeters.

* For **Opaque surfaces** (surfaces where one can't see through) this thickness is **not** relevant.
* For **Translucent surfaces** (surfaces where one can see through), you can use the Transmittance to MFP node where the desired transmittance is expressed for a given thickness.
* For **Thin surfaces** (surfaces having a thickness but too thin to be modeled with geometry), the Is Thin Surface option on the material can be enabled. The thickness of the bottom layer is then specified on the root node.

### Substrate Material Instance Override

It is possible to override certain material properties on a material instance (shading model, specular profiles, etc). These overrides come with some limitations:

* **Shading Model** override is only available if the material only contains SubstrateShadingModel nodes. If the material contains Slabs, the override option is not available.
* **Specular Profile** override is available only if a slab contains a specular profile. If an override is provided, it will override all slabs' specular profiles (if there are any).

### Subsurface Scattering and Participating Media

A Substrate Slab contains participating media and can be used to simulate various volumetric appearances.

For instance, if you render an opaque material only, when a slab is at the bottom of the material topology, it is considered for subsurface scattering. There are two things to consider:

* If a [Subsurface Profile](https://dev.epicgames.com/documentation/en-us/unreal-engine/subsurface-profile-shading-model-in-unreal-engine) is assigned to a Slab in the Details panel of the Material, the profile is used per pixel. Keep in mind that Subsurface Profiles are **not** blendable.
* If there is no Subsurface Profile assigned, scattering is determined from the DiffuseAlbedo and SSS MPF properties of the Slab. These properties are blendable.

The **MFP** (or Mean Free Path) of Subsurface Scattering is the distance (in centimeters) that different wavelengths of light will penetrate through a medium before encountering a collision. The example below shows a DiffuseAlbedo (colored white) and a **SSS MFP** (colored red) scaled from 0 to 1, left to right.

[![Substrate MFP scaled from 0 to 1.](https://dev.epicgames.com/community/api/documentation/image/790916fc-3ea5-410b-8ab3-fce0b6795be9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/790916fc-3ea5-410b-8ab3-fce0b6795be9?resizing_type=fit)

Any slab not at the bottom of an opaque material or used in a translucent one, is considered for a volumetric representation, which also relies on DiffuseAlbedo and SSS MFP attributes. The DiffuseAlbedo represents the medium's base color, accounting for single and multiple scattering.

The **SSS MFP** attribute is a way to control the medium's transmittance for a view perpendicular to a surface — it represents how visible the surface below is. The**Diffuse Color** represents the amount of light scattering, also respecting the MFP distance.

[![Substrate SSS MFP grid of examples.](https://dev.epicgames.com/community/api/documentation/image/6114e72a-c2ad-433f-a602-6457f4e602e0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6114e72a-c2ad-433f-a602-6457f4e602e0?resizing_type=fit)

*Examples of a material with transmittance color ranging from black to blue from left to right, and DiffuseAlbedo ranging from black to white from bottom to top.*

Vertically layering a Slab on top of another is similar to a coating operation. The visibility of the bottom Slab is dependent on the transmittance of the top Slab. It is possible to reduce the coverage of the top Slab (like at the edge of a puddle of water on a surface) to make it progressively disappear. You can achieve this using a **Coverage Weight** operator node, which is analogous to alpha blending.

[![Substrate SSS MFP grid of examples.](https://dev.epicgames.com/community/api/documentation/image/4a8246cb-f372-43a8-b055-412c36a6d037?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4a8246cb-f372-43a8-b055-412c36a6d037?resizing_type=fit)

*Examples of a material with Transmittance ranging from black to blue from left to right, and coverage ranging from 0 to 1 from bottom to top.*

To achieve a specific transmittance or scattering color, you should use the **Substrate Transmittance-To-MeanFreePath** Helper node. The MFP is derived for the **TransmittanceColor** to match at normal incidence — when the surface is viewed perpendicularly, along the normal.

The example below shows a blue subsurface scattering on an opaque material that is pink, where the SSS MFP is derived from Transmittance Color.

[![Example using Substrate Transmittance-To-MeanFreePath Subsurface Scattering.](https://dev.epicgames.com/community/api/documentation/image/dd6296b2-48f6-485b-bba1-105392b82a44?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dd6296b2-48f6-485b-bba1-105392b82a44?resizing_type=fit)

**Authoring Recommendation:**

The mean free path (MFP) represents the same light behavior for translucent or opaque material with subsurface scattering: the mean path inside a medium before light will interact with matter: either be absorbed or scattered. But it can be interesting to author it differently for different use cases.

For translucent (optically thin, see-through) surfaces, it is not recommended to directly control MFP when trying to achieve a particular transmittance color because MFP is not a color, it's a measurement of light transport. It is instead recommended to use the Transmittance-To-MeanFreePath node.

For surfaces with Subsurface scattering (optically thick, opaque), the MFP can be authored directly. In this case it roughly represents the distance in centimeters the light will scatter for each of its components.

## Coverage versus Transmittance

**Coverage** defines the presence of material and can be thought of as a "mask" defining where and how much the material is present.

* **0** means no coverage at all: the layer is not visible.
* **1** means full coverage: the layer is completely covering the surface.

Materials can be blended by adjusting their coverage. In Substrate, the coverage is controlled with the **Coverage Weight** node.

**Transmittance** defines how the light interacts with the material: how much light passes through it.

* **0** means no light is transmitted: the material is fully opaque.
* **1** means light is fully transmitted: the material absorbed no light, and you can fully see through it.

In Substrate, the transmittance is controlled by the **MeanFreePath** input on the Slab. Mean-Free-Path (MFP) defines the average distance at which a light ray interacts with the matter.

* An MFP of 0 means a light ray always hits the matter and does not travel through the material. This is equivalent of a transmittance of 0.
* An MFP of infinite means, a light ray never hits the matter and so travels through it. This is equivalent to a transmittance of 1.

For ease, a **Transmittance-To-MFP** node is provided, translating a particular transmittance color achieved at a particular depth into a mean-free-path.

The **Coverage** will only have a "grey scale" impact on the material appearance (less or more of the material will be visible). On the other hand, the **Transmittance** can change the color of the transmitted light based on its MFP value. Certain colors will be absorbed while others will be transmitted, creating colored transmission. To achieve, the blend mode needs to be set to **TranslucentColoredTransmittance**. For performance, you might want to fallback to grey transmission with**TranslucentGreyTransmittance**.

### Translucency and Blend Modes

Substrate offers more robust options for translucent surface shading than is possible with traditional non-Substrate materials. The list of [Substrate Blend Modes](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.5) now makes more sense when considering a surface is made of matter (a Substrate Slab).

To create a Translucent Material:

1. Choose a **Blend Mode** that supports translucency.

   * TranslucentColoredTransmittance
   * TranslucentGreyTransmittance
   * ColoredTransmittanceOnly
2. With the Material Root node selected, use the **Details** panel to select a **Lighting Mode**. Choose between:

   * Surface Forward Shading
   * Surface Translucency Volume — this option supports reflections on the surface.
   * Volumetric NonDirectional — cheaper to use but does not reflect light.

Below is an example setup of a translucent Substrate material. Its Blend Mode is set to **TranslucentColoredTransmittance** and uses the **Surface ForwardShading** Lighting Mode. It uses a single Slab passed into the Front Material pin of the Material Root node to produce a translucent material that appears opaque.

[![Example of an opaque translucent Substrate material.](https://dev.epicgames.com/community/api/documentation/image/e63d1c0f-766a-4214-9bf8-25da1c06e7a6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e63d1c0f-766a-4214-9bf8-25da1c06e7a6?resizing_type=fit)

Using the **Substrate Coverage Weight** Operator between the Slab and the Front Material input controls the transmittance of the material. Use the **Weight** input on the Substrate Coverage Weight node to control how transparent the material is.

[![Example of a clear translucent Substrate material.](https://dev.epicgames.com/community/api/documentation/image/d0144fbc-44ed-4712-a975-9a0a725299de?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d0144fbc-44ed-4712-a975-9a0a725299de?resizing_type=fit)

You can use a constant value of 0 to 1 to control the opacity of the entire material (like above) or use a texture (like below) to control parts of the material.

[![Example of a masked translucent Substrate material.](https://dev.epicgames.com/community/api/documentation/image/ca06c39f-6989-4643-bb73-897f9550a095?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ca06c39f-6989-4643-bb73-897f9550a095?resizing_type=fit)

You can go a step further to create a slab of matter that resembles colored glass by specifying the MFP of the participating medium. This is set up using the **Transmittance-To-MeanFreePath** Helper node, like in the example below, using an orange TransmittanceColor connected to SSS MFP to tint the material orange only in regions where it transmits light. The specified TransmittanceColor is the "target" color, which is reached at the provided thickness input (default is 0.01 centimeters).

[![Example of a colored transmittance used with a masked translucent Substrate Material.](https://dev.epicgames.com/community/api/documentation/image/55c1f0d7-46a3-4336-8029-4761f7e4ff48?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/55c1f0d7-46a3-4336-8029-4761f7e4ff48?resizing_type=fit)

#### Additional Notes about Substrate Translucency

* Translucent materials do not support Screen Space Subsurface Scattering, even though the Slab is considered a volume of participating medium.

## Substrate Performance

Overview of performance costs:

* When using **a single SubstrateShadingModel** node, or using the Legacy inputs, the overall cost should be similar to the Legacy model. Base pass, lighting, pass, and others should have roughly the same cost.
* When using a **single Slab** with **multiple features**, such as using multiple features at the same time, advanced features like glints, or when using multiple slabs within a material, the frame cost starts to increase.
* When using **multiple Slabs** without parameter blending, the second slab will be more expensive, and following slabs will increase the cost almost linearly.

Substrate uses a material classification pass after the base pass to help the lighting pass to run more efficiently. This adds some small, fixed overhead after the base pass but helps reduce lighting cost overall. You can use the debug view mode to understand the cost:

* Material count displays the number of closures executed per pixel and visualizes what is potentially expensive.
* Material classification displays the lighting complexity at pixels / tiles will run.

## Substrate Debug View Modes

When using Substrate, it's useful to see how its materials are performing and which would benefit from more attention. Substrate's debug visualization modes are in the **View Modes** dropdown list under the **Substrate** category.

[![Select a Substrate Debug View Mode in the Level Editor.](https://dev.epicgames.com/community/api/documentation/image/e6b99fb5-a40d-4338-916f-bfffeca96875?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e6b99fb5-a40d-4338-916f-bfffeca96875?resizing_type=fit)

Substrate includes the following visualization modes for debugging:

Click images in the table to enlarge them.

| Debug Visualization | Debug Visualization Name | Description |
| --- | --- | --- |
|  | **Material Properties** | Visualize Substrate properties under the mouse cursor. Hover over the pixel you want to inspect with your mouse, and you will see the final packed material closure used for lighting, such as properties, colored weight, enabled features of the material, used bytes, and more. |
|  | **Material Count** | Visualize Substrate material count per pixel and color them according to the number of BSDF Slab nodes they are using. |
|  | **Material Bytes Count** | Visualize Substrate material footprint per pixel. Materials are color-coded to the number of bytes they are using. You can also hover your mouse over a material to see the bytes per pixel of the material. |
|  | **Substrate Info** | This mode summarizes information about the use of Substrate in the project, including information about max memory usage, max bytes per pixel (which is useful for setting simplification thresholds) and enabled Substrate features. |
| Substrate Advanced View Modes |  |  |
| --- | --- | --- |
|  | **Advanced Material Properties** | Reports information about the different Substrate Slabs composing the Material currently under the mouse cursor. Each slab is presented separately on screen.  This view mode must be enabled in the Project Settings under the **Engine > Rendering** category with the checkbox **Substrate advanced visualization shaders**. |
|  | **Material Classification** | This mode shows the material complexity per tile and returns a color coded result:   * **Green** denotes a simple, Disney-like material using a Legacy Slab. * **Yellow** indicates a single Slab material with any features but Anisotropy enabled. * **Red** indicates that either multiple Slabs are mixed or layered in the tile, or the material has Anisotropy enabled.   You can get a hint at the complexity of a Substrate material by looking at the Slab node to see if it is **Simple**, **Single**, or **Complex**. |
|  | **Rough Refraction Classification** | This mode displays materials that use the Opaque Rough Refraction property. This mode also distinguishes between Substrate materials that have subsurface scattering enabled or disabled.  The tiles shown in some of these visualization modes are used to run optimized post-lighting passes later. These can be useful to optimize your Substrate materials by reducing the number of slabs used and enabled features, and to [use parameter blending on Operators](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.5).  If a material is made of several materials mixed and layered together, but only a single Slab is visible (due to dynamic masking or low transmittance value) for a given pixel, the non-visible Slabs are not shown (or optimized out) of the visualization. |

## Limitations and Known Issues

* Substrates is a Beta feature, so we recommend not using it for any production work.
* Platform support and testing is currently incomplete. As it moves into Production-ready states, more testing coverage will happen.
* Features and UX are subject to change such that existing assets may behave differently or be invalidated altogether.
* Has Beta support for Path Tracer.
* Some platforms and rendering paths, such as DirectX 11 (DX11) and Mac, exhibit issues and may not work entirely.
* When using Adaptive GBuffer:

  + Cook time (shader compilation time) will increase compared to using Blendable GBuffer, even for simple materials. This is because Adaptive GBuffer requires more processing and has more complex encoding/decoding steps.
  + Runtime performance will regress compared to Blendable GBuffer regression, for the exact same project. This is primarily because of encoding/decoding steps and more complex runtime evaluation.

## Additional Resources

* [The Future of Materials in Unreal Engine - GDC 2023](https://www.youtube.com/watch?v=joOIBteSo1w)
* [The State of Unreal Livestream](https://www.youtube.com/watch?v=teTroOAGZjM&t=8982s) — Timestamp: 02:29:42
* The [Content Examples](https://www.fab.com/listings/4d251261-d98c-48e2-baee-8f4e47c67091) sample project includes a Level named "SubstrateMaterials" where you can explore different examples and demonstrations of how Substrate Materials function.

  Using Substrate with the Content Examples project requires you to enable Substrate for the project. Only this map has been validated for use with Substrate enabled. If you are using only a single instance of the Content Examples project, we recommend only enabling Substrate for this level and disabling it anytime you're using the rest of the project.

* [materials](https://dev.epicgames.com/community/search?query=materials)
* [beta](https://dev.epicgames.com/community/search?query=beta)
* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [shaders](https://dev.epicgames.com/community/search?query=shaders)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [New Projects](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#enabling-substrate)
* [Material Editor Conversion](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#materialeditorconversion)
* [GBuffer Format for Visual Fidelity](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#gbufferformatforvisualfidelity)
* [Blendable GBuffer](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#blendablegbuffer)
* [Adaptive GBuffer](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#adaptivegbuffer)
* [DBuffer](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#dbuffer)
* [Optional Project Settings and Console Variables](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#optionalprojectsettingsandconsolevariables)
* [Substrate's Relationship to Material Layers](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#substrate-s-relationship-to-material-layers)
* [Working with Substrate Materials](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#working-with-substrate-materials)
* [Substrate Material Root Node](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#substrate-material-root-node)
* [Substrate Blend Modes](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#substrate-blend-modes)
* [Substrate Slab](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#substrate-slab)
* [Substrate Material Parameterization](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#substratematerialparameterization)
* [Material Simplification](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#materialsimplification)
* [Substrate Material Nodes](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#substrate-material-nodes)
* [Substrate BSDF Nodes](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#substrate-bsdf-nodes)
* [Substrate Operator Nodes](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#substrate-operator-nodes)
* [Substrate Coverage Weight](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#substrate-coverage-weight)
* [Substrate Horizontal Layer](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#substrate-horizontal-layer)
* [Substrate Vertical Layer](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#substrate-vertical-layer)
* [Substrate Add](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#substrate-add)
* [Substrate Building Block Nodes](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#substrate-building-block-nodes)
* [Substrate Extras Nodes](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#substrate-extras-nodes)
* [Substrate Helper Nodes](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#substrate-helper-nodes)
* [Additional Notes about Substrate Nodes](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#additional-notes-about-substrate-nodes)
* [Substrate Stats Panel](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#substrate-stats-panel)
* [Parameter Blending with Operators](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#parameter-blending-with-operators)
* [Metalness and Specular Response](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#metalness-and-specular-response)
* [Rough Refraction](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#rough-refraction)
* [Translucent Rough Refraction](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#translucent-rough-refraction)
* [Opaque Rough Refraction](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#opaque-rough-refraction)
* [Substrate Layer Thickness](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#substratelayerthickness)
* [Substrate Material Instance Override](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#substratematerialinstanceoverride)
* [Subsurface Scattering and Participating Media](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#subsurface-scattering-and-participating-media)
* [Coverage versus Transmittance](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#coverageversustransmittance)
* [Translucency and Blend Modes](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#translucency-and-blend-modes)
* [Additional Notes about Substrate Translucency](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#additional-notes-about-substrate-translucency)
* [Substrate Performance](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#substrateperformance)
* [Substrate Debug View Modes](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#substrate-debug-view-modes)
* [Limitations and Known Issues](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#limitations-and-known-issues)
* [Additional Resources](/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine?application_version=5.7#additional-resources)
