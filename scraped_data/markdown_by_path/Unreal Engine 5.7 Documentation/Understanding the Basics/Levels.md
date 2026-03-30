<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/levels-in-unreal-engine?application_version=5.7 -->

# Levels

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
5. [Understanding the Basics](/documentation/en-us/unreal-engine/understanding-the-basics-of-unreal-engine "Understanding the Basics")
6. Levels

# Levels

Levels contain everything a player can see and interact with, like environments, usable objects, other characters, and so on.

![Levels](https://dev.epicgames.com/community/api/documentation/image/3c400d69-34a4-4895-9ebf-5b83f3732301?resizing_type=fill&width=1920&height=335)

A **Level** is all or part of your game's "world". Levels contain everything a player can see and interact with, like environments, usable objects, other characters, and so on. In video games, it's common to have multiple levels with clearly delineated transitions between them (for example, once you beat the final boss in a level, you move on to the next one). For other types of interactive experiences made with Unreal Engine, you might use different Levels to transition between different kinds of showcases or environments.

Unreal Engine saves each Level as a separate `.umap` file, which is why you will sometimes see Levels referred to as **Maps**.

Here is a minimal list of elements that come together to create a Level:

* A `.umap` file, which is the Level itself. Think of it as a container that holds everything else.
* An environment made of **Static Mesh Actors**. These can be trees, rocks, walls, or any other environment fixture. Some environments also use other types of Actors, such as Landscape Actors or Water Actors.
* A player character represented by a **Skeletal Mesh Actor**.
* One or more **lights** of different types.
* Ambient sounds and sound effects (for example, footstep sounds).

Complex levels can contain other features like particle effects, visual post-processing, Level Streaming, and so on.

If you would like to see what an advanced Unreal project looks like, have a look at the [Stack O Bot](https://www.fab.com/listings/b4dfff49-0e7d-4c4b-a6c5-8a0315831c9c) example game on Fab.

The pages below can teach you more about how to create and work with Level Assets in Unreal Engine 5.

[![Working with Levels](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e7ac3fd5-5107-4ca1-8abc-fe7ea0ddc0c2/level_topic.png)

Working with Levels

How to create, save, and open level assets.](/documentation/en-us/unreal-engine/working-with-levels-in-unreal-engine)
[![Managing Multiple Levels](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9cc933d3-4aa2-47f4-9604-9e31e9715806/ue5-social.png)

Managing Multiple Levels

Use the Levels window to manage your persistent level and sublevels.](/documentation/en-us/unreal-engine/managing-multiple-levels-in-unreal-engine)
[![World Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b35e3dfc-ce35-4313-bfdb-5e46fe6e8263/world-settings-topic.png)

World Settings

The World Settings panel is where you set and override Level-specific settings.](/documentation/en-us/unreal-engine/world-settings-in-unreal-engine)
[![Changing the Default Level](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/eef82806-b721-48d6-9f68-2c256030d00b/placeholder_topic.png)

Changing the Default Level

How to set the default editor and game Levels for your project](/documentation/en-us/unreal-engine/changing-the-default-level-of-an-unreal-engine-project)

* [levels](https://dev.epicgames.com/community/search?query=levels)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

Related documents

[Static Mesh Actors

![Static Mesh Actors](https://dev.epicgames.com/community/api/documentation/image/cc768f4e-d5f8-44a1-b767-1aa70fe98cb5?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/static-mesh-actors-in-unreal-engine)

[Skeletal Mesh Actors

![Skeletal Mesh Actors](https://dev.epicgames.com/community/api/documentation/image/3d6178dd-d5c4-44c8-b7d6-387f6b4df9df?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/skeletal-mesh-actors-in-unreal-engine)

[Sound Sources

![Sound Sources](https://dev.epicgames.com/community/api/documentation/image/f23e8734-ecae-43e1-ace3-9f8a01e269a2?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/sound-sources-in-unreal-engine)
