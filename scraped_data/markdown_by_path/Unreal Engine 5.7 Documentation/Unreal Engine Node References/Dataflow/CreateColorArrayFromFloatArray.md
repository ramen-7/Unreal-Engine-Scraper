<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateColorArrayFromFloatArray?application_version=5.7 -->

# CreateColorArrayFromFloatArray

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
7. CreateColorArrayFromFloatArray

# CreateColorArrayFromFloatArray

CreateColorArrayFromFloatArray (v1)

On this page

### Description

CreateColorArrayFromFloatArray (v1)

Set the vertex color on the collection based on the normalized float array.

Input(s) :
FloatArray - Float array to use as a scalar for the color

Output(s):
ColorArray - Color array output

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Collection|Utilities |
| Type | [FCreateColorArrayFromFloatArrayDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCreateColorArrayFromFloatArrayD-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bNormalizeInput | Enable normalization of input array | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| Color | Base color for the normalized float array | [FLinearColor](/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=1.000000,G=1.000000,B=1.000000,A=1.000000) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FloatArray | Float array to use as a scalar for the color | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ColorArray | Color array output | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FLinearColor](/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateColorArrayFromFloatArray?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateColorArrayFromFloatArray?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateColorArrayFromFloatArray?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateColorArrayFromFloatArray?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateColorArrayFromFloatArray?application_version=5.7#outputs)
