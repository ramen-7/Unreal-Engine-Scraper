<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/use-clang-to-build-microsoft-platforms-in-unreal-engine?application_version=5.7 -->

# Use Clang to Build Microsoft Platforms

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
8. Use Clang to Build Microsoft Platforms

# Use Clang to Build Microsoft Platforms

Specify Clang options through build configuration, command-line arguments, or engine configuration.

![Use Clang to Build Microsoft Platforms](https://dev.epicgames.com/community/api/documentation/image/de76f1ff-1812-4b3a-9f65-25e74fdc1977?resizing_type=fill&width=1920&height=335)

 On this page

**Unreal Engine (UE)** supports using the **Clang** compiler on Windows to build [supported Microsoft platforms](https://dev.epicgames.com/documentation/en-us/unreal-engine/sharing-and-releasing-projects-for-unreal-engine). You can enable Clang with:

* [Build Configuration](https://dev.epicgames.com/documentation/en-us/unreal-engine/use-clang-to-build-microsoft-platforms-in-unreal-engine)
* [Command-Line Arguments](https://dev.epicgames.com/documentation/en-us/unreal-engine/use-clang-to-build-microsoft-platforms-in-unreal-engine)
* [Engine Configuration](https://dev.epicgames.com/documentation/en-us/unreal-engine/use-clang-to-build-microsoft-platforms-in-unreal-engine)

This page also includes a table of additional options, such as specifying:

* Clang linker
* Clang version
* MSVC version
* Toolchain version

For more information, see the [Additional Options](https://dev.epicgames.com/documentation/en-us/unreal-engine/use-clang-to-build-microsoft-platforms-in-unreal-engine) section below. As of UE 5.3, the latest supported version of Clang is [Clang 16](https://releases.llvm.org/16.0.0/tools/clang/docs/index.html).

## What is Clang

Clang is a front-end compiler that compiles C, C++, Objective-C, and Objective-C++ into machine code. Clang is an alternative to the MSVC (Microsoft Visual C++) compiler.

## Install Clang

You can install Clang through [Visual Studio](https://learn.microsoft.com/en-us/cpp/build/clang-support-msbuild?view=msvc-170) or directly from the [LLVM Downloads](https://releases.llvm.org/download.html) page.

## Enable Clang

Once you have installed Clang, follow any one of the methods below to enable Clang in your Unreal project.

### Build Configuration

To enable Clang in [Build Configuration](https://dev.epicgames.com/documentation/en-us/unreal-engine/build-configuration-for-unreal-engine), navigate to an engine `BuildConfiguration.xml` file, and add the following:

C++

```
|  |  |
| --- | --- |
|  | <?xml version="1.0" encoding="utf-8" ?> |
|  | <Configuration xmlns="https://www.unrealengine.com/BuildConfiguration"> |
|  | ... |
|  | <WindowsPlatform> |
|  | <Compiler>Clang</Compiler> |
|  | </WindowsPlatform> |
|  | ... |
|  | </Configuration> |
```

<?xml version="1.0" encoding="utf-8" ?>
<Configuration xmlns="https://www.unrealengine.com/BuildConfiguration">
...
<WindowsPlatform>
<Compiler>Clang</Compiler>
</WindowsPlatform>
...
</Configuration>

Copy full snippet(8 lines long)

### Command-Line Arguments

To enable Clang with [Command-Line Arguments](https://dev.epicgames.com/documentation/en-us/unreal-engine/command-line-arguments-in-unreal-engine), pass the `-Compiler=Clang` option.

### Engine Configuration

To enable Clang in [Engine Configuration](https://dev.epicgames.com/documentation/en-us/unreal-engine/configuration-files-in-unreal-engine), navigate to an engine configuration file, such as `DefaultEngine.ini`, and add the following:

C++

```
|  |  |
| --- | --- |
|  | [/Script/WindowsTargetPlatform.WindowsTargetSettings] |
|  | Compiler=Clang |
```

[/Script/WindowsTargetPlatform.WindowsTargetSettings]
Compiler=Clang

Copy full snippet(2 lines long)

## Additional Options

The following options assume that:

* Build Configuration options are added inside the `<WindowsPlatform>...</WindowsPlatform>` section of `BuildConfiguration.xml`.
* Engine Configuration options are added to the `[/Script/WindowsTargetPlatform.WindowsTargetSettings]` section of an engine configuration file, such as `DefaultEngine.ini`.

| Option | Build Configuration | Command-Line Argument | Engine Configuration |
| --- | --- | --- | --- |
| Clang linker | `<bAllowClangLinker>true</bAllowClangLinker>` | `-ClangLinker` | `bAllowClangLinker=true` |
| Clang Compiler Version | `<CompilerVersion>Latest</CompilerVersion>` | `-CompilerVersion=Latest` | `CompilerVersion=Latest` |
| MSVC Version | `<Toolchain>VisualStudio2022</VisualStudio>` | `-VCToolchain=VisualStudio2022` | `Toolchain=VisualStudio2022` |
| Toolchain Version | `<ToolchainVersion>Latest</ToolchainVersion>` | `-VCToolchainVersion=Latest` | `ToolchainVersion=Latest` |

### Clang Linker

The Clang Linker is a boolean option that determines whether the Clang Linker is used when compiling with Clang.

### Clang Compiler Version

The Clang compiler version is a string option that determines which version of the specified compiler is used. The options include:

* Specific version number: Use the exact version specified, for example, "16.0.0".
* Latest: Use the newest installed version.

### MSVC Version

The MSVC Toolchain is a string option that determines which toolchain is used. The options include:

* VisualStudio2022

### Toolchain Version

The Toolchain version is a string option that determines which version of the MSVC toolchain is used. The options include:

* Specific version number: Use the exact version specified, for example, "14.37.32822".
* Latest: Use the newest installed version.
* Preview: Use the newest installed preview version.

## More Information

Follow these links for information about:

* [Windows Platform](setting-up-your-production-pipeline/unreal-build-system/unreal-build-tool/build-configuration/#windowsplatform) section of [Build Configuration](setting-up-your-production-pipeline/unreal-build-system/unreal-build-tool/build-configuration)
* [Command-Line Arguments](https://dev.epicgames.com/documentation/en-us/unreal-engine/command-line-arguments-in-unreal-engine)
* [Engine Configuration Files](https://dev.epicgames.com/documentation/en-us/unreal-engine/configuration-files-in-unreal-engine)

* [programming](https://dev.epicgames.com/community/search?query=programming)
* [clang](https://dev.epicgames.com/community/search?query=clang)
* [microsoft](https://dev.epicgames.com/community/search?query=microsoft)
* [toolchain](https://dev.epicgames.com/community/search?query=toolchain)
* [linker](https://dev.epicgames.com/community/search?query=linker)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [What is Clang](/documentation/en-us/unreal-engine/use-clang-to-build-microsoft-platforms-in-unreal-engine?application_version=5.7#what-is-clang)
* [Install Clang](/documentation/en-us/unreal-engine/use-clang-to-build-microsoft-platforms-in-unreal-engine?application_version=5.7#install-clang)
* [Enable Clang](/documentation/en-us/unreal-engine/use-clang-to-build-microsoft-platforms-in-unreal-engine?application_version=5.7#enable-clang)
* [Build Configuration](/documentation/en-us/unreal-engine/use-clang-to-build-microsoft-platforms-in-unreal-engine?application_version=5.7#build-configuration)
* [Command-Line Arguments](/documentation/en-us/unreal-engine/use-clang-to-build-microsoft-platforms-in-unreal-engine?application_version=5.7#command-line-arguments)
* [Engine Configuration](/documentation/en-us/unreal-engine/use-clang-to-build-microsoft-platforms-in-unreal-engine?application_version=5.7#engine-configuration)
* [Additional Options](/documentation/en-us/unreal-engine/use-clang-to-build-microsoft-platforms-in-unreal-engine?application_version=5.7#additional-options)
* [Clang Linker](/documentation/en-us/unreal-engine/use-clang-to-build-microsoft-platforms-in-unreal-engine?application_version=5.7#clang-linker)
* [Clang Compiler Version](/documentation/en-us/unreal-engine/use-clang-to-build-microsoft-platforms-in-unreal-engine?application_version=5.7#clang-compiler-version)
* [MSVC Version](/documentation/en-us/unreal-engine/use-clang-to-build-microsoft-platforms-in-unreal-engine?application_version=5.7#msvc-version)
* [Toolchain Version](/documentation/en-us/unreal-engine/use-clang-to-build-microsoft-platforms-in-unreal-engine?application_version=5.7#toolchain-version)
* [More Information](/documentation/en-us/unreal-engine/use-clang-to-build-microsoft-platforms-in-unreal-engine?application_version=5.7#more-information)
