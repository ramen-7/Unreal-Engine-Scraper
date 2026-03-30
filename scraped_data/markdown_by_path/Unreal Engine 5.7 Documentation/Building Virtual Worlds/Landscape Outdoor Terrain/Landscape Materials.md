<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-materials-in-unreal-engine?application_version=5.7 -->

# Landscape Materials

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
7. Landscape Materials

# Landscape Materials

A reference guide to Landscape Materials and how to use them with your terrain.

![Landscape Materials](https://dev.epicgames.com/community/api/documentation/image/ff1560ec-e811-4d78-95f1-7073d7c26bc9?resizing_type=fill&width=1920&height=335)

 On this page

Unreal Engine (UE) provides several landscape-specific [Material](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-materials) Blueprint nodes that can help improve the textures for your Landscape. You can use the nodes alongside any other material in UE.

You can create and modify **Landscape Materials** in the [Material Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-material-editor-user-guide) in the same way as other materials.

## Layer Weights and Ordering

Landscape materials operate as a blend between multiple layers, where painted blend weights control the influence of each layer.

Each layer is identified by a (case-insensitive) name that gets used in one of the landscape-specific material nodes (e.g. **Landscape Layer Sample**, **Landscape Layer Blend**, etc.). The nodes allow the material to access a specific weightmap of a specific target layer.

To be paintable, the layer needs to be created and associated with a **Landscape Layer Info** asset. For more information, see [Target Layers](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-and-using-custom-heightmaps-and-layers-in-unreal-engine). It is okay to create a target layer in the landscape and not use it in the landscape material. However, if a material looks for a layer name that has no target layer entry in the landscape, its weight will always be considered zero.

In the Blueprints editor, the material graph determines how the weights are interpreted to achieve the blended result. The blending method defines how the landscape uses those weights in the final result.

There are two possible blending modes: **W****eight Blending** and **Alpha Blending**. You can use these methods together to create different effects, such as snow on top of your grass and dirt layers.

| Blending Mode | Description |
| --- | --- |
| **Weight Blending** | Assigns a value between `0` and `1.0` to each layer of the material, which corresponds to a percentage value. Landscape Paint tools ensure that the weight value of all weight blended layers does not exceed `1.0`. The excess value is removed and the other layers scale down appropriately, so that a total of 100% remains.  When one layer is painted to 100%, the weight values for all other layers are 0%. This means that when you use the [Paint](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-paint-mode-in-unreal-engine) tool to remove the layer that is at 100%, there is nothing to replace it with, because all other layers are valued at 0%. This makes it appear as if the layer hasn’t changed. |
| **Alpha Blending** | Assigns each layer an alpha percentage value between 0 and 100%. If your material graph is set up for ordered blending, this method respects the order in which the layers are applied.  The alpha layer exists separately from the other weighted layers, so when the alpha layer weight increases, other existing layer weights decrease. |

The landscape material is responsible for interpreting weight values from the target layers in the landscape actor, then turning them into shading properties. However, the landscape system also comes with an edit-time layer weight blending system that can transform the weight values before they reach the material. For more information on weighted blending, see [Landscape Paint Mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-paint-mode-in-unreal-engine).

## Landscape-Specific Material Nodes

Inside the [Material Editor](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-material-editor-user-guide), there are several specific nodes that you can use with the Landscape system. You can find these nodes by right-clicking and searching the context sensitive menu, or by searching in the **Palette** menu.

[![Material Editor Context Menu](https://dev.epicgames.com/community/api/documentation/image/7dbda72d-a3ce-4d5b-a0a8-590457c93db4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7dbda72d-a3ce-4d5b-a0a8-590457c93db4?resizing_type=fit)

Click image for full size.

### Landscape Layer Blend Node

The **Landscape Layer Blend** node blends together multiple per-layer values, such as texture samples or materials. Layers with higher blend weights have more influence on the blended result.

To add a new layer, click the plus (**+**) icon.

[![Layer Blend Array Elements](https://dev.epicgames.com/community/api/documentation/image/7c900f29-ca7f-4df3-b1fd-4150fdac90b8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7c900f29-ca7f-4df3-b1fd-4150fdac90b8?resizing_type=fit)

Click image for full size.

After you’ve added layers to the node, the Layer Names appear in the LandscapeLayerBlend node. The node has the following inputs:

[![Landscape Layer Blend Mode](https://dev.epicgames.com/community/api/documentation/image/b632b57f-f61b-4cda-a171-e47f8e98a995?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b632b57f-f61b-4cda-a171-e47f8e98a995?resizing_type=fit)

Click image for full size.

| Number | Property | Description |
| --- | --- | --- |
| **1** | **Layers** | Lists layers contained in the array. Add new layers by clicking the plus icon (). |
| **2** | **Additional Layers** | Shows any additional collapsed layers. |
| **3** | **Layer Name** | Displays the unique name of the layer. The **Layer Name** corresponds to the layer name used in [Paint mode](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-paint-mode-in-unreal-engine) in the Landscape tool window. |
| **4** | **Blend Type** | Defines the blend mode used by this layer. It contains the following options: **LB Alpha Blend**, **LB Height Blend**, or **LB Weight Blend.** For more information, see [Landscape Layer Blend Types](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-materials-in-unreal-engine). |
| **5** | **Preview Weight** | Displays the weight value to use when previewing the blending in the Material Editor. |
| **6** | **Const Layer Input** | Defines an RGB value to use when you do not want to use a texture. This is used for debugging a layer. |
| **7** | **Const Height Input** | Defines a height value to use when you do not want to use a texture. |

The **Landscape Layer Blend** node has the following inputs and outputs:

[![Layer Blend Node](https://dev.epicgames.com/community/api/documentation/image/202f23be-ca5b-466c-964f-20bde280e751?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/202f23be-ca5b-466c-964f-20bde280e751?resizing_type=fit)

Click image for full size.

| Number | Item | Description |
| --- | --- | --- |
| **1** | **Layer *Layer Name*** | Displays the unique name of the layer. This input is only available after you have added and names layers in the **Details** panel. |
| **2** | **Height *Layer Name*** | Defines a height map to blend with the named layer. This input is only visible on layers where the **Blend Type** property is set to **LB Height Blend**. |
| **3** | **Output** | Outputs the blended result. |

All layer names must be unique. It is recommended to name your layers with a descriptive name that indicates the layer’s contents.

#### Landscape Layer Blend Types

The **Landscape Layer Blend** node has three types of blend modes. Each different **Layer Blend** mode is used to achieve a different result.

| Blend Mode | Function |
| --- | --- |
| **LB Weight Blend** | Implements a weighted blend between all LB Weight Blend layers. This type is not order dependent. |
| **LB Alpha Blend** | Implements an alpha-blended overlay on top of the LB Weight Blend and LB Height Blend layers. Each LB Alpha Blend layer is applied in the order they appear in the list. For example, painting snow over rock and grass occludes both, but erasing snow reveals the rock and grass beneath it. |
| **LB Height Blend** | This is the same as LB Weight Blend, but also adds detail to the transition between layers based on a height map. For example, you can have dirt appear in the gaps between rocks at the layer transition point, instead of just smoothly blending between rock and dirt.  [LB-blend-image](https://dev.epicgames.com/community/api/documentation/image/d0f4dad7-a488-4971-814e-ec4221de118a?resizing_type=fit)  The dirt appears in the gaps between rocks at the layer transition point, creating a smooth transition where the layers meet. |

#### Adding a Landscape Layer Node

The `LandscapeLayerBlend` node automatically blends multiple layers together using either alpha blending or alpha blending with a height-based offset. The height-based offset lets a layer blend with other layers based on a heightmap input.

1. In the **Material Editor**, add a `LandscapeLayerBlend` node.
2. In the **Details** panel, next to **Layers**, click the plus icon (**+**) to add a layer.

   [![Landscape-layer-blend-add-new-layer](https://dev.epicgames.com/community/api/documentation/image/0e0a2020-8e8e-41a2-81ad-ea2790cd1244?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0e0a2020-8e8e-41a2-81ad-ea2790cd1244?resizing_type=fit)
3. Expand the layer to view its properties.
4. Change the **Layer Name** to a descriptive name for the layer, for example, **Snow**.
5. Determine whether you want the layer to be alpha blended or height blended, and set the **Blend Type** accordingly.

   [![Landscape-layer-blend-change-name](https://dev.epicgames.com/community/api/documentation/image/7b8f5e9a-adef-49a8-91a0-5a60cbfb96e7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7b8f5e9a-adef-49a8-91a0-5a60cbfb96e7?resizing_type=fit)
6. **Add** as many additional layers as you want for your Landscape Material. Rename them, and set their Blend Types appropriately.
7. **Connect** the `LandscapeLayerBlend` node's output to the **Base Color** input of your material's base node.
8. Add **Texture Sample** nodes, and connect their main outputs to the **Layer** inputs of the `LandscapeLayerBlend` nodes. Alternatively, you can create a more complex material network and connect it to the **Landscape Layer Blend Layer** input. For any height-blended layers, connect the **Texture Sample**'s alpha output to the `LandscapeLayerBlend`'s **Height** input.

When you are done, your Landscape material network should look something like this:

[![Landscape-layer-blend-in-Blueprints](https://dev.epicgames.com/community/api/documentation/image/36bb8349-d0cd-4401-8d2c-853619cbb704?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/36bb8349-d0cd-4401-8d2c-853619cbb704?resizing_type=fit)

You can preview the effects of different weights on the material by changing the **Preview Weight** properties of the `LandscapeLayerBlend` nodes.

For more information on the Landscape Layer Blend node, see [Landscape Layer Blend Technical Information](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-materials-in-unreal-engine#landscape-layer-blend-technical-information).

### Landscape Layer Sample Node

The **Landscape Layer Sampl****e** node returns the weight value associated with a given target layer. Its result is a value between `0.0` (when the target layer is not used) and `1.0` (when the target layer is fully painted), that you can then use at will in its material computations.

[![Landscape-layer-sample-node-menu](https://dev.epicgames.com/community/api/documentation/image/d45c91d1-cfe9-4325-9e2f-c04f74908c97?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d45c91d1-cfe9-4325-9e2f-c04f74908c97?resizing_type=fit)

|  |  |
| --- | --- |
| **Parameter Name** | Defines the name of the target layer to sample from. |
| **Preview Weight** | Defines the weight to use for preview purposes in the Material Editor. |

### Landscape Layer Coords Node

The **Landscape Layer Coords** node generates UV coordinates used for mapping the Landscape material onto Landscapes.

[![Landscape Layer Coords Node](https://dev.epicgames.com/community/api/documentation/image/a237623c-ffdf-4378-ba52-66d9474893fa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a237623c-ffdf-4378-ba52-66d9474893fa?resizing_type=fit)

Click image for full size.

This node has the following options:

| Number | Property | Description |
| --- | --- | --- |
| 1 | **Mapping Type** | Specifies the orientation to use when mapping the material or network to the Landscape. It contains the following options:   * **TCMT Auto**: Uses landscape vertex coordinates, in the range [0, OverallLandscapeResolution] * **TCMT XY**: Uses object space XY mapping. This is equivalent to TCMT Auto. * **TCMT XZ**: Uses object space XZ mapping. Recommended for side-projected textures. * **TCMT YZ**: Uses object space YZ mapping. Recommended for side-projected textures. |
| 2 | **Custom UVType** | Outputs the UV coordinates to map the material to the Landscape based on the type. It contains the following options:   * **LCCT None**: Do not use custom UVs. * **LCCT Custom UV0**: Use custom UVs in channel 0. * **LCCT Custom UV1**: Use custom UVs in channel 1. * **LCCT Custom UV2**: Use custom UVs in channel 2. * **LCCT Weight Map UV**: Use original Weightmap UVs. |
| 3 | **Mapping Scale** | Applies uniform scaling to the UV coordinates. |
| 4 | **Mapping Rotation** | Applies the rotation, in degrees, to the UV coordinates. |
| 5 | **Mapping Pan [U]** | Applies the offset in the [U] direction to the UV coordinates. |
| 6 | **Mapping Pan [V]** | Applies the offset in the [V] direction to the UV coordinates. |
| 7 | **Unlabeled Output** | Outputs the UV coordinates to map the material to the Landscape based on the given property values. |

### Landscape Layer Switch Node

You can use the **Landscape Layer Switch** node to exclude some material operations when a specific layer is not contributing to a region of the Landscape. You can use this to optimize your material by removing calculations that are not necessary when a layer's weight is zero.

[![Landscape Layer Switch Node](https://dev.epicgames.com/community/api/documentation/image/d0d94b25-1733-4738-a0b8-3bbf5be80f7d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d0d94b25-1733-4738-a0b8-3bbf5be80f7d?resizing_type=fit)

Click image for full size.

This node has the following options:

| Number | Property | Description |
| --- | --- | --- |
| 1 | **Parameter Name** | Displays the unique name of the parameter. |
| 2 | **Preview Used** | If checked, uses a preview. |
| 3 | **Layer Used** | Indicates the material network to use if the specific layer is in use by the current region of the Landscape. |
| 4 | **Layer Not Used** | Indicates the material network to use if the specific layer is not used by the current region of the Landscape. |
| 5 | **Output** | Either the **Layer Used** or **Layer Not Used** inputs, depending on whether the layer contributes to the particular region of the Landscape. |

### Landscape Layer Weight Node

You can use the **Landscape Layer Weight** node to access layer weights and implement your own custom blending solution in the material graph. The output returns (Base + Layer \* LayerWeight). By chaining multiple Landscape Layer Weight nodes together, you can produce a weighted sum that blends between the specified layers.

You can directly access the `LayerWeight` value without modification by setting the **Base** value to `0` and the **Layer** value to `1.0`.

[![Landscape Layer Weight Node](https://dev.epicgames.com/community/api/documentation/image/1cfa415f-6781-4e97-9155-476772833f95?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1cfa415f-6781-4e97-9155-476772833f95?resizing_type=fit)

Click image for full size.

This node has the following options:

| Number | Property | Description |
| --- | --- | --- |
| 1 | **Parameter Name** | Displays the name of the layer whose weight you want to read. |
| 2 | **Preview Weight** | Defines the weight to use for preview purposes in the Material Editor. |
| 3 | **Const Base** | Defines a specific RGB constant value to use when Base is not connected. |
| 4 | **Base** | The node network to blend with this layer. This includes the value of the previous layers and any other underlying data. This gives the layer value multiplied by the painted layer weight. |
| 5 | **Layer** | The value for the specified layer. This input value is multiplied by the layer weight and accumulated onto Base to produce the Output value. |
| 6 | **Output** | Outputs the result of the blending between the Base and Layer inputs, based on the layer weights of the inputs. |

#### Adding a Landscape Layer Weight Node

1. In the **Material Editor**, add a `LandscapeLayerWeight` node.

   [![Landscape-layer-weight-node-in-Blueprints](https://dev.epicgames.com/community/api/documentation/image/2b204b6a-00c3-45ec-9ed8-7c231ac81ba0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2b204b6a-00c3-45ec-9ed8-7c231ac81ba0?resizing_type=fit)
2. In the **Details** panel, change the **Parameter Name** to a descriptive name for the layer, for example, **Rock**.

   [![Landscape-layer-weight-menu-options](https://dev.epicgames.com/community/api/documentation/image/28232a67-7324-4cde-aa72-e97e7da8c412?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/28232a67-7324-4cde-aa72-e97e7da8c412?resizing_type=fit)

   All layer names must be unique. It is recommended to name your layers with a descriptive name that indicates the layer’s contents.
3. **Add** additional Landscape Layer Weight nodes, until you have one for each layer that you want your material to have. This example uses two `LandscapeLayerWeight` nodes.
4. Add and connect your **Texture Samples** or material network expressions to your **Landscape Layer Weight** nodes.
5. **Add** a `LandscapeLayerCoords` node and **set the UV** titling. Connect it to the **Texture Sample** nodes.
6. **Connect** each Layer node's output pin to the Base pin of the next layer node, while leaving the first layer node's Base pin unconnected.
7. Connect the last Layer node's output pin to the **Base Color** input of the `NewMaterial` node.

You should have something similar to the example below:

[![Landscape-layer-weight-in-Blueprints](https://dev.epicgames.com/community/api/documentation/image/4a8439c5-e210-4a4d-8a35-bf24ca94d228?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4a8439c5-e210-4a4d-8a35-bf24ca94d228?resizing_type=fit)

### Landscape Visibility Mask Node

The **Landscape Visibility Mask** node outputs the visibility value of the landscape. The output is the visibility mask value. The value is `0.0` where the landscape is transparent and `1.0` where the landscape is visible.

[![Landscape-visibility-mask-node](https://dev.epicgames.com/community/api/documentation/image/3861a4e4-8c25-4819-b217-2ac6edc6dde7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3861a4e4-8c25-4819-b217-2ac6edc6dde7?resizing_type=fit)

On a standard landscape, landscape visibility requires the material to use a **Masked Opacity Blend Mode**, as the landscape shader needs to sample the visibility weightmap to discard pixels that are not visible enough. In order to do this, you have to connect the **Landscape Visibility Mask** material node to the **Opacity Mask**. This is more costly performance-wise, and should be avoided as much as possible on the global landscape material.

The landscape system is able to automatically detect the regions (landscape components) where visibility information is present. It can then override the material instance’s blend mode, only in those regions, in order to limit where a masked material is actually used. You need to leave the landscape material’s **Blend Mode** to **Opaque**, but connect the **Opacity Mask** (even if it appears greyed out), like this:

[![Visibility-mask-in-blueprints-editor](https://dev.epicgames.com/community/api/documentation/image/4aa86c18-0817-450f-9613-3f9fc0cc434b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4aa86c18-0817-450f-9613-3f9fc0cc434b?resizing_type=fit)

When generating a [Nanite landscapes](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-nanite-with-landscapes-in-unreal-engine) mesh, there’s no cost in the landscape material, as the Nanite renderer can keep on using the hardware rasterizer (the fast path), as it does with any other opaque materials.

## Landscape Layer Blend Technical Information

Landscape layer nodes behave similar to a [Static Switch Parameter](https://dev.epicgames.com/documentation/en-us/unreal-engine/material-parameter-expressions-in-unreal-engine#static-switch-parameter) node. This switches between using one branch of the material and another. Each component of the Landscape has its own **Material Instance Constant** created from the main Landscape material, which is applied to only that component.

If a Landscape component does not use a specific layer, the subtree of nodes connected to the layer is discarded. This reduces the complexity, letting the material applied to the Landscape contain any number of texture samples, as long as it is within the limits set by the shader model.

Using this method, you can create a main Landscape material that contains every texture or material you need, while keeping the final result within the parameters allowed by the hardware.

Please note that currently most RHIs support shared texture samplers, which means that there’s no hard constraint about how many layers can be used on a given landscape component. The exception being ES3.1 (mobile), which still has a hard limit in terms of sampler count (16), across all texture accesses in the material. Hence, if the game is planned to ship on such a platform, it’s important to make sure that the number of landscape layers remains low, since a new weightmap texture will be added every 4 target layers (1 target layer per channel of an RGB8 texture). This means another texture sampler will be added (on top of all the textures that might get sampled by the target layer’s shader code path).  For more information, see [Mobile Landscape Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-materials-in-unreal-engine#mobile-landscape-materials).

Any network of material expressions can be connected to the **Layer** inputs in place of a simple **Texture Sample**. This makes it possible to do more complex effects such as transitioning from detail textures to larger macro textures depending on the distance the layer is being viewed from.

### Landscape Layer Blend Issues

When you use the LB Height Blend mode for multiple Landscape layers, you may find black spots on your Landscape where different layers meet. LB Height Blend works by managing the blend factor, or weight, for the layer, using the specified height value. When multiple layers are painted on an area and are set to LB Height Blend, the layers painted in a particular area can simultaneously have a `0` height value, so the desired blend factor for each layer becomes `0`.

Because there is no specific ordering, black spots can appear because no layers have any contributions in that area. When you blend a Normal map, even more black spots can appear, because this blending results in a Normal value of (`0,0,0`), which is invalid and causes lighting issues. If this happens, paint the area with a material with a non-zero weight.

In the left image, all layers are LB Height Blend, causing some areas to be black. On the right, the red "1" layer has been changed to use LB Alpha Blend.

[![LB Height Blend Problem](https://dev.epicgames.com/community/api/documentation/image/e4f2b94a-1c22-49f2-971a-b398833bb166?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e4f2b94a-1c22-49f2-971a-b398833bb166?resizing_type=fit)

Click image for full size.

Below is an example of the properties of the **Landscape Layer Blend** node for all the layers being blended together. The **Soil** layer has its blend mode set to LB Alpha Blend, while the other layers have theirs set to LB Height Blend. This is to stop the issue mentioned above from happening.

[![Layer Blend Properties](https://dev.epicgames.com/community/api/documentation/image/ec4d7ab9-a269-431e-b705-45ad4a6b28df?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ec4d7ab9-a269-431e-b705-45ad4a6b28df?resizing_type=fit)

Click image for full size.

To delete a layer, click the dropdown arrow to the right of the layer's element number, and select **Delete**.

[![Delete Layer](https://dev.epicgames.com/community/api/documentation/image/f638880b-3dc4-44c7-b2fa-b462629fe914?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f638880b-3dc4-44c7-b2fa-b462629fe914?resizing_type=fit)

Click image for full size.

## Mobile Landscape Materials

You can use any number of Landscape layers, as long as you have enough **Texture Sampler** nodes. The Landscape layer allocation uses the [Feature Level Switch material node](https://dev.epicgames.com/documentation/en-us/unreal-engine/utility-material-expressions-in-unreal-engine), letting a single PC or console Landscape material also have a mobile version. The following image shows how the Landscape in *Fortnite* Battle Royale looks when used for mobile devices.

[![Mobile Landscape Feature Level](https://dev.epicgames.com/community/api/documentation/image/a2985158-b778-4d20-9c85-4341cf92ccd3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a2985158-b778-4d20-9c85-4341cf92ccd3?resizing_type=fit)

While you can use any number of nodes, we recommend that you only use three.

## Assigning Materials to Landscapes

After creating a Landscape material, assign the material to a Landscape actor in your level.

1. In the **Content Browser**, locate the Landscape material that you want to use.
2. Either in the viewport or using the **World Outliner**, select the Landscape.
3. In the **Details** panel for the Landscape, locate the **Landscape Material** option, and click the dropdown to select a material.

   [![Assigned Material](https://dev.epicgames.com/community/api/documentation/image/9e3c0b65-fdbe-455b-ad47-2439cc2653d2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9e3c0b65-fdbe-455b-ad47-2439cc2653d2?resizing_type=fit)

   Click image for full size.

* [materials](https://dev.epicgames.com/community/search?query=materials)
* [landscape](https://dev.epicgames.com/community/search?query=landscape)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Layer Weights and Ordering](/documentation/en-us/unreal-engine/landscape-materials-in-unreal-engine?application_version=5.7#layer-weights-and-ordering)
* [Landscape-Specific Material Nodes](/documentation/en-us/unreal-engine/landscape-materials-in-unreal-engine?application_version=5.7#landscape-specific-material-nodes)
* [Landscape Layer Blend Node](/documentation/en-us/unreal-engine/landscape-materials-in-unreal-engine?application_version=5.7#landscape-layer-blend-node)
* [Landscape Layer Blend Types](/documentation/en-us/unreal-engine/landscape-materials-in-unreal-engine?application_version=5.7#landscapelayerblendtypes)
* [Adding a Landscape Layer Node](/documentation/en-us/unreal-engine/landscape-materials-in-unreal-engine?application_version=5.7#addingalandscapelayernode)
* [Landscape Layer Sample Node](/documentation/en-us/unreal-engine/landscape-materials-in-unreal-engine?application_version=5.7#landscapelayersamplenode)
* [Landscape Layer Coords Node](/documentation/en-us/unreal-engine/landscape-materials-in-unreal-engine?application_version=5.7#landscape-layer-coords-node)
* [Landscape Layer Switch Node](/documentation/en-us/unreal-engine/landscape-materials-in-unreal-engine?application_version=5.7#landscape-layer-switch-node)
* [Landscape Layer Weight Node](/documentation/en-us/unreal-engine/landscape-materials-in-unreal-engine?application_version=5.7#landscape-layer-weight-node)
* [Adding a Landscape Layer Weight Node](/documentation/en-us/unreal-engine/landscape-materials-in-unreal-engine?application_version=5.7#addingalandscapelayerweightnode)
* [Landscape Visibility Mask Node](/documentation/en-us/unreal-engine/landscape-materials-in-unreal-engine?application_version=5.7#landscape-visibility-mask-node)
* [Landscape Layer Blend Technical Information](/documentation/en-us/unreal-engine/landscape-materials-in-unreal-engine?application_version=5.7#landscape-layer-blend-technical-information)
* [Landscape Layer Blend Issues](/documentation/en-us/unreal-engine/landscape-materials-in-unreal-engine?application_version=5.7#layer-blend-issues)
* [Mobile Landscape Materials](/documentation/en-us/unreal-engine/landscape-materials-in-unreal-engine?application_version=5.7#mobile-landscape-materials)
* [Assigning Materials to Landscapes](/documentation/en-us/unreal-engine/landscape-materials-in-unreal-engine?application_version=5.7#assigning-materials-to-landscapes)
