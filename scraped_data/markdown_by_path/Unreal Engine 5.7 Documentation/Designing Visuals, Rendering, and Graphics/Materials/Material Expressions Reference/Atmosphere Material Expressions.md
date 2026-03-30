<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/atmosphere-material-expressions-in-unreal-engine?application_version=5.7 -->

# Atmosphere Material Expressions

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
7. [Material Expressions Reference](/documentation/en-us/unreal-engine/unreal-engine-material-expressions-reference "Material Expressions Reference")
8. Atmosphere Material Expressions

# Atmosphere Material Expressions

Material Expressions that affect fog and other atmospheric level effects.

![Atmosphere Material Expressions](https://dev.epicgames.com/community/api/documentation/image/51fe2427-93f8-43ff-8a48-7ce272418733?resizing_type=fill&width=1920&height=335)

Learn to use this **Deprecated** feature, but use caution when shipping with it.

 On this page

## Atmospheric Fog Color

The **Atmospheric Fog Color** Material Expression allows you to query the current color of the level's Atmospheric Fog, at any position in World Space. If no World Position is fed into it, then the world position of the pixel in question is used. This is useful when you need Materials to appear to fade into a distant fog color.

In the example below, The Base Color is being set using an Atmospheric Fog node, with the World Position receiving a simple network that queries the location that is always 50,000 units behind the object, relative to the position of the camera.

![Atmosphere Material Expression](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/abe78613-131f-4f8d-b341-28c1f270956c/atmosphere-material-expression.png)


The Atmospheric Fog Color Material Expression is deprecated in Unreal Engine 5, and should not be used. Instead, you should use the **Sky Atmosphere Component**, which is [documented on this page](/documentation/en-us/unreal-engine/sky-atmosphere-component-in-unreal-engine). You may also want to consider using [Volumetric Fog](/documentation/en-us/unreal-engine/volumetric-fog-in-unreal-engine).

* [materials](https://dev.epicgames.com/community/search?query=materials)
* [shaders](https://dev.epicgames.com/community/search?query=shaders)
* [deprecated](https://dev.epicgames.com/community/search?query=deprecated)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Atmospheric Fog Color](/documentation/en-us/unreal-engine/atmosphere-material-expressions-in-unreal-engine?application_version=5.7#atmosphericfogcolor)
