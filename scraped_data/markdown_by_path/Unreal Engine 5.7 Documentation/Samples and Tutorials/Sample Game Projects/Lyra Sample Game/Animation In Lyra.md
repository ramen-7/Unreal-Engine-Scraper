<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-in-lyra-sample-game-in-unreal-engine?application_version=5.7 -->

# Animation In Lyra

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
5. [Samples and Tutorials](/documentation/en-us/unreal-engine/samples-and-tutorials-for-unreal-engine "Samples and Tutorials")
6. [Sample Game Projects](/documentation/en-us/unreal-engine/sample-game-projects-for-unreal-engine "Sample Game Projects")
7. [Lyra Sample Game](/documentation/en-us/unreal-engine/lyra-sample-game-in-unreal-engine "Lyra Sample Game")
8. Animation In Lyra

# Animation In Lyra

An overview of the Animation System in Lyra

![Animation In Lyra](https://dev.epicgames.com/community/api/documentation/image/99721f32-7c95-43e5-b7a8-e293b891a53a?resizing_type=fill&width=1920&height=335)

 On this page

**Lyra**'s character animations were created almost entirely in **Blueprints** using Unreal Engine 5's improvements to the [Animation Blueprint](/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine) system. The system setup is inspired by both Paragon and Fortnite, which achieve similar results through the use of custom C++ functionality.

# Asset Overview

The **AnimBP\_Mannequin\_Base** Animation Blueprint contains the [AnimGraph](/documentation/en-us/unreal-engine/graphing-in-animation-blueprints-in-unreal-engine) window, which you can use to observe the architecture of [Animation Nodes](/documentation/en-us/unreal-engine/animation-blueprint-nodes-in-unreal-engine) that contribute to the final output pose of the Character Mannequin.
You can navigate to this Animation Blueprint by clicking on the **Content Drawer** > **Characters** > **Heroes** > **Mannequin** > **Animations** > **AnimBP\_Mannequin\_Base**.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9136d99e-4136-4a45-97eb-f9c5cf4d18e0/baseoverview.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9136d99e-4136-4a45-97eb-f9c5cf4d18e0/baseoverview.png)

The Mannequin Base Animation Blueprint's AnimGraph and Blueprint Thread Safe Update Animation function.

The AnimBP\_Mannequin\_Base is set up to support common techniques that are used across the Lyra game's Sample Weapons and [Gameplay Abilities](/documentation/en-us/unreal-engine/abilities-in-lyra-in-unreal-engine).

### Blueprint ThreadSafe Update Animation

When developing animations for your character classes, there are some practices to be aware of to ensure your animations are running at optimal performance. In Lyra, we use [Multi Threaded Animation](/documentation/en-us/unreal-engine/animation-optimization-in-unreal-engine) to calculate animation values instead of the [Event Graph](/documentation/en-us/unreal-engine/animation-blueprint-event-nodes-in-unreal-engine) .

The **Animation Fast Path** helps you keep processes that calculate values outside of the Game Thread. You can enable this from the editor by navigating to **Edit** > **Project Settings** > **Engine** > **General Settings** > **Anim Blueprints,** then enabling **Allow Multi Threaded Animation Update**.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d9da7881-432b-47de-86cf-947f434bc626/multithreadsettings.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d9da7881-432b-47de-86cf-947f434bc626/multithreadsettings.png)

You can view the function responsible for gathering the animation data and processing these calculations by opening the **Class Defaults** of the **AnimBP\_Mannequin\_Base**, then navigating to the **My Blueprint** > **Functions** category and clicking the **BlueprintThreadSafeUpdateAnimation** function.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/14e40ea7-ac3a-4043-9981-030f8729810f/bpthreadfunction.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/14e40ea7-ac3a-4043-9981-030f8729810f/bpthreadfunction.png)

When using Thread Safe functions you can not access data directly from game objects as you could in the Event Graph. For example, if you were attempting to copy the Gameplay float value for the Character's speed it would not be considered thread-safe, therefore we recommend the use of Property Access to accommodate these instances.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f87dc0a6-ce25-4f86-b4da-ec7896f4708f/bpthreadupdatefunction.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f87dc0a6-ce25-4f86-b4da-ec7896f4708f/bpthreadupdatefunction.png)

