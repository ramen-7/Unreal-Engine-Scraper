<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/openxr-input-in-unreal-engine?application_version=5.7 -->

# OpenXR Input

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
7. [Making Interactive XR Experiences](/documentation/en-us/unreal-engine/making-interactive-xr-experiences-in-unreal-engine "Making Interactive XR Experiences")
8. OpenXR Input

# OpenXR Input

OpenXR runtimes provide controller emulation to support as many platforms as possible, and controller and hand poses to create immersive interactions.

![OpenXR Input](https://dev.epicgames.com/community/api/documentation/image/9d58855d-e6dc-48b7-906e-cdc4a51e61de?resizing_type=fill&width=1920&height=335)

 On this page

The OpenXR runtime uses [interaction profiles](https://www.khronos.org/registry/OpenXR/specs/1.0/html/xrspec.html#semantic-path-interaction-profiles) to support various hardware controllers and provide action bindings for whichever controller is connected. OpenXR input mapping in Unreal Engine relies on the [Action Mappings Input System](/documentation/en-us/unreal-engine/input-in-unreal-engine) to connect actions to the OpenXR interaction profiles. See [Creating New Inputs](/documentation/en-us/unreal-engine/setting-up-user-inputs-in-unreal-engine) for a guide on how to use the Action Mappings Input System.

The OpenXR input system is designed to provide cross-device compatibility by emulating any controller mapping that isn't explicitly specified with **Action Mappings** in the Unreal project. When emulating controller mappings, the OpenXR runtime chooses controller bindings that closely match the user's controller.
Because OpenXR provides this cross-compatibility for you, you should only add bindings for controllers you support and can test with. Any bindings you specify for a controller define what actions are connected to that controller. If you only partially apply bindings to a controller, then the controller won't support any missing bindings.
In the example below, the project has two actions: **Jump** and **Pickup**.

* **Jump** is mapped to keys on multiple controllers, such as **Vive Index (L) Trigger** and **Oculus Touch (L) Trigger**.
* **Pickup** is only mapped to **Valve Index (L) A Touch**.
  In this case, the OpenXR runtime will not emulate any of the other controllers for the **Pickup** action, because those controllers have bindings for **Jump** but not for **Pickup**. If the keys for the other controllers were removed from **Jump**, then the OpenXR runtime would be able to emulate the controllers for both **Jump** and **Pickup**.

![Example engine input action mappings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8d341a62-a412-411d-8d96-f08cf46f266a/engine_input_2.png)


Some runtimes may only support a single interaction profile and do not have the ability to emulate any other profile. You should add bindings for as many devices as you have access to and plan to support.

## Poses

OpenXR provides two poses to represent how a user would hold their hand when performing the actions:

* **Grip:** Represents the position and orientation of the user's closed hand in order to hold a virtual object.
* **Aim:** Represents a ray from the user's hand or controller used to point at a target.
  See the OpenXR [specification](https://www.khronos.org/registry/OpenXR/specs/1.0/html/xrspec.html) for more details on the two poses. In Unreal Engine, these two poses are represented as motion sources and are returned in the results when you call [Enumerate Motion Sources](https://docs.unrealengine.com/en-US/BlueprintAPI/Input/MotionTracking/EnumerateMotionSources/index.html), if they're available for your device.

Unreal Engine uses a different coordinate system than what's described in the OpenXR specification. Unreal uses the left-handed coordinate system: +X forward, +Z up, and +Y right.



Enable the **OpenXRMsftHandInteraction** plugin to replicate the OpenXR grip and aim poses of tracked hands on runtimes that support this extension plugin.
![Openxr hand interaction plugin](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3c40543c-3179-4fd9-b9cc-377bd634ad9a/openxr_hand_iteraction_plugin.png)

* [xr](https://dev.epicgames.com/community/search?query=xr)
* [input](https://dev.epicgames.com/community/search?query=input)
* [openxr](https://dev.epicgames.com/community/search?query=openxr)
* [ar/vr/xr](https://dev.epicgames.com/community/search?query=ar%2Fvr%2Fxr)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Poses](/documentation/en-us/unreal-engine/openxr-input-in-unreal-engine?application_version=5.7#poses)
