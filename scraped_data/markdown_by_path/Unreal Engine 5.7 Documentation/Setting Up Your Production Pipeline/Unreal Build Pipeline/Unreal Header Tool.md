<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-header-tool-for-unreal-engine?application_version=5.7 -->

# Unreal Header Tool

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
7. Unreal Header Tool

# Unreal Header Tool

UnrealHeaderTool (UHT) is a custom parsing and code-generation tool supporting the UObject system.

![Unreal Header Tool](https://dev.epicgames.com/community/api/documentation/image/c2687461-60db-4bc1-a9df-d039b8562546?resizing_type=fill&width=1920&height=335)

 On this page

## Overview of Unreal Header Tool

**Unreal Header Tool (UHT)** is a custom parsing and code generation tool for Unreal Engine. UHT parses and generates code for Unreal Engine's (UE) **UObject** system. Code compilation in Unreal Engine happens in two phases:

1. **Unreal Build Tool (UBT)** invokes UHT, which parses the C++ headers for Unreal-related class metadata and generates custom code to implement the various UObject-related features.
2. UBT invokes the configured C++ compiler to compile the results.

This page has information about:

* [Run UHT from Command-Line](/documentation/en-us/unreal-engine/unreal-header-tool-for-unreal-engine#uhtcommand-line)
* [Common Issues Running UHT](/documentation/en-us/unreal-engine/unreal-header-tool-for-unreal-engine#commonissuesrunninguht)
* [Extending UHT with Custom Script Generators](/documentation/en-us/unreal-engine/unreal-header-tool-for-unreal-engine#extendinguhtwithscriptgenerators)
* [UHT Command-Line Reference](/documentation/en-us/unreal-engine/unreal-header-tool-for-unreal-engine#uhtcommand-linereference)
* [Links to More Related Information](/documentation/en-us/unreal-engine/unreal-header-tool-for-unreal-engine#moreinformation)

## Run Unreal Header Tool

You are not required to run Unreal Header Tool (UHT) during a typical development workflow as this is taken care of internally by UBT. However, if you are creating a UHT plugin or making modifications to UHT, it can be valuable to run UHT separately.

This section explains how to run UHT manually.

### UHT Command-Line

UHT can be run in two different ways as:

* [Internal UBT Command](/documentation/en-us/unreal-engine/unreal-header-tool-for-unreal-engine#internalubtcommand)
* [UHT Development Command](/documentation/en-us/unreal-engine/unreal-header-tool-for-unreal-engine#uhtdevelopmentcommands)

#### Internal UBT Command

UBT uses the following command-line internally. UBT scans all header files looking for UHT keywords, then generates a manifest file containing all the modules and source files that UHT needs to parse.

```
RunUBT -Mode=UnrealHeaderTool "<PROJECT_FILE>" "<MANIFEST_FILE>" …
Copy full snippet
```

#### UHT Development Commands

You can use the following command-lines during UHT development or when running other exports. Instead of relying on a previously existing manifest file, UHT performs the same scanning UBT normally does, then generates the manifest automatically. UHT uses the same target specification as UBT when run in this mode.

```
RunUBT -Mode=UnrealHeaderTool "-Target=<TARGET> <PLATFORM> <CONFIGURATION>" …
Copy full snippet
```

```
RunUBT -Mode=UnrealHeaderTool "-Target=<TARGET> <PLATFORM> <CONFIGURATION> -Project=\"<PROJECT_FILE>\"" …
Copy full snippet
```

#### Logging Options

UHT supports the same logging options that UBT supports.

#### Error Handling

UHT has two options that affect error handling:

* Warnings As Error
* Fail If Generated Code Changes

UHT is normally run with `-WarningsAsError`. As the name implies, UHT returns an error code if it detects any warnings. The Hot Reload system uses `-FailIfGeneratedCodeChanges` to detect changes to generated code and returns an error if any are found.

##### Debugging

When debugging, UHT's heavy use of C# Tasks can make it difficult to debug. The `-NoGoWide` option disables the use of C# Tasks and runs UHT in a single thread of execution.

#### Exporters

Exporters are the mechanism that UHT uses to generate code and reports. By default, UHT runs the standard Codegen exporter and any enabled script generator exporters. UHT includes two sample exporters that aren't enabled by default:

* Json
* Stats

##### Enable an Exporter

To enable an exporter, use the `-<EXPORTER_NAME>` command-line arguments. To disable a normally enabled exporter, use the `-No<EXPORTER_NAME>` command-line arguments. The `-NoDefaultExporters` option disables all exporters that are enabled by default. This option is convenient when you want to run an exporter such as Stats independently of the default exporters.

##### Exporter Output

UHT can create a single directory of exporter outputs convenient for UHT development. The output of these options is located in the `Engine/Programs/UnrealHeaderTool/Saves` directory. Prior to doing UHT development, use the `-WriteRef` option to create a copy of all generated output. While iterating on modifications, use the `-VerifyRef` option to compare newly generated output with the output generated by `-WriteRef`. This ensures that there are no unexpected changes to the output.

Use the `-NoOutput` option to prevent UHT from writing the output to where it normally would.

### Common Issues Running UHT

#### Source Files Containing Only Delegates Don't Get Parsed

Unlike other statements, UHT automatically parses any `DECLARE_DYNAMIC_` delegates. However, if a header file only contains these delegates and no other UHT keywords, then UBT does not consider the header as something that needs to be parsed.

To get around this issue, use the `UDELEGATE` keyword above at least one of the delegates.

## Extending UHT With Script Generators

C# UHT supports the ability to define a script generator in a plugin. An example of this can be found in `Engine\Plugins\ScriptPlugin\Source\ScriptGeneratorUbtPlugin`.

UBT recognizes a plugin by the existence of a `<PLUGIN_NAME>.ubtplugin.csproj` C# project file name where `<PLUGIN_NAME>` is the name of your plugin. When you configure the C# project, instead of using project references, use assembly references for UBT and UHT in the `Engine\Binaries\DotNET\UnrealBuildTool` directory. This avoids issues with locked files when UBT builds the plugin.

While it is possible to use the same mechanisms in UHT to define specifiers, keywords, properties, and so on, only exporters are supported. Furthermore, exporters are limited to outputting files to the plugin's `Intermediate` directory. UBT does not compile any files generated by anything other than the standard Codegen exporter. For script generator plugins, compilation is usually done by way of a single generated `.inl` file that other C++ code in the plugin includes.

The `IUhtExportFactory` interface provides access back to UHT:

| **Method** | **Description** |
| --- | --- |
| `IUhtExportFactory.Session` | Provides access to the collection of packages and their defined types. Unlike C++ UHT, the tree of types contains all information about each type as parsed by UHT. |
| `IUhtExportFactory.CreateTask` | Create a task to export content or run directly if `-NoGoWide` has been specified. |
| `IUhtExportFactory.MakePath` | Generate file names to be passed to `CommitOutput`. |
| `IUhtExportFactory.CommitOutput` | Write the output to disk if and only if it has changed. If the `-WriteRef` or `-VerifyRef` option is used, then the files are also written there in a subdirectory based on the name of the exporter. |
| `IUhtExportFactory.AddExternalDependency` | Add files to be checked to see if UBT needs to re-run UHT. For example, a configuration file that changes the output can be added as an external dependency. |

### Enable UHT Exporter Extensions

Two things are required for UHT to recognize an extension:

* A class must include the `UnrealHeaderTool` class attribute.
* A function must include the `UhtExporter` method attribute.

When adding an exporter, the attribute must contain the following settings:

* **Name**: Name of the exporter. This name should be reasonably unique.
* **Options**: Set to default so that it is always run when the plugin is enabled.
* **ModuleName**: Name of the plugin module containing the exporter.

For an example, see the example in `ScriptGenerator.cs` located in `Engine\Plugins\ScriptPlugin\Source\ScriptGeneratorUbtPlugin`:

```
[UhtExporter(Name="ScriptPlugin", Description="Generic Script Plugin Generator", Options=UhtExporterOptions.Default, ModuleName="ScriptPlugin")]
Copy full snippet
```

There are other options which are either not required or reserved for Epic exporters. For example, the `Description` option in the sample above is not a required option.

### Other UHT Extensions

The `UnrealHeaderTool` class attribute is used for many more things than just exporters. Currently, script generator exporters are the only supported extension type.

The following attributes define important elements in UHT:

| **Attribute** | **Description** |
| --- | --- |
| `UhtKeword` | Tokens such as `UCLASS`. |
| `UhtSpecifier` | Specifiers. |
| `UhtSpecifierValidator` | Metadata validators. |
| `UhtPropertyType` | New property types. |
| `UhtStructDefaultValue` | Default values for `USTRUCT`. |
| `UhtLocTextDefaultValue` | Default values for `LOCTEXT` macros. |
| `UhtEngineClass` | Associates C# classes with different engine types. |

It is possible to add new specifiers, validators, and default values since they do not require code generation changes. Adding new engine types, property types, or keywords should be approached cautiously, as adding any of these requires a large number of changes to the engine to properly implement.

## UHT Command-Line Reference

### Options

| **Command-Line Argument** | **Description** |
| --- | --- |
| `-Verbose` | Increase log output verbosity. |
| `-VeryVerbose` | Maximize log output verbosity. |
| `-Log` | Specify a log file location. Without this argument, the default location is used: `Engine/Programs/UnrealHeaderTool/Saved/Logs/UnrealHeaderTool.log`. |
| `-Timestamps` | Include timestamps in the log. |
| `-FromMsBuild` | Format messages for the Microsoft Build Engine (MSBuild). |
| `-NoLog` | Disable log file creation, including the default log file. |
| `-Test` | Run test scripts. |
| `-WarningsAsErrors` | Treat warnings as errors. |
| `-NoGoWide` | Disable concurrent parsing and code generation. |
| `-WriteRef` | Write all output to a reference directory. |
| `-VerifyRef` | Write all output to a verification directory and compare it to the reference output. |
| `-FailIfGeneratedCodeChanges` | Consider any changes to output files as errors. |
| `-NoOutput` | Do not save any output files other than the reference output. |
| `-IncludeDebugOutput` | Include extra content in generated output to assist with debugging. |
| `-NoDefaultExporters` | Disable all default exporters. Useful for when a specific exporter needs to run. |

### Generators

| **Command-Line Argument** | **Description** |
| --- | --- |
| `-Stats` | Type stats. |
| `-NoStats` | Disable type stats. |
| `-Json` | Json description of packages. |
| `-NoJson` | Disable Json description of packages. |
| `-CodeGen` | Standard Unreal Engine code generator. This is the default generator. |
| `-NoCodeGen` | Disable the default Unreal Engine code generator. |

## More Information

### Unreal Engine Reflection System

For more information about the Unreal Engine Reflection System, including UObjects and their associated metadata specifiers, see the [Unreal Engine Reflection System](/documentation/en-us/unreal-engine/reflection-system-in-unreal-engine) documentation.

[![Unreal Engine Reflection System](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/53d5f4c5-5872-472c-8f69-911016aeca9b/reflectiontopichero.png)

Unreal Engine Reflection System

Information for programmers developing Objects to be used with Unreal Engine.](/documentation/en-us/unreal-engine/reflection-system-in-unreal-engine)

### Unreal Build Tool

For more information about the Unreal Engine build process and customizing your builds, see the [Unreal Build Tool](/documentation/en-us/unreal-engine/unreal-build-tool-in-unreal-engine) documentation.

[![UnrealBuildTool](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6e2c734a-9b81-4c58-a46d-230de6ba218d/placeholder_topic.png)

UnrealBuildTool

UnrealBuildTool (UBT) manages the process of building Unreal Engine source code across a variety of build configurations.](/documentation/en-us/unreal-engine/unreal-build-tool-in-unreal-engine)

* [programming](https://dev.epicgames.com/community/search?query=programming)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Overview of Unreal Header Tool](/documentation/en-us/unreal-engine/unreal-header-tool-for-unreal-engine?application_version=5.7#overviewofunrealheadertool)
* [Run Unreal Header Tool](/documentation/en-us/unreal-engine/unreal-header-tool-for-unreal-engine?application_version=5.7#rununrealheadertool)
* [UHT Command-Line](/documentation/en-us/unreal-engine/unreal-header-tool-for-unreal-engine?application_version=5.7#uhtcommand-line)
* [Internal UBT Command](/documentation/en-us/unreal-engine/unreal-header-tool-for-unreal-engine?application_version=5.7#internalubtcommand)
* [UHT Development Commands](/documentation/en-us/unreal-engine/unreal-header-tool-for-unreal-engine?application_version=5.7#uhtdevelopmentcommands)
* [Logging Options](/documentation/en-us/unreal-engine/unreal-header-tool-for-unreal-engine?application_version=5.7#loggingoptions)
* [Error Handling](/documentation/en-us/unreal-engine/unreal-header-tool-for-unreal-engine?application_version=5.7#errorhandling)
* [Debugging](/documentation/en-us/unreal-engine/unreal-header-tool-for-unreal-engine?application_version=5.7#debugging)
* [Exporters](/documentation/en-us/unreal-engine/unreal-header-tool-for-unreal-engine?application_version=5.7#exporters)
* [Enable an Exporter](/documentation/en-us/unreal-engine/unreal-header-tool-for-unreal-engine?application_version=5.7#enableanexporter)
* [Exporter Output](/documentation/en-us/unreal-engine/unreal-header-tool-for-unreal-engine?application_version=5.7#exporteroutput)
* [Common Issues Running UHT](/documentation/en-us/unreal-engine/unreal-header-tool-for-unreal-engine?application_version=5.7#commonissuesrunninguht)
* [Source Files Containing Only Delegates Don't Get Parsed](/documentation/en-us/unreal-engine/unreal-header-tool-for-unreal-engine?application_version=5.7#sourcefilescontainingonlydelegatesdon'tgetparsed)
* [Extending UHT With Script Generators](/documentation/en-us/unreal-engine/unreal-header-tool-for-unreal-engine?application_version=5.7#extendinguhtwithscriptgenerators)
* [Enable UHT Exporter Extensions](/documentation/en-us/unreal-engine/unreal-header-tool-for-unreal-engine?application_version=5.7#enableuhtexporterextensions)
* [Other UHT Extensions](/documentation/en-us/unreal-engine/unreal-header-tool-for-unreal-engine?application_version=5.7#otheruhtextensions)
* [UHT Command-Line Reference](/documentation/en-us/unreal-engine/unreal-header-tool-for-unreal-engine?application_version=5.7#uhtcommand-linereference)
* [Options](/documentation/en-us/unreal-engine/unreal-header-tool-for-unreal-engine?application_version=5.7#options)
* [Generators](/documentation/en-us/unreal-engine/unreal-header-tool-for-unreal-engine?application_version=5.7#generators)
* [More Information](/documentation/en-us/unreal-engine/unreal-header-tool-for-unreal-engine?application_version=5.7#moreinformation)
* [Unreal Engine Reflection System](/documentation/en-us/unreal-engine/unreal-header-tool-for-unreal-engine?application_version=5.7#unrealenginereflectionsystem)
* [Unreal Build Tool](/documentation/en-us/unreal-engine/unreal-header-tool-for-unreal-engine?application_version=5.7#unrealbuildtool)

Related documents

[Unreal Engine Reflection System

![Unreal Engine Reflection System](https://dev.epicgames.com/community/api/documentation/image/53d5f4c5-5872-472c-8f69-911016aeca9b?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/reflection-system-in-unreal-engine)

[UnrealBuildTool

![UnrealBuildTool](https://dev.epicgames.com/community/api/documentation/image/6e2c734a-9b81-4c58-a46d-230de6ba218d?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/unreal-build-tool-in-unreal-engine)
