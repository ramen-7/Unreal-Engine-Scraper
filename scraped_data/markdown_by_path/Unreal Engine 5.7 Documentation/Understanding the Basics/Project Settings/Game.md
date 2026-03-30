<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/game-section-of-the-unreal-engine-project-settings?application_version=5.7 -->

# Game

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
5. [Understanding the Basics](/documentation/en-us/unreal-engine/understanding-the-basics-of-unreal-engine "Understanding the Basics")
6. [Project Settings](/documentation/en-us/unreal-engine/project-settings-in-unreal-engine "Project Settings")
7. Game

# Game

Reference for the Game section of the Unreal Engine Project Settings.

On this page

## Asset Manager

### Asset Manager

| **Section** | **Description** |
| --- | --- |
| **Primary Asset Types to Scan** | List of asset types to scan at startup. |
| **Directories to Exclude** | List of directories to exclude from scanning for Primary Assets, useful to exclude test assets. |
| **Primary Asset Rules** | List of specific asset rule overrides. |
| **Custom Primary Asset Rules** | List of game-specific asset rule overrides for types, this will not do anything by default. |
| **Only Cook Production Assets** | If true, `DevelopmentCook` assets will error when they are cooked, you should enable this on production branches. |
| **Should Manager Determine Type and Name** | If true, the asset manager will determine the type and name for Primary Assets that do not implement `GetPrimaryAssetId`, by calling `DeterminePrimaryAssetIdForObject` and using the `.ini` settings.  This works in both cooked and uncooked builds, but is slower than directly implementing `GetPrimaryAssetId` on the native asset. |
| **Should Guess Type and Name in Editor** | If true, `PrimaryAsset` Type / Name will be implied for assets in the editor even if `bShouldManagerDetermineTypeAndName` is false.  This guesses the correct ID for content that hasn't been resaved after `GetPrimaryAssetId` was implemented. |
| **Should Acquire Missing Chunks on Load** | If true, this will query the platform chunk install interface to request missing chunks for any requested primary asset loads. |
| **Should Warn About Invalid Assets** | If true, the asset manager will warn when it is told to load or do something with assets it does not know about. |

### Redirects

| **Section** | **Description** |
| --- | --- |
| **Primary Asset Id Redirects** | Redirect from `Type:Name` to `Type:NameNew`. |
| **Primary Asset Type Redirects** | Redirect from `Type` to `TypeNew`. |
| **Asset Path Redirects** | Redirect from `/game/assetpath` to `/game/assetpathnew`. |

### Asset Registry

| **Section** | **Description** |
| --- | --- |
| **Metadata Tags For Asset Registry** | The metadata tags to be transferred to the Asset Registry. |

## Asset Tools

### Advanced Copy

| **Section** | **Description** |
| --- | --- |
| **Advanced Copy Customizations** | List of rules to use when advanced copying assets. |

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [basics](https://dev.epicgames.com/community/search?query=basics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Asset Manager](/documentation/en-us/unreal-engine/game-section-of-the-unreal-engine-project-settings?application_version=5.7#assetmanager)
* [Asset Manager](/documentation/en-us/unreal-engine/game-section-of-the-unreal-engine-project-settings?application_version=5.7#assetmanager-2)
* [Redirects](/documentation/en-us/unreal-engine/game-section-of-the-unreal-engine-project-settings?application_version=5.7#redirects)
* [Asset Registry](/documentation/en-us/unreal-engine/game-section-of-the-unreal-engine-project-settings?application_version=5.7#assetregistry)
* [Asset Tools](/documentation/en-us/unreal-engine/game-section-of-the-unreal-engine-project-settings?application_version=5.7#assettools)
* [Advanced Copy](/documentation/en-us/unreal-engine/game-section-of-the-unreal-engine-project-settings?application_version=5.7#advancedcopy)
