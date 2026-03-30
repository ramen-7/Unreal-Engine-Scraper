<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/debugging-the-shader-compile-process-in-unreal-engine?application_version=5.7 -->

# Debugging the Shader Compile Process

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
5. [Designing Visuals, Rendering, and Graphics](/documentation/en-us/unreal-engine/designing-visuals-rendering-and-graphics-with-unreal-engine "Designing Visuals, Rendering, and Graphics")
6. [Graphics Programming](/documentation/en-us/unreal-engine/graphics-programming-for-unreal-engine "Graphics Programming")
7. [Shader Development](/documentation/en-us/unreal-engine/shader-development-in-unreal-engine "Shader Development")
8. Debugging the Shader Compile Process

# Debugging the Shader Compile Process

An overview of debugging the shader compile process.

![Debugging the Shader Compile Process](https://dev.epicgames.com/community/api/documentation/image/e35357e9-3051-486f-bda2-02e917b9d581?resizing_type=fill&width=1920&height=335)

 On this page

During development, it's a good idea to take a look at what exactly Unreal Engine is sending to the platform's shader compiler. The information contained in this page will enable you to debug any issues associated with it.

## Building ShaderCompileWorker in Debug Mode

By default, [UnrealBuiltTool](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-build-tool-in-unreal-engine) (UBT) generates projects for tools, they always compile in **Development** mode. For the purposes of debugging, you'll want to build the engine and projects in **Debug** mode. This mode contains symbols for debugging your project's code.

To build your project in **Debug** mode, perform the following actions:

[![](https://dev.epicgames.com/community/api/documentation/image/164a8d2c-c32f-4c3f-9cd3-46cf01b2ea25?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/164a8d2c-c32f-4c3f-9cd3-46cf01b2ea25?resizing_type=fit)

1. Change your **Solution** properties in Visual Studio using the **Configuration Manager**, which can be opened from the **Build** menu.
2. Set the **ShaderCompileWorker (SCW)** dropdown to **Debug\_Program**.

For additional information about these targets, see [Build Configurations Reference.](https://dev.epicgames.com/documentation/en-us/unreal-engine/build-configurations-reference-for-unreal-engine?application_version=5.5)

## Generating Shader Debug Info Files

In order to debug your shaders, you'll first need to generate the files that can be used to debug the compile process. This requires enabling the console variables for dumping intermediate shaders to allow subsequent compilations to dump out generated files.

You will find some predefined console variables in your **ConsoleVariables.ini** configuration file, contained in the `Engine/Config` folder.

The following is the pertinent one for enabling debug information:

Config

```
|  |  |
| --- | --- |
|  | ; Dump shaders in the Saved folder |
|  | ;  Mode 1: dump all. WARNING: leaving this on for a while will fill your hard drive with many small files and folders. |
|  | ;  Mode 2: dump on compilation failure only (default). |
|  | ;  Mode 3: dump on compilation failure or warnings. |
|  | r.DumpShaderDebugInfo=1 |
```

; Dump shaders in the Saved folder
; Mode 1: dump all. WARNING: leaving this on for a while will fill your hard drive with many small files and folders.
; Mode 2: dump on compilation failure only (default).
; Mode 3: dump on compilation failure or warnings.
r.DumpShaderDebugInfo=1

Copy full snippet(5 lines long)

As the comments above indicate, by default the debug information is written for any shader compile jobs, which results in an error being generated. However, you the debug information can optionally be written always (1) or any time warnings or errors are encountered (3).

Modifying console variables intentionally does not invalidate shaders, so a recompile will not occur automatically once you change this value. Instead, you'll need to force a rebuild of any shaders for which you want to obtain debug information.

You can force a rebuild of all shaders by generating a GUID and replacing the one found in `Engine/Shaders/Public/ShaderVersion.ush`. Then, re-run the editor (or cook, or any other process that compiles shaders) to complete this process. The version change will trigger a recompile of all shaders encountered during the editor run and dump all the intermediate files in your project's `Saved/ShaderDebugInfo` folder.

You can also add a temporary line of code, like the following, to any shader source file to force a rebuild of any shaders which include that file:

C++

```
#pragma message("UESHADERMETADATA_VERSION 3F6B6BB8-21E5-42E7-BB92-4105AC3B7F02")
```

#pragma message("UESHADERMETADATA\_VERSION 3F6B6BB8-21E5-42E7-BB92-4105AC3B7F02")

Copy full snippet(1 line long)

## Shader Debug Info Folder Structure

The folder path generated by the dumped shader includes relevant information and allows you to quickly navigate to a specific shader. Various log messages will also include references to the debug info path for specific jobs (such as, when a specific job fails).

Below are some examples of dumped shader paths.

Console Output

```
|  |  |
| --- | --- |
|  | D:\UE5\Samples\Games\Lyra\Saved\ShaderDebugInfo\PCD3D_SM6\Global\FClusteredShadingPS\0 |
|  | D:\UE5\Samples\Games\Lyra\Saved\ShaderDebugInfo\PCD3D_SM6\M_Sparks_Base_2bc7668f760b8ef1\Default\FLocalVertexFactory\TBasePassPSFNoLightMapPolicy\0_6bf23011a88a16c6 |
|  | D:\UE5\Samples\Games\Lyra\Saved\ShaderDebugInfo\PCD3D_SM6\M_Sparks_Base_2bc7668f760b8ef1\Default\VelocityPipeline\FLocalVertexFactory\FVelocityPS\0_6bf23011a88a16c6 |
```

D:\UE5\Samples\Games\Lyra\Saved\ShaderDebugInfo\PCD3D\_SM6\Global\FClusteredShadingPS\0
D:\UE5\Samples\Games\Lyra\Saved\ShaderDebugInfo\PCD3D\_SM6\M\_Sparks\_Base\_2bc7668f760b8ef1\Default\FLocalVertexFactory\TBasePassPSFNoLightMapPolicy\0\_6bf23011a88a16c6
D:\UE5\Samples\Games\Lyra\Saved\ShaderDebugInfo\PCD3D\_SM6\M\_Sparks\_Base\_2bc7668f760b8ef1\Default\VelocityPipeline\FLocalVertexFactory\FVelocityPS\0\_6bf23011a88a16c6

Copy full snippet(3 lines long)

Analyzing this data, all of these paths share some common parts:

* The root shader debug info path `D:\UE5\Samples\Games\Lyra\Saved\ShaderDebugInfo`

  + The shader format as a string `PCD3D_SM6`.

    - All debug info for shaders compiled for this shader format will be saved in this folder structure. If compiling multiple shader formats at once, you'll see multiple folders listed here.
  + Note that this can be optionally overridden by setting the console variable `r.OverrideShaderDebugDir`.

From this point, the folder structure is different for **Global** and **Material** shaders. Have a look at the Global shader example first:

Console Output

```
D:\UE5\Samples\Games\Lyra\Saved\ShaderDebugInfo\PCD3D_SM6\Global\FClusteredShadingPS\0
```

D:\UE5\Samples\Games\Lyra\Saved\ShaderDebugInfo\PCD3D\_SM6\Global\FClusteredShadingPS\0

Copy full snippet(1 line long)

The remaining components of this path are as follows:

* The debug group name for the shader.

  + The name of the `FGlobalShaderType` subclass which defines these shaders is `FClusteredShadingPS`.
  + The integer permutation ID of the specific shader `0`.

    - This is a unique ID within the shader type which represents a specific combination of permutation `#defines`.
  + For global shaders, this is always `Global.`

The next part is the material shaders from the examples above:

Console Output

```
|  |  |
| --- | --- |
|  | D:\UE5\Samples\Games\Lyra\Saved\ShaderDebugInfo\PCD3D_SM6\ M_Sparks_Base_2bc7668f760b8ef1\Default\FLocalVertexFactory\TBasePassPSFNoLightMapPolicy\0_6bf23011a88a16c6 |
|  | D:\UE5\Samples\Games\Lyra\Saved\ShaderDebugInfo\PCD3D_SM6\M_Sparks_Base_2bc7668f760b8ef1\Default\VelocityPipeline\FLocalVertexFactory\FVelocityPS\0_6bf23011a88a16c6 |
```

D:\UE5\Samples\Games\Lyra\Saved\ShaderDebugInfo\PCD3D\_SM6\ M\_Sparks\_Base\_2bc7668f760b8ef1\Default\FLocalVertexFactory\TBasePassPSFNoLightMapPolicy\0\_6bf23011a88a16c6
D:\UE5\Samples\Games\Lyra\Saved\ShaderDebugInfo\PCD3D\_SM6\M\_Sparks\_Base\_2bc7668f760b8ef1\Default\VelocityPipeline\FLocalVertexFactory\FVelocityPS\0\_6bf23011a88a16c6

Copy full snippet(2 lines long)

The remaining components of these paths are as follows:

* The material debug group name `M_Sparks_Base_2bc7660b8ef1`.

  + Note that this has reflects the state of the material, including the values of all static parameters but not the state of the shader source. So, modifications of the latter don't cause new debug folder names to be generated. This has the effect of duplicating debug output for two material instances with the same base material and the same static parameter values.
  + Optionally, the name of the shader pipeline for the shader, if it exists. This is defined in code with `IMPLEMENT_SHADERPIPELINE_TYPE_*` macros.

    - The vertex factory C++ class name is `FLocalVertexFactory`.
    - The shader type C++ class name is 
      `TBasePassPSFNoLightMapPolicy`.
    - The permutation ID `0` and a truncated version of the base material StateID guid `6bf23011a88a16c6`
    - Note that only the second material path is for a shader contained in a pipeline. Pipelines are an optimization that allows detection and removal of unused interpolators between stages.
  + The quality level is set to `Default`.
  + This contains the base material name **M\_Sparks\_Base** as well as a hash reflecting the material/material instance state **2bc7660b8ef1**.

To shorten debug path names, you can set the console variable `r.DumpShaderDebugShortNames=1` in your ConsoleVariables.ini configuration file. It results in slightly shorter paths like this example:  
  
`D:\UE5\Samples\Games\Lyra\Saved\ShaderDebugInfo\PCD3D_SM6\ M_Sparks_Base_2bc7668f760b8ef1\Default\LocalVF\BPVSFNoLMPol\0_6bf23011a88a16c6`

## List of Debug Info Artifacts

The following artifacts are included in these folders by default for all shader formats:

* `<ShaderFileName>.usf`

  + The final preprocessed source passed to the compiler, with all preprocessor defines used to generate this source appended as comments to the top of the file — these are stripped before the actual compilation step.
* `<ShaderFileName>_DebugCompile.usf`

  + If the compile step makes modifications to the preprocessed source, this file will be output and contain a copy of the source prior to these modifications, suitable for running the Shader Compile Worker in "debug compile" mode (typically through a debugger). This file also contains some additional debug information which can be useful:

    - In the case of material shaders, details about attributes of the material that were set when generating this particular shader (usage flags, static switches); this can help to disambiguate which parameters would have been set on material instance(s) which resulted in this shader.
    - `DebugCompile.in`

      * A binary file containing all inputs required to execute the single shader compile job, or a group of jobs for a shader pipeline, using the Shader Compile Worker's debug compile mechanism.
    - `DebugCompileArgs.txt`

      * The arguments that can be passed to ShaderCompileWorker.exe to debug compilation for this shader, or the pipeline containing this shader.
    - `OutputHash.txt`

      * Contains the hash of the shader code used by the shader library for deduplication. This matches the hash returned by `FRHIShader::GetHash`.
    - `DebugHash_<hash>.txt`

      * An empty sentinel file that can be used for quickly finding the debug information for a shader when you have access to the final shader source. For instance, when compiling with shader symbols enabled. The final step of shader preprocessing / stripping appends a comment matching this exact string to the top of the source code, so when looking at a particular shader in your GPU debugging tool of choice, you can paste this string into a file searching tool to find the associated debug info. For example, the set of preprocessor defines used to generate the source code --  as above these are now stripped before actually compiling to improve deduplication.
    - The set of all #defines that were used when preprocessing the shader.

  Certain other shader formats also dump additional artifacts, for example most backends include a batch file that can be used to re-run the platform compiler against the final source directly (using the first copy of source mentioned in the list above as input), as opposed to ShaderCompileWorker calling it in-process. Such outputs can be useful for sending reproductions of shader compilation problems to vendors. Note that all such artifacts are generated by the IShaderFormat’s implementation of the compilation function, in contrast to all the above-listed artifacts which are generated in-editor by the shader system itself. Given that we deduplicate shader compilation jobs in the editor you may have debug info folders where such IShaderFormat-generated artifacts do not exist. In this case, running the debug compilation process (see next section) will create these artifacts.

If preprocessing fails for a shader, the artifacts that will appear in the debug dump are fewer but can be used to dig into the reason why preprocessing fails if not obvious from the error message:

* `<ShaderFileName>.usf`

  + `DebugCompile.in`

    - `DebugCompileArgs.txt`

      * The arguments that can be passed to ShaderCompileWorker.exe to debug compilation for this shader, or the pipeline containing this shader.
    - A binary file containing inputs which can be read by the Shader Compile Worker debug compile mode, which in this case when running the debug compile SCW will break automatically at a point where the `FShaderCompilerInput` struct for the job can be inspected.
  + Contains comments listing all #defines used to preprocess the shader along with their values, but no actual source code, and since preprocessing failed this is not available.

## Debugging the Shader Compilation Process

In the even you need to debug a specific shader compilation step, you'll likely want to run and attach to ShaderCompileWorker directly since shader compilation doesn't occur in the main Unreal Engine process and there are some steps required to actually do so.

The first and most common option is to use the debug info artifacts described in the "Debug Dump Artifacts" section of this page to debug the full shader compilation process, including any logic in the `IShaderFormat` implementation for a specific shader format. The DebugCompileArgs.txt file contains arguments, like the following, that can be set in the Command Arguments section of the ShaderCompileWorker project in Visual Studio.

Console Output

```
"D:/UE5/Samples/Games/Lyra/Saved/ShaderDebugInfo/PCD3D_SM6/M_UI_Base_TeamLogo_3b79f5ba1237ace4/Default/LocalVF/BPVSFNoLMPol/0_90e31777ad10f4ef" 0 "DebugCompile" DebugCompile.in DebugCompile.out -DebugSourceFiles="BasePassVertexShader.usf" -TimeToLive=0.0f -KeepInput`
```

"D:/UE5/Samples/Games/Lyra/Saved/ShaderDebugInfo/PCD3D\_SM6/M\_UI\_Base\_TeamLogo\_3b79f5ba1237ace4/Default/LocalVF/BPVSFNoLMPol/0\_90e31777ad10f4ef" 0 "DebugCompile" DebugCompile.in DebugCompile.out -DebugSourceFiles="BasePassVertexShader.usf" -TimeToLive=0.0f -KeepInput`

Copy full snippet(1 line long)

Once set, you can set ShaderCompileWorker as the startup project and launch and debug this specific compilation step. For any jobs that are a stage of a shader pipeline, these debug compile arguments will always trigger the full pipeline compile job including all other stages. Since the stages are inter-dependent, this ensures that the output of the debug compile always matches that of the normal compilation path.

The section suggested option for debugging SCW is to use the Visual Studio [Child Process Debugging Power Tool](https://marketplace.visualstudio.com/items?itemName=vsdbgplat.MicrosoftChildProcessDebuggingPowerTool2022), which allows you to automatically attach to any child processes launched by by an editor (or cook) process. This can be useful when SCW is hitting problems at random not related to a specific shader.

However, there are vast amounts of child processes not handled very well , which is the case by default when running Unreal Engine on a machine with 64 or more hardware threads. It's recommended to set a lower core limit when attempting this. For example, `-corelmit=8` on the command line, in order to not cause Visual Studio to grind to a halt and throw spurious errors.

## Debugging the Shader Preprocessor

Since Unreal Engine 5.4, all shader preprocessing occurs in the editor / cook process rather than in ShaderCompileWorker. In the unlikely case you need to debug the preprocessor itself, set the following console variable and run the editor / cook process with a debugger attached:

Console Output

```
r.ShaderCompiler.BreakOnPreprocessJob=<job debug name filter>
```

r.ShaderCompiler.BreakOnPreprocessJob=<job debug name filter>

Copy full snippet(1 line long)

This will automatically break the debugger for any jobs whose debug names contain the filter string at the start of the preprocessing function. For materials, the easiest method is to use the debug group name string (`M_Sparks_Base_2bc7668f760b8ef1`). If you want to be more targeted, you can add the additional path components separated by forward slashes.

For example, `M_Sparks_Base_2bc7668f760b8ef1/Default/VelocityPipeline/FLocalVertexFactory/FVelocityPS/0` will match just this single velocity shader.  For global shaders, to break on a particular global shader permutation, you can set the filters to `<GlobalShaderTypeName>/<PermutationID>`, such as `FClusteredShaderingPS/0`.

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [programming](https://dev.epicgames.com/community/search?query=programming)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Building ShaderCompileWorker in Debug Mode](/documentation/en-us/unreal-engine/debugging-the-shader-compile-process-in-unreal-engine?application_version=5.7#enabling-dumping-of-intermediate-shaders)
* [Generating Shader Debug Info Files](/documentation/en-us/unreal-engine/debugging-the-shader-compile-process-in-unreal-engine?application_version=5.7#generatingshaderdebuginfofiles)
* [Shader Debug Info Folder Structure](/documentation/en-us/unreal-engine/debugging-the-shader-compile-process-in-unreal-engine?application_version=5.7#shaderdebuginfofolderstructure)
* [List of Debug Info Artifacts](/documentation/en-us/unreal-engine/debugging-the-shader-compile-process-in-unreal-engine?application_version=5.7#listofdebuginfoartifacts)
* [Debugging the Shader Compilation Process](/documentation/en-us/unreal-engine/debugging-the-shader-compile-process-in-unreal-engine?application_version=5.7#debuggingtheshadercompilationprocess)
* [Debugging the Shader Preprocessor](/documentation/en-us/unreal-engine/debugging-the-shader-compile-process-in-unreal-engine?application_version=5.7#debuggingtheshaderpreprocessor)
