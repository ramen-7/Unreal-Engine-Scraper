<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-visual-studio-development-environment-for-cplusplus-projects-in-unreal-engine?application_version=5.7 -->

# Setting Up Visual Studio

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
5. [Programming with C++](/documentation/en-us/unreal-engine/programming-with-cplusplus-in-unreal-engine "Programming with C++")
6. [Development Setup](/documentation/en-us/unreal-engine/setting-up-your-development-environment-for-cplusplus-in-unreal-engine "Development Setup")
7. Setting Up Visual Studio

# Setting Up Visual Studio

Tips, tricks, and techniques for setting up Visual Studio to work with Unreal Engine.

![Setting Up Visual Studio](https://dev.epicgames.com/community/api/documentation/image/1fee2c21-d787-499f-b2fa-d2bac2c6b6ac?resizing_type=fill&width=1920&height=335)

 On this page

Unreal Engine (UE) is designed to integrate smoothly with **Visual Studio** (VS), providing the means to quickly make code changes in your projects and immediately see results upon compilation. Setting up VS to work with UE can help improve developers' efficiency and overall user experience.

This document covers the basics for setting up your Unreal Engine-to-Visual Studio workflow.

## Version Compatibility

The following table lists which versions of VS are integrated with the binary version of UE.

| Unreal Engine Version | VS 2019 Version | VS 2022 Version |
| --- | --- | --- |
| 5.7 | Not supported | 17.8 or later, 17.14 recommended (Default) |
| 5.6 | Not supported | 17.8 or later, 17.14 recommended (Default) |
| **5.5** | Not supported | 17.8 or later, 17.10 recommended (Default) |
| **5.4** | Not supported | 17.4 or later, 17.8 recommended (Default) |
| **5.3** | 16.11.5 or later | 17.4 or later, 17.6 recommended (Default) |
| **5.2** | 16.11.5 or later | 17.4 or later (Default) |
| **5.1** | 16.11.5 or later (Default) | 17.4 or later |

Other software versions:

| Software | Minimum Version | Recommended Version |
| --- | --- | --- |
| **MSVC** | 14.44.35214 | 14.44.35214 |
| **Windows SDK** | 10.0.19041.0 | 10.0.22621.0 or newer |
| **LLVM** | 18.1.3 | 18.1.8 |
| **.NET** | .NET 8.0 | .NET 8.0 |

## Verifying UE Prerequisites

If you installed UE from the Epic Games Launcher or cloned it from GitHub, the UE Prerequisite Installer automatically installed the necessary dependencies, libraries, and frameworks required to run the engine.   
  
If you installed or synced UE from Perforce, run the Prerequisite Installer before running any UE tools you’ve built locally. Find the installer in `[UNREAL_ENGINE_ROOT]\Engine\Extras\Redist\en-us\.`

## Adding Visual Studio Installation Options

If you are installing Visual Studio (VS) for the first time or modifying an existing installation, ensure you have the following workloads and components enabled.

To modify your VS installation, run the Visual Studio Installer, then click **Modify** next to the latest version.

[![Modify button in the Visual Studio Installer](https://dev.epicgames.com/community/api/documentation/image/17ddf27a-e03b-4b90-95dd-9df35cba38e8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/17ddf27a-e03b-4b90-95dd-9df35cba38e8?resizing_type=fit)

### Adding Required Workloads

In the installer’s **Workloads** tab, under **Desktop & Mobile**, enable the following options:

* .NET desktop development
* Desktop development with C++
* .NET Multi-platform App UI development

Under **Gaming**, enable **Game development with C++**.

### Adding Required Components

In the installer’s **Installation Details** panel, expand **Game development with C++** and enable the following options:

* C++ profiling tools
* C++ AddressSanitizer
* Windows 10 or 11 SDK (10.0.18362 or Newer)
* Unreal Engine installer

[![Visual Studio Workloads and components to include in install](https://dev.epicgames.com/community/api/documentation/image/28753bf9-2392-424e-b224-a03643d9335b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/28753bf9-2392-424e-b224-a03643d9335b?resizing_type=fit)

Click to enlarge image.

When you open your first Unreal Engine C++ project in VS, you might see a missing-components warning in the **Solution Explorer**. Click **Install** to allow VS to install any additional components necessary for your project.

[![Visual Studio Solution Explorer warns about missing components](https://dev.epicgames.com/community/api/documentation/image/9d7b81fe-5a93-4af4-a42e-75ac4fe4c57c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9d7b81fe-5a93-4af4-a42e-75ac4fe4c57c?resizing_type=fit)

## Recommended Settings

These optional VS interface adjustments can make your development experience more convenient.

### Turning Off the Error List Window

Typically, the **Error List** window automatically opens when you have an error in your code. However, when working with UE, the Error List window can display additional downstream errors that make it difficult to identify the root cause. You can disable the Error List window and instead use the Output Log to see real code errors when working with UE.

To turn off the Error List window, follow these steps:

1. In VS, go to **Tools > Options**.
2. On the left side of the **Options** window, select **Projects and Solutions**.
3. Disable **Always show Error List if build finished with errors**.
4. (Optional) Change any other options and features from the table below that are relevant to your project.
5. Click **OK**.

| To: | In Options, go to: | And change this option: |
| --- | --- | --- |
| Prevent chunks of code from appearing grayed out in the text editor | **Text Editor > C/C++ > View** | Set **Show Inactive Blocks** to **False** |
| Hide unneeded folders in the Solution Explorer | **Text Editor > C/C++ > Advanced** | Set **Disable External Dependencies Folders** to **True** |
| Enable IntelliSense (code completion, suggestions, and automatic code formatting as you write) | **Text Editor > C/C++ > IntelliSense** | Turn on **Enable 64-bit IntelliSense** |

### Increasing the Width of Solution Configurations Dropdown Menu

You might find it useful to widen the Solution Configurations dropdown in the VS toolbar so you can view the full name of any custom configurations.

To widen the Solution Configurations menu, follow these steps:

1. In Visual Studio, right-click the main **toolbar** and select **Customize** at the bottom of the context menu.
2. In the **Customize** window, click the **Commands** tab, select the **Toolbar** radio button, and use the dropdown menu to change the **Toolbar** to **Standard**.

   [![In the Customize window, click Toolbar radio button and select Standard from the dropdown](https://dev.epicgames.com/community/api/documentation/image/0cf4ba42-ebd9-4056-8dd7-3a1184cd5b7c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0cf4ba42-ebd9-4056-8dd7-3a1184cd5b7c?resizing_type=fit)
3. In the toolbar **Preview**, scroll through the options to find and select **Solution Configurations**, then click **Modify Selection**.

   [![Click Solution Configurations and then click Modify Selection](https://dev.epicgames.com/community/api/documentation/image/32bd8a23-1b72-48c5-a434-c896680f6622?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/32bd8a23-1b72-48c5-a434-c896680f6622?resizing_type=fit)
4. Change the **Width** to **200** and click **OK**. VS updates the toolbar with its new size.
5. Close the **Customize** window.

### Adding the Solution Platforms Dropdown Menu

When developing for multiple platforms, it’s convenient to have the Solution Platforms dropdown menu in your VS toolbar.

If you don’t see this menu on the right side of the Solution Configurations dropdown, you can add it to the toolbar by clicking the small arrow button on the right side of the Standard toolbar, go to **Add or Remove Buttons**, and select **Solution Platforms**.

[![Visual Studio's main toolbar with Add More Buttons arrow highlighted](https://dev.epicgames.com/community/api/documentation/image/857bc198-4e0a-48ec-9049-fab518a57707?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/857bc198-4e0a-48ec-9049-fab518a57707?resizing_type=fit)

* [visual studio](https://dev.epicgames.com/community/search?query=visual%20studio)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Version Compatibility](/documentation/en-us/unreal-engine/setting-up-visual-studio-development-environment-for-cplusplus-projects-in-unreal-engine?application_version=5.7#version-compatibility)
* [Verifying UE Prerequisites](/documentation/en-us/unreal-engine/setting-up-visual-studio-development-environment-for-cplusplus-projects-in-unreal-engine?application_version=5.7#verifyingueprerequisites)
* [Adding Visual Studio Installation Options](/documentation/en-us/unreal-engine/setting-up-visual-studio-development-environment-for-cplusplus-projects-in-unreal-engine?application_version=5.7#addingvisualstudioinstallationoptions)
* [Adding Required Workloads](/documentation/en-us/unreal-engine/setting-up-visual-studio-development-environment-for-cplusplus-projects-in-unreal-engine?application_version=5.7#addingrequiredworkloads)
* [Adding Required Components](/documentation/en-us/unreal-engine/setting-up-visual-studio-development-environment-for-cplusplus-projects-in-unreal-engine?application_version=5.7#addingrequiredcomponents)
* [Recommended Settings](/documentation/en-us/unreal-engine/setting-up-visual-studio-development-environment-for-cplusplus-projects-in-unreal-engine?application_version=5.7#recommendedsettings)
* [Turning Off the Error List Window](/documentation/en-us/unreal-engine/setting-up-visual-studio-development-environment-for-cplusplus-projects-in-unreal-engine?application_version=5.7#turningofftheerrorlistwindow)
* [Increasing the Width of Solution Configurations Dropdown Menu](/documentation/en-us/unreal-engine/setting-up-visual-studio-development-environment-for-cplusplus-projects-in-unreal-engine?application_version=5.7#increasingthewidthofsolutionconfigurationsdropdownmenu)
* [Adding the Solution Platforms Dropdown Menu](/documentation/en-us/unreal-engine/setting-up-visual-studio-development-environment-for-cplusplus-projects-in-unreal-engine?application_version=5.7#addingthesolutionplatformsdropdownmenu)
