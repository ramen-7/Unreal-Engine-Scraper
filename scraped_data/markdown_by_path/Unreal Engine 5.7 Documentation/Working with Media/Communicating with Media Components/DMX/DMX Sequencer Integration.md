<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/dmx-sequencer-integration-in-unreal-engine?application_version=5.7 -->

# DMX Sequencer Integration

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
6. [Communicating with Media Components](/documentation/en-us/unreal-engine/communicating-with-media-components-from-unreal-engine "Communicating with Media Components")
7. [DMX](/documentation/en-us/unreal-engine/dmx-in-unreal-engine "DMX")
8. DMX Sequencer Integration

# DMX Sequencer Integration

Information about DMX tracks and Sequencer workflow, including integration, recording, and playback of DMX Data in Unreal Engine.

![DMX Sequencer Integration](https://dev.epicgames.com/community/api/documentation/image/a3115185-33da-492f-83cf-bfbefb93dbab?resizing_type=fill&width=1920&height=335)

 On this page

Sequencer is an Unreal Engine feature that provides easy animation and event triggering. Sequencer supports Digital Multiplex (DMX) recording, playback, and editing through custom **DMX Sequencer** tracks to help you better design and preview lighting experiences in virtual or physical shows and live events.

You can add a custom DMX track to a Level Sequence to program and control DMX without the need for Blueprints or programming.

## Add a DMX Sequencer Track to a Level Sequence

The custom DMX Sequencer track connects to a [**DMX Library**](/documentation/en-us/unreal-engine/create-a-dmx-library-and-add-fixture-patches-in-unreal-engine). You can add any [**Fixture Patch**](/documentation/en-us/unreal-engine/dmx-overview) from that DMX Library into the track, and expose the patch's attributes for sending out DMX. You can add keyframes for each attribute to the track to animate and control the DMX output. You can then replay, edit, and share the [**Level Sequence**](/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview) that contains the DMX track.

### Steps

To add a Fixture Patch to a Level Sequence, follow these steps:

1. Press the **+ Track** button and select **DMX Library Track** from the list. Select the DMX Library you want to add to the sequence.

   [![DMX Library Track](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/63aab3d9-67d8-490d-929d-71c09bf5680b/dmx-library-track.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/63aab3d9-67d8-490d-929d-71c09bf5680b/dmx-library-track.png)

   Click image to expand.
2. On the new DMX Library Track, click the **Add (+)** button and select a Fixture Patch to create a new track for the desired patch. You can also click **Add All Patches** in the dropdown menu to create a new track for every Fixture Patch in the library.

   [![Add all Patches](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/eaf2c32c-94ba-4b4e-af31-b27f70b06a5d/add-all-patches.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/eaf2c32c-94ba-4b4e-af31-b27f70b06a5d/add-all-patches.png)

   Click image to expand.
3. Expand a fixture patch track and add a new keyframe by pressing the **Add (+)** button or by modifying the value next to the attribute name. The value ranges are defined by the DMX signal format selected in the DMX Library for each Attribute.

   [![Add a new Keyframe](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/38dbdbc9-e569-4a45-86da-70686eb327ea/add-a-new-keyframe.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/38dbdbc9-e569-4a45-86da-70686eb327ea/add-a-new-keyframe.png)

   Click image to expand.

Sequencer sends DMX data both when you press play and when you scrub the playback head.

By default, the recorded sequence will be locked from editing. To unlock the sequence for editing, click the Lock icon next to the sequence name in the sequence editor.

[![Unlock Sequence for editing](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/de4553cc-8778-4df3-bec4-cc5609d5215a/unlock-sequence.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/de4553cc-8778-4df3-bec4-cc5609d5215a/unlock-sequence.png)

Click image to expand.

## Record DMX with Take Recorder

The DMX plugin **Take Recorder** tool can listen for incoming DMX streams and record the data as new keyframes in a Level Sequence. You can then replay, edit, and share this Level Sequence. You can listen for incoming DMX for a specified Fixture Patch assigned in a DMX library, and record changes to keyframes in the Level Sequence.

### Steps

To record DMX to a level sequence, follow these steps:

1. To open the Take Recorder, click **Window** > **Cinematics** > **Take Recorder**.
2. Click **Source (+)** and select **DMX Library** from the list.

   [![Add selected DMX Library to DMX Take Recorder](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/711301ea-569b-4ec6-8501-1f70058324ff/add-to-dmx-take-recorder.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/711301ea-569b-4ec6-8501-1f70058324ff/add-to-dmx-take-recorder.png)

   Click image to expand.
3. Set the DMX Library parameter to the Library containing the patch you want to record.

   [![DMX Library parameter](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ed6910b4-7d3e-486a-9677-c1d7887e1666/dmx-library-parameter.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ed6910b4-7d3e-486a-9677-c1d7887e1666/dmx-library-parameter.png)

   Click image to expand.
4. Click the **Fixture Patch** parameter and select a patch from the list to add it to the patch record list, or click **Add all Fixture Patches** to add all patches in the library to the patch record list.

   [![Add all Fixture Patches](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bf3efefd-026e-4d49-a7f3-152d7de6b4bb/add-all-fixture-patches.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bf3efefd-026e-4d49-a7f3-152d7de6b4bb/add-all-fixture-patches.png)

   Click image to expand.
5. Click **Record**. All incoming DMX that matches the patch record list will be saved into a new Level Sequence as a new keyframe.
6. When you are done recording, navigate to the created sequence in the **Content Browser** to review and play back the recorded DMX. The new sequence should be saved to `Cinematics/Takes/[RecordDate]/`.

After recording with Take Recorder, the recorded sequence will be locked from editing. To unlock the sequence for editing, click the Lock icon next to the sequence name in the sequence editor.

[![Unlock Sequence for editing](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/57d7cda5-3ef6-47ef-bba5-6a8b7a689352/unlock-sequence.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/57d7cda5-3ef6-47ef-bba5-6a8b7a689352/unlock-sequence.png)

Click image to expand.

* [reference](https://dev.epicgames.com/community/search?query=reference)
* [dmx](https://dev.epicgames.com/community/search?query=dmx)
* [ar/vr/xr](https://dev.epicgames.com/community/search?query=ar%2Fvr%2Fxr)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Add a DMX Sequencer Track to a Level Sequence](/documentation/en-us/unreal-engine/dmx-sequencer-integration-in-unreal-engine?application_version=5.7#addadmxsequencertracktoalevelsequence)
* [Steps](/documentation/en-us/unreal-engine/dmx-sequencer-integration-in-unreal-engine?application_version=5.7#steps)
* [Record DMX with Take Recorder](/documentation/en-us/unreal-engine/dmx-sequencer-integration-in-unreal-engine?application_version=5.7#recorddmxwithtakerecorder)
* [Steps](/documentation/en-us/unreal-engine/dmx-sequencer-integration-in-unreal-engine?application_version=5.7#steps-2)
