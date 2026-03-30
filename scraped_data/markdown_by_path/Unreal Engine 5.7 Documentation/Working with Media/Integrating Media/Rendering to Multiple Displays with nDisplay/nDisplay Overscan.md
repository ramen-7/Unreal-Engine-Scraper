<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/ndisplay-overscan-in-unreal-engine?application_version=5.7 -->

# nDisplay Overscan

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
7. [Rendering to Multiple Displays with nDisplay](/documentation/en-us/unreal-engine/rendering-to-multiple-displays-with-ndisplay-in-unreal-engine "Rendering to Multiple Displays with nDisplay")
8. nDisplay Overscan

# nDisplay Overscan

Use Overscan to achieve pixel perfect render continuity across multiple render nodes when cluster rendering with nDisplay and with post effects enabled.

![nDisplay Overscan](https://dev.epicgames.com/community/api/documentation/image/35306301-c064-4b15-a826-89ebf9022391?resizing_type=fill&width=1920&height=335)

 On this page

Achieve pixel perfect render continuity across multiple render nodes when cluster rendering with nDisplay and with post effects enabled. By overscanning in configurable direction(s), and then cropping out the extra rendered pixels with an exposed amount, users can decide on a (visual accuracy vs performance) ratio that works best for their project.

Visually impactful effects such as bloom, ambient occlusion or motion blur can now be enabled to some extent when range is kept relatively small in most nDisplay projects - at some configurable performance cost.

## Limitations

* Auto-exposure should remain disabled as overscan cannot fix this.
* This technique works well when the range of the post effect doesn't exceed the set overscan percentage. It is designed to help reduce or minimise visual discrepancy since the percentage is arbitrary.
* This implementation works with all projection policies.

## Supported Rendering Features

| Feature | nDisplay Compatibility | Solution | Notes\* | Visual Impact | Accumulation Buffer | In-Camera VFX Compatible |
| --- | --- | --- | --- | --- | --- | --- |
| Rendering / Post Effects |  |  |  |  |  |  |
| [Bloom](/documentation/en-us/unreal-engine/bloom-in-unreal-engine) | Yes\* | Overscan | Keep radius small | High | No | Yes |
| [Lens Flare](/documentation/en-us/unreal-engine/post-process-effects-in-unreal-engine) | No | Avoid |  | High | No | Yes |
| [Auto Exposure (Eye Adaptation)](/documentation/en-us/unreal-engine/auto-exposure-in-unreal-engine) | No | Avoid | Will separate type of logic. | High | Yes | Yes |
| [Motion Blur](/documentation/en-us/unreal-engine/content-examples-sample-project-for-unreal-engine) | Yes\* | Overscan |  | Medium | No | Yes but not working well for cinematography. |
| [Depth of Field (DoF)](/documentation/en-us/unreal-engine/depth-of-field-in-unreal-engine) | No | Avoid |  |  |  |  |
| [Screen Space Ambient Occlusion (SSAO)](/documentation/en-us/unreal-engine/post-process-effects-in-unreal-engine#ambientocclusion) | Yes\* | Overscan | Keep radius small | Medium | No | Yes |
| [Temporal Anti Aliasing (TAA)](/documentation/en-us/unreal-engine/post-process-effects-in-unreal-engine) | Yes\* | Overscan |  | Low | Yes | Yes |
| [Screen Space Reflections (SSR)](/documentation/en-us/unreal-engine/screen-space-reflections-in-unreal-engine) | No | Avoid |  | High | Yes | Yes |
| [Screen Space Global Illumination (SSGI)](/documentation/en-us/unreal-engine/screen-space-global-illumination-in-unreal-engine) | No | Avoid |  | High | Yes | Yes |
| [Vignetting](/documentation/en-us/unreal-engine/post-process-effects-in-unreal-engine) | Yes\* | N/A |  | Medium | No | Yes |
| [Scene Fringe (Chromatic Aberrations)](/documentation/en-us/unreal-engine/post-process-effects-in-unreal-engine) | Yes\* | Avoid | Keep radius small | Low | No | Yes |
| [Raytracing (Denoiser)](/documentation/en-us/unreal-engine/hardware-ray-tracing-in-unreal-engine#evaluatingdenoiserquality) | No |  |  | Low | No | Should work but noise is non-deterministic. |
| Rendering / Other |  |  |  |  |  |  |
| [Planar Reflections](/documentation/en-us/unreal-engine/planar-reflections-in-unreal-engine) | Yes\* | N/A | Users can customize the FOV setting. | High | No | Yes |
| [Sky Atmosphere](/documentation/en-us/unreal-engine/sky-atmosphere-component-in-unreal-engine) | Yes | N/A | Fixed | High | No | Yes |
| [Material (shader) time based animations](/documentation/en-us/unreal-engine/constant-material-expressions-in-unreal-engine#time) | Yes |  |  |  | Sometimes |  |
| [Shadows](/documentation/en-us/unreal-engine/shadowing-in-unreal-engine) | Yes |  |  |  | No |  |
| [Culling](/documentation/en-us/unreal-engine/visibility-and-occlusion-culling-in-unreal-engine) | Yes |  |  |  | No |  |
| [UMG - 2D](/documentation/en-us/unreal-engine/umg-editor-reference-for-unreal-engine) | No |  |  |  | No |  |
| Gameplay |  |  |  |  |  |  |
| [Sequencer](/documentation/en-us/unreal-engine/real-time-compositing-with-sequencer-in-unreal-engine) | Yes | N/A | N/A | High | No | Yes |
| [Blueprints](/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine) | Yes/No | Avoid randoms | Works if using seeded randoms. There is also the BeginPlay issue not running when BP is reconstructed. | High | Sometimes | Yes |
| [Physics (Chaos solver) IKRigid bodiesCloth](/documentation/en-us/unreal-engine/clothing-tool-in-unreal-engine) | Yes | Yes |  | High | No | Yes |
| [Particle System Cascade / Niagara](/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine) | Yes | N/A | Deterministic setting must be set to ON for emitters. | High | Sometimes | Yes |
| Media / Playback |  |  |  |  |  |  |
| [Video / Image sequence](/documentation/en-us/unreal-engine/media-framework-in-unreal-engine) | N/A | N/A | Video engine currently not frame accurate. | High | No |  |
| [Video I/O, BM, Aja](/documentation/en-us/unreal-engine/professional-video-io-in-unreal-engine) | N/A | N/A | N/A | High | No |  |
| [NDI/SMPTE 2110](/documentation/en-us/unreal-engine/media-framework-overview-for-unreal-engine#streammediasource) | N/A | N/A | Need to test for frame accuracy. | High | No |  |

\* The feature functions within limits. For example, Bloom functions for small/medium bloom radiuses as opposed to large blooms which would not make sense or function well in terms of the performance - visual ratio. Refer to the Notes for further details for individual features.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Limitations](/documentation/en-us/unreal-engine/ndisplay-overscan-in-unreal-engine?application_version=5.7#limitations)
* [Supported Rendering Features](/documentation/en-us/unreal-engine/ndisplay-overscan-in-unreal-engine?application_version=5.7#supportedrenderingfeatures)
