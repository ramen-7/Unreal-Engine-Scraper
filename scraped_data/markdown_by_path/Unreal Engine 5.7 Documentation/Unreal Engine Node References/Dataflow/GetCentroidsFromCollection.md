<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetCentroidsFromCollection?application_version=5.7 -->

# GetCentroidsFromCollection

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
7. GetCentroidsFromCollection

# GetCentroidsFromCollection

GetCentroidsFromCollection (v1)

On this page

### Description

GetCentroidsFromCollection (v1)

Gets centroids of pieces from a Collection

Input(s) :
Collection - Input Collection
TransformSelection - The centroids will be output for the bones selected in the TransformSelection

Output(s):
Centroids - Output centroids
Levels - Hidden output to store computed level values for centroids

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FGetCentroidsFromCollectionDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGetCentroidsFromCollectionDataf-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bColorByLevel | Control point color by level or setting | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| Color | Point color | [FLinearColor](/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=0.000000,G=0.000000,B=1.000000,A=1.000000) |
| bSizeByLevel | Control the point size by level or setting | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| Size | Point size | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 8.000000 |
| PointSize | Float curve to control point size by level | [FRuntimeFloatCurve](/documentation/en-us/unreal-engine/API/Runtime/Engine/FRuntimeFloatCurve) | (EditorCurveData=(Keys=((Value=12.000000),(Time=1.000000,Value=6.000000)),DefaultValue=340282346638528859811704183484516925440.000000,PreInfinityExtrap=RCCE\_Constant,PostInfinityExtrap=RCCE\_Constant),ExternalCurve=None) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Input Collection | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | The centroids will be output for the bones selected in the TransformSelection | [FDataflowTransformSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Centroids | Output centroids | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FVector](/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |
| Levels | Hidden output to store computed level values for centroids | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[int32](/documentation/en-us/unreal-engine/API/Runtime/Core)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetCentroidsFromCollection?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetCentroidsFromCollection?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetCentroidsFromCollection?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetCentroidsFromCollection?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetCentroidsFromCollection?application_version=5.7#outputs)
