<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/pcg-editor-mode-in-unreal-engine?application_version=5.7 -->

# PCG Editor Mode

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
5. [Building Virtual Worlds](/documentation/en-us/unreal-engine/building-virtual-worlds-in-unreal-engine "Building Virtual Worlds")
6. [Procedural Content Generation Framework](/documentation/en-us/unreal-engine/procedural-content-generation-framework-in-unreal-engine "Procedural Content Generation Framework")
7. PCG Editor Mode

# PCG Editor Mode

An overview of the PCG editor tools mode.

![PCG Editor Mode](https://dev.epicgames.com/community/api/documentation/image/6df5e63a-e010-4727-b6cd-9b83f2bf6c16?resizing_type=fill&width=1920&height=335)

Learn to use this **Experimental** feature, but use caution when shipping with it.

 On this page

The **PCG editor tool mode** is a feature you can use to place PCG content in levels, including splines, surfaces, painting, and volumes, using a library of customizable tools to create presets that leverage the PCG framework, each with an associated PCG Graph and parameters.

If you used the UE 5.7 preview, your PCG Editor Mode settings might not
have the default setup. If your PCG Editor Mode window does not open and
instead shows an error, open the **Plugins - PCG Editor Mode Settings** in the **Editor Preferences**, then click **Reset to Defaults** in the upper right corner.

To access the PCG editor mode, open the **Modes** dropdown menu and select **PCG**.

[![PCG in the Mode menu](https://dev.epicgames.com/community/api/documentation/image/b3e4c4b9-2596-47f7-89d4-07b0ae70a730?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b3e4c4b9-2596-47f7-89d4-07b0ae70a730?resizing_type=fit)

While this is a first version of this mode, we will improve it over time and make it flexible, so that in addition to setting up and placing default graphs and actors, you can also extend the available tools.

[![PCG editor tools](https://dev.epicgames.com/community/api/documentation/image/cd963921-f30e-4f34-87a3-7f2a4339fd92?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cd963921-f30e-4f34-87a3-7f2a4339fd92?resizing_type=fit)

## PCG Mode Tools

When you select one of the tools, the results depend on whether you have an appropriate actor selected.

* If an actor is selected, it adds a PCG component to the actor if needed, and creates a new tool data asset if none exists.
* If no actor is selected, an actor is created to perform the operation, which changes based on the selected graph or preset.

Tool buttons are disabled when you select an actor that isn't the correct actor class or that doesn’t have the right components for the graph to run properly on it. Similarly, any presets that aren't compatible with the selected actor aren't shown.

Click on a tool button to start using the tool. This displays the **Apply** and **Cancel** buttons and a secondary row of buttons for presets.

[![PCG tools and presets](https://dev.epicgames.com/community/api/documentation/image/f1a46667-901c-4625-af3b-ea7654738497?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f1a46667-901c-4625-af3b-ea7654738497?resizing_type=fit)

Presets are graphs and instances that are marked as tool presets. They are a quick way to select a graph without using the dropdown menu. Using a preset is functionally equivalent to selecting a graph from the dropdown menu.

## Tool Instance Settings

When you select a tool, the panel shows the instance settings that you can access on the PCG component directly, which provides a way for you to change them while interacting with the tool.

[![PCG instance settings](https://dev.epicgames.com/community/api/documentation/image/c8032f0f-0d92-4218-8dcf-c288efe5cc7b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c8032f0f-0d92-4218-8dcf-c288efe5cc7b?resizing_type=fit)

| Instance Setting | Description |
| --- | --- |
| **Tool Graph** | This graph is set on the PCG component; it drives what parameters are available, and you can use it to select the actor class when creating a new actor. |
| ****Parameter** Overrides** | All the graph parameters that are exposed on the graph are available here. |
| **Data Instance** | Defines which ‘data instance’ the tool writes to. This has limited use for splines or volumes, but for painting tools, it provides you with a way to write to different layers (and do different processing per layer). You can change layers with keyboard shortcuts (1, 2, …) |
| **Actor Label** | The label of the spawned actor, if none were selected. Changing the label here renames the actor. The default value comes from the graph’s tool settings. |
| **Component Name** | The name of the component added to the actor (if you are not using an existing one). |
| ****Actor** Class to Spawn** | This is the class of the actor spawned when starting the tool with no selection. This can be changed only when the tool has spawned the actor itself, and loses the tool data when changing classes.  However, it provides a way for you to create BP actors for more complex setups. This field is not visible when starting the tool on an existing actor, as in that state it is not possible to change the actor’s class. |

## PCG ModeTools

### Draw Spline

You can use the **Draw Spline** mode to place objects “on a spline” projected on the environment. Examples include fences, roads, and similar, and works with open and closed splines. This is similar to other spline creation modes, except it is tailored for PCG. Graphs that support this tool have the **SplineTool** tool tag in their properties.

[![PCG Draw Spline tool](https://dev.epicgames.com/community/api/documentation/image/570a852d-8097-4d34-9151-2ed763b73b2c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/570a852d-8097-4d34-9151-2ed763b73b2c?resizing_type=fit)

### Draw Spline Surface

You can use the **Draw Spline Surface** mode to define a spline-bound closed area, inside which a PCG graph populates the interior. Examples include fields, cornrows, grass, and similar. This tool uses the **SplineSurfaceTool** tool tag.

[![PCG Draw Spline Surface tool](https://dev.epicgames.com/community/api/documentation/image/e5a23d7f-7270-44f9-95eb-985a9e5cc007?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e5a23d7f-7270-44f9-95eb-985a9e5cc007?resizing_type=fit)

### Paint

The **Paint** tool provides a way for you to paint on the world (based on collisions), or on the selected actor and is similar to the [Foliage mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/foliage-mode-in-unreal-engine).

This creates points at the locations where raycasts hit physical objects. You can also remove points when holding the shift key (the brush becomes red). This tool uses the **PaintTool** tool tag.

[![PCG Paint tool](https://dev.epicgames.com/community/api/documentation/image/c59af95c-3e5b-4d87-b42b-b0d878e2ec75?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c59af95c-3e5b-4d87-b42b-b0d878e2ec75?resizing_type=fit)

### Volume

The **Volume** tool provides a way for you to create new PCG volumes by first dragging out the footprint, then the height of the box. This tool is disabled unless the actor is a volume or has a box component. This tool uses the **VolumeTool** tool tag.

[![PCG Volume tool](https://dev.epicgames.com/community/api/documentation/image/0d1825ce-d1ee-4472-a962-1d7761ea7e27?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0d1825ce-d1ee-4472-a962-1d7761ea7e27?resizing_type=fit)

## Tool-specific Controls

### Spline Controls

Draw modes control how you interact with the tool and are similar to other [spline tools](https://dev.epicgames.com/documentation/en-us/unreal-engine/draw-spline-tool-in-unreal-engine).

### Raycast Rules

[![PCG raycast rules](https://dev.epicgames.com/community/api/documentation/image/86a3a84f-0e9d-48a4-9c0d-9b05fd61eff6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/86a3a84f-0e9d-48a4-9c0d-9b05fd61eff6?resizing_type=fit)

The **Raycast Rules** control how several tools interact with the world. When enabled, each rule defines a particular interaction with your project.

| Raycast Rule | Description |
| --- | --- |
| **Landscape** | Accepts interaction on the landscape. |
| **Meshes** | Accepts interaction with meshes (for example, actors with collisions). |
| **Ignore PCG Components** | Rejects interaction on PCG-created components. |
| **Allowed Classes** | Accepts interaction only on actor classes in the list (or derived from a parent class in the list). |
| **Constrain to Actor** | Accepts only interactions on the selected actor. |

## Setting Up a Tool Graph

To set up a tool graph, look in the PCG Graph settings in the **Tool Data** section, and then set the values as appropriate for your new tool graph.

[![Setting up a tool graph for PCG](https://dev.epicgames.com/community/api/documentation/image/30dbb36d-3090-42f0-92c5-633971c50f79?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/30dbb36d-3090-42f0-92c5-633971c50f79?resizing_type=fit)

| Tool Data Graph Settings | Description |
| --- | --- |
| **Display Name** | Defines the name shown on the tool preset buttons. |
| **Tooltip** | Defines the tooltip shown when hovering over the tool preset button. |
| **Compatible Tool Tags** | Lists the compatible tags you can use this graph with. You must set this for the graph to appear in the graph drop-down in the matching tool.  The current valid values are:   * **SplineTool** * **SplineSurfaceTool** * **PaintTool** * **VolumeTool** |
| **Initial Actor Class To Spawn** | This setting defines the actor class to spawn when starting the tool from no selection, and acts as a restriction on what actor classes match with this graph.  For example, if this is set to PCG Volume, then if the selection is not a PCG Volume, the graph will not show up in the tool graph drop-down. |
| **New Actor Label** | Defines the default actor label used when spawning an actor. |
| **Is Preset** | Controls whether the graph will appear as a tool preset button or not. You can override this in instances. |

## Setting Up an Instance as a Preset

In a similar way to a tool graph, the graph instances have a **Tool Data Override** section.

[![PCG Tool Data Overrides](https://dev.epicgames.com/community/api/documentation/image/0cae81b5-0fdf-4fcb-a367-c8e34f020d23?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0cae81b5-0fdf-4fcb-a367-c8e34f020d23?resizing_type=fit)

| Tool Data Override | Description |
| --- | --- |
| **Display Name** | The same as for graphs. |
| **Tooltip** | The same as for graphs. |
| **Is Preset** | Defines whether this instance is a preset or not, regardless of the value on the original graph. |

## PCG Editor Mode Settings

[![PCG editor mode tool settings](https://dev.epicgames.com/community/api/documentation/image/e3c734ab-0388-454f-961e-4aa4ea2dacaa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e3c734ab-0388-454f-961e-4aa4ea2dacaa?resizing_type=fit)

The **PCG Editor Mode settings** control the behavior of the PCG tool mode and are found in **Editor Preferences > PCG Editor Mode Settings**.

| PCG Editor Mode Setting | Description |
| --- | --- |
| **Graph Refresh Rate** | Defines the rate at which changes are propagated for PCG to pick them up. If generation is very slow, you can increase this value. |
| **Hide Tool Buttons During Active Tool** | If enabled, when you enter a tool, the UI hides the tool row, and only shows the presets. |
| **Show Editor Toast on Tool Errors** | Controls whether errors will be shown in a toast or just on the tool window. |
| **Interactive Tool Settings** | Defines what tool controls are shown, and their defaults. If this list is empty, it is populated with Reset To Defaults.  This list contains pairs of:   1. The tool class settings. 2. The default graph to select when launching this graph.   The default graphs should work on the actor class by default, otherwise the tool will not always open. |
| **Default New Actor Name** | If an actor's name isn’t provided in the graph, it uses this value instead. |
| **Default New PCG Component Name** | If a PCG component's name isn’t provided in the graph, it uses this value instead. |
| **Default New Spline Component Name** | If a Spline component's name isn’t provided in the graph, it uses this value instead. |

* [pcg](https://dev.epicgames.com/community/search?query=pcg)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [PCG Mode Tools](/documentation/en-us/unreal-engine/pcg-editor-mode-in-unreal-engine?application_version=5.7#pcgmodetools)
* [Tool Instance Settings](/documentation/en-us/unreal-engine/pcg-editor-mode-in-unreal-engine?application_version=5.7#toolinstancesettings)
* [PCG ModeTools](/documentation/en-us/unreal-engine/pcg-editor-mode-in-unreal-engine?application_version=5.7#pcgmodetools-2)
* [Draw Spline](/documentation/en-us/unreal-engine/pcg-editor-mode-in-unreal-engine?application_version=5.7#drawspline)
* [Draw Spline Surface](/documentation/en-us/unreal-engine/pcg-editor-mode-in-unreal-engine?application_version=5.7#drawsplinesurface)
* [Paint](/documentation/en-us/unreal-engine/pcg-editor-mode-in-unreal-engine?application_version=5.7#paint)
* [Volume](/documentation/en-us/unreal-engine/pcg-editor-mode-in-unreal-engine?application_version=5.7#volume)
* [Tool-specific Controls](/documentation/en-us/unreal-engine/pcg-editor-mode-in-unreal-engine?application_version=5.7#tool-specificcontrols)
* [Spline Controls](/documentation/en-us/unreal-engine/pcg-editor-mode-in-unreal-engine?application_version=5.7#splinecontrols)
* [Raycast Rules](/documentation/en-us/unreal-engine/pcg-editor-mode-in-unreal-engine?application_version=5.7#raycastrules)
* [Setting Up a Tool Graph](/documentation/en-us/unreal-engine/pcg-editor-mode-in-unreal-engine?application_version=5.7#settingupatoolgraph)
* [Setting Up an Instance as a Preset](/documentation/en-us/unreal-engine/pcg-editor-mode-in-unreal-engine?application_version=5.7#settingupaninstanceasapreset)
* [PCG Editor Mode Settings](/documentation/en-us/unreal-engine/pcg-editor-mode-in-unreal-engine?application_version=5.7#pcgeditormodesettings)
