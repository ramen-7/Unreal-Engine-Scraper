<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/horde-agents-for-unreal-engine?application_version=5.7 -->

# Horde Agents

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
7. [Horde Configuration](/documentation/en-us/unreal-engine/horde-configuration-for-unreal-engine "Horde Configuration")
8. Horde Agents

# Horde Agents

An overview of Horde Agents.

![Horde Agents](https://dev.epicgames.com/community/api/documentation/image/4f49e72b-2cab-4b91-8cbb-b0f74342e43e?resizing_type=fill&width=1920&height=335)

 On this page

## Installing the Horde Agent

For information about deploying new agents, see [Horde > Deployment > Agent](/documentation/en-us/unreal-engine/horde-agent-deployment-for-unreal-engine).

## Pools

Pools are groups of machines that can be used interchangeably, typically due to being a particular platform or hardware class. Pools simplify the management of build pipelines by allowing DevOps engineers to configure a mapping from agent types to physical machines.

Pools are defined in the [.globals.json](/documentation/en-us/unreal-engine/horde-schema-for-unreal-engine#globals) file, via the `pools` property. Agents may be added to a pool manually through the Horde Dashboard or automatically by matching a particular condition. For example, the following configuration block defines a pool that automatically includes all Windows machines:

```
|  |  |
| --- | --- |
|  | { |
|  | "name": "WinLargeRam", |
|  | "condition": "Platform == 'Win64' && RAM > 64gb" |
|  | } |

Copy full snippet
```

See also: [Condition expression syntax](/documentation/en-us/unreal-engine/horde-conditions-for-unreal-engine)

## Remoting to Agents

If you have a fleet of machines that require identical login credentials, you can configure UnrealGameSync to open Remote Desktop sessions from links in the Horde dashboard.

To enable this functionality, open **Credential Manager** from the Windows Control Panel and select **Windows Credentials**. Click the **Add a new generic credential...** link to create a new entry and name it `UnrealGameSync:RDP`. Enter the login username and password as appropriate.

The **Remote Desktop** button on agent dialogs in Horde will open a URL of the form `ugs://rdp?host=[NameOrIP]`. UnrealGameSync is configured to handle `ugs://` links by default, intercepts these links, and adds a Windows login entry for the given `NameOrIP` before launching the remote desktop application.

* [horde](https://dev.epicgames.com/community/search?query=horde)
* [bronze](https://dev.epicgames.com/community/search?query=bronze)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Installing the Horde Agent](/documentation/en-us/unreal-engine/horde-agents-for-unreal-engine?application_version=5.7#installingthehordeagent)
* [Pools](/documentation/en-us/unreal-engine/horde-agents-for-unreal-engine?application_version=5.7#pools)
* [Remoting to Agents](/documentation/en-us/unreal-engine/horde-agents-for-unreal-engine?application_version=5.7#remotingtoagents)
