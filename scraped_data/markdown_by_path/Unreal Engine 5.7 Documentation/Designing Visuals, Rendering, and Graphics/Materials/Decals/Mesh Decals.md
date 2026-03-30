<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-mesh-decals-in-unreal-engine?application_version=5.7 -->

# Mesh Decals

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
7. [Decals](/documentation/en-us/unreal-engine/decals-in-unreal-engine "Decals")
8. Mesh Decals

# Mesh Decals

A guide to working with and using mesh decals in your projects.

![Mesh Decals](https://dev.epicgames.com/community/api/documentation/image/f0147cb0-62ae-4baf-942c-230797ea20f9?resizing_type=fill&width=1920&height=335)

 On this page

Unreal Engine now has support for **Mesh Decals**, enabling you to use the properties of Deferred Decals on separate surface geometry
for added detail to your Static and Skeletal Meshes. Because Deferred Decals rely on projection, you are limited to mostly planar surface
details that shear and distort when not aligned with the surface it's projecting onto. Mesh Decals afford you decals that do not follow a
simple projection and instead can be used with geometry that wraps around edges, being used with spline meshes, ultimately enhancing the
look of your characters.

## Mesh Decal versus Masked Material

Mesh Decals are a mix of translucent blend mode and deferred decals in that they do not render to depth but do update the GBuffer or DBuffer after the opaque geometry has been rendered. In contrast to using a masked Material, there is no cost for EarlyZ pass, you don't get shadows or proper occlusion, but with the trade-off, you get the soft transitions in the Material.

Mesh Decals provide several differences to Deferred Decal Actors that you should be aware of:

* Since large Deferred Decals often do front and back facing draw calls, there are fewer draw calls.
* Since there are fewer pixels covered and flat back facing decals cover 0 pixels, it's quite faster.
* Since you can use a custom UV, You have the ability to do more complex projections.
* You have the ability to have properly normal mapped decals wrapping around surfaces (or stretching along splines).

![ Mesh Decal ](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f5dae4b1-64fe-44d5-be06-b6ba6bfc7ee4/meshdecal.png)

![ Masked Material ](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fe9ca038-2773-47ab-abe3-224a90d99b10/maskedmaterial.png)

Mesh Decal

Masked Material

## Authoring Content

Authoring content for use as Mesh Decal geometry is in line with any model creation. Since this geometry will not rely on projection (like a Deferred Decal Actor), the geometry
needs only to stay in front of the surface you want to affect. With this in mind, the decal geometry should "hug" the underlying surface, but it does not have to match it very closely
because there is already a small depth bias applied to account for this small offset. Also, using a bit of geometry that feathers out from the decal can be good to create the soft transitions
for the decal, which is something you cannot attain with a masked Material.

|  |  |
| --- | --- |
|  |  |
| Base Mesh and Decal Geometry (Isolated) | Composited Mesh |

Another thing to keep in mind when developing your content, is that Mesh Decals can be a challenge with Levels of Detail (LOD), or long view distances when there is limited depth buffer
precision, because geometry will intersect (or not match-up) as intended. However, you can either change the mesh to account for this (in most cases), or you can use **World Position Offset** in
your Material to adjust the offset without having to return to your modeling application.

![Mesh Decal offset](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c78cd3c2-31bf-40ba-b17d-73d6f147dc37/mesh-decal-offset.png)


![ Offset Value: 0 ](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bb88a548-0877-4939-b74f-6a1b3707abb4/2_offset.png)

![ Offset Value: -0.6 ](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/68cc3a71-3705-4389-bbc3-d94c535ed2c6/1_offset.png)

Offset Value: 0

Offset Value: -0.6

In this example, the decal geometry is close enough to the base mesh, such that the depth cannot account for the offset. Using a small negative offset value pushes the geometry out just enough so that it
does not intersect with the underlying geometry.

## Notes

* DBuffer and non-DBuffer use the same container.
* Sort by depth to avoid artifacts when there are many layers overlapping.
* Parallel Rendering isn't yet hooked up. There are some CPU savings if this feature is used extensively.

## Limitations

* Material Editor Preview is not visible.
* There is no artist specified sort order.
* Tangent Space support is not yet implemented.
* Shader Overdraw/Overdraw functionality is missing.
* Since it assumes base pass usage, the Material Editor does not currently show the correct instructions count.
* There is no easily adjustable DepthBias. Currently, you have to use an offset in the mesh from the surface it's above, or control with World Position Offset in the Material.

* [materials](https://dev.epicgames.com/community/search?query=materials)
* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [lighting](https://dev.epicgames.com/community/search?query=lighting)
* [decals](https://dev.epicgames.com/community/search?query=decals)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Mesh Decal versus Masked Material](/documentation/en-us/unreal-engine/using-mesh-decals-in-unreal-engine?application_version=5.7#meshdecalversusmaskedmaterial)
* [Authoring Content](/documentation/en-us/unreal-engine/using-mesh-decals-in-unreal-engine?application_version=5.7#authoringcontent)
* [Notes](/documentation/en-us/unreal-engine/using-mesh-decals-in-unreal-engine?application_version=5.7#notes)
* [Limitations](/documentation/en-us/unreal-engine/using-mesh-decals-in-unreal-engine?application_version=5.7#limitations)
