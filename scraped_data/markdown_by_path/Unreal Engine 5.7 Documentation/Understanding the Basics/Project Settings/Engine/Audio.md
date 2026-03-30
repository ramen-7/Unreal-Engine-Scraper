<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/audio-settings-in-the-unreal-engine-project-settings?application_version=5.7 -->

# Audio

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
5. [Understanding the Basics](/documentation/en-us/unreal-engine/understanding-the-basics-of-unreal-engine "Understanding the Basics")
6. [Project Settings](/documentation/en-us/unreal-engine/project-settings-in-unreal-engine "Project Settings")
7. [Engine](/documentation/en-us/unreal-engine/engine-settings-in-the-unreal-engine-project-settings "Engine")
8. Audio

# Audio

Reference for the Audio section of the Unreal Engine Project Settings.

On this page

## Audio

### Dialogue

| **Section** | **Description** |
| --- | --- |
| **Dialogue Filename Format** | The format string to use when generating the filename for contexts within dialogue waves.  This must generate unique names for your project.  Available format markers:   * **{DialogueGuid}**: The GUID of the dialogue wave. Guaranteed to be unique and stable against Asset renames. * **{DialogueHash}**: The hash of the dialogue wave. Not guaranteed to be unique or stable against Asset renames, however may be unique enough if combined with the dialogue name. * **{DialogueName}**: The name of the dialogue wave. Not guaranteed to be unique or stable against Asset renames, however may be unique enough if combined with the dialogue hash. * **{ContextId}**: The ID of the context. Guaranteed to be unique within its dialogue wave. Not guaranteed to be stable against changes to the context. * **{ContextIndex}**: The index of the context within its parent dialogue wave. Guaranteed to be unique within its dialogue wave. |

### Audio

| **Section** | **Description** |
| --- | --- |
| **Default Sound Class** | The `SoundClass` assigned to newly created sounds. |
| **Default Media Sound Class** | The `SoundClass` assigned to media player Assets. |
| **Default Sound Concurrency** | The `SoundConcurrency` assigned to newly created sounds. |
| **Default Base Sound Mix** | The `SoundMix` to use as base when no other system has specified a Base Sound Mix. |
| **VOIP Sound Class** | Sound class to be used for the VOIP audio component. |
| **VOIP Sample Rate** | Sample rate used for Voice Over IP (VOIP).  VOIP audio is resampled to the application's sample rate on the receiver side.  You can choose from the following options:   * **Low 16000 Hz** * **Normal 24000 Hz** |
| **Maximum Concurrent Streams** | Defines how many streaming sounds can be played at the same time (if more are played, they will be sorted by priority). |
| **Global Min Pitch Scale** | The value to use to clamp the minimum pitch scale. |
| **Global Max Pitch Scale** | The value to use to clamp the maximum pitch scale. |

### Mix

| **Section** | **Description** |
| --- | --- |
| **Master Submix** | The default submix through which all sounds are routed to.  The root submix that outputs to audio hardware. |
| **Reverb Submix** | The submix through which all sounds set to use reverb are routed. |
| **Default Audio Buses** | Array of `AudioBuses` that are automatically initialized when the `AudioEngine` is initialized. |
| **Base Default Submix** | The default submix the audio engine uses when no submix is specified during a Submix Send. |
| **EQ Submix (Legacy)** | The submix through which all sounds set to use the legacy equalizer (EQ) system are routed |

### Quality

| **Section** | **Description** |
| --- | --- |
| **Quality Levels** | The quality levels of the audio. |
| **Allow Play when Silent** | Allows sounds to play at 0 volume. |
| **Disable Master EQ** | Disables master EQ effect in the audio DSP graph. |
| **Allow Center Channel 3DPanning** | Enables the surround sound spatialization calculations to include the center channel. |
| **Num Stopping Sources** | The maximum number of sources to reserve for "stopping" sounds.  A "stopping" sound applies a fast fade in the DSP render to prevent discontinuities when stopping sources. |
| **Panning Method** | The method to use when doing non-binaural or object-based panning.  You can choose from the following options:   * **Linear** * **Equal Power** |
| **Mono Channel Upmix Method** | The upmixing method for mono sound sources.  Defines how mono channels are upmixed to stereo channels.  You can choose from the following options:   * **Linear** * **Equal Power** * **Full Volume** |

### Debug

| **Section** | **Description** |
| --- | --- |
| **Debug Sounds** | A list of sounds that should only be packaged in non-shipping builds, typically intended for debugging purposes. |

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [basics](https://dev.epicgames.com/community/search?query=basics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Audio](/documentation/en-us/unreal-engine/audio-settings-in-the-unreal-engine-project-settings?application_version=5.7#audio)
* [Dialogue](/documentation/en-us/unreal-engine/audio-settings-in-the-unreal-engine-project-settings?application_version=5.7#dialogue)
* [Audio](/documentation/en-us/unreal-engine/audio-settings-in-the-unreal-engine-project-settings?application_version=5.7#audio-2)
* [Mix](/documentation/en-us/unreal-engine/audio-settings-in-the-unreal-engine-project-settings?application_version=5.7#mix)
* [Quality](/documentation/en-us/unreal-engine/audio-settings-in-the-unreal-engine-project-settings?application_version=5.7#quality)
* [Debug](/documentation/en-us/unreal-engine/audio-settings-in-the-unreal-engine-project-settings?application_version=5.7#debug)
