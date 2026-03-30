<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/importing-static-mesh-lods-using-fbx-in-unreal-engine?application_version=5.7 -->

# Importing Static Mesh LODs Using FBX

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
7. [FBX Static Mesh Pipeline](/documentation/en-us/unreal-engine/fbx-static-mesh-pipeline-in-unreal-engine "FBX Static Mesh Pipeline")
8. Importing Static Mesh LODs Using FBX

# Importing Static Mesh LODs Using FBX

Learn how to import Static Mesh LODs.

![Importing Static Mesh LODs Using FBX](https://dev.epicgames.com/community/api/documentation/image/375dec70-2f3e-4d8f-8e78-c079c3451350?resizing_type=fill&width=1920&height=335)

 On this page

You can import Static Mesh Levels of Detail (LOD) into **Unreal Engine** from external 3D modeling applications, such as **3DS Max**, **Maya**, or **Blender**. Although 3DS Max and Maya are used to illustrate this lesson's goal, you can import Static Mesh LODs into Unreal Engine from any 3D modeling application with a save feature.

### Prerequisites

* You have access to a 3D modeling application.
* You have a model with LODs created.

### Objectives

After going through this guide, you'll know:

* How to set up Static Mesh LODs from external 3D modeling applications.
* How to export Static Mesh LODs from external 3D modeling applications.
* How to import Static Mesh LODs into Unreal Editor from external 3D modeling applications.

The Unreal Engine FBX import pipeline uses **FBX 2020.2**. Using a different version during export may result in incompatibilities.

Choose Your 3D Art Tool

Autodesk Maya
Autodesk 3ds Max

## Setting-up Static Mesh LODs

1. Select all meshes, from the base LOD down to the last LOD. The selection order is essential for ensuring the LODs are added in the correct order of complexity. Then select the *Level of Detail* > Group command from the *Edit* menu.

[![Maya LOD Export Select](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f56a8a5f-c52f-4228-9156-26a8a475ce6b/maya-group-lods.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f56a8a5f-c52f-4228-9156-26a8a475ce6b/maya-group-lods.png)

Click image for full size.

1. All meshes are now grouped under the LOD Group.

[![[Maya LOD Group in Outliner](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a3a28c64-ecf2-41b8-8007-6cd04fef35e7/maya-outliner-lod-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a3a28c64-ecf2-41b8-8007-6cd04fef35e7/maya-outliner-lod-group.png)

Click image for full size.



1. Select all of the LOD meshes (the order is not important) and then select the *Group* command from the *Group* menu.

[![3ds Max Group LODs](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d254c617-1d57-4499-a4d4-fcb0b76ad73d/3ds-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d254c617-1d57-4499-a4d4-fcb0b76ad73d/3ds-group.png)

Click image for full size.

1. Enter a name for the new group in the dialog that opens and the click the ![3ds LOD Ok Button](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ba20ff03-bb94-479b-a4bb-5da31ace38c0/max_lod_ok_button.jpg) button to create the group.

[![3ds Max Group Name](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/705723fd-96e3-4b7d-84b5-d8425890cf05/3ds-group-name.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/705723fd-96e3-4b7d-84b5-d8425890cf05/3ds-group-name.png)

Click image for full size.

1. Click the ![3ds Max Utility Button](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c773fd94-3461-42b1-a885-2c7caa91a877/3ds-utilities-button.png) button to view the *Utilities* panel and then choose the *Level of Detail* utility. **Note:** You may need to click ![max_utility_more_button.jpg](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/28f45657-44bb-4d9b-8fdb-24b458d39844/max_utility_more_button.jpg) and select it from the list.

[![3ds Level of Detail Utility](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2202f9dd-d78d-4cb2-826b-fb9bb8dc5ab7/3ds-utilities-level-of-detail.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2202f9dd-d78d-4cb2-826b-fb9bb8dc5ab7/3ds-utilities-level-of-detail.png)

Click image for full size.

1. With the group selected, click the ![max_lod_create_button.jpg](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d62ec8ed-a258-43b5-8310-379ca34295f9/max_lod_create_button.jpg) button to create a new LOD Set and add the meshes in the selected group to it. The meshes are automatically ordered according to their complexity.

[![3ds Max LOD List](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/25abace3-dc89-4cec-8823-a5718ba11a10/3ds-lods-list.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/25abace3-dc89-4cec-8823-a5718ba11a10/3ds-lods-list.png)

Click image for full size.

## Exporting Static Mesh LODs

1. In Maya, select the LOD Group and any collision geometry.

   [![Maya LOD Export Select](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/69b68363-99e4-42eb-875f-00255bb68534/maya-lod-group-selection.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/69b68363-99e4-42eb-875f-00255bb68534/maya-lod-group-selection.png)

   Click image for full size.
2. Go to the file menu and select Export Selection.

   [![Maya Export Selection](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/61a08a35-903c-4bd1-8457-daf32af6a025/maya-export-selection.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/61a08a35-903c-4bd1-8457-daf32af6a025/maya-export-selection.png)

   Click image for full size.
3. Choose the path where you want to save your mesh. Make sure to give it a name, choose FBX as the file format, and enable the export of animations in the FBX exporter properties. Enabling animation is required for LODs to be exported.

   [![[Maya Save Export](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a7f306e1-4914-409a-b04c-2df80908a7a1/maya-save-fbx-export.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a7f306e1-4914-409a-b04c-2df80908a7a1/maya-save-fbx-export.png)

   Click image for full size.

   1. In 3ds Max select the Group of meshes that comprise the LOD Set and any collision geometry.

      [![Maya LOD Export Select](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3fd43058-225a-4eff-9d89-7bfa597d2376/3ds-lod-group-export.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3fd43058-225a-4eff-9d89-7bfa597d2376/3ds-lod-group-export.png)

      Click image for full size.
   2. Go to the file menu and select *Export* > *Export Selected*.

      [![3ds Max Export Selection](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cbcaf178-d95d-46e6-9bb6-a811fe579d4e/3ds-export-selection.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cbcaf178-d95d-46e6-9bb6-a811fe579d4e/3ds-export-selection.png)

      Click image for full size.
   3. Choose the path where you want to save your mesh. Make sure to give it a name, choose FBX as the file format, and then save.

      [![[3ds Max Save Export](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8e9a0c91-2cdf-42ce-b00c-1d41429e2413/3ds-save.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8e9a0c91-2cdf-42ce-b00c-1d41429e2413/3ds-save.png)

      Click image for full size.
   4. In the FBX Export window enable animation under the Animation properties. This is required for LODs to be exported.

      [![3ds Max Enable Animation on Export](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ebffefb1-28d2-42fc-8ab4-48066da8c96f/3ds-animation-checked.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ebffefb1-28d2-42fc-8ab4-48066da8c96f/3ds-animation-checked.png)

      Click image for full size.

      ## Importing Static Mesh LODs

      Importing Static Mesh LODs is done a few ways. One option uses the *Content Browser*, as shown below, and the other is from within the *Details* panel in the *Static Mesh Editor*. To learn how to import LOD from the Static Mesh Editor, refer to the [Creating and Using LODs](/documentation/en-us/unreal-engine/creating-and-using-lods-in-unreal-engine) documentation.

      1. In the **Content Browser**, click the **Import** button.

         [![Import Button](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/93d18dda-d77b-4a02-9610-53ad26c40e85/05-import-button-ui.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/93d18dda-d77b-4a02-9610-53ad26c40e85/05-import-button-ui.png)

         Click image for full size.
      2. Locate and select the FBX file you want to import.

         [![Import Dialog Box](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4deae93e-1d94-4f0c-8ad8-b49a5827153f/import-fbx.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4deae93e-1d94-4f0c-8ad8-b49a5827153f/import-fbx.png)

         Click image for full size.
      3. Click **Open** to begin importing the mesh file to your project.
      4. In the **FBX Import Options** dialog box, choose the appropriate settings, making sure the **Import LODs** option, under **Mesh** > **Advanced**, is enabled.

         [![Import FBX Option](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6bad621c-7d67-4d87-a993-26699a5728dd/07-import-fbx-options.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6bad621c-7d67-4d87-a993-26699a5728dd/07-import-fbx-options.png)

         Click image for full size.

      There are two import buttons available to us in the FBX Importer. The first option is the Import button, making it possible to import the currently selected FBX file with your specified settings. The second option is the Import All button; this imports all of the currently selected FBX files with our specified settings.

      For more information on the settings in the FBX Importer, refer to the [FBX Import Options Reference](/documentation/en-us/unreal-engine/fbx-import-options-reference-in-unreal-engine) documentation.

      1. Click **Import** or **Import All** to import the mesh to your project.

         [![Import FBX Dialog Box](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/094ab774-0d30-4247-aeef-a2851fa5e872/fbx-import-options.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/094ab774-0d30-4247-aeef-a2851fa5e872/fbx-import-options.png)

         Click image for full size.

         When importing LODs, the name of the imported mesh will follow default [Naming Conventions](/documentation/en-us/unreal-engine/fbx-import-options-reference-in-unreal-engine#namingconventions). Refer to our [FBX Import Dialog](/documentation/en-us/unreal-engine/fbx-import-options-reference-in-unreal-engine) documentation for additional information about all of the settings.
      2. Your imported mesh will show in the **Content Browser**, along with any Textures and Materials applied.

         [![Imported Static Mesh](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5889b66c-23c8-46f1-98c8-f8969ca0b8d5/lod-static-mesh-in-content-browser.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5889b66c-23c8-46f1-98c8-f8969ca0b8d5/lod-static-mesh-in-content-browser.png)

         Click image for full size.
      3. Double-click the Static Mesh to open the **Static Mesh Editor**. By viewing the imported mesh in the **Static Mesh Editor**, you can cycle through its LODs using the **Auto LOD** dropdown.

         ![Cycle through LODs](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e36ee49e-db97-4ad7-9cdc-898b30078306/cycle-lods.gif)

      Now that you have reached the end of this guide, you've learned:

      ✓ How to set up Static Mesh LODs from external 3D modeling applications.  
      ✓ How to export Static Mesh LODs from external 3D modeling applications.  
      ✓ How to import Static Mesh LODs into Unreal Editor from external 3D modeling applications.

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [static mesh](https://dev.epicgames.com/community/search?query=static%20mesh)
* [fbx static mesh pipeline](https://dev.epicgames.com/community/search?query=fbx%20static%20mesh%20pipeline)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisites](/documentation/en-us/unreal-engine/importing-static-mesh-lods-using-fbx-in-unreal-engine?application_version=5.7#prerequisites)
* [Objectives](/documentation/en-us/unreal-engine/importing-static-mesh-lods-using-fbx-in-unreal-engine?application_version=5.7#objectives)
* [Setting-up Static Mesh LODs](/documentation/en-us/unreal-engine/importing-static-mesh-lods-using-fbx-in-unreal-engine?application_version=5.7#setting-upstaticmeshlods)
* [Exporting Static Mesh LODs](/documentation/en-us/unreal-engine/importing-static-mesh-lods-using-fbx-in-unreal-engine?application_version=5.7#exportingstaticmeshlods)
* [Importing Static Mesh LODs](/documentation/en-us/unreal-engine/importing-static-mesh-lods-using-fbx-in-unreal-engine?application_version=5.7#importingstaticmeshlods)

Related documents

[FBX Import Options Reference

![FBX Import Options Reference](https://dev.epicgames.com/community/api/documentation/image/4afaabe2-dfc0-488f-93cb-109043970488?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/fbx-import-options-reference-in-unreal-engine)

[FBX Static Mesh Pipeline

![FBX Static Mesh Pipeline](https://dev.epicgames.com/community/api/documentation/image/76d06d5b-4f87-4fce-a274-0a2c84abc6fe?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/fbx-static-mesh-pipeline-in-unreal-engine)
