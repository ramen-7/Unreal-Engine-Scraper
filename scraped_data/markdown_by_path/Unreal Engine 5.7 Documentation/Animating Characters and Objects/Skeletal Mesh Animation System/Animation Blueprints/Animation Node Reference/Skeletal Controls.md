<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprint-skeletal-controls-in-unreal-engine?application_version=5.7 -->

# Skeletal Controls

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
9. Skeletal Controls

# Skeletal Controls

Animation nodes that enable direct manipulation and applying solvers to the bones of the target Skeleton.

![Skeletal Controls](https://dev.epicgames.com/community/api/documentation/image/caf895c6-ee48-4c08-9796-3a3aeba1eda0?resizing_type=fill&width=1920&height=335)

 On this page

With **Skeletal Control** [Animation Blueprint](/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine) nodes you can take direct control of a character's [Skeleton asset](/documentation/en-us/unreal-engine/skeletons-in-unreal-engine). Skeletal Control nodes can be used within a character's Animation Blueprint, on the **AnimGraph**, to control an individual bone, create IK chains, and other procedural, dynamic bone-driven animations.

![overview skeletal control nodes](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c333b115-2c6c-4188-b5e9-80607355ffb4/overview.png)

Skeletal Control nodes are structured similarly to other AnimBP nodes. The node can receive an animation pose through the **input pin** and generates a modified pose through the **output pin**. Most Skeletal Control nodes operate and compute transforms in the **Component Space**. Animation poses generated in **Component Space** calculate bone transforms relative to the [Skeletal Mesh Component](/documentation/en-us/unreal-engine/skeletal-mesh-assets-in-unreal-engine) of your character as opposed to the bone's Parent Bone. Component space pose pins appear as blue in the Anim Graph.

![skeletal control animation blueprint node with highlighted input and ouput pins component pose](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4f4ab242-c386-477f-92d0-1d03a96af957/inputoutput.png)

You can convert poses from Local Space to Component space with [space conversion nodes](/documentation/en-us/unreal-engine/animation-blueprint-component-space-conversion-in-unreal-engine).

![space conversion nodes](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/06a35cb1-def6-4ed0-afee-6fc57aa68653/overview.png)


Space Conversion nodes have an associated cost to your project's performance. It is recommended that space conversions occur as infrequently as possible by grouping specific space reliant functions together, near the final pose node when possible.

An **alpha value** is also common among Skeletal Control nodes. Similar to [Blend nodes](/documentation/en-us/unreal-engine/animation-blueprint-blend-nodes-in-unreal-engine) the alpha value controls the degree of applied modification to the source pose, when generating the new pose.

![skeletal control node with the alpha pin highlighted](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/86d8373e-627e-4e2c-8ae5-c36208b51a01/alpha.png)

In the case of Skeletal Control nodes, a float value between 0.0 and 1.0 is used as the alpha value to determine the weight of the applied Skeletal Transform. A value of 0.0 gives full weighting to the input pose, while a value of 1.0 gives full weighting to the control's computed Transform.

Within the **Details** panel of each Skeletal Control node, you can also set the **LOD Threshold** in which the node is considered. The value defined as the LOD Threshold will be the highest LOD level the Skeletal Control node will be used. Any higher [LOD levels](/documentation/en-us/unreal-engine/skeletal-mesh-lods-in-unreal-engine), (lower quality models), will ignore the Skeletal Control node.

![lod level of detail threshold property in details panel of skeletal control nodes](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/65dfde09-265e-4197-b652-e51e4349e916/lodthreshold.png)

By restricting the LOD level Skeletal Control nodes to compute bone transforms, you can reduce the performance cost of your animation system.

## Skeletal Control Nodes

Here you can reference additional documentation about each of the Skeletal Control Nodes you can use in your projects.

[![AnimDynamics](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/601c7883-7390-4ed5-b14a-412497c32fbe/topicimage.png)

AnimDynamics

Describes how the AnimDynamics AnimBP node can be used as a light-weight physics simulation solution that you can use to apply physics-based secondary animation to characters.](/documentation/en-us/unreal-engine/animation-blueprint-animdynamics-in-unreal-engine)
[![Apply a Percentage of Rotation](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e748c61e-f823-4407-b0dd-ca3772815c80/topicimage.png)

Apply a Percentage of Rotation

Describes how Apply a Percentage of Rotation drives the Rotation of a target bone with a specified percentage of the Rotation of another bone within the Skeleton.](/documentation/en-us/unreal-engine/animation-blueprint-apply-percent-of-rotation-in-unreal-engine)
[![Bone Driven Controller](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ebbb8f98-6982-42ec-be44-2b3d97d0b2fd/topicimage.png)

Bone Driven Controller

Describes the Bone Driven Controller node which allows a 'Driver' bone to dynamically affect the motion of a target object.](/documentation/en-us/unreal-engine/animation-blueprint-bone-driven-controller-in-unreal-engine)
[![CCDIK](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d8bde91d-66ab-4121-87d2-5fb01727b29e/topicimage.png)

CCDIK

Describes how to access and use the CCDIK Skeletal Control node to set up and control IK chains.](/documentation/en-us/unreal-engine/animation-blueprint-ccdik-in-unreal-engine)
[![Copy Bone](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3efb97b4-2e85-438c-8255-53b54572bc9f/topicimage.png)

Copy Bone

Describes the Copy Bone node which copies the Transform data or any component of it from one bone to another.](/documentation/en-us/unreal-engine/animation-blueprint-copy-bone-in-unreal-engine)
[![Hand IK Retargeting](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/71681b4c-ca5b-4c25-b76d-d16b8a436c50/topicimage.png)

Hand IK Retargeting

Describes the Hand IK Retargeting control which can be used to handle retargeting of IK bones.](/documentation/en-us/unreal-engine/animation-blueprint-hand-ik-retargeting-in-unreal-engine)
[![Look At](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3f8dd39c-1c7e-4994-a563-1918e7a6bf5f/topicimage.png)

Look At

Describes how the Look At control can be used to specify a bone to trace or follow another bone.](/documentation/en-us/unreal-engine/animation-blueprint-head-look-at-in-unreal-engine)
[![Modify Curve](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/02c87ba0-b3c2-48bd-b2cc-33d2bba14e73/topicimage.png)

Modify Curve

Describes the Modify Curve node which can be used to modify animation curves with arbitrary logic inside Animation Graphs.](/documentation/en-us/unreal-engine/animation-blueprint-modify-curve-in-unreal-engine)
[![Observe Bone](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/01c916fd-eb6c-4078-8822-96884ebb17d2/topicimage.png)

Observe Bone

Describes how you can debug a specified Bone with the Observe Bone node.](/documentation/en-us/unreal-engine/animation-blueprint-observe-bone-in-unreal-engine)
[![RigidBody](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/44231014-f6c1-45b5-ad2d-6d4bd4084163/topicimage.png)

RigidBody

Describes the RigidBody node and how it can be used as a lightweight physics simulation inside Animation Blueprints.](/documentation/en-us/unreal-engine/animation-blueprint-rigid-body-in-unreal-engine)
[![Spline IK](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f53a607b-e14a-4c6d-8ddc-0f276481c195/topicimage.png)

Spline IK

Describes how the Spline IK Solver node can be used for controlling character spines or bone chains within Animation Blueprints.](/documentation/en-us/unreal-engine/animation-blueprint-spine-ik-in-unreal-engine)
[![Spring Controller](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/03b5b8ef-d56e-4f76-86dc-e75445394a28/topicimage.png)

Spring Controller

Describes the Spring Controller which is used to limit how far a bone can stretch from its reference pose before force is applied in the opposite direction.](/documentation/en-us/unreal-engine/animation-blueprint-spring-controller-in-unreal-engine)
[![Trail Controller](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/858f0de0-0923-4b7d-9774-b482f2d01822/topicimage.png)

Trail Controller

Describes how the Trail Controller node can be used affect a chain of bones.](/documentation/en-us/unreal-engine/animation-blueprint-trail-controller-in-unreal-engine)
[![Transform Bone](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/65f21fd3-8052-446f-ad02-de1b1872409d/topicimage.png)

Transform Bone

Describes the Transform (Modify) Bone skeletal control node which can be used to modify the transform of a specified bone.](/documentation/en-us/unreal-engine/animation-blueprint-transform-bone-in-unreal-engine)
[![Twist Corrective](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/620aefe3-7a69-40d4-973f-dfbe1aed18b9/topicimage.png)

Twist Corrective

Describes how the Twist Corrective control can be used to drive curve values based on the twist of one bone relative to another.](/documentation/en-us/unreal-engine/animation-blueprint-twist-corrective-in-unreal-engine)
[![Two Bone IK](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ba1923a5-a4af-4e2a-ad53-061b7419cb1f/topicimage.png)

Two Bone IK

Describes how the Two Bone IK control can be used to apply IK to a 3-joint chain.](/documentation/en-us/unreal-engine/animation-blueprint-two-bone-ik-in-unreal-engine)

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [animation blending](https://dev.epicgames.com/community/search?query=animation%20blending)
* [skeletal controls](https://dev.epicgames.com/community/search?query=skeletal%20controls)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Skeletal Control Nodes](/documentation/en-us/unreal-engine/animation-blueprint-skeletal-controls-in-unreal-engine?application_version=5.7#skeletalcontrolnodes)
