<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/rigging-with-control-rig-in-unreal-engine?application_version=5.7 -->

# Rigging with Control Rig

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
7. Rigging with Control Rig

# Rigging with Control Rig

Start rigging by creating a Control Rig Asset and learning about its various features.

![Rigging with Control Rig](https://dev.epicgames.com/community/api/documentation/image/8e306673-5cb5-44dd-b5ca-24f653573d2e?resizing_type=fill&width=1920&height=335)

 On this page

In order to animate characters in Unreal Engine, you must first create controls for it. Control Rig contains various features and tools to create unique rigs for characters of all shapes and sizes.

This page provides an overview of creating Control Rigs, and the primary features of rigging.

## Create Control Rig Asset

You can view the **Control Rig Editor** when you open a **Control Rig Asset** from the [Content Browser](/documentation/en-us/unreal-engine/content-browser-in-unreal-engine). This Asset can be created in the following ways.

In the first method you can right-click on your Skeletal Mesh Asset and select **Create > Control Rig**. This creates a Control Rig Asset in the same directory with the postfix `_CtrlRig`. Double click the Asset to open it.

![create control rig](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/66a9442a-82dd-453a-ad1c-464da660eb58/createcontrolrig.png)

The second method is to create a Control Rig manually. You can do this by clicking in the Content Browser and selecting **Animation > Control Rig**. Next, in the pop-up window, select **ControlRig** and click **Create**. Double click the Asset to open it.

![create control rig](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/37731880-a60d-4254-a356-dcbca0474aae/createcontrolrig2.png)


If you create a Control Rig this way, you will need to manually assign the Skeletal Mesh to your Control Rig Asset after opening. This is done by clicking **Import Hierarchy** in the **Rig Hierarchy** tab, then specifying your Skeletal Mesh.

![import hierarchy](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/008421d2-8bb7-49ce-8df7-687dc9a694c2/importhierarchy.png)

Refer to the [Control Rig Editor](/documentation/en-us/unreal-engine/control-rig-editor-in-unreal-engine) page to learn more about the Control Rig Editor's interface and features.

## Rigging Features

The following features are available to help you rig your Control Rig in Unreal Engine.

[![Control Rig Editor](images/static/document_list/empty_thumbnail.svg)

Control Rig Editor

Learn about the various tools and areas in the Control Rig Editor.](/documentation/en-us/unreal-engine/control-rig-editor-in-unreal-engine)
[![Modular Control Rigs](images/static/document_list/empty_thumbnail.svg)

Modular Control Rigs

Use Modular Rigging tools to quickly rig characters in Unreal Engine.](/documentation/en-us/unreal-engine/modular-control-rigs-in-unreal-engine)
[![Controls, Bones, and Nulls](images/static/document_list/empty_thumbnail.svg)

Controls, Bones, and Nulls

Learn about the primary Rig Elements you can use for constructing Control Rigs.](/documentation/en-us/unreal-engine/controls-bones-and-nulls-in-control-rig-in-unreal-engine)
[![Solve Directions](images/static/document_list/empty_thumbnail.svg)

Solve Directions

Learn about the different solve directions in Control Rig and the features they enable.](/documentation/en-us/unreal-engine/control-rig-forwards-solve-and-backwards-solve-in-unreal-engine)
[![Full-Body IK](images/static/document_list/empty_thumbnail.svg)

Full-Body IK

Build Full Body IK systems for your character.](/documentation/en-us/unreal-engine/control-rig-full-body-ik-in-unreal-engine)
[![Spline Rigging](images/static/document_list/empty_thumbnail.svg)

Spline Rigging

Utilize Splines in your Control Rig to achieve easier procedural animation on long joint chains.](/documentation/en-us/unreal-engine/control-rig-spline-rigging-in-unreal-engine)
[![Pose Caching](images/static/document_list/empty_thumbnail.svg)

Pose Caching

Save bone poses and states to reference in your Control Rig graph.](/documentation/en-us/unreal-engine/control-rig-pose-caching-in-unreal-engine)
[![Control Shapes and Control Shape Library](images/static/document_list/empty_thumbnail.svg)

Control Shapes and Control Shape Library

Customize your controls using different control shapes from the Control Shape Library.](/documentation/en-us/unreal-engine/control-shapes-and-control-shape-library-in-unreal-engine)
[![Control Rig Component](images/static/document_list/empty_thumbnail.svg)

Control Rig Component

Use Control Rig in Blueprints using the Control Rig Component.](/documentation/en-us/unreal-engine/control-rig-in-blueprints-in-unreal-engine)
[![Control Rig Function Libraries](images/static/document_list/empty_thumbnail.svg)

Control Rig Function Libraries

Construct and reference public Control Rig functions to speed up your rigging workflows.](/documentation/en-us/unreal-engine/control-rig-function-libraries-in-unreal-engine)
[![Python Scripting for Rigging with Control Rig](images/static/document_list/empty_thumbnail.svg)

Python Scripting for Rigging with Control Rig

Extend and customize the Control Rig Rigging process using Python scripting.](/documentation/en-us/unreal-engine/control-rig-python-scripting-in-unreal-engine)
[![Control Rig Debugging](images/static/document_list/empty_thumbnail.svg)

Control Rig Debugging

Find and fix issues inside the Control Rig graph using Control Rig Debugging tools.](/documentation/en-us/unreal-engine/control-rig-debugging-in-unreal-engine)

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [control rig](https://dev.epicgames.com/community/search?query=control%20rig)
* [rigging](https://dev.epicgames.com/community/search?query=rigging)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Create Control Rig Asset](/documentation/en-us/unreal-engine/rigging-with-control-rig-in-unreal-engine?application_version=5.7#createcontrolrigasset)
* [Rigging Features](/documentation/en-us/unreal-engine/rigging-with-control-rig-in-unreal-engine?application_version=5.7#riggingfeatures)
