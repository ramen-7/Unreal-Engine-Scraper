<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/virtual-camera-multiuser-quickstart-guide-in-unreal-engine?application_version=5.7 -->

# Virtual Camera Multi-User Quick-Start Guide

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
6. [Cinematics and Sequencer](/documentation/en-us/unreal-engine/cinematics-and-movie-making-in-unreal-engine "Cinematics and Sequencer")
7. [Cameras in Sequencer](/documentation/en-us/unreal-engine/movie-and-cinematic-cameras-in-unreal-engine "Cameras in Sequencer")
8. [Virtual Cameras](/documentation/en-us/unreal-engine/virtual-cameras-in-unreal-engine "Virtual Cameras")
9. Virtual Camera Multi-User Quick-Start Guide

# Virtual Camera Multi-User Quick-Start Guide

Use Switchboard to connect multiple users to simultaneously operate Virtual Cameras.

![Virtual Camera Multi-User Quick-Start Guide](https://dev.epicgames.com/community/api/documentation/image/a104c527-b4ec-4dda-b56d-aa02adab844a?resizing_type=fill&width=1920&height=335)

 On this page

You can use a **Multi-User** **Virtual Camera** (**VCam**) workspace to control and render Vcams in the same scene using multiple workstations. This lets multiple users simultaneously work on the same scene. **Multi-User Vcam** Multi-User Actor Replication feature, which is in beta.

Multi-User Vcam can only be used in Virtual Production projects.

This document provides an example workflow, which you can use to set up a connected work environment that enables [multiple users](https://dev.epicgames.com/documentation/en-us/unreal-engine/multi-user-editing-in-unreal-engine) to operate [VCams](https://dev.epicgames.com/documentation/en-us/unreal-engine/BlueprintAPI/VirtualCamera) in the same scene simultaneously.

#### Prerequisites

* Enable the **Multi-User Editing** [Plugin](https://dev.epicgames.com/documentation/en-us/unreal-engine/plugins-in-unreal-engine). In the **Menu Bar**, navigate to **Edit** > **Plugins**, and locate the **Multi-User Editing** plugin under the **Editor** section. Alternatively, you can use the **Search Bar**. After enabling the plugin, restart the editor.

[![The Plugins window showing the Multi-User Plugin](https://dev.epicgames.com/community/api/documentation/image/07ed671d-613d-438f-a1f8-986732d2752f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/07ed671d-613d-438f-a1f8-986732d2752f?resizing_type=fit)

* You must have a functional **Virtual Production** project. If you do not have one, you can use the [Template](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-projects-and-templates-in-unreal-engine) project.
* You must have a **Multi-User Editor Server**. For more information, refer to the [Multi-User Quick Start Guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/multi-user-editing-in-unreal-engine).
* Your project must have a [Virtual Camera (VCam) Actor](https://dev.epicgames.com/documentation/en-us/unreal-engine/controlling-a-virtual-camera-actor-using-live-link-in-unreal-engine).

#### Launching an MU Session

Replication of a virtual camera between instances of Unreal Engine uses Multi-User Editing. All clients must be in a shared Multi-User (MU) session. For more information on joining an MU, session see [Multi-User Editing in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/multi-user-editing-in-unreal-engine)

#### Replicating a VCam Actor

When a VCam actor is added to the scene in an MU session, the actor is displayed in the editor on every client. This is because no client has declared that it is the author of the VCam’s properties.

To declare authorship over a VCam, tap or click the **Multi User** button in the lower left corner of the VCam. This disables the output providers and modifier stack evaluation on the other clients, which hides the HUD and ensures that this client determines the values used by the Vcam. Tapping again relinquishes authorship and enables the output providers, HUD, and modifiers on every client so that a new client can claim authorship.

[![](https://dev.epicgames.com/community/api/documentation/image/45f97f85-93dc-43e6-97a4-c38d237e3d00?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/45f97f85-93dc-43e6-97a4-c38d237e3d00?resizing_type=fit)

#### Recording Remotely

To record a Virtual Camera on a machine other than its host machine, you must add its respective Record Camera (named [VCamActorName]\_Record) to [Take Recorder](https://dev.epicgames.com/documentation/en-us/unreal-engine/record-gameplay-in-unreal-engine), rather than the VCamActor itself.

## Legacy Roles for MU

The legacy Virtual Camera Multi-User workflows are deprecated, but still function in Unreal Engine 5.4.

This workflow does not support new, high-frequency replication

This section provides an example workflow for using the legacy system for limited, low-frequency virtual camera operation in Multi-User mode.

#### Prerequisites

* Enable the **Switchboard** [Plugin](https://dev.epicgames.com/documentation/en-us/unreal-engine/plugins-in-unreal-engine). In the **Menu Bar**, navigate to **Edit** > **Plugins** and locate the **Switchboard** plugin under the **Virtual Production** section. Alternatively, you can use the **Search Bar**. After enabling the Plugin, restart the editor.

[![image alt text](https://dev.epicgames.com/community/api/documentation/image/5907e048-ebc1-4a55-9fcc-1798ff55093f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5907e048-ebc1-4a55-9fcc-1798ff55093f?resizing_type=fit)

You can access the Switchboard application using the Icon in the Unreal Engine Toolbar, after the plugin has been successfully installed.

[![image alt text](https://dev.epicgames.com/community/api/documentation/image/45ae9f03-458a-4840-b403-7000c6511deb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/45ae9f03-458a-4840-b403-7000c6511deb?resizing_type=fit)

* You must have a functional **Virtual Production** project. If you do not have one, you can use the [Template](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-projects-and-templates-in-unreal-engine) project.
* You must have a **Multi-User Editor Server**. For more information, refer to the [Multi-User Quick Start Guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/multi-user-editing-in-unreal-engine).
* Your project must have a [Virtual Camera (VCam) Actor](https://dev.epicgames.com/documentation/en-us/unreal-engine/controlling-a-virtual-camera-actor-using-live-link-in-unreal-engine).

## Declare Virtual Production Roles

The **Switchboard** application requires each user to occupy a **VP Role**, such as an **Editor** or **Render**, to differentiate and identify which user is associated with which VCam Actor.

1. On your primary workstation in the Unreal Editor, navigate to the Toolbar, and select the **VP Roles**, then select (**+**) **Add Role** from the drop-down menu. Give the new role a name. In this workflow example the primary workstation is named Editor.

   [![](https://dev.epicgames.com/community/api/documentation/image/c576c77f-fb6e-4d14-a11b-5b3b94de16c5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c576c77f-fb6e-4d14-a11b-5b3b94de16c5?resizing_type=fit)

   [![](https://dev.epicgames.com/community/api/documentation/image/dcb2af16-a4e2-4951-8865-a60625b80910?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dcb2af16-a4e2-4951-8865-a60625b80910?resizing_type=fit)
2. Using the same steps, add a second **Role** for your secondary device to occupy. In this workflow example, the secondary workstation is named Render.

   [![](https://dev.epicgames.com/community/api/documentation/image/60a3a0f8-7ecc-4b0e-97cf-88f5ad066a00?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/60a3a0f8-7ecc-4b0e-97cf-88f5ad066a00?resizing_type=fit)
3. In the **Menu Bar**, navigate to **Edit** > **Project Settings**, and under the **Multi-User Editing** section,set the **Validation Mode** property to **Soft**, using the drop-down menu.

   [![](https://dev.epicgames.com/community/api/documentation/image/64897658-2a64-427c-a6f7-896981a116fa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/64897658-2a64-427c-a6f7-896981a116fa?resizing_type=fit)

If your project contains any dirty packages, an error prompt displays when you join a multi-user session. You then have the opportunity to cancel the connection or to fix any present issues. If you choose to proceed any dirty packages will be deleted.

Your project is now ready to connect other devices using Switchboard for multiple users to operate VCams simultaneously in the same scene.

For more information about connecting multiple users using the **Switchboard** plugin, refer to the [Switchboard](https://dev.epicgames.com/documentation/en-us/unreal-engine/switchboard-in-unreal-engine) and the [Switchboard Quick-Start Guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/switchboard-quick-start-for-unreal-engine) documentation.

## Connect Your Devices

After creating your VP Roles in the Unreal Editor, use the Switchboard application to connect your devices to the Multi-User session.

1. In the Toolbar, click the options menu next to the Switchboard button, and select **Launch Switchboard Listener.**

   [![image alt text](https://dev.epicgames.com/community/api/documentation/image/9c7d9d99-7328-4470-818e-a86fe5e4f0d8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9c7d9d99-7328-4470-818e-a86fe5e4f0d8?resizing_type=fit)
2. In the Toolbar, launch the **Switchboard application**.

   [![image alt text](https://dev.epicgames.com/community/api/documentation/image/07dbf6f2-103f-43ff-b8a3-8f1b2d49ecd4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/07dbf6f2-103f-43ff-b8a3-8f1b2d49ecd4?resizing_type=fit)
3. In the **Add Device** drop-down, select **Unreal**. This creates a new Switchboard Device, which represents the primary workstation.

   [![image alt text](https://dev.epicgames.com/community/api/documentation/image/638e4a9d-c987-480c-a799-80bdfebd0196?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/638e4a9d-c987-480c-a799-80bdfebd0196?resizing_type=fit)
4. In the provided field, set the **Name** and **IP Address** for the primary work station. The name must be the same name as the primary workstation role set in Unreal Engine. This workflow example uses **Editor** as the name.

   [![image alt text](https://dev.epicgames.com/community/api/documentation/image/009ccf3a-aeec-4063-af3d-2b8ddf22f232?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/009ccf3a-aeec-4063-af3d-2b8ddf22f232?resizing_type=fit)
5. Repeat steps 1-3 to create a second Switchboard Device. For the second device, use the same name as the second workstation's role. Both devices should now be listed in the Switchboard application, in the **Unreal Devices** list. This workflow example uses the name **Render**.

   [![image alt text](https://dev.epicgames.com/community/api/documentation/image/6c1ce74b-01d3-47d4-a1f0-c76356bfbd3c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6c1ce74b-01d3-47d4-a1f0-c76356bfbd3c?resizing_type=fit)
6. To automatically open a network connection and to connect a device to the Multi-User Editor session, select the **Auto-Join** and **Network Connection** icons for each device in the **Unreal Devices** list. When a device successfully connects to the network, the **Connection Indicator** appears blue.

   [![image alt text](https://dev.epicgames.com/community/api/documentation/image/911c9674-746d-4bba-bc15-d6280a603659?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/911c9674-746d-4bba-bc15-d6280a603659?resizing_type=fit)
7. Assign a **VP Role** to each connected device. In the Switchboard's **Menu Bar**, navigate to **Settings** > **Settings**, and scroll down to each connected device's section. In the **Roles** property, select one of the Unreal Engine **VP Roles**, for each device, using the drop-down menu.

   [![image alt text](https://dev.epicgames.com/community/api/documentation/image/c9e6a0c5-3f53-42e2-9b7d-aa4ab02b15a1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c9e6a0c5-3f53-42e2-9b7d-aa4ab02b15a1?resizing_type=fit)

You can open a **Network Connection** and enable **Auto-Join** for every listed device by using the **Auto-Join** and **Network Connection** icons in the Unreal Device's list header.

[![image alt text](https://dev.epicgames.com/community/api/documentation/image/b9490338-10d2-421a-882c-6a57d846a737?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b9490338-10d2-421a-882c-6a57d846a737?resizing_type=fit)

With your workstations connected, and their roles assigned, you can now launch each device and start operating VCams in a Multi-User environment.

## Multi-User Virtual Camera Operation

1. To connect your primary workstation to the multi-user session, open the Switchboard application, go to the **Unreal Devices** list, locate the primary **Editor** device, and click the **Launch**.

   [![image alt text](https://dev.epicgames.com/community/api/documentation/image/69bd6a81-fac4-4516-b698-004ebc79b692?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/69bd6a81-fac4-4516-b698-004ebc79b692?resizing_type=fit)

   Once your project has launched, you can verify that the editor is connected to the multi-user session in the **Multi-User Browser** window. You can open the Multi-User Browser in the Menu bar, navigating to **Window** > **Multi-User Browser**.

   [![image alt text](https://dev.epicgames.com/community/api/documentation/image/e862b765-f9e5-43b6-8b2b-87177f11d608?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e862b765-f9e5-43b6-8b2b-87177f11d608?resizing_type=fit)
2. In the **World Outliner**, select the **VCamActor**.
3. Select the **VCam component** in the VCam actor's **Details** panel.
4. Set the **Role** property to **Edit** in the **Virtual Camera** properties section and select the **Editor** VP Role from the drop down menu.

   [![image alt text](https://dev.epicgames.com/community/api/documentation/image/a72a0b4d-b3d5-457d-b900-b00e0d4cf0b6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a72a0b4d-b3d5-457d-b900-b00e0d4cf0b6?resizing_type=fit)
5. Enable the Virtual Camera by toggling the **Enabled** property.
6. In the Switchboard application, launch the **Render** device by clicking the **Launch** icon. Following the steps above, verify that the secondary **Render** device is also connected to the multi-user session, using the **Multi-User Browser** window.
7. Now that both editor instances are open, move the **Virtual Camera** on the primary **Editor** device and see the changes replicated in the secondary **Render** device in real time. In the example below the **Editor** device (**Left**) is operating a **VCam Actor** and the **Render** device (**Right**) is receiving the changes and rendering the scene.

* [getting started](https://dev.epicgames.com/community/search?query=getting%20started)
* [virtual camera](https://dev.epicgames.com/community/search?query=virtual%20camera)
* [switchboard](https://dev.epicgames.com/community/search?query=switchboard)
* [working with media](https://dev.epicgames.com/community/search?query=working%20with%20media)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisites](/documentation/en-us/unreal-engine/virtual-camera-multiuser-quickstart-guide-in-unreal-engine?application_version=5.7#prerequisites)
* [Launching an MU Session](/documentation/en-us/unreal-engine/virtual-camera-multiuser-quickstart-guide-in-unreal-engine?application_version=5.7#launching-an-mu-session)
* [Replicating a VCam Actor](/documentation/en-us/unreal-engine/virtual-camera-multiuser-quickstart-guide-in-unreal-engine?application_version=5.7#replicating-a-v-cam-actor)
* [Recording Remotely](/documentation/en-us/unreal-engine/virtual-camera-multiuser-quickstart-guide-in-unreal-engine?application_version=5.7#recording-remotely)
* [Legacy Roles for MU](/documentation/en-us/unreal-engine/virtual-camera-multiuser-quickstart-guide-in-unreal-engine?application_version=5.7#legacy-roles-for-mu)
* [Prerequisites](/documentation/en-us/unreal-engine/virtual-camera-multiuser-quickstart-guide-in-unreal-engine?application_version=5.7#prerequisites)
* [Declare Virtual Production Roles](/documentation/en-us/unreal-engine/virtual-camera-multiuser-quickstart-guide-in-unreal-engine?application_version=5.7#declare-virtual-production-roles)
* [Connect Your Devices](/documentation/en-us/unreal-engine/virtual-camera-multiuser-quickstart-guide-in-unreal-engine?application_version=5.7#connect-your-devices)
* [Multi-User Virtual Camera Operation](/documentation/en-us/unreal-engine/virtual-camera-multiuser-quickstart-guide-in-unreal-engine?application_version=5.7#multi-user-virtual-camera-operation)

Related documents

[Multi-User Editing in Unreal Engine

![Multi-User Editing in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/2b6f163b-4521-4112-a24e-0ccfdcc6906e?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/multi-user-editing-in-unreal-engine)
