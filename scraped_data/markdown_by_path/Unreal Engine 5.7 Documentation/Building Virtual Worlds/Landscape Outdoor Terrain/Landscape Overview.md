<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-overview?application_version=5.7 -->

# Landscape Overview

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
4. Landscape Overview

# Landscape Overview

An overview of the Landscape Outdoor Terrain System and how to use it in your projects.

![Landscape Overview](https://dev.epicgames.com/community/api/documentation/image/a5dff010-bba7-4380-a62d-d01ebc5e8d8b?resizing_type=fill&width=1920&height=335)

 On this page

Using the **Landscape** system, you can create terrain for your world. Mountains, valleys, uneven or sloped ground, and even openings for caves are possible. Using the collection of tools in the Landscape system, you can modify your terrain's shape and appearance.

For information about opening and using the Landscape tool, refer to the Landscape Quick Start Guide.

## Landscape Tool Modes

[![Landscape Tool Modes](https://dev.epicgames.com/community/api/documentation/image/0e80ad98-f9c6-4fb4-9568-fc82a72f5024?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0e80ad98-f9c6-4fb4-9568-fc82a72f5024?resizing_type=fit)

The Landscape tool has three modes, accessible by their buttons at the top of the Landscape tool's window.

[![Landscape-modes-in-landscape-tab](https://dev.epicgames.com/community/api/documentation/image/50b7cf24-73df-4383-bb61-6b9c484e9348?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/50b7cf24-73df-4383-bb61-6b9c484e9348?resizing_type=fit)

| Icon | Mode | Description |
| --- | --- | --- |
| [Manage mode](https://dev.epicgames.com/community/api/documentation/image/78c8964b-6b4d-484c-b23e-ee1a5f155bb7?resizing_type=fit) | **Manage mode** | Create new Landscapes, and modify Landscape components. Manage mode is also where you work with [Landscape Copy Tool](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-copy-tool-in-unreal-engine) to copy, paste, import, and export parts of your Landscape. For more information about Manage mode, refer to [Landscape Manage Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-manage-mode-in-unreal-engine). |
| [Sculpt mode](https://dev.epicgames.com/community/api/documentation/image/c0396738-cf26-4e55-8dff-5369c2571f19?resizing_type=fit) | **Sculpt mode** | Modify the shape of your Landscape by selecting and using specific tools. For more information about Sculpt mode, refer to [Landscape Sculpt Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-sculpt-mode-in-unreal-engine). |
| [Paint mode](https://dev.epicgames.com/community/api/documentation/image/15711be1-7725-45e4-8a5a-6426daf5757a?resizing_type=fit) | **Paint mode** | Modify the appearance of parts of your Landscape by painting textures on it, based on the layers defined in the Landscape's Material. For more information about Paint mode, refer to [Landscape Paint Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-paint-mode-in-unreal-engine). |

Creating a Landscape means creating a Landscape Actor. As with other Actors, you can edit many of its properties, including its assigned Material, in the Level Editor's **Details** panel. For more information about **Details** panels, refer to [Level Editor Details Panel](https://dev.epicgames.com/documentation/en-us/unreal-engine/level-editor-details-panel-in-unreal-engine).

## Landscape Features

Below are the main features and techniques employed by the Landscape terrain system.

### Large Terrain Sizes

The Landscape system paves the way for terrains that are orders of magnitude larger than what has been possible in Unreal Engine previously. Because of its powerful Level of Detail (LOD) system and the way it makes efficient use of memory, heightmaps up to 8192x8192 are now legitimately possible and feasible. Unreal Engine now supports expansive outdoor worlds, which means quick game creation without modifying the stock engine or tools.

[![Landscape Terrain Size](https://dev.epicgames.com/community/api/documentation/image/9564b49d-7bb9-42e5-8d4d-71b27e95fd9e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9564b49d-7bb9-42e5-8d4d-71b27e95fd9e?resizing_type=fit)

City Sample Landscape. Click image to expand.

### World Partition

Landscape integrates natively with [World Partition](https://dev.epicgames.com/documentation/en-us/unreal-engine/world-partition-in-unreal-engine) to subdivide a landscape into separately streamable parts.  The landscape is edited as a single unified object, which is internally subdivided into separate Actors (called **Landscape Proxies**). The Proxies can be dynamically loaded and unloaded in the editor and by the client runtime.

This allows overall landscape sizes that would be too slow to usefully render or edit all at once.  It also enables multiple users to edit different areas of the landscape at the same time without file contention conflicts.

### Landscape Memory Usage

Landscapes are generally a better choice for creating large terrains than **Static Meshes**.

Landscapes use 4 bytes per vertex for the vertex data. Static Meshes store position as a 12-byte vector, and tangent X and Z vectors packed into 4 bytes each, and either 16-bit or 32-bit float UVs for a total of either 24 or 28 bytes per vertex.

This means Static Meshes use 6 or 7 times the memory Landscapes use for the same vertex density. Landscapes also store their data as **Textures** and can stream out unused LOD levels for distant areas and load them from disk in the background as you approach them. Landscapes use a regular heightfield that efficiently stores collision data compared to the collision data for Static Meshes.

### Static Render Data Stored as Textures in GPU Memory

On most platforms, the Landscape system stores the render data for the terrain in Textures in GPU memory. This storage can be used for data look-up in the vertex shader. The render data uses a 32-bit Texture for storage, with the height occupying 16-bits in the form of the R and G channels and the normal stored as 28-bit values for X and Y, occupying the B and A channels, respectively.

### Continuous Geo-MipMap LOD

Standard Texture mipmaps handle LODs for Landscape terrains. Each mipmap is a level of detail, and the mipmap to sample can be specified using the `text2Dlod` HLSL instruction. Your Landscape can have a large number of LODs, yet maintain smooth LOD transitions, because mip levels for both LODs involved in a transition can be sampled, and then the heights and X and Y offsets can be interpolated in the vertex shader creating a clean morphing effect.

|  |  |  |
| --- | --- | --- |
| [Landscape LOD1](https://dev.epicgames.com/community/api/documentation/image/cd1afdb2-f1f9-4100-b084-3c7bca5e0978?resizing_type=fit) | [Landscape LOD1 to LOD2](https://dev.epicgames.com/community/api/documentation/image/489ce2eb-c16f-4166-8204-02ce24b138bc?resizing_type=fit) | [Landscape LOD2](https://dev.epicgames.com/community/api/documentation/image/cfd570c8-7d67-4a42-bca2-3178d8eba6c0?resizing_type=fit) |
| **Fully LOD 1** | **Morphing from LOD 1 to LOD 2** | **Fully LOD 2** |

### Heightmap and Weight Data Streaming

With Textures storing data, the standard Texture streaming system in Unreal Engine handles streaming mipmaps in and out as needed. This applies to the heightmap data and the weights for Texture layers. Only requiring the mipmaps needed for each LOD minimizes the amount of memory used at any time, which means you can create a more extensive terrain.

### High Resolution LOD-Independent Lighting

The entire high-resolution (non-LOD'd) normal data is available for lighting calculations due to the storage of the X and Y slopes of the Landscape.

|  |  |
| --- | --- |
| [Landscape LODs](https://dev.epicgames.com/community/api/documentation/image/1cfc94b9-64e1-470b-9fc7-2349287f853a?resizing_type=fit) | [Landscape Full Resolution Normals](https://dev.epicgames.com/community/api/documentation/image/11d57506-b32c-46eb-afd3-e567b32a09cd?resizing_type=fit) |
| **Landscape LODs** | **Full Resolution Normals** |

This means you can always use the highest resolution of the terrain for per-pixel lighting, even on distant components that have been LOD'd out.

|  |  |
| --- | --- |
| [Landscape Simple Vertex Lighting](https://dev.epicgames.com/community/api/documentation/image/9b057867-245e-4391-afac-349405a226a4?resizing_type=fit) | [Landscape High Res Per-Pixel](https://dev.epicgames.com/community/api/documentation/image/a99750f2-e4de-4201-8db5-2792fc4326fe?resizing_type=fit) |
| **Simple Vertex Lighting** | **High Res Per-Pixel Lighting** |

When this high-resolution normal data combines with detailed normal maps, Landscape terrains can achieve highly detailed lighting with very little overhead.

|  |  |
| --- | --- |
| [Landscape Geometry Normals](https://dev.epicgames.com/community/api/documentation/image/8e1a905c-2def-4bd7-afb0-75bca4ecd47d?resizing_type=fit) | [Landscape Detail Normals](https://dev.epicgames.com/community/api/documentation/image/02cae565-9f7a-44c9-9365-fb3cb07692f8?resizing_type=fit) |
| **Geometry Normals Only** | **With Detail Normals** |

### Collision

Landscape uses a heightfield object for its collision. Each target layer can specify a [Physical Material](https://dev.epicgames.com/documentation/en-us/unreal-engine/physical-materials-in-unreal-engine). The collision system will use the dominant layer at each position to determine which Physical Material to use. It is possible to use a reduced resolution collision heightfield (for example, 0.5x render resolution) to save on memory requirements for large Landscape terrains. The collision and render components for distant Landscapes can also be streamed out using the level streaming system.

## Landscape Project Settings

[![Landscape Project Settings](https://dev.epicgames.com/community/api/documentation/image/9b0b6390-4df2-440a-b50e-426d22b033a4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9b0b6390-4df2-440a-b50e-426d22b033a4?resizing_type=fit)

Landscape Project Settings. Click to expand.

| Option | Description |
| --- | --- |
| **Max Number of Layers** | Defines the maximum number of edit layers that can be added to the landscape. |
| **Show Dialog for Automatic Layer Creation** | When true, automatic edit layer creation pops up a dialog where the new layer can be reordered relative to other layers. |
| **Show Update Edit Layers During Interactive Changes** | For landscape layers-affecting changes, allows the landscape to be updated when performing an interactive change (e.g. when changing an edit layer’s alpha). Set to false if the performance when editing gets too bad (the landscape will be properly updated when the dragging operation is done). |
| **Max Components** | Defines the maximum number of components in a Landscape. |
| **Max Image Import Cache Size Mega Bytes** | Defines the maximum size of the import image cache in MB. |
| **Paint Strength Gamma** | Defines the exponent used for adjusting the strength of the **Paint** tool. |
| **Disable Painting Startup Slowdown** | (Will be decomm'ed in 5.8) Enabling this feature creates a reduced brush strength at the beginning of a brush stroke. You need to hover in one place until the brush output is at the desired strength. |
| **Landscape Dirtying Mode** | Defines when the engine requires the Landscape to be resaved:   * **In Landscape Mode and User Triggered Change****s**: Landscapes that are marked as needing to be resaved will not appear in the **Choose file******s** to save** dialog. However, any user-triggered changes (direct or indirect) will require the Landscape to be resaved. This mode is recommended for team collaboration as it provides the best features of the other two modes while ensuring that modified landscape actors are still saved and properly submitted to source control. Default mode. * **In Landscape Mode Only**: Landscapes that are marked as needing to be resaved will not appear in the **Choose files to save** dialog. This is a manual saving mode that puts the responsibility on the user to avoid file contention with other team members. The viewport will display an error message indicating that landscape actors are not up-to-date and need to be resaved. This is done using **Build > Save Modified Landscapes**. * **Auto**: Landscapes that are marked as needing to be resaved will appear in the **Choose files to save** dialog. Changes are saved whenever the Landscape requires it. |
| **Brush Size UIMax** | Maximum size that can be set via the slider for the landscape sculpt/paint brushes. |
| **Brush Size Clamp Max** | Maximum size that can be set manually for the landscape sculpt/paint brushes. |
| **Disable Temporal Anti Aliasing in Landscape Mode** | When true, temporal anti-aliasing will be inactive while in landscape mode. This avoids the ghosting effect on the landscape brush but can lead to aliasing or shimmering on other parts of the image. |
| **Default Landscape Material** | Defines which landscape material is assigned to new landscapes by default. |
| **Default Layer Info Object** | Defines which **Layer Info Object** is added to a new landscape by default. |
| **Display Target Layer Thumbnails** | When true, each target layer will have a representative thumbnail in landscape mode. However, the thumbnail system can be slow. Plus, certain landscape materials (e.g. using RVT) are not able to properly render thumbnails. Thus, setting this to false will skip needlessly rendering landscape layer thumbnails, which can improve the editing experience. |
| **Target Layer Default Blend Method** | Target layer blend method to use for newly created Landscape Layer Info assets. Changing this setting will not affect existing Landscape Layer Info assets. This is only used when `DefaultLayerInfoObject` isn’t set. |
| **HLOD Max** **Texture** **Size** | Maximum size of the textures generated for Landscape HLODs. |
| **Spline Icon World ZOffset** | Offset in Z for the landscape spline icon in world-space. |
| **Spline Icon Scale** | Size of the landscape spline control point icon in the viewport. |

* [landscape](https://dev.epicgames.com/community/search?query=landscape)
* [building virtual worlds](https://dev.epicgames.com/community/search?query=building%20virtual%20worlds)
* [open world](https://dev.epicgames.com/community/search?query=open%20world)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Landscape Tool Modes](/documentation/en-us/unreal-engine/landscape-overview?application_version=5.7#landscape-tool-modes)
* [Landscape Features](/documentation/en-us/unreal-engine/landscape-overview?application_version=5.7#landscape-features)
* [Large Terrain Sizes](/documentation/en-us/unreal-engine/landscape-overview?application_version=5.7#large-terrain-sizes)
* [World Partition](/documentation/en-us/unreal-engine/landscape-overview?application_version=5.7#worldpartition)
* [Landscape Memory Usage](/documentation/en-us/unreal-engine/landscape-overview?application_version=5.7#landscape-memory-usage)
* [Static Render Data Stored as Textures in GPU Memory](/documentation/en-us/unreal-engine/landscape-overview?application_version=5.7#static-render-data-stored-as-textures-in-gpu-memory)
* [Continuous Geo-MipMap LOD](/documentation/en-us/unreal-engine/landscape-overview?application_version=5.7#continuous-geo-mip-map-lod)
* [Heightmap and Weight Data Streaming](/documentation/en-us/unreal-engine/landscape-overview?application_version=5.7#heightmap-and-weight-data-streaming)
* [High Resolution LOD-Independent Lighting](/documentation/en-us/unreal-engine/landscape-overview?application_version=5.7#high-resolution-lod-independent-lighting)
* [Collision](/documentation/en-us/unreal-engine/landscape-overview?application_version=5.7#collision)
* [Landscape Project Settings](/documentation/en-us/unreal-engine/landscape-overview?application_version=5.7#landscape-project-settings)
