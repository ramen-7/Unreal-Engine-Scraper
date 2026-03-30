<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-track-list-in-unreal-engine?application_version=5.7 -->

# Tracks

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
5. [Animating Characters and Objects](/documentation/en-us/unreal-engine/animating-characters-and-objects-in-unreal-engine "Animating Characters and Objects")
6. [Cinematics and Sequencer](/documentation/en-us/unreal-engine/cinematics-and-movie-making-in-unreal-engine "Cinematics and Sequencer")
7. [Sequencer Overview](/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview "Sequencer Overview")
8. Tracks

# Tracks

Create tracks that affect your actors in Sequencer.

![Tracks](https://dev.epicgames.com/community/api/documentation/image/62175723-31e6-495b-83b3-08e407a6f5f8?resizing_type=fill&width=1920&height=335)

 On this page

In Sequencer, Actor properties and other elements are accessed by the adding of tracks to your timeline. Depending on the track's type, they can be used to organize your tracks, create keyframes, or enable other auxiliary functions.

#### Prerequisites

* You have an understanding of [Sequencer](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-make-movies-in-unreal-engine) and its [Interface](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine).

## Track List

Below is a list of the main tracks you can add in Sequencer.

* [![Object Binding Track](images/static/document_list/empty_thumbnail.svg)

  Object Binding Track

  The Object Binding Track is a track that binds Actors and Objects to Sequencer and provides controls to manipulate their specialized properties or components.](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-actor-tracks-in-unreal-engine)
* [![Animation Track](images/static/document_list/empty_thumbnail.svg)

  Animation Track

  The Animation Track enables the adding of Animation Sequences to your Skeletal Mesh track.](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-animation-track-in-unreal-engine)
* [![Audio Track](https://dev.epicgames.com/community/api/documentation/image/f9f569d3-faa2-4cf7-b2ff-b6ebbb77cc7d?resizing_type=fit&width=640&height=640)

  Audio Track

  An overview of the animation blending tools for non-linear animation.](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-audio-track-in-unreal-engine)
* [![Event Track](images/static/document_list/empty_thumbnail.svg)

  Event Track

  Event Tracks support the creation of custom events that are scripted in a dedicated Sequencer Blueprint layer.](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-event-track-in-unreal-engine)
* [![Geometry Cache Track](https://dev.epicgames.com/community/api/documentation/image/1d17a75e-6e63-41e9-a111-aca015b98e62?resizing_type=fit&width=640&height=640)

  Geometry Cache Track

  The Geometry Cache Track enables the scrubbing and playback of cloth and other Alembic mesh simulations on Static Meshes.](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-geometry-cache-track-in-unreal-engine)
* [![Fade Track](https://dev.epicgames.com/community/api/documentation/image/7ed3d8f3-ed96-49bf-aa5c-7e9480ecf183?resizing_type=fit&width=640&height=640)

  Fade Track

  The Fade Track in Sequencer is used to fade the entire screen to a solid color. With it, you can fade to black, white, or any other color.](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-color-fade-track-in-unreal-engine)
* [![Level Visibility Track](images/static/document_list/empty_thumbnail.svg)

  Level Visibility Track

  Set the contents of Levels to be visible or hidden with the Level Visibility track.](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-level-visibility-track-in-unreal-engine)
* [![Material Tracks](images/static/document_list/empty_thumbnail.svg)

  Material Tracks

  Animate Materials in Sequencer in various ways using Material Tracks with different features.](https://dev.epicgames.com/documentation/en-us/unreal-engine/animate-materials-in-unreal-engine-cinematic)
* [![Time Dilation Track](https://dev.epicgames.com/community/api/documentation/image/70114465-a7f5-40eb-a714-f2c5cf6493e1?resizing_type=fit&width=640&height=640)

  Time Dilation Track

  Speed up or slow down your Cinematics with the Time Dilation Track.](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-playback-rate-in-unreal-engine)
* [![Subsequences Track](images/static/document_list/empty_thumbnail.svg)

  Subsequences Track

  Organize and enable multiple artists to work in the same sequence by using the Subsequences Track.](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-subscequences-track-in-unreal-engine)
* [![Media Track](images/static/document_list/empty_thumbnail.svg)

  Media Track

  The Media Track provides controls for the playback of movies and images from Sequencer using Unreal Engine's Media Framework features.](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-movie-media-track-in-unreal-engine)
* [![Camera Cut Track](https://dev.epicgames.com/community/api/documentation/image/54199af4-b796-4146-97ad-b9768aac444c?resizing_type=fit&width=640&height=640)

  Camera Cut Track

  The Camera Cut Track controls which Cine Camera Actor is currently active during playback in Sequencer.](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-camera-cut-track-in-unreal-engine)
* [![Folder Track](images/static/document_list/empty_thumbnail.svg)

  Folder Track

  Folder Tracks allow for the organization of your tracks within Sequencer's Outliner.](https://dev.epicgames.com/documentation/en-us/unreal-engine/organize-cinematic-tracks-in-unreal-engine)
* [![Transform and Property Tracks](images/static/document_list/empty_thumbnail.svg)

  Transform and Property Tracks

  Sequencer's Property Tracks are used to animate an Actor's common variables or properties such as transform, floats, or color.](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-transform-and-property-tracks-in-unreal-engine)
* [![Console Variable Track](https://dev.epicgames.com/community/api/documentation/image/d17e875b-907c-447c-b19d-344dba7b197d?resizing_type=fit&width=640&height=640)

  Console Variable Track

  Adjust render settings and other console variables in your real-time cinematic using the Console Variable Track](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-console-variable-track-in-unreal-engine)
* [![Customizable Sequencer Track](https://dev.epicgames.com/community/api/documentation/image/89b3584e-885b-4fb4-8359-f88d953ee49d?resizing_type=fit&width=640&height=640)

  Customizable Sequencer Track

  Create your own tracks for use in Sequencer using Blueprints and the Customizable Sequencer Track feature.](https://dev.epicgames.com/documentation/en-us/unreal-engine/customizable-sequencer-track-in-unreal-engine)

## Adding Tracks

Sequencer provides a variety of ways to add tracks to your timeline.

Clicking **Add Track (+)** in Sequencer's Outliner reveals the list of tracks to add to your sequence. Select any track here to add it to Sequencer.

[![sequencer track list](https://dev.epicgames.com/community/api/documentation/image/f0f48154-87f8-4ee7-bac6-7ef226240b5c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f0f48154-87f8-4ee7-bac6-7ef226240b5c?resizing_type=fit)

Right-clicking in the empty region of the outliner will also bring up the track list.

[![sequencer track list](https://dev.epicgames.com/community/api/documentation/image/b797c6f1-6f30-4080-827f-7b1857245ae3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b797c6f1-6f30-4080-827f-7b1857245ae3?resizing_type=fit)

### Adding Actors

One of the most common track Sequencer uses is the [Object Binding Track](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-actor-tracks-in-unreal-engine). These are tracks that bind to **Skeletal Meshes**, **Static Meshes**, **Effects**, **Blueprints**, **Components** and other objects in a Level.

You can add Actors to your sequence by navigating in the **Add Track (+)** menu to the **Actor To Sequencer** submenu. Here you can choose any Actor currently in your Level to add to your sequence, or you can also search for a specific Actor using the search bar.

[![actor to sequencer](https://dev.epicgames.com/community/api/documentation/image/ed04fb8a-a83f-49f7-a15c-418e26d685eb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ed04fb8a-a83f-49f7-a15c-418e26d685eb?resizing_type=fit)

If an Actor is already selected in your Level, then it will be listed at the top of the **Actor To Sequencer** list for convenience.

You can also drag Actors from other windows, like the  and add them into Sequencer.

[![actor to sequencer drag drop](https://dev.epicgames.com/community/api/documentation/image/a92f420a-7b9b-436f-92be-359df18eabdd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a92f420a-7b9b-436f-92be-359df18eabdd?resizing_type=fit)

Actors can also be added as [Spawnables](animating-characters-and-objects/Sequencer/Overview/SpawnablesPossessables) by dragging them from the [Content Browser](https://dev.epicgames.com/documentation/en-us/unreal-engine/content-browser-in-unreal-engine) or [Place Actors](https://dev.epicgames.com/documentation/en-us/unreal-engine/placing-actors-in-unreal-engine) panels.

[![actor to sequencer content browser place actor](https://dev.epicgames.com/community/api/documentation/image/4bcc611a-3753-4598-b544-7858ad82c655?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4bcc611a-3753-4598-b544-7858ad82c655?resizing_type=fit)

### Adding Components

Some tracks allow for components and other track types to be added under their main header track. This is done to access specific track functionality, such as transform, components, properties, and other similar features.

To add a component track, hover over the track and click **Add Track (+)** to view a list of tracks available for the selected track. Typically, this list will be filtered based on the types of tracks and components that track or Actor can support.

[![add child track](https://dev.epicgames.com/community/api/documentation/image/285ba8d0-3a95-4047-8c7a-48781d8edb8e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/285ba8d0-3a95-4047-8c7a-48781d8edb8e?resizing_type=fit)

As you can with most menus in Unreal Engine, you can type to filter the results in the **Add Track (+)** menu, making it easier to locate a specific property, component, or other track to add.

[![type to filter tracks](https://dev.epicgames.com/community/api/documentation/image/b6cf26aa-0703-4705-94e8-505de6e9c0b3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b6cf26aa-0703-4705-94e8-505de6e9c0b3?resizing_type=fit)

## Organization

Most tracks have properties that allow for them to be edited and displayed in different ways. These properties are saved in Sequencer and can be shared with others working on your project.

### Renaming

To assist in organization, all top-level tracks and components can be renamed in Sequencer. You can rename a track by triple-clicking on the track text, or right-clicking and selecting **Rename**, or by pressing **F2**.

[![rename track](https://dev.epicgames.com/community/api/documentation/image/cb6c642a-3b66-45e3-bd03-e64f6acb18b6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cb6c642a-3b66-45e3-bd03-e64f6acb18b6?resizing_type=fit)

When renaming a track bound to an Actor in the Level, the Actor in the level also renames.

[![rename track renames actor](https://dev.epicgames.com/community/api/documentation/image/0dbf7797-b207-4323-a480-8dc59d8eeae0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0dbf7797-b207-4323-a480-8dc59d8eeae0?resizing_type=fit)

Most, but not all tracks can be renamed. Typically, you cannot rename a track if it is a property. However, some property tracks can be renamed, such as Transform.

[![rename track restrict](https://dev.epicgames.com/community/api/documentation/image/a9680aac-0b89-4eb3-bf83-dc85681a4349?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a9680aac-0b89-4eb3-bf83-dc85681a4349?resizing_type=fit)

*Tracks in Green can be renamed, tracks in Red cannot.*

### Lock

Tracks can be locked to prevent keyframes on them and their subtracks from being edited. Right-click a track and select **Locked** to lock that track. When a track is locked, all keyable tracks under it will display with a red border denoting the lock state.

[![lock track](https://dev.epicgames.com/community/api/documentation/image/1c890c8a-11ff-4bb0-9e70-3443e2944297?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1c890c8a-11ff-4bb0-9e70-3443e2944297?resizing_type=fit)

### Pin

You can **Pin** tracks so that they will appear in a separate outliner section at the top of your Sequencer outliner. Right-click a track and select **Pinned** to pin that track.

[![pin track](https://dev.epicgames.com/community/api/documentation/image/fc4018c2-90e3-4d4b-8a18-c10b4c576efb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fc4018c2-90e3-4d4b-8a18-c10b4c576efb?resizing_type=fit)

Only one track can be pinned within each sequence.

### Mute

Muting tracks causes them to become inactive and to not display any of their properties or keyframe results from Sequencer. Right-click a track and select **Mute** to mute that track.

[![mute track](https://dev.epicgames.com/community/api/documentation/image/1efbc802-9df5-4859-af3d-ed4cffe966f7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1efbc802-9df5-4859-af3d-ed4cffe966f7?resizing_type=fit)

If the **[Object Binding Track](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-actor-tracks-in-unreal-engine)** is muted, it will also hide the Actor in the viewport.

### Solo

When you **Solo** a track, all other tracks will be muted, allowing for the soloed track to be viewed in isolation. Right-click a track and select **Solo** to solo that track.

[![solo track](https://dev.epicgames.com/community/api/documentation/image/b3d55f7c-f931-4884-ab5c-15aec4426039?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b3d55f7c-f931-4884-ab5c-15aec4426039?resizing_type=fit)

Soloing and muting are editor-only operations and do not impact the Level at runtime, unless you are previewing through **[Play In Editor](building-virtual-worlds/level-editor/in-editor-testing)**.

### Reordering

Tracks can be reordered in the outliner by dragging them above or below each other. Visual cues appear when dragging to indicate where the track will be placed.

[![reorder tracks](https://dev.epicgames.com/community/api/documentation/image/dc7fdcc7-dbf4-4bb8-896c-6e8e0c8e0b4d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dc7fdcc7-dbf4-4bb8-896c-6e8e0c8e0b4d?resizing_type=fit)

## Search and Filter

You can search and filter for specific track names using Sequencer's search field. Typing the full or partial name of a track will filter out tracks that do not match that name and will include child tracks as part of its search.

[![search track](https://dev.epicgames.com/community/api/documentation/image/92593b2a-17bb-4fc4-aa6d-7c66e4b7b744?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/92593b2a-17bb-4fc4-aa6d-7c66e4b7b744?resizing_type=fit)

Clicking the **Filters** button will also reveal a list of common track types that you can filter for.

[![filter track](https://dev.epicgames.com/community/api/documentation/image/14af237b-a12a-4c6a-8a09-33c7bdc14a1b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/14af237b-a12a-4c6a-8a09-33c7bdc14a1b?resizing_type=fit)

When a filter is applied, the **Filter** button will indicate with a red dot.

[![filter indication](https://dev.epicgames.com/community/api/documentation/image/63a4e511-9b32-41d5-a6fc-77bf0e106f4f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/63a4e511-9b32-41d5-a6fc-77bf0e106f4f?resizing_type=fit)

* [sequencer](https://dev.epicgames.com/community/search?query=sequencer)
* [tracks](https://dev.epicgames.com/community/search?query=tracks)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisites](/documentation/en-us/unreal-engine/sequencer-track-list-in-unreal-engine?application_version=5.7#prerequisites)
* [Track List](/documentation/en-us/unreal-engine/sequencer-track-list-in-unreal-engine?application_version=5.7#track-list)
* [Adding Tracks](/documentation/en-us/unreal-engine/sequencer-track-list-in-unreal-engine?application_version=5.7#adding-tracks)
* [Adding Actors](/documentation/en-us/unreal-engine/sequencer-track-list-in-unreal-engine?application_version=5.7#adding-actors)
* [Adding Components](/documentation/en-us/unreal-engine/sequencer-track-list-in-unreal-engine?application_version=5.7#adding-components)
* [Organization](/documentation/en-us/unreal-engine/sequencer-track-list-in-unreal-engine?application_version=5.7#organization)
* [Renaming](/documentation/en-us/unreal-engine/sequencer-track-list-in-unreal-engine?application_version=5.7#renaming)
* [Lock](/documentation/en-us/unreal-engine/sequencer-track-list-in-unreal-engine?application_version=5.7#lock)
* [Pin](/documentation/en-us/unreal-engine/sequencer-track-list-in-unreal-engine?application_version=5.7#pin)
* [Mute](/documentation/en-us/unreal-engine/sequencer-track-list-in-unreal-engine?application_version=5.7#mute)
* [Solo](/documentation/en-us/unreal-engine/sequencer-track-list-in-unreal-engine?application_version=5.7#solo)
* [Reordering](/documentation/en-us/unreal-engine/sequencer-track-list-in-unreal-engine?application_version=5.7#reordering)
* [Search and Filter](/documentation/en-us/unreal-engine/sequencer-track-list-in-unreal-engine?application_version=5.7#search-and-filter)
