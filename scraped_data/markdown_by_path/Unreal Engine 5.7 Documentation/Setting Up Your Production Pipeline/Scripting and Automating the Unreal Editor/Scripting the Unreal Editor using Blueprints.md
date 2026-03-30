<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-blueprints?application_version=5.7 -->

# Scripting the Unreal Editor using Blueprints

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
5. [Setting Up Your Production Pipeline](/documentation/en-us/unreal-engine/setting-up-your-production-pipeline-in-unreal-engine "Setting Up Your Production Pipeline")
6. [Scripting and Automating the Unreal Editor](/documentation/en-us/unreal-engine/scripting-and-automating-the-unreal-editor "Scripting and Automating the Unreal Editor")
7. Scripting the Unreal Editor using Blueprints

# Scripting the Unreal Editor using Blueprints

Describes how to use Blueprints in the editor to automate content production tasks.

![Scripting the Unreal Editor using Blueprints](https://dev.epicgames.com/community/api/documentation/image/823494f8-d329-42ab-97de-a9c1e43c7736?resizing_type=fill&width=1920&height=335)

 On this page

Blueprints help create runtime gameplay for your project, but you can also use them to develop actions and tools that interact with your project content. You can run Blueprint graphs on demand in the editor to work with assets, layout content in your level, trigger actions in the editor user interface (UI), or even extend the editor with custom UI panels.

This page describes some basics of using Blueprints to script and automate the Unreal Editor.

## Options for Running Blueprints in the Editor

You can use several techniques to set up and trigger your Blueprint code.

### Editor Utility Widgets

Editor Utility Widgets are UMG widgets that the Unreal Editor can render in the same dockable panel used for all other tools in the editor UI. This approach is best if you need a rich UI to control your Blueprint. You can take advantage of all the visual styling options of UMG, combined with the rich scripting control of Blueprints. This is the most flexible and powerful option, but also quite simple to get started with, and is recommended for most editor scripting work.

For more information on how to create an Editor Utility Widget and open it in the editor, see [Editor Utility Widgets](/documentation/en-us/unreal-engine/editor-utility-widgets-in-unreal-engine).

[![Editor Utility Widgets](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ed50342d-0470-47cf-9dac-e067e8e804c9/ue5_1-editor-utility-topic.png)

Editor Utility Widgets

An overview and usage instructions for Editor Utility Widgets.](/documentation/en-us/unreal-engine/editor-utility-widgets-in-unreal-engine)

### Editor Utility Blueprints

Editor Utility Blueprints are a specialized class that is intended for logic that you need to run only within the Unreal Editor, never at runtime, and that does not need any custom UI.

One built-in use case for these classes is to support *scripted actions*. Scripted actions are graphs that you trigger from the context menu that appears when you right-click an Actor in the Level or an Asset in the Content Browser.

For more information, see [Scripted Actions](/documentation/en-us/unreal-engine/scripted-actions-in-unreal-engine).

[![Scripted Actions](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0bb733bb-785b-4fa7-b579-ce4894290c1c/placeholder_topic.png)

Scripted Actions

Create Blueprints that you can invoke by right-clicking an Asset in the Content Browser or an Actor in the Level.](/documentation/en-us/unreal-engine/scripted-actions-in-unreal-engine)

### Call in Editor

When you create a custom event or a function in a Blueprint class, you can mark that event or function as callable in the editor. If you place an instance of that Blueprint class in a Level and select it, you can trigger your custom event or function in the **Details** panel. This approach is best to use anytime you need a Blueprint graph to work both at runtime and in the editor.

For more information, see [Calling Blueprints in the Editor](/documentation/en-us/unreal-engine/calling-blueprints-in-the-unreal-editor).

[![Calling Blueprints in the Editor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d8c30f98-c77f-4ac2-993d-e7f5a7020e27/placeholder_topic.png)

Calling Blueprints in the Editor

Describes how to call Blueprint events and functions on Actors while working in the Editor.](/documentation/en-us/unreal-engine/calling-blueprints-in-the-unreal-editor)

### Startup Objects

You can identify specific Editor Utility Widget classes and Editor Utility Blueprint classes in your Project as startup objects. Each time the editor loads up your Project, it automatically creates an instance of each of these startup objects and invokes a pre-defined function. This is a good option if you need a Blueprint class to always carry out certain actions when your Project is loaded, or if you need to always bind Blueprint logic to events that happen as you work on your Project content in the editor.

For more information, see [Running Blueprints at Editor Startup](/documentation/en-us/unreal-engine/running-blueprints-at-unreal-editor-startup).

[![Running Blueprints at Editor Startup](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f2be3abc-f2ee-4e4e-bda9-8df14b508080/placeholder_topic.png)

Running Blueprints at Editor Startup

Describes how to define Blueprint functions that the editor invokes when it starts up.](/documentation/en-us/unreal-engine/running-blueprints-at-unreal-editor-startup)

## Accessing Editor-Only Blueprint Nodes

Most operations that involve modifying asset files or working with the Unreal Editor UI can't work in your game at runtime. Therefore, you can only access editor-only features like these—that is, any functions that are defined in a module whose type is set to `Editor`—from Blueprint classes that are also editor-only.

For example, if you use a Blueprint class that derives from a parent class that can be used at runtime, such as the base **Actor** class, you'll see a limited set of functions listed under the **Editor Scripting** category in your Blueprint Editor. However, if you create an Editor Utility Blueprint, an Editor Utility Widget, or a normal Blueprint class that derives from any editor-only parent class, you'll see a much larger and more comprehensive set of functions that you can use:

|  |  |
| --- | --- |
| Editor Scripting nodes for the Actor class | Editor Scripting nodes for the EditorUtilityActor class |
| Actor class | EditorUtilityActor class |

If you've installed the Editor Scripting Utilities plugin, this is where you'll find the functions it exposes for working with Static Meshes and other kinds of Assets. See [Scripting and Automating the Editor](/documentation/en-us/unreal-engine/scripting-and-automating-the-unreal-editor).

## Editor Utility Subsystem

At startup, the Unreal Editor initializes a subsystem that is intended specifically for managing the behavior of the editor's scripting features. For example, this subsystem handles things like spawning and cleaning up [Startup Objects](/documentation/en-us/unreal-engine/running-blueprints-at-unreal-editor-startup), and handling the creation and destruction of new editor panels for [Editor Utility Widgets](/documentation/en-us/unreal-engine/editor-utility-widgets-in-unreal-engine).

You can also use the Editor Utility Subsystem in your own C++ or Blueprint code. For example, you could retrieve the Editor Utility Subsystem and call its `SpawnAndRegisterTab()` method to programmatically open up a new panel in the editor UI that hosts an instance of an Editor Utility Widget class in your Project.

For more information about subsystems and how to access and use them in C++, Blueprint, and Python, see [Programming Subsystems](/documentation/en-us/unreal-engine/programming-subsystems-in-unreal-engine).

## Scriptable Tools System

The **Scriptable Tools** system provides functions and an editor mode to create custom interactive tools. The Scriptable Tools system plugin exposes the **Interactive Tools Framework** to Blueprint, providing creators and technical artists the means to design tools.

For more information, see [Scriptable Tools System](/documentation/en-us/unreal-engine/scriptable-tools-system-in-unreal-engine).

[![Scriptable Tools System](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ab89e534-2c34-4287-9b7d-d7d08c12c65b/scriptable-tool-topic.png)

Scriptable Tools System

Overview of the Scriptable Tools system and editor mode to create custom interactive tools.](/documentation/en-us/unreal-engine/scriptable-tools-system-in-unreal-engine)

* [editor](https://dev.epicgames.com/community/search?query=editor)
* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [scripting](https://dev.epicgames.com/community/search?query=scripting)
* [blueprint utilities](https://dev.epicgames.com/community/search?query=blueprint%20utilities)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Options for Running Blueprints in the Editor](/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-blueprints?application_version=5.7#optionsforrunningblueprintsintheeditor)
* [Editor Utility Widgets](/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-blueprints?application_version=5.7#editorutilitywidgets)
* [Editor Utility Blueprints](/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-blueprints?application_version=5.7#editorutilityblueprints)
* [Call in Editor](/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-blueprints?application_version=5.7#callineditor)
* [Startup Objects](/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-blueprints?application_version=5.7#startupobjects)
* [Accessing Editor-Only Blueprint Nodes](/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-blueprints?application_version=5.7#accessingeditor-onlyblueprintnodes)
* [Editor Utility Subsystem](/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-blueprints?application_version=5.7#editorutilitysubsystem)
* [Scriptable Tools System](/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-blueprints?application_version=5.7#scriptabletoolssystem)
