<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/openxr-prerequisites-in-unreal-engine?application_version=5.7 -->

# OpenXR Runtime

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
6. [XR Development](/documentation/en-us/unreal-engine/developing-for-xr-experiences-in-unreal-engine "XR Development")
7. [Getting Started with XR Development](/documentation/en-us/unreal-engine/getting-started-with-xr-development-in-unreal-engine "Getting Started with XR Development")
8. OpenXR Runtime

# OpenXR Runtime

Learn how to install the OpenXR runtime and set up your projects for OpenXR.

![OpenXR Runtime](https://dev.epicgames.com/community/api/documentation/image/da5088af-f643-4ccf-b527-3ed569af508c?resizing_type=fill&width=1920&height=335)

 On this page

OpenXR Runtime

To develop OpenXR projects in Unreal Engine (UE), you must install the OpenXR runtime for the platform and hardware you are developing for. The following sections cover how to install the correct OpenXR runtime and which plugins are needed for each platform.

Currently, some of the platform-specific plugins in UE are incompatible with the OpenXR plugin. Make sure you disable the Oculus, SteamVR and Windows Mixed Reality plugins when using the OpenXR plugin in your Unreal project.

## Windows Mixed Reality

Complete the following items to begin using your Windows Mixed Reality devices with OpenXR in the Unreal Editor:

* Complete the steps in Microsoft's [Getting Started with OpenXR](https://docs.microsoft.com/en-us/windows/mixed-reality/develop/native/openxr-getting-started#getting-started-with-openxr-for-windows-mixed-reality-headsets) documentation to install the **OpenXR** runtime for **Windows Mixed Reality** on your computer.
* Enable the **OpenXR** plugin in your Unreal project.
* Optional:Install the [Microsoft OpenXR Plugin](https://www.fab.com/listings/8c00dec5-60fa-4b23-b861-98ee885419ce)

## Oculus

Complete the following items to begin using your Oculus devices with OpenXR in the Unreal Editor:

* Complete the steps in [Oculus Prerequisites](/documentation/en-us/unreal-engine/oculus-prerequisites-in-unreal-engine) to set up your computer and device.
* Enable the **OpenXR** plugin in your Unreal project.

## SteamVR

Complete the following items to begin using your SteamVR devices with OpenXR in the Unreal Editor:

* Complete the steps in [SteamVR Prerequisites](/documentation/en-us/unreal-engine/steamvr-prerequisites-in-unreal-engine) to set up your computer and device.
* Enable the **OpenXR** plugin in your Unreal project.

## OpenXR Runtime Environment Variable

If there are several OpenXR runtimes on your computer, you will need to set an environment variable so that Unreal Engine can find the correct OpenXR runtime.

While each OpenXR compatible runtime *should* support any OpenXR device, for best results, install the official runtime (SteamVR for Vive/Index, Oculus app for Quest, etc). You can do this manually but we use, and recommend using [OpenXR Explorer](https://github.com/maluoi/openxr-explorer). It allows for easy switching between OpenXR runtimes, shows lists of the runtime's supported extensions, and allows for inspection of common properties and enumerations, with direct links to relevant parts of the [OpenXR specification](https://registry.khronos.org/OpenXR/specs/1.0/pdf/xrspec.pdf).

* [xr](https://dev.epicgames.com/community/search?query=xr)
* [steamvr](https://dev.epicgames.com/community/search?query=steamvr)
* [openxr](https://dev.epicgames.com/community/search?query=openxr)
* [oculus](https://dev.epicgames.com/community/search?query=oculus)
* [windows mixed reality](https://dev.epicgames.com/community/search?query=windows%20mixed%20reality)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Windows Mixed Reality](/documentation/en-us/unreal-engine/openxr-prerequisites-in-unreal-engine?application_version=5.7#windowsmixedreality)
* [Oculus](/documentation/en-us/unreal-engine/openxr-prerequisites-in-unreal-engine?application_version=5.7#oculus)
* [SteamVR](/documentation/en-us/unreal-engine/openxr-prerequisites-in-unreal-engine?application_version=5.7#steamvr)
* [OpenXR Runtime Environment Variable](/documentation/en-us/unreal-engine/openxr-prerequisites-in-unreal-engine?application_version=5.7#openxrruntimeenvironmentvariable)

Related documents

[Developing for Head-Mounted Experiences with OpenXR

![Developing for Head-Mounted Experiences with OpenXR](https://dev.epicgames.com/community/api/documentation/image/e82d4ae1-3113-44c3-9863-528e2ca53a85?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/developing-for-head-mounted-experiences-with-openxr-in-unreal-engine)

[Making Interactive XR Experiences

![Making Interactive XR Experiences](https://dev.epicgames.com/community/api/documentation/image/d40682e3-646b-4d1d-ae59-10546012822b?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/making-interactive-xr-experiences-in-unreal-engine)
