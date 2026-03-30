<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/subsurface-shading-model-in-unreal-engine?application_version=5.7 -->

# Subsurface Shading Model

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
7. [Material Properties](/documentation/en-us/unreal-engine/unreal-engine-material-properties "Material Properties")
8. [Shading Models](/documentation/en-us/unreal-engine/shading-models-in-unreal-engine "Shading Models")
9. Subsurface Shading Model

# Subsurface Shading Model

Description and technical details of the subsurface shading model available in Materials.

![Subsurface Shading Model](https://dev.epicgames.com/community/api/documentation/image/31ec3a36-10e4-4cf0-ba37-f82933b26596?resizing_type=fill&width=1920&height=335)

 On this page

Materials have a new subsurface shading model (***MLM\_Subsurface***) which is intended for materials like wax or jade which appear opaque, but lighting scatters inside them allowing a portion of the light from the opposite side of the surface to show through.

![Jade Material](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ae625672-2cc4-475e-9983-fb20d846ae94/jade_statue.jpg) ![Ice Material](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a5d5c785-09e8-4aaa-aeef-1d57c38365fa/ice_mounds.jpg)

Subsurface scattering (SSS) is often used for creating realistic skin for humans or other creatures; however, the effect from this shading model is lower quality and cheaper than what would generally be used for skin rendering.

## Technical Details

The two components of subsurface lighting are a wrap-around `N dot H` term and a light backscattering term, which shows up when the light is on the other side of an SSS object. Both of these are masked by translucent self shadowing from exponential shadow maps.

## Material Input Channels

The SubsurfaceColor input channel defines the color inside the material which affects SSS lighting.

The Opacity channel of the material takes on a slightly different meaning when the material is using subsurface scattering and the *MLM\_Subsurface* shading model. Since these types of surfaces are completely opaque, the Opacity, in this case, controls how dense the material is when it scatters light as well as:

* How much the normal affects the subsurface lighting, a more opaque material gets more normal influence.
* How far lighting makes it through the material due to self-shadowing, a smaller opacity causes light to travel further.
* How soft the shadow is on the material, a smaller opacity results in softer shadows, but softness is clamped.

Be sure to set the Opacity for any subsurface materials to a reasonable value, e.g. 0.1. The default opacity is 1, which does not produce a very convincing subsurface-type effect.

## Limitations

Additionally there are some limitations with the current implementation:

* Point light shadowing not yet supported.
* Cascaded Shadow Map seams.
* SSS materials can still receive leaked lighting through fully opaque materials if they are close enough to the shadow caster.
* Soft shadows from low opacity are limited in how soft they can be and have aliasing.

* [materials](https://dev.epicgames.com/community/search?query=materials)
* [shaders](https://dev.epicgames.com/community/search?query=shaders)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Technical Details](/documentation/en-us/unreal-engine/subsurface-shading-model-in-unreal-engine?application_version=5.7#technicaldetails)
* [Material Input Channels](/documentation/en-us/unreal-engine/subsurface-shading-model-in-unreal-engine?application_version=5.7#materialinputchannels)
* [Limitations](/documentation/en-us/unreal-engine/subsurface-shading-model-in-unreal-engine?application_version=5.7#limitations)
