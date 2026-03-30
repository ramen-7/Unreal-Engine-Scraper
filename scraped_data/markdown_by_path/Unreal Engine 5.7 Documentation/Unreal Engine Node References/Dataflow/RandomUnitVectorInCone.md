<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/RandomUnitVectorInCone?application_version=5.7 -->

# RandomUnitVectorInCone

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
7. RandomUnitVectorInCone

# RandomUnitVectorInCone

RandomUnitVectorInCone (v1)

On this page

### Description

RandomUnitVectorInCone (v1)

Returns a random vector with length of 1, within the specified cone, with uniform random distribution

Input(s) :
ConeDirection - The base "center" direction of the cone
ConeHalfAngle - The half-angle of the cone (from ConeDir to edge), in degrees

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Math|Random |
| Type | [FRandomUnitVectorInConeDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FRandomUnitVectorInConeDataflowN-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bDeterministic |  | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| RandomSeed |  | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | -56694.234375 |
| ConeDirection | The base "center" direction of the cone | [FVector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |
| ConeHalfAngle | The half-angle of the cone (from ConeDir to edge), in degrees | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.785398 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ReturnValue |  | [FVector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/RandomUnitVectorInCone?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/RandomUnitVectorInCone?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/RandomUnitVectorInCone?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/RandomUnitVectorInCone?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/RandomUnitVectorInCone?application_version=5.7#outputs)
