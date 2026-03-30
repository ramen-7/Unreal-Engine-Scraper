<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-version-binaries-in-unreal-engine?application_version=5.7 -->

# Versioning of Binaries

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
7. [UnrealBuildTool](/documentation/en-us/unreal-engine/unreal-build-tool-in-unreal-engine "UnrealBuildTool")
8. Versioning of Binaries

# Versioning of Binaries

Reference for Unreal Engine's BuildID system, which mitigates potential errors that may result from outdated DLL files.

![Versioning of Binaries](https://dev.epicgames.com/community/api/documentation/image/a27b4bed-7584-40f4-8874-0f4afb2c5745?resizing_type=fill&width=1920&height=335)

 On this page

The **Unreal Engine (UE)** **BuildID** system mitigates potential errors that may result from outdated DLL files. This system not only prevents crashes or failed library linkage, but also hard-to-track bugs that may arise from stale binaries, by loading only DLLs that were compiled at the same time as the executable file itself. The Build ID is typically generated automatically at compile-time, producing a new, unique value every time the Engine is built. However, you can override it with a manually specified value.

## Automatically-Generated Build ID

At build time, every output directory that contains at least one compiled DLL receives a JSON file with the `.modules` extension, such as `UnrealEditor.modules`. This file lists each Module in the directory and the associated DLL for that Module, as well as a GUID for the build itself. Every time the Engine compiles, it generates a new GUID, so that DLLs from other compilation sessions will be recognizable, and the Engine can ignore them. When using source control to maintaining a binary build, you must check in the executable, all DLLs, and their associated `.modules` files together to ensure that the Build ID matches.

## Manually-Specified Build ID

It is possible to force your Build ID to a specific value. You can accomplish this by adding a `BuildId` entry (as a string variable) to your `Build/Build.version` JSON file, but it is not recommended, as it removes the check to prevent using incompatible Modules. It is particularly easy to run outdated code if using a forced Build ID with Plugins that may be shared between multiple Projects.

* [programming](https://dev.epicgames.com/community/search?query=programming)
* [versioning](https://dev.epicgames.com/community/search?query=versioning)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Automatically-Generated Build ID](/documentation/en-us/unreal-engine/how-to-version-binaries-in-unreal-engine?application_version=5.7#automatically-generatedbuildid)
* [Manually-Specified Build ID](/documentation/en-us/unreal-engine/how-to-version-binaries-in-unreal-engine?application_version=5.7#manually-specifiedbuildid)
