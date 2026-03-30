<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/static-mesh-automatic-lod-generation-in-unreal-engine?application_version=5.7 -->

# Static Mesh Automatic LOD Generation

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
7. Static Mesh Automatic LOD Generation

# Static Mesh Automatic LOD Generation

How To use the Automatic LOD Generation system in UE5.

![Static Mesh Automatic LOD Generation](https://dev.epicgames.com/community/api/documentation/image/e73d187a-340a-4d13-96ce-b6134a2b2bae?resizing_type=fill&width=1920&height=335)

 On this page

The Automatic LOD generation system allows you to automatically reduce the polygon count of your Static Meshes to create LODs with the Unreal Engine 5 (UE5) Editor. Automatic LOD generation uses what is called quadratic mesh simplification to help generate the LODs for Static Meshes. Quadratic mesh simplification works by calculating the amount of visual difference that collapsing an edge (by merging two vertices) would generate. It then picks the edge with the least amount of visual impact and collapses it. When this happens, the tool will pick the best place to put the newly merged vertex, removing any triangles that have also collapsed along with the edge. It will continue to collapse edges until it reaches the requested target number of triangles. In the following guide, we'll show you how-to setup and use the automatic LOD generation system in your UE5 projects.

## Setup

In the following section, we will create a new project that has Starter Content, and then open up a Static Mesh asset to work with.

For this part of the how-to guide, we will use the **SM\_Rock** Static Mesh that comes with the Starter Content. However, feel free to use any Static Mesh of your choosing to follow along.

1. If you have not done so already, open, or create a new UE5 project, making sure that the **With Starter Content** setting is enabled.

   [![Project Setup](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/30bd780f-d3c6-4c09-9d45-a0d1ca50c86c/01-new-project-with-starter-content.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/30bd780f-d3c6-4c09-9d45-a0d1ca50c86c/01-new-project-with-starter-content.png)

   Click image for full size.
2. Once the project has loaded, locate the **SM\_Rock** Static Mesh, and double-click on it to open it up in the **Static Mesh Editor**.

   [![SM_Rock Static Mesh](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/442745f3-cea5-4e74-a1ed-768593893cbc/02-alc-sm-rock.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/442745f3-cea5-4e74-a1ed-768593893cbc/02-alc-sm-rock.png)

   Click image for full size.

## Creating LODs

There are two different ways in which LODs can be generated. The first method, which is the method Epic recommends, is to use the **LOD Group** presets, which automatically creates LODs based on pre-configured settings. The second method involves setting up the LODs yourself. Below, you will find detailed descriptions on how to use each LOD creation method.

### Using LOD Groups

Using LOD Groups is the preferred way to create LODs inside UE5 with the Automatic LOD tool. In the following section, we will go over how you go about setting up and using LOD groups in your UE5 projects.

1. First, locate your project's **BaseEngine.ini** file and open it up inside of a Text editor. Now, look for the `[StaticMeshLODSettings]` section. If you do not see this entry in your BaseEngine.ini file, copy and paste the following code into your BaseEngine.ini file.

   ```
            [StaticMeshLODSettings]
            LevelArchitecture=(NumLODs=4,LightMapResolution=32,LODPercentTriangles=50,PixelError=12,SilhouetteImportance=4,Name=LOCTEXT("LevelArchitectureLOD","Level Architecture"))
            SmallProp=(NumLODs=4,LODPercentTriangles=50,PixelError=10,Name=LOCTEXT("SmallPropLOD","Small Prop"))
            LargeProp=(NumLODs=4,LODPercentTriangles=50,PixelError=10,Name=LOCTEXT("LargePropLOD","Large Prop"))
            Deco=(NumLODs=4,LODPercentTriangles=50,PixelError=10,Name=LOCTEXT("DecoLOD","Deco"))
            Vista=(NumLODs=1,Name=LOCTEXT("VistaLOD","Vista"))
            Foliage=(NumLODs=1,Name=LOCTEXT("FoliageLOD","Foliage"))
            HighDetail=(NumLODs=6,LODPercentTriangles=50,PixelError=6,Name=LOCTEXT("HighDetailLOD","High Detail"))
   		
   Copy full snippet
   ```



   Adding, removing, or adjusting entries from this section will add, remove, or adjust how the LOD groups function when they're used.
2. Now, open the UE5 Editor and then open up a Static Mesh you want to generate LODs for by double-clicking on it in the **Content Browser**. For this example, we will be using **SM\_Rock**, which comes with the Starter Content.
3. With the Static Mesh now open in the Static Mesh Editor, go to the **Details** panel and expand the **LOD Settings** section.

   [![LOD Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7f46cb3c-7ced-405f-b36f-793f8119ef42/03-alc-pm-00.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7f46cb3c-7ced-405f-b36f-793f8119ef42/03-alc-pm-00.png)

   Click image for full size.
4. In the LOD Settings section, click on the **LOD Group** button, and from the displayed list, select the **SmallProp** option.

   [![LOD Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2cd27215-37f4-44fb-b605-318429b63478/04-alc-pm-01.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2cd27215-37f4-44fb-b605-318429b63478/04-alc-pm-01.png)

   Click image for full size.
5. You will then be notified that what you are doing will overwrite your current settings with the new setting from SmallProp. Press the **Yes** button to continue.

   [![LOD Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7a8f6d4f-a8e9-411f-b4ac-fd96de19e9f9/05-alc-pm-02.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7a8f6d4f-a8e9-411f-b4ac-fd96de19e9f9/05-alc-pm-02.png)

   Click image for full size.
6. The Static Mesh Editor should now have four new LOD entries (LOD0, LOD1, LOD2, and LOD3) added to the **Details** panel. If you click on each LOD entry, you will notice that the settings correspond to the settings that were defined in the `StaticMeshLODSettings` in your project's BaseEngine.ini file.

   [![LOD Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f746c65c-3d69-4128-836b-2f9ac8fc1ecb/06-alc-pm-03-1.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f746c65c-3d69-4128-836b-2f9ac8fc1ecb/06-alc-pm-03-1.png)

   Click image for full size.

   [![LOD Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/88fab62a-9265-429b-ab14-9aced1e2af14/07-alc-pm-03.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/88fab62a-9265-429b-ab14-9aced1e2af14/07-alc-pm-03.png)

   Click image for full size.

   Make sure **Auto Compute LOD Distances** is checked, as it will help in determining which screen size to use for the LOD. Because the algorithm knows how much visual difference every edge collapse is adding, it can use this information to determine what distance that amount of error is acceptable. Turning this off, means that the screen size for each LOD needs to be set by hand, which could lead to errors.

Now, experiment with the different LOD Group settings to see how they will create LODs for your objects. In the next section, we will go over how to manually create LODs.

### Manually Creating LODs

In this section, we will go over how to manually setup and create LODs for your project's assets.

While the following will create LODs for you, Epic recommends using the LOD Groups method that was described in the previous section.

1. In the **Details** panel of the Static Mesh Editor, expand the **LOD Settings** section, and look for the **Number of LODs** option.

   [![LOD Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/208d1b95-aa5c-44dc-b21f-018cd8aa8be8/08-alc-lod-settings.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/208d1b95-aa5c-44dc-b21f-018cd8aa8be8/08-alc-lod-settings.png)

   Click image for full size.

   The **LOD Group** provides a list of presets to quickly choose the right LOD settings for your project. These can be changed per project in BaseEngine.ini under `[StaticMeshLODSettings]`. We encourage you to set up good categories for your project, primarily using LOD groups, instead of controlling the details of every LOD.
2. Set the **Number of LODs** to **four**, and then press the **Apply Changes** button to add the four (new) LODs to the mesh.

   [![Create LODs](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9f9d58cc-fff9-42c9-927a-86d127d07b2c/09-alc-create-lods.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9f9d58cc-fff9-42c9-927a-86d127d07b2c/09-alc-create-lods.png)

   Click image for full size.

   Make sure **Auto Compute LOD Distances** is checked, as it will help in determining which screen size to use for the LOD. Because the algorithm knows how much visual difference every edge collapse is adding, it can use this information to determine what distance that amount of error is acceptable. Turning this off, means that the screen size for each LOD needs to be set by hand, which could lead to errors.
3. Press the small, white, triangle next to **LOD1** to expand that section, and then press the small, white, triangle next to **Reduction Settings**.

   [![Reduction Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6f6303c5-6e74-41fd-8ba4-cb612d0e4709/10-alc-reduction-settings.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6f6303c5-6e74-41fd-8ba4-cb612d0e4709/10-alc-reduction-settings.png)

   Click image for full size.
4. Under **Reduction Settings**, locate the **Percent Triangle** section, and set it to a value of **75** before pressing the **Apply Changes** button.

   [![LOD1 Reduction](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/14fef997-4a8d-40b4-998f-8c15f68eb9b8/11-alc-lod1-reduction.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/14fef997-4a8d-40b4-998f-8c15f68eb9b8/11-alc-lod1-reduction.png)

   Click image for full size.
5. Now, expand **LOD2** and **LOD3**, setting the **Percent Triangles** for LOD2 to **25** percent, and setting the Percent Triangle for LOD3 to **12** percent. When completed, you will see a number of triangles each LOD uses next to the LOD name (like in the image below).

   [![LOD FINSHED](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2ac6daae-e0ce-4bf9-9468-ff16e0317e5d/12-alc-lod-finished.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2ac6daae-e0ce-4bf9-9468-ff16e0317e5d/12-alc-lod-finished.png)

   Click image for full size.

   [![LOD FINSHED](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2c0168fc-399d-456b-ab23-2667c6261010/13-alc-lod-finished-1.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2c0168fc-399d-456b-ab23-2667c6261010/13-alc-lod-finished-1.png)

   Click image for full size.
6. Now, as you move your camera closer and further away from the object in the Static Mesh Editor, you will be able to see the LODs change. If the visual change in the LODs is too hard to notice, information about the LOD change is displayed on the left side of the screen.

   [![Viewing LODS](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e9fa176c-4735-4cc2-9737-500bf6e85d0e/14-alc-viewing-lods.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e9fa176c-4735-4cc2-9737-500bf6e85d0e/14-alc-viewing-lods.png)

   Click image for full size.

With the LODs now setup for this Static Mesh, when this Static Mesh is placed in a level, it will automatically choose which LOD to display based on how far the camera is away from it.

## End Result

In the following document we took a look at two different ways to use the automatic LOD generation tools UE5 has to offer. Remember that when using the automatic LOD tools, it is best to first setup and define different LOD groups that meet your project's needs and then select those various setting using the LOD Group drop down that can be found under LOD Settings.

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [static meshes](https://dev.epicgames.com/community/search?query=static%20meshes)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Setup](/documentation/en-us/unreal-engine/static-mesh-automatic-lod-generation-in-unreal-engine?application_version=5.7#setup)
* [Creating LODs](/documentation/en-us/unreal-engine/static-mesh-automatic-lod-generation-in-unreal-engine?application_version=5.7#creatinglods)
* [Using LOD Groups](/documentation/en-us/unreal-engine/static-mesh-automatic-lod-generation-in-unreal-engine?application_version=5.7#usinglodgroups)
* [Manually Creating LODs](/documentation/en-us/unreal-engine/static-mesh-automatic-lod-generation-in-unreal-engine?application_version=5.7#manuallycreatinglods)
* [End Result](/documentation/en-us/unreal-engine/static-mesh-automatic-lod-generation-in-unreal-engine?application_version=5.7#endresult)
