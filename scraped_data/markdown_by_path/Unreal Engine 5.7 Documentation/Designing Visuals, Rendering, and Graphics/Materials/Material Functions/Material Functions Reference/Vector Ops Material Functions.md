<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/vector-ops-material-functions-in-unreal-engine?application_version=5.7 -->

# Vector Ops Material Functions

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
9. Vector Ops Material Functions

# Vector Ops Material Functions

Functions built to handle vector mathematics, such as calculating a Fresnel effect.

![Vector Ops Material Functions](https://dev.epicgames.com/community/api/documentation/image/36a17007-8a00-4c02-8347-0472e25166ea?resizing_type=fill&width=1920&height=335)

 On this page

The VectorOps category contains special Material functions for applying various vector-based math equations.

## Fresnel

Unlike the regular Fresnel Material expression node, the Fresnel function allows you to designate your own set of vectors used to calculate the equation, as well as make other adjustments to the blend.

| Item | Description |
| --- | --- |
| Inputs |  |
| **Normal Vector (Vector3)** | The first vector used in the Fresnel operation. Typically, this is the surface normal. |
| **Camera Vector (Vector3)** | The vector of the camera's direction. |
| **Invert Fresnel (StaticBool)** | This inverts the operation, reversing the way normals are calculated to yield results. |
| **Power (Scalar)** | This value controls how quickly color falls off between the core and the edges. |
| **Use Cheap Contrast (StaticBool)** | This activates an internal CheapContrast function to boost the contrast of the Fresnel's result. |
| **Cheap contrast dark (Scalar)** | When using cheap contrast, this controls how much the dark value shows in the result. Has no effect when not using cheap contrast. |
| **Cheap contrast bright (Scalar)** | When using cheap contrast, this controls how much the bright value shows in the result. Has no effect when not using cheap contrast. |
| **Clamp Fresnel Dot Product (B)** | Clamps the result of the Fresnel Dot Product between 0 and 1. This is true by default, but you can override it with a Static Bool set to false. |

![Using a Static Bool to invert the Fresnel effect.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/df4d373d-16b7-44c0-a3cd-e4eefdb74f29/fresnel-function-01.png)
![Using a Static Bool to invert the Fresnel effect.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8c06dfe4-7119-433a-b93f-ba8cfc1a9862/fresnel-function-02.png)

**Using a Static Bool to invert the Fresnel effect.**

* [materials](https://dev.epicgames.com/community/search?query=materials)
* [shaders](https://dev.epicgames.com/community/search?query=shaders)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Fresnel](/documentation/en-us/unreal-engine/vector-ops-material-functions-in-unreal-engine?application_version=5.7#fresnel)
