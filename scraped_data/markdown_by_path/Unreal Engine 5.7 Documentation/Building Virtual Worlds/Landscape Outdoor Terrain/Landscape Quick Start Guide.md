<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-quick-start-guide-in-unreal-engine?application_version=5.7 -->

# Landscape Quick Start Guide

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
7. Landscape Quick Start Guide

# Landscape Quick Start Guide

Getting up and running with the basics of the Landscape System in Unreal Engine.

![Landscape Quick Start Guide](https://dev.epicgames.com/community/api/documentation/image/20274db9-029b-402e-a249-ddff42633cd9?resizing_type=fill&width=1920&height=335)

 On this page

The Unreal Editor Landscape Quick Start Guide walks you through creating a new Landscape, sculpting the Landscape, creating new Materials for the Landscape, and painting those Materials on the Landscape.

## 1 - Working with the Landscape Tools

The **Landscape** system inside of Unreal Engine 5 (UE5) is a collection of tools that provide ways for you to create expansive outdoor environments. But before we dive into creating our first Landscape, let us first familiarize ourselves with some of the tools and keyboard inputs that are most commonly used to interact with the Landscape system.

### Opening the Landscape Tool and Working with Modes

All of the tools that are used to interact with the Landscape system can be found under the **Landscape** option that is located in the **Modes** dropdown menu. To enable the Landscape tools, open the Modes dropdown and choose the option from the menu.

The Landscape tool has three modes, **Manage**, **Sculpt**, and **Paint,**accessible by clicking on their icons at the top of the Landscape's toolbar window. Each mode provides different methods for you to interact with the Landscape. Here is a very quick rundown of what you can do with each mode.

[![Landscape Mode](https://dev.epicgames.com/community/api/documentation/image/1be23ccb-39e4-4eb8-bdfa-30f811bd3677?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1be23ccb-39e4-4eb8-bdfa-30f811bd3677?resizing_type=fit)

| Icon | Mode | Description |
| --- | --- | --- |
| [Manage mode](https://dev.epicgames.com/community/api/documentation/image/e3a9361d-8795-410f-a9f6-b083217f2a6c?resizing_type=fit) | Manage mode | Create new Landscapes, and modify Landscape components. Manage mode is also where you work with [Landscape Copy Tool](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-copy-tool-in-unreal-engine) to copy, paste, import, and export parts of your Landscape. For more information about Manage mode, refer to [Landscape Manage Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-manage-mode-in-unreal-engine). |
| [Sculpt mode](https://dev.epicgames.com/community/api/documentation/image/0a1c9648-e916-497e-9e10-dc8403ef16e2?resizing_type=fit) | Image mode | Modify the shape of your Landscape by selecting and using specific tools. For more information about Sculpt mode, refer to [Landscape Sculpt Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-sculpt-mode-in-unreal-engine). |
| [Image mode](https://dev.epicgames.com/community/api/documentation/image/d752bec0-5759-4af7-aa10-edd5a43077ad?resizing_type=fit) | Sculpt mode | Modify the appearance of parts of your Landscape by painting textures on it, based on the layers defined in the Landscape's Material. For more information about Paint mode, refer to [Landscape Paint Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-paint-mode-in-unreal-engine). |

### Interacting with the Landscape Tools

While each of the three modes within the Landscape tools allows you to interact with the Landscape differently, but the keyboard and mouse keys that you use are similar. Here is a rundown of some of the most common keys, key combinations, and mouse buttons that are used when working with the Landscape tool.

| Common Controls | Operation |
| --- | --- |
| **Ctrl** | Selects Landscape components. |
| **Left Mouse Button (LMB)** | Heightens or increases the heightmap or selected layer's weight. For example, in Sculpting mode, this raises the Landscape heighmap. In Paint mode this applies the selected material to the Landscape. |
| **Shift + LMB** | Lowers or decreases the heightmap or selected layer's weight. For example, in Sculpting mode, this lowers the Landscape heightmap. In Paint mode, this erases the selected material that was applied to a particular section of the Landscape. |
| **Ctrl + Z** | Undoes last action. |
| **Ctrl + Y** | Redoes last undone action. |

## 2 - Creating a new Landscape

Before we begin to create our first Landscape, lets create a new project **First Person** Project.

If you are unfamiliar with how to create a new project, check out the following page on [Creating a New Project](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-a-new-project-in-unreal-engine).

### Creating a Landscape

1. First, create a new **First Person** project if you have not done so already.

   While you can use other templates for this tutorial, the First Person will make it a little easier to inspect your Landscape. After choosing the First Person option, click the **Next** button.

   [![Create a First Person project](https://dev.epicgames.com/community/api/documentation/image/2f8d1725-6e34-4787-a03a-29f9ad6a31aa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2f8d1725-6e34-4787-a03a-29f9ad6a31aa?resizing_type=fit)

   Click image for full size.
2. Make sure your project is set up to use Blueprints and contains the Starter Content folder. Choose a location where your project will be stored on your computer and make sure it has a proper name. Finally, click the **Create Project** button to continue.

   [![Choose project settings and create the project](https://dev.epicgames.com/community/api/documentation/image/9a1e38d3-54d5-430f-9f94-3edaa29a68d4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9a1e38d3-54d5-430f-9f94-3edaa29a68d4?resizing_type=fit)

   Click image for full size.
3. After you create your new project and the editor loads, create a new level using **File > New Level** and select the **Default** Level from the New Level Template.

   [![Create a Default new level](https://dev.epicgames.com/community/api/documentation/image/67c86646-115a-4a37-b7d2-0ed553e440c2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/67c86646-115a-4a37-b7d2-0ed553e440c2?resizing_type=fit)

   Click image for full size.
4. With your new level now created, select the **Floor** from the level and press the **Delete** key to remove it from the level.

   Make sure that you select your player start and move it up slightly in the Z-axis. This will make sure that your player does not start under your newly created Landscape.

   Once completed, you should now have something that looks similar to the following image.

   [![New level in your project](https://dev.epicgames.com/community/api/documentation/image/0ea60d7d-2750-4282-ae87-a49bdfd6cecc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0ea60d7d-2750-4282-ae87-a49bdfd6cecc?resizing_type=fit)

   Click image for full size.
5. With the level cleared out and the player start moved up in the Z-axis slightly, it is now time to create a new Landscape. To create a new Landscape, click on the **Landscape** option in the **Modes** dropdown menu.

   [![Select Landscape in the Modes menu](https://dev.epicgames.com/community/api/documentation/image/b95a44f0-f630-4954-85a7-d179ed003a22?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b95a44f0-f630-4954-85a7-d179ed003a22?resizing_type=fit)

   Click image for full size.
6. After you click on the Landscape option, you will see the following set of Landscape tools displayed in the **Landscape** panel.

   [![Landscape tools](https://dev.epicgames.com/community/api/documentation/image/364720ae-5231-4dc8-87a3-d12f61e530c1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/364720ae-5231-4dc8-87a3-d12f61e530c1?resizing_type=fit)

   Click image for full size.
7. For this tutorial, we will just focus on creating a Landscape using the default settings.
   If you would like to know more about the various settings in the Manage mode of the Landscape tool, please refer to [Creating Landscapes](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-landscapes-in-unreal-engine).
   For now, make sure that your settings match the image below and then press the **Create** button to create the Landscape.

   [![Create the Landscape](https://dev.epicgames.com/community/api/documentation/image/2499f5e5-3a15-43fa-8a81-fa7736297cee?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2499f5e5-3a15-43fa-8a81-fa7736297cee?resizing_type=fit)

   Click image for full size.

   When done, you should have something that looks like this.

   [![Creating a Landscape](https://dev.epicgames.com/community/api/documentation/image/78dda1cb-d1b0-4916-b196-8973f7f99c7c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/78dda1cb-d1b0-4916-b196-8973f7f99c7c?resizing_type=fit)

   Click image for full size.

### 3 - Sculpting the Landscape

Sculpting the **Landscape** is a time-consuming process. You can find all of the tools used for sculpting under the **Sculpt**
tab in the Landscape toolbar. If you would like to know more about what
each of the Sculpting Tools does in detail, take a look at the [Sculpt Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-sculpt-mode-in-unreal-engine)
page. For  a list of the most common key and
mouse interactions that are used when sculpting the Landscape, refer to the [Interacting with the Landscape Tools](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-quick-start-guide-in-unreal-engine#nbsp-interacting-with-the-landscape-tools) section above.

For this part of the Landscape tutorial, you are going to start with a completely flat section of the Landscape and then build up the details as you go along. The goal here is not to exactly mimic what was created in the tutorial but to get you familiar and comfortable with using the various Landscape tools.

There are a variety of reasons why what you do in this tutorial does not come out exactly the same as what you see in the following screen shots. Working with the Landscape tools requires a lot of trial and error so your results will vary, sometimes greatly, from what you see in the following set of images. The most important thing to get out of this tutorial is to understand how each of the Landscape tools operates and how all the tools work together to give you the final product.

1. To begin, find a section of the Landscape that you want to work with.
   For this tutorial, you are not going to be filling in the entire Landscape but just a section of it.
   For ease of use, set a camera bookmark by pressing **Ctrl + 1**
   on the keyboard.
   This sets a camera bookmark which makes it easier for you to
   gauge how your Landscape is coming along by giving you a camera view to
   always come back to.
   At any time during your editor session, if you press the 1 key, your
   camera will return to the exact same position that you set.

   [![Find a Landscape section to work with](https://dev.epicgames.com/community/api/documentation/image/4193a8de-aa63-4173-8e3e-12751c0efafe?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4193a8de-aa63-4173-8e3e-12751c0efafe?resizing_type=fit)

   Click image for full size.
2. With the bookmark set, begin painting in the larger details for hills and valleys using the **Sculpt Tool**.
   You can find the brush size and strength settings that were used for
   this step listed below and when completed, you should have something
   that looks like the following. You can change the value of the Brush
   Size and Strength either in the Landscape panel or the Landscape toolbar
   located just above the viewport.

   | Tool Used | Brush Size | Strength Setting |
   | --- | --- | --- |
   | **Sculpt Tool** | 8192 | 0.29 |

   [![Sculpting hills and valleys](https://dev.epicgames.com/community/api/documentation/image/3371599f-a9d7-458f-a745-2c4a4e1acdc3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3371599f-a9d7-458f-a745-2c4a4e1acdc3?resizing_type=fit)

   Click image for full size.
3. After you block out the the hills and valleys, use the **Smooth Tool** to help refine the look and feel of them. Using this tool smooths your **Landscape**
   features and make them seem more natural. Be careful not to smooth away
   all your features!
   You can find the brush size and strength settings that were used for
   this step listed below and when completed, you should have something
   that looks like the following.

   | Tool Used | Brush Size | Strength Setting |
   | --- | --- | --- |
   | **Smooth Tool** | 2048 | 0.29 |

   [![Smoothing your Landscape](https://dev.epicgames.com/community/api/documentation/image/4611dda3-bcb6-4eb9-bfd2-10378d9450a0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4611dda3-bcb6-4eb9-bfd2-10378d9450a0?resizing_type=fit)

   Click image for full size.
4. Now that you smoothed out the Landscape, it is time to add some flat mesa like sections using the **Flatten Tool**.
   The Flatten Tool captures the height information of the location of
   your first click and raises/lowers the heightmap to meet that point as
   you drag around the brush.
   You can find the brush size and strength settings that were used for
   this step listed below and when completed, you should have something
   that looks like the following.

   | Tool Used | Brush Size | Strength Setting |
   | --- | --- | --- |
   | **Flatten Tool** | 2048 | 0.29 |

   [![Flatten you Landscape](https://dev.epicgames.com/community/api/documentation/image/a98524a6-eb89-42e9-abc4-2b3561b28c9a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a98524a6-eb89-42e9-abc4-2b3561b28c9a?resizing_type=fit)

   Click image for full size.
5. It is time to use the **Ramp Tool** to add some flat ramps
   between the mesas. This tool works by designating a start point and an
   end point for your ramp and then clicking the **Add Ramp**
   button to create a flat path between the two points. Each point can be
   moved any direction to create a ramp that fits each unique situation.
   You can find the brush size and strength settings that were used for
   this step listed below and when completed, you should have something
   that looks like the following.
   If it is not very clear where the Ramp was used, it has been highlighted
   in yellow.

   | Tool Used | Ramp Width | Side Falloff |
   | --- | --- | --- |
   | **Ramp Tool** | 2000 | 0.40 |

   [![Creating Ramps in your Landscape](https://dev.epicgames.com/community/api/documentation/image/6bcf3a7a-9216-4731-bef4-aab9d2374fcb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6bcf3a7a-9216-4731-bef4-aab9d2374fcb?resizing_type=fit)

   Click image for full size.
6. Next, add some erosion effects to the Landscape to give it a weathered look using the **Erosion Tool**
   which works by simulating erosion done by wind. This tool is perfect
   for shaving away parts of your hills to create mountain peaks and
   ridges.
   You can find the brush size and strength settings that were used for
   this step listed below and when completed, you should have something
   that looks like the following.

   | Tool Used | Brush Size | Strength Setting |
   | --- | --- | --- |
   | **Erosion Tool** | 693 | 0.25 |

   [![Erode your Landscape](https://dev.epicgames.com/community/api/documentation/image/226f47a5-6a7c-4364-a830-031ca565bc5e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/226f47a5-6a7c-4364-a830-031ca565bc5e?resizing_type=fit)

   Click image for full size.
7. In the next step, you will take the erosion that was just added in the
   previous step and push it further by adding some Hydro Erosion to the
   Landscape.
   The **Hydro Erosion Tool** is different from the Erosion Tool as it is for simulating how water will erode Landscape details over time. Like the **Smooth Tool**,
   be careful not to erode away all your detail.
   You can find the brush size and strength settings that were used for
   this step listed below and when completed, you should have something
   that looks like the following.

   | Tool Used | Brush Size | Strength Setting |
   | --- | --- | --- |
   | **Hydro** **Erosion** | 2048 | 0.29 |

   [![Using Hydro Erosion on your Landscape](https://dev.epicgames.com/community/api/documentation/image/122edb88-4ea0-4749-82ba-5475b443e101?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/122edb88-4ea0-4749-82ba-5475b443e101?resizing_type=fit)

   Click image for full size.
8. To break up the surface of the Landscape even more, use the **Noise Tool**.
   The Noise Tool adds random noise to the surface of the Landscape by
   randomly moving the Landscape vertices up or down or both at the same
   time.
   You can find the brush size and strength settings that were used for
   this step listed below and when completed, you should have something
   that looks like the following.

   | Tool Used | Brush Size | Strength Setting |
   | --- | --- | --- |
   | **Noise** **Tool** | 2048 | 0.29 |

   [![Using the Noise Tool on your Landscape](https://dev.epicgames.com/community/api/documentation/image/fb76451a-c0d0-4b7a-97dd-0ca22d38b4b4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fb76451a-c0d0-4b7a-97dd-0ca22d38b4b4?resizing_type=fit)

   Click image for full size.
9. For the final step in the Landscape sculpting part of the tutorial, re-use the **Smooth Tool**
   to help smooth out some of the more jagged areas of the Landscape to
   give it a more natural look.
   While you might not need to do this step yourself, in the tutorial this was done to help
   even out some of the areas that appear too deep or areas that the
   player might get stuck in if they fall into. You can find the brush size
   and strength settings that were used for this step listed below and
   when completed, you should have something that looks like the following.

   | Tool Used | Brush Size | Strength Setting |
   | --- | --- | --- |
   | **Smooth Tool** | 1121 | 0.16 |

## 4 - Creating Landscape Materials

### Folder Setup

After you finish sculpting the Landscape, you can now add some Materials to it so that it better resembles something that we see in the real world. But before you do this, you need to first set up some folders to organize the content that you create and migrate into your project.

If you want to know more about how to setup folders in Unreal Engine 5, please refer to the following page about [Folders](https://dev.epicgames.com/documentation/en-us/unreal-engine/sources-panel-reference-in-unreal-engine).

1. Start by creating a new folder called **Landscape** in your project's **Content** folder.
2. Then inside the Landscape folder, create the following three folders:

   * Materials
   * Resources
   * Textures

When completed, you should have something that looks like the following.

[![Setting up your project folders](https://dev.epicgames.com/community/api/documentation/image/164d8cf3-ae0e-4a9a-abe8-ca2477c8e634?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/164d8cf3-ae0e-4a9a-abe8-ca2477c8e634?resizing_type=fit)

Click image for full size.

### Migrating Textures

Now that you have the folders in place, it is time to migrate some textures from the **Landscape Mountains**
learning project so that you have some textures to work with. You can find this
project on Fab in the Epic Games Launcher, or on the Fab website. If
you want to know more about how to Migrate content from one
project to another one, please check out the following page on how to [Migrate Content](https://dev.epicgames.com/documentation/en-us/unreal-engine/sources-panel-reference-in-unreal-engine).

When Migrating content between projects, you could possibly end up with additional folders that you do not want.
To fix this, select the Textures that you want inside of the **Content Browser** and then drag them from their current location into the folder that you want them to be placed in.
This is purely a house keeping step and will have no impact on the outcome of the tutorial.

You can find the textures located in the following folder located in the Landscapes Content example project.

`/Game/ExampleContent/Landscapes/Textures/`

The Textures that you will migrate over from the **Landscape Content Example** project are as follows.

* **T\_LS\_Grass\_01\_D**
* **T\_LS\_Grass\_01\_N**
* **T\_FullGrass\_D**
* **T\_FullGrass\_N**
* **T\_IceNoise\_N**

When you migrate the textures over, place them in the **Textures** folder you created in the steps above.

### Creating the Landscape Material

You can create a material for your Landscape by following these steps.

1. Navigate to the **Materials** folder in the **Content Broswer**.
2. **Right-click** in the **Content Browser** and select **Material** from the **Create Basic Asset** list.
3. Name the newly-created material something that will help you to easily find it, like `Landscape_Material` for example.

If you have not already done so, please check out the [Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-materials) pages to gain a more in-depth understanding of how materials work inside of Unreal Engine 5.

When this is complete, you will have something that looks like this:

[![Your new material in the Content Browser](https://dev.epicgames.com/community/api/documentation/image/6645429f-f31c-4310-b7a6-1ac2fedd5521?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6645429f-f31c-4310-b7a6-1ac2fedd5521?resizing_type=fit)

Click image for full size.

With your new Landscape material created, open up the material by **double-clicking** on it inside of the **Content Browser**. When you do, you will see something like this come up on the screen:

[![Landscape material in the editor](https://dev.epicgames.com/community/api/documentation/image/316f22f9-ba31-4d54-86b0-24985c059f5d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/316f22f9-ba31-4d54-86b0-24985c059f5d?resizing_type=fit)

Click image for full size.

It is time to start adding nodes inside of the Material Editor.
The first node that you are going to create is a **LandscapeLayerCoords** UV node. This node helps to generate UV coordinates  used to map the Landscape Material to the Landscape Actor.

[![Landscape Layer Coordinates UV node](https://dev.epicgames.com/community/api/documentation/image/e45a6ae2-77ee-49da-9d71-f6b20679219c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e45a6ae2-77ee-49da-9d71-f6b20679219c?resizing_type=fit)

Click image for full size.

The quickest way to find nodes specific to Landscape is to search for them in the Materials **Palette** box using Landscape as the key word.

[![Landscape material search](https://dev.epicgames.com/community/api/documentation/image/6afbe679-8530-4147-a9d4-25330087f56a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6afbe679-8530-4147-a9d4-25330087f56a?resizing_type=fit)

Click image for full size.

The next Material nodes that you are going to add are for the textures for the ground's **Base Color** and **Normal** maps.

* For the snow, we are just going to use a **Vector Parameter** (**V + Left-click**) that uses an off White color.
* To make sure that no **Metallic** information is used, a **Constant** (**1 + Left-click**) of 0 is used and plugged into the **Metallic** input.
* For the **Roughness**, set a **Scalar Parameter** (**S + Left-click**) so that this value can be tweaked using a **Material Instance**.
* Finally, make sure that you connect the **LandscapeCoords** to the UV's of each of the **Texture Samples**.

When completed, your node network should look like this:

[![Landscape materials](https://dev.epicgames.com/community/api/documentation/image/0f8d4052-cff5-4aac-a437-1e2daaba7d9a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0f8d4052-cff5-4aac-a437-1e2daaba7d9a?resizing_type=fit)

Click image for full size.

To add the **Texture Sample** nodes for the various textures, select the desired texture in the **Content Browser** and then press **T + Left-click** in the **Material Editor**'s graph to create the node.

To find more information about these keybindings, take a look at the **Edit > Editor Preferences > Keyboard Shortcuts** window and select the **Material Editor - Spawn Nodes** section.

| Number | Texture Name |
| --- | --- |
| **1** | T\_LS\_Grass\_01\_D |
| **2** | T\_FullGrass\_D |
| **3** | T\_LS\_Grass\_01\_N |
| **4** | T\_FullGrass\_N |
| **5** | T\_IceNoise\_N |

After you add the Material nodes and connect the **LandscapeCoords** to the textures UVs, it is time to add and setup the **Landscape Layer Blend** node. The **Landscape Layer Blend**
node  blends layers using Weight blending, Height
blending, or Alpha blending.

* **Weight blending** uses each layer's painted weight to determine which to display. Use Weight blending where you want two surfaces to blend seamlessly into each other, such as rock into sand.
* **Height blending** uses the same weight information along with an additional height value taken from the Texture Sample's Alpha channel and is best used when you want one material to clearly sit on top of another, such as the Grass and Snow sitting on top of the Soil layer.
* **Alpha blending** uses the painted weight information with an Alpha layer to determine the final result.

When you first place down a **Landscape Layer Blend** node, it will be blank like in the image below labeled one. To add **Layers**, you need to select the node in the **Material Graph** and then in the **Details** panel, click on the **Plus** icon that is in-between the word **Elements** and the **Trash Can**
icon. This icon is highlighted yellow in the image labeled two. How
many textures you are using will determine how many Layers you will want
to have.

[![Landscape Layer Blend node](https://dev.epicgames.com/community/api/documentation/image/aa320588-8c83-48f4-83c7-c2260bf8146e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/aa320588-8c83-48f4-83c7-c2260bf8146e?resizing_type=fit)

[![Landscape adding layers to node](https://dev.epicgames.com/community/api/documentation/image/12fd8238-1dce-4d92-803a-d799d040cc9a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/12fd8238-1dce-4d92-803a-d799d040cc9a?resizing_type=fit)

The following table shows what **Textures** are associated with which **Layer Name** and what **Blend Type** they use.

#### Layer Blend Base Color

| Texture | Layer Name | Blend Type | Preview Weight |
| --- | --- | --- | --- |
| T\_LS\_Grass\_01\_D | Soil | LB Weight Blend | 1.0 |
| T\_FullGrass\_D | Grass | LB Height Blend | 0.0 |
| Snow as a Vector 3 | Snow | LB Height Blend | 0.0 |

[![Landscape layer blend](https://dev.epicgames.com/community/api/documentation/image/73add926-8d59-4b9d-a552-2a09b3e7a926?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/73add926-8d59-4b9d-a552-2a09b3e7a926?resizing_type=fit)

Click image for full size.

#### Layer Blend Normal

| Texture | Layer Name | Blend Type | Preview Weight |
| --- | --- | --- | --- |
| `T_LS_Grass_01_N` | Soil | LB Weight Blend | 1.0 |
| `T_FullGrass_N` | Grass | LB Weight Blend | 0.0 |
| `T_IceNoise_N` | Snow | LB Weight Blend | 0.0 |

[![Layer Blend Normal](https://dev.epicgames.com/community/api/documentation/image/9cfd4325-6d24-4297-94c1-807517d00782?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9cfd4325-6d24-4297-94c1-807517d00782?resizing_type=fit)

Click image for full size.

For more in-depth information about using the **Landscape Layer Blend** node or to troubleshoot any issues, please read the [Landscape Material Expressions](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-material-expressions-in-unreal-engine) page.

After you set up the **Layer Blend** nodes up, connect the Texture maps to them. Height blended materials have
both a Layer connection and a Height connection to accommodate the need
for the additional height information. When completed, you should have
something that looks like the following.

[![Landscape material final](https://dev.epicgames.com/community/api/documentation/image/e9fcf0b6-a718-4e07-a369-5ca57a71b1ee?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e9fcf0b6-a718-4e07-a369-5ca57a71b1ee?resizing_type=fit)

Click image for full size.

The material connections were colored in Photoshop to help better illustrate where everything needed to be connected. Currently there is no way to change the color of lines connecting Material nodes inside of Unreal Engine 5.

## 5 - Painting Landscape Materials

With your Landscape material created, you can now apply the material to the Landscape and begin using the Paint tools.

### Landscape Painting Prep

Before you can begin painting the Landscape, there is some setup you need to do first. Start by applying your Landscape material to the Landscape:

1. Find your material in the **Content Browser**. This should be located under a folder labeled **Materials** you created in the previous section. Click on it to select it.

   [![Find your material](https://dev.epicgames.com/community/api/documentation/image/3f273d8e-b816-4a43-8f35-f6339542da75?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3f273d8e-b816-4a43-8f35-f6339542da75?resizing_type=fit)

   Click image for full size.
2. With the Landscape material selected in the **Content Browser**, select the Landscape in the world. Then in the **Details** panel, expand the **Landscape** section and look for the **Landscape Material** input.

   [![Landscape material input](https://dev.epicgames.com/community/api/documentation/image/96ac8af0-c6df-4235-8566-82415b751144?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/96ac8af0-c6df-4235-8566-82415b751144?resizing_type=fit)

   Click image for full size.
3. Apply the Material to the Landscape using the **Use Selected Asset from the Content Browser** arrow icon. You can also drag the Material asset from the **Content Browser** to the **Details** panel and drop it on the **Landscape Material** input.

   [![Apply the material to the Landscape](https://dev.epicgames.com/community/api/documentation/image/36c8a78d-bbfc-4dbe-a184-d2ec555b4bfe?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/36c8a78d-bbfc-4dbe-a184-d2ec555b4bfe?resizing_type=fit)

   Click image for full size.
4. When completed, you should have something that looks like this:

   [![Landscape with material applied](https://dev.epicgames.com/community/api/documentation/image/1a514878-5b99-46b6-9831-19ec0dacaa56?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1a514878-5b99-46b6-9831-19ec0dacaa56?resizing_type=fit)

   Click image for full size.

   If you see black lines in your Landscape, this is due to lighting that is not built. If you rebuild your level's lighting, the black lines will go away.

Now that you applied the Landscape Material, you are almost ready to stat
painting. Before you can do so, you must first create and assign
three **Landscape Layer Info Objects**. If you try to paint before you assign the **Landscape Layer Info Objects**, you get the following warning message.

[![Layer info warning message](https://dev.epicgames.com/community/api/documentation/image/94098f58-91f7-469e-a870-c9cf3f309d37?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/94098f58-91f7-469e-a870-c9cf3f309d37?resizing_type=fit)

Click image for full size.

You need to create three **Landscape Layer Info Objects**, one for each Texture that you want to paint. Here is how you do it:

1. First, make sure that you are in **Landscape Paint** mode.

   [![Landscape paint mode](https://dev.epicgames.com/community/api/documentation/image/fcc84f63-10e6-4520-b399-a0c11fa419e5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fcc84f63-10e6-4520-b399-a0c11fa419e5?resizing_type=fit)

   Click image for full size.
2. In the Landscape panel, under the **Target Layers** section, you should see three inputs labeled **Soil, Grass,** and **Snow**.

   [![Landscape target layers](https://dev.epicgames.com/community/api/documentation/image/3434e789-326c-4a6f-8c2e-758faf8af325?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3434e789-326c-4a6f-8c2e-758faf8af325?resizing_type=fit)

   Click image for full size.
3. To the right of the names, there is a **Plus Sign** icon.
   Clicking that will bring up another menu that will ask what type of
   layer you would like to add. For this example, pick the **Weight-Blended Layer (normal)** option.

   [![Landscape blend layer](https://dev.epicgames.com/community/api/documentation/image/5847d858-651a-4f6e-804c-75daff0934fd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5847d858-651a-4f6e-804c-75daff0934fd?resizing_type=fit)

   Click image for full size.
4. When you select the **Weight-Blended Layer (normal)** option, you are prompted with a pop-up box that asks you where you want to save the newly-created **Landscape Layer Info Objects**. Select the **Resources** folder under the **Landscape folder** then click **Save**.

   [![Landscape layer info save](https://dev.epicgames.com/community/api/documentation/image/3346b22e-eed8-4d07-87a2-07cd18d0e567?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3346b22e-eed8-4d07-87a2-07cd18d0e567?resizing_type=fit)

   Click image for full size.
5. After you complete the first one, repeat the same process for the other two. You should have something that looks like the following:

   [![Landscape finshed layers](https://dev.epicgames.com/community/api/documentation/image/663dd669-01a0-499f-9e76-5b5c07a12980?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/663dd669-01a0-499f-9e76-5b5c07a12980?resizing_type=fit)

   Click image for full size.

Now that you created and applied the **Landscape Layer Info Objects**, you can begin to paint your Landscape.

### Painting the Landscape

Before you begin to paint the Landscape, here is a re-cap of some of the most used commonly used keyboard and mouse inputs that you will use when painting the Landscape.

| Common Controls | Operation |
| --- | --- |
| **Left Mouse Button (LMB)** | Performs a stroke that applies the selected tool's effects to the selected layer. |
| **Ctrl+Z** | Undo last stroke. |
| **Ctrl+Y** | Redo last undone stroke. |

The main tool that you will use for applying textures to your Landscape is going to be the **Paint Tool**. To find out more about all of the tools that you can use to paint on the Landscape, check out the [Paint Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-paint-mode-in-unreal-engine) documentation.

To apply a Material to the Landscape, press and hold the **Left Mouse Button** to apply whatever you have selected to the area under the brush.

To select a new texture to paint, make sure you are in **Landscape Painting Mode** then under the **Target Layers**
section, select which texture you want to paint with by clicking on it
in the list. Whichever texture is highlighted will be painted on the
Landscape. In the image below, you can see the **Soil** layer is highlighted meaning that this is the texture that will be painted to the Landscape.

[![Landscape picking layers to paint](https://dev.epicgames.com/community/api/documentation/image/c67de979-8644-4ba3-8d0d-9f2d88907e16?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c67de979-8644-4ba3-8d0d-9f2d88907e16?resizing_type=fit)

Click image for full size.

When you finish painting, you should have something that looks like this.

[![Landscape final paint](https://dev.epicgames.com/community/api/documentation/image/75900d03-b7ca-453c-9f8b-7a890a08b13b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/75900d03-b7ca-453c-9f8b-7a890a08b13b?resizing_type=fit)

Click image for full size.

### Possible Issues and Workarounds

When you first start painting on your Landscape you might run into an issue where the base Material disappears or turns black, like in the following picture:

[![First paint issues](https://dev.epicgames.com/community/api/documentation/image/3f0a2ad6-2796-45f2-9070-b963b1259367?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3f0a2ad6-2796-45f2-9070-b963b1259367?resizing_type=fit)

Click image for full size.

This happens when there is no Paint Layer data on the Landscape when
you first start to paint. To fix this issue, continue to paint over the
Landscape generating the Paint Layer data as you go. If you would like
to fill in the entire Landscape, first select a large brush size, like
8192.0, pick a layer that you want to use as a base and paint over the
entire Landscape once. This will create Paint Layer data and allow you
to continue to paint without anything turning black.

Another issue that you might run into is that the scale of the
Textures on your Landscape are either too big or too small. To fix this,
open your Landscape Material and select the **Landscape Coords** node. With that node selected, adjust the **Mapping Scale** in the **Details**
panel and save the Material. When the Material is re-compiled, check
the scale in the viewport. If the scale is not to your liking, repeat the processes above until you get the results you want.

[![Landscape texture size](https://dev.epicgames.com/community/api/documentation/image/d903cfed-2cce-4436-9239-c668e3bc9d02?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d903cfed-2cce-4436-9239-c668e3bc9d02?resizing_type=fit)

Click image for full size.

Here is a comparison between a **Mapping Scale** of **0.5** on the Left and **5.0** on the Right.

![Mapping Scale: 0.5](https://dev.epicgames.com/community/api/documentation/image/35d05ec7-0c94-48cf-9bd0-dfd3727a655a?resizing_type=fit&width=1920&height=1080)

![Mapping Scale: 5.0](https://dev.epicgames.com/community/api/documentation/image/54cad4ba-5142-4717-91e0-6000fe7197ca?resizing_type=fit&width=1920&height=1080)

Mapping Scale: 0.5

Mapping Scale: 5.0

## 6 - Landscape Tips and Tricks

While the quick start tutorial above will get you up and running with a Landscape, it barely scratches the surface of what the Landscape tools can do. This section aims to show you some tips and tricks for using the Landscape tools as well as some external tools that you can use to generate your Landscape.

### Tips & Tricks

* When using the **Paint Tools**, you might find it easier to paint over what you would like to erase than to try and erase it using **Shift + Left Mouse Button**.
* When using the **Alpha Brush**, remember that you can change what the pattern that the brush uses by selecting a different RGB channels from the **Texture Channel** drop down menu. This is very handy because you can pack up to three different Alpha patterns in a single texture.

  [![Landscape tips tricks](https://dev.epicgames.com/community/api/documentation/image/759127df-2b38-4861-8afa-7b116d1f2053?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/759127df-2b38-4861-8afa-7b116d1f2053?resizing_type=fit)

  Click image for full size.
* Landscape compiles shaders separately for each component based on
  which layers are painted on them. For example, if you have a component
  with a dirt layer on it but no trace of the grass layer has been painted
  on it, the textures for the grass layer are left out of the material
  for that component, making it cheaper to render. So when you do an
  optimization pass, it can be worthwhile to go over a Landscape and look
  for components that only have a tiny trace of a given layer and erase
  them to reduce material complexity.
* Another issue to watch out for when painting layers is to avoid
  having too many textures on one component. The material editor stats
  show the limit of how many texture samples you are allowed to use, but
  for Landscape materials the masks for each layer count as texture
  samples too and do not show in the stats. If a component starts showing
  the default texture (Grey Squares) when you paint a new layer onto it,
  it is likely that it is gone over the texture sample limit and either
  needs to have a layer erased or the material needs to be optimized to
  use less textures.
* You can change the LOD Distance Factor for individual Landscape
  components so they will simplify at closer or further distance
  thresholds. Things like mountain peaks or anything with a distinct
  silhouette will LOD most noticeably as you move further away, so you can
  reduce the LOD bias for those components to preserve their shape. You
  can also raise the LOD bias for low-detail areas like flat plains that
  will not look noticeably different with less tessellation.

### World Composition

Unreal Engine 5 (UE5) now offers the ability to create massive worlds
made using Landscape that can easily be managed by using the **World Composition**
tool. World Composition was designed to help simplify the management of
large worlds, especially if those worlds are made using the Landscape
system. To find out more about the World Composition tool, please refer
to the official document that you can find here:

* [![World Composition](https://dev.epicgames.com/community/api/documentation/image/1b24f6b1-cba2-491c-a2bc-fa6fd0e8c08d?resizing_type=fit&width=640&height=640)

  World Composition

  System for managing large worlds including origin shifting technology.](https://dev.epicgames.com/documentation/en-us/unreal-engine/world-composition-in-unreal-engine)

### External Creation Tools

While the default Landscape tools do have the ability to meet all of
your sculpting and painting needs, there could be some situations where
you might want some extra control over your Landscape's look and feel.
The following is a list of software packages that could help you obtain
the results you are looking for if you cannot get them from using the
Landscape tools.

| Tool | Description |
| --- | --- |
| [Houdini](https://www.sidefx.com/) | Procedural terrain generation in Houdini uses a collection of heightfield nodes to let you use layer shapes and add noise to define the look of your digital landscapes. Use advanced erosion tools for more control over details such as fluvial lines, river banks, debris, and new hierarchical scattering for more efficient placement of elements into landscapes. You can then export height and/or mask layers to create terrain in UE5, or you can wrap up your terrain networks into Houdini Digital Assets that will open up in UE5 using the Houdini Engine plug-in. When Digital Assets include heightfield nodes, they will integrate seamlessly with Unreal Engine's native Terrain tools. |
| [Mudbox](http://www.autodesk.com/products/mudbox/overview) | While primarily a tool for digital sculpting and painting 3D meshes, Mudbox can also be used to generate heightmap data for your Landscape. You can read more about how Mudbox might be able to help you out with your Landscape by checking out their website. |
| [Terragen](http://planetside.co.uk/) | Terragen is another powerful fully procedural terrain creation software. Much like World Machine, it can be used to build, texture, and export both heightmaps and textures for your Landscape. You can read more about how Terragen might be able to help you out with your Landscape by checking out their website. |
| [World Machine](http://www.world-machine.com/) | World Machine is a powerful procedural terrain creation software. It can be used to build, texture, and export both heightmaps and textures for your Landscape. You can read more about how World Machine might be able to help you out with your Landscape by checking out their website. |
| [ZBrush](http://pixologic.com/) | Zbrush is another digital sculpting and painting tool that can be used to generate heightmap data for your Landscape. You can read more about how Zbrush might be able to help you out with your Landscape by checking out their website. |

* [landscape](https://dev.epicgames.com/community/search?query=landscape)
* [building virtual worlds](https://dev.epicgames.com/community/search?query=building%20virtual%20worlds)
* [open world](https://dev.epicgames.com/community/search?query=open%20world)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [1 - Working with the Landscape Tools](/documentation/en-us/unreal-engine/landscape-quick-start-guide-in-unreal-engine?application_version=5.7#1-workingwiththelandscapetools)
* [Opening the Landscape Tool and Working with Modes](/documentation/en-us/unreal-engine/landscape-quick-start-guide-in-unreal-engine?application_version=5.7#openingthelandscapetoolandworkingwithmodes)
* [Interacting with the Landscape Tools](/documentation/en-us/unreal-engine/landscape-quick-start-guide-in-unreal-engine?application_version=5.7#nbsp-interacting-with-the-landscape-tools)
* [2 - Creating a new Landscape](/documentation/en-us/unreal-engine/landscape-quick-start-guide-in-unreal-engine?application_version=5.7#2-creatinganewlandscape)
* [Creating a Landscape](/documentation/en-us/unreal-engine/landscape-quick-start-guide-in-unreal-engine?application_version=5.7#creatingalandscape)
* [3 - Sculpting the Landscape](/documentation/en-us/unreal-engine/landscape-quick-start-guide-in-unreal-engine?application_version=5.7#3-sculptingthelandscape)
* [4 - Creating Landscape Materials](/documentation/en-us/unreal-engine/landscape-quick-start-guide-in-unreal-engine?application_version=5.7#4-creatinglandscapematerials)
* [Folder Setup](/documentation/en-us/unreal-engine/landscape-quick-start-guide-in-unreal-engine?application_version=5.7#foldersetup)
* [Migrating Textures](/documentation/en-us/unreal-engine/landscape-quick-start-guide-in-unreal-engine?application_version=5.7#migratingtextures)
* [Creating the Landscape Material](/documentation/en-us/unreal-engine/landscape-quick-start-guide-in-unreal-engine?application_version=5.7#creatingthelandscapematerial)
* [Layer Blend Base Color](/documentation/en-us/unreal-engine/landscape-quick-start-guide-in-unreal-engine?application_version=5.7#layerblendbasecolor)
* [Layer Blend Normal](/documentation/en-us/unreal-engine/landscape-quick-start-guide-in-unreal-engine?application_version=5.7#layerblendnormal)
* [5 - Painting Landscape Materials](/documentation/en-us/unreal-engine/landscape-quick-start-guide-in-unreal-engine?application_version=5.7#5-paintinglandscapematerials)
* [Landscape Painting Prep](/documentation/en-us/unreal-engine/landscape-quick-start-guide-in-unreal-engine?application_version=5.7#landscapepaintingprep)
* [Painting the Landscape](/documentation/en-us/unreal-engine/landscape-quick-start-guide-in-unreal-engine?application_version=5.7#paintingthelandscape)
* [Possible Issues and Workarounds](/documentation/en-us/unreal-engine/landscape-quick-start-guide-in-unreal-engine?application_version=5.7#possibleissuesandworkarounds)
* [6 - Landscape Tips and Tricks](/documentation/en-us/unreal-engine/landscape-quick-start-guide-in-unreal-engine?application_version=5.7#6-landscapetipsandtricks)
* [Tips & Tricks](/documentation/en-us/unreal-engine/landscape-quick-start-guide-in-unreal-engine?application_version=5.7#tips&tricks)
* [World Composition](/documentation/en-us/unreal-engine/landscape-quick-start-guide-in-unreal-engine?application_version=5.7#worldcomposition)
* [External Creation Tools](/documentation/en-us/unreal-engine/landscape-quick-start-guide-in-unreal-engine?application_version=5.7#externalcreationtools)
