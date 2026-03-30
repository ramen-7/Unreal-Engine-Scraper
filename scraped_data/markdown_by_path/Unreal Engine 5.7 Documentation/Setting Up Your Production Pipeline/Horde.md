<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/horde-in-unreal-engine?application_version=5.7 -->

# Horde

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
6. Horde

# Horde

An infrastructure to improve your team's workflow.

![Horde](https://dev.epicgames.com/community/api/documentation/image/63633982-cd68-4ff2-8e27-3990ed8c96ef?resizing_type=fill&width=1920&height=335)

 On this page

**Horde** is a set of services supporting workflows Epic Games uses to develop Fortnite, Unreal Engine, and other projects.

## Features

Horde offers the following functionality, most of which can be enabled or disabled independently:

* **Remote Execution**: Functionality to offload compute work to other machines, including C++ compilation with [Unreal Build Accelerator](/documentation/en-us/unreal-engine/horde-unreal-build-accelerator-and-remote-compilation-tutorial-for-unreal-engine).
* **Build Automation (CI/CD)**: A build automation system designed for teams working with large Perforce repositories.
* **Test Automation**: A frontend for querying automation results across streams and projects, integrated with [Automation Tool](/documentation/en-us/unreal-engine/unreal-automation-tool-for-unreal-engine) and [Gauntlet](/documentation/en-us/unreal-engine/gauntlet-automation-framework-in-unreal-engine).
* **Studio Analytics**: Received telemetry from Unreal Editor and shows charts for key workflow metrics.
* **UnrealGameSync Metadata Server**: Various features for teams using [UnrealGameSync](/documentation/en-us/unreal-engine/unreal-game-sync-ugs-for-unreal-engine), including build status reporting, comment aggregation, and crowdsourced build health functionality.
* **Mobile/Console Device Manager**: A system for allocating and managing a farm of development kits and mobile devices.

## Goals & Philosophy

### Opinionated

We created Horde from workflows and best practices that have arisen for Epic Games over time. They aren't the only way to work and may not be for everyone. Being completely generic is a non-goal for Horde. We believe that the interaction between systems and the context in which tools are used provides the richest opportunity for creating smooth and slick workflows for creators.

### Simple to Deploy

We've tried to build Horde in a way that requires little setup to run. While you can have fairly elaborate, multi-machine, distributed deployments, we strive to make it easy to run and debug locally on all our supported desktop platforms with few prerequisites installed. A database is created locally if you don't have one set up, and all the required services will automatically start and stop with the server's lifetime.

### Easy to Manage

Having control over the source for a project like Horde, while also using it in a high-velocity environment, empowers us to optimize for our own ease of use. We have a tight feedback loop with our operations teams and try to make their lives as easy as possible. As such, you can store most configuration data in source control, and we provide built-in profiling and performance tooling.

### Private

We do not host your data with Horde nor receive any telemetry from user deployments. You can host it on a private network, as befits your IT policies, and integrate it with your own OpenID Connect (OIDC) authentication provider to access it.

### Scalable

We distribute full source code for all Horde client and server functionality.

## Getting Started with Horde

Before getting started, download the [Horde Windows MSI Installer](https://github.com/EpicGames/UnrealEngine/releases/download/5.5.0-release/UnrealHordeServer.msi).

Requires access to the EpicGames GitHub repository. If you need access to the repository, follow the instructions on the [UE on GitHub](https://www.unrealengine.com/ue-on-github) page.

After downloading Horde, we recommend starting with the following tutorials based on your needs:

* [Install the Horde agent](/documentation/en-us/unreal-engine/horde-installation-tutorial-for-unreal-engine)
* [Enable remote C++ compilation with Unreal Build Accelerator](/documentation/en-us/unreal-engine/horde-unreal-build-accelerator-and-remote-compilation-tutorial-for-unreal-engine)
* [Set up build automation](/documentation/en-us/unreal-engine/horde-build-automation-tutorial-for-unreal-engine)
* [Enable test automation with Gauntlet](/documentation/en-us/unreal-engine/horde-test-automation-tutorial-for-unreal-engine)
* [Get telemetry and analytics for your team](/documentation/en-us/unreal-engine/horde-analytics-tutorial-for-unreal-engine)
* [Work with mobile and console devices](/documentation/en-us/unreal-engine/horde-device-manager-tutorial-for-unreal-engine)
* [Install UnrealGameSync and distribute Unreal Editor to your team](/documentation/en-us/unreal-engine/horde-unrealgamesync-tutorial-for-unreal-engine)
* [Enable authentication](/documentation/en-us/unreal-engine/horde-authentication-tutorial-for-unreal-engine)

## Topic Directory

[![Horde Deployment](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a7a5879c-1756-4f59-a0b7-4f23f12818bd/placeholder_topic.png)

Horde Deployment

An overview of deploying Horde for use with Unreal Engine.](/documentation/en-us/unreal-engine/horde-deployment-for-unreal-engine)
[![Horde Configuration](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fbac944b-7515-4db0-b363-9848de0e526a/placeholder_topic.png)

Horde Configuration

An overview of Horde configuration options for use with Unreal Engine.](/documentation/en-us/unreal-engine/horde-configuration-for-unreal-engine)
[![Horde Internals](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b9558288-dd93-4179-a378-37ef6ee8c949/placeholder_topic.png)

Horde Internals

An overview of Horde internals for use with Unreal Engine.](/documentation/en-us/unreal-engine/horde-internals-for-unreal-engine)
[![Horde Tutorials](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c6266ceb-b202-4bfc-a73d-3529090fb26c/placeholder_topic.png)

Horde Tutorials

An overview of Horde tutorials for use with Unreal Engine.](/documentation/en-us/unreal-engine/horde-tutorials-for-unreal-engine)
[![Horde Frequently Asked Questions](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fa9d80e5-d008-46f0-9ac4-624855e9ffc8/placeholder_topic.png)

Horde Frequently Asked Questions

Frequently asked questions about Horde for use with Unreal Engine.](/documentation/en-us/unreal-engine/horde-frequently-asked-questions-for-unreal-engine)
[![Horde Glossary](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9c33d69b-53d6-4786-80ed-24f8048be846/placeholder_topic.png)

Horde Glossary

A glossary of terms for Horde for use with Unreal Engine.](/documentation/en-us/unreal-engine/horde-glossary-for-unreal-engine)

* [automation](https://dev.epicgames.com/community/search?query=automation)
* [unrealgamesync](https://dev.epicgames.com/community/search?query=unrealgamesync)
* [horde](https://dev.epicgames.com/community/search?query=horde)
* [unreal build accelerator](https://dev.epicgames.com/community/search?query=unreal%20build%20accelerator)
* [automation tool](https://dev.epicgames.com/community/search?query=automation%20tool)
* [gauntlet](https://dev.epicgames.com/community/search?query=gauntlet)
* [unreal build tool](https://dev.epicgames.com/community/search?query=unreal%20build%20tool)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Features](/documentation/en-us/unreal-engine/horde-in-unreal-engine?application_version=5.7#features)
* [Goals & Philosophy](/documentation/en-us/unreal-engine/horde-in-unreal-engine?application_version=5.7#goals&philosophy)
* [Opinionated](/documentation/en-us/unreal-engine/horde-in-unreal-engine?application_version=5.7#opinionated)
* [Simple to Deploy](/documentation/en-us/unreal-engine/horde-in-unreal-engine?application_version=5.7#simpletodeploy)
* [Easy to Manage](/documentation/en-us/unreal-engine/horde-in-unreal-engine?application_version=5.7#easytomanage)
* [Private](/documentation/en-us/unreal-engine/horde-in-unreal-engine?application_version=5.7#private)
* [Scalable](/documentation/en-us/unreal-engine/horde-in-unreal-engine?application_version=5.7#scalable)
* [Getting Started with Horde](/documentation/en-us/unreal-engine/horde-in-unreal-engine?application_version=5.7#gettingstartedwithhorde)
* [Topic Directory](/documentation/en-us/unreal-engine/horde-in-unreal-engine?application_version=5.7#topicdirectory)
