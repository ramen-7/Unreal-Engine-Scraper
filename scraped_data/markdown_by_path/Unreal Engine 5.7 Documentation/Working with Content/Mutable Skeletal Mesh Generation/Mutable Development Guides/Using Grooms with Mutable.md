<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-grooms-with-mutable-in-unreal-engine?application_version=5.7 -->

# Using Grooms with Mutable

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
4. Using Grooms with Mutable

# Using Grooms with Mutable

A guide to using Grooms with Mutable

![Using Grooms with Mutable](https://dev.epicgames.com/community/api/documentation/image/af8466b1-c839-448f-80c1-16c7e3330fe6?resizing_type=fill&width=1920&height=335)

Learn to use this **Experimental** feature, but use caution when shipping with it.

 On this page

## Requirements

To use [Grooms](/documentation/en-us/unreal-engine/hair-rendering-and-simulation-in-unreal-engine) with Mutable you need to toggle on the **Grooms Extensions For Mutable** plugin in your **Project Settings**.

[![Groom Extensions Plugin](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0909f0ee-8e0a-418e-8fc3-7cb942cd9113/groom-ext-plugin.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0909f0ee-8e0a-418e-8fc3-7cb942cd9113/groom-ext-plugin.png)

Once enabled, you will see a new pin appear on existing **Object** nodes.

[![Groom Pin]](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b237461a-6d1e-45b3-a76b-0c8921a53120/groom-pin.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b237461a-6d1e-45b3-a76b-0c8921a53120/groom-pin.png)

## Usage

Grooms can be added to any Skeletal Mesh Component tagged by Mutable (see [Node Mesh Component](https://github.com/anticto/Mutable-Documentation/wiki/Node-Mesh-Component)). Groom Components are dynamically created as children of the tagged Skeletal Mesh Component.

To use Grooms, follow the steps below:

1. Create a new Groom Constant node and specify which component you want it to bound to using the Component Name.

   [![Groom Constants Node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bd6047c4-9a63-44a0-ba42-9b85180d9331/groom-constants.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bd6047c4-9a63-44a0-ba42-9b85180d9331/groom-constants.png)
2. In the **Node Properties** panel, specify the **Groom** and **Binding** assets. The Binding asset must have the same Skeletal Mesh as the one in the bound Skeletal Mesh Component as the **Target Skeletal Mesh**. Other properties are automatically copied to the dynamically created Groom Component.

   [![Node Properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2e4612d2-0f25-4a61-a415-5f6a7583fb52/node-properties.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2e4612d2-0f25-4a61-a415-5f6a7583fb52/node-properties.png)
3. Connect the new node to an **Object** node. Notice that the Groom Constant nodes can be conditionally activated using Group nodes.

## Current Limitations

* Modifier nodes can not be applied to Mesh Components bound by grooms.
* A Mutable generated Skeletal Mesh must have the same number of LODs as the Source Skeletal Mesh in the Binding Asset.

* [landscape](https://dev.epicgames.com/community/search?query=landscape)
* [working with content](https://dev.epicgames.com/community/search?query=working%20with%20content)
* [experimental](https://dev.epicgames.com/community/search?query=experimental)
* [skeletal mesh](https://dev.epicgames.com/community/search?query=skeletal%20mesh)
* [grooms](https://dev.epicgames.com/community/search?query=grooms)
* [mutable](https://dev.epicgames.com/community/search?query=mutable)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Requirements](/documentation/en-us/unreal-engine/using-grooms-with-mutable-in-unreal-engine?application_version=5.7#requirements)
* [Usage](/documentation/en-us/unreal-engine/using-grooms-with-mutable-in-unreal-engine?application_version=5.7#usage)
* [Current Limitations](/documentation/en-us/unreal-engine/using-grooms-with-mutable-in-unreal-engine?application_version=5.7#currentlimitations)
