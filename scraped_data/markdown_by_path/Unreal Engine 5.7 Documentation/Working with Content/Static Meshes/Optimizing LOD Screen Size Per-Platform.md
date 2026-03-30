<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/optimizing-lod-screen-size-per-platform-in-unreal-engine?application_version=5.7 -->

# Optimizing LOD Screen Size Per-Platform

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
7. Optimizing LOD Screen Size Per-Platform

# Optimizing LOD Screen Size Per-Platform

How to set up LOD Screen Sizes on a per-platform basis.

![Optimizing LOD Screen Size Per-Platform](https://dev.epicgames.com/community/api/documentation/image/1d6c4a33-1fc5-474f-8e10-31566ffba84f?resizing_type=fill&width=1920&height=335)

 On this page

To control when one Level Of Detail (LOD) Static Mesh transitions into another one, Unreal Engine 5 (UE5) uses the current size of the Static Meshes size in Screen Space. While this method of controlling LOD transitions works quite well the numbers used for one platform might not work for another one. In the following How - To we will take a look at customizing the LOD Screen Size for each platform your UE5 project can be used on.

## Steps

In the following section we will take a look at how to specify the Screen Size at which LOD transactions should take place on a per platform basis.

1. First, inside the **Content Browser**, locate a **Static Mesh** that has a few LODs to work with and open it up inside the **Static Mesh Editor**. For this example the Static Mesh that was selected has four LODs however you can pick one that has more or less depending on the needs of your project.

   [![Static Mesh that has a few LODs](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/40de2f1b-1663-4133-a4be-bf1edfb79f2b/01-pplatform-size-01.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/40de2f1b-1663-4133-a4be-bf1edfb79f2b/01-pplatform-size-01.png)

   Click image for full size.
2. Once the Static Mesh is open in the Static Mesh Editor, go to the **Details Panel** and expand the **LOD Settings** category.

   [![LOD Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/93125f1b-12ef-468a-8e3c-e40fc3787271/02-pplatform-size-02.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/93125f1b-12ef-468a-8e3c-e40fc3787271/02-pplatform-size-02.png)

   Click image for full size.
3. Disable the checkmark box next to **Auto Compute LOD Distances** so that we can manually set the distance at which LOD transition should take place.

   [![Auto Compute LOD Distances](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4fb52e83-2c94-400f-8ec2-56cc502bc948/03-pplatform-size-03.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4fb52e83-2c94-400f-8ec2-56cc502bc948/03-pplatform-size-03.png)

   Click image for full size.
4. Next, go to the **LOD Picker** section and enable the **Custom** option by clicking on the checkmark box next to it. This will allow you to see all LODs at the same time in the Static Mesh editor.

   [![Custom option](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ca3074a6-3c6a-4a97-85e4-eaaa854817b1/04-pplatform-size-04.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ca3074a6-3c6a-4a97-85e4-eaaa854817b1/04-pplatform-size-04.png)

   Click image for full size.
5. Expand the **LOD1** section and next to the **Screen Size** option,click on the **small white triangle** to expose the option to add per-platform LOD overrides.

   [![Screen Size](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/80ab06f3-f3e1-4705-9df0-f35bb1a182cb/05-pplatform-size-05.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/80ab06f3-f3e1-4705-9df0-f35bb1a182cb/05-pplatform-size-05.png)

   Click image for full size.
6. From the displayed per-platform override list, select the **Add Override for Mobile** option.

   [![Add Override for Mobile](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/03621b5c-a97f-4c4e-90fd-6b84d776b5ef/06-pplatform-size-06.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/03621b5c-a97f-4c4e-90fd-6b84d776b5ef/06-pplatform-size-06.png)

   Click image for full size.
7. Repeat the above step for **LOD 2** and **LOD 3** and when completed your Details panel should look like the following image.

   [![Screen Size](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c5338ece-93b7-4001-b36c-cfe91ccde744/07-pplatform-size-07.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c5338ece-93b7-4001-b36c-cfe91ccde744/07-pplatform-size-07.png)

   Click image for full size.
8. You can now adjust the Mobile Screen size by inputting a new number in the box under the **Mobile** option. To figure out which screen size you should use for which LOD, the **Viewport** inside the Static Mesh Editor displays the **Current Screen Size**.

   [![Current Screen Size](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fdeb3e58-6be9-4c90-9cca-d6b5aedc20fe/08-pplatform-size-08.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fdeb3e58-6be9-4c90-9cca-d6b5aedc20fe/08-pplatform-size-08.png)

   Click image for full size.

## End Result

With the ability to override the distance at which LODs will transition on Mobile devices set, you can now go back and setup the transition distance for Console and PC using the exact same steps if that is required for your project. If you decide to do this then your LOD sections will look like the following image.

[![End Result](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4d57728e-cc0e-4f58-b8aa-64ec11e9d721/09-pplatform-size-09.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4d57728e-cc0e-4f58-b8aa-64ec11e9d721/09-pplatform-size-09.png)

Click image for full size.

* [import](https://dev.epicgames.com/community/search?query=import)
* [ui](https://dev.epicgames.com/community/search?query=ui)
* [static meshes](https://dev.epicgames.com/community/search?query=static%20meshes)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/optimizing-lod-screen-size-per-platform-in-unreal-engine?application_version=5.7#steps)
* [End Result](/documentation/en-us/unreal-engine/optimizing-lod-screen-size-per-platform-in-unreal-engine?application_version=5.7#endresult)
