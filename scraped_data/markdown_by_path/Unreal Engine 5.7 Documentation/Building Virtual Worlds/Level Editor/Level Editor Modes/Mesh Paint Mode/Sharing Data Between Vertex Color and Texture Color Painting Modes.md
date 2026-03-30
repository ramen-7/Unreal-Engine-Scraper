<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-share-vertex-color-data-between-instances-in-unreal-engine?application_version=5.7 -->

# Sharing Data Between Vertex Color and Texture Color Painting Modes

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
9. Sharing Data Between Vertex Color and Texture Color Painting Modes

# Sharing Data Between Vertex Color and Texture Color Painting Modes

This demonstrates how you can share color data between vertex and texture color modes.

On this page

There are situations when it’s useful to maintain both **Vertex Color** and **Texture Color** data on an instance of a painted mesh, like when one platform supports one mesh painting method but not another. For example, platforms with lower-end specifications may not support the virtual textures that are required to use texture color data. In this case, the platform running the project would need to use vertex color data.

To deploy your content to a range of platforms, you need a way to copy data between mesh painting modes supported by these platforms without needing to do the work twice.

To be able to have both vertex and texture color data with your project, you must:

* Copy existing color data between vertex color and texture color painting modes.
* Paint texture color data automatically to vertex color data.

In the following sections, both of these options are explained along with any further configuration needed.

## Copying Between Vertex Color and Texture Color

To transfer painted color data between the Vertex Color and Texture Color painting modes , you can use the From Texture and From Vertex tools.

To copy data between these tools:

* **Texture Color to Vertex Color Copying**
  + To copy color data from the Texture Color’s Mesh Paint Texture to the vertex color of any selected mesh components, select the **Vertex Color** painting method in the Mesh Paint panel, and use the **From Texture** tool .

    ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f28fc296-a5e0-404f-8cbb-1e44d2e453ac/mp-sharing-fromtexture.png)
* **Vertex Color to Texture Color Copying**
  + To copy color data from Vertex Color onto any selected mesh components, select the **Texture Color** painting method in Mesh Paint panel, and use the **From Vertex**. If there’s no existing Mesh Paint Texture for this mesh, one is created when the color data is copied over.

    ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d1bb02d0-9e0c-4ef0-aee2-cea93d57afce/mp-sharing-fromvertex.png)

The **Paint** tool settings in each mesh paint mode has a **Color View Mode** under the **Visualization** category where you can select different color channels to inspect the color data. For more information on the color view mode and its visualization setting, see the “Visualization Settings” section of [Mesh Paint Mode Tools and Settings](/documentation/en-us/unreal-engine/mesh-paint-tool-reference-in-unreal-engine)

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a8548a07-8981-4cb9-b347-854909fa2497/mp-sharing-colorviewmode.png)

Vertex Color Mode with RGB Channels selected.

You can switch between the Vertex Color and Texture Color modes to see the current color data of each. The examples below show the result of copied data between one another. Notice that there is a slight difference in the Texture Color mode’s copy of vertex color data due to texture interpolation instead of vertex interpolation.

|  |  |
| --- | --- |
|  |  |
| Vertex Color Mode after copying Texture Color Data | Texture Color Mode after copying Vertex Color Data |

For any Nanite-enabled mesh, per-instance vertex color cannot be visualized, even if it exists. To view this color data, you must temporarily disable Nanite in the editor. You can use one of the following ways to do this:

* Use the console command `r.Nanite 0`.
* On the mesh component, check the box for **Disallow Nanite** to force the component to use the fallback mesh when Nanite is enabled on the mesh.

## Painting to both Vertex Color and Texture Color

The Texture Color mode includes an option to automatically transfer the results of all painting to the Vertex Color mode when the Painting tool setting for **Propagate to Vertex Color** is enabled.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2eb3666b-2387-4a29-8e1b-5ef8989d3ecb/mp-sharing-propagatesetting.png)

## Stripping Texture Colors From Your Cooked Build

For projects deploying to multiple platforms, you can disable features that you don’t need or that might not be supported. This can save package overhead by removing things like mesh paint textures from a cooked build. For example, if the platform doesn’t support [Nanite meshes](/documentation/404), you can use a console variable to disable mesh paint textures that are virtual textures per-platform using their device configuration files.

To disable mesh paint textures for a platform, add the following console variable to the platform engine configuration (\*.ini) file in the “Console Variables” section:

r.MeshPaintVirtualTexture.Support False

## Setting up a Material for both Vertex Color and Texture Color

If your project is using both Vertex Color and Texture Color for painting a mesh, you can set up the mesh’s material to select between these two color data sets with some logic in the material graph.

Below is a simplified example showing the **MeshPaintTextureReplace** node handling the path for Vertex Color (top) with the Default path, and Texture Color (bottom) with MeshPaintTexture path. This example can be adapted to the requirements of the platforms you’re developing for:

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f53cfdeb-d3bc-4d80-bb51-bd815fd78460/mp-sharing-meshpainttexturereplacenode.png)

To learn more about setting up materials for mesh painting, see these pages:

* [Setting Up a Vertex Color Material for Mesh Painting](/documentation/en-us/unreal-engine/setting-up-a-vertex-color-material-for-mesh-painting-in-unreal-engine)
* [Setting Up a Material and Mesh for Texture Color Painting](/documentation/en-us/unreal-engine/setting-up-a-material-and-mesh-for-texture-color-painting-in-unreal-engine)

* [materials](https://dev.epicgames.com/community/search?query=materials)
* [reference](https://dev.epicgames.com/community/search?query=reference)
* [building virtual worlds](https://dev.epicgames.com/community/search?query=building%20virtual%20worlds)
* [mesh paint tool](https://dev.epicgames.com/community/search?query=mesh%20paint%20tool)
* [vertex color](https://dev.epicgames.com/community/search?query=vertex%20color)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Copying Between Vertex Color and Texture Color](/documentation/en-us/unreal-engine/how-to-share-vertex-color-data-between-instances-in-unreal-engine?application_version=5.7#copyingbetweenvertexcolorandtexturecolor)
* [Painting to both Vertex Color and Texture Color](/documentation/en-us/unreal-engine/how-to-share-vertex-color-data-between-instances-in-unreal-engine?application_version=5.7#paintingtobothvertexcolorandtexturecolor)
* [Stripping Texture Colors From Your Cooked Build](/documentation/en-us/unreal-engine/how-to-share-vertex-color-data-between-instances-in-unreal-engine?application_version=5.7#strippingtexturecolorsfromyourcookedbuild)
* [Setting up a Material for both Vertex Color and Texture Color](/documentation/en-us/unreal-engine/how-to-share-vertex-color-data-between-instances-in-unreal-engine?application_version=5.7#settingupamaterialforbothvertexcolorandtexturecolor)
