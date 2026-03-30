<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetGeometryCollectionSources?application_version=5.7 -->

# GetGeometryCollectionSources

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
7. GetGeometryCollectionSources

# GetGeometryCollectionSources

GetGeometryCollectionSources (v1)

On this page

### Description

GetGeometryCollectionSources (v1)

Get the list of the original mesh information used to create a specific geometryc collection asset
each entry contains a mesh, a transform and a list of override materials

Input(s) :
Asset - Asset to get geometry sources from

Output(s):
Sources - array of geometry sources

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Asset |
| Type | [FGetGeometryCollectionSourcesDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGetGeometryCollectionSourcesDat-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Asset | Asset to get geometry sources from | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UGeometryCollection](/documentation/en-us/unreal-engine/API/Runtime/GeometryCollectionEngine/UGeometryCollection)> | None |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Sources | array of geometry sources | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FGeometryCollectionSource](/documentation/en-us/unreal-engine/API/Runtime/GeometryCollectionEngine/FGeometryCollectionSource)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetGeometryCollectionSources?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetGeometryCollectionSources?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetGeometryCollectionSources?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetGeometryCollectionSources?application_version=5.7#outputs)
