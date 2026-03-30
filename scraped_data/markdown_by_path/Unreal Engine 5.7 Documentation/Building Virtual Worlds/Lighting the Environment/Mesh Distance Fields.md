<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/mesh-distance-fields-in-unreal-engine?application_version=5.7 -->

# Mesh Distance Fields

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
7. Mesh Distance Fields

# Mesh Distance Fields

An overview of Mesh Distance Fields and its available features that you can use when developing your games.

![Mesh Distance Fields](https://dev.epicgames.com/community/api/documentation/image/4faed720-f2a9-4ccc-8407-6487b78d6264?resizing_type=fill&width=1920&height=335)

 On this page

**Unreal Engine** leverages the power of **Distance Fields** to have dynamic ambient occlusion and shadowing for Static Mesh Actors in your games. In addition to that, the Mesh Distance Field representation of an Actor can be used for other features like GPU particle collision or even with the Material Editor to create dynamic flow maps and much more.

Continue reading below to learn how Mesh Distance Fields work and some of the ways you can use it in your games.

## How does it work?

To represent a Static Mesh's surfaces, a **Signed Distance Field** (SDF) is used. It works by storing the distance to the nearest surface in a volume texture. For every point on the exterior of the mesh is considered positive distance and any point inside the mesh stores a negative distance. In the example below, the positive distances are being traced and stored to represent the tree later on.

![Example of the storing distance to the nearest surface](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8ef9f5cf-b9bf-4911-8bb3-62168e2448f2/01-distance-field-positive-distance-tracing.png)

The first property of SDF that make them useful is that when tracing a ray, you can safely skip through empty space as the distance to the nearest surface is already known (this is sometimes called Sphere Tracing). This allows the intersections to be determined with a small number steps. By ray tracing a distance field, a visibility result is produced, meaning that if the ray intersects the mesh, the light will then be shadowed.

![Example of the sphere tracing principle](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/36617eb9-2551-49ff-b0c8-ff2bd40f7828/02-distance-field-sphere-tracing.png)

The second property that makes SDF useful is that when you trace a ray, by tracking the closest distance a ray passed by an occluding object, an approximate cone intersection can be computed with no extra cost. This approximation makes it possible to do very soft area shadows and sky occlusion using distance fields. This property is key to features like [Distance Field Ambient Occlusion](/documentation/en-us/unreal-engine/distance-field-ambient-occlusion-in-unreal-engine) as a small number of cones can compute a soft visibility for the entire hemisphere of a receiver point.

![Example of the tracking the closest distance a ray passed by an occluding object](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a00fed3b-d268-4fd8-a1af-37f51b80896e/03-distance-field-cone-tracing.png)


You can read further about [using Distance Fields for Lighting](http://iquilezles.org/www/articles/raymarchingdf/raymarchingdf.htm) here.



## Scene Representation

Each level that you create is made up of all these Mesh Distance Fields for your placed Actors. When Mesh Distance Fields are generate, they are done so "offline" using triangle raytracing that stores the results in a volume texture. Because of this, mesh distance field generation cannot be done at runtime. This method computes the Signed Distance Field rays in all directions to find the nearest surface and stores that information.

You can visualize the Mesh Distance Fields that represent your scene by using the viewport and selecting **Show > Visualize > Mesh Distance Fields**.

|  |  |
| --- | --- |
| [undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/af4e2e5b-8665-42a0-90eb-9f2f7a6c9a6f/04-distance-field-enable-mdf-view-mode.png) | [undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e90c07e2-f30f-473b-aa34-e0cef4cc772e/05-distance-field-visualize-mdf.png) |
| Menu to Enable Visualization | Mesh Distance Field Visualization |

Click images for full size.

When you see areas that are more white than gray, it means that many steps were needed to find the intersection of the mesh surface. Rays at grazing angles to surfaces took many more steps to intersect than would have for a simpler mesh.

### Quality

The quality of a Mesh Distance Field representation is controlled by its volume texture resolution. This can be modified using **Distance Field Resolution Scale** in the [Build Settings](/documentation/en-us/unreal-engine/mesh-distance-fields-properties-in-unreal-engine#buildsettings) of the **Static Mesh Editor**.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9567fc66-c5d9-4ed7-88b9-b693db6de4b7/06-distance-field-build-settings.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9567fc66-c5d9-4ed7-88b9-b693db6de4b7/06-distance-field-build-settings.png)

Click image for full size.

The Mesh Distance Field quality will be best for levels that are built out of meshes with similar size, as large meshes tend to create errors. For example, meshes in [Fortnite](https://www.epicgames.com/fortnite) either conform to a grid or are props placed around parts of the level, which gives the best results with few errors. Landscapes are handled separately by [heightfields](/documentation/en-us/unreal-engine/distance-field-ambient-occlusion-in-unreal-engine#landscapes) and are not affected by Distance Field resolution.

|  |  |  |
| --- | --- | --- |
| [undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f6eb0adc-94b5-462a-99a0-ba8dfb3b381e/07-distance-field-mesh.png) | [undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/42a558a5-7895-443d-8b71-7180dda4b3c5/08-distance-field-low-resolution.png) | [undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4f9d690c-59e9-417e-ab3f-35ab6a3b1197/09-distance-field-high-resolution.png) |
| Original Mesh | Resolution is too low, important features are lost | Resolution has been increased, important features represented |

Click images for full size.

The resolution of your Mesh Distance Field should be adjusted enough to capture the important features. As you increase the resolution of the mesh, the memory footprint of the Mesh Distance Field will increase as well. In the Static Mesh Editor, you can see the Mesh Distance Field size listed on the top left of the Viewport.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3c1f3ab9-0f46-46e6-9ef0-2b0dae7581a7/10-distance-field-smeditor-dfsize.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3c1f3ab9-0f46-46e6-9ef0-2b0dae7581a7/10-distance-field-smeditor-dfsize.png)

Click image for full size.

When the Mesh Distance Field is generated, corners are rounded off based on resolution. This can be offset by increasing its resolution, but in most cases, should not be an issue depending on the complexity of the mesh. The maximum size volume texture any single mesh can have is 8 megabytes with a resolution of 128x128x128.

|  |  |  |
| --- | --- | --- |
| Rounded corners based on the resolution 1 | Rounded corners based on the resolution 2 | Rounded corners based on the resolution 3 |

For thin surfaces, they can only be represented with a negative texel inside the mesh, which is necessary for finding its root. Increasing the resolution can capture the larger detail more accurately here, but in cases where you're only using [Distance Field Ambient Occlusion](/documentation/en-us/unreal-engine/distance-field-ambient-occlusion-in-unreal-engine) and the surfaces aren't represented properly. Occlusion further from the surface will be accurate, so it's often not noticeable with sky occlusion.

![Thin serfaces representation with Mesh Distance Field visualization](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8bbec761-8442-4347-aed2-093ee64cc279/14-distance-field-quality-corners-4.png)

### Global Distance Field

The Global Distance Field is a low-resolution Distance Field that uses Signed Distance Fields occlusion in your levels while following the camera. It creates a cache of the per-object Mesh Distance Fields and composites them into a few volume textures centered around the camera, called clipmaps. Only newly visible areas or those affected by the scene modification need to be updated, so composition doesn't cost much.



The lower resolution of the object Distance Field means that it can be used for everything, but when computing cone traces for sky occlusion, they are sampled near the point of being shaded while the Global Distance Field is sampled further away.

You can visualize the Global Distance Field in the viewport by clicking **Show > Visualize > Global Distance Field**.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/73e44d1f-3f19-4f30-b4db-539d9da146ad/15-distance-field-enable-gdf-view-mode.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/73e44d1f-3f19-4f30-b4db-539d9da146ad/15-distance-field-enable-gdf-view-mode.png)

Click image for full size.

Below is a comparison of the per-object Mesh Distance Field visualization in comparison to the Global Distance Field visualization that combines them into clipmaps based on the camera view and distance.

![Mesh Distance Fields Visualization](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f6e2df4f-2a01-49e6-b574-d31dd17b7f73/16-distance-field-mdf-visualization.png)

![Global Distance Fields Visualization](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ddd6a294-ed01-4029-bdb1-bc089b49ae9d/17-distance-field-gdf-visualization.png)

Mesh Distance Fields Visualization

Global Distance Fields Visualization



For more information, visit the [Distance Field Ambient Occlusion](/documentation/en-us/unreal-engine/distance-field-ambient-occlusion-in-unreal-engine) page.

### Foliage

Foliage assets can also leverage the Distance Fields making it possible to have dynamic occlusion or even have distance shadowing beyond what Cascaded Shadow Maps can shadow.

Below are some options you should consider when using any foliage assets in your games to get the most out of performance and quality.

#### Two-Sided Distance Field

For high-density meshes (like trees) where you have surface that are usually made up of a masked material that represents many holes for leaves or branches, these cannot adequately be represented as a solid surface. For this reason, you can enable the [Build Setting](/documentation/en-us/unreal-engine/mesh-distance-fields-properties-in-unreal-engine#buildsettings) for **Two-Sided Distance Field Generation** in the **Static Mesh Editor**. This option will work well for foliage but does come at a higher ray marching cost.

![Enabling the Two-Sided Distance Field](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bd14ec9e-8dda-4df3-854f-3ed8c11e9237/18-distance-field-two-sided-distance-field.png)

Look at the example below. The tree on the left is using a default opaque Mesh Distance Field representation. The one on the right has **Two-Sided Distance Field Generation** enabled. You'll notices that the two-sided mesh distance field is more white than it is gray and the surfaces are now translucent. This means that many more steps were needed to find the intersection of the mesh when generating the volume texture than the opaque one and will come at a higher cost.

|  |  |
| --- | --- |
| [undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/05d6e7c2-e851-4401-9cea-4e3da6f98545/19-distance-field-two-sided-on.png) | [undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/56ca4711-d574-4ffa-ad7d-da058bd59958/20-distance-field-two-sided-off.png) |
| Two-Sided Distance Field Generation Disabled | Two-Sided Distance Field Generation Enabled |

Click images for full size.

#### Foliage Tool Settings

In the [Foliage Tool](/documentation/en-us/unreal-engine/foliage-mode-in-unreal-engine), you must enable each foliage type that you want to use Distance Field lighting features for ambient occlusion and shadowing. By default, this setting is disabled because some foliage assets (like grass) where you would have thousands or tens of thousands of instances would overflow the tile culling buffer. When this happens, you can unsightly artifacts. So, only enable **Affect Distance Field Lighting** for the foliage assets that you need.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ddeddc11-315b-4b48-9655-d0cec44ca593/21-distance-field-foliage-tool-settings.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ddeddc11-315b-4b48-9655-d0cec44ca593/21-distance-field-foliage-tool-settings.png)

Click image for full size.

### Enabling Distance Fields

To enable Mesh Distance Fields for your project, click **Edit** on the **Main** menu and select **Project Settings**.

![Open Project Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6529b812-4f5d-41ee-9ee2-5c900306d76f/22-distance-field-project-settings.png)

Navigate to the **Engine** section and select **Rendering**. Under the **Software Ray Tracing** category, toggle the checkbox next to **Generate Mesh Distance Fields**.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1ca25558-0007-481a-a625-d5765c626692/23-distance-field-enable-generate-mesh.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1ca25558-0007-481a-a625-d5765c626692/23-distance-field-enable-generate-mesh.png)

Click image for full size.

When you enable this, you will be prompted to restart your project.

![Restart Editor to apply new settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ab246222-de06-4b89-8cae-58fa0cfcb4f4/24-distance-field-restarrt-editor-button.png)

Once completed, you can visualize the Mesh Distance Fields in the viewport by clicking **Show** \> **Visualize** \> **Mesh DistanceFields**. You should see a similar view to this.

![Scene View](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/35623ec9-97b1-4a10-a971-b49c054b8a61/25-distance-field-triangle-scene.png)

![Mesh Distance Fields Visualization](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7fe5721e-976e-4262-acf0-4615e556c6e2/26-distance-field-mdf-scene.png)

Scene View

Mesh Distance Fields Visualization

*The entirety of this level is represented by instanced Distance Fields that are stored in volume textures.*

### Limitations

**Limitations of the Distance Fields technique:**

* Support for feature level 5 platforms only (DX-11 and above)
* Only casts shadows from rigid meshes. For Skeletal Meshes, you can use [Capsule Shadows](/documentation/en-us/unreal-engine/capsule-shadows-in-unreal-engine) for indirectly lit areas with Distance Field Ambient Occlusion (DFAO) and soft direct shadowing.
* Materials that deform the mesh through World Position Offset or displacement may cause self-shadowing artifacts, as the Distance Field representation is generated offline and does not know about these deformations.

**Limitations of the current implementation but can be improved in the future:**

* Non-uniform scaling cannot be handled correctly (although, mirroring is ok). Scaling the mesh by two times or less is not generally noticeable.
* Only supports Static Mesh, Instances Static Mesh, Foliage, and Landscape (Heightfield). Foliage must be enabled with **Affect Distance Field Lighting** from the Foliage Tool settings.

**Hardware Limitations:**

* All Mesh Distance Field features have been disabled on Intel cards because the HD 4000 hangs in the RHICreateTexture3D call to allocate the large atlas.

### References

* [Quilez,Inigo. "Raymarching Distance Fields." N.p, 2008](http://iquilezles.org/www/articles/raymarchingdf/raymarchingdf.htm)

## Essentials

[![Using Distance Field Shadows](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1a2d07d0-d0b5-42f6-90ff-8d227c961e64/distancefield_topic.png)

Using Distance Field Shadows

How to setup and use Distance Field Shadowing.](/documentation/en-us/unreal-engine/using-distance-field-shadows-in-unreal-engine)
[![Using Distance Field Ambient Occlusion](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/84aaa4d6-d70e-4779-b660-51cba4d5d6de/dfao_topic.png)

Using Distance Field Ambient Occlusion

How to setup and use Distance Field Ambient Occlusion.](/documentation/en-us/unreal-engine/using-distance-field-ambient-occlusion-in-unreal-engine)
[![Using Distance Field Indirect Shadows](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/93fe11a6-c7d6-4ad9-9a25-b51195413b06/using-dfis-topic.png)

Using Distance Field Indirect Shadows

How to setup and use Distance Field Indirect Shadows.](/documentation/en-us/unreal-engine/using-distance-field-indirect-shadows-in-unreal-engine)
[![Mesh Distance Fields Properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fcebee44-558a-42b1-baeb-7c856b4e111f/mdf-properties-topic.png)

Mesh Distance Fields Properties

A reference page for all the Mesh Distance Field settings that can be found in the Project Settings, Light Components, Static Mesh Editor, and individual Actors.](/documentation/en-us/unreal-engine/mesh-distance-fields-properties-in-unreal-engine)
[![Distance Field Ambient Occlusion](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dfa9bf95-1d0c-4494-a2ee-58c9100778a4/dfao-topic.png)

Distance Field Ambient Occlusion

An overview of using Mesh Distance Fields to create dynamic ambient occlusion for SkyLights.](/documentation/en-us/unreal-engine/distance-field-ambient-occlusion-in-unreal-engine)
[![Distance Field Soft Shadows](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6ffaad43-33bf-45a2-93cd-777fc6fae4bd/dfss-topic.png)

Distance Field Soft Shadows

An overview of using Mesh Distance Fields to create dynamic soft area shadowing.](/documentation/en-us/unreal-engine/distance-field-soft-shadows-in-unreal-engine)

* [static mesh](https://dev.epicgames.com/community/search?query=static%20mesh)
* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [lighting](https://dev.epicgames.com/community/search?query=lighting)
* [shadows](https://dev.epicgames.com/community/search?query=shadows)
* [distance fields](https://dev.epicgames.com/community/search?query=distance%20fields)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [How does it work?](/documentation/en-us/unreal-engine/mesh-distance-fields-in-unreal-engine?application_version=5.7#howdoesitwork?)
* [Scene Representation](/documentation/en-us/unreal-engine/mesh-distance-fields-in-unreal-engine?application_version=5.7#scenerepresentation)
* [Quality](/documentation/en-us/unreal-engine/mesh-distance-fields-in-unreal-engine?application_version=5.7#quality)
* [Global Distance Field](/documentation/en-us/unreal-engine/mesh-distance-fields-in-unreal-engine?application_version=5.7#globaldistancefield)
* [Foliage](/documentation/en-us/unreal-engine/mesh-distance-fields-in-unreal-engine?application_version=5.7#foliage)
* [Two-Sided Distance Field](/documentation/en-us/unreal-engine/mesh-distance-fields-in-unreal-engine?application_version=5.7#two-sideddistancefield)
* [Foliage Tool Settings](/documentation/en-us/unreal-engine/mesh-distance-fields-in-unreal-engine?application_version=5.7#foliagetoolsettings)
* [Enabling Distance Fields](/documentation/en-us/unreal-engine/mesh-distance-fields-in-unreal-engine?application_version=5.7#enablingdistancefields)
* [Limitations](/documentation/en-us/unreal-engine/mesh-distance-fields-in-unreal-engine?application_version=5.7#limitations)
* [References](/documentation/en-us/unreal-engine/mesh-distance-fields-in-unreal-engine?application_version=5.7#references)
* [Essentials](/documentation/en-us/unreal-engine/mesh-distance-fields-in-unreal-engine?application_version=5.7#essentials)
