<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/push-pull-tool-in-unreal-engine?application_version=5.7 -->

# Push Pull

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
8. Push Pull

# Push Pull

Overview of the Push Pull modeling tool for cutting or merging mesh parts.

![Push Pull](https://dev.epicgames.com/community/api/documentation/image/fd375aaa-9618-44a0-8f95-2bc676ab4c68?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

The **Push Pull** tool extrudes PolyGroup faces that cut or merge mesh parts. You can think of this as performing a boolean operation (like those done by the [Boolean tool](/documentation/en-us/unreal-engine/boolean-tool-in-unreal-engine)) between the original mesh and an extruded selection.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ad3a29d3-3a55-42bc-8257-444c896528f1/push-pull-operation.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ad3a29d3-3a55-42bc-8257-444c896528f1/push-pull-operation.png)

Left is the face selection; middle is the Push Pull operation; right is the Extrude operation.

Before you start using the Push Pull tool, we recommend reviewing the [Understanding PolyGroups](/documentation/en-us/unreal-engine/understanding-polygroups-in-unreal-engine) documentation to learn more about PolyGroups and how to create them.

## Accessing the Tool

You can access the Push Pull tool from the following:

* As a standalone tool in the **Select** category when selecting PolyGroup faces. To learn more about this category, see [Mesh Element Selection](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine#meshelementselection).
* As an operation in the **PolyGroup Edit** tool. To learn more, see [PolyGroup Edit Reference](/documentation/en-us/unreal-engine/polygroup-edit-tool-in-unreal-engine)

## Using Push Pull

| **Current Operation** | **Description** |
| --- | --- |
| **Apply** | Bakes extrusion changes into the mesh. |
| **Cancel (Esc)** | Negates changes. |

| **Extrusion Options** | **Description** |
| --- | --- |
| **Distance Mode** | Determines how the extrusion distance is set. You can use the following methods:   * **Click in Viewport:** Mouse movement controls extrusion height and depth. Click in the viewport to complete the extrusion and exit the operation. Using the cursor, you can align the extrusion distance to objects in the level. An additional line from the center of the selection indicates the direction of measurement for the extrusion. * **Fixed:** Set extrusion height or depth from a numerical input (**Distance**). |
| **Direction Mode** | Determines the direction vertices move during extrusion before the boolean operation. You can use the following methods:   * **Vertex Normals:** Follow the vertex normals regardless of selection. * **Single Direction:** Move all triangles in the same direction regardless of their normals. * **Selected Triangle Normals:** Take the angle-weighted average of the selected triangles around each extruded vertex to determine vertex movement direction. * **Selected Triangle Normals Even:** Similar to Selected Triangle Normals, but also adjust the distance moved in an attempt to keep triangles parallel to their original facing.   + **Max Distance Scale Factor:** Controls the maximum distance vertices can move from the target distance in order to stay parallel with their source triangles.   [See below for examples.](/documentation/en-us/unreal-engine/push-pull-tool-in-unreal-engine#pushdirectionmodeexamples) |
| **Shells to Solids** | Controls whether extruding an entire open-border patch should create a solid or open shell.   * True (enable): Open-border faces are extruded as a solid shell (no holes in the mesh). * False (disable): Open-border faces are extruded with an open shell. |

#### Push Direction Mode Examples

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Vertex Normals |  | Selected Triangle Normals | Triangle Normal Even |
| No Extrusion | Vertex Normal | Single Direction | Selected Triangle Normals | Selected Triangle Normals Even |

| **Advanced** | **Description** |
| --- | --- |
| **Measure Direction** | The direction to measure the distance of extrusion when Selected Triangle Normals, Vertex Normals, or Selected Triangle Normals Even is active. The extrusion height is set based on the mouse location on the respective axis. When Single Direction is active, the direction of the extrusion is based on Measure Direction. The setting is only available when Distance Mode is set to Click in Viewport. You can choose from the following directions:   * **Selection Normal** * **World X** * **World Y** * **World Z** * **Local X** * **Local Y** * **Local Z** |
| **Use Colinearity for Setting Border Groups** | Considers edge colinearity for determining how side triangles connecting the extruded face are grouped when extruded faces touch the mesh border.   * If true, side triangles touching the mesh border are grouped per colinear section of boundary. * If false, all side triangles touching the mesh border are grouped as one.   For example, when true, extruding a flat rectangle gives four different PolyGroups on its side rather than one connected PolyGroup. |

Once you are done using the tool, accept or cancel the changes in the [Tool Confirmation](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine#tools,undohistory,andacceptingchanges) panel.

* [beta](https://dev.epicgames.com/community/search?query=beta)
* [modeling mode](https://dev.epicgames.com/community/search?query=modeling%20mode)
* [modeling tools](https://dev.epicgames.com/community/search?query=modeling%20tools)
* [mesh selection](https://dev.epicgames.com/community/search?query=mesh%20selection)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Accessing the Tool](/documentation/en-us/unreal-engine/push-pull-tool-in-unreal-engine?application_version=5.7#accessingthetool)
* [Using Push Pull](/documentation/en-us/unreal-engine/push-pull-tool-in-unreal-engine?application_version=5.7#usingpushpull)
* [Push Direction Mode Examples](/documentation/en-us/unreal-engine/push-pull-tool-in-unreal-engine?application_version=5.7#pushdirectionmodeexamples)

Related documents

[Modeling Tools

![Modeling Tools](https://dev.epicgames.com/community/api/documentation/image/808c9f39-3e12-44a5-8c91-d19bce2c278b?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/modeling-tools-in-unreal-engine)

[Modeling Mode Overview

![Modeling Mode Overview](https://dev.epicgames.com/community/api/documentation/image/056cb8c8-a8a2-4ba1-b18c-42a01965bcb1?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine)
