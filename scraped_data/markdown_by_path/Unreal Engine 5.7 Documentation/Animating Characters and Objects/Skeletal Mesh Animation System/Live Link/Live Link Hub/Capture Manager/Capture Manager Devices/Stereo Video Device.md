<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/stereo-video-device?application_version=5.7 -->

# Stereo Video Device

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
6. [Skeletal Mesh Animation System](/documentation/en-us/unreal-engine/skeletal-mesh-animation-system-in-unreal-engine "Skeletal Mesh Animation System")
7. [Live Link](/documentation/en-us/unreal-engine/live-link-in-unreal-engine "Live Link")
8. [Live Link Hub](/documentation/en-us/unreal-engine/live-link-hub-in-unreal-engine "Live Link Hub")
9. [Capture Manager](/documentation/en-us/unreal-engine/capture-manager "Capture Manager")
10. [Capture Manager Devices](/documentation/en-us/unreal-engine/capture-manager-devices "Capture Manager Devices")
11. Stereo Video Device

# Stereo Video Device

An overview of the Stereo Video device provided by Capture Manager.

![Stereo Video Device](https://dev.epicgames.com/community/api/documentation/image/b88ce52d-fc00-46e6-9825-a0fca905c345?resizing_type=fill&width=1920&height=335)

 On this page

The **Stereo Video** device enables the ingest of pairs of videos as stereo takes. An audio file (`.wav`) may also be provided alongside the video.

[![Device Details Stereo](https://dev.epicgames.com/community/api/documentation/image/ce6dd3b6-75d8-4c51-8d37-a3e4c3261ce8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ce6dd3b6-75d8-4c51-8d37-a3e4c3261ce8?resizing_type=fit)

* **Display Name**: The name of the device as it will appear in the **Devices** list.
* **Take Directory**: The path to the root folder containing pairs of video files. This folder can contain subfolders.
* **Video Discovery Expression**: [Tokens](https://dev.epicgames.com/documentation/en-us/unreal-engine/stereo-video-device?application_version=5.6#discovery-expression-tokens) that can be extracted from the folder and file name of the video to identify the take.
* **Audio Discovery Expression**: [Tokens](https://dev.epicgames.com/documentation/en-us/unreal-engine/stereo-video-device?application_version=5.6#discovery-expression-tokens) that can be extracted from the folder and file name of the audio file to identify the take.

A visual example of the content expected to be found by the Stereo Video device in the **Take Directory** is shown below:

Console Output

```
+-- take_1
|   +-- top.mov
|   \-- bot.mov
|
+-- take_2
|   +-- audio.wav
|   |-- top.mov
|   \-- bot.mov
|
+-- take_3
```

Expand code  Copy full snippet(24 lines long)

## Discovery Expression Tokens

The **Video Discovery Expression** and **Audio Discovery Expression** are used to define the naming convention for video and audio files in your takes. The available tokens are:

|  |  |
| --- | --- |
| `<Slate>` | The slate name. |
| `<Name>` | The identifier for the camera in the stereo pair. |
| `<Take>` | The take number. |
| `<Any>` | Any valid string. |
| `<Auto>` | Used without any other tokens to automatically identify takes based on the directory structure. |

Tokens can be separated using the following delimiters: `_-.\`

When not using the `<Auto>` token, both `<Slate>` and `<Name>` must be present.

For example, consider the following take: `MyTakeFolder/MySlate_MyName_SomeString-005.mov`. If the Video Discovery Expression is set to the default value of `<Auto>`, the following tokens will be identified:

|  |  |
| --- | --- |
| **Slate** | `MyTakeFolder` |
| Name | `MySlate_MyName_SomeString-005` |
| **Take** | `1`(the default value) |

However, if the Video Discovery Expression is set to `<Slate>_<Name>_<Any>-<Take>` the following tokens will be extracted instead:

|  |  |
| --- | --- |
| **Slate** | `MySlate` |
| **Name** | `MyName` |
| Take | `5` |
| **Any** | `SomeString` |

In both cases, the extension `.mov` is ignored.

The same applies for audio files, where any audio extension (such as `.wav`) is ignored.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Discovery Expression Tokens](/documentation/en-us/unreal-engine/stereo-video-device?application_version=5.7#discovery-expression-tokens)
