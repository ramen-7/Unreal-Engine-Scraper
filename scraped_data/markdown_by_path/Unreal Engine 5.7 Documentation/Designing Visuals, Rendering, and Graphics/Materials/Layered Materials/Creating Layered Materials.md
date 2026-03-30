<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-layered-materials-in-unreal-engine?application_version=5.7 -->

# Creating Layered Materials

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
5. [Designing Visuals, Rendering, and Graphics](/documentation/en-us/unreal-engine/designing-visuals-rendering-and-graphics-with-unreal-engine "Designing Visuals, Rendering, and Graphics")
6. [Materials](/documentation/en-us/unreal-engine/unreal-engine-materials "Materials")
7. [Layered Materials](/documentation/en-us/unreal-engine/layering-materials-in-unreal-engine "Layered Materials")
8. Creating Layered Materials

# Creating Layered Materials

An introductory document on the Layered Materials technique in Unreal Engine.

![Creating Layered Materials](https://dev.epicgames.com/community/api/documentation/image/1dfee941-b839-4cb6-9d7d-ab18f5c96a09?resizing_type=fill&width=1920&height=335)

 On this page

This tutorial demonstrates the process of creating a simple **Layered Material** comprised of two layers: chrome and snow. The final Layered Material uses a world-aligned blend to automatically place snow on the upward facing surfaces of the mesh, effectively switching between the two Materials. The blend function always checks for the top surface, meaning even as you rotate the object, the snow Material remains on top, as shown in the image below:

[![World aligned layered Material](https://dev.epicgames.com/community/api/documentation/image/8f02005a-481d-4e82-84f5-c72b6e27d352?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8f02005a-481d-4e82-84f5-c72b6e27d352?resizing_type=fit)

Generally when creating Layered Materials, it is common to create each layer as a Material and copy/paste your node network into a new Material Function. To save time, this tutorial builds each layer within Functions to begin with.

## Simple Chrome

|  |  |
| --- | --- |
| Chrome Textures |  |
|  |  |
| T\_ExampleLayers\_Metal\_1\_BC.png | T\_ExampleLayers\_Metal01\_N.png |
| (Right-click and Save As) | (Right-click and Save As) |

The base layer is a simple chrome Material with some subtle surface imperfections to add visual interest. To help demonstrate editability, the Material includes several inputs that allow you to fine-tune the overall look.

1. Right-click in the **Content Browser**, click **Materials** and select **Material Function** in the context menu.

   [![Create Material Function](https://dev.epicgames.com/community/api/documentation/image/9b49cad9-4804-40c6-9976-fb0d03945dc1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9b49cad9-4804-40c6-9976-fb0d03945dc1?resizing_type=fit)
2. Name the Material Function **Layer\_Chrome**.

   [![Rename function](https://dev.epicgames.com/community/api/documentation/image/efc3e40b-6dc1-4ba2-a9d9-6fb6b91d638a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/efc3e40b-6dc1-4ba2-a9d9-6fb6b91d638a?resizing_type=fit)
3. **Double-click** the Material Function to open it in the Material Editor.

   [![New Material function in editor](https://dev.epicgames.com/community/api/documentation/image/20a2b1ca-7fa3-46d1-8525-7ec5b4fec8d9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/20a2b1ca-7fa3-46d1-8525-7ec5b4fec8d9?resizing_type=fit)
4. **Right-click** in the Material Graph, and then search for and select **Make Material Attributes** in the context menu.

   [![Add Make Material Attributes from context menu](https://dev.epicgames.com/community/api/documentation/image/55bf6d3f-47be-45e8-ba2e-14cd6d9f83ab?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/55bf6d3f-47be-45e8-ba2e-14cd6d9f83ab?resizing_type=fit)
5. Connect the **Make Material Attributes** node to the **Output Result** node.

   [![Connect Make Material Attributes](https://dev.epicgames.com/community/api/documentation/image/646d5923-de48-4d83-bec0-8d2a67f5a911?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/646d5923-de48-4d83-bec0-8d2a67f5a911?resizing_type=fit)

### Chrome Material Network

The Material Graph for the chrome layer is shown below, with a breakdown beneath the image so you can replicate it easily. The two textures used are **T\_ExampleLayers\_Metal\_1\_BC.png** for the Base Color and Roughness, and **T\_ExampleLayers\_Metal01\_N.png** for the normal map, both downloadable at the top of this page.

[![Chrome Material Network](https://dev.epicgames.com/community/api/documentation/image/2d583135-7f8b-428d-950a-f069cbfcefff?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2d583135-7f8b-428d-950a-f069cbfcefff?resizing_type=fit)

Click to enlarge image.

See the following notes explaining the four comment blocks in the Material Graph.

1. **Base Color** - For the Base Color, a Linear Interpolate (LERP) is used to blend between the base chrome color and a very dark gray value (0.3). For the base color, create a **Function Input** node and name it **Tint**. Make sure the input type is set to **Vector3** in the Details Panel, which allows you to input a color into the function to change the tint of the chrome. The red channel of the **T\_ExampleLayers\_Metal\_1\_BC** texture is used to drive the interpolation between the two values.

   [![Input type vector 3](https://dev.epicgames.com/community/api/documentation/image/6773c2e9-ad45-4852-838b-2ccc260a95b8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6773c2e9-ad45-4852-838b-2ccc260a95b8?resizing_type=fit)
2. **Metallic** - Since this is a metal Material, a value of 1 is passed into the Metallic input.
3. **Roughness** - Roughness should generally be very low for a chrome Material, but some subtle variation can add depth to the overall look of the Material. In this case, the red channel of the chrome texture is used to LERP between values of 0.2 and 0.4. This means darker areas on the texture map will have slightly higher roughness than the light areas.
4. **Customizable Normal** - This network simply takes in a tangent space normal map and separates the green and red channels, which control the bulk of the map's detail. Each channel is multiplied by a value supplied from another Function Input. This input is set to a Scalar type and named **Normal Multiplier**, with a default value of 1.0. Using an **AppendVector node**, the results are appended together and then appended to the blue channel of the normal map. The result is that the user has the power to adjust the height of the normal by changing the Normal Multiplier value.

Make sure you compile and save your [Material Function](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-material-functions-overview) when finished.

## Simple Snow

|  |  |
| --- | --- |
| Snow Textures |  |
|  |  |
| T\_Cave\_Ice\_Tiling\_D.png | T\_Cave\_Ice\_Noise\_N.png |
| (Right-click and Save As) | (Right-click and Save As) |

Download the two textures above and import them into Unreal Engine. Follow the steps below to create a second Material Function for the snow layer.

1. Right-click in the **Content Browser**, click **Materials** and select **Material Function** in the context menu.

   [![Create Material Function](https://dev.epicgames.com/community/api/documentation/image/0cfb8ec7-4987-4dfc-9416-1b052ffe7c33?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0cfb8ec7-4987-4dfc-9416-1b052ffe7c33?resizing_type=fit)
2. Name the Material Function **Layer\_Snow**.

   [![Rename function](https://dev.epicgames.com/community/api/documentation/image/b9db3042-ce68-41c6-ac19-3a08dc3b2081?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b9db3042-ce68-41c6-ac19-3a08dc3b2081?resizing_type=fit)
3. **Double-click** the Material Function to open it in the Material Editor.

   [![New Material Function](https://dev.epicgames.com/community/api/documentation/image/d01471b9-129d-44d2-9623-d9a1641cd8c6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d01471b9-129d-44d2-9623-d9a1641cd8c6?resizing_type=fit)
4. **Right-click** in the Material Graph, and search for **Make Material Attributes** in the context menu, and add it to the graph.

   [![Add Make Material Attributes from context menu](https://dev.epicgames.com/community/api/documentation/image/07ad7c60-6ecd-46fb-ae4d-e5a4c2cf3599?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/07ad7c60-6ecd-46fb-ae4d-e5a4c2cf3599?resizing_type=fit)
5. Connect the **Make Material Attributes** node to the **Output Result** node.

   [![Connect Make Material Attributes](https://dev.epicgames.com/community/api/documentation/image/949f98e8-dcb8-46df-8818-3a5b6c18bcd0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/949f98e8-dcb8-46df-8818-3a5b6c18bcd0?resizing_type=fit)

### Snow Layer Network

Below is a simple breakdown of the snow Material Graph. This layer uses the **T\_Cave\_Ice\_Tiling\_D.png** and **T\_Cave\_Ice\_Noise\_N.png** textures, both downloadable at the top of this page.

[![Snow Material network](https://dev.epicgames.com/community/api/documentation/image/c00a75b7-b31b-4e48-bae1-bb985c29f2d0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c00a75b7-b31b-4e48-bae1-bb985c29f2d0?resizing_type=fit)

1. **Base Color** - This is the only relatively sophisticated part of the network, and only because it uses the **FuzzyShading** Material Function. This function simply keeps the texture from getting too dark when the Material is receiving light. This is similar to the way light passes through fibrous surfaces. This makes it perfect for velvet, moss, or in this case, snow. Some contrast is removed from the Base Color texture (T\_Cave\_Ice\_Tiling\_D.png) by raising it to the power of 0.3.

   Next, plug the result into a FuzzyShading Material Function, which you can insert from the Functions tab in the Material Editor palette. Set **Core Darkness** to 0, **Power** to 1, and**EdgeBrightness** to 0.5. Finally, multiply the whole thing by a very pale blue color (R=0.8, G=0.9, B=0.95) to give it a cold, icy color cast.
2. **Metallic** - This is a non-metallic surface, so Metallic is set to 0.
3. **Roughness** - Snow should shine a little bit when the light hits it just right, so the red channel of the T\_Cave\_Ice\_Tiling\_D.png texture is used to drive a Lerp between 0.6 and 0.3.
4. **Normal** - The normal map on its own is a little bit too strong. One way to reduce the effect of the tangent space normal map is to double the strength of the blue channel. This is done by multiplying the normal map by a Constant3 Vector with a value of (1,1,2).

Save your result when finished!

## Layered Material

You can now create a Material and blend the two layer functions together. This example is configured so that the snow always appears on the top of the surface. The Material also contains some parameters to make it customizable in Material instances.

1. In the **Content Browser**, click the **Add New** button and choose Material from the context menu.

   [![Create new Material](https://dev.epicgames.com/community/api/documentation/image/6dc93472-e3a1-40fa-baf3-5bd1063f4386?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6dc93472-e3a1-40fa-baf3-5bd1063f4386?resizing_type=fit)
2. Name your new Material **Mat\_SnowyChrome**.

   [![Rename your Material](https://dev.epicgames.com/community/api/documentation/image/545b5273-2fa6-4494-8c0a-ed6d57ec4639?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/545b5273-2fa6-4494-8c0a-ed6d57ec4639?resizing_type=fit)
3. **Double-click** the Material to open it in the Material Editor.

   [![Open new Material in Material Editor](https://dev.epicgames.com/community/api/documentation/image/6d1da1da-433a-4187-b0b5-51bd140ca096?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6d1da1da-433a-4187-b0b5-51bd140ca096?resizing_type=fit)
4. Drag your **Layer\_Chrome** and **Layer\_Snow** Material Functions from the **Content Browser** into the Material Graph.

   [![Drag layers into Material Graph](https://dev.epicgames.com/community/api/documentation/image/ab42b3b4-972c-4b6d-a4a7-0ab11ae5227a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ab42b3b4-972c-4b6d-a4a7-0ab11ae5227a?resizing_type=fit)
5. Click in the background of the Material Graph to display the base Material Properties in the Details panel. Enable **Use Material Attributes** by checking the box.

   [![Enable Use Material Attributes](https://dev.epicgames.com/community/api/documentation/image/72ea1f31-a3ef-47ff-af4e-f004feb4e9ad?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/72ea1f31-a3ef-47ff-af4e-f004feb4e9ad?resizing_type=fit)
6. From the Palette, add a **MatLayerBlend\_Simple** Material Function, as well as a **WorldAlignedBlend** Function. The MatLayerBlend\_Simple will execute the transition from chrome to snow, and the World\_Aligned\_Blend will power the Layer Blend based on the direction the surface is pointed.

### Layered Material Network

Below is a breakdown of the Mat\_SnowyChrome Material network, along with descriptions for each of the commented areas.

[![Layered Material graph](https://dev.epicgames.com/community/api/documentation/image/2968b966-31be-4a88-b097-38740d3db756?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2968b966-31be-4a88-b097-38740d3db756?resizing_type=fit)

1. **Chrome Setup** - Two parameters are connected to the Layer\_Chrome Material Function. The first is a Scalar Parameter named **Chrome Normal**, which is used to drive the **NormalMultiplier** input. The second is a Vector Parameter named **ChromeTint** that is driving the **Tint** input. These parameters allow you to alter the strength of the normal map, and change the tint of the chrome when the Material is instanced later.
2. **Snow Setup** - No additional nodes are needed. The Layer\_Snow Material Function is plugged directly into the blend node.
3. **World Aligned Blend Setup** - The WorldAlignedBlend node controls the position and sharpness of the Material blend. Set the **Blend Sharpness** value to 10. Then create a Scalar Parameter named **BlendBias** and connect it to the **Blend Bias** input. This allows you to adjust the vertical position on your mesh where the blend occurs.
4. **MatLayerBlend** - This node contains the logic used to drive the blend. In this case, the base Material is Layer\_Chrome and the top Material is Layer\_Snow. The WorldAlignedBlend is plugged into the Alpha input to drive the the transition.

Save your Material when done!

## Instancing a Layered Material

Since this Material contains two parameters, you can now create a Material Instance and customize aspects of the Material Layers.

1. If you included the Starter Content in your project, you will have a set of chairs and a table to apply the new Material to. If not, feel free to place some of your own assets in the scene.

   [![](https://dev.epicgames.com/community/api/documentation/image/2d4c4eec-36b9-4dcf-ac7c-d7ee8ff15455?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2d4c4eec-36b9-4dcf-ac7c-d7ee8ff15455?resizing_type=fit)
2. Right-click on the **Mat\_SnowyChrome** Material and choose **Create Material Instance** in the context menu. The default name should be fine.

   [![Create Material Instance](https://dev.epicgames.com/community/api/documentation/image/e352b116-426e-4d6f-a038-116469e7810c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e352b116-426e-4d6f-a038-116469e7810c?resizing_type=fit)
3. Drag the Material Instance asset from the **Content Browser** onto one of the objects in the scene.

   [![Apply Material instance from Content Browser](https://dev.epicgames.com/community/api/documentation/image/9e1a96e7-e428-4d0f-8133-0f8242b0225a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9e1a96e7-e428-4d0f-8133-0f8242b0225a?resizing_type=fit)
4. **Double-click** the Material Instance to open it in the Material Instance Editor. You can override the tint of the chrome, the depth of the chrome's normal map, and how much snow has fallen on top of it.

* [materials](https://dev.epicgames.com/community/search?query=materials)
* [shaders](https://dev.epicgames.com/community/search?query=shaders)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Simple Chrome](/documentation/en-us/unreal-engine/creating-layered-materials-in-unreal-engine?application_version=5.7#simple-chrome)
* [Chrome Material Network](/documentation/en-us/unreal-engine/creating-layered-materials-in-unreal-engine?application_version=5.7#chrome-material-network)
* [Simple Snow](/documentation/en-us/unreal-engine/creating-layered-materials-in-unreal-engine?application_version=5.7#simple-snow)
* [Snow Layer Network](/documentation/en-us/unreal-engine/creating-layered-materials-in-unreal-engine?application_version=5.7#snow-layer-network)
* [Layered Material](/documentation/en-us/unreal-engine/creating-layered-materials-in-unreal-engine?application_version=5.7#layered-material)
* [Layered Material Network](/documentation/en-us/unreal-engine/creating-layered-materials-in-unreal-engine?application_version=5.7#layered-material-network)
* [Instancing a Layered Material](/documentation/en-us/unreal-engine/creating-layered-materials-in-unreal-engine?application_version=5.7#instancing-a-layered-material)
