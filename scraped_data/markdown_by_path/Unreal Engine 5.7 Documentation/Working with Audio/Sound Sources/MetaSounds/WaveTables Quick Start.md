<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/wavetables-quick-start-in-unreal-engine?application_version=5.7 -->

# WaveTables Quick Start

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
7. [MetaSounds](/documentation/en-us/unreal-engine/metasounds-in-unreal-engine "MetaSounds")
8. WaveTables Quick Start

# WaveTables Quick Start

A quick guide on getting started with WaveTables.

![WaveTables Quick Start](https://dev.epicgames.com/community/api/documentation/image/1825eed0-6c53-43b4-bdd5-f1561ada3dbb?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

**WaveTables** store periodic wave data in lookup tables and provide a way to perform wavetable synthesis and sampling in **MetaSounds**.

This guide teaches you how to create a MetaSound powered by two WaveTables with different Sample Modes.

* **Fixed Resolution** - Enforces uniform resolution of all WaveTables in the bank. This mode supports lockstep mixing, interpolating, and spatializing, which is useful for oscillating or enveloping.
* **Fixed Sample Rate** - Enforces uniform sample rate for all WaveTables in the bank. This mode supports discrete audio playback at a shared speed, which is helpful for sampling and granulating.

## Create the Fixed Resolution WaveTable Bank

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3963d580-0ec1-48f0-8d41-fa7971c543f8/fixed_resolution_bank.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3963d580-0ec1-48f0-8d41-fa7971c543f8/fixed_resolution_bank.png)

Click image for full size.

To create the Fixed Resolution WaveTable Bank:

1. In the **Content Browser**, click the **Add** button.
2. Select **Audio > WaveTable > WaveTable Bank**.
3. Name the WaveTable Bank `WTB_FixedResolution`.
4. Double-click the WaveTable Bank to open the **WaveTable Bank Editor**.
5. In the **Details** panel:
   1. Disable **Bipolar**.
   2. Click the **Add Element (+)** button for **Entries** twice.
   3. Expand **Index [0]** and set **Curve Type** to **Linear (Ramp Out)**.
   4. Expand **Index [1]** and set **Curve Type** to **Linear (Ramp In)**.
6. Save the WaveTable Bank.
7. Close the **WaveTable Bank Editor**.

## Create the Fixed Sample Rate WaveTable Bank

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/95c5e9c3-fead-46d6-b3e8-754e0132127c/fixed_sample_rate_bank.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/95c5e9c3-fead-46d6-b3e8-754e0132127c/fixed_sample_rate_bank.png)

Click image for full size.

To create the Fixed Sample Rate WaveTable Bank:

1. In the **Content Browser**, click the **Add** button.
2. Select **Audio > WaveTable > WaveTable Bank**.
3. Name the WaveTable Bank `WTB_FixedSampleRate`.
4. Double-click the WaveTable Bank to open the **WaveTable Bank Editor**.
5. In the **Details** panel:
   1. Click the **Add Element (+)** button for **Entries** twice.
   2. Expand **Index [0]**:
      1. Set **Curve Type** to **Sine (360 deg)**
      2. Set **Duration (Sec)** to 0.5.
   3. Expand **Index [1]**:
      1. Set **Curve Type** to **Sine (360 deg)**.
      2. Set **Duration (Sec)** to 1.0.
6. Save the WaveTable Bank.
7. Close the **WaveTable Bank Editor**.

## Create the MetaSound Source

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d0d8465f-2830-49b4-be53-501024e3846a/ms_graph.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d0d8465f-2830-49b4-be53-501024e3846a/ms_graph.png)

Click image for full size.

Construct a MetaSound that uses the WaveTable Banks for generating and enveloping. Follow the steps below to build a MetaSound with the graph above.

1. In the **Content Browser**, click the **Add** button.
2. Select **Audio > MetaSound Source**.
3. Name the new MetaSound `MSS_WaveTableDemo`.
4. Double-click the MetaSound to open the **MetaSound Editor**.
5. In the **Interfaces** panel, click the **Remove (Trash Bin)** button next to the **UE.Source.OneShot** Interface entry. This removes the On Finished Output node, which isn't used on looping sounds.

### Build the Generator Section

1. Find the **On Play Input** node in the graph and drag off of the pin into an empty space. Enter "Trigger Repeat" into the node search to create a connected node. You can move the node around the graph by dragging it.
2. On the **Trigger Repeat** node:
   1. Set **Period** to 1.0.
   2. Drag offthe **RepeatOut** pin and create a **Trigger Counter** node.
3. On the **Trigger Counter** node:
   1. Set **Reset Count** to 2.0.
   2. Drag off the **On Trigger** pin and create a **WaveTable** **Player** node.
   3. Connect the **Count** pin to the **Index** pin of the **WaveTable Player** node.
