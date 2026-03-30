<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-use-buildgraph-for-unreal-engine?application_version=5.7 -->

# BuildGraph Usage

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
7. [Unreal Automation Tool](/documentation/en-us/unreal-engine/unreal-automation-tool-for-unreal-engine "Unreal Automation Tool")
8. BuildGraph Usage

# BuildGraph Usage

This page provides sample BuildGraph Script usage.

![BuildGraph Usage](https://dev.epicgames.com/community/api/documentation/image/4537c908-cc60-467f-820a-06fb94f51ff0?resizing_type=fill&width=1920&height=335)

 On this page

**\*BuildGraph** is an **Unreal Automation Tool** script for creating extensible build processes in Unreal Engine which can be run locally or in parallel across a build farm.

## Run From the Command-line

As an Unreal Automation Tool script, you can run BuildGraph directly in the command-line from the `Engine\Build\BatchFiles` directory through the `RunUAT` batch file or shell script depending on your platform.

### Windows

```
./RunUAT.bat BuildGraph [ARGUMENTS]
Copy full snippet
```

### Linux and Mac

```
./RunUAT.sh BuildGraph [ARGUMENTS]
Copy full snippet
```

## Example Scripts

The engine source contains a few example BuildGraph XML files for you to use. These files are located in the directory `Engine/Build/Graph/Examples`. These example files include the following:

* `AllExamples.xml`: This script is a combination of the scripts `Properties.xml`, `TagsAndFiles.xml`, and `Building.xml`.
* `BuildEditorAndTools.xml`: This script shows how to compile the tools and editor binaries required for artists to work with the engine, copy them to a staging directory for distribution, and optionally submit them to Perforce.
* `Building.xml`: This script compiles UnrealPak.
* `BuildWorldPartitionHLODs.xml`: This script builds world partition HLODs.
* `Macros.xml`: This script is an example for defining and using macros.
* `Properties.xml`: This script is an example for using various different BuildGraph properties.
* `TagsAndFiles.xml`: This script is an example for manipulating and interacting with files.

The XML Schema file that BuildGraph uses is named `Schema.xsd` and is located in `Engine/Build/Graph`.

## Example Commands

### All Available Nodes and Options

You can see all available nodes and options available in a BuildGraph script by executing the following:

```
./RunUAT.bat BuildGraph -Script=Engine/Build/Graph/Examples/AllExamples.xml -ListOnly
Copy full snippet
```

### Control Flow

You can see how control flow operates by executing the `Properties.xml` BuildGraph script:

```
./RunUAT.bat BuildGraph -Script=Engine/Build/Graph/Examples/Properties.xml -Target="Property Examples" -Clean
Copy full snippet
```

This script executes the conditionals that evaluate to true and outputs their corresponding messages. It also exhibits the behavior of several control flow statements that are described as part of the [BuildGraph Script Anatomy](/documentation/en-us/unreal-engine/buildgraph-script-anatomy-for-unreal-engine).

### Create an Installed Build of Unreal Engine

You can use the provided `InstalledEngineBuild.xml` BuildGraph script to create an installed build of UE for Windows with the following command:

```
./RunUAT.bat BuildGraph -Script=Engine/Build/InstalledEngineBuild.xml -Target="Make Installed Build Win64" -set:HostPlatformOnly=true -Clean
Copy full snippet
```

This creates an installed engine build that can be found in `<UNREAL_ENGINE_ROOT>/LocalBuilds/InstalledDDC/Engine/Binaries/Win64`.

## Command-line Arguments

BuildGraph supports a `-help` command to display help text in the command-line. To view the available `BuildGraph` arguments from the command-line, run:

```
./RunUAT.bat BuildGraph -help
Copy full snippet
```

### Custom Command-line Options

BuildGraph supports passing custom command-line options to your BuildGraph script. To define a custom option in your XML script, use:

```
<Option Name="NAME" Restrict="REGEX" DefaultValue="DEF_VAL" Description="DESCRIPTION"/>
Copy full snippet
```

The components of an option are as follows:

* `Name`: the name of the option to reference from the command-line.
* `Restrict`: a regular expression to restrict the accepted values.
* `DefaultValue`: the default value of the option if none is provided.
* `Description`: description of this option, including how it might be used.

You can then pass the option to your script from the command-line with:

```
-Set:<OPTION_NAME>=<OPTION_VALUE>
Copy full snippet
```

#### Example

Here is an example of an option defined in an XML script:

```
<Option Name="MyBooleanOption" Restrict="true|false" DefaultValue="false" Description="A boolean option for my BuildGraph script."/>
Copy full snippet
```

And this is how you can pass this option to your script from the command-line:

```
-Set:MyBooleanOption=true
Copy full snippet
```

### Reference

This table contains a list of command-line arguments available for use with BuildGraph when run from the command-line as:

```
./RunUAT.bat BuildGraph [ARGUMENTS]
Copy full snippet
```

| **Argument** | **Description** |
| --- | --- |
| `-Script=<FILE_NAME>` | Path to the script describing the graph. |
| `-Target=<NAME>` | Name of the node or output tag to be built. |
| `-Schema` | Generate a schema to the default location. |
| `-Schema=<FILE_NAME>` | Generate a schema describing valid script documents, including all known tasks. |
| `-ImportSchema=<FILE_NAME>` | Import a schema from an existing schema file. |
| `-Set:<PROPERTY>=<VALUE>` | Set a named `PROPERTY` to the given `VALUE`. |
| `-Branch=<VALUE>` | Override the auto-detection of the current branch. |
| `-Clean` | Clean all cached state of completed build nodes before running. |
| `-CleanNode=<NAME>[+<NAME>...]` | Clean the given nodes before running. |
| `-Resume` | Resume a local build from the last node that completed successfully. |
| `-ListOnly` | Show the content of the preprocessed graph, but do not execute it. |
| `-ShowDiagnostics` | When running with `-ListOnly`, cause diagnostic messages entered to be shown when parsing the graph. |
| `-ShowDeps` | Show node dependencies in the graph output. |
| `-ShowNotifications` | Show notifications that are sent for each node in the output. |
| `-Trigger=<NAME>` | Execute only nodes behind the given trigger. |
| `-SkipTrigger=<NAME>[+<NAME>...]` | Skip the given triggers, including all nodes behind them in the graph. |
| `-SkipTriggers` | Skip all triggers. |
| `-TokenSignature=<NAME>` | Specify the signature identifying the current job, to be written to tokens for modes that require them. Tokens are ignored if this parameter is not specified. |
| `-SkipTargetsWithoutTokens` | Exclude targets which we cannot acquire tokens for rather than failing. |
| `-Preprocess=<FILE_NAME>` | Write the preprocessed graph to the given file. |
| `-Export=<FILE_NAME>` | Export a JSON file containing the preprocessed build graph for use as part of a build system. |
| `-HordeExport=<FILE_NAME>` | Export a JSON file containing the full build graph for use by Horde. |
| `-PublicTasksOnly` | Only include built-in tasks in the schema, excluding any other UAT modules. |
| `-SharedStorageDir=<DIR_NAME>` | Set the directory to use to transfer build products between agents in a build farm. |
| `-SingleNode=<NAME>` | Run only the given node. Intended for use on a build system after running with `-Export`. |
| `-WriteToSharedStorage` | Allow writing to shared storage. If not set, but `-SharedStorageDir` is specified, build products will read, but not be written. |

* [programming](https://dev.epicgames.com/community/search?query=programming)
* [buildgraph](https://dev.epicgames.com/community/search?query=buildgraph)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Run From the Command-line](/documentation/en-us/unreal-engine/how-to-use-buildgraph-for-unreal-engine?application_version=5.7#runfromthecommand-line)
* [Windows](/documentation/en-us/unreal-engine/how-to-use-buildgraph-for-unreal-engine?application_version=5.7#windows)
* [Linux and Mac](/documentation/en-us/unreal-engine/how-to-use-buildgraph-for-unreal-engine?application_version=5.7#linuxandmac)
* [Example Scripts](/documentation/en-us/unreal-engine/how-to-use-buildgraph-for-unreal-engine?application_version=5.7#examplescripts)
* [Example Commands](/documentation/en-us/unreal-engine/how-to-use-buildgraph-for-unreal-engine?application_version=5.7#examplecommands)
* [All Available Nodes and Options](/documentation/en-us/unreal-engine/how-to-use-buildgraph-for-unreal-engine?application_version=5.7#allavailablenodesandoptions)
* [Control Flow](/documentation/en-us/unreal-engine/how-to-use-buildgraph-for-unreal-engine?application_version=5.7#controlflow)
* [Create an Installed Build of Unreal Engine](/documentation/en-us/unreal-engine/how-to-use-buildgraph-for-unreal-engine?application_version=5.7#createaninstalledbuildofunrealengine)
* [Command-line Arguments](/documentation/en-us/unreal-engine/how-to-use-buildgraph-for-unreal-engine?application_version=5.7#command-linearguments)
* [Custom Command-line Options](/documentation/en-us/unreal-engine/how-to-use-buildgraph-for-unreal-engine?application_version=5.7#customcommand-lineoptions)
* [Example](/documentation/en-us/unreal-engine/how-to-use-buildgraph-for-unreal-engine?application_version=5.7#example)
* [Reference](/documentation/en-us/unreal-engine/how-to-use-buildgraph-for-unreal-engine?application_version=5.7#reference)
