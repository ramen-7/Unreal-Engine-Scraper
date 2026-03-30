<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/horde-and-unrealgamesync-metadata-server-for-unreal-engine?application_version=5.7 -->

# Horde and UnrealGameSync Metadata Server

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
5. [Setting Up Your Production Pipeline](/documentation/en-us/unreal-engine/setting-up-your-production-pipeline-in-unreal-engine "Setting Up Your Production Pipeline")
6. [Horde](/documentation/en-us/unreal-engine/horde-in-unreal-engine "Horde")
7. [Horde Configuration](/documentation/en-us/unreal-engine/horde-configuration-for-unreal-engine "Horde Configuration")
8. Horde and UnrealGameSync Metadata Server

# Horde and UnrealGameSync Metadata Server

An overview of using Horde and UnrealGameSync together.

![Horde and UnrealGameSync Metadata Server](https://dev.epicgames.com/community/api/documentation/image/f060b3fe-d2e7-45b6-895d-cbda2382db40?resizing_type=fill&width=1920&height=335)

 On this page

UnrealGameSync (**UGS**) is a tool designed to simplify syncing from Perforce, supporting retrieval of pre-built editor binaries for artists or correctly versioning the local build so engineers can modify content. It is a convenient hub for surfacing build health, flagging issues, and scripting common workflow tasks outside Unreal Editor.

For more information on UGS, see the [UnrealGameSync](/documentation/en-us/unreal-engine/unreal-game-sync-ugs-for-unreal-engine) docs.

Horde includes an updated version of the legacy MetadataServer IIS web app that ships alongside UGS, integrating seamlessly with Horde's CI functionality.

## Configuration

To configure UnrealGameSync to source data from Horde, add the following lines in the `UnrealGameSync.ini` config file:

```
|  |  |
| --- | --- |
|  | [Default] |
|  | ApiUrl=https://{{ HORDE_SERVER_URL }}/ugs |

Copy full snippet
```

This config file can be in a project-specific location (e.g. `{{ PROJECT_DIR }}/Build/UnrealGameSync.ini`) or in a location that applies to all projects in a stream (e.g. `{{ ENGINE_DIR }}/Programs/UnrealGameSync/UnrealGameSync.ini`).

* [horde](https://dev.epicgames.com/community/search?query=horde)
* [bronze](https://dev.epicgames.com/community/search?query=bronze)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Configuration](/documentation/en-us/unreal-engine/horde-and-unrealgamesync-metadata-server-for-unreal-engine?application_version=5.7#configuration)
