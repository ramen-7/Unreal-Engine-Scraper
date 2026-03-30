<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine?application_version=5.7 -->

# Sequencer Editor

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
8. Sequencer Editor

# Sequencer Editor

An overview of the Sequence Editor's user interface, tools, and options.

![Sequencer Editor](https://dev.epicgames.com/community/api/documentation/image/1c8e7546-ee29-40a4-a598-8388f5d6ebbc?resizing_type=fill&width=1920&height=335)

 On this page

The **Sequencer Editor** is the main interface you can use to edit [Level Sequences assets](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview), in order to create cinematic content in **Unreal Engine**.

The following document provides an overview of the Sequencer Editor's user Interface, tools, and properties.

[![sequencer editor overview with highlights](https://dev.epicgames.com/community/api/documentation/image/4fae29f8-a06e-46a8-8825-38fd79949801?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4fae29f8-a06e-46a8-8825-38fd79949801?resizing_type=fit)

1. [Toolbar](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine?application_version=5.5#toolbar)
2. [Outliner](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine?application_version=5.5#outliner)
3. [Timeline](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine?application_version=5.5#timeline)
4. [Playback Controls](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine?application_version=5.5#playback-controls)

## Toolbar

The Sequencer Editor Toolbar contains a suite of tools, options and settings you can use to interface with Level Sequence assets.

[![sequencer toolbar overview with highlights](https://dev.epicgames.com/community/api/documentation/image/9183e3c2-43eb-4fa3-a663-f6cbbc7e36c5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9183e3c2-43eb-4fa3-a663-f6cbbc7e36c5?resizing_type=fit)

| Name | Icon | Description |
| --- | --- | --- |
| [World](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine) | [sequencer world](https://dev.epicgames.com/community/api/documentation/image/dc5caa23-d662-4f46-9e8a-f33f95c24a36?resizing_type=fit) | Lists information on the current world context, Level Sequence Actor, and playback realm. It contains options for specifying whether you want your sequence to autobind to Play In Editor (PIE), Simulation, or other runtime sessions. |
| **Save** | [sequencer save](https://dev.epicgames.com/community/api/documentation/image/1eefd7cc-eb88-4f34-85df-853b00128fc8?resizing_type=fit) | Saves the current sequence and any subscenes or shots. |
| **Find in Content Browser** | [sequencer find](https://dev.epicgames.com/community/api/documentation/image/bf37f8bc-8f92-405c-a0aa-6a5b6c1702f9?resizing_type=fit) | Locates the current sequence's Level Sequence asset in the Content Browser. |
| [Create Camera](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine) | [sequencer camera](https://dev.epicgames.com/community/api/documentation/image/52b93f05-a804-4d5b-9b92-1b5940186aa6?resizing_type=fit) | Creates a new **[Cine Camera Actor](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-cameras-in-unreal-engine)**. A new **[Camera Cut Track](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-camera-cut-track-in-unreal-engine)** will also be created and will reference this camera if one had not already been created. |
| [Render](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine) | [sequencer render](https://dev.epicgames.com/community/api/documentation/image/7359ff39-ee0a-4abc-8d7d-f30933b5a58b?resizing_type=fit) | Opens the  Settings dialog, or the **[Movie Render Queue](animating-characters-and-objects/Sequencer/movie-render-pipeline#movierenderqueue)** if its plugin is enabled. |
| [Director Blueprint](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine) | [sequencer director](https://dev.epicgames.com/community/api/documentation/image/fd2fee70-e35a-4ec3-b9b8-3534e9670e3f?resizing_type=fit) | Opens the Director Blueprint for this sequence, from which **[Event Track](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematic-event-track-in-unreal-engine)** logic can be accessed. |
| [Actions](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine) | [sequencer actions](https://dev.epicgames.com/community/api/documentation/image/d8b0d06e-04a0-41b7-9d4f-feb727e323f3?resizing_type=fit) | Lists various sequence editor actions such as saving, import/export, baking, and selection editing. |
| [View Options](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine) | [sequencer view options](https://dev.epicgames.com/community/api/documentation/image/49a637c6-35d5-4a8a-94ab-1dc61d84e4c9?resizing_type=fit) | Lists various sequence view options. |
| [Playback Options](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine) | [sequencer playback options](https://dev.epicgames.com/community/api/documentation/image/c1072739-d497-4cb7-bf75-5e08aa27d982?resizing_type=fit) | Lists various playback options such as playrate, start/end times, and playhead behavior. |
| [Keyframe Options](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine) | [sequencer keyframe options](https://dev.epicgames.com/community/api/documentation/image/7f634ee6-8154-46f0-90b7-a30b2dd91bcb?resizing_type=fit) | Lists settings for Auto Key transform keyframing behavior, and what default tangents are created. |
| [Auto Key](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine) | [sequencer autokey](https://dev.epicgames.com/community/api/documentation/image/ebeaa4ec-51e6-483a-ac39-a718afc452e9?resizing_type=fit) | Enables Autokey mode, where keyframes are automatically created whenever a property or transform changes. |
| [Edit Options](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine) | [sequencer edit options](https://dev.epicgames.com/community/api/documentation/image/48d756c5-0538-40e1-974f-c36f0a4a9415?resizing_type=fit) | Lists settings for how edits from the Details panel are interpreted by Sequencer when using Auto Key. |
| [Snapping](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine) | [sequencer snapping](https://dev.epicgames.com/community/api/documentation/image/e8e50238-8312-46bd-a3c6-be3d7282f0d0?resizing_type=fit) | Enables snapping. The dropdown menu next to this lists options for setting snapping rules for keyframes, sections, and the timeline. |
| [Frames Per Second](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine) | [sequencer fps](https://dev.epicgames.com/community/api/documentation/image/0c206d89-4346-49c9-bc74-3d3ba82bea2e?resizing_type=fit) | Lists settings for various Frames Per Second (FPS) targets at runtime. Also contains options to enable the runtime to lock to the chosen frame rate. |
| [Curve Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine) | [sequencer curve editor](https://dev.epicgames.com/community/api/documentation/image/502793cc-5899-4338-bb55-dbb51548ce3c?resizing_type=fit) | Opens the **[Curve Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-curve-editor-in-unreal-engine)** which is used for fine tuning of animation keyframes and tangents. |
| [Breadcrumbs](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine) | [sequencer breadcrumbs](https://dev.epicgames.com/community/api/documentation/image/b8b6bfcb-cd15-4563-b81c-e9561d9a2a45?resizing_type=fit) | Displays the current sequence name, and is used to navigate master sequences and shots. |
| **Lock** | [sequencer lock](https://dev.epicgames.com/community/api/documentation/image/e42accf1-0fe4-488f-983b-5e0e90db20ad?resizing_type=fit) | Locks the entire sequence to prevent editing. |

Refer to [Sequence Editor toolbar](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine) for more information about Sequencer's toolbar.

## Outliner

The Sequencer Editor's Outliner contains a list of the Level Sequence asset's tracks, as well as tools to add, filter, and search for tracks. Tracks can represent Actors attached to your Level Sequence such as Cameras, Characters, Audio, and Effects.

[![sequencer outliner overview with highlights](https://dev.epicgames.com/community/api/documentation/image/30e697d1-4fa4-4701-b6db-84a323350bf7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/30e697d1-4fa4-4701-b6db-84a323350bf7?resizing_type=fit)

Refer to [Sequencer Tracks](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-track-list-in-unreal-engine) for more information about different types of tracks.

## Timeline

The Sequencer's Timeline is a non-linear editing environment that represents the entire playable region of your Level Sequence asset. The Timeline includes horizontal regions for each Track, and can include assets, keyframes and timeline controls.

The playback range of your Level Sequence asset is contained within **Start** (Green) and **End** (Red) markers. The current location of your playback is indicated by the [Playhead](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine?application_version=5.5#playhead).

[![sequencer overview with highlights](https://dev.epicgames.com/community/api/documentation/image/8db0e44f-a6d1-43cc-b2d1-3ffc50f04d94?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8db0e44f-a6d1-43cc-b2d1-3ffc50f04d94?resizing_type=fit)

### Navigation

To navigate your Level Sequence asset in the Sequencer Editor, you can [pan](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine?application_version=5.5#panning) and [zoom](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine?application_version=5.5#zooming) within the timeline.

#### Panning

You can pan your Timeline view vertically, to see additional track regions, by dragging the right-side scrollbar up and down.

[![sequencer vertical pan scroll bar](https://dev.epicgames.com/community/api/documentation/image/1bdc4fa0-d883-4718-9c42-66ea1f278855?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1bdc4fa0-d883-4718-9c42-66ea1f278855?resizing_type=fit)

You can pan and zoom the Timeline view horizontally, to see different content in the playback, using the **Range Slider** at the bottom of the timeline.

Dragging the middle area of the slider pans, while dragging the left/right margins will zoom your view.

The Range Slider is enabled by default and can be disabled from the **View Options** dropdown in the Sequencer toolbar.

Image

Holding the right mouse button and dragging along the timeline enables panning horizontally and vertically.

Scrolling will pan the timeline up and down, while holding **Shift** and scrolling the mouse wheel will pan the timeline left and right.

#### Zooming

You can zoom in the timeline by holding **CTRL** and scrolling the mouse wheel.

[![horizontal scrolling](https://dev.epicgames.com/community/api/documentation/image/e6ece45e-f77e-4097-9e4f-7e2a96cdaaa7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e6ece45e-f77e-4097-9e4f-7e2a96cdaaa7?resizing_type=fit)

By holding **ALT** + **Shift** and clicking and dragging left and right with the Right Mouse Button, you can free-form zoom.

[![horizontal scrolling](https://dev.epicgames.com/community/api/documentation/image/29332988-b823-4e4d-a8ef-b22892442013?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/29332988-b823-4e4d-a8ef-b22892442013?resizing_type=fit)

By holding **CTRL** and dragging along the time bar to the **right**, you can define a zoom region. Holding **CTRL** and dragging the time bar to the **left** resets the zoom back to full.

[![horizontal scrolling](https://dev.epicgames.com/community/api/documentation/image/3e325ea9-2739-4dee-9b02-42fe87b74e8d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3e325ea9-2739-4dee-9b02-42fe87b74e8d?resizing_type=fit)

The zoom pivot is relative to the playhead by default and can be changed by locating the **Zoom Position** preference in the **Level Sequence Editor** section of the **Editor Preferences**.

If your zoom and timeline framing have overextended, you can reset your zoom and timeline framing by pressing the **Home** key, which also resets the bounds of the range slider.

[![home button horizontal zoom scrolling](https://dev.epicgames.com/community/api/documentation/image/c06b816b-8cbc-4c81-813f-90227526c025?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c06b816b-8cbc-4c81-813f-90227526c025?resizing_type=fit)

### Playhead

The playhead displays the current time in the sequence and is one of the main controls for timeline interactions. During playback it will move across the timeline at the specified playrate and can be stopped in place by pausing.

[![sequencer playhead](https://dev.epicgames.com/community/api/documentation/image/4ea8f932-a876-42e4-9342-886dc180b02d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4ea8f932-a876-42e4-9342-886dc180b02d?resizing_type=fit)

You can **Left Mouse Button** (**LMB**)drag the playhead to change the current time in the sequence, and preview changes in the viewport. This is commonly referred to as "scrubbing". See [Scrubbing Responsiveness](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine#scrubbing-responsiveness) and [Synchronous Scrubbing](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine#synchronous-scrubbing) below for more information.

**Middle Mouse Button** (**MMB**) dragging causes the playhead to change to the selected position without causing the sequence to evaluate. This technique is used to change time, without changing property values and can be used to create same-value keyframes quickly. When manipulating the playhead in this way, it will change its color to **yellow**, to indicate the sequence is not evaluating.

The current time of the playhead is displayed and can be manipulated from the sequence outliner. You can press **CTRL + T** to focus selection to this field and type in a new time value.

[![sequencer playhead values](https://dev.epicgames.com/community/api/documentation/image/5a6f89ae-ee15-48bc-b519-36d426911b28?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5a6f89ae-ee15-48bc-b519-36d426911b28?resizing_type=fit)

You can also right-click the playhead or anywhere on the time bar to reveal additional options.

[![sequencer timeline playhead context menu](https://dev.epicgames.com/community/api/documentation/image/6faca2c9-d85e-4f0d-9cb3-8f985958716e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6faca2c9-d85e-4f0d-9cb3-8f985958716e?resizing_type=fit)

| Name | Description | Hotkey |
| --- | --- | --- |
| **Set Start Time** | Set the start time of the sequence to the current position of your cursor. | **[** |
| **Set End Time** | Set the end time of the sequence to your cursor. | **]** |
| **Set Selection Start** | Set the start point of a custom timeline selection range to your cursor. | **i** |
| **Set Selection End** | Set the endpoint of a custom timeline selection range to your cursor. | **o** |
| **Clear Selection Range** | Remove the selected range. |  |
| **Add Mark** | Create a custom timeline mark at the current playhead time. | **m** |
| **Delete All Marks** | Remove all custom marks from the sequence. |  |
| **Locked** | When enabled, all marks will be locked, which prevents marks from being edited allowing you to scrub the timeline slider freely. |  |

The Playhead time indicator can display with an **asterisk** (\*) if the current time is on a sub-frame or in-between frame. This can happen if [snapping](https://dev.epicgames.com/documentation/en-us/unreal-engine/sequencer-cinematic-toolbar-in-unreal-engine) is disabled.

[![sequencer sub frames asterisk](https://dev.epicgames.com/community/api/documentation/image/330ed548-b33d-439a-a39f-978652b414c7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/330ed548-b33d-439a-a39f-978652b414c7?resizing_type=fit)

#### Scrubbing Responsiveness

Seeking a specific location and scrubbing along a track in Sequencer are both asynchronous non-blocking operations, whose responsiveness depends on the video codec used.

* **Apple Pro Res** provides the best scrubbing experience.
* **H.264/5** is effective, but shows a few frames of lag even when you enable hardware decoding.

#### Media Player Info

For convenience, Media Sections display media player and media file information directly in the Sequencer UI. This provides visual confirmation of the media player in use for playback.

Certain GOP codecs (H.264 in the screenshot below) might cause slow scrubbing performance; a yellow warning message is shown in such cases.

[![Codec warning message in Sequencer UI](https://dev.epicgames.com/community/api/documentation/image/bfaf05ac-00d9-48a6-a317-723f31921f62?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bfaf05ac-00d9-48a6-a317-723f31921f62?resizing_type=fit)

#### Synchronous Scrubbing

For use-cases where you need perfect frame alignment while scrubbing, for example when animating in Sequencer against reference video footage, you can enable the **Synchronous Scrubbing** Sequencer media track option. It aligns the video and animation frames exactly where the playhead is located, which ensures perfect alignment at some editor scrubbing responsiveness cost. This option is disabled by default to favor speed and responsiveness.

This setting only affects scrubbing, it has no impact on playback which is always frame accurate.

[![Synchronous Scrubbing](https://dev.epicgames.com/community/api/documentation/image/181c1ed1-d593-47e5-a1b4-0e2aa8c9ac78?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/181c1ed1-d593-47e5-a1b4-0e2aa8c9ac78?resizing_type=fit)

### Selection Ranges

Selection ranges are custom regions you can define in a sequence to assist with timeline selection and playback.

To create a selection range, right- click a point in the timeline bar and set a **Start** and **End Selection Range**.

[![sequencer selection range start end](https://dev.epicgames.com/community/api/documentation/image/92a430cf-7659-48d2-9862-857cb3ed37b7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/92a430cf-7659-48d2-9862-857cb3ed37b7?resizing_type=fit)

The selection range handles can be adjusted similarly to the start and end times of the sequence.

[![sequencer selection range manipulation](https://dev.epicgames.com/community/api/documentation/image/3892428b-6c0f-4bb0-81fe-a16496fc73ee?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3892428b-6c0f-4bb0-81fe-a16496fc73ee?resizing_type=fit)

You can also set the playback of the sequence to loop within the section range.

Selection ranges can also be used to select keyframes and sections within them by clicking the **Actions** toolbar button and selecting **Select Keys in Selection Range** or **Select Sections in Selection Range**.

[![sequencer selection range settings](https://dev.epicgames.com/community/api/documentation/image/93080a2a-9489-419c-bd41-bf80372818ac?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/93080a2a-9489-419c-bd41-bf80372818ac?resizing_type=fit)

To remove a selection range, right-click the time bar and select **Clear Selection Range**.

### Custom Frame Marks

Custom frame marks are points you can add to call attention to areas or provide annotation for your sequence.

To create a mark, right-click a point in the timeline bar and select **Add Mark**.

[![sequencer add mark option](https://dev.epicgames.com/community/api/documentation/image/8370360f-07c1-411d-b3ee-b47c81eec64c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8370360f-07c1-411d-b3ee-b47c81eec64c?resizing_type=fit)

Frame Marks can be selected and multi-selected in the Sequencer Timeline in order to edit their location.

To edit a mark, right-click the mark flag in the Sequencer Timeline to access its context menu. Here you can customize its properties such as **Frame Number, Label,** and **Color**.

[![sequencer mark properties](https://dev.epicgames.com/community/api/documentation/image/0c8dc224-a6e6-4a3b-bd6d-723c0a7aa54b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0c8dc224-a6e6-4a3b-bd6d-723c0a7aa54b?resizing_type=fit)

Use these properties to observe and set Custom Frame Mark behavior when creating cinematics in the Sequencer Editor:

| Property | Description |
| --- | --- |
| **Marked Frame** | Sets or reference the **frame number** the mark is located in your Level Sequence. |
| **Label** | Sets a name for the Custom Frame Mark. The value set will be visible in the Sequencer Timeline at the top of the Mark flag. |
| **Comment** | Adds comments associated with the custom mark. |
| **Color** | Sets a custom color for the Mark flag in the Sequencer Timeline. |
| **Is Determinism Fence?** | When enabled, the Mark is treated as a **Determinism Fence**, which ensures that all Sequencer Components are evaluated at the Mark's location in the Sequencer Timeline.  Determinism Fences cannot be crossed with a single evaluation, and force the evaluation to be conducted in two separate parts, ensuring an accurate evaluation of all present Sequencer components.  It is recommended to add Marks, with the **Is Determinism Fence** property enabled, to important frames in your Level Sequence, in order to ensure accurate playback at runtime. |
| **Add Mark** | Creates a new custom mark at the timecode your cursor is at.  Only one custom mark can exist per level sequence frame. |
| **Delete Mark** | Deletes the currently selected mark. |
| **Delete All Marks** | Deletes all custom marks within the level sequence asset. |

## Playback Controls

The playback controls can be found in the bottom-left corner of Sequencer and function similarly to standard media playback applications.

Buttons for toggling playing, pausing, and other playback-related functions are found here.

[![sequencer add mark option](https://dev.epicgames.com/community/api/documentation/image/3926b3db-f6b6-4245-8784-32c6b74e409b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3926b3db-f6b6-4245-8784-32c6b74e409b?resizing_type=fit)

| Icon | Description |
| --- | --- |
| [sequencer record button take recorder](https://dev.epicgames.com/community/api/documentation/image/cc94a050-e237-4998-9d39-1694ec05e5e8?resizing_type=fit) | Records the motion of a selected actor in the Sequencer Outliner, using **Take Recorder**.  In order to use this playback control, you must install the Take Recorder plugin. For more information, see the [Take Recorder](https://dev.epicgames.com/documentation/en-us/unreal-engine/take-recorder-in-unreal-engine) documentation. |
|  | Sets the start time of the sequence to the current location of the playhead. |
|  | Jumps to the start of the sequence. |
|  | Jumps to the previous keyframe in the selected track. |
|  | Jumps to the previous frame. |
|  | Plays or pauses the sequence in reverse from the current position of the playhead. |
|  | Plays or pauses the sequence from the position of the playhead. |
|  | Jumps to the next frame. |
|  | Jumps to the next keyframe in the selected track. |
|  | Jumps to the end of the sequence. |
|  | Sets the end time of the sequence to the current location of the playhead. |
|  | Toggles between looping and no looping. Selection range looping is added if selection ranges are being used in the timeline. |

### Playback and Looping

Playback and looping performance are the most important functions of video playback. However, the Sequencer timeline makes a wide variety of Media Track section configurations possible, including native, cropped, extended, extended and cropped, with or without pre-roll and post-roll. These create edge-cases which cause problems for looping. The examples below are the currently-supported use cases for looping.

#### Baseline Looping

Baseline looping applies for use cases where:

* The Media Section length is unaltered, that is, it corresponds to the duration of the video clip.
* The Sequencer playback range fits within the Media Section pre-roll and post-roll bounds.

[![Sequencer baseline looping](https://dev.epicgames.com/community/api/documentation/image/bb70062e-aced-401d-ab02-70f832e369ea?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bb70062e-aced-401d-ab02-70f832e369ea?resizing_type=fit)

In this configuration, the video clip is at full length and located at T=0, which prevents using the pre-roll section. Since the red and green crop lines are located at clip edges, the Media Section implementation keeps the Player alive and can perform proper seamless looping when the playhead reaches the end of the Sequencer’s playback range.

To prevent user error and because it is difficult to precisely set the red crop line in Sequencer, we recommend you use special care in placing the red line or to use the Media Section post-roll feature to prevent the Player unallocating prematurely.

#### Internal Clipped Looping

Internal clipped looping applies for use cases where you have done either of the following:

* Cropped a video in Sequencer by moving the green and red crop lines within the Media Section.

  + For example, placing the green line at frame 100 and red line at frame 700 while the Media Section has 1000 Frames.
* Manually cropped the Media Section by adjusting its start and end points inside the video clip’s duration.

  + For example, starting at frame 100 and ending at frame 700 if the Media Section had 1000 frames to begin with.

[![Sequencer internal clipped looping](https://dev.epicgames.com/community/api/documentation/image/ec8c56bc-41fd-446f-be9a-b1773469e152?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ec8c56bc-41fd-446f-be9a-b1773469e152?resizing_type=fit)

This use case is fully supported because the media player is properly notified of those new start and end frames, and can cache the correct frames accordingly.

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [sequencer](https://dev.epicgames.com/community/search?query=sequencer)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Toolbar](/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine?application_version=5.7#toolbar)
* [Outliner](/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine?application_version=5.7#outliner)
* [Timeline](/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine?application_version=5.7#timeline)
* [Navigation](/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine?application_version=5.7#navigation)
* [Panning](/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine?application_version=5.7#panning)
* [Zooming](/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine?application_version=5.7#zooming)
* [Playhead](/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine?application_version=5.7#playhead)
* [Scrubbing Responsiveness](/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine?application_version=5.7#scrubbing-responsiveness)
* [Media Player Info](/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine?application_version=5.7#mediaplayerinfo)
* [Synchronous Scrubbing](/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine?application_version=5.7#synchronous-scrubbing)
* [Selection Ranges](/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine?application_version=5.7#selection-ranges)
* [Custom Frame Marks](/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine?application_version=5.7#custom-frame-marks)
* [Playback Controls](/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine?application_version=5.7#playback-controls)
* [Playback and Looping](/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine?application_version=5.7#playbackandlooping)
* [Baseline Looping](/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine?application_version=5.7#baselinelooping)
* [Internal Clipped Looping](/documentation/en-us/unreal-engine/sequencer-cinematic-editor-unreal-engine?application_version=5.7#internalclippedlooping)
