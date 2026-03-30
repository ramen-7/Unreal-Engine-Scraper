<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-paint-mode-in-unreal-engine?application_version=5.7 -->

# Landscape Paint Mode

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
6. [Landscape Outdoor Terrain](/documentation/en-us/unreal-engine/landscape-outdoor-terrain-in-unreal-engine "Landscape Outdoor Terrain")
7. [Editing Landscapes](/documentation/en-us/unreal-engine/editing-landscapes-in-unreal-engine "Editing Landscapes")
8. Landscape Paint Mode

# Landscape Paint Mode

Guide to the Landscape Paint mode tools and how to use them.

![Landscape Paint Mode](https://dev.epicgames.com/community/api/documentation/image/124cbf0a-21f4-4c02-81cf-43f137afb502?resizing_type=fill&width=1920&height=335)

 On this page

The Landscape Paint mode tools adjust layer weights to selectively apply materials and modify the appearance of your landscape.

[![Grassy Field Example by Quixel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7b54f282-33d6-4647-ba3d-2b422df4af31/grassy-field-example.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7b54f282-33d6-4647-ba3d-2b422df4af31/grassy-field-example.png)

Grassy field created by artists at Quixel.

For more information about Landscape Materials, see [Landscape Material Layer Blending](/documentation/en-us/unreal-engine/landscape-materials-in-unreal-engine).

## Layers

Layers are a part of the assigned Landscape Material that define which material you are painting on your Landscape.

Landscape layers determine how the material is applied. A landscape can use multiple layers with different textures, scaling, rotation, and panning blended together to create the final textured terrain.

Each layer that is defined in the Landscape Material automatically populates the list of **Target Layers** found in the Landscape Mode panel and displays with its name and thumbnail image.

[![Select your active layer from the Target Layers list in the Landscape Mode panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ea7a3805-9139-4ece-bda9-14fb16fe3ed4/07-landscape-target.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ea7a3805-9139-4ece-bda9-14fb16fe3ed4/07-landscape-target.png)

Select your active layer from the Target Layers list in the Landscape Mode panel.

The highlighted layer is applied to the landscape according to the tool’s options and [brush](/documentation/en-us/unreal-engine/landscape-brushes-in-unreal-engine) settings.

[![Moutain  Landscape with multiple paint layers](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ca86f63b-4947-4eaa-9e97-c235832fafb8/08-landscape-layers.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ca86f63b-4947-4eaa-9e97-c235832fafb8/08-landscape-layers.png)

A mountain landscape painted with multiple layers.

The Paint tools manipulate the weightmap of the landscape similar to how the Sculpting tools manipulate heightmaps.

Layers are created in the Landscape Material. For more information about layers and Landscape Materials, see [Landscape Material Layer Blending](/documentation/en-us/unreal-engine/landscape-materials-in-unreal-engine).

### Layer Info Objects

A Layer Info Object is an asset that contains the weightmap and other information about a particular Landscape layer. Every Landscape layer must have a layer info object assigned to it You can create layer info objects in the Landscape Mode panel.

There are two kinds of layer info object, Weight-Blended and Non Weight-Blended:

* **Weight-Blended** - Painting a weight-blended layer will decrease the weight of all other weight-blended layers. For example, painting mud will remove grass, and painting grass will remove mud. This is the most commonly used type of layer info object.
* **Non Weight-Blended** - Layers that are independent of each other. Painting a non weight-blended layer does not affect the weights of the other layers. These are used for more advanced effects, such as blending snow onto other layers: instead of having grass, mud, rock *or* snow, you would use a non weight-blended snow layer to blend between "grass, mud, or rock" and "snowy grass, snowy mud, or snowy rock."

You can either create a layer info object from the layer itself, or reuse an existing layer info object from another Landscape.

**To create a layer info object:**

1. Click the **Plus** icon to the right of the Layer name.
2. Select **Weight-Blended Layer (normal)** or **Non Weight-Blended Layer**.

   ![Weight Blended Non Weight Blended](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ab4eb362-e4fa-43ac-abeb-4f451ef2d75e/09-weight-blended-non-weight-blended.png "Weight Blended Non Weight Blended")
3. Choose the save location for the new layer info object.

Layer info objects exist as assets in the **Content Browser** after creation and can be reused with other landscapes. Each layer of your landscape must use a different layer info object.

![Layer Info Object](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8bdd6d7e-af82-4dcf-bd8e-39ab2b435ba5/10-layer-info-object.png "Layer Info Object")

**To reuse an existing layer info object from another Landscape:**

1. Find and select the layer info object in the **Content Browser**.
2. In the **Target Layers** section, click the Assign icon (![Assign](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/92cc2f6a-752a-42ff-b815-a88dcc61ad77/11-assign.png "Assign")) to the right of the layer you want to use the layer info object.

Layer info objects can only be used if their layer name matches the layer they were originally created for.

The primary purpose of layer info objects is to store the weightmap data for a painted layer They also contain the following properties:

| Option | Description |
| --- | --- |
| **Layer Name** | Displays the name of the layer. |
| **Phys Material** | The [Physical Material](/documentation/en-us/unreal-engine/physical-materials-in-unreal-engine) (if any) assigned to areas of Landscape where this layer is dominant. |
| **Hardness** | The value used by the [Erosion](/documentation/en-us/unreal-engine/landscape-erosion-tool-in-unreal-engine) tool. |
| **Minimum Collision Relevance Weight** | Determines the minimum required weight needed to be considered the dominant layer. |
| **No Weight Blend** | Toggles weight blending. |
| **Layer Usage Debug Color** | Determines the color used when debugging layers. |
| **Spline Falloff Modulation** | Settings for controlling Spline Falloff Modulation. |

#### Orphaned Layers

If a layer is removed from the landscape material after it has been populated in the **Target Layers** list and it has painted data on the Landscape, it will be displayed in the list with a **?** icon. This denotes an orphaned layer.

[![Interface showing a missing Grass layer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f62ce3a8-4b57-41e6-a9f6-98f8546c4b2a/12-missing-layer.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f62ce3a8-4b57-41e6-a9f6-98f8546c4b2a/12-missing-layer.png)

Interface showing a missing Grass layer.

Areas previously painted with this layer likely appear black, though the exact behavior depends on your landscape material.

#### Deleting Orphaned Layers

You can delete orphaned layers from the Landscape. It is recommended that you first paint over any areas where the layer was used. Painted layer data is preserved until the layer is deleted, so no information is lost if you make a mistake in the landscape material.

To remove a layer from your Landscape, click the **X** icon to the right of the layer's name.

[![Click the X to delete the orphaned layer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/86442ee4-36dc-4f52-8577-6ffbd7299d87/13-delete-layer.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/86442ee4-36dc-4f52-8577-6ffbd7299d87/13-delete-layer.png)

Click the X to delete the orphaned layer.

### Weight Editing

At each vertex in your landscape, each layer has a weight specifying how much influence that layer has on the Landscape. Layers have no particular blending order. Instead, each layer's weight is stored separately and the results added. In the case of weight-blended layers, the weight values add up to 255.

Non weight-blended layers are independent of other layers and can have any weight value.

The Paint tool increases or decreases the weight of the selected layer. For weight-blended layers, as you increase the weight of one layer, the weight of the other layers uniformly decreases. Fully painting one layer will result in no weight value on any other layer.

You can reduce the value of a weight-blended layer by holding **Ctrl + Shift** while painting. This causes the weight value of other layers to uniformly increase. Because of this, it is not possible to paint layers completely away. Instead, it is recommended to choose the layer you want to paint in its place and paint that additively.

## Using the Painting Tools

Painting tools modify the appearance of your landscape by selectively applying layers of specially designed [Landscape Materials](/documentation/en-us/unreal-engine/landscape-materials-in-unreal-engine) to portions of the landscape components.

The tools use the following controls:

| **Controls** | **Description** |
| --- | --- |
| **LMB** | Performs a stroke that applies the selected tool's effects to the selected layer. |
| **Ctrl+Shift+LMB** | Performs a stroke that applies the opposite of the selected tool's effects to the selected layer. |
| **Ctrl+Z** | Undo last stroke. |
| **Ctrl+Y** | Redo last undone stroke. |

Though each tool has specific options, they all share the following:

| **Common Option** | **Description** |
| --- | --- |
| **Tool Strength** | Determines how much effect each brush stroke has. |

### Paint

[![Paint Tool Interface button](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/741bbbfe-c550-4b92-9458-7c62a6f1ec5c/01-paint-tool.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/741bbbfe-c550-4b92-9458-7c62a6f1ec5c/01-paint-tool.png)

The Paint tool increases or decreases the weight of the material layer being applied to the Landscape using the currently selected brush and falloff.

| **Option** | **Description** |
| --- | --- |
| **Use Target Value** | Blends the values of the noise being applied toward a target value. |

### Smooth

[![Smooth Tool Interface button](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/43c65b41-b613-41dc-8fa9-19a61d068f00/02-smooth-tool.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/43c65b41-b613-41dc-8fa9-19a61d068f00/02-smooth-tool.png)

The Smooth tool averages the layer weights across the area on which the tool is used. The strength determines the amount of smoothing.

**Layer Smoothing**

![Landscape Smooth Layer Before](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a80c8eaf-6242-473c-bfcd-b45b33c1fcd3/03-layer-smoothing-before.png "Landscape Smooth Layer Before")

![Landscape Smooth Layer After](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/794e7b6e-0fa4-4a17-a040-8c0f71116ecf/04-layer-smoothing-after.png "Landscape Smooth Layer After")

Landscape Smooth Layer Before

Landscape Smooth Layer After

| **Option** | **Description** |
| --- | --- |
| **Filter Kernal Scale** | Sets the scale multiplier for the smoothing filter kernel. |
| **Detail Smooth** | Performs a detail preserving smooth using the specified detail smoothing value. Larger detail smoothing values remove more details, while smaller values preserve more details. |

### Flatten

[![Flatten Tool Interface button](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/686b7dc0-2068-4efb-863c-420e82693f43/05-flatten-tool.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/686b7dc0-2068-4efb-863c-420e82693f43/05-flatten-tool.png)

The Flatten tool directly sets the selected layer's weight to the value of the **Tool Strength** slider.

| **Option** | **Description** |
| --- | --- |
| **Flatten Mode** | Determines whether the tool will increase or decrease the application of the selected layer's weight, or do both. |

### Noise

[![Noise Tool Interface button](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0b349b1e-9fcd-4bc4-a329-0deef431dbc2/06-noise-tool.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0b349b1e-9fcd-4bc4-a329-0deef431dbc2/06-noise-tool.png)

This tool applies a noise filter to the layer weight. The strength determines the amount of noise.

| **Option** | **Description** |
| --- | --- |
| **Use Target Value** | Blends the values of the noise being applied toward a target value. |
| **Noise Mode** | Determines whether to apply all noise effects, only the noise effects that result in increasing the application of the layer, or only the noise effects that result in reducing the application of the layer. |
| **Noise Scale** | Determines the size of the perlin noise filter used. The noise filter is related to position and scale. If the Noise Scale does not change, the same filter is applied to the same position many times. |

### Blueprint

[![Blueprint Brush Tool Interface button](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/45bf8149-1d10-429c-b24b-f6f2e8752b5b/blueprint-tool.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/45bf8149-1d10-429c-b24b-f6f2e8752b5b/blueprint-tool.png)

Landscape Blueprint Brush tool provides user-defined sculpting brushes that are used as part of a non-destructive landscape workflow. Requires the Landmass plugin to use. This tool is found under the Sculpt mode tools once the plugin is enabled.

For more information on Landscape Blueprint Brushes, see [Landscape Blueprint Brushes](/documentation/en-us/unreal-engine/landscape-blueprint-brushes-in-unreal-engine).

* [landscape](https://dev.epicgames.com/community/search?query=landscape)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Layers](/documentation/en-us/unreal-engine/landscape-paint-mode-in-unreal-engine?application_version=5.7#layers)
* [Layer Info Objects](/documentation/en-us/unreal-engine/landscape-paint-mode-in-unreal-engine?application_version=5.7#layerinfoobjects)
* [Orphaned Layers](/documentation/en-us/unreal-engine/landscape-paint-mode-in-unreal-engine?application_version=5.7#orphanedlayers)
* [Deleting Orphaned Layers](/documentation/en-us/unreal-engine/landscape-paint-mode-in-unreal-engine?application_version=5.7#deletingorphanedlayers)
* [Weight Editing](/documentation/en-us/unreal-engine/landscape-paint-mode-in-unreal-engine?application_version=5.7#weightediting)
* [Using the Painting Tools](/documentation/en-us/unreal-engine/landscape-paint-mode-in-unreal-engine?application_version=5.7#usingthepaintingtools)
* [Paint](/documentation/en-us/unreal-engine/landscape-paint-mode-in-unreal-engine?application_version=5.7#paint)
* [Smooth](/documentation/en-us/unreal-engine/landscape-paint-mode-in-unreal-engine?application_version=5.7#smooth)
* [Flatten](/documentation/en-us/unreal-engine/landscape-paint-mode-in-unreal-engine?application_version=5.7#flatten)
* [Noise](/documentation/en-us/unreal-engine/landscape-paint-mode-in-unreal-engine?application_version=5.7#noise)
* [Blueprint](/documentation/en-us/unreal-engine/landscape-paint-mode-in-unreal-engine?application_version=5.7#blueprint)
