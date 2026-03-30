<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/horde-leases-for-unreal-engine?application_version=5.7 -->

# Horde Leases

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
8. Horde Leases

# Horde Leases

An overview of Horde leases for use with Unreal Engine.

![Horde Leases](https://dev.epicgames.com/community/api/documentation/image/7d321a26-1ca2-4d22-8415-308a3812f70e?resizing_type=fill&width=1920&height=335)

 On this page

The mechanism by which Horde communicates with its agents is based heavily on Google's Remote Worker API. Work items assigned to agents are known as **leases**.

Communication between the agent and server is done through streaming gRPC calls initiated by the agent. The ends of the connection exchange copies of what they believe the current state of leases owned by the agent should be, and a state machine determines which field is authoritative at different times. The server and agent keep exchanging state objects and reconciling differences until they are in sync; at that point, the agent has acknowledged that it is taking any new leases added by the server, and the server has acknowledged the completion of any removed leases by the agent.

Within the Horde server, leases are assigned to agents through classes implementing `ITaskSource`.

## Lease Types

Each lease type consists of the following key classes:

* a message defining the lease itself (i.e. what the agent needs to do),
* a task source on the server that decides to assign a lease to an agent (`ITaskSource`),
* a lease handler on the agent which does the work (`LeaseHandler`).

Horde ships with the following lease types:

| Message | Task source (server) | Lease handler (agent) | Description |
| --- | --- | --- | --- |
| `job_task.proto` | `JobTaskSource` | `JobHandler` | Executes a batch as part of a CI job. |
| `upgrade_task.proto` | `UpgradeTaskSource` | `UpgradeHandler` | Upgrades the Horde agent software to a newer version. |
| `conform_task.proto` | `ConformTaskSource` | `ConformHandler` | Syncs all the workspaces on a machine to latest and optionally removes any untracked files. |
| `restart_task.proto` | `RestartTaskSource` | `RestartHandler` | Restarts the machine. |
| `shutdown_task.proto` | `ShutdownTaskSource` | `ShutdownHandler` | Powers down the machine. |

## Adding New Lease Types

To add a new lease type, each of the key classes above must be added.

* After adding a task source to the server, register it as a singleton implementing `ITaskSource` in `Startup.cs`.
* After adding a lease handler to the agent, register it as a singleton implementing `LeaseHandler` in `Program.cs`.

* [horde](https://dev.epicgames.com/community/search?query=horde)
* [bronze](https://dev.epicgames.com/community/search?query=bronze)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Lease Types](/documentation/en-us/unreal-engine/horde-leases-for-unreal-engine?application_version=5.7#leasetypes)
* [Adding New Lease Types](/documentation/en-us/unreal-engine/horde-leases-for-unreal-engine?application_version=5.7#addingnewleasetypes)
