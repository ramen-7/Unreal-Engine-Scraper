<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/predefined-shapes-in-unreal-engine?application_version=5.7 -->

# Predefined Shapes

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
8. Predefined Shapes

# Predefined Shapes

Learn to create a new mesh using a selection of predefined primitives.

![Predefined Shapes](https://dev.epicgames.com/community/api/documentation/image/80033a94-ccab-4a1e-9611-3b4e80e1f901?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

You can create a new mesh using the **Create** category in **Modeling Mode**. The category provides a selection of predefined primitives to use as a starting base. To learn more about Modeling Mode and how to access it, see [Modeling Mode Overview](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine).

## Using Predefined Shapes

You can choose between nine shapes, represented in the table below.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
| Box | Sphere | Cylinder | Cone | Torus |
|  |  |  |  |  |
| Arrow | Rectangle | Disc | Stairs |  |

You can select your desired shape and drag it into the scene for placement. After placing your mesh, you can still adjust the tool settings in the [Tool Properties](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine#accessingmodelingmode) panel. Once you have your desired settings, click **Accept**.

## Tool Settings

You use the **Tool Properties** panel to control settings such as the output type, dimensions, and material.

As with other Modeling Mode tools, parameter values are remembered when reopening the tool.

### Output Type

The **Output Type** sets the type of mesh you create. You can choose between the following types:

* **Static mesh**
* **Dynamic mesh**
* **Volume**

You can update the mesh type at any stage of the modeling process by various tools, such as **Convert** and **Transfer**, found in the **Transform** category.

To learn more about these output types and asset management, refer to the [Working with Meshes](/documentation/en-us/unreal-engine/working-with-meshes-in-unreal-engine) documentation.

### Shape

You can adjust the dimensions and subdivisions of your mesh under the **Shape** setting. Each shape has specific options.

In addition, you can configure the PolyGroups of your new mesh using the **PolyGroup Mode** setting. The Polygroup Mode has the following grouping options:

|  |  |  |
| --- | --- | --- |
| Generate PolyGroups per Shape | Generate PolyGroups per Face | Generate PolyGroups per Quad |
| **Per Shape** | **Per Face** | **Per Quad** |
| Outputs the entire mesh as a single group. | Automatically divide the mesh into recognizable face groups. | Automatically divide the mesh into a group for each quad. |

To learn more about PolyGroups, refer to the [Understanding PolyGroups](/documentation/en-us/unreal-engine/understanding-polygroups-in-unreal-engine) documentation.

### Positioning

You can position your mesh in your level based on your scene or the ground plane.

Choosing **On Scene** from **Target Surface** positions your mesh based on the surface normal of the geometry your cursor resides over.



If you set [Collision Presets](/documentation/en-us/unreal-engine/setting-up-collisions-with-static-meshes-in-unreal-engine#simulatingphysicsandcollisionpresets) to **No Collision** for any object in your level, then **On Scene** will not detect the object.

Choosing **Ground Plane** positions your mesh in the level with the Z-axis set to 0.

You can adjust the pivot location to the base, top, or center. You can visualize the position of the pivot by the cursor placement, highlighted in the table below.

|  |  |  |
| --- | --- | --- |
|  |  |  |
| Base | Centered | Top |

### Material

You can select the appropriate **Material** for your mesh. You can also set the **UV Scale** and enable **Show Wireframe**.

![Applying a material to your mesh](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cc28cd8d-38f0-42ea-9903-16832b39b478/material-setting.png)

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [landscape](https://dev.epicgames.com/community/search?query=landscape)
* [geometry](https://dev.epicgames.com/community/search?query=geometry)
* [beta](https://dev.epicgames.com/community/search?query=beta)
* [modeling mode](https://dev.epicgames.com/community/search?query=modeling%20mode)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Using Predefined Shapes](/documentation/en-us/unreal-engine/predefined-shapes-in-unreal-engine?application_version=5.7#usingpredefinedshapes)
* [Tool Settings](/documentation/en-us/unreal-engine/predefined-shapes-in-unreal-engine?application_version=5.7#toolsettings)
* [Output Type](/documentation/en-us/unreal-engine/predefined-shapes-in-unreal-engine?application_version=5.7#outputtype)
* [Shape](/documentation/en-us/unreal-engine/predefined-shapes-in-unreal-engine?application_version=5.7#shape)
* [Positioning](/documentation/en-us/unreal-engine/predefined-shapes-in-unreal-engine?application_version=5.7#positioning)
* [Material](/documentation/en-us/unreal-engine/predefined-shapes-in-unreal-engine?application_version=5.7#material)

Related documents

[Modeling Tools

![Modeling Tools](https://dev.epicgames.com/community/api/documentation/image/808c9f39-3e12-44a5-8c91-d19bce2c278b?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/modeling-tools-in-unreal-engine)

[Modeling Mode Overview

![Modeling Mode Overview](https://dev.epicgames.com/community/api/documentation/image/056cb8c8-a8a2-4ba1-b18c-42a01965bcb1?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine)
