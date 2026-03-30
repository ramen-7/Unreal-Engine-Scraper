<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/code-a-firstperson-adventure-game-in-unreal-engine?application_version=5.7 -->

# Code a First-Person Adventure Game

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
6. [Unreal Engine for New Users](/documentation/en-us/unreal-engine/unreal-engine-for-new-users "Unreal Engine for New Users")
7. Code a First-Person Adventure Game

# Code a First-Person Adventure Game

Learn how to create C++ classes that implement the basic mechanics of a first-person game.

On this page

Using C++ with Unreal Engine gives you full control and access to the engine’s features so you can create new functionality within your project. It's perfect for creating complex systems, optimizing performance, and taking your game to the next level!

You can use **Blueprints** or C++ classes to create new functionality through code in Unreal Engine. Blueprints is the engine’s visual coding tool. It’s beginner friendly, easy to discover, and quick to edit. You’ll edit Blueprints in UE’s Blueprint Editor and end up with a Blueprint-type asset in your Content Browser.

However, Blueprints can become hard to read and manage as they grow in complexity. In larger projects, C++ is more concise to read, performs faster, and gives you access to all functionality within Unreal so you get full control over gameplay mechanics.

C++ and Blueprints also work together! You can extend your C++ class to a Blueprint so designers can easily tweak variables or use it in a more visual way. The Blueprint acts as a child of the C++ class, inheriting all functionality of the class.

In this tutorial, you’ll use C++ and Unreal Editor to set up a new UE code project and build a custom player character.

This tutorial requires Unreal Engine 5.6.1 or later. Unreal Engine 5.6.0 has a known issue that breaks Blueprint creation from C++ in Blueprint-based projects, which is required for this tutorial series.

## Before You Begin

* Read the other getting-started pages in [Unreal Engine for New Users](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-for-new-users).
* [Set Up Visual Studio for Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-visual-studio-development-environment-for-cplusplus-projects-in-unreal-engine?application_version=5.5)

## Let's Go!

* [![Set Up and Compile Your Project](https://dev.epicgames.com/community/api/documentation/image/23e51566-011a-47b6-b454-8a8976b2d3d6?resizing_type=fit&width=640&height=640)

  Set Up and Compile Your Project

  Learn how to set up and compile a new C++ game project from a template.](https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-01-set-up-and-compile-a-cplusplus-project-in-unreal-engine)
* [![Create a Player Character With Input Actions](https://dev.epicgames.com/community/api/documentation/image/b7155dfc-b014-4288-ae6d-d4620dc7420d?resizing_type=fit&width=640&height=640)

  Create a Player Character With Input Actions

  Learn how to start building a C++ character with Input Actions.](https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-02-create-a-player-character-with-input-actions-in-cplusplus)
* [![Configure Character Movement](https://dev.epicgames.com/community/api/documentation/image/63cf4ce2-6faa-4f79-a8d2-f476a7a6adf2?resizing_type=fit&width=640&height=640)

  Configure Character Movement

  Learn how to bind player input to character movement in C++.](https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-03-configure-character-movement-with-cplusplus-in-unreal-engine)
* [![Add a First-Person Camera, Mesh, and Animation](https://dev.epicgames.com/community/api/documentation/image/2ee65bff-b2bf-47fb-9d15-b88aae401617?resizing_type=fit&width=640&height=640)

  Add a First-Person Camera, Mesh, and Animation

  Learn how to use C++ to attach mesh and camera components on a first-person Character.](https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-04-adding-a-firstperson-camera-mesh-and-animation)
* [![Manage Items and Data](https://dev.epicgames.com/community/api/documentation/image/1db9f4bd-93e0-4ad8-8abf-c7be6ecec5e8?resizing_type=fit&width=640&height=640)

  Manage Items and Data

  Learn to use Item Data Structs, Data Assets, and Data Tables to define items and store and organize item data for scalability.](https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-05-manage-item-and-data-in-an-unreal-engine-game)
* [![Create a Respawning Pickup Item](https://dev.epicgames.com/community/api/documentation/image/680d7d74-76be-46e0-9631-a62ac8dd8c04?resizing_type=fit&width=640&height=640)

  Create a Respawning Pickup Item

  Learn how to use C++ to create custom pickups and initialize them in your level.](https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-06-create-a-respawning-pickup-item-in-unreal-engine)
* [![Equip Your Character](https://dev.epicgames.com/community/api/documentation/image/d7ce94e9-285d-4876-b873-3c7728f842fa?resizing_type=fit&width=640&height=640)

  Equip Your Character

  Learn to use C++ to create custom equippable items and attach them to your character.](https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools)
* [![Implement a Projectile](https://dev.epicgames.com/community/api/documentation/image/25ecf04a-ccd5-4507-80d4-446d937d850c?resizing_type=fit&width=640&height=640)

  Implement a Projectile

  Learn to use C++ to implement projectiles and spawn them during gameplay.](https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-08-implement-a-projectile-in-unreal-engine)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Before You Begin](/documentation/en-us/unreal-engine/code-a-firstperson-adventure-game-in-unreal-engine?application_version=5.7#beforeyoubegin)
* [Let's Go!](/documentation/en-us/unreal-engine/code-a-firstperson-adventure-game-in-unreal-engine?application_version=5.7#let'sgo!)

Related documents

[Your First Hour in Unreal Engine

![Your First Hour in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/b68b5e7a-09df-4354-acb4-2fb8b3291793?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/first-hour-in-unreal-engine)

[Design a Puzzle Adventure

![Design a Puzzle Adventure](https://dev.epicgames.com/community/api/documentation/image/a7b7ff2c-23d0-47a0-8a04-e569209942b0?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine)

[Art Pass for a Puzzle Adventure Game](/documentation/en-us/unreal-engine/art-pass-for-a-puzzle-adventure-game)
