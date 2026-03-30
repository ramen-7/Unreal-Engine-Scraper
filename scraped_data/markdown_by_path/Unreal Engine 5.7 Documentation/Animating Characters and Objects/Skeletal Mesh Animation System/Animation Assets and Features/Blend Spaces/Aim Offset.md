<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/aim-offset-in-unreal-engine?application_version=5.7 -->

# Aim Offset

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
8. [Blend Spaces](/documentation/en-us/unreal-engine/blend-spaces-in-unreal-engine "Blend Spaces")
9. Aim Offset

# Aim Offset

An Aim Offset is a type of Blend Space that uses additive poses, typically for creating aim-spaces.

![Aim Offset](https://dev.epicgames.com/community/api/documentation/image/37d2700e-f2a2-4c9a-9ca0-af1f43450ca4?resizing_type=fill&width=1920&height=335)

 On this page

An **Aim Offset** is a type of [Blend Space](/documentation/en-us/unreal-engine/blend-spaces-in-unreal-engine) in which the animation samples are **additive**. Typically Aim Offsets are used to create a multi-directional weapon aiming blend structure, which then apply additively to a default aiming pose.

#### Prerequisites

* Your project has a Skeletal Mesh character with the necessary imported animations and poses to use as samples in the Aim Offset graph.
* You have an understanding of [Blend Spaces](/documentation/en-us/unreal-engine/blend-spaces-in-unreal-engine); Aim Offsets are a type of Blend Space.

## Overview

The main concept with Aim Offsets is that they are designed to be additively applied to an existing base animation. In weapon aiming examples, this base animation would typically be an "aiming forward" neutral animation.

![aim offset base animation](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e05bd07a-7afc-47c4-94c5-14fdf07c7ddd/aimbase.gif)

From this base, you can then implement the full range of additive poses within your Aim Offset graph. The number of poses you will need is dependent on the motions your character will need to do. A typical aim-space sample system might look like this:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
| Up Right Behind | Up Right | Up | Up Left | Up Left Behind |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
| Right Behind | Right | Base | Left | Left Behind |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
| Down Right Behind | Down Right | Down | Down Left | Down Left Behind |

## Creation and Setup

To create an Aim Offset in the Content Browser, click **Add (+)** and select **Animation > Aim Offset** or [**Aim Offset 1D**](/documentation/en-us/unreal-engine/blend-spaces-in-unreal-engine#1d) from the context menu. When creating a new Aim Offset, you have to designate a Skeleton asset. Be sure to choose the same one used by the Skeletal Mesh you want to use with the Aim Offset.

![create aim offset](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e3592da2-e983-4c9a-93e9-44e228af26cf/createaim.png)

Open the newly created Aim Offset to continue setup.

### Base Pose Setup

Because Aim Offsets are meant to be used with additive animation samples, you should set a base animation to play in order to preview the additive behavior correctly. To do this, navigate to the **Preview Base Pose** property in the [Asset Details](/documentation/en-us/unreal-engine/blend-spaces-in-unreal-engine#assetdetails) panel and specify an animation asset to play.

![aim offset preview base pose](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fe8db3a6-36f0-4d44-a384-1217323eebb4/basepose.png)

### Referencing Aim Poses

Like [Blend Spaces](/documentation/en-us/unreal-engine/blend-spaces-in-unreal-engine#addinganimationstothegraph), Aim Offsets are created by referencing animation samples within a blending graph. The easiest way to do this is by dragging the animations from the **Asset Browser** panel into the graph.

![add animation aim offset](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/16db9ffa-45b0-4942-bef4-ee6dabd774f8/addanims.png)


When creating your Aim Offset system, you should be mindful about how you allow the yaw (side-to-side) motion to animate. For example, the example poses you see [above](/documentation/en-us/unreal-engine/aim-offset-in-unreal-engine#overview) will look fine when the character is standing still. However it may produce issues if you allow it to play during other animation states, such as running or walking.

To alleviate this, you can use Animation Blueprints to limit the incoming data for the Aim Offset so that the side-to-side extremes are only in use when the character is stationary. Alternatively, you can change your Aim Offset to just aim the character up and down, allowing the rotation of the actual character to deal with side-to-side motion.

### Mesh Space Additive

For your animation samples to work with an Aim Offset, ensure your animations are additive, and that the **Additive Anim Type** is set to **Mesh Space**. This is required because Aim Offsets only accept animations that are additive.

To do this, open all of the **Animation Sequences** being used in your Aim Offset. In their **Asset Details** panels, locate and set the following properties:

* Set **Additive Anim Type** to **Mesh Space**.
* Set **Base Pose Type** to **Selected animation frame**.
* Set **Base Pose Animation** to use the same base animation as the [Base Pose Setup](/documentation/en-us/unreal-engine/aim-offset-in-unreal-engine#baseposesetup).
* Set **Ref Frame Index** to **0**.

![aim offset additive](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/64d0f7e5-4c30-4df3-a3ab-bf61f5939cfd/additive.png)

The reason **Mesh Space** must be selected instead of **Local Space** is because Mesh Space applies its additive effect in the space of the **Skeletal Mesh Component**. This causes rotations to move in the same direction, regardless of the orientation of the preceding Bone in the Skeletal Mesh. This is important for Aim Offsets because in some cases, you may want the rotations coming from the Blend Space to be applied consistently, regardless of the current base pose of the character.

For example, if your character has the ability to lean sideways while aiming, this can cause the Bones' overall local space to shift towards the lean direction. If your additive type is set to **Local Space**, then it can cause the upward-aiming pose to be skewed, and not correctly face up. Using **Mesh Space** as your additive type corrects this by applying the rotation offsets from the Blend Space in the expected way.

![mesh space local space additive difference](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/88a0fd16-3171-4e2a-880e-b41a33b0f0da/additive2.png)

1. Base pose with leaning.
2. Leaning and aiming up when using Local Space additive.
3. Leaning and aiming up when using Mesh Space additive.

## Animation Blueprint Setup

Once your Aim Offset is created, you can reference it within your [Animation Blueprint](/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine). Similar to Blend Spaces, you can reference it as a [player](/documentation/en-us/unreal-engine/blend-spaces-in-animation-blueprints-in-unreal-engine#blendspaceplayer), which references the Aim Offset asset directly, or as a [graph](/documentation/en-us/unreal-engine/blend-spaces-in-animation-blueprints-in-unreal-engine#blendspaceplayer), where you can diverge the logic within your Anim Graph.

To reference an Aim Offset Player in the Anim Graph, right-click in the graph and select your **Aim Offset Player Asset** from the **Blend Spaces** category. Connect the output to the **Output Pose** node.

![aim offset animation blueprints](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b29d2324-d187-4bb4-883e-5fe5db9f93e2/animbp1.png)

You must also connect a **Base Pose** to the Aim Offset node, typically this would be the same animation defined in the [Base Pose step earlier](/documentation/en-us/unreal-engine/aim-offset-in-unreal-engine#headername), or a [State Machine](/documentation/en-us/unreal-engine/state-machines-in-unreal-engine) that uses a similar base pose.

![aim offset base pose locomotion](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8fcad5d6-8148-4f3f-8f29-f0361251b32d/animbp2.png)

Finally, you must create logic to drive the **Yaw** and **Pitch** values on the Aim Offset. Depending on your player controls, this logic can be created in several different ways. For this example, you can use [property access](/documentation/en-us/unreal-engine/graphing-in-animation-blueprints-in-unreal-engine#propertyaccess) to output data from the pawn's base aim rotation.

![aim offset values](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d18b90b0-000a-4b88-a7d8-37f8ca0a327b/animbp3.png)

* [animation](https://dev.epicgames.com/community/search?query=animation)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisites](/documentation/en-us/unreal-engine/aim-offset-in-unreal-engine?application_version=5.7#prerequisites)
* [Overview](/documentation/en-us/unreal-engine/aim-offset-in-unreal-engine?application_version=5.7#overview)
* [Creation and Setup](/documentation/en-us/unreal-engine/aim-offset-in-unreal-engine?application_version=5.7#creationandsetup)
* [Base Pose Setup](/documentation/en-us/unreal-engine/aim-offset-in-unreal-engine?application_version=5.7#baseposesetup)
* [Referencing Aim Poses](/documentation/en-us/unreal-engine/aim-offset-in-unreal-engine?application_version=5.7#referencingaimposes)
* [Mesh Space Additive](/documentation/en-us/unreal-engine/aim-offset-in-unreal-engine?application_version=5.7#meshspaceadditive)
* [Animation Blueprint Setup](/documentation/en-us/unreal-engine/aim-offset-in-unreal-engine?application_version=5.7#animationblueprintsetup)
