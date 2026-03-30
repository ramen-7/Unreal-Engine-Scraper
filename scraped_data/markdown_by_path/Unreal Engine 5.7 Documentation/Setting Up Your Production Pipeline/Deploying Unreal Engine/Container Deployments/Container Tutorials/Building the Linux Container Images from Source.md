<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/building-the-linux-container-images-from-source?application_version=5.7 -->

# Building the Linux Container Images from Source

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
9. Building the Linux Container Images from Source

# Building the Linux Container Images from Source

How to build the Linux container images that ship with Unreal Engine from source.

![Building the Linux Container Images from Source](https://dev.epicgames.com/community/api/documentation/image/f2ed48de-503a-450a-a28d-49118d5aa8f8?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

All container images that are included with Unreal Engine have prebuilt versions available for download from GitHub Container Registry. It is only necessary to build the images from source if you want to create development images for a custom version of Unreal Engine or to make modifications to the image source code.

## Requirements

To build the Linux container images that are included with Unreal Engine, your computer will need to meet the hardware and software requirements listed in the Linux containers section of the [Hardware and Software Requirements](/documentation/en-us/unreal-engine/hardware-and-software-requirements-for-container-deployments-in-unreal-engine) page.

Building the Linux container images from source under Windows is not supported. Although it is possible to build the images using either Docker Desktop or WSL2 under Windows 10 and Windows 11, this process requires additional configuration and troubleshooting to function correctly, and Epic Games does not provide support for doing so. Instead, you should build the Linux container images under Linux, either installed in a virtual machine or directly on the host machine.

## Installing Docker

Docker is the recommended tool for building and running the container images that are included with Unreal Engine. The steps for installing Docker will depend on the operating system that you are using. The links below provide instructions on how to do this on each platform it is available on:

* **Windows:** [Install Docker Desktop for Windows](https://docs.docker.com/docker-for-windows/install/)
* **macOS:** [Install Docker Desktop for Mac](https://docs.docker.com/docker-for-mac/install/)
* **Linux:** Follow the appropriate instructions to install Docker Engine for your specific Linux distribution:

  + [CentOS](https://docs.docker.com/engine/install/centos/)
  + [Debian](https://docs.docker.com/engine/install/debian/)
  + [Fedora](https://docs.docker.com/engine/install/fedora/)
  + [Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
  + [Other Linux distributions](https://docs.docker.com/engine/install/binaries/)

## Building the Images for an Official Engine Release

If you have downloaded the Unreal Engine source code from GitHub then you will need to run `Setup.sh` from the root of the source tree to download the engine's binary dependencies, just as you would when building the engine from source. If you do not perform this step, then the files required for building container images will be missing.

Navigate to the following subdirectory of the Unreal Engine source code:

```
	Engine/Extras/Containers/Dockerfiles/linux

Copy full snippet
```

The build scripts for the Linux container images search for Git credentials in files called `username.txt` and `password.txt`:

* Create the `username.txt` file and populate it with your GitHub username.
* Create the `password.txt` file and populate it with your GitHub personal access token.

To build the Linux container images for a given release of the Unreal Engine, run the command shown below in a Bash shell, replacing `ENGINE_RELEASE` with the appropriate release number (e.g. "4.27.0"):

```
	./build.sh ENGINE_RELEASE

Copy full snippet
```

This will build both the runtime images for Linux and the development images for Linux, followed by images for specific use cases such as [Pixel Streaming](/documentation/en-us/unreal-engine/pixel-streaming-in-unreal-engine). The development images will take the longest to build, since they download the Unreal Engine source code from GitHub and create an [Installed Build](/documentation/en-us/unreal-engine/installed-build-reference-guide-for-unreal-engine) of the Engine.

## Building the Images for a Custom Version of the Engine

The build scripts only support retrieving the Unreal Engine source code from Git. Other version control systems such as Perforce are not supported. It is possible to use other version control systems by manually modifying the Dockerfiles for the development images but Epic Games does not provide support for doing so.

The build scripts for the Linux container images support specifying a custom Git repository and branch from which to retrieve the Unreal Engine source code instead of using the official GitHub repository. Custom repositories might include GitHub forks of the official Unreal Engine repository or private repositories stored on on-premises Git servers maintained by an organization for internal use.

How you populate the Git credentials in the `username.txt` and `password.txt` files will depend upon the type of Git repository being used:

* **GitHub fork:**

  + Use your GitHub username and personal access token.
* **Custom Git server:**

  + Populate the `username.txt` file with your Git username.
  + Populate the `password.txt` file with your Git password.

To build the Linux container images for a specific branch of a Git repository, run the command shown below in a Bash shell, replacing `BRANCH` with the name of the branch and `REPOSITORY` with the HTTPS URL for the Git repository (e.g. *"https://github.com/EpicGames/UnrealEngine.git"*):

```
	./build.sh BRANCH REPOSITORY
Copy full snippet
```

## Modifying Advanced Build Parameters

The build script `build.sh` includes the following advanced build parameters that can be modified by manually editing the file:

* `BASEIMAGE`: This is a string that specifies the Linux base image that will be used when building the development images. This value defaults to an Ubuntu base image [provided by NVIDIA](https://hub.docker.com/r/nvidia/opengl) that includes the OpenGL development headers.

* [beta](https://dev.epicgames.com/community/search?query=beta)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Requirements](/documentation/en-us/unreal-engine/building-the-linux-container-images-from-source?application_version=5.7#requirements)
* [Installing Docker](/documentation/en-us/unreal-engine/building-the-linux-container-images-from-source?application_version=5.7#installingdocker)
* [Building the Images for an Official Engine Release](/documentation/en-us/unreal-engine/building-the-linux-container-images-from-source?application_version=5.7#buildingtheimagesforanofficialenginerelease)
* [Building the Images for a Custom Version of the Engine](/documentation/en-us/unreal-engine/building-the-linux-container-images-from-source?application_version=5.7#buildingtheimagesforacustomversionoftheengine)
* [Modifying Advanced Build Parameters](/documentation/en-us/unreal-engine/building-the-linux-container-images-from-source?application_version=5.7#modifyingadvancedbuildparameters)
