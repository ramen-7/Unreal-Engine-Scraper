<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/draw-spline-tool-in-unreal-engine?application_version=5.7 -->

# Draw Spline

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
8. Draw Spline

# Draw Spline

Overview for creating splines with the Draw Spline modeling tool.

![Draw Spline](https://dev.epicgames.com/community/api/documentation/image/52edaa02-2f62-4b60-abc4-6a9b60531834?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

The **Draw Spline** tool creates splines in the Level Editor. You can use your created splines with the **Revolve Spline** and **Mesh Splines** modeling tools to create meshes, or with custom blueprint actors to create a variety of objects such as rails or vines.

To learn more about other spline workflows, see the following:

* [Blueprint Splines](/documentation/en-us/unreal-engine/blueprint-splines-in-unreal-engine)
* [Camera Rig](/documentation/en-us/unreal-engine/camera-jibs-and-dollies-in-unreal-engine)

You can edit splines outside of the tool by selecting and manipulating points on the spline, right-clicking the spline, or using the **Details** panel.

## Accessing the Tool

You can access the Draw Splines tool from the **Create** category in **Modeling Mode**. To learn more about Modeling Mode and how to access it, see [Modeling Mode Overview](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine).

## Using Draw Spline

To create a spline, follow these steps:

1. Choose an output type for the spline from the **Output Mode** dropdown.
2. Choose how to draw your spline from the **Draw Mode** dropdown.
3. Click or drag in the level to draw your spline.
4. Accept or cancel the changes in the [Tool Confirmation](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine#tools,undohistory,andacceptingchanges) panel.

### Output Mode

**Output Mode** determines how a spline component is created.

| **Output Mode** | **Description** |
| --- | --- |
| **Empty Actor** | Creates an empty actor with a spline component. |
| **Existing Actor** | Attaches the spline component to an existing actor or replaces a spline inside that actor if **Existing Spline Index To Replace** is valid. To choose an existing actor, click the actor before switching the mode or use the eyedropper to choose. |
| **Create Blueprint** | Creates the Blueprint specified by **Blueprint To Create** and attaches the spline to that, or replaces an existing spline in the created object if **Existing Spline Index To Replace** is valid. |

If you are working with a blueprint actor that has an expensive construction script, it can be helpful to turn off **Rerun Construction Script on Drag** under advanced options.

### Draw Mode

To adjust how the spline is drawn in the scene, use the properties in the **Draw Mode** section. You can switch between the modes while creating a spline in the level.

| **Draw Mode** | **Description** | **Example** |
| --- | --- | --- |
| **Tangent Drag** | Draws a spline point by point with manual control over curvature (via tangents). Click to place a point and drag to set its tangent. Clicking without dragging creates sharp corners. | Tangent Drag Draw Mode |
| **Click Auto Tangent** | Draws a spline point by point with curvature automatically set. Click and drag to place new points, with the tangent set automatically. | Click Auto Tangent Draw Mode |
| **Free Draw** | Draws a spline with a freehand motion. Click and drag to place multiple points, with spacing controlled by **Min Point Spacing**. | Free Draw Draw Mode |

To have an open or closed path you can toggle **Loop**. When true, points continue to append to the loop as you draw onto it. To help visualize the path and rotation, increase the **Frame Visualization Width** value.

### Raycast Targets

The **Raycast Targets** section determines how the mouse location interacts with the scene while drawing a spline. You can toggle multiple options at the same time.

You must have at least one option enabled to draw a spline.

| **Raycast Targets** | **Description** | **Example** |
| --- | --- | --- |
| **World** | Splines are drawn on mesh surfaces in the level, except the target mesh when **Existing Actor** is enabled. | World Raycast Target |
| **Custom Plane** | Splines are drawn on a plane that you can reposition with the gizmo or with **Ctrl + Click.** | Custom Plane Raycast Target |
| **Ground Planes** | Splines are drawn on the XY ground plane in the perspective viewport, or on the viewed plane in orthographic viewports. | Ground Plane Raycast Target |

### Hotkeys

| **Hotkey** | **Description** |
| --- | --- |
| **C** | Zooms into the location of the mouse. |
| **Enter** | Accepts tool changes. |
| **ESC** | Cancels the changes and exit the tool. |

* [beta](https://dev.epicgames.com/community/search?query=beta)
* [modeling mode](https://dev.epicgames.com/community/search?query=modeling%20mode)
* [modeling tools](https://dev.epicgames.com/community/search?query=modeling%20tools)
* [splines](https://dev.epicgames.com/community/search?query=splines)
* [spline mesh](https://dev.epicgames.com/community/search?query=spline%20mesh)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Accessing the Tool](/documentation/en-us/unreal-engine/draw-spline-tool-in-unreal-engine?application_version=5.7#accessingthetool)
* [Using Draw Spline](/documentation/en-us/unreal-engine/draw-spline-tool-in-unreal-engine?application_version=5.7#usingdrawspline)
* [Output Mode](/documentation/en-us/unreal-engine/draw-spline-tool-in-unreal-engine?application_version=5.7#outputmode)
* [Draw Mode](/documentation/en-us/unreal-engine/draw-spline-tool-in-unreal-engine?application_version=5.7#drawmode)
* [Raycast Targets](/documentation/en-us/unreal-engine/draw-spline-tool-in-unreal-engine?application_version=5.7#raycasttargets)
* [Hotkeys](/documentation/en-us/unreal-engine/draw-spline-tool-in-unreal-engine?application_version=5.7#hotkeys)

Related documents

[Modeling Tools

![Modeling Tools](https://dev.epicgames.com/community/api/documentation/image/808c9f39-3e12-44a5-8c91-d19bce2c278b?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/modeling-tools-in-unreal-engine)

[Modeling Mode Overview

![Modeling Mode Overview](https://dev.epicgames.com/community/api/documentation/image/056cb8c8-a8a2-4ba1-b18c-42a01965bcb1?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine)
