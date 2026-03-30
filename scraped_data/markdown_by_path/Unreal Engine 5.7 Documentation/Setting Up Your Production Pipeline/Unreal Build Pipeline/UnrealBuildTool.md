<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-build-tool-in-unreal-engine?application_version=5.7 -->

# UnrealBuildTool

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
6. [Unreal Build Pipeline](/documentation/en-us/unreal-engine/using-the-unreal-engine-build-pipeline "Unreal Build Pipeline")
7. UnrealBuildTool

# UnrealBuildTool

UnrealBuildTool (UBT) manages the process of building Unreal Engine source code across a variety of build configurations.

![UnrealBuildTool](https://dev.epicgames.com/community/api/documentation/image/83c0f281-b76b-4300-ac56-8d48e2f79751?resizing_type=fill&width=1920&height=335)

 On this page

**UnrealBuildTool (UBT)** is a custom tool that manages the process of building **Unreal Engine (UE)** source code across a variety of build configurations. Read  `BuildConfiguration.cs` to explore various user-configurable build options.

## Modular Architecture

UE is split into many modules. Each module has a `.build.cs` file that controls how it is built, including options for defining module dependencies, additional libraries, include paths, etc. By default, these modules are compiled into DLLs and loaded by a single executable. You can choose to build a monolithic executable in the `BuildConfiguration.cs` file.

It is important to understand that the build process executes independently of any project files for the development environment, such as `.sln` or `.vcproj` files (for Visual Studio). These files are useful to have for editing purposes though, so there is a tool being provided to generate them dynamically (based on the contents of your project directory tree). You can run this tool with the `GenerateProject.bat` file located in your `[Unreal Engine Root Directory]`.

**Note:** Running `GenerateProject.bat` from time-to-time will keep your code editor up-to-date with files that are being added to (or being removed) from disk.

## Topics

[![Targets](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/eb06ef2c-483e-44ec-bca3-644ec733ed4d/placeholder_topic.png)

Targets

An overview of UBT Targets, including property descriptions.](/documentation/en-us/unreal-engine/unreal-engine-build-tool-target-reference)
[![Module Properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2d30daa8-27e8-4e55-82f1-b1d0307ccafb/placeholder_topic.png)

Module Properties

An overview of Unreal Build Tool Modules, including property descriptions.](/documentation/en-us/unreal-engine/module-properties-in-unreal-engine)
[![Build Configuration](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/29891828-ff9f-427d-8f9d-6f4a87757d51/topic_buildconfigprops.png)

Build Configuration

Configure how the engine is built.](/documentation/en-us/unreal-engine/build-configuration-for-unreal-engine)
[![Include What You Use](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dd3169c7-7e89-48c9-9d05-6c40ad6a950c/topic_iwyu.png)

Include What You Use

A brief overview of the code base for Unreal Engine, using an Include-What-You-Use (IWYU) dependency model.](/documentation/en-us/unreal-engine/include-what-you-use-iwyu-for-unreal-engine-programming)
[![Project Files for IDEs](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9e8e742e-4fde-4d6e-9cea-92805538c494/topic_prjfilegen.png)

Project Files for IDEs

A guide to automatically generate project files for games and modules in the current workspace.](/documentation/en-us/unreal-engine/how-to-generate-unreal-engine-project-files-for-your-ide)
[![Versioning of Binaries](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0cd9ac40-0c28-41ed-9a63-178ef2933993/placeholder_topic.png)

Versioning of Binaries

Reference for Unreal Engine's BuildID system, which mitigates potential errors that may result from outdated DLL files.](/documentation/en-us/unreal-engine/how-to-version-binaries-in-unreal-engine)
[![Third-Party Libraries](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b962e7e4-3da3-4ed0-a5ed-2eb13b565887/placeholder_topic.png)

Third-Party Libraries

Integrating third-party libraries into Unreal Engine](/documentation/en-us/unreal-engine/integrating-third-party-libraries-into-unreal-engine)
[![Static Code Analysis](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/589894e9-b38b-4024-92eb-58b26e75791b/placeholder_topic.png)

Static Code Analysis

Unreal Build Tool supports running a variety of static code analyzers.](/documentation/en-us/unreal-engine/static-code-analysis-in-unreal-engine)
[![Use Clang to Build Microsoft Platforms](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2e74d2c5-027a-456e-b1f6-21bc4d3d30c2/placeholder_topic.png)

Use Clang to Build Microsoft Platforms

Specify Clang options through build configuration, command-line arguments, or engine configuration.](/documentation/en-us/unreal-engine/use-clang-to-build-microsoft-platforms-in-unreal-engine)

* [programming](https://dev.epicgames.com/community/search?query=programming)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Modular Architecture](/documentation/en-us/unreal-engine/unreal-build-tool-in-unreal-engine?application_version=5.7#modulararchitecture)
* [Topics](/documentation/en-us/unreal-engine/unreal-build-tool-in-unreal-engine?application_version=5.7#topics)
