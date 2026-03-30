<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/change-the-oculus-rift-guardian-system-color-in-unreal-engine?application_version=5.7 -->

# Change the Oculus Rift Guardian System Color

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
10. Change the Oculus Rift Guardian System Color

# Change the Oculus Rift Guardian System Color

Changing the color of the Rift Guardian system.

![Change the Oculus Rift Guardian System Color](https://dev.epicgames.com/community/api/documentation/image/2c044ec2-5268-448a-913b-77d3a08faa13?resizing_type=fill&width=1920&height=335)

 On this page

Skill\_family: Tutorial Level 2
Version: 5.0
Parent: sharing-and-releasing-projects/xr-development/supported-xr-platforms/developing-for-oculus/OculusHowTo
Order: 2
tags: Oculus
topic-image:sharing-and-releasing-projects/xr-development/supported-xr-platforms/developing-for-oculus/OculusHowTo/GuardianSystem\HTGuardian\_System\_Topic\_Image.png
prereq:sharing-and-releasing-projects/xr-development/supported-xr-platforms/developing-for-steamvr/HowTo/StandingCamera
prereq:sharing-and-releasing-projects/xr-development\MotionController
prereq:sharing-and-releasing-projects/xr-development/supported-xr-platforms/developing-for-oculus/OculusHowTo/GuardianSystem

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f312c816-16ab-4967-ab6c-aabd3563d215/htguardian_system_07.png)

The Oculus Guardian system is used to display the boundaries of the VR interaction area. As a tracked device approaches the boundaries, the Oculus Runtime automatically provides visual cues notifying the user of this. In the following tutorial we will take a look at changing the color the Oculus Guardian system uses to display the VR interaction area.

For the Guardian system to work, you will need to make sure you have set it up using the Oculus App. For more information on how to do this, please see the official [Oculus Guardian System](https://developer.oculus.com/documentation/pcsdk/latest/concepts/dg-guardian-system/) Setup pages.



It is **NOT** possible nor advisable to disable the Guardian system from inside UE. You can, however, adjust how UE will react to the user getting close to the boundaries.

## Steps

Make sure that your Pawn has an **OculusRiftBoundary** added to it or the following will not work. If you are not certain how to do this, please see the [Setting Up Guardian System](/documentation/en-us/unreal-engine/set-up-the-oculus-rift-guardian-system-in-unreal-engine) pages for more information on how to do this.

1. Create a new **Variable** called **Oculus Rift Boundary Color** and set its type to **Linear Color** and its color to **Red**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0430a105-f09a-432e-973e-fddf65444a1a/htguardian_system_04.png)
2. In the **Event Graph** add a **Event Begin Play** and **Set Tracking Origin** node. Make sure that the Set Tracking Origin node has had its **Origin** set to **Floor Level** and then connect the Event Begin Play to the Set Tracking Origin node.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d4cae32c-cf9c-467a-ba17-895539e834a6/htguardian_system_02.png)
3. Right - click on the Event Graph and from the menu search for **Set Outer Boundary Color**, clicking on it to add it to the graph.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/07348524-b056-441c-b4d1-edf45fdc162e/htguardian_system_03.png)
4. Drag both the **Oculus Rift Boundary Color** variable and the **Oculus Rift Boundary** component into the Event Graph. Connect the Oculus Rift Boundary Color variable to in the **In Boundary Color** on the Set Boundary Color node and connect the Oculus Rift Boundary to the **Target** input.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/168d482d-58da-40d4-a154-e082b24ac778/htguardian_system_05.png)
5. Connect the output of the Set Tracking Origin node to the input of the Set Outer Boundary Color node and when completed your Event Graph should look like the following.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/69b6c9b4-9508-43ee-bc92-41307d845454/htguardian_system_06.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/69b6c9b4-9508-43ee-bc92-41307d845454/htguardian_system_06.png)

   Click for full image.

## End Result

Now when you run the level and put the Oculus Rift on when the boundary is displayed, it will be the color you set in the Oculus Rift Boundary Color variable.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/92c1ea7e-e858-4d01-a75b-78f4df3c7a69/htguardian_system_07.png)

## UE Project Downloads

Below you will find a link to where you can download the UE project that was used to create this example.

* [**Oculus Rift Guardian System Example Project**](https://epicgames.box.com/s/s4vvkb2i0ohtice8vtqude6i8ih7hy8i)

* [oculus](https://dev.epicgames.com/community/search?query=oculus)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/change-the-oculus-rift-guardian-system-color-in-unreal-engine?application_version=5.7#steps)
* [End Result](/documentation/en-us/unreal-engine/change-the-oculus-rift-guardian-system-color-in-unreal-engine?application_version=5.7#endresult)
* [UE Project Downloads](/documentation/en-us/unreal-engine/change-the-oculus-rift-guardian-system-color-in-unreal-engine?application_version=5.7#ueprojectdownloads)
