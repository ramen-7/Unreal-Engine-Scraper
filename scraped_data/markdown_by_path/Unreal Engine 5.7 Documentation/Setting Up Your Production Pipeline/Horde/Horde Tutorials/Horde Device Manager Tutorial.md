<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/horde-device-manager-tutorial-for-unreal-engine?application_version=5.7 -->

# Horde Device Manager Tutorial

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
8. Horde Device Manager Tutorial

# Horde Device Manager Tutorial

A tutorial for using the Horde device manager with Unreal Engine.

![Horde Device Manager Tutorial](https://dev.epicgames.com/community/api/documentation/image/9a4b488a-9bc2-46ed-a3e2-32fc9c9d80be?resizing_type=fill&width=1920&height=335)

 On this page

## Introduction

Horde includes a [device manager](/documentation/en-us/unreal-engine/horde-devices-for-unreal-engine) for maintaining mobile and console development kit resources. Managed devices are reserved by automated tests using a simple REST api. Additionally, devices may be partitioned into user pools that support checkouts of shared remote devices for manual testing and development.

The device manager includes a dashboard UI which makes it easy to administer and monitor devices. Device usage generates telemetry which can be viewed to help allocate and schedule tests. The Horde device manager is used extensively at Epic and is battle tested with features such as automatic problem reporting, kit rollover on errors, and integration with Slack.

While the device manager is integreated with Horde [build automation](/documentation/en-us/unreal-engine/horde-build-automation-for-unreal-engine), it is possible to use it in isolation via the REST api.

## Prerequisites

* Horde Server and an Android phone or tablet (see the [Horde Installation Tutorial](/documentation/en-us/unreal-engine/horde-installation-tutorial-for-unreal-engine)).

## Steps

1. Navigate to the Device management view on the Horde dashboard

   ![Device Navigation](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ba3d27fe-ebe6-4374-8d68-a1e4a977e26f/tutorial-devicemanager-devices.png)
2. The example Horde configuration includes a definition for the Android platform. It also defines a shared and automation pool which devices can be partioned into for user checkouts and automated testing respectively.

   ```
        "devices": {
        "platforms": [
            {
            "id": "android",
            "name": "Android"
            }
        ],
        "pools": [
            {
            "id": "ue5",
            "name": "UE5",
            "poolType": "Automation"
            },
            {
            "id": "remote-ue5",
            "name": "Remote UE5",
            "poolType": "Shared"
            }
        ]
        }
   Copy full snippet
   ```

   Click Add Device and fill out the new device form including the devices IP. Select the example UE5 automation pool to assign the device for this workload.

   ![New Device](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d72bb8b8-284f-44da-a17f-5597cf9136f4/tutorial-devicemanager-newdevice.png)

   Once saved, the Android device will be added and available for work. The device can also be edited, maintenance notes applied, and historical job details viewed.

   ![Device Added](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f82396e3-64c5-4f36-a962-6dfda89ca071/tutorial-devicemanager-deviceadded.png)
3. Optionally repeat step 2 selecting a shared pool instead for the device. This will populate the Shared device pivot, making that device available for users to check out.

* [horde](https://dev.epicgames.com/community/search?query=horde)
* [bronze](https://dev.epicgames.com/community/search?query=bronze)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Introduction](/documentation/en-us/unreal-engine/horde-device-manager-tutorial-for-unreal-engine?application_version=5.7#introduction)
* [Prerequisites](/documentation/en-us/unreal-engine/horde-device-manager-tutorial-for-unreal-engine?application_version=5.7#prerequisites)
* [Steps](/documentation/en-us/unreal-engine/horde-device-manager-tutorial-for-unreal-engine?application_version=5.7#steps)
