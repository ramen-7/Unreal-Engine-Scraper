<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/hybrid-nonnanite-and-nanite-content-workflows?application_version=5.7 -->

# Hybrid Non-Nanite and Nanite Content Workflows

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
8. Hybrid Non-Nanite and Nanite Content Workflows

# Hybrid Non-Nanite and Nanite Content Workflows

Workflows for projects using both Nanite and Non-Nanite content.

On this page

The following sections highlight workflows you can use in your Nanite-enabled projects that need to also support non-Nanite features and platforms without duplicating assets.

## Importing a High-Resolution Mesh for Nanite

You can import a high resolution mesh to be your Nanite representation for any existing non-Nanite static meshes through the Content Browser or the Static Mesh editor.

From the Content Browser, you can use the right-click context menu on a static mesh asset to select Level of Detail > High Res > Import High Res and navigate to the file you want to import.

[![](https://dev.epicgames.com/community/api/documentation/image/5fd17214-c1d5-4f6e-bc84-229d2d3a40b3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5fd17214-c1d5-4f6e-bc84-229d2d3a40b3?resizing_type=fit)

Alternatively, you can use the Static Mesh editor to import a high resolution mesh using the Nanite Settings in the Details panel. Click Import and navigate to the file you want to import.

[![](https://dev.epicgames.com/community/api/documentation/image/952e066e-fa87-4abc-a649-a4236a304ebf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/952e066e-fa87-4abc-a649-a4236a304ebf?resizing_type=fit)

Using this workflow, the pre-existing static mesh and its level of detail (LOD) chain become the fallback mesh rather than having the import process automatically generate a fallback mesh from the Nanite geometry.

This workflow respects the Disallow Nanite setting on static mesh actors in your scenes and is explained more in the Static Mesh Component Option section below.

## Material Workflows

There are two ways you can improve your non-Nanite and Nanite workflows with materials:

* By using a node in the material graph to break up logic paths.
* By using an override material only used for rendering with Nanite.

### Nanite Pass Switch Node

The Nanite Pass Switch node gives you a way to define specialized behavior in a material graph when rendered with Nanite.

[![](https://dev.epicgames.com/community/api/documentation/image/8ecb2d34-d3b2-4299-94c5-58f24a19c12a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8ecb2d34-d3b2-4299-94c5-58f24a19c12a?resizing_type=fit)

Use the Default input when rendering into non-Nanite passes, to handle the material as it would be normally. Use the Nanite input for any material logic you want to simplify or be specifically rendered to Nanite passes. For example, in cases where a material uses a feature not supported by Nanite, you can keep the same logic for the Default input and use a friendlier logic for the Nanite input.

### Nanite Override Material

The Nanite Override Material slot is available on materials and material instances. When you set an override material, any Nanite-enabled meshes that have the material or material instance assigned will use the referenced Nanite override material instead. This means that you can create materials specific to Nanite workflows rather than managing logic directly inside the material graph using the Nanite Pass Switch node.

[![](https://dev.epicgames.com/community/api/documentation/image/b17c6758-c9a9-4f31-906d-04888de07e9c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b17c6758-c9a9-4f31-906d-04888de07e9c?resizing_type=fit)

In material instances, the Nanite Override Material slot is forcibly defaulted to None so that setting the override in a parent material will not cause it to automatically be inherited in any of the child instances of that material.

In the example below, the static mesh asset for the statue has Nanite enabled and it has a material instance applied. The material instance has its Nanite override material set with some simple color changes for demonstration purposes. The static mesh actor on the left displays the Nanite override material since the mesh is being rendered with Nanite. The static mesh actor on the right displays the same material until Disallow Nanite is set on the actor, disabling the Nanite override material to show the non-Nanite base material of the material instance.

## Static Mesh Component Option: Disallow Nanite

You can set when Nanite-enabled static meshes should use their Nanite representation using the Disallow Nanite setting on individual scene actors. This means you can have a mix of Nanite and non-Nanite actors which use the same static mesh asset.

[![](https://dev.epicgames.com/community/api/documentation/image/365fa81b-69a2-488b-9b44-bea008d24bb4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/365fa81b-69a2-488b-9b44-bea008d24bb4?resizing_type=fit)

The example below shows a single Nanite-enabled static mesh asset where the left is the Nanite mesh representation and the right has Disallow Nanite enabled.

[![](https://dev.epicgames.com/community/api/documentation/image/3aa6860e-3558-4d8a-b2fc-75b4bba1520b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3aa6860e-3558-4d8a-b2fc-75b4bba1520b?resizing_type=fit)

## Landscape Terrain

You can enable Nanite on landscape actors. Nanite landscape meshes are rebuilt in the background to not disrupt user workflow while in the editor. Nanite landscape does not improve landscape resolution but does provide the user the leverage of Nanite runtime features such as GPU culling, automatic geometry streaming, and LODs. It generally boosts runtime performance, especially for demanding features such as VSM.

To learn how to enable and use Nanite with your landscape, see [Using Nanite with Landscapes](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-nanite-with-landscapes-in-unreal-engine).

## Performance of Typical Content

For comparison purposes, the following GPU timings were taken from the Unreal Engine 5 technical demo [Lumen in the Land of Nanite](https://www.youtube.com/watch?v=qC5KtatMcUw) on a PlayStation 5:

* Average render resolution of 1400p temporally upsampled to 4K.
* ~2.5 milliseconds (ms) to cull and rasterize all Nanite meshes (which was nearly everything in this demo)

  + Nearly all geometry used was a Nanite mesh
  + Nearly no CPU cost since it is 100% GPU-driven
* ~2ms to evaluate materials for all Nanite meshes

  + Small CPU cost with 1 draw call per material present in the scene.

When considering these GPU times together, it's approximately 4.5ms combined for what would be equivalent to Unreal Engine 4's depth prepass plus the base pass. This makes Nanite well-suited for game projects targeting 60 FPS.

Numbers like these should be expected from content that doesn't suffer from the aforementioned performance pitfalls in previous sections. Very high instance counts and large numbers of unique materials can also cause increased costs and is an area of Nanite development that we are actively working on.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Importing a High-Resolution Mesh for Nanite](/documentation/en-us/unreal-engine/hybrid-nonnanite-and-nanite-content-workflows?application_version=5.7#importingahigh-resolutionmeshfornanite)
* [Material Workflows](/documentation/en-us/unreal-engine/hybrid-nonnanite-and-nanite-content-workflows?application_version=5.7#materialworkflows)
* [Nanite Pass Switch Node](/documentation/en-us/unreal-engine/hybrid-nonnanite-and-nanite-content-workflows?application_version=5.7#nanitepassswitchnode)
* [Nanite Override Material](/documentation/en-us/unreal-engine/hybrid-nonnanite-and-nanite-content-workflows?application_version=5.7#naniteoverridematerial)
* [Static Mesh Component Option: Disallow Nanite](/documentation/en-us/unreal-engine/hybrid-nonnanite-and-nanite-content-workflows?application_version=5.7#staticmeshcomponentoption:disallownanite)
* [Landscape Terrain](/documentation/en-us/unreal-engine/hybrid-nonnanite-and-nanite-content-workflows?application_version=5.7#landscapeterrain)
* [Performance of Typical Content](/documentation/en-us/unreal-engine/hybrid-nonnanite-and-nanite-content-workflows?application_version=5.7#performanceoftypicalcontent)
