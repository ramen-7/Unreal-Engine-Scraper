<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SetFleshDefaultProperties?application_version=5.7 -->

# SetFleshDefaultProperties

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
7. SetFleshDefaultProperties

# SetFleshDefaultProperties

SetFleshDefaultProperties (v1) Set Flesh Default Properties Node

On this page

### Description

SetFleshDefaultProperties (v1)

Set Flesh Default Properties Node

### Information

|  |  |
| --- | --- |
| Module | [ChaosFleshNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes) |
| Category | Flesh |
| Type | [FSetFleshDefaultPropertiesNode](/documentation/en-us/unreal-engine/API/Plugins/ChaosFleshNodes/FSetFleshDefaultPropertiesNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Density |  | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| VertexStiffness |  | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1000000.000000 |
| VertexDamping |  | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| VertexIncompressibility | Sets incompressibility on vertex basis. 0.6 is default behavior. 1 means absolutely incompressible. 0 means no incompressibility constraint on the material | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.600000 |
| VertexInflation | Sets inflation on vertex basis. 0.5 means no inflation/deflation. 1 means inflation to 2X volume on each dimension. 0 means the material is deflated to 0 volume. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetFleshDefaultProperties?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetFleshDefaultProperties?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetFleshDefaultProperties?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetFleshDefaultProperties?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetFleshDefaultProperties?application_version=5.7#outputs)
