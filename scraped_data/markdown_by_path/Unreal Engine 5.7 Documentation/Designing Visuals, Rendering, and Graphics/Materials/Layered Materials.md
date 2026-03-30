<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/layering-materials-in-unreal-engine?application_version=5.7 -->

# Layered Materials

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
7. Layered Materials

# Layered Materials

Two methods for layering Materials to create complex, unique surfaces.

![Layered Materials](https://dev.epicgames.com/community/api/documentation/image/8dfdd0d7-3fa4-408e-8634-ba22650dfe1f?resizing_type=fill&width=1920&height=335)

 On this page

Unreal Engine provides two main ways to layer your Materials and create complex blends between unique surface types. These workflows give you a way to apply distinct Material properties to different regions of a single mesh. While you could achieve similar results in a regular Material using texture masks and other per-pixel logic, the two systems documented here produce easier to read Material graphs and a more artist-friendly editing workflow when changes to the Material are needed.

The two workflows for layering Materials are listed below.

* **Layered Materials** as an extension of the Material Functions system.
* **Material Layers** as implemented in the Material Instance Editor.

## Layering Materials with Material Functions

This approach to layering Materials works as an extension of the [Material Functions](/documentation/en-us/unreal-engine/unreal-engine-material-functions-overview) system. Each Material type you wish to use as a layer is fully defined within its own Material Function using the [Material Attributes](/documentation/en-us/unreal-engine/material-attributes-expressions-in-unreal-engine) expressions. You then create a base Material which contains all the logic needed to blend between your various layers. Read the two pages below to learn how to use this workflow.

[![Layered Materials Overview](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3d5898bc-74fb-4f26-af0f-5696f42964f2/layeredmaterialstopic.png)

Layered Materials Overview

An introductory document on using Material Functions to create complex layered Materials.](/documentation/en-us/unreal-engine/layered-materials-in-unreal-engine)
%designing-visuals-rendering-and-graphics/materials/layered-materials/creating-layered-materials:topic%

## Material Layers

The [Material Layers](/documentation/en-us/unreal-engine/using-material-layers-in-unreal-engine) system makes it easier to edit layered Materials by providing a user-inteface tab in the [Material Instance Editor](/documentation/en-us/unreal-engine/unreal-engine-material-instance-editor-ui). This **Layer Parameters** tab allows artists intuitively swap layers in and out of a Material Instance, change the order of the layer stack, and modify the way layers are blended without ever editing the node graph in the base Material.

While the Layered Material Functions workflow documented above is still a valid approach, the **Material Layers** system typically provides a faster and more iterative user experience for artists and designers who may not have the technical background needed to edit the node graph. Learn how to use Material Layers below.

[![Using Material Layers](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d1d4b65f-f44a-4dc3-bfcc-cc9bd056b87f/material-layers-topic.png)

Using Material Layers

Build complex layered and blended Materials that take advantage of Material instancing.](/documentation/en-us/unreal-engine/using-material-layers-in-unreal-engine)

* [materials](https://dev.epicgames.com/community/search?query=materials)
* [shaders](https://dev.epicgames.com/community/search?query=shaders)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Layering Materials with Material Functions](/documentation/en-us/unreal-engine/layering-materials-in-unreal-engine?application_version=5.7#layeringmaterialswithmaterialfunctions)
* [Material Layers](/documentation/en-us/unreal-engine/layering-materials-in-unreal-engine?application_version=5.7#materiallayers)
