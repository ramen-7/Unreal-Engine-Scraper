<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-audio-implementation-in-parrot?application_version=5.7 -->

# Audio Engine Implementation in Parrot

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
8. Audio Engine Implementation in Parrot

# Audio Engine Implementation in Parrot

Learn about how Parrot uses the audio engine in Unreal Engine.

![Audio Engine Implementation in Parrot](https://dev.epicgames.com/community/api/documentation/image/df5836e0-d9cd-4f86-98c8-b98ddc1e7e7c?resizing_type=fill&width=1920&height=335)

 On this page

The Unreal Engine 5 audio features can support projects with various audio requirements. Importing audio can be done by navigating to a content folder, clicking the **Import** button, or navigating to the folder using your OS explorer. The engine then creates a `.uasset` with your sound. Unreal Engine supports `.wav`, `.ogg`, `.flac`, `.aif`, `.opus`, `.mp3` files. Files can have a bit depth of 16 or 24 and any sample rate. Internally, Unreal Engine stores imported audio files in a 16-bit uncompressed `.wav` format.

For more information on the Audio Engine in Unreal, see the following documentation:

* [Audio Engine Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/audio-engine-overview-in-unreal-engine?application_version=5.5)
* [Importing Audio Files](https://dev.epicgames.com/documentation/en-us/unreal-engine/importing-audio-files)
* [Audio In Unreal Engine 5](https://dev.epicgames.com/documentation/en-us/unreal-engine/audio-in-unreal-engine-5)

Sound cues are objects used to play sounds at runtime. Sound cues select from a set of audio files that represent the same concept. For example, you may have a sound cue for “Wind”, and at runtime the sound cue would choose from multiple audio files of wind sounds for playback. An example of this in Parrot is the water splash sound cue: `Content/Sound/SFX/WaterSplash/CUE_WaterSplashSound`

Sound classes are asset types used by the audio engine to group multiple sounds together and then alter the parameters of all relevant sound waves at the same time. Parrot has **MainSoundClass**, which mixes both **Music** and **SFX**.

[![The MainSoundClass node connected to the Music node and SFX node](https://dev.epicgames.com/community/api/documentation/image/524782fc-bed3-42b5-aed0-8f46c1e0b68c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/524782fc-bed3-42b5-aed0-8f46c1e0b68c?resizing_type=fit)

Sound class mixes can apply volume thresholds and are automatically applied whenever any sound in a sound class is played.

## Parrot Specific Implementation

In Parrot, most sounds used are sound cues that contain one sound. Volume and pitch are set per sound cue with overall volume controlled by a default sound class and sound mixes for settings. To streamline this for music, Parrot has a custom Audio Subsystem.

## Pickup Example

Pickups are an example of simple sound cues that play once and are then destroyed. Pickups use coin sound effects from [opengameart.org](http://opengameart.org). The imported source assets are located under `Content/Assets/OpenGameArt/8bitCoinSounds`. The created sound cues for each of these files are under `Content/Sound/SFX/Pickups`. Call **Play Sound 2D** with the desired sound cue in **BP\_PickupBase** when the pickup event is initiated.

All Pickups support VFX, SFX, and need to be destroyed on contact. This can be done in the BP\_PickupBase class.

[![The Play Sound 2D node in BP_PickupBase](https://dev.epicgames.com/community/api/documentation/image/e0dc96fa-dbd2-4b30-9669-dad1fc25261a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e0dc96fa-dbd2-4b30-9669-dad1fc25261a?resizing_type=fit)

You can use Play Sound 2D here because the sound doesn't need to be spatially relevant in the world. If the sound needed to be spatially relevant, you could use Play Sound At Location instead.

## Music Loops

Music works much like the standard sound cues. Importing the sound files and setting up sound cues is the same as sound effects. However, there are some additional steps:

* On the imported sound asset itself, make sure that the virtualization mode is set to **Play When Silent**. This is important for the music as it allows the player to respect the volume settings. Without it, when the volume is muted, the sound will be destroyed and will no longer play when you restore your volume.
* In the sound cue itself, click on the track node and ensure that **Looping** is set.

## Sound Settings

All the settings in Parrot are related to various sound volumes.

Under `Content/Sound/Settings` there is a sound class asset called **MainSoundClass**. Under **Child Classes,**you can point your sound class to any other relevant sound classes. The default child classes includes **SFX** and **Music**.

[![The MainSoundClass settings, showing the Child Classes, SFX and Music](https://dev.epicgames.com/community/api/documentation/image/6162a2d0-f944-4270-b43a-5b948145113d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6162a2d0-f944-4270-b43a-5b948145113d?resizing_type=fit)

In the same folder, there is an asset called **DefaultSoundMix**. You can set **Sound Class Effects** in the  **MainSoundClass** settings. Make sure that **Apply To Children** is enabled.

[![The Sound Class Effects settings, with Apply to Children enabled](https://dev.epicgames.com/community/api/documentation/image/5c739974-5eff-4b19-8a8e-c567641fbf17?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5c739974-5eff-4b19-8a8e-c567641fbf17?resizing_type=fit)

In each sound cue, make sure that the class is set to the appropriate category. For pickups, use the SFX class.

[![The SFX class set on a sound cue](https://dev.epicgames.com/community/api/documentation/image/17ff72fd-cac4-42dc-8e6f-94c8611cfb98?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/17ff72fd-cac4-42dc-8e6f-94c8611cfb98?resizing_type=fit)

To modify your mix’s settings at runtime, you can use the **Set Sound Class Mix Override** node with the **Push Sound Mix Modifier** node. This applies any changes you’ve made.

[![The Set Sound Class Mix Override node with the Push Sound Mix Modifier node](https://dev.epicgames.com/community/api/documentation/image/a8e2c894-1117-4035-ae44-953e2fead2b5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a8e2c894-1117-4035-ae44-953e2fead2b5?resizing_type=fit)

This is a blueprint example, but in Parrot this is usually done in C++ in the Audio Subsystem.

## Parrot Audio Subsystem

This section explains what the Audio Subsystem implementation does. To learn why Parrot has a subsystem for Audio, see [Subsystems in Parrot](https://dev.epicgames.com/documentation/en-us/unreal-engine/subsystems-in-parrot-in-unreal-engine).

The Parrot Audio Subsystem is a C++ class is called `UParrotAudioSubsystem`. It shares the lifetime of the game instance, because the volume settings can be changed at any time from the main menu or the pause menu. When a playthrough is happening, the Audio subsystem also listens for game state changes. Then, you can change the music track when a level starts, when a level is completed, or when the player goes out of bounds.

**WBP\_SettingScreen** shows the Audio Subsystem in action. Slider values from UMG (Unreal Motion Graphics UI Designer) are passed to the subsystem in C++. The runtime sound mixer updates whenever the values change. The **Fade In** time is zero so that volume changes are applied immediately.

[![The WBP_SettingScreen Blueprint](https://dev.epicgames.com/community/api/documentation/image/2ba2d8ce-d271-49a0-a95a-499f935e8024?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2ba2d8ce-d271-49a0-a95a-499f935e8024?resizing_type=fit)

Settings get saved with the **Save Audio Settings** node.

[![The Save Audio Settings node](https://dev.epicgames.com/community/api/documentation/image/bf0a7382-0c13-46cf-9b74-7161214e9dd8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bf0a7382-0c13-46cf-9b74-7161214e9dd8?resizing_type=fit)

To see the details of how serialization works for saving these settings, see [Serialization in Parrot](https://dev.epicgames.com/documentation/en-us/unreal-engine/serialization-in-parrot-in-unreal-engine).

The music in Parrot is done almost entirely in C++. Because of the structure of Parrot, where each map is a level, there is an `AParrotWorldSettings` class. You can use it to set any world specific data, like the level music. The Audio Subsystem queries the world settings and pulls the track it needs. To react to state changes after the game has started, bind to the Parrot Game State on `WorldBeginPlay`.

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [fab](https://dev.epicgames.com/community/search?query=fab)
* [parrot game sample](https://dev.epicgames.com/community/search?query=parrot%20game%20sample)
* [learning](https://dev.epicgames.com/community/search?query=learning)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Parrot Specific Implementation](/documentation/en-us/unreal-engine/unreal-engine-audio-implementation-in-parrot?application_version=5.7#parrotspecificimplementation)
* [Pickup Example](/documentation/en-us/unreal-engine/unreal-engine-audio-implementation-in-parrot?application_version=5.7#pickupexample)
* [Music Loops](/documentation/en-us/unreal-engine/unreal-engine-audio-implementation-in-parrot?application_version=5.7#musicloops)
* [Sound Settings](/documentation/en-us/unreal-engine/unreal-engine-audio-implementation-in-parrot?application_version=5.7#soundsettings)
* [Parrot Audio Subsystem](/documentation/en-us/unreal-engine/unreal-engine-audio-implementation-in-parrot?application_version=5.7#parrotaudiosubsystem)
