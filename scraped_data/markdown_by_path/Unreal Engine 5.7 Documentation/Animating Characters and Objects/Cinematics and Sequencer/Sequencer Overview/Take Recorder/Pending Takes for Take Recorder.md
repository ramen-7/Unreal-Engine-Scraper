<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/pending-takes-for-take-recorder-in-unreal-engine?application_version=5.7 -->

# Pending Takes for Take Recorder

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
8. [Take Recorder](/documentation/en-us/unreal-engine/take-recorder-in-unreal-engine "Take Recorder")
9. Pending Takes for Take Recorder

# Pending Takes for Take Recorder

Learn the basics of using Pending Take in Take Recorder.

On this page

You can use **Pending Takes** for recording gameplay, simulations, and PIE events, then use them to add to or overwrite existing sequences with the newly-recorded data.

## Adding New Sequence Data

To add new data to an existing sequence, follow these steps:

1. Set up a new project and animate a cube by following the steps from the [Creating Camera Cuts Using Sequencer](/documentation/en-us/unreal-engine/creating-camera-cuts-using-sequencer-in-unreal-engine) tutorial for [setting up a 3rd person project](/documentation/en-us/unreal-engine/creating-camera-cuts-using-sequencer-in-unreal-engine#setuptheproject) and [animating a cube](/documentation/en-us/unreal-engine/creating-camera-cuts-using-sequencer-in-unreal-engine#animateacube).
2. Open the **Take Recorder** panel: **Window > Cinematics > Take Recorder**.
3. Right-click on the cube sequence in the **Content Browser** and select **Open in Take Recorder**. The sequence you selected does not appear as a source in the **Source** panel. However, in the **Outliner**, Sequencer displays '**Pending Take**' as its sequence, which informs you the take is active with Take Recorder.

   ![Existing sequence added to Take Recorder](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8570e0dd-6a9e-4905-bdb3-956bfcd0bd2f/outline_pending_take.png)
4. Add the **Player** actor to **Take Recorder** and record your player interaction with the cube.
   1. Click **+ Source** and select **Player**.
   2. Start **PIE**.
   3. In the **Take Recorder**, click **Record**. The sequence starts playing the moment you start recording. If your cube animation isn't longer than three seconds, you need to adjust the [Countdown](/documentation/en-us/unreal-engine/take-recorder-in-unreal-engine#countdown) value in **User Settings** as it defaults to a three second delay at the start of recording.
   4. Move your player around the animated cube.
5. When finished, click the **Stop** button or press the **Esc** key.
6. Click **Review last recording** to review your take.

Your take can go beyond the duration of the added sequence.
Opening a sequence in Take Recorder is different from sourcing a sequence.

## Overriding Sequence Data

Overriding a sequence only records the duration of the selected sequence.

Using Record with Take Recorder provides you with a way to re-record a take and overwrite the existing sequence data.
This is a destructive process! Record with Take Recorder adds all sourced actors tracks to the select sequence and overrides the data for any actors in the sequence.
The length of the take is determined by the duration of the selected sequence.

1. Set up a new project and animate a cube by following the steps from the [Creating Camera Cuts Using Sequencer](/documentation/en-us/unreal-engine/creating-camera-cuts-using-sequencer-in-unreal-engine) tutorial for [setting up a 3rd person project](/documentation/en-us/unreal-engine/creating-camera-cuts-using-sequencer-in-unreal-engine#setuptheproject) and [animating a cube](/documentation/en-us/unreal-engine/creating-camera-cuts-using-sequencer-in-unreal-engine#animateacube).
2. Open the **Take Recorder** panel: **Window > Cinematics > Take Recorder**.
3. Right-click on the cube sequence in the **Content Browser** and select **Record with Take Recorder**. The selected sequence does not appear as a source in the Source panel. However, the Slate title has the name of the sequence you added.
4. Add the **Player** actor to **Take Recorder** and record your player interaction with the cube.
   1. Click **+ Source** and select **Player**.
   2. Start **PIE**.
   3. In the **Take Recorder**, click **Record**. The sequence starts playing the moment you start recording. If you want to end the take earlier, click the **Stop** button or press **Esc** key.
   4. Move your player to interact with the moving cube and let the duration of the sequence end the recording.
5. In **Sequencer**, play the revised sequence and note the changes.

![Record with Take Recorder](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0728a98a-b9ee-4c07-8849-614b294fa9fa/record_with_take_recorder.gif)

* [sequencer](https://dev.epicgames.com/community/search?query=sequencer)
* [take recorder](https://dev.epicgames.com/community/search?query=take%20recorder)
* [pending take](https://dev.epicgames.com/community/search?query=pending%20take)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Adding New Sequence Data](/documentation/en-us/unreal-engine/pending-takes-for-take-recorder-in-unreal-engine?application_version=5.7#addingnewsequencedata)
* [Overriding Sequence Data](/documentation/en-us/unreal-engine/pending-takes-for-take-recorder-in-unreal-engine?application_version=5.7#overridingsequencedata)
