<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/understanding-polygroups-in-unreal-engine?application_version=5.7 -->

# Understanding PolyGroups

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
7. [Getting Started with Modeling Mode](/documentation/en-us/unreal-engine/getting-started-with-modeling-mode "Getting Started with Modeling Mode")
8. Understanding PolyGroups

# Understanding PolyGroups

Learn the use of PolyGroups and how to create them.

![Understanding PolyGroups](https://dev.epicgames.com/community/api/documentation/image/0038e913-9acc-4a30-b322-098b505e2009?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

The [Modeling Mode Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine), introduces you to **PolyGroups**, and the [Quick Start](https://dev.epicgames.com/documentation/en-us/unreal-engine/modeling-mode-quick-start-in-unreal-engine) guide shows you how to use some of the tools for assigning PolyGroups. We recommend reviewing these two documents before continuing.

This guide further explores the tools for creating PolyGroups and how you can use these groups in other tools and scripts. The goal at the end of this guide is to understand PolyGroups to build an efficient workflow for creating and editing your geometry in-engine.

## The Why and What of PolyGroups

### Why

In traditional modeling software, you have the option of polygonal modeling. However, Unreal Engine renders all models as triangulated meshes.

|  |  |
| --- | --- |
| [Quad modeling in Autodesk Maya](https://dev.epicgames.com/community/api/documentation/image/c9136c52-3969-44e2-aa28-ad02d0738ead?resizing_type=fit) | [Triangle based rendering in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/b8ab338b-16f2-4e75-9e01-e850a8265f5c?resizing_type=fit) |
| A quad based cube in Maya. | The same cube rendered as triangles in Unreal Engine. |

The conversion to triangles means Unreal Engine does not natively recognize quads or n-gons, making triangles the foundation on which in-engine modeling is built. To provide an approximation to the traditional modeling workflow, you can use **PolyGroups**.

### What

PolyGroups are a set of grouped triangles. You can use the groups for:

* UV layout
* Material organization
* Modeling and deformation
* Traditional box modeling with quads
* Creating and editing skin weights

For example, using the cube [imported](working-with-content/static-meshes/importing-static-meshes) from Maya, we assign a separate PolyGroup to each triangle using the **Tri Select** tool under the **Mesh** category.

To visualize the PolyGroups on the mesh, set **Face Color Mode** to **By Group**.

With PolyGroups set, you can use the [PolyGroup Edit](https://dev.epicgames.com/documentation/en-us/unreal-engine/polygroup-edit-tool-in-unreal-engine) tool under the **Model** category. However, the current PolyGroups each represent a single triangle, which isn't the best use of the PolyGroup Edit tool.

[![Creating PolyGroups in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/f8b34127-0c3a-4a9b-83bb-f353318888e3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f8b34127-0c3a-4a9b-83bb-f353318888e3?resizing_type=fit)

PolyGroups consisting of one triangle, where each color indicates a PolyGroup.

When you merge two triangles into one PolyGroup, you have the representation of a quad.

*In the video, using **Merge** creates a new PolyGroup consisting of two triangles.*

When working with low-polygon meshes and blockouts, PolyGroups provide a way to interact with more intuitive surfaces than raw triangles. However, you can also apply PolyGroups to high-polygon meshes to help manipulate chunks of complex geometry, which otherwise would be complicated to edit.

## PolyGroup Anatomy

A PolyGroup consists of three elements which you can select and edit:

* Face: The area of a PolyGroup.
* Vertex: Connecting point of edges. Also known as a corner.
* Edge: The border between PolyGroups.

As you group triangles to create a PolyGroup, a boundary edge forms, encompassing the triangles. Depending on the topology of your mesh and generated PolyGroups, editing the edges of your mesh may not work as you expect compared to other modeling Digital Content Creation (DCC) software.

In the image below the mesh includes two PolyGroups, represented by the highlighted boundary edge. Although the boundary of the PolyGroups appears to have multiple edges due to the bending shape, it does not consist of any PolyGroup vertices, and consists of only one PolyGroup edge.

[![PolyGroup Boundary Edge](https://dev.epicgames.com/community/api/documentation/image/0f3cca7c-ced6-4164-a16d-e5af4b7b4117?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0f3cca7c-ced6-4164-a16d-e5af4b7b4117?resizing_type=fit)

PolyGroup edges and vertices are generated under the following conditions:

* Two or more connecting PolyGroup faces (or a mesh boundary) create a PolyGroup edge.
* Three or more connecting PolyGroup edges create a PolyGroup vertex.

## Creating PolyGroups

To better understand PolyGroups, it helps to know the tools you can use to create them. The order in which you use these tools depends on your preferred workflow and needs. The important thing to remember is you can use any set of triangles as a PolyGroup.

### Triangle Selection Tool

As shown in the video above, the **Tri Select** tool can assign a PolyGroup to one or more triangles. Instead of selecting one triangle per PolyGroup, we now select two in order to perform quad editing with the **PolyGroup Edit** tool.

*In the video, new PolyGroups are created at the intersection of each edge loop.*

Triangles not assigned a PolyGroup are automatically grouped into one.

### Merge

When using the **PolyGroup Edit** tool, you can continue combining existing PolyGroups into a new group.

The process of combining existing PolyGroups is destructive, meaning the prior PolyGroups will no longer exist.

*In the video each face represents a PolyGroup, and you can group faces using Merge.*

### Paint PolyGroups Tool

There are dedicated tools for creating PolyGroups, and one is the [Paint PolyGroups](https://dev.epicgames.com/documentation/en-us/unreal-engine/paint-polygroups-tool-in-unreal-engine) tool, where you can interactively paint your groupings.

*In the video the Paint PolyGroup tool creates new PolyGroups consisting of two triangles. **Show Wireframe** is enabled to visualize the two triangles in each PolyGroup.*

You can use the **Action** setting to choose any of the following selection modes:

* **Brush**
* **Fill**
* **Group Fill**
* **Lasso**

To see what PolyGroup is assigned, hover over said PolyGroup and use the hotkey **Shit + G**. The **Set Group** row will update to the associated number.

### Generate PolyGroups Tool

Another dedicated tool for grouping triangles is the [Generate PolyGroups](https://dev.epicgames.com/documentation/en-us/unreal-engine/generate-polygroups-tool-in-unreal-engine) tool. PolyGroups are automatically assigned upon opening the tool. How the PolyGroups are assigned is determined by the **Conversion Mode**.

| Conversion Mode | Description |
| --- | --- |
| **Face Normal Deviation** | Convert based on Angle Tolerance between face normals. |
| **Find Quads** | Create PolyGroups by merging triangle pairs into quads. |
| **From UV Islands** | Create PolyGroups based on UV islands. |
| **From Hard Normal Seams** | Create PolyGroups based on hard normal seams. |
| **From Connected Tris** | Create PolyGroups based on connected triangles. |
| **Furthest Point Sampling** | Create PolyGroups centered on well-spaced sample points, approximating a surface Voronoi diagram. |
| **Copy From Layer** | Copy from existing PolyGroup layer. |

[![Generate PolyGroups in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/7df43834-b984-4c9c-a309-66e26dde3673?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7df43834-b984-4c9c-a309-66e26dde3673?resizing_type=fit)

PolyGroups are generated by quads (merging triangle pairs).

You can use the **Output Layer** to create a new PolyGroup layer.

### Predefined Shapes

When creating predefined shapes in the **Create** category, you can configure the PolyGroups of your new meshes using the **PolyGroup Mode** setting.

[![Creating PolyGroups for Quad Modeling in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/5de6bdfd-9c7e-4c3b-86f9-38a9d8f4f276?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5de6bdfd-9c7e-4c3b-86f9-38a9d8f4f276?resizing_type=fit)

The Polygroup Mode has the following grouping options:

|  |  |  |
| --- | --- | --- |
| [Generate PolyGroups per Shape](https://dev.epicgames.com/community/api/documentation/image/01ea1a46-30c8-4f8c-9098-701ac2157794?resizing_type=fit) | [Generate PolyGroups per Face](https://dev.epicgames.com/community/api/documentation/image/04670024-8064-4a52-8984-11ee046862cb?resizing_type=fit) | [Generate PolyGroups per Quad](https://dev.epicgames.com/community/api/documentation/image/12e1c678-3fd4-498a-bbe9-34584b3b32b6?resizing_type=fit) |
| **Per Shape** | **Per Face** | **Per Quad** |
| Outputs the entire mesh as a single group. | Automatically divide the mesh into recognizable face groups. | Automatically divide the mesh into a group for each quad. |

### PolyGroup Layers

Because PolyGroups are arbitrary, you can create multiple **PolyGroup Layers** to handle different sets of them on the same model. You can configure these layers in the [Edit Attributes](https://dev.epicgames.com/documentation/en-us/unreal-engine/edit-attributes-tool-in-unreal-engine) tool of the **Attributes** category.

PolyGroup Layers are not universal to your project. Instead, you create them for individual static mesh assets. This particular assignment means that you cannot assume that two different meshes have the same PolyGroup layers. However, it also means that you can define them as needed on a case-by-case basis.

## Using PolyGroups

### Building shapes

The fundamental use of PolyGroups is geometry editing, as shown with the **PolyGroup Edit** tool.

Additional ways in which PolyGroups help with constructing a mesh include:

* Precise region edits.

  *Four PolyGroups are merged into one for extrusion.*
* Hole creation.
* Smoothing a mesh with the [Subdivide](https://dev.epicgames.com/documentation/en-us/unreal-engine/subdivide-tool-in-unreal-engine) tool.

  [![Subdividing a model in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/55082212-2125-4a1b-ac59-cf1b05b81b7f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/55082212-2125-4a1b-ac59-cf1b05b81b7f?resizing_type=fit)

  Click image to expand.
* Creating deformations with the [Deform PolyGroups](https://dev.epicgames.com/documentation/en-us/unreal-engine/deform-polygroups-tool-in-unreal-engine) tool.

Interior vertices of a PolyGroup are not selectable, only bordering vertices. To select the interior vertices, use **Decompose** to deconstruct the PolyGroup.

### Creating UVs

You can use PolyGroups to assist in creating UVs for your model. In the [Modeling Mode Quick Start](https://dev.epicgames.com/documentation/en-us/unreal-engine/modeling-mode-quick-start-in-unreal-engine) guide, six PolyGroups are assigned to the crate (one per side). Then UV islands are generated based on the existing PolyGroups.

[![Using PolyGroups to UV Unwrap in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/815e6f1c-04e3-4f8e-9dba-b62b237661cd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/815e6f1c-04e3-4f8e-9dba-b62b237661cd?resizing_type=fit)

You can then use the UV tools to deconstruct the UVs further or you can add more PolyGroups.

[![Assigning Additional PolyGroups to UV Unwrap in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/c332cf1e-d2f1-426a-bbf3-8240e7c1b7a2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c332cf1e-d2f1-426a-bbf3-8240e7c1b7a2?resizing_type=fit)

Additional PolyGroups are assigned to indicate an UV island.

Now when you unwrap your model, more UV islands are created.

[![Using PolyGroups to UV Unwrap in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/c2bec0fc-07a5-47c2-995d-bf466780aaea?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c2bec0fc-07a5-47c2-995d-bf466780aaea?resizing_type=fit)

To learn more about the UV tools, refer to the [UVs Category](working-with-content/modeling-and-geometry-scripting/modeling-tools/uvs-category) documentation.

### Assigning Multiple Materials to One Mesh

You can assign multiple Materials to your geometry using the **Edit Materials** tool. To help visualize what triangles you want to assign the Material, you can select PolyGroups from the **Face Color Mode**, which is especially helpful for high-density meshes.

## Frequently Asked Questions

**Is there a way to clear all PolyGroups to start over?**

Yes, by using the **Clear All** option in the **Paint PolyGroups** tool.

**Does it matter if I have PolyGroups consisting of one triangle?**

Although you can still edit your mesh using tools such as **PolyGroup Edit**, it may yield unexpected results. For example, when adding an edge loop to a mesh where the top side has two PolyGroups containing one triangle, the loop will slant to the side. If there is one PolyGroup grouping the two triangles (representing a quad), then the loop would continue straight across.

|  |  |
| --- | --- |
| [Distorted Edge Loop in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/6b46b3cd-a900-4011-9829-902afdea4ea1?resizing_type=fit) | [Corrected Edge Loop in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/061305c1-d929-4501-8a9e-b3e5c4dfa0f3?resizing_type=fit) |
| Distorted Edge Loop | Corrected Edge Loop |

**Does creating PolyGroups interfere with rendering?**

No, PolyGroups are just a tool to help perform classic modeling techniques you may be used to in other modeling software. At render time, triangles are still used.

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [landscape](https://dev.epicgames.com/community/search?query=landscape)
* [modeling](https://dev.epicgames.com/community/search?query=modeling)
* [geometry](https://dev.epicgames.com/community/search?query=geometry)
* [beta](https://dev.epicgames.com/community/search?query=beta)
* [modeling tools](https://dev.epicgames.com/community/search?query=modeling%20tools)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [The Why and What of PolyGroups](/documentation/en-us/unreal-engine/understanding-polygroups-in-unreal-engine?application_version=5.7#the-why-and-what-of-poly-groups)
* [Why](/documentation/en-us/unreal-engine/understanding-polygroups-in-unreal-engine?application_version=5.7#why)
* [What](/documentation/en-us/unreal-engine/understanding-polygroups-in-unreal-engine?application_version=5.7#what)
* [PolyGroup Anatomy](/documentation/en-us/unreal-engine/understanding-polygroups-in-unreal-engine?application_version=5.7#poly-group-anatomy)
* [Creating PolyGroups](/documentation/en-us/unreal-engine/understanding-polygroups-in-unreal-engine?application_version=5.7#creating-poly-groups)
* [Triangle Selection Tool](/documentation/en-us/unreal-engine/understanding-polygroups-in-unreal-engine?application_version=5.7#triangle-selection-tool)
* [Merge](/documentation/en-us/unreal-engine/understanding-polygroups-in-unreal-engine?application_version=5.7#merge)
* [Paint PolyGroups Tool](/documentation/en-us/unreal-engine/understanding-polygroups-in-unreal-engine?application_version=5.7#paint-poly-groups-tool)
* [Generate PolyGroups Tool](/documentation/en-us/unreal-engine/understanding-polygroups-in-unreal-engine?application_version=5.7#generate-poly-groups-tool)
* [Predefined Shapes](/documentation/en-us/unreal-engine/understanding-polygroups-in-unreal-engine?application_version=5.7#predefined-shapes)
* [PolyGroup Layers](/documentation/en-us/unreal-engine/understanding-polygroups-in-unreal-engine?application_version=5.7#poly-group-layers)
* [Using PolyGroups](/documentation/en-us/unreal-engine/understanding-polygroups-in-unreal-engine?application_version=5.7#using-poly-groups)
* [Building shapes](/documentation/en-us/unreal-engine/understanding-polygroups-in-unreal-engine?application_version=5.7#building-shapes)
* [Creating UVs](/documentation/en-us/unreal-engine/understanding-polygroups-in-unreal-engine?application_version=5.7#creating-u-vs)
* [Assigning Multiple Materials to One Mesh](/documentation/en-us/unreal-engine/understanding-polygroups-in-unreal-engine?application_version=5.7#assigning-multiple-materials-to-one-mesh)
* [Frequently Asked Questions](/documentation/en-us/unreal-engine/understanding-polygroups-in-unreal-engine?application_version=5.7#frequently-asked-questions)

Related documents

[Modeling Mode Quick Start

![Modeling Mode Quick Start](https://dev.epicgames.com/community/api/documentation/image/9828c874-2ee3-4591-9649-57b5f5614c2e?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/modeling-mode-quick-start-in-unreal-engine)

[Modeling Mode Overview

![Modeling Mode Overview](https://dev.epicgames.com/community/api/documentation/image/056cb8c8-a8a2-4ba1-b18c-42a01965bcb1?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine)
