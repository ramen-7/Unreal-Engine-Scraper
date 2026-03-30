<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/building-unreal-engine-from-source?application_version=5.7 -->

# Building Unreal Engine from Source

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
5. [Get Started](/documentation/en-us/unreal-engine/get-started "Get Started")
6. [Install Unreal Engine](/documentation/en-us/unreal-engine/install-unreal-engine "Install Unreal Engine")
7. [Downloading Unreal Engine Source Code from GitHub](/documentation/en-us/unreal-engine/downloading-source-code-in-unreal-engine "Downloading Unreal Engine Source Code from GitHub")
8. Building Unreal Engine from Source

# Building Unreal Engine from Source

Compiling Unreal Engine from source code.

![Building Unreal Engine from Source](https://dev.epicgames.com/community/api/documentation/image/1422a50b-1403-4ff4-9149-0cb0e36ee23a?resizing_type=fill&width=1920&height=335)

###### Prerequisite topics

In order to understand and use the content on this page, make sure you are familiar with the following topics:

* [Downloading Unreal Engine Source Code](/documentation/en-us/unreal-engine/downloading-source-code-in-unreal-engine)
* [Installing Unreal Engine](/documentation/en-us/unreal-engine/installing-unreal-engine)

 On this page

Operating System 

×Windows

Select an option from the dropdown to see content relevant to it.

## Building Unreal Engine from Source

Read about [Hardware and Software Specifications](https://dev.epicgames.com/documentation/en-us/unreal-engine/hardware-and-software-specifications-for-unreal-engine?application_version=5.5), and make sure that **Microsoft Visual Studio** is installed prior to building **Unreal Engine (UE)** from source. Also, depending on your system's specifications, it may take between 10 and 40 minutes to compile the Engine.

1. Inside the root directory, where you [downloaded and adjusted the UE Source Code](https://dev.epicgames.com/documentation/en-us/unreal-engine/downloading-source-code-in-unreal-engine#downloading-the-source-code) run `GenerateProjectFiles.bat` to set-up your project files.

   [![Generate project files](https://dev.epicgames.com/community/api/documentation/image/5811d4a1-3f26-416b-8dba-b09fd5392af6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5811d4a1-3f26-416b-8dba-b09fd5392af6?resizing_type=fit)

   All project files are intermediate (`[UERoot]\Engine\Intermediate\ProjectFiles`). You must generate project files each time you sync a new build to ensure they are up to date. If you delete your `Intermediate` folder, you must regenerate project files using the `GenerateProjectFiles` batch file.
2. Load the project into Visual Studio by double-clicking `UE5.sln`.

   [![Load the project](https://dev.epicgames.com/community/api/documentation/image/ec3836b4-dd49-46d3-99ea-4f16335ca57d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ec3836b4-dd49-46d3-99ea-4f16335ca57d?resizing_type=fit)
3. Set your solution configuration to **Development Editor**.

   [![Set solution configuration to Development Editor](https://dev.epicgames.com/community/api/documentation/image/41110de2-2463-4416-b584-a3dd94b23e5a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/41110de2-2463-4416-b584-a3dd94b23e5a?resizing_type=fit)
4. Set your solution platform to **Win64**.

   [![Set solution platform to Win64](https://dev.epicgames.com/community/api/documentation/image/dc34475c-5847-48ce-94e5-6458e3f01504?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dc34475c-5847-48ce-94e5-6458e3f01504?resizing_type=fit)
5. Right-click the **UE5** target and select **Build**.

   [![Build the UE target](https://dev.epicgames.com/community/api/documentation/image/f58079aa-393a-4c4a-b3f3-c36957549ebd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f58079aa-393a-4c4a-b3f3-c36957549ebd?resizing_type=fit)

## Running the Editor

1. Set your startup project by right-clicking the **UE5** target and selecting **Set as StartUp Project**.

   [![Set as Startup Project](https://dev.epicgames.com/community/api/documentation/image/17b98744-84b8-4a22-8cf0-8e30851abcc9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/17b98744-84b8-4a22-8cf0-8e30851abcc9?resizing_type=fit)
2. Right-click the **UE5** project, then select **Debug > Start New Instance** to launch the Editor.

   [![Start New Instance](https://dev.epicgames.com/community/api/documentation/image/3faf0f64-cfa3-47ca-977c-1714fbe7aa26?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3faf0f64-cfa3-47ca-977c-1714fbe7aa26?resizing_type=fit)

   Alternatively, you can **press the F5 key** on your keyboard to start a new instance of the Editor.
3. Congratulations! You've compiled and launched the Engine from source.

## Getting Started with Unreal Engine

Learn how to use Unreal Engine by referring to the [Understanding the Basics](https://dev.epicgames.com/documentation/en-us/unreal-engine/understanding-the-basics-of-unreal-engine) documentation!

If you're looking to quickly get started with UE, refer to the following tutorials:

* [Programming Quick Start](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-cpp-quick-start)
* [Level Designer Quick Start](https://dev.epicgames.com/documentation/en-us/unreal-engine/level-designer-quick-start-in-unreal-engine)

UE's in-editor help features are a great way to get your questions answered.

* [programming](https://dev.epicgames.com/community/search?query=programming)
* [unreal build system](https://dev.epicgames.com/community/search?query=unreal%20build%20system)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Building Unreal Engine from Source](/documentation/en-us/unreal-engine/building-unreal-engine-from-source?application_version=5.7#building-unreal-engine-from-source)
* [Running the Editor](/documentation/en-us/unreal-engine/building-unreal-engine-from-source?application_version=5.7#runningtheeditor)
* [Getting Started with Unreal Engine](/documentation/en-us/unreal-engine/building-unreal-engine-from-source?application_version=5.7#gettingstartedwithunrealengine)

Related documents

[Understanding the Basics

![Understanding the Basics](https://dev.epicgames.com/community/api/documentation/image/31b32dc6-f266-4e2b-9c87-5cc50ca8e533?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/understanding-the-basics-of-unreal-engine)

[Programming Quick Start

![Programming Quick Start](https://dev.epicgames.com/community/api/documentation/image/7f50ff49-43a0-454f-b37e-51425406b08f?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/unreal-engine-cpp-quick-start)

[Level Designer Quick Start

![Level Designer Quick Start](https://dev.epicgames.com/community/api/documentation/image/dafacbc5-7b21-4f6b-aeb3-196fdab47bf5?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/level-designer-quick-start-in-unreal-engine)

[Unreal Build Pipeline

![Unreal Build Pipeline](https://dev.epicgames.com/community/api/documentation/image/407151ed-0efe-4205-ab74-43bd3270c4dc?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/using-the-unreal-engine-build-pipeline)
