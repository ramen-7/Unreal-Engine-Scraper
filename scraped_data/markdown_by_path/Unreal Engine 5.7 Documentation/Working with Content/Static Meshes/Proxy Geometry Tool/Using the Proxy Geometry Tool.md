<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-proxy-geometry-tool-in-unreal-engine?application_version=5.7 -->

# Using the Proxy Geometry Tool

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
8. Using the Proxy Geometry Tool

# Using the Proxy Geometry Tool

In the following How - To we will take a look at how you go about using the Proxy Geometry Tool in your UE5 projects.

![Using the Proxy Geometry Tool](https://dev.epicgames.com/community/api/documentation/image/4c79a311-c082-42a6-a4bc-3adede9d4717?resizing_type=fill&width=1920&height=335)

 On this page

In the following How - To we will take a look at using the Proxy Geometry Tool to create new Static Meshes and Textures for your UE5 projects levels.

## Steps

1. The  **Proxy Geometry Tools**  are part of the Merge Actor tools so to open them up you need to go to  **Tools** and then click on the **Merge Actors** option.

   [![Merge Actors tool](https://dev.epicgames.com/community/api/documentation/image/a97e1df1-d2fd-47b6-adf5-132148cf69c0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a97e1df1-d2fd-47b6-adf5-132148cf69c0?resizing_type=fit)

   Click image for full size.
2. When the Merge Actors tool is open, you should see two icons at the top. Click on the second icon to show the options for the Proxy Geometry Tools.

   [![Merge Actors tool](https://dev.epicgames.com/community/api/documentation/image/b7c66933-1a11-411a-86b3-ea1dcab1c312?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b7c66933-1a11-411a-86b3-ea1dcab1c312?resizing_type=fit)

   Click image for full size.

   The options in the Proxy Geometry tool will only become active when you have Static Meshes selected in a level.
3. Navigate to a location in a level and then start selecting Static Meshes. For this example 21 Static Meshes have been selected but please feel free to select as many Static Meshes as you want.

   [![Selecting Static Meshes](https://dev.epicgames.com/community/api/documentation/image/8448098a-8bb2-4623-97fb-c3c21fcfb6fc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8448098a-8bb2-4623-97fb-c3c21fcfb6fc?resizing_type=fit)

   Click image for full size.
4. With the Static Meshes still selected locate the Merge Actors window and then press the **Merge Actors** button to begin the Proxy Geometry tool creation process.

   [![Merge Actors button](https://dev.epicgames.com/community/api/documentation/image/65ecc6ff-ea9b-4989-80bf-6cfa586778cd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/65ecc6ff-ea9b-4989-80bf-6cfa586778cd?resizing_type=fit)

   Click image for full size.
5. When prompted, specify a **Name** and **Location** for the new assets that the Proxy Geometry Tool will create. Once that is completed, press the **Save** button to continue the Proxy Geometry tool creation process.

   [![Creating Static Mesh](https://dev.epicgames.com/community/api/documentation/image/490b5476-0260-4fc2-8342-4b79c5254bbe?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/490b5476-0260-4fc2-8342-4b79c5254bbe?resizing_type=fit)

   Click image for full size.

   The time that it takes for the Proxy Geometry tool to finish can range from a few minutes to a few hours. The current progress will be shown in the following window.

   [![Creating Mesh Proxy](https://dev.epicgames.com/community/api/documentation/image/4b9a98a2-c808-42bf-a23a-03bee84b7221?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4b9a98a2-c808-42bf-a23a-03bee84b7221?resizing_type=fit)

   Click image for full size.
6. When the Proxy Geometry tool has completed, go to the Content Browser and search for the newly created assets by input the name given to them in step five.

   [![Newly Created Static Mesh](https://dev.epicgames.com/community/api/documentation/image/66ceed08-b0b5-4767-baf4-36e8a1e53d29?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/66ceed08-b0b5-4767-baf4-36e8a1e53d29?resizing_type=fit)

   Click image for full size.

## End Result

To view the Static Mesh that was created, go to the Content Browser and double-click on the Static Mesh that was generated. When looking at the Static Mesh in the Static Mesh Editor, note the reduced triangle and material count.

[![The Static Mesh view.png](https://dev.epicgames.com/community/api/documentation/image/4ad3f5e8-3a43-43fe-983c-ebbc4d809f75?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4ad3f5e8-3a43-43fe-983c-ebbc4d809f75?resizing_type=fit)

Click image for full size.

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [optimization](https://dev.epicgames.com/community/search?query=optimization)
* [proxy geometry tool](https://dev.epicgames.com/community/search?query=proxy%20geometry%20tool)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/using-the-proxy-geometry-tool-in-unreal-engine?application_version=5.7#steps)
* [End Result](/documentation/en-us/unreal-engine/using-the-proxy-geometry-tool-in-unreal-engine?application_version=5.7#end-result)
