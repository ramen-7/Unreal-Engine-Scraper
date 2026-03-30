<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/paper-2d-overview-in-unreal-engine?application_version=5.7 -->

# Paper 2D

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
6. Paper 2D

# Paper 2D

Paper 2D is a sprite-based system for creating 2D and 2D/3D hybrid games in Unreal Engine.

![Paper 2D](https://dev.epicgames.com/community/api/documentation/image/d815e05c-f867-4e5b-8385-cbddbd0db336?resizing_type=fill&width=1920&height=335)

 On this page

**Paper 2D** is **Unreal Engine**'s gameplay and animation system that you can use to create 2D and 2D/3D hybrid projects. In this document you can read about the components of the Paper 2D system that you can use to create 2D and 2D/3D hybrid games in Unreal Engine.

#### Prerequisites

* Enable the Paper 2D [Plugin](/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine). Navigate in the **Menu Bar** to **Edit > Plugins** and locate the **Paper 2D** plugin in the **2D** section, or by using the **Search Bar**. **Enable** the plugin and restart the editor.

![paper 2d plugin](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/098d0c9f-d8bf-4620-919c-963fe3b13198/image79.png)

## Sprites

Paper 2D's primary asset type is called a **Sprite**. Sprites are static 2-dimensional textures that you can use to represent characters or objects, when developing projects in Unreal Engine.

![single manny sprite example](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/371ea5d1-4a29-4272-b405-02c917642542/sprite.png)

Sprites often come in the form of a **Sprite Sheet**, or a single image file that contains many variations of the sprite, that you can use to animate characters and objects.

![manny running sprite sheet example with every frame of animation](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/24026930-810a-4eb6-a07b-3fefddf4102c/spritesheet.png)

By playing the static sprites from a sprite sheet sequentially, using a [Flipbook](/documentation/en-us/unreal-engine/paper-2d-overview-in-unreal-engine#flipbook), you can animate Sprite based characters and objects.

For more information about importing and editing sprites with the Sprite Editor, please see the Paper 2D Sprites documentation.

[![Paper 2D Sprites](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d54c1466-8c7f-40f5-8cef-ef49f5f368e1/topicimage.png)

Paper 2D Sprites

How to import and use Paper 2D Sprites in Unreal Engine.](/documentation/en-us/unreal-engine/how-to-import-and-use-paper-2d-sprites-in-unreal-engine)

### Tiles

**Tiles** are 2D-textures that you can use to create the background and environment of a level.

![example of tile map being used as a level](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2e72894e-1693-42fa-9811-d1a7de1c2d1f/tilemap.png)

Many tiles can be imported as a single image file, and divided into individual tiles using a **TileSet** asset.

![example of tile sheet](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b84e2d49-55c1-499a-8abf-3c489eafe3ed/tilesheet.png)

You can then use TileSets to build a **TileMap** asset, to create a 2D level or environment.

![tile map being built](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/47a62f5c-7fb0-42a2-934c-0fa97d775626/tilemap-1.png)

For more information about importing Tiles and creating TileSets see the [Tiles](/documentation/en-us/unreal-engine/paper-2d-tile-sets-and-tile-maps-in-unreal-engine) documentation.

## Flipbooks

You can use **Flipbooks** in Unreal Engine, to play a sequence of sprites to animate characters and objects in your project.

![flipbook example manny running](run.gif)(convert:false)

After importing a sprite sheet, you can combine the extracted sprites to create a Flipbook to animate a character or object. You can then add FlipBooks directly to your character's or object's Blueprint to dynamically play animations during run time.

For more information about editing and using FlipBooks see the Flipbook documentation.

[![Paper 2D Flipbooks](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5918bc32-1745-4062-ab3f-131f22a8bdbf/flipbook-topic.png)

Paper 2D Flipbooks

Description of Paper 2D Flipbooks and how to create them.](/documentation/en-us/unreal-engine/paper-2d-flipbooks-in-unreal-engine)

## Workflow Guides

Here you can find workflow guides that you can reference when creating Paper2D projects in Unreal Engine.

[![Paper 2D - How To..](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/93bf0f97-dc0b-4e9b-9ed8-c1caa53b2177/placeholder_topic.png)

Paper 2D - How To..

The Paper 2D How To pages provides several short step-by-step guides for working with Paper 2D.](/documentation/en-us/unreal-engine/how-to-use-paper-2d-in-unreal-engine)

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [paper 2d](https://dev.epicgames.com/community/search?query=paper%202d)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisites](/documentation/en-us/unreal-engine/paper-2d-overview-in-unreal-engine?application_version=5.7#prerequisites)
* [Sprites](/documentation/en-us/unreal-engine/paper-2d-overview-in-unreal-engine?application_version=5.7#sprites)
* [Tiles](/documentation/en-us/unreal-engine/paper-2d-overview-in-unreal-engine?application_version=5.7#tiles)
* [Flipbooks](/documentation/en-us/unreal-engine/paper-2d-overview-in-unreal-engine?application_version=5.7#flipbooks)
* [Workflow Guides](/documentation/en-us/unreal-engine/paper-2d-overview-in-unreal-engine?application_version=5.7#workflowguides)
