<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/visibility-and-occlusion-culling-reference-in-unreal-engine?application_version=5.7 -->

# Visibility and Occlusion Culling Reference

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
7. [Visibility and Occlusion Culling](/documentation/en-us/unreal-engine/visibility-and-occlusion-culling-in-unreal-engine "Visibility and Occlusion Culling")
8. Visibility and Occlusion Culling Reference

# Visibility and Occlusion Culling Reference

A reference for available visibility and occlusion culling methods' settings.

![Visibility and Occlusion Culling Reference](https://dev.epicgames.com/community/api/documentation/image/145a34aa-abe6-406b-b61c-660c53cde7f7?resizing_type=fill&width=1920&height=335)

 On this page

In this page, you'll find settings for your project and different volume types that are used for visibility and occlusion culling in your Unreal Engine projects.

## Project Settings

The **Project Settings** contains culling settings that affect the entirety of your project, such as support for Hardware Occlusion Queries, the screen size that lights should be culled, and more.

You can view these settings by opening the Project Settings window, select **Rendering** and locate the **Culling** section.

[![ProjectSettings.png](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5d3d3726-3488-4640-809a-7dadec2315c2/projectsettings.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5d3d3726-3488-4640-809a-7dadec2315c2/projectsettings.png)

Click image for full size.

| Property | Description |
| --- | --- |
| **Occlusion Culling** | Allows occlusion query methods (such as Hardware, Software, and Round Robin Occlusion Queries) to cull Actors. This setting does not disable distance-based culling methods, like Cull Distance or Precomputed Visibility Volumes.  Disabling occlusion culling can have significant performance implications for your project and levels depending on the number of Actors being rendered. |
| **Min Screen Radius for Lights** | Sets the minimum screen radius at which lights are culled from view. Larger values can improve performance by culling lights more quickly. However, very large values can degrade performance if large occluders are not rendered. |
| **Min Screen Radius for Early Z Pass** | Sets the minimum screen radius for objects to be culled by the Early-Z Pass. Larger values can improve performance by culling objects more quickly. However, very large values can degrade performance if large occluders are not rendered. |
| **Min Screen Radius for Cascaded Shadow Maps** | Sets the minimum screen radius for objects to be culled for Cascaded Shadow Map depth passes. Larger values can improve performance. However, they can cause artifacts as objects stop casting shadows at closer distances from the camera. |
| **Warn about no precomputed visibility** | Enables a warning when there is no precomputed visibility data available for the current camera location. It can be a helpful reminder if your project relies on precomputed visibility for occlusion. |

## Actor Settings

Selected Actors in a Level or Blueprint contain distance settings accessed through their **Details** panel. They enable per-instance distances to be set or whether the Actor is culled using a Cull Distance Volume.

[![DetailsPanel-1.png](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9014f58b-9a11-44b0-b7cd-2f08018e8ac3/detailspanel-1.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9014f58b-9a11-44b0-b7cd-2f08018e8ac3/detailspanel-1.png)

Click for full size image.

| Property | Description |
| --- | --- |
| **Min Draw Distance** | Sets the minimum draw distance at which the object will be rendered in the scene. This is measured in world space units (centimeters) from the center of the object's bounding sphere to the camera position. |
| **Desired Max Draw Distance** | Sets the maximum draw distance for Level Designers. The "real" max distance is **Min Draw Distance** (disregarding 0). |
| **Current Max Draw Distance** | A read-only distance that the object will be culled at. This value is representative of either the **Min Draw Distance** or one of the **Cull Distances** set by a Cull Distance Volume for reference. When a value of 0 is shown, it indicates that this object should not be culled. |
| **Never Distance Cull** | When enabled, this object will not be culled by distance. It is also ignored if it's a child of a Hierarchical Level of Detail (HLOD) mesh. |
| **Allow Cull Distance Volume** | Whether to accept cull distance volume's cull distance values to modify cached cull distance. |
| **Treat as Background for Occlusion** | Enables this object to be treated as part of the background for occlusion purposes. This can be used as an optimization to reduce the cost of rendering skyboxes and large ground planes that are part of the vista. |
| **Use as Occluder** | Whether to render the primitive in the depth-only pass. This should generally be true for all objects and let the renderer make decisions about whether to render objects in the depth-only pass. |

## Cull Distance Volume

**Cull Distance Volumes** enable you to specify a range of sizes and cull distances that Actors should no longer be drawn.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ad6baf7d-6912-4ef3-ba53-618aafe9758d/pvisoverride.png "PVisOverride.png")

| Property | Description |
| --- | --- |
| **Cull Distances** | A array listing of Size and Cull Distance pairs used to set the draw distance of objects based on their size within a Cull Distance Volume. The code will calculate the sphere diameter of a object's bounding box and look for a best fit in this array to determine which cull distance to assign to an object.  **Size** --- The size to associate with cull distance.  **Cull Distance** --- The distance to associate with an Actor's bounds size. |
| **Enabled** | Whether the volume is currently enabled or not. |

## Precomputed Visibility World Settings

In the **World Settings** under **Precomputed Visibility** you'll have access to settings that change how precomputed visibility is generated.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3d5280a9-425f-49b4-a1d3-572c87a4c071/pvisworldsettings.png "PVisWorldSettings.png")

| Property | Description |
| --- | --- |
| **Precomputed Visibility** | Whether to place visibility cells inside Precomputed Visibility Volumes and along camera tracks for this level. Precomputing visibility reduces rendering thread time at the cost of some runtime memory and somewhat increased lighting build times. |
| **Place Cells Only Along Camera Tracks** | When this is enabled visibility cells will only be placed along the camera track. |
| **Visibility Cells** | World space size of precomputed visibility cells in the x and y. Smaller sizes produce more effective occlusion culling at the cost of increased runtime memory usage and lighting build times. |
| **Visibility Aggressiveness** | Determines how aggressive precomputed visibility should be. More aggressive settings cull more objects, but also cause more visibility errors like popping. |

For additional information, see [Precomputed Visibility Volumes](/documentation/en-us/unreal-engine/precomputed-visibility-volumes-in-unreal-engine).

## Precomputed Visibility Override Volume

**Precomputed Visibility Override Volumes** enable you to override visibility control of Actors and Levels within an existing Precomputed Visibility Volumes.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ecd05da3-116d-443b-9f7a-42662b61a799/pvisoverride1.png "PvisOverride1.png")

| Property | Description |
| --- | --- |
| **Override Visible Actors** | An array of Actors that will always be considered visible by precomputed visibility when viewed from inside this volume. |
| **Override Invisible Actors** | An array of Actors that will always be considered invisible by precomputed visibility when viewed from inside this volume. |
| **Override Invisible Levels** | An array of level names whose Actors will always be considered invisible by precomputed visibility when viewed from inside this volume. |

For additional information, see [Precomputed Visibility Volumes](/documentation/en-us/unreal-engine/precomputed-visibility-volumes-in-unreal-engine).

* [performance](https://dev.epicgames.com/community/search?query=performance)
* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [optimization](https://dev.epicgames.com/community/search?query=optimization)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Project Settings](/documentation/en-us/unreal-engine/visibility-and-occlusion-culling-reference-in-unreal-engine?application_version=5.7#projectsettings)
* [Actor Settings](/documentation/en-us/unreal-engine/visibility-and-occlusion-culling-reference-in-unreal-engine?application_version=5.7#actorsettings)
* [Cull Distance Volume](/documentation/en-us/unreal-engine/visibility-and-occlusion-culling-reference-in-unreal-engine?application_version=5.7#culldistancevolume)
* [Precomputed Visibility World Settings](/documentation/en-us/unreal-engine/visibility-and-occlusion-culling-reference-in-unreal-engine?application_version=5.7#precomputedvisibilityworldsettings)
* [Precomputed Visibility Override Volume](/documentation/en-us/unreal-engine/visibility-and-occlusion-culling-reference-in-unreal-engine?application_version=5.7#precomputedvisibilityoverridevolume)
