<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-assemblies?application_version=5.7 -->

# Nanite Assemblies

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
8. Nanite Assemblies

# Nanite Assemblies

An overview of Nanite Assemblies and how you can create them to use with Nanite Foliage.

![Nanite Assemblies](https://dev.epicgames.com/community/api/documentation/image/f323c5a4-c88a-4b8f-99b8-f96d54e5309d?resizing_type=fill&width=1920&height=335)

 On this page

**Nanite Assemblies** are a key component of the [Nanite Foliage](https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-foliage) system that is designed to efficiently handle the rendering of complex, repeatable geometry, such as the branches and fronds of a tree. It's a supplemental feature for both skeletal and static meshes, allowing for the "micro-instancing" of small, highly detailed parts.

Nanite assemblies are a crucial part of Nanite Foliage’s rendering pipeline. Without them, there wouldn’t be enough disk space or streaming memory to render these large-world forests, like the one shown in the [Unreal Fest The Witcher 4 technical demo](https://youtu.be/Nthv4xF_zHU?si=wdKXM3loFJVr2rLG).

In the scene above from the demonstration, the disk space for the biggest tree went from being **3.5 gigabytes** (Gb) to approximately **29 megabytes** (Mb). The streaming memory of just one of the trees in one particular view was measured to go down from approximately **36 Mb** to around **2.7 Mb**. This kind of saving makes it possible to render 500k instances of dozens of tree variants in a scene, with each tree being highly detailed and having between one and ten million polygons each.

## How Nanite Assemblies Work

Nanite Assemblies are a collection of **Parts** meshes used to build Nanite Foliage. They are highly detailed meshes that are instanced across a single piece of foliage. These instances transform their position, rotation, and scale within the assembly’s local space. You can combine these parts with a non-instanced base mesh, such as a tree trunk, to create a complete piece of foliage.

|  |  |
| --- | --- |
|  |  |
| **Nanite Assembly Parts** | **Nanite Assemblies instanced on a base skeletal mesh.** |

For skeletal meshes, these parts can be attached to one or more bones, with individual weights to handle deformation. This makes it possible to create detailed animated foliage that responds correctly to skeletal animation, like reacting to dynamic wind.

Nanite Foliage skeletal meshes animating dynamically with wind.

At runtime, Nanite handles the assembly level of detail (LOD) dynamically. This means that at close distances to the camera, the individual parts of an assembly render as their Nanite Instances, preserving all their geometric detail. As the objects become smaller on screen, these parts are simplified, such that Nanite’s rendering system intelligently reduces the complexity until the entire assembly is represented by a single, simplified cluster. This ensures optimal performance.

## Nanite Assemblies versus Standard Instancing

For standard instancing, there are a couple of things that must be considered: it’s memory overhead, and distances these will be rendered at.

Standard instancing has a significant memory overhead in GPU scene buffers for the amount of instancing needed for large, expansive forests. With that comes rendering these instances at near and far distances, with each visible instance requiring at least one root cluster be drawn. Instancing thousands of branches on thousands of trees would mean rasterizing millions of clusters in even the simplest of situations to maintain a high level of detail.

In both of these cases, Nanite Assemblies can handle this much better in terms of performance and maintaining visual fidelity. Assemblies have a much lighter weight overhead per instance, because they are simply a large array of matrices. The trade off in performance does mean you won’t be able to do some things for Nanite Assembly parts that you can do in a material graph using per-instance data. But, what this does mean is during build time, root clusters of assembly parts are combined to create the lowest-resolution levels of the assembly so that are far distances, assemblies simplify all the way down to a single cluster, which is similar to having its own internal hierarchical level of detail (HLOD) to use.

At farther distances, these simplified levels of individual part instances are merged together, with their geometry getting treated as part of the base mesh — the parts lose any identity of being an instance. For this reason, per-instance data isn’t exposed in material graphs for assembly parts.

## Example of a Nanite Assembly Skeletal Mesh

The example below shows the triangles of the base mesh of the **Skeletal Assembly** tree — the trunk and the large branches — are stored in the asset itself alongside references to its assembly **Parts** meshes — twigs attached to the branches. These twigs are just other, small skeletal mesh assets found in the content folder.

For Skeletal Mesh Assemblies, each part instance is bound to one or more bones on the Skeleton of the base mesh so that its pivot animates with the base mesh.

At this time, the vertices of skeletal assembly parts are **not skinned**, so they only animate rigidly in their bind pose.

[![Example of a rendered tree and its assembly parts instanced.](https://dev.epicgames.com/community/api/documentation/image/432aae3d-16ad-450c-a1b1-f1ef30a20c04?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/432aae3d-16ad-450c-a1b1-f1ef30a20c04?resizing_type=fit)

Example of a rendered tree and its assembly parts instanced.

## Creating Nanite Assemblies

Unreal Engine includes some experimental plugins that can help you create Nanite Assemblies by importing them or creating them in-editor. These plugins are:

| Plugin Name |  | Description |
| --- | --- | --- |
| **Nanite Assembly Editor Utilities** |  | This is used to create a Nanite Assembly from Blueprint. It exposes functionality to the editor blueprint to create static and skeletal assemblies. |
| **Procedural Content Generation Framework (PCG) Nanite Assemblies Interop** |  | This is used to generate an assembly from a PCG Graph for Static Mesh Nanite Assemblies. |
| **Procedural Vegetation Editor** |  | This is a graph-based editor used to create high-quality, Nanite-ready vegetation directly in the editor. It applies real-world botanical principles that replicate natural growth patterns with customization and variation for different species of vegetation. |
| **USD Importer** |  | You can import Nanite Assemblies directly from a USD file. Schemas for authoring assemblies is included with the USD Core plugin. |

### Importing Nanite Assemblies with USD

You can import Nanite Assemblies into Unreal Engine from a USD file using the **USD Importer** plugin. The relevant schemas for authoring assemblies are included with the **USD Core** plugin. These include `NaniteAssemblyRootAPI`, `NaniteAssemblyExternalRefAPI`, and `NaniteAssemblySkelBindingAPI`.

For more information on using these schemas, refer to their documentation provided with them in the source code.

### Using Nanite Assembly Editor Utilities for In-Editor Creation

In the editor, you can create assemblies using the **Nanite Assembly Editor Utilities** plugin. This plugin exposes `UNaniteAssemblyStaticMeshBuilder` and `UNaniteAssemblySkeletalMeshBuilder` to Blueprint, providing a powerful way to create assemblies from existing assets.

The plugin also includes level editor scripted actions to:

* Create a static mesh assembly from a selection of static meshes in the level editor.
* Create a skeletal mesh assembly from a skeletal mesh actor and any skeletal mesh components attached to it.

### Using Procedural Vegetation Editor for In-Editor Creation

The **Procedural Vegetation Editor** (PVE) is a powerful, graph-based tool integrated with Unreal Engine and the [Procedural Content Generation](https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-content-generation-framework-in-unreal-engine) (PCG) framework. It enables users to create high-quality, Nanite-ready vegetation assets directly within the editor. PVE leverages real-world botanical principles, simulating plant generation based on hormone distribution and adaptive responses.

[![](https://dev.epicgames.com/community/api/documentation/image/347038f5-25b0-456a-a388-bc498e618989?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/347038f5-25b0-456a-a388-bc498e618989?resizing_type=fit)

Procedural Vegetation Editor (PVE) with example shrub.

  For more information on this tool and its usage, see [Procedural Vegetation Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-vegetation-editor-pve-in-unreal-engine).

## Known Limitations

These are some current limitations to be aware of:

* You cannot create assemblies of other assemblies. The system currently supports a single layer of instancing.
* Geometry is not duplicated between assemblies that reference the same part meshes. Each assembly stores its own copy of the part data.
* For skeletal meshes, you cannot pose individual parts — they will only render in their bind pose.

  + Future updates will add support for instancing animation on individual parts.

## Additional Resources

External developer-created topics you can use to learn more about using Nanite Assemblies.

* **Nanite Assemblies in USD**

  + [Part 1 - Scene Structure](https://dev.epicgames.com/community/learning/tutorials/7O3z/unreal-engine-nanite-assemblies-in-usd-scene-structure-part-1-of-2)
  + [Part 2 - Houdini Tutorials](https://dev.epicgames.com/community/learning/tutorials/1mxR/unreal-engine-nanite-assemblies-in-usd-houdini-tutorials-part-2)

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [optimization](https://dev.epicgames.com/community/search?query=optimization)
* [foliage](https://dev.epicgames.com/community/search?query=foliage)
* [nanite](https://dev.epicgames.com/community/search?query=nanite)
* [trees](https://dev.epicgames.com/community/search?query=trees)
* [forests](https://dev.epicgames.com/community/search?query=forests)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [How Nanite Assemblies Work](/documentation/en-us/unreal-engine/nanite-assemblies?application_version=5.7#hownaniteassemblieswork)
* [Nanite Assemblies versus Standard Instancing](/documentation/en-us/unreal-engine/nanite-assemblies?application_version=5.7#naniteassembliesversusstandardinstancing)
* [Example of a Nanite Assembly Skeletal Mesh](/documentation/en-us/unreal-engine/nanite-assemblies?application_version=5.7#exampleofananiteassemblyskeletalmesh)
* [Creating Nanite Assemblies](/documentation/en-us/unreal-engine/nanite-assemblies?application_version=5.7#creatingnaniteassemblies)
* [Importing Nanite Assemblies with USD](/documentation/en-us/unreal-engine/nanite-assemblies?application_version=5.7#importingnaniteassemblieswithusd)
* [Using Nanite Assembly Editor Utilities for In-Editor Creation](/documentation/en-us/unreal-engine/nanite-assemblies?application_version=5.7#usingnaniteassemblyeditorutilitiesforin-editorcreation)
* [Using Procedural Vegetation Editor for In-Editor Creation](/documentation/en-us/unreal-engine/nanite-assemblies?application_version=5.7#usingproceduralvegetationeditorforin-editorcreation)
* [Known Limitations](/documentation/en-us/unreal-engine/nanite-assemblies?application_version=5.7#knownlimitations)
* [Additional Resources](/documentation/en-us/unreal-engine/nanite-assemblies?application_version=5.7#additionalresources)
