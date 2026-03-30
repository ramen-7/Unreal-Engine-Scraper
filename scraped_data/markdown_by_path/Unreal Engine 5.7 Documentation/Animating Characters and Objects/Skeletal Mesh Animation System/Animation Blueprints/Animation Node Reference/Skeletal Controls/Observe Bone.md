<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprint-observe-bone-in-unreal-engine?application_version=5.7 -->

# Observe Bone

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
7. [Animation Blueprints](/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine "Animation Blueprints")
8. [Animation Node Reference](/documentation/en-us/unreal-engine/animation-blueprint-nodes-in-unreal-engine "Animation Node Reference")
9. [Skeletal Controls](/documentation/en-us/unreal-engine/animation-blueprint-skeletal-controls-in-unreal-engine "Skeletal Controls")
10. Observe Bone

# Observe Bone

Describes how you can debug a specified Bone with the Observe Bone node.

![Observe Bone](https://dev.epicgames.com/community/api/documentation/image/5a2919bb-43e7-428f-a122-bcb1b9d1ff6a?resizing_type=fill&width=1920&height=335)

 On this page

With the **Observe Bone** [Animation Blueprint](/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine) node, you can watch a selected bone's translation rotation and scale motion for debug purposes.

![observe bone animation blueprint node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2b78ea88-cefb-402e-93de-12192a286b12/observebone.png)

Here a character's `upperarm_l` is being observed during an animation.

![observe bone animation blueprint node demonstration](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0fdbd804-ad0a-4dcf-837e-11099282ac27/demo.gif)

The node will display debug data in the **AnimGraph** with the coordinates of the **Bone to Observe**'s motion. Each line of the debug data displays an element of motion data on each axis.

For example:

* **TX** represents Translation on the X axis.
* **RY** represents Rotation on the Y axis.
* **SZ** represents Scale on the Z axis.

## Property Reference

Here you can reference the Observe Bone properties accessible in the node's **Details** panel.

| Property | Description |
| --- | --- |
| **Bone to Observe** | Here you can define a bone from the character's [skeleton](/documentation/en-us/unreal-engine/skeletons-in-unreal-engine) to track position and motion data. |
| **Display Space** | Here you can select what space the **Bone to Observe** motion is calculated.   * **World Space**: observes the absolute position of the **Bone to Observe**\* in world space. * **Component Space**: observes the position of the **Bone to Observe** within the [Skeletal Mesh](/documentation/en-us/unreal-engine/skeletal-mesh-assets-in-unreal-engine)'s reference frame. * **Parent Bone Space**: observes the position of the **Bone to Observe** relative to the parent bone. * **Bone Space**: observes the position of the **Bone to Observe** within its own reference frame. |
| **Relative to Ref Pose** | When enabled this property will track the position and motion data of the **Bone to Observe** relevant to the [Skeletal Mesh](/documentation/en-us/unreal-engine/skeletal-mesh-assets-in-unreal-engine)'s reference pose, based on the space defined in the **Display Space** property. |

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [skeletal control](https://dev.epicgames.com/community/search?query=skeletal%20control)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Property Reference](/documentation/en-us/unreal-engine/animation-blueprint-observe-bone-in-unreal-engine?application_version=5.7#propertyreference)
