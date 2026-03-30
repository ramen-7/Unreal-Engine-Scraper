<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-multi-process-rendering-in-unreal-engine?application_version=5.7 -->

# Getting Started with Multi-Process Rendering

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
5. [Working with Media](/documentation/en-us/unreal-engine/working-with-media-in-unreal-engine "Working with Media")
6. [Integrating Media](/documentation/en-us/unreal-engine/integrating-media-in-unreal-engine "Integrating Media")
7. [Rendering to Multiple Displays with nDisplay](/documentation/en-us/unreal-engine/rendering-to-multiple-displays-with-ndisplay-in-unreal-engine "Rendering to Multiple Displays with nDisplay")
8. [Multi-Process Rendering](/documentation/en-us/unreal-engine/multi-process-rendering-with-unreal-engine "Multi-Process Rendering")
9. Getting Started with Multi-Process Rendering

# Getting Started with Multi-Process Rendering

Learn how to set up multi-process rendering.

![Getting Started with Multi-Process Rendering](https://dev.epicgames.com/community/api/documentation/image/7cf9de57-112e-425e-a05f-4e2b6ff5ac34?resizing_type=fill&width=1920&height=335)

 On this page

## Getting Started

A Multi-Process nDisplay config, whether created from scratch or by converting an existing one, will have the following:

* **Onscreen Nodes:** Each regular “onscreen” nDisplay node has its GPU adapter set to the primary GPU
* **Offscreen Nodes:** Additional “offscreen” nDisplay nodes are added for each host, with the GPU adapter set to the secondary GPU
* **ICVFX Cameras:** The **Shared Media Input** and **Output** are set up for each ICVFX camera component to transfer the render from the offscreen node to the onscreen node. Due to the ICVFX camera rendering on the secondary GPU, a performance advantage is gained.

This guide will outline each of these setup aspects in more detail.

If you would like to learn about creating a new config from scratch, check out the In-Camera VFX Quick Start documentation linked below:

* [In-Camera VFX Quick Start](/documentation/en-us/unreal-engine/in-camera-vfx-quick-start-for-unreal-engine)

## Setting up the Regular Onscreen nDisplay Node

The regular “onscreen” nDisplay node must be set to render on a different GPU than the offscreen node. Setting the regular nDisplay node’s Graphics Adapter to 0 will assign it to the computer’s primary GPU. Note: While this numbering is typical, some machines may require a different number. If you experience unexpected GPU utilization in Switchboard monitor, it may be advisable to change the GPU Index number.

Graphics Adapter settings are found in the Details panel of a node.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/566da169-4b47-41ac-9c29-d6bea0c757bd/gs-0.png)

The regular nDisplay node can be found in the Cluster tab.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d6a1de16-64d0-4502-a180-18edfb7f6dbd/gs-1.png)

Graphics Adapter settings are found in the Details panel of a node.

## Setting up the Offscreen nDisplay Node

An “offscreen” render node is added for each of the host machines:

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d2f6d0a6-0c25-448f-aa79-6945e9eafea2/gs-2.png)

“Add New Cluster Node” can be found in the Cluster tab.

Note the following details in the **Add New Cluster Node** window:

* The **Name** requires a unique identifier. In the example below, “\_OS” has been added to indicate that this is the offscreen node. Note that the rest of the name (“Node\_0”) is kept consistent - this is important so that it is clear which nodes belong to each host machine in Switchboard.
* **Add Viewport to New Cluster Node** is unticked to prevent a viewport from being added. If this option were enabled, the viewport would need to be removed for Headless Rendering.
* **Headless Rendering** is **enabled**. This forces the render to render offscreen, therefore not negatively impacting desktop real estate or interfering with Nvidia Sync.
* **Graphics Adapter** is set to **1**, indicating the secondary GPU. Note: While this numbering is typical, some machines may require a different number.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d6398e0c-e414-4f9d-a389-862d991ca2dd/gs-3.png)

Image highlighting which sections of the Add New Cluster Node window must be updated.

## ICVFX Camera Setup

### Shared Media Input and Output

In the Details panel of the ICVFX component, there is a Media section. In this context, it’s helpful to think of “media” as the inner frustum render, which is transferred from the offscreen node to the regular node and then displayed over the outer frustum. The Media settings control how different types of media are sent and received by nDisplay viewports. Media must be “enabled” and two areas must be configured:

