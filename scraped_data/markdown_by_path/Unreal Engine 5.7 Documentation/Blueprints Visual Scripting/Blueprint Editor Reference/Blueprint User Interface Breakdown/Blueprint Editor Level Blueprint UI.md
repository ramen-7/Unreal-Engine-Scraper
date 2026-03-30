<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprints-visual-scripting-editor-user-interface-for-level-blueprints-in-unreal-engine?application_version=5.7 -->

# Blueprint Editor Level Blueprint UI

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
8. Blueprint Editor Level Blueprint UI

# Blueprint Editor Level Blueprint UI

A breakdown of the UI elements of the Blueprint Editor when working on Level Blueprints.

![Blueprint Editor Level Blueprint UI](https://dev.epicgames.com/community/api/documentation/image/a0dc4489-f13b-4b6e-bbda-f98d78ce4977?resizing_type=fill&width=1920&height=335)

 On this page

A **Level Blueprint** is a specialized type of **Blueprint** that acts as a level-wide global event graph.
Each level in your project has its own Level Blueprint created by default that can be edited within the Unreal Editor, however new Level Blueprints
cannot be created through the editor interface.

Events pertaining to the level as a whole, or specific instances of Actors within the level, are
used to fire off sequences of actions in the form of Function Calls or Flow Control operations.
Those familiar with Unreal Engine 3 should be very familiar with this concept as this is very similar
to how Kismet worked in Unreal Engine 3.

Level Blueprints also provide a control mechanism for level streaming and [Sequencer](/documentation/en-us/unreal-engine/real-time-compositing-with-sequencer-in-unreal-engine) as well
as for binding events to Actors placed within the level.

## Interface

The Blueprint Editor contains the following sections when editing Level Blueprints:

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/05ab4748-e1b1-4497-8e5b-e4a42feb8528/levelblueprintui.png)

| Default Visible UI Components | Available in the Window Menu |
| --- | --- |
| 1. [Menu](/documentation/en-us/unreal-engine/menu-for-the-blueprints-visual-scripting-editor-in-unreal-engine) 2. [Toolbar](/documentation/en-us/unreal-engine/toolbar-in-the-blueprints-visual-scripting-editor-for-unreal-engine) 3. [My Blueprint](/documentation/en-us/unreal-engine/my-blueprint-panel-in-the-blueprints-visual-scripting-editor-for-unreal-engine) 4. [Details](/documentation/en-us/unreal-engine/details-panel-in-the-blueprints-visual-scriting-editor-for-unreal-engine) 5. [Graph Editor](/documentation/en-us/unreal-engine/graph-editor-for-the-blueprints-visual-scripting-editor-in-unreal-engine) | * [Compiler Results](/documentation/en-us/unreal-engine/compiler-results-in-the-blueprints-visual-scripting-editor-for-unreal-engine) * [Debug](/documentation/en-us/unreal-engine/debug-panel-in-the-blueprints-visual-scripting-editor-for-unreal-engine) * [Find Results](/documentation/en-us/unreal-engine/find-result-panel-in-the-blueprints-visual-scripting-editor-for-unreal-engine) * [Palette](/documentation/en-us/unreal-engine/palette-in-the-bleprints-visual-scripting-editor-for-unreal-engine) * [Viewport](/documentation/en-us/unreal-engine/components-mode-viewport-in-the-blueprints-visual-scripting-editor-for-unreal-engine) |

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Interface](/documentation/en-us/unreal-engine/blueprints-visual-scripting-editor-user-interface-for-level-blueprints-in-unreal-engine?application_version=5.7#interface)
