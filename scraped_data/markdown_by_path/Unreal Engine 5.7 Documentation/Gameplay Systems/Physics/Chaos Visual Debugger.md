<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/chaos-visual-debugger-in-unreal-engine?application_version=5.7 -->

# Chaos Visual Debugger

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
5. [Gameplay Systems](/documentation/en-us/unreal-engine/gameplay-systems-in-unreal-engine "Gameplay Systems")
6. [Physics](/documentation/en-us/unreal-engine/physics-in-unreal-engine "Physics")
7. Chaos Visual Debugger

# Chaos Visual Debugger

Documentation for Chaos Visual Debugger in Unreal Engine.

![Chaos Visual Debugger](https://dev.epicgames.com/community/api/documentation/image/95242672-00d9-4b40-bd21-463462d3ce21?resizing_type=fill&width=1920&height=335)

 On this page

**Chaos Visual Debugger** (**CVD**) is an in-editor tool and standalone program that you can use to record [Chaos physics](https://dev.epicgames.com/documentation/en-us/unreal-engine/physics-in-unreal-engine) simulations and collect state data during runtime.

Using this tool and the data it provides, you can efficiently and collaboratively debug physics simulations for applications running on your machine, as well as from a remote machine, or a platform that’s connected to your machine.

[![](https://dev.epicgames.com/community/api/documentation/image/0eb5d67b-af49-4fc0-b007-e37781953d4b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0eb5d67b-af49-4fc0-b007-e37781953d4b?resizing_type=fit)

## What’s New in Chaos Visual Debugger 1.2

[![Chaos Visual Debugger](https://dev.epicgames.com/community/api/documentation/image/89184bfc-a1c1-4c22-b184-d949a15ec552?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/89184bfc-a1c1-4c22-b184-d949a15ec552?resizing_type=fit)

Chaos Visual Debugger 1.2 includes the following:

* **The** [Standalone Debugger](https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger#as-a-standalone-program)**:**
  Build and package CVD as a standalone Unreal Engine program.
* **Improved support for networked physics debugging**:

  + **[Multi-source support](https://dev.epicgames.com/documentation/en-us/unreal-engine/playback-in-chaos-visual-debugger#multi-source-recordings):** 
    Load two or more separate recordings at once.
  + **The [Session Discovery System](https://dev.epicgames.com/documentation/en-us/unreal-engine/live-debugging-with-chaos-visual-debugger):** 
    Find any locally running server or client build, and start recordings in a single click.
* **Improved performance**: To reduce resource consumption, we overhauled how geometry is generated and how objects are represented under the hood.

For a full overview of the new features, see the [CVD section](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-5-6-release-notes?application_version=5.6#chaos-visual-debugger) of the Unreal 5.6 Release Notes.

## Next Up

* [![Getting Started with Chaos Visual Debugger](https://dev.epicgames.com/community/api/documentation/image/cd8e296e-438e-4c83-aece-fb837a8a819f?resizing_type=fit&width=640&height=640)

  Getting Started with Chaos Visual Debugger

  Navigate Chaos Visual Debugger’s user interface.](https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-chaos-visual-debugger)

* [![Data Visualization Flags](https://dev.epicgames.com/community/api/documentation/image/30c4b8fb-085b-461f-9543-fe2b6e998a80?resizing_type=fit&width=640&height=640)

  Data Visualization Flags

  Understand data visualization flags in Chaos Visual Debugger.](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-visualization-flags-in-chaos-visual-debugger)

* [![Data Inspectors](https://dev.epicgames.com/community/api/documentation/image/e41606f4-f2e2-4f65-bf67-295486d1ef4f?resizing_type=fit&width=640&height=640)

  Data Inspectors

  Understand data inspectors in Chaos Visual Debugger.](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-inspectors-in-chaos-visual-debugger)

* [![Capturing Data with Chaos Visual Debugger](https://dev.epicgames.com/community/api/documentation/image/e4f0e2ed-45af-4558-8dbd-04be6afe4bd7?resizing_type=fit&width=640&height=640)

  Capturing Data with Chaos Visual Debugger

  Capture and play back recordings with Chaos Visual Debugger.](https://dev.epicgames.com/documentation/en-us/unreal-engine/capturing-data-with-chaos-visual-debugger)

* [![Recording to File](https://dev.epicgames.com/community/api/documentation/image/c6586e65-2b47-4ae3-b63c-f187268d22c3?resizing_type=fit&width=640&height=640)

  Recording to File

  Record to file with Chaos Visual Debugger](https://dev.epicgames.com/documentation/en-us/unreal-engine/recording-to-file)

* [![Recording a Live Session](https://dev.epicgames.com/community/api/documentation/image/611a2540-a88b-4a2d-9044-78c3cb86d61d?resizing_type=fit&width=640&height=640)

  Recording a Live Session

  Record a live session with Chaos Visual Debugger](https://dev.epicgames.com/documentation/en-us/unreal-engine/live-debugging-with-chaos-visual-debugger)

* [![Playback in Chaos Visual Debugger](https://dev.epicgames.com/community/api/documentation/image/118531b5-4316-4ac7-a933-abe744980883?resizing_type=fit&width=640&height=640)

  Playback in Chaos Visual Debugger

  Play back recordings in Chaos Visual Debugger.](https://dev.epicgames.com/documentation/en-us/unreal-engine/playback-in-chaos-visual-debugger)

* [chaos visual debugger](https://dev.epicgames.com/community/search?query=chaos%20visual%20debugger)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [What’s New in Chaos Visual Debugger 1.2](/documentation/en-us/unreal-engine/chaos-visual-debugger-in-unreal-engine?application_version=5.7#what%E2%80%99snewinchaosvisualdebugger12)
* [Next Up](/documentation/en-us/unreal-engine/chaos-visual-debugger-in-unreal-engine?application_version=5.7#nextup)
