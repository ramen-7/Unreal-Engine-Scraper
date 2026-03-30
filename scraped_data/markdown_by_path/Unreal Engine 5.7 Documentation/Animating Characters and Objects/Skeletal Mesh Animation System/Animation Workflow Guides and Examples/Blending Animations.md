<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/blending-animations-in-unreal-engine?application_version=5.7 -->

# Blending Animations

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
5. [Animating Characters and Objects](/documentation/en-us/unreal-engine/animating-characters-and-objects-in-unreal-engine "Animating Characters and Objects")
6. [Skeletal Mesh Animation System](/documentation/en-us/unreal-engine/skeletal-mesh-animation-system-in-unreal-engine "Skeletal Mesh Animation System")
7. [Animation Workflow Guides and Examples](/documentation/en-us/unreal-engine/animation-workflow-guides-and-examples-in-unreal-engine "Animation Workflow Guides and Examples")
8. Blending Animations

# Blending Animations

Transitioning smoothly between two animations on a single Skeletal Mesh

![Blending Animations](https://dev.epicgames.com/community/api/documentation/image/4b6ee2f0-692a-4ab9-9636-d343a8928727?resizing_type=fill&width=1920&height=335)

 On this page

Animation blending, as a concept, simply means making a smooth transition between two or more animations on a single character or Skeletal Mesh. In Unreal Engine, there are various ways in which such blending can be applied. In this document, we will overview each one and how they can be applied to your characters.

## Blend Spaces

One of the most common ways to blend together animations is with Blend Spaces.

For more information on Blend Spaces, please see the [Blend Spaces](/documentation/en-us/unreal-engine/blend-spaces-in-unreal-engine) documentation.

## Blending with Blueprints

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/aafd5d21-dcf8-43d9-9316-e27b3948f975/personablendanimgraph.png)

Animation blending can also be handled directly by way of the AnimGraph within an Animation Blueprint. The AnimGraph charts the flow of animation pose data through a series of different nodes, each node contributing in some way to the final look of the pose or motion. There are a variety of nodes specially designed to aid in blending multiple poses together in some way. These can be additive, literally combining two animations based on a weighted bias or alpha value, or can be direct overrides of the existing pose. You can also send animation directly to a specific bone in the Skeleton and all of its children. For instance, you can start with an animation in which the character is running, but then selectively apply a waving animation just to the right arm. The final result will be the character running and waving.

For an understanding of how animation blending can be handled with Blueprints, please see [Animation Blueprints](/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine) and [Blend Nodes](/documentation/en-us/unreal-engine/animation-blueprint-blend-nodes-in-unreal-engine).

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [animation blending](https://dev.epicgames.com/community/search?query=animation%20blending)
* [animation features](https://dev.epicgames.com/community/search?query=animation%20features)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Blend Spaces](/documentation/en-us/unreal-engine/blending-animations-in-unreal-engine?application_version=5.7#blendspaces)
* [Blending with Blueprints](/documentation/en-us/unreal-engine/blending-animations-in-unreal-engine?application_version=5.7#blendingwithblueprints)