4. On the **WaveTable Player** node:
   1. Click the **Bank** dropdown and set it to `WTB_FixedSampleRate`.
   2. Set **Pitch Shift** to 440.0.
   3. Enable **Loop**.

### Build the Envelope Section

1. Right-click in an empty space and create a **Get WaveTable From Bank** node.
2. On the **Get WaveTable From Bank** node:
   1. Click the **Bank** dropdown and set it to `WTB_FixedResolution`.
   2. Drag off the **TableIndex** pin and select **Promote to Graph Input**. This creates a **Float Input** node named TableIndex.
   3. Drag off the **Out** pin and create a **WaveTable Envelope** node.
3. On the **WaveTable Envelope** node:
   1. Drag off the **On Play** pin and create a **Get On Play** node.
   2. Click the down arrow at the bottom of the node to expand the pin list.
   3. Set **Mode** to Loop.

### Connect the Outputs

1. Right-click in an empty space and create a **Mono Mixer (2)** node.
2. On the **Mono Mixer (2)** node:
   1. Connect the **In 0** pin to the **Mono Out** pin of the **WaveTable Player** node.
   2. Connect the **Gain 0 (Lin)** pin to the **Out** pin of the **WaveTable Envelope** node.
   3. Connect the **Out** pin to the **Out Mono Output** node.
3. Save the MetaSound.

## Test the MetaSound

Click the **Play** button on the **MetaSound Editor Toolbar** to play the MetaSound. You can adjust the **TableIndex** graph input value by clicking the **Input Widget (Dial)** on the node and dragging up or down.

The WaveTables in `WTB_FixedSampleRate` alternate playback every second. The gain is controlled by a WaveTable from `WTB_FixedResolution`, which is selected by the TableIndex graph input. TableIndex values between 0 and 1 produce a blend between the WaveTables in the bank.

## Own Your Own!

Now that you've finished this Quick Start, consider taking this project further. Below are some suggestions you can explore on your own.

* Build a MetaSound with the WaveTable nodes not used in this guide, such as the **WaveTable Oscillator** node and **Evaluate WaveTable** node. For more information on WaveTable nodes, see [MetaSounds Reference Guide](/documentation/en-us/unreal-engine/metasounds-reference-guide-in-unreal-engine).
* Customize your WaveTable curves by setting the **Curve Type** to **Custom**. See [Curve Editor](/documentation/en-us/unreal-engine/animation-curve-editor-in-unreal-engine) for more information about the toolbar and editing curves.
* Import audio files as a WaveTable by setting the **Curve Type** to **File** and the **Wave Table Settings > File Path.**

* [beta](https://dev.epicgames.com/community/search?query=beta)
* [audio](https://dev.epicgames.com/community/search?query=audio)
* [sound sources](https://dev.epicgames.com/community/search?query=sound%20sources)
* [metasounds](https://dev.epicgames.com/community/search?query=metasounds)
* [wavetables](https://dev.epicgames.com/community/search?query=wavetables)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Create the Fixed Resolution WaveTable Bank](/documentation/en-us/unreal-engine/wavetables-quick-start-in-unreal-engine?application_version=5.7#createthefixedresolutionwavetablebank)
* [Create the Fixed Sample Rate WaveTable Bank](/documentation/en-us/unreal-engine/wavetables-quick-start-in-unreal-engine?application_version=5.7#createthefixedsampleratewavetablebank)
* [Create the MetaSound Source](/documentation/en-us/unreal-engine/wavetables-quick-start-in-unreal-engine?application_version=5.7#createthemetasoundsource)
* [Build the Generator Section](/documentation/en-us/unreal-engine/wavetables-quick-start-in-unreal-engine?application_version=5.7#buildthegeneratorsection)
* [Build the Envelope Section](/documentation/en-us/unreal-engine/wavetables-quick-start-in-unreal-engine?application_version=5.7#buildtheenvelopesection)
* [Connect the Outputs](/documentation/en-us/unreal-engine/wavetables-quick-start-in-unreal-engine?application_version=5.7#connecttheoutputs)
* [Test the MetaSound](/documentation/en-us/unreal-engine/wavetables-quick-start-in-unreal-engine?application_version=5.7#testthemetasound)
* [Own Your Own!](/documentation/en-us/unreal-engine/wavetables-quick-start-in-unreal-engine?application_version=5.7#ownyourown!)

Related documents

[MetaSounds

![MetaSounds](https://dev.epicgames.com/community/api/documentation/image/25e90f66-dad2-46f5-b360-4be6aef03efb?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/metasounds-in-unreal-engine)
