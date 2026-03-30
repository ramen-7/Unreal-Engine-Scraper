<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-unreal-stage-outliner-in-unreal-engine?application_version=5.7 -->

# Using the Unreal Stage Outliner

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
9. Using the Unreal Stage Outliner

# Using the Unreal Stage Outliner

The Unreal Stage Outliner will show any actors in the scene and provides some handy tools, including filtering, visibility, and multi-select, as well as some utility tools, including duplicating or deleting selected actors.

![Using the Unreal Stage Outliner](https://dev.epicgames.com/community/api/documentation/image/6a42dd2a-8282-40fa-9e17-2def7f63a00e?resizing_type=fill&width=1920&height=335)

Learn to use this **Experimental** feature, but use caution when shipping with it.

 On this page

## The Outliner

The Outliner can optionally be displayed at any time and will list out all of the ICVFX content within the scene and show anything that is currently selected.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/57a02346-a8cf-46ca-adf5-b49bea9d89fc/outliner-1.gif)

## Outliner Tools

The Outliner menu bar offers the following tools for managing ICVFX content.

### Filtering

As with the Outliner in desktop Unreal Engine, the list of content can be filtered by type to more easily find a desired actor, especially in larger and more complex scenes.

There is also a 'search by' to find content by name.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1f78c8b8-4221-43b3-8169-a60774e0394f/outliner-2.gif)

### Visibility

The visibility button in Unreal Stage toggles the Actor Hidden in Game property, which will hide the selected content from view. Hidden content will no longer be visible in nDisplay on the LED volume, but it is still available for further manipulation (such as making adjustments without disrupting other work on-stage, or finding it to make it visible again) through the Editor and in-app. Hidden content will display as italicized in the Outliner to distinguish it from content that is visible.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/093c053c-ccce-4dad-8eb6-4799e3984531/outliner-3.gif)

### Multi-Select

Multi-selection mode can be toggled on and off via the Outliner. When on, selecting content will add it to the selection to create a selection set instead of changing the selection from one actor to another.

If multi-selecting content with different visibility states (ex. one visible, one hidden), Unreal Stage will treat the selection as visible. This means that tapping the visibility button will hide all selected actors on the LED Volume.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2b24feba-255d-4cce-b6da-d1c8465bb20b/outliner-4.gif)

### Ellipsis Menu

* Additional utility operations can be found in the ellipsis menu:
* Focus Selected
* The Editor Preview will be zoomed and panned to focus on the selected actor.
* Duplicate Selected
* Delete Selected
* Rename Selected

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b4809dce-4f3d-4dce-bf84-383638a329f9/outliner-5.gif)

### Swipe Operations

Actors in the Outliner can also be swiped left and right for quicker and easier access to key operations:

* Swipe Right
* Toggle Visibility
* Swipe Left
* Delete Selected

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d1f3c74d-9f74-41d5-98cf-11545aedbb1e/outliner-6.gif)

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

* [The Outliner](/documentation/en-us/unreal-engine/using-the-unreal-stage-outliner-in-unreal-engine?application_version=5.7#theoutliner)
* [Outliner Tools](/documentation/en-us/unreal-engine/using-the-unreal-stage-outliner-in-unreal-engine?application_version=5.7#outlinertools)
* [Filtering](/documentation/en-us/unreal-engine/using-the-unreal-stage-outliner-in-unreal-engine?application_version=5.7#filtering)
* [Visibility](/documentation/en-us/unreal-engine/using-the-unreal-stage-outliner-in-unreal-engine?application_version=5.7#visibility)
* [Multi-Select](/documentation/en-us/unreal-engine/using-the-unreal-stage-outliner-in-unreal-engine?application_version=5.7#multi-select)
* [Ellipsis Menu](/documentation/en-us/unreal-engine/using-the-unreal-stage-outliner-in-unreal-engine?application_version=5.7#ellipsismenu)
* [Swipe Operations](/documentation/en-us/unreal-engine/using-the-unreal-stage-outliner-in-unreal-engine?application_version=5.7#swipeoperations)
