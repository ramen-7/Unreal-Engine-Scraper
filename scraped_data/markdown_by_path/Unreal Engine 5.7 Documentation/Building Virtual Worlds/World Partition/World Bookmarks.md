<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/world-bookmarks?application_version=5.7 -->

# World Bookmarks

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
5. [Building Virtual Worlds](/documentation/en-us/unreal-engine/building-virtual-worlds-in-unreal-engine "Building Virtual Worlds")
6. [World Partition](/documentation/en-us/unreal-engine/world-partition-in-unreal-engine "World Partition")
7. World Bookmarks

# World Bookmarks

World Bookmarks are used to help project organization and navigation within large open worlds.

On this page

## Overview

In Unreal Engine, regular bookmarks and **World Bookmarks** serve different purposes. Regular bookmarks are used for navigating within the level editor's viewport, where you can jump to specific camera locations or editor states. World Bookmarks are primarily used within Blueprints to mark specific locations or nodes within the graph, facilitating doing work with complex logic.

World Bookmarks is a system to help project organization and navigation within large open worlds. A bookmark can store the state of various systems in the editor, for example:

* The active world
* Camera location/orientation
* Loaded regions in a partitioned world
* States of data layers
* Actor editor context

There is a dedicated World Bookmark Outliner window to help users access and organize bookmarks. As assets, bookmarks can be local to a user or shared with everyone.

There are also console commands to capture/restore bookmarks as text, such as in workflows similar to bugit/bugitgo.

## Creating a World Bookmark

