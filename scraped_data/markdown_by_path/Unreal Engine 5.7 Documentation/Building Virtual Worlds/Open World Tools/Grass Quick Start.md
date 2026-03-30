<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/grass-quick-start-in-unreal-engine?application_version=5.7 -->

# Grass Quick Start

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
6. [Open World Tools](/documentation/en-us/unreal-engine/open-world-tools-in-unreal-engine "Open World Tools")
7. Grass Quick Start

# Grass Quick Start

Learn how to add Grass textures to a landscape.

![Grass Quick Start](https://dev.epicgames.com/community/api/documentation/image/6e92f126-ef1f-4ba5-a54a-a4ebb326260e?resizing_type=fill&width=1920&height=335)

 On this page

### Overview

In this Quick Start guide, we will take a look at how you can set up and apply a grass texture to a landscape.
Over the course of this Quick Start tutorial you will learn how to create, set up, and spawn static meshes to make your Landscape appear covered in thick grass.
You will be introduced to key properties and settings that will help you shape your virtual grasslands to fit your project's needs.

[![Grass Intro](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1d6fd83d-ce1b-450c-b9e4-7e2303b74364/01-t-grass-intro.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1d6fd83d-ce1b-450c-b9e4-7e2303b74364/01-t-grass-intro.png)

Click image for full size.

You will also learn about the Actors and properties required for a grassy-looking result to function correctly and deliver the results you want.
When you have completed this Quick Start, you will have a new level that should look similar to the image above.

Currently, the Grass system will only work with the Landscape Terrain Actor. Trying to use the Grass system to spawn grass on any other Actor type will not work.

## 1 - Prerequisites

Download the **Open World Demo Collection** content pack as some of the content from the collection will be used in the following Quick Start.
Once the Open World Demo Collection is downloaded, add it to the project that you are using to follow along with this Quick Start by doing the following:

1. From the Epic Games Launcher in either the **Learn** or **Marketplace** tab, locate and then download the **Open World Demo Collection**.

   [![Open World Demo Collection](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/df8c3aa4-8f1c-4c74-8896-dd4aefc0d13f/02-owdc-1.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/df8c3aa4-8f1c-4c74-8896-dd4aefc0d13f/02-owdc-1.png)

   Click image for full size.
2. Go the the **Library** section of the launcher and under **Vault** section locate the Open World Demo Collection.

   [![Open World Demo Collection](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6a08d967-ec49-4bfc-85fe-f0f73a0138d1/03-owdc-2.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6a08d967-ec49-4bfc-85fe-f0f73a0138d1/03-owdc-2.png)

   Click image for full size.
3. Click on the **Add to Project** button.

   [![Add to Project](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3a663a30-2f60-479c-8795-0b71be3c034f/04-add-to-project.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3a663a30-2f60-479c-8795-0b71be3c034f/04-add-to-project.png)

   Click image for full size.
4. A list of projects that you can add this to will appear. Select the project that you are using to follow along with this Quick Start and then press the **Add to Project** button.

   [![Select_Project](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d9828778-66a6-4d04-8807-439815ef88bb/05-select-project.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d9828778-66a6-4d04-8807-439815ef88bb/05-select-project.png)

   Click image for full size.

## 2 - Initial Level Setup

Now, we will create a new level and Landscape terrain so that we have something on which to apply the grass.

1. Create a new level that uses the blank **Default** template as a base.

   [![New Level](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ff1f512b-ec47-4a55-86c0-c0dc5d5b1978/06-t-new-level.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ff1f512b-ec47-4a55-86c0-c0dc5d5b1978/06-t-new-level.png)

   Click image for full size.
2. Add a new Landscape Actor to the level. In the Main Toolbar, click the **Modes** button, and select **Landscape** to display the Landscape panel and toolbar, and then click on the **Create** button.

   [![Create Landscape](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b617c3af-8519-4411-a4f1-be74286d0023/07-create-landscape.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b617c3af-8519-4411-a4f1-be74286d0023/07-create-landscape.png)

   Click image for full size.
3. To help better show off the Grass Tool, we are going to add a some noise to our Landscape terrain so it is not completely flat. In the **Landscape** toolbar **Sculpt** tab, click **Noise** from the tool list. Set the Noise properties with the following values.

   [![Sculpt Tool Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/576b0ec6-794a-4d1f-8363-6ac3bfeddb32/08-t-sculpt-tool-settings.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/576b0ec6-794a-4d1f-8363-6ac3bfeddb32/08-t-sculpt-tool-settings.png)

   Click image for full size.

   | Property Name | Value | Additional Details |
   | --- | --- | --- |
   | **Brush Size** | 65536.0 | This gives us a brush that is big enough to effect the entire Landscape terrain at once. |
   | **Tool Strength** | 0.01 | Since we only want a very subtle effect, set the Tool Strength very low and add more intensity by painting more. |
   | **Noise Scale** | 256 | Making the Noise Scale bigger makes the noise look smoother and more natural when applied to the Landscape. |
4. Position the Landscape Brush in the viewport so that it covers the entire Landscape terrain. Click the Left Mouse Button **3** to **4** times to add some very subtle noise to the Landscape terrain.
5. Exit Landscape mode. Click the **Modes** button, and choose **Select** to display the **Place Actors** panel.

   [![Place Actors](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/84e14c14-c574-4041-be78-6dc0a60f16b2/09-place-actors.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/84e14c14-c574-4041-be78-6dc0a60f16b2/09-place-actors.png)

   Click image for full size.

   When completed, you should have something that looks similar to the following image.

   [![Noise On Landscape](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/db41273c-34d4-4fd7-a64a-bfa3a15c985a/10-t-noise-on-landscape.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/db41273c-34d4-4fd7-a64a-bfa3a15c985a/10-t-noise-on-landscape.png)

   Click image for full size.

   The Grass system works on a completely flat Landscape terrain. The above modification to the Landscape was done purely for artistic reasons, to help show the final result.

## 3 - Grass Tool Actor Creation and Setup

We will create the required Actors and Materials the Grass Tool needs to function correctly.
We will continue to work with the the level that was created in the last step.

1. Create a Landscape Grass Type: **right-click** in the **Content Browser**. From the displayed context menu, go to **Foliage** > **Landscape Grass Type** and name it **Grass\_00**.

   [![Create LS Grass](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8aafca61-ef92-41fd-b8ee-1be2facc4d62/11-t-create-ls-grass.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8aafca61-ef92-41fd-b8ee-1be2facc4d62/11-t-create-ls-grass.png)

   Click image for full size.
2. Open up the Landscape Grass Type and add a new item to the **Grass Varieties** array: **double-click** on **Landscape Grass Type** and once opened, press the **Plus** icon that is to the right of the **Grass Varieties** name.

   [![Add_New Grass Varieties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ab4275ba-4bbb-41d2-8375-b2e3395b5dbd/12-t-add-new-gv.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ab4275ba-4bbb-41d2-8375-b2e3395b5dbd/12-t-add-new-gv.png)

   Click image for full size.
3. Inside of the **Landscape Grass Type** Actor look for the **Grass Mesh** section, click on the input box that says **None** and enter **SM\_FieldGrass\_01** as the search term, then click on the **SM\_FieldGrass\_01** to load it as the **Grass Mesh**.

   [![Set Grass Type](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7bc49406-a232-44c9-8e86-d39bbe426740/13-t-set-grass-type.gif)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7bc49406-a232-44c9-8e86-d39bbe426740/13-t-set-grass-type.gif)

   Click image for full size.
4. With the Static Mesh added we need to set the following properties to ensure that we are spawning enough grass mesh and that those meshes are randomly rotated and aligned to the Landscape terrain.

   [![Grass Props](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0c3dd204-eb79-4dfa-9563-0fe40d051bbf/14-t-grass-props.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0c3dd204-eb79-4dfa-9563-0fe40d051bbf/14-t-grass-props.png)

   Click image for full size.

   | Property Name | Value | Additional Details |
   | --- | --- | --- |
   | **Grass Density** | 400.0 | Because we want this to look like grass, we must spawn a lot of Static Meshes to make the Landscape appear densely covered in grass. |
   | **Use Grid** | Enabled | To make the Static Meshes look more naturally placed, this offset is their placement position. |
   | **Random Rotation** | Enabled | Giving the Static Meshes used for the plants and grasses a random rotation makes sure that the same side of the Static Mesh used is not seen all the time, adding to the visual variety of the scene. |
   | **Align to Surface** | Enabled | This makes sure that the Static Mesh used conforms to the surface of the Landscape terrain. |

## 4 - Landscape Materials and the Grass Tool

Before we can begin to use the Grass Tools we first have to create a Material that can work with both the Landscape terrain and the **Landscape Grass Type**.
We will cover how to set up this Material, as well as how to link it so that it will work with the Landscape Grass Type.

If you would like to have a more in-depth look at how the Landscape terrain works in UE5, refer to the [Landscape](/documentation/en-us/unreal-engine/landscape-outdoor-terrain-in-unreal-engine) pages for more information.

1. Create a new Material for our Landscape Terrain by **right-clicking** in the **Content Browser**, then selecting the **Material & Textures** option from the **Create Basic Asset** section, and name the new Material, **MAT\_GT\_Grass**.

   [![Create New Material](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/73c03ea3-a5e3-4a5b-a544-850c70e9d677/15-t-create-new-material.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/73c03ea3-a5e3-4a5b-a544-850c70e9d677/15-t-create-new-material.png)

   Click image for full size.
2. Open up the **MAT\_GT\_Grass** Material by **double-clicking** on the Material inside of the **Content Browser**, then add the following two Textures from the **Open World Demo Collection** to the Material Graph.

   * **T\_AlpinePatch001\_D\_alt\_R**
   * **T\_GDC\_Grass01\_D\_NoisyAlpha**

     [![Added Textures](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6d0aa90d-a88b-4639-b14c-dce081e7ce76/16-t-added-textures.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6d0aa90d-a88b-4639-b14c-dce081e7ce76/16-t-added-textures.png)

     Click image for full size.
3. Using the **Palette** search function, search for the Material Expression nodes listed below.
   Once you locate a required Material Expression node, select it in the Palette and then drag it into the Material Graph.

   | Material Expression Name | Amount | Additional Details |
   | --- | --- | --- |
   | **Landscape Layer Blend** | 1 | To make the Landscape terrain look more realistic you will often need to blend and paint multiple together or separately and that is what the Landscape Layer Blend allows you to do. |
   | **Landscape Layer Sample** | 1 | This Material Expression allows the Material and the Landscape to talk to one another to ensure the right Static Mesh is used whenever a certain Landscape layer is painted. |
   | **Landscape Grass Output** | 1 | This enables the Landscape terrain to be able to spawn the Grass Types based on the setup in the Landscape Material. |

   [![Add Material Nodes](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d0a41dba-e45f-4814-ad97-742984fc29d1/17-t-add-material-nodes.gif)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d0a41dba-e45f-4814-ad97-742984fc29d1/17-t-add-material-nodes.gif)

   Click image for full size.

   If you are unfamiliar with how the UE5 Material Editor works or would just like more information about it, check the official **[Unreal Engine Material documentation](/documentation/en-us/unreal-engine/unreal-engine-materials)** for more information on all things related to Materials.
4. Select the **Landscape Layer Blend** node and under the **Details** panel in the **Layers** section and add two new Layers to it by clicking the **Plus** icon 2 times.

   [![Landscape Layer Blend Add Layers](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0988fee2-fae3-41c4-851a-3f9df1fd9c17/18-t-lb-add-2-layers.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0988fee2-fae3-41c4-851a-3f9df1fd9c17/18-t-lb-add-2-layers.png)

   Click image for full size.
5. Once 2 layers have been added, set the **Layer Name** of one to **Grass** and set the **Layer Name** of the other one to **Rock** also setting the **Preview Weight** to **1.0** for each.

   [![LS Layer Blend Setup](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bfb60991-cfd0-4049-ad2e-fb77d1bd095f/19-t-ls-layer-blend-setup.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bfb60991-cfd0-4049-ad2e-fb77d1bd095f/19-t-ls-layer-blend-setup.png)

   Click image for full size.
6. Connect the **T\_AlpinePatch001\_D\_alt\_R** Texture to the **Layer Rock** input on the **Landscape Layer Blend** node then connect the **T\_GDC\_Grass01\_D\_NoisyAlpha** to the **Layer Grass** input finally connect the **Output** of the **Landscape Layer Blend** node into the **Base Color** input on the Main Material Node, **Mat\_GT\_Grass**.

   [![Hook Up Textures](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ecf091c3-056c-4da2-920c-77c424a025e5/20-t-hook-up-textures.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ecf091c3-056c-4da2-920c-77c424a025e5/20-t-hook-up-textures.png)

   Click image for full size.
7. In the **Content Browser**, select the **Grass\_00** Landscape Grass Type that was created in the last step.
8. In the **Material** under the **Grass Type** option, press the **Arrow** icon to load the Actor that is currently selected in the Content Browser.

   [![Input Grass Type](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/61385bb3-407d-493c-a8ed-2f8d960de652/21-t-input-grass-type.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/61385bb3-407d-493c-a8ed-2f8d960de652/21-t-input-grass-type.png)

   Click image for full size.
9. Select the **Landscape Layer Sample** node under the **Parameter Name** input **Grass** for the name and connect the Output from the **Landscape Layer Sample** to the input of the **Landscape Grass Output** node.

   [![Landscape Layer Weight Setup](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/20da95be-2422-41a6-b7d8-c20fb1e5ed0c/22-t-llw-setup.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/20da95be-2422-41a6-b7d8-c20fb1e5ed0c/22-t-llw-setup.png)

   Click image for full size.
10. When completed you should have a Material that looks like the following. As always, do not forget to press the **Apply** and **Save** buttons to compile and save the Material.

    [![Final Material](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/52224392-ad9f-42c6-a408-7e8718dc5443/23-t-final-material.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/52224392-ad9f-42c6-a408-7e8718dc5443/23-t-final-material.png)

    Click image for full size.

## 5 - Using the Grass Tools

In order to see the Grass system in action, we need to apply the Material that was created in the last step to the Landscape and then use the Landscape painting tools to define where we want the grass to be spawned.
In the following section, we will go over how to apply our Material to the Landscape Terrain, then how to use the Landscape Painting Tools to define areas where grass should spawn.
We will continue to work in the level that was created in the last step.

1. Select the Landscape Actor that was placed in the level by clicking on it in the viewport.

   [![Selected Landscape](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3351f509-d7d6-4c2a-a3b6-9cde271791dd/24-t-selected-landscape.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3351f509-d7d6-4c2a-a3b6-9cde271791dd/24-t-selected-landscape.png)

   Click image for full size.
2. Locate the **MAT\_GT\_Grass** Material in the **Content Browser** and click on it to select it.
3. On the Landscape Terrain under the **Details** panel in the **Landscape Material** section, press the **Arrow** icon to apply the **MAT\_GT\_Grass** Material to the Landscape Terrain.

   [![Apply Material](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5a45f9a6-a1f0-4719-a414-5f7e43d31ab8/25-t-apply-material.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5a45f9a6-a1f0-4719-a414-5f7e43d31ab8/25-t-apply-material.png)

   Click image for full size.
4. In the **Main Toolbar**, click the **Modes** button, select **Landscape** mode. From the **Landscape** toolbar, click on the **Paint** tab to go into **Paint** mode.

   [![Landscape Paint Mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bbaddd01-2c23-4aa4-a440-5e39b96c8f6c/26-t-landscape-paint-mode.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bbaddd01-2c23-4aa4-a440-5e39b96c8f6c/26-t-landscape-paint-mode.png)

   Click image for full size.

   [![Landscape Paint Mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0203687e-2991-4612-8616-11db562aec12/27-t-landscape-paint-mode-1.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0203687e-2991-4612-8616-11db562aec12/27-t-landscape-paint-mode-1.png)

   Click image for full size.
5. Under the **Target Layers** section, add a new **Layer Info** by pressing the **Plus** icon on the far right of the layer name.

   [![Add Target Layers](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d89627bc-7365-4b6e-a68d-afd69da62278/28-t-add-target-layers.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d89627bc-7365-4b6e-a68d-afd69da62278/28-t-add-target-layers.png)

   Click image for full size.
6. When prompted, select the **Weight-Blended Layer (normal)** option, then select a location to save the new Layer Blend in the Content Browser.
   Make sure that you create **Layer Info** for both the Rock and the Grass.
7. Select the **Grass** Target Layer, then hold down the **Left Mouse Button** inside the viewport to begin painting the Grass Material to the Landscape Terrain.
   For this step, try to completely cover the Landscape, giving you results that look like this.

   [![Painting Grass](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/88aba9d3-057f-412e-a67f-2316b838f945/29-t-painting-grass-2.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/88aba9d3-057f-412e-a67f-2316b838f945/29-t-painting-grass-2.png)

   Click image for full size.

   Depending on the power of your development PC, when you start to paint on the Landscape the editor might become unresponsive as the grass is spawned.
   This is normal behavior as the grass is dynamically spawned after you have finished painting.
   Turning down the **Grass Density** in the **Landscape Grass Type** while working, then putting it back up to the desired level when done, is a great way to help mitigate this as much as possible.
8. To remove grass from the Landscape Terrain, select the Rock Target Layer then inside of the viewport hold down the **Left Mouse button** to begin replacing the grass Texture with the rock Texture.

   Adjusting the **Brush Size** and **Tool Strength** will help to better define how the grass is placed or removed while painting on the Landscape.

## 6 - On Your Own

Now that you have seen the power that the Grass tool offers, try using the tools listed below in conjunction with what you have just learned to make a level that looks like the following image:

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3e2551d2-366a-45d2-82d2-98fe8522fc1c/44-t-on-your-own.png "On Your Own")

* Use the [Procedural Foliage Tool](/documentation/en-us/unreal-engine/procedural-foliage-tool-in-unreal-engine) Tool to make the Landscape look like it is densely covered in grass, flowers and bushes.
* Define the look and feel of the Landscape terrain using the **[Landscape Sculpt](/documentation/en-us/unreal-engine/landscape-sculpt-mode-in-unreal-engine)** tools to add features such as hills, mountains and lakes.
* Give the surface of the Landscape more visual variety and detail by creating a [Landscape Material](/documentation/en-us/unreal-engine/landscape-materials-in-unreal-engine) that has multiple Textures that can be painted on the Landscape terrain.
* Adjust the **[Directional Light](/documentation/en-us/unreal-engine/directional-lights-in-unreal-engine)** to make the level lighting resemble lighting that happens in the early morning or late afternoon.
* Set up the level lighting to use a completely dynamic based lighting solution that will make use of dynamic shadows as well as **[Ray Traced Distance Field Soft Shadows](/documentation/en-us/unreal-engine/distance-field-soft-shadows-in-unreal-engine)**.
* Try using the [Foliage System](/documentation/en-us/unreal-engine/foliage-mode-in-unreal-engine) tools to remove or tweak the placement, rotation and scale of the Foliage meshes that are placed by the Procedural Foliage tool so that you can get the exact look you are going for.
* Show off your creation to others by using a [Camera](/documentation/en-us/unreal-engine/camera-actors-in-unreal-engine) in conjunction with [Sequencer](/documentation/en-us/unreal-engine/real-time-compositing-with-sequencer-in-unreal-engine) to render out a video of your level for you to share with the world.

* [landscape](https://dev.epicgames.com/community/search?query=landscape)
* [building virtual worlds](https://dev.epicgames.com/community/search?query=building%20virtual%20worlds)
* [open world](https://dev.epicgames.com/community/search?query=open%20world)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Overview](/documentation/en-us/unreal-engine/grass-quick-start-in-unreal-engine?application_version=5.7#overview)
* [1 - Prerequisites](/documentation/en-us/unreal-engine/grass-quick-start-in-unreal-engine?application_version=5.7#1-prerequisites)
* [2 - Initial Level Setup](/documentation/en-us/unreal-engine/grass-quick-start-in-unreal-engine?application_version=5.7#2-initiallevelsetup)
* [3 - Grass Tool Actor Creation and Setup](/documentation/en-us/unreal-engine/grass-quick-start-in-unreal-engine?application_version=5.7#3-grasstoolactorcreationandsetup)
* [4 - Landscape Materials and the Grass Tool](/documentation/en-us/unreal-engine/grass-quick-start-in-unreal-engine?application_version=5.7#4-landscapematerialsandthegrasstool)
* [5 - Using the Grass Tools](/documentation/en-us/unreal-engine/grass-quick-start-in-unreal-engine?application_version=5.7#5-usingthegrasstools)
* [6 - On Your Own](/documentation/en-us/unreal-engine/grass-quick-start-in-unreal-engine?application_version=5.7#6-onyourown)
