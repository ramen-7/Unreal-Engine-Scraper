<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-sequences-in-parrot?application_version=5.7 -->

# Sequences in Parrot

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
7. [Parrot Game Sample](/documentation/en-us/unreal-engine/parrot-game-sample-for-unreal-engine "Parrot Game Sample")
8. Sequences in Parrot

# Sequences in Parrot

Learn how Parrot uses Sequencer.

![Sequences in Parrot](https://dev.epicgames.com/community/api/documentation/image/fafec984-4b6a-4498-a56a-c0f9d7e7b981?resizing_type=fill&width=1920&height=335)

 On this page

Sequencer is a tool in Unreal Engine for creating cinematic sequences. Parrot uses Sequencer to create moving obstacles in the levels, such as a shark. For more information about using Sequencer in Unreal Engine, see [Cinematics and Sequencer](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematics-and-movie-making-in-unreal-engine).

## Shark Obstacle

The **MainMenu** level of Parrot uses level sequences to create a swimming shark. You can view how these basic sequences are set up by opening `Content/Maps/MainMenu/SwimmingShark`.

With the sequence open in Sequencer, you can see how the tracks are set up. There is a path track under the shark actor in the level, which makes the shark swim around a spline actor placed in the level. There is also an event track that triggers events to manipulate the shark’s animator to switch between its animations.

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [fab](https://dev.epicgames.com/community/search?query=fab)
* [parrot game sample](https://dev.epicgames.com/community/search?query=parrot%20game%20sample)
* [learning](https://dev.epicgames.com/community/search?query=learning)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Shark Obstacle](/documentation/en-us/unreal-engine/unreal-engine-sequences-in-parrot?application_version=5.7#sharkobstacle)
