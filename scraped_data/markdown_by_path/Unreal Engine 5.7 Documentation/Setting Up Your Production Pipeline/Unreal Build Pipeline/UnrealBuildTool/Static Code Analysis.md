<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/static-code-analysis-in-unreal-engine?application_version=5.7 -->

# Static Code Analysis

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
8. Static Code Analysis

# Static Code Analysis

Unreal Build Tool supports running a variety of static code analyzers.

![Static Code Analysis](https://dev.epicgames.com/community/api/documentation/image/c4dd6629-9c19-4fad-94a4-a2bb069bdb7d?resizing_type=fill&width=1920&height=335)

 On this page

**Unreal Build Tool (UBT)** supports running several different static code analyzers. **Static Code Analyzers** use a variety of algorithms and techniques to inspect source code and find bugs without executing the code. This means faster analysis, earlier detection of memory leaks and logic errors, and reduced technical debt.

## Use a Static Code Analyzer with UBT

The general command-line syntax for running a static code analyzer with UBT from your Unreal Engine root directory is:

```
Engine\Build\BatchFiles\RunUBT.bat TARGET PLATFORM Development -StaticAnalyzer=ANALYZER
Copy full snippet
```

`TARGET`, `PLATFORM`, and `ANALYZER` are required arguments in the above command you must replace with your desired values.

* `TARGET`: A build target supported by UBT, see the documentation on [Targets](/documentation/en-us/unreal-engine/unreal-engine-build-tool-target-reference) for more information.
* `PLATFORM`: A platform supported by Unreal Engine. Visit the [General Platform Support](/documentation/en-us/unreal-engine/tools-for-general-platform-support-in-unreal-engine) pages to learn about Unreal Engine platform support.
* `ANALYZER`: A static code analyzer that UBT uses to analyze the provided target on the designated platform. Refer to the [Supported Analyzers](/documentation/en-us/unreal-engine/static-code-analysis-in-unreal-engine#supportedanalyzers) section below to view the available options.

### Supported Analyzers

| Analyzer | Description |
| --- | --- |
| Default | Default static analyzer for the selected compiler (if it has one). |
| VisualCpp | Built-in Visual C++ static analyzer. Only supported for Microsoft Visual C++ (MSVC) based platforms. |
| PVSStudio | VS-Studio static analyzer. Only supported for MSVC-based platforms.  PVS-Studio requires a license file placed next to the installed `PVS-Studio.exe` executable. For more information about PVS-Studio and obtaining a license, visit the [PVS-Studio](https://pvs-studio.com/) documentation. |
| Clang | Clang static analyzer. This forces the compiler to Clang for MSVC-based platforms.  As of UE 5.3, Clang static analysis requires you to build with the `-DisableUnity` flag. No warnings are reported if this flag is omitted. As a result of this, if you analyze the engine with `-DisableUnity`, there are additional warnings that we are actively working on resolving that might be unrelated to your project code.  One way to reduce the number of warnings is to focus Clang static analysis on a specific module by using the command-line argument `-Module=<PROJECT_MODULE>`. |

### Examples

Run the following command from your Unreal Engine root directory to use the default static code analyzer with Unreal Editor as the target on a Windows 64-bit platform:

```
Engine\Build\BatchFiles\RunUBT.bat UnrealEditor Win64 Development -StaticAnalyzer=Default
Copy full snippet
```

Run the following command from your Unreal Engine root directory to use the Visual C++ static code analyzer with the Lyra Starter Game as the target on a Windows 64-bit platform:

```
Engine\Build\BatchFiles\RunUBT.bat LyraGame Win64 Development -StaticAnalyzer=VisualCpp
Copy full snippet
```

### Command-line Options for Clang Analyzer

| Option | Description |
| --- | --- |
| `-StaticAnalyzerOutputType=html` | Writes out web pages with navigation that describe the analysis warnings. These HTML files are written into the appropriate folders within the `Engine/Intermediate/Build` directory for the selected platform and target. |
| `-StaticAnalyzerMode=shallow` | Enables shallow analysis. This means analysis completes more quickly, but is less informative than standard analysis. We do not recommend using this mode for general purposes. |
| `-StaticAnalyzerChecker=CHECKER` | Provides a list of static analyzer checkers that you want to enable rather than the default list. |
| `-StaticAnalyzerDisableChecker=CHECKER` | Disables static analyzer default checkers. This option overrides the default disabled checkers which are `deadcode.DeadStores` and `security.FloatLoopCounter`. This option is unused if `-StaticAnalyzerChecker` is set. |
| `-StaticAnalyzerAdditionalChecker=CHECKER` | Enables additional non-default static analyzer checkers. This option is unused if `-StaticAnalyzerChecker` is set. |

For a full list of Clang analyzer checkers, see [Available Checkers](https://clang.llvm.org/docs/analyzer/checkers.html) in the Clang documentation.

* [programming](https://dev.epicgames.com/community/search?query=programming)
* [code analysis](https://dev.epicgames.com/community/search?query=code%20analysis)
* [analyzer](https://dev.epicgames.com/community/search?query=analyzer)
* [clang](https://dev.epicgames.com/community/search?query=clang)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Use a Static Code Analyzer with UBT](/documentation/en-us/unreal-engine/static-code-analysis-in-unreal-engine?application_version=5.7#useastaticcodeanalyzerwithubt)
* [Supported Analyzers](/documentation/en-us/unreal-engine/static-code-analysis-in-unreal-engine?application_version=5.7#supportedanalyzers)
* [Examples](/documentation/en-us/unreal-engine/static-code-analysis-in-unreal-engine?application_version=5.7#examples)
* [Command-line Options for Clang Analyzer](/documentation/en-us/unreal-engine/static-code-analysis-in-unreal-engine?application_version=5.7#command-lineoptionsforclanganalyzer)
