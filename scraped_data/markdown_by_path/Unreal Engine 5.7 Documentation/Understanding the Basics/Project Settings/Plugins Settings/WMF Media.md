<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/wmf-media-settings-in-the-unreal-engine-project-settings?application_version=5.7 -->

# WMF Media

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
7. [Plugins Settings](/documentation/en-us/unreal-engine/plugins-section-of-the-unreal-engine-project-settings "Plugins Settings")
8. WMF Media

# WMF Media

Reference for the WMF Media section of the Unreal Engine Project Settings.

![WMF Media](https://dev.epicgames.com/community/api/documentation/image/06d255a6-3bc5-4545-a9e6-10c26a8011cf?resizing_type=fill&width=1920&height=335)

 On this page

## WMF Media

### Media

| **Setting** | **Description** |
| --- | --- |
| **Allow Non Standard Codecs** | Defines whether to allow the loading of media that uses non-standard codecs (default = off).  By default, the player will attempt to detect audio and video codecs that are not supported by the operating system out of the box, but may require the user to install additional codec packs.  Enable this option to skip this check and allow the usage of non-standard codecs. |
| **Low Latency** | Enable low latency processing in the Windows media pipeline (default = off).  When this setting is enabled, the media data is generated with the lowest possible delay.  This might be desirable for certain real-time applications, but it can negatively affect audio and video quality.  This setting is only supported on Windows 8 or newer. |
| **Hardware Accelerated Video Decoding (Experimental)** | Use hardware accelerated video acceleration (GPU) when possible, otherwise fall back to software implementation (CPU). Windows and DX11 only. |

### Debug

| **Setting** | **Description** |
| --- | --- |
| **Native Audio Out** | Play audio tracks via the operating system's native sound mixer (default = off). |

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [basics](https://dev.epicgames.com/community/search?query=basics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [WMF Media](/documentation/en-us/unreal-engine/wmf-media-settings-in-the-unreal-engine-project-settings?application_version=5.7#wmfmedia)
* [Media](/documentation/en-us/unreal-engine/wmf-media-settings-in-the-unreal-engine-project-settings?application_version=5.7#media)
* [Debug](/documentation/en-us/unreal-engine/wmf-media-settings-in-the-unreal-engine-project-settings?application_version=5.7#debug)
