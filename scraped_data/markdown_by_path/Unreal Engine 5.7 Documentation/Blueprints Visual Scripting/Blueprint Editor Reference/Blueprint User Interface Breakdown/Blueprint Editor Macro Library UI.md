<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprints-visual-scripting-editor-user-interface-for-macro-libraries-in-unreal-engine?application_version=5.7 -->

# Blueprint Editor Macro Library UI

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
4. Blueprint Editor Macro Library UI

# Blueprint Editor Macro Library UI

A breakdown of the UI elements of the Blueprint Editor when working on Blueprint Macro Libraries.

![Blueprint Editor Macro Library UI](https://dev.epicgames.com/community/api/documentation/image/0670c455-c413-4458-afe4-598adbed3e45?resizing_type=fill&width=1920&height=335)

 On this page

A **Blueprint Macro Library** is a container that holds a collection of **Macros** or self-contained graphs that can
be placed as nodes in other Blueprints. These can be time-savers as they can store commonly used sequences of nodes
complete with inputs and outputs for both execution and data transfer.

Macros are shared among all graphs that reference them, but they are auto-expanded into graphs as if they were a
collapsed node during compiling. This means that Blueprint Macro Libraries do not need to be compiled. However, changes
to a Macro are only reflected in graphs that reference that Macro when the Blueprint containing those graphs is
recompiled.

For more information on Macro Libraries and how to use them, please see the [Blueprint Macro Library](/documentation/en-us/unreal-engine/blueprint-macro-library-in-unreal-engine) documentation.

## Interface

Much like with Blueprint Interfaces, when you first open the Blueprint Editor for a Macro Library, you will see a simplified UI without a graph:

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/48e6ecd7-7209-4e4f-a00c-7dbd648f429e/macrolibraryuiclean.png)

| Default Visible UI Components | Available in the Window Menu |
| --- | --- |
| 1. [Menu](/documentation/en-us/unreal-engine/menu-for-the-blueprints-visual-scripting-editor-in-unreal-engine) 2. [Toolbar](/documentation/en-us/unreal-engine/toolbar-in-the-blueprints-visual-scripting-editor-for-unreal-engine) 3. [My Blueprint](/documentation/en-us/unreal-engine/my-blueprint-panel-in-the-blueprints-visual-scripting-editor-for-unreal-engine) 4. [Details](/documentation/en-us/unreal-engine/details-panel-in-the-blueprints-visual-scriting-editor-for-unreal-engine) 5. [Graph Editor](/documentation/en-us/unreal-engine/graph-editor-for-the-blueprints-visual-scripting-editor-in-unreal-engine) | * [Debug](/documentation/en-us/unreal-engine/debug-panel-in-the-blueprints-visual-scripting-editor-for-unreal-engine) * [Find Results](/documentation/en-us/unreal-engine/find-result-panel-in-the-blueprints-visual-scripting-editor-for-unreal-engine) * [Palette](/documentation/en-us/unreal-engine/palette-in-the-bleprints-visual-scripting-editor-for-unreal-engine) |

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Interface](/documentation/en-us/unreal-engine/blueprints-visual-scripting-editor-user-interface-for-macro-libraries-in-unreal-engine?application_version=5.7#interface)
