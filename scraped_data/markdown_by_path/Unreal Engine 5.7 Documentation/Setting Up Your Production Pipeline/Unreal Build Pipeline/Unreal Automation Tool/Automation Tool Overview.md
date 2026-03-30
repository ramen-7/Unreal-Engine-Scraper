<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-automation-tool-overview-for-unreal-engine?application_version=5.7 -->

# Automation Tool Overview

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
8. Automation Tool Overview

# Automation Tool Overview

A host program and a set of utility libraries that enable you to script unattended processes related to Unreal Engine.

![Automation Tool Overview](https://dev.epicgames.com/community/api/documentation/image/456dc0ad-f44d-4087-9b20-3985dfbc1e50?resizing_type=fill&width=1920&height=335)

 On this page

**Automation Tool** is a host program and a set of utility libraries you can use to script unattended processes related to **Unreal Engine (UE)** when using C#. Internally, we use Automation Tool for a variety of tasks, including building, cooking, and running games, running automation tests, and scripting other operations to be executed on our build farm.

The source code for Automation Tool, and various scripts that run under it, can be found under `Engine/Source/Programs/AutomationTool`.

While we provide this tool as a courtesy, the level of support we can provide is limited.

## How Automation Tool Works

### Automation Projects

When run, Automation Tool finds all automation projects (saved as Visual Studio C# projects with an `.Automation.csproj` extension), compiles them, and then uses reflection to find the appropriate command to be executed. Those commands are implemented as classes derived from the `BuildCommand` base class, and are identified by the class name.

To learn more, read how to [add an automation project](/documentation/en-us/unreal-engine/create-an-automation-project-in-unreal-engine).

### Running Automation Tool

You can run commands under the Visual Studio debugger on Windows, or from the command line on Windows, Mac, and Linux.

#### Running Commands under the Debugger

To run Automation Tool under the Debugger in Visual Studio:

1. Right click the Automation Tool Project, and select **Properties** from the context menu.
2. Select the **Debug** tab, and enter your command name (here, we use `SampleCommand`) into the Start **Options > Command line arguments:** field.
   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5c407eb8-5712-4b10-9b92-01717901da17/automationtool_cmdlinearg.png)
3. Set a breakpoint in your script before pressing the F5 key (or clicking the **Start** button in the Visual Studio toolbar).

#### Running Commands from the command line (Windows)

To run Automation Tool from the command line:

1. Open a Command Prompt window.
2. Change the working directory to `Engine/Build/BatchFiles`.
3. Enter the following into the command line: `RunUAT.bat SampleCommand`

#### Running Commands from the terminal (Mac/Linux)

To run Automation Tool from the terminal:

1. Open the terminal.
2. Change the working directory to `Engine/Build/BatchFiles`.
3. Enter the following into the command line: `./RunUAT.sh SampleCommand`

### Command Line Syntax

The general syntax of the Automation Tool command line is:

```
	RunUAT.bat COMMAND_1 [-ARG_1 -ARG_2...] COMMAND_2 [-ARG_3 -ARG_4...] ...

Copy full snippet
```

Here, two commands will be run sequentially. `-ARG_1` and `-ARG_2` are passed to `COMMAND_1`, `-ARG_3` and `-ARG_4` are passed to `COMMAND_2`, and so on.

Global options:

| Option | Description |
| --- | --- |
| `-Help` | Shows help and options for Automation Tool in general, or (when specified after a command name) help for that particular command. |
| `-List` | Displays a list of all available Automation Tool commands. |
| `-P4` | Enable Perforce support. |
| `-Submit` | Allows automated processes to submit files. |
| `-NoCompile` | Prevents Automation Tool from compiling any `.Automation.csproj` files on startup. |

If set, the following environment variables are used to configure Perforce support for build machines. They may be set via the Automation Tool command line in the `VARNAME=VALUE` syntax or inherited from the current session.

| Environment Variable | Description |
| --- | --- |
| `uebp_PORT` | The Perforce server and port (for example, `perforce:1666`). |
| `uebp_CLIENT_ROOT` | Path to the local root directory of the current client (for example, `D:\P4`). |
| `uebp_CL` | The current changelist that is synced to. |
| `uebp_CodeCL` | The current code changelist that is synced to. This may be before the current changelist specified by `uebp_CL`. |
| `uebp_USER` | The Perforce user. |
| `uebp_CLIENT` | Name of the client used to access Perforce. |
| `uebp_BuildRoot_P4` | Path to the root of the current branch or stream (for example, `//UE4/Release-4.22`). |

* [programming](https://dev.epicgames.com/community/search?query=programming)
* [automationtool](https://dev.epicgames.com/community/search?query=automationtool)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [How Automation Tool Works](/documentation/en-us/unreal-engine/unreal-automation-tool-overview-for-unreal-engine?application_version=5.7#howautomationtoolworks)
* [Automation Projects](/documentation/en-us/unreal-engine/unreal-automation-tool-overview-for-unreal-engine?application_version=5.7#automationprojects)
* [Running Automation Tool](/documentation/en-us/unreal-engine/unreal-automation-tool-overview-for-unreal-engine?application_version=5.7#runningautomationtool)
* [Running Commands under the Debugger](/documentation/en-us/unreal-engine/unreal-automation-tool-overview-for-unreal-engine?application_version=5.7#runningcommandsunderthedebugger)
* [Running Commands from the command line (Windows)](/documentation/en-us/unreal-engine/unreal-automation-tool-overview-for-unreal-engine?application_version=5.7#runningcommandsfromthecommandline(windows))
* [Running Commands from the terminal (Mac/Linux)](/documentation/en-us/unreal-engine/unreal-automation-tool-overview-for-unreal-engine?application_version=5.7#runningcommandsfromtheterminal(mac/linux))
* [Command Line Syntax](/documentation/en-us/unreal-engine/unreal-automation-tool-overview-for-unreal-engine?application_version=5.7#commandlinesyntax)
