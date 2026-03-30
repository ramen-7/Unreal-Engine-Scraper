<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/macos-development-requirements-for-unreal-engine?application_version=5.7 -->

# MacOS Development Requirements

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
5. [Sharing and Releasing Projects](/documentation/en-us/unreal-engine/sharing-and-releasing-projects-for-unreal-engine "Sharing and Releasing Projects")
6. [MacOS](/documentation/en-us/unreal-engine/developing-macos-projects-in-unreal-engine "MacOS")
7. MacOS Development Requirements

# MacOS Development Requirements

Development requirements for macOS, including compatible hardware, software, and SDK information.

![MacOS Development Requirements](https://dev.epicgames.com/community/api/documentation/image/6c92375d-13d9-41ef-ab70-5dac4f6e5d64?resizing_type=fill&width=1920&height=335)

 On this page

This page contains the software development kit (SDK) requirements needed to develop Unreal Engine (UE) projects for macOS.

## Recommended Hardware

|  |  |
| --- | --- |
| **Recommended Operating System** | Latest macOS Sonoma 14 |
| **Recommended Processor** | Apple Silicon M3 |
| **Minimum Processor** | M1 or M2 depending on rendering features |
| **Recommended Memory** | 32 GB or more |
| **Minimum Memory** | 16 GB |
| **Video Card** | Metal 1.2 Compatible Graphics Card |

## Minimum Software Requirements

Minimum requirements for running the engine or editor are listed below.

| Running the Engine |  |
| --- | --- |
| **Minimum Operating System** | Sonoma 14.0 |

The requirements for programmers developing with the engine are listed below.

| Developing with the Engine |  |
| --- | --- |
| **Recommended Xcode Version** | 15.4 or newer |
| **Minimum Xcode Version** | Xcode 15.2 |

Although Xcode is preferred for macOS development, Unreal Engine also supports VS Code and Rider.

## Requirements for UE5 Rendering Features

| UE5 Feature | System Requirements |
| --- | --- |
| **Lumen Global Illumination and Reflections with Software Ray Tracing** | Apple computers with an Intel and AMD Based GPU and/or Apple Silicon M1+.  To learn more see, [Lumen Technical Details](building-virtual-worlds/lighting-and-shadows/global-illumination/lumen/TechOverview). |
| **Lumen Global Illumination and Reflections with Hardware Ray Tracing and MegaLights** | Not currently supported.  To learn more see, [Lumen Technical Details](building-virtual-worlds/lighting-and-shadows/global-illumination/lumen/TechOverview). |
| **Nanite Virtualized Geometry and Virtual Shadow Maps** | Apple Silicon M2+ (beta support).  To learn more see, [Nanite Virtualized Geometry](designing-visuals-rendering-and-graphics/rendering-optimization/nanite). |
| **Temporal Super Resolution** | Apple computers with an Intel and AMD Based GPU and/or Apple Silicon M1+.  To learn more see, [Temporal Super Resolution](https://dev.epicgames.com/documentation/en-us/unreal-engine/temporal-super-resolution-in-unreal-engine).  There are some runtime costs to be aware of. To learn more see the [Anti-aliasing Performance](https://www.unrealengine.com/en-US/tech-blog/unreal-engine-5-2-brings-native-support-for-apple-silicon-and-other-developments-for-macos) section of our tech blog. |

## Version History

| UE Version | Minimum macOS Version | Recommended macOS Version | Minimum Xcode Version | Recommended Xcode Version | Notes |
| --- | --- | --- | --- | --- | --- |
| 5.6 | Sonoma 14.0 | Latest macOS 14 Sonoma | Xcode 15.2 | 15.4 or newer |  |
| 5.5 | Ventura 13.5 | Latest macOS 13 Ventura | Xcode 15.2 | 15.4 or newer |  |
| 5.4 | macOS 13 Ventura | Latest macOS 13 Ventura | Xcode 14.1 | Latest Xcode 14 |  |
| 5.2 - 5.3 | macOS 12.5 Monterey | Latest macOS 13 Ventura | Xcode 14.1 | Latest Xcode 14 | Unreal Editor is distributed with universal binaries for macOS through the Epic Games Launcher. Code plugins are required to use universal binaries to be considered compatible with macOS.  MacOS requirements are now updated to maintain consistency with iOS requirements. |
| 5.1 | macOS 12 Monterey | Latest macOS 13 Ventura | Xcode 13.4.1 | Latest Xcode 14 | Native Apple Silicon support is available for macOS targets for both editor and project builds. Editor support for Apple Silicon is experimental. Some third-party SDKs and plugins do not yet contain ARM64 slices and may have compatibility issues. |
| 5.0 | macOS Catalina 10.15.7 | Latest macOS Monterey | Xcode 12.4 | Latest Xcode 13 | Added preliminary support for native Apple Silicon for macOS targets. Some SDKs do not yet contain ARM64 slices (e.g. Steam, Vivox). |

* [specifications](https://dev.epicgames.com/community/search?query=specifications)
* [macos](https://dev.epicgames.com/community/search?query=macos)
* [compatibility](https://dev.epicgames.com/community/search?query=compatibility)
* [sdk](https://dev.epicgames.com/community/search?query=sdk)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Recommended Hardware](/documentation/en-us/unreal-engine/macos-development-requirements-for-unreal-engine?application_version=5.7#recommended-hardware)
* [Minimum Software Requirements](/documentation/en-us/unreal-engine/macos-development-requirements-for-unreal-engine?application_version=5.7#minimum-software-requirements)
* [Requirements for UE5 Rendering Features](/documentation/en-us/unreal-engine/macos-development-requirements-for-unreal-engine?application_version=5.7#requirements-for-ue5-rendering-features)
* [Version History](/documentation/en-us/unreal-engine/macos-development-requirements-for-unreal-engine?application_version=5.7#version-history)
