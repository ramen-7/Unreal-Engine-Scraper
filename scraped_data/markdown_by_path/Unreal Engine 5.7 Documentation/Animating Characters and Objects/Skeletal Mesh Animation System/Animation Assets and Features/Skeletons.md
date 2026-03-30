<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletons-in-unreal-engine?application_version=5.7 -->

# Skeletons

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
8. Skeletons

# Skeletons

Learn about Skeletons, Bones, and animation data management in Unreal Engine.

![Skeletons](https://dev.epicgames.com/community/api/documentation/image/b370232a-91f5-4ff8-ac41-6787f7f32135?resizing_type=fill&width=1920&height=335)

 On this page

A **Skeleton** is a hierarchy that is used to define **Bones** (sometimes called **joints**) in a [Skeletal Mesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-actors-in-unreal-engine). In some ways, these Bones mimic a real biological skeleton due to their position and control over how characters deform.

In Unreal Engine, Skeletons are used to store and associate animation data, the overall skeletal hierarchy, and [Animation Sequences](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-sequences-in-unreal-engine). Skeleton Assets can also be shared through a variety of methods, enabling for additional animations and data to be shared between different Skeletons.

This document provides an overview of how to create and use Skeletons.

#### Prerequisites

* Your project contains a [Skeletal Mesh Actor](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-actors-in-unreal-engine), or you have a skinned FBX character to import into Unreal Engine.

## Creating Skeletons

The primary way to create a Skeleton is to [import](https://dev.epicgames.com/documentation/en-us/unreal-engine/importing-skeletal-meshes-using-fbx-in-unreal-engine) a skinned character FBX, which then converts to a **Skeletal Mesh** in Unreal Engine. When importing a Skeletal Mesh, in the [FBX Import Options](https://dev.epicgames.com/documentation/en-us/unreal-engine/fbx-import-options-reference-in-unreal-engine) window, leaving the **Skeleton** field empty will automatically create a Skeleton Asset based on the skinned character being imported.

[![import skeletal mesh](https://dev.epicgames.com/community/api/documentation/image/1860201f-7f79-4544-9def-d4343d0d6c35?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1860201f-7f79-4544-9def-d4343d0d6c35?resizing_type=fit)

After importing your character, the **Skeleton Asset** will be created along with other Skeletal Mesh Assets.

[![skeleton asset](https://dev.epicgames.com/community/api/documentation/image/af6caf6a-5b5c-426f-8ed9-576e4e62f910?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/af6caf6a-5b5c-426f-8ed9-576e4e62f910?resizing_type=fit)

You can also create a copy of a Skeleton from any Skeletal Mesh by right-clicking on it in the **Content Browser** and selecting **Skeleton > Create Skeleton**. This creates a new Skeleton associated with an existing mesh. If that mesh had another Skeleton associated with it, it will re-link to the new Skeleton and any animations will then link to the new Skeleton.

[![create skeleton copy](https://dev.epicgames.com/community/api/documentation/image/08921957-56ff-46b7-a53c-a16453d95d8e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/08921957-56ff-46b7-a53c-a16453d95d8e?resizing_type=fit)

Double-click the Skeleton Asset to open the [Skeleton Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeleton-editor-in-unreal-engine).

[![skeleton editor](https://dev.epicgames.com/community/api/documentation/image/39338a8a-cf34-4791-85de-41d24a4a3da9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/39338a8a-cf34-4791-85de-41d24a4a3da9?resizing_type=fit)

## Skeleton Tree Information

Bones and other items displayed in the [Skeleton Tree](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeleton-editor-in-unreal-engine) can appear different depending on several factors.

| Icon | Description |
| --- | --- |
|  | A normal Bone that influences vertices on the Skeletal Mesh. |
|  | A Bone in the current Skeleton that doesn't influence vertices on the Skeletal Mesh. These Bones are typically used in an auxiliary manner, such as for attaching weapons or props, while still being animatable as a Bone. |
|  | A [Socket](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-sockets-in-unreal-engine), which is a static point that acts as an offset attachment point for Bones. |
|  | A [Virtual Bone](https://dev.epicgames.com/documentation/en-us/unreal-engine/virtual-bones-in-unreal-engine), which is a Bone that follows the transforms of another Bone, but in a different Bone space. These are useful for locking down unwanted joint movements, and are used in conjunction with [IK](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprint-two-bone-ik-in-unreal-engine). |
|  | A Bone that exists in the Skeleton, but is not used by the current Skeletal Mesh. This can happen if you have [merged](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletons-in-unreal-engine) Skeletons, or are previewing different LODs on this Skeleton that are not using certain Bones. |

## Animation Data Storage

In addition to controlling animation, Skeletons in Unreal Engine also store animation-specific data. When data is created from those sources, such as creating an [Animation Notify](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-notifies-in-unreal-engine) in an Animation Sequence, it gets added to the Skeleton as shared data.

Skeletons store the following types of animation data:

* [Animation Notifies](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-notifies-in-unreal-engine).
* [Animation Curves](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curves-in-unreal-engine).
* [Slots](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-slots-in-unreal-engine).
* [Retarget Sources](https://dev.epicgames.com/documentation/en-us/unreal-engine/retarget-manager-in-unreal-engine).
* [Blend Profiles and Blend Masks](https://dev.epicgames.com/documentation/en-us/unreal-engine/blend-masks-and-blend-profiles-in-unreal-engine).

This data can be viewed in dedicated tool panels by clicking **Window** in the Skeleton Editor menu, then enabling one or more of these panels.

[![animation data panels](https://dev.epicgames.com/community/api/documentation/image/414c1977-a8fd-4328-bfda-04f6e83f479e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/414c1977-a8fd-4328-bfda-04f6e83f479e?resizing_type=fit)

## Sharing Skeletons

An important feature of Skeleton Assets is that a single Skeleton Asset can be used by multiple Skeletal Meshes, so long as the Skeletal Meshes use the same general rig hierarchy. This means that the names and hierarchical order of your Bones must be consistent in order for sharing to work correctly.

For example, consider a limb with three Bones in a Skeletal Mesh. The bones are named **1**, **2**, and **3**:

[![sharing skeleton example 1](https://dev.epicgames.com/community/api/documentation/image/b06107b9-d22d-42fc-b96a-0994f88d605b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b06107b9-d22d-42fc-b96a-0994f88d605b?resizing_type=fit)

If you want to share this Skeleton with another Skeletal Mesh, you will need to keep these Bones in the same order and with the same names. The second Skeletal Mesh, however, can contain Bones that are additions or peripheral to the hierarchy. Any time animation data is received for a Bone that is not included in the Skeletal Mesh, that animation data will be ignored.

In that case, your new hierarchy could look like the image below. Here, the second Skeletal Mesh has extra Bones, while still retaining and not interfering with the original hierarchy from the first Skeletal Mesh.

[![sharing skeleton example 2](https://dev.epicgames.com/community/api/documentation/image/a3b49396-4c79-49ab-9172-40e6b36f2f44?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a3b49396-4c79-49ab-9172-40e6b36f2f44?resizing_type=fit)

However, in order for both Skeletal Meshes to use the same Skeleton Asset, you cannot change the hierarchy order or rename the Bones. If a second Skeletal Mesh uses a different Bone hierarchy and naming structure, you will need to create a new Skeleton Asset.

[![sharing skeleton example 3](https://dev.epicgames.com/community/api/documentation/image/b5822c1c-67c2-441b-9f75-d51226cffeda?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b5822c1c-67c2-441b-9f75-d51226cffeda?resizing_type=fit)

If you insert a bone into the hierarchy without changing the order, you will be able to share successfully. However in most cases the extra bone may cause unintended transform offsets in your skeleton. It is recommended that you avoid this if possible.

[![sharing skeleton example 4](https://dev.epicgames.com/community/api/documentation/image/f59c6a74-174d-42e8-a36e-e31eb29ae828?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f59c6a74-174d-42e8-a36e-e31eb29ae828?resizing_type=fit)

Taking these sharing rules into account, there are several ways you can share Skeletons between Skeletal Meshes in Unreal Engine. These are detailed below.

### Merging during Import

The first method for sharing Skeletons is done during the FBX import process. When importing your new Skeletal Mesh (with additional and peripheral Bones compliant with the rules above), you can select a Skeleton from a Skeletal Mesh that already exists in your project. Unreal Engine will then merge the Skeletons, appending any new Bones into the hierarchy. Additionally, your Skeleton's proportions will be defined by the original Skeletal Mesh from which it was created.

[![merge sharing](https://dev.epicgames.com/community/api/documentation/image/b8b1fbb7-509d-4e37-b8da-ffe7bc4bec0d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b8b1fbb7-509d-4e37-b8da-ffe7bc4bec0d?resizing_type=fit)

If you are importing a Skeleton that is vastly different from the Skeleton you are attempting to merge to and breaks any sharing rules, you will see an error message:

[![failed to merge bones](https://dev.epicgames.com/community/api/documentation/image/d96a0b6c-5f50-4c61-9d18-413e9385e1f7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d96a0b6c-5f50-4c61-9d18-413e9385e1f7?resizing_type=fit)

In this case, you may need to create a new Skeleton Asset for the Skeletal Mesh you are importing, rather than merge into an existing one.

When viewing your merged Skeleton, you will see these additional Bones listed in your hierarchy, but they will only be visible and active for the Skeletal Mesh they are intended for.

|  |  |
| --- | --- |
|  |  |
| Skeletal Mesh Variant 1 | Skeletal Mesh Variant 2 |

### Compatible Skeletons

Additionally, skeletons can non-destructively share animation assets by defining other skeletons as compatible. Compatible skeletons can share [Animation Sequences](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-sequences-in-unreal-engine), [Montages](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-montage-in-unreal-engine), [Animation Blueprints](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine), and more.

To define another skeleton as compatible for a character, open the character's skeleton asset in the [Skeleton Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeleton-editor-in-unreal-engine), and then open the **Retarget Manager** by clicking the button in the **Toolbar**.

[![compatible skeletons](https://dev.epicgames.com/community/api/documentation/image/05ade0b6-4518-4afb-8fd0-09bdf27bcf88?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/05ade0b6-4518-4afb-8fd0-09bdf27bcf88?resizing_type=fit)

In the **Retarget Manager**, locate the **Manage Compatible Skeletons** section of the **Retarget Sources** panel and click **Add Skeleton** to select another skeleton asset in your project using the context menu.

[![add compatible skeleton](https://dev.epicgames.com/community/api/documentation/image/11332bc4-1d5a-4564-b16d-82955a981dfe?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/11332bc4-1d5a-4564-b16d-82955a981dfe?resizing_type=fit)

Now, animations can be shared from the Skeleton that was added to the **Manage Compatible Sources** list.

[![compatible skeletons](https://dev.epicgames.com/community/api/documentation/image/407efd6f-e84d-4823-9c0e-81bb849b0555?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/407efd6f-e84d-4823-9c0e-81bb849b0555?resizing_type=fit)

Skeleton compatibility is bi-directional. If you set Skeleton 1 to be compatible with Skeleton 2, that also means that Skeleton 2 is now compatible with Skeleton 1.

Creating and managing a system of compatible skeletons can be an effective way to optimize the number of animation assets your project requires to animate multiple characters. However, in order to utilize the Compatible Skeletons system, all characters must have nearly identical skeleton hierarchy structures and naming conventions. Additionally, all characters must have similar mesh proportions to achieve ideal results.

To share animations across characters with the same skeleton structure but with different proportions see the [Animation Retargeting](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-retargeting-in-unreal-engine) documentation.

To rebuild animation sequences to work across characters with radically different skeleton structures, see the [IK Rig Retargeting](https://dev.epicgames.com/documentation/en-us/unreal-engine/ik-rig-animation-retargeting-in-unreal-engine) documentation.

## Skeleton Features

Skeletons in Unreal Engine support a variety of features for attaching, blending, and other settings. Refer to the following pages to learn more about these features:

* [![Animation Retargeting](https://dev.epicgames.com/community/api/documentation/image/e4882091-5f4e-4b17-aee4-917b02e6dce8?resizing_type=fit&width=640&height=640)

  Animation Retargeting

  Describes how retargeted animations can be used with multiple Skeletal Meshes, allowing you to share animations.](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-retargeting-in-unreal-engine)
* [![Blend Masks and Blend Profiles](https://dev.epicgames.com/community/api/documentation/image/cee21598-256e-4bf9-91f5-1406a547366d?resizing_type=fit&width=640&height=640)

  Blend Masks and Blend Profiles

  Exclude Bones or change their individual blend speed by using Blend Masks and Blend Profiles.](https://dev.epicgames.com/documentation/en-us/unreal-engine/blend-masks-and-blend-profiles-in-unreal-engine)
* [![Skeletal Mesh LODs](https://dev.epicgames.com/community/api/documentation/image/efa231e8-640a-49f6-a0cb-1aa2ae573f87?resizing_type=fit&width=640&height=640)

  Skeletal Mesh LODs

  Generate and modify LODs for Skeletal Meshes using the Skeletal Mesh Reduction Tool](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-lods-in-unreal-engine)
* [![Skeleton Editing](images/static/document_list/empty_thumbnail.svg)

  Skeleton Editing

  Create and Edit Skeleton Assets using the Skeleton Editing tools.](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeleton-editing-in-unreal-engine)
* [![Skeletal Mesh Sockets](https://dev.epicgames.com/community/api/documentation/image/84c90a05-b5f9-438b-9d5f-74157553b472?resizing_type=fit&width=640&height=640)

  Skeletal Mesh Sockets

  Create attachment points within your Skeletal Mesh using Sockets.](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-sockets-in-unreal-engine)
* [![Virtual Bones](https://dev.epicgames.com/community/api/documentation/image/aabfdbdf-ad5a-480d-8ca9-7db36c838a17?resizing_type=fit&width=640&height=640)

  Virtual Bones

  Resolve layered animation problems by using Virtual Bones with IK.](https://dev.epicgames.com/documentation/en-us/unreal-engine/virtual-bones-in-unreal-engine)

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [skeleton](https://dev.epicgames.com/community/search?query=skeleton)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisites](/documentation/en-us/unreal-engine/skeletons-in-unreal-engine?application_version=5.7#prerequisites)
* [Creating Skeletons](/documentation/en-us/unreal-engine/skeletons-in-unreal-engine?application_version=5.7#creating-skeletons)
* [Skeleton Tree Information](/documentation/en-us/unreal-engine/skeletons-in-unreal-engine?application_version=5.7#skeleton-tree-information)
* [Animation Data Storage](/documentation/en-us/unreal-engine/skeletons-in-unreal-engine?application_version=5.7#animation-data-storage)
* [Sharing Skeletons](/documentation/en-us/unreal-engine/skeletons-in-unreal-engine?application_version=5.7#sharing-skeletons)
* [Merging during Import](/documentation/en-us/unreal-engine/skeletons-in-unreal-engine?application_version=5.7#merging-during-import)
* [Compatible Skeletons](/documentation/en-us/unreal-engine/skeletons-in-unreal-engine?application_version=5.7#compatible-skeletons)
* [Skeleton Features](/documentation/en-us/unreal-engine/skeletons-in-unreal-engine?application_version=5.7#skeleton-features)
