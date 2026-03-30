<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/converting-from-mgpu-to-multi-process-rendering-in-unreal-engine?application_version=5.7 -->

# Converting from mGPU to Multi-Processing Rendering

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
9. Converting from mGPU to Multi-Processing Rendering

# Converting from mGPU to Multi-Processing Rendering

Convert an existing multi-GPU config for multi-process rendering.

![Converting from mGPU to Multi-Processing Rendering](https://dev.epicgames.com/community/api/documentation/image/97c08116-1680-484c-b070-93fa38c7a631?resizing_type=fill&width=1920&height=335)

 On this page

## Converting an mGPU Config

Existing nDisplay ICVFX users may have already used Multi-GPU and have configs that they would like to convert for multi-process rendering. Some settings on the computer and in Unreal Engine must be changed to make this possible.

The following section is focused on converting an existing nDisplay config from Multi-GPU to Multi-Process. With the knowledge gained on the [Getting Started page](/documentation/en-us/unreal-engine/getting-started-with-multi-process-rendering-in-unreal-engine), this section is written as a step-by-step guide to provide a practical example.

### Settings

These NVIDIA Control Panel settings are specific to the context of converting a Multi-GPU config to Multi-Process. To access the NVIDIA Control Panel, right-click on your computer desktop and select it from the context menu.

* **SLI:** A machine set up for mGPU will have SLI enabled. We’ll go to the section titled Set SLI and PhysX Configuration and **disable SLI**.
* **Mosaic:** Multi-GPU uses maximum GPU topology, while Multi-Process requires minimum GPU topology. If you are using Mosaic, then this setting will need to be changed under the Set Up Mosaic section of the NVIDIA Control Panel. If you are not using Mosaic then this setting does not apply.

### Adding Offscreen Nodes

The nDisplay config in this example is slightly more complex and has a few more nodes to represent what advanced users will likely be working with.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6e5b7af8-77b8-4df4-a673-e8e5efd9d799/conversion-1.png)

In the Cluster panel, select the host of each machine and **+add** a new Cluster Node.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f69f5837-a08b-44bd-bfd1-df27c32267ff/conversion-2.png)

In the **Add New Cluster Node** window, adjust the following settings:

Using the naming conventions of the nodes we already have, I’m naming this Node\_1\_OS to indicate that it is offscreen.

**Disable** Adding a Viewport.

**Enable** Headless Rendering.

Keep the IP Address the same, so it matches the regular onscreen node address.

Set the **Graphics Adapter** to **1**, which is our secondary GPU.

Click **Add**.

For more information on the Add New Cluster Node settings, check out the [Getting Started page](/documentation/en-us/unreal-engine/getting-started-with-multi-process-rendering-in-unreal-engine).

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/479c8ce8-22f7-45ff-a0cd-ccfeac7436d7/conversion-3.png)

**I’ll go ahead and repeat that process for the other nodes.** We will end up with Node\_2\_OS and Node\_3\_OS, all with the same settings as above.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7179fa66-3bea-4a53-8691-f24b8070455b/conversion-4.png)

### Camera Setup

Next, we need to set up our ICVFXCamera component. In this project, we have two cameras, which means we also have two frustums.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f1c49f0b-0d64-4916-8ff8-496d650def3e/conversion-5.png)

We will open the Details panel for the first ICVFX Camera. These initial steps are the same as when we created a Multi-Process Rendering config in the Getting Started section.

In this example, instead of just one node, we have three nodes that will receive information in the project. Use the dropdown menu to set them to **Node\_1, Node\_2, and Node\_3**.

The Media Source will be **Shared Media**.

I’ll set the Unique Name to **ICVFXCamA**.

Now we’ll set up our **Output Group**. We’ll again add three nodes, but this time we will set them to **Node\_1\_OS, Node\_2\_OS, and Node\_3\_OS**.

The Media Source will be **Shared Media**.

The Unique Name will be exactly the same - **ICVFXCamA**. We recommend copying and pasting because it is string-sensitive, and even slight differences in the names can cause errors.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c8dafe7e-949a-4d25-ad16-ffd1e4f434fd/conversion-6.png)

Now we will repeat those steps for the second camera, but with a different Unique Name. This is very important - I’ll name mine **ICVFXCamB**.

**Compile** and save.

## Switchboard

In the Switchboard you can see that we have three Multi-Process Nodes and three regular nDisplay nodes. All six of these need to be launched because for each machine there is both a regular nDisplay render node and an offscreen render node.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0a172bc7-345d-4572-a2ff-7368ace0f70a/conversion-7.png)

Your Multi-GPU config is now converted and ready to be used for Multi-Process rendering!

* [ndisplay](https://dev.epicgames.com/community/search?query=ndisplay)
* [icvfx](https://dev.epicgames.com/community/search?query=icvfx)
* [bronze](https://dev.epicgames.com/community/search?query=bronze)
* [multi-process rendering](https://dev.epicgames.com/community/search?query=multi-process%20rendering)
* [mgpu](https://dev.epicgames.com/community/search?query=mgpu)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Converting an mGPU Config](/documentation/en-us/unreal-engine/converting-from-mgpu-to-multi-process-rendering-in-unreal-engine?application_version=5.7#convertinganmgpuconfig)
* [Settings](/documentation/en-us/unreal-engine/converting-from-mgpu-to-multi-process-rendering-in-unreal-engine?application_version=5.7#settings)
* [Adding Offscreen Nodes](/documentation/en-us/unreal-engine/converting-from-mgpu-to-multi-process-rendering-in-unreal-engine?application_version=5.7#addingoffscreennodes)
* [Camera Setup](/documentation/en-us/unreal-engine/converting-from-mgpu-to-multi-process-rendering-in-unreal-engine?application_version=5.7#camerasetup)
* [Switchboard](/documentation/en-us/unreal-engine/converting-from-mgpu-to-multi-process-rendering-in-unreal-engine?application_version=5.7#switchboard)
