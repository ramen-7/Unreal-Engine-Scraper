<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/generate-polygroups-tool-in-unreal-engine?application_version=5.7 -->

# Generate PolyGroups

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
8. Generate PolyGroups

# Generate PolyGroups

Overview for automatically grouping triangles to create PolyGroups with the Generate PolyGroup modeling tool.

![Generate PolyGroups](https://dev.epicgames.com/community/api/documentation/image/1439fe7b-cdaa-4ac7-881f-601597c5fe5e?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

The **Generate PolyGroup** tool automatically groups triangles to create PolyGroups for a mesh. A PolyGroup is a set of grouped triangles. You can use PolyGroups for various operations, such as:

* Modeling and deformation
* Traditional box modeling
* UV layout
* Material organization
* Skin weights

To learn more, see [Understanding PolyGroups](/documentation/en-us/unreal-engine/understanding-polygroups-in-unreal-engine).



In the video above, we generate PolyGroups based on the mesh's UV islands. The groupings are then used to insert an edge and dynamically alter the shape of a mesh. In addition, the video uses the [PolyGroup Edit](/documentation/en-us/unreal-engine/polygroup-edit-tool-in-unreal-engine) and [Deform PolyGroups](/documentation/en-us/unreal-engine/deform-polygroups-tool-in-unreal-engine) tools.

The Generate PolyGroups tool is a great starting point for applying baseline PolyGroup data to a mesh, which you can then fine-tune with the [Paint PolyGroups](/documentation/en-us/unreal-engine/paint-polygroups-tool-in-unreal-engine) tool.

## Accessing the Tool

You can access the Generate PolyGroup tool from the following:

* The **Attributes** category in **Modeling Mode**. To learn more about Modeling Mode and how to access it, see [Modeling Mode Overview](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine).
* The **Editing Tools** tab in the **Skeleton Editor**. To learn more, see [Skeleton Editing](/documentation/en-us/unreal-engine/skeleton-editing-in-unreal-engine).

## Using Generate PolyGroup

Upon opening the Generate PolyGroup tool, PolyGroups are automatically generated. The **Conversion Mode** defines how triangles are grouped. Choose a conversion mode to generate new PolyGroups and adjust specified values. The table below lists these conversion modes.

| Conversion Mode | Description |
| --- | --- |
| **Face Normal Deviation** | Creates PolyGroups based on the **Angle Tolerance** between face normals. |
| **Find Quads** | Creates PolyGroups by merging triangle pairs into quads. |
| **From UV Islands** | Creates PolyGroups based on UV islands. To learn more about creating UV islands, see [UV Editor](/documentation/en-us/unreal-engine/uv-editor-in-unreal-engine). |
| **From Hard Normal Seams** | Creates PolyGroups based on hard normal seams. |
| **From Connected Tris** | Creates PolyGroups based on connected triangles. Useful for a mesh with disconnected parts. |
| **Furthest Point Sampling** | Creates PolyGroups centered on well-spaced sample points, approximating a surface [Voronoi diagram](https://en.wikipedia.org/wiki/Voronoi_diagram). |
| **Copy From Layer** | Copies PolyGroups from an existing PolyGroup layer. |

You can generate PolyGroups on existing or new PolyGroup layers. These layers can correspond to different operations without having to go back and adjust PolyGroups each time. For example, you can set layer 1 for adjusting topology, layer 2 for UVs, and layer 3 for multiple materials assignment. To add additional layers, use the **Output Layer** property.

Once you are done using the tool, accept or cancel the changes in the [Tools Confirmation](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine#tools,undohistory,andacceptingchanges) panel.

### Hotkeys

| **Hotkey** | **Description** |
| --- | --- |
| **Enter** | Accepts tool changes. |
| **ESC** | Cancels the changes and exits the tool. |

* [beta](https://dev.epicgames.com/community/search?query=beta)
* [modeling mode](https://dev.epicgames.com/community/search?query=modeling%20mode)
* [modeling tools](https://dev.epicgames.com/community/search?query=modeling%20tools)
* [polygroups](https://dev.epicgames.com/community/search?query=polygroups)
* [quads](https://dev.epicgames.com/community/search?query=quads)
* [skeleton editing](https://dev.epicgames.com/community/search?query=skeleton%20editing)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Accessing the Tool](/documentation/en-us/unreal-engine/generate-polygroups-tool-in-unreal-engine?application_version=5.7#accessingthetool)
* [Using Generate PolyGroup](/documentation/en-us/unreal-engine/generate-polygroups-tool-in-unreal-engine?application_version=5.7#usinggeneratepolygroup)
* [Hotkeys](/documentation/en-us/unreal-engine/generate-polygroups-tool-in-unreal-engine?application_version=5.7#hotkeys)

Related documents

[Modeling Tools

![Modeling Tools](https://dev.epicgames.com/community/api/documentation/image/808c9f39-3e12-44a5-8c91-d19bce2c278b?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/modeling-tools-in-unreal-engine)

[Modeling Mode Overview

![Modeling Mode Overview](https://dev.epicgames.com/community/api/documentation/image/056cb8c8-a8a2-4ba1-b18c-42a01965bcb1?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine)