1. In Unreal Engine, in the top file menu, go to **Window > World Partition > World Bookmarks**.
2. This will open a dedicated World Bookmark Outliner window. To create a new bookmark, select the **+** button.

   [![World Bookmark window with the plus sign button in the upper right of the window.](https://dev.epicgames.com/community/api/documentation/image/e9835203-7f35-4dda-9fcd-b3cf6cbfd404?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e9835203-7f35-4dda-9fcd-b3cf6cbfd404?resizing_type=fit)
3. You will be prompted to select or create a **folder location** for your World Bookmark. Click **Save**. The new World Bookmark will populate in your folder.

   World Bookmarks are a new asset type.

   [![Image of the World Bookmark icon in a folder in the Content Browser.](https://dev.epicgames.com/community/api/documentation/image/800a7813-4055-4b47-ba4d-4adc01860d26?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/800a7813-4055-4b47-ba4d-4adc01860d26?resizing_type=fit)

## World Bookmark Settings

### Individual Settings

Navigate to ****Window > World Partition > World Bookma**rk** to open the bookmark modal. **Click** on your bookmark to open its settings menu. Each World Bookmark contains the following information:

1. Actor Editor Context
2. Category
3. Camera (Location, Rotation, and Camera FOVAngle)
4. World

   [![Image of World Bookmark settings menu.](https://dev.epicgames.com/community/api/documentation/image/dc6c5bae-5439-46d1-8a9f-275e57ece482?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dc6c5bae-5439-46d1-8a9f-275e57ece482?resizing_type=fit)

### Global Bookmark Settings

Navigate to **Window > World Partition > World Bookmark** to open the bookmark modal. Click on the **Settings icon** (cog) to access the global settings menu.

[![Image of the global settings icon (cog).](https://dev.epicgames.com/community/api/documentation/image/48551904-4e07-4f3b-9da1-737a47c81c32?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/48551904-4e07-4f3b-9da1-737a47c81c32?resizing_type=fit)

| Setting Name | Description |
| --- | --- |
| View Type |  |
| **List** | Provides a list of all the bookmarks according to the show settings. |
| **Tree** | Provides a tree view of the World Bookmarks asset locations. |
| Show |  |
| --- | --- |
| **Show only for Current World** | Displays only bookmarks that are bound to the current world. |
| **Show only Uncontrolled Bookmarks** | Displays only local bookmarks that are kept in an uncontrolled changelist. |
| **Show only Favorite Bookmarks** | Displays only bookmarks that were flagged as favorite. |
| **Show only Last Recently Used Bookmarks** | Displays only bookmarks that were recently used. |
| **L**ast Recently Used Items**** | You can set the quantity of bookmarks to be shown by clicking into the field. |

## Using the Command Line

World Bookmarks are also usable from the command line interface.

[![Image of command line options for World Bookmarks.](https://dev.epicgames.com/community/api/documentation/image/82308587-9bba-4a25-81e1-6dcdfa73834d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/82308587-9bba-4a25-81e1-6dcdfa73834d?resizing_type=fit)

**WorldBookmark.capture** captures the current World Bookmark details and posts to the Output Log:

[![Image of command line showing the world bookmark capture command.](https://dev.epicgames.com/community/api/documentation/image/5cab8c10-19a2-41f2-98ee-daa3750a06ce?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5cab8c10-19a2-41f2-98ee-daa3750a06ce?resizing_type=fit)

**WorldBookmark.CaptureToClipboard** captures the current world bookmark details and creates a pasteable argument that can be restored using ****WorldbookMarks.Restor**e** and **WorldBookmark.RestoreFromClipboard**.

`WorldBookmark.Restore` will restore a world bookmark when you provide an argument created with `WorldBookmark.capture`. Example argument:

worldbookmark.restore BMAMgBAAD5AAAAeJyFj9FOwjAUhl9l6TV0hbWOcbc0w5sJi0S9MMbUrjFLSk/TVsWQvbsdKIGg8a75z/ef83WHfBBBeTR/3KFnroX3S7FRaI7StXSdDemdcUroqsUP4HRbtV0Atx46aIQ+hmhgr2MnXXTOh0Y5D4Y3TXojrD/Nqq3YWK1ijH9NUT/6T6GU8fhBgYMJahvOfcTFfD/hoLWSoQMTly7BDOhLaa3+vFy4MjWI+Kfg3tSfQrV6V/pQwydvHiknzpXkPqtBiu/7OZ3mOKPJeMYoxaRI2IxleMqO7C2EH3ac5ZgVyYRMML1KCCbkSC1W96V51dGqIP1T/wVQI52J======================================================

`WorldBook.RestoreFromClipboard` will restore a world bookmark from the clipboard when you have copied the world bookmark argument into your clipboard.

## Use Cases

Being able to send a bookmark of the location with all its camera settings is huge. It's a considerable time saver when it comes to team collaboration, as it allows us to create shareable locations as assets. For example, if you notice the VFX in an area is causing slowdown, you can quickly create a world book and pass that location onto the relevant team to be fixed. If you find a bug in a complicated scene, you can quickly and efficiently copy and paste the relevant location details.

Being able to categorize a bookmark for its usage, i.e. VFX, scripted events, etc., allows for quick level navigation. For example, if I wanted to look at how the Cassini demo was performing, I could create a number of bookmarks around different locations, label them PCG performance, and quickly monitor them going forward.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Overview](/documentation/en-us/unreal-engine/world-bookmarks?application_version=5.7#overview)
* [Creating a World Bookmark](/documentation/en-us/unreal-engine/world-bookmarks?application_version=5.7#creatingaworldbookmark)
* [World Bookmark Settings](/documentation/en-us/unreal-engine/world-bookmarks?application_version=5.7#worldbookmarksettings)
* [Individual Settings](/documentation/en-us/unreal-engine/world-bookmarks?application_version=5.7#individualsettings)
* [Global Bookmark Settings](/documentation/en-us/unreal-engine/world-bookmarks?application_version=5.7#globalbookmarksettings)
* [Using the Command Line](/documentation/en-us/unreal-engine/world-bookmarks?application_version=5.7#usingthecommandline)
* [Use Cases](/documentation/en-us/unreal-engine/world-bookmarks?application_version=5.7#usecases)