### Anim Node functions

In Lyra, the state-specific logic is created by using Anim Node Functions. This has the benefit of keeping the Animation logic organized. If you need to calculate a value while the character is in the Idle Animation, then you can put that logic into the Idle state. To see an example follow the steps below:

1. Navigate to the **AnimBP\_Mannequin\_Base** > **Anim Graph** and double-click the **LocomotionSM** State Machine to open a window that displays the Locomotion states.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f4b8cfc6-523a-44d2-b0d3-c317e0d3db07/statemachine.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f4b8cfc6-523a-44d2-b0d3-c317e0d3db07/statemachine.png)

   The Locomotion State Machine includes State Aliases to transition between different Animation states.
2. You can double-click the **Idle** state and select the **Output Animation Pose** node, then under **Functions** in the **Details** panel, you can see the Anim Node Functions that provide a setup for the initial values of our nodes.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4b3418b1-75ce-4efb-bc45-4a2ca0acc2e2/functionnode.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4b3418b1-75ce-4efb-bc45-4a2ca0acc2e2/functionnode.png)

   In our example image, we opened the Idle state machine to view the Anim Node functions used in its Output Animation Pose.

   | Function | Description |
   | --- | --- |
   | **On Initial Update** | Called before the node is updated for the first time. |
   | **On Become Relevant** | Called when the node becomes relevant. |
   | **On Update** | Called when the node is updated. |
3. Navigate to **My Blueprint > Functions > State Node Functions** and double-click the **UpdateIdleState** function to view the logic used to calculate the final output pose of the Idle State locomotion node.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1bed2275-2ca1-4da0-99b1-1392d672a760/statenodefunction.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1bed2275-2ca1-4da0-99b1-1392d672a760/statenodefunction.png)



   In previous Engine versions, Legacy state machine events are fired after the animation update.

### State Aliases

As your projects begin to grow in size, you may have multiple animation states that your characters need to transition to. This can result in a State Machine with multiple transitional lines that can make it difficult to view in the Graph. State Aliases are used to simplify the transition logic while providing control over each individual transition between states. In Lyra, you can view an example of a State Alias being used by navigating to the **AnimBP\_Mannequin\_Base** > **Anim Graph** > **LocomotionSM** graph, then select the **JumpSources** state node.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9d97072d-9ce2-498d-ac3e-5ad49ac44486/jumpsources.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9d97072d-9ce2-498d-ac3e-5ad49ac44486/jumpsources.png)

The Locomotion State Machine graph with the Jump Sources node highlighted to observe the State Aliases available.

In the Details panel, you can view the Locomotion States which can directly transition to the Jump state.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a18f03bc-7723-4786-985a-4400a4383ce7/detailspanel.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a18f03bc-7723-4786-985a-4400a4383ce7/detailspanel.png)

When a Lyra Character is Idle, and the Player uses the Jump action, then the Lyra Character will enter into a jumping state. Eventually, they will transition into a falling state and then will either enter back into a cycle or idle state.

### Upper/Lower Body Layering

[BlendNodes](/documentation/en-us/unreal-engine/animation-blueprint-blend-nodes-in-unreal-engine) are used to blend animations together. Most of the locomotion animations used in Lyra are full body, meaning that the animation is playing on the entire skeleton (like the **jog\_fwd** animation), then they are combined with a variety of upper body actions that the player can use at any time (such as weapon fire or reload animations).

This is achieved through using the **Layered blend per bone** node, which you can view by opening the **AnimBP\_Mannequin\_Base** > **AnimGraph**, then navigating to the comment Upperbody/lowerbody split.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/01ccd883-6de4-4f52-90d7-590c816a1dd1/layeredblend.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/01ccd883-6de4-4f52-90d7-590c816a1dd1/layeredblend.png)

When you select the Layered blend per bone node, you can view the Details panel which includes Blend Masks that provide explicit control over the weight of individual bones involved with a blend.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3ad666d4-43e7-45be-90aa-b2a5c7e4bf24/blendmask.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3ad666d4-43e7-45be-90aa-b2a5c7e4bf24/blendmask.png)

