<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/usd-stage-editor-quick-start-in-unreal-engine?application_version=5.7 -->

# USD Stage Editor Quick Start

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
6. [Universal Scene Description (USD)](/documentation/en-us/unreal-engine/universal-scene-description-usd-in-unreal-engine "Universal Scene Description (USD)")
7. USD Stage Editor Quick Start

# USD Stage Editor Quick Start

A tutorial on using the USD Stage workflow with your USD data.

![USD Stage Editor Quick Start](https://dev.epicgames.com/community/api/documentation/image/e71331aa-888b-4c7b-af21-40d64d8d2835?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

Unreal Engine provides support for USD through the USD Stage Actor and the USD Stage workflow. In this Quick Start guide, you will:

* Creating the USD Stage Actor.
* Editing properties using the USD Stage Window.
* Adding new Prims to your USD Stage Actor.
* Writing data back to your USD file.
* Accessing USD animations using Sequencer.
* Importing assets into an Unreal Engine project.

Before you begin, you will need the **USD Importer** plugin enabled in your project. For more information, see [Working with Plugins](/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine).

### Prerequisite Topics

In order to understand and use the content on this page, make sure you are familiar with the following topic:

* [Universal Scene Description in Unreal Engine](/documentation/en-us/unreal-engine/universal-scene-description-in-unreal-engine)

This tutorial uses the Kitchen Set USD file from Pixar. Pixar maintains a small library of USD sample files for learning and demonstration. Download the Kitchen Set and other samples [here](https://graphics.pixar.com/usd/release/dl_downloads.html).

## 1. Creating the USD Stage Actor

Start working with USD content by opening the USD Stage panel.

[![The USD Stage panel.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3bb801f2-67d8-47fc-8907-4270cd3e3455/5-0-010-usd-stage-panel.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3bb801f2-67d8-47fc-8907-4270cd3e3455/5-0-010-usd-stage-panel.png)

Click image for full size.

1. In the Level Editor, from the Top Menu, select **Window > Virtual Production > USD Stage**.
2. From the menu in the **USD Stage Editor** panel, select **File > Open** and navigate to your USD file.

The Hierarchy section will populate with the scene hierarchy from your USD file.

[![The USD Stage Hierarchy section](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2ed0040d-4f0a-4b6d-b644-be0a8904bbd2/5-0-020-usd-hierarchy.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2ed0040d-4f0a-4b6d-b644-be0a8904bbd2/5-0-020-usd-hierarchy.png)

The Hierarchy section of the USD Stage window populated with the contents of the Kitchen Set.
Click image for full size.

Each USD file you open in Unreal Engine requires its own **USD Stage** Actor that serves as an anchor for your USD data. The process outlined above will automatically add a USD Stage Actor to your Level.

It is also possible to add a USD Stage Actor using the **Place Actors** panel and select an associated USD file for it using the **Root Layer** option in the **Details** panel.

## 2. Editing Properties Using the USD Stage Window

You can edit the properties of your USD Stage Actor and prims using the Properties section of the USD Stage Editor window.

### Changing the UpAxis of the USD Stage Actor

1. Select **Stage** at the top of the hierarchy in the USD Stage window. In the Properties section, locate the **upAxis** property and click the dropdown menu. Select the new axis to represent up for your USD data.

   [![Select the axis the best fits your USD data](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/13fadc02-eab7-4cff-9360-43d69a02eea9/5-0-030-change-usd-property.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/13fadc02-eab7-4cff-9360-43d69a02eea9/5-0-030-change-usd-property.png)

   Select the axis the best fits your USD data.
   Click image for full size.

### Changing the Variant of a Prim

1. In the USD Stage Editor, select **Options > Selection** and enable **Synchronize with Editor**. This synchronizes your selection between the Unreal Engine Level and the USD Stage Editor window.

   [![USD Synchronize with Editor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4546188c-07c3-4bc7-b9f5-2acd2c7e9703/5-0-040-synchronize-with-editor.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4546188c-07c3-4bc7-b9f5-2acd2c7e9703/5-0-040-synchronize-with-editor.png)

   Enable Synchronize with Editor to synchronize your selection between the USD Stage and the Unreal Engine viewport.
   Click image for full size.
2. In the Hierarchy section, click the dropdown arrow next to **Kitchen\_Set** to expand the group. Expand **Props\_grp** to display the props in the scene.
3. Expand **West\_grp** to display individual prims. Props highlighted in orange indicate that they are **composition arcs**, and you can right-click any of their prims to add references to them (or clear references from them). Other right-click actions include the ability to add or remove prims, and the ability to toggle, load, or unload payloads.

   [![Prim Contextual Menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6834d098-adf6-4fd2-b59e-909e5cb837f6/5-0-050-prim-contextual-menu.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6834d098-adf6-4fd2-b59e-909e5cb837f6/5-0-050-prim-contextual-menu.png)

   Click image for full size.
4. Expand **DiningTable\_grp** and select **ChairB\_1**. In the Properties section you can edit the following:

   | Property | Description |
   | --- | --- |
   | **name** | Displays the name of the selected asset. |
   | **path** | Displays the path of the selected asset. |
   | **kind** | Defines the type of the selected asset.  * **assembly**: Collection of models. * **component**: Type of model that contains subcomponents. * **group**: Collection of models within an assembly. * **model**: Base type of kind. Assets should not have their kind set to model since it is an abstract commonality used to differentiate components and groups. For more information, see [Model Hierarchy](https://graphics.pixar.com/usd/release/glossary.html#usdglossary-model) in the Pixar USD documentation. * **subcomponent**: Prims inside a component. Not a type of model. |
   | **purpose** | Sets the initial Purpose to load. Uses a USD Stage Actor and an integer as input.  Options include:  * default * proxy * render * guide |
   | **visibility** | Sets the initial Purpose to load. Uses a USD Stage Actor and an integer as input.  Options include:  * **inherited**: Inherits visibility from its parent * **invisibile**: Prim and any prims included in its subtree are not rendered. |
   | **xformOp:rotateZ** | Defines the Z rotation of the selected asset. |
   | **xformOp:translate** | Defines the X, Y, and Z location of the asset. |
   | **xformOpOrder** | Displays the order in which transform operations are applied to the asset. |
   | **modelingVariant** | Defines the current variant being displayed in the scene. It will only be visible if the asset has one or more variants. |
   | **References** | Displays all references attached to this prim. |
5. The chairs in this scene have two variants, **ChairA** and **ChairB**. With **ChairB\_1** selected, locate the **Variants** section of the Properties. Change **modelingVariant** to **ChairA**. This will swap the chair mesh used in the scene with the new variant.

## 3. Adding New Prims to Your USD Stage Actor

Prims are added or removed from the hierarchy using the right-click menu. Once added, their properties can be edited in the Properties section.

### Adding a new chair to the Kitchen Set

1. Right-click the **DiningTable\_grp** entry in the hierarchy and select **Add Prim** from the menu. Name this new prim **ChairB\_3**.

   [![Adding a new prim to the USD Stage](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/eae4e626-9c31-4db6-ab96-f3378f4df948/5-0-060-add-prim.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/eae4e626-9c31-4db6-ab96-f3378f4df948/5-0-060-add-prim.png)

   Adding a new prim to the USD Stage.
   Click image for full size.
2. Select your new prim in the hierarchy. In the **Details** section, change its **kind** to **component**.

   [![Changing the properties of the new prim](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b730f8f4-c2d7-4c38-932f-6adb42802e3a/5-0-070-kind-component.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b730f8f4-c2d7-4c38-932f-6adb42802e3a/5-0-070-kind-component.png)

   Changing the properties of the new prim.
   Click image for full size.
3. Reference the chair USD file to bring it into the stage. Right-click **ChairB\_3** in the hierarchy and select **Add Reference**. Navigate to the location of your Kitchen Set files. Open the **assets > Chair** folder and select **Chair.usd**. Click **Open**.
4. Your new prim now references the Chair USD data and displays the **ChairA** variant. It should be located at the Level's origin. Select **ChairB\_3** in the hierarchy and change the modelingVariant to **ChairB**.
5. Click the new chair in the viewport and use the transform tools to place the chair near the table.

## 4. Writing Data Back to Your USD File

Changes made using the USD Stage Actor can be written back to your USD file. From the USD Stage panel, select **File > Save**.

## 5. Accessing USD Animations Using Sequencer

### Accessing USD Animations

Animations stored within a USD file are accessible from a specifically-generated Level Sequence spawned by the USD Stage Actor.

1. In the **Outliner**, select **UsdStageActor**. In the **USD** section of the **Details** panel, locate the **Level Sequence**. Double-click the asset to open it in **Sequencer**.

   [![Open the Level Sequence](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/317ec762-8bf7-4696-ab84-f0cf1fe29631/5-0-080-usd-stage-actor-in-outliner.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/317ec762-8bf7-4696-ab84-f0cf1fe29631/5-0-080-usd-stage-actor-in-outliner.png)

   Double click the Level Sequence in the Details panel.
   Click image for full size.

For more information on using Sequencer, see [Cinematics and Sequencer](/documentation/en-us/unreal-engine/cinematics-and-movie-making-in-unreal-engine).

### Animating the Chair

To add animation to the new prim **ChairB\_3** that you created in step three, you will create a new USD file and add it as a layer to the USD Stage Actor.

1. In the **Layers** section of the USD Stage window, right-click the **kitchen\_set.usd** layer and select **Add New**. Save this new file as **myanim.usda**.

   [![Add a new Layer to your USD data for the animation](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/48af3bdd-25a4-4b0f-90f9-b9f71438a0b0/5-0-090-add-new-usd-layer.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/48af3bdd-25a4-4b0f-90f9-b9f71438a0b0/5-0-090-add-new-usd-layer.png)

   Add a new Layer to your USD data for the animation.
   Click image for full size.
2. USD layers use a [LIVRPS structure](https://graphics.pixar.com/usd/release/glossary.html#usdglossary-livrpsstrengthordering) to determine how layers affect the final composition of the scene. For animation to affect the kitchen set, the layer containing that animation must be higher in the layer structure than the scene containing the prims. From the Top Menu in the Level Editor, select **Window > Place Actors** to open the panel. Search for **Usd Stage Actor** in the **Place Actors** panel and drag a new copy into your Level.

   [![New USD Actors in the Place Actors panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ca631234-a98e-424a-9b3e-e5ae628e0f44/5-0-100-place-usd-stage-actor.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ca631234-a98e-424a-9b3e-e5ae628e0f44/5-0-100-place-usd-stage-actor.png)

   New USD Actors in the Place Actors panel.
   Click image for full size.
3. Select the **UsdStageActor** in the **Outliner**. From the USD Stage panel, select **File > Open** and browse to your **myanim.usda** file.
4. Add the kitchen set back into the layer stack by right-clicking the **myanim.usda** layer and selecting the **Add Existing** option. In the File window, navigate to your **kitchen\_set.usd** file and click **Open**.
5. Before adding the animation, the USD Stage needs to know how long the animation will be. Click the **Stage** prim in the hierarchy. In the Properties section, change the **endTimeCode** and **endFrame** values to **48**.

   [![Change the endTimeCode and endFrame properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ca66b252-d91f-483d-81b6-8e25c05672d0/5-0-110-set-end-frame-and-timecode.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ca66b252-d91f-483d-81b6-8e25c05672d0/5-0-110-set-end-frame-and-timecode.png)

   Change the endTimeCode and endFrame properties.
   Click image for full size.
6. Select your new USD Stage Actor in the **Outliner**. From the **Details** panel, scroll down to the USD section and locate **Level Sequence**. Double-click the asset to open it in **Sequencer**.
7. In the Sequencer panel, click the **+ Track** button and select the Actor you want to animate from the **Actor to Sequencer** submenu.

   [![Add a new Track group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2eb5ac77-ee3d-44cf-bd5a-6d5941d21455/5-0-120-actor-to-sequencer.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2eb5ac77-ee3d-44cf-bd5a-6d5941d21455/5-0-120-actor-to-sequencer.png)

   Add a new Track group for the selected Actor.
   Click image for full size.
8. Click the **Add (+)** button on the new track and create a new **Transform** track.

   [![Add a new Transform track](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cdaac33f-6dbe-4125-86f2-030139260aa1/5-0-130-add-transform-track.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cdaac33f-6dbe-4125-86f2-030139260aa1/5-0-130-add-transform-track.png)

   Add a new Transform track.
   Click image for full size.
9. Animate the chair rotating in place. For more information on using Tracks in Sequencer, see [Tracks](/documentation/en-us/unreal-engine/sequencer-track-list-in-unreal-engine).
10. Write the data back to USD using **File > Save** in the USD Stage window.

## 6. Importing Assets into an Unreal Engine Project

Actors displayed on the USD Stage Actor can be imported into the Unreal Editor's Content Browser through any of the following import options.

* Using **File > Import Into Level**. This process will import both assets (static mesh, skeletal mesh, materials, textures, and so on) and Actors.
* Using the **Add/Import** button in the **Content Browser**. This process will only import assets.
* Dragging and dropping the file into the **Content Browser**. This process will only import assets.
* Using the **Action > Import** option in the USD Stage Editor window. This process will import everything on the USD Stage Actor and works with both assets and Actors. After the import process is complete, assets on the USD Stage are replaced with new Actors from the **Content Browser**.

### Importing the Kitchen Set into Unreal Engine

1. With the Kitchen Set open in the USD Stage window, open the **Actions** menu and select **Import**.
2. Select the location to store the imported assets. In this example, importing the Kitchen Set will create a folder named **Kitchen\_set** in the selected location. Materials and static meshes are saved into separate subfolders.

* [beta](https://dev.epicgames.com/community/search?query=beta)
* [usd](https://dev.epicgames.com/community/search?query=usd)
* [universal scene description](https://dev.epicgames.com/community/search?query=universal%20scene%20description)
* [import/export](https://dev.epicgames.com/community/search?query=import%2Fexport)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisite Topics](/documentation/en-us/unreal-engine/usd-stage-editor-quick-start-in-unreal-engine?application_version=5.7#prerequisitetopics)
* [1. Creating the USD Stage Actor](/documentation/en-us/unreal-engine/usd-stage-editor-quick-start-in-unreal-engine?application_version=5.7#1creatingtheusdstageactor)
* [2. Editing Properties Using the USD Stage Window](/documentation/en-us/unreal-engine/usd-stage-editor-quick-start-in-unreal-engine?application_version=5.7#2editingpropertiesusingtheusdstagewindow)
* [Changing the UpAxis of the USD Stage Actor](/documentation/en-us/unreal-engine/usd-stage-editor-quick-start-in-unreal-engine?application_version=5.7#changingtheupaxisoftheusdstageactor)
* [Changing the Variant of a Prim](/documentation/en-us/unreal-engine/usd-stage-editor-quick-start-in-unreal-engine?application_version=5.7#changingthevariantofaprim)
* [3. Adding New Prims to Your USD Stage Actor](/documentation/en-us/unreal-engine/usd-stage-editor-quick-start-in-unreal-engine?application_version=5.7#3addingnewprimstoyourusdstageactor)
* [Adding a new chair to the Kitchen Set](/documentation/en-us/unreal-engine/usd-stage-editor-quick-start-in-unreal-engine?application_version=5.7#addinganewchairtothekitchenset)
* [4. Writing Data Back to Your USD File](/documentation/en-us/unreal-engine/usd-stage-editor-quick-start-in-unreal-engine?application_version=5.7#4writingdatabacktoyourusdfile)
* [5. Accessing USD Animations Using Sequencer](/documentation/en-us/unreal-engine/usd-stage-editor-quick-start-in-unreal-engine?application_version=5.7#5accessingusdanimationsusingsequencer)
* [Accessing USD Animations](/documentation/en-us/unreal-engine/usd-stage-editor-quick-start-in-unreal-engine?application_version=5.7#accessingusdanimations)
* [Animating the Chair](/documentation/en-us/unreal-engine/usd-stage-editor-quick-start-in-unreal-engine?application_version=5.7#animatingthechair)
* [6. Importing Assets into an Unreal Engine Project](/documentation/en-us/unreal-engine/usd-stage-editor-quick-start-in-unreal-engine?application_version=5.7#6importingassetsintoanunrealengineproject)
* [Importing the Kitchen Set into Unreal Engine](/documentation/en-us/unreal-engine/usd-stage-editor-quick-start-in-unreal-engine?application_version=5.7#importingthekitchensetintounrealengine)

Related documents

[Universal Scene Description in Unreal Engine

![Universal Scene Description in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/bff646fc-34ae-4f94-b81a-a32ae898ee59?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/universal-scene-description-in-unreal-engine)
