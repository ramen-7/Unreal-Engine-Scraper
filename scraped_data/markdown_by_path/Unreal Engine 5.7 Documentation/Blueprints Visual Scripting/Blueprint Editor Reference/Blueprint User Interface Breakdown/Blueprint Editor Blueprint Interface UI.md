<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprints-visual-scripting-editor-user-interface-for-blueprint-interfaces-in-unreal-engine?application_version=5.7 -->

# Blueprint Editor Blueprint Interface UI

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
7. [Blueprint User Interface Breakdown](/documentation/en-us/unreal-engine/user-interface-breakdown-in-unreal-engine "Blueprint User Interface Breakdown")
8. Blueprint Editor Blueprint Interface UI

# Blueprint Editor Blueprint Interface UI

A breakdown of the UI elements of the Blueprint Editor when working on Blueprint Interfaces.

![Blueprint Editor Blueprint Interface UI](https://dev.epicgames.com/community/api/documentation/image/9fde86d0-9783-4993-bff8-29d9ee5776cf?resizing_type=fill&width=1920&height=335)

 On this page

A **Blueprint Interface** is a collection of one or more functions - name only, no implementation - that can be added to
other Blueprints. Any Blueprint that has the Interface added is guaranteed to have those functions. The functions
of the Interface can be given functionality in each of the Blueprints that added it. This is essentially like the
concept of an interface in general programming, which allows multiple different types of Objects to all share and be accessed
through a common interface. Put simply, Blueprint Interfaces allow different Blueprints to share with and send data to one another.

Blueprint Interfaces can be made by content creators through the editor in a similar fashion to other Blueprints, but they
come with certain limitations in that they cannot:

* Add new variables
* Edit graphs
* Add Components

## Blueprint Interface Editor UI

When you first open a [Blueprint Interface](/documentation/en-us/unreal-engine/blueprint-interface-in-unreal-engine), the UI will look extremely simple, consisting only of the following:

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/95390df8-9562-46e8-9833-9adeb8bddf81/interfacenumbered.png)

| Default Visible UI Components | Available in the Window Menu |
| --- | --- |
| 1. [Menu](/documentation/en-us/unreal-engine/menu-for-the-blueprints-visual-scripting-editor-in-unreal-engine) 2. [Toolbar](/documentation/en-us/unreal-engine/toolbar-in-the-blueprints-visual-scripting-editor-for-unreal-engine) 3. [My Blueprint](/documentation/en-us/unreal-engine/my-blueprint-panel-in-the-blueprints-visual-scripting-editor-for-unreal-engine) 4. [Details](/documentation/en-us/unreal-engine/details-panel-in-the-blueprints-visual-scriting-editor-for-unreal-engine) 5. [Graph Editor](/documentation/en-us/unreal-engine/graph-editor-for-the-blueprints-visual-scripting-editor-in-unreal-engine) | * [Debug](/documentation/en-us/unreal-engine/debug-panel-in-the-blueprints-visual-scripting-editor-for-unreal-engine) * [Compiler Results](/documentation/en-us/unreal-engine/compiler-results-in-the-blueprints-visual-scripting-editor-for-unreal-engine) * [Find Results](/documentation/en-us/unreal-engine/find-result-panel-in-the-blueprints-visual-scripting-editor-for-unreal-engine) |

## Usage Notes

It is important to note that the Graph View in this case is a bit different than the Graph Editor usually available within the Blueprint Editor. You might notice that it is grayed out and that you can neither navigate it nor can you add any nodes to it. That is because this is more of a visualization tool than it is a way to edit the graph. Keep in mind that an Interface holds no functionality in and of itself, so there is no need to create an actual functioning network in this case. Think of this view as just a preview of what your inputs and outputs will be.

For more information on creating and working with Blueprint interfaces, please see [Blueprint Interface](/documentation/en-us/unreal-engine/blueprint-interface-in-unreal-engine).

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Blueprint Interface Editor UI](/documentation/en-us/unreal-engine/blueprints-visual-scripting-editor-user-interface-for-blueprint-interfaces-in-unreal-engine?application_version=5.7#blueprintinterfaceeditorui)
* [Usage Notes](/documentation/en-us/unreal-engine/blueprints-visual-scripting-editor-user-interface-for-blueprint-interfaces-in-unreal-engine?application_version=5.7#usagenotes)
