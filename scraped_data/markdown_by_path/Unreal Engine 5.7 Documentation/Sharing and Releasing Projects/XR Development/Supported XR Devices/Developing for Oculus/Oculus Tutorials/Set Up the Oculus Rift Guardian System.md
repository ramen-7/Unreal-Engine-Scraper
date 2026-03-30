<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/set-up-the-oculus-rift-guardian-system-in-unreal-engine?application_version=5.7 -->

# Set Up the Oculus Rift Guardian System

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
10. Set Up the Oculus Rift Guardian System

# Set Up the Oculus Rift Guardian System

Setting up the Rift Guardian System for room scale VR.

![Set Up the Oculus Rift Guardian System](https://dev.epicgames.com/community/api/documentation/image/7574fe3b-fb73-4ddc-83d6-6c11a02507dd?resizing_type=fill&width=1920&height=335)

###### Prerequisite topics

In order to understand and use the content on this page, make sure you are familiar with the following topics:

* [Motion Controller Component Setup](/documentation/en-us/unreal-engine/motion-controller-component-setup-in-unreal-engine)

 On this page

Skill\_family: Tutorial Level 1
Version: 5.0
Parent: sharing-and-releasing-projects/xr-development/supported-xr-platforms/developing-for-oculus/OculusHowTo
Order: 4
tags: Basics
topic-image:HTGuardian\_System\_Topic\_Image.png
prereq:sharing-and-releasing-projects/xr-development/supported-xr-platforms/developing-for-steamvr/HowTo/StandingCamera
prereq:sharing-and-releasing-projects/xr-development/making-interactive-xr-experiences/set-up-motion-controllers

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2ef9f2d3-87ee-49db-8dde-ab8d5d25f7f8/htguardian_system_hero_image.png)

The Oculus Guardian system is used to display the boundaries of the VR interaction area. As a tracked device approaches the boundaries, the Oculus Runtime automatically provides visual cues notifying the user of this. In the following tutorial we will take a look at adding the Oculus Guardian system to your UE projects player Pawn.

For the Guardian system to work, you will need to make sure you have set it up using the Oculus App. For more information on how to do this, please see the official [Oculus Guardian System](https://developer.oculus.com/documentation/pcsdk/latest/concepts/dg-guardian-system/) Setup pages.



It is **NOT** possible nor advisable to disable the Guardian system from inside UE. You can, however, adjust how UE will react to the user getting close to the boundaries.

## Steps

To add the Oculus Rift Guardian system to your UE player pawn, you will need to do the following:

1. Open up your projects player Pawn Blueprint and make sure the **Components** tab is visible.
2. Click on the **Add Component** button and from the displayed list search for the **OculusRiftBoundy** component. When located, click on it to add it to the Component list.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/42733999-05bd-4560-94e4-0256c3602eb7/htguardian_system_00.png)
3. When completed, your player pawn should look like the following image.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0c1b8b1c-f052-4862-b19e-b36d07214aae/htguardian_system_01.png)

## End Result

Now, launch your project in VR and put on your Rift HMD and when you approach the bounds of your VR interaction area, you should see something similar to the following video.

## UE Project Downloads

Below you will find a link to where you can download the UE project that was used to create this example.

* [**Oculus Rift Guardian System Set Up Project**](https://epicgames.box.com/s/s4vvkb2i0ohtice8vtqude6i8ih7hy8i)

* [basics](https://dev.epicgames.com/community/search?query=basics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/set-up-the-oculus-rift-guardian-system-in-unreal-engine?application_version=5.7#steps)
* [End Result](/documentation/en-us/unreal-engine/set-up-the-oculus-rift-guardian-system-in-unreal-engine?application_version=5.7#endresult)
* [UE Project Downloads](/documentation/en-us/unreal-engine/set-up-the-oculus-rift-guardian-system-in-unreal-engine?application_version=5.7#ueprojectdownloads)
