<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-materials-with-static-meshes-in-unreal-engine?application_version=5.7 -->

# Setting Up Materials With Static Meshes

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
6. [Static Meshes](/documentation/en-us/unreal-engine/static-meshes "Static Meshes")
7. Setting Up Materials With Static Meshes

# Setting Up Materials With Static Meshes

How to set a material on a mesh in the Static Mesh Editor.

![Setting Up Materials With Static Meshes](https://dev.epicgames.com/community/api/documentation/image/2f24a39e-e14c-4b66-8716-91491a7bc90f?resizing_type=fill&width=1920&height=335)

 On this page

No matter what type of **Static Mesh** you put into your **Level**, chances are when the player looks at that object, you want it to have a **Material**. In this guide, you will learn a couple of ways to apply a Material to your Static Mesh.

## Setup

If you already have a project you are working on, you can use that project to follow along. If you do not, start by launching **Unreal Engine** and creating a new project with **Starter Content** enabled. For more information on creating new projects in Unreal Engine, refer to [Creating a New Project.](/documentation/en-us/unreal-engine/creating-a-new-project-in-unreal-engine)

This guide uses the First Person game template, but the template you use does not matter for this tutorial. The important thing is to make sure **Starter Content** is enabled if you are creating a new project. If you do not, you won't have the assets referenced later in this guide, which might make it difficult to follow along.

[![New Project With Starter Content](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f68bb728-eb54-4e21-92a5-dd1c584f8713/01-new-project-with-starter-content.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f68bb728-eb54-4e21-92a5-dd1c584f8713/01-new-project-with-starter-content.png)

Click image for full size.

Once your project is loaded, open your **Content Browser** and open the folder labeled **Starter Content**, as shown below.

[![Content Browser With Starter Content](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8df9b572-04c0-41cb-9472-0c1e0d6c465b/01-content-browser-with-starter-content.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8df9b572-04c0-41cb-9472-0c1e0d6c465b/01-content-browser-with-starter-content.png)

Click image for full size.

Inside of the **Starter Content** folder, there is a folder labeled **Props**. Open that folder and find the **Static Mesh** labeled **SM\_Chair**.

**SM** in **SM\_Chair** stands for Static Mesh and follows the standard naming convention recommended by Unreal Engine. Following a consistent naming convention helps maintain an organized project. To learn more about naming files in Unreal Engine, refer to [Recommended Asset Naming Conventions](/documentation/en-us/unreal-engine/recommended-asset-naming-conventions-in-unreal-engine-projects).

[![Chair In Content Browser](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/eacfcf4b-0748-4fca-a859-70e06fc4b54e/02-chair-in-content-browser.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/eacfcf4b-0748-4fca-a859-70e06fc4b54e/02-chair-in-content-browser.png)

Click image for full size.

Click and drag **SM\_Chair** into the **Level Viewport**. A copy of the Static Mesh now appears in your Level. To learn other methods of adding a Static Mesh to your Level, refer to [Placing Actors](/documentation/en-us/unreal-engine/placing-actors-in-unreal-engine).

[![Chair In Level](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bd018576-c935-4a01-9946-a6f836d45d89/dragging-static-mesh-in-level.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bd018576-c935-4a01-9946-a6f836d45d89/dragging-static-mesh-in-level.png)

Click image for full size.

## Applying a Material via the Details Panel

A quick way to switch the Material of one instance of a Static Mesh is by highlighting that particular instance and changing the Material in the **Details** panel. The following section goes over how you can do that.

When placing a Static Mesh into your Level an instance of the mesh is created. Any Material assigned to the instance will not affect the Static Mesh itself.

Highlight your Static Mesh by clicking it in the Viewport or searching for **SM\_Chair** in the **Outliner**.

With the Static Mesh selected, go to the **Details** panel. There will be a **Materials** section with a thumbnail and a dropdown menu with the current Material name.

[![Materials](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cfb72046-5e93-45fa-8c82-332fcac49f3d/materials-in-details-panel.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cfb72046-5e93-45fa-8c82-332fcac49f3d/materials-in-details-panel.png)

Click image for full size.

Selecting another Material from the dropdown menu changes the Material applied to that instance of the Static Mesh. The change is reflected in your Viewport, as demonstrated below:

|  |  |
| --- | --- |
| Normal Chair With Details | Brick Chair With Details |
| Normal Chair with Details | Brick Chair with Details |

## Applying a Material via the Static Mesh Editor

Now you can change the Material of one instance of a Static Mesh in your Level, but what if you want to change the default Material of the Static Mesh itself? Well, you can do that from within the **Static Mesh Editor**.

Go back to **SM\_Chair** within the **Props** folder in your **Content Browser**. Once you have it selected, you can access the Static Mesh Editor in two ways:

* **Double-click** the mesh inside the **Content Browser**.
* **Right-click** on the mesh and select **Edit** from the context menu.

[![Right Click Menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/52c84f24-a3ed-4f62-9b9b-8586d2db399d/05-right-click-menu.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/52c84f24-a3ed-4f62-9b9b-8586d2db399d/05-right-click-menu.png)

Click image for full size.

After **double-clicking** the asset inside the **Content Browser** or selecting **Edit** from the **right-click** context menu, the Static Mesh Editor will open, as shown below.

[![Static Mesh Editor Material](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/012f275f-c053-4284-a6e4-9ce0177ca926/06-static-mesh-editor-material.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/012f275f-c053-4284-a6e4-9ce0177ca926/06-static-mesh-editor-material.png)

Click image for full size.

In the **Details** panel, on the right-hand side of the Static Mesh Editor, find the **Material Slots** section. There you can see a thumbnail of the Material used on the Static Mesh and a dropdown menu beside it with the name of the Material. To learn more about the layout of the Static Mesh Editor, refer to [Static Mesh Editor UI](/documentation/en-us/unreal-engine/static-mesh-editor-ui-in-unreal-engine).

[![Material In Editor Changed](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/887ac207-bfe2-47be-87d6-b9a50ab7588a/07-material-in-editor-changed.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/887ac207-bfe2-47be-87d6-b9a50ab7588a/07-material-in-editor-changed.png)

Click image for full size.

**Click** on the dropdown menu and select another Material.

You have now applied a new Material to the Static Mesh, as shown below.

[![Concrete Chair In Editor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8f29e70f-8ee1-412a-8286-24f960a23fe6/08-concrete-chair-in-editor.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8f29e70f-8ee1-412a-8286-24f960a23fe6/08-concrete-chair-in-editor.png)

Click image for full size.

Next, click **Save** in the Toolbar at the top of the Static Mesh Editor. The applied Material is now the default Material of the Static Mesh and any instance of the mesh placed in the Level.

[![Concrete Chair In Level](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1f48c25c-84fe-46b2-9374-3d4dc02c9ed3/09-concrete-chair-in-level.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1f48c25c-84fe-46b2-9374-3d4dc02c9ed3/09-concrete-chair-in-level.png)

Click image for full size.

To continue learning about Materials, refer to [Materials](/documentation/en-us/unreal-engine/unreal-engine-materials) documentation.

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [static meshes](https://dev.epicgames.com/community/search?query=static%20meshes)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Setup](/documentation/en-us/unreal-engine/using-materials-with-static-meshes-in-unreal-engine?application_version=5.7#setup)
* [Applying a Material via the Details Panel](/documentation/en-us/unreal-engine/using-materials-with-static-meshes-in-unreal-engine?application_version=5.7#applyingamaterialviathedetailspanel)
* [Applying a Material via the Static Mesh Editor](/documentation/en-us/unreal-engine/using-materials-with-static-meshes-in-unreal-engine?application_version=5.7#applyingamaterialviathestaticmesheditor)
