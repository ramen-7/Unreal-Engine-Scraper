<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/streaming-settings-of-the-unreal-engine-project-settings?application_version=5.7 -->

# Streaming

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
8. Streaming

# Streaming

Reference for the Streaming Settings section in the Unreal Engine Project Settings.

On this page

## Streaming

### Package Streaming

| **Section** | **Description** |
| --- | --- |
| **Async Loading Thread Enabled** | Enables separate thread for package streaming.  Changing this setting requires restarting Unreal Engine. |
| **Warn If Time Limit Has Been Exceeded** | Enables log warning if time limit for time-sliced package streaming has been exceeded. |
| **Time Limit Exceeded Warning Multiplier** | Multiplier for the time limit before logging warning messages. |
| **Minimum Time Limit For Time Limit Exceeded Warning** | Minimum time before logging warning messages when loading a package. |
| **Minimum Bulk Data Size For Async Loading (deprecated)** | Minimum time that triggers the time limit exceeded warning when elapsed. This setting has been deprecated and should not be used |

### Level Streaming

| **Section** | **Description** |
| --- | --- |
| **Use Background Level Streaming** | Defines whether to allow background level streaming. |
| **Async Loading Use Full Time Limit** | Defines whether to use the entire time limit even if blocked on I/O. |
| **Async Loading Time Limit** | Maximum amount of time to spend doing asynchronous loading, in miliseconds per frame. |
| **Priority Async Loading Extra Time** | Additional time to spend doing asynchronous loading during a high-priority load. |
| **Actor Initialization Update Time Limit** | Maximum allowed time to spend for actor registration steps during Level streaming, in miliseconds per frame.  Streaming a Level can take a long time. Using this value, you can control how much time per frame Unreal Engine spends doing Actor initialization. |
| **Priority Actor Initialization Update Extra Time** | Additional time to spend on Actor registration steps during a high-priority load or if you are in a seamless travel, in miliseconds per frame.  High-priority loading is driven by the replicated flag `bHighPriorityLoading` in the **World Settings** panel. |
| **Components Registration Granularity** | Batching granularity used to register Actor components during Level streaming.  This number controls how many components are updated or registered before the engine checks again the time limit (per frame) allowed for adding Levels to the world. |
| **Added Primitive Granularity** | Batching granularity used to add primitives to the scene in parallel when registering Actor components during Level streaming.  If this option is set to 0, there is no parallel registration. |
| **Component Unregister Update Time Limit** | Maximum allowed time to spend while unregistering components during Level streaming, in miliseconds per frame.  Similarly to streaming in a Level into the world, streaming out a Level can also take some time.  Use this to control how much time per frame the engine spends removing Levels from the world. |
| **Components Unregistration Granularity** | Batching granularity used to unregister actor components during Level streaming.  This number controls how many components are unregistered before the engine checks again the time limit (per frame) allowed for removing Levels from the world. |

### General

| **Section** | **Description** |
| --- | --- |
| **Flush Streaming when Exiting the Application** | If enabled, streaming will be flushed when exiting the application, otherwise it will be canceled. |

### Deprecated Settings

| **Section** | **Description** |
| --- | --- |
| **Use Event-Driven Loader (Disabling Not Recommended)** | Enables the event-driven loader (EDL) in cooked builds. This setting is enabled by default.  Disabling this option will result in using a deprecated loading path. For this reason, disabling EDL is not recommended. |

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [basics](https://dev.epicgames.com/community/search?query=basics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Streaming](/documentation/en-us/unreal-engine/streaming-settings-of-the-unreal-engine-project-settings?application_version=5.7#streaming)
* [Package Streaming](/documentation/en-us/unreal-engine/streaming-settings-of-the-unreal-engine-project-settings?application_version=5.7#packagestreaming)
* [Level Streaming](/documentation/en-us/unreal-engine/streaming-settings-of-the-unreal-engine-project-settings?application_version=5.7#levelstreaming)
* [General](/documentation/en-us/unreal-engine/streaming-settings-of-the-unreal-engine-project-settings?application_version=5.7#general)
* [Deprecated Settings](/documentation/en-us/unreal-engine/streaming-settings-of-the-unreal-engine-project-settings?application_version=5.7#deprecatedsettings)
