<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/material-function-expressions-in-unreal-engine?application_version=5.7 -->

# Material Function Expressions

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
8. Material Function Expressions

# Material Function Expressions

Material expressions that are used to create or execute Materials Functions.

![Material Function Expressions](https://dev.epicgames.com/community/api/documentation/image/6fc56e30-7eb9-45e6-98be-2d3cb6669af4?resizing_type=fill&width=1920&height=335)

 On this page

## FunctionInput

The **FunctionInput** expression can only be placed in a material function, where it defines one of the function's inputs.

| Item | Description |
| --- | --- |
| Properties |  |
| **Input Name** | The input's name, which will be displayed on MaterialFunctionCall expressions that use the material function containing the input. |
| **Description** | A description of the input, which will be displayed as a 'tooltip' when the connector for this input on a MaterialFunction Call expression is hovered over with the mouse. |
| **Input Type** | The type of data this input expects. Data passed to this input will be cast to this type, throwing a compiler error if the cast fails because the data is not compatible. |
| **Preview Value** | The value to use as a preview for this input when editing the material function containing it. |
| **Use Preview Value As Default** | If enabled, **Preview Value** will be used as the default value for this input if no data is passed in. |
| **Sort Priority** | Specifies the priority for this input to use when determining the order of the inputs to be displayed on a MaterialFunctionCall expression. |

This node is used with [Material Functions](/documentation/en-us/unreal-engine/material-functions-in-unreal-engine).

## FunctionOutput

The **FunctionOutput** expression can only be placed in a material function, where it defines one of the function's outputs.

| Item | Description |
| --- | --- |
| Properties |  |
| **Output Name** | The output's name, which will be displayed on MaterialFunctionCall expressions that use the material function containing the output. |
| **Description** | A description of the output, which will be displayed as a tooltip when the connector for this output on a MaterialFunction Call expression is hovered over with the mouse. |
| **Sort Priority** | Specifies the priority for this output to use when determining the order of the outputs to be displayed on a MaterialFunctionCall expression. |

This node is used with [Material Functions](/documentation/en-us/unreal-engine/material-functions-in-unreal-engine).

## MaterialFunctionCall

The **MaterialFunctionCall** expression allows you to use an external [Material Function](/documentation/en-us/unreal-engine/material-functions-in-unreal-engine) from another material or function. The external function's input and output nodes become inputs and outputs of the function call node. If a MaterialFunction is selected in the **Content Browser** when placing one of these expressions, it will automatically be assigned.

**Shortcut:** *F + Left Mouse Click*

| Item | Description |
| --- | --- |
| Properties |  |
| **Material Function** | Specifies the [Material Function](/documentation/en-us/unreal-engine/material-functions-in-unreal-engine) to be used. |

This node is used with [Material Functions](/documentation/en-us/unreal-engine/material-functions-in-unreal-engine).

## StaticBool

The **StaticBool** expression is used to provide a default bool value for a static bool function input within a function. This node does not switch between anything, so it must be used in conjunction with a StaticSwitch node.

| Item | Description |
| --- | --- |
| Properties |  |
| **Value** | The value of the bool, *True* (checked) or *False*. |

This node is used with [Material Functions](/documentation/en-us/unreal-engine/material-functions-in-unreal-engine).

## StaticSwitch

The **StaticSwitch** expression works like a StaticSwitchParameter, except that it only implements the switch and does not create a parameter.

| Item | Description |
| --- | --- |
| Properties |  |
| **Default Value** | The default bool value of the parameter that determines which input is active, *True* (checked) or *False*. |
| Inputs |  |
| **True** | The input that is used when the **Value** of the switch is *True*. |
| **False** | The input that is used when the **Value** of the switch is *False*. |
| **Value** | Takes in a bool value that determines which input is active. |

This node is used with [Material Functions](/documentation/en-us/unreal-engine/material-functions-in-unreal-engine).

## TextureObject

The **TextureObject** expression is used to provide a default texture for a texture function input within a function. This node does not actually sample the texture, so it must be used in conjunction with a TextureSample node.

| Item | Description |
| --- | --- |
| Properties |  |
| **Texture** | The texture from the **Content Browser** that will be applied to this node. |
| **Sampler Type** | The type of data that will be output from the node. |

* [materials](https://dev.epicgames.com/community/search?query=materials)
* [shaders](https://dev.epicgames.com/community/search?query=shaders)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [FunctionInput](/documentation/en-us/unreal-engine/material-function-expressions-in-unreal-engine?application_version=5.7#functioninput)
* [FunctionOutput](/documentation/en-us/unreal-engine/material-function-expressions-in-unreal-engine?application_version=5.7#functionoutput)
* [MaterialFunctionCall](/documentation/en-us/unreal-engine/material-function-expressions-in-unreal-engine?application_version=5.7#materialfunctioncall)
* [StaticBool](/documentation/en-us/unreal-engine/material-function-expressions-in-unreal-engine?application_version=5.7#staticbool)
* [StaticSwitch](/documentation/en-us/unreal-engine/material-function-expressions-in-unreal-engine?application_version=5.7#staticswitch)
* [TextureObject](/documentation/en-us/unreal-engine/material-function-expressions-in-unreal-engine?application_version=5.7#textureobject)
