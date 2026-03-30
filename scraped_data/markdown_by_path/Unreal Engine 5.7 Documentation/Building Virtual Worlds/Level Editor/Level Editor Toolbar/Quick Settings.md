<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/quick-settings-in-the-unreal-engine-level-toolbar?application_version=5.7 -->

# Quick Settings

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
6. [Level Editor](/documentation/en-us/unreal-engine/level-editor-in-unreal-engine "Level Editor")
7. [Level Editor Toolbar](/documentation/en-us/unreal-engine/level-editor-toolbar-in-unreal-engine "Level Editor Toolbar")
8. Quick Settings

# Quick Settings

Configure selection, editing, and preview in the Level Viewport.

![Quick Settings](https://dev.epicgames.com/community/api/documentation/image/201808e6-1213-4b4f-b22b-4bab98beafb9?resizing_type=fill&width=1920&height=335)

 On this page

The **Settings** menu in the **Level Editor Toolbar** contains a set of properties that control selecting, editing, and previewing in the Level Viewport. Open the Settings menu from the Main Toolbar (also known as the [Level Editor Toolbar](/documentation/en-us/unreal-engine/level-editor-toolbar-in-unreal-engine)).

![Settings button in the Main Toolbar](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e1ee1e38-a58c-4396-96cb-a57257cbcf5d/ue5_1-main-toolbar-settings-button.png)

The Settings menu contains the following groups of settings:

* Selection
* Scalability
* Real Time Audio
* Snapping
* Viewport
* Previewing

## Selection

| **Option** | **Description** |
| --- | --- |
| **Allow Translucent Selection** | If enabled, clicking geometry with translucent Materials applied selects the Actor.  Enabling this option makes it possible to select transparent meshes, such as glass objects. Disabling it can be useful in other cases. For example, if you have a room filled with translucent particles, selecting other objects in the room would be difficult with this option enabled because clicking the particles would select the Emitter Actor. |
| **Allow Group Selection** | If enabled, selecting an Actor in a group selects the whole group instead of the individual Actor. |
| **Strict Box Selection** | If enabled, an Actor must be completely within the marquee selection box in order to be selected. |
| **Box Select Occluded Objects** | If enabled, marquee box select operations also select objects that are occluded by other objects. |
| **Show Transform Widget** | Toggles the visibility of the Transform widget in Viewports. |

## Scalability

| **Option** | **Description** |
| --- | --- |
| **Engine Scalability Settings** | Provides quick access to [Scalability](/documentation/en-us/unreal-engine/scalability-in-unreal-engine) settings that control the fidelity of various rendering features.  Enable the **Monitor Engine Performance?** option to see how changing this settings affects your project's performance in real time. |
| **Material Quality Level** | Sets the Material quality level used for previewing in the Viewports.  See [Material Quality Switch Expression](/documentation/en-us/unreal-engine/utility-material-expressions-in-unreal-engine#qualityswitch) for more information on setting up Materials to work with this setting. |
| **Preview Rendering Level** | Sets the rendering level used by the editor. You can restrict rendering quality to device-specific capabilities, including different version of:   * Android * iOS * D3D |

## Real Time Audio

| **Option** | **Description** |
| --- | --- |
| **Volume** | Controls the volume of Level audio that plays when the Viewport is set to realtime. |

## Snapping

| **Option** | **Description** |
| --- | --- |
| **Enable Actor Snapping** | If enabled, Actors snap to the location of other Actors if they are within a specified distance. |
| **Distance** | Sets the distance Actors must be within in order to snap to one another if **Enable Actor Snapping** is enabled. |
| **Enable Socket Snapping** | If enabled, Actors can snap to sockets. |
| **Enable Vertex Snapping** | If enabled, Actors snap to the nearest vertex on another Actor in the direction of movement. |
| **Enable Planar Snapping** | If enabled, Actors snap to the nearest location on the constraint plane. This only works correctly in Perspective views. |

## Viewport

| **Option** | **Description** |
| --- | --- |
| **Hide Viewport UI** | Hides the Viewport toolbar and all Viewport UI widgets. |

## Previewing

| **Option** | **Description** |
| --- | --- |
| **Draw Brush Polys** | If enabled, semi-translucent polygons are rendered for the faces of a CSG (constructive Solid Geometry) brush when selected. |
| **Only Load Visible Levels in Game Preview** | If enabled, only visible levels will be loaded when game preview starts. |
| **Enable Particle System LOD Switching** | If enabled, particle systems will use distance LOD switching in perspective Viewports. |
| **Toggle Particle System Helpers** | If enabled, shows particle system helpers in Viewports. |
| **Freeze Particle Simulation** | If enabled, particle systems freeze their simulation state. |
| **Enable LOD View Locking** | If enabled, Viewports of the same type use the same LOD. |
| **Enable Automatic Level Streaming** | If enabled, the Viewport will stream in levels automatically when the camera moves. |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Selection](/documentation/en-us/unreal-engine/quick-settings-in-the-unreal-engine-level-toolbar?application_version=5.7#selection)
* [Scalability](/documentation/en-us/unreal-engine/quick-settings-in-the-unreal-engine-level-toolbar?application_version=5.7#scalability)
* [Real Time Audio](/documentation/en-us/unreal-engine/quick-settings-in-the-unreal-engine-level-toolbar?application_version=5.7#realtimeaudio)
* [Snapping](/documentation/en-us/unreal-engine/quick-settings-in-the-unreal-engine-level-toolbar?application_version=5.7#snapping)
* [Viewport](/documentation/en-us/unreal-engine/quick-settings-in-the-unreal-engine-level-toolbar?application_version=5.7#viewport)
* [Previewing](/documentation/en-us/unreal-engine/quick-settings-in-the-unreal-engine-level-toolbar?application_version=5.7#previewing)

Related documents

[Selecting Actors

![Selecting Actors](https://dev.epicgames.com/community/api/documentation/image/1e7dc513-0737-460d-9c31-ab849738c7c2?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/selecting-actors-in-unreal-engine)

[Actor Snapping

![Actor Snapping](https://dev.epicgames.com/community/api/documentation/image/ea33013f-4d72-4356-a700-8885b1178cfd?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/actor-snapping-in-unreal-engine)
