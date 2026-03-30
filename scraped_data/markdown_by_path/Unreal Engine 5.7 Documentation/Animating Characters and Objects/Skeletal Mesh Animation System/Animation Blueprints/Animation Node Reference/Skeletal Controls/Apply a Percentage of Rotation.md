<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprint-apply-percent-of-rotation-in-unreal-engine?application_version=5.7 -->

# Apply a Percentage of Rotation

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
10. Apply a Percentage of Rotation

# Apply a Percentage of Rotation

Describes how Apply a Percentage of Rotation drives the Rotation of a target bone with a specified percentage of the Rotation of another bone within the Skeleton.

![Apply a Percentage of Rotation](https://dev.epicgames.com/community/api/documentation/image/3ec38f48-7203-4abf-9ca3-71df1db03d0d?resizing_type=fill&width=1920&height=335)

 On this page

With the **Apply a Percentage of Rotation** [Animation Blueprint](/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine) node, you can apply a **Source Bone**'s rotation motion to a **Target Bone**.

Here, the robot's antena are matching the X-axis rotation its head.

|  |  |
| --- | --- |
| apply a percentage of rotation disabled | apply a percentage of rotation enabled |
| Disabled Apply a Percentage of Rotation | Enabled Apply a Percentage of Rotation |

## Overview

The Apply a Percentage of Rotation node operates within **Component Space**, so a [space conversion](/documentation/en-us/unreal-engine/animation-blueprint-component-space-conversion-in-unreal-engine) will need to occur to implement the node within your character's Animation Blueprint.

![Apply a Percentage of Rotation animation blueprint node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2a59b7b5-6e70-4205-9ff6-49a9f4ef5ca1/applypercentage.png)

With the **Alpha** property or pin, you can control the degree of the applied rotation on the generated output pose. A value of **1** will fully use the generated output pose, while a value of **0** will output the source pose.

The **Multiplier** property or pin allows you to multiply the degree of the rotation beyond the **Source Bones** rotation.

A **Multiplyer** value of 0 will not apply any rotation to the Target Bone.

In the Apply a Percentage of Rotation node's **Details** panel you can select a **Source Bone**, to copy the rotational movement from, as well as a **Target Bone** in which to apply the copied rotation motion.

![apply a percentage of rotation animation blueprint node with target bone and soruce bone properties highlighted in details panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6f957c00-ffc5-4ac4-a90d-4cd1a3c5f2b7/detailspanelhighlight.png)

See the [Property Reference](/documentation/en-us/unreal-engine/animation-blueprint-apply-percent-of-rotation-in-unreal-engine#propertyreference) table for more information about the Apply a Percentage of Rotation node's properties.

### Stacking Nodes

Multiple Axis rotation can be used by stacking addition Apply a Percentage of Rotation nodes together, and assigning unique axis of rotation to each.

![combined apply a percentage of rotation animation blueprint nodes](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e1cdd2d1-ddb9-42f8-8fce-eb7528fefa11/stack.png)


When stacking Apply a Percentage of Rotation nodes, ensure the **Is Additive** property is enabled in the **Details** panel for any additive or stacked nodes applying rotation to the same bone. This property is also important to enable when using the Apply a Percentage of Rotation node in conjunction with any other animation or node making adjustments to the same bone.

## Property Reference

![apply a percentage of rotation animation blueprint node with details panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cef077a2-763b-47b5-a71f-e97edc54cd8b/detailspanel.png)

Here you can reference a list of the Apply a Percentage of Rotation node's properties.

| Property | Description |
| --- | --- |
| **Target Bone** | Select a bone from the character's [Skeleton](/documentation/en-us/unreal-engine/skeletons-in-unreal-engine) in which to apply the rotation from the **Source Bone**. Any child bones of the Target Bone will also be moved relevant to the parent bone motion. |
| **Source Bone** | Select a bone in which to copy the rotational motion from, on the axis defined in the **Rotation Axis to Refer** property. This rotation motion will then be applied to the **Target Bone**. |
| **Multiplyer** | Set a multiplier to apply to the rotation motion from the **Source Bone** as it is applied to the **Target Bone**. A value of 1 will copy the rotation motion exactly.  By default this property is accessible in the **AnimGraph** on the selected node. |
| **Rotation Axis To Refer** | Here you can select which axis of rotation motion will be copied from the **Source Bone**, and applied to the **Target Bone**. |
| **Is Additive** | Enable this property to enable the rotation motion to be applied to the bone as additive. Disabling this property will overwrite any previous motion on the **Target Bone**. |

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [animation blending](https://dev.epicgames.com/community/search?query=animation%20blending)
* [skeletal controls](https://dev.epicgames.com/community/search?query=skeletal%20controls)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Overview](/documentation/en-us/unreal-engine/animation-blueprint-apply-percent-of-rotation-in-unreal-engine?application_version=5.7#overview)
* [Stacking Nodes](/documentation/en-us/unreal-engine/animation-blueprint-apply-percent-of-rotation-in-unreal-engine?application_version=5.7#stackingnodes)
* [Property Reference](/documentation/en-us/unreal-engine/animation-blueprint-apply-percent-of-rotation-in-unreal-engine?application_version=5.7#propertyreference)
