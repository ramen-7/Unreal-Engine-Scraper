<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine?application_version=5.7 -->

# Animation Blueprints

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
7. Animation Blueprints

# Animation Blueprints

Animation Blueprints are visual scripts that are used for the creation and control of complex animation behaviors.

![Animation Blueprints](https://dev.epicgames.com/community/api/documentation/image/0ea00b74-4dd3-47c6-b8bd-2931369da39a?resizing_type=fill&width=1920&height=335)

 On this page

**Animation Blueprints** are specialized **Blueprints** that control the animation of a **Skeletal Mesh** during simulation or gameplay. **Graphs** are edited inside of the **Animation Blueprint Editor**, where you can blend animation, control the bones of a Skeleton, or create logic that will define the final animation pose for a Skeletal Mesh to use per frame.

This document provides an overview of how to create an Animation Blueprint, its editor, and its primary features.

#### Prerequisites

* Your project contains a [Skeletal Mesh](/documentation/en-us/unreal-engine/skeletal-mesh-actors-in-unreal-engine).

## Animation Blueprint Creation

You can create Animation Blueprints in the following ways:

In the **Content Browser**, click **Add (+)**, then select **Animation > Animation Blueprint**. You will then be prompted to specify which **Skeleton** to target for the Animation Blueprint. Select one and click **Create**.

![create animation blueprint](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6368083b-2787-4801-bf9f-2a60bc1e6952/create1.png)


For this creation method, you can optionally specify a **Template Animation Blueprint**, and **Parent Class**, if you are wanting to create a child Blueprint. For more information about templates, visit the [Animation Blueprint Linking](/documentation/en-us/unreal-engine/animation-blueprint-linking-in-unreal-engine) page.

Animation Blueprints can also be created by right-clicking on a **Skeletal Mesh Asset** in the **Content Browser** and selecting **Create > Anim Blueprint**.

![create animation blueprint](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ce31777e-98db-405a-a926-be56ff72fc98/create2.png)

Once created, double-click your new **Animation Blueprint** to open it in the **Animation Blueprint Editor**. To learn more about the interface, toolbar, and sections of this editor, refer to the [Animation Blueprint Editor](/documentation/en-us/unreal-engine/animation-blueprint-editor-in-unreal-engine) page.

[![Animation Blueprint Editor](images/static/document_list/empty_thumbnail.svg)

Animation Blueprint Editor

An overview of the Animation Blueprint Editor and its user interface.](/documentation/en-us/unreal-engine/animation-blueprint-editor-in-unreal-engine)

### Assigning to Characters

Animation Blueprints on their own will not affect your characters until you assign them. Typically this is done on the Skeletal Mesh of your character, regardless if it is referenced in a level or as a component in Blueprints.

To assign your Animation Blueprint, select your Skeletal Mesh and set the following properties:

* Set **Animation Mode** to **Use Animation Blueprint**.
* Set **Anim Class** to your Animation Blueprint asset.

![assign animation blueprint to character](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a7db83be-d012-4836-820b-154ba35fd181/assign1.png)

## Working with Animation Blueprints

There are several features and workflows available to you when using Animation Blueprints. From creating animation logic using the **AnimGraph**, to using **Linked Anim Instances**, Animation Blueprints provide a powerful suite of tools for you.

Reference the following pages to learn how to create robust Animation Blueprint logic for your characters.

[![Animation Blueprint Editor](images/static/document_list/empty_thumbnail.svg)

Animation Blueprint Editor

An overview of the Animation Blueprint Editor and its user interface.](/documentation/en-us/unreal-engine/animation-blueprint-editor-in-unreal-engine)
[![Graphing in Animation Blueprints](images/static/document_list/empty_thumbnail.svg)

Graphing in Animation Blueprints

Edit, blend, and manipulate poses on Skeletal Meshes using various graphs in Animation Blueprints.](/documentation/en-us/unreal-engine/graphing-in-animation-blueprints-in-unreal-engine)
[![State Machines](images/static/document_list/empty_thumbnail.svg)

State Machines

Create logic-based branching animation by using State Machines.](/documentation/en-us/unreal-engine/state-machines-in-unreal-engine)
[![Animation Node Reference](images/static/document_list/empty_thumbnail.svg)

Animation Node Reference

Descriptions of the various animation nodes available for use in Animation Blueprints.](/documentation/en-us/unreal-engine/animation-blueprint-nodes-in-unreal-engine)
[![Animation Slots](images/static/document_list/empty_thumbnail.svg)

Animation Slots

Insert entry-points within your Anim Graph to play animation from using Slots.](/documentation/en-us/unreal-engine/animation-slots-in-unreal-engine)
[![Sync Groups](images/static/document_list/empty_thumbnail.svg)

Sync Groups

Synchronize the cycles of animations with different lengths using Sync Groups.](/documentation/en-us/unreal-engine/animation-sync-groups-in-unreal-engine)
[![Animation Blueprint Linking](images/static/document_list/empty_thumbnail.svg)

Animation Blueprint Linking

Modularize your Animation Blueprint logic by using Animation Blueprint Linking and Templates.](/documentation/en-us/unreal-engine/animation-blueprint-linking-in-unreal-engine)

* [animation](https://dev.epicgames.com/community/search?query=animation)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisites](/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine?application_version=5.7#prerequisites)
* [Animation Blueprint Creation](/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine?application_version=5.7#animationblueprintcreation)
* [Assigning to Characters](/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine?application_version=5.7#assigningtocharacters)
* [Working with Animation Blueprints](/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine?application_version=5.7#workingwithanimationblueprints)
