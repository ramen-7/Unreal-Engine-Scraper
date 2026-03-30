<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/horde-installation-tutorial-for-unreal-engine?application_version=5.7 -->

# Horde Installation Tutorial

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
7. [Horde Tutorials](/documentation/en-us/unreal-engine/horde-tutorials-for-unreal-engine "Horde Tutorials")
8. Horde Installation Tutorial

# Horde Installation Tutorial

A tutorial for installing Horde for use with Unreal Engine.

![Horde Installation Tutorial](https://dev.epicgames.com/community/api/documentation/image/d5d5d1d3-79ef-48da-bd4a-3c9f1f415da3?resizing_type=fill&width=1920&height=335)

 On this page

## Introduction

This guide describes a simple local Horde server installation on Windows.

Horde can also be installed via [Docker on Linux](/documentation/en-us/unreal-engine/horde-server-for-unreal-engine#docker-linux), both as a single instance and horizontally scaled service via a container orchestration system such as Kubernetes.

For a more detailed discussion of these advanced deployment scenarios, see [Horde > Deployment](/documentation/en-us/unreal-engine/horde-deployment-for-unreal-engine).

## Prerequisites

* A machine to function as the Horde Server.
* One or more machines to function as Horde Agents. We currently recommend dedicated machines for this purpose.

## Steps

### Horde Server

1. Install the Horde Server by running `Engine\Extras\Horde\UnrealHordeServer.msi`.

   * The Horde Server can also be deployed on [Linux using Docker](/documentation/en-us/unreal-engine/horde-server-for-unreal-engine#docker-linux).
   * By default, Horde is configured to use [ports 13340 (HTTP) and 13342 (HTTP/2)](/documentation/en-us/unreal-engine/horde-server-for-unreal-engine#ports). We recommend setting up [HTTPS](/documentation/en-us/unreal-engine/horde-server-for-unreal-engine#https) for production deployments.
   * See also: [Deployment > Server](/documentation/en-us/unreal-engine/horde-server-for-unreal-engine)

### Horde Agents

1. Navigate to the installed [Horde Server](/documentation/en-us/unreal-engine/horde-installation-tutorial-for-unreal-engine#horde-server) in a web browser on the agent machine.

   * This is typically `http://{{ HOST_NAME_OR_IP_ADDRESS }}:13340` with a default installation.
   * Note that the Horde Server defaults to HTTP hosting by default (not HTTPS), so you may need to enter `http://` manually as part of the address.
2. Open the **Tools** menu at the top of the dashboard and select **Downloads**.
3. Download and run **Horde Agent (Windows Installer)**.

   * Enter the same server address you used above when prompted, and choose an empty working directory for the remote execution sandbox.
   * We recommend choosing a drive with at least 100GB of free space for C++ compilation.
4. Leave the `Enroll with Server` option checked at the end of the installation, or locate the Unreal icon in the system notification area, right-click on it, and select `Enroll with Server`.
5. Choose your agent from the list, and select **Enroll**. This process validates that you trust the agent and permits it to take on work.

* [horde](https://dev.epicgames.com/community/search?query=horde)
* [bronze](https://dev.epicgames.com/community/search?query=bronze)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Introduction](/documentation/en-us/unreal-engine/horde-installation-tutorial-for-unreal-engine?application_version=5.7#introduction)
* [Prerequisites](/documentation/en-us/unreal-engine/horde-installation-tutorial-for-unreal-engine?application_version=5.7#prerequisites)
* [Steps](/documentation/en-us/unreal-engine/horde-installation-tutorial-for-unreal-engine?application_version=5.7#steps)
* [Horde Server](/documentation/en-us/unreal-engine/horde-installation-tutorial-for-unreal-engine?application_version=5.7#hordeserver)
* [Horde Agents](/documentation/en-us/unreal-engine/horde-installation-tutorial-for-unreal-engine?application_version=5.7#hordeagents)
