<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/serialization-in-parrot-in-unreal-engine?application_version=5.7 -->

# Serialization in Parrot

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
8. Serialization in Parrot

# Serialization in Parrot

Learn about how saving and loading works in Parrot.

![Serialization in Parrot](https://dev.epicgames.com/community/api/documentation/image/aa1c27c0-4a59-4f1e-8d77-001f34861a38?resizing_type=fill&width=1920&height=335)

 On this page

Setting up save and load functions for your game vary depending on the complexity of your game. Unreal Engine has [serialization support](https://dev.epicgames.com/documentation/en-us/unreal-engine/saving-and-loading-your-game-in-unreal-engine) to handle saving and loading. Unreal Engine has a **SaveGame** object class that can be derived in Blueprint or C++ and works for saving simple variables. If your game requires more complicated saving and loading behavior, see this talk on [Serialization Best Practices and Techniques](https://dev.epicgames.com/community/learning/talks-and-demos/4ORW/unreal-engine-serialization-best-practices-and-techniques). If you want to write user configurable settings, use the `UGameUserSettings` utility class.

`UParrotGameUserSettings` in Parrot is derived from `UGameUserSettings`. This saves and loads the player configurable settings that Parrot needs.

## Audio Settings Example

In Parrot, the player can configure audio settings. Parrot saves the following float values:

* Main Volume
* Music Volume
* SFX Volume

Make sure that the project is using the correct game user settings class. This can be configured under **Edit** > **Project Settings** > **Engine - General Settings** by changing the **Game User Settings Class** field to point to **ParrotGameUserSettings**.

[![The Game User Settings Class field pointing to ParrotGameUserSettings](https://dev.epicgames.com/community/api/documentation/image/79210b7e-a2a4-4987-b98c-d4bd928b6ff7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/79210b7e-a2a4-4987-b98c-d4bd928b6ff7?resizing_type=fit)

Then, cast the user settings to the **UParrotGameSettings** type, and call the save function. This can be seen in `UParrotAudioSubsystem`, which is covered in [Audio Engine Implementation in Parrot](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-audio-implementation-in-parrot).

Another useful feature of using a `UGameUserSettings` derived class is that deserialization is not an issue. User settings are read and automatically applied when the game is started.

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [fab](https://dev.epicgames.com/community/search?query=fab)
* [parrot game sample](https://dev.epicgames.com/community/search?query=parrot%20game%20sample)
* [learning](https://dev.epicgames.com/community/search?query=learning)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Audio Settings Example](/documentation/en-us/unreal-engine/serialization-in-parrot-in-unreal-engine?application_version=5.7#audiosettingsexample)
