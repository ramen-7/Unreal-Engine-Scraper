<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawSpline?application_version=5.7 -->

# Draw Spline

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
5. [Unreal Engine Node References](/documentation/en-us/unreal-engine/node-reference "Unreal Engine Node References")
6. [ControlRig](/documentation/en-us/unreal-engine/node-reference/ControlRig "ControlRig")
7. Draw Spline

# Draw Spline

Draws the given spline in the viewport

On this page

### Description

Draws the given spline in the viewport

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigSpline](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigSpline) |
| Category | Splines |
| Type | [FRigUnit\_DrawControlRigSpline](/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FRigUnit_DrawControlRigSpline) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Spline | The spline to draw | [Control Rig Spline](/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FControlRigSpline) | () |
| Color | The color to use for the debug draw | [Linear Color](/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=0.000000,B=0.000000,A=1.000000) |
| Thickness | The line thickness to use when drawing the spline | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| Detail | The detail to use to render the spline | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 16 |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawSpline?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawSpline?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawSpline?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/DrawSpline?application_version=5.7#inputs)
