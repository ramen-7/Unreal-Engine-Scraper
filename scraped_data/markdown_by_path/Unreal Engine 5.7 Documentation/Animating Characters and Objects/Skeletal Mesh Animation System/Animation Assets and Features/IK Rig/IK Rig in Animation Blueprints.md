<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/ik-rig-in-animation-blueprints-in-unreal-engine?application_version=5.7 -->

# IK Rig in Animation Blueprints

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
8. [IK Rig](/documentation/en-us/unreal-engine/unreal-engine-ik-rig "IK Rig")
9. IK Rig in Animation Blueprints

# IK Rig in Animation Blueprints

Use IK Rig in Animation Blueprints to create procedural IK adjustment of your character in gameplay.

![IK Rig in Animation Blueprints](https://dev.epicgames.com/community/api/documentation/image/08223718-f308-470a-b661-3c3d2d663385?resizing_type=fill&width=1920&height=335)

 On this page

Once your **IK Rig** is created, you can reference it within [Animation Blueprints](/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine) to use its IK behavior in gameplay.

This document provides an overview of this process, and the various features available to you.

#### Prerequisites

* You have created an IK Rig for a **Skeletal Mesh**. Refer to the [IK Rig Editor](/documentation/en-us/unreal-engine/ik-rig-in-unreal-engine) page for example setup instructions.
* Your Skeletal Mesh has an **Animation Blueprint**, which the [Third Person Template](/documentation/404) project provides if you do not have one.
* You have a basic understanding of using [Animation Blueprints](/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine).

## Setup

IK Rigs are referenced in Animation Blueprints from the AnimGraph panel. Right-click in the **graph** and select **IK Rig** from the **Misc** category to create an IK Rig node.

![ik rig blueprint node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/354ca69b-2b57-4a5b-adb4-3533db66c55e/setup1.png)

Once added, you will need to assign your IK Rig to the **Rig Definition Asset** property in the **Details** panel.

![ik rig definition asset](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9a102cb0-7da4-491f-903e-7699f71986fb/setup2.png)

In common setups the IK Rig node is placed after most of your locomotion and other AnimBP logic. This is so that IK adjustments can occur correctly in sequence after other effects.

![ik rig node graph placement](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8df0fd23-8428-44cf-8f5a-71a05948981f/setup3.png)

## Usage

By default the IK Rig will not cause any change in your animation pose. In order to affect IK changes from the node you need to expose an IK Goal's position, rotation, or both.

To do this, select an **IK Goal** in the **IK Rig editor** and enable **Expose Position** and **Expose Rotation** in the **Details** panel. This will add pins for that goal's position or rotation on the IK Rig node, and expose the goal for manipulation.

![expose position expose rotation](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d43755f6-8fb9-4e39-b3a4-b38373298eb8/usage1.png)

From here you can create **Variables** for these properties and build logic that manipulates your IK Rig.

You can test the behavior of the IK Rig in the Animation Blueprint by adjusting either the **Goal Position** or **Rotation** pin values.

![ik rig node adjust ik position](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8a379680-5705-4f0b-a8c1-55595e29e0e1/usage2.png)

Editing the **Position / Rotation Alpha** will blend the IK effect on/off for that goal on the respective axis.

![position rotation alpha](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dadca970-29df-4733-8807-df36475abebd/usage3.gif)

## Properties

Selecting the IK Rig node reveals the following IK Rig-specific properties in the Details panel:

![ik rig node properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7a72b90e-9b81-4d05-88ad-eee95ecea49a/properties.png)

| Name | Description |
| --- | --- |
| **Goals** | The property section will populate for each IK Goal that is exposed, and provide you with additional settings to control its behavior. You can specify a goal to be one of the following types:   * **Manual Input**, which exposes the Position and Rotation pins on the node for manual control of the goal's transform. You can also choose the position or rotation space that is applied to the goal:   + **Additive**, which treats the goal transform as a world-space additive offset relative to the to the Bone at the effector.   + **Component**, which treats the goal transform as being in the space of the Skeletal Mesh Actor Component.   + **World**, which treats the goal transform as being in world space. * **Bone**, where you can specify a Bone within this skeleton for the goal to snap to. This can be useful when using auxiliary Bones, like weapon or prop Bones, which may procedurally adjust. ik goal bone |
| **Rig Definition Asset** | The IK Rig Asset to modify the incoming pose. |
| **Start from Ref Pose** | Enabling this ignores the incoming pose and instead starts the solve using the Skeletal Mesh reference pose. |
| **Enable Debug Draw** | This enables the visibility of all IK Goals within the Viewport for debugging and preview. enable debug draw |
| **Debug Scale** | Increases or decreases the scale of the IK Rig debug draw, if Enable Debug Draw is enabled. |

* [animation](https://dev.epicgames.com/community/search?query=animation)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisites](/documentation/en-us/unreal-engine/ik-rig-in-animation-blueprints-in-unreal-engine?application_version=5.7#prerequisites)
* [Setup](/documentation/en-us/unreal-engine/ik-rig-in-animation-blueprints-in-unreal-engine?application_version=5.7#setup)
* [Usage](/documentation/en-us/unreal-engine/ik-rig-in-animation-blueprints-in-unreal-engine?application_version=5.7#usage)
* [Properties](/documentation/en-us/unreal-engine/ik-rig-in-animation-blueprints-in-unreal-engine?application_version=5.7#properties)
