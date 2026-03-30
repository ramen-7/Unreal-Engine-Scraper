<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Cast?application_version=5.7 -->

# Cast

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
7. Cast

# Cast

4 nodes with name Cast

On this page

## Cast ()

Turns the given bool into a float value
Turns the given bool into an integer value
Makes a color from a single float
Makes a color from a single double
Returns the double cast to an int (this uses floor)
Returns the double cast to a float
Returns the float cast to an int (this uses floor)
Returns the float cast to a double
Returns the int cast to a float
Returns the int cast to a double
Makes a transform from a matrix
Makes a matrix from a transform
Makes a quaternion from a rotator
Retrieves the rotator
Makes a quaternion based transform from a euler based transform
Retrieves a euler based transform from a quaternion based transform
Makes a vector from a single float
Makes a vector from a single double
Casts the provided item key to its name

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Tags | Cast,To Float,To Integer,From Float,Make,Construct,From Double,To Int,To Double,To Transform,From Transform,From Rotator,To Rotator,To Euler Transform,To Name,Engine Test Rig VM Custom Type from Int,Engine Test Rig VM Custom Type to Int |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The bool value to convert | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core)   [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Rotator](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Quat](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Matrix](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Euler Transform](/documentation/en-us/unreal-engine/API/Runtime/AnimationCore/FEulerTransform)   [Rig Element Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)   FEngineTest\_CustomType | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting float number (0 or 1) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   double   [int32](/documentation/en-us/unreal-engine/API/Runtime/Core)   [FName](/documentation/en-us/unreal-engine/API/Runtime/Core/FName)   [Rotator](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Quat](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Linear Color](/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor)   [Matrix](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Euler Transform](/documentation/en-us/unreal-engine/API/Runtime/AnimationCore/FEulerTransform)   FEngineTest\_CustomType |  |

## Cast (FRigVMDispatch\_CastEnumToInt)

Casts from enum to int

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Enum |
| Tags | As |
| Type | [FRigVMDispatch\_CastEnumToInt](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_CastEnumToInt) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The enum value to cast to an integer | [Wildcard](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting integer value | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

## Cast (FRigVMDispatch\_CastIntToEnum)

Casts from int to enum

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Enum |
| Tags | As |
| Type | [FRigVMDispatch\_CastIntToEnum](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_CastIntToEnum) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The integer value to cast to an enum value | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting enum value | [Wildcard](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

## Cast (FRigVMDispatch\_CastObject)

Casts between object types

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Object |
| Tags | As |
| Type | [FRigVMDispatch\_CastObject](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMDispatch_CastObject) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The object to cast to a new type | [Wildcard](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting cast object. This may be potentially nullptr as well if the cast was not successful. | [Wildcard](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMUnknownType) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Cast ()](/documentation/en-us/unreal-engine/node-reference/ControlRig/Cast?application_version=5.7#cast())
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/Cast?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/Cast?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/Cast?application_version=5.7#outputs)
* [Cast (FRigVMDispatch\_CastEnumToInt)](/documentation/en-us/unreal-engine/node-reference/ControlRig/Cast?application_version=5.7#cast(frigvmdispatch-castenumtoint))
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/Cast?application_version=5.7#information-2)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/Cast?application_version=5.7#inputs-2)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/Cast?application_version=5.7#outputs-2)
* [Cast (FRigVMDispatch\_CastIntToEnum)](/documentation/en-us/unreal-engine/node-reference/ControlRig/Cast?application_version=5.7#cast(frigvmdispatch-castinttoenum))
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/Cast?application_version=5.7#information-3)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/Cast?application_version=5.7#inputs-3)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/Cast?application_version=5.7#outputs-3)
* [Cast (FRigVMDispatch\_CastObject)](/documentation/en-us/unreal-engine/node-reference/ControlRig/Cast?application_version=5.7#cast(frigvmdispatch-castobject))
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/Cast?application_version=5.7#information-4)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/Cast?application_version=5.7#inputs-4)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/Cast?application_version=5.7#outputs-4)
