<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-foliage?application_version=5.7 -->

# Nanite Foliage

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
8. Nanite Foliage

# Nanite Foliage

An overview of Nanite Foliage and its rendering pipeline.

![Nanite Foliage](https://dev.epicgames.com/community/api/documentation/image/cf6c1b06-4191-4bb6-9203-c90751b22aed?resizing_type=fill&width=1920&height=335)

Learn to use this **Experimental** feature, but use caution when shipping with it.

 On this page

**Nanite Foliage** is a set of integral systems using [Nanite’s virtualized geometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine) rendering to achieve dense, highly-detailed foliage at scale. Nanite foliage makes use of old and new techniques to render open worlds with large open vistas at higher quality at a fraction of the original frame costs, with instancing, skinned meshes, voxelization, animation, and material characteristics. When combined, this allows for more robust worlds to be imagined with lifelike and animated foliage.

A flythrough of The Witcher 4 Technical Demo forest rendered using Nanite Foliage.

To understand the goals of Nanite Foliage and where it’s headed, it’s important to understand that what has worked in the past isn't efficient for the future in creating these types of fully realized worlds.

Let’s look at some of the ways that the “old way” of developing foliage doesn’t work well for Nanite Foliage:

|  |  |  |
| --- | --- | --- |
|  |  |  |
| **Alpha Masking** | **100% Nanite Triangle Representation** | **World Position Offset (WPO) Material** |

* **Alpha Masking:** Nanite doesn’t work well with it since it introduces a lot of overdraw in addition to having to execute a potentially expensive mask function. Using alpha masking also means that foliage would continue to be rendered as flat cards instead of the geometric complexity it’s capable of.
* **Full Nanite Triangle Representation:** This would cause sub-optimal cluster culling and poor simplification in the distance. Also, each foliage type would require large amounts of disk space to store them.
* **World Position Offset (WPO):** Using WPO in a material to move leaves and branches of foliage has been a way to simulate wind. This isn’t a good match for what Nanite can render since it adds per vertex calculations and forces sub-optimal cluster bounds since there’s no way to know how a material will move a vertex, meaning the calculations have to be more conservative.

Now that you have some idea about what isn’t going to work well, let’s take a look at the Nanite Foliage pipeline to render fully modeled trees, down to the individual leaves and needles. It needs to scale to large open worlds while being memory efficient, performant, and highly dynamic without the need for levels of detail (LOD) meshes.

To do this, Nanite Foliage is made up of three systems:

|  |  |  |
| --- | --- | --- |
|  |  |  |
| **Nanite Assemblies** | **Nanite Voxels** | **Nanite Skinning** |

* **Nanite Assemblies** are the “parts” that become highly detailed instances across a piece of foliage. This can significantly reduce memory and disk size.
* **Nanite Voxels** are near pixel-sized aggregate voxels that preserve triangle details, animation, and material properties based on camera distance. Triangles seamlessly switch to voxels to solve the problem of rendering dense and dynamic aggregate triangle meshes. These voxels are imperceptible to the eye because of their size on screen.
* **Nanite Skinning** defines how foliage behaves dynamically with systems, such as wind, where wind is simulated through a bone hierarchy. By not using WPO to simulate wind animation, Nanite Foliage can use optimal cluster bounds.

In the example below, you can see how all this works together. As the camera zooms in on the detail, you can see how dense and highly-detailed the tree is down to individual pine needles. As the camera pulls away, once Nanite clusters become small enough they seamlessly transition to voxels. This allows trees to retain their volumetric look at distances without resorting to billboards or LODs in the distance.

With this tree, it has the following:

* 41 million triangles
* 12 unique assembly parts
* 2160 assembly part instances
* 850 skeletal bones

## Enabling Nanite Foliage

To enable Nanite Foliage for your project, use the **Project Settings > Rendering** to check the box for Nanite Foliage. You’ll need to restart the editor for the changes to take effect.

Nanite Foliage is not enabled by default for projects. If the engine encounters a Nanite Assembly asset without it enabled, a pop-up warning appears.

[![](https://dev.epicgames.com/community/api/documentation/image/64e5dd76-dd97-47cc-96d0-b5d9d77f8b68?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/64e5dd76-dd97-47cc-96d0-b5d9d77f8b68?resizing_type=fit)

### Nanite Assemblies

**Nanite Assemblies** are a key component of Nanite Foliage and are designed to efficiently handle the rendering of complex, repeatable geometry, such as branches and fronds of a tree. Assemblies work with both static and skeletal mesh assets, allowing for the “micro-instancing” of small, highly detailed parts. They can contain up to 65k instances of other meshes. These instances are called the “parts” of the assembly. This approach saves a significant amount of disk space and streaming space, with a small performance trade-off during cluster culling.

[![Example of a rendered tree and its assembly parts instanced.](https://dev.epicgames.com/community/api/documentation/image/530144be-aed1-42e0-a39e-7a27179dc084?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/530144be-aed1-42e0-a39e-7a27179dc084?resizing_type=fit)

Example of a rendered tree and its assembly parts instanced.

Nanite assemblies work by taking the clusters of the part meshes and encodes them into the final mesh’s hierarchy without duplicating the geometry of the parts during build time. At runtime, Nanite handles the part instances by calculating their final transform on-demand during cluster culling as it descends the hierarchy.

On non-Nanite platforms, the triangles of the parts are transformed and merged together into a single mesh. From there, it is simplified to generate a fallback mesh that works the same as regular Nanite fallback meshes.

Assemblies are a crucial part of Nanite Foliage. Without them, there wouldn’t be enough disk space or streaming memory to render a large-world forest, like the one shown in [Unreal Fest The Witcher 4 technical demo](https://youtu.be/Nthv4xF_zHU?si=wdKXM3loFJVr2rLG). For example, the UASSET disk space of the biggest tree in the demonstration went from being **3.5 gigabytes** (Gb) to approximately **29 megabytes** (Mb). The streaming memory of just one of the trees in one particular view was measured to go down from approximately **36 Mb** to around **2.7 Mb**. This kind of saving makes it possible to render 500k instances of dozens of tree variants in a scene, with each tree being highly detailed and having between one and ten million polygons each.

For more information about using and creating assemblies in Unreal Engine, see [Nanite Assemblies](https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-assemblies).

## Nanite Voxels

**Nanite Voxels** are near pixel-sized voxels that preserve detail, animation, and material properties of the geometry it represents and preserve the volumetric appearance of things, like leaves on trees. Previous Nanite techniques for preventing leaves from losing their shape in the distance, worked well enough by adding a surface area back into surviving triangles when the simplification process would eliminate them. It was a mitigation for foliage geometry becoming sparse when rendering simplified clusters in the distance.

[![](https://dev.epicgames.com/community/api/documentation/image/d7348a27-373a-4382-a857-418da49fea28?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d7348a27-373a-4382-a857-418da49fea28?resizing_type=fit)

### Rasterization Process

Nanite Voxels can preserve the general silhouette of aggregate geometry (disconnected pieces) during simplification at distance. When simplifying clusters of these voxel-enabled meshes, Nanite Builder voxelizes them into clusters of, at most, 128 4x4x4 voxel bricks. The simplification error of the voxel representation is the deciding factor for if the simplify makes the switch to voxels from triangles — it will switch to voxels if doing so would result in lower error than using triangles.

At runtime, voxel clusters are binned separately from triangle clusters and rasterized with a special shader permutation. The clusters are sorted into depth buckets, and rasterized from front to back to gain some benefits of early Z testing, with the end result generally performing better in the distance over rasterized triangles.

Below are some examples of the voxelization process visualized on a standalone asset and in the technical demo of The Witcher 4.

![](https://dev.epicgames.com/community/api/documentation/image/5b63991d-94c3-4b5e-90be-0aab44413090?resizing_type=fit)

### Shading Process

Many surfaces with different normals can be contained inside the region covered by a single voxel. So instead of storing a single normal per voxel, a distribution of normals is stored instead. This is similar in concept to how material roughness controls the distribution of microfacets used for shading.

When writing to the GBuffer, a normal is chosen stochastically per pixel from this distribution. In a future release the distribution will be accounted for directly in the shading like roughness is. This will reduce noise and was already in use in the Witcher 4 demo.

This requires extra data to store the statistics for the distribution. Currently that is stored in the vertex color alpha channel meaning it will override whatever was there. This may move to separate data independent from vertex color in the future.

### Enabling Nanite Voxels

To enable Nanite Voxelization:

[![](https://dev.epicgames.com/community/api/documentation/image/e37b1d99-3e24-4d52-8fc6-992a3804ce46?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e37b1d99-3e24-4d52-8fc6-992a3804ce46?resizing_type=fit)

1. From the **Details** panel in a Static Mesh, look under the **Nanite Settings** category.
2. Locate **Shape Preservation** and use the dropdown to select **Voxelize**.

Some properties below this dropdown become available to edit when **Voxelize** is set. These are not intended for most, if anyone, to adjust for their projects. Some are still in development and don’t actually work as intended yet, if at all. These settings are likely to change or be removed in future versions of Unreal Engine as Nanite Foliage matures.

## Using Nanite Skinning for Animation of Nanite Foliage

When it comes to wind animation of foliage in games, a lot of it is done using world position offset (WPO) in the material, usually for the materials used for branches and leaves of trees. Because the WPO for a given vertex can be any arbitrary offset, artists are required to set the **Max WPO Displacement** on any of materials for the worst-case in order to help pad the culling bounds for proper culling of these foliage assets. However, this can result in overly conservative bounds that contribute to high overdraw cost.

Because WPO also changes vertex shader logic, each material is binned into separate dispatches, which has associated GPU costs. With many materials, these programmable raster bins can be a performance issue.

**Nanite Skinning** resolves this because more accurate bounds can be calculated from skinning matrices and everything can use the fixed function rasterizer.

In this shot below, there are one-hundred thousand bones updating, which takes about 0.1 milliseconds on the GPU, making Nanite Foliage very fast and scalable. Animation stops being applied automatically on trees that are below a certain screen size, with wind being able to affect trees very far in the distance for better immersion. This also applies to grass and shrubs that use skeletal meshes.

### Dynamic Wind Plugin

This plugin is experimental.

The **Dynamic Wind** plugin is designed to work with Nanite Foliage. It requires some additional setup using a **Dynamic Wind Skeletal Data** asset for a particular skeletal mesh. The data in this asset classifies bones of the skeleton into **Simulation Groups** that helps the system logically identify bone chains in the simulation, as well as enabling you to adjust wind influence per group.

You can enable the plugin from the **Plugins** browser under the **Rendering** category.

[![](https://dev.epicgames.com/community/api/documentation/image/64707dac-ed89-4af6-9896-cb4e3e56805c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/64707dac-ed89-4af6-9896-cb4e3e56805c?resizing_type=fit)

The plugin provides a [scripted asset action](https://dev.epicgames.com/community/learning/tutorials/owYv/unreal-engine-getting-started-with-editor-utility-blueprints#ascriptedassetaction) to import necessary data from a .JSON file. It also includes a Universal Scene Description (USD) schema that you can apply to a Skeleton to provide this data, along with an example Python script to create a JSON file from the USD.

#### Dynamic Wind Transform Provider Data

Skeletal meshes that contain user data from a **Dynamic Wind Data** asset can use this data to drive wind animation in an Instanced Skinned Mesh Component.

To enable wind on a skinned mesh, use the **Transform Provider** dropdown on the component to select the **Transform Provider Data**. This creates a new **Dynamic Wind** **Data** asset for the mesh.

This asset is needed to register the component with the wind system. It doesn’t serve any other purpose (at this time).

[![](https://dev.epicgames.com/community/api/documentation/image/0cf130af-6c63-4aa3-9998-ce8b1b39540c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0cf130af-6c63-4aa3-9998-ce8b1b39540c?resizing_type=fit)

The current limitations of this are:

* Adding more physically based simulation, such as near field.
* Only has support for global wind direction.
* No collision with players or objects.
* Dynamic Wind Skeletal Data must be imported with a JSON file.

  + Future work includes having this automatically imported when importing a USD.
* Add adjustments to the Dynamic Wind Transform Provider data.

### Nanite Skinning Performance Tips

While Nanite Skinning works better than WPO for foliage wind movement, it’s still necessary to be mindful of performance.

Keep these areas in mind:

* [Virtual Shadow Map (VSM)](https://dev.epicgames.com/documentation/en-us/unreal-engine/virtual-shadow-maps-in-unreal-engine?application_version=5.5) performance requires you to disable animation in the distance.
* Instanced meshes that are disabled switch to an unskinned raster bin and render like a fixed function static mesh (in bind pose).
* Use **Animation Min Screen Size** on the component to disable skinning when the object is small on screen.

  + This is similar to the setting **World Position Offset Disable Distance**, except that it’s always active. If left at **0**, the global default value is used, which is 1/10th (0.1) of the object’s screen size when animation is stopped at. You can change this with the console command `r.Skinning.DefaultAnimationMinScreenSize`.

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [optimization](https://dev.epicgames.com/community/search?query=optimization)
* [forest](https://dev.epicgames.com/community/search?query=forest)
* [foliage](https://dev.epicgames.com/community/search?query=foliage)
* [nanite](https://dev.epicgames.com/community/search?query=nanite)
* [trees](https://dev.epicgames.com/community/search?query=trees)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Enabling Nanite Foliage](/documentation/en-us/unreal-engine/nanite-foliage?application_version=5.7#enablingnanitefoliage)
* [Nanite Assemblies](/documentation/en-us/unreal-engine/nanite-foliage?application_version=5.7#naniteassemblies)
* [Nanite Voxels](/documentation/en-us/unreal-engine/nanite-foliage?application_version=5.7#nanitevoxels)
* [Rasterization Process](/documentation/en-us/unreal-engine/nanite-foliage?application_version=5.7#rasterizationprocess)
* [Shading Process](/documentation/en-us/unreal-engine/nanite-foliage?application_version=5.7#shadingprocess)
* [Enabling Nanite Voxels](/documentation/en-us/unreal-engine/nanite-foliage?application_version=5.7#enablingnanitevoxels)
* [Using Nanite Skinning for Animation of Nanite Foliage](/documentation/en-us/unreal-engine/nanite-foliage?application_version=5.7#usingnaniteskinningforanimationofnanitefoliage)
* [Dynamic Wind Plugin](/documentation/en-us/unreal-engine/nanite-foliage?application_version=5.7#dynamicwindplugin)
* [Dynamic Wind Transform Provider Data](/documentation/en-us/unreal-engine/nanite-foliage?application_version=5.7#dynamicwindtransformproviderdata)
* [Nanite Skinning Performance Tips](/documentation/en-us/unreal-engine/nanite-foliage?application_version=5.7#naniteskinningperformancetips)
