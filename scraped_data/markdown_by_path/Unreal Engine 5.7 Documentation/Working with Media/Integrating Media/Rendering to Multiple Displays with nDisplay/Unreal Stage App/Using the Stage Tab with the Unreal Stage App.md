<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-stage-tab-with-the-unreal-stage-app-in-unreal-engine?application_version=5.7 -->

# Using the Stage Tab with the Unreal Stage App

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
7. [Rendering to Multiple Displays with nDisplay](/documentation/en-us/unreal-engine/rendering-to-multiple-displays-with-ndisplay-in-unreal-engine "Rendering to Multiple Displays with nDisplay")
8. [Unreal Stage App](/documentation/en-us/unreal-engine/unreal-stage-app-for-unreal-engine "Unreal Stage App")
9. Using the Stage Tab with the Unreal Stage App

# Using the Stage Tab with the Unreal Stage App

Use the Stage tab to interact with your stage and see a live preview of changes.

![Using the Stage Tab with the Unreal Stage App](https://dev.epicgames.com/community/api/documentation/image/db7fc7ea-bdef-49d3-a6b2-c851dbd54d01?resizing_type=fill&width=1920&height=335)

Learn to use this **Experimental** feature, but use caution when shipping with it.

 On this page

## Editor Preview

The Stage tab shows a live preview of nDisplay's output on the LED wall with touch-capable, interactive ICVFX content. This is the same preview shown in Unreal Engine's nDisplay Editor Preview and ICVFX Editor on the desktop.

### View Options

You can toggle the view of the nDisplay Editor Preview via the dropdown menu. There are four different view options:

* **Dome**
  + The most commonly-used view option for hemispheric LED volumes with ceilings
* **Orthographic**
  + Another popular projection option for hemispheric stages
* **Perspective**
  + Typically most useful for configurations with flat LED walls
* **UV**
  + A flattened representation of the LED volume that can more easily show both the walls and ceiling simultaneously and requires secondary UVs to be set up for the nDisplay configuration meshes

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ee72e954-5576-4247-9907-ea724e07699a/stagetab-1.gif)

### Navigation

The preview can be navigated to view exactly what you want. Interact with the preview as follows:

* **Pinch Zoom**
  + Zoom in and out of the preview
* **One Finger**
  + Tumble the preview
* **Two Fingers**
  + Pan across the preview

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2126c8b7-4048-48e6-a8ea-20cd83efe5f3/stagetab-2.gif)

## Content Controls

The same ICVFX content that can be placed in Unreal Engine's ICVFX Editor can also be placed via Unreal Stage:

* Light Cards
* Flags
* Color Correction Windows
* Chromakey Cards
* Templates

### Place Actors

Use the Add button in the top-right to add new content at the default location, which may be off-screen. You can also press and hold at a specific location in the Stage tab to add content at that exact spot.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/15aa653c-351a-4251-a34d-c831da3cd82d/stagetab-3.gif)

### Position and Reposition Content

You can reposition any ICVFX content placed within the scene by using a single finger to press and hold the object until it is selected. You can then drag it freely via touch and position it wherever you want.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/17a9ca52-151e-4e1b-af82-4ef8ff30b998/stagetab-4.gif)

### Object Mode

Object Mode allows you to further modify content beyond placement. Using the same press-and-hold action as before, select the content and toggle to Object Mode. Controls will only focus on the selected content while in Object Mode, so you can quickly and easily make changes without accidentally modifying anything else in the scene. Pinch zoom will scale the size of the selected object. You can also quickly reposition the selected content while in Object Mode by tapping anywhere on the screen to grab it before dragging it to your desired location.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bee80ae6-9888-4006-8814-ca690345e2d8/stagetab-5.gif)

* [getting started](https://dev.epicgames.com/community/search?query=getting%20started)
* [experimental](https://dev.epicgames.com/community/search?query=experimental)
* [virtual production](https://dev.epicgames.com/community/search?query=virtual%20production)
* [ndisplay](https://dev.epicgames.com/community/search?query=ndisplay)
* [icvfx](https://dev.epicgames.com/community/search?query=icvfx)
* [virtual sets](https://dev.epicgames.com/community/search?query=virtual%20sets)
* [bronze](https://dev.epicgames.com/community/search?query=bronze)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Editor Preview](/documentation/en-us/unreal-engine/using-the-stage-tab-with-the-unreal-stage-app-in-unreal-engine?application_version=5.7#editorpreview)
* [View Options](/documentation/en-us/unreal-engine/using-the-stage-tab-with-the-unreal-stage-app-in-unreal-engine?application_version=5.7#viewoptions)
* [Navigation](/documentation/en-us/unreal-engine/using-the-stage-tab-with-the-unreal-stage-app-in-unreal-engine?application_version=5.7#navigation)
* [Content Controls](/documentation/en-us/unreal-engine/using-the-stage-tab-with-the-unreal-stage-app-in-unreal-engine?application_version=5.7#contentcontrols)
* [Place Actors](/documentation/en-us/unreal-engine/using-the-stage-tab-with-the-unreal-stage-app-in-unreal-engine?application_version=5.7#placeactors)
* [Position and Reposition Content](/documentation/en-us/unreal-engine/using-the-stage-tab-with-the-unreal-stage-app-in-unreal-engine?application_version=5.7#positionandrepositioncontent)
* [Object Mode](/documentation/en-us/unreal-engine/using-the-stage-tab-with-the-unreal-stage-app-in-unreal-engine?application_version=5.7#objectmode)
