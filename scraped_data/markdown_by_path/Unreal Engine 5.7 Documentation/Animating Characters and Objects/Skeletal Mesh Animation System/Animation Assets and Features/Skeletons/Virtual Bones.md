<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/virtual-bones-in-unreal-engine?application_version=5.7 -->

# Virtual Bones

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
8. [Skeletons](/documentation/en-us/unreal-engine/skeletons-in-unreal-engine "Skeletons")
9. Virtual Bones

# Virtual Bones

Resolve layered animation problems by using Virtual Bones with IK.

![Virtual Bones](https://dev.epicgames.com/community/api/documentation/image/a621873f-cd4f-415f-a843-f530d7eee8a9?resizing_type=fill&width=1920&height=335)

 On this page

When building complex blending, layered, or compressed animation systems, there may be cases where this causes extra and undesired movement (known as "swimming") on character limbs, typically on hands and feet. **Virtual Bones**, used in combination with [IK nodes](/documentation/en-us/unreal-engine/animation-blueprint-two-bone-ik-in-unreal-engine), can be used to correct this unwanted behavior.

This document provides an overview of how to create Virtual Bones in your [Skeleton](/documentation/en-us/unreal-engine/skeletons-in-unreal-engine), and use them within your [Animation Blueprint](/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine).

#### Prerequisites

* Your project contains a [Skeletal Mesh Actor](/documentation/en-us/unreal-engine/skeletal-mesh-assets-in-unreal-engine).
* You have a basic understanding of working in [Animation Blueprints](/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine).

## Virtual Bone Overview

Virtual Bones are Bones that follow the transforms of another Bone, but in a different Bone space. In most cases this means that a Virtual Bone would be parented to the **root Bone**, but following an **end Bone**, like a hand or foot. In other words, Virtual Bones can directly follow a target Bone, without receiving the additional effects of the forward kinematic (FK) hierarchy of all joints leading to that target. Using this feature, you can set up inverse kinematic (IK) systems which make the character limbs follow the Virtual Bone, resolving "swimming" and other limb wobbling problems from complex animation systems.

In this example, Virtual Bones with IK are being used to maintain the rifle and hand positions while an additive head-look animation is playing. Without it, the hands and weapon will "swim" causing unintended movement.

|  |  |
| --- | --- |
|  |  |
| Using Virtual Bones | No Virtual Bones |

### Differences from Traditional IK

One of the main aspects of Virtual Bones is that they follow the target bone. This makes it so that you can still play an animation in which the target bone can move, changing the position of the Virtual Bone. Such a setup can be superior to traditional IK-only systems where IK can interfere with animation. For example, if you were to set up a system where the hands were IK-attached to a weapon, you would have to perform extra steps to disable IK in certain situations, such as reloading.

In this example, Virtual Bones with IK are still able to allow for base hand movement relative to another object, even with the additive animation playing. Although a traditional IK setup might resolve the "swimming" issue, the result will pin the hands in place at all times, forcing you to create extra logic to turn off IK during cases like this.

|  |  |
| --- | --- |
|  |  |
| Virtual Bones allowing for base hand movement | IK-only setup which pins the hands in place |

## Creating Virtual Bones

You can create Virtual Bones in the Animation Editor's [Skeleton Tree](/documentation/en-us/unreal-engine/skeleton-editor-in-unreal-engine#skeletontree). Right-click on a Bone, which will be the **parent**, and then select **Add Virtual Bone**. Select a Bone from this list to specify the **target**. In this example, a Virtual Bone is being created parented to the **root Bone**, then targeting the **hand\_l Bone**.

![create virtual bone](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/733cbdf0-1547-4809-83e7-fa10cd62b6ac/create1.png)

Once created, you should now see the Virtual Bone as a child of the **parent Bone**, but matching the transform of the **target Bone**. By default, Virtual Bones are automatically named as `VB <Parent>_<Target>` for their naming convention.

![virtual bone created](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f4067640-359a-4902-acde-84cdfe3bc700/create2.png)


You can also preview an [Animation Sequence](/documentation/en-us/unreal-engine/animation-sequences-in-unreal-engine) and observe the Virtual Bone following the target Bone for the duration of the animation.

![virtual bone follow](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7f4f069e-6ff2-491a-b906-7c553c1dbf91/create3.gif)

## Animation Blueprint Setup

Once you have created your Virtual Bones, you can set up logic for them in [Animation Blueprints](/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine). Due to the arbitrary nature of Virtual Bones, there are many different ways you can use them. This section will demonstrate how to create a basic weapon override and additive animation setup for Virtual Bones.

### Slot Setup

First, in your Animation Blueprint [Anim Graph](/documentation/en-us/unreal-engine/graphing-in-animation-blueprints-in-unreal-engine), create two [Slot](/documentation/en-us/unreal-engine/animation-slots-in-unreal-engine) nodes. Slots are proxy areas in your Animation Blueprint where you can insert one-off animations, and will be used to differentiate between your base and additive animation layers.

Right-click in the Anim Graph and select **Montage > Slot 'DefaultSlot'** to create a Slot.

![create slots](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3da6429e-bbc9-4920-8ad5-e892c6dd7b24/slot1.png)

For the second Slot, select it and set the **Slot Name** property in the **Details** panel to a different value other than DefaultSlot, so that the animations diverge correctly.

![additive slot](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/892f711e-75a4-48f0-b0ad-a7dbac461cb8/slot2.png)

Connect your Slots to an **Apply Additive** node, connecting the **default Slot** to the **Base** pin, and the **additive Slot** to the **Additive** pin.

![connect slots to apply additive](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9c6fcbf3-8c27-4846-a7cd-e83603c4a9ea/slot3.png)

### Exclude Virtual Bones

Next, you will need to create a [Blend Mask](/documentation/en-us/unreal-engine/blend-masks-and-blend-profiles-in-unreal-engine) in order to exclude the Virtual Bones from being evaluated from your additive Slot.

In the Animation Editor's [Skeleton Tree](/documentation/en-us/unreal-engine/skeleton-editor-in-unreal-engine#skeletontree), click the **Options** dropdown menu and select **Add Blend Mask**. Give it a name and press **Enter**.

![add blend mask](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5b37c5ff-ef90-48ad-a3e5-693363a80b50/exclude1.png)

Next, navigate to your Virtual Bones and set their blend values to **0.0**.

![set blend mask value to 0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d94504b0-3bd6-49e5-95d1-a062d23904ff/exclude2.png)

Returning to the Anim Graph, create a [Layered Blend per Bone](/documentation/en-us/unreal-engine/animation-blueprint-blend-nodes-in-unreal-engine#layeredblendperbone) node and set the following properties on it:

* Set **Blend Mode** to **Blend Mask**.
* Set **Blend Masks** to your Virtual bone-excluding Blend Mask.

![layered blend per bone using blend mask](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1bfd3f06-9f2b-41e5-bf0c-90fed32c0d25/exclude3.png)

Connect this node so that it is in between your **additive Slot** and **Apply to Additive** node, connecting the Slot only to the **Blend Poses** pin. Now, as animation plays from this additive Slot, the Blend Mask will cause the additive animation to not affect the Virtual Bones.

![connect slot to layered blend per bone](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/96238e06-ebad-41c1-822f-58a9ba34baff/exclude4.png)

### IK Setup

Lastly, you will need to create an IK setup that causes the limb to follow the Virtual Bone, while the additive layer will exclude any extra Virtual Bone movement.

Create a [Two Bone IK](/documentation/en-us/unreal-engine/animation-blueprint-two-bone-ik-in-unreal-engine) node and set the following properties on it in the Details panel:

* Set IKBone to your ending target Bone for this limb.
* Set **Effector Location Space** to **Bone Space**.
* Enable **Take Rotation from Effector Space**, which will add rotation to the IK Bone.
* Set **Effector Target** to your Virtual Bone for this limb.
* Set **Joint Target Location Space** to **Parent Bone Space**.
* Set **Joint Target** to the same value of **IKBone**.

![two bone ik properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5c5ee44f-e78c-4326-b90d-f643f3311676/ik1.png)

Joint Target Location is used to define the IK Pole Vector, which should be set to a position behind the elbow. Depending on your character's joints, this value may be different. For the default Unreal Engine mannequin, this value is set to:

1. **X: -25.0**
2. **Y: -50.0**
3. **Z: 0.0**

![joint target location](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/84bf9e5e-5111-4d1c-b312-4dedded7077b/ik2.png)

Create additional **Two Bone IK** nodes for each limb you want to match to a Virtual Bone.

### View Results

Once fully complete, your Anim Graph should look something like this, where you have:

1. [Slot](/documentation/en-us/unreal-engine/animation-slots-in-unreal-engine) nodes for your base and additive animation layers
2. The Slots are connected to an Apply Additive node, and a [Layered Blend per Bone](/documentation/en-us/unreal-engine/animation-blueprint-blend-nodes-in-unreal-engine#layeredblendperbone) node is being used to exclude the Virtual Bones from the Additive layer using a [Blend Mask](/documentation/en-us/unreal-engine/blend-masks-and-blend-profiles-in-unreal-engine).
3. IK nodes are being used on the limbs to attach to the final Virtual Bone location, which will use the base animation layer.

![anim graph summary](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/283c1507-5623-40de-a709-d20270664d99/results1.png)

Now when playing your animations within this framework, you should see your character's limbs following the Virtual Bone position, while not being affected whenever additive animations are playing.

![virtual bone result](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a6b9965c-bb73-4ee2-a8de-940131b4838d/results2.gif)

* [animation](https://dev.epicgames.com/community/search?query=animation)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisites](/documentation/en-us/unreal-engine/virtual-bones-in-unreal-engine?application_version=5.7#prerequisites)
* [Virtual Bone Overview](/documentation/en-us/unreal-engine/virtual-bones-in-unreal-engine?application_version=5.7#virtualboneoverview)
* [Differences from Traditional IK](/documentation/en-us/unreal-engine/virtual-bones-in-unreal-engine?application_version=5.7#differencesfromtraditionalik)
* [Creating Virtual Bones](/documentation/en-us/unreal-engine/virtual-bones-in-unreal-engine?application_version=5.7#creatingvirtualbones)
* [Animation Blueprint Setup](/documentation/en-us/unreal-engine/virtual-bones-in-unreal-engine?application_version=5.7#animationblueprintsetup)
* [Slot Setup](/documentation/en-us/unreal-engine/virtual-bones-in-unreal-engine?application_version=5.7#slotsetup)
* [Exclude Virtual Bones](/documentation/en-us/unreal-engine/virtual-bones-in-unreal-engine?application_version=5.7#excludevirtualbones)
* [IK Setup](/documentation/en-us/unreal-engine/virtual-bones-in-unreal-engine?application_version=5.7#iksetup)
* [View Results](/documentation/en-us/unreal-engine/virtual-bones-in-unreal-engine?application_version=5.7#viewresults)
