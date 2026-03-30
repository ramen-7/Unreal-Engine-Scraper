<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/electra-protron-player-in-unreal-engine?application_version=5.7 -->

# Electra Protron Player

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
5. [Working with Media](/documentation/en-us/unreal-engine/working-with-media-in-unreal-engine "Working with Media")
6. [Integrating Media](/documentation/en-us/unreal-engine/integrating-media-in-unreal-engine "Integrating Media")
7. [Media Framework](/documentation/en-us/unreal-engine/media-framework-in-unreal-engine "Media Framework")
8. [Electra Media Player](/documentation/en-us/unreal-engine/electra-media-player-in-unreal-engine "Electra Media Player")
9. Electra Protron Player

# Electra Protron Player

An overview of the Electra Protron player.

On this page

![Electra Protron in action](https://dev.epicgames.com/community/api/documentation/image/367a0ba4-129a-46d0-865c-7db159b87480?resizing_type=fit)

**Electra Protron** is a version of the Electra player optimized for local filesystems and container based media. It is meant to help you achieve smooth in-editor scrubbing, looping, and seeking performance, not only in-editor but also for live video performance. For best scrubbing performance, use the Apple Pro Res codec.

## Enabling Electra Protron in the Editor

In the **Project Settings**, you can find a new section called **Electra Protron Factory**. This provides a way for you to override the default player to pick Protron as preferred player over Electra for the following cases:

* In-Editor: Protron only gets picked while in editor.
* In-Game: Protron also gets picked while in Standalone or Packaged modes.

[![Electra Protron Factory in the Project Settings](https://dev.epicgames.com/community/api/documentation/image/69380293-86b0-4762-ae67-6a4cbf69db21?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/69380293-86b0-4762-ae67-6a4cbf69db21?resizing_type=fit)

## Enabling Protron Player in File Media Source Assets

The Protron player is part of the Electra plugin so there are no other prerequisites for enabling it. By default, UE uses the Electra player instead of the Protron player. If you do not want to use the Project Settings override, you can still use the Protron player directly with any File Media Source asset you want. Proceed as follows:

* Open the asset in the editor.
* In the **Details** panel under **Platforms**, open the menu for **Windows**, then select **Electra Protron**.

Any further playback request for the asset, for example from the Media Plate actor, the Media Track in Sequencer, or the Media Viewer, now uses Protron Player.

[![Electra Protron in the Details panel of a File Media Source asset](https://dev.epicgames.com/community/api/documentation/image/ffbe287a-f6ad-477f-9f89-61975225e77c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ffbe287a-f6ad-477f-9f89-61975225e77c?resizing_type=fit)

## Verifying Protron

To ensure UE uses Protron when appropriate,  you can verify the player in-use in various areas where the engine plays media assets.

### File Media Source

You can verify Protron is used when playing a File Media Source asset. When you open and play the media asset, you can see the current active Player name displayed under Media Details during playback.

[![Electra Protron in the File Media Source asset Media Details](https://dev.epicgames.com/community/api/documentation/image/f59980e7-66c0-4dba-84f0-16a44d9e6d29?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f59980e7-66c0-4dba-84f0-16a44d9e6d29?resizing_type=fit)

### Media Plate Actor

The same Media Details section is also available in the Details panel of the Media Plate Actor.

[![Electra Protron in the Media Plate actor Details panel](https://dev.epicgames.com/community/api/documentation/image/4db8d896-9deb-464d-9314-3485dbbc56ce?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4db8d896-9deb-464d-9314-3485dbbc56ce?resizing_type=fit)

### Sequencer

The Sequencer Media sections display Player and Media information during playback.

[![Electra Protron in Sequencer](https://dev.epicgames.com/community/api/documentation/image/99cf2530-0287-4654-a867-2a1cf9864292?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/99cf2530-0287-4654-a867-2a1cf9864292?resizing_type=fit)

### Media Viewer

The Media Viewer plugin supports video playback, and displays Player and Media information as an overlay during playback.

[![Electra Protron in the Media Viewer](https://dev.epicgames.com/community/api/documentation/image/b16ad924-f3d7-42aa-8486-3ea14417ce79?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b16ad924-f3d7-42aa-8486-3ea14417ce79?resizing_type=fit)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Enabling Electra Protron in the Editor](/documentation/en-us/unreal-engine/electra-protron-player-in-unreal-engine?application_version=5.7#enablingelectraprotronintheeditor)
* [Enabling Protron Player in File Media Source Assets](/documentation/en-us/unreal-engine/electra-protron-player-in-unreal-engine?application_version=5.7#enablingprotronplayerinfilemediasourceassets)
* [Verifying Protron](/documentation/en-us/unreal-engine/electra-protron-player-in-unreal-engine?application_version=5.7#verifyingprotron)
* [File Media Source](/documentation/en-us/unreal-engine/electra-protron-player-in-unreal-engine?application_version=5.7#filemediasource)
* [Media Plate Actor](/documentation/en-us/unreal-engine/electra-protron-player-in-unreal-engine?application_version=5.7#mediaplateactor)
* [Sequencer](/documentation/en-us/unreal-engine/electra-protron-player-in-unreal-engine?application_version=5.7#sequencer)
* [Media Viewer](/documentation/en-us/unreal-engine/electra-protron-player-in-unreal-engine?application_version=5.7#mediaviewer)
