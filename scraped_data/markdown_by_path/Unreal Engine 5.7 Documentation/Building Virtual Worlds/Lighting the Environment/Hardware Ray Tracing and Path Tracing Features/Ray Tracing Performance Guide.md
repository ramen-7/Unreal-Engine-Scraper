<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/ray-tracing-performance-guide-in-unreal-engine?application_version=5.7 -->

# Ray Tracing Performance Guide

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
8. Ray Tracing Performance Guide

# Ray Tracing Performance Guide

A selection of topics for improving performance of ray tracing features in your projects.

![Ray Tracing Performance Guide](https://dev.epicgames.com/community/api/documentation/image/b1d26aeb-c0a9-4a20-a192-1eb7c9511cd3?resizing_type=fill&width=1920&height=335)

 On this page

For projects that need to maintain a real-time performance budget, it's important to set a frame budget in order to achieve that target frame rate. Typically, that would be 30 or 60 frames per second (FPS). There are many opportunities for optimizing and improving performance of your projects by making adjustments to content or workflows.

This guide covers some starting points for optimizing Ray Tracing features of Unreal Engine and ways you can pin-point trouble areas through debugging the scene and investigating those issues.

## Overview of Ray Tracing Costs

Hardware Ray Tracing uses a two-level **Bounding Volume Hierarchy** (BVH) to accelerate ray traversal. The **Top Level Acceleration Structure** (TLAS) contains all mesh instances for the whole scene. The meshes referenced by those instances are **Bottom Level Acceleration Structures** (BLAS).

The diagram below gives a visual representation of how the BVH works for ray traversal.

[![diagram of ray tracing acceleration structure](https://dev.epicgames.com/community/api/documentation/image/f352f1e6-4b42-415c-8af0-2c338d808163?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f352f1e6-4b42-415c-8af0-2c338d808163?resizing_type=fit)

There are three main categories of costs associated with Ray Tracing:

1. Building the Bottom Level Acceleration Structures for dynamically deforming meshes, like skinned meshes and hair.
2. Building the Top Level Acceleration Structure for the scene and the Shader Binding Table (SBT).
3. Ray traversal for each feature that uses Ray Tracing.

For development of your project, you can test the ray tracing cost of specific types of geometry with console variables. This is useful for measuring their costs or disabling them entirely for Ray Tracing features. You'll find them listed under `r.RayTracing.Geometry.*`.

| Geometry Type | Console Variable | Default State |
| --- | --- | --- |
| Static Meshes | `r.RayTracing.Geometry.StaticMeshes` | Enabled |
| Skeletal Meshes | `r.RayTracing.Geometry.SkeletalMeshes` | Enabled |
| Instanced Static Meshes | `r.RayTracing.Geometry.InstancedStaticMeshes` | Enabled |
| Landscape Terrain | `r.RayTracing.Geometry.Landscape` | Enabled |
| Geometry Cache | `r.RayTracing.Geometry.GeometryCache` | Enabled |
| Geometry Collection | `r.RayTracing.Geometry.GeometryCollection` | Disabled |
| Niagara Meshes | `r.RayTracing.Geometry.NiagaraMeshes` | Enabled |
| Niagara Ribbons | `r.RayTracing.Geometry.NiagaraRibbons` | Enabled |
| Niagara Sprites | `r.RayTracing.Geometry.NiagaraSprites` | Enabled |
| Procedural Meshes | `r.RayTracing.Geometry.ProceduralMeshes` | Enabled |

## Bottom Level Acceleration Structure Updates

While the BLAS for Static Meshes are only built once at load (or during the cook on consoles), dynamically deforming meshes have to rebuild every frame and this can incur significant cost. The BLAS rebuilds are a GPU operation, and are typically proportional to the total number of triangles being deformed. **Using a large number of Skeletal Meshes with a large number of triangles can quickly become a major GPU cost.**

BLAS rebuild costs can be observed in the GPU Profiler under the following areas:

* Scene > CommitRayTracingGeometryUpdates
* Scene > CommitHairRayTracingGeometryUpdates
* Scene > RayTracingGeometry

Geometry types which rebuild every frame include:

* Skinned meshes through GPUSkinCache
* Landscape is rebuilt to support its continuously morphing level of detail (LOD)
* Geometry Collections for Chaos Destruction
* Hair
* Procedural Mesh
* Niagara Particle Systems

High polygon Skeletal Meshes are the most common cause of high BLAS build costs. Skeletal Meshes can use the property **Ray Tracing Min LOD** found in the [Skeletal Mesh Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-animation-system-in-unreal-engine), which prevents the highest LODs from being used for Ray Tracing features.

Use the console command `D3D12.DumpRayTracingGeometries` when running a project with D3D12 to get a list of all the memory allocations for dynamic BLAS rebuilds dumped to the log. This list can be used to optimize your project.

### World Position Offset on Static Mesh Components

World Position Offset (WPO) is challenging to support efficiently with Ray Tracing features because it requires dynamically rebuilding the BLAS, as well as unique memory for each instance.

By default, Unreal Engine ignores WPO when building Ray Tracing Scene, which can cause self-intersections artifacts. Static Mesh Components can opt-in to using WPO with ray tracing with the **Evaluate World Position Offset** setting. However, it only works for a short distance around the camera, 50 meters unless otherwise specified.

Use the following to enable and adjust the supported WPO distance from the camera:

* `r.RayTracing.Geometry.StaticMeshes.WPO 1`
* `r.RayTracing.Geometry.StaticMeshes.WPO.CullingRadius 5000.0f`

The dynamic BLAS builds caused by WPO show up in the GPU profiler under `Scene > RayTracingGeometry > RayTracingDynamicGeometryUpdate`.

Instanced components, like Instanced Static Mesh Component, do not support WPO by default because of its extreme cost. Components that have a **Evaluate World Position Offset** toggle do not enable it by default. Toggling it on can significantly increase memory pressure and slow render times because it effectively converts every instance in a single mesh with a separate BLAS.

### Managing Ray Tracing Build Cost

As mentioned in previous sections of this page, multiple types of meshes will use dynamic geometry build path, which can negatively affect performance.

As mentioned above multiple types of meshes will go via dynamic geometry build path which can negatively affect performance. You can restrict how many triangles are dynamically updated per frame by specifying a desired limit with `r.RayTracing.DynamicGeometry.MaxUpdatePrimitivesPerFrame`. Depending on the target platform performance a good starting point is setting a 10k-30k limit.

By default all dynamic ray tracing geometries will be updated in a round-robin fashion. This might not be desired. For example, more priority should be given to meshes closer to the camera and can be changed by using `r.RayTracing.DynamicGeometry.PriorityBasedUpdate`. In this mode which geometry is updated depends on the mesh distance to the camera and how many frames passed since the last update.

The number of frames since last update and how it affects priority calculations can be controlled with `r.RayTracing.DynamicGeometry.PriorityBasedUpdate.MaxFramesSinceLastUpdate` and `r.RayTracing.DynamicGeometry.PriorityBasedUpdate.LastUpdateWeight`, respectively.

Additionally, depending on the type of update, the quality of updated BLAS can be much lower than that of a rebuilt BLAS. This usually happens in situations when the animation results in a mesh that significantly differs from the original position for which the initial BLAS was built. A good example of this would be a mesh moving far away from its original position because of WPO. In such a situation it makes sense to periodically rebuild, as opposed to update, the BLAS. This can be achieved by setting a non-zero limit for `r.RayTracing.DynamicGeometry.ForceBuild.MaxPrimitivesPerFrame`.

Another option to limit the cost of dynamic ray tracing geometry build is to get feedback from rays, which can be enabled with `r.RayTracing.Scene.UseTracingFeedback`. Lumen and MegaLights passes can mark which ray tracing instances are hit and use that information to only build dynamic ray tracing geometries that were hit by those rays. This allows only geometries that are actually used to be updated at small tracing performance cost. You can check how many triangles were skipped because of the feedback when looking at **Ray tracing dynamic skipped primitives** counter in `stat SceneRendering`. You can see an example of this below:

[![](https://dev.epicgames.com/community/api/documentation/image/8b681a6f-4a6c-40ed-a9dc-e24c79fb8c01?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8b681a6f-4a6c-40ed-a9dc-e24c79fb8c01?resizing_type=fit)

### Managing Ray Tracing Memory Cost

#### Reference Based Residency

Ray tracing can significantly increase memory requirements. For each loaded mesh, a ray tracing bottom-level acceleration structure (BLAS) needs to be allocated, which can consume a significant amount of memory. Generally, the memory requirement for a BLAS scales linearly with the number of triangles / vertices, but the exact size is platform-dependent. To overcome this problem, you can use the Reference Based Residency system so that only BLAS that are directly referenced by TLAS are kept in memory. This also allows specifying the memory budget for the remaining BLAS. When over-budget, the system will evict BLAS not currently referenced by the TLAS.

You can enable the Reference Based Residency system by using the console command `r.RayTracing.UseReferenceBasedResidency` (enabled by default). You can also control the size of the ray tracing geometry pool with `r.RayTracing.ResidentGeometryMemoryPoolSizeInMB`, this can be adjusted per platform.

Keep in mind that this is a soft limit and meshes without LODs will not get evicted and will be permanently resident. To guarantee there is proper LOD setup for ray tracing geometry you can enable **Rendering > Generate Ray Tracing Proxies**.

This ensures there is a LOD setup for ray tracing that works well with Reference Based Residency. At the moment it means 2 LODs will be created and LOD1 will always be resident.

#### Generate Nanite Fallback Meshes

In cases when Nanite fallback meshes are only used for ray tracing, you can toggle off **Platforms > [Platform] > Generate Nanite Fallback Meshes**. Disabling it will strip Nanite fallback meshes from the build, usually saving a lot of memory in the process. Ray tracing uses Ray Tracing Proxies instead and stream them in and out on demand (alongside index and vertex buffers, if needed).

For individual cases when fallback meshes are needed (like with Niagara), this can be enabled on a case-by-case basis. You can toggle settings like **Allow CPUAccess**, which results in fallback meshes getting created.

#### Ray Tracing Mode

On platforms that support both inline ray tracing and ray tracing shaders, you can use the per-platform option for fine-grained control over how ray tracing is enabled. You can find this in the Project Settings under **Platforms > [Platform] > Ray Tracing Mode**.

It includes the following modes:

* **Disabled:** All ray tracing on this platform is disabled.
* **Inline:** Only inline ray tracing passes are enabled, such as Lumen Hardware Ray Tracing mode with Surface Cache and Barycentrics / Traversal debug view. In this mode, ray tracing material shaders and select global shaders are not compiled. This saves memory and CPU cost by not having to prepare binding for ray tracing shaders.
* **Full:** Every feature of ray tracing is supported on this platform.

## Top Level Acceleration Structure Build

The Top Level Acceleration Structure is rebuilt every frame, and has a cost on the Rendering Thread, RHI Thread, and the GPU. These costs are mostly proportional to how many mesh instances go into the acceleration structure.

Using the stat command `Stat SceneRendering`, you will find the number of instances being rebuilt every frame under **Ray tracing instances**.

[![ray tracing instances in stat scenerendering](https://dev.epicgames.com/community/api/documentation/image/8bb97fa7-e231-4c9a-91a8-ee79a19f0991?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8bb97fa7-e231-4c9a-91a8-ee79a19f0991?resizing_type=fit)

To measure the cost of the Rendering Thread, use the command `Stat SceneRendering` and look for the **GatherRayTracingWorldInstances**.

[![gather ray tracing world instances in stat scenerendering](https://dev.epicgames.com/community/api/documentation/image/a8cbeab3-0485-4764-8b19-c4088faafaa9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a8cbeab3-0485-4764-8b19-c4088faafaa9?resizing_type=fit)

To measure the cost of the RHI Thread, you can use per-RHI stats, such as `Stat D3D12RayTracing`.

[![measure cost of rhi thread in stat d3d12raytracing](https://dev.epicgames.com/community/api/documentation/image/83d05820-7dca-4490-a96f-e7d948f1ecbe?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/83d05820-7dca-4490-a96f-e7d948f1ecbe?resizing_type=fit)

GPU cost can be measured with the stat command `Stat GPU`. Look at entries for **RayTracingScene** and **RayTracing** to get an idea of their costs.

[![GPU cost measured with stat GPU](https://dev.epicgames.com/community/api/documentation/image/60e69320-0e4b-443c-8ed6-312c31308954?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/60e69320-0e4b-443c-8ed6-312c31308954?resizing_type=fit)

In order to achieve a 30 frames per second target on next generation consoles, scenes should generally have 100,000 instances or fewer in the Ray Tracing Scene after culling. On Windows, the number of instances can vary significantly.

### Culling

Scenes with ray tracing require objects outside of the camera view to be present in the scene, especially for highly reflective surfaces. This increases the cost of rendering the scene. Culling objects that aren't visible or needed helps with optimizing performance.

Since ray tracing needs to keep objects visible, even when they aren't in view, the console variable `r.RayTracing.Culling` provides some options to help optimize what is visible outside of the current view and over what distance.

The following options are provided:

* **1** culls objects behind the camera by distance and solid angle.
* **2** culls objects in front of and behind the camera by distance and solid angle.
* **3** culls objects in front and behind the camera by distance or solid angle (default ray tracing culling method).

Each culling option progressively culls more objects in the ray tracing scene.

Because the TLAS is rebuilt every frame, mesh instances can be culled based on their distance or angle to the camera when setting option 3.

Additionally, the **Radius** and **Angle** that the Ray Tracing Culling option uses can be configured on their on using the following console commands:

* `r.RayTracing.Culling.Radius`: Sets a distance around the camera beyond which objects are culled. Default radius is 10000 (100 meters).
* `r.Raytracing.Culling.Angle`: Culls meshes whose projected angle is smaller than 5 degrees. The default is 1.

For an open world project, such as City Sample, the culling **Radius** was increased to 15000 (150 meters), while the culling **Angle** was reduced to 0.5 (2.5 degrees) in account for large areas with lots of reflective surfaces that needed objects to be visible over farther distances.

Culling causes a lack of coverage in the Ray Tracing Scene and is best paired with the [Far Field](https://dev.epicgames.com/documentation/en-us/unreal-engine/lumen-technical-details-in-unreal-engine#far-field) to provide traces for distant geometry.

Mesh components tagged with a **Ray Tracing Group Id** greater than 0 can be culled as an aggregate using `r.RayTracing.Culling.UserGroupIds 1`. This method can be useful if your scene is built out of many disparate parts, but you'd like to cull them as a single object.

[![ray tracing details panel settings](https://dev.epicgames.com/community/api/documentation/image/34df7b1e-36ea-4911-985c-d1d28c814c9a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/34df7b1e-36ea-4911-985c-d1d28c814c9a?resizing_type=fit)

Ray Tracing Group Id property found on a selected Actor in a Level.

### Managing Top Level Acceleration Structure Build Cost

The cost of building TLAS typically scales linearly with the number of instances before culling (**Ray tracing total instances** in `stat SceneRendering`). If that number is much larger than **Ray tracing active instances**, it indicates that very few instances survive culling.

To avoid paying the full cost of those culled instances you can compact the active instance list (with `r.RayTracing.Scene.CompactInstances`). Then the minimum number of expected instances can be configured with `r.RayTracing.Scene.CompactInstances.Min` and since the number can change every frame you can also specify a margin with `r.RayTracing.Scene.CompactInstances.Margin`.

In practice those values should be derived from the actual game. Under the hood, on platforms that do not support indirect TLAS build, the engine reads back on the CPU the actual number of instances after culling from the GPU, which can take a couple of frames to do that. This means there might be moments when there are more instances than the system can handle. This will result in visible flickering during those frames until the system settles down. In those cases, either increase the margin or the minimum number of instances until the flickering goes away.

## Ray Traversal Cost

Ray queries are spawned by features which use [Hardware Ray Tracing](https://dev.epicgames.com/documentation/en-us/unreal-engine/hardware-ray-tracing-in-unreal-engine), such as Ray Tracing Shadows, Lumen Global Illumination, and Lumen Reflections. GPUs solve these Ray queries with dedicated hardware that traverses the acceleration structures to find a hit.

An example of ray traversal costs in the Profile GPU log output would be:

2.36ms LumenReflections 1 draw 1 prims 0 verts 13 dispatches
4.1% 0.67ms ReflectionHardwareRayTracing [default] <indirect> 1 draw 1 prims 0 verts 1 dispatch 1 groups

The cost of ray traversal is proportional to the number of Ray queries issued by the lighting feature, and the amount of mesh overlap in the scene.

When meshes overlap, the ray must traverse them all independently to find the closest hit, because Ray Tracing uses a two-level acceleration structure. The mesh overlap can cause extremely slow ray traversal in scenes built by piecing different assets together as needed (also called kitbashing).

[![overlapping meshes](https://dev.epicgames.com/community/api/documentation/image/ab6d682e-6e06-44f3-a567-35b99efbfa19?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ab6d682e-6e06-44f3-a567-35b99efbfa19?resizing_type=fit)

*Example of kitbashed assets used to layer rocks in the Unreal Engine 5 "Valley of the Ancients" technical demo.*

In order for scenes to be compatible with Hardware Ray Tracing, mesh overlap **must** be kept to a minimum.

There are other common causes of high ray traversal costs, the first being skyboxes — they overlap the entire scene and must be traversed by every ray, even if they are not hit. Another is grass — it has large bounds and high geometry complexity.

In these cases (or any others that are similar), you can choose to have those ray tracing tracing skip those meshes. Select the Actors in the world and use their Details panel to disable **Visible in Ray Tracing**.

### Ray Traversal Debug Visualization Modes

The following debug modes are currently only available on console platforms.

There are two debug modes that are useful for investigating high traversal costs: Performance and Traversal.

To enable these modes, you'll use the following commands:

C++

```
r.RayTracing.Visualize [mode]
```

r.RayTracing.Visualize [mode]

Copy full snippet(1 line long)

"[Mode]" is replaced by the visualization method you want to see. For example, it would be `r.RayTracing.Visualize Traversal Primary Node`to visualize the number of nodes intersected when tracing primary rays.

### Traversal Debug Visualization

The **Traversal** debug visualization shows a heatmap of only BVH traversal — how many iterations it takes to find a hit. For Lumen passes that don't use materials or similar passes that use simple hit shading/inline, the highest cost is usually the BVH traversal.

The colors of the heatmap goes from green (few iterations) to red (many iterations). Intuitively, the more iterations that happen, the slower the traversal. The values are in the range of 50-100 iterations for a typical scene. For a complicated scene, including multiple overlapping high polygon meshes, there are around 100-150 iterations.

Anything above that suggests there might be a problem, for example, it would not be uncommon for a broken mesh to see 1000+ iterations. The Traversal Triangle debug visualization is useful for checking individual meshes triangles.

For Traversal debugging, choose from the following mode:

| Traversal Debug mode | Command Name | Description | Visualization View |
| --- | --- | --- | --- |
| **Node Intersection Count** | `Traversal Primary Node`  or  `Traversal Secondary Node` | Used to investigate scene traversal costs. For example, when many instances are overlapping in TLAS.  These are BVH nodes in the internal, platform-specific representations of BLAS. |  |
| **Triangle Intersection Count** | `Traversal Primary Triangle`  or  `Traversal Secondary Triangle` | Shows the hits of nodes that contain only triangles (leaf nodes). |  |
| **Total Intersection Count** | `Traversal Primary All`  or  `Traversal Secondary All` | Sum of BVH node hits and triangle node hits. |  |

### Timing Debug Visualization

**Timing**debug visualization modes show a heatmap of the TraceRay call timing. For example, the "Timing Material" mode shows the combined time of BVH traversal and material evaluation time (executing Closest Hit/Miss shaders).

[![performance debug visualization](https://dev.epicgames.com/community/api/documentation/image/de66671a-5095-4182-ac65-4a143dfdcc2c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/de66671a-5095-4182-ac65-4a143dfdcc2c?resizing_type=fit)

*Ray Tracing Performance debug visualization.*

The colors of the visualization go from purple (no cost) to yellow (high cost). The heatmaps scale can be adjusted to fit your project's needs using `r.RayTracing.Visualize.TimingScale`.

This mode is most useful to find problematic objects and materials for Ray Tracing. If Ray Tracing cost is too high, it is a good idea to check if what's showing in that mode looks reasonable.

For example, the objects visible in the main view are also present in debug mode, no undesired objects are present and the material cost looks as expected for those objects. If there is nothing that stands out, it might be because the slow down is not caused by one single object but the combination of different smaller issues.

### Hit Shading Costs

When a ray hits a triangle, the material is evaluated and used for shading the hit point. For complex materials using procedural texturing and many virtual textures, this can be a very expensive process.

The **Ray Tracing Quality Switch** node is an expression that can be used in your Materials to provide a cheaper implementation for shading ray hits.

[![ray tracing quality switch material node](https://dev.epicgames.com/community/api/documentation/image/21461133-99ca-411b-8d30-e7fa1fc37768?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/21461133-99ca-411b-8d30-e7fa1fc37768?resizing_type=fit)

The node can replace entire parts of your Material logic to lower the overall cost of Ray Tracing features. Using this node affects all ray tracing effects for this material.

A simple example (see below) would be a material that includes logic that is costly for ray tracing effects. The RayTracingQualitySwitch node includes two inputs: Normal and RayTraced.

The **Normal** input contains all the logic needed for the material and is how it would appear on surfaces in the world. The **RayTraced** input should have less complexity in the logic path that increases the cost of ray tracing effects, like the Normal map.

[![simplified ray tracing quality switch material example](https://dev.epicgames.com/community/api/documentation/image/d9502d42-b220-4d40-94f3-a0164916466d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d9502d42-b220-4d40-94f3-a0164916466d?resizing_type=fit)

*Click image for full size.*

### Far Field

Ray Tracing supports a **Far Field** representation that extends Lumen Global Illumination and Reflections to one kilometer from the camera by default. The Far Field makes use of [Hierarchical Level of Detail (HLOD) meshes generated by World Partition](https://dev.epicgames.com/documentation/en-us/unreal-engine/world-partition---hierarchical-level-of-detail-in-unreal-engine) by default. The HLOD1 mesh is used for Far Field representation.

Currently, only Lumen lighting features make use of [Far Field](https://dev.epicgames.com/documentation/en-us/unreal-engine/ray-tracing-performance-guide-in-unreal-engine#far-field), and only when enabled for the project with the command `r.LumenScene.FarFields 1`.

In the Editor, the Far Field is visualized in each of the debug modes. This can be changed by entering the following command:

Console Output

```
r.RayTracing.Visualize.FarField 0
```

r.RayTracing.Visualize.FarField 0

Copy full snippet(1 line long)

In the visualization below, the far-field is the tinted red geometry using the HLOD1 meshes generated by World Partition. Anything closer to the camera is the high-detail geometry.

[![far field visualization](https://dev.epicgames.com/community/api/documentation/image/2f561884-2e35-4abf-9ddb-1077f72e7f1e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2f561884-2e35-4abf-9ddb-1077f72e7f1e?resizing_type=fit)

Lumen's Ray Tracing Far Field debug visualization. Far-field geometry is tinted red.

### Achieving 60 FPS with Ray Tracing

This is a list of console variables we suggest using to achieve 60 frames per second on the current generation consoles when using Lumen and Nanite:

| Suggestion | Console Variables to Set |
| --- | --- |
| **Disable all geometry types that do not currently contribute to the Lumen Scene** | Config  ``` |  |  | | --- | --- | |  | r.RayTracing.Geometry.InstancedStaticMeshes=0 | |  | r.RayTracing.Geometry.NiagaraRibbons=0 | |  | r.RayTracing.Geometry.NiagaraSprites=0 | |  | r.RayTracing.Geometry.NiagaraMeshes=0 | |  | r.RayTracing.Geometry.SplineMeshes=0 | |  | r.RayTracing.Geometry.Text=0 | |  | r.RayTracing.Geometry.Cable=0 | ``` r.RayTracing.Geometry.InstancedStaticMeshes=0 r.RayTracing.Geometry.NiagaraRibbons=0 r.RayTracing.Geometry.NiagaraSprites=0 r.RayTracing.Geometry.NiagaraMeshes=0 r.RayTracing.Geometry.SplineMeshes=0 r.RayTracing.Geometry.Text=0 r.RayTracing.Geometry.Cable=0 Copy full snippet(7 lines long) |
| **Set up WPO on Static Meshes** | Config  ``` |  |  | | --- | --- | |  | r.RayTracing.Geometry.StaticMeshes.WPO.Culling=1 | |  | r.RayTracing.Geometry.StaticMeshes.WPO.CullingRadius=<desired radius> | |  | r.RayTracing.Geometry.NaniteProxies.WPO=0 | ``` r.RayTracing.Geometry.StaticMeshes.WPO.Culling=1 r.RayTracing.Geometry.StaticMeshes.WPO.CullingRadius=<desired radius> r.RayTracing.Geometry.NaniteProxies.WPO=0 Copy full snippet(3 lines long) |
| **Reduce the landscape update frequency** | Config  ``` r.RayTracing.Geometry.Landscape.FractionalLODUpdateThreshold=0.3 ``` r.RayTracing.Geometry.Landscape.FractionalLODUpdateThreshold=0.3 Copy full snippet(1 line long) |
| **Set up budget for dynamic geometry** | Config  ``` |  |  | | --- | --- | |  | r.RayTracing.Geometry.SkeletalMeshes.LODBias=2 | |  | r.RayTracing.DynamicGeometry.MaxUpdatePrimitivesPerFrame=20000 | ``` r.RayTracing.Geometry.SkeletalMeshes.LODBias=2 r.RayTracing.DynamicGeometry.MaxUpdatePrimitivesPerFrame=20000 Copy full snippet(2 lines long) |

## Additional Ray Tracing Debug Visualization Modes

The **Ray Tracing Debug** visualization modes enable you to gather information about the ray tracing scene.

You can access these visualization modes from the Level Viewport using the **View Modes** dropdown selection, or by entering the console command `r.RayTracing.Visualize` followed by the name of the visualization mode (the list of available modes can be queued using `r.RayTracing.Visualize ?`).

[![Ray Tracing Debug Visualization Modes selected through the Level viewport.](https://dev.epicgames.com/community/api/documentation/image/d1c506b3-db1d-434e-abdb-5798010746c8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d1c506b3-db1d-434e-abdb-5798010746c8?resizing_type=fit)

### Picker Debug Visualization Mode

The `Picker` debug visualization mode displays information about the ray-tracing geometry and the instance under the cursor. The Picker mode can operate on two different domains: **Triangles** and **Instances**.

You can swap between these modes using the console command `r.RayTracing.Debug.PickerDomain` followed by **0**\* for Triangles (default) or **1** for Instances.

|  |  |
| --- | --- |
|  |  |
| Triangles Debug Picker Domain | Instance Debug Picker Domain |

On the left side of the viewport, information about the ray-tracing geometry is displayed along with which Picker Domain is currently being used.

[![Debug Picker information displayed in the level viewport.](https://dev.epicgames.com/community/api/documentation/image/a33a83b0-8964-482a-8cd6-0bbb8fbcb10c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a33a83b0-8964-482a-8cd6-0bbb8fbcb10c?resizing_type=fit)

### Dynamic Instances Debug Visualization Mode

The `Dynamic Instance` debug visualization mode shows dynamic instances within the ray-tracing scene. Every frame, dynamic instances are rebuilt and show as either **Red** for static instances or **Green** for dynamic instances.

[![Ray Tracing Debug Visualization Dynamic Instances](https://dev.epicgames.com/community/api/documentation/image/f0aad9de-ce25-41b4-b916-e26429adf47a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f0aad9de-ce25-41b4-b916-e26429adf47a?resizing_type=fit)

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [lighting](https://dev.epicgames.com/community/search?query=lighting)
* [optimization](https://dev.epicgames.com/community/search?query=optimization)
* [global illumination](https://dev.epicgames.com/community/search?query=global%20illumination)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Overview of Ray Tracing Costs](/documentation/en-us/unreal-engine/ray-tracing-performance-guide-in-unreal-engine?application_version=5.7#overview-of-ray-tracing-costs)
* [Bottom Level Acceleration Structure Updates](/documentation/en-us/unreal-engine/ray-tracing-performance-guide-in-unreal-engine?application_version=5.7#bottom-level-acceleration-structure-updates)
* [World Position Offset on Static Mesh Components](/documentation/en-us/unreal-engine/ray-tracing-performance-guide-in-unreal-engine?application_version=5.7#world-position-offset-on-static-mesh-components)
* [Managing Ray Tracing Build Cost](/documentation/en-us/unreal-engine/ray-tracing-performance-guide-in-unreal-engine?application_version=5.7#managingraytracingbuildcost)
* [Managing Ray Tracing Memory Cost](/documentation/en-us/unreal-engine/ray-tracing-performance-guide-in-unreal-engine?application_version=5.7#managing-ray-tracing-memory-cost)
* [Reference Based Residency](/documentation/en-us/unreal-engine/ray-tracing-performance-guide-in-unreal-engine?application_version=5.7#referencebasedresidency)
* [Generate Nanite Fallback Meshes](/documentation/en-us/unreal-engine/ray-tracing-performance-guide-in-unreal-engine?application_version=5.7#generatenanitefallbackmeshes)
* [Ray Tracing Mode](/documentation/en-us/unreal-engine/ray-tracing-performance-guide-in-unreal-engine?application_version=5.7#raytracingmode)
* [Top Level Acceleration Structure Build](/documentation/en-us/unreal-engine/ray-tracing-performance-guide-in-unreal-engine?application_version=5.7#top-level-acceleration-structure-build)
* [Culling](/documentation/en-us/unreal-engine/ray-tracing-performance-guide-in-unreal-engine?application_version=5.7#culling)
* [Managing Top Level Acceleration Structure Build Cost](/documentation/en-us/unreal-engine/ray-tracing-performance-guide-in-unreal-engine?application_version=5.7#managingtoplevelaccelerationstructurebuildcost)
* [Ray Traversal Cost](/documentation/en-us/unreal-engine/ray-tracing-performance-guide-in-unreal-engine?application_version=5.7#ray-traversal-cost)
* [Ray Traversal Debug Visualization Modes](/documentation/en-us/unreal-engine/ray-tracing-performance-guide-in-unreal-engine?application_version=5.7#ray-traversal-debug-visualization-modes)
* [Traversal Debug Visualization](/documentation/en-us/unreal-engine/ray-tracing-performance-guide-in-unreal-engine?application_version=5.7#traversaldebugvisualization)
* [Timing Debug Visualization](/documentation/en-us/unreal-engine/ray-tracing-performance-guide-in-unreal-engine?application_version=5.7#performance-debug-visualization)
* [Hit Shading Costs](/documentation/en-us/unreal-engine/ray-tracing-performance-guide-in-unreal-engine?application_version=5.7#hit-shading-costs)
* [Far Field](/documentation/en-us/unreal-engine/ray-tracing-performance-guide-in-unreal-engine?application_version=5.7#far-field)
* [Achieving 60 FPS with Ray Tracing](/documentation/en-us/unreal-engine/ray-tracing-performance-guide-in-unreal-engine?application_version=5.7#achieving60fpswithraytracing)
* [Additional Ray Tracing Debug Visualization Modes](/documentation/en-us/unreal-engine/ray-tracing-performance-guide-in-unreal-engine?application_version=5.7#additional-ray-tracing-debug-visualization-modes)
* [Picker Debug Visualization Mode](/documentation/en-us/unreal-engine/ray-tracing-performance-guide-in-unreal-engine?application_version=5.7#picker-debug-visualization-mode)
* [Dynamic Instances Debug Visualization Mode](/documentation/en-us/unreal-engine/ray-tracing-performance-guide-in-unreal-engine?application_version=5.7#dynamic-instances-debug-visualization-mode)
