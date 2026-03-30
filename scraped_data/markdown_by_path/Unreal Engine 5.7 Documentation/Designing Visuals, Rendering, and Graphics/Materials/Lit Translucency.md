<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/lit-translucency-in-unreal-engine?application_version=5.7 -->

# Lit Translucency

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
7. Lit Translucency

# Lit Translucency

Explanation of how translucent surfaces are lit and cast shadows including self-shadows.

![Lit Translucency](https://dev.epicgames.com/community/api/documentation/image/645bf258-187f-4e01-b30c-72f150a46940?resizing_type=fill&width=1920&height=335)

 On this page

Translucent effects generally fall into a few categories: volumetric, volumetric but dense enough to have normal information, and surfaces. Different lighting techniques are needed for each of these, so a material must specify the Translucency Lighting Mode that should be used.

Lit translucency gets most of its lighting through a series of cascaded volume textures oriented around the view frustum. This allows lighting to be known in a single forward pass for any point inside the volumes, but has the downside that the volume texture is fairly low resolution, and can only cover a limited depth range from the viewer.

The volume is configured through cvars that can be set differently based on the scalability level:

* r.TranslucencyLightingVolumeDim, which defaults to 64. Raising this by a factor of 2 increases the cost to light volume by a factor of 8.
* r.TranslucencyLightingVolumeInnerDistance, which defaults to 1500. Raising this increases lighting volume coverage but reduces effective resolution.
* r.TranslucencyLightingVolumeOuterDistance, which defaults to 5000. Raising this increases lighting volume coverage but reduces effective resolution.

Shadowed direct lighting from all movable light types is injected into the translucency lighting volume. Light functions are also taken into account.

![Lit Translucency](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/406563fd-c49a-44e2-9980-d8b746ed06da/3litsnow4.png)

Translucent materials receive diffuse GI from the [Indirect Lighting Cache](/documentation/en-us/unreal-engine/indirect-lighting-cache-in-unreal-engine). Only one lighting sample is interpolated, at the center of the object's bounds. There is only one sample taken for the whole object, even if it is a large particle system. The indirect lighting interpolates over time if the bounds center changes, so it does not pop.

![Lit translucent spheres](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5231028e-5b1c-42e2-8ed7-d10d9201e41c/littrans_idlc_spheres.png)

*The left sphere is lit translucency using the Indirect Lighting Cache, the right sphere is opaque with baked lighting from Lightmass.*

## Volumetric effects

### Casting Shadows & Self-Shadowing

Translucency can cast shadows onto the opaque world and onto itself and other lit translucency Actors. This is implemented with Fourier Opacity maps, which do a great job for shadowing from blobby volumes, but have severe ringing artifacts with more opaque translucent surfaces. Translucency self shadowing goes through the lighting volume for point and spot lights, so it is often not visible due to low resolution unless the effect is very large and dense. Directional lights however do translucent self shadowing per-pixel, and get much higher quality. Directional lights also have subsurface shading for lit materials using the subsurface shading model.

Translucent self-shadowing uses per-object shadows, which means that it needs user specified fixed particle system bounds and they need to be correct. The easiest way to set this up is to author your particle movement, then **right-click** on the 'show bounds' button on the Cascade toolbar, which will pop up a dialog that allows you to generate fixed bounds. Very large self-shadowing particle systems will get reduced shadowmap resolution, since the shadowmap is stretched to cover the system bounds. Verify that your bounds are reasonable by enabling Show Bounds, which can be found under Show -> Advanced -> Bounds. Then select the emitter in the editor and it will draw the bounding box and sphere.

|  |  |
| --- | --- |
| Translucent Particle Self-Shadowing | Translucent Particle Self-Shadowing |

### Static shadowing

Translucency can receive static shadowing from [stationary lights](/documentation/en-us/unreal-engine/stationary-light-mobility-in-unreal-engine) through a special static shadow depth map generated by Lightmass at lighting build time.

## Translucent Surfaces

### Reflection Captures

TLM\_Surface materials receive image based reflections (specular GI) from the reflection captures placed in the level. Unlike opaque materials, only one reflection capture's cubemap is applied (no blending) which currently causes a pop if the object moves closer to another reflection capture. The cubemap is also applied as if it lies at infinity, instead of nearby, which can cause artifacts on large flat surfaces.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8bef7b2b-2800-4f6a-bc2d-a85251073078/littrans_reflspheres.png)

*The left sphere is translucent, the right is opaque, and they are both setup as metals, which means 100% of the lighting comes from specular.*

### Per-Pixel Translucent Lighting

In the deferred renderer, the Forward Shading functionality can be used on translucent surfaces to get specular highlights from multiple lights and image-based reflections from parallax-corrected reflection captures.

To enable Per-Pixel Translucent Lighting set the Lighting Mode to **Surface ForwardShading** and then make sure that **Screen Space Reflections** are enabled.

![Per pixel translucency settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3ea76a94-cedd-4542-91f1-ec98d2731ec7/lit-translucency-properties.png)

### Thin Translucency

The **Thin Translucent** Shading Model and its material output expression enables you to accurately represent physically based transparent materials, such as tinted or colored transparent materials that accurately respond to lighting and shading. The transparent material is able to display white specular highlights and properly tint the background in a single pass.

![Standard Translucent Shading Model](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1cdc6223-4248-4429-bca3-96b81b4260d8/transparency.png)

![Thin Translucent Shading Model](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/aaf325b2-e5c5-4994-8950-c82fcc442cb9/thintransparency.png)

Standard Translucent Shading Model

Thin Translucent Shading Model

Enable Thin Transparency output in your materials by setting the following in the Material Details panel:

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/30cf5bea-1073-4e0d-bb00-c5f3ae574f60/lit-translucency-graph.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/30cf5bea-1073-4e0d-bb00-c5f3ae574f60/lit-translucency-graph.png)

