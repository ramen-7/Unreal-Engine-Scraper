<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ToVectors?application_version=5.7 -->

# To Vectors

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
7. To Vectors

# To Vectors

2 nodes with name To Vectors

On this page

## To Vectors (FRigVMFunction\_MathMatrixToVectors)

Converts the matrix to its vectors

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Matrix |
| Tags | Make,Construct |
| Type | [FRigVMFunction\_MathMatrixToVectors](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathMatrixToVecto-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The matrix to split up to vectors | [Matrix](/documentation/en-us/unreal-engine/API/Runtime/Core) | (XPlane=(W=0.000000,X=1.000000,Y=0.000000,Z=0.000000),YPlane=(W=0.000000,X=0.000000,Y=1.000000,Z=0.000000),ZPlane=(W=0.000000,X=0.000000,Y=0.000000,Z=1.000000),WPlane=(W=1.000000,X=0.000000,Y=0.000000,Z=0.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Origin | The resulting origin | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| X | The resulting X component | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Y | The resulting Y component | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Z | The resulting Z component | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

## To Vectors ()

Retrieves the forward, right and up vectors of a quaternion
Retrieves the forward, right and up vectors of a transform's quaternion

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math |
| Tags | ToVectors,To Vectors,Forward,Right,Up |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Value | The input quaternion | [Quat](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000,W=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Forward | The forward axis of the quaternion | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Right | The right axis of the quaternion | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Up | The up axis of the quaternion | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [To Vectors (FRigVMFunction\_MathMatrixToVectors)](/documentation/en-us/unreal-engine/node-reference/ControlRig/ToVectors?application_version=5.7#tovectors(frigvmfunction-mathmatrixtovectors))
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/ToVectors?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/ToVectors?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/ToVectors?application_version=5.7#outputs)
* [To Vectors ()](/documentation/en-us/unreal-engine/node-reference/ControlRig/ToVectors?application_version=5.7#tovectors())
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/ToVectors?application_version=5.7#information-2)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/ToVectors?application_version=5.7#inputs-2)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/ToVectors?application_version=5.7#outputs-2)
