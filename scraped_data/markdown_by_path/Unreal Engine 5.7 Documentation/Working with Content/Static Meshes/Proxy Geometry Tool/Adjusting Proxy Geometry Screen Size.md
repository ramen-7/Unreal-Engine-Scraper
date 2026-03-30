<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/adjusting-proxy-geometry-screen-size-in-unreal-engine?application_version=5.7 -->

# Adjusting Proxy Geometry Screen Size

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
7. [Proxy Geometry Tool](/documentation/en-us/unreal-engine/proxy-geometry-tool-in-unreal-engine "Proxy Geometry Tool")
8. Adjusting Proxy Geometry Screen Size

# Adjusting Proxy Geometry Screen Size

Product documentation including reference and guides for Unreal Engine 5

![Adjusting Proxy Geometry Screen Size](https://dev.epicgames.com/community/api/documentation/image/66453294-2b0a-4c31-84cb-868b1b8278e4?resizing_type=fill&width=1920&height=335)

 On this page

In the following How - To we, will take a look at using the **Spatial Sampling Distance** override parameter to manually adjust the feature minimum size that the system captures when it re-meshes all the Objects (before it simplifies).

## Steps

1. First, inside of any Unreal Engine 5 (UE5) level, select a few Static Meshes to work with.

   [![Select a few Static Meshes](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3bfa7d2f-7b5b-4b23-9746-55f85044ecdf/01-a-few-static-meshes.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3bfa7d2f-7b5b-4b23-9746-55f85044ecdf/01-a-few-static-meshes.png)

   Click image for full size.
2. With the Static Meshes still selected open up the **Merge Actors** tool by going to  **Tools.**  Then from the displayed list, select the **Merge Actors** tool.

   [![Merge Actors tool](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/01afb58d-81ee-4718-961c-cca2c16efc99/02-merge-actors-tool.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/01afb58d-81ee-4718-961c-cca2c16efc99/02-merge-actors-tool.png)

   Click image for full size.
3. When the Merge Actors tool opens, click on the **2nd** icon to access the **Proxy Geometry** tools. Then under **Proxy Settings**, expand the **Material Settings** section.

   [![Proxy Geometry tools](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5dd17b42-b2a8-4b73-beff-2b868cc390c7/03-simplify.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5dd17b42-b2a8-4b73-beff-2b868cc390c7/03-simplify.png)

   Click image for full size.
4. Locate the **Override Spatial Sampling Distance** parameter and click on the box next to its name to enable it.

   [![Override Spatial Sampling Distance](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2ad8e7fa-593e-4ba5-b873-8c6e993e57ec/04-override-spatial-sampling-distance.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2ad8e7fa-593e-4ba5-b873-8c6e993e57ec/04-override-spatial-sampling-distance.png)

   Click image for full size.
5. Set the value of Override Spatial Sampling Distance to 100 and then press the **Merge Actors** button.

   [![Merge Actors](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/79875696-4346-4ec7-b525-5baed4da5e4d/05-merge-actors.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/79875696-4346-4ec7-b525-5baed4da5e4d/05-merge-actors.png)

   Click image for full size.

   By default, the system computes a guess at this size based on the bounding box of the geometry and the requested **Screen Size**. If you look in the **Window > Developer Tool > Output Log**, you will see that the actual number used by the system will be written out. The larger this number is, the less simplification will be performed. The smaller the number is, more simplification will be performed.
6. Specify a name and location for the newly created Static Mesh and then press the **Save** button to begin the Proxy Geometry creation process.

   [![Newly created Static Mesh](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5f0b42f9-a51b-48d9-b9e1-6d1afe12d695/06-newly-created-static-mesh.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5f0b42f9-a51b-48d9-b9e1-6d1afe12d695/06-newly-created-static-mesh.png)

   Click image for full size.

## End Result

When the process has completed you will now have a new Static Mesh, Material and Textures of all the Static Meshes you had selected in the first step of this How - To. The images below demonstrate the effects of setting the Override Spatial Sampling Distance to different values has on the created Static Mesh.

![Override Spatial Sampling Distance = 0.5 | Override Spatial Sampling Distance = 1 | Override Spatial Sampling Distance = 10 | Override Spatial Sampling Distance = 100](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6df43147-22d3-46c0-a6e3-26ac7d211563/07-override-spatial-sampling-distance-original.png "Override Spatial Sampling Distance Original")
![Override Spatial Sampling Distance = 0.5 | Override Spatial Sampling Distance = 1 | Override Spatial Sampling Distance = 10 | Override Spatial Sampling Distance = 100](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8aa20bae-5d41-4f16-8457-e19926c7c5c5/08-override-spatial-sampling-distance-0-5.png "Override Spatial Sampling Distance = 0.5")
![Override Spatial Sampling Distance = 0.5 | Override Spatial Sampling Distance = 1 | Override Spatial Sampling Distance = 10 | Override Spatial Sampling Distance = 100](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a2680098-300f-4ef5-9aff-fff7cc126142/09-override-spatial-sampling-distance-1.png "Override Spatial Sampling Distance = 1")
![Override Spatial Sampling Distance = 0.5 | Override Spatial Sampling Distance = 1 | Override Spatial Sampling Distance = 10 | Override Spatial Sampling Distance = 100](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a16aeb71-2817-44bb-89bb-3df2d58a3617/10-override-spatial-sampling-distance-10.png "Override Spatial Sampling Distance = 10")
![Override Spatial Sampling Distance = 0.5 | Override Spatial Sampling Distance = 1 | Override Spatial Sampling Distance = 10 | Override Spatial Sampling Distance = 100](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d21c997a-2a52-425b-8c22-7fc72ddddf15/11-override-spatial-sampling-distance-100.png "Override Spatial Sampling Distance = 100")

Override Spatial Sampling Distance = 0.5 | Override Spatial Sampling Distance = 1 | Override Spatial Sampling Distance = 10 | Override Spatial Sampling Distance = 100

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [optimization](https://dev.epicgames.com/community/search?query=optimization)
* [proxygeometrytool](https://dev.epicgames.com/community/search?query=proxygeometrytool)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/adjusting-proxy-geometry-screen-size-in-unreal-engine?application_version=5.7#steps)
* [End Result](/documentation/en-us/unreal-engine/adjusting-proxy-geometry-screen-size-in-unreal-engine?application_version=5.7#endresult)
