<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetCollectionAttributeDataTyped?application_version=5.7 -->

# SetCollectionAttributeDataTyped

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
7. SetCollectionAttributeDataTyped

# SetCollectionAttributeDataTyped

SetCollectionAttributeDataTyped (v1)

On this page

### Description

SetCollectionAttributeDataTyped (v1)

Set attribute data in a Collection

Input(s) :
Collection [Intrinsic] - Collection for the custom attribute
AttributeKey - Input to drive the Attribute and Group name
BoolAttributeData - Bool type attribute data
FloatAttributeData - Float type attribute data
DoubleAttributeData - Float type attribute data
Int32AttributeData - Int type attribute data
StringAttributeData - Int type attribute data
Vector3fAttributeData - Vector3f type attribute data
Vector3dAttributeData - Vector3d type attribute data
LinearColorAttributeData - LinearColor type attribute data

Output(s):
Collection [Passthrough] - Collection for the custom attribute

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FSetCollectionAttributeDataTypedDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FSetCollectionAttributeDataTyped-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| GroupName | Standard group names | [EStandardGroupNameEnum](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/EStandardGroupNameEnum) | Dataflow\_EStandardGroupNameEnum\_Transform |
| CustomGroupName | User specified group name | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |
| AttrName | Attribute name | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection for the custom attribute | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| AttributeKey | Input to drive the Attribute and Group name | [FCollectionAttributeKey](/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="") |
| BoolAttributeData | Bool type attribute data | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[bool](/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| FloatAttributeData | Float type attribute data | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)> |  |
| DoubleAttributeData | Float type attribute data | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray) |  |
| Int32AttributeData | Int type attribute data | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| StringAttributeData | Int type attribute data | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString)> |  |
| Vector3fAttributeData | Vector3f type attribute data | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector3f](/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| Vector3dAttributeData | Vector3d type attribute data | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector3d](/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| LinearColorAttributeData | LinearColor type attribute data | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FLinearColor](/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor)> |  |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Collection for the custom attribute | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetCollectionAttributeDataTyped?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetCollectionAttributeDataTyped?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetCollectionAttributeDataTyped?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetCollectionAttributeDataTyped?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetCollectionAttributeDataTyped?application_version=5.7#outputs)
