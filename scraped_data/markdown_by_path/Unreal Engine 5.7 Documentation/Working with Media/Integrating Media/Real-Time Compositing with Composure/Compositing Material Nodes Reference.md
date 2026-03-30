<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/compositing-material-nodes-reference-for-unreal-engine?application_version=5.7 -->

# Compositing Material Nodes Reference

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
5. [Working with Media](/documentation/en-us/unreal-engine/working-with-media-in-unreal-engine "Working with Media")
6. [Integrating Media](/documentation/en-us/unreal-engine/integrating-media-in-unreal-engine "Integrating Media")
7. [Real-Time Compositing with Composure](/documentation/en-us/unreal-engine/realtime-compositing-with-composure-in-unreal-engine "Real-Time Compositing with Composure")
8. Compositing Material Nodes Reference

# Compositing Material Nodes Reference

Product documentation including reference and guides for Unreal Engine

![Compositing Material Nodes Reference](https://dev.epicgames.com/community/api/documentation/image/84c53312-4a07-451d-999c-3ba52f6fe4e8?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

To make compositing easier, UE5 has a series of nodes to serve some of the most common compositing operations. Here, each one is briefly highlighted and has an explanation of its purpose.

[![Material Nodes Example](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d4b7e60f-2676-4418-a5a7-5aeafb354682/01-composure-element-blueprint.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d4b7e60f-2676-4418-a5a7-5aeafb354682/01-composure-element-blueprint.png)

Click image to expand.

The compositing material nodes expect a **float4** input, so make sure you're passing in **RGBA** and not just **RGB**.

## Over

This node layers one image (A) over another (B), using the alpha from input A.

![Over Node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/aa1a91a7-2377-492f-8a38-55cd7c98f259/02-over-node.png "Over Node")


This node expects that the input color channels are pre-multiplied with the image's alpha.

## In

This node returns the portion of A that is inside the shape of B.

![In Node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3454702c-2376-4d1d-8f18-62271e636f87/03-in-node.png "In Node")

## Out

This node returns the portion of A that is outside the shape of B.

![Out Node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/61f6c657-aaec-467b-9434-693d36143ed9/04-out-node.png "Out Node")

## PreMult

This node multiplies the input's RGBA channel by its alpha.

![PreMult Node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/426f6779-8b0f-40fc-ac87-9fe934365027/05-premult-node.png "PreMult Node")

## UnPreMult

This node divides the input's RGBA channel by its alpha.

![UnPreMult Node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/91da0193-ca1a-45dd-9d55-d551036345a1/06-unpremult-node.png "UnPreMult Node")

## KeyMix

This node layers two images together using a specified mask.

![KeyMix Node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9b3d39a7-dee5-4f0d-b10d-7c2839346a17/07-key-mix-node.png "KeyMix Node")

* [beta](https://dev.epicgames.com/community/search?query=beta)
* [reference](https://dev.epicgames.com/community/search?query=reference)
* [ar/vr/xr](https://dev.epicgames.com/community/search?query=ar%2Fvr%2Fxr)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Over](/documentation/en-us/unreal-engine/compositing-material-nodes-reference-for-unreal-engine?application_version=5.7#over)
* [In](/documentation/en-us/unreal-engine/compositing-material-nodes-reference-for-unreal-engine?application_version=5.7#in)
* [Out](/documentation/en-us/unreal-engine/compositing-material-nodes-reference-for-unreal-engine?application_version=5.7#out)
* [PreMult](/documentation/en-us/unreal-engine/compositing-material-nodes-reference-for-unreal-engine?application_version=5.7#premult)
* [UnPreMult](/documentation/en-us/unreal-engine/compositing-material-nodes-reference-for-unreal-engine?application_version=5.7#unpremult)
* [KeyMix](/documentation/en-us/unreal-engine/compositing-material-nodes-reference-for-unreal-engine?application_version=5.7#keymix)
