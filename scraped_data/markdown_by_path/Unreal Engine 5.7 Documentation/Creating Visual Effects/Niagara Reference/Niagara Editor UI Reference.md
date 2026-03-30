<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/editor-ui-reference-for-niagara-effects-in-unreal-engine?application_version=5.7 -->

# Niagara Editor UI Reference

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
5. [Creating Visual Effects](/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine "Creating Visual Effects")
6. [Niagara Reference](/documentation/en-us/unreal-engine/reference-for-niagara-effects-in-unreal-engine "Niagara Reference")
7. Niagara Editor UI Reference

# Niagara Editor UI Reference

This page describes the user interface (UI) of the Niagara Emitter and System Editor.

![Niagara Editor UI Reference](https://dev.epicgames.com/community/api/documentation/image/761eae95-3d8a-4af3-b6f0-e9772aff456c?resizing_type=fill&width=1920&height=335)

 On this page

## Overview

The Niagara Editor can be opened by double-clicking on any Niagara emitter or system, or through the context menu by right-clicking on a Niagara emitter or system and selecting **Edit**. This document identifies and describes the parts of the Niagara Editor. Because the user interface (UI) of the editor is mostly the same for both emitters and systems, descriptions for both have been included.

[![Editor Fullscreen](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b47c47ba-af04-4764-ad00-571e9da1e11d/ue5_01-editor-fullscreen.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b47c47ba-af04-4764-ad00-571e9da1e11d/ue5_01-editor-fullscreen.png)

Click image for full size.

1. Menu Bar
2. Tool Bar
3. Preview Panel
4. Parameters Panel
5. System Overview
6. Scratch Pad Panel
7. Selection Panel (the Stack)
8. Curves Panel
9. Niagara Log Panel
10. Timeline Panel

## Menu

[![Menu Bar](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ac686c1f-4126-422f-b84c-5ed555371a3e/ue5_02-menu-bar.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ac686c1f-4126-422f-b84c-5ed555371a3e/ue5_02-menu-bar.png)

Click image for full size.

The tables below only describe commands that apply to the Niagara Editor itself; there may be additional commands displayed in those menus that open Asset editors or other parts of Unreal Editor.

### File

[![File Menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7a77c6d1-1593-4e41-b31c-49774e9fa718/ue5_03-file-menu.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7a77c6d1-1593-4e41-b31c-49774e9fa718/ue5_03-file-menu.png)

Click image for full size.

| Command | Description |
| --- | --- |
| **Save** | Saves the current emitter. |
| **Save As** | Saves the current emitter under a different name. |
| **Open Asset** | Displays a window to select other assets. |
| **Save All** | Saves all assets and levels in this project. |
| **Choose Files to Save** | Displays a dialog with options for saving assets and levels. |
|  |  |

### Edit

[![Edit Menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/828e2781-f1fa-4453-83bc-87639f670971/ue5_04-edit-menu.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/828e2781-f1fa-4453-83bc-87639f670971/ue5_04-edit-menu.png)

Click image for full size.

| Command | Description |
| --- | --- |
| **Undo** | Undoes the last action. |
| **Redo** | Redoes an action that was undone. |
| **Undo History** | Displays a dialog listing all undone actions. |
| **Editor Preferences** | Opens the Editor Preferences window to enable you to adjust the preferences of the editors. |
| **Project Settings** | Opens the Project Settings window to enable you to adjust the setting of the Project. |
| **Plugins** | Opens the Plugins windows for you to enable or disable plugins. |
|  |  |

### Asset

[![Asset Menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d90f8030-0ace-4568-8834-f63e856b9f31/ue5_05-asset-menu.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d90f8030-0ace-4568-8834-f63e856b9f31/ue5_05-asset-menu.png)

Click image for full size.

| Command | Description |
| --- | --- |
| **Find in Content Browser** | Switches to most recently used Content Browser, and selects the current Asset in that Content Browser. |
| **Reference Viewer** | Displays a dialog that shows all of the current Asset's references. |
| **Size Map** | Displays an interactive map showing the approximate size of the Asset and everything it references. |
| **Audit Assets** | Opens the Asset Audit UI and displays information about the selected assets. |
| **Shader Cook Statistics** | Displays shader cook statistics. |
|  |  |

### Window

[![Window Menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ee516d96-ed8e-4011-ae58-c6b818861dd9/ue5_06-window-menu.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ee516d96-ed8e-4011-ae58-c6b818861dd9/ue5_06-window-menu.png)

Click image for full size.

| Command | Description |
| --- | --- |
| **Preview** | Shows or hides the Preview panel. |
| **Curves** | Shows or hides the Curves panel. |
| **Timeline** | Shows or hides the Timeline panel. |
| **Parameters** | Shows or hides the Parameters panel. |
| **Legacy Parameters** | Open the Legacy Parameters window. |
| **Selection** | Shows or hides the Selection panel. |
| **Attribute Spreadsheet** | Shows or hides the Attribute Spreadsheet. |
| **Preview Scene Settings** | Shows or hides the Preview Scene Settings. |
| **Generated Code** | Shows or hides the Generated Code panel. |
| **Niagara Log** | Shows or hides the Niagara Log panel. |
| **System Overview** | Shows or hides the System Overview panel. |
| **Scratch Pad** | Shows or hides the Scratch Pad panel. |
| **Script Stats** | Shows or hides the Script Stats panel. |
| **Baker** | Opens the Baker window. |
| **Cinematics** | Opens the **Sequence Recorder** panel as a new window. |
| **Content Browser** | Opens the selected Content Browser as a new window. |
| **Device Output Log** | Open the Device Output Log window. |
| **Interchage Results Browser** | Open the Interchage Results Browser window. |
| **Message Log** | Open the Message Log window. |
| **Output Log** | Open the Output Log window. |
| **Open Marketplace** | Opens the Open Marketplace. |
| **Quixel Bridge** | Opens the Quixel Bridge. |
| **Load Layout** | Click on a layout to load a previously saved layout. |
| **Save Layout** | Save a new layout. |
| **Remove Layout** | Click on a layout to remove a previously saved layout. |
| **Enable Fullscreen** | Click to toggle on Fullscreen Mode. |
|  |  |

## Tools

[![Tools Menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9eef4e53-5cad-4333-863d-26dc805f7692/ue5_07-tools-menu.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9eef4e53-5cad-4333-863d-26dc805f7692/ue5_07-tools-menu.png)

Click image for full size.

| Command | Description |
| --- | --- |
| **New C++ Class** | Adds C++ code to the project. The code can only be compiled if you have Visual Studio installed. |
| **Generate Visual Studio Project** | Generates your C++ code project in Visual Studio. |
| **Find in Blueprints** | Opens the selected Find In Blueprints panel as a new window. |
| **Cache Statistics** | Shows the Derived Data Cache Statistics window. |
| **Class Viewer** | Displays all classes that exist within this project. |
| **CSV to SVG** | Tool for generating vector line graphs from comma-separated value files generated from CSV profiles. |
| **Localization Dashboard** | Opens the experimental Localization Dashboard window. |
| **Merge Actors** | Open the Merge Actors window. |
| **Nanite Tools** | Shows the Tools for auditing and optimizing Nanite assets window. |
| **Project Launcher** | Opens the Project Launcher window. |
| **Resource Usage** | Shows the Derived Data Resource Usage window. |
| **Session Frontend** | Open the Session Frontend window. |
| **Struct Viewer** | Displays all structs that exist within this project. |
| **Virtual Assets** | Open the Virtual Assets Statistics. |
| **Debug** | Enables you to open up various different Debug Tools. |
| **Profile** | Enables you to open up various different Profile Tools. |
| **Audit** | Enables you to open up various different Audit Tools. |
| **Platforms** | View and manage connected devices. |
| **View Changelists** | Opens a dialog displaying current changelists. |
| **Submit Content** | Opens a dialog with check in options for content and levels. |
| **Connect to Source Control** | Displays a dialog where you can connect to source control, allowing source control functions to be performed on content. |
| **Run Unreal Insights** | Run the Unreal Insights standalone application. |
|  |  |

## Toolbar

[![Toolbar](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ea3f3697-c78f-4197-b581-464e318e81c4/ue5_09-toolbar.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ea3f3697-c78f-4197-b581-464e318e81c4/ue5_09-toolbar.png)

Click image for full size.

| Tool Name | Description |
| --- | --- |
| **Save** Save Icon | Saves the current emitter. |
| **Browse** Browse Icon | Switches to the most recent Content Browser and selects the current emitter. |
| **Compile** Compile Icon | Compiles all the modules in the emitter. You can also change the Auto-Compile settings by clicking the dropdown arrow. Click the dropdown to select the following options:   * **Full Build**: Triggers a full rebuild of this system, ignoring the change tracking. * **Auto-Compile**: Automatically compiles when the Graph changes. |
| **Thumbnail** Thumbnail Icon | Generates a thumbnail image of the Asset. |
| **Bounds** Bounds Icon | Shows the bounds of the scene in the Preview panel. Click the dropdown to **Set Fixed Bounds**. |
| **Performance** Performance Icon | Click the dropdown to see the following Performance Options:   * **Clear Stats**: Clear all existing stat captures. * **GPU Profiling**: Enable this to measure the GPU runtime cost of scripts. Can be expensive for simulation stages with lots of iterations. * **Display Average**: Enable this to display the average of captured stats. * **Display Maximum**: Enable this to display the maximum of captured stats. * **Display Relative Values**: Enable this to display the captured stats in percent of the parent script. * **Display Absolute Values**: Enable this to display the captured module stat times directly. |
| **Debug** Debug Icon | Click the dropdown to see the following Debug Options:   * **Debug HUD**: Open the Niagara Debug HUD. * **FX Outliner**: Open the Niagara FX Outliner. * **Attribute Spreadsheet**: Open the Niagara Debug Outliner. |
| **Simulation** Simulation Icon | Click the dropdown to see the following Simulation Options:   * **Auto-Play**: Enable this to make simulation auto-play when you open the Asset in the Niagara Editor, and also when you modify the Asset. * **Reset on Change**: Enable this to make the simulation reset whenever you make a change to the Asset in the Niagara Editor. * **Resimulate When Paused**: Enable this to make the simulation rerun to the current time when you make changes while it is paused. |
| **Baker** Baker Icon | Click the dropdown to see the following Baker Options:   * **Open Baker Tab**: Opens the flip book window. * **Bake**: Runs the bake process. |
|  |  |

## Preview Panel

[![Preview panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8004896d-d353-49c7-9ccf-b9ba1bbf182f/ue5_19-preview-panel.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8004896d-d353-49c7-9ccf-b9ba1bbf182f/ue5_19-preview-panel.png)

Click image for full size.

| Menu Item | Description |
| --- | --- |
| Viewport Options |  |
| **Realtime** | Toggles real-time rendering in the viewport. Changes you make in the emitter stack will immediately be shown in the viewport, even if the emitter is not compiled. |
| **Show Stats** | Toggles showing stats in the viewport. If **Realtime** is not enabled, **Show Stats** automatically enables it. |
| **Show FPS** | Toggles showing the frames per second in the viewport. If **Show Stats** is not enabled, **Show FPS** automatically enables it. |
| **Field of View** | Changes the FOV of the viewport camera. This effectively zooms the lens of the camera in and out. |
| **Far View Plane** | Choose the distance to use as your far view plane. Setting this to zero acts as an infinite far view plane. |
| **Screen Percentage** | Sets the percentage of the screen your Preview panel uses. |
| Viewpoint Type |  |
| **Perspective** | The default viewpoint used in the viewport. |
| **Orthographic** | Choose **Top**, **Bottom**, **Left**, **Right**, **Front** or **Back**. Selecting one of these changes the View Mode to **Wireframe**. |
| View Mode |  |
| **Lit** | The default setting; it renders the scene with normal lighting. |
| **Unlit** | Renders the scene with no lights. No light maps, dynamic lights, static lights, or emissive materials affect the scene. |
| **Wireframe** | Renders the scene in brushed wireframe. This displays the raw triangles of everything in the viewport, and turns off the back faces to make the scene more readable. |
| **Detail Lighting** | Renders the scene with detail lighting only. This means only lighting with normal data pulled from materials will be used. Color emitted from lights will affect the scene. |
| **Lighting Only** | Renders the scene with lighting only, and no textures. Only the vertex normals of the scene will be taken into account. |
| **Reflections** | Renders the scene with reflections only. This includes both reflection captures and **Screen Space** Reflections. |
| **Player Collision** | Renders a color-coded view of what a Player or Pawn can collide with. Static Mesh collision displays as green, Volumes as pink, and Brushes as a grayish-violet. |
| **Visibility Collision** | This setting will render a color-coded view of what Actors in the scene will block visibility traces. Static mesh collision displays as green, volumes as pink, and brushes as a grayish-violet. |
| **Optimization Viewmodes** | Select from the following options:   * **Light Complexity**: Renders a view showing where raw light overlaps. * **Lightmap Density**: Renders a view of lightmap density in the scene, with blue being the least dense and red being the most dense. * **Stationary Light Overlap**: Renders a view of where stationary lights overlap. * **Shader Complexity**: Renders a view of the shader complexity in a scene. Light green is the least complex, moving to darker greens as complexity increases, and the most complex areas are in red. * **Shader Complexity and Quads**: Renders a view with both shader complexity and quad overdraw displayed. * **Quad Overdraw**: Renders a view with just quad overdraw complexity displayed. * **Material Texture Scales**: Visualize the accuracy of the material texture scales used for texture streaming. * **Virtual Texture Pending Mips**: Visualize the ratio between the currently streamed virtual texture level and the level wanted by the GPU. |
| **Level of Detail Coloration** | Select from the following options:   * **Mesh LOD Coloration**: Renders the scene using LOD color visualization. * **Hierarchical LOD Coloration**: Renders the scene using HLOD color visualization. |
| **Player Collision** | Renders player collision visualization. |
| **Visibility Collision** | Renders visibility collision visualization. |
| **Auto** | If enabled, enables automatic exposure. |
| **EV100** | Sets the exposure value of the camera using the specified EV100. |
| Show |  |
| **Grid** | Toggles the viewport's grid. |
| **Instruction Counts** | Toggles the display of instruction counts in the upper left corner of the viewport. |
| **Particle Counts** | Toggles the display of particle counts in the viewport. |
| **Emitter Execution Order** | Toggles the display of the order that emitters are executed in the viewport. |
|  |  |

## Parameters Panel

[![Parameters Panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/559ebe3d-1bd5-4122-82bd-61d0e85995ee/ue5_20-parameters-panel.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/559ebe3d-1bd5-4122-82bd-61d0e85995ee/ue5_20-parameters-panel.png)

Click image for full size.

This panel lists all the user exposed, system, emitter, particle, and engine-provided parameters (also called *attributes*) that are used by the active emitter or system.

From the **Parameters** panel, you can drag and drop parameters to any appropriate node in the **System Overview**, or to any appropriate module parameter in the **Selection** panel. The number of times a parameter is referenced is shown on the right, enabling you to spot errors and make decisions on how to change your variables. If you have other emitters open, this panel pulls in data from those open emitters. This enables the user to share data between emitters. The Namespace for a parameter is displayed with a prominent icon, and you can see a tooltip that explains that Namespace when you mouse over the icon. To see more advanced Namespaces, such as parameter collections, click the **Eye** icon next to the Search bar.

## System Overview Panel

[![System Overview](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ca50111a-217f-41a1-b750-d68b02b4260e/ue5_21-system-overview.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ca50111a-217f-41a1-b750-d68b02b4260e/ue5_21-system-overview.png)

Click image for full size.

The **System Overview** panel gives a high-level overview of the system or emitter being edited, combining a pan-and-zoom Graph view with compact versions of the system or emitter stack. This panel makes it easier to navigate between different parts of the data, and it gives you a high level view when you open an emitter or system for the first time.

In a system, select an emitter in the **Timeline** panel and it will display the full stack for that emitter in the **Selection** panel. In this full stack view, the system information is on top, followed by the emitter module groups below. You can also get a full stack view of an emitter node or the system node by clicking on that node in the System Overview panel. However, if you want a less cluttered or more focused view, you can select an individual group or module within the emitter node in the System Overview to see just that group or module in the Selection panel.

### System Node

[![System Node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/257ece52-e9d7-40b6-84e8-fc9a860789b8/ue5_22-system-node.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/257ece52-e9d7-40b6-84e8-fc9a860789b8/ue5_22-system-node.png)

Click image for full size.

The **System** Node has icons that identify each group of modules, as well as having colored dots next to modules that identify what that module or parameter affects.

### Emitter Nodes

[![Emitter Node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ae9b6dc8-ada1-4183-8c5c-a83e6614cbe6/ue5_23-emitter-node.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ae9b6dc8-ada1-4183-8c5c-a83e6614cbe6/ue5_23-emitter-node.png)

Click image for full size.

**Emitter Properties** has an icon that identifies whether the simulation is run on the CPU or the GPU. Other icons and colored dots on the emitter node help you identify the group, module, or parameter quickly.

## Scratch Pad Panel

[![Scratch Pad](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7b35ea19-8fd7-4f6b-b36a-80c5dab32224/ue5_24-scratch-pad.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7b35ea19-8fd7-4f6b-b36a-80c5dab32224/ue5_24-scratch-pad.png)

Click image for full size.

With the **Scratch Pad**, you can create reusable modules or dynamic inputs that are contained locally in the active emitter or system Asset. This makes it easier to design and implement new custom modules or dynamic inputs, because you can see the results immediately within the emitter or system. You can keep or discard these at will. Once you have the result you are looking for, you can copy-paste the script to an existing Asset. You can also save it as a new Asset by right-clicking **Scratch Script Selector** and selecting **Create Asset**. The Scratch Pad also allows you to make something that is very specific to the active emitter or system, and does not need to be made into its own Asset.

There are two ways to open the Scratch Pad panel in the Niagara Editor. You can open it from the **Windows** menu, the way you would show or hide any other panel. The disadvantage to this method is that when you use the Scratch Pad to build a custom module, you need to manually add that module to your overall emitter or system script in the System Overview. You also have to add the module or dynamic input starting shell yourself, by clicking the **Plus sign** icon (**+**) next to **Modules** or **Dynamic Inputs**.

[![Scratch Pad from Windows Menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b752a7e1-f1a6-48b8-9347-d9616bc6693a/ue5_25-scratch-pad-from-windows-menu.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b752a7e1-f1a6-48b8-9347-d9616bc6693a/ue5_25-scratch-pad-from-windows-menu.png)

Click image for full size.

The second way to open the Scratch Pad panel is to use the **Plus sign** icon (**+**) and selecting **New Scratch Pad Module**. This places a Scratch Pad module in your stack (wherever the new module will belong), which is automatically added to your script. You will also see that a shell for the new module or dynamic input is automatically added to your Scratch Pad Graph.

[![New Scratch Pad Module](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a1280161-5967-45e5-b5c5-6b9815f1bb5f/ue5_26-new-scratch-pad-module.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a1280161-5967-45e5-b5c5-6b9815f1bb5f/ue5_26-new-scratch-pad-module.png)

Click image for full size.

## Selection Panel (the Stack)

[![Selection Panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/52ea54e7-cd27-4c83-8c9e-ef9620085b66/ue5_27-selection-panel.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/52ea54e7-cd27-4c83-8c9e-ef9620085b66/ue5_27-selection-panel.png)

Click image for full size.

In the Emitter Nodes and the **Selection** panel, the various groups are color-coded.

* **Orange** is for Emitter-level modules. Orange sections are:
  + **Emitter Settings**: the **Emitter Properties** item is in this group.
  + **Emitter Spawn**: what happens on the first frame.
  + **Emitter Update**: what happens after the first frame, as the emitter is updated.
* **Green** is for Particle-level modules. Green sections are:
  + **Particle Spawn**: what happens when the Particle is created.
  + **Particle Update**: what happens during the Particle's lifetime.
  + **Update Age** and **Solve Forces and Velocity** are normally low-level, boilerplate modules that everyone uses. But these can be removed and are completely optional.
* **Red** is for Renderer items. Niagara decouples simulation from rendering. This means you can create simulation behavior once, then assign multiple renderers to that simulation.

If you select the **System** node in the System Overview, you will see system-related groups that are colored **Blue**.

* **System Settings**: this group includes the User Parameters and System Properties items.
* **System Spawn**: what happens when the system is created.
* **System Update**: what happens during the system's lifetime.

The UI of the Niagara Editor is somewhat complex. The next two sections will highlight some specific elements of the UI that might be confusing to new users.

### Groups in the Selection Panel

[![Groups in Selection Panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b463674b-aa6a-4559-b022-68bd55f7525c/ue5_28-groups-in-selection-panel.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b463674b-aa6a-4559-b022-68bd55f7525c/ue5_28-groups-in-selection-panel.png)

Click image for full size.

When you click on a group in an emitter or system node, that entire group is displayed in the Selection panel. To the right of the group name, you will see a **Plus sign** icon (**+**), colored to match the group. When you click that icon, a list of available module categories displays. Click the dropdown next to the category name to expand it and see the modules in that category. Selecting the name of a module adds that module to the group.

You can also click the **Plus sign** icon in the emitter or system node, directly in the System Overview. The same list will display.

### Modules in the Selection Panel

[![Modules in Selection Panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/64eddf24-4ba6-4240-9696-9cf3fb254fac/ue5_29-modules-in-selection-panel.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/64eddf24-4ba6-4240-9696-9cf3fb254fac/ue5_29-modules-in-selection-panel.png)

Click image for full size.

Depending on the module, you may want to modify a parameter value to achieve a specific outcome. To add a dynamic input, expression, or link to another attribute you can click on the dropdown arrow to the right of the value field you want to modify. A list of available categories displays. When you expand the category, you can select from a list of available options and the selected option will be applied to that value field. For example, to randomize a value you can click the dropdown and select **Dynamic Inputs > Random Ranged Float**.

If you don't see a module or dynamic input you have created in the list, try unchecking **Library Only**.

## Timeline Panel

[![Timeline Panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d66a9328-6d2d-4aa1-95f6-269335b58a5f/ue5_30-timeline-panel.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d66a9328-6d2d-4aa1-95f6-269335b58a5f/ue5_30-timeline-panel.png)

Click image for full size.

With the **Timeline** panel, you can manage looping, loop count, bursts, random starts and stops, and spawn rate. All of these elements can interact right in the Timeline.

In a system, the Timeline panel lists all emitters active in that System, with metadata about what kind of renderers they use and the ability to toggle which emitters are active. You can control looping behavior using the Timeline, and you can set spawn burst keys in it as well. This is driven by module metadata, which can be extended by users if needed.

For more information on using Sequencer, see [Sequencer Editor](/documentation/en-us/unreal-engine/cinematics-and-movie-making-in-unreal-engine).

## Curves Panel

[![Curves](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4bad5fd9-a757-42c7-bf4d-ea3e42ce644a/ue5_31-curves.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4bad5fd9-a757-42c7-bf4d-ea3e42ce644a/ue5_31-curves.png)

Click image for full size.

This panel provides a Curve Editor that enables the user to adjust any values that need to change during the life of a particle, or across the life of an emitter. In order for any property to be editable within the Curve Editor, that property will need to have a Distribution type that utilizes a curve, such as *FloatfromCurve*. See the [Curve Editor User Guide](/documentation/en-us/unreal-engine/animation-curve-editor-in-unreal-engine) page for more details on using the Curve Editor.

## Niagara Log Panel

[![Niagara Log](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8923d801-544a-4d36-805e-edf3bcef79cf/ue5_32-niagara-log.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8923d801-544a-4d36-805e-edf3bcef79cf/ue5_32-niagara-log.png)

Click image for full size.

If there are any warnings or errors when compiling a script, emitter or system, they appear here. For many errors and warnings, you can click it in the Niagara Log panel and jump to the error's location in the Niagara Editor.

## Other Optional Panels

There are some additional panels that are not displayed by default, but that can be opened using the **Window** menu. By default, these panels will display as tabs in the area where the **Selection** panel displays, but you can drag and drop them to dock them somewhere else.

### Attribute Spreadsheet Panel

[![Attribute Spreadsheet](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6380f9c2-bbf4-4a20-86e6-72f12c925055/ue5_33-attribute-spreadsheet.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6380f9c2-bbf4-4a20-86e6-72f12c925055/ue5_33-attribute-spreadsheet.png)

Click image for full size.

With the **Attribute Spreadsheet**, you can filter and debug information coming from the CPU or GPU simulation. For all CPU VM-based effects, you can take advantage of the attribute debugger. It allows you to see the inputs to the simulation as well as the per-particle computed values.

The Attribute Spreadsheet targets the emitter or system previewed in the Preview panel. You can also target systems in a level by setting the in-level system to **Force Solo**, then selecting that system as a target in the Attribute Spreadsheet while you are in PIE (Play In Editor) mode.

### Preview Scene Settings Panel

[![Preview Scene Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6281d26c-4100-4cdf-bbed-74fc738ebec2/ue5_34-preview-scene-settings.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6281d26c-4100-4cdf-bbed-74fc738ebec2/ue5_34-preview-scene-settings.png)

Click image for full size.

This panel contains settings for modifying the Preview panel.

### Generated Code Panel

[![Generated Code Panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/30da6e12-5116-48fd-a541-a8bcc49ec377/ue5_35-generated-code-panel.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/30da6e12-5116-48fd-a541-a8bcc49ec377/ue5_35-generated-code-panel.png)

Click image for full size.

This panel displays the generated HLSL and Assembly code for the selected emitter and owning system. This enables you to view and search that code. This tool is for advanced users who need to debug problems that may be difficult to spot with other methods.

You can select the HLSL or Assembly code being displayed using the Scripts dropdown menu. To view a specific emitter's generated HLSL or Assembly code, follow these steps.

1. Select the emitter in the **System Overview** or **Timeline** panel.
2. Select the desired script under the **Scripts** dropdown menu in the **Generated Code** panel.

* [effects](https://dev.epicgames.com/community/search?query=effects)
* [vfx](https://dev.epicgames.com/community/search?query=vfx)
* [niagara](https://dev.epicgames.com/community/search?query=niagara)
* [visual effects](https://dev.epicgames.com/community/search?query=visual%20effects)
* [particle effects](https://dev.epicgames.com/community/search?query=particle%20effects)
* [emitter editor](https://dev.epicgames.com/community/search?query=emitter%20editor)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Overview](/documentation/en-us/unreal-engine/editor-ui-reference-for-niagara-effects-in-unreal-engine?application_version=5.7#overview)
* [Menu](/documentation/en-us/unreal-engine/editor-ui-reference-for-niagara-effects-in-unreal-engine?application_version=5.7#menu)
* [File](/documentation/en-us/unreal-engine/editor-ui-reference-for-niagara-effects-in-unreal-engine?application_version=5.7#file)
* [Edit](/documentation/en-us/unreal-engine/editor-ui-reference-for-niagara-effects-in-unreal-engine?application_version=5.7#edit)
* [Asset](/documentation/en-us/unreal-engine/editor-ui-reference-for-niagara-effects-in-unreal-engine?application_version=5.7#asset)
* [Window](/documentation/en-us/unreal-engine/editor-ui-reference-for-niagara-effects-in-unreal-engine?application_version=5.7#window)
* [Tools](/documentation/en-us/unreal-engine/editor-ui-reference-for-niagara-effects-in-unreal-engine?application_version=5.7#tools)
* [Toolbar](/documentation/en-us/unreal-engine/editor-ui-reference-for-niagara-effects-in-unreal-engine?application_version=5.7#toolbar)
* [Preview Panel](/documentation/en-us/unreal-engine/editor-ui-reference-for-niagara-effects-in-unreal-engine?application_version=5.7#previewpanel)
* [Parameters Panel](/documentation/en-us/unreal-engine/editor-ui-reference-for-niagara-effects-in-unreal-engine?application_version=5.7#parameterspanel)
* [System Overview Panel](/documentation/en-us/unreal-engine/editor-ui-reference-for-niagara-effects-in-unreal-engine?application_version=5.7#systemoverviewpanel)
* [System Node](/documentation/en-us/unreal-engine/editor-ui-reference-for-niagara-effects-in-unreal-engine?application_version=5.7#systemnode)
* [Emitter Nodes](/documentation/en-us/unreal-engine/editor-ui-reference-for-niagara-effects-in-unreal-engine?application_version=5.7#emitternodes)
* [Scratch Pad Panel](/documentation/en-us/unreal-engine/editor-ui-reference-for-niagara-effects-in-unreal-engine?application_version=5.7#scratchpadpanel)
* [Selection Panel (the Stack)](/documentation/en-us/unreal-engine/editor-ui-reference-for-niagara-effects-in-unreal-engine?application_version=5.7#selectionpanel(thestack))
* [Groups in the Selection Panel](/documentation/en-us/unreal-engine/editor-ui-reference-for-niagara-effects-in-unreal-engine?application_version=5.7#groupsintheselectionpanel)
* [Modules in the Selection Panel](/documentation/en-us/unreal-engine/editor-ui-reference-for-niagara-effects-in-unreal-engine?application_version=5.7#modulesintheselectionpanel)
* [Timeline Panel](/documentation/en-us/unreal-engine/editor-ui-reference-for-niagara-effects-in-unreal-engine?application_version=5.7#timelinepanel)
* [Curves Panel](/documentation/en-us/unreal-engine/editor-ui-reference-for-niagara-effects-in-unreal-engine?application_version=5.7#curvespanel)
* [Niagara Log Panel](/documentation/en-us/unreal-engine/editor-ui-reference-for-niagara-effects-in-unreal-engine?application_version=5.7#niagaralogpanel)
* [Other Optional Panels](/documentation/en-us/unreal-engine/editor-ui-reference-for-niagara-effects-in-unreal-engine?application_version=5.7#otheroptionalpanels)
* [Attribute Spreadsheet Panel](/documentation/en-us/unreal-engine/editor-ui-reference-for-niagara-effects-in-unreal-engine?application_version=5.7#attributespreadsheetpanel)
* [Preview Scene Settings Panel](/documentation/en-us/unreal-engine/editor-ui-reference-for-niagara-effects-in-unreal-engine?application_version=5.7#previewscenesettingspanel)
* [Generated Code Panel](/documentation/en-us/unreal-engine/editor-ui-reference-for-niagara-effects-in-unreal-engine?application_version=5.7#generatedcodepanel)
