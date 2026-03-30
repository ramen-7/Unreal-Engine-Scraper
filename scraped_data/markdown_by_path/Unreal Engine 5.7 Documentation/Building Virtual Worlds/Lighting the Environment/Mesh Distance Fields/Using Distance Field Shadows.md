<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-distance-field-shadows-in-unreal-engine?application_version=5.7 -->

# Using Distance Field Shadows

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
5. [Building Virtual Worlds](/documentation/en-us/unreal-engine/building-virtual-worlds-in-unreal-engine "Building Virtual Worlds")
6. [Lighting the Environment](/documentation/en-us/unreal-engine/lighting-the-environment-in-unreal-engine "Lighting the Environment")
7. [Mesh Distance Fields](/documentation/en-us/unreal-engine/mesh-distance-fields-in-unreal-engine "Mesh Distance Fields")
8. Using Distance Field Shadows

# Using Distance Field Shadows

How to setup and use Distance Field Shadowing.

![Using Distance Field Shadows](https://dev.epicgames.com/community/api/documentation/image/bdc9eb26-3a7b-4814-b6bf-c3ecd02acf0d?resizing_type=fill&width=1920&height=335)

 On this page

When you're developing your games, you will find that there are situations where dynamic lighting is the best choice for your levels, like those with long view distances or ones where you have a large open world. In instances like this, precomputed lighting can be inefficient or too demanding on the target system's resources. **Distance Field Shadows**, also referred to as **Distance Field Shadows**, enables you to shadow at farther distances than traditional **Cascaded Shadow Maps** (CSM) with a [Directional Light](/documentation/en-us/unreal-engine/directional-lights-in-unreal-engine).

In this guide, you'll learn how to enable Distance Field Shadowing for different [Light Types](/documentation/en-us/unreal-engine/light-types-and-their-mobility-in-unreal-engine), including Directional, Point, and Spot Lights.

## Steps

This feature requires that **Generate Mesh Distance Fields** be enabled in your **Project Settings** in the **Rendering** section. See how to [enable Mesh Distance Fields](/documentation/en-us/unreal-engine/mesh-distance-fields-in-unreal-engine) here, if you have not done so already.

1. Start by navigating to the **Place Actors** panel, then in the **Lights** tab, select and drag a **Directional**, **Spot**, or **Point** Light into the main viewport.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/01575b73-7d98-4e94-b47a-0c6eb7442492/addlighttype.png)


   To enable Distance Field Shadows on any Light component, the process is the same. The additional sections of this guide will cover specific properties for these light types.
2. With the Light selected, navigate over to its **Details** panel and set its Mobility to **Movable** or **Stationary**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/936f7329-ac9b-4368-ba2c-44a2beaef6ed/transformmobility.png)
3. In the **Details** panel under **Distance Field Shadows**, set **Distance Field Shadows** to enabled.

   |  |  |
   | --- | --- |
   |  |  |
   | Directional Light | Spot/Point Light |

   If this option is grayed out, make sure that you've first enabled the option for **Generate Mesh Distance Fields** in the Project Settings, and then check to make sure that the light's Mobility is set to **Movable** or **Stationary**.

## End Result

Once your Light's have been set to Movable or Stationary and toggled **Distance Field Shadowing** on, your light will automatically use them for your level. For Directional Lights, Distance Field Shadowing will be enabled for any distance beyond the Cascaded Shadow Maps **Dynamic Shadow Distance** value.

![Cascaded Shadow Maps Only](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/74cd355e-3077-4e8c-afa4-d4e993c168a4/csmonly.png)

![Cascaded Shadow Maps | and | Distance Field Shadows](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/852fd6e7-579c-4e33-9591-07e60e6bf7c1/csmanddf.png)

Cascaded Shadow Maps Only

Cascaded Shadow Maps | and | Distance Field Shadows

In this test level for Fortnite, Cascaded Shadow Map (CSM) **Dynamic Shadow Distance** is 4,500 cm (centimeters) from the camera and when Distance Field Shadowing is enabled, they handle any shadowing beyond the CSM Shadow Distance. When CSM is the only shadowing method being used, distant objects (like the Court House columns) will have light leaking because it is not within the shadow distance. Farther distance objects will also not be shadowed properly.

When using a Directional Light, it can be helpful to set the Cascaded Shadow Map **Dynamic Shadow Distance Moveable Light** slider to **0** making it possible to only see the shadows produced from Mesh Distance Fields. This is a useful way of testing your scene and diagnosing any potential Distance Field Quality issues in addition to using the visualization view modes.

## Additional Light Settings

Use the [Distance Field Reference](/documentation/en-us/unreal-engine/mesh-distance-fields-properties-in-unreal-engine) to learn about settings specific to [Distance Field Shadowing](/documentation/en-us/unreal-engine/distance-field-soft-shadows-in-unreal-engine) for [Directional Lights](/documentation/en-us/unreal-engine/mesh-distance-fields-properties-in-unreal-engine#directionallight) and [Point/Spot Lights](/documentation/en-us/unreal-engine/mesh-distance-fields-properties-in-unreal-engine#point/spotlight). These settings enable you to have artistic control over your scene where you'll be able to control the softness of shadows and the farthest distance any shadow can cast. There are also some global adjustments specific to Directional Lights that can be used to remove self-shadowing artifacts in the scene caused from LOD (Level of Detail) meshes at farther distances from the camera.

* [static mesh](https://dev.epicgames.com/community/search?query=static%20mesh)
* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [lighting](https://dev.epicgames.com/community/search?query=lighting)
* [shadows](https://dev.epicgames.com/community/search?query=shadows)
* [distance fields](https://dev.epicgames.com/community/search?query=distance%20fields)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/using-distance-field-shadows-in-unreal-engine?application_version=5.7#steps)
* [End Result](/documentation/en-us/unreal-engine/using-distance-field-shadows-in-unreal-engine?application_version=5.7#endresult)
* [Additional Light Settings](/documentation/en-us/unreal-engine/using-distance-field-shadows-in-unreal-engine?application_version=5.7#additionallightsettings)
