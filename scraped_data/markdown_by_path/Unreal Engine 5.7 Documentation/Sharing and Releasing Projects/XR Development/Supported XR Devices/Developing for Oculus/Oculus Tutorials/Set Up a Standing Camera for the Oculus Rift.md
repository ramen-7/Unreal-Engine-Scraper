<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/set-up-a-standing-camera-for-the-oculus-rift-in-unreal-engine?application_version=5.7 -->

# Set Up a Standing Camera for the Oculus Rift

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
5. [Sharing and Releasing Projects](/documentation/en-us/unreal-engine/sharing-and-releasing-projects-for-unreal-engine "Sharing and Releasing Projects")
6. [XR Development](/documentation/en-us/unreal-engine/developing-for-xr-experiences-in-unreal-engine "XR Development")
7. [Supported XR Devices](/documentation/en-us/unreal-engine/supported-xr-devices-in-unreal-engine "Supported XR Devices")
8. [Developing for Oculus](/documentation/en-us/unreal-engine/developing-for-oculus-in-unreal-engine "Developing for Oculus")
9. [Oculus Tutorials](/documentation/en-us/unreal-engine/oculus-how-to-in-unreal-engine "Oculus Tutorials")
10. Set Up a Standing Camera for the Oculus Rift

# Set Up a Standing Camera for the Oculus Rift

Setting up the UE camera to work with a standing Oculus Rift experience.

![Set Up a Standing Camera for the Oculus Rift](https://dev.epicgames.com/community/api/documentation/image/099eb7cb-c544-485e-9d7c-03a7525670f7?resizing_type=fill&width=1920&height=335)

 On this page

Skill\_family: Tutorial Level 1
Version:5.0
Parent: sharing-and-releasing-projects/xr-development/supported-xr-platforms/developing-for-oculus/OculusHowTo
Order: 2
tags:Basics
topic-image:HT\_Rift\_Camera\_Setup\_Topic\_Image.png

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/01028070-330d-4603-8ecb-09cc461cbf54/vr_standing_experience.png)

One of the first things you will need to think about when starting to develop any Unreal Engine (UE) powered VR experience to be used with the Oculus Rift is deciding whether the experience will be a seated one or a standing one. In the following tutorial we will take a look at how to setup your UE projects VR camera for a standing Oculus Rift VR experience.

## Steps

Below you will find instructions on setting up a Pawn to work with a standing Oculus Rift experience.

1. First, open up or create a new Pawn Blueprint and then go to the **Component** section of the **Viewport** tab. From there add the following two components with the following names, making sure that the VRCamera is a child of VRCameraRoot:

   | Component Name | Value |
   | --- | --- |
   | **Scene** | VRCameraRoot |
   | **Camera** | VRCamera |

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/817643da-a144-4f94-980a-3278d9acccb3/ht_rift_camera_setup_03.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/817643da-a144-4f94-980a-3278d9acccb3/ht_rift_camera_setup_03.png)

   Click for full image.

   When

   No matter what VR HMD you are using, this is the Epic recommended way to set up a VR camera as it allows you to offset the position of the camera without having to move the actual camera.
2. Next, open up the Pawn Blueprint if not already open and in the **Event Graph** drag off the **Event Begin Play** node to show the Executable Actions list. In the list search for the **Set Tracking Origin** node and click on it to add it to the Event Graph.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ed47a165-d956-4e93-9575-c611ee07ff3d/ht_rift_camera_setup_09.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ed47a165-d956-4e93-9575-c611ee07ff3d/ht_rift_camera_setup_09.png)

   Click for full image.
3. The Set Tracking Origin node has two options, **Floor Level** and **Eye Level**. For a standing experience, you will need to keep the **Origin** of the Set Tracking Origin node to the default of **Floor Level**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/424ae9fd-a3d1-427d-8bb3-59f1539407f4/ht_rift_camera_setup_10.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/424ae9fd-a3d1-427d-8bb3-59f1539407f4/ht_rift_camera_setup_10.png)

   Click for full image.
4. Drag the Pawn Blueprint from the Content Browser to a level, making sure that it is placed at 0,0,0 in the level.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2b0d7795-b91e-4250-abec-936f04ee96de/ht_rift_camera_setup_06.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2b0d7795-b91e-4250-abec-936f04ee96de/ht_rift_camera_setup_06.png)

   Click for full image.
5. Select the Pawn Blueprint that was put in the level and in the **Details** panel under the **Pawn** setting, set the **Auto Possess Player** from **Disabled** to **Player 0**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/713a12d5-1c06-462a-9bf9-f1b0684389de/ht_rift_standing_camera_04.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/713a12d5-1c06-462a-9bf9-f1b0684389de/ht_rift_standing_camera_04.png)

   Click for full image.

## End Result

Finally, go to the **Main Toolbar** and change the **Play Mode** to **VR Preview** and then press the **Play** button. When you put your Oculus Rift HMD on and view the level while standing, you should see something similar to the following video.

## UE Project Downloads

Below you will find a link to where you can download the UE project that was used to create this example.

* [**Oculus Rift Standing VR Camera Example Project**](https://epicgames.box.com/s/qgoh6uk0f8ra4rtvp0jdrxygfb2n9ykv)

* [basics](https://dev.epicgames.com/community/search?query=basics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/set-up-a-standing-camera-for-the-oculus-rift-in-unreal-engine?application_version=5.7#steps)
* [End Result](/documentation/en-us/unreal-engine/set-up-a-standing-camera-for-the-oculus-rift-in-unreal-engine?application_version=5.7#endresult)
* [UE Project Downloads](/documentation/en-us/unreal-engine/set-up-a-standing-camera-for-the-oculus-rift-in-unreal-engine?application_version=5.7#ueprojectdownloads)
