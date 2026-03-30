<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/global-illumination-in-unreal-engine?application_version=5.7 -->

# Global Illumination

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
5. [Building Virtual Worlds](/documentation/en-us/unreal-engine/building-virtual-worlds-in-unreal-engine "Building Virtual Worlds")
6. [Lighting the Environment](/documentation/en-us/unreal-engine/lighting-the-environment-in-unreal-engine "Lighting the Environment")
7. Global Illumination

# Global Illumination

A collection of topics on the global illumination options available to choose from.

![Global Illumination](https://dev.epicgames.com/community/api/documentation/image/e43aacf3-3a2c-4203-9c8b-e74daae908cf?resizing_type=fill&width=1920&height=335)

 On this page

**Global illumination** (sometimes referred to as indirect lighting and indirect illumination) simulates lighting interactions with geometry and material surfaces to add accurate lighting to scenes. Global illumination also takes into account absorption and reflectiveness of the materials in which it interacts.

Simulating the way in which light behaves in a 3D world is handled in one of two ways: using lighting that supports movement and interaction, or precomputed lighting that doesn't require scenes to be overly dynamic or interactive with lighting.

Unreal Engine provides multiple lighting paths to choose from for global illumination solutions, and often they are not exclusive to one another and can be seamlessly blended. For example, it is possible to have both dynamic lighting and baked lighting within the same scene.

For comparison, the list below highlights some of the benefits of choosing a precomputed or dynamic global illumination path for your project:

|  |  |
| --- | --- |
| * Ideal for scenes where lighting doesn't need to change. * Performance costs are relative to the memory required to load and store the lightmap textures. * Quality and accuracy of results is set by the texture resolution of the lightmap texture being baked and applied to geometry. * Supports Static Mesh and BSP geometry by default. * Static Meshes require setting up a Lightmap UV to store lighting data. * Can be used in combination with dynamic lighting. | * Ideal for times where lighting needs to change, such as turning a light on or off, or a time-of-day system. * Large, open-world environments present impractical requirements for baked lighting (even without a time-of-day system). Bake times, memory usage, texture storage and playback are considerable factors to use dynamic GI. * Performance costs can be significantly more expensive to calculate in real-time depending on the method being used. * Quality and accuracy is often traded with performance. Some Dynamic GI methods are limited by real-time usage. * Supports all geometry types by default. * Can be used in combination with precomputed lighting. |

## Precomputed Global Illumination

The light baking system in Unreal Engine computes lighting data on the CPU, or GPU, using the Lightmass Global Illumination system. This method of precomputing lighting is used to achieve high-quality results that aren't compromised by real-time limitations by storing the information in textures that are then applied to geometry. This method of lighting cannot be changed dynamically and is ideal for projects where lighting doesn't need to change, or for mobile projects where dynamic lighting is limited.

* **CPU-based Lightmass** uses the CPU with a separate program called [Unreal Swarm](/documentation/en-us/unreal-engine/unreal-swarm-in-unreal-engine) to compute and generate lighting data. This method can use a single machine or distribute lighting data to build farms.
* **GPU-based Lightmass** uses your current machine's NVIDIA GPU which supports DirectX 12 and ray tracing to compute and generate lighting data.

### Precomputed Global Illumination Methods

[![CPU Lightmass Global Illumination](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a10d9073-8b0e-4c1a-8cab-f78bb3890c06/lightmass-global-illum-topic.png)

CPU Lightmass Global Illumination

A run down of all the features and settings of Lightmass.](/documentation/en-us/unreal-engine/cpu-lightmass-global-illumination-in-unreal-engine)
[![GPU Lightmass Global Illumination](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4ad4f9df-e2e3-4507-92e4-7071d2e49cd8/13_gpulm_withdenoisingapplied.png)

GPU Lightmass Global Illumination

Learn about the GPU-based system for generating precomputed lighting data.](/documentation/en-us/unreal-engine/gpu-lightmass-global-illumination-in-unreal-engine)

### Precomputed Global Illumination Supporting Topics

[![Indirect Lighting Cache](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/073559e0-f198-4f07-b5cd-8bdadba1242d/indirect-cache-topic.png)

Indirect Lighting Cache

Cached indirect lighting samples used for global illumination of dynamic objects and unbuilt scene preview.](/documentation/en-us/unreal-engine/indirect-lighting-cache-in-unreal-engine)
[![Volumetric Lightmaps](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/408ba672-b0ab-4ab1-bab4-45c206dfee3d/volumetric-lightmaps-topic.png)

Volumetric Lightmaps

Volumetric lighting samples used for global illumination of dynamic objects and unbuild scene previews.](/documentation/en-us/unreal-engine/volumetric-lightmaps-in-unreal-engine)
[![Lightmass Portals](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/469de71b-becb-44de-9800-a0abd76e296c/lightmass-portals-topic.png)

Lightmass Portals

Help increase the quality of baked interior lighting.](/documentation/en-us/unreal-engine/lightmass-portals-in-unreal-engine)
[![Unreal Swarm](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f9a69df1-fa48-4157-b115-4b2c207a82b0/unrealswarm_overviewimage-2.png)

Unreal Swarm

An overview of Unreal Swarm, our task distribution system for computationally expensive applications, including Unreal Lightmass, the high-quality static global illumination solver.](/documentation/en-us/unreal-engine/unreal-swarm-in-unreal-engine)
[![Lightmass Basics](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/be91e0c1-5ef4-4037-9566-245395a2b5b2/lightmass-basics-topic.png)

Lightmass Basics

High level introduction to Lightmass.](/documentation/en-us/unreal-engine/lightmass-basics-in-unreal-engine)
[![Precomputed Lighting Scenarios](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/da88aed3-7490-4b5a-bcce-e6327c97e38c/pcls-topic.png)

Precomputed Lighting Scenarios

An overview of using multiple lighting setups for a single scene.](/documentation/en-us/unreal-engine/using-precomputed-lighting-scenarios-in-unreal-engine)

## Dynamic Global Illumination

The dynamic global illumination methods in Unreal Engine provide real-time scalable solutions for dynamic indirect lighting in your projects. This means being able to place, move, and light objects in the world without additional costs of baking lighting or having additional set up. Dynamic indirect lighting also means being able to accurately simulate time-of-day transitions or something as simple as turning a light on and off and having light bounce and reflect accurately.

![lumen-global-illumination](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/96f61b68-6220-473a-bcdb-1f20b956592d/lumentechdemo_1.png)

* **Lumen** is a fully dynamic global illumination and reflection system that is designed for next-generation consoles. It is the default dynamic global illumination system and uses multiple ray tracing methods to solve global illumination and reflections at scale.
* **Screen Space Global Illumination** (SSGI) is a post processing effect that generates global illumination for objects within the scene based solely on the current visible objects within the camera view. This is a low-cost and most effectively used in conjunction with existing precomputed or dynamic global illumination methods as an additive effect.

  This feature is deprecated. It may be removed in a future release.

### Dynamic Global Illumination Topics

%building-virtual-worlds/lighting-and-shadows/global-illumination/lumen:Topic%
%building-virtual-worlds/lighting-and-shadows/global-illumination/lumen/TechOverview:Topic%
[![Screen Space Global Illumination](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c6e11730-7981-4557-b116-9f32ed95fc04/screen-space-topic.png)

Screen Space Global Illumination

An overview of dynamic global illumination using a screen space effect.](/documentation/en-us/unreal-engine/screen-space-global-illumination-in-unreal-engine)
%building-virtual-worlds/lighting-and-shadows/ray-tracing-and-path-tracing/hardware-ray-tracing:Topic%

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [lighting](https://dev.epicgames.com/community/search?query=lighting)
* [global illumination](https://dev.epicgames.com/community/search?query=global%20illumination)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Precomputed Global Illumination](/documentation/en-us/unreal-engine/global-illumination-in-unreal-engine?application_version=5.7#precomputedglobalillumination)
* [Precomputed Global Illumination Methods](/documentation/en-us/unreal-engine/global-illumination-in-unreal-engine?application_version=5.7#precomputedglobalilluminationmethods)
* [Precomputed Global Illumination Supporting Topics](/documentation/en-us/unreal-engine/global-illumination-in-unreal-engine?application_version=5.7#precomputedglobalilluminationsupportingtopics)
* [Dynamic Global Illumination](/documentation/en-us/unreal-engine/global-illumination-in-unreal-engine?application_version=5.7#dynamicglobalillumination)
* [Dynamic Global Illumination Topics](/documentation/en-us/unreal-engine/global-illumination-in-unreal-engine?application_version=5.7#dynamicglobalilluminationtopics)
