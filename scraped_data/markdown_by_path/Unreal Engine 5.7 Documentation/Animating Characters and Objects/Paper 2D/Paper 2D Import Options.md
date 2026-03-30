<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/import-sprites-in-unreal-engine?application_version=5.7 -->

# Paper 2D Import Options

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
5. [Animating Characters and Objects](/documentation/en-us/unreal-engine/animating-characters-and-objects-in-unreal-engine "Animating Characters and Objects")
6. [Paper 2D](/documentation/en-us/unreal-engine/paper-2d-overview-in-unreal-engine "Paper 2D")
7. Paper 2D Import Options

# Paper 2D Import Options

Importing assets from third party applications for use with Paper 2D.

![Paper 2D Import Options](https://dev.epicgames.com/community/api/documentation/image/08cc7ef3-3333-4561-903b-9be19257ee56?resizing_type=fill&width=1920&height=335)

 On this page

Paper 2D in Unreal Engine supports a number of different import options for your externally created content. Below are some examples of importing assets from some of the more commonly used content creation applications.

## Importing from Texture Packer

If you are using the third party sprite sheet generation tool **Texture Packer** for content creation, it has a plug-in built into it which will allow you to easily import your content into Unreal Engine by creating a **.paper2dsprites** file. This file when imported into UE will automatically import your sprite sheet as a texture, extract and create sprites from it as well as create a **Sprite Asset** which can be used to auto-generate **Flipbooks** out of your sprites.

**Example Workflow**

1. Inside **Texture Packer**, select the **UnrealEngine - Paper2d** framework option.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/12fb3315-cc07-4e91-8c39-462d407a3f3a/newprojecttp.png)
2. Add your assets that will be included in the sprite sheet.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4e831ee4-851a-4e17-9073-f695c796b753/assets_added.png)
3. Under **Layout** set **Size Constraints** to **POT (Power of 2)**.
4. Under **Sprites**, show advanced and set **Border** and **Shape Padding** to **0**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f9046063-e4b6-4547-ba9b-10dca464659a/exportsettings.png)

   This will eliminate the spaces between your sprites, making it easier to tile them together or create **Flipbook** animations.
5. Click the **Publish** sprite option (this will create a **.paper2dsprites** file along with a **.png** sprite sheet)
6. Drag the **.paper2dsprites** file into the **Content Browser** of your project to import it.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9f51cc35-7127-4143-8106-bf14db616c78/draganddrop.png)

   The .png file is already included with the .paper2dsprites file so there is no need to import that as well.
7. This will create a **Sprite Sheet** asset and two folders **Frames** (extracted sprites) and **Textures** (your sprite sheet).

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c2f21d92-8ca0-43ec-9fd0-d48f030c4c72/contentadded.png)

From here you can **Right-click** on...

* Your **Sprite Sheet** asset to automatically generate **Flipbooks** based on your sprites.
* Your imported texture to adjust its settings, configure it for retro sprites or create a **Tile Set** based on it.
* Your individual frames to manually add them to a **Flipbook**.

## Importing from Tiled / Adobe Flash CS6

If you are building your content in external content generation tools such as **Tiled** or **Adobe Flash CS6**, you can import your work into Unreal Engine in the **.json** file format. This will automatically import the sprite sheet(s) used to create your map and create **Tile Sets** and a **Tile Map** based off those assets for you.

**Example Workflow for Tiled**

1. Inside **Tiled**, choose the File/Save As option, then Save as type **.json**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6cdd92e3-1061-4bf5-8834-8d05c0245590/tiledexport.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6cdd92e3-1061-4bf5-8834-8d05c0245590/tiledexport.png)

   *Click for full view.*
2. Drag-and-drop the **.json** asset into the **Content Browser** of your project.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a3a41b43-fe9c-432f-b266-883ec8c90251/jsonimport.png)
3. This will import your sprite sheet textures, create **Tile Sets** and a **Tile Map** from those textures.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0e2b164a-ad77-4873-81e8-ac7014f16f84/jsonassets.png)

   Opening the **Tile Map** created, you will see the map constructed externally which can be modified inside Unreal Engine.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Importing from Texture Packer](/documentation/en-us/unreal-engine/import-sprites-in-unreal-engine?application_version=5.7#importingfromtexturepacker)
* [Importing from Tiled / Adobe Flash CS6](/documentation/en-us/unreal-engine/import-sprites-in-unreal-engine?application_version=5.7#importingfromtiled/adobeflashcs6)
