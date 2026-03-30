<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.7 -->

# Nanite Virtualized Geometry Overview

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
7. [Nanite Virtualized Geometry](/documentation/en-us/unreal-engine/nanite-in-unreal-engine "Nanite Virtualized Geometry")
8. Nanite Virtualized Geometry Overview

# Nanite Virtualized Geometry Overview

Learn about Nanite's virtualized geometry system and how it achieves pixel scale detail and high object counts.

![Nanite Virtualized Geometry Overview](https://dev.epicgames.com/community/api/documentation/image/a0600593-927d-403f-a1a7-2241915e69ed?resizing_type=fill&width=1920&height=335)

 On this page

Nanite is Unreal Engine's virtualized geometry system which uses an internal mesh format and rendering technology to render pixel scale detail and high object counts. It intelligently does work on only the detail that is visible on-screen and no more. Nanite's data format is also highly compressed and supports fine-grained streaming with automatic level of detail.

[![Example Scenes with Nanite](https://dev.epicgames.com/community/api/documentation/image/b5150c40-c160-4e9b-a9e8-ed00c3e000f2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b5150c40-c160-4e9b-a9e8-ed00c3e000f2?resizing_type=fit)

## Benefits of Nanite

* Multiple orders of magnitude increase in geometry complexity, higher triangle and objects counts than has been possible before in real-time
* Frame budgets are no longer constrained by polycounts, draw calls, and mesh memory usage
* Now possible to directly import film-quality source arts, such as ZBrush sculpts and photogrammetry scans
* Use high-poly detailing rather than baking detail into normal map textures
* Level of Detail (LOD) is automatically handled and no longer requires manual setup for individual mesh's LODs
* Loss of quality is rare or non-existent, especially with LOD transitions

Although the advantages can be game-changing, practical limits still remain. For example, instance counts, triangles per mesh, material complexity, output resolution, and performance should be carefully measured for any combination of content and hardware. As Nanite continues to mature, we will expand its capabilities and improve performance.

## Differences Between a Nanite Mesh and Static Mesh

Nanite meshes are just Static Meshes that have Nanite enabled on them, but there are some key differences you should be aware of:

* **Nanite meshes are triangle meshes.**

  + A mesh that has Nanite enabled is essentially still a triangle mesh at its core, only with a lot of level of detail and compression applied to its data. Nanite uses a system for rendering that data format in an extremely efficient way when compared to traditional rendering of mesh data.
* **Requires a flag to be set on the mesh itself.**

  + Authoring content for Nanite is no different than traditional meshes, except that Nanite can handle orders of magnitude more triangles and instances than is possible for traditionally rendered geometry — move the camera close enough and Nanite will draw the original source triangles that were imported.
* **Supports multiple UVs and vertex colors.**

  + Materials are assigned to sections of the mesh such that those materials can use different shading models and dynamic effects, which can be done in the shaders. Material assignments can be swapped dynamically, just like any other mesh geometry, and Nanite doesn’t require any process to bake down materials.
  + [Virtual textures](https://dev.epicgames.com/documentation/en-us/unreal-engine/virtual-texturing-in-unreal-engine) are not required for use with Nanite, but they are highly recommended. Virtual textures are an orthogonal Unreal Engine feature with similar goals for texture data that Nanite achieves with mesh data.

Working with Nanite should be familiar to workflows for Static Meshes, but there are many things not yet supported. See the [Supported Features](https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.5) section of this page for more details.

## How does Nanite work?

Nanite integrates as seamlessly as possible into existing engine workflows while using a novel approach to storing and rendering mesh data.

* During import, meshes are analyzed and broken down into hierarchical clusters of triangle groups.
* During rendering, clusters are swapped on the fly at varying levels of detail based on the camera view and connect perfectly without cracks to neighboring clusters within the same object. Data is streamed in on demand so that only visible detail needs to reside in memory. Nanite runs in its own rendering pass that completely bypasses traditional draw calls. You can use various Nanite visualization modes to inspect the Nanite pipeline.

Since Nanite relies on the ability to rapidly stream mesh data from disk on demand, we recommend solid state drives (SSDs) for runtime storage.

## What Types of Meshes Should Nanite Be Used For?

Nanite should generally be enabled wherever possible on platforms that support it. Any mesh that has it enabled will typically render faster, and take up less memory and disk space.

More specifically, a mesh is an especially good candidate for Nanite if it:

* Contains many triangles, or has triangles that will be very small on screen
* Has many instances in the scene
* Acts as a major occluder of other Nanite geometry
* Casts shadows using [Virtual Shadow Maps](https://dev.epicgames.com/documentation/en-us/unreal-engine/virtual-shadow-maps-in-unreal-engine?application_version=5.5)

An example of an exception to these rules is something like a sky sphere; its triangles will be large on screen, it doesn't occlude anything, and there is only one in the scene. Typically, these exceptions are rare and performance loss for using Nanite with them is fairly minimal so don't be overly concerned about where Nanite shouldn't be enabled if Nanite supports the use case.

Some use cases are not supported by Nanite currently. See the [Supported Features](https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.5) section of this page for more details.

## Enabling Nanite Support on Meshes

Nanite can be enabled on supported geometry in the following ways:

* [On import](https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.5)
* [Using individual mesh editors](https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.5)
* [Batched selection in the Content Browser](https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.5)

Converting geometry to Nanite requires some processing time for each mesh. On large projects, use of a shared Derived Data Cache (DDC) is especially helpful if there are many Nanite Assets.   
  
For more information, see [Shared DDC](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-derived-data-cache-in-unreal-engine) .

### Importing a Mesh

When importing a mesh intended for us with Nanite, check the box for **Build Nanite**.

[![Nanite FBX Import Options](https://dev.epicgames.com/community/api/documentation/image/08c74ab4-6130-4e01-9331-3c70f7955837?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/08c74ab4-6130-4e01-9331-3c70f7955837?resizing_type=fit)

When not using precomputed (built) lighting with [Lightmass for global illumination](https://dev.epicgames.com/documentation/en-us/unreal-engine/global-illumination-in-unreal-engine), we recommend disabling Generate Lightmap UVs. When Build Nanite is enabled, highly detailed geometry adds significant time to importing and building static mesh data. This property also adds an additional UV channel, which includes a significant amount of data for very dense meshes. If your project doesn't require baked lighting, there's no need to incur either cost.

### Enabling Nanite on Assets

In cases where you already have your project populated with assets that you want to enable to use Nanite, there are two options:

* Batch-enabled through the Content Browser.
* Enabled per-mesh.

#### Enable Nanite on Meshes in Batches

For batches of Static or Skeletal Mesh Assets that you want to enable Nanite for, use the **Content Browser** to select them all. **Right-click** and choose **Nanite > Enable** from the context menu.

[![Enable Nanite on Batches of Asset in the Content Browser](https://dev.epicgames.com/community/api/documentation/image/783c5083-d94f-4e4e-a7ed-09d83fa34992?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/783c5083-d94f-4e4e-a7ed-09d83fa34992?resizing_type=fit)

#### Enable Nanite on Individual Meshes

For any mesh that supports Nanite (such as a static mesh, skeletal mesh, or geometry collection), open its asset editor and enable Nanite through its Details panel.

In the Static Mesh Editor, locate the **Nanite Settings** and check the box for **Enable Nanite Support**.

[![Enable Nanite in the Static Mesh Editor](https://dev.epicgames.com/community/api/documentation/image/6757488b-f72e-4e57-a297-63fb53b16534?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6757488b-f72e-4e57-a297-63fb53b16534?resizing_type=fit)

In the Skeletal Mesh Editor, locate the **Nanite Settings** and check the box for **Enable Nanite Support**.

[![](https://dev.epicgames.com/community/api/documentation/image/0b81a91d-81d4-420b-beeb-b9fd5305a175?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0b81a91d-81d4-420b-beeb-b9fd5305a175?resizing_type=fit)

In the Geometry Collections Editor, locate the **Nanite** section and check the box for **Enable Nanite**.

[![Enable Nanite on Geometry Caches](https://dev.epicgames.com/community/api/documentation/image/ab9e01ef-4528-4c8b-b99e-ade63caa8ae6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ab9e01ef-4528-4c8b-b99e-ade63caa8ae6?resizing_type=fit)

## Features of Nanite

These are some features of Nanite that you can use

### Nanite Static Mesh

[![](https://dev.epicgames.com/community/api/documentation/image/5bdab34d-60d0-443d-bc81-81270b1ba8cd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5bdab34d-60d0-443d-bc81-81270b1ba8cd?resizing_type=fit)

 Nanite for static meshes uses no LODs, scaling dynamically the number of polygons they use based on the resolution of the screen being used. Nanite static meshes fully support Lumen global illumination and reflections, and virtual shadow maps to have highly detailed scenes with lots of instances.

For more information, see [Working with Nanite-Enabled Content](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-naniteenabled-content).

### Nanite Skeletal Mesh

[![](https://dev.epicgames.com/community/api/documentation/image/49d4aab9-13b1-4fb4-b03e-295259ff03bf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/49d4aab9-13b1-4fb4-b03e-295259ff03bf?resizing_type=fit)

Nanite Skeletal Meshes include support for:

* A Skeletal Mesh API making it simpler to achieve rendering them.
* One draw call for an entire mesh.
* Shadowing from Virtual Shadow Maps.
* No geometry LODs. Nanite Skeletal Mesh uses animation LODs.
* Instancing with animation banks.

For more information, see [Working with Nanite-Enabled Content](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-naniteenabled-content).

### Nanite with Landscapes

[![](https://dev.epicgames.com/community/api/documentation/image/a49b8f91-c0a9-459e-9522-6d893b712f97?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a49b8f91-c0a9-459e-9522-6d893b712f97?resizing_type=fit)

Nanite can be enabled for landscape terrain to improve performance with Nanite rendering, especially when used in conjunction with [Virtual Shadows](https://dev.epicgames.com/documentation/en-us/unreal-engine/virtual-shadow-maps-in-unreal-engine?application_version=5.5).

For more information, see [Using Nanite with Landscapes](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-nanite-with-landscapes-in-unreal-engine).

### Nanite Foliage

Technical demonstration of a large forest rendered with Nanite in The Witcher 4 Unreal Engine technical demo.

Nanite Foliage is a set of integral systems using Nanite's virtualized geometry rendering to achieve dense, highly detailed foliage at scale by making use of old and new techniques to render these types of large open vistas at higher quality and at a fraction of the original frame cost. It uses a combination of instancing, skinned meshes, voxelization, animation, and material characteristics to achieve lifelike animated foliage.

For more information, see [Nanite Foliage](https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-foliage).

### Nanite Splines

Spline meshes are used for deforming meshes along the shape of a spline, such as roads and paths over a landscape terrain. Nanite-enabled meshes support splines by default and can be created as [Landscape Splines](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-splines-in-unreal-engine) and [Blueprint Splines](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprint-splines-in-unreal-engine).

[![Nanite Spline Example](https://dev.epicgames.com/community/api/documentation/image/d66ef909-ca78-426a-bce6-77fc3e3c1299?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d66ef909-ca78-426a-bce6-77fc3e3c1299?resizing_type=fit)

Example scene with Nanite mesh in foreground and Nanite Spline. This scene shows the Lit and Nanite Triangles visualization.

  For more information, see [Working with Nanite-Enabled Content](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-naniteenabled-content).

### Nanite Static Displacement Mapping

The Static Mesh Editor includes an option to add detail to Nanite-enabled meshes through an offline adaptive tessellator. The tessellator generates an optimized Nanite mesh using displacement maps baked into it. This texture-driven approach is non-destructive and allows you to control the amount of tessellation and displacement through scalar parameters.

[![Examples with and without Nanite Static Displacement mapping](https://dev.epicgames.com/community/api/documentation/image/d05d960d-c811-4c69-a80e-916ef763c915?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d05d960d-c811-4c69-a80e-916ef763c915?resizing_type=fit)

  For more information, see [Working with Nanite-Enabled Content](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-naniteenabled-content).

### Nanite Tessellation

|  |  |
| --- | --- |
| [With Nanite Tessellation](https://dev.epicgames.com/community/api/documentation/image/4f5db2a5-b8b6-4bcf-b632-9723dff613b2?resizing_type=fit) | [Without Nanite Tessellation](https://dev.epicgames.com/community/api/documentation/image/df1aebea-ad78-40c5-ba2f-9354910e6e9d?resizing_type=fit) |
| With Nanite Tessellation | Without Nanite Tessellation |

Nanite tessellation is dynamic programmable displacement that allows for Nanite meshes to be modified at runtime using a displacement map or procedural material.

The benefits of Nanite tessellation include:

* Using source meshes that include less detail in the authoring pipeline.
* Material-driven and animated displacement.
* Creating detailed Nanite landscapes.

  For more information, see [Working with Nanite-Enabled Content](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-naniteenabled-content).

## Supported Features of Nanite

This section describes how best to work with Nanite in an Unreal Engine project with details on what is and is not supported and possible limitations.

### Geometry

Nanite can be enabled on Static Meshes and [Geometry Collections](https://dev.epicgames.com/documentation/en-us/unreal-engine/geometry-collections-user-guide).

A Nanite-enabled mesh can be used with the following Component types:

* Static mesh
* Skeletal mesh
* Instanced static mesh
* Spline mesh
* Hierarchical instanced static mesh
* Geometry collection
* Foliage painter
* Landscape grass

Some additional notes about geometry with Nanite:

* Maximum number of Nanite instances in a scene

  + The maximum number of instances that can be present in the scene is hard-locked to 16 million instances, which includes all instances that are streamed in, not just those enabled for use with Nanite. Only instances streamed in are counted towards this total.
* Per-Vertex Tangents

  + Per-vertex tangents are not stored from the static mesh when it is enabled for Nanite. Instead, tangent space is implicitly derived in the pixel shader. Tangent data is not stored in order to reduce data size. This difference in tangent space using this approach could cause discontinuities at edges. However, this particular issue has not shown to be significant, and there are plans to support vertex tangents in a future release.

#### Mesh Deformation

Nanite has limited support for the deformation of rigid meshes. Nanite supports dynamic translation, rotation, and non-uniform scaling of these meshes, whether it is dynamic or static. This means moving any position of a Nanite-enabled mesh in a way that is more complex than can be expressed in a single 4x3 matrix multiply, uniformly applied to the entire mesh.

While deformation with **World Position Offset** (WPO) in a material is supported, it is limited.

* Nanite meshes using WPO displacement are split into smaller clusters whereby each of those clusters have their own individual bounds and are culled individually on the GPU. You must clamp the amount of displacement in order to manage how many clusters of the Nanite mesh are culled.
* Foliage using WPO is less problematic because the foliage is filled with holes and cannot really occlude itself.

Deformation with **Morph Targets** is not supported with Nanite.

### Materials

Nanite supports materials that have their **Blend Mode** set to **Opaque** and **Masked**. When an unsupported material type is detected, a default material is assigned to the mesh along with a warning showing up in the Output Log with additional contextual information.

Additional material features notes:

* Nanite-enabled meshes can receive decals projected onto their surfaces but do not support [Mesh Decals](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-mesh-decals-in-unreal-engine), which require materials to use a **Translucent** Blend Mode.
* **Wireframe** checkbox is not supported.
* The **Vertex Interpolator** node and **Custom UVs** are supported but will be evaluated three times per pixel.
* **Custom** expression nodes, or any nodes that use them (such as the `ParallaxOcclusionMapping` material function) might result in artifacts with Nanite. This is expected since Nanite doesn't yet have analytic derivative support yet.

### Rendering

The following rendering features are not currently supported:

* View-specific filtering of objects using:

  + Minimum Screen Radius
  + Distance culling
* Forward Rendering
* Stereo rendering for Virtual Reality
* Split Screen
* Multisampling Anti-Aliasing (MSAA)
* Lighting Channels
* Ray-tracing against Nanite meshes

  + The Fallback Mesh is used for Nanite-enabled meshes by default. Lower the **Fallback Relative Error** parameter in the Static Mesh Editor to use more of the source mesh's triangles.
  + (Experimental) Initial support for native ray-tracing of Nanite meshes is enabled with the console variable `r.RayTracing.Nanite.Mode 1`. This preserves all detail while using significantly less GPU memory than zero-error Fallback Meshes.
* Some visualization view modes do not yet support displaying Nanite meshes

  Use caution with some visualization modes in the Static Mesh editor when viewing highly detailed geometry. Viewing normals and UVs can cause problems with editor performance as it tries to display all this data on screen at once.

### Supported Platforms

Nanite supports current console and desktop platforms with graphics cards using the latest drivers with DirectX 12 with Shader Model 6 (SM6).

For additional information about hardware and software specifications recommended by Epic Games, see [Hardware and Software Specifications](https://dev.epicgames.com/documentation/en-us/unreal-engine/hardware-and-software-requirements-for-container-deployments-in-unreal-engine).

## Nanite Project Settings

Settings for Nanite can be found in the **Project Settings** under the **Engine > Rendering** category under the Nanite section.

[![](https://dev.epicgames.com/community/api/documentation/image/5a48282c-c7e5-4235-9ad0-70b17d8ff70f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5a48282c-c7e5-4235-9ad0-70b17d8ff70f?resizing_type=fit)

Asset editors that support Nanite, such as the static and skeletal meshes will have their own Nanite settings to configure in their Details panels.

For more information on these settings, see [Nanite Technical Details](https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-technical-details).

* [performance](https://dev.epicgames.com/community/search?query=performance)
* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [optimization](https://dev.epicgames.com/community/search?query=optimization)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Benefits of Nanite](/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.7#benefits-of-nanite)
* [Differences Between a Nanite Mesh and Static Mesh](/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.7#differences-between-a-nanite-mesh-and-static-mesh)
* [How does Nanite work?](/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.7#how-does-nanite-work)
* [What Types of Meshes Should Nanite Be Used For?](/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.7#what-types-of-meshes-should-nanite-be-used-for)
* [Enabling Nanite Support on Meshes](/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.7#enabling-nanite-support-on-meshes)
* [Importing a Mesh](/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.7#importing-a-mesh)
* [Enabling Nanite on Assets](/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.7#enabling-nanite-on-assets)
* [Enable Nanite on Meshes in Batches](/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.7#enable-nanite-on-meshes-in-batches)
* [Enable Nanite on Individual Meshes](/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.7#enable-nanite-on-individual-meshes)
* [Features of Nanite](/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.7#featuresofnanite)
* [Nanite Static Mesh](/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.7#nanitestaticmesh)
* [Nanite Skeletal Mesh](/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.7#naniteskeletalmesh)
* [Nanite with Landscapes](/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.7#nanitewithlandscapes)
* [Nanite Foliage](/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.7#nanitefoliage)
* [Nanite Splines](/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.7#nanitesplines)
* [Nanite Static Displacement Mapping](/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.7#nanitestaticdisplacementmapping)
* [Nanite Tessellation](/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.7#nanitetessellation)
* [Supported Features of Nanite](/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.7#supported-features-of-nanite)
* [Geometry](/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.7#geometry)
* [Mesh Deformation](/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.7#meshdeformation)
* [Materials](/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.7#materials)
* [Rendering](/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.7#rendering)
* [Supported Platforms](/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.7#supported-platforms)
* [Nanite Project Settings](/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.7#naniteprojectsettings)
