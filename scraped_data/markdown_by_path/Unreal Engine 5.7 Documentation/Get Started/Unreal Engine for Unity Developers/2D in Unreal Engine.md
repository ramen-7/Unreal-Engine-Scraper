<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/2d-in-unreal-engine?application_version=5.7 -->

# 2D in Unreal Engine

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
5. [Get Started](/documentation/en-us/unreal-engine/get-started "Get Started")
6. [Unreal Engine for Unity Developers](/documentation/en-us/unreal-engine/unreal-engine-for-unity-developers "Unreal Engine for Unity Developers")
7. 2D in Unreal Engine

# 2D in Unreal Engine

An overview of creating 2D and 2D/3D projects using the Paper 2D plugin.

![2D in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/75e1e4d3-c7e8-41ac-aaf5-e43fcee5327a?resizing_type=fill&width=1920&height=335)

 On this page

**Paper 2D** is a plugin for **Unreal Engine (UE)** that you can use to create 2D and 2D/3D hybrid gameplay and animation systems. The Paper 2D plugin contains support for the various 2D asset types, such as Sprites for 2D characters and objects, Flipbooks for animating Sprites, TileSets, and TileMaps, which you can use to create 2D levels and environments, along with all of the associated editors you will need to create and edit your assets.

* [![Paper 2D](https://dev.epicgames.com/community/api/documentation/image/ba8c8712-7145-406a-a515-58cb49621fe3?resizing_type=fit&width=640&height=640)

  Paper 2D

  Paper 2D is a sprite-based system for creating 2D and 2D/3D hybrid games in Unreal Engine.](https://dev.epicgames.com/documentation/en-us/unreal-engine/paper-2d-overview-in-unreal-engine)

The Paper 2D system offers many choices when building projects with 2D elements. The plugin is feature-rich with assets and editors that you can use to create high-quality 2D content, from characters to environments. The plugin is also completely compatible with UE’s 3D rendering capabilities, meaning 2D elements can be seamlessly integrated with 3D characters, objects, or environments.

[![paper 2d hybrid example](https://dev.epicgames.com/community/api/documentation/image/d7a58e09-5d77-4f2b-b243-586179078dbf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d7a58e09-5d77-4f2b-b243-586179078dbf?resizing_type=fit)

#### Prerequisites

To start creating 2D and 2D/3D hybrid projects in UE, ensure the Paper 2D plugin is installed.

* In the Unreal Editor, navigate to the **Menu Bar** to **Edit** > **Plugins** and locate the **Paper 2D** plugin in the **2D section** or by using the **Search Bar**. If the plugin is not enabled, enable it by checking the box then restart the editor.

[![paper 2d plugin](https://dev.epicgames.com/community/api/documentation/image/1f5f76b3-2ca1-46df-8467-631f43db5b02?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1f5f76b3-2ca1-46df-8467-631f43db5b02?resizing_type=fit)

## Migrating Projects from Unity

When migrating a 2D project from Unity to UE, use the following steps:

1. Locate your 2D assets’ associated image files in your Unity Project’s **Assets** folder, which is found in the root directory of your Unity project.

   All 2D image files that Unity supports are also supported in UE, such as `.jpg` and `.png`.
2. After locating your image files in your Unity project folder, you can drag and drop them into your UE project’s **Content Browser** or browse to the file's location on your computer using the Content Browser’s **Import** button.

Image files imported to UE will be imported as Texture Assets, which can be used to create Paper 2D assets such as Sprites, Flipbooks, and TileMaps.

When importing low-resolution images, such as sprite-based artwork, you can apply sprite-specific settings to the texture to sharpen and enhance the look of pixel art, by right-clicking the asset in the Content Browser and selecting the **Sprite Actions** > **Apply Paper 2D Import Settings** option in the Context Menu.

For more information about importing sprite-based assets into UE, see the [Importing Sprites section](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-import-and-use-paper-2d-sprites-in-unreal-engine) of the Paper 2D Sprites document.

After importing your image assets into UE, you can create Sprite and TileSet assets and use their respective editors to begin building your game objects.

## Assets

The following sections provide a quick overview of the Paper 2D system and contain links to more extensive documentation.

### Sprites

Like Unity, the main asset you can use to create 2D characters and objects is called a **Sprite** asset. Sprites are a planer game object that you can map an image to be used as a character or an object. While any image can be used as a Sprite asset, the Paper 2D plugin comes packaged with specialized settings and materials to help improve the look of low-resolution pixel style graphics typically found in 2D style projects.

[![manny sprite](https://dev.epicgames.com/community/api/documentation/image/3fcd2996-1cff-4cc7-a695-968b96226763?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3fcd2996-1cff-4cc7-a695-968b96226763?resizing_type=fit)

Sprites can then be added to any UE **Actor** or **Paper 2D Character Actor**, as a **Sprite Component**.

For more information about Sprites in UE, such as settings, and a reference to using the Sprite Editor, see the following documentation:

* [![Paper 2D Sprites](https://dev.epicgames.com/community/api/documentation/image/d54c1466-8c7f-40f5-8cef-ef49f5f368e1?resizing_type=fit&width=640&height=640)

  Paper 2D Sprites

  How to import and use Paper 2D Sprites in Unreal Engine.](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-import-and-use-paper-2d-sprites-in-unreal-engine)

### Flipbooks

Sprite actors can be animated using **Flipbooks** assets, which store a linear sequential playback of different sprite assets. Unlike Unity, Flipbooks are unique assets that can be used independently of an individual Sprite asset or even Actor object. This means animations are more versatile and reusable and can be played anytime using Blueprints or C++ code.

[![manny flipbook](https://dev.epicgames.com/community/api/documentation/image/251702f1-b451-4beb-b3e0-b56fdacd642c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/251702f1-b451-4beb-b3e0-b56fdacd642c?resizing_type=fit)

For more information about creating, using and editing Flipbooks in UE, see the following documentation:

* [![Paper 2D Flipbooks](https://dev.epicgames.com/community/api/documentation/image/5918bc32-1745-4062-ab3f-131f22a8bdbf?resizing_type=fit&width=640&height=640)

  Paper 2D Flipbooks

  Description of Paper 2D Flipbooks and how to create them.](https://dev.epicgames.com/documentation/en-us/unreal-engine/paper-2d-flipbooks-in-unreal-engine)

### TileSets and TileMaps

The Paper 2D plugin also contains the TileSet and TileMap assets, along with their corresponding editors that you can use to create 2D levels and environments. Using TileSet assets, you can import one large asset containing all of your background assets for a level, extract each tile, and define collision settings that will influence how your player can interact with the environment.

You can then assemble the tiles into a TileMap asset to build levels, using tools like layers to build dynamic and interesting environments for your project.

[![tilemap in unreal engine](https://dev.epicgames.com/community/api/documentation/image/079a4fee-bcdd-4ca3-bfdd-ce1a708e3f8e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/079a4fee-bcdd-4ca3-bfdd-ce1a708e3f8e?resizing_type=fit)

For more information about using TileSets and TileMaps in UE, see the following documentation:

* [![Paper 2D Tile Sets / Tile Maps](https://dev.epicgames.com/community/api/documentation/image/1f60a987-9bed-4c9d-bf96-2e8571f9fdc2?resizing_type=fit&width=640&height=640)

  Paper 2D Tile Sets / Tile Maps

  Overview of how to create Tile Sets and Tile Maps for use within Paper 2D.](https://dev.epicgames.com/documentation/en-us/unreal-engine/paper-2d-tile-sets-and-tile-maps-in-unreal-engine)

* [unity](https://dev.epicgames.com/community/search?query=unity)
* [paper 2d](https://dev.epicgames.com/community/search?query=paper%202d)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisites](/documentation/en-us/unreal-engine/2d-in-unreal-engine?application_version=5.7#prerequisites)
* [Migrating Projects from Unity](/documentation/en-us/unreal-engine/2d-in-unreal-engine?application_version=5.7#migrating-projects-from-unity)
* [Assets](/documentation/en-us/unreal-engine/2d-in-unreal-engine?application_version=5.7#assets)
* [Sprites](/documentation/en-us/unreal-engine/2d-in-unreal-engine?application_version=5.7#sprites)
* [Flipbooks](/documentation/en-us/unreal-engine/2d-in-unreal-engine?application_version=5.7#flipbooks)
* [TileSets and TileMaps](/documentation/en-us/unreal-engine/2d-in-unreal-engine?application_version=5.7#tile-sets-and-tile-maps)
