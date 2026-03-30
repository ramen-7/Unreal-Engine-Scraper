<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/patching-content-delivery-and-dlc-in-unreal-engine?application_version=5.7 -->

# Patching and DLC

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
5. [Sharing and Releasing Projects](/documentation/en-us/unreal-engine/sharing-and-releasing-projects-for-unreal-engine "Sharing and Releasing Projects")
6. Patching and DLC

# Patching and DLC

Information about packaging content for patching and delivering DLC

![Patching and DLC](https://dev.epicgames.com/community/api/documentation/image/ae2e9ccb-18b5-4600-959c-7b436fc637e1?resizing_type=fill&width=1920&height=335)

 On this page

**Unreal Engine** can divide content into **.pak** files and deliver them to users separately from the main executable. This functionality supports DLC and patching for live services.

## General Information

The following pages contain information about the UE cooking and chunking process, how to prepare .pak files for distribution, and reference information for mounting chunks.

[![Preparing Assets for Chunking](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d13d74df-0e33-445e-bb02-23f8649ce2fc/placeholder_topic.png)

Preparing Assets for Chunking

How to divide assets into chunks and cook them into packaging files](/documentation/en-us/unreal-engine/preparing-assets-for-chunking-in-unreal-engine)
[![Patching Overview](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/95e75c05-3635-4203-8ad3-ec66779cc188/placeholder_topic.png)

Patching Overview

Creating updated content packages for updating your project after release.](/documentation/en-us/unreal-engine/updating-unreal-engine-projects-with-patches-after-release)
[![How To Create a Patch (Platform-Agnostic)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e23ca17e-7278-4d40-9d6c-5ead01bd4fe9/create-patch-topic.png)

How To Create a Patch (Platform-Agnostic)

This page describes how to create a patch for an existing project.](/documentation/en-us/unreal-engine/how-to-create-a-patch-in-unreal-engine)

## Chunk Downloader Plugin

The **ChunkDownloader** plugin is a general patching solution intended for games that need to deliver a large number of small files.

[![Setting Up the ChunkDownloader Plugin](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/eb858fc8-dadd-4fa9-bde0-45108b1d93e0/placeholder_topic.png)

Setting Up the ChunkDownloader Plugin

How to set up a Project Settings and Plugins for working with ChunkDownloader](/documentation/en-us/unreal-engine/setting-up-the-chunkdownloader-plugin-in-unreal-engine)
[![Hosting a Manifest and Assets for ChunkDownloader](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b58cc13d-a6e9-49aa-a311-2ad5009cce89/placeholder_topic.png)

Hosting a Manifest and Assets for ChunkDownloader

Setting up a local host web site](/documentation/en-us/unreal-engine/hosting-a-manifest-and-assets-for-chunkdownloader-in-unreal-engine)
[![Implementing ChunkDownloader Ingame](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3d1b4d02-5e8e-4e97-ab74-36ce4a978250/placeholder_topic.png)

Implementing ChunkDownloader Ingame

How to integrate ChunkDownloader into your project, using Visual Studio and Blueprints, and how to test out the system on your local machine.](/documentation/en-us/unreal-engine/implementing-chunkdownloader-in-your-gameplay-in-unreal-engine)

## Google Play Asset Delivery (GooglePAD)

The **GooglePAD** plugin uses Google's **Play Asset Delivery** system on the Google Play store. This patching solution is a companion to the **Android App Bundle** system, which delivers customized APKs that are optimized for users' individual devices.

You can read more about GooglePAD in the [Google Play Asset Delivery Reference](/documentation/en-us/unreal-engine/using-google-play-asset-delivery-in-unreal-engine).

* [patching](https://dev.epicgames.com/community/search?query=patching)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [General Information](/documentation/en-us/unreal-engine/patching-content-delivery-and-dlc-in-unreal-engine?application_version=5.7#generalinformation)
* [Chunk Downloader Plugin](/documentation/en-us/unreal-engine/patching-content-delivery-and-dlc-in-unreal-engine?application_version=5.7#chunkdownloaderplugin)
* [Google Play Asset Delivery (GooglePAD)](/documentation/en-us/unreal-engine/patching-content-delivery-and-dlc-in-unreal-engine?application_version=5.7#googleplayassetdelivery(googlepad))
