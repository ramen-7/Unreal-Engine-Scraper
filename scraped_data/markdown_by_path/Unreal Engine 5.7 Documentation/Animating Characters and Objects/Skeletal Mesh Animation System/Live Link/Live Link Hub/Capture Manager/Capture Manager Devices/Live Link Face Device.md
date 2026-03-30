<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/live-link-face-device?application_version=5.7 -->

# Live Link Face Device

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
9. [Capture Manager](/documentation/en-us/unreal-engine/capture-manager "Capture Manager")
10. [Capture Manager Devices](/documentation/en-us/unreal-engine/capture-manager-devices "Capture Manager Devices")
11. Live Link Face Device

# Live Link Face Device

An overview of the Live Link Face device provided by Capture Manager.

![Live Link Face Device](https://dev.epicgames.com/community/api/documentation/image/a4daa5eb-637d-44e6-ab9b-4d8d5a4bce7e?resizing_type=fill&width=1920&height=335)

 On this page

The **Live Link Face** device enables the ingest of takes directly from a connected iOS device running the [Live Link Face App](https://dev.epicgames.com/documentation/en-us/metahuman/live-link-face-app?application_version=5.6). When using this device, make sure the LiveLink Face application is running in the foreground (is active).

Although the Live Link Face application is available on Android devices for real time animation in MetaHuman Animator, it does not support capture for offline processing.

[![Device Details Live Link Face](https://dev.epicgames.com/community/api/documentation/image/edf08bf3-7bc9-4f99-a953-b0194ce711c4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/edf08bf3-7bc9-4f99-a953-b0194ce711c4?resizing_type=fit)

* **Display Name**: The name of the device as it will appear in the **Devices** list.
* **Ip Address**: The IP address of the device on the network.
* **Port**: The port of the device on the network.
* **Connect**: Tokens that can be extracted from the folder and file name of the audio file to identify the take.

Live Link Hub and the mobile device must be able to connect across the network; make sure your network settings, firewalls, VPNs, and so on are set to allow this connection.

## Capturing Data

It is possible to trigger recording in the Live Link Face app from the Live Link Hub Live Data layout. This will pass **Session**, **Slate**, and **Take** information to the app.

[![Capturing Data](https://dev.epicgames.com/community/api/documentation/image/ef98c442-6304-4a68-9d88-aebc4133aaac?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ef98c442-6304-4a68-9d88-aebc4133aaac?resizing_type=fit)

This will trigger recording on all connected Live Link Hub devices; it is not possible to trigger a specific device.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Capturing Data](/documentation/en-us/unreal-engine/live-link-face-device?application_version=5.7#capturingdata)
