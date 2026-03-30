<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/locomotion-in-unreal-engine?application_version=5.7 -->

# Locomotion

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
7. [Animation Assets and Features](/documentation/en-us/unreal-engine/animation-assets-and-features-in-unreal-engine "Animation Assets and Features")
8. Locomotion

# Locomotion

An overview of Character Locomotion features in Unreal Engine.

![Locomotion](https://dev.epicgames.com/community/api/documentation/image/0c99c8d1-01fb-47a3-8432-563c8bdf9695?resizing_type=fill&width=1920&height=335)

 On this page

In **Unreal Engine** character **Locomotion** is built on the foundation of [character object](/documentation/en-us/unreal-engine/setting-up-a-character-in-unreal-engine), [movement](/documentation/404), and [animation](/documentation/en-us/unreal-engine/animation-assets-and-features-in-unreal-engine) playback. This foundation is supported with Locomotion tools that you can use to synchronize character movement behavior with reactive and dynamic animations.

This document provides an overview of the character Locomotion tool in Unreal Engine.

## Root Motion

By enabling **Root Motion**, a character's movement can be driven by an animation sequence using motion data from the Root Bone. Animations with their Root Motionenabled, create more realistic and grounded movement behaviors and interactions within levels.

![root motion enabled animation](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bd6394cb-998c-4176-98b9-5884b45ef264/recursiverootmotion.gif)

Read about how you can drive a Character's movement with animation playback using Root Motion in the following documentation.

[![Root Motion](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a8634d57-a151-44b7-97e0-5850b8423b58/topicimage.png)

Root Motion

An overview Root Motion Animations in Unreal Engine.](/documentation/en-us/unreal-engine/root-motion-in-unreal-engine)

## Pose Warping

You can enable **Pose Warping** to dynamically adjustment a character's animated poses to align with character movement, using [Root Motion](/documentation/en-us/unreal-engine/locomotion-in-unreal-engine#root%20motion). With Pose Warping, you need fewer individual animations to reach the same level of animated-movement coverage as before. This reduces the dependency on animation-dictated gameplay, and allows animation and gameplay tuning to evolve side by side during development.

![pose warping demo](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9e2e75a6-0481-4e61-9858-192998ae5fe0/posewarpdemo.gif)

Read about Pose Warping and an example implementation in the following documentation.

[![Pose Warping](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e21062b3-79e6-4954-82f5-3a8a7eba7e1c/topicimage.png)

Pose Warping

Pose Warping dynamically warps a character's animated pose to align with capsule movement.](/documentation/en-us/unreal-engine/pose-warping-in-unreal-engine)

## Motion Warping

With **Motion Warping**, you can dynamically warp windows of a character's animation to align with [Root Motion](/documentation/en-us/unreal-engine/locomotion-in-unreal-engine#root%20motion) or to align with assigned **Warp Targets**. With this feature, you can rely less on the manual creation and fine tuning of animations to fit specific object interactions, and apply logic to bend base animations to fit pre-established conditions.

![motion warping animation to warp target](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0d1de273-031b-4eec-b1fd-26354909b503/motionwarpingresult.gif)

In the following documentation you can read more about Motion Warping and follow along with an example workflow.

[![Motion Warping](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6307b3ab-2fef-458a-b53e-d0d926ad4aec/topicimage.png)

Motion Warping

An in depth look at Motion Warping for animations in Unreal Engine.](/documentation/en-us/unreal-engine/motion-warping-in-unreal-engine)

## Distance Matching

With **Distance Matching** you can use a calculated distance value, to or from, a target to drive Animation Sequences. Distance Matching can align animation playback with character speed, reducing the need for manual animation tuning when altering character behaviors.

![distance matching animation pose selection](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/77797fbd-dc86-4964-8248-446942d09332/lyradistancematchingdemo.gif)

Read about Distance Matching and see an example workflow in the documentation below.

[![Distance Matching](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5c52d4bf-3036-4549-a547-666743e916d3/topicimage.png)

Distance Matching

An in depth look at Distance Matching in Unreal Engine with an example workflow implementation.](/documentation/en-us/unreal-engine/distance-matching-in-unreal-engine)

* [animation](https://dev.epicgames.com/community/search?query=animation)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Root Motion](/documentation/en-us/unreal-engine/locomotion-in-unreal-engine?application_version=5.7#rootmotion)
* [Pose Warping](/documentation/en-us/unreal-engine/locomotion-in-unreal-engine?application_version=5.7#posewarping)
* [Motion Warping](/documentation/en-us/unreal-engine/locomotion-in-unreal-engine?application_version=5.7#motionwarping)
* [Distance Matching](/documentation/en-us/unreal-engine/locomotion-in-unreal-engine?application_version=5.7#distancematching)
