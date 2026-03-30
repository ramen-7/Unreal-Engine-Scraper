<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/level-editor-in-unreal-engine?application_version=5.7 -->

# Level Editor

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
6. Level Editor

# Level Editor

An overview of the interface used for the design and construction of game levels and environments.

![Level Editor](https://dev.epicgames.com/community/api/documentation/image/fa122be2-b098-4ff7-87e8-32ab634916d9?resizing_type=fill&width=1920&height=335)

 On this page

The **Level Editor** provides the core level creation functionality for Unreal Editor. You will use it to create, view, and modify levels .You will modify a level mainly by placing, transforming, and editing the properties of [**Actors**](/documentation/en-us/unreal-engine/actors-and-geometry-in-unreal-engine).



In Unreal Editor, the scenes in which you create your game experience are generally referred to as [Levels](/documentation/en-us/unreal-engine/levels-in-unreal-engine). You can think of a level as a 3D environment into which you place a series of objects and geometry to define the world your players will experience. Any object that is placed in your world, be it a light, a mesh, or a character, is considered to be an Actor. Technically speaking, an Actor is a programming class used within the Unreal Engine to define an object that has 3D position, rotation, and scale data. Think of an Actor as any object that can be placed in your levels.

[![Level Editor Windows](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/683bee74-98c7-46e1-a941-f92d85727e19/01-level-editor-windows.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/683bee74-98c7-46e1-a941-f92d85727e19/01-level-editor-windows.png)

Click image for full size.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3c55f519-454f-4e57-aaa5-1675278585de/leveleditor_mac.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3c55f519-454f-4e57-aaa5-1675278585de/leveleditor_mac.png)



Creating levels begins by placing items in a map inside Unreal Editor. These items may be world geometry, decorations in the form of Brushes, Static Meshes, lights, player starts, weapons, or vehicles. Which items are added when is usually defined by the particular workflow used by the level design team.

## The Default Interface

Since the interface for Unreal Editor is highly customizable, it is possible that what you see may change from one launch to the next. Below, you can see the default interface layout.

[![Default Interface Windows](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/280e6d89-179e-45f8-a096-52641a6a90f1/02-default-interface-windows.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/280e6d89-179e-45f8-a096-52641a6a90f1/02-default-interface-windows.png)

Click image for full size.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/120d7300-dbd4-41a2-9e30-40b45783cc19/defaultinterface_mac.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/120d7300-dbd4-41a2-9e30-40b45783cc19/defaultinterface_mac.png)

1. [Tab Bar and Menu Bar](/documentation/en-us/unreal-engine/level-editor-in-unreal-engine#tabbar)
2. [Toolbar](/documentation/en-us/unreal-engine/level-editor-in-unreal-engine#toolbar)
3. [Buttom Toolbar](/documentation/en-us/unreal-engine/level-editor-in-unreal-engine#bottomtoolbar)
4. [Place Actor / Modes](/documentation/en-us/unreal-engine/level-editor-in-unreal-engine#modes)
5. [Viewports](/documentation/en-us/unreal-engine/level-editor-in-unreal-engine#viewport)
6. [Content Browser / Content Drawer](/documentation/en-us/unreal-engine/content-browser-in-unreal-engine)
7. [Outliner](/documentation/en-us/unreal-engine/level-editor-in-unreal-engine#outliner)
8. [Details](/documentation/en-us/unreal-engine/level-editor-in-unreal-engine#details)

### Tab Bar

The Level Editor has a tab along the top with the name of the current level. Tabs from other editor windows may be docked alongside this tab for quick and easy navigation, similar to a web browser.

[![Tab Bar](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d1bd62ec-bec7-401a-aaed-0b1c54d430e1/03-tab-bar.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d1bd62ec-bec7-401a-aaed-0b1c54d430e1/03-tab-bar.png)

Click image for full size.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/15e3c1b0-1c8e-4a00-affe-8bad2fee8f5b/tabbar_mac.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/15e3c1b0-1c8e-4a00-affe-8bad2fee8f5b/tabbar_mac.png)

The name of the tab reflects the level currently being edited. This is a pattern consistent throughout the editor—tabs will be named after the current asset being edited.

To the right of the Tab Bar is the name of the current project.

### Toolbar

[![Toolbar Panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b8fe1d6d-009d-4578-b8c3-38c105d18f7f/07-toolbar-panel.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b8fe1d6d-009d-4578-b8c3-38c105d18f7f/07-toolbar-panel.png)

Click image for full size.

The **Toolbar** panel displays a group of commands, providing quick access to commonly used tools and operations.

See the [**Toolbar**](/documentation/en-us/unreal-engine/level-editor-toolbar-in-unreal-engine) page for descriptions Toolbar items.

### Menu Bar

The **Menu Bar** in the editor should be familiar to anyone who has used Windows applications previously. It provides access to general tools and commands that are used when working with levels in the editor.

[![Main Menu Bar](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/540a277c-e640-4788-b14f-c88bef2da893/04-main-menu-bar.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/540a277c-e640-4788-b14f-c88bef2da893/04-main-menu-bar.png)

Click image for full size.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/94e224c0-b986-43a2-8c3e-b4a640362ecf/menubar_mac.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/94e224c0-b986-43a2-8c3e-b4a640362ecf/menubar_mac.png)

The **Console** (**`**) is a text field that allows special console commands to be entered that are recognized by the editor. The text field has an auto-complete feature that automatically lists all commands matching the characters in the field.

If are running Source Control, the button on the far right of the menu bar is indicates its status.

| Button | Name | Description |
| --- | --- | --- |
| Button Source Control On = On Button Source Control Off = Off | **Source Control Status** | Mouse over the button for connection details. A green icon can be clicked to log in to your connection. A red icon indicates that source control is not in use. Perforce and Subversion are supported. See [Source Control documentation](/documentation/en-us/unreal-engine/using-source-control-in-the-unreal-editor) for details. |

### Modes

The **Level Editor** can be put into different editing modes to enable specialized editing interfaces and workflows for editing particular types of Actors or geometry.

To display a selection of modes, in the Level Editor Toolbar, open the **Modes** dropdown.

[![Modes dropdown](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9d9193fa-4fdc-4674-bbb1-2c36dc79b316/01-modes-dropdown.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9d9193fa-4fdc-4674-bbb1-2c36dc79b316/01-modes-dropdown.png)

Click image for full size.

| Icon | Mode | Shortcut | Description |
| --- | --- | --- | --- |
| LE Tools Select | **Select** | **Shift + 1** | Activate [**Select** mode](/documentation/en-us/unreal-engine/select-mode-in-unreal-engine) to select Actors in your scene. |
| LE Tools Landscape | **Landscape** | **Shift + 2** | Activate [**Landscape** mode](/documentation/en-us/unreal-engine/landscape-outdoor-terrain-in-unreal-engine) to edit Landscape terrains. |
| LE Tools Foliage | **Foliage** | **Shift + 3** | Activate [**Foliage** Mode](/documentation/en-us/unreal-engine/foliage-mode-in-unreal-engine) to paint instanced foliage. |
| LE Tools Mesh Paint | **Mesh Paint** | **Shift + 4** | Activate [**Mesh Paint** mode](/documentation/en-us/unreal-engine/mesh-paint-mode-in-unreal-engine) to paint vertex colors and textures on Static Mesh Actors directly in the viewport. |
| LE Tools Modeling | **Modeling** | **Shift + 5** | Activate **Modeling** editing mode. |
| LE Tools Fracture | **Fracture** | **Shift-6** | Activate [**Fracture** mode](/documentation/en-us/unreal-engine/chaos-destruction-in-unreal-engine) to create destructible objects and environments. |
| LE Tools Brush | **Brush Editing** | **Shift + 7** | Activate [**Brush Editing** mode](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine) to modify Geometry Brushes. |
| LE Tools Animation | **Animation** | **Shift + 8** | Activate **Animation** editing mode. |

**Modes** change the primary behavior of the Level Editor for a specialized task, such as moving and transforming assets in the world, sculpting landscapes, generating foliage, creating geometry brushes and volumes, and painting on meshes. Modes panels contain a selection of tools tailored to the selected editing mode.

[![Landscape Panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b9551150-73c2-4e06-b787-def4b7666720/10-landscape-panel.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b9551150-73c2-4e06-b787-def4b7666720/10-landscape-panel.png)

Click image for full size.

The Landscape panel

You can close any panel by clicking the small "X" in the upper-right corner of the tab. You can also hide any panel by right-clicking on the tab, and then clicking **Hide Tab** on the context menu that appears. To reopen a panel that you have closed, click that panel's name on the **Window** menu.

### Viewport

The **Viewport** panel is your window into the worlds you create in Unreal Engine.

[![Viewport Panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3338b356-4644-4a58-b0de-ec32f3ee9a10/08-viewport-panel.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3338b356-4644-4a58-b0de-ec32f3ee9a10/08-viewport-panel.png)

Click image for full size.

This panel contains a set of viewports, each of which can be maximized to fill the entire panel and offer the ability to display the world from one of three orthographic views (Top, Side, Front) or a perspective view giving you complete control over what you see and how you see it.

See [**Viewports**](/documentation/en-us/unreal-engine/editor-viewports-in-unreal-engine) for more information on working with viewports.

### Details

[![Details Panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ca43f43d-bb53-4108-8467-77ff171d04ff/09-details-panel.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ca43f43d-bb53-4108-8467-77ff171d04ff/09-details-panel.png)

Click image for full size.

The **Details** panel contains information, utilities, and functions for the current selection in the viewport. It contains transform edit boxes for moving, rotating, and scaling Actors, displays all of the editable properties for the selected Actors, and provides quick access to additional editing functionality depending on the type of Actor(s) selected in the viewport. For example, selected Actors can be exported to FBX and converted to another compatible type. Selection Details allow you to view the materials used by the selected Actors, if any, and quickly open them for editing.

See the [**Details**](/documentation/en-us/unreal-engine/level-editor-details-panel-in-unreal-engine) page for a more complete overview and guide to using the **Details** panel in the Level Editor.

### Outliner

[![Scene Outliner Panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b1cc6072-a611-470d-949c-663401f83233/20-scene-outliner-panel.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b1cc6072-a611-470d-949c-663401f83233/20-scene-outliner-panel.png)

Click image for full size.

The **Outliner** panel displays all of the Actors within the scene in a hierarchical tree view. You can select and modify Actors directly from the **Outliner**. Use the Info dropdown menu to display an additional column that shows Levels, Layers, or ID Names.

See the [**Outliner**](/documentation/en-us/unreal-engine/outliner-in-unreal-engine) page for details on using the **Outliner**.

### Bottom Toolbar

[![Bottom Toolbar Panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f4c99bae-51c7-4899-a529-75e7a63bcc01/22-bottom-toolbar.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f4c99bae-51c7-4899-a529-75e7a63bcc01/22-bottom-toolbar.png)

Click image for full size.

Contains shortcuts to the Command Console, Output Log, and Derived Data functionality. Also displays source control status.

See the [**Toolbar**](/documentation/en-us/unreal-engine/level-editor-toolbar-in-unreal-engine) page for descriptions Toolbar items.

### Layers

The **Layers** panel allows you to organize Actors in your Level.

[![Layer Infra](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c0cfee11-caf1-44cd-b455-496a3952574b/01-layer-infra.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c0cfee11-caf1-44cd-b455-496a3952574b/01-layer-infra.png)

Click image for full size.

Layers provide the ability to quickly select as well as control visibility of groups of related Actors.
You can use your layers to quickly un-clutter a scene leaving only the geometry and Actors that you are
working with. For example, you might be working on a building that has multiple levels but is comprised
of many modular parts. By assigning each floor to a layer, you can hide each of the floors you are not
working on making the top view much more manageable.

See the [Layers Panel](/documentation/en-us/unreal-engine/layers-panel-in-unreal-engine) page for details on using the **Layers** panel.

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [building virtual worlds](https://dev.epicgames.com/community/search?query=building%20virtual%20worlds)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [The Default Interface](/documentation/en-us/unreal-engine/level-editor-in-unreal-engine?application_version=5.7#thedefaultinterface)
* [Tab Bar](/documentation/en-us/unreal-engine/level-editor-in-unreal-engine?application_version=5.7#tabbar)
* [Toolbar](/documentation/en-us/unreal-engine/level-editor-in-unreal-engine?application_version=5.7#toolbar)
* [Menu Bar](/documentation/en-us/unreal-engine/level-editor-in-unreal-engine?application_version=5.7#menubar)
* [Modes](/documentation/en-us/unreal-engine/level-editor-in-unreal-engine?application_version=5.7#modes)
* [Viewport](/documentation/en-us/unreal-engine/level-editor-in-unreal-engine?application_version=5.7#viewport)
* [Details](/documentation/en-us/unreal-engine/level-editor-in-unreal-engine?application_version=5.7#details)
* [Outliner](/documentation/en-us/unreal-engine/level-editor-in-unreal-engine?application_version=5.7#outliner)
* [Bottom Toolbar](/documentation/en-us/unreal-engine/level-editor-in-unreal-engine?application_version=5.7#bottomtoolbar)
* [Layers](/documentation/en-us/unreal-engine/level-editor-in-unreal-engine?application_version=5.7#layers)
