<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/importing-static-meshes-using-fbx-in-unreal-engine?application_version=5.7 -->

# Importing Static Meshes Using FBX

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
8. Importing Static Meshes Using FBX

# Importing Static Meshes Using FBX

Learn how to import static meshes.

![Importing Static Meshes Using FBX](https://dev.epicgames.com/community/api/documentation/image/c5fc25b6-f302-4b84-bf10-07212a937b3f?resizing_type=fill&width=1920&height=335)

 On this page

Choose your operating system

Windows
macOS
Linux

We can import static meshes into Unreal Engine from external 3D modeling applications, such as **3DS Max**, **Maya** or **Blender**. Although we're using 3DS Max and Maya to illustrate this lesson's goal, you can import **static meshes** into Unreal Engine from any 3D modeling application with a save feature.

Before getting started: Please make sure you have access to a 3D modeling application.

## Goals

The focus of this guide is to show you how to import static meshes from external 3D modeling applications.

## Objectives

After going through this guide, you'll know:

* How to import static meshes into Unreal Editor from external 3D modeling applications.
* How to verify that static meshes were imported properly.

The Unreal Engine FBX import pipeline uses **FBX 2020.2**. Using a different version during export may result in incompatibilities.

Choose Your 3D Art Tool

Autodesk Maya
Autodesk 3ds Max

## Importing Static Meshes from External 3D Modeling Applications

1. Select the mesh(es) and joints to be exported in the viewport.

   ![meshAndJointsSel.png](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/602453e5-bf0a-4369-9104-3af0dffec120/meshandjointssel.png)
2. In the *File* menu choose *Export Selection* (or *Export All* if you want to export everything in the scene regardless of selection).

   ![maya_export_2.jpg](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2167b9b1-0cb7-4523-9962-d630d1886fdc/maya_export_2.jpg)
3. Choose the location and name for the FBX file to export the mesh(es) to and set the appropriate options in the **FBX Export** dialog and then click the ![maya_export_button.jpg](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/09d01e10-a9ee-4269-a8c1-7b5b068b741b/maya_export_button.jpg) button to create the FBX file containing the mesh(es).

   ![maya_export_3.jpg](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/76afa621-6fa7-482c-893b-7cc5c5b1be92/maya_export_3.jpg)



1. Select the mesh(es) and bones to be exported in the viewport.

   ![max_export_1.png](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4bc331ff-4e3f-47c9-b635-46c24587f036/max_export_1.png)
2. In the *File* menu, choose *Export Selected* (or *Export All* if you want to export everything in the scene regardless of selection).

   ![max_export_2.jpg](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6d0b005f-a543-4d75-930e-dd74dc98da49/max_export_2.jpg)
3. Choose the location and name for the FBX file to export the mesh(es) to and click the ![max_save_button.jpg](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8ca264d4-7ca8-4e59-9030-025beb7229f1/max_save_button.jpg) button.

   ![max_export_3.jpg](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a2d1f95a-cc0f-45a4-9692-21e00448f723/max_export_3.jpg)
4. Set the appropriate options in the **FBX Export** dialog and then click the ![max_ok_button.jpg](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/382e0b58-7622-487a-a2ca-07a00d227b9d/max_ok_button.jpg) button to create the FBX file containing the mesh(es).

   ![max_export_4.jpg](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/207f2370-295a-4412-8a0d-8cc3de6043a8/max_export_4.jpg)

## Verifying Imported Static Meshes

Double-click the imported mesh to view it in the **Static Mesh Editor**.

[![Verify Static Mesh](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9cb3e3fe-6431-417c-84a5-e6c9d6c70642/05-verify-static-mesh.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9cb3e3fe-6431-417c-84a5-e6c9d6c70642/05-verify-static-mesh.png)

Click image for full size.

[![Verify Static Mesh](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3c3d0862-a1a5-4a51-883a-91a6a046936a/verifystaticmesh_mac.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3c3d0862-a1a5-4a51-883a-91a6a046936a/verifystaticmesh_mac.png)

Click image for full size.

*Verify that the asset imported properly by viewing the imported mesh in the **Static Mesh Editor**.*

Now that we've reached the end of this guide, you've learned:

✓ How to import static meshes into Unreal Editor from external 3D modeling applications.  
✓ How to verify that static meshes were imported properly.

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [optimization](https://dev.epicgames.com/community/search?query=optimization)
* [fbx static mesh pipeline](https://dev.epicgames.com/community/search?query=fbx%20static%20mesh%20pipeline)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Goals](/documentation/en-us/unreal-engine/importing-static-meshes-using-fbx-in-unreal-engine?application_version=5.7#goals)
* [Objectives](/documentation/en-us/unreal-engine/importing-static-meshes-using-fbx-in-unreal-engine?application_version=5.7#objectives)
* [Importing Static Meshes from External 3D Modeling Applications](/documentation/en-us/unreal-engine/importing-static-meshes-using-fbx-in-unreal-engine?application_version=5.7#importingstaticmeshesfromexternal3dmodelingapplications)
* [Verifying Imported Static Meshes](/documentation/en-us/unreal-engine/importing-static-meshes-using-fbx-in-unreal-engine?application_version=5.7#verifyingimportedstaticmeshes)

Related documents

[FBX Import Options Reference

![FBX Import Options Reference](https://dev.epicgames.com/community/api/documentation/image/4afaabe2-dfc0-488f-93cb-109043970488?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/fbx-import-options-reference-in-unreal-engine)

[FBX Static Mesh Pipeline

![FBX Static Mesh Pipeline](https://dev.epicgames.com/community/api/documentation/image/76d06d5b-4f87-4fce-a274-0a2c84abc6fe?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/fbx-static-mesh-pipeline-in-unreal-engine)
