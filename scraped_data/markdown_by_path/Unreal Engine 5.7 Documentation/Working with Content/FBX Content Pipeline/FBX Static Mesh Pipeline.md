<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/fbx-static-mesh-pipeline-in-unreal-engine?application_version=5.7 -->

# FBX Static Mesh Pipeline

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
6. [FBX Content Pipeline](/documentation/en-us/unreal-engine/fbx-content-pipeline "FBX Content Pipeline")
7. FBX Static Mesh Pipeline

# FBX Static Mesh Pipeline

Setting up, exporting, and importing Static Meshes using the FBX content pipeline.

![FBX Static Mesh Pipeline](https://dev.epicgames.com/community/api/documentation/image/ccec9f2a-1e1a-471c-b223-18c166b7d67f?resizing_type=fill&width=1920&height=335)

 On this page

The *StaticMesh* support in the FBX import pipeline makes getting meshes from 3D applications into Unreal Engine 5 a simple, painless task. When meshes are imported, the textures used in the materials applied to those meshes in their respective 3D application (diffuse and normal map only) are also imported and, in turn, used to generate the materials applied to the mesh in UE5.

Features supported for importing *Static Meshes* using FBX:

* [*Static Meshes* with materials including textures](/documentation/en-us/unreal-engine/fbx-static-mesh-pipeline-in-unreal-engine#materials)
* [Custom collision](/documentation/en-us/unreal-engine/fbx-static-mesh-pipeline-in-unreal-engine#collision)
* [Multiple UV sets](/documentation/en-us/unreal-engine/fbx-static-mesh-pipeline-in-unreal-engine#uvtexturecoordinates)
* Smoothing groups
* [Vertex colors](/documentation/en-us/unreal-engine/fbx-static-mesh-pipeline-in-unreal-engine#vertexcolors)
* [LODs](/documentation/en-us/unreal-engine/fbx-static-mesh-pipeline-in-unreal-engine#staticmeshlods)
* Multiple separate *Static Meshes* (can also be combined into a single mesh at import)

Currently, when importing multiple meshes with custom collision in a single file, only the first mesh's collision will be imported.



The Unreal Engine FBX import pipeline uses **FBX 2020.2**. Using a different version during export may result in incompatibilities.

## General Setup

In general, you are free to create *Static Meshes* using any tools and methods you want. There are some stipulations as far as setting up UVs, placement of the mesh, etc. that you need to account for in order for the exporting and importing to go smoothly and for the mesh to work properly in Unreal Editor.

### Pivot Point

The pivot point of the mesh in Unreal Engine determines the point around which any transformations (translation, rotation, scale) will be performed.

[![Pivot point of a mesh](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/29b4bacc-3131-4703-889a-09d7d338df8e/01-pivot.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/29b4bacc-3131-4703-889a-09d7d338df8e/01-pivot.png)

Click image for full size.

The pivot point is always located at the origin (0,0,0) when exporting from a 3D modeling application. Because of this, it is best to create your meshes at the origin, with the origin generally being located at one corner of the mesh to allow for proper alignment when snapping to the grid inside of Unreal Editor.

[![Pivot point located at the origin](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d391a13e-f419-4188-9ed5-985ac71030aa/02-pivot-origin.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d391a13e-f419-4188-9ed5-985ac71030aa/02-pivot-origin.png)

Click image for full size.

### Triangulation

Meshes in Unreal Engine must be triangulated as the graphics hardware only deals with triangles.

[![Triangles on a cube mesh](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ffac595a-33f8-4c83-9c30-09335262aff4/03-triangles.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ffac595a-33f8-4c83-9c30-09335262aff4/03-triangles.png)

Click image for full size.

There are several ways you can ensure your mesh is triangulated.

* Model the mesh with only tris - best solution, provides the most control over the end result.
* Triangulate the mesh in the 3D app - good solution, allows cleanup and modification before export.
* Allow the FBX exporter to triangulate the mesh - okay solution, allows no cleanup but can work for simple meshes.
* Allow the importer to triangulate the mesh - okay solution, allows no cleanup but can work for simple meshes.

It will always be best to manually triangulate the mesh in the 3D application, controlling the direction and placement of edges. Automatic triangulation can lead to undesirable results.

[![Examples of bad automatic triangulation](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6da5d673-d0a4-4d9d-9639-b997b1f1b367/04-bad-automatic-triangulation.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6da5d673-d0a4-4d9d-9639-b997b1f1b367/04-bad-automatic-triangulation.png)

Click image for full size.

### UV Texture Coordinates

The import of multiple UV sets is supported by the FBX pipeline in Unreal Engine 5. For *Static Meshes*, this is generally used to handle one set of UVs for the diffuse. There are no special requirements for setting up the UVs for *Static Meshes* using the FBX pipeline.

### Creating Normal Maps

Normal maps can be created for your meshes directly inside of most modeling applications by creating both a low-res render mesh and a high-res detail mesh.

[![Low-res mesh and high-res mesh side by side](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fd45aacb-de23-4904-81bb-b389e5afc7f3/05-detail-mesh-render-mesh.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fd45aacb-de23-4904-81bb-b389e5afc7f3/05-detail-mesh-render-mesh.png)

Click image for full size.

The geometry of the high-res detail mesh is used to generate the normals for the normal map. Epic uses a workflow internally that introduces XNormal into the process and generally results in much better normals when rendering inside of Unreal Engine 5. For details on this process, see the [Textures](/documentation/en-us/unreal-engine/textures-in-unreal-engine).

### Materials

The materials applied to meshes modeled in external applications will be exported along with the mesh and then imported into Unreal. This streamlines the process as textures do not need to be imported separately in Unreal, materials do not need to be created and applied, etc. The import process is capable of performing all of these actions when using the FBX pipeline.

These materials also need to be set up in a specific way, especially when the mesh has multiple materials or the order of the materials on the mesh is important (i.e. for character models where material 0 needs to be the body and material 1 needs to be the head).

For complete details of setting up materials for export, see the [FBX Material Pipeline](/documentation/en-us/unreal-engine/fbx-material-pipeline-in-unreal-engine) page.

### Collision

Simplified collision geometry is important for optimizing collision detection in-game. Unreal Engine 5 provides basic tools for creating collision geometry within the **Static Mesh Editor**. Some circumstances, though, are best handled by creating custom collision geometry within your 3D modeling application and exporting it with the render mesh. Generally, this is true for any mesh with an opening or concave area that objects need to not collide with.

For instance:

* Doorway meshes
* Walls with window cutouts
* Oddly shaped meshes

Collision meshes are identified by the importer based on their name. The collision naming syntax should be:

| **Mesh Prefix and Name** | **Description** |
| --- | --- |
| **UBX\_[RenderMeshName]\_##** | A **Box** must be created using a regular rectangular 3D object. You cannot move the vertices around or deform it in any way to make it something other than a rectangular prism, or else it will not work. |
| **UCP\_[RenderMeshName]\_##** | A **Capsule** must be a cylindrical object capped with hemispheres. It does not need to have many segments (8 is a good number) at all because it is converted into a true capsule for collision. Like boxes, you should not move the individual vertices around. |
| **USP\_[RenderMeshName]\_##** | A **Sphere** does not need to have many segments (8 is a good number) at all because it is converted into a true sphere for collision. Like boxes, you should not move the individual vertices around. |
| **UCX\_[RenderMeshName]\_##** | A **Convex** object can be any completely closed convex 3D shape. For example, a box can also be a convex object. The diagram below illustrates what is convex and what is not: Image comparing correct and incorrect ways to create convex objects |

#### Caveats and Considerations

* `RenderMeshName` must be identical to the name of the render mesh the collision mesh is associated with in the 3D application. So if you have a render mesh named `Tree_01` in your 3D application, your collision mesh should be in the scene with that mesh and named `UCX_Tree_01`, and then exported along with the render mesh to the same FBX file. If you need more than one collision object for a mesh, you can extend their names with further identifiers, such as: `UCX_Tree_01_00`, `UCX_Tree_01_01`, `UCX_Tree_01_02`, etc... and they all will be associated as collision for that mesh.
* Currently, spheres are only used for rigid-body collision and Unreal's zero-extent traces (e.g. weapons), not non-zero extent traces (e.g. Player movement). Also, spheres and boxes do not work if the *StaticMesh* is non-uniformly scaled. In general you probably want to create *UCX* primitives.
* Once your collision objects are set up, you can export both the render and collision mesh in the same .FBX file. When you import the .FBX file into Unreal Editor, it will find the collision mesh, remove it from the render mesh, and turn it into the collision model.
* Breaking up a non-convex mesh into convex primitives is a complex operation, and can give unpredictable results. Another approach is to break the collision model into convex pieces yourself in Max or Maya.
* In the case of an object whose collision is defined by multiple convex hulls, results are best when the hulls do not intersect with one another. For example, if the collision for a lollipop were defined by two convex hulls, one for the candy and one for the stick, a gap should be left between the two as in the following illustration:

[![Candy Collision](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c48a7119-9c21-41d8-b9b5-7b79f95cb4c7/07-candy-collision.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c48a7119-9c21-41d8-b9b5-7b79f95cb4c7/07-candy-collision.png)

Click image for full size.

1. *UCX\_Candy*
2. Small gap between collision surfaces
3. *UCX\_Stick*

### Sockets

Sockets are commonly used in games to attach an object to another object, whether this be for a Skeletal or Static mesh. Unreal Engine 4 provides tools for creating
sockets inside the Static Mesh Editor. Sometimes it may be necessary to set these up within your 3D modeling application and export it with your render mesh.
These sockets can be Translated, Rotated, and scaled relative to the bone on a Skeletal mesh or or the size of the Static Mesh.

To use a socket in your modeling application you will need to use a Dummy or Helper object with the `SOCKET_` Prefix.

| Mesh Prefix and Name | Description |
| --- | --- |
| **SOCKET\_[RenderMeshName]\_##** | Use this on any Dummy or Helper objects in your modeling application to assign a socket to your mesh. |

#### Caveats and Considerations

* `RenderMeshName` must be identical to the name of the render mesh the socket object is associated with in the 3D application. So if you have a render
  mesh named `Object_01` in your 3D application, your socket object should be in the scene with that mesh and named SOCKET\_Object\_01, and then exported along
  with the render mesh to the same FBX file. If you need more than one socket object for a mesh, you can extend their names with further identifiers,
  such as: SOCKET\_Object\_01\_00, SOCKET\_Object\_01\_01, SOCKET\_Object\_01\_02, etc... and they all will be associated as sockets for that mesh.
* When creating sockets for your mesh, you can only have a single mesh FBX setup with sockets that can be imported into Unreal Engine 5. For instance, if
  you have two render meshes that you want to be separate assets will need to be imported as separate FBX files. This means that you cannot import multiple meshes and
  assign the sockets to each separate mesh, and that if you have two sets of render meshes with their own sockets they will not import correctly. As an example, if I have
  Object\_01 with SOCKET\_Object\_01\_00, and another render mesh Box\_01 with SOCKET\_Box\_01\_00 I cannot export both of these meshes with their sockets together. They would need to be exported as
  separate FBX files.

### Vertex Colors

Vertex colors for *Static Meshes* can be transferred using the FBX pipeline. No special setup is necessary

[![Mesh showing vertex colors](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c21e3693-6a0d-489d-b72f-c4e96df3729c/08-vertex-colors.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c21e3693-6a0d-489d-b72f-c4e96df3729c/08-vertex-colors.png)

Click image for full size.

## Export Mesh

*Static Meshes* can be exported individually or multiple meshes can be exported to a single FBX file. The import pipeline will separate multiple *Static Meshes* into multiple assets within the destination package unless specified to combine the meshes by enabling the **Combine Meshes** setting at the time of import. Refer to the documentation for exporting FBX files for your 3rd party DCC tool of choice, remembering to adhere to the guidelines presented earlier for the creation of your meshes.

The Unreal Engine FBX import pipeline uses **FBX 2020.2**. Using a different version during export may result in incompatibilities.

## Import Mesh

1. Click the **Add/Import** button in the **Content Browser** and choose *Import*. Navigate to and select the FBX file you want to import in the file browser that opens.

   You may want to select ![FBX file extension](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4bd79ea2-8448-41fc-b24b-768e0e1eae93/09-fbx-file-extension.png "FBX file extension") in the dropdown to filter out unwanted files.

   [![File window showing FBX files for import](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/177708b5-d857-44c1-a6b3-ab1ba3b2adf9/10-file-window-showing-fbx-files-for-import.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/177708b5-d857-44c1-a6b3-ab1ba3b2adf9/10-file-window-showing-fbx-files-for-import.png)

   Click image for full size.

   The path of the imported asset depends on the current location within the **Content Browser**. Make sure to navigate to the appropriate folder prior to performing the import. You may also drag the imported assets into a new folder once import is complete.
2. Choose the appropriate settings in the **Import** dialog. The defaults should be sufficient in most cases. See the [FBX Import Dialog](/documentation/en-us/unreal-engine/fbx-import-options-reference-in-unreal-engine) section for complete details of all of the settings.

   [![Static mesh import options](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f08188c2-3063-4ece-8b42-09450862da05/11-import-options.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f08188c2-3063-4ece-8b42-09450862da05/11-import-options.png)

   Click image for full size.
3. Click the **Import** button to import the mesh(es). The resulting mesh, material(s), and texture(s) will be displayed in the **Content Browser** if the process was successful.

   [![An imported material, mesh, and texture in the content browser](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8f377422-5a79-4a11-bbb0-c3063a1a92f7/12-after-mesh-is-imported.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8f377422-5a79-4a11-bbb0-c3063a1a92f7/12-after-mesh-is-imported.png)

   Click image for full size.

   Although textures and materials can be imported with a Static Mesh, only **Color** and **Normal** will automatically be connected (assuming a [supported material was used](/documentation/en-us/unreal-engine/fbx-material-pipeline-in-unreal-engine)), **Specular** maps will be imported but not connected, other maps, for example an **Ambient Occlusion** map in the **Diffuse** slot of a Maya material, will not even be imported; it is best to check your materials and connect any unconnected maps and check which maps did not import. Simply **double-click** the new material and connect the available textures with their appropriate inputs.

   By viewing the imported mesh in the **Static Mesh Editor** and enabling the display of collision, you can determine that the process worked as expected.

   [![Sample mesh displayed in the static mesh editor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a2c71fa0-399b-4bce-b5df-8dc55bdf6add/13-open-sm-editor.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a2c71fa0-399b-4bce-b5df-8dc55bdf6add/13-open-sm-editor.png)

   Click image for full size.

Alternatively, you can actually just click and drag an FBX file from Windows into the **Content Browser** and it will bring up the import dialog for you.

## Static Mesh LODs

*Static Meshes* can make use of levels of detail (LODs) in-game in order to limit the impact of meshes as they get farther from the camera. Generally, this means each level of detail will have a reduced number of tris and, perhaps, a simpler material (or materials) applied to it.

[![Four levels of detail comparison](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/de822876-f260-4897-becb-d9f3d335c51a/14-lods-comparison.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/de822876-f260-4897-becb-d9f3d335c51a/14-lods-comparison.png)

Click image for full size.

The FBX pipeline can be used to import LOD meshes created using DCC tools, or LODs can be created for imported static meshes directly inside UE.

### LOD Setup

In general, LODs are handled by creating models of varying complexity going from the full-detail base mesh to the lowest-detail LOD mesh. These should all be aligned and occupying the same space with the same pivot point. Each LOD mesh can have completely different materials assigned, including different amounts of materials. This means the base mesh could use multiple materials to give the desired amount of detail up close, but the lower-detail meshes could use a single material since details will be less noticeable.

Each DCC tool will have its own workflow for creating LODs for static meshes, so refer to the documentation for your tool of choice for specifics about how to create and include them in your FBX exports.

### Import LODs

Static Mesh LODs can be imported along with the base mesh in the **Content Browser** or they can be imported individually through the Static Mesh Editor.

1. Click the **Add/Import** button in the **Content Browser** and choose *Import*. Navigate to and select the FBX file you want to import in the file browser that opens.

   You may want to select ![FBX file extension](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/41defb64-4ad3-4a4f-805d-a692ebe4ad76/15-fbx-file-extension.png "FBX file extension") in the dropdown to filter out unwanted files.

   The path of the imported asset depends on the current location within the **Content Browser**. Make sure to navigate to the appropriate folder prior to performing the import. You may also drag the imported assets into a new folder once import is complete.
2. Choose the appropriate settings in the **Import** dialog. The defaults should be sufficient, but also make sure that *Import LODs* is enabled. **Note:** When importing LODs, the name of the imported mesh will follow the default [naming rules](/documentation/en-us/unreal-engine/fbx-import-options-reference-in-unreal-engine#namingconventions). See the [FBX Import Dialog](/documentation/en-us/unreal-engine/fbx-import-options-reference-in-unreal-engine) section for complete details of all of the settings.

   [![Import Options LOD](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8bebe4a5-2f8b-4f27-ace5-5775462ff7e4/16-import-options-lod.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8bebe4a5-2f8b-4f27-ace5-5775462ff7e4/16-import-options-lod.png)

   Click image for full size.
3. Click the **Import** button to import the mesh and LODs. The resulting mesh, material(s), and texture(s) will be displayed in the **Content Browser** if the process was successful.

   [![An imported material, mesh, and texture in the content browser](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/48269b44-c43b-46f8-9d74-9e2764330f16/17-after-mesh-is-imported.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/48269b44-c43b-46f8-9d74-9e2764330f16/17-after-mesh-is-imported.png)

   Click image for full size.

   Although textures and materials can be imported with a Static Mesh, only **Color** and **Normal** will automatically be connected (assuming a [supported material was used](/documentation/en-us/unreal-engine/fbx-material-pipeline-in-unreal-engine)), **Specular** maps will be imported but not connected, other maps, for example an **Ambient Occlusion** map in the **Diffuse** slot of a Maya material, will not even be imported; it is best to check your materials and connect any unconnected maps and check which maps did not import. Simply **double-click** the new material and connect the available textures into their appropriate inputs.

By viewing the imported mesh in the Static Mesh Editor, you can cycle through the LODs using the **LOD Picker** in the **Details** panel.

[![Static mesh editor level of detail picker](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3365ef31-6371-4709-bcb6-fbfa813c8fdd/18-lod-picker.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3365ef31-6371-4709-bcb6-fbfa813c8fdd/18-lod-picker.png)

Click image for full size.

### Create LODs for Imported Static Meshes

Once a static mesh has been imported, you can either [create LODs for it manually](/documentation/en-us/unreal-engine/creating-and-using-lods-in-unreal-engine), which is longer but will get the best results, especially for complex meshes, or you can use UE's [LOD autogeneration tool](/documentation/en-us/unreal-engine/static-mesh-automatic-lod-generation-in-unreal-engine), which is faster for when you need to generate LODs for multiple simple meshes.

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [static meshes](https://dev.epicgames.com/community/search?query=static%20meshes)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [General Setup](/documentation/en-us/unreal-engine/fbx-static-mesh-pipeline-in-unreal-engine?application_version=5.7#generalsetup)
* [Pivot Point](/documentation/en-us/unreal-engine/fbx-static-mesh-pipeline-in-unreal-engine?application_version=5.7#pivotpoint)
* [Triangulation](/documentation/en-us/unreal-engine/fbx-static-mesh-pipeline-in-unreal-engine?application_version=5.7#triangulation)
* [UV Texture Coordinates](/documentation/en-us/unreal-engine/fbx-static-mesh-pipeline-in-unreal-engine?application_version=5.7#uvtexturecoordinates)
* [Creating Normal Maps](/documentation/en-us/unreal-engine/fbx-static-mesh-pipeline-in-unreal-engine?application_version=5.7#creatingnormalmaps)
* [Materials](/documentation/en-us/unreal-engine/fbx-static-mesh-pipeline-in-unreal-engine?application_version=5.7#materials)
* [Collision](/documentation/en-us/unreal-engine/fbx-static-mesh-pipeline-in-unreal-engine?application_version=5.7#collision)
* [Caveats and Considerations](/documentation/en-us/unreal-engine/fbx-static-mesh-pipeline-in-unreal-engine?application_version=5.7#caveatsandconsiderations)
* [Sockets](/documentation/en-us/unreal-engine/fbx-static-mesh-pipeline-in-unreal-engine?application_version=5.7#sockets)
* [Caveats and Considerations](/documentation/en-us/unreal-engine/fbx-static-mesh-pipeline-in-unreal-engine?application_version=5.7#caveatsandconsiderations-2)
* [Vertex Colors](/documentation/en-us/unreal-engine/fbx-static-mesh-pipeline-in-unreal-engine?application_version=5.7#vertexcolors)
* [Export Mesh](/documentation/en-us/unreal-engine/fbx-static-mesh-pipeline-in-unreal-engine?application_version=5.7#exportmesh)
* [Import Mesh](/documentation/en-us/unreal-engine/fbx-static-mesh-pipeline-in-unreal-engine?application_version=5.7#importmesh)
* [Static Mesh LODs](/documentation/en-us/unreal-engine/fbx-static-mesh-pipeline-in-unreal-engine?application_version=5.7#staticmeshlods)
* [LOD Setup](/documentation/en-us/unreal-engine/fbx-static-mesh-pipeline-in-unreal-engine?application_version=5.7#lodsetup)
* [Import LODs](/documentation/en-us/unreal-engine/fbx-static-mesh-pipeline-in-unreal-engine?application_version=5.7#importlods)
* [Create LODs for Imported Static Meshes](/documentation/en-us/unreal-engine/fbx-static-mesh-pipeline-in-unreal-engine?application_version=5.7#createlodsforimportedstaticmeshes)
