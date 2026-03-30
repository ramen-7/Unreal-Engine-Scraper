<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/material-functions-in-unreal-engine?application_version=5.7 -->

# Material Functions

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
7. Material Functions

# Material Functions

Snippets of Material that you can save in packages and reuse across multiple Materials.

![Material Functions](https://dev.epicgames.com/community/api/documentation/image/64856363-c991-47aa-a0ef-94455cd719f8?resizing_type=fill&width=1920&height=335)

 On this page

**Material Functions** let you package parts of a Material graph into a reusable asset that you can share to a library and easily insert into other Materials. Their purpose is to streamline Material creation by giving instant access to commonly used networks of Material nodes. Material Functions allow you to abstract complex Material logic into a single node, making Material creation easier for artists.

A secondary benefit of Material Functions is that edits to a single function propagate throughout all Material networks which use it. So if you need to make a fix or change how a Material Function works, you will not have to make further edits to the many Materials which may be using that function. These two pages provide information about how to create and use Material Functions in Unreal Engine.

[![Material Functions Overview](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ac946896-ff66-4fb9-a2c0-35077f6f1964/material-functions-overview-topic.png)

Material Functions Overview

An overview of how Material functions work and some critical concepts for their use.](/documentation/en-us/unreal-engine/unreal-engine-material-functions-overview)

[![Creating and Using Material Functions](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/74015811-0626-41ef-8717-042b3f8d4801/creating-material-functions-topic.png)

Creating and Using Material Functions

A guide to the process of creating and using Material Functions.](/documentation/en-us/unreal-engine/creating-and-using-material-functions-in-unreal-engine)

## Functions Reference

The reference pages below provide information and usage examples for all the default Material Functions included with Unreal Engine. These are organized according to the categories in the [Material Editor](/documentation/en-us/unreal-engine/unreal-engine-material-editor-ui) palette.

[![Blend Material Functions](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/41456552-daad-4f53-ac77-b013ae52ea7b/blends.png)

Blend Material Functions

Functions designed to blend one color with another, similar to blend modes in popular image editing applications.](/documentation/en-us/unreal-engine/blend-material-functions-in-unreal-engine)
[![Gradient Material Functions](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/12288205-2a7a-49e4-9b1a-4dd2ea4fabd8/gradients.png)

Gradient Material Functions

Procedurally generated gradients to add to your materials, eliminating the need for textures and saving memory.](/documentation/en-us/unreal-engine/gradient-material-functions-in-unreal-engine)
[![Image Adjustment Material Functions](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e9333a26-35c9-486a-a6ce-f4636fe01390/imageadjustment.png)

Image Adjustment Material Functions

Functions for making adjustments to existing image textures, such as shifting contrast or hue.](/documentation/en-us/unreal-engine/image-adjustment-material-functions-in-unreal-engine)
[![Math Material Functions](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c9df8816-3eae-4ec1-a533-32526918c2eb/math.png)

Math Material Functions

Material Functions which perform preconfigured mathematical operations such as the calculation of pi, addition of vector components, and others.](/documentation/en-us/unreal-engine/math-material-functions-in-unreal-engine)
[![Misc Material Functions](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/152a987c-1ce4-424f-b842-a6a10d4cb809/misc.png)

Misc Material Functions

Misc Material Functions that do not fall into existing categories.](/documentation/en-us/unreal-engine/misc-material-functions-in-unreal-engine)
[![Opacity Material Functions](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a0aaec90-ce2a-4281-ad81-f209c7f333a2/opacity.png)

Opacity Material Functions

Functions to handle opacity values within a Material network.](/documentation/en-us/unreal-engine/opacity-material-functions-in-unreal-engine)
[![Particles Material Functions](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4ce80724-93ac-4115-bfb7-cd7ac8d179ba/particles.png)

Particles Material Functions

Specialized functions designed to aid setting up the look of complex particle networks.](/documentation/en-us/unreal-engine/particles-material-functions-in-unreal-engine)
[![Procedurals Material Functions](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e447e58c-fcda-4831-80e1-d4351e102f39/procedurals.png)

Procedurals Material Functions

Procedurally generated textures and operations, such as the creation of normal maps from existing height maps.](/documentation/en-us/unreal-engine/procedurals-material-functions-in-unreal-engine)
[![Reflections Material Functions](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2c7ad8aa-deaf-455f-b23d-7117e19fe9b3/reflections.png)

Reflections Material Functions

Functions for aiding in the calculation of values for a variety of reflection types.](/documentation/en-us/unreal-engine/reflections-material-functions-in-unreal-engine)
[![Shading Material Functions](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1617633e-8529-4a2c-b2d8-34882967425a/shading.png)

Shading Material Functions

Functions for handling special shading types, such as Fuzzy Shading networks.](/documentation/en-us/unreal-engine/shading-material-functions-in-unreal-engine)
[![Texturing Material Functions](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6c9a0d63-d70f-4b76-85a4-ce4d3d191f3e/texturing.png)

Texturing Material Functions

A wide variety of functions designed to aid in working with textures, such as reprojecting UVs, cropping, and many more.](/documentation/en-us/unreal-engine/texturing-material-functions-in-unreal-engine)
[![Vector Ops Material Functions](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6b2499ae-1682-4591-8a82-31b8a7672a92/vectorops.png)

Vector Ops Material Functions

Functions built to handle vector mathematics, such as calculating a Fresnel effect.](/documentation/en-us/unreal-engine/vector-ops-material-functions-in-unreal-engine)
[![World Position Offset Material Functions](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c5f0508c-2ce0-493e-8e7b-b91f860033a6/worldpositionoffset.png)

World Position Offset Material Functions

Functions for handling vertex manipulation using world position offset.](/documentation/en-us/unreal-engine/world-position-offset-material-functions-in-unreal-engine)

* [materials](https://dev.epicgames.com/community/search?query=materials)
* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [shaders](https://dev.epicgames.com/community/search?query=shaders)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Functions Reference](/documentation/en-us/unreal-engine/material-functions-in-unreal-engine?application_version=5.7#functionsreference)
