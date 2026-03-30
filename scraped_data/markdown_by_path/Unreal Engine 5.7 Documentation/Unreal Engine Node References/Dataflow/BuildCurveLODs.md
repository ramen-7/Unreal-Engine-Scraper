<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/BuildCurveLODs?application_version=5.7 -->

# BuildCurveLODs

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
7. BuildCurveLODs

# BuildCurveLODs

BuildCurveLODs (v1)

On this page

### Description

BuildCurveLODs (v1)
Experimental

Builds the curves LODs

Input(s) :
Collection - Managed array collection to be used to store data
CurveSelection - Curve selection to focus the geometry LODs spatially

Output(s):
Collection [Passthrough] - Managed array collection to be used to store data
CurveParentsKey - Curve parent indices key to be used in other nodes if necessary
CurveLodsKey - Curve lods indices key to be used in other nodes if necessary

### Information

|  |  |
| --- | --- |
| Module | [HairStrandsDataflow](/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow) |
| Category | Groom |
| Type | [FBuildCurveLODsDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/HairStrandsDataflow/FBuildCurveLODsDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store data | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| CurveSelection | Curve selection to focus the geometry LODs spatially | [FDataflowCurveSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowCurveSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | Managed array collection to be used to store data | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| CurveParentsKey | Curve parent indices key to be used in other nodes if necessary | [FCollectionAttributeKey](/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |
| CurveLodsKey | Curve lods indices key to be used in other nodes if necessary | [FCollectionAttributeKey](/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/BuildCurveLODs?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/BuildCurveLODs?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/BuildCurveLODs?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/BuildCurveLODs?application_version=5.7#outputs)
