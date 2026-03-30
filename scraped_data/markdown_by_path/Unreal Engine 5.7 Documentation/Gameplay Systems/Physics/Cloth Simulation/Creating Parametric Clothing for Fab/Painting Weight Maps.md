<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/painting-weight-maps?application_version=5.7 -->

# Painting Weight Maps

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
9. Painting Weight Maps

# Painting Weight Maps

Painting weight maps for parametric outfit assets.

![Painting Weight Maps](https://dev.epicgames.com/community/api/documentation/image/5c7e78e3-e76d-445f-9430-41d498217616?resizing_type=fill&width=1920&height=335)

 On this page

This document provides additional setup which may increase the quality of your parametric outfit asset.

Due to the limitations of skin weight transfer from the body, you may occasionally encounter strange looking artifacts, such as tearing in areas like armpits and upper thigh regions. If you notice these during animation sequences, this means you need to pre-paint maps that control skinning operations. You can paint maps on your garment which can control the following operations:  **Relax**, **Prune**, **Hammer**, **Clamp**, and **Normalize**.

## Painting Weight Maps

Open the cloth asset by right-clicking on it and choosing **Open in Dataflow Editor**. Do not double-click on it.

[![Dataflow Editor](https://dev.epicgames.com/community/api/documentation/image/eec3e4b8-24c4-4f0d-b01d-5412ca65bae5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/eec3e4b8-24c4-4f0d-b01d-5412ca65bae5?resizing_type=fit)

Use the same path that you chose from [Building an Outfit Asset](https://dev.epicgames.com/documentation/en-us/unreal-engine/building-an-outfit-asset-in-unreal-engine):

* **[Path A](https://dev.epicgames.com/documentation/en-us/unreal-engine/painting-weight-maps#path-a)**: Your model is an FBX, and only has a render mesh. If you are converting your existing MetaHuman clothing to be parametric, choose this path.
* **[Path B](https://dev.epicgames.com/documentation/en-us/unreal-engine/painting-weight-maps#path-b)**: Your model is a USD exported from Marvelous Designer or Clo, which has a sim mesh and render mesh.
* **[Path C](https://dev.epicgames.com/documentation/en-us/unreal-engine/painting-weight-maps#path-c)**: Your model is a render mesh and you have created a sim mesh by hand.

### Path A

Click on your **StaticMeshImport** node and then click the **Paint Weight Map** button up at the top of the screen.

[![Paint Weight Map](https://dev.epicgames.com/community/api/documentation/image/b8fde801-7eae-4af9-90a2-d8af900e04e4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b8fde801-7eae-4af9-90a2-d8af900e04e4?resizing_type=fit)

This will create a map on that mesh. However, you will not see anything in the Construction Viewport. In order to view and paint the map, follow these steps:

1. To paint on a render mesh only, in the **Node Details** panel, change the **Vertex Group** to **RenderVertices.**

   [![](https://dev.epicgames.com/community/api/documentation/image/96ff4323-a74e-4413-abe7-c6ee7d5430e9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/96ff4323-a74e-4413-abe7-c6ee7d5430e9?resizing_type=fit)
2. Double-click **Paint Weight Map** and it should appear in the Construction Viewport. If it doesn’t, check to see if **Render** is selected.

   [![Construction Viewport Render](https://dev.epicgames.com/community/api/documentation/image/24a5427c-db66-4d72-8d3b-0b236bcbe229?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/24a5427c-db66-4d72-8d3b-0b236bcbe229?resizing_type=fit)

   Name the map something informative. In this example, the map is for an `LOD_0` mesh which controls “relax,” so we named it `LOD0_relaxMap`.
3. Paint the areas you would want affected by your operation of choice white, and leave everything else black. When you are done, click **Accept**.

   [![Paint Weight Maps](https://dev.epicgames.com/community/api/documentation/image/d03470fe-7cd7-4bec-b241-fe941cf45b3c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d03470fe-7cd7-4bec-b241-fe941cf45b3c?resizing_type=fit)
4. Now, the static mesh is ready to have a map attached. Right-click in the Dataflow graph, type **SetSkinningSelection**, and select it when it pops up.

   * Connect the **Collection** (out) pin of the **PaintWeightMap**to the **Collection** (in) pin of the **SetSkinningSelection**node.
   * Connect the **Attribute Key** pin on **PaintWeightMap**to the **Selection Map** pin on the **SetSkinningSelection** node.
   * Connect the **Collection** (out) pin on the **SetSkinningSelection**node to the **Collection** (in) pin on the **TransferSkinWeights** node.

   [![Weight Painting Nodes](https://dev.epicgames.com/community/api/documentation/image/fc14fd14-2571-451f-91ab-41d22dad6e49?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fc14fd14-2571-451f-91ab-41d22dad6e49?resizing_type=fit)
5. Click on the **SetSkinningSelection** node and in the **Node Details** panel, and change **Vertex Group** to **RenderVertices**.

   [![Node Details Panel](https://dev.epicgames.com/community/api/documentation/image/4dcf8903-80b0-4683-9b0f-070130898e28?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4dcf8903-80b0-4683-9b0f-070130898e28?resizing_type=fit)
6. Set **Correction Type** to whichever type you want to use.

   You can leave the **Selection Map** blank, as it is connected to the **PaintWeightMap** node already via the **Attribute Key** and **Selection Map** connection.

   You can connect the same map to more than one **SetSkinningSelection** node if you wish to use the same map.
7. Now repeat for every asset you want to make maps for. If you hand made LODS, you need to paint maps for those as well.

   Once you’ve done this, you must re-evaluate your cloth asset and save it. Then, open your outfit asset (if you’ve already made one), re-evaluate, and save that too.

   Here is an example of an asset with handmade LODS:

   [![Handmade LODs](https://dev.epicgames.com/community/api/documentation/image/0df28632-b240-49de-a7c7-5fc236a0034f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0df28632-b240-49de-a7c7-5fc236a0034f?resizing_type=fit)

### Path B

Click on the **USDImport**node and then select the **Paint Weight Map** button up at the top of the screen.

[![](https://dev.epicgames.com/community/api/documentation/image/804a02bb-b519-40f1-9d18-86424ce8e015?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/804a02bb-b519-40f1-9d18-86424ce8e015?resizing_type=fit)

1. To paint on the sim mesh, in the **Node Details** panel, change the **Vertex Group** to **SimVertices3d**.

   [![](https://dev.epicgames.com/community/api/documentation/image/01ca06a0-c570-45dd-bbdb-c0e95ae721df?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/01ca06a0-c570-45dd-bbdb-c0e95ae721df?resizing_type=fit)
2. Double-click **Paint Weight Map** and it should appear in the Construction Viewport. If it doesn’t, check to see if **3dSim** is selected.

   Name it something informative. In this example, the map is for an `LOD_0` mesh which controls “relax,” so we named it `LOD0_relaxMap`.
3. Paint the areas you would want affected by your operation of choice in white, and leave everything else black. When you are done, click **Accept**.

   [![Weight Painting](https://dev.epicgames.com/community/api/documentation/image/763b670d-aed0-434e-8bc4-35704bf75fca?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/763b670d-aed0-434e-8bc4-35704bf75fca?resizing_type=fit)
4. Now, the static mesh is ready to have a map attached. Right-click in the Dataflow graph, type `SetSkinningSelection`, and select it when it pops up.

   1. Connect the **Collection** (out) pin of the **PaintWeightMap** node to the **Collection** (in) pin of the **SetSkinningSelection** node.
   2. Connect the **Attribute Key** pin on **PaintWeightMap** to the **Selection Map** pin on the **SetSkinning****Selection** node.
   3. Connect the **Collection** (out) pin on the **SetSkinningSelection** node to the **Collection** (in) pin on the **TransferSkinWeights** node.

   [![Weight Painting Nodes](https://dev.epicgames.com/community/api/documentation/image/11e9e6e8-4db3-454d-b58c-54b9725c34a3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/11e9e6e8-4db3-454d-b58c-54b9725c34a3?resizing_type=fit)
5. Click on the **SetSkinningSelection** node and in the **Node Details** panel. Change **Vertex Group** to **SimVertices3D**.

   Set **Correction Typ**e to whatever you want to use.

   You can leave the **Selection Map** blank, as it is connected to the **PaintWeightMap** node already via the **Attribute Key** or **Selection Map** connection.

   You can connect the same map to more than one **SetSkinningSelection** node if you wish to use the same map.
6. Now repeat for every asset you want to make maps for. If you hand made LODS, you need to paint maps for those as well.

   Once you’ve done this, you must re-evaluate your cloth asset and save it. Then, open your outfit asset (if you’ve already made one), re-evaluate, and save that too.

### Path C

Follow [Path B](https://dev.epicgames.com/documentation/en-us/unreal-engine/painting-weight-maps#path-b), but instead of creating maps on the **USDImport** node, create them on the **MergeClothCollections** node:

[![Collection Node](https://dev.epicgames.com/community/api/documentation/image/fd1d313e-23e7-4930-ac1f-a0b7680aa216?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fd1d313e-23e7-4930-ac1f-a0b7680aa216?resizing_type=fit)

## Additional Optional Setups

Other optional setups include:

* **Resize UVs**: Enables you to set up resizing of UVs where you have a repeating texture.
* **Custom Region Resizing**: Allows you to control **Resizing** where certain portions of your outfit will scale uniformly as opposed to warping with the body. This is useful for hard-surface objects or other portions of a garment you do not wish to warp with the body.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Painting Weight Maps](/documentation/en-us/unreal-engine/painting-weight-maps?application_version=5.7#paintingweightmaps)
* [Path A](/documentation/en-us/unreal-engine/painting-weight-maps?application_version=5.7#path-a)
* [Path B](/documentation/en-us/unreal-engine/painting-weight-maps?application_version=5.7#path-b)
* [Path C](/documentation/en-us/unreal-engine/painting-weight-maps?application_version=5.7#path-c)
* [Additional Optional Setups](/documentation/en-us/unreal-engine/painting-weight-maps?application_version=5.7#additionaloptionalsetups)
