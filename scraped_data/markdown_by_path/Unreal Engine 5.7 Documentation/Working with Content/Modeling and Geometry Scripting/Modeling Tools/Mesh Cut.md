<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/mesh-cut-tool-in-unreal-engine?application_version=5.7 -->

# Mesh Cut

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
8. Mesh Cut

# Mesh Cut

Overview of the Mesh Cut modeling tool for editing mesh pairs.

![Mesh Cut](https://dev.epicgames.com/community/api/documentation/image/5d07e981-9380-47e2-a287-33be548503c7?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

The **Mesh Cut** tool splits one mesh into parts using a second mesh. You can use the tool to break up meshes into smaller components and add detail, reducing the manual process of adding edges and deleting faces when modeling.

## Accessing the Tool

Mesh Cut is located in the **Model** category of **Modeling Mode**. To learn more about Modeling Mode and how to access it, see [Modeling Mode Overview](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine).

## Using Mesh Cut

Gizmos for each mesh appear in the Viewport to dynamically change the cut.

Similar to the [Boolean](/documentation/en-us/unreal-engine/boolean-tool-in-unreal-engine) tool, the selection order matters as follows:

* The first selected mesh becomes the one you cut.
* The second selection becomes the cutting boundary.

Mesh Cut is a single-cut tool, meaning you must start a new session for each cut you want to make on the mesh.

Once you are done using the tool, accept or cancel the changes in the [Tool Confirmation](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine#toolsundohistoryandacceptingchanges) panel.

## Settings

| **Setting** | **Description** |
| --- | --- |
| **Try Fix Holes** | When true, Mesh Cut automatically attempts to fill holes created by numerical errors. |
| **Try Collapse Edges** | When true, any extra edges created by the boolean operation are collapsed. |
| **Winding Threshold** | Determines whether a triangle in one mesh is inside or outside of the other. |
| **Show New Boundaries** | When true, shows boundary edges created by the boolean operation caused by numerical errors. |
| **Use First Mesh Materials** | When True, only the first mesh keeps its material assignments. All other triangles are assigned material 0. |
| **Show Gizmo** | Toggles the transform gizmo's visibility. |

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

* [Accessing the Tool](/documentation/en-us/unreal-engine/mesh-cut-tool-in-unreal-engine?application_version=5.7#accessingthetool)
* [Using Mesh Cut](/documentation/en-us/unreal-engine/mesh-cut-tool-in-unreal-engine?application_version=5.7#usingmeshcut)
* [Settings](/documentation/en-us/unreal-engine/mesh-cut-tool-in-unreal-engine?application_version=5.7#settings)

Related documents

[Modeling Tools

![Modeling Tools](https://dev.epicgames.com/community/api/documentation/image/808c9f39-3e12-44a5-8c91-d19bce2c278b?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/modeling-tools-in-unreal-engine)

[Modeling Mode Overview

![Modeling Mode Overview](https://dev.epicgames.com/community/api/documentation/image/056cb8c8-a8a2-4ba1-b18c-42a01965bcb1?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine)