* **Media Output Groups** control where rendered media is sent from.
* **Media Input Groups** control where the rendered media is received.

### Media Output Group

It is essential that all offscreen nodes are added under the **Cluster Nodes Index**. Additionally, a **unique name** (“CameraA”) has been assigned to the Media Output. Since this name is used to receive the texture on the input group, it is case-sensitive and must be unique for each ICVFX camera component.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f1df7f6d-b007-4bd0-9eb0-2120f578213c/gs-4.png)

### Media Input Group

The Media Input Group has a similar setup:

* The regular node has been added to the **Cluster Nodes Index**. All regular nodes should be listed here.
* The **unique name** (“CameraA”) should be **identical** to the one set in the Media Output Section, per ICVFX Camera component.
* Mode is set to **Framelocked**. This ensures that the frames rendered on the offscreen node are correctly paired with the frame currently being rendered on the onscreen node. This is important because the offscreen node is running sync policy none, which is essentially freerunning. Without Framelocked enabled, it could be possible to present a frame that has been received ahead of when it's needed.
* **Zero Latency** is **enabled**. This removes any latency, which is typically used as a buffer to protect against FPS drops. That is redundant for ICVFX since target FPS must always be achieved.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4afd793e-cc14-49f2-a888-460807a639c2/gs-5.png)

Once these settings are updated, **Compile**.

## Reference Project

A reference to a Multi-Process enabled nDisplay config is available in the **InCamera VFX** template project. This can be found via the new project window under **Film/Video & Live Events > InCameraVFX**.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a266dd19-cfaf-4811-b76f-b073ac55b3b3/gs-6.png)

This config can be found in the Content Browser under **Content > InCamVFXBP > nDisplay\_InCamVFX\_MultiProcess\_Config**.

## Running Multi-Process with Switchboard

Once the Multi-Process nDisplay config has been added, both the offscreen and onscreen nodes show as separate devices in Switchboard. [Learn more about Switchboard in Unreal Engine here.](/documentation/en-us/unreal-engine/switchboard-in-unreal-engine)

Connection is required for each node, but only a single instance of the switchboard listener is required per machine.
Both onscreen and offscreen nodes should be launched and run simultaneously. This is best achieved via the Start All Connected nDisplay Devices button.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6ce54aab-988b-4519-a0c7-7d2c8f8d1074/gs-7.png)

* [ndisplay](https://dev.epicgames.com/community/search?query=ndisplay)
* [icvfx](https://dev.epicgames.com/community/search?query=icvfx)
* [bronze](https://dev.epicgames.com/community/search?query=bronze)
* [multi-process rendering](https://dev.epicgames.com/community/search?query=multi-process%20rendering)
* [mgpu](https://dev.epicgames.com/community/search?query=mgpu)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Getting Started](/documentation/en-us/unreal-engine/getting-started-with-multi-process-rendering-in-unreal-engine?application_version=5.7#gettingstarted)
* [Setting up the Regular Onscreen nDisplay Node](/documentation/en-us/unreal-engine/getting-started-with-multi-process-rendering-in-unreal-engine?application_version=5.7#settinguptheregularonscreenndisplaynode)
* [Setting up the Offscreen nDisplay Node](/documentation/en-us/unreal-engine/getting-started-with-multi-process-rendering-in-unreal-engine?application_version=5.7#settinguptheoffscreenndisplaynode)
* [ICVFX Camera Setup](/documentation/en-us/unreal-engine/getting-started-with-multi-process-rendering-in-unreal-engine?application_version=5.7#icvfxcamerasetup)
* [Shared Media Input and Output](/documentation/en-us/unreal-engine/getting-started-with-multi-process-rendering-in-unreal-engine?application_version=5.7#sharedmediainputandoutput)
* [Media Output Group](/documentation/en-us/unreal-engine/getting-started-with-multi-process-rendering-in-unreal-engine?application_version=5.7#mediaoutputgroup)
* [Media Input Group](/documentation/en-us/unreal-engine/getting-started-with-multi-process-rendering-in-unreal-engine?application_version=5.7#mediainputgroup)
* [Reference Project](/documentation/en-us/unreal-engine/getting-started-with-multi-process-rendering-in-unreal-engine?application_version=5.7#referenceproject)
* [Running Multi-Process with Switchboard](/documentation/en-us/unreal-engine/getting-started-with-multi-process-rendering-in-unreal-engine?application_version=5.7#runningmulti-processwithswitchboard)
