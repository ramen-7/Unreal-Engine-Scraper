<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-direct-link-to-synchronize-3ds-max-and-unreal-engine?application_version=5.7 -->

# Synchronizing 3ds Max and Unreal with Direct Link

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
7. [Datasmith Software Interop Guides](/documentation/en-us/unreal-engine/datasmith-software-interop-guides-for-unreal-engine "Datasmith Software Interop Guides")
8. [3ds Max](/documentation/en-us/unreal-engine/using-datasmith-with-3ds-max-in-unreal-engine "3ds Max")
9. Synchronizing 3ds Max and Unreal with Direct Link

# Synchronizing 3ds Max and Unreal with Direct Link

Explains how to set up a Datasmith Direct Link connection so you can synchronize a 3ds Max scene with Unreal Engine.

![Synchronizing 3ds Max and Unreal with Direct Link](https://dev.epicgames.com/community/api/documentation/image/7c2cdc1a-de27-4fee-8f55-60f20d8d69e0?resizing_type=fill&width=1920&height=335)

 On this page

The Datasmith Export for 3ds Max plugin supports Datasmith Direct Link (see [Using Datasmith Direct Link](/documentation/en-us/unreal-engine/using-datasmith-direct-link-in-unreal-engine)). Direct Link works by exporting your 3ds Max scene to a local cache. When you connect 3ds Max to Unreal Engine, or another connected application such as Twinmotion, it imports the scene from the cache.

To synchronize a 3ds Max Scene with Unreal Engine, your Unreal Engine project must have the Datasmith Importer plugin enabled. If you don't enable the plugin, you won't see the Datasmith options in Unreal Engine. For more information, refer tosee Enable the Datasmith Importer Plugin.

To synchronize a 3ds Max Scene with Unreal Engine:

* Update the Direct Link cache (see [Update the Direct Link Cache](/documentation/en-us/unreal-engine/using-direct-link-to-synchronize-3ds-max-and-unreal-engine#updatethedirectlinkcache)).
* Use Direct Link to Import the 3ds Max scene into Unreal Engine (see [Import the 3ds Max Scene with Direct Link](/documentation/en-us/unreal-engine/using-direct-link-to-synchronize-3ds-max-and-unreal-engine#importthe3dsmaxscenewithdirectlink)).

If you perform a Direct Link import before you update the cache, Unreal Engine will display an error message because there is nothing in the cache to import.

## Update the Direct Link Cache

From the 3ds Max ribbon, use the synchronize options in the Direct Link panel of the Datasmith tab.

* **Synchronize**: Performs a one-time push to the Direct Link Cache. When Unreal Engine, or another connected application, connects to 3ds Max via Direct Link, it imports the cache.

  Use this command if you want to control when Unreal Engine displays changes to the 3ds Max scene.
* **Toggle Auto Sync**: When enabled, Datasmith pushes the 3ds Max scene to the Direct Link cache every time you make a change. Unreal engine and any other connected applications re-import the cache automatically.

  Use this command if you want Unreal Engine to update whenever you make a change to the 3ds Max scene.

## Import the 3ds Max Scene with Direct Link

1. In 3ds Max, open the scene you want to import into Unreal Engine, and [update the Direct Link cache](/documentation/en-us/unreal-engine/using-direct-link-to-synchronize-3ds-max-and-unreal-engine#updatethedirectlinkcache).
2. In Unreal Engine, in the main toolbar, open the Create menu and select **Datasmith > Direct Link Import**.   
   ![Direct Link Import](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8abc341a-6da5-4fcf-8c2a-25f880a03eef/direct-link-import-menu.png)  
   The Direct Link Available Sources dialog opens.

   If you have more than one instance of 3ds Max open, each instance appears as a separate source in the Direct Link Available Sources dialog.
3. Select the 3ds Max source that you want to import into Unreal Engine, and click Select. A file dialog opens.
4. Choose a location in your project to store the imported content, and click OK. The Datasmith Import Options dialog opens.

   To create a new top-level folder for your Datasmith content, right-click an empty area in the file dialog. To create a subfolder of an existing folder, right-click that folder.
5. Set the import options as needed, and click Import. For more information about the Datasmith Import options, see [Importing Datasmith Content Into Unreal Engine](/documentation/en-us/unreal-engine/importing-datasmith-content-into-unreal-engine).

## Change the Direct Link Cache Directory

When you connect 3ds Max to Unreal Engine using Direct Link, Datasmith uses a cache directory to temporarily store the contents of your Datasmith scene. For example, sent and received `.udatasmith` scenes, meshes, textures, and so on.

You can change the cache directory from the [Connection Status window](/documentation/en-us/unreal-engine/the-datasmith-3ds-max-ui-for-exporting-to-unreal-engine#thedatasmithdirectlinkconnectionstatuswindow):

1. From the **Direct Link** panel of the **Datasmith** tab in the 3ds Max ribbon, select **Connections**. The **Connection Status** window opens.
2. Click the more options button (**⋮**) to display the Cache Directory setting.
3. Click the ellipsis button (**...**) to open a file dialog.
4. Navigate to the directory you want to use, and click **Select Folder**.

The cache location updates the next time you open or create a 3ds Max file and synchronize it with Unreal Engine.

To reset the cache to the default directory, click **Reset**.

* [datasmith](https://dev.epicgames.com/community/search?query=datasmith)
* [enterprise](https://dev.epicgames.com/community/search?query=enterprise)
* [3ds max](https://dev.epicgames.com/community/search?query=3ds%20max)
* [interop](https://dev.epicgames.com/community/search?query=interop)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Update the Direct Link Cache](/documentation/en-us/unreal-engine/using-direct-link-to-synchronize-3ds-max-and-unreal-engine?application_version=5.7#updatethedirectlinkcache)
* [Import the 3ds Max Scene with Direct Link](/documentation/en-us/unreal-engine/using-direct-link-to-synchronize-3ds-max-and-unreal-engine?application_version=5.7#importthe3dsmaxscenewithdirectlink)
* [Change the Direct Link Cache Directory](/documentation/en-us/unreal-engine/using-direct-link-to-synchronize-3ds-max-and-unreal-engine?application_version=5.7#changethedirectlinkcachedirectory)
