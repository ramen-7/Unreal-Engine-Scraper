<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/placing-actors-in-unreal-engine?application_version=5.7 -->

# Placing Actors

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
6. [Actors and Geometry](/documentation/en-us/unreal-engine/actors-and-geometry-in-unreal-engine "Actors and Geometry")
7. Placing Actors

# Placing Actors

Shows how you can place Actors such as props, lights, and cameras into your Level.

![Placing Actors](https://dev.epicgames.com/community/api/documentation/image/c5c55d41-9fc1-4b36-a6b2-2c01f263dbb7?resizing_type=fill&width=1920&height=335)

 On this page

An **Actor** is any object that can be placed into a **Level**, from **Static Meshes** that create your game's environment, to sounds, cameras, player characters, and so on. This page will show you how to place these Actors into your Level so you can bring your world to life.

Placing an Actor into your Level creates an **instance** of the object the Actor is based on.

Adding Actors to your Level also adds them to the **World Outliner**, which is located in the upper-right corner of the Unreal Editor by default. Refer to the [World Outliner](/documentation/en-us/unreal-engine/outliner-in-unreal-engine) documentation for more information.

## Required Setup

Before you can follow the workflows described on this page, you must create a new project and open it in Unreal Editor. The examples on this page will use the [Third Person Template](/documentation/404), but you can choose any template you like.

## Using the Place Actors Panel

This section will show you how to place Actors from the **Place Actors** panel. To open this panel, from the main menu, go to **Window > Place Actor**. The Place Actors panel will open at the left-hand side of the Unreal Editor window.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bd48ecaf-d68c-4bda-8e76-9a6e466e54fa/place-actors-panel.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bd48ecaf-d68c-4bda-8e76-9a6e466e54fa/place-actors-panel.png)

The Place Actors panel in the Unreal Editor. Click the image for full size.

Let's go ahead and place a simple cube into your Level. In the **Place Actors** panel, left-click the **Cube** Actor, then drag it into the Level, as shown in the GIF below.

![Placing a cube Static Mesh Actor into the Level](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f97ee698-51e2-44c4-95b6-73f903ec2265/place-actors-example.gif)

You can do this for any Actor in the **Place Actors** panel.

### Place Actors Panel Interface

![Place Actors panel interface](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/69b5fa16-8d60-4146-905e-73d2f14bfdaf/place-actors-panel-ui.png)

The **Place Actors** panel consists of three major areas:

1. Search
2. Filters
3. Asset View

#### 1. Search

Use the **Search** bar to find any Actor by name.

#### 2. Filters

Use these tabs to quickly switch between Actor categories.

| Tab | Contents |
| --- | --- |
| **Recently Placed** | Rolling history of up to the last 20 types of Actors you placed in your Level. This history is project-specific. |
| **Basic** | Basic Actors such as planes, Pawns, and trigger volumes. Also contains empty Actors and Characters. |
| **Lights** | Different types of lights you can place into your Level. |
| **Shapes** | Simple primitives (cube, sphere, cylinder, cone, and plane). |
| **Cinematic** | A cinematic camera and related Actors that you can use to simulate real-world camera movement. |
| **Visual Effects** | Volumes that visually affect part of all of your Level in some way, such as fog, post-processing, and reflections. |
| **Geometry** | Geometry brushes you can use to quickly block out or prototype a level.  Use the Add or Subtract radio buttons to change whether the brush adds geometry to the Level or removes existing geometry. |
| **Volumes** | All placeable Volume types. |
| **All Classes** | All placeable Actors. |

#### 3. Asset View

This view shows all Assets that correspond to the search or filters you selected.

An **Asset** is any piece of content within an Unreal Engine project. All Actors are Assets.

## Placing Actors Using the Context Menu

This section will show you how to place Actors through a **context menu**. A context menu is any menu that opens when you right-click inside Unreal Engine.

You will select the Actor you want to place from the [Content Browser](/documentation/en-us/unreal-engine/content-browser-in-unreal-engine). The fastest way to open an instance of the Content Browser is to click the **Content Drawer** button in the lower-left corner of the Unreal Editor window. If you want this instance to persist when it loses focus (when you click away from it), click the **Dock in Editor** button in its upper-right corner.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/25158317-fa31-4561-933d-8d268fba42ed/content-browser.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/25158317-fa31-4561-933d-8d268fba42ed/content-browser.png)

The Content Browser in the Unreal Editor. Click the image for full size.

To place an Actor from the Content Browser, follow the steps below:

