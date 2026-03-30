<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/primitive-debugger-in-unreal-engine?application_version=5.7 -->

# Primitive Debugger

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
5. [Designing Visuals, Rendering, and Graphics](/documentation/en-us/unreal-engine/designing-visuals-rendering-and-graphics-with-unreal-engine "Designing Visuals, Rendering, and Graphics")
6. [Optimizing and Debugging Projects for Real-Time Rendering](/documentation/en-us/unreal-engine/optimizing-and-debugging-projects-for-realtime-rendering-in-unreal-engine "Optimizing and Debugging Projects for Real-Time Rendering")
7. Primitive Debugger

# Primitive Debugger

This is a runtime-only tool to view information about primitives being rendered in the game client.

![Primitive Debugger](https://dev.epicgames.com/community/api/documentation/image/99bc3287-c96b-4f1d-bdb7-a9b497af147d?resizing_type=fill&width=1920&height=335)

Learn to use this **Experimental** feature, but use caution when shipping with it.

 On this page

The **Primitive Debugger** is a runtime-only tool used to view information about primitives being rendered in the game client such as draw calls and LOD information.

## Using the Primitive Debugger

To launch the Primitive Debugger:

1. Run a **Development** or **Test** client.
2. Open the console with backtick key and enter the command `PrimitiveDebugger.Open`.
3. The **Primitive Debugger** window will appear and be populated by a list of primitives that were being rendered at the time the window was open.
4. To refresh the list of displayed primitives, press the **Refresh** button.

   Primitives that are destroyed during gameplay will be automatically removed from the list.

## Features of the Primitive Debugger

### List and Detail Views

Within the Primitive Debugger, you can filter the primitive list shown to you by using the search bar at the top. The search bar supports filtering the following properties by name:

* Primitive name
* Actor name
* Component name
* Actor class
* Component class
* Material name
* Texture name

You can toggle visibility of each listed primitive as well as pin them to the top of the list for quick access. Scrolling the list shows the name of the actor for each primitive. When you select a table row opens up a Details panel with additional properties for the selected primitive.

This includes the following:

* Triangle count (non-nanite meshes)
* Location in world space
* Current LOD (non-nanite meshes)
* Total available LODs (non-nanite meshes)
* Nanite support and usage
* Materials
* Textures used
* Draw calls
* Component and Actor type
* Component and Actor name
* Skeletal mesh bone count

![Details Panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b310754e-53a3-49cb-a154-c45fc6a7476e/rpd-1.png)

Details Panel

### Debugging Controls and Visualizations

The Details panel provides some basic debugging tools depending on the configuration of the current build. A slider is available for all non-Nanite meshes to force a specific level of detail (LOD) for the primitive, updating the model shown in game.

Nanite meshes have an option to force disable Nanite rendering for them, causing the game to instead render a normal static mesh in its place. This option is useful for checking differences between Nanite and non-Nanite material variations, or checking for other visual inconsistencies and performance impacts.

In Development builds, skeletal meshes can display a debug visualization of the bones in its skeleton, updated in real time similar to what can be seen in the editor. This can be helpful to spot animation or rigging errors. Development builds also support displaying a debug bounding box around any primitive in the level, which will also be updated in real time. These bounds are different from the collider, and will represent the maximum extents of the primitive in 3D space.

|  |  |
| --- | --- |
| [undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/91f4ded8-4b9f-40ad-9a9c-59afa07d38c4/rpd-2.png) | [undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c6aa7ef1-8a75-4114-943e-5404a63c7c09/rpd-3.png) |
| Debug visualization of skeleton. | Debug bounds visualization. |

Click images for full size.

Once you’re finished using the debug visualizations and using the tool, you can close the window to automatically undo any of the changes that have been made.

### Saving a Snapshot

The contents of the primitive list, including the details of each primitive, can be saved to the disk for later reference by using the **Save to CSV** option located in the top right of the window. This will dump all primitives recorded in the current snapshot, including those hidden by the search filter, to a csv file which can be found in the project’s **Saved/Profiling/Primitives/** folder in a timestamped **PrimitivesDetailed.csv** file. Alternatively, this action can be performed from the command line by using the command **DumpDetailedPrimitives** from the in-game command line.

## Limitations and Future Changes

These are some known limitations of the Primitive Debugger:

* Debug visualizations are only available in Development configurations.
* This tool is not supported in the editor and is designed to be used only in a built client binary.
* Non-mesh primitives such as Niagara emitters currently have limited support.
* The displayed draw call information may not provide the complete picture for instanced meshes. Currently the draw calls are computed as if the mesh exists by itself without batching.

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [experimental](https://dev.epicgames.com/community/search?query=experimental)
* [performance and profiling](https://dev.epicgames.com/community/search?query=performance%20and%20profiling)
* [debugging](https://dev.epicgames.com/community/search?query=debugging)
* [primitives](https://dev.epicgames.com/community/search?query=primitives)
* [runtime](https://dev.epicgames.com/community/search?query=runtime)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Using the Primitive Debugger](/documentation/en-us/unreal-engine/primitive-debugger-in-unreal-engine?application_version=5.7#usingtheprimitivedebugger)
* [Features of the Primitive Debugger](/documentation/en-us/unreal-engine/primitive-debugger-in-unreal-engine?application_version=5.7#featuresoftheprimitivedebugger)
* [List and Detail Views](/documentation/en-us/unreal-engine/primitive-debugger-in-unreal-engine?application_version=5.7#listanddetailviews)
* [Debugging Controls and Visualizations](/documentation/en-us/unreal-engine/primitive-debugger-in-unreal-engine?application_version=5.7#debuggingcontrolsandvisualizations)
* [Saving a Snapshot](/documentation/en-us/unreal-engine/primitive-debugger-in-unreal-engine?application_version=5.7#savingasnapshot)
* [Limitations and Future Changes](/documentation/en-us/unreal-engine/primitive-debugger-in-unreal-engine?application_version=5.7#limitationsandfuturechanges)
