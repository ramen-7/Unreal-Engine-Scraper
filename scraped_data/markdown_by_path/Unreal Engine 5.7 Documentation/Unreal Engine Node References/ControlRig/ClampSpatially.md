<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ClampSpatially?application_version=5.7 -->

# ClampSpatially

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
7. ClampSpatially

# ClampSpatially

Clamps a transform's position using a plane collision, cylindric collision or spherical collision.

On this page

### Description

Clamps a transform's position using a plane collision, cylindric collision or spherical collision.
Clamps a position using a plane collision, cylindric collision or spherical collision.
The collision happens both towards an inner envelope (minimum) and towards an outer envelope (maximum).
You can disable the inner / outer envelope / collision by setting the minimum / maximum to 0.0.

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | ClampSpatially,Clamp Spatially,Collide,Collision |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input transform to clamp | [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| Axis | The axis to use for the filter | [Axis](/documentation/en-us/unreal-engine/API/Runtime/Core/EAxis__Type) | X |
| Type | The filter / spatial mode to use | [Rig VMClamp Spatial Mode](/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMClampSpatialMode__Type) | Plane |
| Minimum | The minimum allowed distance at which a collision occurs. Note: For capsule this represents the radius. Disable by setting to 0.0. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Maximum | This maximum allowed distance. A collision will occur towards the center at this wall. Note: For capsule this represents the length. Disable by setting to 0.0. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 100.000000 |
| Space | The space this spatial clamp happens within. The input position will be projected into this space. | [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| bDrawDebug | Draws debug information if True | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| DebugColor | The color to use for the debug draw | [Linear Color](/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=0.000000,B=0.000000,A=1.000000) |
| DebugThickness | The thickness to use for the debug draw | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting transform with a clamped position | [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/ClampSpatially?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/ClampSpatially?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/ClampSpatially?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/ClampSpatially?application_version=5.7#outputs)
