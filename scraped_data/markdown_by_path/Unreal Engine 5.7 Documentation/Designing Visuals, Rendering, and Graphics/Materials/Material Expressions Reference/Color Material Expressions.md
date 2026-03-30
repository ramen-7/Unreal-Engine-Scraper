<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/color-material-expressions-in-unreal-engine?application_version=5.7 -->

# Color Material Expressions

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
7. [Material Expressions Reference](/documentation/en-us/unreal-engine/unreal-engine-material-expressions-reference "Material Expressions Reference")
8. Color Material Expressions

# Color Material Expressions

Material expressions that perform actions on color inputs.

![Color Material Expressions](https://dev.epicgames.com/community/api/documentation/image/2aad21c8-ec9a-424a-83d4-a4896c3f1309?resizing_type=fill&width=1920&height=335)

 On this page

## Desaturation

The **Desaturation** expression desaturates its input, or converts the colors of its input into shades of gray, based a certain percentage.

| Item | Description |
| --- | --- |
| Properties |  |
| **Luminance Factors** | Specifies the amount that each channel contributes to the desaturated color. This is what controls that green is brighter than red which is brighter than blue when desaturated. |
| Inputs |  |
| **Fraction** | Specifies the amount of desaturation to apply to the input. Percent can range from 0.0(full original color, no desaturation) to 1.0 (fully desaturated). |

![Desaturation Material Expression](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4ad1fbd4-8664-4433-a111-139b49d20aea/desaturation-expression.png)


**Programmers:** Define desaturated color `D`, input color `I` and luminance factor `L`. The output will be `O = (1 - Percent)*( D.dot( I )) + Percent * I`

* [materials](https://dev.epicgames.com/community/search?query=materials)
* [shaders](https://dev.epicgames.com/community/search?query=shaders)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Desaturation](/documentation/en-us/unreal-engine/color-material-expressions-in-unreal-engine?application_version=5.7#desaturation)
