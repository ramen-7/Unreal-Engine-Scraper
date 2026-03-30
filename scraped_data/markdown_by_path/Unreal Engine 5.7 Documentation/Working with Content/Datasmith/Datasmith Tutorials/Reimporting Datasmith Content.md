<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/reimporting-datasmith-content-into-unreal-engine?application_version=5.7 -->

# Reimporting Datasmith Content

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
6. [Datasmith](/documentation/en-us/unreal-engine/datasmith-plugins-for-unreal-engine "Datasmith")
7. [Datasmith Tutorials](/documentation/en-us/unreal-engine/datasmith-tutorials-in-unreal-engine "Datasmith Tutorials")
8. Reimporting Datasmith Content

# Reimporting Datasmith Content

Detailed instructions on the various ways you can update Datasmith content that you've already imported into Unreal to pick up changes in the source material.

![Reimporting Datasmith Content](https://dev.epicgames.com/community/api/documentation/image/f105d51a-d540-4746-b5a2-3a5abb897340?resizing_type=fill&width=1920&height=335)

 On this page

This page describes how to reimport Datasmith content into the Unreal Editor, and how to control what updates get synchronized to the Actors in your Levels.

For background information, including an overview of what reimporting does to the assets in your Project and the Actors in your Level, see [Datasmith Reimport Workflow](/documentation/en-us/unreal-engine/datasmith-reimport-workflow-in-unreal-engine).

## Reimporting the Datasmith Scene Asset

To reimport the Datasmith Scene Asset from a new version of a source file:

1. Right-click the **Datasmith Scene** Asset in the Content Browser.

   [![Reimport or Reimport With New File](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/243913e8-74c4-486a-a559-a99aa55effd3/ue5_01-datasmith-reimport-scene.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/243913e8-74c4-486a-a559-a99aa55effd3/ue5_01-datasmith-reimport-scene.png)

   Click image for full size.

   * If you've saved the changes to your source scene into the same file on disk that you last used to create or reimport this Datasmith Scene Asset, select **Reimport** from the context menu.
   * If you've saved the changes to your source scene into a different file on disk, select **Reimport With New File** from the context menu, and browse to the new file you want to use.
2. You'll be prompted to specify some reimport options. These are the same ones you originally set on import, with a couple of additions.  
   The new options, under **Sync Current Level Actors**, determine whether the updates made to your Datasmith Scene Asset should also be applied to any Datasmith Scene Actors in the current Level that were created from the Asset you're updating.

   [![Reimport options](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d7ec087c-6fa5-454f-9b9b-c99f76c308b5/ue5_02-datasmith-reimport-options.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d7ec087c-6fa5-454f-9b9b-c99f76c308b5/ue5_02-datasmith-reimport-options.png)

   Click image for full size.

   If you don't want to synchronize your Actors now, you can do it later. See [Synchronizing a Datasmith Scene Actor with its Asset](/documentation/en-us/unreal-engine/reimporting-datasmith-content-into-unreal-engine#synchronizingadatasmithsceneactorwithitsasset) below.  
   For more information on the other import options, see [Datasmith Import Process](/documentation/en-us/unreal-engine/datasmith-import-process-in-unreal-engine).
3. Set the options you want the importer to use, and click **Import**.

The reimport process may overwrite Static Mesh geometry, Parent Materials, and Texture Assets in your Content Browser. For details, see [Datasmith Reimport Workflow](/documentation/en-us/unreal-engine/datasmith-reimport-workflow-in-unreal-engine).

## Synchronizing a Datasmith Scene Actor with its Asset

There are two ways you can re-synchronize a Datasmith Scene Actor in a Level with its corresponding Datasmith Scene Asset:

* [During the reimport](/documentation/en-us/unreal-engine/reimporting-datasmith-content-into-unreal-engine#duringthereimport).
* [After the reimport](/documentation/en-us/unreal-engine/reimporting-datasmith-content-into-unreal-engine#afterthereimport).

### During the Reimport

At the time you reimport a Datasmith Scene Asset:

1. Open the Level that contains your Datasmith Scene Actor.
2. Reimport your Datasmith Scene Asset as described under [Reimporting the Datasmith Scene Asset](/documentation/en-us/unreal-engine/reimporting-datasmith-content-into-unreal-engine#reimportingthedatasmithsceneasset) above.
3. In the **Import Options** dialog, find the **Sync Current Level Actors** section. Make sure to check the **Datasmith Scene Actors** box.  
   If you want to add back to your Level any Actors that you've previously deleted, also check the **Re-Spawn Deleted Actors** option.

   [![Reimport options](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/28aa60ee-6e70-4d02-8ccd-b820418041aa/ue5_03-datasmith-reimport-options.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/28aa60ee-6e70-4d02-8ccd-b820418041aa/ue5_03-datasmith-reimport-options.png)

   Click image for full size.
4. Click **Import**.

### After the Reimport

At any time after you reimport a Datasmith Scene Asset:

1. Open the Level that contains your Datasmith Scene Actor.
2. Select the Datasmith Scene Actor in the **Outliner**.

   [![Select Datasmith Scene Actor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/aba517f4-bb57-4899-bf27-011d10530ca2/ue5_04-datasmith-reimport-select-scene-actor.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/aba517f4-bb57-4899-bf27-011d10530ca2/ue5_04-datasmith-reimport-select-scene-actor.png)

   Click image for full size.
3. In the **Details** panel, find the **Datasmith** section.

   [![Update Actors from Scene](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2750b46c-e8b3-44d5-bbe2-3598437128c9/ue5_05-datasmith-reimport-sync-details.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2750b46c-e8b3-44d5-bbe2-3598437128c9/ue5_05-datasmith-reimport-sync-details.png)

   Click image for full size.
4. If you want to add back to your Level any Actors that you've previously deleted, check the **Respawn deleted actors** option.
5. Click **Update actors from Scene**.

## Reimporting Individual Assets

Instead of reimporting an entire Datasmith Scene Asset, you can pick and choose individual Static Mesh, Material, and Texture Assets to update.

To re-import a single Asset:

1. Right-click the Asset in the Content Browser, and choose **Reimport** from the context menu.

   [![Reimport Static Mesh Asset](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f1da3b3b-1139-43c8-803e-0c7a85ea7c38/ue5_06-datasmith-reimport-asset.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f1da3b3b-1139-43c8-803e-0c7a85ea7c38/ue5_06-datasmith-reimport-asset.png)

   Click image for full size.

   For a Material Asset, choose **Datasmith > Reimport Material**.

   [![Reimport Material Asset](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/992c2379-0768-4c2f-91dd-f46009fd746f/ue5_07-datasmith-reimport-material.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/992c2379-0768-4c2f-91dd-f46009fd746f/ue5_07-datasmith-reimport-material.png)

   Click image for full size.

   You'll only see the **Datasmith > Reimport** **Material** option for Material Assets that Datasmith created from scratch to match a material definition in your source file, which is typically the case only for Parent Materials imported from 3ds Max. However, this option does not appear for Material Assets that are instances of Materials built in to Datasmith, which is typically the case for Materials imported from CAD files or SketchUp.
2. You'll be prompted to specify some reimport options for the Asset.  
   These are the same ones you originally set on import. For more information on all these options, see [Datasmith Import Process](/documentation/en-us/unreal-engine/datasmith-import-process-in-unreal-engine).

When you re-import individual Assets, you don't get the option to synchronize Level Actors. Every reference to the Asset in your Project will automatically use the updated version of your Asset. See [Datasmith Reimport Workflow](/documentation/en-us/unreal-engine/datasmith-reimport-workflow-in-unreal-engine).

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [datasmith](https://dev.epicgames.com/community/search?query=datasmith)
* [enterprise](https://dev.epicgames.com/community/search?query=enterprise)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Reimporting the Datasmith Scene Asset](/documentation/en-us/unreal-engine/reimporting-datasmith-content-into-unreal-engine?application_version=5.7#reimportingthedatasmithsceneasset)
* [Synchronizing a Datasmith Scene Actor with its Asset](/documentation/en-us/unreal-engine/reimporting-datasmith-content-into-unreal-engine?application_version=5.7#synchronizingadatasmithsceneactorwithitsasset)
* [During the Reimport](/documentation/en-us/unreal-engine/reimporting-datasmith-content-into-unreal-engine?application_version=5.7#duringthereimport)
* [After the Reimport](/documentation/en-us/unreal-engine/reimporting-datasmith-content-into-unreal-engine?application_version=5.7#afterthereimport)
* [Reimporting Individual Assets](/documentation/en-us/unreal-engine/reimporting-datasmith-content-into-unreal-engine?application_version=5.7#reimportingindividualassets)
