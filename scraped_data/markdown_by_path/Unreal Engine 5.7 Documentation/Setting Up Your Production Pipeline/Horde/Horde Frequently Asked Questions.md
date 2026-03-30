<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/horde-frequently-asked-questions-for-unreal-engine?application_version=5.7 -->

# Horde Frequently Asked Questions

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
7. Horde Frequently Asked Questions

# Horde Frequently Asked Questions

Frequently asked questions about Horde for use with Unreal Engine.

![Horde Frequently Asked Questions](https://dev.epicgames.com/community/api/documentation/image/fbc3b5a3-ce74-42f8-b079-e737f1f7a24a?resizing_type=fill&width=1920&height=335)

 On this page

### Why are all these use cases being muddled together?

Most of our target use cases are traditionally handled as distinct components, but bringing them all together lets us take a lot of shortcuts and optimize for common use cases. For example:

* Storage is a key component of any data pipeline for caching.
* Remote execution needs data close to compute nodes where it can be retrieved quickly.
* Scalable build automation systems use the same scheduling, management tools, and auto-scaling functionality as a remote execution platform and require a storage backend for intermediate and final artifacts.

By sharing the infrastructure that supports our internal dev teams, we hope to remove more of the busy work that is needed for teams to collaborate successfully.

### Will I need to deploy Horde to use Unreal Engine?

No. Horde is not a requirement to use Unreal Engine, but it has been valuable for Epic Games, and we hope it can be valuable for other teams too.

### Do I have to deploy Horde to the cloud?

No. Horde runs well in local deployments using off-the-shelf hardware, though some applications may benefit from cloud storage even if you don't host any other infrastructure in the cloud.

### Do I have to use the CI system / remote execution functionality / test framework / etc.?

No. Each feature is optional, and any disabled features do not incur any costs.

### Why would I use Horde for build automation rather than Jenkins or TeamCity?

Most build automation systems are purposefully generic, so you can run any workload on them.

That leaves a lot of plumbing for build ops teams to do: writing build scripts, managing artifact transfers between agents to implement parallelism, setting up stores for final artifacts, implementing a way to manage the allocation of network-connected devkits and mobile devices for build agents and so on.

What's more, the resulting system is not very smart. You may have notifications for build failures, but it requires a human to diagnose what and when a failure began and who needs to fix it. You need a way to clean up old build artifacts and manage permissions for them. If you're using network shares for artifacts, you need to deal with lots of overlapping artifacts that are almost the same. Then, if you're a large organization, you need to figure out a way to distribute these artifacts to developers in different locations - and, of course, you probably want some tooling so devs can find and fetch these artifacts.

Functionality such as servers for tracking results of automated tests between builds is another layer; it may run on the build automation system, but you might have a myriad of tests generating data over lots of different changes that needs to be stored somewhere, and want to go spelunking through that data to find when, say, framerate dropped below a certain threshold in a certain map, or when the size of a particular level exceeded a certain point.

A lot of these problems are orthogonal to the problems that build automation systems typically concern themselves with solving. Still, by thinking about them together, we can make much smarter implementation decisions that understand their operating context.

That said, Horde's CI functionality is not enabled by default. Other functionality in Horde can still be used without migrating to a new build automation system.

### Does the build automation system support Git / Subversion / etc...?

Not at the moment. We make a number of assumptions that are fairly Perforce-centric, such as being able to strongly order changes in a single, linear branch history. We also have a lot of custom logic for provisioning Perforce workspaces in an efficient way.

We may explore support for other version control systems in future.

### Does Epic Games get telemetry about our project if we use Horde?

No. Horde does not send any data to Epic Games.

* [horde](https://dev.epicgames.com/community/search?query=horde)
* [bronze](https://dev.epicgames.com/community/search?query=bronze)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Why are all these use cases being muddled together?](/documentation/en-us/unreal-engine/horde-frequently-asked-questions-for-unreal-engine?application_version=5.7#whyarealltheseusecasesbeingmuddledtogether?)
* [Will I need to deploy Horde to use Unreal Engine?](/documentation/en-us/unreal-engine/horde-frequently-asked-questions-for-unreal-engine?application_version=5.7#willineedtodeployhordetouseunrealengine?)
* [Do I have to deploy Horde to the cloud?](/documentation/en-us/unreal-engine/horde-frequently-asked-questions-for-unreal-engine?application_version=5.7#doihavetodeployhordetothecloud?)
* [Do I have to use the CI system / remote execution functionality / test framework / etc.?](/documentation/en-us/unreal-engine/horde-frequently-asked-questions-for-unreal-engine?application_version=5.7#doihavetousethecisystem/remoteexecutionfunctionality/testframework/etc?)
* [Why would I use Horde for build automation rather than Jenkins or TeamCity?](/documentation/en-us/unreal-engine/horde-frequently-asked-questions-for-unreal-engine?application_version=5.7#whywouldiusehordeforbuildautomationratherthanjenkinsorteamcity?)
* [Does the build automation system support Git / Subversion / etc...?](/documentation/en-us/unreal-engine/horde-frequently-asked-questions-for-unreal-engine?application_version=5.7#doesthebuildautomationsystemsupportgit/subversion/etc?)
* [Does Epic Games get telemetry about our project if we use Horde?](/documentation/en-us/unreal-engine/horde-frequently-asked-questions-for-unreal-engine?application_version=5.7#doesepicgamesgettelemetryaboutourprojectifweusehorde?)
