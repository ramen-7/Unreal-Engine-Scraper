<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/deform-polygroups-tool-in-unreal-engine?application_version=5.7 -->

# Deform PolyGroups

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
8. Deform PolyGroups

# Deform PolyGroups

Learn to deform a mesh using the Deform PolyGroups modeling tool.

![Deform PolyGroups](https://dev.epicgames.com/community/api/documentation/image/12d977d2-b180-4305-a7fd-5a916fa3c725?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

The **Deform PolyGroups** modeling tool dynamically alters the shape of a mesh through its [PolyGroups](/documentation/en-us/unreal-engine/understanding-polygroups-in-unreal-engine). Deformation is an efficient way to reshape a mesh quickly and create organic geometry.

You can select vertices, edges, or faces and drag them along the world grid axes to deform the overall profile of a mesh. You can also apply multiple deformations in a single tool session.



If your mesh does not deform as expected, your resolution (triangle count) may be too low. You can use the **[Remesh](/documentation/en-us/unreal-engine/modeling-tools-in-unreal-engine#mesh)** tool to re-triangulate.

## Accessing the Tool

You can access the Deform PolyGroups tool from the following:

* The **Deform** category in Modeling Mode. To learn more about Modeling Mode and how to access it, see [Modeling Mode Overview](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine).
* The **Editing Tools** tab in the **Skeleton Editor**. To learn more, see [Skeleton Editing](/documentation/en-us/unreal-engine/skeleton-editing-in-unreal-engine).

## Settings

### Options

The two core options for using the tool are **Deformation** and **Transformation**.

You can choose between **Linear** and **Smooth** for the type of deformation to occur.

| **Deformation** | **Description** |
| --- | --- |
| **Linear** | PolyGroup edges connected to the selected component remain straight. |
| **Smooth** | PolyGroup edges connected to the selected component are smoothly interpolated into a curve. |

The Transformation option determines the type of movement that occurs when selecting a component.

| **Transformation** | **Description** |
| --- | --- |
| **Translate** | Move the selected components linearly on the X, Y, and Z axes. |
| **Rotation** | Move the selected component around the X, Y, and Z axes. |

### Selection

**Selection** determines which element types (edge, face, or vertice) are selectable. You can toggle multiple options at the same time.

If you cannot select elements as expected, confirm you set your PolyGroups correctly. For more information, see [Understanding PolyGroups](/documentation/en-us/unreal-engine/understanding-polygroups-in-unreal-engine).

### Show Wireframe

When you enable **Show Wireframe**, a 2D lining overlays on the mesh, depicting underlying triangles.

Once you are done using the tool, accept or cancel the changes in the [Tool Confirmation](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine#tools,undohistory,andacceptingchanges) panel.

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [landscape](https://dev.epicgames.com/community/search?query=landscape)
* [beta](https://dev.epicgames.com/community/search?query=beta)
* [modeling mode](https://dev.epicgames.com/community/search?query=modeling%20mode)
* [modeling tools](https://dev.epicgames.com/community/search?query=modeling%20tools)
* [sculpting](https://dev.epicgames.com/community/search?query=sculpting)
* [skeleton editing](https://dev.epicgames.com/community/search?query=skeleton%20editing)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Accessing the Tool](/documentation/en-us/unreal-engine/deform-polygroups-tool-in-unreal-engine?application_version=5.7#accessingthetool)
* [Settings](/documentation/en-us/unreal-engine/deform-polygroups-tool-in-unreal-engine?application_version=5.7#settings)
* [Options](/documentation/en-us/unreal-engine/deform-polygroups-tool-in-unreal-engine?application_version=5.7#options)
* [Selection](/documentation/en-us/unreal-engine/deform-polygroups-tool-in-unreal-engine?application_version=5.7#selection)
* [Show Wireframe](/documentation/en-us/unreal-engine/deform-polygroups-tool-in-unreal-engine?application_version=5.7#showwireframe)

Related documents

[Modeling Tools

![Modeling Tools](https://dev.epicgames.com/community/api/documentation/image/808c9f39-3e12-44a5-8c91-d19bce2c278b?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/modeling-tools-in-unreal-engine)

[Modeling Mode Overview

![Modeling Mode Overview](https://dev.epicgames.com/community/api/documentation/image/056cb8c8-a8a2-4ba1-b18c-42a01965bcb1?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine)
