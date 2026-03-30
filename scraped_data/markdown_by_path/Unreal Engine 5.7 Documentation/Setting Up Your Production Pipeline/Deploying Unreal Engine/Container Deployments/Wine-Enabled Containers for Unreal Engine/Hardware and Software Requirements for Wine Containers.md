<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/hardware-and-software-requirements-for-wine-containers-for-unreal-engine?application_version=5.7 -->

# Hardware and Software Requirements for Wine Containers

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
8. [Wine-Enabled Containers for Unreal Engine](/documentation/en-us/unreal-engine/wine-enabled-containers-for-unreal-engine "Wine-Enabled Containers for Unreal Engine")
9. Hardware and Software Requirements for Wine Containers

# Hardware and Software Requirements for Wine Containers

Hardware and software requirements for building and running Wine-enabled container images.

![Hardware and Software Requirements for Wine Containers](https://dev.epicgames.com/community/api/documentation/image/adff4f1f-2395-4622-ba94-c38f57eec4f3?resizing_type=fill&width=1920&height=335)

 On this page

## Requirements for Linux Containers

You can build and run the Wine-enabled container images for Unreal Engine on Windows, macOS, or Linux. To build or run the container images, your computer will need to meet the following hardware requirements:

* A 64-bit CPU with support for [Second Level Address Translation (SLAT)](https://en.wikipedia.org/wiki/Second_Level_Address_Translation).
* Hardware virtualization support enabled in the system BIOS.
* Minimum of 4 GB of system RAM.

Your computer will also need to meet the following software requirements:

* Windows: A 64-bit Windows 10 Home, Pro, Enterprise, or Education, version 1903 or newer with Docker Desktop for Windows installed. See the [Installing Docker](/documentation/en-us/unreal-engine/hardware-and-software-requirements-for-wine-containers-for-unreal-engine#installingdocker) section below for instructions on how to install Docker Desktop for Windows.
* macOS: macOS version 10.14 or newer with Docker Desktop for Mac installed. See the [Installing Docker](/documentation/en-us/unreal-engine/hardware-and-software-requirements-for-wine-containers-for-unreal-engine#installingdocker) section below for instructions on how to install Docker Desktop for Mac.
* Linux: A 64-bit version of CentOS 8 or newer, Debian 10 or newer, Fedora 32 or newer, Ubuntu 16.04 or newer, or any Linux distribution that meets [Docker's prerequisites](https://docs.docker.com/engine/install/binaries/#prerequisites) with Docker Engine installed. See the [Installing Docker](/documentation/en-us/unreal-engine/hardware-and-software-requirements-for-wine-containers-for-unreal-engine#installingdocker) section below for instructions on how to install Docker Engine.

## Installing Docker

Docker is the recommended tool for building and running container images with Wine and the Unreal Engine. The steps for installing Docker will depend on the operating system you are using. The links below provide instructions on how to do this on each platform it is available on:

* Windows: [Install Docker Desktop on Windows](https://docs.docker.com/desktop/setup/install/windows-install/)
* macOS: [Install Docker Desktop on Mac](https://docs.docker.com/desktop/setup/install/mac-install/)
* Linux: Follow the appropriate instructions to install Docker Engine for your specific Linux distribution:
  + [CentOS](https://docs.docker.com/engine/install/centos/)
  + [Debian](https://docs.docker.com/engine/install/debian/)
  + [Fedora](https://docs.docker.com/engine/install/fedora/)
  + [Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
  + [Other Linux distributions](https://docs.docker.com/engine/install/binaries/)

* [container](https://dev.epicgames.com/community/search?query=container)
* [containers](https://dev.epicgames.com/community/search?query=containers)
* [linux](https://dev.epicgames.com/community/search?query=linux)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)
* [bronze](https://dev.epicgames.com/community/search?query=bronze)
* [wine](https://dev.epicgames.com/community/search?query=wine)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Requirements for Linux Containers](/documentation/en-us/unreal-engine/hardware-and-software-requirements-for-wine-containers-for-unreal-engine?application_version=5.7#requirementsforlinuxcontainers)
* [Installing Docker](/documentation/en-us/unreal-engine/hardware-and-software-requirements-for-wine-containers-for-unreal-engine?application_version=5.7#installingdocker)
