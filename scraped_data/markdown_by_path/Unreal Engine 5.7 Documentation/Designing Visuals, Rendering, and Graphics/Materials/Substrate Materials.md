<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/substrate-materials-in-unreal-engine?application_version=5.7 -->

# Substrate Materials

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
7. Substrate Materials

# Substrate Materials

Topics and reference about using the Substrate Materials framework.

![Substrate Materials](https://dev.epicgames.com/community/api/documentation/image/7b63b9f8-976b-4b9d-ad16-0ffb2b218203?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

**Substrate** is Unreal Engine 5's approach to authoring materials, which replaces the fixed suite of shading models and blend modes, such as Default Lit and Clear Coat, with a more expressive and modular framework.

## Getting Started

* [![Substrate Materials Overview](https://dev.epicgames.com/community/api/documentation/image/ea20099f-08b2-41d2-89af-3cf14ae81482?resizing_type=fit&width=640&height=640)

  Substrate Materials Overview

  An overview of the Substrate Materials framework for principled BSDF-based material authoring.](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine)

## Programmer Guides

* [![Programming with Substrate GBuffer Formats](images/static/document_list/empty_thumbnail.svg)

  Programming with Substrate GBuffer Formats

  An overview for programmers using Substrates GBuffer formats in their shader code.](https://dev.epicgames.com/documentation/en-us/unreal-engine/programming-with-substrate-gbuffer-formats)

## Developer's Blog

Epic Staff-created information and tutorials in the Epic Developer Community (EDC).

* **A Deep Dive on Substrate Materials**

  + [Theory behind F0, F90, and Specular Color](https://dev.epicgames.com/community/learning/courses/Emv/unreal-engine-a-deep-dive-on-substrate-materials/qEOY/unreal-engine-theory-behind-f0-f90-and-specular-color)
  + Simple Dielectric Materials in Substrate

    - [Example 1: Simple Dielectric](https://dev.epicgames.com/community/learning/courses/Emv/unreal-engine-a-deep-dive-on-substrate-materials/mmZL/unreal-engine-example-1-simple-dielectric)
  + Gemstones, Metalloids, and Semiconductors

    - [Example 2: Pure Carbon](https://dev.epicgames.com/community/learning/courses/Emv/unreal-engine-a-deep-dive-on-substrate-materials/Kx6r/unreal-engine-example-2-pure-carbon)
  + Conductors - From Simple to Complex

    - [Example 3: Pure Copper](https://dev.epicgames.com/community/learning/courses/Emv/unreal-engine-a-deep-dive-on-substrate-materials/98nE/unreal-engine-example-3-pure-copper)
  + How to find an Appropriate Reflectance for a Material

    - [Interlude: How to find an Appropriate F0](https://dev.epicgames.com/community/learning/courses/Emv/unreal-engine-a-deep-dive-on-substrate-materials/l526/unreal-engine-interlude-how-to-find-an-appropriate-f0)
  + Thin Film Interference and Secondary Roughness

    - [Example 4: Thin Film Interference and Secondary Roughness](https://dev.epicgames.com/community/learning/courses/Emv/unreal-engine-a-deep-dive-on-substrate-materials/EvGj/unreal-engine-example-4-thin-film-interference-and-secondary-roughness)
  + A Quick Overview of Mean Free Path

    - [Interlude: An Aside on Mean Free Path (MFP)](https://dev.epicgames.com/community/learning/courses/Emv/unreal-engine-a-deep-dive-on-substrate-materials/v7EW/unreal-engine-interlude-an-aside-on-mean-free-path-mfp)
  + BSDF Layering and Substrate Operators

    - [Example 5: BSDF Layering and Substrate Operators](https://dev.epicgames.com/community/learning/courses/Emv/unreal-engine-a-deep-dive-on-substrate-materials/Ox23/unreal-engine-example-5-bsdf-layering-and-substrate-operators)
  + Metallic Representation and Interpolation

    - [Interlude: Metallic Representation and Interpolation](https://dev.epicgames.com/community/learning/courses/Emv/unreal-engine-a-deep-dive-on-substrate-materials/6vxD/unreal-engine-interlude-metallic-representation-and-interpolation)
  + Fuzzy Shading in Substrate

    - [Interlude on Fuzz on the Substrate Slab](https://dev.epicgames.com/community/learning/courses/Emv/unreal-engine-a-deep-dive-on-substrate-materials/nKlO/unreal-engine-interlude-fuzz-on-the-substrate-slab)
  + Example Material Final Details

    - [Example 6: Copper - Finishing Touches and Final Details](https://dev.epicgames.com/community/learning/courses/Emv/unreal-engine-a-deep-dive-on-substrate-materials/B9Xy/unreal-engine-example-6-copper-finishing-touches-and-final-details)

* [materials](https://dev.epicgames.com/community/search?query=materials)
* [beta](https://dev.epicgames.com/community/search?query=beta)
* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [shaders](https://dev.epicgames.com/community/search?query=shaders)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Getting Started](/documentation/en-us/unreal-engine/substrate-materials-in-unreal-engine?application_version=5.7#getting-started)
* [Programmer Guides](/documentation/en-us/unreal-engine/substrate-materials-in-unreal-engine?application_version=5.7#programmerguides)
* [Developer's Blog](/documentation/en-us/unreal-engine/substrate-materials-in-unreal-engine?application_version=5.7#developer'sblog)
