<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-bookmarks-for-blueprint-graphs-in-unreal-engine?application_version=5.7 -->

# Blueprint Bookmarks

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
5. [Blueprints Visual Scripting](/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine "Blueprints Visual Scripting")
6. [Blueprint Editor Reference](/documentation/en-us/unreal-engine/user-interface-reference-for-the-blueprints-visual-scripting-editor-in-unreal-engine "Blueprint Editor Reference")
7. Blueprint Bookmarks

# Blueprint Bookmarks

Product documentation including reference and guides for Unreal Engine 4

![Blueprint Bookmarks](https://dev.epicgames.com/community/api/documentation/image/1be55b90-29e6-4842-9fc9-589e80dc2064?resizing_type=fill&width=1920&height=335)

 On this page

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6134570a-6510-4200-bdf2-0531b1af87e3/bookmarksheroimage.png)

With **Blueprint Bookmarks** you can create named Bookmarks in any function graph in the Blueprint Editor. This bookmark will capture the position and zoom level of the Viewport and the active tab you were viewing when you created the bookmark. Bookmarks are stored locally on your machine, so they won't affect the Blueprint itself, and syncing your content will not overwrite your Bookmarks with another user's Bookmarks.

## Creating Bookmarks

To create a Blueprint Bookmark:

1. With the Graph and Zoom position you wish to Bookmark, click the **Star** icon in the upper-left of the graph.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ec699d8f-bdfb-4e57-ba84-ddf010c0e619/blueprintbookmarks_creation_01.png "BlueprintBookmarks_Creation_01.png")
2. In the **New Bookmark** dialog box, enter your desired name and click the **Add** button.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/640b47c9-4f7e-4d90-a9a9-5455bd09aedc/blueprintbookmarks_creation_02.png "BlueprintBookmarks_Creation_02.png")

## Viewing and Using Bookmarks

To view or use a previously created Bookmark, select the **Bookmarks** option from the **Window** menu.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0f266d95-09b5-49e3-b577-5c4621ac66b9/blueprintbookmarks_using_01.png "BlueprintBookmarks_Using_01.png")

This will open the **Bookmarks** menu that displays all the Bookmarks for the current asset as well as any [Comment Nodes](/documentation/en-us/unreal-engine/comments-in-unreal-engine#commentboxes).

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/90849468-0ffe-4057-bb9c-237387fa151b/blueprintbookmarks_using_02.png "BlueprintBookmarks_Using_02.png")

In the Bookmarks window, clicking the **Eye** icon in the upper-right corner will expand additional options. Disabling **Show Comment Blocks** removes Comment Nodes from being displayed in the menu.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ede26655-d433-4985-bf02-1b6975ce3815/blueprintbookmarks_using_03.png "BlueprintBookmarks_Using_03.png")

Enabling **Show Bookmarks for Current Graph Only** will show Bookmarks for your active Graph, while disabling it will show all Bookmarks for the asset while on any Graph.

For Bookmarks displayed in the window, you can right-click on a Bookmark (or Comment) to expand additional options.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6984ae35-60bd-4763-ba28-334d72c16eae/blueprintbookmarks_using_04.png)  
The right-click context menu enables you to **Delete** or **Rename** Bookmarks, as well as to jump directly to the selected Bookmark (or Comment).

Double-click on a Bookmark or Comment Node block to jump to that section of your Graph.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cb55e2e3-b0be-4808-bdfe-4c55c979c655/blueprintbookmarks_using_05.png "BlueprintBookmarks_Using_05.png")


When jumping to a Bookmark, the **Star** icon in the upper-left of the Graph will also be filled indicating you are at the Bookmark.

## Quick Jump Bookmarks

In addition to creating **Bookmarks**, you can create a **Quick Jump Bookmark**, similarly to how Bookmarks work in the [Level Editor Viewport](https://docs.unrealengine.com/5.0/en-US/editor-viewports-in-unreal-engine/). As with labeled Bookmarks in the Blueprint Editor, Quick Jump Bookmarks will persist across Editor sessions and are local to the user and machine where they were created.

To assign and use a Quick Jump Bookmark:

1. With a Graph open, press **Ctrl + 0-9** (any number key) to remember your current Blueprint, Graph location and Zoom level.
2. Inside any Graph, press **Shift + 0-9** (the same number from previous step) to return to that Blueprint, Graph location and Zoom level.

Quick Jump Bookmarks do not require you to have the asset open. They will automatically open the asset, Graph location and Zoom level (as shown in the example video below).




As of 4.21, Quick Jump Bookmarks are currently not displayed in the Bookmarks window.

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [blueprint bookmarks](https://dev.epicgames.com/community/search?query=blueprint%20bookmarks)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Creating Bookmarks](/documentation/en-us/unreal-engine/working-with-bookmarks-for-blueprint-graphs-in-unreal-engine?application_version=5.7#creatingbookmarks)
* [Viewing and Using Bookmarks](/documentation/en-us/unreal-engine/working-with-bookmarks-for-blueprint-graphs-in-unreal-engine?application_version=5.7#viewingandusingbookmarks)
* [Quick Jump Bookmarks](/documentation/en-us/unreal-engine/working-with-bookmarks-for-blueprint-graphs-in-unreal-engine?application_version=5.7#quickjumpbookmarks)
