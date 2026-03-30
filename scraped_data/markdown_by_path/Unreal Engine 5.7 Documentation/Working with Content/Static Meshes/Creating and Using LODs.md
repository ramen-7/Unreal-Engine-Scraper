<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-and-using-lods-in-unreal-engine?application_version=5.7 -->

# Creating and Using LODs

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
7. Creating and Using LODs

# Creating and Using LODs

How To Create and Use LODs.

![Creating and Using LODs](https://dev.epicgames.com/community/api/documentation/image/d7369e65-e6df-464b-b9de-acd8f9bc6669?resizing_type=fill&width=1920&height=335)

 On this page

When a player is up close to a Static Mesh you have placed in your level, you want the mesh to look very detailed. However, you do not need that mesh to be very detailed and complex once the player moves far away from the mesh. There is no point in having a very complex and detailed mesh if it is only taking up a few pixels on the screen and the player can barely see it. However, the mesh needs to be detailed when the player is up close to the mesh and can see it clearly. In UE5, you can place a mesh in your level that switches to a less complex mesh as the player moves away from it in order to make your level perform better. You can do this through the use of **Level of Details**, or **LODs**. This How-to will show you how you can import a less detailed version of a mesh into UE5 and have your mesh seamlessly swap from one mesh to the other as the player moves closer or farther away.

## Set Up

This How-to does require that you already have some sort of mesh saved as a .FBX that you can import into UE5. For this example, we will be using a simple crate made in Maya. Note, you may also use an asset of your own that you have created in another application.

Once you have exported your mesh, launch UE5. If you have a project that you would like to work with, feel free to use it for this How-to. Otherwise, create a new project with the **Blueprint First Person** template making sure that **Starter Content** is enabled. If it is not, you may not have some of the assets that we will be using later and it may become hard to follow along.

For detailed instructions on creating a new Project, see the [Create a New Project](/documentation/en-us/unreal-engine/creating-a-new-project-in-unreal-engine) page.

After you have done that, give your project a name and location, and click the **Create Project** button.

## Creating a LOD

Once your project has loaded, navigate to the **Meshes** folder inside the **Content Browser** and find the asset named **SM\_Cube**.

[![Cube In Content Browser](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2cf90ecd-4ad3-4847-9213-93b4d5c7520e/01-cube-in-content-browser.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2cf90ecd-4ad3-4847-9213-93b4d5c7520e/01-cube-in-content-browser.png)

Click image for full size.

Once you have found that asset, open it inside the Static Mesh Editor by either **double-clicking** or by **right-clicking** and selecting **Edit** from the context menu that appears. Now you should have something that looks similar to what is shown below.

[![Cube In Static Mesh Editor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d8d6a4fb-0fdf-4611-b6cf-7cae1a353fdc/02-cube-in-static-mesh-editor.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d8d6a4fb-0fdf-4611-b6cf-7cae1a353fdc/02-cube-in-static-mesh-editor.png)

Click image for full size.

Once you have the asset open in the Static Mesh Editor, locate the **Details** panel. It is in the upper right corner by default. Once you find it, it should look like what is shown below:

[![Details LOD0](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1209e403-6a52-4572-bc73-9d480be2cac6/03-details-lod-0.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1209e403-6a52-4572-bc73-9d480be2cac6/03-details-lod-0.png)

Click image for full size.

The top section is labeled LOD0. LOD is a zero-based system, so LOD0 will be the first entry, LOD1 would be the second, and so on. LOD0 is the base LOD of the mesh and will be the only one that is used if the mesh only has 1 LOD, which this mesh does right now. Next, we are going to change that.

The section directly under that one is named LOD Settings. In this section, there are a few options we are going to go over. The first one is Number of LODs. It is at 1 by default and will increase as you import LODs. This value also can be editable if auto mesh reduction is available. However, in order to use this feature you must first obtain a license from [Simplygon.](https://www.simplygon.com/)

The next option we will go over is **LOD Import**. This option will give you a drop down menu similar to this:

[![Import LOD Level 1](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/89a4d50e-ad4d-4166-bd87-9c1c5ad663d0/04-import-lod-level-1.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/89a4d50e-ad4d-4166-bd87-9c1c5ad663d0/04-import-lod-level-1.png)

Click image for full size.

Select **Import LOD Level 1**. This should open up a window that allows you to browse to the .FBX file mentioned earlier in this How-to. Browsing to and selecting the **.FBX** file will import that mesh LOD1, or the second LOD. Once you have done this, you will see a pop-up notification at the bottom right of your screen that should look similar to this:

[![Successful Import](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e26f14fe-3941-41f9-a2eb-e62d3e7c233b/05-successful-import.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e26f14fe-3941-41f9-a2eb-e62d3e7c233b/05-successful-import.png)

Click image for full size.

In this example we are only importing 1 LOD which will give us a total of 2, but you can import more if you wish. To do so, simply click on the drop down menu for **LOD Import** and select **Import LOD Level X** where X equals whichever LOD was the next one that you wanted to import. You could also reimport any LOD you had already imported. If you wanted to import another mesh for LOD1 instead of the one you already had imported, just click on the drop down menu for **LOD Import** and select **Reimport LOD Level 1**. If you clicked on the drop down menu now, your options would look like this:

[![Import LOD Level 2](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6cc40024-b54f-4d6b-aab0-d666c00148e3/06-import-lod-level-2.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6cc40024-b54f-4d6b-aab0-d666c00148e3/06-import-lod-level-2.png)

Click image for full size.

Now that the mesh for LOD1 has been imported, we are going adjust a few of the values to demonstrate the power of LODs. The first option inside the **LOD Settings** section of the Details panel we are going to look at is **Auto Compute LOD Distances**. What this does is tell when to switch from one LOD to another by equally dividing the percent of screen size by the amount of LODs. For example, in this case, we have two LODs, so when the mesh takes up 50 percent or more of the screen, LOD0 will appear. When the mesh takes up less than 50 percent of the screen, LOD1 will appear. If there are three LODs, than LOD0 will appear when the mesh takes up 66.7 percent of the screen or more, LOD1 will appear between that value and 33.3 percent, and LOD2 will appear if the mesh takes up less than 33.3 percent of the screen. This may not be very helpful in this case however as the mesh we are using will more often than not take up less than 50 percent of the screen. We can manually change these values, however, by unchecking **Auto Compute LOD Distances** and manually adjust the **Screen Size** value for the individual LODs

[![Auto Compute LOD Distances](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cc8bece3-b2a1-4558-836b-ff2f0528e3de/07-auto-compute-lod-dist.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cc8bece3-b2a1-4558-836b-ff2f0528e3de/07-auto-compute-lod-dist.png)

Click image for full size.

For the purposes of this demonstration, we are going to uncheck **Auto Compute LOD Distances**. Once you have done that, find the **Screen Size** value under **LOD1** and change it to **0.01**. This means that when the cube mesh that we have in our level takes up less than 1 percent of the screen size, our cube will switch to the mesh you imported as LOD1 (in this example, a crate.) We can also change the material for each LOD, as well. Just to further demonstrate the power and usefulness of LODs, we will change the material of LOD1 to **M\_Metal\_Gold**.

[![Change Material 1](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/99abbf36-ef6d-427d-9714-7780e5e6f76a/08-change-material-1.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/99abbf36-ef6d-427d-9714-7780e5e6f76a/08-change-material-1.png)

Click image for full size.

## Collision

You can set the **Static Mesh** to use **Complex Collision** (per triangle) from any **LOD** you have imported. This is useful for optimising physics performance, especially if you have lots of Complex Collisions against **Static Meshes** or **Complex Collision Traces**. However, there is no switch at run time between **Complex Collision** when the LOD's change, the chosen LOD will be used for all Complex Collision against the mesh.

See [Setting Up Collisions With Static Meshes](/documentation/en-us/unreal-engine/setting-up-collisions-with-static-meshes-in-unreal-engine) for information on setting this up.

## LODs in Use

After you have done this, save your mesh and go back to the **Level Editor**. You will see that whenever you are closer to the mesh, it is the cube. As you back away from the mesh, it becomes the crate you imported. Also note that it is not calculated by distance, but by screen size, so if you place a larger instance of the mesh beside a smaller instance of the mesh and start moving an equal distance away from both of them, the smaller instance will switch to the next LOD before the larger instance does. Take a look at the example below.

|  |  |
| --- | --- |
| LOD Example Far | LOD Example Near |
| LOD Far | LOD Near |

Note that as we moved farther away, only the cube in the foreground took up more than 1 percent of the screen, so it was still at LOD0, or the cube. However, the meshes in the back became smaller as we moved away and thus took less than 1 percent, and switched to LOD1 (or the golden crates in this example.) Also note that LODs scale with screen size so if you detach the Viewport and resize it, the percentage of what the mesh covers will scale with the size of the Viewport and, thus, change LODs accordingly.

Obviously changing a cube to a crate is not the most practical use of LODs, but this example illustrates how LODs function. Now you are ready to apply LODs to the meshes in your level so that they look good up close but are optimized for performance when further away.

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [static meshes](https://dev.epicgames.com/community/search?query=static%20meshes)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Set Up](/documentation/en-us/unreal-engine/creating-and-using-lods-in-unreal-engine?application_version=5.7#setup)
* [Creating a LOD](/documentation/en-us/unreal-engine/creating-and-using-lods-in-unreal-engine?application_version=5.7#creatingalod)
* [Collision](/documentation/en-us/unreal-engine/creating-and-using-lods-in-unreal-engine?application_version=5.7#collision)
* [LODs in Use](/documentation/en-us/unreal-engine/creating-and-using-lods-in-unreal-engine?application_version=5.7#lodsinuse)
