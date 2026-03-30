<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/morph-target-previewer?application_version=5.7 -->

# Morph Target Previewer

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
8. Morph Target Previewer

# Morph Target Previewer

User guide for the editing modes available in the Animation Editor.

![Morph Target Previewer](https://dev.epicgames.com/community/api/documentation/image/56c1062e-46ac-4bdd-8641-6e62050103c8?resizing_type=fill&width=1920&height=335)

 On this page

The **Morph Target Previewer** previews any **Morph Targets** (sometimes called "morphs" or "blend shapes") that are applied to a **Skeletal Mesh**. Each **Morph Target** is additively blended into the existing **Skeletal Mesh** geometry. Multiple morph targets can be combined to create a complex vertex-driven animation, which is often ideal for such things as facial expressions.

The **Morph Target Previewer** window is visible by default whenever any [Animation Editor](/documentation/en-us/unreal-engine/animation-editors-in-unreal-engine) is open.

## Interface

The **Morph Target Previewer** panel has two main sections:

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2153926c-9243-4327-bebc-35c1d7e08092/morphtargetpreviewerinterface.png)

1. Search Bar
2. Morph Target List

The Search Bar filters the list of **Morph Targets** to quickly find the one you need. Type the first few letters of the desired target and the list will begin filtering.
You can also right-click on a **Morph Target**, which will pop-up a dialog box with additional actions, such as **Delete** or **Copy Morph Target Names**.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f524fbac-176e-4ae6-adb1-76fb038b9ef0/rightclickdelete.png)

## Creating Morph Targets

You can import **Morph Targets** as a part of a **Skeletal Mesh**, as well as independently (from a given mesh). This is supported via the FBX file format.

For more information on the setup procedure, as well as how to import Morph Targets into Unreal, please see [FBX Morph Target Pipeline](/documentation/en-us/unreal-engine/fbx-morph-target-pipeline-in-unreal-engine).

## Using Morph Targets

Once your Morph Targets are in place, you will need to set up your [Animation Blueprint](/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine) to utilize them. This is done within your Event Graph via the **Set Morph Target** node.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c7150255-13aa-4760-ac62-8e11c99ec289/setmorphtarget.png)

| Pin | Description |
| --- | --- |
| Input Pins |  |
| Execution | An execution wire to trigger the effect of the node. |
| Target | The target **Skeletal Mesh**. For most circumstances, this will point to "self". |
| Morph Target Name | The name of the **Morph Target** being edited. |
| Value | A float value (between 0.0 and 1.0) used to set the value of the **Morph Target** being edited. |
| Output Pins |  |
| Execution | Passes execution on to the next node. |

## Morph Target Debug View Mode

You can enable this view mode to easily see what vertices are affected by each Morph Target.

1. In the viewport window, click on **Show** > **Mesh Overlay** >, and then **Selected MorphTarget Vertices**.
2. Now select any **Morph Target** from the **Morph Target Preview** panel to see the debug view.

## Optimization

For target platforms that support Shader Model 5, you can enable the GPU calculation of morph targets. This means that the CPU does not have to perform the calculations if your game is CPU bound, and you have GPU processing to spare. This feature can be activated in the **Project Settings**, as follows:

1. On the file menu, go to **Edit** > **Project Settings**.
2. Open the **Rendering** section of **Project Settings**.
3. In the **Optimizations** category, find the **Use GPU for computing morph targets** checkbox and enable it.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d1f2a256-a10a-45c5-9b6e-ce6a83cfe207/projectsettingsmorphgpu.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d1f2a256-a10a-45c5-9b6e-ce6a83cfe207/projectsettingsmorphgpu.png)

Click for full image.

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [morph target](https://dev.epicgames.com/community/search?query=morph%20target)
* [skeletal mesh](https://dev.epicgames.com/community/search?query=skeletal%20mesh)
* [fbx importing](https://dev.epicgames.com/community/search?query=fbx%20importing)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Interface](/documentation/en-us/unreal-engine/morph-target-previewer?application_version=5.7#interface)
* [Creating Morph Targets](/documentation/en-us/unreal-engine/morph-target-previewer?application_version=5.7#creatingmorphtargets)
* [Using Morph Targets](/documentation/en-us/unreal-engine/morph-target-previewer?application_version=5.7#usingmorphtargets)
* [Morph Target Debug View Mode](/documentation/en-us/unreal-engine/morph-target-previewer?application_version=5.7#morphtargetdebugviewmode)
* [Optimization](/documentation/en-us/unreal-engine/morph-target-previewer?application_version=5.7#optimization)
