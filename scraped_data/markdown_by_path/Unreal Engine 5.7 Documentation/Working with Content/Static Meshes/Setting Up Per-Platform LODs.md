<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-per-platform-lods?application_version=5.7 -->

# Setting Up Per-Platform LODs

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
7. Setting Up Per-Platform LODs

# Setting Up Per-Platform LODs

How to set up LOD's on a per-platform basis.

![Setting Up Per-Platform LODs](https://dev.epicgames.com/community/api/documentation/image/22809d19-0708-413f-a07b-8cbec81d4325?resizing_type=fill&width=1920&height=335)

 On this page

While having multiple Level of Detail (LOD) Static Meshes can help lessen the rendering cost of distance objects, the extra memory required to store this information can be an issue on platforms that have limited resources like memory. In the following How-To we will take a look at restricting the number of LOD's a platform can use.

## Steps

In the following section we will take a look at specifying which LOD's should be used when your UE5 project is used on PC, Console, and Mobile platforms.

1. First, inside the **Content Browser**, locate a **Static Mesh** that has a few LOD's to work with and open it up inside the **Static Mesh Editor**. For this example the Static Mesh that was selected has four LOD's however you can pick one that has more or less depending on the needs of your project.

   [![Per-Platform LOD](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/24474dab-945f-49fb-a3d3-d64158b8ea3f/01-pplatform-lod01.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/24474dab-945f-49fb-a3d3-d64158b8ea3f/01-pplatform-lod01.png)

   Click image for full size.
2. Once the Static Mesh is open in the Static Mesh Editor, go to the **Details Panel** and expand the **LOD Settings** category.

   [![LOD Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d0beedfe-a856-4d58-9e3b-72a239a003b6/02-pplatform-lod02.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d0beedfe-a856-4d58-9e3b-72a239a003b6/02-pplatform-lod02.png)

   Click image for full size.
3. Locate the **Minimum LOD** input and then click on the small white triangle next to it to expose the per-platform LOD options.

   [![Minimum LOD](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0f8dff86-d916-4961-9188-93524db7474d/03-pplatform-lod03.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0f8dff86-d916-4961-9188-93524db7474d/03-pplatform-lod03.png)

   Click image for full size.
4. From the displayed list, select the platform that you want to override by clicking on the platform name. For this example we will be setting overrides for **Desktop**, **Mobile** and **Console**.

   [![Desktop Mobile Console](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/be329868-31b3-4be7-aa5a-5cbb83c93613/04-pplatform-lod04.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/be329868-31b3-4be7-aa5a-5cbb83c93613/04-pplatform-lod04.png)

   Click image for full size.
5. The Minimum LOD setting works by restricting which LOD level should be used first. Since our example Static Mesh has four LOD's this means that we can input numbers ranging from zero to four. Inputting zero will allow each LOD to be used while inputting four will allow only the last LOD to be used. For this example input a value of **zero** into Default, input a value of **one** into Desktop, input a value of **two** into Console, and finally input a value of **three** into Mobile.

   [![Desktop Mobile Console](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/76db45d7-6e30-498a-b43b-c2f72f0d75fe/05-pplatform-lod05.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/76db45d7-6e30-498a-b43b-c2f72f0d75fe/05-pplatform-lod05.png)

   Click image for full size.
6. Once that is completed, make sure to press the **Save** button to save your changes.

   [![Save button](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/46541a3b-a61f-4ea0-bbfe-eae7c4b840f7/06-pplatform-lod06.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/46541a3b-a61f-4ea0-bbfe-eae7c4b840f7/06-pplatform-lod06.png)

   Click image for full size.

## End Result

Once all platforms have had their respective LOD's set, the Static Mesh is now ready to be used in your UE5 project. To get a better understanding of how this works, check out the following image:

[![End Result](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6f7b2a10-c5bb-4824-bb4b-f5642473211c/07-pplatform-lod07.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6f7b2a10-c5bb-4824-bb4b-f5642473211c/07-pplatform-lod07.png)

Click image for full size.

* When this Static Mesh is viewed on a PC, it will only display three of the four LOD's because the **Minimum LOD** for **PC** was set to a value of **one**.
* When this Static Mesh is viewed on a Console, it will only display two of the four LOD's because the **Minimum LOD** for **Console's** was set to a value of **two**.
* When this Static Mesh is viewed on Mobile, it will only display one of the four LOD's because the **Minimum LOD** for **Mobile** was set to a value of **three**.

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [static meshes](https://dev.epicgames.com/community/search?query=static%20meshes)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/setting-up-per-platform-lods?application_version=5.7#steps)
* [End Result](/documentation/en-us/unreal-engine/setting-up-per-platform-lods?application_version=5.7#endresult)
