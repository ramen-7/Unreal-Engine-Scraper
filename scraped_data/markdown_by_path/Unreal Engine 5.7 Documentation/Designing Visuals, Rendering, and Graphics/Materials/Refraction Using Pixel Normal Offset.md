<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/refraction-using-pixel-normal-offset-in-unreal-engine?application_version=5.7 -->

# Refraction Using Pixel Normal Offset

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
7. Refraction Using Pixel Normal Offset

# Refraction Using Pixel Normal Offset

Overview of the Refraction Mode for Pixel Normal Offset in your Materials.

![Refraction Using Pixel Normal Offset](https://dev.epicgames.com/community/api/documentation/image/c09157c6-e538-4149-a9ef-ac8a7e079242?resizing_type=fill&width=1920&height=335)

 On this page

By default, Unreal Engine uses a physically based refraction model derived from **Index of Refraction** values. The physical **Index of Refraction** model mimics the way light rays refract as they transfer between mediums. This works well for small objects, like jars, glasses, and other curved surfaces. However, when used with large flat surfaces it can produce unpredictable results and artifacts as the scene color is being read from off screen.

**Pixel Normal Offset** is an alternative Refraction Mode available in the [Material Editor](/documentation/en-us/unreal-engine/unreal-engine-material-editor-user-guide). It uses the vertex normal as a reference and then computes the refraction offset by calculating how different the per-pixel normal is from the vertex normal. This is useful for large flat surfaces, like water, where you do not want a constant offset that is reading data from off screen.

## Physical vs Non-Physical Refraction Model

You can change the **Refraction Mode** of your Material in the Details Panel. Scroll down and expand the **Refraction** section, and then choose between the two options in the Refraction Mode drop-down. All Materials use **Index of Refraction** by default.

For additional information about the physical model of refraction, and how to use it in your Materials, you can read the page on [Using Refraction](/documentation/en-us/unreal-engine/using-refraction-in-unreal-engine).

|  |  |
| --- | --- |
|  |  |
| Physical Refraction Model: Index of Refraction | Non-Physical Refraction Model: Pixel Normal Offset |

The comparisons below demonstrate the differences in how the normal is read in the Material when the Refraction Mode is changed from **Index of Refraction** to **Pixel Normal Offset.**

![Refraction Mode: Index of Refraction without Normal Map](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6a19cab2-4763-4e0f-8266-944aab3352f5/ior_withoutnormals.png)

![Refraction Mode: Pixel Normal Offset without Normal Map](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a594a3eb-fdc1-4418-82fb-1642c9a298df/pno_withoutnormals.png)

Refraction Mode: Index of Refraction without Normal Map

Refraction Mode: Pixel Normal Offset without Normal Map

Above you will notice that the image is shifted when using the **Index of Refraction** mode compared to the **Pixel Normal Offset** mode where you do not read from off screen so much. Note that **Index of
Refraction** will work without a Normal map plugged into the Material, whereas with **Pixel Normal Offset**, if there is no Normal map you will not get any refraction.

![Refraction Mode: Index of Refraction with Normal Map](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a1f0143c-5a07-47bc-b8c2-950c53ebb616/ior_withnormals.png)

![Refraction Mode: Pixel Normal Offset with Normal Map](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/aef32af9-3225-470e-974c-7813f491f628/pno_withnormals.png)

Refraction Mode: Index of Refraction with Normal Map

Refraction Mode: Pixel Normal Offset with Normal Map

When you add a Normal map to your Material with a value greater than 1 plugged into the Refraction input, the normal will translate along the surface when using **Pixel Normal Offset**.
However, you will notice that with **Index of Refraction**, you will still have an offset that reads from off screen, which is not a desirable effect for flat surfaces using refraction.

### Final Result

In this example, the refraction amount is adjusted between a value of 1.0, which is no refraction at all, to a value of 2.0, for some refraction along the surface without shifting the image while using
**Pixel Normal Offset**.

## Pixel Normal Offset and Glass

Pixel Normal Offset is also beneficial for large flat glass surfaces, such as the windows in the cafe scene below. The first image in the slider uses the default **Index of Refraction** setting. The window refraction is chaotic and contains an artifact in the bottom right corner. When the refraction mode is changed to **Pixel Normal Offset,** the windows appear much more true to life and the artifact disappears.

![Move the slider to see how the glass changes when the Refraction Mode is changed from Index of Refraction (image 1) to Pixel Normal Offset (image 2).](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/205714df-3219-4e35-8846-971172b25a12/bistro-glass-ior.png)
![Move the slider to see how the glass changes when the Refraction Mode is changed from Index of Refraction (image 1) to Pixel Normal Offset (image 2).](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d4c47528-f8c0-4c36-abcd-8f95f0fcf53b/bistro-glass-pixel-normal-offset.png)

**Move the slider to see how the glass changes when the Refraction Mode is changed from Index of Refraction (image 1) to Pixel Normal Offset (image 2).**

In **Pixel Normal Offset** mode, the refraction in this example is extremely slight because the normal map for this glass only contains micro abrasions and minor surface imperfections. This is an expected result for clean architectural glass.

However if you wanted a textured or patterned glass effect you could use a more representative normal map and raise the **Refraction** value to something around **1.52**.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/502112f5-7dcf-4565-99d4-ed9edc25d97b/textured-glass-graph.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/502112f5-7dcf-4565-99d4-ed9edc25d97b/textured-glass-graph.png)

This is how the normal map affects the refraction in the glass windows.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6325c015-d671-42aa-a356-2cd24f1ca906/textured-glass.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6325c015-d671-42aa-a356-2cd24f1ca906/textured-glass.png)

* [materials](https://dev.epicgames.com/community/search?query=materials)
* [rendering](https://dev.epicgames.com/community/search?query=rendering)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Physical vs Non-Physical Refraction Model](/documentation/en-us/unreal-engine/refraction-using-pixel-normal-offset-in-unreal-engine?application_version=5.7#physicalvsnon-physicalrefractionmodel)
* [Final Result](/documentation/en-us/unreal-engine/refraction-using-pixel-normal-offset-in-unreal-engine?application_version=5.7#finalresult)
* [Pixel Normal Offset and Glass](/documentation/en-us/unreal-engine/refraction-using-pixel-normal-offset-in-unreal-engine?application_version=5.7#pixelnormaloffsetandglass)

Related documents

[Using Refraction

![Using Refraction](https://dev.epicgames.com/community/api/documentation/image/8f6a4934-a39e-4bc0-b071-c319725cb4c6?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/using-refraction-in-unreal-engine)
