<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/boolean-tool-in-unreal-engine?application_version=5.7 -->

# Boolean

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
6. [Modeling and Geometry Scripting](/documentation/en-us/unreal-engine/modeling-and-geometry-scripting-in-unreal-engine "Modeling and Geometry Scripting")
7. [Modeling Tools](/documentation/en-us/unreal-engine/modeling-tools-in-unreal-engine "Modeling Tools")
8. Boolean

# Boolean

Overview of the Boolean modeling tool for editing mesh pairs.

![Boolean](https://dev.epicgames.com/community/api/documentation/image/3751d2cb-3157-4acb-a978-aa89fac40310?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

The **Boolean** tool subtracts or adds mesh pairs. It is helpful for quickly adding detail and displacement effects to your mesh.

## Accessing the Tool

Boolean is located in the **Model** category of **Modeling Mode**. To learn more about Modeling Mode and how to access it, see [Modeling Mode Overview](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine).

## Using Boolean

Two meshes are required to use the tool as the resulting mesh change revolves around the area where both meshes intersect. The order in which you select the meshes matters for the first two operations:

* Your first selection becomes **A**.
* Your second selection becomes **B**.

You can choose from four operations shown in the table below.

| **Operation** | **Description** |
| --- | --- |
| **Difference A - B** | Subtracts the second mesh from the first mesh. |
| **Difference B - A** | Subtracts the first mesh from the second mesh. |
| **Intersection** | Subtracts non-overlapping geometry. |
| **Union** | Combines both meshes and resolves self-intersections. |

Once both meshes are selected and the tool is activated, you can interactively manipulate one or both meshes in the Viewport, depending on the operation.

After you edit the mesh, you can decide how to handle the mesh output using the operations shown in the table below.

| **Operation** | **Description** |
| --- | --- |
| **Output Type** | Chooses the type of actor to create. Only available if **New Object** is selected in **Output Object**. |
| **Output Object** | Determines whether to create a new actor or to override one of the input meshes. |
| **On Tool Accept** | Determines what happens to the selected meshes when changes are accepted. |

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [landscape](https://dev.epicgames.com/community/search?query=landscape)
* [beta](https://dev.epicgames.com/community/search?query=beta)
* [modeling mode](https://dev.epicgames.com/community/search?query=modeling%20mode)
* [modeling tools](https://dev.epicgames.com/community/search?query=modeling%20tools)
* [low-poly modeling](https://dev.epicgames.com/community/search?query=low-poly%20modeling)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Accessing the Tool](/documentation/en-us/unreal-engine/boolean-tool-in-unreal-engine?application_version=5.7#accessingthetool)
* [Using Boolean](/documentation/en-us/unreal-engine/boolean-tool-in-unreal-engine?application_version=5.7#usingboolean)

Related documents

[Modeling Tools

![Modeling Tools](https://dev.epicgames.com/community/api/documentation/image/808c9f39-3e12-44a5-8c91-d19bce2c278b?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/modeling-tools-in-unreal-engine)

[Modeling Mode Overview

![Modeling Mode Overview](https://dev.epicgames.com/community/api/documentation/image/056cb8c8-a8a2-4ba1-b18c-42a01965bcb1?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine)
