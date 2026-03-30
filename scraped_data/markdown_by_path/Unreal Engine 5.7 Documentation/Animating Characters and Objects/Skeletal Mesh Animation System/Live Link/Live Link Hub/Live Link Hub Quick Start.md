<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/live-link-hub-quick-start-in-unreal-engine?application_version=5.7 -->

# Live Link Hub Quick Start

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
5. [Animating Characters and Objects](/documentation/en-us/unreal-engine/animating-characters-and-objects-in-unreal-engine "Animating Characters and Objects")
6. [Skeletal Mesh Animation System](/documentation/en-us/unreal-engine/skeletal-mesh-animation-system-in-unreal-engine "Skeletal Mesh Animation System")
7. [Live Link](/documentation/en-us/unreal-engine/live-link-in-unreal-engine "Live Link")
8. [Live Link Hub](/documentation/en-us/unreal-engine/live-link-hub-in-unreal-engine "Live Link Hub")
9. Live Link Hub Quick Start

# Live Link Hub Quick Start

Get started using the Live Link Hub application.

![Live Link Hub Quick Start](https://dev.epicgames.com/community/api/documentation/image/d86532e2-a121-4bf1-877d-535b748787e8?resizing_type=fill&width=1920&height=335)

 On this page

This page provides the basic steps to set up and get started using Live Link Hub.

## Activate Required Plugins in Unreal Editor

To enable the Live Link Hub plugin navigate to **Edit** > **Plugins** and open the **Plugin Browser**. Search for "Live Link".

[![Live Link plugins](https://dev.epicgames.com/community/api/documentation/image/c7275950-d773-48b3-9181-822cf381a75c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c7275950-d773-48b3-9181-822cf381a75c?resizing_type=fit)

Enable the Live Link Hub plugin entry.

Live Link - this plugin is on by default in blank projects. You may have disabled it previously. If so, enable it now.

Restart the editor.

## Launch Live Link Hub

On the menu there will be a new entry for Live Link Hub. Navigate to **Tools->Live Link Hub**.

[![Live Link Hub in the Tools menu](https://dev.epicgames.com/community/api/documentation/image/d6af2b64-0d1d-42c3-9fb6-ccd66329ead8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d6af2b64-0d1d-42c3-9fb6-ccd66329ead8?resizing_type=fit)

This will launch Live Link Hub on your machine.

If you want to run Live Link Hub on a machine that does not have Unreal Engine installed, you can download Live Link Hub from the [Epic Games store](https://store.epicgames.com).

When starting Live Link Hub, any client PCs on the same network, running Unreal Editor with the Live Link Hub Plugin enabled, will be listed in the Clients panel.

Your editor session should already be listed on the right-most Clients panel.

[![An Unreal Editor session in Live Link Hub](https://dev.epicgames.com/community/api/documentation/image/f29e5921-e70e-4712-8097-3c977abba1cf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f29e5921-e70e-4712-8097-3c977abba1cf?resizing_type=fit)

In UE, the message bar will show a green Live Link Connected banner:

[![Live Link Connected banner](https://dev.epicgames.com/community/api/documentation/image/e28c6c8d-d4f1-4c38-9c1c-35b79d8b4077?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e28c6c8d-d4f1-4c38-9c1c-35b79d8b4077?resizing_type=fit)

If there is an error, the message bar will show a warning message:

[![Live Link Hub Error warning message](https://dev.epicgames.com/community/api/documentation/image/b76cf9c6-9814-4ae9-bc7b-3165a631f8ec?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b76cf9c6-9814-4ae9-bc7b-3165a631f8ec?resizing_type=fit)

Open the Live Link panel in UE to check if there is a source listed, labeled Live Link Hub. It should appear as follows:

[![Live Link Hub source in the Live Link panel](https://dev.epicgames.com/community/api/documentation/image/de29f6ed-50c1-4ec2-91df-1081469311c2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/de29f6ed-50c1-4ec2-91df-1081469311c2?resizing_type=fit)

If there is no Live Link Hub source listed, you can add it manually by clicking **+Add Source**.

New clients (engine sessions) are automatically added to Live Link Hub when they are brought online. They will be listed as disconnected when they are no longer connected.

## Add a Source

To add a source of real time animation data, click **+Add Source** on the **Sources** panel:

[![Add a source](https://dev.epicgames.com/community/api/documentation/image/cd4a0e3b-6c45-465b-b442-f4620f84b9f4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cd4a0e3b-6c45-465b-b442-f4620f84b9f4?resizing_type=fit)

Data will be sent to all the connected clients. Your source’s subjects will be listed on the central **Subjects** panel:

[![Your source's subjects](https://dev.epicgames.com/community/api/documentation/image/8e8632eb-bba7-4d79-ad95-e56e67d3bb1d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8e8632eb-bba7-4d79-ad95-e56e67d3bb1d?resizing_type=fit)

And in UE, if you click the Live Link Hub section of the message bar or open the Live Link Panel you will see the subjects listed:

[![Live Link subjects listed in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/7b5ff639-a16c-4765-95f3-514ea47d4c38?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7b5ff639-a16c-4765-95f3-514ea47d4c38?resizing_type=fit)

Data is now streaming to your Unreal Editor(s), to be consumed as described in the [Live Link documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-live-link-data-in-unreal-engine).

## Advanced Topics

### Launching from the Command Line

You can launch Live Link Hub from the command line, which provides access to some additional launch arguments.

If you are running Live Link Hub from an Unreal Engine install, you can optionally enable the following Live Link Plugins in Hub:

* LiveLinkFreeD
* LiveLinkPrestonMDR
* LiveLinkMasterLockit
* LiveLinkVRPN

Press Windows+R and type CMD. Press enter to open a command line window.

Type and execute the following command:

C++

```
[your install directory]\Engine\Binaries\LiveLinkHub.exe -EnablePlugins="LiveLinkFreeD,LiveLinkPrestonMDR,LiveLinkMasterLockit,LiveLinkVRPN"
```

[your install directory]\Engine\Binaries\LiveLinkHub.exe -EnablePlugins="LiveLinkFreeD,LiveLinkPrestonMDR,LiveLinkMasterLockit,LiveLinkVRPN"

Copy full snippet(1 line long)

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [live link](https://dev.epicgames.com/community/search?query=live%20link)
* [animation tool](https://dev.epicgames.com/community/search?query=animation%20tool)
* [bronze](https://dev.epicgames.com/community/search?query=bronze)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Activate Required Plugins in Unreal Editor](/documentation/en-us/unreal-engine/live-link-hub-quick-start-in-unreal-engine?application_version=5.7#activate-required-plugins-in-unreal-editor)
* [Launch Live Link Hub](/documentation/en-us/unreal-engine/live-link-hub-quick-start-in-unreal-engine?application_version=5.7#launch-live-link-hub)
* [Add a Source](/documentation/en-us/unreal-engine/live-link-hub-quick-start-in-unreal-engine?application_version=5.7#add-a-source)
* [Advanced Topics](/documentation/en-us/unreal-engine/live-link-hub-quick-start-in-unreal-engine?application_version=5.7#advanced-topics)
* [Launching from the Command Line](/documentation/en-us/unreal-engine/live-link-hub-quick-start-in-unreal-engine?application_version=5.7#launching-from-the-command-line)
