<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/create-an-installed-build-of-unreal-engine?application_version=5.7 -->

# Create an Installed Build

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
7. Create an Installed Build

# Create an Installed Build

Create pre-packaged binaries for Unreal Editor that you can distribute to your team.

![Create an Installed Build](https://dev.epicgames.com/community/api/documentation/image/c3c66be3-da84-4503-b9ce-cba6de8a9e04?resizing_type=fill&width=1920&height=335)

 On this page

Operating System 

×Windows

Select an option from the dropdown to see content relevant to it.

When working on a source build of an **Unreal Engine (UE)** project with a team, some team members might not have the necessary software or knowledge to [build and run Unreal Engine from source](https://dev.epicgames.com/documentation/en-us/unreal-engine/building-unreal-engine-from-source). In these cases, you can build Unreal Engine binaries and distribute them to your team as an **installed build**. This creates a package similar to what is deployed by the Epic Games Launcher.

For more general instructions on how to create an Installed Build, refer to the [Installed Build Reference Guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/installed-build-reference-guide-for-unreal-engine). This page provides additional information and steps for developers using **Windows**.

## Prerequisites

Before you make an installed build, make sure you have the following prerequisites:

* A [source code build of Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/building-unreal-engine-from-source).
* [Windows DotNet 6.0 Runtime](https://dotnet.microsoft.com/en-us/download/dotnet/6.0/runtime?cid=getdotnetcore&os=windows&arch=x64).
* Windows Debugging Tools component for Windows 10 SDK (Windows 10 only – See below).

### Recommended Hardware

We recommend you use a machine with a high processor core/thread count for builds. While UE builds on a single core, build times are significantly reduced with multi-core processors. See [Hardware and Software Specifications](https://dev.epicgames.com/documentation/en-us/unreal-engine/hardware-and-software-specifications-for-unreal-engine?application_version=5.5) for more details on recommended hardware.

### Windows 10 SDK (Windows 10 users only)

On Windows 10, you need to install the [Windows Debugging Tools component in the Windows 10 SDK](https://developer.microsoft.com/en-us/windows/downloads/sdk-archive/). This enables `PDBCopy.exe`, which is used in the build process to strip symbols and optimize the resulting package size.

If you do not already have the Windows 10 SDK installed, follow these steps:

1. [Download and install the Windows 10 SDK from Microsoft's site](https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/).
2. When you reach the dialogue that says **select the features you want to install**, make sure **Debugging Tools for Windows** is checked, then proceed with the installation.

   [![Debugging Tools for Windows is selected in the feature selection dialog for the Windows 10 SDK installer.](https://dev.epicgames.com/community/api/documentation/image/7e75d2cc-a889-4057-8792-4cb833565f72?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7e75d2cc-a889-4057-8792-4cb833565f72?resizing_type=fit)
3. Proceed with the installation.

If you already have the Windows 10 SDK set up, but don’t have Debugging Tools for Windows, follow these steps:

1. Open **Add or Remove Programs.**
2. In the list of available programs, locate your Windows Software Development Kit installation. Click **Modify**.

   [![Modifying the Windows SDK in Add or Remove Programs](https://dev.epicgames.com/community/api/documentation/image/d1703e06-b34d-4253-b825-7dc6aa1939e8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d1703e06-b34d-4253-b825-7dc6aa1939e8?resizing_type=fit)
3. In the list of options that appears, check **Change** and click **Next.**
4. When you see the dialog that says **select the features you want to change**, check **Debugging Tools for Windows**, then click **Change** to proceed with the installation.

## Make an Installed Build

To make an Installed Build on Windows, follow these steps:

1. Regenerate your Unreal Engine project files.

   * If you encounter error messages when attempting to regenerate project files, double check that you have the [Windows DotNet 6.0 runtime](https://dotnet.microsoft.com/en-us/download/dotnet/6.0/runtime) installed.
2. Use `RunUAT.bat` to create an installed build. The following is an example of a BuildGraph command to create an installed build for Windows:

   Command Line

   C++

   ```
   RunUAT.bat BuildGraph -script=Engine/Build/InstalledEngineBuild.xml -target="Make Installed Build Win64" -nosign -set:GameConfigurations=Development;Shipping -set:WithWin64=true -set:WithAndroid=true -set:WithDDC=false -set:WithLinux=false -set:WithLinuxArm64=false -set:WithIOS=false -set:WithTVOS=false -set:WithMac=false -clean
   ```

   RunUAT.bat BuildGraph -script=Engine/Build/InstalledEngineBuild.xml -target=&quot;Make Installed Build Win64&quot; -nosign -set:GameConfigurations=Development;Shipping -set:WithWin64=true -set:WithAndroid=true -set:WithDDC=false -set:WithLinux=false -set:WithLinuxArm64=false -set:WithIOS=false -set:WithTVOS=false -set:WithMac=false -clean

   Copy full snippet(1 line long)

   Make sure you specify whether or not every platform that you have available should be added or not. If you have additional platforms not mentioned here in your source code, add `-Set:With[Platform]=true` or `-Set:With[Platform]=false` according to your project’s needs, where [Platform] is replaced with the name of the added platform.

   The details about the parameters used in the above example are as follows:

   | Parameter | Required or Optional | Description |
   | --- | --- | --- |
   | `-target="Make Installed Build Win64”` | Required | Instructs BuildGraph to run a specific operation. This graph of dependencies is described in the script="Engine/Build/InstalledEngineBuild.xml" and there are other options available that may meet your requirements better, but for the purposes of this document our example targets a build that matches what a user would receive from the launcher version of Unreal Engine. |
   | `-set With[Platform]=true` or `-set With[Platform]=false` | Required | Specifies whether or not support for a given platform should be added to your installed build, where [Platform] is replaced with the name of a platform you want to enable or disable. **Make sure to add this parameter for every platform you have source code for.** For details on which platforms to enable or disable, refer to the Required Platforms section below. |
   | `-set:GameConfigurations=Development;Shipping` | Required | Flag for different versions of the editor. We recommend including **Development** and **Shipping**. |
   | `-set WithClient=false` and `-set WithServer=false` | Optional | Specifies whether to create Client and Server builds for network multiplayer projects. Defaults to false. |
   | `-set WithDDC=false` | Optional | Specifies whether to create a build that includes [Derived Data Cache](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-derived-data-cache-in-unreal-engine) support. Defaults to false. |
   | `-clean` | Recommended | Performs a fresh recompile of the project. Remove this parameter if you encounter an "Other Compilation Error” message. |

   If you receive an "Other Compilation Error" message, remove the `-clean` parameter and try again, as there are known issues with this command on Linux.
3. Build the Shader Compiler Worker.

   C++

   ```
   Engine\Build\BatchFiles\Build.bat ShaderCompileWorker Win64 Development
   ```

   Engine\Build\BatchFiles\Build.bat ShaderCompileWorker Win64 Development

   Copy full snippet(1 line long)

Your build appears in the Windows directory where Feature Packs, Templates, and Engine are located for distribution.

### Required Platforms

When creating installed builds on Windows, make sure you enable the following platforms with the `-With[Platform]` parameter:

| Platform | Parameter | Description |
| --- | --- | --- |
| Android | `-set WithAndroid=true` | Required to support publishing on Android, which is the target platform for most HMI projects. |
| Windows 64-bit | `-set WithWin64=true` | Required to support building the editor on Windows. |

Disable all other platforms, as they are not necessary for either running Unreal Editor or packaging HMI projects.

## Test the Installed Build Executable

Installed builds appear in the LocalBuilds folder under `LocalBuilds/Engine/Linux/Engine/Binaries/Win64`. On the Windows operating system, `UnrealEditor.exe` is the main executable for the Unreal Editor. Run this executable to test your build.

[![The location of UEEditor.exe](https://dev.epicgames.com/community/api/documentation/image/ddd31465-43e3-42b7-8323-a5c20ffc4f79?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ddd31465-43e3-42b7-8323-a5c20ffc4f79?resizing_type=fit)

When you run your installed build for the first time, a prompt appears to ask for firewall permissions. We advise that you accept these permissions for full functionality.

To archive and distribute the build, place your installed build in the top directory of your source control repository alongside the FeaturePacks, Templates, and Engine directories.

[![An error stating "unable to launch ShaderCompileWorker"](https://dev.epicgames.com/community/api/documentation/image/32b6d1a3-412b-497d-afc0-cc6e50b80eaf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/32b6d1a3-412b-497d-afc0-cc6e50b80eaf?resizing_type=fit)

If you see a prompt stating "Unable to launch ShaderCompileWorker" or experience a crash while compiling shaders, the Shader Compiler Worker has not been built yet. Revisit the last step of the workflow under Make an Installed Build above. We build Shader Compiler Worker separately so that you do not need to rebuild Shader Compiler Worker every time you build the editor.

* [android](https://dev.epicgames.com/community/search?query=android)
* [installed build](https://dev.epicgames.com/community/search?query=installed%20build)
* [binaries](https://dev.epicgames.com/community/search?query=binaries)
* [precompiled binaries](https://dev.epicgames.com/community/search?query=precompiled%20binaries)
* [hmi](https://dev.epicgames.com/community/search?query=hmi)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisites](/documentation/en-us/unreal-engine/create-an-installed-build-of-unreal-engine?application_version=5.7#prerequisites)
* [Recommended Hardware](/documentation/en-us/unreal-engine/create-an-installed-build-of-unreal-engine?application_version=5.7#recommended-hardware)
* [Windows 10 SDK (Windows 10 users only)](/documentation/en-us/unreal-engine/create-an-installed-build-of-unreal-engine?application_version=5.7#windows10sdk(windows10usersonly))
* [Make an Installed Build](/documentation/en-us/unreal-engine/create-an-installed-build-of-unreal-engine?application_version=5.7#make-an-installed-build)
* [Required Platforms](/documentation/en-us/unreal-engine/create-an-installed-build-of-unreal-engine?application_version=5.7#required-platforms)
* [Test the Installed Build Executable](/documentation/en-us/unreal-engine/create-an-installed-build-of-unreal-engine?application_version=5.7#test-the-installed-build-executable)
