<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-a-fence-generator-using-shape-grammar-in-unreal-engine?application_version=5.7 -->

# Creating a Fence Generator Using Shape Grammar

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
6. [Procedural Content Generation Framework](/documentation/en-us/unreal-engine/procedural-content-generation-framework-in-unreal-engine "Procedural Content Generation Framework")
7. [PCG Development Guides](/documentation/en-us/unreal-engine/pcg-development-guides "PCG Development Guides")
8. Creating a Fence Generator Using Shape Grammar

# Creating a Fence Generator Using Shape Grammar

A how to guide to building a Fence Generator using Shape Grammar.

![Creating a Fence Generator Using Shape Grammar](https://dev.epicgames.com/community/api/documentation/image/a4d383d9-e193-476f-a23a-fc8d67cc9ad9?resizing_type=fill&width=1920&height=335)

 On this page

A common use case for [Shape Grammar](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-shape-grammar-with-pcg-in-unreal-engine) in Unreal Engine's [Procedural Content Generation Framework](https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-content-generation-overview) is building systems. In this example, you will create a fence generator that spawns several static meshes along a spline using grammar and changes the meshes when the spline control points are altered.

This sample uses the [Privacy Fence Pack (with damaged sections)](https://www.fab.com/listings/71f4143b-a429-4c8b-9ae6-8e03609cbaf4) pack available for free on Fab. However, this example could be made using any static meshes of your choice.

## Prerequisites

This how to guide uses terms and concepts discussed in the following documentation:

* [Procedural Content Generation Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-content-generation-overview)
* [Using Shape Grammar With PCG](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-shape-grammar-with-pcg-in-unreal-engine)

## Project Setup

1. [Create a new Project](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-a-new-project-in-unreal-engine) in Unreal Engine.
2. [Create a new Level](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-levels-in-unreal-engine) using the Basic level template. Save your Level.
3. Open **Edit > Plugins** and confirm the following plugins are active:

   1. **Procedural Content Generation Framework (PCG)**
   2. **Procedural Content Generation Framework (PCG) Geometry Script Interop**

[![Activate the Plugins](https://dev.epicgames.com/community/api/documentation/image/fe3c4d50-b007-4538-b2af-66d730250eeb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fe3c4d50-b007-4538-b2af-66d730250eeb?resizing_type=fit)

## Create the Spline

The PCG graph connects to a PCG component and a spline which are contained with a new blueprint class. Create the blueprint class by following the steps below:

1. Create a new blueprint class by right clicking in the **Content Drawer** or **Content Browser** and selecting **Blueprint Class**.
2. Name your new blueprint class **FenceSpline**.
3. In the **Components** tab, add a utility **Spline** and a **PCG** component.
4. Save your blueprint class.

[![Create the FenceSpline Blueprint Class](https://dev.epicgames.com/community/api/documentation/image/537a507f-1b3d-4f0e-b66a-67268f8a2a75?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/537a507f-1b3d-4f0e-b66a-67268f8a2a75?resizing_type=fit)

## PCG Graph Asset

The **PCG Graph** is the foundation of the fence generator and contains the instructions that are used to generate the fence sections along the spline. Create a new PCG graph asset by following the steps below:

1. Right click in the **Content Drawer** or **Content Browser**, navigate to **PCG**, and select **PCG Graph**.

   [![Create a New PCG Graph](https://dev.epicgames.com/community/api/documentation/image/23a5fae1-c1a8-40bd-9a06-ec3c40432006?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/23a5fae1-c1a8-40bd-9a06-ec3c40432006?resizing_type=fit)
2. Name the new asset **PCG\_FenceGen** and press **Enter**.
3. Double-click **PCG\_FenceGen** to open the PCG Graph Editor.

## Create the PCG Grammar

The grammar is stored in a graph parameter as a string. Storing the value in a parameter makes it possible to use **Parameter Overrides** to customize each instance of the fence generator in the level. The **Grammar** attribute is then added to the spline data and passed to a **Subdivide Spline** node to assigned points along the spline.

1. In the **PCG Graph Editor** window, add a **Get Spline Data** node to the graph.
2. Open the **Graph Settings** by clicking the button at the top of the screen and create a new **Parameter**. Name the new parameter **Grammar** and change its type to **String**.

   [![Set Grammar to String](https://dev.epicgames.com/community/api/documentation/image/282b538b-f1b7-412f-b03e-189124760e07?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/282b538b-f1b7-412f-b03e-189124760e07?resizing_type=fit)
3. Set the initial value of **Grammar** to `A*`. This will tell the graph to place an initial static mesh and then fill the rest of the spline in with static meshes as long as there is room.
4. Drag from the output of **Get Spline Data** and create an **Add Attribute** node. In the Details panel, change the **Output Target** to `Grammar`.
5. Create a Get node for the **Grammar** parameter and connect it to the **Attributes** input on **Add Attribute**.

   [![Add the Add Attribute node](https://dev.epicgames.com/community/api/documentation/image/4b7a2cd3-e88a-4bf3-a2f7-fbce4deb0747?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4b7a2cd3-e88a-4bf3-a2f7-fbce4deb0747?resizing_type=fit)
6. Click the checkbox for **Accept Incomplete Subdivision**.
7. Click the checkbox for **Grammar as Attribute** and set **Grammar Attribute** to `Grammar`.

   [![Add Subdivide Spline node](https://dev.epicgames.com/community/api/documentation/image/459427c8-d025-4b3e-92d5-134821fec96c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/459427c8-d025-4b3e-92d5-134821fec96c?resizing_type=fit)

## Assign Meshes to the Grammar

Each symbol in the grammar needs to be assigned a static mesh to spawn. This is done by using two parameters: **Module Info** and **Mesh Info**. Module Info contains an array of symbols. Mesh Info contains an array of static meshes. This information is passed to the **Subdivide Spline** node later as an attribute set.

1. Select the **Subdivide Spline** node and click the checkbox for **Module Info as Input**. This adds an input for an attribute that can be used to assign module information to your grammar symbols.
2. Create a new parameter in the Graph Settings and name it Module Info. Change the type to **PCG Subdivision Submodule** and click the dropdown menu next to the type and select **Array**. This will hold our symbol information.

   [![Set Module Info to an Array](https://dev.epicgames.com/community/api/documentation/image/dd56350f-d2cd-498e-b139-8d50063833a0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dd56350f-d2cd-498e-b139-8d50063833a0?resizing_type=fit)
3. Click the **+** button to add a new array element and click the arrow next to **Index [0]** to open the entry.
4. Set the value of **Symbol** to `A` and click the checkbox next to the **Scalable** option.
5. Create a new parameter in the Graph Settings and name it **Mesh Info**. Change the type to **Static Mesh** and click the dropdown menu next to the type and select **Array**. This will hold our static mesh information.

   [![Create Mesh Info](https://dev.epicgames.com/community/api/documentation/image/ee378597-e592-4742-81d1-1c12418d0b48?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ee378597-e592-4742-81d1-1c12418d0b48?resizing_type=fit)
6. Click the **+** button to add a new array element to Mesh Info.
7. Open the dropdown menu next to **Index [0]** and select the **Fence\_17\_DE** static mesh.

## Create the Extract Info Subgraph

The subdivision process assigns each module a size and places a pivot point in the middle of the bounds. This creates a problem if the mesh changes later or does not have its pivot in the middle of the mesh. This subgraph extracts the size information directly from the selected mesh’s bounds and adjusts its pivot point to be at the center.

### Setup the Input Node

1. In the **Content Drawer** or **Content Browser**, create a new **PCG Graph** and name it **PCG\_ExtractInfo**.
2. Click on the **Input** node and open the **Pins** option in the Details panel. **Open Index [0]** and change the **Label** to `Mesh Info`.
3. Change the **Allowed Types** option to **Point or Param**.
4. Change the **Pin Status** option to **Normal**.
5. Set the **Tooltip** to `List of meshes to extract info from`.

   [![Input Node Settings](https://dev.epicgames.com/community/api/documentation/image/5eb6686c-e128-4d8e-977a-5494374ae096?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5eb6686c-e128-4d8e-977a-5494374ae096?resizing_type=fit)

### Extract the Mesh Bounds

1. Open the **Graph Settings** and create a new parameter. Name it **Mesh Attribute Name** and set the type to **Name**. Set the initial value to `Mesh`.
2. Drag from the output of the **Input** node and create an **Attribute Rename** node.
3. In the Details panel, set the **New Attribute Name** to `Mesh`.
4. Create a **Get Mesh Attribute Name** node and connect it to the **Attribute to Rename** input on the **Attribute Rename** node.
5. Drag from the **Attribute Rename** node and create a new **Bounds From Mesh** node.
6. Click the new node and set the Mesh Attribute value to `Mesh`.

   [![Add Attribute Rename node and settings](https://dev.epicgames.com/community/api/documentation/image/dc1deda7-dfcd-40e8-bfa7-780b0872b19a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dc1deda7-dfcd-40e8-bfa7-780b0872b19a?resizing_type=fit)
7. Drag from the output of **Attribute Rename** and connect it to the **Attribute** input on the **Bounds From Mesh** node. The graph will automatically create a filter to create the appropriate input.
8. Hold the **ALT** key and click the output of the new filter node to break its connection.
9. Drag off the disconnected filter node and create an **Attribute Set To Point** node. Connect the output of that node to the input on **Bounds From Mesh**. Doing this gives the graph the ability to support both point and attribute set data types.
10. Click the Bounds From Mesh node and set the value of the **Mesh Attribute** option to `Mesh`.

    [![Graph structure processes both point and attribute set data](https://dev.epicgames.com/community/api/documentation/image/b7eca422-397c-4bfa-9057-a4ea86575fc7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b7eca422-397c-4bfa-9057-a4ea86575fc7?resizing_type=fit)

### Adjust the Pivot Point

1. The pivot point on the static mesh needs to be adjusted to display correctly on the spline, drag from **Bounds From Mesh** and create a **Multiply** node.
2. Click on the new node and set the value of **Input Source 1** to `$Extents.X` This will extract the X extents from the bounds data.
3. Drag off from the **In B** input and create a **Create Attribute** node. Change the **Double Value** to `2.0`.
4. Click back on the **Multiply** node and change the **Output Target** value to `Size`. This will output the full X value multiplied by two and store it in an attribute called Size.

   [![Add Multiply node and settings](https://dev.epicgames.com/community/api/documentation/image/727c2a02-d0af-43b2-98c0-3a999124f5ae?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/727c2a02-d0af-43b2-98c0-3a999124f5ae?resizing_type=fit)
5. Drag off from the **Multiply** node and create a **Copy Attributes** node. Drag off the **Multiply** output again and connect it to the **Source** input on the new node. This node extracts the Z extents from the bounds data and saves it to an attribute to help with future scaling, if needed.
6. Click on **Copy Attributes** and set the **Input Source** to `$Extents.Z`.
7. Set the **Output Target** to `ExtentsZ`.

   [![The Copy Attributes node](https://dev.epicgames.com/community/api/documentation/image/0d16154e-87b0-4cb4-90ea-af86f837a70f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0d16154e-87b0-4cb4-90ea-af86f837a70f?resizing_type=fit)
8. Drag from the output on **Copy Attributes** and create another **Multiply** node. This node will help move the pivot of the mesh to the center.
9. Drag off from the **In B** input and create a **Create Attribute** node. Change the **Double Value** to `-1.0`.
10. Click back to the **Multiply** node. In the Details panel, set the value of **Input Source 1** to `$LocalCenter`.
11. Set the value of **Output Target** to `PivotOffset`.

    [![Add a second Multiply node](https://dev.epicgames.com/community/api/documentation/image/a82aca45-cad8-41cb-8a8b-7351c69249b4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a82aca45-cad8-41cb-8a8b-7351c69249b4?resizing_type=fit)

### Setup the Output Node

1. Click on the **Output** node and position it at the end of the graph.
2. Open the **Pins** option in the Details panel. **Open Index [0]** and change the **Allowed Types** to **Attribute Set**.
3. Change the **Pin Status** option to **Normal**.

   [![Output node settings](https://dev.epicgames.com/community/api/documentation/image/11d74792-3fa9-4e56-940d-3e3a13688122?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/11d74792-3fa9-4e56-940d-3e3a13688122?resizing_type=fit)
4. Drag from the output on the **Multiply** node and create a new **Point to Attribute** Set node.
5. Connect the output of the new node to the **Out** pin on the **Output** node.

   [![Convert the point data to an attribute set](https://dev.epicgames.com/community/api/documentation/image/106430f5-c14b-4b62-898c-467ff7a59ca4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/106430f5-c14b-4b62-898c-467ff7a59ca4?resizing_type=fit)
6. Save the completed graph.

   [![The complete subgraph](https://dev.epicgames.com/community/api/documentation/image/691d1bc3-4950-4a1e-a210-f9caafce5265?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/691d1bc3-4950-4a1e-a210-f9caafce5265?resizing_type=fit)
7. Return to the **PCG\_FenceGen** graph editor window. Drag and drop your **PCG\_ExtractInfo** graph asset from the **Content Drawer** or **Content Browser** into the viewport and select **Create PCG\_ExtractInfo Subgraph Node**.

   [![Create the Subgraph node](https://dev.epicgames.com/community/api/documentation/image/395aa462-de8b-442c-b519-35784aa4fa65?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/395aa462-de8b-442c-b519-35784aa4fa65?resizing_type=fit)

## Apply the Module and Mesh Information

1. Back in the **PCG\_FenceGen** graph, create an **Add Attribute** node and position it near the **Subdivide Spline** node.
2. Create a **Get Module Info** node and connect it to the **In** on **Add Attribute**.
3. Create a **Get Mesh Info** node and connect it to the **Attributes** input on **Add Attribute**.
4. Connect the **Out** from **Add Attribute** to the **Mesh Info** input on your **PCG\_ExtractInfo** subgraph node.
5. Connect the output from the subgraph node to the **Modules Info** input on the **Subdivide Spline** node.

   [![Connect the Module and Mesh data](https://dev.epicgames.com/community/api/documentation/image/cd32d788-9d8c-4fca-a9e8-ae7fe5b779cd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cd32d788-9d8c-4fca-a9e8-ae7fe5b779cd?resizing_type=fit)
6. Drag from the output of the **Subdivide Spline** node and create a **Match and Set Attributes** node. Connect the output of the subgraph node to its **Match Data** input. This node takes in the point data and grammar from the **Subdivide Spline** and matches it with the **Module Info** and **Mesh Info** from those parameters.
7. Click on the Match and Set Attributes node and set the following options:

   1. Click the checkbox next to **Match Attributes**.
   2. Set the value of the **Input Attribute** and the **Match Attribute** to `Symbol`.

   [![The Match And Set Attributes node](https://dev.epicgames.com/community/api/documentation/image/01075701-3c49-42ae-bc39-072879ecccde?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/01075701-3c49-42ae-bc39-072879ecccde?resizing_type=fit)

## Apply the Pivot Offset Transform

1. Drag from the output of **Match and Set Attribute** to create a **Multiply** node.This node scales the pivot of each mesh using data from the **PCG\_ExtractInfo** subgraph.
2. Drag from the output of **Match and Set Attribute** and connect it to the **In B** input on the **Multiply** node.
3. Click on the **Multiply** node. Set the **Input Source 1** value to `PivotOffset` and the **Input Source 2** value to `$Scale`.

   [![Scale the Pivot with the Multiply node](https://dev.epicgames.com/community/api/documentation/image/9801fdba-6a49-44d1-b3f3-ae6899188090?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9801fdba-6a49-44d1-b3f3-ae6899188090?resizing_type=fit)
4. Drag from the **Multiply** and create a **Vector: Transform Direction** node. This node will rotate the pivot to match the points on the spline.
5. Drag from the output of **Multiply** and connect it to the **Transform** input on the **Vector: Transform Direction** node.
6. Click on the new node and set the **Operation** to **Transform Direction**.
7. Set the **Input Source 1** value to `PivotOffset` and the **Input Source 2** value to `$Transform`.

   [![Rotate the pivot with Tranform Direction](https://dev.epicgames.com/community/api/documentation/image/70d8e423-c7dc-47d1-b3da-84293c3eb9a6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/70d8e423-c7dc-47d1-b3da-84293c3eb9a6?resizing_type=fit)
8. Drag from **Vector: Transform Direction** and create a new **Add** node. This node adds the final pivot offset to the position of the pivot on the mesh.
9. Drag from the output of **Vector: Transform Direction** and connect it to the **In B** input on the **Add** node.
10. Set the **Input Source 1** value to `$Position` and the **Input Source 2** value to `PivotOffset`.

    [![Apply the offset with the Add node](https://dev.epicgames.com/community/api/documentation/image/2219e7e3-dbe6-4d37-9a0b-e007d71899da?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2219e7e3-dbe6-4d37-9a0b-e007d71899da?resizing_type=fit)

## Spawn The Static Meshes

1. Drag from the output of the **Add** node and create a new **Static Mesh Spawner**. This node spawns the static meshes along the spline.
2. In the Details panel, set the **Mesh Selector Type** to **PCGMeshSelectorByAttribute**.
3. Set the **Attribute Name** value to `Mesh`.
4. Save the graph.

   [![Connect the Static Mesh Spawner](https://dev.epicgames.com/community/api/documentation/image/4884b886-8c37-4cde-9e90-749e97ae4143?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4884b886-8c37-4cde-9e90-749e97ae4143?resizing_type=fit)
5. Click the **FenceSpline** actor in the level. In the Details panel, select the **PCG** component and use the dropdown menu to set the **Graph** option to **PCG\_FenceGen**.

   [![Connect the PCG Graph to the PCG component](https://dev.epicgames.com/community/api/documentation/image/e79fc22f-e9d4-4305-bfc9-6b4d5b742e61?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e79fc22f-e9d4-4305-bfc9-6b4d5b742e61?resizing_type=fit)

## Result

You should see a line of fence static meshes spawning along the length of the spline.

[![The complete Fence Generator](https://dev.epicgames.com/community/api/documentation/image/35e36585-4fab-431d-bd10-28ffe238f7b0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/35e36585-4fab-431d-bd10-28ffe238f7b0?resizing_type=fit)

You can add additional variety to the static meshes by adding symbols to your grammar, defining them in your Modules Info, and assigning them static meshes in your Meshes Info. You can do this in the graph itself or on a per-instance basis using **Parameter Overrides**.

[![Parameter Overrides work on a per instance basis](https://dev.epicgames.com/community/api/documentation/image/0b05474c-e7ee-4474-9030-d321581df351?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0b05474c-e7ee-4474-9030-d321581df351?resizing_type=fit)

In the example below, the fence line has the following extra features:

* Posts using the symbol `P`.
* A gate using the symbol `G`.
* Large broken sections using the symbol `BL`.
* Small broken sections using the symbol `BS`.

The grammar has been updated to `{[A,P]:2,[BL,P]:1,[BS,P]:1}*,[G,P], {[A,P]:2,[BL,P]:1,[BS,P]:1}*`.

[![The updated grammar generates a more interesting result](https://dev.epicgames.com/community/api/documentation/image/930e7f45-d787-4de8-937e-048e466f01d5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/930e7f45-d787-4de8-937e-048e466f01d5?resizing_type=fit)

* [landscape](https://dev.epicgames.com/community/search?query=landscape)
* [building virtual worlds](https://dev.epicgames.com/community/search?query=building%20virtual%20worlds)
* [procedural generation](https://dev.epicgames.com/community/search?query=procedural%20generation)
* [grammar](https://dev.epicgames.com/community/search?query=grammar)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisites](/documentation/en-us/unreal-engine/creating-a-fence-generator-using-shape-grammar-in-unreal-engine?application_version=5.7#prerequisites)
* [Project Setup](/documentation/en-us/unreal-engine/creating-a-fence-generator-using-shape-grammar-in-unreal-engine?application_version=5.7#project-setup)
* [Create the Spline](/documentation/en-us/unreal-engine/creating-a-fence-generator-using-shape-grammar-in-unreal-engine?application_version=5.7#create-the-spline)
* [PCG Graph Asset](/documentation/en-us/unreal-engine/creating-a-fence-generator-using-shape-grammar-in-unreal-engine?application_version=5.7#pcg-graph-asset)
* [Create the PCG Grammar](/documentation/en-us/unreal-engine/creating-a-fence-generator-using-shape-grammar-in-unreal-engine?application_version=5.7#create-the-pcg-grammar)
* [Assign Meshes to the Grammar](/documentation/en-us/unreal-engine/creating-a-fence-generator-using-shape-grammar-in-unreal-engine?application_version=5.7#assign-meshes-to-the-grammar)
* [Create the Extract Info Subgraph](/documentation/en-us/unreal-engine/creating-a-fence-generator-using-shape-grammar-in-unreal-engine?application_version=5.7#create-the-extract-info-subgraph)
* [Setup the Input Node](/documentation/en-us/unreal-engine/creating-a-fence-generator-using-shape-grammar-in-unreal-engine?application_version=5.7#setup-the-input-node)
* [Extract the Mesh Bounds](/documentation/en-us/unreal-engine/creating-a-fence-generator-using-shape-grammar-in-unreal-engine?application_version=5.7#extract-the-mesh-bounds)
* [Adjust the Pivot Point](/documentation/en-us/unreal-engine/creating-a-fence-generator-using-shape-grammar-in-unreal-engine?application_version=5.7#adjust-the-pivot-point)
* [Setup the Output Node](/documentation/en-us/unreal-engine/creating-a-fence-generator-using-shape-grammar-in-unreal-engine?application_version=5.7#setup-the-output-node)
* [Apply the Module and Mesh Information](/documentation/en-us/unreal-engine/creating-a-fence-generator-using-shape-grammar-in-unreal-engine?application_version=5.7#apply-the-module-and-mesh-information)
* [Apply the Pivot Offset Transform](/documentation/en-us/unreal-engine/creating-a-fence-generator-using-shape-grammar-in-unreal-engine?application_version=5.7#apply-the-pivot-offset-transform)
* [Spawn The Static Meshes](/documentation/en-us/unreal-engine/creating-a-fence-generator-using-shape-grammar-in-unreal-engine?application_version=5.7#spawn-the-static-meshes)
* [Result](/documentation/en-us/unreal-engine/creating-a-fence-generator-using-shape-grammar-in-unreal-engine?application_version=5.7#result)
