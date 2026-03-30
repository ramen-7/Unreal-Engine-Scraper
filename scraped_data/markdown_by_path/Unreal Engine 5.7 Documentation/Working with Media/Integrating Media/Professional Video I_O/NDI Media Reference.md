<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/ndi-media-reference?application_version=5.7 -->

# NDI Media Reference

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
7. [Professional Video I/O](/documentation/en-us/unreal-engine/professional-video-io-in-unreal-engine "Professional Video I/O")
8. NDI Media Reference

# NDI Media Reference

Describes the options and settings exposed by the NDI Media Framework components.

![NDI Media Reference](https://dev.epicgames.com/community/api/documentation/image/17cd00da-877c-4732-86b3-fca7dd948097?resizing_type=fill&width=1920&height=335)

 On this page

This page describes the options and settings exposed on NDI Media Framework assets. Using NDI Media Source and Media Output assets requires enabling the NDI Media plugin, and you also need an NDI source. See the [NDI documentation](https://ndi.video/) for more information.

## NDI Media Source

Each NDI Media Source asset you create exposes the following Configuration dropdown menu settings and Details panel settings.

### NDI Media Source Configuration Dropdown Settings

The settings described here are available in the Configuration dropdown menu accessible at the top of the NDI Media Source Details panel. By default, only the Device is configurable, and all the other settings are determined automatically by the NDI stream.

Do not disable the **Auto** checkbox, as the settings shown are intended for use with capture cards and are nonfunctional class defaults for NDI that do not represent actual stream settings.

[![NDI Configuration dropdown menu](https://dev.epicgames.com/community/api/documentation/image/db2307c3-160c-401a-8e86-71c32694f268?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/db2307c3-160c-401a-8e86-71c32694f268?resizing_type=fit)

| Setting | Description |
| --- | --- |
| **Device** | Sets the NDI virtual device that this Media Source uses to bring video into Unreal Engine. If you have multiple NDI streams available on your computer, you can choose which one to use here. |

### NID Media Source Details Panel Settings

The settings in the Details panel shown under **NDI > Configuration** are always greyed-out, as they are set through the Configuration dropdown menu. For NDI, only the device name is used. The other settings show default values that are nonfunctional for NDI.

The Media Source Details panel settings are shared for NDI and all capture cards, so some of the settings are nonfunctional. Check carefully what settings are appropriate for your NDI setup.

[![NDI Media Source asset Detail panel](https://dev.epicgames.com/community/api/documentation/image/bc089138-85d5-463a-846f-39396921bb2c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bc089138-85d5-463a-846f-39396921bb2c?resizing_type=fit)

| Setting | Description |
| --- | --- |
| NDI |  |
| **Configuration** | Provides access to the Configuration dropdown, and shows a summary of the settings. |
| Configuration - Media Connection |  |
| --- | --- |
| **Device** | Shows the NDI source that this Media Source will use to bring media content into Unreal Engine. Includes subfields for the Device Name and the Device Identifier. Read-only. |
| **Protocol** | Nonfunctional for NDI |
| **Transport Type** | Nonfunctional for NDI |
| **Quad Transport Type** | Nonfunctional for NDI |
| **Port Identifier** | Nonfunctional for NDI |
| Configuration - Media Mode |  |
| --- | --- |
| **Frame Rate** | Nonfunctional for NDI |
| **Resolution** | Nonfunctional for NDI |
| **Standard** | Nonfunctional for NDI |
| **Device Mode Identifier** | Nonfunctional for NDI |
| **Bandwidth** | Determines the bandwidth mode used for this connection to the NDI source. Options are:   * Metadata Only * Audio Only * Lowest * Highest (default) |
| **Sync Timecode to Source** | When enabled, the timecode is synced to the source timecode.  When disabled, the timecode is synced to UE's timecode. |
| Video |  |
| --- | --- |
| **Capture Video** | Determines whether Unreal Engine captures video from the NDI source. |
| **Deinterlacer** | You can select how an incoming interlaced stream should be processed. Options are:   * None * Blend Deinterlacer * Bob Deinterlacer (default) * Discard Deinterlacer |
| **Interlace Field Order** | The order in which interlace fields should be copied. Options are:   * Top Field First * Bottom Field First |
| **Override Source Encoding** | Enable this field to override the source encoding. Select the override encoding from the dropdown menu. |
| **Override Source Color Space** | Enable this field to override the source color space. Select the override color space from the dropdown menu. |
| Video - Color Conversion Settings |  |
| --- | --- |
| **Configuration Source** | Use this property to define your OCIO configuration. See the  [OCIO documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/color-management-with-opencolorio-in-unreal-engine)  for more information. |
| **Transform Source** | Use this property to define your OCIO transform source. See the  [OCIO documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/color-management-with-opencolorio-in-unreal-engine)  for more information. |
| **Transform Destination** | Use this property to define your OCIO transform destination. See the  [OCIO documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/color-management-with-opencolorio-in-unreal-engine)  for more information. |
| Video - Advanced |  |
| --- | --- |
| **Max Num Video Frame Buffer** | Sets the maximum number of frames of video data Unreal Engine stores in memory at any given time. If the input video jumps or hitches, you can try raising this value. |
| Audio |  |
| --- | --- |
| **Capture Audio** | Determines whether Unreal Engine captures audio from the NDI source. |
| Audio - Advanced |  |
| --- | --- |
| **Max Num Audio Frame Buffer** | Sets the maximum number of frames of audio data Unreal Engine stores in memory at any given time. If the input video jumps or hitches, you can try raising this value. |
| Ancillary |  |
| --- | --- |
| **Capture Ancillary** | Determines whether Unreal Engine captures ancillary metadata that accompanies the video signal. |
| Ancillary - Advanced |  |
| --- | --- |
| **Max Num Ancillary Frame Buffer** | Sets the maximum number of frames of ancillary data Unreal Engine stores in memory at any given time. If the input video jumps or hitches, you can try raising this value. |
| Synchronization |  |
| --- | --- |
| **Time Synchronization** | When enabled, synchronizes media based on the engine's timecode. A prerequisite for the Timecode Sample Evaluation Type and Frame Delay settings. |
| **Frame Delay** | This setting depends on whether time synchronization is enabled or not. It is used to find the right frame based on the engine’s timecode and is calculated based on the player/media source frame rate.  For example: If the Player is at frame #2 and you set the value of Frame Delay at 1 Frame, the Media Player will display an older frame (2 - Frame Delay = 1) on the screen, despite frame #2 also being available. |
| **Time Delay** | This setting is used when you aren't using time synchronization, similarly to Frame Delay it is taken into account when the engine selects the frame to display. |
| Synchronization - Advanced |  |
| --- | --- |
| **Just in Time Rendering** | Enabling this option defers the processing of the media source’s pixels to the last possible point in the current frame pipeline, which provides more time for pixels to arrive from external sources and be rendered in the current frame on the playback device. |
| **Framelock** | This option does not function for NDI sources. |
| Debug |  |
| --- | --- |
| **Sample Evaluation Type** | Latest - Displays the received sample as soon as possible. This does not use any of the time-based synchronization techniques and shows the latest available frame.  Platform Time - The displayed sample is synchronized based on the platform time.  Timecode - Synchronize based on the timecode. Requires a timecode provider set either in the Media Profile or the Project settings. |
| **Log Drop Frame** | When enabled, Unreal Engine prints a message to its output log every time it detects a dropped frame in the input feed. |
| **Burn Frame Timecode** | When enabled, the engine embeds the timecode of each frame into the captured video. You can use this to check that the timecode for each frame of input matches the values you're expecting. See  [Timecode Texel Encoding](https://dev.epicgames.com/documentation/en-us/unreal-engine/timecode-and-genlock-in-unreal-engine#timecode-texel-encoding) . |

## NDI Media Output

Each NDI Media Output asset you create exposes the following Details panel settings.

### NDI Media Output Details Panel Settings

The Media Source Details panel settings are shared for NDI and all capture cards, so some of the settings will be nonfunctional. Check carefully what settings are appropriate for your NDI source.

[![NDI Media Output asset Details panel](https://dev.epicgames.com/community/api/documentation/image/85feb44b-9a25-4540-ae06-054165305907?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/85feb44b-9a25-4540-ae06-054165305907?resizing_type=fit)

| Setting | Description |
| --- | --- |
| Media |  |
| **Source Name** | Describes a name for the output stream, to differentiate it from other output streams on the current machine. |
| **Group Name** | Defines the group this source is part of. If left empty, the source is ungrouped, and by default is shown in the Public group in NDI Access Manager and NDI Bridge. |
| **Output Type** | Determines the type of output. Options are:   * Fill * Fill and Key |
| **Invert Key Output** | When enabled, inverts the key output when saving images. |
| **Desired Size X/Y** | When enabled, provides a way to specify the X and Y dimensions of the output NDI stream. |
| **Desired Pixel Format** | When enabled, provides a way to specify the pixel format to use instead of the default back buffer. |
| **Frame Rate** | Defines the desired rate of frames per second for video sent over NDI. |
| Audio |  |
| --- | --- |
| **Output Audio** | Enable to send the engine’s audio alongside the video signal on the output. |
| **Audio Buffer Size** | Determines the size of the buffer holding rendered audio samples. A bigger buffer produces a more stable output but introduces more delay. |
| **Num Output Audio Channels** | Determines how many audio channels are output to the NDI source. Must be greater than the number of audio channels used in the engine. |
| **Audio Sample Rate** | The number of audio samples per second sent to the NDI source. The value must match the engine’s audio sample rate. |
| **Send Audio Only if Receivers Connected** | When enabled, audio is not converted and sent if there are no connected receivers.  When disabled, audio is converted and sent regardless of whether there are connected receivers or not. |
| Synchronization |  |
| --- | --- |
| **Wait for Sync Event** | When enabled, it locks the render thread to the NDI frame rate.  This setting functions very differently from the similarly-named setting for capture cards like AJA and Blackmagic. Don't confuse them. |
| Output - Advanced |  |
| --- | --- |
| **Number of Texture Buffers** | Sets the number of buffers used to transfer each frame image from the GPU to main thread memory. Lower values are more likely to cause a bottleneck on the GPU side as it waits for each transfer to complete; larger numbers are more likely to increase latency. |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [NDI Media Source](/documentation/en-us/unreal-engine/ndi-media-reference?application_version=5.7#ndimediasource)
* [NDI Media Source Configuration Dropdown Settings](/documentation/en-us/unreal-engine/ndi-media-reference?application_version=5.7#ndimediasourceconfigurationdropdownsettings)
* [NID Media Source Details Panel Settings](/documentation/en-us/unreal-engine/ndi-media-reference?application_version=5.7#nidmediasourcedetailspanelsettings)
* [NDI Media Output](/documentation/en-us/unreal-engine/ndi-media-reference?application_version=5.7#ndimediaoutput)
* [NDI Media Output Details Panel Settings](/documentation/en-us/unreal-engine/ndi-media-reference?application_version=5.7#ndimediaoutputdetailspanelsettings)
