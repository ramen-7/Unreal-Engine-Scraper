<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BreakTransform?application_version=5.7 -->

# BreakTransform

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
6. [Dataflow](/documentation/en-us/unreal-engine/node-reference/Dataflow "Dataflow")
7. BreakTransform

# BreakTransform

BreakTransform (v1)

On this page

### Description

BreakTransform (v1)

Break a Transform into Translation, Rotation (Euler, Rotator, Quaternion), Scale

Input(s) :
Transform - Transform to break into components

Output(s):
Translation - Translation
Rotation - Rotation as Euler
Rotator - Rotation as a rotator
Quat - Rotation as a quaternion
Scale - Scale

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Transform |
| Type | [FBreakTransformDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FBreakTransformDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform | Transform to break into components | [FTransform](/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Translation | Translation | [FDataflowVectorTypes](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) |  |
| Rotation | Rotation as Euler | [FVector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Rotator | Rotation as a rotator | [FRotator](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Quat | Rotation as a quaternion | [FQuat](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Scale | Scale | [FDataflowVectorTypes](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVectorTypes) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/BreakTransform?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/BreakTransform?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/BreakTransform?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/BreakTransform?application_version=5.7#outputs)
