<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-and-using-custom-heightmaps-and-layers-in-unreal-engine?application_version=5.7 -->

# Creating and Using Custom Heightmaps and Target Layers

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
5. [Building Virtual Worlds](/documentation/en-us/unreal-engine/building-virtual-worlds-in-unreal-engine "Building Virtual Worlds")
6. [Landscape Outdoor Terrain](/documentation/en-us/unreal-engine/landscape-outdoor-terrain-in-unreal-engine "Landscape Outdoor Terrain")
7. [Creating Landscapes](/documentation/en-us/unreal-engine/creating-landscapes-in-unreal-engine "Creating Landscapes")
8. Creating and Using Custom Heightmaps and Target Layers

# Creating and Using Custom Heightmaps and Target Layers

How to use custom heightmaps and target layers to add more dimension to your Landscapes.

![Creating and Using Custom Heightmaps and Target Layers](https://dev.epicgames.com/community/api/documentation/image/426a74f1-e3db-4a91-bd15-008bd2a3939b?resizing_type=fill&width=1920&height=335)

 On this page

There will be times your **Landscape** will require that you use external programs to create both the **heightmap** and **target layers** that you need.
Unreal Engine accommodates this style of workflow by allowing for the import of custom heightmaps and target layers.

You use an **Edit Layer** (like a temporary paint layer) to *make* changes, and those changes are applied to a **Target Layer** (like a specific material blend) on the landscape.

Edit layers function as containers for actors (e.g. meshes, lights) to toggle them on/off or assign them to specific views or visibility sets.

A target layer is a specific layer *in your material* (e.g. a "grass" or "mud" weightmap) that your active edit is modifying.

[![Image from the Electric Dreams sample project](https://dev.epicgames.com/community/api/documentation/image/f43c085c-ae21-4d99-8c69-9be7a6c15b57?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f43c085c-ae21-4d99-8c69-9be7a6c15b57?resizing_type=fit)

The Electric Dreams project

If this is your first time using the Landscape tools, you might want to check out the [Landscape Overview](building-virtual-worlds/landscape-outdoor-terrain/editing-landscapes) first.

## Importing Landscape Data from Image Files

Image files can be imported into landscape heightmaps and target layers, which can be used to customize the look and feel of your Landscape.

### Image File Formats

Image data from .PNG and .RAW files can be imported.  The native data format for heightmaps should be single-channel, grayscale, 16 bits per pixel.  The native data format for target layers should be single-channel, grayscale, 8 bits per pixel.  Standard three-channel RGB images can be used, but color information will be lost and the precision of the import process may be limited. If you are creating an image file in Photoshop to use for importing landscape data, use the following settings when creating a new document for a target layer:

[![Image of Photoshop sample settings](https://dev.epicgames.com/community/api/documentation/image/afc379fd-3099-4b7c-a192-479ff7bdd18a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/afc379fd-3099-4b7c-a192-479ff7bdd18a?resizing_type=fit)

Custom image file import formats can be implemented using the `ILandscapeHeightmapFileFormat` and `ILandscapeWeightmapFileFormat` interfaces.

## Using Target Layers in a Landscape Material

Importing image files that are made in an external application provides you with the flexibility to use your preferred terrain workflow, but you first need to make sure that a few things are set up in order to get everything to work smoothly.

1. First, make sure that you have created a Landscape to work with. If you have questions regarding the Landscape creation process, check out [Landscape Creation](building-virtual-worlds/landscape-outdoor-terrain/creating-landscapes).
2. Next, make a new material. For this example, you will be making a very basic material that ca be easily expanded upon if needed. The setup for your material should look something like this.

   [![Blueprints-showing-materials](https://dev.epicgames.com/community/api/documentation/image/a21bf0bb-1c26-4430-a206-a27fe06dad26?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a21bf0bb-1c26-4430-a206-a27fe06dad26?resizing_type=fit)

   | Number | Description |
   | --- | --- |
   | 1 | `LandscapeLayerCoords` |
   | 2 | TextureSample:  Uncut Grass from Quixel Megascans ([Fab](https://www.fab.com/listings/69f0e5f2-0fce-43f5-b737-b3d18de2eb62)) |
   | 3 | TextureSample: Rocky Forest Floor from Quixel Megascans ([Fab](https://www.fab.com/listings/dc4315f2-b1c0-4ceb-ab41-0511dca75926)) |
   | 4 | TextureSample: Rock Cliff from Quixel Megascans ([Fab](https://www.fab.com/listings/9eb0b240-b41d-4cff-b0ac-f278fcd4172c)) |
   | 5 | `LandscapeLayerBlend` |
3. Once the material is complete, apply it to the Landscape actor. This will turn your landscape black.

   [![Apply the Material to the Landscape Actor](https://dev.epicgames.com/community/api/documentation/image/5918307c-e05b-42ee-b6d2-db7497899430?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5918307c-e05b-42ee-b6d2-db7497899430?resizing_type=fit)

   Apply the Material by selecting it in the Content Browser and dragging it to the Landscape Material option in the Details panel.
4. To fix the issue, add some Layer Info to your Landscape actor. For this example, create one Layer Info object for each of the three layers. To read more about Layer Info objects, refer to the [Layer Info Objects](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-paint-mode-in-unreal-engine) page.

   [![Create Layer Info objects and save them](https://dev.epicgames.com/community/api/documentation/image/eaef289e-34aa-44c4-9a6b-24e048782563?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/eaef289e-34aa-44c4-9a6b-24e048782563?resizing_type=fit)

   Create each Layer Info object and save them.
5. When completed, your Target Layers section of your Landscape panel should look something like this.

   [![Target Layers section with each Layer having a Layer Info](https://dev.epicgames.com/community/api/documentation/image/c4e626e7-d52b-4d8f-bc85-c3e696702aa5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c4e626e7-d52b-4d8f-bc85-c3e696702aa5?resizing_type=fit)

   Target Layers section with each Material having an assigned Layer Info.
6. Now it is time to import your custom layer. In **Landscape Mode**, on the **Manage** tab, select the Import from file tab. At the **Heightmap** field, use the (**...**) button to **Browse for file**. This will prompt you to choose the .PNG or .RAW file that contains your custom layer data. Your custom layer file should be the same resolution as your Landscape actor's **Overall Resolution** that was set when you created it (the default is 505 x 505).

   The following chart shows the relation between Landscape heightmap size and Landscape layer size. It is very important that you make sure that your Landscape layer is the correct size. If the layer size is wrong it will not import into UE4.

   | Landscape Heightmap | Layer size |
   | --- | --- |
   | 16 x 16 | 16 x 16 |
   | 32 x 32 | 32 x 32 |
   | 64 x 64 | 64 x 64 |
   | 128 x 128 | 128 x 128 |
   | 256 x 256 | 256 x 256 |
   | 512 x 512 | 505 x 505 |
   | 1024 x 1024 | 1072 x 1072 |
   | 2048 x 2048 | 2160 x 2160 |
   | 4096 x 4096 | 4336 x 4336 |
7. If your layers are not output at the correct size, you will see the following warning:

   [![error-message-about-file-size](https://dev.epicgames.com/community/api/documentation/image/131ab9fe-ca68-43b0-99f3-5ec791d79866?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/131ab9fe-ca68-43b0-99f3-5ec791d79866?resizing_type=fit)

   To fix this issue, return to your image editing software and resize your file to match the correct Landscape extent as displayed by the warning message.

## Heightmaps

Using external tools to create a base heightmap to use inside Unreal Engine can be an excellent way of speeding up the Landscape creation process. Programs such as World Machine and Terragen can quickly create the base heightmap for your Landscape. The base can then be imported, cleaned up, or modified using the editing tools inside Unreal Editor, making it a better fit with the world and the desired game play.

For more information on importing and exporting heightmaps, see [Importing and Exporting Landscape Heightmaps](https://dev.epicgames.com/documentation/en-us/unreal-engine/importing-and-exporting-landscape-heightmaps-in-unreal-engine).

* [landscape](https://dev.epicgames.com/community/search?query=landscape)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Importing Landscape Data from Image Files](/documentation/en-us/unreal-engine/creating-and-using-custom-heightmaps-and-layers-in-unreal-engine?application_version=5.7#layers)
* [Image File Formats](/documentation/en-us/unreal-engine/creating-and-using-custom-heightmaps-and-layers-in-unreal-engine?application_version=5.7#layer-formats)
* [Using Target Layers in a Landscape Material](/documentation/en-us/unreal-engine/creating-and-using-custom-heightmaps-and-layers-in-unreal-engine?application_version=5.7#layer-import)
* [Heightmaps](/documentation/en-us/unreal-engine/creating-and-using-custom-heightmaps-and-layers-in-unreal-engine?application_version=5.7#heightmaps)

Related documents

[Editing Landscapes

![Editing Landscapes](https://dev.epicgames.com/community/api/documentation/image/90239937-9e2b-4683-9aae-1d7f10792ba9?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/editing-landscapes-in-unreal-engine)

[Landscape Paint Mode

![Landscape Paint Mode](https://dev.epicgames.com/community/api/documentation/image/0e0cd66b-96d3-4784-a8f4-7794f83599d5?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/landscape-paint-mode-in-unreal-engine)

[Creating Landscapes

![Creating Landscapes](https://dev.epicgames.com/community/api/documentation/image/a0c769f9-1e24-49f9-a3a7-131bdd695011?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/creating-landscapes-in-unreal-engine)
