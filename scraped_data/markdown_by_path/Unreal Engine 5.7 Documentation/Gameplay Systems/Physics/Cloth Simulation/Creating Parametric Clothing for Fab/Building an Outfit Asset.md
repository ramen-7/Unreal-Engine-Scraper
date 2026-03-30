<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine?application_version=5.7 -->

# Building an Outfit Asset

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
5. [Gameplay Systems](/documentation/en-us/unreal-engine/gameplay-systems-in-unreal-engine "Gameplay Systems")
6. [Physics](/documentation/en-us/unreal-engine/physics-in-unreal-engine "Physics")
7. [Cloth Simulation](/documentation/en-us/unreal-engine/cloth-simulation-in-unreal-engine "Cloth Simulation")
8. [Creating Parametric Clothing for Fab](/documentation/en-us/unreal-engine/creating-parametric-clothing-for-fab "Creating Parametric Clothing for Fab")
9. Building an Outfit Asset

# Building an Outfit Asset

Building an outfit asset in Unreal Engine.

![Building an Outfit Asset](https://dev.epicgames.com/community/api/documentation/image/30a74804-20a3-4ac4-bffe-0c8b1f544b16?resizing_type=fill&width=1920&height=335)

 On this page

## Before You Begin

You must have a clothing model (FBX or USD) available to import into **Unreal Editor**. This tutorial uses the working folder **techwearOutfit**inside the **Content Browser** at this path:

`All/Content/Outfits/techwearOutfit/techwearOutfit`

[![Working Folder](https://dev.epicgames.com/community/api/documentation/image/683700aa-f613-4dc3-b128-e6a3b146e2e9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/683700aa-f613-4dc3-b128-e6a3b146e2e9?resizing_type=fit)

It also uses the skeletal mesh generated in [Creating Your MetaHuman](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-your-metahuman-in-unreal-engine):

`bodyShapeG_CombinedSkelMesh`

If your model is already imported and has dependencies in other locations within the Editor, any dependencies (such as shared assets like skeletons and parent materials) must be moved into the same working folder as your model.

This tutorial requires certain Unreal Engine plugins to create cloth assets. For information on setting up plugins, see [Parametric Asset Setup](https://dev.epicgames.com/documentation/en-us/unreal-engine/parametric-asset-setup).

To move shared assets, follow these steps:

1. In the **Content Browser**, drag the shared assets to the working folder and select **Move Here** in the contextual dialog box.

   [![Move Here](https://dev.epicgames.com/community/api/documentation/image/c49a9ed7-dd5e-4261-a5c4-88a130ec3b0a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c49a9ed7-dd5e-4261-a5c4-88a130ec3b0a?resizing_type=fit)
2. To update asset references, right-click on the working folder and select **Update Redirector References**.

   [![Update Redirector References](https://dev.epicgames.com/community/api/documentation/image/0241d963-10ef-4ec4-85cb-62f233bb76b2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0241d963-10ef-4ec4-85cb-62f233bb76b2?resizing_type=fit)

   The **Move Here** option updates asset references. **Copy Here** does not.

## Selecting a Workflow Path

The process of creating LODs can differ depending on your development needs. For the purpose of this tutorial, choose the workflow path that best matches your needs:

* [Path A](https://dev.epicgames.com/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine#path-a): Your model is an FBX, and only has a render mesh. If you are converting your existing **MetaHuman** clothing to be parametric, choose this path.
* [Path B](https://dev.epicgames.com/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine#path-b): Your model is a USD exported from Marvelous Designer or Clo, which has a sim and render mesh.
* [Path C](https://dev.epicgames.com/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine#path-c): Your model is a render mesh and you have created a sim mesh by hand.

## Path A

### Importing Your FBX

1. Drag your FBX into the working folder in the **Content Browser**. Alternatively, you can click **Import**.

   [![Content Browser Import](https://dev.epicgames.com/community/api/documentation/image/81b0e334-05c1-4413-a72a-4f8f379d74f7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/81b0e334-05c1-4413-a72a-4f8f379d74f7?resizing_type=fit)
2. In the **Import Content** dialog, leave all options as default and click **Import**. Your asset will import as a static mesh (or a skeletal mesh if your FBX has a skeleton).
3. Name the static mesh `techwear_bodyShapeG_LOD0`.

While it is possible to import FBXs with rigging or skinning information as skeletal meshes (instead of static meshes), it is not recommended due to issues with visualization in the Dataflow Editor.

### Creating a Cloth Asset

1. To create a cloth asset, inside your working folder, right-click in the Content Browser and select **Physics > Cloth Asset**.

   [![Create Cloth Asset](https://dev.epicgames.com/community/api/documentation/image/d2782e96-0fe6-467d-b88c-690eb53bd0af?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d2782e96-0fe6-467d-b88c-690eb53bd0af?resizing_type=fit)
2. Name your new cloth asset `CA_techwearOutfit_bodyShapeG`. This creates a new Dataflow asset.

   [![Name Cloth Asset](https://dev.epicgames.com/community/api/documentation/image/cc45ca7e-4536-42cb-b3e0-33e51a499d08?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cc45ca7e-4536-42cb-b3e0-33e51a499d08?resizing_type=fit)
3. Right-click your cloth asset, and select **Open in Dataflow Editor (Experimental)** to open your asset in the **Dataflow Editor**.

   [![Dataflow Nodes](https://dev.epicgames.com/community/api/documentation/image/c34259e3-0889-448f-ab9d-2f2efe0d5cdd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c34259e3-0889-448f-ab9d-2f2efe0d5cdd?resizing_type=fit)

   If you only have one LOD, select and delete all nodes inside the **Graph** tab, except for the following four:

   * **TransferSkinWeights**
   * **Remesh**
   * **Remesh\_LOD2**
   * **ClothAssetTerminal**

   Your graph should now look like this:

   [![Path A Clean Graph](https://dev.epicgames.com/community/api/documentation/image/b2a37634-1cbf-4a09-99ad-ecb6e5957a9d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b2a37634-1cbf-4a09-99ad-ecb6e5957a9d?resizing_type=fit)

   If you handmade LODs, delete all nodes except the following two:

   * **TransferSkinWeights**
   * **ClothAssetTerminal**

   Your graph should now look like this:

   [![Path A Clean Graph Handmade](https://dev.epicgames.com/community/api/documentation/image/684580a2-dc60-4f9c-98aa-409926b2261a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/684580a2-dc60-4f9c-98aa-409926b2261a?resizing_type=fit)

### Setting Up Your Meshes in Dataflow Editor

1. In the Dataflow Editor, in the Graph tab, right-click and search for **StaticMeshImport**. Click it or drag to add the StaticMeshImport node to the graph.
2. In the **Node Details** panel, on the right side of the editor, uncheck **Import Sim Mesh**.
3. In the dropdown menu next to **Static Mesh**, select your model’s static mesh. In this tutorial, it’s called `techwear_bodyShapeG_LOD0`. Alternatively, you can select the static mesh in the Content Browser and click the **Use Selected Asset From Content Browser** button.

   [![Path A Node Details Panel](https://dev.epicgames.com/community/api/documentation/image/8cfc1b91-1953-4cda-87ae-fc04e992fa69?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8cfc1b91-1953-4cda-87ae-fc04e992fa69?resizing_type=fit)
4. In the Graph tab, connect the **Collection** pin on the **StaticMeshImport** node to the Collection pin on the **TransferSkinWeights**node.
5. With the TransferSkinWeights node selected, return to the Node Details panel:

   * Under the **Target Mesh(es)** dropdown, select **Render Mesh**.
   * Under the **Render Mesh Transfer Source** dropdown, select **Skeletal Mesh**.
   * Under **Skeletal Mesh**, select `bodyShapeG_CombinedSkelMesh` created in [Creating Your Metahuman](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-your-metahuman-in-unreal-engine).
   * Under the **Transfer Method** dropdown, select **Closest Point on Surface**.
6. In the Graph tab, connect the **Collection**(out) pin on the TransferSkinWeights node to the **Collection Lods[0]** pin on the ClothAssetTerminal node.

   [![Path A Connect SkinTransferWeights](https://dev.epicgames.com/community/api/documentation/image/747aadad-4b2c-4726-97d1-a45ff2cff774?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/747aadad-4b2c-4726-97d1-a45ff2cff774?resizing_type=fit)

If you do not wish to add or generate any LODs, right-click on the **ClothAssetTerminal** and select **Remove Option** **Pin** to remove the remaining pins (so it does not expect any more LODs). Then, proceed to [Creating an Outfit Asset](https://dev.epicgames.com/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine#creating-an-outfit-asset).

If you need to add hand-generated LODs or automatically-generated LODs, continue to [Path A: Setting Up LODs](https://dev.epicgames.com/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine#path-a-setting-up-lo-ds).

### Path A: Setting Up LODs

This tutorial covers both hand-generated LODs and automatically-generated LODs.

#### Hand-Generated LODs

1. In the Graph tab, right-click on the ClothAssetTerminal node and select **Add Pin**to add a fourth pin.
2. Duplicate the **StaticMeshImport** and **TransferSkinWeights** nodes three times. Working in ascending order, in the Nodes Details panel of each new **TransferSkinWeights** node, select the new static meshes and skeletal meshes associated with that LOD.

   [![Path A Hand Generated LODs](https://dev.epicgames.com/community/api/documentation/image/4d79ecae-a8e7-47be-a50e-cb258c259307?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4d79ecae-a8e7-47be-a50e-cb258c259307?resizing_type=fit)

MetaHuman expects four body LODs; 0, 1, 2, and 3.

#### Automatically-Generated LODs

1. In the Graph tab, right-click and search for **Remesh**. Drag the Remesh node to the graph.
2. Connect the **Collection** (out) pin on the TransferSkinWeights node to the **Collection** (in) pin of the Remesh node. Don’t disconnect TransferSkinWeights from ClothAssetTerminal.

   [![Path A Connect Remesh](https://dev.epicgames.com/community/api/documentation/image/0fbf7b81-6bfb-4bbf-98e5-78dc2d1abbc5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0fbf7b81-6bfb-4bbf-98e5-78dc2d1abbc5?resizing_type=fit)
3. With the Remesh node selected, in the Details panel, uncheck the **Remesh Sim** checkbox. Check **Remesh Render**.

   [![Remesh Node Details](https://dev.epicgames.com/community/api/documentation/image/458ea71f-6f81-4706-a392-f42d545ef8a4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/458ea71f-6f81-4706-a392-f42d545ef8a4?resizing_type=fit)
4. You can visualize changes made in the settings of the Remesh node by enabling the Construction **Viewport**. In the Construction Viewport tab of the Dataflow Editor, click the dropdown in the top-right corner and select **Render**.

   [![Path A Construction Viewport](https://dev.epicgames.com/community/api/documentation/image/bc204dad-a66f-40c7-92c8-aa3054b4e0a6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bc204dad-a66f-40c7-92c8-aa3054b4e0a6?resizing_type=fit)

   You can also change the Construction Viewport display from Lit to Wireframe and many other options.

   If you do not see your asset in the Construction Viewport, always check whether Render is selected. This option can become deselected easily.
5. Connect the Remesh node’s **Collection** (out) pin to the ClothAssetTerminal.

   [![Path A Connect Remesh to ClothAssetTerminal](https://dev.epicgames.com/community/api/documentation/image/745e4d68-3dba-4cd3-bcdb-5fba23305082?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/745e4d68-3dba-4cd3-bcdb-5fba23305082?resizing_type=fit)
6. Repeat steps 1, 2, 3, and 5 for each LOD. For this tutorial, you will adjust each Remesh node's **Target Percent Render** in the Node Details panel. In practice these can be adjusted as needed:

   * Remesh node for **LOD[1]**: Set Target Percent Render to 50.
   * Remesh node for **LOD[2]**: Set Target Percent Render to 30.
   * Remesh node for **LOD[3]**: Set Target Percent Render to 10.

   [![Path A Final Graph](https://dev.epicgames.com/community/api/documentation/image/2bbbb893-78c0-4277-be32-d6710573f14b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2bbbb893-78c0-4277-be32-d6710573f14b?resizing_type=fit)

Proceed to [Creating an Outfit Asset](https://dev.epicgames.com/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine#creating-an-outfit-asset).

## Path B

### Creating a Cloth Asset

1. To create a cloth asset, inside your working folder, right-click in the Content Browser and select **Physics > Cloth Asset**.

   [![Create Cloth Asset](https://dev.epicgames.com/community/api/documentation/image/d2e2562a-4569-46df-ab46-3f6ef89d10c4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d2e2562a-4569-46df-ab46-3f6ef89d10c4?resizing_type=fit)
2. Name your new cloth asset `CA_techwearOutfit_bodyShapeG`. This creates a new Dataflow asset.

   [![Name Cloth Asset](https://dev.epicgames.com/community/api/documentation/image/886e38f6-6cb5-4cbe-9ad7-1336ac2e008c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/886e38f6-6cb5-4cbe-9ad7-1336ac2e008c?resizing_type=fit)
3. Right-click `CA_techwearOutfit_bodyShapeG`, and select **Open in Dataflow Editor (Experimental)** to open your asset in the Dataflow Editor.

   [![Dataflow Nodes](https://dev.epicgames.com/community/api/documentation/image/8e7e066b-9ec5-46c1-a711-41769dcdf166?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8e7e066b-9ec5-46c1-a711-41769dcdf166?resizing_type=fit)
4. In the Graph panel, delete all but the following nodes:

   * **USDimport**
   * **TransferSkinWeights**
   * **Remesh**
   * **Remesh\_LOD2**
   * **ClothAssetTerminal**

   Your graph should now look like this:

   [![Path B Clean Graph](https://dev.epicgames.com/community/api/documentation/image/3242bff2-687f-4952-989d-533c743a96c8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3242bff2-687f-4952-989d-533c743a96c8?resizing_type=fit)

### Setting Up Your Meshes in Dataflow Editor

1. In the Graph panel, select the **USDImport** node. In the Node Details panel, import your USD by clicking the three dots next to **USD File**.

   [![Path B Node Details Panel](https://dev.epicgames.com/community/api/documentation/image/846e349b-7905-48b0-9131-84be6338328a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/846e349b-7905-48b0-9131-84be6338328a?resizing_type=fit)

   Once imported, your asset should be visible in the Construction Viewport in the Dataflow Editor.

   A new folder containing your USD file, materials, static meshes, and textures will appear in your working folder in the Content Browser.
2. Connect the **Collection** pin on the USDImport node to the **Collection** (in) pin on the TransferSkinWeights node.

   [![Path B Connet TransferSkinWeights](https://dev.epicgames.com/community/api/documentation/image/163f91c8-fa58-462e-9610-ef2676057010?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/163f91c8-fa58-462e-9610-ef2676057010?resizing_type=fit)
3. Select the TransferSkinWeights node. In the Node Details panel, under **Skeletal Mesh**, select `bodyShapeG_CombinedSkelMesh`. This was created in [Creating Your Metahuman](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-your-metahuman-in-unreal-engine).
4. In the Graph panel, connect the **Collection** (out) pin on the TransferSkinWeights node to the **Collection LOD[0]** pin on the ClothAssetTerminal node.

   Your graph should now look like this:

   [![Path B Final Clean Graph](https://dev.epicgames.com/community/api/documentation/image/809c487d-789b-4c1e-a8bc-eef140ea0dec?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/809c487d-789b-4c1e-a8bc-eef140ea0dec?resizing_type=fit)

If you do not wish to add or generate any more LODs, right-click on the **ClothAssetTerminal** select **Remove Option Pin** to remove the remaining pins (so it does not expect any more LODs). Then, proceed to [Creating an Outfit Asset](https://dev.epicgames.com/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine#creating-an-outfit-asset).

If you need to generate more LODs, continue to [Path B: Setting Up LODs.](https://dev.epicgames.com/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine#path-b-setting-up-lo-ds)

### Path B: Setting Up LODs

1. In the Graph tab, right-click and search for Remesh. Drag the Remesh node to the graph.
2. In the Graph tab, connect the **Collection** (out) pin on the TransferSkinWeights node to the **Collection** (in) pin of the Remesh node. Don’t disconnect TransferSkinWeights from ClothAssetTerminal.

   [![Path B Connect Remesh](https://dev.epicgames.com/community/api/documentation/image/c2ca60dc-28e0-4040-b202-a590f61ac249?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c2ca60dc-28e0-4040-b202-a590f61ac249?resizing_type=fit)
3. You can visualize changes made in the settings of the Remesh node by enabling the **Construction Viewport**. In the Construction Viewport tab of the Dataflow Editor, click the dropdown in the top-right corner and select **Render**.

   [![Path B Construction Viewport](https://dev.epicgames.com/community/api/documentation/image/47ee1bf6-e0d5-48b5-be21-3f59d5f5d3cc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/47ee1bf6-e0d5-48b5-be21-3f59d5f5d3cc?resizing_type=fit)

   You can also change the Construction Viewport display from Lit to Wireframe and many other options.

   If you do not see your asset in the Construction Viewport, always check whether Render is selected. This option can become deselected easily.
4. Connect the Remesh node’s **Collection** (out) pin to the ClothAssetTerminal.
5. Repeat steps 1, 2, and 4 for each LOD. For this tutorial, adjust each Remesh node's **Target Percent Render** in the Node Details panel:

   * Remesh node for **LOD[1]**: Set Target Percent Render to 50.
   * Remesh node for **LOD[2]**: Set Target Percent Render to 30.
   * Remesh node for **LOD[3]**: Set Target Percent Render to 10.

   [![Path B Final Graph](https://dev.epicgames.com/community/api/documentation/image/e0e493ea-daf9-431e-8f89-1456c85f336d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e0e493ea-daf9-431e-8f89-1456c85f336d?resizing_type=fit)

Proceed to [Creating an Outfit Asset](https://dev.epicgames.com/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine#creating-an-outfit-asset).

## Path C

### Importing Your Render and Sim Meshes

1. Drag your sim and render meshes into the working folder in the **Content Browser**. Alternatively, you can click **Import**.

   [![Content Browser Import](https://dev.epicgames.com/community/api/documentation/image/5f5659a3-0651-4d0a-928f-887625fe988e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5f5659a3-0651-4d0a-928f-887625fe988e?resizing_type=fit)
2. In the **Import Content** dialog, leave all options as default and click **Import**. Name the static mesh `techwear_bodyShapeG_LOD0`.

### Creating a Cloth Asset

1. To create a cloth asset, inside your working folder, right-click in the Content Browser and select **Physics > Cloth Asset**.

   [![Create Cloth Asset](https://dev.epicgames.com/community/api/documentation/image/d2e2562a-4569-46df-ab46-3f6ef89d10c4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d2e2562a-4569-46df-ab46-3f6ef89d10c4?resizing_type=fit)
2. Name your new cloth asset `CA_techwearOutfit_bodyShapeG`. This creates a new Dataflow asset.

   [![Name Cloth Asset](https://dev.epicgames.com/community/api/documentation/image/886e38f6-6cb5-4cbe-9ad7-1336ac2e008c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/886e38f6-6cb5-4cbe-9ad7-1336ac2e008c?resizing_type=fit)
3. Right-click `CA_techwearOutfit_bodyShapeG`, and select **Open in Dataflow Editor (Experimental)** to open your asset in the **Dataflow Editor**.

   [![Dataflow Nodes](https://dev.epicgames.com/community/api/documentation/image/8e7e066b-9ec5-46c1-a711-41769dcdf166?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8e7e066b-9ec5-46c1-a711-41769dcdf166?resizing_type=fit)

   If you only have one LOD, select and delete all nodes inside the **Graph** tab, except for the following four:

   * **TransferSkinWeights**
   * **Remesh**
   * **Remesh\_LOD2**
   * **ClothAssetTerminal**

   Your graph should now look like this:

   [![Path C Clean Graph One LOD](https://dev.epicgames.com/community/api/documentation/image/e961ea35-5fed-4a10-a503-0dc0d66af2be?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e961ea35-5fed-4a10-a503-0dc0d66af2be?resizing_type=fit)

   If you handmade LODs, delete all nodes except the following two:

   * **TransferSkinWeights**
   * **ClothAssetTerminal**

   Your graph should now look like this:

   [![Path C Clean Graph Handmade LODs](https://dev.epicgames.com/community/api/documentation/image/a3d08e21-0e61-45f2-bf24-42f5ef0e89a3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a3d08e21-0e61-45f2-bf24-42f5ef0e89a3?resizing_type=fit)

### Setting Up Your Meshes in Dataflow Editor

1. In the Dataflow Editor, in the Graph tab, right-click and search for **StaticMeshImport**. Click it or drag to add it to the graph.
2. In the **Node Details** panel, on the right side of the editor, verify that **Import Sim Mesh** is checked and **Import Render Mesh** is unchecked.

   [![Path C Node Details Panel](https://dev.epicgames.com/community/api/documentation/image/8551fbf6-644d-43f2-a24e-b2c5add100d2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8551fbf6-644d-43f2-a24e-b2c5add100d2?resizing_type=fit)
3. In the dropdown menu next to **Static Mesh**, select your model’s sim mesh. Alternatively, you can select the static mesh in the Content Browser and click the **Use Selected Asset From Content** Browser button.
4. In the Graph, create a second StaticMeshImport node. In the Node Details panel, uncheck **Import Sim Mesh** and check **Import Render Mesh**.

   [![Path C Node Details Panel Render Mesh](https://dev.epicgames.com/community/api/documentation/image/6360c0a3-fbd0-4b6f-afd1-26ab17445b66?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6360c0a3-fbd0-4b6f-afd1-26ab17445b66?resizing_type=fit)
5. In the dropdown menu next to **Static Mesh**, select your model’s render mesh.
6. In the Graph, create a **MergeClothCollections** node. Connect the **Collection** pins of both StaticMeshImport nodes to the **Collection** (in) pins of the MergeClothCollections node.

   [![Path C Connect MergeClothCollections](https://dev.epicgames.com/community/api/documentation/image/464bf7cd-78e6-468a-8e58-b03aa8e4ec4e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/464bf7cd-78e6-468a-8e58-b03aa8e4ec4e?resizing_type=fit)
7. Connect the **Collection** (out) pin on the MergeClothCollections node to the **Collection** (in) pin on the TransferSkinWeights node.

   [![Path C Connect TransferSkinWeights](https://dev.epicgames.com/community/api/documentation/image/5f9c9198-2626-478d-b7db-293523707a6a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5f9c9198-2626-478d-b7db-293523707a6a?resizing_type=fit)
8. Select the TransferSkinWeights node. In the Node Details panel, under **Skeletal Mesh**, select `bodyShapeG_CombinedSkelMesh`.
9. In the Graph panel, connect the **Collection** (out) pin on the TransferSkinWeights node to the **Collection LOD[0]** pin on the ClothAssetTerminal node.

   Your graph should now look like this:

   [![Path C Final Graph](https://dev.epicgames.com/community/api/documentation/image/53c71703-2c47-4926-b471-a3d7f3db7a06?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/53c71703-2c47-4926-b471-a3d7f3db7a06?resizing_type=fit)

If you do not wish to add or generate any more LODs, right-click on the **ClothAssetTerminal** select **Remove Option Pin** to remove the remaining pins (so it does not expect any more LODs). Then, proceed to [Creating an Outfit Asset](https://dev.epicgames.com/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine#creating-an-outfit-asset).

If you need to generate more LODs, continue to [Path C: Setting Up LODs](https://dev.epicgames.com/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine#path-c-setting-up-lo-ds).

### Path C: Setting Up LODs

This tutorial covers both hand-generating LODs and automatically-generating LODs.

#### Automatically-Generated LODs

1. In the Graph tab, right-click and search for **Remesh**. Drag the Remesh node to the graph.
2. Connect the **Collection** (out) pin on the TransferSkinWeights node to the **Collection** (in) pin of the Remesh node. Don’t disconnect TransferSkinWeights from ClothAssetTerminal.

   [![Path C Connect Remesh](https://dev.epicgames.com/community/api/documentation/image/27d601fa-fc5c-473f-b478-3a5f6a8cdbfb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/27d601fa-fc5c-473f-b478-3a5f6a8cdbfb?resizing_type=fit)
3. You can visualize changes made in the settings of the Remesh node by enabling the **Construction Viewport**. In the Construction Viewport tab of the Dataflow Editor, click the dropdown in the top-right corner and select **Render**.

   [![Path C Construction Viewport](https://dev.epicgames.com/community/api/documentation/image/c5bd6990-eda5-4950-a370-3b72318625b7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c5bd6990-eda5-4950-a370-3b72318625b7?resizing_type=fit)

   You can also change the Construction Viewport display from Lit to Wireframe and many other options.

   If you do not see your asset in the Construction Viewport, always check whether Render is selected. This option can become deselected easily.
4. Connect the Remesh node’s **Collection** (out) pin to the ClothAssetTerminal.
5. Repeat steps 1, 2, and 4 for each LOD. For this tutorial, you will adjust each Remesh node's **Target Percent Render** in the Node Details panel:

   * Remesh node for **LOD[1]**: Set Target Percent Render to 50.
   * Remesh node for **LOD[2]**: Set Target Percent Render to 30.
   * Remesh node for **LOD[3]**: Set Target Percent Render to 10.

   [![Path C Auto-Generated LODs](https://dev.epicgames.com/community/api/documentation/image/f253d143-94eb-439e-91ed-10001f113fa8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f253d143-94eb-439e-91ed-10001f113fa8?resizing_type=fit)

#### Hand-Generated LODs

1. In the Graph tab, right-click on the ClothAssetTerminal node and select **Add Option Pin** to add a fourth pin.
2. Duplicate the **StaticMeshImport** and **TransferSkinWeights** nodes three times. Working in ascending order, in the Nodes Details panel of each new **TransferSkinWeights** node, select the new static meshes and skeletal meshes associated with that LOD.

   [![Path C Hand-Generated LODs](https://dev.epicgames.com/community/api/documentation/image/28f53e28-e7e3-46bf-b4ef-094d6bae982c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/28f53e28-e7e3-46bf-b4ef-094d6bae982c?resizing_type=fit)

   MetaHuman expects four body LODs; 0, 1, 2, and 3.

Proceed to [Creating an Outfit Asset](https://dev.epicgames.com/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine#creating-an-outfit-asset).

## Creating an Outfit Asset

1. In the Content Browser, navigate to the **techwearOutfit** folder. Right-click and create an outfit asset by selecting **Physics > Outfit Asset**.
2. Name the asset `OA_techwearOutfit`.

   [![Create Outfit Asset](https://dev.epicgames.com/community/api/documentation/image/55b0b056-0d3d-4683-a718-f04d0370ad5c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/55b0b056-0d3d-4683-a718-f04d0370ad5c?resizing_type=fit)

   The outfit asset’s name must match the name of the folder it’s contained in.
3. In the **Select an Outfit Asset Template** dialog, choose **Resizable Outfit**.

   [![Select An Outfit Asset Template](https://dev.epicgames.com/community/api/documentation/image/4f08ed8d-fe38-4b46-b3d8-1fd9247385d7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4f08ed8d-fe38-4b46-b3d8-1fd9247385d7?resizing_type=fit)
4. (Optional) This creates `DF_techwearOutfit`. If you want to package for FAB, click and drag it into your working folder, and select **Move Here** in the contextual popup.

   [![Move Here](https://dev.epicgames.com/community/api/documentation/image/2b6bba86-b480-43ea-bf2b-e99f1f82de9d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2b6bba86-b480-43ea-bf2b-e99f1f82de9d?resizing_type=fit)
5. Double-click on your outfit asset to open up the Dataflow Editor.
6. To speed up evaluation, in the Dataflow Editor, click on the three dots next to **Evaluate Dataflow** **Graph** and choose **Manual Graph Evaluation**.

   [![Manual Graph Evaluation](https://dev.epicgames.com/community/api/documentation/image/ec2c81c9-3791-4dd8-8330-ff5bb1e49946?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ec2c81c9-3791-4dd8-8330-ff5bb1e49946?resizing_type=fit)
7. In the **Dataflow Members** panel, check the **Sized Outfit Source** checkbox. Click the plus (**+**) icon to create an Index for each cloth asset you have that corresponds to a body. In this example, we have two:

   [![Sized Outfit Source](https://dev.epicgames.com/community/api/documentation/image/e44c9851-b000-4107-b9a4-2dd036a570fd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e44c9851-b000-4107-b9a4-2dd036a570fd?resizing_type=fit)
8. Expand the dropdown next to **Index.**In **Size Name**, type the name of your clothing asset. In this case, it's bodyShapeG.

   [![Size Name](https://dev.epicgames.com/community/api/documentation/image/81d36f8e-6217-445e-8067-a3131a431099?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/81d36f8e-6217-445e-8067-a3131a431099?resizing_type=fit)
9. Expand the dropdown next to **Index** and assign your cloth asset to **Source** **Asset**. Your cloth asset is `CA_techwear_bodyShapeG`. Under **Source Body Parts**, assign your skeletal mesh. Your skeletal mesh is `bodyShapeG_combinedSkelMesh`.

   Bodies and cloth assets should be paired; if you made clothing for bodyShapeG, your cloth asset should be assigned to the same index.

   [![Source Asset](https://dev.epicgames.com/community/api/documentation/image/7376d52d-db8e-40e7-89ba-a4736054ba98?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7376d52d-db8e-40e7-89ba-a4736054ba98?resizing_type=fit)
10. (Optional) **Num Resizing Interpolation Points** refers to the number of points on the body that are being sampled in the process of resizing. The more points you use, the more accurate to the body shape your garment will be but it will affect speed. It’s recommended to stay between about 1000 and 2500 but you can feel free to experiment with this setting.

    For this tutorial, you can leave it at the default 1500.
11. In the Dataflow Editor, click **Evaluate Dataflow Graph** and then turn **Automatic Graph Evaluation** back on. A progress bar will indicate successful evaluation, sometimes this can take several minutes.

    [![Manual Graph Evaluation](https://dev.epicgames.com/community/api/documentation/image/89c36992-3383-4680-98ed-68d6dc3086d7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/89c36992-3383-4680-98ed-68d6dc3086d7?resizing_type=fit)

    If you make changes to any of the assets that your outfit asset has dependencies on, you must click Evaluate Dataflow Graph to re-evaluate your outfit asset.

## Next Step

In the next step, you will upload your outfit asset to **MetaHuman Creator**.

* [![Testing and Setup in MetaHuman Creator](https://dev.epicgames.com/community/api/documentation/image/dd922972-0be6-4175-b543-0da067e914b2?resizing_type=fit&width=640&height=640)

  Testing and Setup in MetaHuman Creator

  Test your outfit asset in MetaHuman Creator.](https://dev.epicgames.com/documentation/en-us/unreal-engine/testing-and-setup-in-metahuman-creator)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Before You Begin](/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine?application_version=5.7#beforeyoubegin)
* [Selecting a Workflow Path](/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine?application_version=5.7#selectingaworkflowpath)
* [Path A](/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine?application_version=5.7#path-a)
* [Importing Your FBX](/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine?application_version=5.7#importingyourfbx)
* [Creating a Cloth Asset](/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine?application_version=5.7#creatingaclothasset)
* [Setting Up Your Meshes in Dataflow Editor](/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine?application_version=5.7#settingupyourmeshesindatafloweditor)
* [Path A: Setting Up LODs](/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine?application_version=5.7#path-a-setting-up-lo-ds)
* [Hand-Generated LODs](/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine?application_version=5.7#hand-generatedlods)
* [Automatically-Generated LODs](/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine?application_version=5.7#automatically-generatedlods)
* [Path B](/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine?application_version=5.7#path-b)
* [Creating a Cloth Asset](/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine?application_version=5.7#creatingaclothasset-2)
* [Setting Up Your Meshes in Dataflow Editor](/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine?application_version=5.7#settingupyourmeshesindatafloweditor-2)
* [Path B: Setting Up LODs](/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine?application_version=5.7#path-b-setting-up-lo-ds)
* [Path C](/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine?application_version=5.7#path-c)
* [Importing Your Render and Sim Meshes](/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine?application_version=5.7#importingyourrenderandsimmeshes)
* [Creating a Cloth Asset](/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine?application_version=5.7#creatingaclothasset-3)
* [Setting Up Your Meshes in Dataflow Editor](/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine?application_version=5.7#settingupyourmeshesindatafloweditor-3)
* [Path C: Setting Up LODs](/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine?application_version=5.7#path-c-setting-up-lo-ds)
* [Automatically-Generated LODs](/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine?application_version=5.7#automatically-generatedlods-2)
* [Hand-Generated LODs](/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine?application_version=5.7#hand-generatedlods-2)
* [Creating an Outfit Asset](/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine?application_version=5.7#creating-an-outfit-asset)
* [Next Step](/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine?application_version=5.7#nextstep)
