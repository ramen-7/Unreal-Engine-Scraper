<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview?application_version=5.7 -->

# Sequencer Overview

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
7. Sequencer Overview

# Sequencer Overview

Learn about Level Sequences and the primary features of the Sequencer Editor.

![Sequencer Overview](https://dev.epicgames.com/community/api/documentation/image/d0cb5c6c-ed2a-45e4-a623-cf8649525667?resizing_type=fill&width=1920&height=335)

 On this page

Sequencer gives users the ability to create in-game cinematics through its specialized multi-track editor. By creating Level Sequences, adding tracks, and creating keyframes you can manipulate objects, characters, and cameras.

This page provides an overview of Sequencer Actors, Level Sequence Assets, and the primary features of Sequencer.

## Sequencer Asset and Actor

Sequencer in Unreal Engine consists of 2 main parts: a **Level Sequence Asset** and a **Level Sequence Actor**.

The **Level Sequence Asset** is located in the Content Browser and contains Sequencer's data. This includes tracks, cameras, keyframes, and animations. This is assigned to a **Level Sequence Actor** in order to bind its data to a Level.

![level sequence asset](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/49c55c39-b51a-4afd-bef4-9d18ac8a6cdb/seqasset.png)

The **Level Sequence Actor** is located in the Level and is the container for the **Level Sequence Asset**. You can select it to view its details in the **Details** panel.

![level sequence actor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6b22525d-4df0-43c8-b131-f13bc74eaf10/seqactor.png)

| Name | Description |
| --- | --- |
| **Open Level Sequence** | Opens the Sequence Editor for the currently bound level sequence asset. |
| **Level Sequence** | The currently bound level sequence asset. |
| Playback |  |
| **Auto Play** | The sequence will automatically play when the actor is created. |
| **Loop** | Loop options for the sequence. Don't Loop will cause the sequence to play once and finish. Loop Indefinitely will cause the sequence to loop forever. Loop Exactly... will expose a numerical time entry where you can specify the amount of times the sequence will loop, then finish. |
| **Play Rate** | The speed of the sequence to play. Does not affect Time Dilation. |
| **Start Offset** | The amount of time in seconds the sequence should start relative to the start time. |
| **Random Start Time** | Starts playing the sequence at a random point between the start and end time. Enabling this will disable Start Offset. |
| **Restore State** | Restores all actors to their previous state before the sequence started. |
| **Pause at End** | The sequence will pause upon reaching the end, keeping all actors in their final positions in the sequence. |
| Cinematic |  |
| **Disable Movement Input** | Disables translation input from the player pawn for the duration of the sequence. |
| **Disable Look At Input** | Disables rotation input from the player pawn for the duration of the sequence. |
| **Hide Player** | Disables the player pawn's visibility for the duration of the sequence. |
| **Hide Hud** | Hides all Heads Up Display (HUD) elements for the duration of the sequence. |
| **Disable Camera Cuts** | Disables the Camera Cuts track, causing the sequence to not take control of the camera. |

### Sequencer Creation

There are several ways you can create and assign your Level Sequences.

One of the quickest ways is to click the **Cinematics** dropdown in the Level Editor's main toolbar and select **Add Level Sequence**. This will prompt you to create a new **Level Sequence Asset** in the Content Browser. Give it a name and click **Save**. Once created, your Level will now contain a **Level Sequence Actor** with a reference to the newly created **Level Sequence Asset**.

![create level sequence](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e1d6815f-65de-4be6-a34c-12aa1a6f0025/createseq1.png)

An alternate way of creating and assigning your sequence is to click **Add/Import > Animation > Level Sequence** in the **[Content Browser](/documentation/en-us/unreal-engine/content-browser-in-unreal-engine)**. This will also prompt you to create a new **Level Sequence** Asset.

![create level sequence](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7daae85b-71bd-4dac-96ce-3200ab4fb471/createseq2.png)

Once the sequence Asset has been created, navigate to the **[Place Actors](/documentation/en-us/unreal-engine/placing-actors-in-unreal-engine)** panel and drag in a **Level Sequence Actor** from the **Cinematic** category.

![add sequence actor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9ef55f7d-04a9-4377-9ceb-9212cb22a8a6/addseqactor.png)

Then bind your Level Sequence Asset to the Level Sequence Actor by dragging and dropping the Asset onto the Level Sequence property.

![bind level sequence](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/13eccbc8-8bc4-4310-8e25-8807301543a0/assignseq.png)

## Sequencer Editor

The Sequencer tab contains the Sequencer Editor, which provides a user interface for creating cinematic content.

![sequencer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/22ae54fc-a86f-43f5-ac3f-2ddb470a0c40/seqwindow.png)

There are various ways you can open this window.

One way is to click the **Cinematics** dropdown in the Level Editor's main toolbar and select your sequence from the list. Your sequence must be assigned to a Level Sequence Actor within your Level for it to appear here.

![open sequencer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/27e7df6e-1aad-466f-80d9-38d8e35ac7a2/openseq1.png)

Another way is by clicking the Level Sequence Actor's **Open Level Sequence** button in the **Details** panel.

![open sequencer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7267cf70-3ca5-443e-ace7-e66661698fba/openseq21.png)

Or by double-clicking the **Level Sequence** property icon in the **Details** panel.

![open sequencer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/210a5858-20ab-4311-bce6-359f321cf86b/openseq2.png)

You can also open it by double-clicking the Level Sequence Asset in the **Content Browser**.

![open sequencer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8a06b9f6-1bba-4de6-99f3-32b4e6c39b8a/openseq3.png)


When opening a sequence from the Content Browser, you must currently have a Level opened in which this sequence is being referenced. Otherwise the contents will be unbound.

Finally, you can open it by navigating to the main menu bar and clicking **Window > Cinematics > Sequencer**.

![open sequencer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1ab4eb42-618f-43de-92cc-d60dc63dd662/opensec4.png)

Visit the  page for more information on the Sequencer editor.

[![Curve Editor](images/static/document_list/empty_thumbnail.svg)

Curve Editor

Tweak your keyframes and curves by using the Curve Editor and tools within it.](/documentation/en-us/unreal-engine/animation-curve-editor-in-unreal-engine)
[![Tracks](images/static/document_list/empty_thumbnail.svg)

Tracks

Create tracks that affect your actors in Sequencer.](/documentation/en-us/unreal-engine/sequencer-track-list-in-unreal-engine)
[![Sequences, Shots, and Takes](images/static/document_list/empty_thumbnail.svg)

Sequences, Shots, and Takes

Edit cinematics in a non-linear editor using Sequences, Shots, and Takes.](/documentation/en-us/unreal-engine/sequences-shots-and-takes-in-unreal-engine)
[![Actor Sequence Component](images/static/document_list/empty_thumbnail.svg)

Actor Sequence Component

Describes how you can embed Sequences within Actor Blueprints using an Actor Sequence Component.](/documentation/en-us/unreal-engine/sequencer-blueprint-component-in-unreal-engine)
[![Take Recorder](images/static/document_list/empty_thumbnail.svg)

Take Recorder

Record Editor, Gameplay, and Live Link Actors with Take Recorder.](/documentation/en-us/unreal-engine/take-recorder-in-unreal-engine)
[![Keyframing](images/static/document_list/empty_thumbnail.svg)

Keyframing

Animate objects, actors, and properties in Sequencer by keyframing them and utilizing sections.](/documentation/en-us/unreal-engine/creating-animation-keyframes-in-unreal-engine)
[![Editor Preferences and Project Settings](images/static/document_list/empty_thumbnail.svg)

Editor Preferences and Project Settings

Tweak Sequencer's behavior using Editor and Project Settings.](/documentation/en-us/unreal-engine/cinematic-editor-and-project-settings-in-unreal-engine)
[![Render Movie](images/static/document_list/empty_thumbnail.svg)

Render Movie

Describes the options available to you when rendering out your cinematic sequences.](/documentation/en-us/unreal-engine/old-render-movie-in-unreal-engine)
[![Importing and Exporting FBX files](images/static/document_list/empty_thumbnail.svg)

Importing and Exporting FBX files

Describes how you can export FBX files from Sequencer and import FBX files to Sequencer.](/documentation/en-us/unreal-engine/import-and-export-cinematic-fbx-animations-in-unreal-engine)
[![Template Sequences](images/static/document_list/empty_thumbnail.svg)

Template Sequences

Reuse animation data created in sequencer with Template Sequences.](/documentation/en-us/unreal-engine/template-sequences-in-unreal-engine)
[![Sequencer Tags and Groups](images/static/document_list/empty_thumbnail.svg)

Sequencer Tags and Groups

Reference your Sequencer Actors using Tags for Blueprint scripting, and organize your tracks with Groups.](/documentation/en-us/unreal-engine/cinematic-tags-and-groups-in-unreal-engine)
[![Dynamic Binding](images/static/document_list/empty_thumbnail.svg)

Dynamic Binding

Dynamic Binding provides custom Blueprints logic that picks which object to possess in the level or which to spawn.](/documentation/en-us/unreal-engine/dynamic-binding-in-sequencer)
[![Sequencer Playlists](images/static/document_list/empty_thumbnail.svg)

Sequencer Playlists

Prepare and trigger Sequences during your virtual production session.](/documentation/en-us/unreal-engine/sequencer-playlists-in-unreal-engine)
[![Python Scripting in Sequencer](images/static/document_list/empty_thumbnail.svg)

Python Scripting in Sequencer

Learn common Python scripting commands and features used with Sequencer.](/documentation/en-us/unreal-engine/python-scripting-in-sequencer-in-unreal-engine)

## Sequencer Features

The following pages detail the primary animation and movie-making features of Sequencer.

[![Curve Editor](images/static/document_list/empty_thumbnail.svg)

Curve Editor

Tweak your keyframes and curves by using the Curve Editor and tools within it.](/documentation/en-us/unreal-engine/animation-curve-editor-in-unreal-engine)
[![Tracks](images/static/document_list/empty_thumbnail.svg)

Tracks

Create tracks that affect your actors in Sequencer.](/documentation/en-us/unreal-engine/sequencer-track-list-in-unreal-engine)
[![Sequences, Shots, and Takes](images/static/document_list/empty_thumbnail.svg)

Sequences, Shots, and Takes

Edit cinematics in a non-linear editor using Sequences, Shots, and Takes.](/documentation/en-us/unreal-engine/sequences-shots-and-takes-in-unreal-engine)
[![Actor Sequence Component](images/static/document_list/empty_thumbnail.svg)

Actor Sequence Component

Describes how you can embed Sequences within Actor Blueprints using an Actor Sequence Component.](/documentation/en-us/unreal-engine/sequencer-blueprint-component-in-unreal-engine)
[![Take Recorder](images/static/document_list/empty_thumbnail.svg)

Take Recorder

Record Editor, Gameplay, and Live Link Actors with Take Recorder.](/documentation/en-us/unreal-engine/take-recorder-in-unreal-engine)
[![Keyframing](images/static/document_list/empty_thumbnail.svg)

Keyframing

Animate objects, actors, and properties in Sequencer by keyframing them and utilizing sections.](/documentation/en-us/unreal-engine/creating-animation-keyframes-in-unreal-engine)
[![Editor Preferences and Project Settings](images/static/document_list/empty_thumbnail.svg)

Editor Preferences and Project Settings

Tweak Sequencer's behavior using Editor and Project Settings.](/documentation/en-us/unreal-engine/cinematic-editor-and-project-settings-in-unreal-engine)
[![Render Movie](images/static/document_list/empty_thumbnail.svg)

Render Movie

Describes the options available to you when rendering out your cinematic sequences.](/documentation/en-us/unreal-engine/old-render-movie-in-unreal-engine)
[![Importing and Exporting FBX files](images/static/document_list/empty_thumbnail.svg)

Importing and Exporting FBX files

Describes how you can export FBX files from Sequencer and import FBX files to Sequencer.](/documentation/en-us/unreal-engine/import-and-export-cinematic-fbx-animations-in-unreal-engine)
[![Template Sequences](images/static/document_list/empty_thumbnail.svg)

Template Sequences

Reuse animation data created in sequencer with Template Sequences.](/documentation/en-us/unreal-engine/template-sequences-in-unreal-engine)
[![Sequencer Tags and Groups](images/static/document_list/empty_thumbnail.svg)

Sequencer Tags and Groups

Reference your Sequencer Actors using Tags for Blueprint scripting, and organize your tracks with Groups.](/documentation/en-us/unreal-engine/cinematic-tags-and-groups-in-unreal-engine)
[![Dynamic Binding](images/static/document_list/empty_thumbnail.svg)

Dynamic Binding

Dynamic Binding provides custom Blueprints logic that picks which object to possess in the level or which to spawn.](/documentation/en-us/unreal-engine/dynamic-binding-in-sequencer)
[![Sequencer Playlists](images/static/document_list/empty_thumbnail.svg)

Sequencer Playlists

Prepare and trigger Sequences during your virtual production session.](/documentation/en-us/unreal-engine/sequencer-playlists-in-unreal-engine)
[![Python Scripting in Sequencer](images/static/document_list/empty_thumbnail.svg)

Python Scripting in Sequencer

Learn common Python scripting commands and features used with Sequencer.](/documentation/en-us/unreal-engine/python-scripting-in-sequencer-in-unreal-engine)

* [sequencer](https://dev.epicgames.com/community/search?query=sequencer)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Sequencer Asset and Actor](/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview?application_version=5.7#sequencerassetandactor)
* [Sequencer Creation](/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview?application_version=5.7#sequencercreation)
* [Sequencer Editor](/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview?application_version=5.7#sequencereditor)
* [Sequencer Features](/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview?application_version=5.7#sequencerfeatures)
