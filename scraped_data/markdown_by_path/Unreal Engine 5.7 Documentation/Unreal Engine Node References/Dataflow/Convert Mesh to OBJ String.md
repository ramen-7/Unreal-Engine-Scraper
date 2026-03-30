<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertMeshtoOBJString?application_version=5.7 -->

# Convert Mesh to OBJ String

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
7. Convert Mesh to OBJ String

# Convert Mesh to OBJ String

Convert Mesh to OBJ String (v1)

On this page

### Description

Convert Mesh to OBJ String (v1)

Convert a mesh to a string formatted as an OBJ file, which can be read by many external mesh viewers

Input(s) :
bInvertFaces - Whether to flip the orientation of the triangles in the OBJ output

Output(s):
StringOBJ - A string representing the input mesh in the OBJ file format

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Development |
| Type | [FMeshToOBJStringDebugDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMeshToOBJStringDebugDataflowNod-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Mesh |  | [TObjectPtr](/documentation/en-us/unreal-engine/API/Runtime/Core/TObjectPtr)<[UDynamicMesh](/documentation/en-us/unreal-engine/API/Runtime/GeometryFramework/UDynamicMesh)> | None |
| bInvertFaces | Whether to flip the orientation of the triangles in the OBJ output | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| StringOBJ | A string representing the input mesh in the OBJ file format | [FString](/documentation/en-us/unreal-engine/API/Runtime/Core/FString) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertMeshtoOBJString?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertMeshtoOBJString?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertMeshtoOBJString?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertMeshtoOBJString?application_version=5.7#outputs)
