<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/wavetables-overview-in-unreal-engine?application_version=5.7 -->

# WaveTables Overview

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
8. WaveTables Overview

# WaveTables Overview

An overview of the wavetable synthesis system.

![WaveTables Overview](https://dev.epicgames.com/community/api/documentation/image/458e5195-11dc-460d-b6d3-fdf3014f8cc0?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

**WaveTables** store periodic wave data in lookup tables and provide a way to perform wavetable synthesis and sampling in **MetaSounds**.

## WaveTable Banks

Unreal Engine stores WaveTables in **WaveTable Bank** assets.

You can create a WaveTable Bank in the **Content Browser** by clicking the **Add** button and selecting **Audio > WaveTable > WaveTable Bank**.

### Editor

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a7ea71f2-11bd-4ad5-a54a-62ef58a1eb6a/wavetable_bank_editor.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a7ea71f2-11bd-4ad5-a54a-62ef58a1eb6a/wavetable_bank_editor.png)

Click image for full size.

You can edit a WaveTable Bank in the **WaveTable Bank Editor**. Double-click a WaveTable Bank in the Content Browser to open the WaveTable Bank Editor.

The WaveTable Bank Editor has three main UI components.

1. **Curve Editor Toolbar** - Use these tools to change your viewing mode or edit Custom Curve Type WaveTables. For more information about the toolbar and editing curves, see [Curve Editor](/documentation/en-us/unreal-engine/animation-curve-editor-in-unreal-engine).
2. **Details** **Panel** - Edit the WaveTable Bank's properties.
3. **Transform Curve** **Panel** - View all of the WaveTable curves in the WaveTable Bank.

### Properties

You can find the WaveTable Bank's properties in the Details panel.

| **Property** | **Description** |
| --- | --- |
| **Sample Mode** | The sampling mode used for the bank. Options include:   * **Fixed Resolution** - Enforces uniform resolution of all WaveTables in the bank. This mode supports lockstep mixing, interpolating, and spatializing, which is useful for oscillating or enveloping. * **Fixed Sample Rate** - Enforces uniform sample rate for all WaveTables in the bank. This mode supports discrete audio playback at a shared speed, which is useful for sampling and granulating. |
| **Resolution / Sample Rate** | The number of samples cached for each bank entry. |
| **Bipolar** | If enabled, the curve is clamped between -1.0 and 1.0, which is useful for waveform generation and oscillation. If disabled, the curve is clamped between 0.0 and 1.0, which is useful for enveloping. |
| **WaveTable Size (MB)** | (Read-only) The total size of all WaveTable data within the bank. |
| **Entries** | The array of WaveTables in the bank. |
| **Curve Type** | The curve to apply when transforming the output. Options include:   * Presets, such as Sine (360 deg) and Linear (Ramp In). * **Shared** - Reference a shared **Curve** asset. * **Custom** - Design a custom curve. * **File** - Generate a WaveTable from an audio file. |
| **Duration (Sec)** | (Fixed Sample Rate only) The duration of the curve. |

## MetaSound Nodes

There are three categories of WaveTable MetaSound nodes.

* Generators
* Envelopes
* Utility

For more information about each of the nodes below, see [MetaSounds Reference Guide](/documentation/en-us/unreal-engine/metasounds-reference-guide-in-unreal-engine).

### Generators

MetaSound supports several core generator nodes, such as **Sine** and **Saw**. They are powerful synthesis tools, but WaveTable generator nodes are even more so.

With WaveTable generator nodes, you can use custom waves and samples to drive your synthesis.

These nodes include:

* **WaveTable Player** - Plays the WaveTable at the given index of a WaveTable Bank. This node expects a Fixed Sample Rate WaveTable Bank.
* **WaveTable Oscillator** - Plays the WaveTable at the given frequency. This node expects a Fixed Resolution WaveTable Bank.

### Envelopes

MetaSound also supports several core envelope nodes, such as **AD Envelope** and **ADSR Envelope**. WaveTable envelope nodes improve on those traditional options as well.

With WaveTable envelope nodes, you can use custom waves and samples for more powerful modulation.

These nodes include:

* **WaveTable Envelope** - Reads the WaveTable over the given duration. This node expects a Fixed Resolution WaveTable Bank.
* **Evaluate WaveTable** - Evaluates the WaveTable at the given input value.

### Utility

You can use the **Get WaveTable From Bank** node to get a WaveTable to use as an input into another node. The **TableIndex** float input supports blending between WaveTables in a Fixed Resolution bank.

* [beta](https://dev.epicgames.com/community/search?query=beta)
* [audio](https://dev.epicgames.com/community/search?query=audio)
* [sound sources](https://dev.epicgames.com/community/search?query=sound%20sources)
* [metasounds](https://dev.epicgames.com/community/search?query=metasounds)
* [wavetables](https://dev.epicgames.com/community/search?query=wavetables)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [WaveTable Banks](/documentation/en-us/unreal-engine/wavetables-overview-in-unreal-engine?application_version=5.7#wavetablebanks)
* [Editor](/documentation/en-us/unreal-engine/wavetables-overview-in-unreal-engine?application_version=5.7#editor)
* [Properties](/documentation/en-us/unreal-engine/wavetables-overview-in-unreal-engine?application_version=5.7#properties)
* [MetaSound Nodes](/documentation/en-us/unreal-engine/wavetables-overview-in-unreal-engine?application_version=5.7#metasoundnodes)
* [Generators](/documentation/en-us/unreal-engine/wavetables-overview-in-unreal-engine?application_version=5.7#generators)
* [Envelopes](/documentation/en-us/unreal-engine/wavetables-overview-in-unreal-engine?application_version=5.7#envelopes)
* [Utility](/documentation/en-us/unreal-engine/wavetables-overview-in-unreal-engine?application_version=5.7#utility)

Related documents

[MetaSounds

![MetaSounds](https://dev.epicgames.com/community/api/documentation/image/25e90f66-dad2-46f5-b360-4be6aef03efb?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/metasounds-in-unreal-engine)
