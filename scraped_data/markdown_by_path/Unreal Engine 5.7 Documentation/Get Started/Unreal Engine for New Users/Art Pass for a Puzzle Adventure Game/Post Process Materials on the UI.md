<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-06-post-process-materials-on-the-ui-in-unreal-engine?application_version=5.7 -->

# Post Process Materials on the UI

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
5. [Get Started](/documentation/en-us/unreal-engine/get-started "Get Started")
6. [Unreal Engine for New Users](/documentation/en-us/unreal-engine/unreal-engine-for-new-users "Unreal Engine for New Users")
7. [Art Pass for a Puzzle Adventure Game](/documentation/en-us/unreal-engine/art-pass-for-a-puzzle-adventure-game "Art Pass for a Puzzle Adventure Game")
8. Post Process Materials on the UI

# Post Process Materials on the UI

Learn how to use Materials to create gameplay-driven, on-screen post-process effects.

![Post Process Materials on the UI](https://dev.epicgames.com/community/api/documentation/image/85d7c076-2589-476b-841a-2ba7116f1d29?resizing_type=fill&width=1920&height=335)

 On this page

So far, you’ve used a Post Process Volume to adjust pre-existing settings that control the look of your scene. To add your own custom post-process effect, you can create a **post-process material**. The material can then apply that effect to the camera or add it to a Post Process Volume to affect what the player sees on screen.

In this part of the series, you’ll add an effect to visually convey damage on screen when the player takes damage. The edges of the screen will pulse in red. As the player’s health gets lower, the effect intensifies and takes up more space on the screen.

To implement this, you’ll:

* Build a parent post-process material.
* Create a Material Instance to control the parameters in the parent material.
* Display and control the on-screen effect with Blueprint Visual Scripting.
* Modify the player character’s blueprint logic so their health (HP) regenerates after a period of time, making the damaged-player visual effect disappear.

## Before You Begin

Make sure you understand these topics covered in previous sections of the [Art Pass for a Puzzle Adventure Game](https://dev.epicgames.com/documentation/en-us/unreal-engine/art-pass-for-a-puzzle-adventure-game) tutorial series:

* Building Materials and Material Instances.
* Adding a Post Process Volume to a level.

You’ll work with the following assets in the [sample project file](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-01-project-setup-and-content-import):

* `BP_AdventureCharacter` Blueprint

## Create a Material to Show Damage

First, you’ll make a material that will be the base that defines the effect’s appearance. The material will create a grayscale mask, making the in-game camera view display on the lighter parts of the mask and the pulsing-red damage effect appear on the darker parts of the mask.

[![You'll build this set of expressions throughout this tutorial](https://dev.epicgames.com/community/api/documentation/image/1e18f42b-94bb-4a19-8b8b-4f852b2a8472?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1e18f42b-94bb-4a19-8b8b-4f852b2a8472?resizing_type=fit)

To create a new post-process material, follow these steps:

1. In the **Content Browser**, go to the **AdventureGame > Artist > Materials** folder.
2. In the **Materials** folder, create a new **Material** asset named `M_Screen_Damage`. Open the material.
3. In the **Details** panel, change the material **Domain** to **Post Process**.

   You’ll notice this changes what pins are available on the material’s root node. For a post-process material, you’ll only control the emissive color because these materials don’t use scene lighting.

In **Surface**-type materials, the emissive color controls how much light the material gives off. When you change a material’s **Domain** to **Post Process**, it’s no longer shading a surface, but writing directly to the screen. In this case, emissive color controls the final output color for each pixel.

### Define the Damage Effect Shape

Now, you’ll start building the material’s graph, starting with the mask that defines the shape of the post-process effect. First, you’ll use a **GeneratedRoundRectNode** to draw a grayscale mask in the shape of a rounded rectangle, where the inside of the shape is white and the outside is black. Later, you’ll define what appears on each part of the mask.

[![](https://dev.epicgames.com/community/api/documentation/image/0e1bdab6-de97-4415-a336-2e2f5a514d5b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0e1bdab6-de97-4415-a336-2e2f5a514d5b?resizing_type=fit)

You'll add this set of expressions in this section of the tutorial.

To create the grayscale mask, follow these steps:

1. In the material graph, on the left side of the material root node, add a **GeneratedRoundRect** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/79ffaae8-f694-4aaa-aa58-2cabcdfb1177?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/79ffaae8-f694-4aaa-aa58-2cabcdfb1177?resizing_type=fit)

   You can see an example of the node’s output in the preview window if you connect it to the material root node.
2. Add a ScreenPosition node.
3. Connect the **ScreenPosition** node's **ViewportUV** output to the **UV Coords (V2)** input on the **GeneratedRoundRect** node.

   The **ViewportUV** output tells the **GeneratedRoundRect** node to draw the mask within the same space as the viewport screen’s coordinates.

To control the mask’s shape with a vector parameter, follow these steps:

1. Add a **Constant4Vector** node. You can use this node to create a color value, or use it more broadly as a collection of values that can control the size and shape of the **GeneratedRoundRect** mask.

   Press and hold **4** on your keyboard and click the graph to add this node.
2. Right-click the vector node and select **Convert to Parameter** to turn the constant into a Vector Parameter. Name it`Damage Mask Controls`.

   [![](https://dev.epicgames.com/community/api/documentation/image/c37534e6-4a26-442a-a56d-d0022ef37b28?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c37534e6-4a26-442a-a56d-d0022ef37b28?resizing_type=fit)

   With Vector Parameters, you can use each channel’s value the same as you would separate single-value Constant (or Scalar Parameter) nodes, making your graph more efficient and tidier. By default, the values have RGBA color channel labels, but you can make these values represent whatever you like by renaming them in the node’s **Details** panel.
3. In the **Details** panel, in the **Parameter Customization** category, expand **Channel Names** and assign names to each color channel in the vector parameter node. You’ll name these channels to correspond to the **GeneratedRoundRect** node’s inputs:

   * **R** = `Size X`
   * **G** = `Size Y`
   * **B** = `Corner Radius`
   * **A** = `Sharpness`

   |  |  |
   | --- | --- |
   |  |  |
   | **Details** panel parameter channel names | **Damage Mask Controls** with renamed channel names |
4. In the **Material Expression Vector Parameter** category, expand **Default Value** and set the following default values for each channel:

   * **Size X** = 1
   * **Size Y** = 1
   * **Corner Radius** = 0.4
   * **Sharpness** = 0.2
5. In the graph, drag off the constant vector node’s **Size X** pin and create an **AppendVector** node.
6. Connect the **Size Y** pin to the **Append**node’s **B** input.
7. Connect the **Append** node’s output pin to the **Box Dimensions** pin on the **GeneratedRoundRect** node.
8. Connect the **Corner Radius** and **Sharpness** pins on the **Damage Mask Controls** and **GeneratedRoundRect** nodes.

   [![](https://dev.epicgames.com/community/api/documentation/image/3b174566-7127-4ace-a64a-faa31de1d14d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3b174566-7127-4ace-a64a-faa31de1d14d?resizing_type=fit)
9. Add a comment block around these nodes labelled `Damage Mask Falloff`.

In the **GeneratedRoundRectNode**, **UV Coords** defines where the material draws the rectangle, and **Box Dimensions** defines how large the rectangle is within that space. **Box Dimensions** of (1, 1) make the rectangle (or white portion) take up most of the screen space, and (0.5, 0.5) make the rectangle fill half the screen’s width and height.

To view the rectangular mask, follow these steps:

1. Connect the **GeneratedRoundRect** node to the **Emissive Color** input of the material root node.

   [![](https://dev.epicgames.com/community/api/documentation/image/d4a4a9a2-0862-4b6f-af69-2666f4a0cfe8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d4a4a9a2-0862-4b6f-af69-2666f4a0cfe8?resizing_type=fit)
2. Select the **Damage Mask Controls** node and experiment with different **Size**, C**orner Radius**, and **Sharpness** values to see the effect each has on the rectangle.
3. Reset the values back to the defaults you set earlier, and delete the wire between **GeneratedRoundRect** and the main material node.

### Display Visuals on Different Parts of the Mask

In [Expanded Material Instances](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-04-expanded-material-instances), you used **linear interpolation (lerp)** to blend between dry and wet looks on your stone floor material. The floor material’s **Lerp** node used a Timeline as the **Alpha** input to blend between two parameter values. Remember, in a **Lerp** node, the **Alpha** input controls how much the Lerp blends between **A** and **B** inputs. When Alpha is 0, you get all A. When Alpha is 1, you get all B.

The Alpha value can also come from a grayscale mask where each pixel provides a value: white areas show B, black areas show A, and gray areas blend between them. So in this section, you’ll use a **Lerp** node to blend between your unobscured game view in the middle of the screen (where the mask is white) to a red color along the edge of the screen (where the mask is black).

[![](https://dev.epicgames.com/community/api/documentation/image/a2510778-7c7b-42f1-b31c-0582ed95d13f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a2510778-7c7b-42f1-b31c-0582ed95d13f?resizing_type=fit)

You'll add these expressions in this section of the tutorial.

To blend between the game screen and the red color that represents damage taken, follow these steps:

1. To the right of the **GeneratedRoundRect** node, add a LinearInterpolate (or **Lerp**) node. Hover over the node, click the **Toggle Comment Bubble** button, and enter `1`.

   Numbering your Lerp nodes helps you follow along with the tutorial since this graph uses several Lerp nodes. We’ll refer to this node as **Lerp (1)**.

   ![](https://dev.epicgames.com/community/api/documentation/image/d01a54b3-9ceb-4d65-aaa0-4de0e8d1aa73?resizing_type=fit)
2. Connect the **GeneratedRoundRect Result** output to the **Alpha** input of the **Lerp (1)** node.
3. Add a **SceneTexture**node.
4. In the **Details** panel, change the **Scene Texture Id** to **PostProcessInput0**.

   [![](https://dev.epicgames.com/community/api/documentation/image/6afd10e2-0bec-4416-9d90-ba80050098d3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6afd10e2-0bec-4416-9d90-ba80050098d3?resizing_type=fit)
5. Connect the **Color** output of the **SceneTexture** node to the **B** input of the **Lerp (1)** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/f533c59e-e2d6-4993-8467-f0537fa00c88?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f533c59e-e2d6-4993-8467-f0537fa00c88?resizing_type=fit)
6. In the graph, add a **Constant3Vector**. Right-click the node and select **Convert to Parameter**. Name the parameter `Damage Color`. This parameter controls the color of the damage effect.
7. Click the color swatch next to **Default Value** and change the color to red (**R = 1**).
8. Connect the **Damage Color** node’s top (white) pin to the **A** input on the **Lerp (1)** node. The top pin of the damage color only outputs the three RGB color channels.
9. Connect the **Lerp (1)** output to the material root node’s **Emissive Color** pin to check the results in the preview window. You’ll see an undefined arithmetic error due to a Float3-to-Float4 conversion issue.

   [![](https://dev.epicgames.com/community/api/documentation/image/f52f5b62-acd9-4722-9e0c-c4c1227c8255?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f52f5b62-acd9-4722-9e0c-c4c1227c8255?resizing_type=fit)

The **Damage Color** node’s top pin outputs a Float3 value (three channels, RGB), and the **SceneTexture** node’s **Color** pin outputs a Float4 value (four channels, RGBA). To resolve this error and make the value types match, you can use a **Component Mask** to remove the **Alpha** channel from the **Color** output of the **Scene Texture**, since you only need the three channels (RGB) to match. Component Masks are a common way to solve this sort of error.

To turn the **SceneTexture** node’s color into a Float3 value and resolve the error, follow these steps:

1. Add a **ComponentMask** node and connect the **SceneTexture** node’s **Color** pin to the **Mask**node.
2. Connect the output of the **Mask** node to the **B** input of the **Lerp (1)** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/968f4a07-c8da-4353-9f41-9b826b9db0e6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/968f4a07-c8da-4353-9f41-9b826b9db0e6?resizing_type=fit)
3. Click the arrow at the bottom of the **Mask** node to see checkboxes for each channel in the Color output.
4. By default, the component mask only masks R and G channels. Add a checkmark next to **B**. This creates a Float3 component mask so both **Lerp (1)** inputs use the same channels.

   [![](https://dev.epicgames.com/community/api/documentation/image/792cece1-8656-4def-beb8-846a3bc75bcc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/792cece1-8656-4def-beb8-846a3bc75bcc?resizing_type=fit)

The graph should look like this:

[![](https://dev.epicgames.com/community/api/documentation/image/5a36c2df-2f94-46d8-8631-e674f9b1032c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5a36c2df-2f94-46d8-8631-e674f9b1032c?resizing_type=fit)

The material should look like this in your preview viewport:

[![](https://dev.epicgames.com/community/api/documentation/image/7535a3af-fcad-4fce-baee-f6e98c45afee?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7535a3af-fcad-4fce-baee-f6e98c45afee?resizing_type=fit)

### Add Noise and Variation to the Effect

In this section, you’ll build out the noise section of the material by applying a texture around the outer edge of the frame. With this, you can use material parameters to direct the final look of the effect as it relates to the character’s damage in-game.

In visual effects, noise adds controlled randomness. It’s a pattern you can use to make materials feel more organic and less perfect, like on uneven surfaces or on a flickering light.

[![](https://dev.epicgames.com/community/api/documentation/image/d51d1bc5-af51-423a-8756-8565fa7eb301?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d51d1bc5-af51-423a-8756-8565fa7eb301?resizing_type=fit)

You'll add these expressions in this section of the tutorial.

To add noise to the material, follow these steps:

1. At the bottom of the graph, add a **ScreenAlignedUVs** node. With the **ScreenAlignedUVs** node, you can map a texture or effect across the entire screen. It generates UV coordinates for the whole viewport or screen.
2. Drag off the **X 100%, Y 100%** pin and add a **Multiply** node.
3. Right-click and create a **Constant** node. Right-click it, select **Convert to Parameter**, and name it **Noise Tiling**. Connect it to the **B** input of the **Multiply** node.
4. In the **Noise Tiling** node, set the **Default Value** to `1`.

   [![](https://dev.epicgames.com/community/api/documentation/image/5d105627-d623-4f4a-a968-020e548e70f9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5d105627-d623-4f4a-a968-020e548e70f9?resizing_type=fit)
5. Drag off the **Multiply** node’s output pin and create a **TextureSample** node, with the wire connected to the **UVs** input.
6. Right-click on **TextureSample**, convert it to a parameter, and name it `Noise Texture`.

   [![](https://dev.epicgames.com/community/api/documentation/image/b3611422-b82f-4f61-bd06-8ab32a33397c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b3611422-b82f-4f61-bd06-8ab32a33397c?resizing_type=fit)
7. With the **Noise Texture** node selected, near the bottom of the **Details** panel in the **Material Expression Texture Base** category, set the **Noise Texture** texture assignment slot to `TilingNoise05`.

   [![](https://dev.epicgames.com/community/api/documentation/image/2affd5f7-27bb-4aea-b7cf-c21e50390d79?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2affd5f7-27bb-4aea-b7cf-c21e50390d79?resizing_type=fit)

   This texture is a part of the Engine Content included with Unreal Engine. You can use your own, but this one is a good default to start with if you don’t have an alternative. Note that if you use a different texture, your results may differ from those shown in this tutorial.
8. Drag off the **R** channel of the **Noise Texture** node and create a **Multiply** node.
9. Right-click its **B** pin and select **Promote to Parameter**. Name the parameter `Noise Falloff` and set its **Default Value** to `1`.
10. Drag off the **Multiply** node’s output pin and create a **Power** node.
11. Right-click the **Exp** pin and select **Promote to Parameter**. Name the parameter `Noise Amount` and set its **Default Value** to `1`.
12. Select the eight nodes you just created and press **C** to add a comment box around them. Label the comment box `Noise in Damage Mask`.

    [![](https://dev.epicgames.com/community/api/documentation/image/e39c23bb-cae7-40d8-b417-870a9f9d81e0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e39c23bb-cae7-40d8-b417-870a9f9d81e0?resizing_type=fit)

At this point, you can test this part of the material by connecting the **Power** node directly to the **Emissive Color** input on the `M_Screen_Damage` material root node. You should see the following in the preview window:

[![](https://dev.epicgames.com/community/api/documentation/image/84cc0819-b9ca-4dbf-adbe-db8088fa462e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/84cc0819-b9ca-4dbf-adbe-db8088fa462e?resizing_type=fit)

When you’re done testing, disconnect the material root node from the noise texture logic and reconnect it to the **Lerp (1)** node. You’ll continue to build other parts of the material before connecting everything later in this guide.

### Add Noise to the Mask

Now that you have your noise mask, you need to blend it into the damage mask falloff by combining the two using a multiply node. This applies the noise mask to the inner-edge results of the damage mask closest to the center of the screen.

[![](https://dev.epicgames.com/community/api/documentation/image/0a97bf22-629f-44a2-9e23-e8c80c5142ac?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0a97bf22-629f-44a2-9e23-e8c80c5142ac?resizing_type=fit)

You'll add the highlighted set of expressions in this section of the tutorial.

To add the noise texture to the black areas of the mask, follow these steps:

1. Move the `M_Screen_Damage` material root node to the right to create some space next to the **GeneratedRoundRect** node. Delete the wire between the **GeneratedRoundRect** node and the existing **Lerp (1)** node since you’ll be adding new logic here.
2. Right-click the graph and create a new **Lerp** node. Hover over the node, click **Toggle Comment Bubble**, and enter `2` as the comment.

   [![](https://dev.epicgames.com/community/api/documentation/image/ed4026cb-2d46-4b5a-b633-8e2be708f612?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ed4026cb-2d46-4b5a-b633-8e2be708f612?resizing_type=fit)
3. Connect the **Result** pin of the **GenerateRoundRect** node to the **Alpha** pin of the **Lerp (2)** node.
4. Drag the **output** of the **GenerateRoundRect** node and create a **One Minus** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/bf970a81-9ee5-467e-9b8d-052234f5caee?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bf970a81-9ee5-467e-9b8d-052234f5caee?resizing_type=fit)
5. Drag off the **One Minus** node, create an **Add** node, and connect its output to the **Lerp (2)** node’s **B** pin.

   [![](https://dev.epicgames.com/community/api/documentation/image/02e0c23b-fcbc-485e-a590-b0295c946a0a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/02e0c23b-fcbc-485e-a590-b0295c946a0a?resizing_type=fit)
6. Drag off the **One Minus** node and add a **Multiply** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/2cb9f82f-a792-4ad1-b8cb-22c97377f780?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2cb9f82f-a792-4ad1-b8cb-22c97377f780?resizing_type=fit)
7. Drag off the **Multiply** output, add a new **One Minus** node, and connect it to the **B** input of the **Add** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/f52c5707-5061-43e5-9512-d82a810a02f9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f52c5707-5061-43e5-9512-d82a810a02f9?resizing_type=fit)
8. After the **Lerp (2)** node, add a **Saturate** node. This clamps the output values in a **0-1** range.
9. Add a comment to this logic and label it `Gets the Brightest Spots of the Mask`.

   [![](https://dev.epicgames.com/community/api/documentation/image/2e0b9df8-ece8-4add-9310-14eab5a451ec?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2e0b9df8-ece8-4add-9310-14eab5a451ec?resizing_type=fit)

At this point, you’re material should look similar to this:

[![](https://dev.epicgames.com/community/api/documentation/image/533834a1-5f86-4352-aca0-05c8b4242647?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/533834a1-5f86-4352-aca0-05c8b4242647?resizing_type=fit)

### Connect the Noise, Mask, and Damage Color Sections

To connect the Noise, Damage Mask, and Damage Color elements of the graph, follow these steps:

1. In the Noise Mask logic, drag off the **Power** node and connect it to the **B** input of the **Multiply** node in the Damage Mask Area logic.

   Use reroute nodes on any wire to help create clearer paths and reorganize the graph. Double-click on a wire to add a reroute node, then drag it to change the wire’s path.
2. Connect the **Saturate** node’s output pin to the **Lerp (1)** node’s **Alpha** pin.

   [![](https://dev.epicgames.com/community/api/documentation/image/5690571d-db34-4f42-84f9-b61df7e99631?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5690571d-db34-4f42-84f9-b61df7e99631?resizing_type=fit)
3. **Save** and **Apply** changes to the material.

You can connect the **Lerp (1)** node to the **Emissive Color** input on the material root node to see the result:

[![](https://dev.epicgames.com/community/api/documentation/image/e60d8cf7-e59b-467f-a2b8-0597045cd68c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e60d8cf7-e59b-467f-a2b8-0597045cd68c?resizing_type=fit)

Now, you’ve defined a rectangular mask area, applied a color to this mask, created a noise mask using a texture, and blended them into what you see in the material editor preview window.

### Add Pulsations to the Damage Effect

In this section, you’ll build the material logic that causes the red color damage indicator around the edge to pulse as the player takes more damage. You’ll use a **Sine** node to drive the pulsing behavior, and modify the sine wave to only use positive values.

[![](https://dev.epicgames.com/community/api/documentation/image/7c9dabfc-1405-4d3b-bc51-aa05c9b7ef40?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7c9dabfc-1405-4d3b-bc51-aa05c9b7ef40?resizing_type=fit)

You'll add the highlighted section of expressions in this part of the tutorial.

To make the red effect pulse as the damage increases, follow these steps:

1. In an empty section at the top of your graph, add a **Time** node.

   The **Time** node outputs the passage of time in the editor and is helpful for animating materials and changing them over a specified period.
2. Drag off its pin and add a **Multiply**node.
3. Create a **Constant** node, convert it to a parameter, and name it **Pulse Speed**. In the node, set its **Default Value** to `0.5`.
4. Connect **Pulse Speed** to the **B** input on the **Multiply** node.
5. Drag off the **Multiply** node and add a **Sine** node.

   The **Sine** node converts the increasing **Time** value into a value that smoothly oscillates between -1 and 1 in a repeating wave pattern.

   [![](https://dev.epicgames.com/community/api/documentation/image/d1db6d18-4fa6-44d8-bf73-09b8cea40f04?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d1db6d18-4fa6-44d8-bf73-09b8cea40f04?resizing_type=fit)
6. Drag off the **Sine** node output and add an **Add** node. Ensure its **B** input value is set to **1.0**.
7. Drag off the **Add** node and add a **Divide** node. Ensure its **B** input is **2.0**.

   By setting up this **Add** 1 and **Divide** by 2, you’re changing the sine wave to go from 1 to 0 instead of between 1 and -1. This prevents the **Sine** node from inverting the texture’s values, causing it to flash from red to light blue (the inversion of red).

   [![](https://dev.epicgames.com/community/api/documentation/image/11c9a294-a8a2-4106-9e99-05ac1104a601?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/11c9a294-a8a2-4106-9e99-05ac1104a601?resizing_type=fit)
8. Drag off the **Divide** node and add a **Multiply** node.
9. Drag off its **B** input and create a **Constant**. Convert it to a parameter and name it `Pulse Amount`. Set its **Default Value** to `1`.

   [![](https://dev.epicgames.com/community/api/documentation/image/4b00b9fb-aa24-4615-87cf-cdd1fd81a1c7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4b00b9fb-aa24-4615-87cf-cdd1fd81a1c7?resizing_type=fit)
10. Select the nodes in this section of the graph and press **C** to add a comment block. Label it `Damage Pulse Amount and Speed`.

    [![](https://dev.epicgames.com/community/api/documentation/image/749bc24c-f99f-4bce-8f90-4144a7a5dddf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/749bc24c-f99f-4bce-8f90-4144a7a5dddf?resizing_type=fit)

Your material now contains all the primary elements that comprise the damage effect for this post-process material. Your graph should look similar to this one now:

[![](https://dev.epicgames.com/community/api/documentation/image/e0a7008b-7efa-4afb-acae-b53a6a2e50d1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e0a7008b-7efa-4afb-acae-b53a6a2e50d1?resizing_type=fit)

### Connect the Pulse Logic

Now that you’ve got the pulsing logic set up, you’ll integrate this into the application of damage color to the scene texture. Then, you can change the intensity of the mask as it pulses.

[![](https://dev.epicgames.com/community/api/documentation/image/5b8f4c8e-d100-433d-9bd7-d3098accc313?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5b8f4c8e-d100-433d-9bd7-d3098accc313?resizing_type=fit)

You'll add the highlighted section of expressions in this part of the tutorial.

You’ll build off the **Damage Pulse Amount and Speed** section and add expressions that connect the pulse logic to the Damage Color and Scene Texture sections of the graph.

While working in this section, you’ll be disconnecting some elements you’ve already set up in previous sections and integrating new connections. You can drag nodes around to create space when overlapping wires are difficult to follow.

To connect the pulse logic to the damage color, follow these steps:

1. Right-click in the graph and create a new **Lerp** node near the **Damage Color** node and pulse logic. Label it with a `3`.
2. At the end of the pulse logic, connect the **output** of the **Multiply** node to the **Alpha** pin of **Lerp (3)**.

   [![](https://dev.epicgames.com/community/api/documentation/image/1ee318df-5201-4b48-a7aa-1d79622f8bde?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1ee318df-5201-4b48-a7aa-1d79622f8bde?resizing_type=fit)

   In the **Lerp (3)** node, the **Alpha** controls the amount of pulse applied to the mask and how often the pulse should happen.
3. Delete the **Damage Color** wire from the **A** input of **Lerp (1)**, and connect it to the **B** input of the new **Lerp (3)** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/2e342a54-56a2-4261-a226-d750cadb941d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2e342a54-56a2-4261-a226-d750cadb941d?resizing_type=fit)
4. Select the Damage Color node. In the Details panel under **Parameter Customization**, expand Channel Names, and use the text field to change the A channel name to `Color Amount`.
5. In the **Material Expressions Vector Parameter** category, under **Default Value**, set the **Color Amount** value to `2`.

   [![](https://dev.epicgames.com/community/api/documentation/image/3ad61b73-9f03-46dd-a4ed-84421218262e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3ad61b73-9f03-46dd-a4ed-84421218262e?resizing_type=fit)
6. On the **Damage Color** node, drag off the **Color Amount** pin, add a **Divide** node, and connect its output to the **A** input of the **Lerp (3)** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/d9a1da26-2139-4867-a8b4-a40b5fc8604b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d9a1da26-2139-4867-a8b4-a40b5fc8604b?resizing_type=fit)
7. Create a new **Lerp** node near the **Lerp (3)** node and pulse logic. Label it with a `4`.
8. Connect the **Lerp (3)** node’s output to the **Alpha** input of **Lerp (4)**.

   [![](https://dev.epicgames.com/community/api/documentation/image/cc6b8648-bfcf-4471-a491-6ddac67c46c9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cc6b8648-bfcf-4471-a491-6ddac67c46c9?resizing_type=fit)
9. Connect the **RGB** (white color) pin of the **Damage Color** node to the **B** input of **Lerp (4)**.
10. Return to the **Mask (RGB)** node connected to the **SceneTexture** node. Connect the **Mask** node’s output to the **A** input of **Lerp (4)**. The component mask node now has wires going to **Lerp (1)** input **B** and **Lerp (4)** input **A**.

    [![](https://dev.epicgames.com/community/api/documentation/image/ad186bff-b723-4d85-bafb-b261d02c92d6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ad186bff-b723-4d85-bafb-b261d02c92d6?resizing_type=fit)
11. Connect the output of **Lerp (4)** to the **A** input of **Lerp (1)**.
12. Drag and select the **Lerp (3)** and **Lerp (4)** nodes. Press **C** to create a comment box around them, and label it `Lerp Pulse and Color`.
13. Click **Save** and **Apply**.

This new part of the graph should look like this:

[![](https://dev.epicgames.com/community/api/documentation/image/916e0337-9b27-4aa9-80f6-480dcd867ffd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/916e0337-9b27-4aa9-80f6-480dcd867ffd?resizing_type=fit)

You can connect **Lerp (3)** to the **Emissive Color** input on the material root node to see the results of the damage effect in the material preview window:

![66](https://dev.epicgames.com/community/api/documentation/image/8e5629ec-81e2-4b8d-bf60-e3a8fe0b1070?resizing_type=fit)

In the example above, the **Color Amount** value on the **Damage Color** node has been increased to 5.0 to make the effect clearly visible in the preview window.

In the graph, change the **Pulse Speed** and **Pulse Amount** values to see how they change the size of the effect and the speed at which the effect is applied. **Pulse Amount** must be between 0 and 1. In later steps, you’ll be able to control both of these parameters in a Material Instance.

### Control the Effect with a Damage Amount Parameter

The last thing you’ll add to your material graph is a new parameter called **Damage Amount** that controls the effect's size based on how much damage the player has received when playing the game.

This parameter will be set in the character’s Blueprint so that when the player takes damage, the parameter controls the amount of pulsing damage displayed around the outer edges of the screen. The more damage the player takes, the stronger the effect of this material becomes on the player’s screen.

To add a parameter that controls the size of the effect at runtime, follow these steps:

1. Add some space between your existing material logic and the `M_Screen_Damage` material root node. Right-click the graph and add a **Lerp** node. Label this **Lerp** node with a `5`.
2. Connect the **Mask (RGB)** node’s output to the **A** pin of the **Lerp (5)** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/46a7ad1b-1a82-40e9-81c8-47bb9a4f7dfb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/46a7ad1b-1a82-40e9-81c8-47bb9a4f7dfb?resizing_type=fit)
3. Connect the **Lerp (1)** node’s output to the **B** input of **Lerp (5)**.

   [![](https://dev.epicgames.com/community/api/documentation/image/459113bc-5c61-4c64-a991-fa8fd08fe111?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/459113bc-5c61-4c64-a991-fa8fd08fe111?resizing_type=fit)
4. On **Lerp (5)**, right-click the **Alpha** pin and select **Promote to Parameter**, name the parameter **Damage Amount**, and change its default value to `1`.

   [![](https://dev.epicgames.com/community/api/documentation/image/365533b4-b758-4aa3-9d73-0b3108b32cb6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/365533b4-b758-4aa3-9d73-0b3108b32cb6?resizing_type=fit)

   Name this parameter accurately and ensure it has a default value; the player character blueprint will use this parameter to control how much this material appears on screen when the player takes and heals from damage.
5. Connect the **Lerp (5)** node’s output to the **Emissive Color** input of the root node.

The **Damage Amount** value uses a value between 0 (no damage, effect off) and 1 (max damage, effect on).

This is the result you’ll see in the preview window:

[![](https://dev.epicgames.com/community/api/documentation/image/b4633b8b-978c-4a01-b3da-6680657c6e09?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b4633b8b-978c-4a01-b3da-6680657c6e09?resizing_type=fit)

In the example here, the **Color Amount** value on the **Damage Color** node has been increased to 5.0 to make the effect clearly visible in the preview window.

Next, you’ll add a new set of nodes that uses **Damage Amount** as input to affect the size of the **GeneratedRoundRect** mask. This addition makes the damage effect pulse inward toward the center of the screen as the player takes more damage, and recede as the player’s health is regenerated.

To make **Damage Amount** affect the size and intensity of the damage mask, follow these steps:

1. In the material graph, go to the **Damage Mask Falloff** section. Delete the wire between the **Append** node and the  **GeneratedRoundRect** node.
2. Drag off the **Append** node and add a **Multiply** node.
3. Connect the output of the **Multiply** node to the **Box Dimensions** input of the **GeneratedRoundRect** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/2c86eec3-ca3f-4a5f-8081-2fe12b8577d7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2c86eec3-ca3f-4a5f-8081-2fe12b8577d7?resizing_type=fit)
4. On the **Multiply** node, drag off input **B** and add a **Lerp** node. Label the **Lerp** node `6`.
5. On the **Lerp (6)** node, leave the **A** value at **0** and set the **B** value to `0.75`.
6. Right-click the **Lerp (6)** node’s **Alpha** and choose **Promote to Parameter**. Name the node **Damage Amount** to match your other **Damage Amount** node. Alternatively, you could copy and paste the original **Damage Amount** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/1edc4595-0ea0-4650-acde-6e5e01fa1e3a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1edc4595-0ea0-4650-acde-6e5e01fa1e3a?resizing_type=fit)
7. Click **Apply** and **Save**.

This is the result you’ll see in the preview window:

![](https://dev.epicgames.com/community/api/documentation/image/eefddb24-fc1a-427a-a003-b1d79b609388?resizing_type=fit)

In the example here, the **Color Amount** value on the **Damage Color** node has been increased to 5.0 to make the effect clearly visible in the preview window.

Your `M_Screen_Damage` material graph should look like the following when everything is built:

Blueprint

Copy full snippet(1072 lines long)

To copy this snippet into your project, delete any existing nodes in your material graph, click **Copy Full Snippet**, and press **Ctrl + V** in your material. Then, connect the **Lerp (5)**node to the main material node’s **Emissive Color** pin.

## Create a Material Instance to Control the Effect

Now that you have your material, create a Material Instance to control all the parameters you created in the material. You’ll use the exposed parameters in the material instance to define the final look and feel of the damage effect on screen.

To set up a Material Instance to control material parameters, follow these steps:

1. In the **Content Browser**, in your **Artist > Materials** folder, right-click the material `M_Screen_Damage` and select **Create Material Instance** from the context menu.
2. Name the asset `MI_Screen_Damage` and open it.

   [![](https://dev.epicgames.com/community/api/documentation/image/166c8c96-f9cb-4590-b983-44dc9fd16086?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/166c8c96-f9cb-4590-b983-44dc9fd16086?resizing_type=fit)
3. To make the material preview run in real-time and see how changing parameters affects the material, click the yellow stopwatch button above the viewport twice.

   [![](https://dev.epicgames.com/community/api/documentation/image/adc904c2-42c3-469b-b3f7-5284aca66316?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/adc904c2-42c3-469b-b3f7-5284aca66316?resizing_type=fit)
4. In the **Details** panel, expand the sections in **Parameter Groups** to see all the parameters you’ve exposed in the material. Expand the vector parameters, like **Damage Mask Controls**, to see their individual parameter values.
5. Add checkmarks next to all parameters except **Noise Texture** to allow them to be overridden.

   Removing the checkmark from a parameter after you’ve changed its value uses the original default value set in the parent material.
6. While working on your material instance, experiment with the different parameters to see how they affect the damage effect in the preview window. Try different values for **Pulse Amount**, **Noise Falloff**, **Pulse Speed**, and the **Damage Mask Controls** (vector parameter) to see how these change the effect.
7. The value for **Damage Amount** is set to 1 by default, so you can see the changes happening to the material in the preview window. However, change this to `0` so that when the game starts, the effect doesn’t appear on screen until the player is damaged. In the next section, you’ll make the player character blueprint control this value.
8. **Save** the Material Instance.

Later, when you’re able to test the effect in-game, you can return to the Material Instance and repeat these steps to adjust the effect.

### Set Parameter Values in the Material Instance

This tutorial’s sample level uses the following parameter values. You can use these values or adjust them as desired in your project.

|  |  |  |
| --- | --- | --- |
| Parameter | Default Values | Suggested Values |
| **Global Scalar Parameter Values** |  |
| Damage Amount | 0 | 0 |
| Noise Amount | 1.0 | 0.35 |
| Noise Falloff | 1.0 | 0.75 |
| Noise Tiling | 1.0 | 1.1 |
| Pulse Amount | 1.0 | 0.75 |
| Pulse Speed | 0.5 | 0.65 |
| **Global Texture Parameter Values** |  |
| Noise Texture | TilingNoise05 | TilingNoise05 |
| **Global Vector Parameter Values** |  |
| Damage Color | Hex sRGB: FF0000FF | Hex sRGB: FF0000FF |
| Damage Color: Color Amount | 2.0 | 5.0 |
| Damage Mask Controls: Size X | 1.0 | 0.75 |
| Damage Mask Controls: Size Y | 1.0 | 0.5 |
| Damage Mask Controls: Corner Radius | 0.4 | 2.0 |
| Damage Mask Controls: Sharpness | 0.2 | 2.1 |

### [Optional] Organize and Limit Parameter Values

To make the Material Instance’s parameter values simpler to navigate and use and reduce the chance of extreme values, you can organize parameters in groups and apply value ranges to keep numerical sliders within acceptable or intended values.

For example, **Damage Amount** is used to mirror the health of the player, where 0 is no damage on screen and 1 is full damage on screen, so it makes sense to set up a slider that is within this range since it can’t exceed that range.

In the parent material, select each named parameter and use the **Details** panel to set up each one’s **Group** and **Slider Min** and **Slider Max** range as follows:

|  |  |  |  |
| --- | --- | --- | --- |
| Parameter | Group | Slider Min | Slider Max |
| Damage Amount | Damage | 0 | 1 |
| Pulse Amount | Pulse | 0 | 1 |
| Pulse Speed | Pulse | 0 | 2 |
| Damage Color: Color Amount | Pulse | N/A | N/A |
| Noise Tiling | Noise | -1 | 2 |
| Noise Falloff | Noise | 1 | 5 |
| Noise Amount | Noise | 0.5 | 3 |
| Damage Mask Controls | Noise | N/A | N/A |
| Noise Texture | Noise | N/A | N/A |

In the Material Instance, you can see how this change affects this value in the parameters list. Parameters are organized into new categories depending on their Group. You can drag sliders between their min and max values without exceeding those values.  However, you can override the slider’s limits by manually entering a new value.

[![](https://dev.epicgames.com/community/api/documentation/image/6e1ba180-4e9a-4fc8-8c72-33ef0ca03523?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6e1ba180-4e9a-4fc8-8c72-33ef0ca03523?resizing_type=fit)

## Add the Post-Process Material to the Character Blueprint

You now have the post-process material set up and instanced. Next, you’ll set up the character’s blueprint to create and use a **Dynamic Material Instance** (also called a Material Instance Dynamic, or MID). This will use the `MI_Screen_Damage` material instance to read the parameter named Damage Amount in the Blueprint. Using logic you set up in the blueprint graph, you can make material adjustments in real-time based on what’s happening during gameplay by injecting a value into the material instance for Damage Amount.

The character has a Health variable that changes when they are damaged. You’ll use this variable with the material instance to apply the effect to the character's screen as they take more damage and remove the effect as their health regenerates.

### Create a Dynamic Material Instance and Add it to Post-Processing

Your material instance is an asset that you can’t directly modify at runtime. Instead, in the character blueprint, you’ll create a **Dynamic Material Instance**. A Dynamic Material Instance is a runtime version of a material instance, created when the game starts, that you can change while the game is running through its named parameters. Then, you’ll assign the MID to the player’s camera so that it’s displayed on screen when the player takes damage.

To create and save an instance of your material in a variable, follow these steps:

1. In the **Content Browser**, go to **Content > AdventureGame > Designer > Blueprints > Characters** and open the `BP_AdventureCharacter` blueprint.
2. In the Event Graph, find the group of logic that starts with the **Event BeginPlay** node. Drag this group to an area of the graph with more space so you can add more nodes to this logic.

   To find an event node in the graph, in the My Blueprint panel, expand the **EventGraph** list, and double-click **Event BeginPlay**. The graph view focuses on that node.

   [![](https://dev.epicgames.com/community/api/documentation/image/4e2f7577-391a-4472-8ab3-1c8c0088550f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4e2f7577-391a-4472-8ab3-1c8c0088550f?resizing_type=fit)
3. After the **Set Default Movement Speed** node, drag off the execution (**exec**) pin and add a **Create Dynamic Material Instance** node.
4. On this **Create Dynamic Material Instance** node, set the Parent to `MI_ScreenDamage`. This is the material instance you created earlier that you’ll use to control the damage effect on the screen.

   [![](https://dev.epicgames.com/community/api/documentation/image/8014a861-a744-4a9e-a793-87fd11601d08?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8014a861-a744-4a9e-a793-87fd11601d08?resizing_type=fit)
5. Right-click the node’s **Return Value** pin and select **Promote to Variable**.
6. In the **My Blueprint** panel, in the **Variables** list, rename **NewVar** to `MID Damage`.

   [![](https://dev.epicgames.com/community/api/documentation/image/a12d28a5-6c9a-478a-8671-55caf93c5de4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a12d28a5-6c9a-478a-8671-55caf93c5de4?resizing_type=fit)

Now, the **Create Dynamic Material Instance** node creates a runtime version of `MI_Screen_Damage` and saves it in the new variable, making it available to reference elsewhere in your graph.

To assign the material instance to the camera’s post-processing pass, follow these steps:

1. In the **Components** panel, drag the **FirstPersonCamera** component onto the graph. This creates a reference to the player camera.
2. Drag off its output and create a **Set Post Process Settings** node.
3. Connect the two **Set** nodes’ **exec** pins.

   [![](https://dev.epicgames.com/community/api/documentation/image/af6504f8-5a24-494c-ba42-f757271a6ea8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/af6504f8-5a24-494c-ba42-f757271a6ea8?resizing_type=fit)
4. Drag off the Set Post Process Settings node’s Post Process Settings input and add a Make Post Process Settings node.
5. Select the Make Post Process Settings node. In the Details panel, in the Rendering Features category, add a check mark next to Post Process Materials to add that pin to the Make Post Process Settings node.

   [![](https://dev.epicgames.com/community/api/documentation/image/3636c1e0-b69a-4094-aa08-6ceb10862ba5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3636c1e0-b69a-4094-aa08-6ceb10862ba5?resizing_type=fit)
6. In the node, right-click the **Post Process Materials** input pin and select **Split Struct Pin**. The pin now takes an array as input.
7. Drag off the **Post Process Materials Array** pin and add a **Make Array** node.
8. Drag off the **Make Array** node’s **[0]** input and add a **Make Weighted Blendable** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/22c9fd08-56ea-4bcf-a04b-4a3b5eeb1924?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/22c9fd08-56ea-4bcf-a04b-4a3b5eeb1924?resizing_type=fit)
9. On the **Make Weighted Blendable** node, change **Weight** to `1`.
10. Drag off the **Set MID Damage** node’s output (blue) pin and connect it to the **Make Weighted Blendable** node’s **Object** input.

    [![](https://dev.epicgames.com/community/api/documentation/image/ab2b3149-41f3-4b96-a8ca-937aa0c4f3b5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ab2b3149-41f3-4b96-a8ca-937aa0c4f3b5?resizing_type=fit)

    A **Set** node’s output pin gives a reference to that variable.
11. Select the nodes you’ve added in the graph and press **C** to create a comment box around them. Label it `Create Dynamic Material Instance for Post-Process Effect and assign to Player Camera`.

    [![](https://dev.epicgames.com/community/api/documentation/image/1f114908-a921-4da7-bdcc-caa953697f5c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1f114908-a921-4da7-bdcc-caa953697f5c?resizing_type=fit)
12. **Compile** and **Save** the blueprint.

This logic creates the Dynamic Material Instance when the game starts and applies it to the first-person camera of this blueprint.

The new section of the player’s **Event BeginPlay** logic looks like this:

[![](https://dev.epicgames.com/community/api/documentation/image/ddf388bd-39ab-4a8a-bd91-77b2d44e2a3f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ddf388bd-39ab-4a8a-bd91-77b2d44e2a3f?resizing_type=fit)

Here's a snippet of the highlighted section above that you can copy into the event graph instead of building the logic yourself:

Blueprint

Copy full snippet(300 lines long)

 To copy this snippet into your project, click Copy Full Snippet, press Ctrl + V to paste it into BP\_AdventureCharacter’s event graph, and then connect the Set Default Movement Speed node’s exec pin to the Create Dynamic Material Instance node. 

### Test the Effect In-Game

In the Material Instance (`MI_Screen_Damage`), temporarily change **Damage Amount** to `1`, and click **Save**. When you play the game, you can test the effect without taking damage to dial in the look and feel you want for the effect. With **Damage Amount** set to `1`, the material is turned on continuously. When you’re done testing the material, set the **Damage Amount** back to `0`.

[![](https://dev.epicgames.com/community/api/documentation/image/f44ccce9-63b9-4e86-a77f-d0b180710a72?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f44ccce9-63b9-4e86-a77f-d0b180710a72?resizing_type=fit)

The in-game result when you set Damage Amount to 1 to continually show without the player having taken damage.

Next, you’ll add the logic to the character blueprint that tells this material instance dynamic to appear when the character receives damage and recede when their health regenerates.

## Hide or Show the Effect With Damage Taken

To make the Dynamic Material Instance effect only appear when the player is damaged, you’ll extend the existing damage-handling logic in the player character.

This new logic needs to:

1. Change the material’s **Damage Amount** parameter based on the character’s **Health** variable so that:

   * There is no post-process effect on the screen when **Health** is full.
   * There is a post-process effect on the screen that intensifies as Health decreases.
2. Restore **Health** to full after the player doesn’t take damage for a period of time, removing the post-process effect.

### Create a Maximum Health Variable

You'll be working with the player's health value, so it's best to save the player's maximum health in a variable that you can reference throughout the damage-effect logic instead of entering a static, hard-coded value of 100. This way, if you decide to give your character more or less starting health, your blueprint logic still works properly.

To create a variable that stores the player's maximum health, follow these steps:

1. In `BP_AdventureCharacter`, in the **My Blueprint** panel, in the **Variables** section, click **+** to add a new variable.
2. Name it `MaxHealth` and change the type to **Float**. Compile the blueprint.
3. In the event graph, in the **Event BeginPlay** group of logic you were working with in the previous section, focus on the **Event BeginPlay** and **Set Default Movement Speed** nodes.

   [![](https://dev.epicgames.com/community/api/documentation/image/e54cf1c4-515e-441a-b1b9-0ce1ad1d15a2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e54cf1c4-515e-441a-b1b9-0ce1ad1d15a2?resizing_type=fit)
4. Drag off **Event BeginPlay** and add a **Set MaxHealth** node.
5. From the **Variables** list, drag the **Health** variable onto the new **Set** node's **Max Health** pin.

   [![](https://dev.epicgames.com/community/api/documentation/image/146ab23f-64fa-4bd2-9857-7d6ec816801e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/146ab23f-64fa-4bd2-9857-7d6ec816801e?resizing_type=fit)

Now when the game starts, the **Health** value (100 by default) is saved to **MaxHealth**. As the player plays the game and **Health** changes, **MaxHealth** stays the same, preserving the player's maximum health.

### Connect Current Player Health to the Material

First, you’ll extend the player’s damage-handling logic to control the Dynamic Material Instance using the **Damage Amount** parameter so that as the player’s health decreases, the intensity of the effect on screen increases.

[![](https://dev.epicgames.com/community/api/documentation/image/1110a427-964f-4317-8084-472d7051195c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1110a427-964f-4317-8084-472d7051195c?resizing_type=fit)

To scale the **Damage Amount** up as the player loses health, follow these steps:

1. In the character blueprint, go to the group of logic labelled **(DT) Damage and defeat handling** near the bottom-left section of the event graph. You’re going to add new logic between the **Set Health** and the **Branch** nodes, so add some space between these nodes.

   [![](https://dev.epicgames.com/community/api/documentation/image/089d311a-ccea-4e38-aa66-93f742652074?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/089d311a-ccea-4e38-aa66-93f742652074?resizing_type=fit)
2. In the **Variables** list, drag the **MID Damage** variable onto the graph and select **Get MID Damage**.
3. Drag off the **Get MID Damage** node's output pin and choose **Set Scalar Parameter Value** from the list.
4. Connect **Set Health** to the **Set Scalar Parameter Value**, and then to the **Branch** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/1c658674-7748-43e5-894f-c962c445557d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1c658674-7748-43e5-894f-c962c445557d?resizing_type=fit)
5. On the **Set Scalar Parameter Value** node, for the **Parameter Name**, enter `Damage Amount`. This is the material parameter that controls the size and strength of the effect on-screen.

   This name MUST match the corresponding parameter in the material `M_Screen_Damage` for the effect to work.

   [![](https://dev.epicgames.com/community/api/documentation/image/5200bd98-ea27-418e-855f-f4ccd1a44774?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5200bd98-ea27-418e-855f-f4ccd1a44774?resizing_type=fit)
6. On the **Set Scalar Parameter Value** node, drag off the **Value** input and create a **Lerp** node.
7. On the **Lerp** node, set **A** to `1.0` and B to `0`. This remaps the values so that when damage is applied, it goes from max health (100) to 0 as you lose health instead of the other way around.
8. On the **Lerp** node, drag off the **Alpha** input and create a **Divide** node.
9. From the **Variables** list, drag the character’s **Health** variable onto the top input of the **Divide** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/12ae90e1-01b6-48e0-9df6-413a8961f460?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/12ae90e1-01b6-48e0-9df6-413a8961f460?resizing_type=fit)
10. Drag the character's **MaxHealth** variable onto the bottom input of the **Divide** node.

The **Divide** node turns the player’s health into a number between 1 and 0, where 1 is full health (no damage). However, the **Damage Amount** value needs to increase as the player loses health, not decrease. The Lerp node reverses the value range. For example, if **Health** is 25, the **Lerp** returns a value of 0.75 to the **Set Scalar Parameter Value** node, resulting in an effect that is 75% of the maximum intensity.

The **(DT) Damage and defeat handling section** of the graph should look similar to this now:

[![](https://dev.epicgames.com/community/api/documentation/image/b477cb4b-a774-437a-a5e2-8c74c5af70f4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b477cb4b-a774-437a-a5e2-8c74c5af70f4?resizing_type=fit)

### Add a Resetting Delay to Regenerate Health

For the player’s **Health** variable (or HP) to regenerate to full so the damage effect disappears, the player character should stop taking damage for a short amount of time. You’ll use a **Retriggerable Delay** node to implement a five-second delay that must complete before **Health** is restored.  You can use this type of delay node to reset a cooldown — it waits for a set amount of time before executing the next node, but if it’s triggered again before the time runs out, it restarts the countdown.

To add a delay before removing the damage effect, follow these steps:

1. Under the **Branch** node, drag off the **Fn Set HP** node’s **exec** pin and add a **Sequence** node. You’ll use this to add a series of actions to execute after the player takes damage and is not yet out of health.

   [![](https://dev.epicgames.com/community/api/documentation/image/741214b0-5237-43a2-b3b5-7d2779b0205c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/741214b0-5237-43a2-b3b5-7d2779b0205c?resizing_type=fit)
2. Drag off the **Then 0** path and add a **Retriggerable Delay** node. In the delay node, set the **Duration** to `5` seconds.

   [![](https://dev.epicgames.com/community/api/documentation/image/16dcb55f-2f80-4000-b99c-64677fc69611?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/16dcb55f-2f80-4000-b99c-64677fc69611?resizing_type=fit)
3. As a best practice, check that the player is still alive after the delay:

   1. Drag off the **Retriggerable Delay** and add a **Branch** node.
   2. On the **Branch** node, drag off the **Condition** pin and add a **Greater (>)** node.
   3. In the **Variables** panel, drag a **Health** variable onto the top pin of the **Greater (>)** node.

      [![](https://dev.epicgames.com/community/api/documentation/image/05d5227a-e91b-4a6a-ae18-5e22dbf9414e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/05d5227a-e91b-4a6a-ae18-5e22dbf9414e?resizing_type=fit)

Now, each time the player takes damage and isn’t eliminated (their health is not 0), the time delay restarts from 0. Next, you’ll set up the logic that should execute after the delay completes.

Your blueprint graph should look similar to this now:

[![](https://dev.epicgames.com/community/api/documentation/image/b28e87bc-2365-4bda-8396-b7d283ce880b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b28e87bc-2365-4bda-8396-b7d283ce880b?resizing_type=fit)

### Set Up a Timeline for Blending Player Health

In this section of the graph, you’ll add a Timeline that you’ll use to gradually regenerate the player’s Health over a short time. The Timeline node’s controls define how it starts, stops, and what happens during the track time.

To set up a five-second-long Timeline, follow these steps:

1. In the graph under the **Sequence** node’s **Then 0** logic, right-click the graph, search for `add timeline` in the node actions list, and select **Add Timeline**. Name the Timeline node `Damage Blend`.

   [![](https://dev.epicgames.com/community/api/documentation/image/8c325421-9525-451f-9622-29bf08392227?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8c325421-9525-451f-9622-29bf08392227?resizing_type=fit)
2. Double-click the **Damage Blend** node to open it in its own tab in the blueprint.
3. In this tab, click **+ Track > Add Float Track** to add a new track to the Timeline.

   [![](https://dev.epicgames.com/community/api/documentation/image/df2f10de-e4d8-41ed-9af7-c400af40b40a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/df2f10de-e4d8-41ed-9af7-c400af40b40a?resizing_type=fit)
4. Name the track **Blend**. This track label also appears as an output pin on the 
   Damage Blend Timeline node.

   [![](https://dev.epicgames.com/community/api/documentation/image/8cabf9f6-f324-4fc8-b7fe-c3e22e03a38f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8cabf9f6-f324-4fc8-b7fe-c3e22e03a38f?resizing_type=fit)
5. Next to the **+ Track** button, ensure the **Length** is **5** seconds.
6. In the **Blend** track, right-click and select **Add key to CurveFloat\_0**. Repeat this to add another key; you need two in total.
7. Click the first key to select it and change its values to **Time** = **0** and **Value** = **0**.

   [![](https://dev.epicgames.com/community/api/documentation/image/5c19c8c8-fd31-47f5-8700-d3e0d1270fcf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5c19c8c8-fd31-47f5-8700-d3e0d1270fcf?resizing_type=fit)
8. Click the second key and change its values to **Time** = **5** and V**alue** = **1**.
9. Right-click the first key and select **Auto**. This changes the blend from linear blending to a smooth blend between 0 and 1.

   [![](https://dev.epicgames.com/community/api/documentation/image/67779b6e-54f8-4a03-a0e7-86e970079d4a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/67779b6e-54f8-4a03-a0e7-86e970079d4a?resizing_type=fit)
10. Using the blueprint tabs, go back to the Event Graph where the **Damage Blend** Timeline node is located.
11. On the **Sequence** node, connect the **Then 1** exec pin to the 
    Damage Blend  node’s **Stop** pin.

    [![](https://dev.epicgames.com/community/api/documentation/image/84a84ccd-2f08-4109-ae6b-1e130cfd60ed?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/84a84ccd-2f08-4109-ae6b-1e130cfd60ed?resizing_type=fit)
12. From the **Branch** node after the delay, drag off **True** and connect it to the **Play from Start** input on the Damage Blend node.

    [![](https://dev.epicgames.com/community/api/documentation/image/9b197324-29af-4e16-867e-a81dca9e3c00?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9b197324-29af-4e16-867e-a81dca9e3c00?resizing_type=fit)

Now, this Timeline node outputs a value that changes from 0 to 1 over five seconds. When the **Retriggerable Delay** finishes, the Timeline plays. When the Timeline track logic finishes, execution continues through the **Then 1** path and stops the Timeline from updating.

### Restore Player Health and Remove the Post-Process Material

Now that you have a Timeline set up, you’ll build the logic that uses the five-second track to blend the player’s Health variable back to its full, starting value and lower the material’s **Damage Amount** back to 0.

To gradually restore player health using the Timeline, follow these steps:

1. After the **Damage Blend** Timeline node, create a **Lerp** node. Connect the timeline's **Blend** output pin to the **Alpha** input on the **Lerp** node.
2. On the **Lerp** node, drag off the **B** input and add a reference to **MaxHealth**.
3. In the **Variables** list, drag the **Health** variable onto the **A** input of the **Lerp** node.
4. Drag off the **Lerp** node’s **Return Value** pin and add a **Set Health** node (under **Variables** > **Default** in the node actions list).
5. Drag off the Timeline’s **Update** pin and connect it to the **Set Health** node’s **exec** pin.

   [![](https://dev.epicgames.com/community/api/documentation/image/832a1de1-ca92-4d40-8c46-8a55a0002efe?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/832a1de1-ca92-4d40-8c46-8a55a0002efe?resizing_type=fit)

   Now, the **Lerp** node blends from the player’s current **Health** value to the maximum health they had at the start of the game (in this case, 100) over five seconds (the length of the Timeline).
6. Return to the part of the Event Graph with the **Set Scalar Parameter Value** node you created before the **Branch** node. Drag to select the **Set Scalar Parameter Value**, **MID Damage**, **Lerp**, **Divide**, and **Health** nodes and press **Ctrl+C** to copy them.

   [![](https://dev.epicgames.com/community/api/documentation/image/abf4dd51-6197-4064-9480-737fe202d94a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/abf4dd51-6197-4064-9480-737fe202d94a?resizing_type=fit)
7. In the Event Graph, return to the **Damage Blend** Timeline and press **Ctrl+V** to paste the nodes.
8. Connect the **Set Health** node's **exec** pin to the **Set Scalar Parameter Value** **exec** pin.

   [![](https://dev.epicgames.com/community/api/documentation/image/e6a6991c-7ff2-44c5-aa91-80f3d5cbc54c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e6a6991c-7ff2-44c5-aa91-80f3d5cbc54c?resizing_type=fit)

Now, as the player’s **Health** variable is restored to full, **Damage Amount** decreases back to 0.

Your graph should look similar to this now:

[![](https://dev.epicgames.com/community/api/documentation/image/1ffabf98-e680-4adc-a956-789b236d5ab7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1ffabf98-e680-4adc-a956-789b236d5ab7?resizing_type=fit)

### Display Updated Health on the HUD

As the **Health** variable regenerates back to 100, it displays on the player’s UI with two decimal places. To remove this visual noise from the HUD, you’ll add logic that removes the decimal places and only displays **Health** as a whole number.

This is an example that shows the difference between using Truncate to remove decimal places:

[![](https://dev.epicgames.com/community/api/documentation/image/94055718-154f-423c-89b5-cf429edd40c8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/94055718-154f-423c-89b5-cf429edd40c8?resizing_type=fit)

To ensure player **Health** is a round number when displayed in the HUD, follow these steps:

1. Go to the **Fn Set HP** node that executes before the **Sequence** node you created. Select the **Fn Set HP** node and its inputs (**HUD** and **Health**) and press **Ctrl + C** to copy.

   [![](https://dev.epicgames.com/community/api/documentation/image/7d6f52d1-58ae-4d09-b6c6-e42507faf20b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7d6f52d1-58ae-4d09-b6c6-e42507faf20b?resizing_type=fit)
2. After the **Set Scalar Parameter Value** node at the end of your Timeline logic, press **Ctrl + V** to paste the three nodes.
3. Connect the **Set Scalar Parameter Value** and **Fn Set HP** nodes’ **exec** pins.

   [![](https://dev.epicgames.com/community/api/documentation/image/823718c9-33d4-4214-a48c-f35ba0f7a802?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/823718c9-33d4-4214-a48c-f35ba0f7a802?resizing_type=fit)
4. Drag the **Fn Set HP** node to the right to create some space.
5. Delete the wire between the **Health** variable and the **New HP** input on the **Fn Set HP** node.
6. Drag off the **Health** variable and add a **Truncate** node. This converts the float value to an integer, removing any decimal places.
7. Drag off the **Truncate** node and connect it to the **Fn Set HP** node’s **New HP** input. Unreal Engine automatically adds an Integer-to-Float conversion node.

   [![](https://dev.epicgames.com/community/api/documentation/image/faae2226-2b82-4c13-ac2d-fd87d5d8fa1b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/faae2226-2b82-4c13-ac2d-fd87d5d8fa1b?resizing_type=fit)
8. **Compile** and **Save** the blueprint.

Your complete Blueprint should look like this now with all the additions you made:

[![](https://dev.epicgames.com/community/api/documentation/image/c00239a9-ee27-4e8c-8dcd-40d099a30e52?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c00239a9-ee27-4e8c-8dcd-40d099a30e52?resizing_type=fit)

## Test The Final Effect

When you play the game now and take damage, you should see the post-process damage effect appear and grow as you take more damage.

You can return to the Material Instance and adjust the parameter values to achieve the final look you want. The damage effect is amplified in the example below.

## Next Up

In the next section, you'll learn to enhance your level's atmospheric elements by adding denser fog in low-lying areas and adding storm clouds in the sky.

* [![Adjust Environment Lighting Features](https://dev.epicgames.com/community/api/documentation/image/dec29683-7a6c-4230-bee7-ed15fd14d1b8?resizing_type=fit&width=640&height=640)

  Adjust Environment Lighting Features

  Learn to enhance your level's atmospheric elements by adding denser fog in low-lying areas and adding storm clouds in the sky.](https://dev.epicgames.com/documentation/en-us/unreal-engine/07-adjust-environment-lighting-features)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Before You Begin](/documentation/en-us/unreal-engine/artist-06-post-process-materials-on-the-ui-in-unreal-engine?application_version=5.7#beforeyoubegin)
* [Create a Material to Show Damage](/documentation/en-us/unreal-engine/artist-06-post-process-materials-on-the-ui-in-unreal-engine?application_version=5.7#createamaterialtoshowdamage)
* [Define the Damage Effect Shape](/documentation/en-us/unreal-engine/artist-06-post-process-materials-on-the-ui-in-unreal-engine?application_version=5.7#definethedamageeffectshape)
* [Display Visuals on Different Parts of the Mask](/documentation/en-us/unreal-engine/artist-06-post-process-materials-on-the-ui-in-unreal-engine?application_version=5.7#displayvisualsondifferentpartsofthemask)
* [Add Noise and Variation to the Effect](/documentation/en-us/unreal-engine/artist-06-post-process-materials-on-the-ui-in-unreal-engine?application_version=5.7#addnoiseandvariationtotheeffect)
* [Add Noise to the Mask](/documentation/en-us/unreal-engine/artist-06-post-process-materials-on-the-ui-in-unreal-engine?application_version=5.7#addnoisetothemask)
* [Connect the Noise, Mask, and Damage Color Sections](/documentation/en-us/unreal-engine/artist-06-post-process-materials-on-the-ui-in-unreal-engine?application_version=5.7#connectthenoise,mask,anddamagecolorsections)
* [Add Pulsations to the Damage Effect](/documentation/en-us/unreal-engine/artist-06-post-process-materials-on-the-ui-in-unreal-engine?application_version=5.7#addpulsationstothedamageeffect)
* [Connect the Pulse Logic](/documentation/en-us/unreal-engine/artist-06-post-process-materials-on-the-ui-in-unreal-engine?application_version=5.7#connectthepulselogic)
* [Control the Effect with a Damage Amount Parameter](/documentation/en-us/unreal-engine/artist-06-post-process-materials-on-the-ui-in-unreal-engine?application_version=5.7#controltheeffectwithadamageamountparameter)
* [Create a Material Instance to Control the Effect](/documentation/en-us/unreal-engine/artist-06-post-process-materials-on-the-ui-in-unreal-engine?application_version=5.7#createamaterialinstancetocontroltheeffect)
* [Set Parameter Values in the Material Instance](/documentation/en-us/unreal-engine/artist-06-post-process-materials-on-the-ui-in-unreal-engine?application_version=5.7#setparametervaluesinthematerialinstance)
* [[Optional] Organize and Limit Parameter Values](/documentation/en-us/unreal-engine/artist-06-post-process-materials-on-the-ui-in-unreal-engine?application_version=5.7#%5Boptional%5Dorganizeandlimitparametervalues)
* [Add the Post-Process Material to the Character Blueprint](/documentation/en-us/unreal-engine/artist-06-post-process-materials-on-the-ui-in-unreal-engine?application_version=5.7#addthepost-processmaterialtothecharacterblueprint)
* [Create a Dynamic Material Instance and Add it to Post-Processing](/documentation/en-us/unreal-engine/artist-06-post-process-materials-on-the-ui-in-unreal-engine?application_version=5.7#createadynamicmaterialinstanceandaddittopost-processing)
* [Test the Effect In-Game](/documentation/en-us/unreal-engine/artist-06-post-process-materials-on-the-ui-in-unreal-engine?application_version=5.7#testtheeffectin-game)
* [Hide or Show the Effect With Damage Taken](/documentation/en-us/unreal-engine/artist-06-post-process-materials-on-the-ui-in-unreal-engine?application_version=5.7#hideorshowtheeffectwithdamagetaken)
* [Create a Maximum Health Variable](/documentation/en-us/unreal-engine/artist-06-post-process-materials-on-the-ui-in-unreal-engine?application_version=5.7#createamaximumhealthvariable)
* [Connect Current Player Health to the Material](/documentation/en-us/unreal-engine/artist-06-post-process-materials-on-the-ui-in-unreal-engine?application_version=5.7#connectcurrentplayerhealthtothematerial)
* [Add a Resetting Delay to Regenerate Health](/documentation/en-us/unreal-engine/artist-06-post-process-materials-on-the-ui-in-unreal-engine?application_version=5.7#addaresettingdelaytoregeneratehealth)
* [Set Up a Timeline for Blending Player Health](/documentation/en-us/unreal-engine/artist-06-post-process-materials-on-the-ui-in-unreal-engine?application_version=5.7#setupatimelineforblendingplayerhealth)
* [Restore Player Health and Remove the Post-Process Material](/documentation/en-us/unreal-engine/artist-06-post-process-materials-on-the-ui-in-unreal-engine?application_version=5.7#restoreplayerhealthandremovethepost-processmaterial)
* [Display Updated Health on the HUD](/documentation/en-us/unreal-engine/artist-06-post-process-materials-on-the-ui-in-unreal-engine?application_version=5.7#displayupdatedhealthonthehud)
* [Test The Final Effect](/documentation/en-us/unreal-engine/artist-06-post-process-materials-on-the-ui-in-unreal-engine?application_version=5.7#testthefinaleffect)
* [Next Up](/documentation/en-us/unreal-engine/artist-06-post-process-materials-on-the-ui-in-unreal-engine?application_version=5.7#nextup)

Related documents

[Post Process Materials

![Post Process Materials](https://dev.epicgames.com/community/api/documentation/image/3198247a-13f2-40d5-967d-eea706fdab57?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/post-process-materials-in-unreal-engine)

[Art Pass for a Puzzle Adventure Game](/documentation/en-us/unreal-engine/art-pass-for-a-puzzle-adventure-game)

[Design a Puzzle Adventure

![Design a Puzzle Adventure](https://dev.epicgames.com/community/api/documentation/image/a7b7ff2c-23d0-47a0-8a04-e569209942b0?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine)
