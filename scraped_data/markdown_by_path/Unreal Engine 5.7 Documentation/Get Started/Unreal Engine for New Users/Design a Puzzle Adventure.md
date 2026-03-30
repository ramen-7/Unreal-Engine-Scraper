<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine?application_version=5.7 -->

# Design a Puzzle Adventure

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
7. Design a Puzzle Adventure

# Design a Puzzle Adventure

Learn how to design a full level and gameplay loop in this getting started tutorial!

![Design a Puzzle Adventure](https://dev.epicgames.com/community/api/documentation/image/c78e0977-d0ea-4a31-9d3a-a7a28f42bc4c?resizing_type=fill&width=1920&height=335)

 On this page

Unreal Engine provides users with the professional-grade tools to bring their game ideas to life. Once you have made decisions about what types of gameplay you want, it’s time to start building the play spaces and environments that will define the visual world of your game.

Designer Track Overview

Game and Level Design is about designing experiences that challenge players while still providing a fun and engaging world that supports those experiences. While the Code a First-Person Adventure Game tutorial focuses on using C++ to create gameplay, you can create many of the same elements using the Blueprint Scripting language. Blueprints provide non-programmers with a flexible scripting language that can be used to create gameplay, scripted events, and interactable elements. Unreal Engine provides the ability to create games using Blueprints, C++, or a mix of both.

This tutorial series takes you through the design process of building a level and several puzzles using blueprints to create a completely playable gameplay experience. You will learn how to create gameplay using Blueprints, as well as how to use and reuse gameplay elements to prototype a level using a process called grayboxing.

[![Designer Track Puzzles](https://dev.epicgames.com/community/api/documentation/image/bb5d5a4a-2437-4295-8b48-72fc52f5be9c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bb5d5a4a-2437-4295-8b48-72fc52f5be9c?resizing_type=fit)

Designer Track Puzzles

## Designer Track Overview

Throughout this tutorial, you will build an adventure puzzle game with multiple rooms, showcasing different kinds of mechanics.

[![Overview Diagram of the Designer Track Level](https://dev.epicgames.com/community/api/documentation/image/946207a5-ebf2-4d52-ab05-f21632b18759?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/946207a5-ebf2-4d52-ab05-f21632b18759?resizing_type=fit)

Overview Diagram of the Designer Track Level

1. Set up and grayboxing your level. This is an important first step to thinking through your level’s design before you start digging into the level’s mechanics and gameplay.
2. Create a key and door open and close mechanic.
3. Implement a heads-up-display (HUD) on the player’s user interface using UMG.
4. Design the cube puzzles, first with a light switch activator and then with moving platforms.
5. Build traps under the platformer and learn about player failure and how to set damage over time.
6. Configure enemy pawns to attack the player, and then a sprint movement for the player so they can get past the enemies quickly!
7. Add an end state so the game knows when the game is over, plus additional polish!

When you finish the tutorial, you will have a fully functional puzzle game!

## Before You Begin

* If you’re new to Unreal Engine, read the other getting-started pages in [Unreal Engine for New Users](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-for-new-users).
* The Code a First-Person Adventure Game is a tutorial series that uses C++ and Unreal Editor to build a custom player character. You can use what you build in the Programmer Track as a starting point for this track.

## Example Project

Below is a link to download the final sample project that you can build using this tutorial series. You can use this example project to see what your final project might look like, or as a reference to see how we built and designed the project.

[Download the Designer Track here](https://d1iv7db44yhgxn.cloudfront.net/documentation/attachments/bcb4d714-941a-4a93-9d50-25ff231868e6/adventuredesigner.zip)

*(Download size: 75 MB)*

To open the project, unzip the file and move the **adventuredesigner** folder to your Unreal Projects directory (by default, find this in `C:\Users\UserName\Documents\Unreal Projects`).

## Let’s Go!

* [![Project Setup and Level Blockout](https://dev.epicgames.com/community/api/documentation/image/6e552d12-1c85-47b1-ae6e-86f8c6c93eb9?resizing_type=fit&width=640&height=640)

  Project Setup and Level Blockout

  Get started planning, designing, and blocking out your puzzle adventure level! Practice using different Viewport modes, transforming objects, and organizing assets in the Outliner.](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine)
* [![Create a Key](https://dev.epicgames.com/community/api/documentation/image/03094522-adf5-4121-863e-16ba0071b20e?resizing_type=fit&width=640&height=640)

  Create a Key

  Using blueprints, learn how to create a key that players can pick up.](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-02-create-a-key-in-unreal-engine)
* [![Open Doors with Keys](https://dev.epicgames.com/community/api/documentation/image/a8a6ceb2-292f-4306-9ba4-0121d3fc6dda?resizing_type=fit&width=640&height=640)

  Open Doors with Keys

  Configure the BP\_DoorFrame blueprint so the doors can change color and only open with the matching BP\_Key.](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-03-open-doors-with-keys-in-unreal-engine)
* [![Player HUD](https://dev.epicgames.com/community/api/documentation/image/9b754da0-a689-4622-a7a9-9155cfd86535?resizing_type=fit&width=640&height=640)

  Player HUD

  Create a simple heads-up-display (HUD) that updates when the player picks up an item.](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-04-player-hud-in-unreal-engine)
* [![Puzzles: Switches and Cubes](https://dev.epicgames.com/community/api/documentation/image/e19af92d-9bce-482b-841f-e8021d9c6fd6?resizing_type=fit&width=640&height=640)

  Puzzles: Switches and Cubes

  In the first part of the platformer puzzle section, use materials, physics, and blueprints to create a switch that’s activated by a cube.](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-05-puzzles-switches-and-cubes-in-unreal-engine)
* [![Puzzles: Moving Platforms](https://dev.epicgames.com/community/api/documentation/image/368c36ed-f258-4eac-87e0-5c3076b944d1?resizing_type=fit&width=640&height=640)

  Puzzles: Moving Platforms

  In the second part of the platformer puzzle, create the moving platforms with blueprints and learn how to debug your script.](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-06-puzzles-moving-platforms-in-unreal-engine)
* [![Traps and Damage](https://dev.epicgames.com/community/api/documentation/image/87f77dd2-9774-4a28-9a73-a178e0642500?resizing_type=fit&width=640&height=640)

  Traps and Damage

  Learn to build environmental blueprints that damage the player and build a game-over loop that triggers when the player is eliminated.](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-07-traps-and-damage-in-unreal-engine)
* [![Create an Enemy](https://dev.epicgames.com/community/api/documentation/image/4fbadab0-8092-43bc-9cd7-af30b9660238?resizing_type=fit&width=640&height=640)

  Create an Enemy

  Build game logic to create Enemy Characters that deal and receive damage.](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-08-create-an-enemy-in-unreal-engine)
* [![Add a Sprint Mechanic to the Player](https://dev.epicgames.com/community/api/documentation/image/270b9145-0c98-4508-bc16-cac1a9c05617?resizing_type=fit&width=640&height=640)

  Add a Sprint Mechanic to the Player

  Use Input Actions to add a sprint mechanic to the player character's move set.](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-09-sprint-input-action-in-unreal-engine)
* [![Complete the Level](https://dev.epicgames.com/community/api/documentation/image/ba0d92a7-77cf-4109-a9f5-df3746f87858?resizing_type=fit&width=640&height=640)

  Complete the Level

  Finish the level by completing the gameplay loop and configuring an end state for the player.](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-10-complete-the-level-in-unreal-engine)
* [![Bonus: Spawn New Cubes](https://dev.epicgames.com/community/api/documentation/image/74689b74-657d-4bee-87d4-35498f257195?resizing_type=fit&width=640&height=640)

  Bonus: Spawn New Cubes

  Add a new mechanic to your puzzle adventure game where BP\_Cube actors spawn to a specified limit.](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-11-spawn-new-cubes-mechanic-in-unreal-engine)

* [blueprint](https://dev.epicgames.com/community/search?query=blueprint)
* [level design](https://dev.epicgames.com/community/search?query=level%20design)
* [beginner](https://dev.epicgames.com/community/search?query=beginner)
* [graybox](https://dev.epicgames.com/community/search?query=graybox)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Designer Track Overview](/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine?application_version=5.7#designertrackoverview)
* [Before You Begin](/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine?application_version=5.7#beforeyoubegin)
* [Example Project](/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine?application_version=5.7#exampleproject)
* [Let’s Go!](/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine?application_version=5.7#let%E2%80%99sgo!)

Related documents

[Code a First-Person Adventure Game

![Code a First-Person Adventure Game](https://dev.epicgames.com/community/api/documentation/image/ffc1a8f8-e7e5-42c0-b4ed-32ce6d3adbbc?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/code-a-firstperson-adventure-game-in-unreal-engine)

[Art Pass for a Puzzle Adventure Game](/documentation/en-us/unreal-engine/art-pass-for-a-puzzle-adventure-game)

[Your First Hour in Unreal Engine

![Your First Hour in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/b68b5e7a-09df-4354-acb4-2fb8b3291793?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/first-hour-in-unreal-engine)

[Unreal Engine for New Users](/documentation/en-us/unreal-engine/unreal-engine-for-new-users)
