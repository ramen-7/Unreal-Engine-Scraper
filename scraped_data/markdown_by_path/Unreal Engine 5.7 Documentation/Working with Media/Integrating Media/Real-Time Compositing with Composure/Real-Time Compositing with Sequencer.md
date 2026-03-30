<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/real-time-compositing-with-sequencer-in-unreal-engine?application_version=5.7 -->

# Real-Time Compositing with Sequencer

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
7. [Real-Time Compositing with Composure](/documentation/en-us/unreal-engine/realtime-compositing-with-composure-in-unreal-engine "Real-Time Compositing with Composure")
8. Real-Time Compositing with Sequencer

# Real-Time Compositing with Sequencer

Product documentation including reference and guides for Unreal Engine

![Real-Time Compositing with Sequencer](https://dev.epicgames.com/community/api/documentation/image/e4c9ce1a-6695-4be4-8ebe-4a7fa09e1b37?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

[Sequencer](/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview), our in-engine cinematic editor, can be used in conjunction with the Composure compositing system.

![Using Composure with Sequencer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/aa214da4-16c5-41a7-8aeb-ea880c777505/composure-sequencer.gif "composure-sequencer.gif")

Primarily, Sequencer can be used to:

1. Control the scene camera (referenced by the compositing system).
2. Render out composites and their contributing pieces, including Arbitrary Output Values (AOVs). This can be useful for compositing outside of the engine.

## Rendering Out Elements and AOVs

Any Composure element can be added to a sequence to indicate that its output should be exported when rendering out the sequence using the **Render Movie Settings** dialog with the **ComposureExport** output format.

[![Render Movie Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/14f6cde3-39ba-4419-a43d-92dbad9084e5/ue5_01-render-movie-settings.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/14f6cde3-39ba-4419-a43d-92dbad9084e5/ue5_01-render-movie-settings.png)

Click image to expand.

When such elements are rendered as part of this process, their final output will be written out to disk as an EXR image using the filename format specified in the dialog. Additional format specifiers can be included in the directory and filename options for the **{element}** and **{pass}**.

When multiple elements are included for **Export Output** in Sequencer, they will write over the same image file if **{element}** is not included in the name.

[![ue5_02-output-directory.png](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b1476723-ebb5-44a7-a4b4-9740c6657515/ue5_02-output-directory.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b1476723-ebb5-44a7-a4b4-9740c6657515/ue5_02-output-directory.png)

Click image to expand.

Additional AOVs to be exported with each element can be specified on each element by configuring the **Buffers to Export** on any CG Capture.

![Buffers to Export](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/076de18e-85e5-4cb2-95b2-570791c1ea8e/buffers-to-export.gif "buffers-to-export.gif")

Custom AOVs may be implemented by adding new Buffer Visualization materials, and adding them to the `[Engine.BufferVisualizationMaterials]` config section with the following format:

`CustomAOV=(Material="/Game/AOVs/CustomAOV.CustomAOV", Name=LOCTEXT("CustomAOV", "CustomAOV"))`

* [getting started](https://dev.epicgames.com/community/search?query=getting%20started)
* [beta](https://dev.epicgames.com/community/search?query=beta)
* [ar/vr/xr](https://dev.epicgames.com/community/search?query=ar%2Fvr%2Fxr)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Rendering Out Elements and AOVs](/documentation/en-us/unreal-engine/real-time-compositing-with-sequencer-in-unreal-engine?application_version=5.7#renderingoutelementsandaovs)
