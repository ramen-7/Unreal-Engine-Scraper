<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/control-rig-spline-rigging-in-unreal-engine?application_version=5.7 -->

# Spline Rigging

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
6. [Control Rig](/documentation/en-us/unreal-engine/control-rig-in-unreal-engine "Control Rig")
7. [Rigging with Control Rig](/documentation/en-us/unreal-engine/rigging-with-control-rig-in-unreal-engine "Rigging with Control Rig")
8. Spline Rigging

# Spline Rigging

Utilize Splines in your Control Rig to achieve easier procedural animation on long joint chains.

![Spline Rigging](https://dev.epicgames.com/community/api/documentation/image/ff874973-cbc3-4b9e-ae8c-45ec42f5a649?resizing_type=fill&width=1920&height=335)

 On this page

Splines can be built and used in Control Rig in order to create dynamic and procedural motion regardless of skeletal hierarchy. With splines, you can create more complex poses with fewer necessary controls on limbs such as tentacles, spines, and snakes.

This document provides an overview of how to create and use splines in your rig.

#### Prerequisites

* You have created a Control Rig Asset for a Skeletal Mesh that has a suitable joint structure for splines, such as a tail. See the **[Control Rig Quick Start](/documentation/en-us/unreal-engine/how-to-create-control-rigs-in-unreal-engine)** page for information on how to do this.
* You are familiar with how to create and position **[Controls](/documentation/en-us/unreal-engine/controls-bones-and-nulls-in-control-rig-in-unreal-engine#controls)**.

## Create Spline

Spline creation in Control Rig is done by specifying arbitrary translation points, which are used to construct the spline. In typical setups, these points are based on the transform information from **Controls**.

To start, create a **Spline From Points** node by right-clicking in the rig graph and selecting **Spline From Points**.

![spline from points](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3a2cac61-7476-421f-8c0d-061926427190/create1.png)

Next, create rig elements which are used to define the points in the spline. In this example, four controls are created and evenly distributed along the length of the tentacle. The number of controls does not need to correspond to the number of bones in the chain.

![create spline controls](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/53721692-44fe-42a9-a524-56657b8e1eef/create2.png)

Next, reference your root rig element into the rig graph, and click the **Add (+)** button on the **Spline From Points** node to add the first spline point in the array. Expand the **Transform** pin on your element reference and connect the **Translation** pin to the input on the **Points** pin.

![control rig spline points](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/83302257-de6e-4ecf-a217-be85fce7b4fc/create3.png)

Continue to add additional spline points for all the rig elements you want to use to form the spline. You must ensure that the order in which you connect them to the **Spline From Points** node corresponds to the direction of the spline.

![control rig spline points](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a79d23c8-749d-4c17-ae7c-6f3318945d0a/create4.png)


Splines in Control Rig require a minimum of four points in order to create the spline successfully.

You can now preview your spline by using the **Draw Spline** node, which provides a visual display for the spline. Create this node by right-clicking in the graph and selecting **Draw Spline**, then connect the **Spline** pin from **Spline From Points**, and the **Execute** event from **Forwards Solve**. Manipulating your controls in the viewport will preview the spline behavior.

![control rig spline preview](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7b8b6f20-664b-4a28-bece-74981824829b/create5.gif)

### Apply Spline to Bones

Once the spline has been created, you can apply it to your joint chain.

First, create a **Fit Chain on Spline Curve** node by right-clicking in the graph and selecting **Fit Chain on Spline Curve**.

![fit chain on spline curve](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a35bf3a9-bc06-4f19-907c-a201fdd89ef3/apply1.png)

Next, multi-select the bones you want to include in the spline from the **Rig Hierarchy** panel, drag them into the Rig Graph, and select **Create Item Array**. For this operation, selection order is important to ensure the resulting bone array matches the same order as the spline points.

![spline bone array](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a146fd9f-c56e-43d5-8671-21b02746aa75/apply2.gif)

Lastly, connect the **Rig Element** array to the **Items** pin, the **Spline** pin from **Spline From Points**, and ensure the **Execute** event is connected to your Control Rig logic chain.

![control rig spline bones](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bcef45d0-c3e5-483d-a51f-786552f850d7/apply3.png)

Your spline should now affect the bone chain.

![control rig spline](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/49d00d45-6f36-4ab4-aa98-36b2affd8a03/apply4.gif)

## Spline Properties

The following properties are available on the **Spline From Points** node.

![spline from points](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/994a850e-e8fd-4a57-be15-691fc3236832/node_splinefrompoints.png)

| Name | Description |
| --- | --- |
| **Points** | The position information that will be used to construct the spline. Can be either an array or built using individual translation pins by clicking the **Add (+)** button. |
| **Spline Mode** | The type of spline to use. You can choose from either:   * **Hermite**, which will ensure the Spline passes through all defined **Points**. hermite spline type * **BSpline**, which is a smoother spline and will only pass through the start and end points. This is based on the **[TinySpline](https://msteinbeck.github.io/tinyspline/)** library. bspline type |
| **Samples Per Segment** | This property controls the approximation accuracy of the spline. Higher numbers will cause the spline to be more accurate and smooth. Lower numbers will cause the spline to appear more jagged and incorrect. Performance costs increase with the sample count, so it is a good idea to ensure this number is not set too high. |
| **Compression** | The amount the spline should compress when reducing its length. |
| **Stretch** | The amount the spline should stretch when increasing its length. |
| **Spline (Output)** | The resulting spline from this node. |

The following properties are available on the **Fit Chain on Spline Curve** node.

![fit chain on spline curve](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a1963de4-2172-4a66-b30d-2c0b4251e4ff/node_fitchain.png)

| Name | Description |
| --- | --- |
| **Items** | An array of rig elements to align to the provided **Spline**. |
| **Spline** | The **Spline** curve to align to. |
| **Alignment** | Whether or not to stretch the aligned elements to the full spline length.   * **Stretched** will cause the full amount of stretching to occur. spline stretched alignment * **Front** will disable stretching. spline front alignment |
| **Minimum** | The Minimum **U** value to use on the curve. **U** is the normalized (0 - 1) percentage between all combined control points. |
| **Maximum** | The Maximum **U** value to use on the curve. **U** is the normalized (0 - 1) percentage between all combined control points. |
| **Sampling Precision** | This property controls the approximation accuracy of the spline. Higher numbers will cause the spline to be more accurate and smooth. Lower numbers will cause the spline to appear more jagged and incorrect. This overwrites the **Samples Per Segment** property from **Spline From Points**. Performance costs increase with the sample count, so it is a good idea to ensure this number is not set too high. |
| **Primary Axis** | The major axis being aligned in the chain. In simple setups this property can be ignored, but typically you will want to set this to be the direction your item chain is progressing in. spline primary axis |
| **Secondary Axis** | The minor or "up" axis being aligned in the chain. In simple setups this property can be ignored, but typically you will want to set this to be in the direction of a pole vector if it is being used. spline secondary axis |
| **Pole Vector Position** | The position of an optional pole vector control. This only has an effect if the **Secondary Axis** is set. |
| **Rotations** | An array of rotations to apply additively to the overall spline. |
| **Rotation Ease Type** | The easing type to use between each rotation element. |
| **Weight** | The factor to apply the elements to the curve. |
| **Propagate to Children** | Whether or not the changes in the rig elements should apply recursively to all children. |

## Spline Nodes

The following Spline nodes are available for use in your Control Rig Graph:

| Name | Image | Description |
| --- | --- | --- |
| **Closest Parameter From Spline** | closest parameter from spline | Retrieves the closest **U** value from a given spline and position. |
| **Draw Spline** | draw spline | Displays the spline curve in the viewport for preview purposes. Includes properties for controlling the **Color**, **Thickness**, and sample **Detail**. |
| **Fit Chain on Spline Curve** | fit chain on spline curve | Fits a given spline along an array of items. This node typically is used when performing backwards solves that include splines. |
| **Fit Spline Curve on Chain** | fit spline curve on chain | Applies a chain of rig elements to a spline. |
| **Get Length Of Spline** | get length of spline | Gets the length of a spline. |
| **Parameter At Length Percentage** | parameter at length percentage | Returns the **U** value of a spline given a length percentage. |
| **Position From Spline** | position from spline | Returns the position along a spline given the **U** value. |
| **Set Spline Points** | set spline points | Sets the currently existing points of a spline to new values, then outputs the resulting new spline. |
| **Spline From Points** | spline from points | Builds a spline from an array of translation points. |
| **Tangent From Spline** | tangent from spline | Returns the tangent angle of a point along the spline defined by **U**. |
| **Transform From Spline** | transform from spline | Returns a transform from a given **Spline** and **U** value based on the given **Up** and **Roll**. |

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [control rig](https://dev.epicgames.com/community/search?query=control%20rig)
* [spline](https://dev.epicgames.com/community/search?query=spline)
* [rigging](https://dev.epicgames.com/community/search?query=rigging)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisites](/documentation/en-us/unreal-engine/control-rig-spline-rigging-in-unreal-engine?application_version=5.7#prerequisites)
* [Create Spline](/documentation/en-us/unreal-engine/control-rig-spline-rigging-in-unreal-engine?application_version=5.7#createspline)
* [Apply Spline to Bones](/documentation/en-us/unreal-engine/control-rig-spline-rigging-in-unreal-engine?application_version=5.7#applysplinetobones)
* [Spline Properties](/documentation/en-us/unreal-engine/control-rig-spline-rigging-in-unreal-engine?application_version=5.7#splineproperties)
* [Spline Nodes](/documentation/en-us/unreal-engine/control-rig-spline-rigging-in-unreal-engine?application_version=5.7#splinenodes)