## Linked Layer Animation Blueprint

The [Animation Blueprint Linking](/documentation/en-us/unreal-engine/using-animation-blueprint-linking-in-unreal-engine) system enables dynamic switching between different sub-sections on the Animation Graph. The main Animation Blueprint has multiple places where you can override the pose through Linked Layer Animation Blueprints.
In Lyra, this means that depending on which weapon the player is holding, you can have different locomotion behavior, animation assets, or pose corrections. You can keep their functionality separate and allow multiple users to work on the animation simultaneously, or reduce dependencies between assets while still sharing the same core functionality.

### Anim Layer Interface

**ALI\_ItemAnimLayers** is an Anim Layer Interface that specifies where you can override an animation in the Animation Blueprint. In Lyra, this is done for locomotion states in addition to layers for aiming and skeletal controls.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/61588c47-487a-4de9-8504-e780d51a40fc/fullbodyaiming.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/61588c47-487a-4de9-8504-e780d51a40fc/fullbodyaiming.png)

The FullBody\_Aiming animation layer, which is a part of the Item Anim Layers interface.

**ABP\_ItemAnimLayersBase** is the base Linked Layer Animation Blueprint that all of the weapons use. You can access this Blueprint from **Content** > **Characters** > **Heroes** > **Mannequin** > **Animations** > **LinkedLayers**.

### Accessing Data From the Main AnimBP

Inside of the **ABP\_ItemAnimLayersBase** Animation Blueprint there is a custom function **Get Main Anim BPThreadSafe**, that is used to get a reference to the main Animation Blueprint (**AnimBP\_Mannequin\_Base**).

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/87c0f6d4-be77-448a-8b58-7bc116414f20/mainthreadsafe.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/87c0f6d4-be77-448a-8b58-7bc116414f20/mainthreadsafe.png)

The Get Main Anim BPThreadSafe function as it appears in the Item Anim Layers Base Animation Blueprint.

This provides the use of Property Access to access all of its data and avoids having to re-calculate any values the linked layer may use like **Acceleration** or **Velocity**.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4952ef56-fefa-46f9-a642-23bfcf71d217/propertyaccess.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4952ef56-fefa-46f9-a642-23bfcf71d217/propertyaccess.png)

### Using Anim Node Functions for animation selection

In Lyra, **Linked Anim Layers** use **Property Access** along with Anim Node Functions to run logic when an animation updates (On Update) or becomes relevant (On Become Relevant).

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2c478849-465c-4719-9b10-9d36b8a4029e/animlayers.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2c478849-465c-4719-9b10-9d36b8a4029e/animlayers.png)

In the example below, we are choosing a directional start animation every time the animation becomes relevant.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1dc8bac6-fc42-450d-9dd1-c931b401df71/setupstart.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1dc8bac6-fc42-450d-9dd1-c931b401df71/setupstart.png)

### Linked Layer Child Animation Blueprint

In Lyra, every weapon has a Child Animation Blueprint that inherits from the **ABP\_ItemAnimLayersBase**. Animators can slot in animations and edit any variables per-weapon as seen in the image of the **ABP\_PistolAnimLayers** Animation Blueprint shown below.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6e5ca48d-eae3-4b9e-9643-5d050b1d5b00/layerchild.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6e5ca48d-eae3-4b9e-9643-5d050b1d5b00/layerchild.png)

## Distance Matching and Stride Warping

**Distance Matching** adjusts the playrate of an animation in instances where it is difficult to match the motion between Animation assets and Gameplay, for example locomotion animation assets like starts, stops, and landing animations.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d3201959-d415-4970-aeec-8bc9b210e3dd/distancematching.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d3201959-d415-4970-aeec-8bc9b210e3dd/distancematching.png)

Stride Warping is used to dynamically adjust the length of the character's stride in instances where the playrate adjustment will not, such as when the character enters into the Jog state.

|  |  |
| --- | --- |
| [undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/db2fcab9-6691-4bdd-9162-0e0692a5c70a/stridewarping.png) | stride-warp-motion |

