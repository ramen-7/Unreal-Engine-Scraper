<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-create-control-rigs-in-unreal-engine?application_version=5.7 -->

# Control Rig Quick Start

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
6. [Control Rig](/documentation/en-us/unreal-engine/control-rig-in-unreal-engine "Control Rig")
7. Control Rig Quick Start

# Control Rig Quick Start

Learn the basic fundamentals of Control Rig in Unreal Engine.

![Control Rig Quick Start](https://dev.epicgames.com/community/api/documentation/image/b7ff099b-b5a6-4bf0-8004-0d574a8cd3d4?resizing_type=fill&width=1920&height=335)

 On this page

This page provides an overview of Control Rig, and shows how to create and animate rigs in Unreal Engine.

## What is a Control Rig?

Control Rig is Unreal Engine's solution to animating characters directly in the engine.

The **Control Rig Editor** is where you can create custom controls, channels, and other manipulators for your characters. After a rig is created, you can animate these controls within other areas of Unreal Engine, such as **[Sequencer](animating-characters-and-objects/Sequencer)**.

[![control rig editor overview](https://dev.epicgames.com/community/api/documentation/image/316c068c-51e6-4d0d-aea8-4b0bbfef697a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/316c068c-51e6-4d0d-aea8-4b0bbfef697a?resizing_type=fit)

Control Rigs require the creation of **Control Rig Assets**, which are created and stored in the **Content Browser**.

[![Control-rig-asset-content-browser](https://dev.epicgames.com/community/api/documentation/image/9177c05e-924e-4e6b-a4c3-34915ab916b0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9177c05e-924e-4e6b-a4c3-34915ab916b0?resizing_type=fit)

## How do I Create and Open a Control Rig?

The main way to create a new Control Rig asset is to right-click on a **[Skeletal Mesh](working-with-content/SkeletalMeshes)** in the Content Browser and select **Create > Control Rig**. This creates a Control Rig asset in the same directory with the postfix "\_CtrlRig".

[![create control rig](https://dev.epicgames.com/community/api/documentation/image/3c73c635-1ac1-43ed-98f9-a89edc1f2c6c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3c73c635-1ac1-43ed-98f9-a89edc1f2c6c?resizing_type=fit)

Next, double-click on the Control Rig asset to open the **Control Rig Editor**.

[![open control rig](https://dev.epicgames.com/community/api/documentation/image/1513445a-ab66-4c8e-8d13-9a5e378424a7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1513445a-ab66-4c8e-8d13-9a5e378424a7?resizing_type=fit)

## How do I Rig and Animate with Control Rig?

One of the simplest control types you can create is an **FK Control**. This guide gives an overview of how to create this control and animate it in **Sequencer**.

### Create Control

In the Control Rig Editor, select the **Rig Hierarchy** tab to view the skeleton hierarchy for your character. Navigate to the bone you want to animate, right-click it, and select **New Element > New Control**.

[![Create-new-control](https://dev.epicgames.com/community/api/documentation/image/e5b779c9-8918-44c7-9e04-ee0a1fd874e7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e5b779c9-8918-44c7-9e04-ee0a1fd874e7?resizing_type=fit)

This creates a control at the same location and orientation of the bone. The control is also named the same as the bone with the postfix "\_ctrl".

[![create new control](https://dev.epicgames.com/community/api/documentation/image/04df25db-6876-4e85-b42d-9ccfa25ceb5f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/04df25db-6876-4e85-b42d-9ccfa25ceb5f?resizing_type=fit)

Although you can keep the control nested within the skeleton hierarchy, it is best practice to remove it from the hierarchy and build your own control rig hierarchy adjacent to the skeleton. Select the control and press **Shift+P** to unparent the control from the skeleton.

[![unparent control](https://dev.epicgames.com/community/api/documentation/image/284efd06-e51c-4cf2-92ad-24521d6bb1c4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/284efd06-e51c-4cf2-92ad-24521d6bb1c4?resizing_type=fit)

### Edit Control Shape

In order to better see and select the control in the viewport, you can change the **Control Shape**. To do this, navigate to the **Details** panel and locate the **Shape** property category. Here you can set a new shape using the **Shape Properties**, as well as customize the scale and offset of it using the **Shape** **Transform** properties.

For this example, the shape is set to **Circle\_Thick**, Rotation Y is set to **90**, and all Scale axes are set to **3.0**.

[![change control shape](https://dev.epicgames.com/community/api/documentation/image/fcfea6c5-03ce-4fc6-afc3-fe90c90ec7d9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fcfea6c5-03ce-4fc6-afc3-fe90c90ec7d9?resizing_type=fit)

### Drive Bone with Control

Next, reference your control and bone in the **Rig Graph**. Do this by dragging the control from the **Rig Hierarchy** panel into the graph, then select **Get Control**.

[![get control graph](https://dev.epicgames.com/community/api/documentation/image/f0461ae1-f775-4929-b109-a371555141f4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f0461ae1-f775-4929-b109-a371555141f4?resizing_type=fit)

Do the same for the bone you want this control to affect. Drag the bone from the **Rig Hierarchy** panel into the graph, then select **Set Bone**.

[![set bone graph](https://dev.epicgames.com/community/api/documentation/image/e934eae8-6163-4945-a59d-89226ed100e0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e934eae8-6163-4945-a59d-89226ed100e0?resizing_type=fit)

Connect the **Transform** output data pin from the **Get Transform - Control** node to the **Value**input data pin of the **Set Transform - Bone** node, then connect the **Execute** output pin from the **Forwards Solve** node to the input execution pin of the **Set Transform - Bone** node.

[![set bone transform control](https://dev.epicgames.com/community/api/documentation/image/5637a331-f1ef-4f67-b7d4-da558a3b3490?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5637a331-f1ef-4f67-b7d4-da558a3b3490?resizing_type=fit)

You can now manipulate the control in the viewport and see the control driving the bone.

[![test control](https://dev.epicgames.com/community/api/documentation/image/233c2b8d-7536-4114-a12a-43d3e266a3c7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/233c2b8d-7536-4114-a12a-43d3e266a3c7?resizing_type=fit)

Clicking **Compile** resets the control position back to default.

### Animate Control in Sequencer

Now that your control is appropriately manipulating a character's bone, you can start to animate it in **[Sequencer](animating-characters-and-objects/Sequencer)**.

[![Animate-control-in-sequencer](https://dev.epicgames.com/community/api/documentation/image/7c0520e9-07c5-4b45-8eb8-eb411718d520?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7c0520e9-07c5-4b45-8eb8-eb411718d520?resizing_type=fit)

Drag the **Control Rig Asset** from the **Content Browser** into the Level viewport. Once this is done, Sequencer opens with the character added to it as a **[Track](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-track-list-in-unreal-engine)**.

Expand the **Control Rig** track to locate the controls you created. You can either select them here, or in the viewport.

[![control rig in sequencer](https://dev.epicgames.com/community/api/documentation/image/65269ed8-f1b7-40e2-9383-6708e70c381d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/65269ed8-f1b7-40e2-9383-6708e70c381d?resizing_type=fit)

With the control selected in the Viewport, press the **S** key to create a transform **Keyframe** for the selected control at the [Playhead](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine?application_version=5.5#playhead). Afterward, drag the **Playhead** to a different location in the sequence, manipulate your control, then press **S** again to set a second **Keyframe**.

Now when playing or scrubbing the sequence, you should see your control and character animate between the two keyframes.

[![keyframe control rig](https://dev.epicgames.com/community/api/documentation/image/8f42c997-f91c-4fe8-b3d9-e64667f8ad2a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8f42c997-f91c-4fe8-b3d9-e64667f8ad2a?resizing_type=fit)

* [control rig](https://dev.epicgames.com/community/search?query=control%20rig)
* [controls](https://dev.epicgames.com/community/search?query=controls)
* [ring](https://dev.epicgames.com/community/search?query=ring)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [What is a Control Rig?](/documentation/en-us/unreal-engine/how-to-create-control-rigs-in-unreal-engine?application_version=5.7#what-is-a-control-rig)
* [How do I Create and Open a Control Rig?](/documentation/en-us/unreal-engine/how-to-create-control-rigs-in-unreal-engine?application_version=5.7#how-do-i-create-and-open-a-control-rig)
* [How do I Rig and Animate with Control Rig?](/documentation/en-us/unreal-engine/how-to-create-control-rigs-in-unreal-engine?application_version=5.7#how-do-i-rig-and-animate-with-control-rig)
* [Create Control](/documentation/en-us/unreal-engine/how-to-create-control-rigs-in-unreal-engine?application_version=5.7#create-control)
* [Edit Control Shape](/documentation/en-us/unreal-engine/how-to-create-control-rigs-in-unreal-engine?application_version=5.7#edit-control-shape)
* [Drive Bone with Control](/documentation/en-us/unreal-engine/how-to-create-control-rigs-in-unreal-engine?application_version=5.7#drive-bone-with-control)
* [Animate Control in Sequencer](/documentation/en-us/unreal-engine/how-to-create-control-rigs-in-unreal-engine?application_version=5.7#animate-control-in-sequencer)
