<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-a-vertex-color-material-for-mesh-painting-in-unreal-engine?application_version=5.7 -->

# Setting Up a Vertex Color Material for Mesh Painting

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
5. [Building Virtual Worlds](/documentation/en-us/unreal-engine/building-virtual-worlds-in-unreal-engine "Building Virtual Worlds")
6. [Level Editor](/documentation/en-us/unreal-engine/level-editor-in-unreal-engine "Level Editor")
7. [Level Editor Modes](/documentation/en-us/unreal-engine/level-editor-modes-in-unreal-engine "Level Editor Modes")
8. [Mesh Paint Mode](/documentation/en-us/unreal-engine/mesh-paint-mode-in-unreal-engine "Mesh Paint Mode")
9. Setting Up a Vertex Color Material for Mesh Painting

# Setting Up a Vertex Color Material for Mesh Painting

A guide to setting up a material for vertex color painting.

On this page

When you use the Vertex Color mode with mesh painting, the vertex color data is used with a material to color the mesh. To do this, you use the **Vertex Color** material expression in a material graph with some logic to effectively use this color data.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ed3c26b3-4b23-4da7-9893-93ac7d098b01/vertexcolornode.png)

Vertex Color Material Expression.

There are many ways in which you can use this color-painted data with a Vertex Color material expression. The sections below demonstrate how to add vertex-painted color to an existing material to tint that color in some way. This is one way you can use the Vertex Color expression with your materials with the mesh painting system.

To learn more about vertex color materials and how you can use them to blend textures layers together for painting on a mesh, see [Setting Up a Texture Blended Material for Mesh Painting](/documentation/en-us/unreal-engine/setting-up-a-texture-blended-material-for-vertex-weights-painting-in-unreal-engine).

## The Mesh and its Material

The example mesh and its material below demonstrate how to integrate vertex color workflows into your existing materials.

|  |  |
| --- | --- |
| Base Static Mesh | Base material applied to a static mesh. |
| Base Static Mesh | Base material applied to the mesh. |

## Vertex Color Material Setup

To set up a paintable material that takes in painted vertex color to tint an existing base color in a material, add a **VertexColor** material expression that plugs the RGB color channel into the **A** input of a **Multiply** node.

![Simple Vertex Color Example](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/76bd6497-a7be-4a3b-a769-00b945fc8edb/vertex-color-example.png)

Next, plug the material logic for your Base Color (Albedo) into the **B** input of the **Multiply** node, and then plug the output of the Multiply into the **Main Material** node.

The material should look similar to the image below with its paintable vertex color setup.

![Example of a vertex color node in a material graph.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/df340a29-4621-4871-a657-d2e4265e02d7/vertex-color-material-setup.png)

## Using a Vertex Color Material to Paint on a Mesh

When you switch to the **Mesh Paint** mode in the level viewport, select the **Vertex Color** tab in the mode toolbar.

![Vertex Color paint mode selection.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fc22a92b-4ce1-490d-8481-2b852dfc3903/vertex-color-paintmode.png)

To get started, use this workflow:

1. Use the **Select** tool to click on your mesh that has a material setup to use vertex color painting.
2. Switch to the **Paint** tool and choose a **Paint Color** to apply to your mesh.
3. Use the **Color View Mode** dropdown selection to inspect the painted colors, as needed.

With this change to your material, you can paint a color that tints the base material.

* [materials](https://dev.epicgames.com/community/search?query=materials)
* [reference](https://dev.epicgames.com/community/search?query=reference)
* [building virtual worlds](https://dev.epicgames.com/community/search?query=building%20virtual%20worlds)
* [mesh paint tool](https://dev.epicgames.com/community/search?query=mesh%20paint%20tool)
* [vertex color](https://dev.epicgames.com/community/search?query=vertex%20color)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [The Mesh and its Material](/documentation/en-us/unreal-engine/setting-up-a-vertex-color-material-for-mesh-painting-in-unreal-engine?application_version=5.7#themeshanditsmaterial)
* [Vertex Color Material Setup](/documentation/en-us/unreal-engine/setting-up-a-vertex-color-material-for-mesh-painting-in-unreal-engine?application_version=5.7#vertexcolormaterialsetup)
* [Using a Vertex Color Material to Paint on a Mesh](/documentation/en-us/unreal-engine/setting-up-a-vertex-color-material-for-mesh-painting-in-unreal-engine?application_version=5.7#usingavertexcolormaterialtopaintonamesh)
