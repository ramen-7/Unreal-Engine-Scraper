<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/waveform-editor-quick-start-in-unreal-engine?application_version=5.7 -->

# Waveform Editor Quick Start

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
5. [Working with Audio](/documentation/en-us/unreal-engine/working-with-audio-in-unreal-engine "Working with Audio")
6. [Sound Sources](/documentation/en-us/unreal-engine/sound-sources-in-unreal-engine "Sound Sources")
7. Waveform Editor Quick Start

# Waveform Editor Quick Start

A quick guide on getting started with the Waveform Editor.

![Waveform Editor Quick Start](https://dev.epicgames.com/community/api/documentation/image/33094ef0-2471-4ea0-841d-749b15bae6a2?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

Using the **Waveform Editor**, you can edit Sound Waves with basic transformations, such as trim fade and normalization.

The Waveform Editor is not intended to replace a traditional digital audio workstation (DAW).

## Prerequisites

![Waveform Editor Plugin](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ffdeaa69-336e-4164-8403-bf2291cfa8d0/plugin.png)

* The Waveform Editor plugin is disabled by default. To enable it, open the **Plugin** panel by selecting **Edit > Plugins**, use the search bar to find the plugin, and then select the corresponding checkbox.
* This guide also requires you to have a **Sound Wave** asset in your project. See [Importing Audio Files](/documentation/en-us/unreal-engine/importing-audio-files) for information on how to create Sound Waves.

## 1 - Open the Waveform Editor

![Edit Waveform Context Menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3bce2af5-c02c-4e2e-9ebf-b4763a3a9d30/edit_waveform.png)

To edit your Sound Wave asset, you need to open the Waveform Editor.

1. Right-click the **Sound Wave** file you want to edit in the **Content Browser**.
2. Select **Edit Waveform** from the context menu. This opens the Waveform Editor in a new window.

## 2 - Get Familiar with the UI

![Waveform Editor UI Overview](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4fc24df8-2043-4503-ba8c-c90358440f53/ui_overview.png)

Now that you have the Waveform Editor open, take a moment to get familiar with the user interface.

1. **File Controls**: Save the current Sound Wave or locate it in the Content Browser.
2. **Transport Controls**: Play, pause, and stop the active Sound Wave.
3. **Zoom Controls**: Zoom the waveform in or out.
4. **Export Options**: Export the current edits to another Sound Wave asset or change the channel format (mono or stereo).
5. **Processing Panel**: View or apply waveform transformations.
6. **Details Panel**: View or modify the Sound Wave asset details.
7. **Time Ruler**: Display the timing of the current Sound Wave or track and change playback by moving the playhead.

You can change colors, line thickness, and other display settings for the Waveform Editor in **Editor Preferences > Waveform Editor Display**.

## 3 - Trim Fade

![Trim Fade Transformation](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3122801f-c435-40e6-a2dc-b11683151657/trim_fade.png)

You can use the **Trim Fade** transformation to edit timing and add fades to the beginning and end of a sound.

1. Find the Transformations array in the **Processing** panel.
2. Click **Add Element** to add a transformation to the array.

   ![Add Element Button](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bbd4352a-f990-47c4-ae5d-5377f77866e1/add_button.png)

   The Add Element button
3. Select **Waveform Transformation Trim Fade** from the new index's dropdown.
4. Expand the transformation properties by clicking the arrows on the left of the index, the **Trim** group, and the **Fade** group.
5. Change the Trim properties to your liking.
   * **Start Time**: The time (in seconds) to start the trimmed sound.
   * **End Time**: The time (in seconds) to stop the trimmed sound.
6. Change the Fade properties to your liking.
   * **Fade-In Duration**: The duration (in seconds) of the fade-in.
   * **Fade-In Curve**: The shape of the fade-in.
   * **Fade-Out Duration**: The duration (in seconds) of the fade-out.
   * **Fade-Out Curve**: The shape of the fade-out.

You can use your mouse to control the properties of the Trim Fade transformation.

* Drag the trim boundary to change the Start Time and End Time.
* Drag from the top-left corner to change the Fade-In Duration.
* Drag from the top-right corner to change the Fade-Out Duration.
* Scroll the mouse-wheel over a fade line to change the Fade Curve.

## 4 - Normalize

![Normalize Transformation](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/163e9588-739c-44df-8e16-1e6e12ad1a12/normalize.png)

You can use the **Normalize** transformation to apply a constant amount of gain to target a maximum volume level. By doing this after the **Trim Fade** transformation, the normalization will apply only to the trimmed section of the waveform.

1. Find the Transformations array in the **Processing** panel.
2. Click **Add Element** to add another transformation to the array.
3. Select **Waveform Transformation Normalize** from the new index's dropdown.
4. Expand the **Transformation** properties by clicking the arrows on the left of the index and the Normalization group.
5. Change the **Normalization** properties to your liking.
   * **Target**: The target maximum volume (in decibels).
   * **Max Gain**: The maximum gain to apply.
   * **Mode**: The type of analysis used to find the peak value.

## 5 - Export the Edits

![Edited Asset](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f018a245-1701-46ee-af23-043a9217f945/edited_asset.png)

Once you've made your edits, you can export the edited waveform to a new Sound Wave asset.

1. Click **Export Options** and select your desired channel format.

   ![Export Options Button](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e8b1c4cd-9ebe-4b82-b9b9-38fd337e1042/export_options_button.png)

   The Export Options button
2. Click the **Export** button. A **Save Content** window appears.

   ![Export Button](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/987c7add-b394-4961-aea3-f952aa90f23d/export_button.png)

   The Export button
3. Click **Save Selected** in the **Save Content** window.
4. Using the **Content Browser**, you can now find the new edited Sound Wave asset in the same directory as the original with `_Edited` appended to its original name.
5. If you want to rename the asset, right click and select **Rename** from the context menu.

## Result

Your edited Sound Wave asset is now ready for use in your project.

You can set default transformations to be applied every time the Waveform Editor is opened within **Editor Preferences > Waveform Editor Transformations**.

* [beta](https://dev.epicgames.com/community/search?query=beta)
* [audio](https://dev.epicgames.com/community/search?query=audio)
* [sound sources](https://dev.epicgames.com/community/search?query=sound%20sources)
* [waveform editor](https://dev.epicgames.com/community/search?query=waveform%20editor)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisites](/documentation/en-us/unreal-engine/waveform-editor-quick-start-in-unreal-engine?application_version=5.7#prerequisites)
* [1 - Open the Waveform Editor](/documentation/en-us/unreal-engine/waveform-editor-quick-start-in-unreal-engine?application_version=5.7#1-openthewaveformeditor)
* [2 - Get Familiar with the UI](/documentation/en-us/unreal-engine/waveform-editor-quick-start-in-unreal-engine?application_version=5.7#2-getfamiliarwiththeui)
* [3 - Trim Fade](/documentation/en-us/unreal-engine/waveform-editor-quick-start-in-unreal-engine?application_version=5.7#3-trimfade)
* [4 - Normalize](/documentation/en-us/unreal-engine/waveform-editor-quick-start-in-unreal-engine?application_version=5.7#4-normalize)
* [5 - Export the Edits](/documentation/en-us/unreal-engine/waveform-editor-quick-start-in-unreal-engine?application_version=5.7#5-exporttheedits)
* [Result](/documentation/en-us/unreal-engine/waveform-editor-quick-start-in-unreal-engine?application_version=5.7#result)
