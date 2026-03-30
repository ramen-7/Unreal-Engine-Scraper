<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-scene-variants-in-unreal-engine?application_version=5.7 -->

# Working with Scene Variants

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
5. [Working with Content](/documentation/en-us/unreal-engine/working-with-content-in-unreal-engine "Working with Content")
6. Working with Scene Variants

# Working with Scene Variants

The Variant Manager can help you switch between different representations of your scene.

![Working with Scene Variants](https://dev.epicgames.com/community/api/documentation/image/fdd60faf-8d67-471d-9d5c-6fe9e3d253fa?resizing_type=fill&width=1920&height=335)

 On this page

When you create realtime 3D experiences around design data, you often need to switch the objects in your scene from one state to another. This may mean swapping objects' positions and rotations in 3D space from one place to another, showing and hiding specific objects, changing Materials, turning lights on and off, and so on.

This is a particularly common need in mechanical and industrial design applications, where some industry-standard modeling and scene design tools allow you to set up multiple *variants* to represent different versions of your scene. This is sometimes referred to as *150% BOM* (Bill of Materials), meaning that the scene contains more than 100% of the visible options.

The classic example is a configurator that lets clients choose in advance between different possible options for an expensive vehicle such as a car, motorcycle, or aircraft, before the vehicle is actually assembled or manufactured. The simple example in the video below shows a car configurator that offers multiple options for items such as wheel trims, brake calipers, and body paint colors.

To help you handle these kinds of scenarios in your own visualization projects, Unreal Engine offers a helper called the **Variant Manager**. The Variant Manager makes it easier to set up multiple variants of your scene and to switch between these variants—both in the editor and at runtime. For example, in the sample application shown above, the Variant Manager is set up with each available option. A simple on-screen UMG UI calls Blueprint functions exposed by the Variant Manager to activate those options on demand.

The topics in this section describe what the Variant Manager is and how you can use it to produce similar effects.

## Getting Started

[![Variant Manager Template Overview](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8ccbe830-bcba-441b-a5b6-dbfda26c0617/topic-image.png)

Variant Manager Template Overview

What the Variant Manager is and how it works.](/documentation/en-us/unreal-engine/variant-manager-template-overview)

## Tutorials

[![Calling Functions on Variant Activation](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/374a8f08-b986-4fd5-a0fa-61c2cf0ff6d5/topic-image.png)

Calling Functions on Variant Activation

When you activate a Variant, call a function instead of changing a property value.](/documentation/en-us/unreal-engine/calling-functions-on-variant-activation)
[![Scripting the Variant Manager Setup](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8d1812a6-9282-4f85-b9f7-75052710305d/placeholder_topic.png)

Scripting the Variant Manager Setup

Use Editor Scripting to set up the Variant Manager with all your scene variants.](/documentation/en-us/unreal-engine/scripting-the-variant-manager-setup)
[![Product Configurator Template](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/832c48e6-02ed-4bb7-91fc-11777ed0de5b/topic-image.png)

Product Configurator Template

How to customize and use the Product Configurator template](/documentation/en-us/unreal-engine/product-configurator-template-in-unreal-engine)

## Credits

The car model used on this page is courtesy of [Allegorithmic](https://www.substance3d.com/).

* [datasmith](https://dev.epicgames.com/community/search?query=datasmith)
* [enterprise](https://dev.epicgames.com/community/search?query=enterprise)
* [manufacturing](https://dev.epicgames.com/community/search?query=manufacturing)
* [variants](https://dev.epicgames.com/community/search?query=variants)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Getting Started](/documentation/en-us/unreal-engine/working-with-scene-variants-in-unreal-engine?application_version=5.7#gettingstarted)
* [Tutorials](/documentation/en-us/unreal-engine/working-with-scene-variants-in-unreal-engine?application_version=5.7#tutorials)
* [Credits](/documentation/en-us/unreal-engine/working-with-scene-variants-in-unreal-engine?application_version=5.7#credits)
