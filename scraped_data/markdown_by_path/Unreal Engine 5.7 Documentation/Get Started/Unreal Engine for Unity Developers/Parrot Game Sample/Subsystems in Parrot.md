<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/subsystems-in-parrot-in-unreal-engine?application_version=5.7 -->

# Subsystems in Parrot

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
8. Subsystems in Parrot

# Subsystems in Parrot

Learn about how Parrot uses subsystems.

![Subsystems in Parrot](https://dev.epicgames.com/community/api/documentation/image/ca976f5d-d15e-4a5f-be35-84705985fdf2?resizing_type=fill&width=1920&height=335)

 On this page

Parrot uses [subsystems](https://dev.epicgames.com/documentation/en-us/unreal-engine/programming-subsystems-in-unreal-engine) in Unreal Engine. Subsystems provide engine-managed lifetimes and add extension points for common functions. If you’ve used a [Singleton Pattern](https://en.wikipedia.org/wiki/Singleton_pattern) in Unity, subsystems fill a similar need. Subsystems are tied directly to the following scopes in the engine:

* Engine
* Editor
* Game Instance
* World
* Local Player

As these scopes enter different states, so do subsystems, and they can react accordingly.

A common reason to use subsystems is when you need to expose common C++ functionality to Blueprint and you know the expected lifetime.

## Audio Subsystem Example

Parrot uses an [audio subsystem](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-audio-implementation-in-parrot) for the following reasons:

* The subsystem is tied to the Game Instance’s lifetime without being on the Game Instance itself.
* The subsystem is accessible in C++ and Blueprint.
* Sound settings such as volume can be changed at any time from anywhere in the game.
* Manipulating audio settings through a subsystem provides a centralized debugging access point.
* Audio settings can be saved at any point by any external system.

To see this working in practice, look at `UParrotAudioSubsystem`. The audio subsystem interacts most with UI systems as that’s where the audio can be manipulated by the player. However, the flexibility is there if audio needs to be changed elsewhere. Whenever you’re adding a system to your game, consider whether a subsystem would be a useful abstraction.

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [fab](https://dev.epicgames.com/community/search?query=fab)
* [parrot game sample](https://dev.epicgames.com/community/search?query=parrot%20game%20sample)
* [learning](https://dev.epicgames.com/community/search?query=learning)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Audio Subsystem Example](/documentation/en-us/unreal-engine/subsystems-in-parrot-in-unreal-engine?application_version=5.7#audiosubsystemexample)
