<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/media-viewer-in-unreal-engine?application_version=5.7 -->

# Media Viewer

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
5. [Working with Media](/documentation/en-us/unreal-engine/working-with-media-in-unreal-engine "Working with Media")
6. [Integrating Media](/documentation/en-us/unreal-engine/integrating-media-in-unreal-engine "Integrating Media")
7. Media Viewer

# Media Viewer

An overview of how to use the Media Viewer feature.

![Media Viewer](https://dev.epicgames.com/community/api/documentation/image/70d2fd47-9fb3-472b-9d42-b5c46787dd05?resizing_type=fill&width=1920&height=335)

 On this page

![Media Viewer in action.](https://dev.epicgames.com/community/api/documentation/image/064cb6e3-8755-40fd-aa5b-3cf7a1c03964?resizing_type=fit)

## Introduction

When creating animation in Unreal Engine (UE), you might need to align your animations against existing reference footage. For this reason, when using the **Media Viewer**, you can dock media (images, media textures, video files, live viewport textures) next to the Viewport where you do your animation work. Two AB banks in either horizontal or vertical configurations help compare two sets of images, and you can use zoom and pan controls to further align content.

The Media Viewer plugin provides the following workflows and usability improvements:

* Reference and view **media textures** from **Sequencer** or from the **Content Browser**.
* Reference **live Viewport textures**.
* Reference and view **img/file media sources** from the Content Browser or from Windows Explorer.
* Control media using standard **playback** controls (Play, Stop, Pause, Scan).
* **Pan** and **zoom** controls, including enhanced zoom controls using ALT + RMB.
* **Bookmark** and quickly recall A/B asset bank configurations using hot keys.
* The **lock** button mirrors the playback controls and timeline while in dual Player mode.

## Getting Started

To use the new Media Viewer, you need to enable the following plugins:

**Media Viewer (main BETA Plugin)**

[![Media Viewer plugin](https://dev.epicgames.com/community/api/documentation/image/b61b92ee-0fcb-457c-b555-1d7862225fca?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b61b92ee-0fcb-457c-b555-1d7862225fca?resizing_type=fit)

Optional but recommended:

* **Electra Player**: To use the Protron Player for more efficient playback and scrubbing.
* **D3D12 Hardware accelerated video decoding plugin for Electra**: For the best playback and scrubbing performance. Disabled by default, requires cvars, see below.
* **Apple Pro Res Decoder for Electra**: The preferred format and container for video for MacOS.

D3D12 hardware accelerated video decoding provides the most playback and scrubbing performance for H.264/5 video files. To enable it, you need to set the following cvars:

* `ElectraDecoders.bDoNotUseD3D12Video` set to `FALSE`
* `ElectraDecoders.bDisableD3D12Video` set to `FALSE`

Hardware video decode is fragile and disabled by default because of GPU compatibility concerns. It may crash your editor so use caution. Even if you get it working on a particular PC, do not assume it will work on different hardware .

### Media Viewer Window

You can find the **Media Viewer** in the main **Window** menu.

[![Media Viewer in the Window menu](https://dev.epicgames.com/community/api/documentation/image/1c9706e5-7653-4932-96f4-b9471421c9dc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1c9706e5-7653-4932-96f4-b9471421c9dc?resizing_type=fit)

#### Media Viewer User Interface

You can dock the Media Viewer window anywhere in the main UE Editor. We designed the controls and widgets to have a minimal footprint.

When you are looking at the default Media Viewer layout, you can see the following:

* [Library Tab](https://dev.epicgames.com/documentation/en-us/unreal-engine/media-viewer-in-unreal-engine#library) on the left.
* [Toolbar](https://dev.epicgames.com/documentation/en-us/unreal-engine/media-viewer-in-unreal-engine#toolbar-controls) controls and widgets on top.
* [The drag and drop zone](https://dev.epicgames.com/documentation/en-us/unreal-engine/media-viewer-in-unreal-engine#adding-media-assets) for Content Browser items in the middle.

#### Multiple Tabs

The main Media Viewer supports the creation of multiple tabs you can dock anywhere in the Editor UI.

[![](https://dev.epicgames.com/community/api/documentation/image/44a4417e-f76e-4f54-aadb-dab4a1c0914d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/44a4417e-f76e-4f54-aadb-dab4a1c0914d?resizing_type=fit)

#### Prompt to Open Previous Session

If you worked in the Media Viewer before, you can use the following prompt to restore the previous session, or start fresh.

[![](https://dev.epicgames.com/community/api/documentation/image/e5ca0556-026a-4ceb-9b02-70117f255a0e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e5ca0556-026a-4ceb-9b02-70117f255a0e?resizing_type=fit)

### Library

The Media Viewer has a Library tab that contains the following categories:

[![](https://dev.epicgames.com/community/api/documentation/image/eac4aa35-95c5-4ca7-8adc-5a9745652c1c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/eac4aa35-95c5-4ca7-8adc-5a9745652c1c?resizing_type=fit)

* **Pinned**: A user-defined section where you can store image or video references.
* **Snapshots**: A section where snapshots are referenced. Snapshots are saved to the Content Browser.
* **History**: A list of all previously opened or dragged and dropped items.
* **Editor Viewports**: Displays a list of all available Editor Viewport Textures.
* **Media Tracks**: Displays a list of currently available or opened media tracks in Sequencer.
* **Media Textures**: Displays a list of allocated and active Media Textures. This includes Media Texture assets used in Sequencer Media Tracks.

From the Library, you can add images, media textures, or viewport textures by dragging and dropping them into the A/B drop zones or by using the **add A/B bank** buttons to add them to either the A or B banks.

You can also drag and drop items from the **History** section into the **Pinned** section.

### Adding Media Assets

You can interact with the Media Viewer primarily using the A/B media banks drop zones, as follows:

* Drag and drop a media asset from the Content Browser into the Media Viewer Window and drop zones will appear.
* The drop zones guide you towards single or side-by-side view configurations:

### Toolbar Controls

You can manipulate the assets in the Media Viewer using the toolbar controls at the top of the window.

#### Single and Side-By-Side Views

[![](https://dev.epicgames.com/community/api/documentation/image/b7179aba-acaf-488e-8ab5-dfeba4a1be7f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b7179aba-acaf-488e-8ab5-dfeba4a1be7f?resizing_type=fit)

You can use the Media Viewer in either single view or side-by-side view configurations.

* In **single view** mode, you can display and control only one media asset at a time.
* In **side-by-side view** mode, you can view two media assets simultaneously, and compare them using the middle slider. You can pick between two side-by-side configurations:

  + **Vertical**: compares content with a vertical slider in-between.
  + **Horizontal**: compares content with a horizontal slider in-between.

In side-by-side view configuration, the first media asset is displayed across the whole Media Viewer surface area. The second media asset is rendered and overlaid on top with adjustable opacity controls.

#### Pan, Zoom, and Rotation Controls

The Media Viewer **pan**, **zoom**, and **rotation** controls are always active.

* Use left-click and hold for **pan**.
* Use ALT + RMB or wheel rotation for **zoom**.
* The rotation angle setting is exposed in the A/B banks details panels. You can also use the numpad “4” and “6” keys to **rotate**.

[![Media Viewer zoom value in the toolbar](https://dev.epicgames.com/community/api/documentation/image/c18d26e3-8028-491f-af9a-fc1e8379c2b6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c18d26e3-8028-491f-af9a-fc1e8379c2b6?resizing_type=fit)

In addition, you can view and set the current zoom value in the Toolbar.

[![A/B media bank swap, lock, and reset controls](https://dev.epicgames.com/community/api/documentation/image/16997530-5735-4bb2-adaa-8a7ed8bd2ce8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/16997530-5735-4bb2-adaa-8a7ed8bd2ce8?resizing_type=fit)

* The **A/B media bank swap** control gives you a way to swap A and B media banks, including their current pan and zoom controls.
* By default, the **lock** control applies to the pan and zoom controls for both A and B media banks. You can  disable the lock option to have individual controls for each bank.
* The **reset** control resets all pan and zoom controls for both A and B banks.

#### Opacity and Compare Controls

When working in the side-by-side view configuration, you can use the **opacity control** to adjust how opaque or translucent media bank B appears when rendering on top of media bank A.

[![Media Viewer opacity and compare controls](https://dev.epicgames.com/community/api/documentation/image/3ff188b1-c9ff-4556-b9a9-e9ec3fdb2c17?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3ff188b1-c9ff-4556-b9a9-e9ec3fdb2c17?resizing_type=fit)

### Additional Controls and Settings

You can find some additional and advanced controls under the **Details Panel** menu as illustrated below:

[![](https://dev.epicgames.com/community/api/documentation/image/46d31b08-b59e-4254-8ffc-b13d0a069cd3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/46d31b08-b59e-4254-8ffc-b13d0a069cd3?resizing_type=fit)

You can adjust the settings for the A and B bank media assets separately. You can inspect and set:

* **Material**

  + **Render Target**:  You can use this dropdown menu to select the media asset.
  + **Real Time**: Enable this checkbox for real-time updates.
* **Media**

  + **Offset (X, Y, Z)**: This control sets the default position of the media. You can use the Pan controls to change it while you work.
  + **Rotation (X, Y, Z)**
  + **Scale (X, Y, Z)**: This control sets the default zoom level of the media. You can use the Zoom controls to change it while you work.
  + **Tint**: This control applies a color to the overlay.
* **Panel**

  + **Background Color**: Use the color picker to set the value.
  + **Background Texture**: Select a texture asset to use as the background. Optional.

### Context Menu

Right-clicking anywhere in the main Media Viewer UI opens a context menu with some additional options:

[![Media Viewer context menu](https://dev.epicgames.com/community/api/documentation/image/4a68965d-42e4-42bb-9a2e-ac610337d901?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4a68965d-42e4-42bb-9a2e-ac610337d901?resizing_type=fit)

* **Reset Transform**: Resets the current transforms applied to the image.
* **Copy Transform**: Copies the transform data in memory from the currently-selected image.
* **Pin Image**: Adds the current image to the Pinned category in the Library tab.
* **Show Overlays**: Toggles the display of the various overlay data on top of images.
* **Sync Transforms**: All transforms applied to either image are applied to both the images.
* **Resets All Transforms**: Resets all transforms for both image banks.
* **Swap A and B**: Swaps the A and B images.
* **Open Bookmark**: Loads the selected bookmark.
* **Save Bookmark**: Saves the current state as a bookmark.

### Video Playback and Controls

Media Viewer has embedded video controls and playback capabilities you can use to view video assets.

When dragging and dropping a File Media Source into either the A or B media banks, the following playback controls appear at the bottom. The controls disappear after a few seconds, mouse over them to bring them back:

[![](https://dev.epicgames.com/community/api/documentation/image/16136bf8-f116-4431-85e3-88a43deaf9c5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/16136bf8-f116-4431-85e3-88a43deaf9c5?resizing_type=fit)

**Playhead controls** resemble Sequencer controls and provide similar functionality:

* Play forward or reverse.

  + Reverse is only available for some codecs only such as Apple Pro Res.
* Step one frame forward or backward.
* Jump to the beginning or end.
* Use the scrubbing bar.

**Additional information** is displayed in the UI:

* Resolution and Player information in the top left section.
* Current Frame/Total Frames to the left of the controls.
* Current Time/Length to the right of the controls.

Playback and Scrubbing performance are impacted by many factors including:

* The type of source media.

  + For example, Apple Pro Res files or image sequences will scrub better than their H.264/5 counterparts.
* The choice of Player within the FileMediaSource UAsset.

  + For example, Protron Player plays and scrubs faster because it is optimized for local playback. You might get different results with Electra or WMF players.
* Specific cvars for hardware decode (applies only to H.264/5 codecs).

  + `ElectraDecoders.bDoNotUseD3D12Video` and `ElectraDecoders.bDisableD3D12Video` set to `FALSE`.

### A/B Synced Playback

Media Viewer gives you the option to lock both the A and B bank playback controls when the lock icon is enabled. This mirrors the playback controls such as play, pause, and rewind for both A and B content banks. The scrubbing bar is also mirrored so you can accurately scrub both clips in time using either scrubber.

### External Video Playback

To avoid cluttering existing projects with reference media, you can also use Media Viewer to play external video files not located in or imported to the Content Browser. In this workflow configuration, the preferred Player is used to decode the requested file. You can configure this under **Project Settings > Electra Protron Factory** where you can pick Protron as your preferred Player if none is defined.

[![](https://dev.epicgames.com/community/api/documentation/image/11c60874-a196-48d6-b2a6-bb9b0ac22c34?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/11c60874-a196-48d6-b2a6-bb9b0ac22c34?resizing_type=fit)

Here is an example of dragging and dropping an Apple Pro Res .mov file on the Media Viewer.

[![Adding a .mov file to the Media Viewer](https://dev.epicgames.com/community/api/documentation/image/b150e500-4d79-4b2f-84a8-63373a748fab?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b150e500-4d79-4b2f-84a8-63373a748fab?resizing_type=fit)

### Sequencer-driven Playback

Sequencer-driven video playback is a standard Media Viewer workflow that offers frame accuracy and alignment with animations. Follow the instructions below to set up the workflow.

#### Add a Media Track to Sequencer

* Begin by adding a **Media Track** in Sequencer.
* Assign your **Image** or **File Media Source** reference asset.

#### Set a Media Texture

* Next, while still on the Media Track, select a **Media Texture**. This texture is used automatically by Media Viewer.

#### Visualize Media Texture in Media Viewer

* After you select the Media Texture on the Media Track in Sequencer, it appears in the Media Viewer.

  + Alternatively, you can drag and drop the asset from the Content Browser.

[![](https://dev.epicgames.com/community/api/documentation/image/abc21eaa-c469-4116-acda-549661938ab2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/abc21eaa-c469-4116-acda-549661938ab2?resizing_type=fit)

#### Use Sequencer for Playback Controls

* After you select your assets, you can use the Sequencer playback controls to adjust your animation and the reference media together for proper alignment.

### Set Up Videos For Fast Playback or Scrubbing

To get the best performance for video playback and scrubbing, do the following:

* Enable the Electra Player Plugin.
* Use a scrub-friendly video container like Apple Pro Res.
* Open the video file File Media Source and set **Electra Protron** as the Player.

  1. Alternatively, you can set your **Electra Factory project settings** to pick Protron Player.

[![](https://dev.epicgames.com/community/api/documentation/image/7494a5c7-0341-42f7-aa3b-88d662d4b875?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7494a5c7-0341-42f7-aa3b-88d662d4b875?resizing_type=fit)

### Content Browser Context Menu

 You can open and view video assets using the Media Viewer using the Content Browser context menu options.

When you select **Open in Media Viewer**, the editor opens the Media Viewer and immediately starts playing the File Media Source asset.

[![](https://dev.epicgames.com/community/api/documentation/image/c2824e20-aed0-4415-ad11-cc0cf92054ca?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c2824e20-aed0-4415-ad11-cc0cf92054ca?resizing_type=fit)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Introduction](/documentation/en-us/unreal-engine/media-viewer-in-unreal-engine?application_version=5.7#introduction)
* [Getting Started](/documentation/en-us/unreal-engine/media-viewer-in-unreal-engine?application_version=5.7#gettingstarted)
* [Media Viewer Window](/documentation/en-us/unreal-engine/media-viewer-in-unreal-engine?application_version=5.7#mediaviewerwindow)
* [Media Viewer User Interface](/documentation/en-us/unreal-engine/media-viewer-in-unreal-engine?application_version=5.7#mediavieweruserinterface)
* [Multiple Tabs](/documentation/en-us/unreal-engine/media-viewer-in-unreal-engine?application_version=5.7#multipletabs)
* [Prompt to Open Previous Session](/documentation/en-us/unreal-engine/media-viewer-in-unreal-engine?application_version=5.7#prompttoopenprevioussession)
* [Library](/documentation/en-us/unreal-engine/media-viewer-in-unreal-engine?application_version=5.7#library)
* [Adding Media Assets](/documentation/en-us/unreal-engine/media-viewer-in-unreal-engine?application_version=5.7#adding-media-assets)
* [Toolbar Controls](/documentation/en-us/unreal-engine/media-viewer-in-unreal-engine?application_version=5.7#toolbar-controls)
* [Single and Side-By-Side Views](/documentation/en-us/unreal-engine/media-viewer-in-unreal-engine?application_version=5.7#singleandside-by-sideviews)
* [Pan, Zoom, and Rotation Controls](/documentation/en-us/unreal-engine/media-viewer-in-unreal-engine?application_version=5.7#pan,zoom,androtationcontrols)
* [Opacity and Compare Controls](/documentation/en-us/unreal-engine/media-viewer-in-unreal-engine?application_version=5.7#opacityandcomparecontrols)
* [Additional Controls and Settings](/documentation/en-us/unreal-engine/media-viewer-in-unreal-engine?application_version=5.7#additionalcontrolsandsettings)
* [Context Menu](/documentation/en-us/unreal-engine/media-viewer-in-unreal-engine?application_version=5.7#contextmenu)
* [Video Playback and Controls](/documentation/en-us/unreal-engine/media-viewer-in-unreal-engine?application_version=5.7#videoplaybackandcontrols)
* [A/B Synced Playback](/documentation/en-us/unreal-engine/media-viewer-in-unreal-engine?application_version=5.7#a/bsyncedplayback)
* [External Video Playback](/documentation/en-us/unreal-engine/media-viewer-in-unreal-engine?application_version=5.7#externalvideoplayback)
* [Sequencer-driven Playback](/documentation/en-us/unreal-engine/media-viewer-in-unreal-engine?application_version=5.7#sequencer-drivenplayback)
* [Add a Media Track to Sequencer](/documentation/en-us/unreal-engine/media-viewer-in-unreal-engine?application_version=5.7#addamediatracktosequencer)
* [Set a Media Texture](/documentation/en-us/unreal-engine/media-viewer-in-unreal-engine?application_version=5.7#setamediatexture)
* [Visualize Media Texture in Media Viewer](/documentation/en-us/unreal-engine/media-viewer-in-unreal-engine?application_version=5.7#visualizemediatextureinmediaviewer)
* [Use Sequencer for Playback Controls](/documentation/en-us/unreal-engine/media-viewer-in-unreal-engine?application_version=5.7#usesequencerforplaybackcontrols)
* [Set Up Videos For Fast Playback or Scrubbing](/documentation/en-us/unreal-engine/media-viewer-in-unreal-engine?application_version=5.7#setupvideosforfastplaybackorscrubbing)
* [Content Browser Context Menu](/documentation/en-us/unreal-engine/media-viewer-in-unreal-engine?application_version=5.7#contentbrowsercontextmenu)

Related documents

[Electra Media Player

![Electra Media Player](https://dev.epicgames.com/community/api/documentation/image/bb524cb7-db37-46c8-8b3f-14c30df87788?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/electra-media-player-in-unreal-engine)
