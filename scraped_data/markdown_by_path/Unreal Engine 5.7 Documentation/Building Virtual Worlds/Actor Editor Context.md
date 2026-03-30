<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/actor-editor-context-in-unreal-engine?application_version=5.7 -->

# Actor Editor Context

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
6. Actor Editor Context

# Actor Editor Context

An introduction to Actor Editor Context, a system for organizing the Actors in your Level

![Actor Editor Context](https://dev.epicgames.com/community/api/documentation/image/350b73fa-22a5-4c8a-8534-82d299574180?resizing_type=fill&width=1920&height=335)

 On this page

**Actor Editor Context** is an Editor feature that you can use to set a [Level](/documentation/en-us/unreal-engine/levels-in-unreal-engine), [Data Layer](/documentation/en-us/unreal-engine/world-partition---data-layers-in-unreal-engine), [Level Instance](/documentation/en-us/unreal-engine/level-instancing-in-unreal-engine), or [Outliner Actor Folder](/documentation/en-us/unreal-engine/outliner-in-unreal-engine) as the **current editor context**. When set to current, any Actors you add to the Viewport are assigned to the current context.
Assigning a current Actor Editor Context helps keep your world organized when adding a large number of Actors by assigning them to a specified context automatically, such as keeping all the trees in an environment in a Trees Outliner folder and assigning them to a Trees Data Layer.

[![The Actor Editor Context set to the Trees Data Layer and Trees Actor Folder](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3cca89d7-92ac-41cd-ac26-6c74effb7d78/trees-folder-data-layer.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3cca89d7-92ac-41cd-ac26-6c74effb7d78/trees-folder-data-layer.png)

The Actor Editor Context set to the Trees Data Layer and Trees Actor Folder. Click image for full size.

A widget in the lower-right corner of the Viewport displays the currently active Level, Level Instance, Data Layer, or Actor Folder.

## Setting the Current Context

### Current Level

In worlds that don't use [World Partition](/documentation/en-us/unreal-engine/world-partition-in-unreal-engine), knowing which level you are working in is an integral part of the sublevel workflow. After adding sublevels to your Level using the Levels window, the Actor Editor Context displays the current Level:

[![Level window showing the Persistent Level with one sublevel named SubLevel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6b4cd66c-6d99-43fd-b61f-53a44033d425/current-sublevel-window.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6b4cd66c-6d99-43fd-b61f-53a44033d425/current-sublevel-window.png)

Level window showing the Persistent Level with one sublevel named SubLevel. Click image for full size.

[![Actor Editor Context showing SubLevel as the current level. ](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a2181695-0276-45da-ba12-31143574079e/current-sublevel.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a2181695-0276-45da-ba12-31143574079e/current-sublevel.png)

Actor Editor Context showing SubLevel as the current level. Click image for full size.

Using the dropdown menu in the Actor Editor Context widget, you can specify the current Level. All Actors you add to the Viewport are assigned to that Level.

[![Click the dropdown to change the current Level](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/31701556-8837-423b-a516-5997db3124f6/current-sublevel-select.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/31701556-8837-423b-a516-5997db3124f6/current-sublevel-select.png)

Click the dropdown to change the current Level.

### Current Level Instance

Level Instancing is a Level-based workflow that creates prefabricated **Level Instances** you can place in your world more than once. When editing a Level Instance, Unreal Engine creates a new empty context and the Actor Editor Context widget displays the current Level Instance:

[![Actor Editor Context showing the current open Level Instance](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ff1d1b51-0470-4711-8b14-e638d780fc1c/current-level-instance.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ff1d1b51-0470-4711-8b14-e638d780fc1c/current-level-instance.png)

Actor Editor Context showing the current open Level Instance. Click image for full size.

All Actors you add to the Viewport are assigned to the currently open Level Instance. When you commit your changes to the Level Instance, the editor returns you to your previous Actor Editor Context.

### Current Data Layer

Data Layers control the loading and unloading of Actors both in the editor and at runtime. Unlike Levels, Actors can be assigned to more than one Data Layer.
To set the current Data Layer (or Layers):

1. If needed, open the **Data Layers Outliner** by selecting **Window > World Partition > Data Layer Outliner**.
2. Right-click the Data Layer you want to make current and select **Make Current Data Layer (s)**.

[![Data Layer Outliner showing the Trees Data Layer set to current](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4e2450ed-d2fa-4eea-8a60-1cca0ebaf66b/current-data-layer-outliner.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4e2450ed-d2fa-4eea-8a60-1cca0ebaf66b/current-data-layer-outliner.png)

Data Layer Outliner showing the Trees Data Layer set to current.

This adds the selected Data Layer to the current context. Its name and assigned debug color now display in the Actor Editor Context widget.

[![Actor Editor Context widget showing Trees as the current Data Layer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1d6678e1-48b1-4675-af5e-e320f6b42786/current-data-layer.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1d6678e1-48b1-4675-af5e-e320f6b42786/current-data-layer.png)

Actor Editor Context widget showing Trees as the current Data Layer. Click image for full size.

All Actors you add to the Viewport are assigned to the current Data Layer (or Layers). To clear the current Data Layer context, right-click in the Data Layer Outliner and select **Clear Current Data Layer(s)** or click the **X** button located in that section of the Actor Editor Context widget.

[![Clear the current Data Layer by clicking the X button in the Actor Editor Context widget](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/620ffbb0-56f7-43cf-98f7-4c43532132db/clear-data-layer.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/620ffbb0-56f7-43cf-98f7-4c43532132db/clear-data-layer.png)

Clear the current Data Layer by clicking the X button in the Actor Editor Context widget.

### Current Actor Folder

Similar to Data Layers, you can also assign a current Actor Folder in the Outliner.
To set the current Actor Folder:

1. If needed, open the **Outliner** by selecting **Window > Outliner** and selecting one of the four Outliner instances.
2. Right-click the folder you want to make current, then select **Make Current Folder** from the context menu.

[![Outliner showing Trees as the current Actor Folder](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/27cdd14f-f6c6-41d7-bd45-4b03e4770d9e/clear-actor-folder-outliner.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/27cdd14f-f6c6-41d7-bd45-4b03e4770d9e/clear-actor-folder-outliner.png)

Outliner showing Trees as the current Actor Folder.

This adds the selected folder to the current context. Its name now displays in the Actor Editor Context widget.

[![Actor Editor Context widget showing Trees as the current Actor Folder](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fa29f8d7-2bd5-453c-adaf-c13b61167a0f/current-actor-folder.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fa29f8d7-2bd5-453c-adaf-c13b61167a0f/current-actor-folder.png)

Actor Editor Context widget showing Trees as the current Actor Folder. Click image for full size.

All Actors you add to the Viewport are assigned to the current Actor Folder. To clear this context, right-click in the Outliner and select **Clear Current Folder** or click the **X** button located in that section of the Actor Editor Context widget.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/08375947-c78b-49f6-848e-57577a368601/clear-actor-folder.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/08375947-c78b-49f6-848e-57577a368601/clear-actor-folder.png)

Clear the current Actor Folder by clicking the X button in the Actor Editor Context widget.

## Toggling Actor Editor Context in the Viewport

The Actor Editor Context widget is enabled by default. To disable it, follow these steps:

1. Click the **Viewport Options** button in the top-left corner of the Viewport, then select **Advanced Settings**. This opens the **Editor Preferences** window.

   [![Click the Viewport options button and select Advanced Settings at the bottom](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cb9d7f1c-8a74-41c1-b142-d73f793124ab/viewport-settings.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cb9d7f1c-8a74-41c1-b142-d73f793124ab/viewport-settings.png)

   Click the Viewport options button and select Advanced Settings at the bottom.
2. Navigate to the **Look and Feel** section of the **Level Editor - Viewports** settings and clear the **Show Actor Editor Context** checkbox.

   [![The Level Editor - Viewports settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f7ba416b-1566-4ee0-96e4-f3d310a74244/look-and-feel-toggle.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f7ba416b-1566-4ee0-96e4-f3d310a74244/look-and-feel-toggle.png)

   The Level Editor - Viewports settings. Click image for full size.

* [outliner](https://dev.epicgames.com/community/search?query=outliner)
* [landscape](https://dev.epicgames.com/community/search?query=landscape)
* [building virtual worlds](https://dev.epicgames.com/community/search?query=building%20virtual%20worlds)
* [actor editor context](https://dev.epicgames.com/community/search?query=actor%20editor%20context)
* [data layers](https://dev.epicgames.com/community/search?query=data%20layers)
* [level instancing](https://dev.epicgames.com/community/search?query=level%20instancing)
* [level editor](https://dev.epicgames.com/community/search?query=level%20editor)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Setting the Current Context](/documentation/en-us/unreal-engine/actor-editor-context-in-unreal-engine?application_version=5.7#settingthecurrentcontext)
* [Current Level](/documentation/en-us/unreal-engine/actor-editor-context-in-unreal-engine?application_version=5.7#currentlevel)
* [Current Level Instance](/documentation/en-us/unreal-engine/actor-editor-context-in-unreal-engine?application_version=5.7#currentlevelinstance)
* [Current Data Layer](/documentation/en-us/unreal-engine/actor-editor-context-in-unreal-engine?application_version=5.7#currentdatalayer)
* [Current Actor Folder](/documentation/en-us/unreal-engine/actor-editor-context-in-unreal-engine?application_version=5.7#currentactorfolder)
* [Toggling Actor Editor Context in the Viewport](/documentation/en-us/unreal-engine/actor-editor-context-in-unreal-engine?application_version=5.7#togglingactoreditorcontextintheviewport)