1. In the **Content Browser**, find the **Asset** you want to place.
2. Left-click the **Asset** to select it.
3. With the **Asset** still selected, right-click anywhere in the **Level Viewport** to open the context menu.
4. Click the **Asset** under the **Place Actor** section.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/84001531-65ec-4bd1-977a-97486ecb1351/place-actors-context-menu.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/84001531-65ec-4bd1-977a-97486ecb1351/place-actors-context-menu.png)

Placing an Actor from the Content Browser into a Level using the context menu. Click the image for full size.

After selecting the Asset from the context menu, you will see it appear inside your Level at the coordinates where you right-clicked.

You can also use the context menu to quickly add different types of Assets to your level, even when you have a specific Asset selected in the **Content Browser**. To see the types of Assets you can add, right-click anywhere in your **Level Viewport**, then hover over the **Place Actor** section. Click any Actor you see in this section to place it.

### Replacing Actors

You can also use the context menu to replace one or more Actors in the **Level Viewport** with an Asset you selected in the **Content Browser**. This can be useful if you want to swap multiple Assets at once.

To replace one or more Actors, follow the steps below:

1. In the **Content Browser**, select the Actor you want to replace another Actor with.
2. Right-click the Actor or Actors in the **Level Viewport** to open the context menu.
3. Click **Replace Selected Actors with**.

You can also use this method to replace the selected Actor with any Actor that is also available from the **Place Actors** panel.

## Placing Actors Using Drag and Drop

You can add Actors to your Level from the Content Browser by using drag and drop. To do this, follow the steps below:

1. In the **Content Browser**, find the **Asset** you want to place.
2. Left-click the **Asset**, then drag it into the **Level Viewport** and drop it at the location where you want to place it.

![Placing an actor into the Level using drag-and-drop](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9baf9cb1-b5d6-4937-bfc1-ed70aaf1369c/place-actor-drag-and-drop.gif)

When you drag and drop an Asset from the Content Browser, the following types of Actors are created for the associated type of Asset:

* **Blueprint**: Places an instance of the Blueprint.
* **Skeletal Mesh**: Places a SkeletalMeshActor.
* **Static Mesh**: Places a StaticMeshActor.
* **Sound Cue**: Places an AmbientSound.
* **Sound Wave**: Places an AmbientSound.

## Placing Actors from the Class Viewer

A more advanced method of placing Actors is by using the **Class Viewer**, which is a hierarchical list of all classes used by the Unreal Editor.

To place an Actor from the Class Viewer, follow these steps:

1. Open the **Class Viewer**. From the main menu, go to **Tools > Class Viewer**.

   Any Actor that can be placed in the level will be tinted blue in this window.
2. Select the **Asset** you want to place, then drag it into the **Level Viewport**.

![Placing an Actor from the Class Viewer using drag-and-drop](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/98477981-af3f-44a6-94f8-837e589b83c3/place-actor-class-viewer.gif)

For more information, refer to the [Class Viewer](/documentation/en-us/unreal-engine/class-viewer-in-unreal-engine) page.

* [actors](https://dev.epicgames.com/community/search?query=actors)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Required Setup](/documentation/en-us/unreal-engine/placing-actors-in-unreal-engine?application_version=5.7#requiredsetup)
* [Using the Place Actors Panel](/documentation/en-us/unreal-engine/placing-actors-in-unreal-engine?application_version=5.7#usingtheplaceactorspanel)
* [Place Actors Panel Interface](/documentation/en-us/unreal-engine/placing-actors-in-unreal-engine?application_version=5.7#placeactorspanelinterface)
* [1. Search](/documentation/en-us/unreal-engine/placing-actors-in-unreal-engine?application_version=5.7#1search)
* [2. Filters](/documentation/en-us/unreal-engine/placing-actors-in-unreal-engine?application_version=5.7#2filters)
* [3. Asset View](/documentation/en-us/unreal-engine/placing-actors-in-unreal-engine?application_version=5.7#3assetview)
* [Placing Actors Using the Context Menu](/documentation/en-us/unreal-engine/placing-actors-in-unreal-engine?application_version=5.7#placingactorsusingthecontextmenu)
* [Replacing Actors](/documentation/en-us/unreal-engine/placing-actors-in-unreal-engine?application_version=5.7#replacingactors)
* [Placing Actors Using Drag and Drop](/documentation/en-us/unreal-engine/placing-actors-in-unreal-engine?application_version=5.7#placingactorsusingdraganddrop)
* [Placing Actors from the Class Viewer](/documentation/en-us/unreal-engine/placing-actors-in-unreal-engine?application_version=5.7#placingactorsfromtheclassviewer)
