<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-the-chunkdownloader-plugin-in-unreal-engine?application_version=5.7 -->

# Setting Up the ChunkDownloader Plugin

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
5. [Sharing and Releasing Projects](/documentation/en-us/unreal-engine/sharing-and-releasing-projects-for-unreal-engine "Sharing and Releasing Projects")
6. [Patching and DLC](/documentation/en-us/unreal-engine/patching-content-delivery-and-dlc-in-unreal-engine "Patching and DLC")
7. [Using ChunkDownloader for Patching](/documentation/en-us/unreal-engine/using-chunkdownloader-for-patching-unreal-engine-games "Using ChunkDownloader for Patching")
8. Setting Up the ChunkDownloader Plugin

# Setting Up the ChunkDownloader Plugin

How to set up a Project Settings and Plugins for working with ChunkDownloader

![Setting Up the ChunkDownloader Plugin](https://dev.epicgames.com/community/api/documentation/image/a76b6c15-b406-4636-9fc1-6979ae06c524?resizing_type=fill&width=1920&height=335)

 On this page

The **ChunkDownloader** patching system is a built-in plugin for **Unreal Engine** that provides patching functionality. This page shows how to set up **Project Settings** and **Plugins** of your Unreal Engine project for using ChunkDowloader.

This example uses **C++ project** based on **Blank template**. This project has name **PatchingDemo**.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/44389e60-fc08-4b6b-98df-d7317199bffd/01_createproject.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/44389e60-fc08-4b6b-98df-d7317199bffd/01_createproject.png)

Click image to enlarge.

This example uses **C++ project** based on **Blank template**. The project has name **PatchingDemo**.

## Steps

1. Open your **Project Settings**, navigate to **Project > Packaging**, then make sure that **Use Pak File** and **Generate Chunks** are both enabled.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/35ff3075-8f3c-460d-9756-458aeeb3fe10/02_projsetenablechunking.png)
2. Open the **Plugins** window and enable the **Chunk Downloader** plugin. Restart the **Unreal Editor** for your changes to take effect.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/734580b7-b9a6-4d73-9582-54d856aedec2/03_chunkdownloaderplugin.png)
3. Open your project's `[ProjectName]Build.cs` file in **Visual Studio**. This file locates under `[ProjectName]/Source/[ProjectName]`.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8ee769d1-27d6-46ee-b279-d8c6efb7c55b/04_buildfileloc.png)
4. Edit file by adding **ChunkDownloader** to your `ModuleRules` as `PrivateDependencyModuleNames`. For this add the following section to the `ModuleRules` in the file.

   ```
            PrivateDependencyModuleNames.AddRange(new string[] { "ChunkDownloader" } );
   		
   Copy full snippet
   ```
5. **Save** your changes to this file.
6. Right-click on your **[ProjectName].uproject** file and click **Generate Visual Studio project files**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/df31c821-d060-4acb-a671-e87b320f2c60/05_genvsprojfiles.png)
7. Return to your project's solution in **Visual Studio**, then **Build** the project.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bf2249f2-97ac-4373-a7dc-0ce7105bc02c/06_vsbuildproject.png)

## Final Result

Now, ChunkDownloader is available to use in your project. You can proceed with implementing this in your game's code to download and mount packaging files (see [Preparing Assets for Chunking](/documentation/en-us/unreal-engine/preparing-assets-for-chunking-in-unreal-engine)).

* [patching](https://dev.epicgames.com/community/search?query=patching)
* [chunkdownloader](https://dev.epicgames.com/community/search?query=chunkdownloader)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/setting-up-the-chunkdownloader-plugin-in-unreal-engine?application_version=5.7#steps)
* [Final Result](/documentation/en-us/unreal-engine/setting-up-the-chunkdownloader-plugin-in-unreal-engine?application_version=5.7#finalresult)
