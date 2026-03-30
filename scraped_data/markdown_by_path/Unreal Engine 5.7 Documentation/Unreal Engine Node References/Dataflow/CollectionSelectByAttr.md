<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectByAttr?application_version=5.7 -->

# CollectionSelectByAttr

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
7. CollectionSelectByAttr

# CollectionSelectByAttr

CollectionSelectByAttr (v1)

On this page

### Description

CollectionSelectByAttr (v1)

Selects specified Vertices/Faces/Transforms in the GeometryCollection by using an attribute value
Currently supported attribute types: float, int32, String, bool

Input(s) :
Collection [Intrinsic] - GeometryCollection for the selection
AttributeKey - AttributeKey input

Output(s):
Collection [Passthrough] - GeometryCollection for the selection
VertexSelection - Vertex selection output
FaceSelection - Face selection output
TransformSelection - Transform selection output
GeometrySelection - Geometry selection output
MaterialSelection - Material selection output
CurveSelection - Curve selection output

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Selection|All |
| Type | [FCollectionSelectionByAttrDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FCollectionSelectionByAttrDatafl-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Group | Group | [ESelectionByAttrGroup](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ESelectionByAttrGroup) | Faces |
| Attribute | Attribute for the selection | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | Internal |
| Operation | Operation | [ESelectionByAttrOperation](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/ESelectionByAttrOperation) | Equal |
| Value | Attribute value for the operation | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) | true |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| AttributeKey | AttributeKey input | [FCollectionAttributeKey](/documentation/en-us/unreal-engine/API/Plugins/DataflowEnginePlugin/FCollectionAttributeKey) | (Attribute="",Group="") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection | GeometryCollection for the selection | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |
| VertexSelection | Vertex selection output | [FDataflowVertexSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowVertexSelection) |  |
| FaceSelection | Face selection output | [FDataflowFaceSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowFaceSelection) |  |
| TransformSelection | Transform selection output | [FDataflowTransformSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) |  |
| GeometrySelection | Geometry selection output | [FDataflowGeometrySelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowGeometrySelection) |  |
| MaterialSelection | Material selection output | [FDataflowMaterialSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowMaterialSelection) |  |
| CurveSelection | Curve selection output | [FDataflowCurveSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowCurveSelection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectByAttr?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectByAttr?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectByAttr?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectByAttr?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectByAttr?application_version=5.7#outputs)