By combining both of these techniques, you can dynamically choose to favor one technique over the other. During start states, we begin with using Distance Matching to preserve the pose, then blend in by using Stride Warping as we approach the Jog state.

![update-start-anim](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a3db66ee-dc0d-4841-b87e-69021d5e2987/updatestartanim.png)

## Orientation warping

Orientation Warping can be used with the root motion angle of a Character's movement and bend the lower body of a Character to match the angle. In Lyra, Strafe animations are created for four cardinal directions, because the player can move with 360 degrees of freedom, we use Orientation Warping to procedurally adjust their pose. This technique is used during starts because we have limited animation coverage.

![orientation-warping](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6a49ef9d-b4fb-4554-a181-86ab51f53cc9/orientationwarping.gif)

## Turn in place

Turn in place animation selection is done from inside Lyra's base Linked Animation Blueprint's Idle state machine. Different animations that are based on the turn angle, and how long the player waits before triggering them can be customized in the per-weapon Anim Set section of the Child Anim Blueprints by navigating to the **Class Defaults** > **Anim Set - Turn In Place** > **Turn In Place Transitions**.

![turn-in-place](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ff860a20-147e-4363-9005-5ef18e91cccc/turninplace.gif)

In Lyra, the Character Actor is oriented to the Controller's yaw. To minimize foot sliding, a counter to the rotation is used by a Rotate Root Bone node and is offset by the Root Yaw Offset.

![counter-controller-yaw](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/060e2806-7a9c-4ed8-b31d-6df784c5bc3b/controlleryaw.png)

This additional offset is used when passing the yaw values to the Aim Offset in the FullBody Aiming layer. Depending on what action the player is doing, we want to allow the Root Yaw Offset to change its mode to one of the following states from the table below.

| Offset Mode | Description |
| --- | --- |
| **Accumulate** | During idles, Accumulate will completely counter the Actor's rotation. |
| **Hold** | During starts, Hold will preserve whichever original offset this animation started with |
| **Blend Out** | When going into a jog cycle, Blend Out will smoothly blend it, and follow the default "orient to controller" behavior. |

This is done with a **Request Root Yaw Offset Mode** function that each of the states can call when needed.

![request-root-yaw-offset-mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ee384c14-987c-4ad6-bb6f-983f92fb9ef9/requestroot.png)

When a character is idle and the offset mode is set to Accumulate, then we want to apply the animation's root rotation to the Root Yaw Offset. This information is baked into curves using the **Turn Yaw Anim Modifier**, and it requires the source animation to have Root Motion enabled.

![turn-yaw-anim](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9a9b2761-da05-4be7-996c-843650a8dfaa/turnyawanim.png)

## Additional Notes

### Gameplay Tag Bindings

Lyra uses the [Gameplay Ability System](/documentation/en-us/unreal-engine/gameplay-ability-system-for-unreal-engine) for most of the player's actions. You can respond to these events in the Animation Blueprint by using Gameplay Tag Bindings. You can navigate to the Gameplay Tags inside the **AnimBP\_Mannequin\_Base** Blueprint from the **Class Defaults** > **Details** > **Gameplay Tags** > **Gameplay Tag Property Map**.

![gameplay-tags](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0dddae0e-11a1-4d1f-abea-d736dd96e4b3/gameplaytags.png)

### Montages

