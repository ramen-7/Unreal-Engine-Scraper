<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/logging-for-networked-games-in-unreal-engine?application_version=5.7 -->

# Logging

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
5. [Gameplay Systems](/documentation/en-us/unreal-engine/gameplay-systems-in-unreal-engine "Gameplay Systems")
6. [Networking and Multiplayer](/documentation/en-us/unreal-engine/networking-and-multiplayer-in-unreal-engine "Networking and Multiplayer")
7. [Testing, Debugging, and Optimization](/documentation/en-us/unreal-engine/network-debugging-for-unreal-engine "Testing, Debugging, and Optimization")
8. Logging

# Logging

An overview of Logging for Network Games.

![Logging](https://dev.epicgames.com/community/api/documentation/image/2b3a0a49-d9a0-452d-a573-bf1fa9e8f35a?resizing_type=fill&width=1920&height=335)

 On this page

## Logging for Networked Games

**Client** and **Server** logs are important for identifying and debugging networking issues. While many networking logs fall into the **LogNet** category, we recommend checking log categories that are more closely related to specific systems to provide greater insight into any issues.

These categories are not enabled by default and have varying amounts of verbosity that you may need to adjust to gain information about the behavior you're experiencing. The list below provides some recommended categories:

| Category | Description |
| --- | --- |
| **LogNetTraffic** | Logs all network traffic when this log variable is set to VeryVerbose. |
| **LogNetPackageMap** | Logs information related to how NetGUIDs are Sent, Received, and Acknowledged. |
| **LogNetVersion**  **LogNetFastTArray**  **LogNetDormancy**  **LogRep**  **LogRepTraffic** | Logs information related to Property Replication and RepNotify functions that are used by FRepLayout and FObjectReplicator. |
| **LogRepProperties** | Logs information related to the sending and receiving of replicated properties. |
| **PacketHandlerLog** | Logs information on the packet handler and its components. These components have their own sub-categories. For example, LogDTLSHandler, OodleNetworkHandlerComponentLog, and LogHandshake. |
| **LogDemo** | Logs information on recording and playing back replays. Each replay streamer has a related log category: LogLocalFileReplay, LogSaveGameReplay, LogNullReplay, and LogMemoryReplay. |

You can enable these log categories and adjust their verbosity by the following methods:

### Command-Line Argument

Pass the `LogCmds` command line argument:

C++

```
-LogCmds="<LOG_CATEGORY> <LOG_VERBOSITY>"
```

-LogCmds="<LOG\_CATEGORY> <LOG\_VERBOSITY>"

Copy full snippet(1 line long)

For example, to set `LogNetTraffic` to `VeryVerbose`:

C++

```
-LogCmds="LogNetTraffic VeryVerbose"
```

-LogCmds="LogNetTraffic VeryVerbose"

Copy full snippet(1 line long)

### Console Command

Use the `Log` console command:

C++

```
Log <LOG_CATEGORY> <LOG_VERBOSITY>
```

Log <LOG\_CATEGORY> <LOG\_VERBOSITY>

Copy full snippet(1 line long)

For example, to set `LogNetTraffic` to `Verbose`:

C++

```
Log LogNetTraffic Verbose
```

Log LogNetTraffic Verbose

Copy full snippet(1 line long)

### Engine Configuration

Set them in your project's `DefaultEngine.ini.`:

C++

```
|  |  |
| --- | --- |
|  | [Core.Log] |
|  | <LOG_CATEGORY1>=<LOG_VERBOSITY1> |
|  | <LOG_CATEGORY2>=<LOG_VERBOSITY2> |
|  | ... |
```

[Core.Log]
<LOG\_CATEGORY1>=<LOG\_VERBOSITY1>
<LOG\_CATEGORY2>=<LOG\_VERBOSITY2>
...

Copy full snippet(4 lines long)

For example, to set multiple categories to different verbosities:

C++

```
|  |  |
| --- | --- |
|  | [Core.Log] |
|  | LogNetPackageMap=Log |
|  | LogNetTraffic=Verbose |
|  | LogRep=VeryVerbose |
```

[Core.Log]
LogNetPackageMap=Log
LogNetTraffic=Verbose
LogRep=VeryVerbose

Copy full snippet(4 lines long)

## Helpful Errors

When reading logs, the following list can be useful for determining what kind of error occurred.

|  |  |
| --- | --- |
| **UEngine::BroadcastNetworkFailure** | Printed when a net driver encounters some major error. The log line will include the failure type, the error string, and the description of the net driver that encountered the error. You can see a list of the possible network failures with brief descriptions in the ENetworkFailure enum in EngineBaseTypes.h. |
| **UNetConnection::Close** | A description of the connection being closed. |
| **UActorChannel::Close** | A LogNetTraffic category that will include the channel index, the Actor for that channel, and the reason it was closed. Checking the logs around these lines can help provide some indication as to why a connection or Actor channel was closed. |

The command-line argument `-LogTrace=<PARTIAL_LOG_LINE>` performs stack traces from partial log message strings. For example: `-LogTrace=UNetConnection::Close` will produce a stack trace whenever `UNetConnection::Close` is printed to the logs. The command-line argument `-DumpRPCs` provides the capability to dump RPCs and their parameters, which can be useful for tracking what RPCs are being sent and their parameters.

LogTrace and DumpRPCs both require **NetcodeUnitTest** to be enabled.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Logging for Networked Games](/documentation/en-us/unreal-engine/logging-for-networked-games-in-unreal-engine?application_version=5.7#logging-for-networked-games)
* [Command-Line Argument](/documentation/en-us/unreal-engine/logging-for-networked-games-in-unreal-engine?application_version=5.7#command-line-argument)
* [Console Command](/documentation/en-us/unreal-engine/logging-for-networked-games-in-unreal-engine?application_version=5.7#console-command)
* [Engine Configuration](/documentation/en-us/unreal-engine/logging-for-networked-games-in-unreal-engine?application_version=5.7#engine-configuration)
* [Helpful Errors](/documentation/en-us/unreal-engine/logging-for-networked-games-in-unreal-engine?application_version=5.7#helpful-errors)
