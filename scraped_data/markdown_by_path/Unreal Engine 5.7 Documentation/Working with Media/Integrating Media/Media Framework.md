<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/media-framework-in-unreal-engine?application_version=5.7 -->

# Media Framework

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
7. Media Framework

# Media Framework

Working with Media Playback functionality in Unreal Engine.

![Media Framework](https://dev.epicgames.com/community/api/documentation/image/18a4dd68-4095-4ca0-9f96-cd50c761812b?resizing_type=fill&width=1920&height=335)

 On this page

![A GIF showing media playing inside Unreal Engine](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f3bf4143-807c-4e22-8765-7957208c9b81/mediaframework.gif)

While there is currently a **Startup Movie Player** system in UE, it can only be used for playing startup movies while the Engine loads up. It cannot be used to play movies in-game,
say for instance as part of a UI element or perhaps on a Static Mesh in your level like a movie playing on a TV. This is where the **Media Framework** comes in, as not only
will it allow you to do both of the examples presented above, it will also provide much more general media playback capabilities (outlined below) and is also scheduled to replace the deprecated Startup Movie Player framework in a future engine release.

The Media Framework in Unreal Engine is:

* Both Engine & Slate Agnostic
* Able to support Localized Audio & Video Tracks
* Accessible in the Content Browser, Material Editor, & Sound System
* Available for use with Blueprint & the UMG UI Designer
* Able to support Streaming Media
* Able to Fast Forward, Reverse, Play, Pause, & Scrub Media
* Able to support Pluggable Players

As stated above, the Media Framework itself is both Engine and Slate agnostic, which means it can be used in pretty much any application not just the game engine or the Editor. There are layers on top of the framework that provide media playback capabilities to other sub-systems as well, such as **Engine**, **Blueprints**, **Slate**, and
the **UMG UI Designer**. This will cover most expected use cases, such as in-game textures & UI, in-Editor video tutorials, and Marketplace videos.

This page contains several links to additional documentation regarding Media Framework. It is recommended that you check out the Overview page for more of a breakdown of the features of Media Framework as well as the How-To and Quick Start pages for step-by-step instructions to working with Media Framework.

## Essentials

[![Electra Media Player](images/static/document_list/empty_thumbnail.svg)

Electra Media Player](/documentation/en-us/unreal-engine/electra-media-player-in-unreal-engine)
[![Media Editor Reference](images/static/document_list/empty_thumbnail.svg)

Media Editor Reference](/documentation/en-us/unreal-engine/media-editor-reference-for-unreal-engine)
[![Media Framework Overview](images/static/document_list/empty_thumbnail.svg)

Media Framework Overview](/documentation/en-us/unreal-engine/media-framework-overview-for-unreal-engine)
[![Media Framework Quick Start](images/static/document_list/empty_thumbnail.svg)

Media Framework Quick Start](/documentation/en-us/unreal-engine/media-framework-quick-start-for-unreal-engine)
[![Media Framework Technical Reference](images/static/document_list/empty_thumbnail.svg)

Media Framework Technical Reference](/documentation/en-us/unreal-engine/media-framework-technical-reference-for-unreal-engine)
[![Media Framework Tutorials](images/static/document_list/empty_thumbnail.svg)

Media Framework Tutorials](/documentation/en-us/unreal-engine/media-framework-unreal-engine-tutorials)

* [vfx](https://dev.epicgames.com/community/search?query=vfx)
* [media framework](https://dev.epicgames.com/community/search?query=media%20framework)
* [video playback](https://dev.epicgames.com/community/search?query=video%20playback)
* [media player](https://dev.epicgames.com/community/search?query=media%20player)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Essentials](/documentation/en-us/unreal-engine/media-framework-in-unreal-engine?application_version=5.7#essentials)
