<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/importing-audio-files?application_version=5.7 -->

# Importing Audio Files

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
7. [Sound Waves](/documentation/en-us/unreal-engine/sound-waves "Sound Waves")
8. Importing Audio Files

# Importing Audio Files

Learn how to create Sound Wave assets by importing audio files.

![Importing Audio Files](https://dev.epicgames.com/community/api/documentation/image/9b973d85-e089-4372-b3d8-e85fadfe28b1?resizing_type=fill&width=1920&height=335)

 On this page

Unreal Engine provides several features for you to create the desired audio for your project. **Sound Wave** assets are representations of audio files and are one of the basic building blocks required to work with many of those features. You can create Sound Waves by importing audio files into the Unreal Editor.

### Supported Audio Files

|  |  |
| --- | --- |
| **Format** | `.wav`, `.ogg`, `.flac`, `.aif`, `.opus`, `.mp3` |
| **Bit Depth** | 16, 24 |
| **Sample Rate** | Any |
| **Speaker Channels** | Mono, Stereo, 4.0, 5.1, 7.1 |

All imported audio files are converted to 16-bit `.wav` files internally. As such, exporting (by right-clicking a Sound Wave and selecting **Asset Actions > Export...**) will produce the converted file and not the originally imported file. Additionally, 24-bit files are not dithered during conversion so importing 16-bit files is recommended.

### How to Import an Audio File

1. In the Content Browser, click the **Import** button.

   ![Content Browser Import Button](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/83637333-8e3c-4ebe-ae0e-cb713bd7988e/content_browser_import.png)
2. Select the file you wish to import using the **File Explorer**.
3. Find the newly created **Sound Wave** asset.

   ![Content Browser Imported Sound Wave](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/53d607aa-9bd6-4c30-a143-cd74dba28ba5/content_browser_imported.png)
4. To preview the Sound Wave, hover over it until a **Play/Stop** toggle button appears and click it.

   ![Play Sound Wave](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5b927ad9-00e7-4f21-9bde-1a84141bb60b/play_sound_wave.png)
   ![Stop Sound Wave](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f5681f2c-1228-4d14-923f-e03ac4a405a1/stop_sound_wave.png)
5. Double-click the Sound Wave to open the **Details** panel. You can view and edit the properties of your asset here.

   ![Sound Wave Details Panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/940e1c34-3aa0-4345-9723-9d6e95b0bb29/details_panel.png)

You can also import audio files by dragging them from Windows Explorer directly into the **Content Browser**.



Unreal Engine also supports importing first-order ambisonic files. See [Native Soundfield Ambisonics Rendering](/documentation/en-us/unreal-engine/native-soundfield-ambisonics-rendering-in-unreal-engine) for information on importing and using ambisonic assets.

### Compression

All Sound Waves are compressed with the **Default Audio Compression Type** specified in the **Project Settings**. You can also set the codec and quality level for each platform and Sound Wave.

| Codec | Type | Ratio | Description |
| --- | --- | --- | --- |
| **Bink Audio** | Lossy | Up to 10:1 | (Default) A perceptual-based codec that supports all features across all platforms. Low memory usage and comparable CPU usage to **ADPCM**. |
| **ADPCM** | Lossy | Up to 4:1 | A time-domain codec with fixed-sized quality and is relatively cheap to decode. |
| **PCM** | Lossless | Uncompressed | Uses uncompressed audio that results in higher memory usage as streamed chunks contain less audio per chunk but provides extremely cheap decoding and support for all features. |
| **Platform Specific** | - | - | Encodes the asset in a platform-specific format. Seeking is not supported. |

* [audio](https://dev.epicgames.com/community/search?query=audio)
* [sound sources](https://dev.epicgames.com/community/search?query=sound%20sources)
* [sound waves](https://dev.epicgames.com/community/search?query=sound%20waves)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Supported Audio Files](/documentation/en-us/unreal-engine/importing-audio-files?application_version=5.7#supportedaudiofiles)
* [How to Import an Audio File](/documentation/en-us/unreal-engine/importing-audio-files?application_version=5.7#howtoimportanaudiofile)
* [Compression](/documentation/en-us/unreal-engine/importing-audio-files?application_version=5.7#compression)
