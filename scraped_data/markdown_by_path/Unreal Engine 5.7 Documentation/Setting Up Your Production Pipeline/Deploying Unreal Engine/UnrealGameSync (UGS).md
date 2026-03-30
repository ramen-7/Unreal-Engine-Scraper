<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-game-sync-ugs-for-unreal-engine?application_version=5.7 -->

# UnrealGameSync (UGS)

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
6. [Deploying Unreal Engine](/documentation/en-us/unreal-engine/deploying-unreal-engine "Deploying Unreal Engine")
7. UnrealGameSync (UGS)

# UnrealGameSync (UGS)

An overview of UnrealGameSync (UGS), an internal tool used by developers to sync their Workspace with a project's stream.

![UnrealGameSync (UGS)](https://dev.epicgames.com/community/api/documentation/image/496d1782-ba24-4c4d-be47-e7c1f0fa1be8?resizing_type=fill&width=1920&height=335)

 On this page

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6d151ec0-7bab-45a4-af18-5eb83d3a82c7/deployment_banner-1.png "Deployment_Banner-1.png")

When a team is working on an **Unreal Engine (UE)** project, they're working in an environment where code and content is continuously developed and integrated into the project. Oftentimes, while working in a collaborative development environment, success depends on a team's ability to effectively collaborate and communicate on problems that might arise during the development and integration process.

This is where a sync tool can help.

## What is UnrealGameSync (UGS)?

Conceptually, **UGS** is a tool that promotes code and content integration in a collaborative development environment, enabling teammates distributed over time and distance to labor on the same project as it gets updated. Technically, UGS provides a graphical front-end to sync UE projects from **Perforce**, optionally building those projects with Microsoft's [Visual Studio](https://www.visualstudio.com/) Compiler.

When they're using this tool, an **Artist's** workflow typically involves UGS syncing their project files, resolving merge conflicts, syncing editor binaries, updating version files, and optionally running their Unreal project.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4004456c-baa6-4d11-98e8-ce6eb9c04e1b/artist_workflow.png "Artist_Workflow.png")

For **Programmers**, their workflow typically involves UGS syncing their project files, resolving merge conflicts, updating version files, generating project files, optionally building UE4, and optionally running their Unreal project.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cfe78d0f-3b18-4eb1-a175-750515c91792/programmerworkflow.png "ProgrammerWorkflow.png")


Resolving merge conflicts is enabled by default; however, you can disable this service in the **Options** shortcut menu. Additionally, disabling UGS from building your project precludes UGS from running it.

After installing UGS, members of any team will be able to quickly bootstrap and iterate on projects without the overhead that typically comes with using sync tools.

## Who Benefits from Using UGS?

Anyone wanting to gain insight into or contribute to a UE game project, but more specifically; Developers, Designers, and Artists. In general, for all team members, it's safe to submit changes containing assets and source code because UGS syncs both code and content with ease.

### Developers

* Developers can sync to a changelist (CL) as soon as it's submitted, thereby enabling them to locally compile the source code matching the CL. Additionally, they can add comments to each change, flagging builds as good or bad for other developers.
* When engineers are working on a fix for a broken build, they can notify the rest of the team that they're working on the fix by setting a flag.
* Developers can safely make content changes from local builds without submitting unversioned assets because Engine version files (`Version.h` and `Build.version`) are updated to the synced CL.
* Because UGS includes custom build steps, UGS enables developers to set up tools and utilities that are specific to their project.

Note that build system results can be surfaced alongside a list of submitted CLs (along with a link to build logs).

### Creatives

* If creatives, such as artists or designers, don't have Visual Studio (or if they don't need to compile the Editor), they can get a compressed Editor build of the project, which is compiled by the **Continuous Integration System (CIS)**.
* Getting a compressed Editor build of the project is particularly useful for artists because the compressed build can be synced and automatically decompressed.

Finally, it's important to note that other disciplines, such as Quality Assurance, Production, or Business units can also use UGS to gain insight into a project's status or collaborate with developers and creatives. If you're new to UGS and you want to start using it, check out the [UGS Quick Start](/documentation/en-us/unreal-engine/unreal-game-sync-quick-start-guide) guide.

## Unreal Game Sync Documentation

[![UGS Client Setup](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/335ecff7-3b73-4610-b42b-f8bfc0479036/placeholder_topic.png)

UGS Client Setup

How to set up an Unreal Game Sync client](/documentation/en-us/unreal-engine/unreal-game-sync-client-setup-for-unreal-engine)
[![UGS Quick Start](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e299c21d-19bd-4aa3-a58f-f02b9fe8572b/placeholder_topic.png)

UGS Quick Start

Learn how to get started using UnrealGameSync.](/documentation/en-us/unreal-engine/unreal-game-sync-quick-start-guide)
[![UGS Reference](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/42d6bf66-154a-4d46-afe9-5a4f829e6455/placeholder_topic.png)

UGS Reference

This page describes how to configure UGS for deployment as a studio.](/documentation/en-us/unreal-engine/unreal-game-sync-reference-guide-for-unreal-engine)
[![UGS Menu Reference](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/680da580-1335-4e17-b140-72eafb0f1bfe/placeholder_topic.png)

UGS Menu Reference

All the options in the Unreal Game Sync menus](/documentation/en-us/unreal-engine/unreal-game-sync-menu-reference-for-unreal-engine)
[![UGS Precompiled Binaries](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b8f9eaaf-c01e-4d75-baca-73a0d816cd49/placeholder_topic.png)

UGS Precompiled Binaries

How to use precompiled binaries to optimize development for your project](/documentation/en-us/unreal-engine/using-precompiled-binaries-in-unreal-game-sync-for-unreal-engine)
[![UGS Troubleshooting](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c19d08e9-19a8-4215-8c3c-ab6b731a96a7/placeholder_topic.png)

UGS Troubleshooting

Some tips and procedures for correcting common problems with UGS](/documentation/en-us/unreal-engine/unreal-game-sync-troubleshooting)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [What is UnrealGameSync (UGS)?](/documentation/en-us/unreal-engine/unreal-game-sync-ugs-for-unreal-engine?application_version=5.7#whatisunrealgamesync(ugs)?)
* [Who Benefits from Using UGS?](/documentation/en-us/unreal-engine/unreal-game-sync-ugs-for-unreal-engine?application_version=5.7#whobenefitsfromusingugs?)
* [Developers](/documentation/en-us/unreal-engine/unreal-game-sync-ugs-for-unreal-engine?application_version=5.7#developers)
* [Creatives](/documentation/en-us/unreal-engine/unreal-game-sync-ugs-for-unreal-engine?application_version=5.7#creatives)
* [Unreal Game Sync Documentation](/documentation/en-us/unreal-engine/unreal-game-sync-ugs-for-unreal-engine?application_version=5.7#unrealgamesyncdocumentation)
