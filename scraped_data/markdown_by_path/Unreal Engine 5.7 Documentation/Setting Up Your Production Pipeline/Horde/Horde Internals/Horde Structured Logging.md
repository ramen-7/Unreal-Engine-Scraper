<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/horde-structured-logging-for-unreal-engine?application_version=5.7 -->

# Horde Structured Logging

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
6. [Horde](/documentation/en-us/unreal-engine/horde-in-unreal-engine "Horde")
7. [Horde Internals](/documentation/en-us/unreal-engine/horde-internals-for-unreal-engine "Horde Internals")
8. Horde Structured Logging

# Horde Structured Logging

An overview of Horde structured logging for use with Unreal Engine.

![Horde Structured Logging](https://dev.epicgames.com/community/api/documentation/image/b66200f8-fa36-4900-8e64-bfe7d7adc4d1?resizing_type=fill&width=1920&height=335)

 On this page

Horde heavily uses structured logging output from Unreal Engine and tools, which provides more context-specific information than is typically available in plain-text logs.

To understand how Horde uses structured logging, it's helpful to consider the sort of information we'd like to get from diagnostics in our automated processes:

* Human-readable message
* Source of diagnostic (compiler, linker, etc.)
* File(s) triggering the error (local path, path in version control)
* Line number
* Severity
* Error code
* Other context-specific information

Ideally, we would tag errors at source and add as much context-specific information as possible. For example, the following log fragment:

```
|  |  |
| --- | --- |
|  | NVENC_EncoderH264.cpp (0:05.95 at +16:18) |
|  | d:\build\AutoSDK\Sync\HostWin64\Win64\Windows Kits\10\include\10.0.18362.0\um\winnt.h(603): error C2220: the following warning is treated as an error |
|  | d:\build\AutoSDK\Sync\HostWin64\Win64\Windows Kits\10\include\10.0.18362.0\um\winnt.h(603): warning C4005: 'TEXT': macro redefinition |
|  | Engine\Source\Runtime\Core\Public\HAL\Platform.h(1081): note: see previous definition of 'TEXT' |

Copy full snippet
```

...provides the following information:

* There has been a **compile** error.
* It occurred while compiling `NVENC_EncoderH264.cpp`, due to a conflict between macros defined in `winnt.h` (line 603) and `Platform.h` (line 1081).
* We can map `NVENC_EncoderH264.cpp` and `Platform.h` to files in source control and see their revision history.
* The warning number is `C4005`, which is treated as error `C2220`.
* It took 5.95 seconds to compile the file.

Rather than outputting plain text for log events, we preserve the format string and arguments and render them later. That allows us to render those arguments differently for types we understand and enables us to index and search logs based on those fields.

Horde natively supports structured log events, which we use to do things like render source files as links to the P4V timelapse view and error codes as links to MSDN. We can also map paths back to their history in source control, which we use to figure out who broke the build via Horde's build health system.

Anyone who's bumped up against the build system treating any log line containing the string "error:" as an error can rejoice; if you output a structured log event directly, Horde will no longer need to guess whether it's an error or not.

## Formatting

Unreal Engine uses standard [message templates](https://messagetemplates.org) syntax to write errors, for example:

```
Logger.LogInformation("Hello {Text}", "world");
Copy full snippet
```

Notably:

* All parameters in a format string should be named rather than using numeric placeholders (ie. {Text} rather than {0}, {1} etc.). These identifiers are used to name properties in the structured log event and can be indexed and searched through tools like Splunk and Datadog.
* Format strings should be constants rather than using interpolated or concatenated strings. This allows the logger implementation to cache and reuse parsed format strings between messages.

The log events may be rendered into a plain-text log for display in the console immediately or preserved in a structured form in a [JSONL](https://jsonlines.org/) file.

## Writing Events from C

AutomationTool and UnrealBuildTool have support for writing log events using the NET ILogger API.

All logging should be done through an [ILogger](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.logging.ilogger) instance (defined in the Microsoft.Extensions.Logging namespace) rather than passed through the legacy `Log.TraceInformation` and other static methods.

## Writing Events from C++

Unreal Engine runtime supports writing structured log events using the `UE_LOGFMT` macro.

## Capturing Output

Horde sets a UE\_LOG\_JSON\_TO\_STDOUT environment variable, which instructs tools such as AutomationTool to output JSON directly to stdout, which it ingests and stores for rendering on the dashboard.

## Legacy Log Output

For external tools that don't support structured logs (e.g. compilers, etc.), we have a library of regexes that run over plain text output and construct structured log events from them. Some are in UBT (`Engine/Source/Programs/UnrealBuildTool/Matchers/...`) and some in UAT (`Engine/Source/Programs/AutomationTool/AutomationUtils/Matchers/...`). These are used by the `LogEventParser` class in EpicGames.Core.

To implement a new matcher for plain-text log output, create a class that implements the `ILogEventMatcher` interface from `EpicGames.Core`, and ensure it's registered

When adding or modifying log parsers, we strongly recommend running (and writing) tests in the `UnrealBuildTool.Tests` and `HordeAgent.Tests` projects to check interaction with other handlers.

* [horde](https://dev.epicgames.com/community/search?query=horde)
* [bronze](https://dev.epicgames.com/community/search?query=bronze)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Formatting](/documentation/en-us/unreal-engine/horde-structured-logging-for-unreal-engine?application_version=5.7#formatting)
* [Writing Events from C](/documentation/en-us/unreal-engine/horde-structured-logging-for-unreal-engine?application_version=5.7#writingeventsfromc)
* [Writing Events from C++](/documentation/en-us/unreal-engine/horde-structured-logging-for-unreal-engine?application_version=5.7#writingeventsfromc++)
* [Capturing Output](/documentation/en-us/unreal-engine/horde-structured-logging-for-unreal-engine?application_version=5.7#capturingoutput)
* [Legacy Log Output](/documentation/en-us/unreal-engine/horde-structured-logging-for-unreal-engine?application_version=5.7#legacylogoutput)
