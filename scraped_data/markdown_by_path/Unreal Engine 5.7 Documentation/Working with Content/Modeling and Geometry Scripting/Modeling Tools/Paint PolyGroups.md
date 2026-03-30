<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/paint-polygroups-tool-in-unreal-engine?application_version=5.7 -->

# Paint PolyGroups

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
8. Paint PolyGroups

# Paint PolyGroups

Overview for interactively grouping triangles to create PolyGroups with the Paint PolyGroup modeling tool.

![Paint PolyGroups](https://dev.epicgames.com/community/api/documentation/image/bb35e089-5eaa-4bfa-9dee-e373a0a521a6?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

The **Paint PolyGroups** tool provides the means for interactively painting PolyGroups on a mesh. A PolyGroup is a set of grouped triangles. You can use PolyGroups for various operations, such as:

* Modeling and deformation
* Traditional box modeling
* UV layout
* Material organization
* Skin weights

To learn more, see [Understanding PolyGroups](/documentation/en-us/unreal-engine/understanding-polygroups-in-unreal-engine).

## Accessing the Tool

You can access the Paint PolyGroups tool from the following:

* The **Attributes** category in **Modeling Mode**. To learn more about Modeling Mode and how to access it, see [Modeling Mode Overview](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine).
* The **Editing Tools** tab in the **Skeleton Editor**. To learn more, see [Skeleton Editing](/documentation/en-us/unreal-engine/skeleton-editing-in-unreal-engine).

## Using Paint PolyGroup

The Paint PolyGroups tool carries over preexisting groupings when opening the tool. Choose the PolyGroup layer you want to edit from the **Active PolyGroup** property. To create new layers, use the [Edit Attributes](/documentation/en-us/unreal-engine/edit-attributes-tool-in-unreal-engine) or [Generate PolyGroup](/documentation/en-us/unreal-engine/generate-polygroups-tool-in-unreal-engine) tools.

Use the **Action** setting to choose any of the following selection modes for painting PolyGroups:

* **Brush:** Paints PolyGroups with a brush. **Click + Drag** across the mesh to paint.
* **Fill:** Fills the entire component with the current group. **Click** the mesh to add the fill.
* **Group Fill:** Fills only the hovered group(s) with the current set group ID.
* **Poly Lasso:** Draws an area on the mesh to paint the current group ID. **Click + Drag** to highlight an area of the mesh to add PolyGroups.

To create a different PolyGroup, add a value in the **Set Group** property. The value represents the group ID. You can erase groupings by adding the group ID to the **Erase Group** property and using the **Shift + Click + Drag** hotkey. To view the current group IDs, toggle the properties in the **Visualization** section or use the **Shift + G** hotkey.

To help control group selection, use the quick action buttons in the **Freezing** and **Operations** sections.

Once you are done using the tool, accept or cancel the changes in the [Tools Confirmation](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine#tools,undohistory,andacceptingchanges) panel.

### Hotkeys

| **Hotkey** | **Description** |
| --- | --- |
| **Shift + Click + Drag** | Erases painted PolyGroups. |
| **[ or S** | Decreases the brush size. Hold **Shift** for smaller steps. |
| **] or D** | Increases the brush size. Hold **Shift** for smaller steps. |
| **Shift + Q** | Creates a new group and applies it to **Set Group**. |
| **Shift + G** | Assigns the hovered group as the **Set Group**. |
| **Shift + F** | Freezes or unfreezes the hovered group. |
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

* [Accessing the Tool](/documentation/en-us/unreal-engine/paint-polygroups-tool-in-unreal-engine?application_version=5.7#accessingthetool)
* [Using Paint PolyGroup](/documentation/en-us/unreal-engine/paint-polygroups-tool-in-unreal-engine?application_version=5.7#usingpaintpolygroup)
* [Hotkeys](/documentation/en-us/unreal-engine/paint-polygroups-tool-in-unreal-engine?application_version=5.7#hotkeys)

Related documents

[Modeling Tools

![Modeling Tools](https://dev.epicgames.com/community/api/documentation/image/808c9f39-3e12-44a5-8c91-d19bce2c278b?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/modeling-tools-in-unreal-engine)

[Modeling Mode Overview

![Modeling Mode Overview](https://dev.epicgames.com/community/api/documentation/image/056cb8c8-a8a2-4ba1-b18c-42a01965bcb1?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine)
