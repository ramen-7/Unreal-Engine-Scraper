<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/blend-material-functions-in-unreal-engine?application_version=5.7 -->

# Blend Material Functions

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
7. [Material Functions](/documentation/en-us/unreal-engine/material-functions-in-unreal-engine "Material Functions")
8. [Material Functions Reference](/documentation/en-us/unreal-engine/unreal-engine-material-functions-reference "Material Functions Reference")
9. Blend Material Functions

# Blend Material Functions

Functions designed to blend one color with another, similar to blend modes in popular image editing applications.

![Blend Material Functions](https://dev.epicgames.com/community/api/documentation/image/53fd83b6-61d6-40a8-b9b5-8c2642055302?resizing_type=fill&width=1920&height=335)

 On this page

A **Blend** is a type of function that performs mathematical calculations in the color information of a texture so that one texture can blend into another in a particular manner.

Blends will always have a Base and a Blend input, both of which are Vector3. These will each take in a texture and the two will be blended in some way. The manner in which the blend takes place depends on the type of blend function used.

## Blend Functions

Below is a list of all of the blend material functions.

### Blend\_ColorBurn

**Blend\_ColorBurn** blends the textures in such a way that the darker the Blend color the more of that color will be used in the final result. If the Blend color is white, no change takes place.

| Item | Description |
| --- | --- |
| Inputs |  |
| **Base (Vector3)** | The base, or original texture that will be blended with the Blend texture in some way. |
| **Blend (Vector3)** | The blend texture, which is combined with the base in some way based on the type of blend operation taking place. |

![Color Burn](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c3531572-733b-4d6b-9b9f-aa25da4cc83e/colorburn.png)

|  |  |  |  |
| --- | --- | --- | --- |
|  | Base | Blend | Color Burn Blend |
|  | Base | Blend | Result |

### Blend\_ColorDodge

**Blend\_ColorDodge** lightens the result by inverting the Base color and dividing it by the Blend color.

| Item | Description |
| --- | --- |
| Inputs |  |
| **Base (Vector3)** | The base, or original texture that will be blended with the Blend texture in some way. |
| **Blend (Vector3)** | The blend texture, which is combined with the base in some way based on the type of blend operation taking place. |

![Color Dodge](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b71571b3-406f-4997-835f-d1162116c52f/colordodge.png)

|  |  |  |  |
| --- | --- | --- | --- |
|  | Base | Blend | Color Dodge Blend |
|  | Base | Blend | Result |

### Blend\_Darken

**Blend\_Darken** works by choosing the darker value for each pixel of the Base and Blend colors. A white Blend color does not produce a change.

| Item | Description |
| --- | --- |
| Inputs |  |
| **Base (Vector3)** | The base, or original texture that will be blended with the Blend texture in some way. |
| **Blend (Vector3)** | The blend texture, which is combined with the base in some way based on the type of blend operation taking place. |

![Darken](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a18da62f-17bf-4e23-8c55-0822a9496bb6/darken.png)

|  |  |  |  |
| --- | --- | --- | --- |
|  | Base | Blend | Darken Blend |
|  | Base | Blend | Result |

### Blend\_Difference

**Blend\_Difference** creates a sort of inversion-style effect by subtracting the Base from the Blend and then taking the absolute value of the result.

| Item | Description |
| --- | --- |
| Inputs |  |
| **Base (Vector3)** | The base, or original texture that will be blended with the Blend texture in some way. |
| **Blend (Vector3)** | The blend texture, which is combined with the base in some way based on the type of blend operation taking place. |

![Difference](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8441e338-15b0-407c-a594-499c925e26d5/difference.png)

|  |  |  |  |
| --- | --- | --- | --- |
|  | Base | Blend | Difference Blend |
|  | Base | Blend | Result |

### Blend\_Exclusion

**Blend\_Exclusion** halves both the Base and Blend textures, combines them, and then does a partial inversion on the result.

| Item | Description |
| --- | --- |
| Inputs |  |
| **Base (Vector3)** | The base, or original texture that will be blended with the Blend texture in some way. |
| **Blend (Vector3)** | The blend texture, which is combined with the base in some way based on the type of blend operation taking place. |

![Exclusion](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4393b1df-eacc-4773-a0f2-580aee09437f/exclusion.png)

|  |  |  |  |
| --- | --- | --- | --- |
|  | Base | Blend | Exclusion Blend |
|  | Base | Blend | Result |

### Blend\_HardLight

Like a harsher version of Blend\_Overlay, **Blend\_HardLight** will either screen or multiply the Base and Blend together. The function does a comparison on the Blend color such that wherever the Blend is brighter than 50% gray, the Base and Blend will be combined via a Screen operation. If the Blend is darker than 50% gray, the Base will be multiplied by the Blend as in the Multiply function. The contrast of the final result is then boosted for a harsh output.

| Item | Description |
| --- | --- |
| Inputs |  |
| **Base (Vector3)** | The base, or original texture that will be blended with the Blend texture in some way. |
| **Blend (Vector3)** | The blend texture, which is combined with the base in some way based on the type of blend operation taking place. |

![Hard Light](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/70afc8e9-6deb-49a4-8061-6d7ef467fff5/hardlight.png)

|  |  |  |  |
| --- | --- | --- | --- |
|  | Base | Blend | Hard Light Blend |
|  | Base | Blend | Result |

### Blend\_Lighten

**Blend\_Lighten** compares each pixel of the Base and Blend colors and returns the brighter result.

| Item | Description |
| --- | --- |
| Inputs |  |
| **Base (Vector3)** | The base, or original texture that will be blended with the Blend texture in some way. |
| **Blend (Vector3)** | The blend texture, which is combined with the base in some way based on the type of blend operation taking place. |

![Lighten](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/15ad0ab6-8977-4e43-b28d-ba07f4a36511/lighten.png)

|  |  |  |  |
| --- | --- | --- | --- |
|  | Base | Blend | Lighten Blend |
|  | Base | Blend | Result |

### Blend\_LinearBurn

**Blend\_LinearBurn** adds Base color to the Blend color and then subtracts 1 from the result.

| Item | Description |
| --- | --- |
| Inputs |  |
| **Base (Vector3)** | The base, or original texture that will be blended with the Blend texture in some way. |
| **Blend (Vector3)** | The blend texture, which is combined with the base in some way based on the type of blend operation taking place. |

![Linear Burn](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9a082f7c-53a9-40a0-bcd7-823eb2ddae58/linearburn.png)

|  |  |  |  |
| --- | --- | --- | --- |
|  | Base | Blend | Linear Burn Blend |
|  | Base | Blend | Result |

### Blend\_LinearDodge

**Blend\_LinearDodge** adds the Base color to the Blend color.

| Item | Description |
| --- | --- |
| Inputs |  |
| **Base (Vector3)** | The base, or original texture that will be blended with the Blend texture in some way. |
| **Blend (Vector3)** | The blend texture, which is combined with the base in some way based on the type of blend operation taking place. |

![Linear Dodge](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/827e22d5-c3e8-4747-848c-db35b6741411/lineardodge.png)

|  |  |  |  |
| --- | --- | --- | --- |
|  | Base | Blend | Linear Dodge Blend |
|  | Base | Blend | Result |

### Blend\_LinearLight

**Blend\_LinearLight** is a linear version of Blend\_Overlay, providing harsher results. The function does a comparison on the Blend color such that wherever the Blend is brighter than 50% gray, the Base and Blend will be combined via a Screen operation. If the Blend is darker than 50% gray, the Base will be multiplied by the Blend as in the Multiply function.

| Item | Description |
| --- | --- |
| Inputs |  |
| **Base (Vector3)** | The base, or original texture that will be blended with the Blend texture in some way. |
| **Blend (Vector3)** | The blend texture, which is combined with the base in some way based on the type of blend operation taking place. |

![Linear Light](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/690570e4-f15d-4361-9846-c1db89403711/linearlight.png)

|  |  |  |  |
| --- | --- | --- | --- |
|  | Base | Blend | Linear Light Blend |
|  | Base | Blend | Result |

### Blend\_Overlay

**Blend\_Overlay** will either screen or multiply the Base and Blend together. The function does a comparison on the Blend color such that wherever the Blend is brighter than 50% gray, the Base and Blend will be combined via a Screen operation. If the Blend is darker than 50% gray, the Base will be multiplied by the Blend as in the Multiply function.

| Item | Description |
| --- | --- |
| Inputs |  |
| **Base (Vector3)** | The base, or original texture that will be blended with the Blend texture in some way. |
| **Blend (Vector3)** | The blend texture, which is combined with the base in some way based on the type of blend operation taking place. |

![Overlay](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3179dc78-265a-4667-b2e8-3da645a5c5d6/overlay.png)

|  |  |  |  |
| --- | --- | --- | --- |
|  | Base | Blend | Overlay Blend |
|  | Base | Blend | Result |

### Blend\_PinLight

Like Blend\_Overlay, **Blend\_PinLight** will either lighten or darken the Base and Blend together. The function does a comparison on the Blend color such that wherever the Blend is brighter than 50% gray, the Base and Blend will be combined via a Screen operation. If the Blend is darker than 50% gray, the Base will be multiplied by the Blend as in the Multiply function. The contrast is softened, making this a less harsh version of Overlay.

| Item | Description |
| --- | --- |
| Inputs |  |
| **Base (Vector3)** | The base, or original texture that will be blended with the Blend texture in some way. |
| **Blend (Vector3)** | The blend texture, which is combined with the base in some way based on the type of blend operation taking place. |

![Pin Light](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5b1b0271-f33e-4baf-9177-17fde3a42069/pinlight.png)

|  |  |  |  |
| --- | --- | --- | --- |
|  | Base | Blend | Pin Light Blend |
|  | Base | Blend | Result |

### Blend\_Screen

**Blend\_Screen** lightens the Base by the Blend color. It does this by doing a "one minus" on both colors, multiplying them together, and taking a one-minus of the result.

| Item | Description |
| --- | --- |
| Inputs |  |
| **Base (Vector3)** | The base, or original texture that will be blended with the Blend texture in some way. |
| **Blend (Vector3)** | The blend texture, which is combined with the base in some way based on the type of blend operation taking place. |

![Screen](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8c2d9dd2-1899-4be6-a0c9-1a7526e45f08/screen.png)

|  |  |  |  |
| --- | --- | --- | --- |
|  | Base | Blend | Screen Blend |
|  | Base | Blend | Result |

### Blend\_SoftLight

**Blend\_SoftLight** is a softer version of Overlay. The function does a comparison on the Blend color such that wherever the Blend is brighter than 50% gray, the Base and Blend will be combined via a Screen operation. If the Blend is darker than 50% gray, the Base will be multiplied by the Blend as in the Multiply function. The contrast is softened, making this a less harsh version of Overlay.

| Item | Description |
| --- | --- |
| Inputs |  |
| **Base (Vector3)** | The base, or original texture that will be blended with the Blend texture in some way. |
| **Blend (Vector3)** | The blend texture, which is combined with the base in some way based on the type of blend operation taking place. |

![Soft Light](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9b8ac455-e7c6-417e-86d6-3b35206c7fd8/softlight.png)

|  |  |  |  |
| --- | --- | --- | --- |
|  | Base | Blend | Soft Light Blend |
|  | Base | Blend | Result |

* [materials](https://dev.epicgames.com/community/search?query=materials)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Blend Functions](/documentation/en-us/unreal-engine/blend-material-functions-in-unreal-engine?application_version=5.7#blendfunctions)
* [Blend\_ColorBurn](/documentation/en-us/unreal-engine/blend-material-functions-in-unreal-engine?application_version=5.7#blend-colorburn)
* [Blend\_ColorDodge](/documentation/en-us/unreal-engine/blend-material-functions-in-unreal-engine?application_version=5.7#blend-colordodge)
* [Blend\_Darken](/documentation/en-us/unreal-engine/blend-material-functions-in-unreal-engine?application_version=5.7#blend-darken)
* [Blend\_Difference](/documentation/en-us/unreal-engine/blend-material-functions-in-unreal-engine?application_version=5.7#blend-difference)
* [Blend\_Exclusion](/documentation/en-us/unreal-engine/blend-material-functions-in-unreal-engine?application_version=5.7#blend-exclusion)
* [Blend\_HardLight](/documentation/en-us/unreal-engine/blend-material-functions-in-unreal-engine?application_version=5.7#blend-hardlight)
* [Blend\_Lighten](/documentation/en-us/unreal-engine/blend-material-functions-in-unreal-engine?application_version=5.7#blend-lighten)
* [Blend\_LinearBurn](/documentation/en-us/unreal-engine/blend-material-functions-in-unreal-engine?application_version=5.7#blend-linearburn)
* [Blend\_LinearDodge](/documentation/en-us/unreal-engine/blend-material-functions-in-unreal-engine?application_version=5.7#blend-lineardodge)
* [Blend\_LinearLight](/documentation/en-us/unreal-engine/blend-material-functions-in-unreal-engine?application_version=5.7#blend-linearlight)
* [Blend\_Overlay](/documentation/en-us/unreal-engine/blend-material-functions-in-unreal-engine?application_version=5.7#blend-overlay)
* [Blend\_PinLight](/documentation/en-us/unreal-engine/blend-material-functions-in-unreal-engine?application_version=5.7#blend-pinlight)
* [Blend\_Screen](/documentation/en-us/unreal-engine/blend-material-functions-in-unreal-engine?application_version=5.7#blend-screen)
* [Blend\_SoftLight](/documentation/en-us/unreal-engine/blend-material-functions-in-unreal-engine?application_version=5.7#blend-softlight)
