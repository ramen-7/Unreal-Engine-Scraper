<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/GetConvexHullVolume?application_version=5.7 -->

# GetConvexHullVolume

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
7. GetConvexHullVolume

# GetConvexHullVolume

GetConvexHullVolume (v1)

On this page

### Description

GetConvexHullVolume (v1)

Get the sum of volumes of the convex hulls on the selected nodes

Input(s) :
TransformSelection [Intrinsic] - The transforms to consider

Output(s):
Volume - Sum of convex hull volumes

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | GeometryCollection|Utilities |
| Type | [FGetConvexHullVolumeDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FGetConvexHullVolumeDataflowNode) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bSumChildrenForClustersWithoutHulls | For any cluster transform that has no convex hulls, whether to fall back to the convex hulls of the cluster's children. Otherwise, the cluster will not add to the total volume sum. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| bVolumeOfUnion | Whether to take the volume of the union of selected hulls, rather than the sum of each hull volume separately. This is more expensive but more accurate when hulls overlap. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| DebugDrawRenderSettings |  | [FDataflowNodeDebugDrawSettings](/documentation/en-us/unreal-engine/API/Runtime/DataflowEngine/FDataflowNodeDebugDrawSettings) | (RenderType=Wireframe,bTranslucent=True,Color=(R=0.000000,G=1.000000,B=0.000000,A=1.000000),LineWidthMultiplier=2.000000) |
| bRandomizeColor | Randomize color per convex hull | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| ColorRandomSeed | Random seed | [int32](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |
| TransformSelection | The transforms to consider | [FDataflowTransformSelection](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowTransformSelection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Volume | Sum of convex hull volumes | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetConvexHullVolume?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetConvexHullVolume?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetConvexHullVolume?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetConvexHullVolume?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetConvexHullVolume?application_version=5.7#outputs)
