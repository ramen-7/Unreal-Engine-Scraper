<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/automating-platform-and-sdk-management-with-unreal-turnkey?application_version=5.7 -->

# Unreal Turnkey

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
6. Unreal Turnkey

# Unreal Turnkey

Unreal Turnkey simplifies platform setup by automating SDK installation and management.

![Unreal Turnkey](https://dev.epicgames.com/community/api/documentation/image/b79d341d-543d-4494-8cc8-1b47119a59bd?resizing_type=fill&width=1920&height=335)

 On this page

**Turnkey** is a system introduced in **Unreal Engine 5** that automates most of the steps required for setting up platform support, including finding source files for installing SDKs and flashing dev kits.

Once your organization has set up a filesource repository for Turnkey, individual team members can use a one-click process to set up their system for any target platform. The guides listed on this page will show you how to host SDKs for Turnkey, and how to use Turnkey to download and install them on individual instances of Unreal Engine.

## Overview

Turnkey is an **AutomationTool** script, accessed through `RunUAT.bat`, featuring many tools you can use to interact with SDKs. It accesses the repository you set up for your organization, then automatically downloads files and sets up SDKs from that repository.

When you run Turnkey to install an SDK, it performs the following processes:

* Turnkey starts up and scans for SDKs using the information provided by `TurnkeyManifest.xml`.
* Turnkey selects a platform based on the user's input.
* The build system tells Turnkey what versions of the SDK are valid for the current Unreal Engine version.
* The best SDK is selected from all of the valid SDKs available.
  + Turnkey uses a series of platform-specific rules to convert the version numbers to integers, and the largest number within the range of valid SDKs is selected. These rules are specified in the `*PlatformSDK.cs` files.
* Turnkey downloads the SDK files to the user's machine.
  + If the SDK files are contained in a `.zip` file, they will be automatically decompressed in a temporary location.
* The build system installs the downloaded SDKs.

This provides a way to quickly set up your Unreal Engine project even if there are a large number of available SDK versions, and streamlines maintenance whenever you need to update your available SDKs.

## Setting Up Turnkey

To use Turnkey, you need to host your SDKs in a filesource repository, then set up `TurnkeyManifest.xml` and `TurnkeyStudioSettings.xml` files with the necessary information for Turnkey to discover them.

The pages listed below provide instructions on how to set up each of these components, as well as how to structure directories so that Turnkey's automation will recognize your SDK versions.

[![Setting Up Turnkey For Your Organization](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d04a6bd5-fb78-41e6-9869-a5cff27a5b05/settingupturnkeyforyourorganizationtopicimage.png)

Setting Up Turnkey For Your Organization

Information about how to write Turnkey manifests and set up copy providers for your organization.](/documentation/en-us/unreal-engine/setting-up-turnkey-for-your-organization-in-unreal-engine)
[![Setting Up Google Drive for Unreal Turnkey](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4c8c8434-d647-4d3e-bae3-02ffb4f37a5c/settingupgoogledriveforunrealturnkeytopicimage.png)

Setting Up Google Drive for Unreal Turnkey

How to set up the Google Drive API and host SDKs for use with Unreal Turnkey](/documentation/en-us/unreal-engine/setting-up-google-drive-for-turnkey-for-unreal-engine)

## Usage

Once you have set up Turnkey for your organization, users can interact with it either directly from within Unreal Engine, or using `RunUAT.bat` with a command-line interface. The pages listed below contain information about how to use each of these.

[![Managing Platforms in Unreal Editor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/438a4e65-8061-4e86-b99c-3649fea50780/managingplatformsinunrealenginetopicimage.png)

Managing Platforms in Unreal Editor

Using the new Platform dropdown in Unreal Editor to install SDKs and manage devices](/documentation/en-us/unreal-engine/using-the-platforms-dropdown-in-unreal-editor)
[![Using the Turnkey Commandline](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/89e9d030-413a-462a-bd4e-d44d5333bbe0/usingtheturnkeycommandlinetopicimage.png)

Using the Turnkey Commandline

Reference information for how to run Turnkey from RunUAT.bat using a commandline interface](/documentation/en-us/unreal-engine/using-the-turnkey-commandline-for-unreal-engine)

* [platforms](https://dev.epicgames.com/community/search?query=platforms)
* [turnkey](https://dev.epicgames.com/community/search?query=turnkey)
* [platform sdks](https://dev.epicgames.com/community/search?query=platform%20sdks)
* [sdks](https://dev.epicgames.com/community/search?query=sdks)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Overview](/documentation/en-us/unreal-engine/automating-platform-and-sdk-management-with-unreal-turnkey?application_version=5.7#overview)
* [Setting Up Turnkey](/documentation/en-us/unreal-engine/automating-platform-and-sdk-management-with-unreal-turnkey?application_version=5.7#settingupturnkey)
* [Usage](/documentation/en-us/unreal-engine/automating-platform-and-sdk-management-with-unreal-turnkey?application_version=5.7#usage)
