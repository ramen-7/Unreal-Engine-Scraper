<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/umg-slots-in-unreal-engine?application_version=5.7 -->

# UMG Slots

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
6. [Basics](/documentation/en-us/unreal-engine/basics-of-user-interface-development-in-unreal-engine "Basics")
7. [Building Your UI](/documentation/en-us/unreal-engine/building-your-ui-in-unreal-engine "Building Your UI")
8. UMG Slots

# UMG Slots

An overview of how to use UMG slots.

![UMG Slots](https://dev.epicgames.com/community/api/documentation/image/de23d383-d2af-49fa-bb46-72eb89fef17f?resizing_type=fill&width=1920&height=335)

 On this page

**Slots** are the invisible glue that bind Widgets together. In Slate they are a lot more explicit in that you must first create a Slot then
choose what control to place inside of it. In UMG, however, you have Panel Widgets that automatically use the right kind of Slot when Child Widgets are added to them.

Moreover, each Slot is different. For example, if you were to place a control on a Grid, you would expect to be able to set things like Row and Column. But these properties have no business being on a Widget that was placed on a Canvas. That is where Slots come in. A **Canvas Slot** understands how to layout content absolutely and through Anchors, while a **Grid Slot** only understands Rows and Columns.

## Accessing Slots

By convention, all Slot-related properties appear under the **Slot** category in the **Details** panel. You will also notice that the type of Slot being used by your Widget is displayed in parentheses.

![Slot Section in Details panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6af0cf3c-ff0a-4456-8446-30c205b153d4/ue5_1-01-canvas-panel-slot.png)

### Setting Layout Properties

At runtime, to modify properties under Layout, you can access the Slot member of the Widget in Blueprint or C++ and then **Cast** it to the correct **Slot Type**. Once doing so, you will then be able to modify the properties, an example of which is indicted below.

![Blueprint Script](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/399d81ba-942c-4949-8db3-90351104a049/ue5_1-02-blueprint-script.png)

Above, a **Vertical Box** entitled **GameTitleBox** has been placed on a **CanvasPanel**. By getting the Slot associated with the Vertical Box and **Casting** to the **CanvasPanelSlot** type, we are then able to set the position of the box when our "StartButton" is clicked.

Currently in Blueprints, only SETTER nodes are exposed. If you need to GET properties from the Layout, you may want to create a Variable to store your property and upon **Event Construct**, and **SET** your Layout property via your Variable so that you have reference to and can access it later.

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [programming](https://dev.epicgames.com/community/search?query=programming)
* [umg ui designer](https://dev.epicgames.com/community/search?query=umg%20ui%20designer)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Accessing Slots](/documentation/en-us/unreal-engine/umg-slots-in-unreal-engine?application_version=5.7#accessingslots)
* [Setting Layout Properties](/documentation/en-us/unreal-engine/umg-slots-in-unreal-engine?application_version=5.7#settinglayoutproperties)
