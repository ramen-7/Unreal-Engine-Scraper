<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-invalidation-box-for-umg-in-unreal-engine?application_version=5.7 -->

# Invalidation Box

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
5. [Creating User Interfaces](/documentation/en-us/unreal-engine/creating-user-interfaces-with-umg-and-slate-in-unreal-engine "Creating User Interfaces")
6. [Widget Type Reference](/documentation/en-us/unreal-engine/widget-type-reference-for-umg-ui-designer-in-unreal-engine "Widget Type Reference")
7. Invalidation Box

# Invalidation Box

An overview of Invalidation Box, which helps developers optimize UI Widgets.

![Invalidation Box](https://dev.epicgames.com/community/api/documentation/image/56c01578-6c41-4151-817e-356d06396f0b?resizing_type=fill&width=1920&height=335)

 On this page

## Description

Widgets that are wrapped with an **Invalidation Box** allows the child widget geometry to be cached to speed up Slate rendering. Any widgets that are cached by an Invalidation Box are not pre-passed, ticked, or painted. In general, if you are looking to optimize your project, wrapping certain widgets with Invalidation Boxes may boost your performance (particularly for mobile projects or complicated UI displays). For widgets that do not change constantly, they can be placed inside an Invalidation Box and cached instead of considered during paint, tick, or prepass.

If the widget changes, however, it will become invalid and you will need to manually invalidate the cache which will throw it away essentially and force it to redraw on the next paint pass. Anything that changes the visual appearance of the widget requires it to be invalidated. The only exception to this is a change to the appearance that is not stored in the vertex buffer for those widgets (for example Materials, as changing a Material Parameter does not require invalidating the widget).

## Details

In the **Details** panel for a placed **Invalidation Box**, there are a couple of specific options that can be set that pertain to the widget:

[![Invalidation Box properties in the Details panel](https://dev.epicgames.com/community/api/documentation/image/7ded3528-8af5-44fc-98b6-b32a2b3c0578?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7ded3528-8af5-44fc-98b6-b32a2b3c0578?resizing_type=fit)

| Option | Description |
| --- | --- |
| **Cache Relative Transforms** | Caches the locations for child draw elements relative to the invalidation box which adds extra overhead to drawing them every frame. However, in cases where the position of the invalidation boxes changes every frame, this can be a big saving. |
| **Is Volatile** | If true, prevents the widget or its child's geometry or layout information from being cached. If this widget changes every frame, but you want it to still be in an invalidation panel, you should make it as volatile instead of invalidating it every frame, which would prevent the invalidation panel from actually ever caching anything. |

Regarding the **Is Volatile** check box, any widget can be set to be volatile. Volatile widgets act like normal Slate widgets pre-invalidation. They're redrawn every frame, including all their children. When combined with the invalidation panel, it allows you to care only about redrawing the most dynamic bits of the UI, as invalidating a whole panel could be far more costly.

## Functions

When using an **Invalidation Box**, it is up to the user to call [Invalidate](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/Widgets/SWidget/Invalidate?application_version=5.5) through C++ or the **Invalidate Layout And Volatility** node (pictured below) on a child widget to force invalidation.

[![Invalidate node](https://dev.epicgames.com/community/api/documentation/image/452950e3-6b65-435e-a139-e26ff0b153b5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/452950e3-6b65-435e-a139-e26ff0b153b5?resizing_type=fit)

Currently, some core widgets do this automatically when certain properties are changed, however more will do it over time.

## Debugging

You can debug your Invalidation Boxes using the **Widget Reflector** (CTRL+Shift+W) and clicking the **Invalidation Debugging** toggle.

To display the legend when `SlateDebugger.Invalidate.Enable 1` is invoked, use `SlateDebugger.Invalidate.ToggleLegend`.

[![Widget Reflector](https://dev.epicgames.com/community/api/documentation/image/1d3ac683-0d76-485e-977d-cea8288c29b4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1d3ac683-0d76-485e-977d-cea8288c29b4?resizing_type=fit)

Click image for full view.

With the Widget Reflector up and Invalidation Debugging on, you will see the following colors:

| Color | Description |
| --- | --- |
| **Yellow** | Paint invalidated this frame. |
| **Gray** | Volatility invalidated this frame. |
| **Cyan** | ChildOrder invalidated this frame. |
| **Black** | RenderTransform invalidated this frame. |
| **White** | Visibility invalidated this frame. |
| **Pink** | Layout invalidated this frame for Invalidation Box. |
| **Blue** | Every widget was reordered. |
| **Red** | Fully re-updated. |

To debug InvalidationBox behavior, use `SlateDebugger.InvalidationRoot.Enable`.

Example below shows an image that is marked as volatile inside of a Border which is wrapped with an Invalidation Box.
Since the image is marked as volatile, it can be updated dynamically during gameplay while the Border (or any other art assets that you wanted to appear around the image that do not change) is cached.

[![Eample of using Invalidation Box](https://dev.epicgames.com/community/api/documentation/image/079e6a85-56b3-4712-90fc-21047923bfc3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/079e6a85-56b3-4712-90fc-21047923bfc3?resizing_type=fit)

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [programming](https://dev.epicgames.com/community/search?query=programming)
* [umg ui designer](https://dev.epicgames.com/community/search?query=umg%20ui%20designer)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/using-the-invalidation-box-for-umg-in-unreal-engine?application_version=5.7#description)
* [Details](/documentation/en-us/unreal-engine/using-the-invalidation-box-for-umg-in-unreal-engine?application_version=5.7#details)
* [Functions](/documentation/en-us/unreal-engine/using-the-invalidation-box-for-umg-in-unreal-engine?application_version=5.7#functions)
* [Debugging](/documentation/en-us/unreal-engine/using-the-invalidation-box-for-umg-in-unreal-engine?application_version=5.7#debugging)
