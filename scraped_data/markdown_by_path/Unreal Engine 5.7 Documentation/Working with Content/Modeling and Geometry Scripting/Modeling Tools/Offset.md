<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/offset-tool-in-unreal-engine?application_version=5.7 -->

# Offset

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
8. Offset

# Offset

Overview of the Offset modeling tool.

![Offset](https://dev.epicgames.com/community/api/documentation/image/62ec78ac-25df-4b23-a2b6-0f6cc088098c?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

The **Offset** tool adjusts the position of a mesh's vertices by a specified amount along its normal, such as creating additional details, like a cobblestone pattern, in highly tessellated geometry.

|  |  |
| --- | --- |
|  |  |
| Flat Rectangle | Cobblestone |

The tool is additionally helpful for:

* Adding thickness to a mesh, such as a wall.
* Growing or shrinking a solid object.
* Creating custom [Volume Actors](/documentation/en-us/unreal-engine/volume-actors-in-unreal-engine) and [Cutting Actors for fracturing](https://dev.epicgames.com/community/learning/tutorials/k84m/unreal-engine-chaos-destruction-fracture-and-clustering#:~:text=Play%20Video-,MESH%20CUT,-The%20Mesh%20fracture).

## Accessing the Tool

You can access the Offset tool from the following:

* The **Deform** category in **Modeling Mode**. To learn more about Modeling Mode and how to access it, see [Modeling Mode Overview](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine).
* The **Editing Tools** tab in the **Skeleton Editor**. To learn more, see [Skeleton Editing](/documentation/en-us/unreal-engine/skeleton-editing-in-unreal-engine).

## Using Offset

Offset has the following operation types:

* **Iterative**: Offsets with N iterations.
* **Implicit**: Offsets in a way that produces smoother output and does a better job at preserving UVs but can be slow on large meshes.

When you offset a mesh, you can toggle **Create Shell** to add a thickened shell instead of only moving the input vertices.

To help visualize the effect of the brush on your mesh, you can toggle **Show Wireframe** and **Flat Shading** and change the material mode in the **Rending** section.

![Weight Map](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5075d603-1ca3-44e4-8d9a-c5d66741bc5c/map-paint-tool.png)

Once you are done using the tool, accept or cancel the changes in the [Tool Confirmation](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine#toolsundohistoryandacceptingchanges) panel.

| **Key Command** | **Operation** |
| --- | --- |
| **F** | Zooms into the location of the mesh. |
| **ESC** | Cancels the changes and exits the tool. |
| **Enter** | Accepts the tool changes. |

* [beta](https://dev.epicgames.com/community/search?query=beta)
* [modeling mode](https://dev.epicgames.com/community/search?query=modeling%20mode)
* [sculpting](https://dev.epicgames.com/community/search?query=sculpting)
* [skeleton editing](https://dev.epicgames.com/community/search?query=skeleton%20editing)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Accessing the Tool](/documentation/en-us/unreal-engine/offset-tool-in-unreal-engine?application_version=5.7#accessingthetool)
* [Using Offset](/documentation/en-us/unreal-engine/offset-tool-in-unreal-engine?application_version=5.7#usingoffset)

Related documents

[Modeling Tools

![Modeling Tools](https://dev.epicgames.com/community/api/documentation/image/808c9f39-3e12-44a5-8c91-d19bce2c278b?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/modeling-tools-in-unreal-engine)

[Modeling Mode Overview

![Modeling Mode Overview](https://dev.epicgames.com/community/api/documentation/image/056cb8c8-a8a2-4ba1-b18c-42a01965bcb1?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine)
