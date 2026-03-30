<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/mutable-real-time-morphs-in-unreal-engine?application_version=5.7 -->

# Real-Time Morphs

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
5. [Working with Content](/documentation/en-us/unreal-engine/working-with-content-in-unreal-engine "Working with Content")
6. [Mutable Skeletal Mesh Generation](/documentation/en-us/unreal-engine/mutable-skeletal-mesh-generation-in-unreal-engine "Mutable Skeletal Mesh Generation")
7. [Mutable Development Guides](/documentation/en-us/unreal-engine/mutable-development-guides-in-unreal-engine "Mutable Development Guides")
8. Real-Time Morphs

# Real-Time Morphs

Learn how to use real-time morph targets with the Mutable plugin.

![Real-Time Morphs](https://dev.epicgames.com/community/api/documentation/image/120b6990-79cf-49ce-a786-a5980162b5da?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

In addition to supporting baked morphs (see [Morph Node](https://github.com/anticto/Mutable-Documentation/wiki/Node-Mesh-Morph)), Mutable can also add real-time morph targets to generated meshes.

## Enable Real-Time Morph Targets

This feature needs to be enabled for each CutomizableObject in its compilation options. Go to the **Object Properties** tab and click **Compile Options** > **Enable Real Time Morph Targets**.

![The Enable Real Time Morph Targets option](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/94d14975-ce06-4a2c-ad0c-da5b7ccc9e60/enable-real-time-morph-targets.png)

Once enabled, any selected morph target present in a skeletal mesh participating of a generated mutable skeletal mesh will be added to that mesh. If a morph target is present with the same name in multiple meshes composing the generated mesh, the morph targets will be merged so that all affected vertices will be driven by the same curve.

### Morph Target Selection

There are three ways to select which morph targets need to be considered.

#### SkeletalMesh Node

One way to select morph targets is in the SkeletalMesh node. In the Node's properties view, a list of all morphs targets found in the SkeletalMesh is shown. There individual or all morph targets can be selected.

![The list of morph targets in the SkeletalMesh](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/30894717-1179-4c25-bff8-ba68f3e477a1/list-of-morph-targets.png)

#### Tables

When working with data tables, there is no list where morph targets can be selected. In this case, the default SkeletalMesh, set in the data table struct, is used to determine which morph will be selected. If the morph target name is present in the default skeletal mesh list of morph targets then the morph is selected for all skeletal meshes in the table.

#### Global Selection

Sometimes it is useful to select all morph targets with a specific name for all meshes in the graph. Going to all SkeletalMeshes nodes in the CustomizableObject and selecting manually one particular morph target can be cumbersome and error-prone if the graph is very large or has a lot of sub-graphs. To help with these cases, a list of override selected morphs can be edited at the graph root Base Object's **Node Properties** panel. In the **Node Properties** panel, click **Real Time Morph Targets** > **Real Time Morph Override Selection**.

This list lets you override the morphs target selection in the SkeletalMesh nodes globally. Each entry is composed of a morph target name and a selection override with three values: **No Override**, **Enable**, or **Disable**. **No Override** is the default option and indicates the Nodes selection will be used. **Enable** and **Disable** force all morph targets with that name to be enabled or disabled regardless of the Node selection. If a more fine-tuned per skeletal mesh override is needed, a list of per-skeletal mesh overrides can be specified. The skeletal mesh override value always has preference over the morph target override, so if a mesh does not need to override the morph target then the mesh name should not be in the list.

![The list of Real Time Morph Override Selections](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b2713393-40d1-4b6d-b019-e3635693833e/global-selection.png)

### Additional considerations

The real-time morph targets that will end up in the mutable generated meshes are regular SkeletalMesh morph targets, so the same workflows apply. For example, to check which morphs are being used for a particular CustomizableObjectInstance, inspect the SkeletalMesh generated using the SkeletalMesh viewer Morph Target Preview tab.

* [beta](https://dev.epicgames.com/community/search?query=beta)
* [working with content](https://dev.epicgames.com/community/search?query=working%20with%20content)
* [skeletal mesh](https://dev.epicgames.com/community/search?query=skeletal%20mesh)
* [mutable](https://dev.epicgames.com/community/search?query=mutable)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Enable Real-Time Morph Targets](/documentation/en-us/unreal-engine/mutable-real-time-morphs-in-unreal-engine?application_version=5.7#enablereal-timemorphtargets)
* [Morph Target Selection](/documentation/en-us/unreal-engine/mutable-real-time-morphs-in-unreal-engine?application_version=5.7#morphtargetselection)
* [SkeletalMesh Node](/documentation/en-us/unreal-engine/mutable-real-time-morphs-in-unreal-engine?application_version=5.7#skeletalmeshnode)
* [Tables](/documentation/en-us/unreal-engine/mutable-real-time-morphs-in-unreal-engine?application_version=5.7#tables)
* [Global Selection](/documentation/en-us/unreal-engine/mutable-real-time-morphs-in-unreal-engine?application_version=5.7#globalselection)
* [Additional considerations](/documentation/en-us/unreal-engine/mutable-real-time-morphs-in-unreal-engine?application_version=5.7#additionalconsiderations)
