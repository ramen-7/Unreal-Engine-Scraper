<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprint-copy-bone-in-unreal-engine?application_version=5.7 -->

# Copy Bone

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
10. Copy Bone

# Copy Bone

Describes the Copy Bone node which copies the Transform data or any component of it from one bone to another.

![Copy Bone](https://dev.epicgames.com/community/api/documentation/image/2c88cecf-0f4a-48d8-91da-e4ebfbfc1df3?resizing_type=fill&width=1920&height=335)

 On this page

With the **Copy Bone** [Animation Blueprint](/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine) node, you can copy transform data such as **Translation**, **Rotation**, and **Scale**, from a **Source Bone** to a **Target Bone**.

![copy bone animation blueprint node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5e2b1f54-3235-4420-8580-bcb8f048b696/copybone.png)

Using a simple implementation, you can use the Copy Bone node to copy the position and motion of the **Source Bone** to the **Target Bone**. Here the character's right-hand auxiliary weapon bone (`weapon_r`), is selected as the **Target Bone**, copying the **Source Bone**'s, the character's left hand (`hand_l`), position and motion. Here the effect of the Copy Bone node can be seen as it moves the weapon bone at runtime from the character's right hand to their left hand.

|  |  |
| --- | --- |
| copy bone demo disabled | copy bone demo enabled |
| Copy Bone Disabled | Copy Bone Enabled |

You can use this implementation of the Copy Bone node to pass an object from one of the [Skeletal Mesh](/documentation/en-us/unreal-engine/skeletal-mesh-assets-in-unreal-engine)'s hands to the other during animation playback.

In the **AnimGraph**, you can toggle the different components of motion, including **Translation**, **Rotation**, and **Scale**, to apply the **Source Bone** motion to the **Target Bone**.

With the **Alpha** value or pin, you can control the degree of the blend on the generated output pose. A value of **1** will fully use the generated output pose, while a value of **0** will output the source pose.

## Property Reference

![copy bone animation blueprint node details panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/432eebbb-b247-4927-b084-87f4056e2f11/details.png)

Here you can reference the Copy Bone node's properties.

| Property | Description |
| --- | --- |
| **Source Bone** | Select a bone from the character's [skeleton](/documentation/en-us/unreal-engine/skeletons-in-unreal-engine) as the source of the motion data applied to the **Target Bone**. |
| **Target Bone** | Select a bone from the character's [skeleton](/documentation/en-us/unreal-engine/skeletons-in-unreal-engine) as the destination for the motion data. |
| **Copy Translation** | Applies the **Translation** motion from the **Source Bone** to the **Target Bone**. By default this property appears as a Boolean on the node in the **AnimGraph**. |
| **Copy Rotation** | Applies the **Rotation** motion from the **Source Bone** to the **Target Bone**. By default this property appears as a Boolean on the node in the **AnimGraph**. |
| **Copy Scale** | Applies the **Scale** motion from the **Source Bone** to the **Target Bone**. By default this property appears as a Boolean on the node in the **AnimGraph**. |
| **Control Space** | Select in which space the **Source Bone** motion is calculated and applied to the **Target Bone**.   * **World Space**: copies the absolute position of the **Source Bone** in world space. * **Component Space**: copies the position and motion data of the **Source Bone** within the [Skeletal Mesh](/documentation/en-us/unreal-engine/skeletal-mesh-assets-in-unreal-engine)'s reference frame. * **Parent Bone Space**: copies the position and motion data of the **Source Bone** relative to the parent bone. * **Bone Space**: copies the position and motion data of the **Source Bone** within its own reference frame. |

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [landing page](https://dev.epicgames.com/community/search?query=landing%20page)
* [skeletal controls](https://dev.epicgames.com/community/search?query=skeletal%20controls)
* [skeletal control](https://dev.epicgames.com/community/search?query=skeletal%20control)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Property Reference](/documentation/en-us/unreal-engine/animation-blueprint-copy-bone-in-unreal-engine?application_version=5.7#propertyreference)
