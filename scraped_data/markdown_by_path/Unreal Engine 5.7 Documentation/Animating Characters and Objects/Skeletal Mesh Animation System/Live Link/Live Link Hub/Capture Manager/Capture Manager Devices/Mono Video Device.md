<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/mono-video-device?application_version=5.7 -->

# Mono Video Device

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
11. Mono Video Device

# Mono Video Device

An overview of the Mono Video device provided by Capture Manager.

![Mono Video Device](https://dev.epicgames.com/community/api/documentation/image/ce049c46-12ef-49d7-b0b8-968830a21a39?resizing_type=fill&width=1920&height=335)

 On this page

The **Mono Video** device enables the ingest of individual video files as mono takes. If the video contains an audio track it will also be extracted during ingest.

[![Capture Manager Device Details](https://dev.epicgames.com/community/api/documentation/image/61ca965e-501c-4439-856e-5d3c73de3d6c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/61ca965e-501c-4439-856e-5d3c73de3d6c?resizing_type=fit)

* **Display Name**: The name of the device as it will appear in the **Devices** list.
* **Take Directory**: The path to the root folder containing video files. This folder can contain subfolders.
* **Video Discovery Expression**: [Tokens](https://dev.epicgames.com/documentation/en-us/unreal-engine/mono-video-device#discovery-expression-tokens) that can be extracted from the folder and file name to identify the take.

A visual example of the content expected to be found by the **Mono Video** device in the **Take Directory** is shown below:

Console Output

```
|  |  |
| --- | --- |
|  | +-- takes |
|  | |   +-- take_1.mov |
|  | |   \-- take_2.mov |
|  | | |
|  | \-- take_3.mov |
```

+-- takes
| +-- take\_1.mov
| \-- take\_2.mov
|
\-- take\_3.mov

Copy full snippet(5 lines long)

## Discovery Expression Tokens

The **Video Discovery Expression** is used to define the naming convention for video files in your takes. The available tokens are:

|  |  |
| --- | --- |
| `<Slate>` | The slate name. |
| **`<Name>`** | The identifier for the camera. |
| **`<Take>`** | The take number. |
| **`<Any>`** | Any valid string. |
| `<Auto>` | Used without any other tokens to automatically identify takes based on the directory structure. |

Tokens can be separated using the following delimiters: `_-.\`

When not using the `<Auto>` token, both `<Slate>` and `<Name>` must be present.

For example, consider the following take: `MyTakeFolder/MySlate_MyName_SomeString-005.mov`. If the Video Discovery Expression is set to the default value of `<Auto>`, the following tokens will be identified:

|  |  |
| --- | --- |
| **Slate** | `MySlate_MyName_SomeString` |
| **Name** | `video` (the default value) |
| **Take** | `1` (the default value) |

However, if the Video Discovery Expression is set to `<Slate>_<Name>_<Any>-<Take>` the following tokens will be extracted instead:

|  |  |
| --- | --- |
| **Slate** | `MySlate` |
| **Name** | `MyName` |
| **Take** | `5` |
| **Any** | `SomeString` |

In both cases, the extension `.mov` is ignored.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Discovery Expression Tokens](/documentation/en-us/unreal-engine/mono-video-device?application_version=5.7#discovery-expression-tokens)
