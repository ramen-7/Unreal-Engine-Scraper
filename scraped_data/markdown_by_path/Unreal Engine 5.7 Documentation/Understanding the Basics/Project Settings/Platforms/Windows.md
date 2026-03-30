<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/windows-settings-in-the-unreal-engine-project-settings?application_version=5.7 -->

# Windows

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
7. [Platforms](/documentation/en-us/unreal-engine/platforms-section-of-the-unreal-engine-project-settings "Platforms")
8. Windows

# Windows

Reference for the Windows section of the Unreal Engine Project Settings.

![Windows](https://dev.epicgames.com/community/api/documentation/image/d539543e-c43d-43b2-b24c-df20b19bd621?resizing_type=fill&width=1920&height=335)

 On this page

## Windows

### Targeted RHIs

| **Setting** | **Description** |
| --- | --- |
| **Default RHI** | Here, you can select which Rendering Hardware Interface (RHI) to use.  Make sure the RHI you select is also selected as a Targeted RHI.  Changing this setting requires restarting the editor.  You can choose from the following options:   * **Default** * **DirectX 11** * **DirectX 12** * **Vulkan** |
| **DirectX 11 & 12 (SM5)** | Enable this to use DirectX 11 and DirectX 12 as targeted RHIs. |
| **DirectX 12 (SM6, Experimental)** | Enable this to use DirectX 12 as the targeted RHI. |
| **Vulkan (SM5)** | Enable this to use Vulkan as the targeted RHI. |
| **DirectX Mobile Emulation** | Enable this to use DirectX Mobile Emulation as the targeted RHI. |

### Toolchain

| **Setting** | **Description** |
| --- | --- |
| **Compiler Version** | The compiler version to use for this project.  May be different from the chosen IDE.  You can choose from the following options:   * **Default** * **Visual Studio 2015 (deprecated)** * **Visual Studio 2017** * **Visual Studio 2019** * **Visual Studio 2022** |

### Splash

| **Setting** | **Description** |
| --- | --- |
| **Editor Splash** | Editor Splash. |
| **Game Splash** | Game Splash. |

### Icon

| **Setting** | **Description** |
| --- | --- |
| **Game Icon** | Game Icon. |

### Audio

| **Setting** | **Description** |
| --- | --- |
| **Audio Mixer Sample Rate** | Sample rate to run the audio mixer with. |
| **Callback Buffer Size** | The amount of audio to compute each callback block.  Lower values decrease latency but may increase CPU cost. |
| **Number of Buffers To Enqueue** | The number of buffers to keep enqueued.  More buffers increase latency but can compensate for variable compute availability in audio callbacks on some platforms. |
| **Max Channels** | The maximum number of channels (voices) to limit for this platform.  If you specify Max Channels both here and in your global audio quality settings, your application will use the smaller of the two values.  If this is set to 0, Unreal Engine will use all the channels available. |
| **Number of Source Workers** | The number of workers to use to compute source audio.  Will only use up to max number of sources (Max Channels value).  Will evenly divide sources to each source worker. |
| **Compression Overrides** | See the [Compression Overrides](/documentation/en-us/unreal-engine/windows-settings-in-the-unreal-engine-project-settings#compressionoverrides) table below. |
| **Cook Overrides** | See the [Cook Overrides](/documentation/en-us/unreal-engine/windows-settings-in-the-unreal-engine-project-settings#cookoverrides) table below. |
| **Spatialization Plugin** | Defines which of the currently enabled spatialization plugins to use.  If your desired spatialization isn't found in the dropdown menu, make sure it's enabled in the **Plugins** window (main menu: **Edit > Plugins**).  You can choose from the following options:   * **Built-In Spatialization** * **Resonance Audio** * **Other** |
| **Reverb Plugin** | Defines which of the currently enabled reverb plugins to use.  If your desired reverb plugin isn't found in the dropdown menu, make sure it's enabled in the **Plugins** window (main menu: **Edit > Plugins**).  You can choose from the following options:   * **Built-In Reverb** * **Resonance Audio** * **Other** |
| **Occlusion Plugin** | Defines which of the currently enabled occlusion plugins to use.  If your desired occlusion plugin isn't found in the dropdown menu, make sure it's enabled in the **Plugins** window (main menu: **Edit > Plugins**).  You can choose from the following options:   * **Built-In Occlusion** * **Other** |
| **Sound Cue Cook Quality** | Quality level to cook SoundCues at (if set, all other levels will be stripped by the cooker). |

#### Compression Overrides

| **Setting** | **Description** |
| --- | --- |
| **Override Compression Times** | If enabled, overrides the Sound Group on each Sound Wave, and instead uses the Duration Threshold value to determine whether a sound should be fully decompressed during initial loading. |
| **Duration Threshold** | When Override Compression Times is set to true, any sound under this threshold (in seconds) will be fully decompressed on load.  Otherwise, the first chunk of this sound is cached at load and the rest is decompressed in real time.  If set to 0, will default to the Sound Group on the relevant Sound Wave. |
| **Maximum Branches on Random SoundCue Nodes** | On this platform, any random nodes on Sound Cues will automatically only preload this number of branches and dispose of any others on load.  This can drastically reduce memory usage.  If set to 0, no branches are culled. |
| **Quality Index for Sound Cues** | On this platform, use the specified quality at this index to override the quality used for SoundCues. |

Return to the [Audio](/documentation/en-us/unreal-engine/windows-settings-in-the-unreal-engine-project-settings#audio) table.

#### Cook Overrides

| **Setting** | **Description** |
| --- | --- |
| **Resample for Device** | Enables audio resampling on this platform using the given Resampling Quality Sample Rates. |
| **Compression Quality Modifier** | Scales all compression qualities when cooking to this platform.  For example, 0.5 will halve all compression qualities, and 1.0 will leave them unchanged. |
| **Stream Caching** | See the [Stream Caching](/documentation/en-us/unreal-engine/windows-settings-in-the-unreal-engine-project-settings#streamcaching) table below. |
| **Resampling Quality** | See the [Resampling Quality](/documentation/en-us/unreal-engine/windows-settings-in-the-unreal-engine-project-settings#resamplingquality) table below. |

Return to the [Audio](/documentation/en-us/unreal-engine/windows-settings-in-the-unreal-engine-project-settings#audio) table.

##### Stream Caching

| **Setting** | **Description** |
| --- | --- |
| **Max Cache Size (KB)** | This determines the maximum amount of memory that should be used for the cache at any given time.  If set low (<= 8 MB), it lowers the size of individual chunks of audio during cooking. |
| **Max Chunk Size Override (KB)** | Overrides the default maximum chunk size used when chunking audio for stream caching (ignored if < 0). |

Return to the [Cook Overrides](/documentation/en-us/unreal-engine/windows-settings-in-the-unreal-engine-project-settings#cookoverrides) table.

##### Resampling Quality

| **Setting** | **Description** |
| --- | --- |
| **Max Sample Rate** | Resampling quality maximum sample rate. |
| **High Sample Rate** | Resampling quality high sample rate. |
| **Medium Sample Rate** | Resampling quality medium sample rate. |
| **Low Sample Rate** | Resampling quality low sample rate. |
| **Min Sample Rate** | Resampling quality minimum sample rate. |

Return to the [Cook Overrides](/documentation/en-us/unreal-engine/windows-settings-in-the-unreal-engine-project-settings#cookoverrides) table.

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [basics](https://dev.epicgames.com/community/search?query=basics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Windows](/documentation/en-us/unreal-engine/windows-settings-in-the-unreal-engine-project-settings?application_version=5.7#windows)
* [Targeted RHIs](/documentation/en-us/unreal-engine/windows-settings-in-the-unreal-engine-project-settings?application_version=5.7#targetedrhis)
* [Toolchain](/documentation/en-us/unreal-engine/windows-settings-in-the-unreal-engine-project-settings?application_version=5.7#toolchain)
* [Splash](/documentation/en-us/unreal-engine/windows-settings-in-the-unreal-engine-project-settings?application_version=5.7#splash)
* [Icon](/documentation/en-us/unreal-engine/windows-settings-in-the-unreal-engine-project-settings?application_version=5.7#icon)
* [Audio](/documentation/en-us/unreal-engine/windows-settings-in-the-unreal-engine-project-settings?application_version=5.7#audio)
* [Compression Overrides](/documentation/en-us/unreal-engine/windows-settings-in-the-unreal-engine-project-settings?application_version=5.7#compressionoverrides)
* [Cook Overrides](/documentation/en-us/unreal-engine/windows-settings-in-the-unreal-engine-project-settings?application_version=5.7#cookoverrides)
* [Stream Caching](/documentation/en-us/unreal-engine/windows-settings-in-the-unreal-engine-project-settings?application_version=5.7#streamcaching)
* [Resampling Quality](/documentation/en-us/unreal-engine/windows-settings-in-the-unreal-engine-project-settings?application_version=5.7#resamplingquality)