Montages have been updated to support [Blend Profiles](/documentation/en-us/unreal-engine/blend-masks-and-blend-profiles-in-unreal-engine#blendprofiles) and [Inertialization](/documentation/en-us/unreal-engine/animation-blueprint-blend-nodes-in-unreal-engine#inertialization).

Enabling Both simultaneously is currently not supported in 5.0.

![montages](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f667b377-e815-4a31-960e-2ab501c01049/montages.png)

### Notifies

Additional Animation Notify information has been exposed to State Machine transitions. In Lyra, we use this to control precise timing on when we can transition out of specific states.

![state-machine-notify](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/44afaba0-bb6e-49ad-ae9e-2eb4fc232921/statemachinenotify.png)

### Debugging

By using the Pose Watch Manager, you can add pose watches to specific points on the graph to inspect the runtime poses and quickly navigate to them. You can navigate to **Window** > **Pose Watch Manager** to open the Pose Watch Manager.

![pose-watch-manager](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/af86ee85-da43-4bfe-aed0-402b441e8b78/posewatchmanager.png)

For debugging, you can use the [Rewind Debugger](/documentation/en-us/unreal-engine/animation-rewind-debugger-in-unreal-engine) , in addition to the tips and tricks located on the [Animation Productivity Tips And Tricks](/documentation/en-us/unreal-engine/animation-shortcuts-and-tips-unreal-engine) page.

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [lyra](https://dev.epicgames.com/community/search?query=lyra)
* [pose warping](https://dev.epicgames.com/community/search?query=pose%20warping)
* [stride warping](https://dev.epicgames.com/community/search?query=stride%20warping)
* [motion blend](https://dev.epicgames.com/community/search?query=motion%20blend)
* [animation blueprints](https://dev.epicgames.com/community/search?query=animation%20blueprints)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Asset Overview](/documentation/en-us/unreal-engine/animation-in-lyra-sample-game-in-unreal-engine?application_version=5.7#assetoverview)
* [Blueprint ThreadSafe Update Animation](/documentation/en-us/unreal-engine/animation-in-lyra-sample-game-in-unreal-engine?application_version=5.7#blueprintthreadsafeupdateanimation)
* [Anim Node functions](/documentation/en-us/unreal-engine/animation-in-lyra-sample-game-in-unreal-engine?application_version=5.7#animnodefunctions)
* [State Aliases](/documentation/en-us/unreal-engine/animation-in-lyra-sample-game-in-unreal-engine?application_version=5.7#statealiases)
* [Upper/Lower Body Layering](/documentation/en-us/unreal-engine/animation-in-lyra-sample-game-in-unreal-engine?application_version=5.7#upper/lowerbodylayering)
* [Linked Layer Animation Blueprint](/documentation/en-us/unreal-engine/animation-in-lyra-sample-game-in-unreal-engine?application_version=5.7#linkedlayeranimationblueprint)
* [Anim Layer Interface](/documentation/en-us/unreal-engine/animation-in-lyra-sample-game-in-unreal-engine?application_version=5.7#animlayerinterface)
* [Accessing Data From the Main AnimBP](/documentation/en-us/unreal-engine/animation-in-lyra-sample-game-in-unreal-engine?application_version=5.7#accessingdatafromthemainanimbp)
* [Using Anim Node Functions for animation selection](/documentation/en-us/unreal-engine/animation-in-lyra-sample-game-in-unreal-engine?application_version=5.7#usinganimnodefunctionsforanimationselection)
* [Linked Layer Child Animation Blueprint](/documentation/en-us/unreal-engine/animation-in-lyra-sample-game-in-unreal-engine?application_version=5.7#linkedlayerchildanimationblueprint)
* [Distance Matching and Stride Warping](/documentation/en-us/unreal-engine/animation-in-lyra-sample-game-in-unreal-engine?application_version=5.7#distancematchingandstridewarping)
* [Orientation warping](/documentation/en-us/unreal-engine/animation-in-lyra-sample-game-in-unreal-engine?application_version=5.7#orientationwarping)
* [Turn in place](/documentation/en-us/unreal-engine/animation-in-lyra-sample-game-in-unreal-engine?application_version=5.7#turninplace)
* [Additional Notes](/documentation/en-us/unreal-engine/animation-in-lyra-sample-game-in-unreal-engine?application_version=5.7#additionalnotes)
* [Gameplay Tag Bindings](/documentation/en-us/unreal-engine/animation-in-lyra-sample-game-in-unreal-engine?application_version=5.7#gameplaytagbindings)
* [Montages](/documentation/en-us/unreal-engine/animation-in-lyra-sample-game-in-unreal-engine?application_version=5.7#montages)
* [Notifies](/documentation/en-us/unreal-engine/animation-in-lyra-sample-game-in-unreal-engine?application_version=5.7#notifies)
* [Debugging](/documentation/en-us/unreal-engine/animation-in-lyra-sample-game-in-unreal-engine?application_version=5.7#debugging)
