<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/building-the-windows-container-images-from-source?application_version=5.7 -->

# Building the Windows Container Images from Source

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
5. [Setting Up Your Production Pipeline](/documentation/en-us/unreal-engine/setting-up-your-production-pipeline-in-unreal-engine "Setting Up Your Production Pipeline")
6. [Deploying Unreal Engine](/documentation/en-us/unreal-engine/deploying-unreal-engine "Deploying Unreal Engine")
7. [Container Deployments](/documentation/en-us/unreal-engine/container-deployments-and-images-for-unreal-editor-and-unreal-engine "Container Deployments")
8. [Container Tutorials](/documentation/en-us/unreal-engine/tutorials-and-examples-of-containers-in-unreal-engine "Container Tutorials")
9. Building the Windows Container Images from Source

# Building the Windows Container Images from Source

How to build the Windows container images that are included with Unreal Engine from source.

![Building the Windows Container Images from Source](https://dev.epicgames.com/community/api/documentation/image/fa08cc25-9afa-42dc-9916-777b9b95f084?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

All container images that are included with Unreal Engine have prebuilt versions available for download from GitHub Container Registry. It is only necessary to build the images from source if you want to create development images for a custom version of Unreal Engine or to make modifications to the image source code.

## Requirements

To build the Windows container images that ship with Unreal Engine, your computer will need to meet the hardware and software requirements listed in the Windows containers section of the [Hardware and Software Requirements](/documentation/en-us/unreal-engine/hardware-and-software-requirements-for-container-deployments-in-unreal-engine) page.

## Installing Docker

Docker is the recommended tool for building the container images that are included with Unreal Engine. To install Docker, follow the instructions to [install Docker Desktop for Windows](https://docs.docker.com/docker-for-windows/install/).

Once Docker Desktop is installed, you will need to [switch from Linux containers mode](https://docs.docker.com/docker-for-windows#switch-between-windows-and-linux-containers) (the default) to Windows containers mode.

## Building the Images

If you have downloaded the Unreal Engine source code from GitHub then you will need to run `Setup.bat` from the root of the source tree to download the engine's binary dependencies, just as you would when building the engine from source. If you do not perform this step then the files required for building container images will be missing.

Navigate to the following subdirectory of the Unreal Engine source code:

Engine/Extras/Containers/Dockerfiles/windows

To build the Windows container images, double-click the `build.bat` file. This will build the Windows runtime image for the same version of Windows that your machine is running.

* [beta](https://dev.epicgames.com/community/search?query=beta)
* [container](https://dev.epicgames.com/community/search?query=container)
* [containers](https://dev.epicgames.com/community/search?query=containers)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Requirements](/documentation/en-us/unreal-engine/building-the-windows-container-images-from-source?application_version=5.7#requirements)
* [Installing Docker](/documentation/en-us/unreal-engine/building-the-windows-container-images-from-source?application_version=5.7#installingdocker)
* [Building the Images](/documentation/en-us/unreal-engine/building-the-windows-container-images-from-source?application_version=5.7#buildingtheimages)
