<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprint-modify-curve-in-unreal-engine?application_version=5.7 -->

# Modify Curve

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
7. [Animation Blueprints](/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine "Animation Blueprints")
8. [Animation Node Reference](/documentation/en-us/unreal-engine/animation-blueprint-nodes-in-unreal-engine "Animation Node Reference")
9. [Skeletal Controls](/documentation/en-us/unreal-engine/animation-blueprint-skeletal-controls-in-unreal-engine "Skeletal Controls")
10. Modify Curve

# Modify Curve

Describes the Modify Curve node which can be used to modify animation curves with arbitrary logic inside Animation Graphs.

![Modify Curve](https://dev.epicgames.com/community/api/documentation/image/f52ae76d-37c2-4d18-b1c1-e3df95d7293c?resizing_type=fill&width=1920&height=335)

 On this page

With the **Modify Curve** [Animation Blueprint](/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine) node, you can blend, scale and remap [Animation Curves](/documentation/en-us/unreal-engine/animation-curves-in-unreal-engine) at runtime.

![modify animation curve animation blueprint node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d998d665-444e-44d2-bd79-c293989ea97f/modifycurve.png)

By **right-clicking** the Modify Curve node in the **AnimGraph**, you can select one of the character's [Animation Curves](/documentation/en-us/unreal-engine/animation-curves-in-unreal-engine) from the **Add Curve Pin** option in the context menu to add a pin that corresponds to the selected [Animation Curve](/documentation/en-us/unreal-engine/animation-curves-in-unreal-engine).

![right click the modify curve node to create a new curve input pin add curve pin](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f318bbcd-e1b2-49fe-87d1-4a63c14d455c/addcurve.png)

Here, a **Hue Shift** curve has been added to the Modify Curve node to alter the hue of the characters material.

| Description | Graph | Restults |
| --- | --- | --- |
| Here the **Hue Shift** curve has been set to a static value of **1.0** on the Modify Curve Node in the **AnimGraph**. This returns a static value from the curve, resulting in the character displaying a single color material. | modify cuuve animaiton blueprint node disabled | modify curve animation blueprint node bot demo disabled |
| Here a **sine wave** is set to drive the **Hue Shift** curve value on the Modify Curve node in the **AnimGraph**. This returns a dynamic value, resulting in the character displaying a rotating color material. | modify cuuve animaiton blueprint node disabled | modify curve animation blueprint node bot demo enabled |

## Property Reference

![modify curve animation blueprint node details panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0a32f499-0e16-45bc-ab4c-02a5dcdecd7a/details.png)

Here you can reference a list of the Modify Curve node's properties.

| Property | Description |
| --- | --- |
| **Curve Map** | Here you can set any curve maps. Curve maps are associative, unordered containers that associate a set of keys with a set of values. Each key in a map must be unique, but values can be duplicated. |
| **Curve Values** | Curve values are the values used to drive curve modifications. You can add a new curve by right-clicking the Modify Curve node in the **AnimGraph** and selecting one of the character's Animation Cures from the Add Curve Pin option in the context menu. These added curve pins can then drive their respective curves with a value. |
| **Alpha** | Set the alpha value to control the blend of the modified curve pose and the source animation pose. By default this property appears as a pin on the node in the **AnimGraph**. |
| **Apply Mode** | Set the method to apply the modification to the [Animation Curve](/documentation/en-us/unreal-engine/animation-curves-in-unreal-engine). The application modification options include:  **Add**: Add new value to input curve value. **Scale**: Scale input value by new value. **Blend**: Blend input with new curve value, using alpha setting on the node. **Weighted Moving Average**: Bend the new curve value with the last curve value using Alpha to determine eht weighting. For example, .5 is a moving average, higher values react to new values faster lower slower. **Remap Curve**: Rempas the new curve values between the Curve Values entry and 1.0. For example, .5 in Curve Values makes 0.51 map to 0.02. |

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [animation blending](https://dev.epicgames.com/community/search?query=animation%20blending)
* [curves](https://dev.epicgames.com/community/search?query=curves)
* [animation curves](https://dev.epicgames.com/community/search?query=animation%20curves)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Property Reference](/documentation/en-us/unreal-engine/animation-blueprint-modify-curve-in-unreal-engine?application_version=5.7#propertyreference)
