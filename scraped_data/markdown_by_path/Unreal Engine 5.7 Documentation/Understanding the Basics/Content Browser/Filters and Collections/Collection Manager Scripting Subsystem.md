<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/collection-manager-scripting-subsystem?application_version=5.7 -->

# Collection Manager Scripting Subsystem

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
6. [Content Browser](/documentation/en-us/unreal-engine/content-browser-in-unreal-engine "Content Browser")
7. [Filters and Collections](/documentation/en-us/unreal-engine/filters-and-collections-in-unreal-engine "Filters and Collections")
8. Collection Manager Scripting Subsystem

# Collection Manager Scripting Subsystem

The Collection Manager Scripting Subsystem adds a new field for more precise asset management.

On this page

## Overview

The **Collection Manager Scripting Subsystem** was created to provide access to the Collection System through Blueprints. This includes the ability to create and delete collections, as well as add, remove, and search for assets within a given collection.

Collection management is currently exposed to Blueprints through the **Asset Tags Subsystem**. This system offers both editor and game functionality for collections. The editor functionality includes the ability to create, delete, and modify collections, while the game functionality offers only the ability to read and search collections.

## Limitations the Collection Manager Subsystem Addresses

There are two limitations with the Asset Tags Subsystem that are addressed by the new system.

### Content Containers

Prior to Unreal Engine 5.6, all collections were stored and associated with a base game project. In order to support more modular workflows (e.g. metaverse workflow projects), **Collection Containers** were introduced. These offer the ability for sets of collections to be associated with a project other than the base game project. Collection Manager Scripting Subsystem allows Blueprints to access these containers, which gives a Blueprint author access to collections across different projects.

[![Blueprints image of Get Base Game container as an asset source.](https://dev.epicgames.com/community/api/documentation/image/e1cfa000-627e-4487-815c-754e827738f4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e1cfa000-627e-4487-815c-754e827738f4?resizing_type=fit)

In the example above, the Base Game Collection Container is just one of many potential sources for collections.

### Collection Accessibility

Under the hood, collections have three different accessibility levels:

* **Local**: Not source controlled. Stored locally on the user’s computer and accessible only to that user.
* **Private**: Source controlled but only accessible to the user that authored it.
* **Shared**: Source controlled and accessible by anyone on the team.

Asset Tags Subsystem does not expose these share types to Blueprints, making it impossible to differentiate between collections of the same name but with different share types. In its current form, when a collection name is provided, the system returns the first found item with a matching name. This can be problematic if two collections share the same name but different share types, as the Blueprint author may inadvertently target the wrong collection.

[![Image of the Destroy Asset function with a warning message.](https://dev.epicgames.com/community/api/documentation/image/54806eca-eb47-4c79-9931-cacfc8f6a241?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/54806eca-eb47-4c79-9931-cacfc8f6a241?resizing_type=fit)

In the example above, if there are multiple collections with the name “ExampleCollection”, but different share types (one Local and one Shared), which would be deleted?

Collection Manager Scripting Subsystem exposes the share type, requiring an author to be explicit about which collection they’re targeting:

[![Image of the new field for Collection Share Type.](https://dev.epicgames.com/community/api/documentation/image/973a83a2-58c0-41ff-b221-6ccc1ab3433e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/973a83a2-58c0-41ff-b221-6ccc1ab3433e?resizing_type=fit)

In the example above, there can only be one “ExampleCollection” with a share-type of Local, so that there is no way to inadvertently delete the wrong one.

### Additional Improvements

While the Asset Tags Subsystem could have been extended, there were two primary motivations for creating a new subsystem.

| Improvement | Description |
| --- | --- |
| **Clearer Naming for Improved Discoverability** | By giving it a name that matches the underlying feature, it will be easier for Blueprint authors to discover the system and know what it’s used for. |
| **Editor-Only Implementation** | While the Asset Tags Subsystem compiles for both editor and game, Collection Manager Scripting Subsystem compiles **only for editor**, removing any ambiguity as to how it should be used. |

## Functionality Changes

The following Asset Tags Subsystem **editor-only** functions are now deprecated, and should be transitioned to their Collection Manager Scripting Subsystem equivalent:

| Deprecated Functions: | Current Functions: |
| --- | --- |
| Asset Tags Subsystem | Collection Manager Scripting Subsystem |
| `CreateCollection` | `CreateCollection` |
| `DestroyCollection` | `DestroyCollection` |
| `RenameCollection` | `RenameCollection` |
| `ReparentCollection` | `ReparentCollection` |
| `EmptyCollection` | `EmptyCollection` |
| `AddAssetToCollection` | `AddAssetToCollection` |
| `AddAssetDataToCollection` | `AddAssetDataToCollection` |
| `AddAssetPtrToCollection` | `AddAssetPtrToCollection` |
| `AddAssetsToCollection` | `AddAssetsToCollection` |
| `AddAssetDatasToCollection` | `AddAssetDatasToCollection` |
| `AddAssetPtrsToCollection` | `AddAssetPtrsToCollection` |
| `RemoveAssetFromCollection` | `RemoveAssetFromCollection` |
| `RemoveAssetDataFromCollection` | `RemoveAssetDataFromCollection` |
| `RemoveAssetPtrFromCollection` | `RemoveAssetPtrFromCollection` |
| `RemoveAssetsFromCollection` | `RemoveAssetsFromCollection` |
| `RemoveAssetDatasFromCollection` | `RemoveAssetDatasFromCollection` |
| `RemoveAssetPtrsFromCollection` | `RemoveAssetPtrsFromCollection` |
|  | `GetCollectionContainers` |
|  | `GetCollections` |
|  | `CollectionExists` |
|  | `GetCollectionsByName` |
|  | `GetAssetsInCollection` |
|  | `GetCollectionsContainingAsset` |
|  | `GetCollectionsContainingAssetData` |
|  | `GetCollectionsContainingAssetPtr` |
|  | `GetBaseGameCollectionContainer` |

The following **in-game** functions remain supported for use at runtime:

* `CollectionExists`
* `GetCollections`
* `GetAssetsInCollection`
* `GetCollectionsContainingAsset`
* `GetCollectionsContainingAssetData`
* `GetCollectionsContainingAssetPtr`

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Overview](/documentation/en-us/unreal-engine/collection-manager-scripting-subsystem?application_version=5.7#overview)
* [Limitations the Collection Manager Subsystem Addresses](/documentation/en-us/unreal-engine/collection-manager-scripting-subsystem?application_version=5.7#limitationsthecollectionmanagersubsystemaddresses)
* [Content Containers](/documentation/en-us/unreal-engine/collection-manager-scripting-subsystem?application_version=5.7#contentcontainers)
* [Collection Accessibility](/documentation/en-us/unreal-engine/collection-manager-scripting-subsystem?application_version=5.7#collectionaccessibility)
* [Additional Improvements](/documentation/en-us/unreal-engine/collection-manager-scripting-subsystem?application_version=5.7#additionalimprovements)
* [Functionality Changes](/documentation/en-us/unreal-engine/collection-manager-scripting-subsystem?application_version=5.7#functionalitychanges)
