<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-lighting-channels-in-unreal-engine?application_version=5.7 -->

# Lighting Channels

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
7. [Direct Lighting](/documentation/en-us/unreal-engine/features-and-properties-of-lights-in-unreal-engine "Direct Lighting")
8. Lighting Channels

# Lighting Channels

An overview of using channels of a light source to light specific surfaces.

![Lighting Channels](https://dev.epicgames.com/community/api/documentation/image/082ef797-2cd9-4e3a-b093-22c6c403ebea?resizing_type=fill&width=1920&height=335)

 On this page

![Banner image](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/53aaee60-180c-4e05-90aa-068780f03834/using-lightning-channels-banner.png)

**Lighting Channels** allow dynamic lights to only affect objects when their lighting channels overlap. This is primarily intended for cinematic use to give users powerful control over how **Actors** are lit. At the moment, **Unreal Engine** supports up to 3 lighting channels.

## Usage

By default, Directional Lights, Spot Lights, Point Lights, and all Actors that can be affected by lights (Static Meshes, Skeletal Meshes, etc.) have **Lighting Channel 0** enabled. If you would like a lightable **Actor** to be affected by another **Lighting Channel**, you must enable that channel on both the Actor and the light.

### Example

![Example of using Lightning Channels](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bc4db559-b3f1-4d1b-9829-decc684974e9/01-using-lightning-channels-example.png)

In the above image, the white Directional Light can only affect **Channel 0**, which includes the mannequin on the left and the background Static Meshes, while the purple Point Light can only affect **Channel 1**, which only includes the mannequin on the right.

You can see how the properties are set here:

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c2564571-3b0d-4ec4-9ae4-9a9db863f325/02-using-lightning-channels-properties.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c2564571-3b0d-4ec4-9ae4-9a9db863f325/02-using-lightning-channels-properties.png)

Click for full image.

For lights, the property can be found in the **Advanced** pulldown menu of the **Light** category in the **Details** panel. For Actors that can be lit, you can find the **Lighting Channels** properties in the **Lighting** category of the **Details** panel.

## Limitations

Lighting channel influence is applied dynamically. This means it won't work with Static Lights or Static Mesh Actors with Static Mobility. Static Mesh Actors with **Mobility** set to **Movable** do work, however. You'll need to use either **Stationary** or **Movable** lights.

Lighting channels will only affect direct lighting on opaque materials. So, translucent or masked materials will not work.

## Performance

The performance impact of using **Lighting Channels** is minimal, but also non-zero. In a scene with 1 directional light, Radeon 7870, at 1080p for example:

| Lighting Channels Satus | Time in ms |
| --- | --- |
| **off** | 0.42ms StandardDeferredLighting 1 draws 1 prims 3 verts |
| **on** | 0.08ms CopyStencilToLightingChannels 1 draws 1 prims 3 verts  0.45ms StandardDeferredLighting 1 draws 1 prims 3 verts |

## On Mobile

As of Unreal Engine 4.13, Lighting Channels works on mobile renderers with the following features supported:

* Multiple directional lights are supported in different channels.
* Each primitives can only be affected by one directional, and it will use the directional light from first lighting channel it has set.
* CSM shadows from stationary or movable directional lights cast only on primitives with matching lighting channels.
* Dynamic point lights fully support lighting channels.

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [lighting](https://dev.epicgames.com/community/search?query=lighting)
* [shadows](https://dev.epicgames.com/community/search?query=shadows)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Usage](/documentation/en-us/unreal-engine/using-lighting-channels-in-unreal-engine?application_version=5.7#usage)
* [Example](/documentation/en-us/unreal-engine/using-lighting-channels-in-unreal-engine?application_version=5.7#example)
* [Limitations](/documentation/en-us/unreal-engine/using-lighting-channels-in-unreal-engine?application_version=5.7#limitations)
* [Performance](/documentation/en-us/unreal-engine/using-lighting-channels-in-unreal-engine?application_version=5.7#performance)
* [On Mobile](/documentation/en-us/unreal-engine/using-lighting-channels-in-unreal-engine?application_version=5.7#onmobile)
