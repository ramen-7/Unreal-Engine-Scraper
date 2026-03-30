<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/polygroup-edit-tool-in-unreal-engine?application_version=5.7 -->

# PolyGroup Edit

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
8. PolyGroup Edit

# PolyGroup Edit

Overview of the PolyGroup Edit tool for polygonal modeling.

![PolyGroup Edit](https://dev.epicgames.com/community/api/documentation/image/1ae086bc-a3d3-4b21-bda3-ade3d5a1830b?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

The **PolyGroup Edit** tool includes a suite of operations for editing a mesh with PolyGroups. Common operations such as **Extrude**, **Bevel**, **Weld**, and **Bridge** are available. Also included are operations that only work with structured PolyGroups, such as **Insert Edge Loop** and edge loop selection.

Combining all these tools with PolyGroup-specific operations like **Merge** (groups) or **Simplify By Groups** creates a low polygon workflow commonly associated with Digital Content Creation (DCC) software such as 3ds Max, Blender, and Maya.



PolyGroup Edit is not available for meshes with no PolyGroup information.

## Understanding PolyGroups

PolyGroups are a set of grouped triangles. You can use the groups for:

* Modeling and deformation
* Traditional box modeling
* UV layout
* Material organization

PolyGroups are automatically generated on [predefined shapes](/documentation/en-us/unreal-engine/predefined-shapes-in-unreal-engine) in the **Create** category. You can also create them using the **Paint PolyGroups**, **Generate PolyGroups**, and **Tri Select** tools.

Before you start using PolyGroup Edit, we recommend reviewing the [Understanding PolyGroups](/documentation/en-us/unreal-engine/understanding-polygroups-in-unreal-engine) documentation to learn more about PolyGroups and how to create them.

## Accessing the Tool

You can access the PolyGroup Edit tool from the following:

* The **Model** category in **Modeling Mode**. To learn more about Modeling Mode and how to access it, see [Modeling Mode Overview](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine).
* The **Editing Tools** tab in the **Skeleton Editor**. To learn more, see [Skeleton Editing](/documentation/en-us/unreal-engine/skeleton-editing-in-unreal-engine).

## Using PolyGroup Edit

PolyGroup Edit's editing operations are grouped into three categories:

* **Face Edits:** Operations for editing the PolyGroup faces of a mesh.
* **Shape Edits:** Operations for editing the mesh as a whole.
* **Edge Edits:** Operations for editing the PolyGroup edge of a mesh.

Many operations have a panel of settings that open upon selection. These panels have an accept and cancel option separate from PolyGroup Edit's [Tool Confirmation](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine#toolsundohistoryandacceptingchanges) panel.

### Element Selection

You can control which element of your mesh you want to select by using the **Selection Filter**.

| **Element Icon** | **Description** |
| --- | --- |
| Select vertices | Selects vertices of a PolyGroup. |
| Select edges | Selects edges of a PolyGroup. |
| Select faces. | Selects PolyGroup faces. |
| Select edge loops. | Selects PolyGroup edge loops. Edge loops are paths through vertices with four attached edges. |
| Select a ring of edges | Selects ring of PolyGroup edges. Rings are sequences of edges that lie across from each other over a face with four PolyGroup edges. |

If you cannot select elements as expected, confirm you set your PolyGroups correctly or try regenerating extra corners in the [Topolgy Options](/documentation/en-us/unreal-engine/polygroup-edit-tool-reference-in-unreal-engine#topologyoptions) section of the reference guide.

Marquee selection is available for quickly selecting the enabled element. All elements in the selection area are toggled by default, including ones you can't see. To ensure you are not selecting elements you can't see, uncheck **Marquee Ignore Occlusion**.

You can also use the following hotkeys to adjust your selection:

* **Shift + Click** to add to the current selection.
* **Ctrl + Click** to remove from the current selection.

While using **PolyGroup Edit**, you can interactively set UVs using **Planar Projection**. To scale the UV island, drag the cursor in and out. To learn more about creating and editing UVs, see [UV Category](/documentation/en-us/unreal-engine/uvs-category-in-unreal-engine).

To continue learning about the PolyGroup Edit properties, see the [PolyGroup Edit Reference](/documentation/en-us/unreal-engine/polygroup-edit-tool-reference-in-unreal-engine) documentation and [PolyGroup Edit video series](https://youtu.be/JgPU9A4nJWY?feature=shared).

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [landscape](https://dev.epicgames.com/community/search?query=landscape)
* [beta](https://dev.epicgames.com/community/search?query=beta)
* [modeling mode](https://dev.epicgames.com/community/search?query=modeling%20mode)
* [modeling tools](https://dev.epicgames.com/community/search?query=modeling%20tools)
* [low-poly modeling](https://dev.epicgames.com/community/search?query=low-poly%20modeling)
* [skeleton editing](https://dev.epicgames.com/community/search?query=skeleton%20editing)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Understanding PolyGroups](/documentation/en-us/unreal-engine/polygroup-edit-tool-in-unreal-engine?application_version=5.7#understandingpolygroups)
* [Accessing the Tool](/documentation/en-us/unreal-engine/polygroup-edit-tool-in-unreal-engine?application_version=5.7#accessingthetool)
* [Using PolyGroup Edit](/documentation/en-us/unreal-engine/polygroup-edit-tool-in-unreal-engine?application_version=5.7#usingpolygroupedit)
* [Element Selection](/documentation/en-us/unreal-engine/polygroup-edit-tool-in-unreal-engine?application_version=5.7#elementselection)

Related documents

[PolyGroup Edit Reference

![PolyGroup Edit Reference](https://dev.epicgames.com/community/api/documentation/image/0195b349-2d8d-4dc5-bda2-59e7d32ac4f0?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/polygroup-edit-tool-reference-in-unreal-engine)

[Modeling Tools

![Modeling Tools](https://dev.epicgames.com/community/api/documentation/image/808c9f39-3e12-44a5-8c91-d19bce2c278b?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/modeling-tools-in-unreal-engine)

[Modeling Mode Overview

![Modeling Mode Overview](https://dev.epicgames.com/community/api/documentation/image/056cb8c8-a8a2-4ba1-b18c-42a01965bcb1?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine)
