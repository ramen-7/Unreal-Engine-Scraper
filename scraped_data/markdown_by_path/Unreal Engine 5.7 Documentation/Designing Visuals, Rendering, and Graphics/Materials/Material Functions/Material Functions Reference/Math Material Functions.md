<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/math-material-functions-in-unreal-engine?application_version=5.7 -->

# Math Material Functions

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
9. Math Material Functions

# Math Material Functions

Material Functions which perform preconfigured mathematical operations such as the calculation of pi, addition of vector components, and others.

![Math Material Functions](https://dev.epicgames.com/community/api/documentation/image/8b2b0dd1-0ed9-4013-b4ec-7f1e2c998f69?resizing_type=fill&width=1920&height=335)

 On this page

Math functions perform basic math equations on the values of pixels within a Material network.

## Add Components

The **AddComponents** function takes in a Vector2, a Vector3, or a Vector4, combines their components together and then outputs the result. You must use the appropriate output for the corresponding input. For example, if you input an image into *f3 (Vector3)*, then you must use the *f3* output.

| Item | Description |
| --- | --- |
| Inputs |  |
| **f2 (Vector2)** | Takes in a Vector2 value so that its components can be added together and sent to the *f2* output. |
| **f3 (Vector3)** | Takes in a Vector3 value so that its components can be added together and sent to the *f3* output. |
| **f4 (Vector4)** | Takes in a Vector4 value so that its components can be added together and sent to the *f4* output. |
| Outputs |  |
| **f2 (Vector2)** | Outputs the combined value of the components from the *f2* input. |
| **f3 (Vector3)** | Outputs the combined value of the components from the *f3* input. |
| **f4 (Vector4)** | Outputs the combined value of the components from the *f4* input. |

![Add Components](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/70823f81-3266-497e-89fb-4842c2fd509c/add-components.png)


Since each input is calculated individually for its corresponding output, you may use all three inputs on a single node, so long as you also use an output for each one. For instance, you may use one AddComponents function node to combine the components of a Vector2, utilizing the *f2* output, and use the same node to combine the components of a Vector3, utilizing the *f3* output.

## Pi

The **Pi** function serves as a constant for Pi, as calculated to the 6th decimal place (3.141592). The node also comes with an input for a multiplier.

| Inputs | Description |
| --- | --- |
| **Multiplier (Scalar)** | Input a value that will be multiplied times pi. |

![Pi](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2384008b-a7dc-4967-a602-4d4a89da50c9/pi-function.png)

## LinearSine

The **LinearSine** function takes in a scalar value and outputs the linear sine (or rounded linear sine) of that value, running between 0 and 1. If you connect a Time expression to the value input and use the Linear Sine, you can see animation in the output that coincides with a linear sine wave.

| Item | Description |
| --- | --- |
| Inputs |  |
| **Value** (Scalar) | This is the incoming value to which the linear sine function will be applied. If this value changes over time, the output will be a wave. |
| **Period** (Scalar) | Period controls the time required to make one full transition. Input values higher than 1 to slow the wave down. |
| **-1 to 1** (StaticBool) | Setting this to *true* scales and offsets the wave to run between -1 and 1, rather than 0-1. |
| **Sine Phase** (StaticBool) | Setting this *true* will output normal sine behavior rather than linear behavior. |
| Outputs |  |
| **Linear Sine** | This outputs a linear sine wave. |
| **Rounded Linear Sine** | Outputs a linear sine with rounded edges. |
| **Direction** | Outputs 0 or 1, depending on whether the sine wave is traveling downward (0) or upward (1). |

## VectorToRadialValue

The **VectorToRadialValue** function transforms the vector of a Vector2 into an angle, or transforms UV coordinate data into radial coordinates. In the case of a vector, the angle will output in one channel and the length of the vector in the other.

| Item | Description |
| --- | --- |
| Inputs |  |
| **Vector or UVs (Vector2)** | Takes in either a Vector2 or a set of UV coordinates. |
| **Swizzle Coordinate Output (StaticBool)** | Flips the U and V components of the output. |
| Outputs |  |
| **Radial Coordinates** | Returns the radial coordinates of the input. In the case of a vector, the angle is on one channel and the distance is on the other. |
| **Vector Converted to Angle** | Returns the angle of the input vector or a radial gradient in the case of UVs. |
| **Linear Distance** | Returns the linear length of the input vector, or in the case of UVs, outputs a radial gradient of distances. |

![Vector To Radial Value](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cfb30aa9-0b8b-4dff-8380-2de2b0e2d230/vector-to-radial.png)

* [materials](https://dev.epicgames.com/community/search?query=materials)
* [shaders](https://dev.epicgames.com/community/search?query=shaders)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Add Components](/documentation/en-us/unreal-engine/math-material-functions-in-unreal-engine?application_version=5.7#addcomponents)
* [Pi](/documentation/en-us/unreal-engine/math-material-functions-in-unreal-engine?application_version=5.7#pi)
* [LinearSine](/documentation/en-us/unreal-engine/math-material-functions-in-unreal-engine?application_version=5.7#linearsine)
* [VectorToRadialValue](/documentation/en-us/unreal-engine/math-material-functions-in-unreal-engine?application_version=5.7#vectortoradialvalue)
