<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprint-hand-ik-retargeting-in-unreal-engine?application_version=5.7 -->

# Hand IK Retargeting

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
10. Hand IK Retargeting

# Hand IK Retargeting

Describes the Hand IK Retargeting control which can be used to handle retargeting of IK bones.

![Hand IK Retargeting](https://dev.epicgames.com/community/api/documentation/image/afa2b50b-6989-4783-b542-1c61ac0e2ca2?resizing_type=fill&width=1920&height=335)

 On this page

With the **Hand IK Retargeting** [Animation Blueprint](/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine) node, you can retarget IK bone chains, to correct fk hand locations when using animations with characters of different proportions.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2f32e90c-0848-4447-b4e4-cc983829200b/handikretargeting.png)

Here, the same animation is playing across both Masculine and Feminine characters, as the Feminine character twists, their right arm is overextending in order to keep their hands connected to the weapon.

|  |  |
| --- | --- |
|  |  |
| Masculine Character with Hand IK Retargeting Node Disabled | Feminine Character with Hand IK Retargeting Node Disabled |

You can use the Hand IK Retargeting node's **Hand FKWeight** property to shift the prioritization weight of the set FK bone, to correct any over-extension.

|  |
| --- |
|  |
| Feminine Character with Hand IK Retargeting Node Enabled |

In the example, the characters arms are being attached to the weapon, using a combination of the [Two Bone IK](/documentation/en-us/unreal-engine/animation-blueprint-two-bone-ik-in-unreal-engine) nodes. The Hand IK Retargeting node is then being used to correct for the over extension of the character's left arm. The Hand FKWeight is set to a value of 0 to achieve this result.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4a73be05-3a79-46f5-99d8-9e96ed2b48fc/graph.png)

## Property Reference

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/34a595c4-5d6a-4583-b25c-3b34794f6f13/details.png)

Here you can reference a list of the Hand IK Retargeting node's properties.

| Property | Description |
| --- | --- |
| **Right Hand FK** | Select the characters right hand bone from the characters skeleton to set as the **Right Hand FK**. |
| **Left Hand FK** | Select the characters left hand bone from the characters skeleton to set as the **Left Hand FK**. |
| **Right Hand IK** | Select the right hand IK bone from the characters skeleton to set as the **Right Hand IK**. |
| **Left Hand IK** | Select the left hand IK bone from the characters skeleton to set as the **Left Hand IK**. |
| **IKBones to Move** | Here you can select other bones to be moved. You can add bones with **Add (+)** and select a bone from the character's skeleton in the drop down.  Additional bones to move could be weapon bones, or other bones used for object interactions. |
| **Hand FKWeight** | Here you can set the weight to favor the right or the left hand to correct for joint popping and stretching. For example, 0 would favor the left hand, 1 would favor the right hand and 0.5 would be equal weight. By default this property appears as a pin on the Hand IK Retargeting node in the **AnimGraph**. |

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [skeletal control](https://dev.epicgames.com/community/search?query=skeletal%20control)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Property Reference](/documentation/en-us/unreal-engine/animation-blueprint-hand-ik-retargeting-in-unreal-engine?application_version=5.7#propertyreference)
