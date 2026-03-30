<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateCurveGeometry?application_version=5.7 -->

# GenerateCurveGeometry

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
7. GenerateCurveGeometry

# GenerateCurveGeometry

GenerateCurveGeometry (v1)

On this page

### Description

GenerateCurveGeometry (v1)
Experimental

Build the curve geometry from a collection containing curves

Input(s) :
Collection - Managed array collection to be used to store datas
SourceCurves - Managed array collection to be used to store datas
CurveSelection - Curve selection to focus the curves generation spatially
CurveCount - Max number of guides

Output(s):
Collection [Passthrough] - Managed array collection to be used to store datas

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Category | Groom |
| Type | [FGenerateCurveGeometryDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow/FGenerateCurveGeometryDataflowNo-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bMergeCurves | Flag to check if we can merge guides or not | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| SourceCurves | Managed array collection to be used to store datas | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| CurveSelection | Curve selection to focus the curves generation spatially | [FDataflowCurveSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowCurveSelection) | () |
| CurveCount | Max number of guides | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store datas | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateCurveGeometry?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateCurveGeometry?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateCurveGeometry?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateCurveGeometry?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateCurveGeometry?application_version=5.7#outputs)
