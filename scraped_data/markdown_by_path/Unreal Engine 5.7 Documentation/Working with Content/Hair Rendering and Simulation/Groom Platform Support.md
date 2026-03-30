<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/groom-platform-support-in-unreal-engine?application_version=5.7 -->

# Groom Platform Support

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
5. [Working with Content](/documentation/en-us/unreal-engine/working-with-content-in-unreal-engine "Working with Content")
6. [Hair Rendering and Simulation](/documentation/en-us/unreal-engine/hair-rendering-and-simulation-in-unreal-engine "Hair Rendering and Simulation")
7. Groom Platform Support

# Groom Platform Support

A summary of groom's features supported on various platforms.

![Groom Platform Support](https://dev.epicgames.com/community/api/documentation/image/9790a355-9a3c-42cb-9ea5-682512d62f78?resizing_type=fill&width=1920&height=335)

 On this page

This page contains information on various platforms that support different features of grooms.

## Groom Geometry Types

Groom **Cards** and Groom **Meshes** geometry are supported on all platforms. However, Groom **Strands** rendering can only run on certain platforms due to its demanding rendering cost.

Strands rendering is only supported on the following platforms:

* Microsoft Windows that uses either DirectX 11, DirectX 12, or Vulkan.
* Apple macOS, requires Shader Model 6 on the Mac M2 and above.
* Linux
* Current generation console, such as PlayStation 5 and Xbox Series S/X.

For more general information about what hardware and software Unreal Engine supports, see Unreal Engine's [Hardware and Software Specifications](understanding-the-basics\installing-unreal-engine\hardware-software-specifications).

## Groom Binding

A Groom can be attached to skeletal mesh geometry with Groom Bindings. There are two types of binding attachments: rigid and skinned.

These bindings attachments support the following platforms:

* **Rigid attachment** is supported on all platforms.
* **Skinned attachment** is supported on all platforms except Nintendo Switch and mobile because the performance cost is too much and there is missing implementation to support it.

Similar to Skinned attachment, **Global Interpolation** (also called RBF) is supported on all platforms except Nintendo Switch and mobile.

To learn more about groom bindings and how they are used, see [Setting up Bindings for Grooms](https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-bindings-for-grooms-in-unreal-engine).

## Simulation

Groom simulation is supported on all platforms.

To learn more about using simulation with grooms, see [Enabling Physics Simulation on Grooms](https://dev.epicgames.com/documentation/en-us/unreal-engine/enabling-physics-simulation-on-grooms-in-unreal-engine).

## Groom Cache

Using a Groom Cache allows for pre-computed simulation / animation. This is achieved at the Guide level or Strands level.

* The **Strands Cache** is available only on platforms that support Strand rendering (see ["Groom Geometry Types"](https://dev.epicgames.com/documentation/en-us/unreal-engine/groom-platform-support-in-unreal-engine) above).
* The **Guides Cache** is supported on all platforms.

To learn more about the grooms cache and its function, see [Groom Caches](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-groom-caches-with-hair-in-unreal-engine).

## Known Platform Limitations

* Frame rate depends on several factors, such as the size of the groom, the resolution of the groom, and the hardware on which the groom is being run.

  + For example, you should expect a 30Hz or higher framerate with a NVIDIA RTX-2090Ti GPU for a human-like groom rendered at 1080p. Higher quality settings will result in a significant performance drop.
* Depth of Field is supported but may produce some artifacts.
* Grooms rendered with the [Path Tracer](building-virtual-worlds\lighting-and-shadows\ray-tracing-and-path-tracing\path-tracer) have a different appearance than the rasterizer's output.
* Grooms do not yet support proper precomputed lighting (Static or Stationary).

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [physics](https://dev.epicgames.com/community/search?query=physics)
* [hair](https://dev.epicgames.com/community/search?query=hair)
* [metahumans](https://dev.epicgames.com/community/search?query=metahumans)
* [grooms](https://dev.epicgames.com/community/search?query=grooms)
* [platforms](https://dev.epicgames.com/community/search?query=platforms)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Groom Geometry Types](/documentation/en-us/unreal-engine/groom-platform-support-in-unreal-engine?application_version=5.7#groom-geometry-types)
* [Groom Binding](/documentation/en-us/unreal-engine/groom-platform-support-in-unreal-engine?application_version=5.7#groom-binding)
* [Simulation](/documentation/en-us/unreal-engine/groom-platform-support-in-unreal-engine?application_version=5.7#simulation)
* [Groom Cache](/documentation/en-us/unreal-engine/groom-platform-support-in-unreal-engine?application_version=5.7#groom-cache)
* [Known Platform Limitations](/documentation/en-us/unreal-engine/groom-platform-support-in-unreal-engine?application_version=5.7#known-platform-limitations)