Click image for full size.

* **Blend Mode:** Translucent
* **Shading Model:** Thin Translucent
* **Lighting Mode:** Surface ForwardShading

In the Material Graph, you'll want to use the **Thin Translucent Material** output expression node to control the color transmittance of the transparency.

## Limitations

* Lit translucent surfaces are missing direct specular.
* Lit translucent surfaces get all their direct lighting through the translucency volume lighting texture, which causes them to be lower resolution than needed for most surface materials (glass, water).

* [materials](https://dev.epicgames.com/community/search?query=materials)
* [shaders](https://dev.epicgames.com/community/search?query=shaders)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Volumetric effects](/documentation/en-us/unreal-engine/lit-translucency-in-unreal-engine?application_version=5.7#volumetriceffects)
* [Casting Shadows & Self-Shadowing](/documentation/en-us/unreal-engine/lit-translucency-in-unreal-engine?application_version=5.7#castingshadows&self-shadowing)
* [Static shadowing](/documentation/en-us/unreal-engine/lit-translucency-in-unreal-engine?application_version=5.7#staticshadowing)
* [Translucent Surfaces](/documentation/en-us/unreal-engine/lit-translucency-in-unreal-engine?application_version=5.7#translucentsurfaces)
* [Reflection Captures](/documentation/en-us/unreal-engine/lit-translucency-in-unreal-engine?application_version=5.7#reflectioncaptures)
* [Per-Pixel Translucent Lighting](/documentation/en-us/unreal-engine/lit-translucency-in-unreal-engine?application_version=5.7#per-pixeltranslucentlighting)
* [Thin Translucency](/documentation/en-us/unreal-engine/lit-translucency-in-unreal-engine?application_version=5.7#thintranslucency)
* [Limitations](/documentation/en-us/unreal-engine/lit-translucency-in-unreal-engine?application_version=5.7#limitations)
