<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprint-spring-controller-in-unreal-engine?application_version=5.7 -->

# Spring Controller

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
10. Spring Controller

# Spring Controller

Describes the Spring Controller which is used to limit how far a bone can stretch from its reference pose before force is applied in the opposite direction.

![Spring Controller](https://dev.epicgames.com/community/api/documentation/image/3e7ad160-da44-430a-8ade-1f474fc93fcf?resizing_type=fill&width=1920&height=335)

 On this page

With the **Spring Controller** [Animation Blueprint](/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine) node, you can apply a controlled stretch to bone from a character's skeleton.

![spring controller animation blueprint node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8bbec2cf-db23-4f25-9d2a-b8157e4786b1/springcontroller.png)

Here is an example of the Spring Controller node being used to simulate movement of non-animated bones by applying a force in the opposite direction for the character's motion.

|  |  |
| --- | --- |
| spring cotroller demo disabled(convert:false) | spring controller demo enabled |
| Spring Controller Disabled | Spring Controller Enabled |

## Property Reference

![spring controller animation blueprint node details pannel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/97e97454-1422-4145-a678-e51755319b23/details.png)

Here you can reference a list of the Spring Controller node's properties.

| Property | Description |
| --- | --- |
| **Spring Bone** | Select the bone from the character's skeleton to apply the Spring Controller node to. |
| **Max Displacement** | Set the maximum distance the bone can stretch from the reference pose location, in Unreal Engine units, when **Limit Displacement** is enabled. |
| **Spring Stiffness** | Set a multiplier value used to calculate the stiffness of the spring. Larger values require more bone velocity to displace the bone and result in a larger applied force with quicker reactive movements. |
| **Spring Damping** | Set a multiplier to reduce the **Spring Bones**'s velocity, to create smoother and more controlled results. |
| **Error Reset Thresh** | Set a threshold to reset the Spring Bones in Unreal Engine units. If the **Spring Bone** stretches more than this amount, it resets in order to avoid errors introduced by sudden, large displacements such as those caused by teleporting Actors. |
| **Limit Displacement** | When enabled the **Max Displacement** property will be considered. |

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [skeletal controls](https://dev.epicgames.com/community/search?query=skeletal%20controls)
* [animation graph](https://dev.epicgames.com/community/search?query=animation%20graph)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Property Reference](/documentation/en-us/unreal-engine/animation-blueprint-spring-controller-in-unreal-engine?application_version=5.7#propertyreference)
