<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/multi-track-audio-capture-for-take-recorder-in-unreal-engine?application_version=5.7 -->

# Multi-Track Audio Capture for Take Recorder

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
9. Multi-Track Audio Capture for Take Recorder

# Multi-Track Audio Capture for Take Recorder

Record multi-track audio with Take Recorder.

Multi-Track Audio Capture for Take Recorder
**Take Recorder** provides options for recording audio. You can create multiple (up to 8) **Microphone Audio** sources in Take Recorder to record audio from multi-channel audio devices.

![Multi-track audio sources](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c46cb610-e878-4086-b378-bb902cd2ab7b/multi-track_audio_sources.png)

Each **Microphone Audio** source has an associated **Audio Input Device Channel** that designates the input channel on the selected audio device. Up to 8 channels are supported via the **Windows Audio Session API**. It is important to note that the audio device must have **Windows WDM multi-channel support** in order to have 8 channels available. There are third-party audio device manufacturers that offer Windows WDM multi-channel support.

See [Microphone Audio Recorder](/documentation/en-us/unreal-engine/take-recorder-in-unreal-engine#microphoneaudiorecorder) and [Audio Input Device](/documentation/en-us/unreal-engine/take-recorder-in-unreal-engine#audioinputdevice) sections for more information about these audio settings.

* [audio](https://dev.epicgames.com/community/search?query=audio)
* [sequencer](https://dev.epicgames.com/community/search?query=sequencer)
* [take recorder](https://dev.epicgames.com/community/search?query=take%20recorder)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)
