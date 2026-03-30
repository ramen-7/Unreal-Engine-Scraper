<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/visualizing-play-area-bounds-in-unreal-engine?application_version=5.7 -->

# Visualizing Play Area Bounds

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
7. [Creating UI for XR Experiences](/documentation/en-us/unreal-engine/design-user-interfaces-for-xr-experiences-in-unreal-engine "Creating UI for XR Experiences")
8. Visualizing Play Area Bounds

# Visualizing Play Area Bounds

Visualize the user's stage in their head-mounted experience with OpenXR

![Visualizing Play Area Bounds](https://dev.epicgames.com/community/api/documentation/image/f9bcb282-ceb9-48b1-9f3c-68cec273501e?resizing_type=fill&width=1920&height=335)

 On this page

Users can specify the bounds of their play area, sometimes called the *stage*, on their device. You can access these bounds in Unreal Engine with the [OpenXR APIs](/documentation/en-us/unreal-engine/developing-for-head-mounted-experiences-with-openxr-in-unreal-engine).

![image alt text](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/88ae5d1c-9121-4845-9c9b-491b9d4a7155/play-area-boundary-oculus-guardian.gif)

On Oculus devices, the Guardian boundary appears when the user gets close.

This page shows how you can visualize the play area bounds in your project. For setting up play area bounds on your device, refer to your device's documentation.

## Get Play Area Bounds

The `Get Play Area Bounds` function returns the length of the largest rectangle that can be found inside your play area. Play area bounds are visualized by your OpenXR compatible runtime when the user gets close to the boundary. It can also be useful to inform the user when they are moving close to the boundary with custom visualizations in your application.

![image alt text](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9cf23f63-bf80-4b66-a366-202517484d3b/get-play-area-bounds-blueprint-node.png)

The `Get Play Area Bounds` function has three reference spaces it can return: **Eye Level**, **Floor Level**, and **Stage**. These three spaces map to the OpenXR reference spaces **View**, **Local**, and **Stage**, respectively. In most cases, we recommend you return the **Stage** reference space. For more details on the OpenXR reference spaces, refer to the [OpenXR Specification](https://www.khronos.org/registry/OpenXR/specs/1.0/html/xrspec.html#reference-spaces).

If the `Get Play Area Bounds` function doesn't return any data, the OpenXR runtime you're using might not have implemented the OpenXR functionality for play area bounds.

## Teleportation Visualization

An example of visualizing play area bounds is teleportation visualization. The [VR Template](/documentation/en-us/unreal-engine/vr-template-in-unreal-engine) provides an implementation of this visualization during teleport.

![image alt text](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/da8bd429-b463-4718-9835-c3170b261e77/vr-template-teleport-visualization.gif)

The teleport visualization is defined in the Blueprint **VRTeleportVisualizer** located in **Content/VRTemplate/Blueprints**. The following is a description of the logic for visualizing the boundaries.

**On Begin Play:**

1. The Blueprint calls `Get Play Area Bounds` using the Stage reference space.
2. The Blueprint then assigns the X and Y data to a User Variable in the [Niagara System](/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine) **NS\_PlayAreaBounds**.
3. NS\_PlayAreaBounds dynamically draws a rectangle using the X and Y values returned from Get Play Area Bounds.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/64d45931-6f1b-4e24-9f7c-56d4045debd4/teleport-visualization-on-begin-play.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/64d45931-6f1b-4e24-9f7c-56d4045debd4/teleport-visualization-on-begin-play.png)

**On Tick:**

1. The Blueprint moves NS\_PlayAreaBounds relative to the teleport location, identified by **NS\_TeleportRing**.
2. This results in an accurate visualization of where the player will be, relative to the play area bounds, after teleportation.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9e3a209d-c800-4828-b034-cd9d86c5377c/teleport-visualization-on-tick.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9e3a209d-c800-4828-b034-cd9d86c5377c/teleport-visualization-on-tick.png)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Get Play Area Bounds](/documentation/en-us/unreal-engine/visualizing-play-area-bounds-in-unreal-engine?application_version=5.7#getplayareabounds)
* [Teleportation Visualization](/documentation/en-us/unreal-engine/visualizing-play-area-bounds-in-unreal-engine?application_version=5.7#teleportationvisualization)
