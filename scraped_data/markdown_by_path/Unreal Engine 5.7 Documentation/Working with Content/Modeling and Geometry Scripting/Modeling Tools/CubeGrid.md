<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/cubegrid-tool-in-unreal-engine?application_version=5.7 -->

# CubeGrid

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
8. CubeGrid

# CubeGrid

Overview of the CubeGrid modeling tool for creating blockout meshes.

![CubeGrid](https://dev.epicgames.com/community/api/documentation/image/edeca721-c68d-4da2-addb-ec2b0f35e2c0?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

The **CubeGrid** tool creates blockout meshes using a repositionable grid. You can use CubeGrid to create a new mesh or edit the selected mesh.

The **Push** and **Pull** actions are helpful in quickly building level prototypes.

## Accessing the Tool

CubeGrid is located in the **Create** category of **Modeling Mode**. To learn more about Modeling Mode and how to access it, see [Modeling Mode Overview](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine).

## Using CubeGrid

What makes CubeGrid an efficient tool for blocking out a level are the tool's operations coupled with hotkey commands. Below are hotkeys for building out your grid and adjusting its size.

| **Hotkey** | **Description** |
| --- | --- |
| **Click** | Makes a grid selection. |
| **Click + Drag** | Dynamically creates an array of rows and columns. |
| **Shift + Click** | Creates an array of rows and columns between the initial and second positions clicked. |
| **Ctrl + E** | Increases the grid size. |
| **Ctrl + Q** | Decreases the grid size. |
| **Shift + E** | Shifts your selection forward one grid cell. |
| **Shift + Q** | Shifts your selection backward one grid cell. |

Once your grid is selected, you can use the **Actions** buttons or the following hotkeys to build your mesh.

| **Hotkey** | **Description** |
| --- | --- |
| **Ctrl + Drag** | Push or pull geometry from the selected grid. |
| **E** | Pull geometry from the selected grid. |
| **Q** | Push from the selected grid. |
| **Z** | Enters **Corner Mode**, where you can select corners of your selected grid that are pushed or pulled by **Ctrl + Drag** or **E/Q**. Press **Z** again to apply the change. |

You can reposition the grid using the grid gizmo (toggled with the **R** key) or by **Ctrl + Middle-Click**, which will move the gizmo to the corner of the nearest cell. You can also set specific position and orientation in the **[Tool Properties](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine#accessingmodelingmode)** panel or reinitialize from the transform of a created mesh.

See **Shortcut Info** in the **Tool Properties** panel to learn more about the various hotkeys for the tool.

## Output

After you finish editing the mesh, you can choose the following **Output Types**:

* Static mesh
* Dynamic mesh
* Volume

Once you are done using the tool, accept or cancel the changes in the [Tool Confirmation](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine#toolsundohistoryandacceptingchanges) panel.

To learn more about the Output Types and their use cases, see [Working with Meshes](/documentation/en-us/unreal-engine/working-with-meshes-in-unreal-engine). For a concept breakdown of blockouts and when to use it, see [Blockouts and Stand-in Meshes](https://dev.epicgames.com/community/learning/tutorials/bXd/unreal-engine-blockouts-and-stand-in-meshes).

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [landscape](https://dev.epicgames.com/community/search?query=landscape)
* [beta](https://dev.epicgames.com/community/search?query=beta)
* [modeling mode](https://dev.epicgames.com/community/search?query=modeling%20mode)
* [modeling tools](https://dev.epicgames.com/community/search?query=modeling%20tools)
* [low-poly modeling](https://dev.epicgames.com/community/search?query=low-poly%20modeling)
* [level blocking](https://dev.epicgames.com/community/search?query=level%20blocking)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Accessing the Tool](/documentation/en-us/unreal-engine/cubegrid-tool-in-unreal-engine?application_version=5.7#accessingthetool)
* [Using CubeGrid](/documentation/en-us/unreal-engine/cubegrid-tool-in-unreal-engine?application_version=5.7#usingcubegrid)
* [Output](/documentation/en-us/unreal-engine/cubegrid-tool-in-unreal-engine?application_version=5.7#output)

Related documents

[Modeling Tools

![Modeling Tools](https://dev.epicgames.com/community/api/documentation/image/808c9f39-3e12-44a5-8c91-d19bce2c278b?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/modeling-tools-in-unreal-engine)

[Modeling Mode Overview

![Modeling Mode Overview](https://dev.epicgames.com/community/api/documentation/image/056cb8c8-a8a2-4ba1-b18c-42a01965bcb1?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine)
