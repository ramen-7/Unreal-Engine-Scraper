<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7 -->

# Dataflow

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
6. Dataflow

# Dataflow

On this page

### Cloth

| Node | Description |
| --- | --- |
| [AddStitch](/documentation/en-us/unreal-engine/node-reference/Dataflow/AddStitch) | AddStitch (v1) Chaos Cloth Asset Add Stitch Node |
| [ApplyProxyDeformer](/documentation/en-us/unreal-engine/node-reference/Dataflow/ApplyProxyDeformer) | ApplyProxyDeformer (v1) Update the Render Mesh by applying any existing proxy deformer data. |
| [ApplyResizing](/documentation/en-us/unreal-engine/node-reference/Dataflow/ApplyResizing) | ApplyResizing (v1) Experimental Apply resizing for a given Target Mesh. |
| [Attribute](/documentation/en-us/unreal-engine/node-reference/Dataflow/Attribute) | Attribute (v2) Experimental Create a new attribute for the specified group. |
| [BindToRootBone](/documentation/en-us/unreal-engine/node-reference/Dataflow/BindToRootBone) | BindToRootBone (v1) Bind an entire mesh to the single root bone of the current skeleton set on the cloth collection. |
| [BlendVertices](/documentation/en-us/unreal-engine/node-reference/Dataflow/BlendVertices) | BlendVertices (v1) Blend vertex values from another cloth collection. |
| [ClothAssetImport](/documentation/en-us/unreal-engine/node-reference/Dataflow/ClothAssetImport) | ClothAssetImport (v1) For Reimport Input(s) : ClothAsset - The Cloth Asset to import into a collection. |
| [ClothAssetTerminal](/documentation/en-us/unreal-engine/node-reference/Dataflow/ClothAssetTerminal) | ClothAssetTerminal (v2) Cloth terminal node to generate a cloth asset from a cloth collection. |
| [ClothCollectionQuery](/documentation/en-us/unreal-engine/node-reference/Dataflow/ClothCollectionQuery) | ClothCollectionQuery (v1) Query a Managed Array Collection about its Cloth Collection properties. |
| [ClothCollectionToDynamicMesh](/documentation/en-us/unreal-engine/node-reference/Dataflow/ClothCollectionToDynamicMesh) | ClothCollectionToDynamicMesh (v1) Experimental Convert a Cloth Collection mesh to a dynamic mesh. |
| [CopySimulationToRenderMesh](/documentation/en-us/unreal-engine/node-reference/Dataflow/CopySimulationToRenderMesh) | CopySimulationToRenderMesh (v1) Copy the simulation mesh to the render mesh to be able to render the simulation mesh, or when not using a different mesh for rendering. |
| [CustomRegionResizing](/documentation/en-us/unreal-engine/node-reference/Dataflow/CustomRegionResizing) | CustomRegionResizing (v1) Experimental Node for adding custom region resizing data used by the ChaosOutfitAsset's Resizeable Outfit. |
| [DeleteElement](/documentation/en-us/unreal-engine/node-reference/Dataflow/DeleteElement) | DeleteElement (v1) For EChaosClothAssetElementType |
| [EnableUVResizing](/documentation/en-us/unreal-engine/node-reference/Dataflow/EnableUVResizing) | EnableUVResizing (v1) Experimental Node for enabling UV Resizing used by the ChaosOutfitAsset's Resizeable Outfit. |
| [ExtractClothSelectionSet](/documentation/en-us/unreal-engine/node-reference/Dataflow/ExtractClothSelectionSet) | ExtractClothSelectionSet (v1) Experimental Extract a selection set from a Cloth Collection. |
| [ExtractClothWeightMap](/documentation/en-us/unreal-engine/node-reference/Dataflow/ExtractClothWeightMap) | ExtractClothWeightMap (v1) Experimental Extract a weight map from a Cloth Collection. |
| [GenerateSimMorphTarget](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateSimMorphTarget) | GenerateSimMorphTarget (v1) Generate a Sim Morph target from a cloth collection sim mesh (with matching topology). |
| [ImportSimulationCache](/documentation/en-us/unreal-engine/node-reference/Dataflow/ImportSimulationCache) | ImportSimulationCache (v1) Experimental Set vertex values from a simulation cache. |
| [MakeClothAsset](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeClothAsset) | MakeClothAsset (v1) Experimental Cloth terminal node to generate a cloth asset from a cloth collection. |
| [MergeClothCollections](/documentation/en-us/unreal-engine/node-reference/Dataflow/MergeClothCollections) | MergeClothCollections (v2) Merge multiple cloth collections into a single cloth collection of multiple patterns. |
| [ProceduralSelection](/documentation/en-us/unreal-engine/node-reference/Dataflow/ProceduralSelection) | ProceduralSelection (v1) Procedurally generate a Cloth Selection set. |
| [ProxyDeformer](/documentation/en-us/unreal-engine/node-reference/Dataflow/ProxyDeformer) | ProxyDeformer (v3) Adds the proxy deformer information to this cloth collection's render data. |
| [RecalculateNormals](/documentation/en-us/unreal-engine/node-reference/Dataflow/RecalculateNormals) | RecalculateNormals (v1) Experimental Recalculate the geometry's normals. |
| [ReferenceBone](/documentation/en-us/unreal-engine/node-reference/Dataflow/ReferenceBone) | ReferenceBone (v1) Explicitly set the cloth Reference Bone (used when calculating SimulationVelocityScale). |
| [Remesh](/documentation/en-us/unreal-engine/node-reference/Dataflow/Remesh) | Remesh (v2) Remesh the cloth surface(s) to get the specified mesh resolution(s). |
| [ReverseNormals](/documentation/en-us/unreal-engine/node-reference/Dataflow/ReverseNormals) | ReverseNormals (v1) Reverse the geometry's normals or/and winding order of the simulation or/and render meshes stored in the cloth collection. |
| [Selection](/documentation/en-us/unreal-engine/node-reference/Dataflow/Selection) | Selection (v2) Chaos Cloth Asset Selection Node V 2 Input(s) : TransferCollection - The collection used to transfer sets from. |
| [SelectionToIntMap](/documentation/en-us/unreal-engine/node-reference/Dataflow/SelectionToIntMap) | SelectionToIntMap (v1) Convert an integer index selection to an integer map. |
| [SelectionToWeightMap](/documentation/en-us/unreal-engine/node-reference/Dataflow/SelectionToWeightMap) | SelectionToWeightMap (v1) Convert an integer index selection to a vertex weight map where different map values can be set for selected and unselected vertices. |
| [SetPhysicsAsset](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetPhysicsAsset) | SetPhysicsAsset (v1) Replace the current physics assets to collide the simulation mesh against. |
| [SimAccessoryMeshNode](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimAccessoryMeshNode) | SimAccessoryMeshNode (v1) Add a SimAccessoryMesh by converting a cloth collection into an accessory mesh and attaching it to an existing cloth collection. |
| [SimulationAerodynamicsConfig](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationAerodynamicsConfig) | SimulationAerodynamicsConfig (v1) Aerodynamics properties configuration node. |
| [SimulationAnimDriveConfig](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationAnimDriveConfig) | SimulationAnimDriveConfig (v1) Anim drive properties configuration node. |
| [SimulationBackstopConfig](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationBackstopConfig) | SimulationBackstopConfig (v1) Backstop properties configuration node. |
| [SimulationBendingConfig](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationBendingConfig) | SimulationBendingConfig (v1) Bending constraint property configuration node. |
| [SimulationBendingOverrideConfig](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationBendingOverrideConfig) | SimulationBendingOverrideConfig (v1) Experimental Bending constraint property override configuration node. |
| [SimulationClothVertexFaceSpringConfig](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationClothVertexFaceSpringConfig) | SimulationClothVertexFaceSpringConfig (v1) Experimental Node for creating vertex-face constraints and setting their simulation properties. |
| [SimulationClothVertexSpringConfig](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationClothVertexSpringConfig) | SimulationClothVertexSpringConfig (v1) Experimental Node for creating vertex-vertex constraints and setting their simulation properties. |
| [SimulationCollisionConfig](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationCollisionConfig) | SimulationCollisionConfig (v1) Chaos Cloth Asset Simulation Collision Config Node |
| [SimulationDampingConfig](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationDampingConfig) | SimulationDampingConfig (v1) Damping properties configuration node. |
| [SimulationDefaultConfig](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationDefaultConfig) | SimulationDefaultConfig (v1) Add default simulation properties to the cloth collection in the format of the skeletal mesh cloth editor. |
| [SimulationGravityConfig](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationGravityConfig) | SimulationGravityConfig (v1) Gravity properties configuration node. |
| [SimulationLongRangeAttachmentConfig](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationLongRangeAttachmentConfig) | SimulationLongRangeAttachmentConfig (v2) Long range attachment constraint property configuration node. |
| [SimulationMassConfig](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationMassConfig) | SimulationMassConfig (v1) Mass properties configuration node. |
| [SimulationMaxDistanceConfig](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationMaxDistanceConfig) | SimulationMaxDistanceConfig (v1) Maximum distance constraint property configuration node. |
| [SimulationMorphTargetConfig](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationMorphTargetConfig) | SimulationMorphTargetConfig (v1) Simulation Morph Target configuration node. |
| [SimulationMultiResConfig](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationMultiResConfig) | SimulationMultiResConfig (v1) Experimental Experimental Solver multires configuration node. |
| [SimulationPressureConfig](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationPressureConfig) | SimulationPressureConfig (v1) Pressure properties configuration node. |
| [SimulationResolveExtremeDeformationConfig](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationResolveExtremeDeformationConfig) | SimulationResolveExtremeDeformationConfig (v1) Resolve extreme deformation properties configuration node. |
| [SimulationSelfCollisionConfig](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationSelfCollisionConfig) | SimulationSelfCollisionConfig (v2) Self-collision repulsion forces (point-face) properties configuration node. |
| [SimulationSelfCollisionSpheresConfig](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationSelfCollisionSpheresConfig) | SimulationSelfCollisionSpheresConfig (v1) Self-collision spheres properties configuration node. |
| [SimulationSolverConfig](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationSolverConfig) | SimulationSolverConfig (v1) Solver properties configuration node. |
| [SimulationStretchConfig](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationStretchConfig) | SimulationStretchConfig (v1) Stretching constraint property configuration node. |
| [SimulationStretchOverrideConfig](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationStretchOverrideConfig) | SimulationStretchOverrideConfig (v1) Experimental Stretching constraint property override configuration node. |
| [SimulationVelocityScaleConfig](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationVelocityScaleConfig) | SimulationVelocityScaleConfig (v1) Velocity scale properties configuration node. |
| [SkeletalMeshImport](/documentation/en-us/unreal-engine/node-reference/Dataflow/SkeletalMeshImport) | SkeletalMeshImport (v2) Import a skeletal mesh asset into the cloth collection simulation and/or render mesh containers. |
| [SkinningBlend](/documentation/en-us/unreal-engine/node-reference/Dataflow/SkinningBlend) | SkinningBlend (v1) Initialize the RenderDeformerSkinningBlend weight map from the ProxyDeformer mapping data. |
| [StaticMeshImport](/documentation/en-us/unreal-engine/node-reference/Dataflow/StaticMeshImport) | StaticMeshImport (v2) Import a static mesh asset into the cloth collection simulation and/or render mesh containers. |
| [TransferSkinWeights](/documentation/en-us/unreal-engine/node-reference/Dataflow/TransferSkinWeights) | TransferSkinWeights (v1) Transfer the skinning weights set on a skeletal mesh to the simulation and/or render mesh stored in the cloth collection. |
| [TransformPositions](/documentation/en-us/unreal-engine/node-reference/Dataflow/TransformPositions) | TransformPositions (v1) Chaos Cloth Asset Transform Positions Node |
| [TransformUVs](/documentation/en-us/unreal-engine/node-reference/Dataflow/TransformUVs) | TransformUVs (v1) Chaos Cloth Asset Transform UVs Node |
| [UpdateClothFromDynamicMesh](/documentation/en-us/unreal-engine/node-reference/Dataflow/UpdateClothFromDynamicMesh) | UpdateClothFromDynamicMesh (v1) Experimental Update cloth collection attributes from a DynamicMesh |
| [USDImport](/documentation/en-us/unreal-engine/node-reference/Dataflow/USDImport) | USDImport (v2) Import a USD file from a third party garment construction software. |
| [WeightMap](/documentation/en-us/unreal-engine/node-reference/Dataflow/WeightMap) | WeightMap (v1) For Name implicit operators. |
| [WeightMapToSelection](/documentation/en-us/unreal-engine/node-reference/Dataflow/WeightMapToSelection) | WeightMapToSelection (v1) Convert a vertex weight map to an integer selection set. |

### Collection

| Node | Description |
| --- | --- |
| [CorrectSkinWeights](/documentation/en-us/unreal-engine/node-reference/Dataflow/CorrectSkinWeights) | CorrectSkinWeights (v1) Experimental Correct skin weights vertex properties. |
| [EditSkeletonBones](/documentation/en-us/unreal-engine/node-reference/Dataflow/EditSkeletonBones) | EditSkeletonBones (v1) Experimental Edit skeleton bones properties. |
| [EditSkinWeights](/documentation/en-us/unreal-engine/node-reference/Dataflow/EditSkinWeights) | EditSkinWeights (v1) Experimental Edit skin weights vertex properties. |
| [GetSkinningSelection](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetSkinningSelection) | GetSkinningSelection (v1) Experimental Get skin weights selection attributes. |
| [PaintWeightMap](/documentation/en-us/unreal-engine/node-reference/Dataflow/PaintWeightMap) | PaintWeightMap (v1) Scalar vertex properties. |
| [SetSkinningSelection](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetSkinningSelection) | SetSkinningSelection (v1) Experimental Set skin weights selection attributes. |
| [SetSkinningSkeletalMesh](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetSkinningSkeletalMesh) | SetSkinningSkeletalMesh (v1) Experimental Set the skeletal mesh for the collection Input(s) : Collection - Managed array collection to be used to store datas SkeletalMesh - Skeletal mesh binding to be stored in the collection GeometrySelection - Geometries to set skinning skeletal mesh on Output(s): Collection [Passthrough] - Managed array collection to be used to store datas |

### Collection|Utilities

| Node | Description |
| --- | --- |
| [CreateColorArrayFromFloatArray](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateColorArrayFromFloatArray) | CreateColorArrayFromFloatArray (v1) Set the vertex color on the collection based on the normalized float array. |
| [SetVertexColorFromFloatArray](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetVertexColorFromFloatArray) | SetVertexColorFromFloatArray (v1) Set the vertex color on the collection based on the normalized float array. |
| [SetVertexColorFromVertexIndices](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetVertexColorFromVertexIndices) | SetVertexColorFromVertexIndices (v1) Set the vertex color of the collection based on the selection set. |
| [SetVertexColorFromVertexSelection](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetVertexColorFromVertexSelection) | SetVertexColorFromVertexSelection (v1) Set the vertex color of the collection based on the selection set. |

### Convert

| Node | Description |
| --- | --- |
| [ConvertBoolArrayTypes](/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertBoolArrayTypes) | ConvertBoolArrayTypes (v1) Convert Bool array types Input(s) : In [Intrinsic] - Input value Output(s): Out - Output value |
| [ConvertBoolTypes](/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertBoolTypes) | ConvertBoolTypes (v1) Convert Bool types Input(s) : In [Intrinsic] - Input value Output(s): Out - Output value |
| [ConvertIndexArrayToSelection](/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertIndexArrayToSelection) | ConvertIndexArrayToSelection (v1) Convert Index Array to Selection Input(s) : Collection [Intrinsic] - Collection for the selection In [Intrinsic] - Input value Output(s): Collection [Passthrough] - Collection for the selection Out - Output value |
| [ConvertIndexToSelection](/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertIndexToSelection) | ConvertIndexToSelection (v1) Convert Index to Selection Input(s) : Collection [Intrinsic] - Collection for the selection In [Intrinsic] - Input value Output(s): Collection [Passthrough] - Collection for the selection Out - Output value |
| [ConvertNumericArrayTypes](/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertNumericArrayTypes) | ConvertNumericArrayTypes (v1) Convert Numeric array types Input(s) : In [Intrinsic] - Input value Output(s): Out - Output value |
| [ConvertNumericTypes](/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertNumericTypes) | ConvertNumericTypes (v1) Convert Numeric types (double, float, int64, uint64, int32, uint32, int16, uint16, int8, uint8) Input(s) : In [Intrinsic] - Input value Output(s): Out - Output value |
| [ConvertRotation](/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertRotation) | ConvertRotation (v1) Convert Rotation (FQuat, FRotator, FVector) Input(s) : In [Intrinsic] - Input value Output(s): Out - Output value |
| [ConvertSelectionToIndexArray](/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertSelectionToIndexArray) | ConvertSelectionToIndexArray (v1) Convert Selection to Index Array Input(s) : In [Intrinsic] - Input value Output(s): Out - Output value |
| [ConvertSelectionTypes](/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertSelectionTypes) | ConvertSelectionTypes (v1) Convert Selection types Input(s) : Collection [Intrinsic] - GeometryCollection for the selection In [Intrinsic] - Input value Output(s): Collection [Passthrough] - GeometryCollection for the selection Out - Output value |
| [ConvertStringArrayTypes](/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertStringArrayTypes) | ConvertStringArrayTypes (v1) Convert String array types Input(s) : In [Intrinsic] - Input value Output(s): Out - Output value |
| [ConvertStringConvertibleTypes](/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertStringConvertibleTypes) | ConvertStringConvertibleTypes (v1) Convert String convertible types (String types, Numeric types, Vector types and Booleans) Input(s) : In [Intrinsic] - Input value Output(s): Out - Output value |
| [ConvertStringTypes](/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertStringTypes) | ConvertStringTypes (v1) Convert String types (FString or FName or FText) Input(s) : In [Intrinsic] - Input value Output(s): Out - Output value |
| [ConvertTransformArrayTypes](/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertTransformArrayTypes) | ConvertTransformArrayTypes (v1) Convert Transform array types Input(s) : In [Intrinsic] - Input value Output(s): Out - Output value |
| [ConvertTransformTypes](/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertTransformTypes) | ConvertTransformTypes (v1) Convert Transform types Input(s) : In [Intrinsic] - Input value Output(s): Out - Output value |
| [ConvertVectorArrayTypes](/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertVectorArrayTypes) | ConvertVectorArrayTypes (v1) Convert Vector array types Input(s) : In [Intrinsic] - Input value Output(s): Out - Output value |
| [ConvertVectorTypes](/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertVectorTypes) | ConvertVectorTypes (v1) Convert Vector types (2D, 3D and 4D vector, single and double precision) Input(s) : In [Intrinsic] - Input value Output(s): Out - Output value |

### Core

| Node | Description |
| --- | --- |
| [Print](/documentation/en-us/unreal-engine/node-reference/Dataflow/Print) | Print (v1) Print value in the log Supports any type comnvertible to a string |
| [ReRouteNode](/documentation/en-us/unreal-engine/node-reference/Dataflow/ReRouteNode) | ReRouteNode (v1) Dataflow Re Route Node |

### Dataflow

| Node | Description |
| --- | --- |
| [BreakAttributeKey](/documentation/en-us/unreal-engine/node-reference/Dataflow/BreakAttributeKey) | BreakAttributeKey (v1) Break Attribute Key Dataflow Node |
| [FloatOverride](/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatOverride) | FloatOverride (v1) Float Override Dataflow Node |
| [GetVariable](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetVariable) | GetVariable (v1) Get Dataflow Variable Node |
| [SelectionSet](/documentation/en-us/unreal-engine/node-reference/Dataflow/SelectionSet) | SelectionSet (v1) Selection Set Dataflow Node |

### Fields

| Node | Description |
| --- | --- |
| [BoxFalloffField](/documentation/en-us/unreal-engine/node-reference/Dataflow/BoxFalloffField) | BoxFalloffField (v1) BoxFalloff Field Dataflow node |
| [FieldMakeDenseFloatArray](/documentation/en-us/unreal-engine/node-reference/Dataflow/FieldMakeDenseFloatArray) | FieldMakeDenseFloatArray (v1) Converts a sparse FloatArray (a selected subset of the whole incoming array) into a dense FloatArray (same number of elements as the incoming array using NumSamplePositions) using the Remap input NumSamplePositions controls the size of the output array, only indices smaller than l to than NumSamplePositions will be processed |
| [NoiseField](/documentation/en-us/unreal-engine/node-reference/Dataflow/NoiseField) | NoiseField (v1) Noise Field Dataflow node |
| [PlaneFalloffField](/documentation/en-us/unreal-engine/node-reference/Dataflow/PlaneFalloffField) | PlaneFalloffField (v1) PlaneFalloff Field Dataflow node |
| [RadialFalloffField](/documentation/en-us/unreal-engine/node-reference/Dataflow/RadialFalloffField) | RadialFalloffField (v1) RadialFalloff Field Dataflow node |
| [RadialIntMaskField](/documentation/en-us/unreal-engine/node-reference/Dataflow/RadialIntMaskField) | RadialIntMaskField (v1) RadialIntMask Field Dataflow node |
| [RadialVectorField](/documentation/en-us/unreal-engine/node-reference/Dataflow/RadialVectorField) | RadialVectorField (v1) RadialVector Field Dataflow node |
| [RandomVectorField](/documentation/en-us/unreal-engine/node-reference/Dataflow/RandomVectorField) | RandomVectorField (v1) RandomVector Field Dataflow node |
| [SumScalarField](/documentation/en-us/unreal-engine/node-reference/Dataflow/SumScalarField) | SumScalarField (v1) Sum Scalar Field Dataflow Node |
| [SumVectorField](/documentation/en-us/unreal-engine/node-reference/Dataflow/SumVectorField) | SumVectorField (v1) Sum Vector Field Dataflow Node |
| [UniformIntegerField](/documentation/en-us/unreal-engine/node-reference/Dataflow/UniformIntegerField) | UniformIntegerField (v1) UniformInteger Field Dataflow node |
| [UniformScalarField](/documentation/en-us/unreal-engine/node-reference/Dataflow/UniformScalarField) | UniformScalarField (v1) UniformScalar Field Dataflow node |
| [UniformVectorField](/documentation/en-us/unreal-engine/node-reference/Dataflow/UniformVectorField) | UniformVectorField (v1) UniformVector Field Dataflow node |
| [WaveScalarField](/documentation/en-us/unreal-engine/node-reference/Dataflow/WaveScalarField) | WaveScalarField (v1) WaveScalar Field Dataflow node v2 |

### Flesh

| Node | Description |
| --- | --- |
| [AddKinematicParticles](/documentation/en-us/unreal-engine/node-reference/Dataflow/AddKinematicParticles) | AddKinematicParticles (v1) Add Kinematic Particles Dataflow Node |
| [AppendTetrahedralCollection](/documentation/en-us/unreal-engine/node-reference/Dataflow/AppendTetrahedralCollection) | AppendTetrahedralCollection (v2) Append another Tetrahedral Collection to this collection. |
| [AppendToCollectionTransformAttribute](/documentation/en-us/unreal-engine/node-reference/Dataflow/AppendToCollectionTransformAttribute) | AppendToCollectionTransformAttribute (v1) @todo(deprecate), move to GeometryCollection as AppendCollectionTransformDataflowNode |
| [AuthorSceneCollisionCandidates](/documentation/en-us/unreal-engine/node-reference/Dataflow/AuthorSceneCollisionCandidates) | AuthorSceneCollisionCandidates (v1) Marks mesh vertices as candidates for scene collision raycasts. |
| [AuthorTetMetrics](/documentation/en-us/unreal-engine/node-reference/Dataflow/AuthorTetMetrics) | AuthorTetMetrics (v1) Generate quality metrics Input(s) : Collection - Passthrough geometry collection. |
| [ComputeFiberField](/documentation/en-us/unreal-engine/node-reference/Dataflow/ComputeFiberField) | ComputeFiberField (v1) Computes a muscle fiber direction per tetrahedron from a GeometryCollection containing tetrahedra, vertices, and origin & insertion vertex fields. |
| [ComputeFiberStreamline](/documentation/en-us/unreal-engine/node-reference/Dataflow/ComputeFiberStreamline) | ComputeFiberStreamline (v1) Computes fiber streamlines (line segments) flowing from muscle origins to insertions in the muscle fiber field. |
| [ComputeIslands](/documentation/en-us/unreal-engine/node-reference/Dataflow/ComputeIslands) | ComputeIslands (v1) @todo(deprecate) |
| [ComputeMuscleActivationData](/documentation/en-us/unreal-engine/node-reference/Dataflow/ComputeMuscleActivationData) | ComputeMuscleActivationData (v2) Determines muscles that are eligible for activation and computes muscle activation data. |
| [CreateAirTetrahedralConstraint](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateAirTetrahedralConstraint) | CreateAirTetrahedralConstraint (v1) Create air tetrahedral constraint between point-triangle pair from surface meshes of different geometries based on search radius. |
| [CreateAirVolumeConstraint](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateAirVolumeConstraint) | CreateAirVolumeConstraint (v1) Experimental Creates volume constraint (defined by point-triangle tetrahedron volume) between surface meshes of different geometries. |
| [CreateTetrahedron](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateTetrahedron) | CreateTetrahedron (v1) Create Tetrahedron Dataflow Node Input(s) : Collection - Input pass-through collection. |
| [DeleteFleshVertices](/documentation/en-us/unreal-engine/node-reference/Dataflow/DeleteFleshVertices) | DeleteFleshVertices (v1) Extract a Tetrahedral Collection from this collection based on selected vertex. |
| [DeleteVertexTrianglePositionTargetBinding](/documentation/en-us/unreal-engine/node-reference/Dataflow/DeleteVertexTrianglePositionTargetBinding) | DeleteVertexTrianglePositionTargetBinding (v1) Delete vertex-triangle weak constraints (zero rest length springs) between VertexSelection1 and VertexSelection2. |
| [GenerateOriginInsertion](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateOriginInsertion) | GenerateOriginInsertion (v1) Given two sets of vertex indices, generate two sets of vertex indices for origins and insertions that are within X distance away. |
| [GenerateSkeletalBindings](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateSkeletalBindings) | GenerateSkeletalBindings (v1) Generate barycentric bindings (used by the FleshDeformer deformer graph) of a render surface to a tetrahedral mesh. |
| [GenerateSurfaceBindings](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateSurfaceBindings) | GenerateSurfaceBindings (v1) Generate barycentric bindings (used by the FleshDeformer deformer graph and Geometry Cache generation) of a render surface to a tetrahedral mesh and its surface. |
| [GetFleshAsset](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetFleshAsset) | GetFleshAsset (v1) Get Flesh Asset Dataflow Node |
| [GetSurfaceIndices](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetSurfaceIndices) | GetSurfaceIndices (v1) Get Surface Indices Node |
| [IsolateComponent](/documentation/en-us/unreal-engine/node-reference/Dataflow/IsolateComponent) | IsolateComponent (v1) Isolate Component Node Input(s) : Collection - typedef FManagedArrayCollection DataType; Output(s): Collection [Passthrough] - typedef FManagedArrayCollection DataType; |
| [KinematicBodySetupInitialization](/documentation/en-us/unreal-engine/node-reference/Dataflow/KinematicBodySetupInitialization) | KinematicBodySetupInitialization (v1) @todo(deprecate), rename to FCollisionBodyConstraintDataflowNode |
| [KinematicInitialization](/documentation/en-us/unreal-engine/node-reference/Dataflow/KinematicInitialization) | KinematicInitialization (v1) @todo(deprecate), rename to FKinematicConstraintDataflowNode |
| [KinematicMuscleAttachments](/documentation/en-us/unreal-engine/node-reference/Dataflow/KinematicMuscleAttachments) | KinematicMuscleAttachments (v1) Kinematic Muscle Attachments Dataflow Node |
| [KinematicSkeletalMeshInitialization](/documentation/en-us/unreal-engine/node-reference/Dataflow/KinematicSkeletalMeshInitialization) | KinematicSkeletalMeshInitialization (v1) @todo(deprecate), rename to FSkeletalMeshConstraintDataflowNode |
| [KinematicSkeletonConstraint](/documentation/en-us/unreal-engine/node-reference/Dataflow/KinematicSkeletonConstraint) | KinematicSkeletonConstraint (v1) Bind a animation driven skeleton hierarchy into the tetrahedron on the collection. |
| [RadialTetrahedron](/documentation/en-us/unreal-engine/node-reference/Dataflow/RadialTetrahedron) | RadialTetrahedron (v1) @todo(deprecate), rename to FRadialTetrahedronDataflowNode |
| [ReadSkeletalMeshCurves](/documentation/en-us/unreal-engine/node-reference/Dataflow/ReadSkeletalMeshCurves) | ReadSkeletalMeshCurves (v1) Read Skeletal Mesh Curves Dataflow Node |
| [SetCollidableVertices](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetCollidableVertices) | SetCollidableVertices (v1) Set custom vertices so that only these vertices can collide with other surfaces. |
| [SetFleshBonePositionTargetBinding](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetFleshBonePositionTargetBinding) | SetFleshBonePositionTargetBinding (v2) Binds vertices from Collection to bone skeletal mesh surface via kinematic or weak constraints. |
| [SetFleshDefaultProperties](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetFleshDefaultProperties) | SetFleshDefaultProperties (v1) Set Flesh Default Properties Node |
| [SetMuscleActivationParameter](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetMuscleActivationParameter) | SetMuscleActivationParameter (v1) Sets per-muscle parameters for custom muscle contraction. |
| [SetVertexTetrahedraPositionTargetBinding](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetVertexTetrahedraPositionTargetBinding) | SetVertexTetrahedraPositionTargetBinding (v1) Set Vertex Tetrahedra Position Target Binding Dataflow Node |
| [SetVertexTrianglePositionTargetBinding](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetVertexTrianglePositionTargetBinding) | SetVertexTrianglePositionTargetBinding (v1) Create point-triangle weak constraints (springs) between surface meshes of different geometries based on search radius. |
| [SetVertexVertexPositionTargetBinding](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetVertexVertexPositionTargetBinding) | SetVertexVertexPositionTargetBinding (v1) Set Vertex Vertex Position Target Binding Dataflow Node |
| [SkinSimulationProperties](/documentation/en-us/unreal-engine/node-reference/Dataflow/SkinSimulationProperties) | SkinSimulationProperties (v1) Set triangle mesh to simulate using skin constraints |
| [TriangleMeshSimulationProperties](/documentation/en-us/unreal-engine/node-reference/Dataflow/TriangleMeshSimulationProperties) | TriangleMeshSimulationProperties (v1) Convert tetmesh to simulate using surface traingle mesh only |
| [VisualizeFiberField](/documentation/en-us/unreal-engine/node-reference/Dataflow/VisualizeFiberField) | VisualizeFiberField (v1) Visualizes a muscle fiber direction per tetrahedron from a GeometryCollection containing tetrahedra. |
| [VisualizeKinematicFaces](/documentation/en-us/unreal-engine/node-reference/Dataflow/VisualizeKinematicFaces) | VisualizeKinematicFaces (v1) Visualizes kinematic faces from GeometryCollection. |
| [VisualizePositionTargets](/documentation/en-us/unreal-engine/node-reference/Dataflow/VisualizePositionTargets) | VisualizePositionTargets (v1) Visualizes position target vectors from GeometryCollection. |

### Flesh|Experimental

| Node | Description |
| --- | --- |
| [TriangleBoundaryIndices](/documentation/en-us/unreal-engine/node-reference/Dataflow/TriangleBoundaryIndices) | TriangleBoundaryIndices (v1) Experimental Outputs boundary nodes of a triangle mesh |

### Flesh|Utilities

| Node | Description |
| --- | --- |
| [VisualizeTetrahedrons](/documentation/en-us/unreal-engine/node-reference/Dataflow/VisualizeTetrahedrons) | VisualizeTetrahedrons (v1) Visualize tetrahedrons in a collection Input(s) : Collection [Intrinsic] - Collection for the custom attribute Output(s): Collection [Passthrough] - Collection for the custom attribute |

### FlowControl

| Node | Description |
| --- | --- |
| [Branch](/documentation/en-us/unreal-engine/node-reference/Dataflow/Branch) | Branch (v1) Dataflow Branch Node |
| [ForceDependency](/documentation/en-us/unreal-engine/node-reference/Dataflow/ForceDependency) | ForceDependency (v1) Force an evaluation dependency between two values Input(s) : Value - Evaluating Value will force an evaluation of DependentValue DependentValue - Evaluating Value will force an evaluation of DependentValue Output(s): Value [Passthrough] - Evaluating Value will force an evaluation of DependentValue |
| [Select](/documentation/en-us/unreal-engine/node-reference/Dataflow/Select) | Select (v1) Dataflow Select Node |

### General

| Node | Description |
| --- | --- |
| [GetPhysicsAssetFromSkeletalMesh](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetPhysicsAssetFromSkeletalMesh) | GetPhysicsAssetFromSkeletalMesh (v1) Get the physics assets from input skeletal mesh. |
| [SkeletalMesh](/documentation/en-us/unreal-engine/node-reference/Dataflow/SkeletalMesh) | SkeletalMesh (v1) Get Skeletal Mesh Dataflow Node |
| [SkeletalMeshBone](/documentation/en-us/unreal-engine/node-reference/Dataflow/SkeletalMeshBone) | SkeletalMeshBone (v1) Skeletal Mesh Bone Dataflow Node |
| [SkeletalMeshReferenceTransform](/documentation/en-us/unreal-engine/node-reference/Dataflow/SkeletalMeshReferenceTransform) | SkeletalMeshReferenceTransform (v1) Skeletal Mesh Reference Transform Dataflow Node |
| [Skeleton](/documentation/en-us/unreal-engine/node-reference/Dataflow/Skeleton) | Skeleton (v1) Get Skeleton Dataflow Node |
| [StaticMesh](/documentation/en-us/unreal-engine/node-reference/Dataflow/StaticMesh) | StaticMesh (v1) Get Static Mesh Dataflow Node |

### Generators|Box

| Node | Description |
| --- | --- |
| [MakeBox](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeBox) | MakeBox (v1) Make a box |

### Generators|Collection

| Node | Description |
| --- | --- |
| [MakeCollection](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeCollection) | MakeCollection (v1) Make an empty ManagedArrayCollection |

### Generators|Mesh

| Node | Description |
| --- | --- |
| [MakeBoxMesh](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeBoxMesh) | MakeBoxMesh (v1) Make a box mesh Output(s): Mesh - Output mesh |
| [MakeCapsuleMesh](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeCapsuleMesh) | MakeCapsuleMesh (v1) Make a capsule mesh Output(s): Mesh - Output mesh |
| [MakeCylinderMesh](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeCylinderMesh) | MakeCylinderMesh (v1) Make a cylinder mesh Output(s): Mesh - Output mesh |
| [MakeDiscMesh](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeDiscMesh) | MakeDiscMesh (v1) Make a disc mesh Output(s): Mesh - Output mesh |
| [MakeRectangleMesh](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeRectangleMesh) | MakeRectangleMesh (v1) Make a rectangle mesh Input(s) : Origin - Rectangle will be translated so that center is at this point Normal - Normal vector of all vertices will be set to this value. |
| [MakeSphereMesh](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeSphereMesh) | MakeSphereMesh (v1) Make a sphere mesh Output(s): Mesh - Output mesh |
| [MakeStairMesh](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeStairMesh) | MakeStairMesh (v1) Make a stair mesh Output(s): Mesh - Output mesh |
| [MakeTorusMesh](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeTorusMesh) | MakeTorusMesh (v1) Make a torus mesh Input(s) : Origin - Torus will be translated so that center is at this point Output(s): Mesh - Output mesh |

### Generators|Plane

| Node | Description |
| --- | --- |
| [MakePlane](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakePlane) | MakePlane (v1) Make a plane Input(s) : BasePoint - Base point Normal - Normal vector Output(s): Plane - Output mesh |

### Generators|Point

| Node | Description |
| --- | --- |
| [AppendPoints](/documentation/en-us/unreal-engine/node-reference/Dataflow/AppendPoints) | AppendPoints (v1) Combine two arrays of points into one |
| [ClusterScatterPoints](/documentation/en-us/unreal-engine/node-reference/Dataflow/ClusterScatterPoints) | ClusterScatterPoints (v1) Cluster Scatter Points Dataflow Node Input(s) : NumberClustersMin - Minimum number of clusters of points to create. |
| [GridScatterPoints](/documentation/en-us/unreal-engine/node-reference/Dataflow/GridScatterPoints) | GridScatterPoints (v1) Grid Scatter Points Dataflow Node Input(s) : NumberOfPointsInX - Number of points in X direction NumberOfPointsInY - Number of points in Y direction NumberOfPointsInZ - Number of points in Z direction RandomSeed - Seed for random MaxRandomDisplacementX - Random displacement in X direction will be in the range (-MaxRandomDisplacementX, MaxRandomDisplacementX) MaxRandomDisplacementY - Random displacement in Y direction will be in the range (-MaxRandomDisplacementY, MaxRandomDisplacementY) MaxRandomDisplacementZ - Random displacement in Z direction will be in the range (-MaxRandomDisplacementZ, MaxRandomDisplacementZ) BoundingBox - BoundingBox to generate points inside of Output(s): Points - Generated points |
| [MakePoints](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakePoints) | MakePoints (v1) Make a points array from specified points |
| [RadialScatterPoints](/documentation/en-us/unreal-engine/node-reference/Dataflow/RadialScatterPoints) | RadialScatterPoints (v2) Radial Scatter Points Dataflow Node V 2 Input(s) : BoundingBox - BoundingBox to generate points inside of Center - Center of generated pattern Normal - Normal to plane in which sites are generated RandomSeed - Seed for random AngularSteps - Number of angular steps AngleOffset - Angle offset at each radial step (in degrees) AngularNoise - Amount of global variation to apply to each angular step (in degrees) Radius - Pattern radius (in cm) RadialSteps - Number of radial steps RadialStepExponent - Radial steps will follow a distribution based on this exponent, i.e., Pow(distance from center, RadialStepExponent) RadialMinStep - Minimum radial separation between any two voronoi points (in cm) RadialNoise - Amount of global variation to apply to each radial step (in cm) RadialVariability - Amount to randomly displace each Voronoi site radially (in cm) AngularVariability - Amount to randomly displace each Voronoi site in angle (in degrees) AxialVariability - Amount to randomly displace each Voronoi site in the direction of the rotation axis (in cm) Output(s): Points - Generated points |
| [TransformPoints](/documentation/en-us/unreal-engine/node-reference/Dataflow/TransformPoints) | TransformPoints (v1) Transform an array of points |
| [UniformScatterPoints](/documentation/en-us/unreal-engine/node-reference/Dataflow/UniformScatterPoints) | UniformScatterPoints (v2) Uniform Scatter Points Dataflow Node V 2 Input(s) : MinNumberOfPoints - Minimum for the random range MaxNumberOfPoints - Maximum for the random range RandomSeed - Seed for random BoundingBox - BoundingBox to generate points inside of Output(s): Points - Generated points |

### Generators|Sphere

| Node | Description |
| --- | --- |
| [MakeSphere](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeSphere) | MakeSphere (v1) Description for this node |

### Generators|Transform

| Node | Description |
| --- | --- |
| [MakeRotator](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeRotator) | MakeRotator (v1) Make a Rotator Input(s) : Pitch - Rotation around the right axis (around Y axis), Looking up and down (0=Straight Ahead, +Up, -Down) Yaw - Rotation around the up axis (around Z axis), Turning around (0=Forward, +Right, -Left) Roll - Rotation around the forward axis (around X axis), Tilting your head, (0=Straight, +Clockwise, -CCW) Output(s): Rotator - Rotator output |
| [MakeTransform](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeTransform) | MakeTransform (v1) Make an FTransform Note: Originaly this version was depricated and replaced with FMakeTransformDataflowNode\_v2 but when AnyRotationType was introduced with the ConvertAnyRotation node FMakeTransformDataflowNode\_v2 became obsolete and this version became the current version again Input(s) : InTranslation - Translation InRotation - Rotation as Euler InScale - Scale Output(s): OutTransform - Result transform |

### GeometryCollection

| Node | Description |
| --- | --- |
| [AddRootProxyMeshToArray](/documentation/en-us/unreal-engine/node-reference/Dataflow/AddRootProxyMeshToArray) | AddRootProxyMeshToArray (v1)  *Add a root proxy object to an array of root proxy mesh*  \* (used by geometry collection assets) Input(s) : RootProxyMeshes - Root proxy array to add the mesh to Output(s): RootProxyMeshes [Passthrough] - Root proxy array to add the mesh to |
| [AppendCollections](/documentation/en-us/unreal-engine/node-reference/Dataflow/AppendCollections) | AppendCollections (v1) Description for this node |
| [CloseGeometryOnCollection](/documentation/en-us/unreal-engine/node-reference/Dataflow/CloseGeometryOnCollection) | CloseGeometryOnCollection (v1) Close Geometry on Collection Dataflow Node |
| [CollectionToSkeletalMesh](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionToSkeletalMesh) | CollectionToSkeletalMesh (v1) Collection to Skeletal Mesh Dataflow Node |
| [MakeAttributeKey](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeAttributeKey) | MakeAttributeKey (v1) Make Attribute Key Dataflow Node |
| [MakeRootProxyMesh](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeRootProxyMesh) | MakeRootProxyMesh (v1) Create a RootProxyMesh object (used by geometry collection assets) Input(s) : Mesh - mesh to use as a proxy Transform - transform to use for the proxy, relative to the asset it will be used for Output(s): RootProxyMesh - mesh to use as a proxy |
| [MakeRootProxyMeshArray](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeRootProxyMeshArray) | MakeRootProxyMeshArray (v1) Create a RootProxyMesh Array (used by geometry collection assets) Output(s): RootProxyMeshes - newly created array |
| [SetKinematicVertexSelection](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetKinematicVertexSelection) | SetKinematicVertexSelection (v1) Set VertexSelection to be kinematic. |
| [SkeletalMeshToCollection](/documentation/en-us/unreal-engine/node-reference/Dataflow/SkeletalMeshToCollection) | SkeletalMeshToCollection (v1) Skeletal Mesh to Collection Dataflow Node |
| [TransferVertexAttribute](/documentation/en-us/unreal-engine/node-reference/Dataflow/TransferVertexAttribute) | TransferVertexAttribute (v1) Transfer float properties from a source collection to a target collection. |
| [TransferVertexSkinWeights](/documentation/en-us/unreal-engine/node-reference/Dataflow/TransferVertexSkinWeights) | TransferVertexSkinWeights (v1) Transfer skin weights from a source collection to a target collection. |
| [TransformCollectionAttribute](/documentation/en-us/unreal-engine/node-reference/Dataflow/TransformCollectionAttribute) | TransformCollectionAttribute (v1) Transform Collection Attribute Dataflow Node |
| [VertexScalarToVertexIndices](/documentation/en-us/unreal-engine/node-reference/Dataflow/VertexScalarToVertexIndices) | VertexScalarToVertexIndices (v1) Convert an vertex float array to a list of indices Input(s) : AttributeKey - The name of the vertex attribute and group to generate indices from. |

### GeometryCollection|Asset

| Node | Description |
| --- | --- |
| [BlueprintToCollection](/documentation/en-us/unreal-engine/node-reference/Dataflow/BlueprintToCollection) | BlueprintToCollection (v2) Create a geometry collection from an asset Output(s): Collection - Geometry collection newly created Materials - Material instances array from the static mesh InstancedMeshes - Array of instanced meshes RootProxyMeshes - corresponding source proxies |
| [CreateGeometryCollectionFromSources](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateGeometryCollectionFromSources) | CreateGeometryCollectionFromSources (v2) create a geometry collection from a set of geometry sources if the source array is not connected, the source array from the current asset is going to be used Input(s) : Sources - array of geometry sources Output(s): Collection - Geometry collection newly created Materials - Materials array to use for this asset InstancedMeshes - array of instanced meshes RootProxyMeshes - corresponding source proxies |
| [GeometryCollectionToCollection](/documentation/en-us/unreal-engine/node-reference/Dataflow/GeometryCollectionToCollection) | GeometryCollectionToCollection (v2) Converts a UGeometryCollection asset to an FManagedArrayCollection Output(s): Collection - Geometry collection newly created Materials - Material instances array from the static mesh InstancedMeshes - Array of instanced meshes RootProxyMeshes - corresponding source proxies |
| [GetCollectionFromAsset](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetCollectionFromAsset) | GetCollectionFromAsset (v1) Description for this node |
| [GetGeometryCollectionAsset](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetGeometryCollectionAsset) | GetGeometryCollectionAsset (v1) Get Current geometry collection asset Note : Use with caution as this may get replaced in a near future for a more generic getAsset node Output(s): Asset - Asset this data flow graph instance is assigned to |
| [GetGeometryCollectionSources](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetGeometryCollectionSources) | GetGeometryCollectionSources (v1) Get the list of the original mesh information used to create a specific geometryc collection asset each entry contains a mesh, a transform and a list of override materials Input(s) : Asset - Asset to get geometry sources from Output(s): Sources - array of geometry sources |
| [StaticMeshToCollection](/documentation/en-us/unreal-engine/node-reference/Dataflow/StaticMeshToCollection) | StaticMeshToCollection (v2) Create a geometry collection from a UStaticMesh Input(s) : StaticMesh - Asset input MeshTransform - Transform to apply to the mesh before converting it to a collection Output(s): Collection - Geometry collection newly created Materials - Material array from the static mesh InstancedMeshes - Array of instanced meshes RootProxyMeshes - corresponding source proxies |

### GeometryCollection|Cluster

| Node | Description |
| --- | --- |
| [AutoCluster](/documentation/en-us/unreal-engine/node-reference/Dataflow/AutoCluster) | AutoCluster (v1) Automatically group pieces of a fractured Collection into a specified number of clusters Input(s) : ClusterSites - Use a Voronoi diagram with this many Voronoi sites as a guide for deciding cluster boundaries ClusterFraction - Choose the number of Voronoi sites used for clustering as a fraction of the number of child bones to process SiteSize - Choose the Edge-Size of the cube used to groups bones under a cluster (in cm). |
| [Cluster](/documentation/en-us/unreal-engine/node-reference/Dataflow/Cluster) | Cluster (v1) Cluster selected nodes under a new parent Input(s) : Collection [Intrinsic] - Collection on which to cluster nodes TransformSelection - Bone selection Output(s): Collection [Passthrough] - Collection on which to cluster nodes |
| [ClusterIsolatedRoots](/documentation/en-us/unreal-engine/node-reference/Dataflow/ClusterIsolatedRoots) | ClusterIsolatedRoots (v1) Add a single cluster to the Geometry Collection if it only has a single transform with no clusters Input(s) : Collection [Intrinsic] - Collection to modify Output(s): Collection [Passthrough] - Collection to modify |
| [ClusterMagnet](/documentation/en-us/unreal-engine/node-reference/Dataflow/ClusterMagnet) | ClusterMagnet (v1) Cluster by grouping the selected bones with their adjacent, neighboring bones. |
| [ClusterMerge](/documentation/en-us/unreal-engine/node-reference/Dataflow/ClusterMerge) | ClusterMerge (v1) Merge selected bones under a new parent cluster Input(s) : Collection [Intrinsic] - Collection on which to merge bones into a cluster TransformSelection - Bone selection Output(s): Collection [Passthrough] - Collection on which to merge bones into a cluster |
| [ClusterMergeToNeighbors](/documentation/en-us/unreal-engine/node-reference/Dataflow/ClusterMergeToNeighbors) | ClusterMergeToNeighbors (v1) Merge selected bones to their neighbors Input(s) : Collection [Intrinsic] - Collection on which to merge bones into a neighboring cluster TransformSelection - Bone selection MinVolumeCubeRoot - Size (cube root of volume) of minimum desired post-merge clusters; if > 0, selected clusters may be merged multiple times until the cluster size is above this value bOnlyToConnected - Whether to only allow clusters to merge if their bones are connected in the proximity graph bOnlySameParent - Whether to only allow clusters to merge if they have the same parent bone Output(s): Collection [Passthrough] - Collection on which to merge bones into a neighboring cluster |
| [Flatten](/documentation/en-us/unreal-engine/node-reference/Dataflow/Flatten) | Flatten (v1) Flattens selected bones. |
| [Uncluster](/documentation/en-us/unreal-engine/node-reference/Dataflow/Uncluster) | Uncluster (v1) Uncluster selected nodes Input(s) : Collection [Intrinsic] - Fractured GeometryCollection to uncluster TransformSelection - Bone selection Output(s): Collection [Passthrough] - Fractured GeometryCollection to uncluster |

### GeometryCollection|Development

| Node | Description |
| --- | --- |
| [Convert Mesh to OBJ String](/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertMeshtoOBJString) | Convert Mesh to OBJ String (v1) Convert a mesh to a string formatted as an OBJ file, which can be read by many external mesh viewers Input(s) : bInvertFaces - Whether to flip the orientation of the triangles in the OBJ output Output(s): StringOBJ - A string representing the input mesh in the OBJ file format |
| [Write String to File](/documentation/en-us/unreal-engine/node-reference/Dataflow/WriteStringtoFile) | Write String to File (v1) Write a string to a file Input(s) : FilePath - Where file should be written on disk FileContents - Contents of the file to write |

### GeometryCollection|Edit

| Node | Description |
| --- | --- |
| [MergeInCollection](/documentation/en-us/unreal-engine/node-reference/Dataflow/MergeInCollection) | MergeInCollection (v1) Merges selected bones into a single bone Input(s) : Collection [Intrinsic] - Fractured GeometryCollection to merge TransformSelection [Intrinsic] - Transform selection for merging Output(s): Collection [Passthrough] - Fractured GeometryCollection to merge |
| [PruneInCollection](/documentation/en-us/unreal-engine/node-reference/Dataflow/PruneInCollection) | PruneInCollection (v1) Deletes selected bones from Collection. |
| [SetVisibilityInCollection](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetVisibilityInCollection) | SetVisibilityInCollection (v1) Sets all selected bone's visibilty to Visible/Hidden Input(s) : Collection [Intrinsic] - Fractured GeometryCollection to set visibility TransformSelection [Intrinsic] - Transform selection for setting visibility FaceSelection [Intrinsic] - Face selection for setting visibility Output(s): Collection [Passthrough] - Fractured GeometryCollection to set visibility |

### GeometryCollection|Fracture

| Node | Description |
| --- | --- |
| [BrickCutter](/documentation/en-us/unreal-engine/node-reference/Dataflow/BrickCutter) | BrickCutter (v1) Editor Fracture Mode / Fracture / Brick tool Fracture with a customizable brick pattern. |
| [MeshCutter](/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshCutter) | MeshCutter (v1) Editor Fracture Mode / Fracture / Mesh tool Fracture using the shape of a chosen static mesh and/or array of dynamic meshes Input(s) : Collection [Intrinsic] - Collection to cut BoundingBox - Boundingbox to create the cutting planes in TransformSelection - The selected pieces to cut Transform - Transform to apply to cut planes CuttingDynamicMeshes - Dynamic Meshes to cut with CuttingStaticMesh - Static Mesh to cut with NumberToScatter - Number of meshes to random scatter GridX - Number of meshes to add to grid in X GridY - Number of meshes to add to grid in Y GridZ - Number of meshes to add to grid in Z Variability - Magnitude of random displacement to cutting meshes MinScaleFactor - Minimum scale factor to apply to cutting meshes. |
| [PlaneCutter](/documentation/en-us/unreal-engine/node-reference/Dataflow/PlaneCutter) | PlaneCutter (v2) Editor Fracture Mode / Fracture / Planar tool Fracture using a set of noised up planes. |
| [SliceCutter](/documentation/en-us/unreal-engine/node-reference/Dataflow/SliceCutter) | SliceCutter (v1) Editor Fracture Mode / Fracture / Slice tool Fracture with a grid of X, Y, and Z slices, with optional random variation in angle and offset. |
| [UniformFracture](/documentation/en-us/unreal-engine/node-reference/Dataflow/UniformFracture) | UniformFracture (v1) Editor Fracture Mode / Fracture / Uniform tool Fracture using a Voronoi diagram with a uniform random pattern, creating fracture pieces of similar volume across the shape. |
| [VoronoiFracture](/documentation/en-us/unreal-engine/node-reference/Dataflow/VoronoiFracture) | VoronoiFracture (v2) Voronoi fracture Fracture using a Voronoi diagram with a uniform random pattern, creating fracture pieces of similar volume across the shape. |

### GeometryCollection|Fracture|Utilities

| Node | Description |
| --- | --- |
| [ExplodedView](/documentation/en-us/unreal-engine/node-reference/Dataflow/ExplodedView) | ExplodedView (v1) "Explodes" the pieces from the Collection for better visualization Input(s) : Collection [Intrinsic] - Collection to explode UniformScale - Scale amount to expand the pieces uniformly in all directions Scale - Scale amounts to expand the pieces in all 3 directions Offset - Translate collection for exploded view Output(s): Collection [Passthrough] - Collection to explode |
| [FixTinyGeo](/documentation/en-us/unreal-engine/node-reference/Dataflow/FixTinyGeo) | FixTinyGeo (v1) Editor Fracture Mode / Utilities / TinyGeo tool Merge pieces of geometry onto their neighbors -- use it to, for example, clean up too small pieces of geometry. |
| [RecomputeNormalsInGeometryCollection](/documentation/en-us/unreal-engine/node-reference/Dataflow/RecomputeNormalsInGeometryCollection) | RecomputeNormalsInGeometryCollection (v1) Editor Fracture Mode / Utilities / Normals tool Recompute normals and tangents. |
| [ResampleGeometryCollection](/documentation/en-us/unreal-engine/node-reference/Dataflow/ResampleGeometryCollection) | ResampleGeometryCollection (v1) Editor Fracture Mode / Utilities / Resample tool Resample to add collision particles in large flat regions that otherwise might have poor collision response. |
| [ValidateGeometryCollection](/documentation/en-us/unreal-engine/node-reference/Dataflow/ValidateGeometryCollection) | ValidateGeometryCollection (v1) Editor Fracture Mode / Utilities / Validate tool Ensures that geometrycollection is valid and clean. |
| [VisualizeFracture](/documentation/en-us/unreal-engine/node-reference/Dataflow/VisualizeFracture) | VisualizeFracture (v1) Visualizing fracture/cluster info in fractured collection Input(s) : Collection [Intrinsic] - Collection to visualize RandomSeed - Seed for random ExplodeAmount - Scale amount to expand the pieces uniformly in all directions Scale - Scale amounts to expand the pieces in all 3 directions Offset - Translate collection for exploded view Output(s): Collection [Passthrough] - Collection to visualize |

### GeometryCollection|Mesh

| Node | Description |
| --- | --- |
| [Convex Hull to Mesh](/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvexHulltoMesh) | Convex Hull to Mesh (v1) Convert convex hulls on a geometry collection to a dynamic mesh Input(s) : OptionalSelectionFilter - Optional transform selection to convert hulls from -- if not provided, all convex hulls will be converted. |
| [Sphere Covering to Mesh](/documentation/en-us/unreal-engine/node-reference/Dataflow/SphereCoveringtoMesh) | Sphere Covering to Mesh (v1) Convert a sphere covering, as generated by the 'protect negative space' option on the "Generate Cluster Convex Hull" nodes, to a dynamic mesh Input(s) : SphereCovering [Intrinsic] - The sphere covering to convert to a mesh |

### GeometryCollection|Overrides

| Node | Description |
| --- | --- |
| [GetBoolOverrideFromAsset](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetBoolOverrideFromAsset) | GetBoolOverrideFromAsset (v1) Get Bool Override from Asset Dataflow Node |
| [GetFloatOverrideFromAsset](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetFloatOverrideFromAsset) | GetFloatOverrideFromAsset (v1) Get Float Override from Asset Dataflow Node |
| [GetIntOverrideFromAsset](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetIntOverrideFromAsset) | GetIntOverrideFromAsset (v1) Get Int Override from Asset Dataflow Node |
| [GetStringOverrideFromAsset](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetStringOverrideFromAsset) | GetStringOverrideFromAsset (v1) Get String Override from Asset Dataflow Node |

### GeometryCollection|Selection

| Node | Description |
| --- | --- |
| [CollectionSelectInternalFaces](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectInternalFaces) | CollectionSelectInternalFaces (v1) Select internal faces Input(s) : Collection [Intrinsic] - Collection to select the internal faces from TransformSelection - Transform selection to get the internal faces from if this input is not connected, then all internal faces from the collection will be returned Output(s): Collection [Passthrough] - Collection to select the internal faces from FaceSelection - selection containing Internal faces |
| [CollectionSelectionConvert](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectionConvert) | CollectionSelectionConvert (v1) Converts Vertex/Face/Transform selection into Vertex/Face/Transform selection Input(s) : Collection [Intrinsic] - GeometryCollection for the selection TransformSelection - Transform selection including the new indices FaceSelection - Face selection including the new indices VertexSelection - Vertex selection including the new indices Output(s): Collection [Passthrough] - GeometryCollection for the selection TransformSelection [Passthrough] - Transform selection including the new indices FaceSelection [Passthrough] - Face selection including the new indices VertexSelection [Passthrough] - Vertex selection including the new indices |
| [CollectionSelectionInvert](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectionInvert) | CollectionSelectionInvert (v1) Inverts selection ( support all selection types ) Input(s) : Selection [Intrinsic] - selection to invert Output(s): Selection [Passthrough] - selection to invert |
| [CollectionSelectionSetOperation](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectionSetOperation) | CollectionSelectionSetOperation (v1) Runs boolean operation on selection ( support all selection types ) Input(s) : SelectionA [Intrinsic] - First Selection object SelectionB [Intrinsic] - Second Selection object Output(s): Selection - Array of the selected bone indices after operation |

### GeometryCollection|Selection|All

| Node | Description |
| --- | --- |
| [CollectionSelectByAttr](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectByAttr) | CollectionSelectByAttr (v1) Selects specified Vertices/Faces/Transforms in the GeometryCollection by using an attribute value Currently supported attribute types: float, int32, String, bool Input(s) : Collection [Intrinsic] - GeometryCollection for the selection AttributeKey - AttributeKey input Output(s): Collection [Passthrough] - GeometryCollection for the selection VertexSelection - Vertex selection output FaceSelection - Face selection output TransformSelection - Transform selection output GeometrySelection - Geometry selection output MaterialSelection - Material selection output CurveSelection - Curve selection output |
| [GeometrySelectionToVertexSelection](/documentation/en-us/unreal-engine/node-reference/Dataflow/GeometrySelectionToVertexSelection) | GeometrySelectionToVertexSelection (v1) Converts GeometrySelection to VertexSelection Input(s) : Collection - GeometryCollection GeometrySelection - Input geometry selection Output(s): VertexSelection - Vertex selection output |

### GeometryCollection|Selection|Array

| Node | Description |
| --- | --- |
| [CollectionTransformSelectionFromIndexArray](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectionFromIndexArray) | CollectionTransformSelectionFromIndexArray (v1) Convert index array to a transform selection Input(s) : Collection [Intrinsic] - Collection to use for the selection. |
| [SelectFloatArrayIndicesInRange](/documentation/en-us/unreal-engine/node-reference/Dataflow/SelectFloatArrayIndicesInRange) | SelectFloatArrayIndicesInRange (v1) Selects indices of a float array by range Input(s) : Values - GeometryCollection for the selection Output(s): Indices - Indices of float Values matching the specified range |

### GeometryCollection|Selection|Face

| Node | Description |
| --- | --- |
| [CollectionFaceSelectCustom](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionFaceSelectCustom) | CollectionFaceSelectCustom (v1) Selects specified faces in the GeometryCollection by using a space separated list Input(s) : Collection [Intrinsic] - GeometryCollection for the selection Output(s): Collection [Passthrough] - GeometryCollection for the selection FaceSelection - Face selection including the new indices |

### GeometryCollection|Selection|Transform

| Node | Description |
| --- | --- |
| [CollectionSelectTransformString](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectTransformString) | CollectionSelectTransformString (v1) Selects transforms by name using a the BoneName attributeor other Transform group string typed attributes Input(s) : Collection [Intrinsic] - Collection for the selection Attribute - Text to serach in the name SearchText - Text to serach in the name Output(s): Collection [Passthrough] - Collection for the selection TransformSelection - output selection of the matching transforms |
| [CollectionSetTransformString](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSetTransformString) | CollectionSetTransformString (v1) Set selected transform string value the string format can use the following predefined value : - {Current} current value of the attribute - {Index} index in the selection passed as input Input(s) : Collection [Intrinsic] - Collection for the selection TransformSelection - input selection of the transforms to set - if not connected use all Attribute - Text to serach in the name TextToSet - Text to set Output(s): Collection [Passthrough] - Collection for the selection |
| [CollectionTransformSelectAll](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectAll) | CollectionTransformSelectAll (v1) Selects all the bones for the Collection Input(s) : Collection [Intrinsic] - GeometryCollection for the selection Output(s): Collection [Passthrough] - GeometryCollection for the selection TransformSelection - Array of the selected bone indices |
| [CollectionTransformSelectByFloatAttribute](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectByFloatAttribute) | CollectionTransformSelectByFloatAttribute (v1) Selects bones by a float attribute Input(s) : Collection [Intrinsic] - GeometryCollection for the selection Output(s): Collection [Passthrough] - GeometryCollection for the selection TransformSelection - Array of the selected bone indices |
| [CollectionTransformSelectByIntAttribute](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectByIntAttribute) | CollectionTransformSelectByIntAttribute (v1) Selects bones by an int attribute Input(s) : Collection [Intrinsic] - GeometryCollection for the selection Output(s): Collection [Passthrough] - GeometryCollection for the selection TransformSelection - Transform selection including the new indices |
| [CollectionTransformSelectByPercentage](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectByPercentage) | CollectionTransformSelectByPercentage (v1) Outputs the specified percentage of the selected bones Input(s) : TransformSelection [Intrinsic] - Array of the selected bone indices RandomSeed - Seed value for the random generation Output(s): TransformSelection [Passthrough] - Array of the selected bone indices |
| [CollectionTransformSelectBySize](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectBySize) | CollectionTransformSelectBySize (v1) Selects pieces based on their size Input(s) : Collection [Intrinsic] - GeometryCollection for the selection Output(s): Collection [Passthrough] - GeometryCollection for the selection TransformSelection - Array of the selected bone indices |
| [CollectionTransformSelectByVolume](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectByVolume) | CollectionTransformSelectByVolume (v1) Selects pieces based on their volume Input(s) : Collection [Intrinsic] - GeometryCollection for the selection Output(s): Collection [Passthrough] - GeometryCollection for the selection TransformSelection - Array of the selected bone indices |
| [CollectionTransformSelectChildren](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectChildren) | CollectionTransformSelectChildren (v1) Selects the children of the selected bones Input(s) : TransformSelection [Intrinsic] - Array of the selected bone indices Collection [Intrinsic] - GeometryCollection for the selection Output(s): TransformSelection [Passthrough] - Array of the selected bone indices Collection [Passthrough] - GeometryCollection for the selection |
| [CollectionTransformSelectCluster](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectCluster) | CollectionTransformSelectCluster (v2) Selects the clusters in the Collection this version works properly and address the issues found in the deprecated version 1 Input(s) : Collection [Intrinsic] - GeometryCollection for the selection Output(s): Collection [Passthrough] - GeometryCollection for the selection TransformSelection - Array of the selected bone indices |
| [CollectionTransformSelectContact](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectContact) | CollectionTransformSelectContact (v1) Selects the contact(s) of the selected bones Input(s) : TransformSelection [Intrinsic] - Array of the selected bone indices Collection [Intrinsic] - GeometryCollection for the selection Output(s): TransformSelection [Passthrough] - Array of the selected bone indices Collection [Passthrough] - GeometryCollection for the selection |
| [CollectionTransformSelectCustom](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectCustom) | CollectionTransformSelectCustom (v2) Selects specified bones in the GeometryCollection by using a comma separated list, e.g. "0, 2, 5-10, 12-15" Input(s) : Collection [Intrinsic] - GeometryCollection for the selection Output(s): Collection [Passthrough] - GeometryCollection for the selection TransformSelection - Array of the selected bone indices |
| [CollectionTransformSelectInBox](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectInBox) | CollectionTransformSelectInBox (v1) Selects bones if their Vertices/BoundingBox/Centroid in a box Input(s) : Collection [Intrinsic] - GeometryCollection for the selection Box [Intrinsic] - Box to contain Vertices/BoundingBox/Centroid Output(s): Collection [Passthrough] - GeometryCollection for the selection TransformSelection - Array of the selected bone indices |
| [CollectionTransformSelectInSphere](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectInSphere) | CollectionTransformSelectInSphere (v1) Selects bones if their Vertices/BoundingBox/Centroid in a sphere Input(s) : Collection [Intrinsic] - GeometryCollection for the selection Sphere [Intrinsic] - Sphere to contain Vertices/BoundingBox/Centroid Output(s): Collection [Passthrough] - GeometryCollection for the selection TransformSelection - Array of the selected bone indices |
| [CollectionTransformSelectionInfo](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectionInfo) | CollectionTransformSelectionInfo (v1) Generates a formatted string of the bones and the selection Input(s) : TransformSelection [Intrinsic] - Array of the selected bone indices Collection - GeometryCollection for the selection Output(s): String - Formatted string of the bones and selection |
| [CollectionTransformSelectLeaf](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectLeaf) | CollectionTransformSelectLeaf (v1) Selects the leaves in the Collection Input(s) : Collection [Intrinsic] - GeometryCollection for the selection Output(s): Collection [Passthrough] - GeometryCollection for the selection TransformSelection - Array of the selected bone indices |
| [CollectionTransformSelectNone](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectNone) | CollectionTransformSelectNone (v1) Generates an empty bone selection for the Collection Input(s) : Collection [Intrinsic] - GeometryCollection for the selection Output(s): Collection [Passthrough] - GeometryCollection for the selection TransformSelection - Array of the selected bone indices |
| [CollectionTransformSelectParent](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectParent) | CollectionTransformSelectParent (v1) Selects the parents of the currently selected bones Input(s) : TransformSelection [Intrinsic] - Array of the selected bone indices Collection [Intrinsic] - GeometryCollection for the selection Output(s): TransformSelection [Passthrough] - Array of the selected bone indices Collection [Passthrough] - GeometryCollection for the selection |
| [CollectionTransformSelectRandom](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectRandom) | CollectionTransformSelectRandom (v1) Selects bones randomly in the Collection Input(s) : RandomSeed - Seed for the random generation, only used if Deterministic is on RandomThreshold - Bones get selected if RandomValue > RandomThreshold Collection [Intrinsic] - GeometryCollection for the selection Output(s): Collection [Passthrough] - GeometryCollection for the selection TransformSelection - Array of the selected bone indices |
| [CollectionTransformSelectRoot](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectRoot) | CollectionTransformSelectRoot (v1) Selects the root bones in the Collection Input(s) : Collection [Intrinsic] - GeometryCollection for the selection Output(s): Collection [Passthrough] - GeometryCollection for the selection TransformSelection - Array of the selected bone indices |
| [CollectionTransformSelectSameLevel](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectSameLevel) | CollectionTransformSelectSameLevel (v1) Expand the selection to include all nodes with the same level as the selected nodes Input(s) : TransformSelection [Intrinsic] - Array of the selected bone indices Collection [Intrinsic] - GeometryCollection for the selection Output(s): TransformSelection [Passthrough] - Array of the selected bone indices Collection [Passthrough] - GeometryCollection for the selection |
| [CollectionTransformSelectSiblings](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectSiblings) | CollectionTransformSelectSiblings (v1) Selects the siblings of the selected bones Input(s) : TransformSelection [Intrinsic] - Array of the selected bone indices Collection [Intrinsic] - GeometryCollection for the selection Output(s): TransformSelection [Passthrough] - Array of the selected bone indices Collection [Passthrough] - GeometryCollection for the selection |
| [CollectionTransformSelectTargetLevel](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionTransformSelectTargetLevel) | CollectionTransformSelectTargetLevel (v1) Selects the root bones in the Collection Input(s) : Collection [Intrinsic] - GeometryCollection for the selection TargetLevel - Level to select Output(s): Collection [Passthrough] - GeometryCollection for the selection TransformSelection - Array of the selected bone indices |

### GeometryCollection|Selection|Vertex

| Node | Description |
| --- | --- |
| [CollectionVertexSelectByPercentage](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionVertexSelectByPercentage) | CollectionVertexSelectByPercentage (v1) Outputs the specified percentage of the selected vertices Input(s) : VertexSelection [Intrinsic] - Array of the selected bone indices RandomSeed - Seed value for the random generation Output(s): VertexSelection [Passthrough] - Array of the selected bone indices |
| [CollectionVertexSelectCustom](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionVertexSelectCustom) | CollectionVertexSelectCustom (v1) Selects specified vertices in the GeometryCollection by using a space separated list Input(s) : Collection [Intrinsic] - GeometryCollection for the selection Output(s): Collection [Passthrough] - GeometryCollection for the selection VertexSelection - Vertex selection including the new indices |

### GeometryCollection|Texture

| Node | Description |
| --- | --- |
| [BakeTextureFromCollection](/documentation/en-us/unreal-engine/node-reference/Dataflow/BakeTextureFromCollection) | BakeTextureFromCollection (v1)  *Bake a texture from a geometry collection*  Output to a 4 channels Image object ( RGBA ) Input(s) : Collection [Intrinsic] - Target Collection FaceSelection - selection of faces to bake : if not connected, all faces will be used Resolution - resolution of the image to bake GutterSize - Approximate space to leave between UV islands, measured in texels UVChannel - Index of the added UV channel MaxDistance - Max distance to search for the outer mesh surface OcclusionRays - Number of occlusion rays OcclusionBlurRadius - Pixel Radius of Gaussian Blur Kernel applied to AO map (0 will apply no blur) CurvatureBlurRadius - Pixel Radius of Gaussian Blur Kernel applied to Curvature map (0 will apply no blur) VoxelResolution - Voxel resolution of smoothed shape representation SmoothingIterations - Amount of smoothing iterations to apply before computing curvature ThicknessFactor - Distance to search for correspondence between fractured shape and smoothed shape, as factor of voxel size MaxCurvature - Curvatures in the range [-MaxCurvature, MaxCurvature] will be mapped from [0,1]. |

### GeometryCollection|Utilities

| Node | Description |
| --- | --- |
| [AddCustomCollectionAttribute](/documentation/en-us/unreal-engine/node-reference/Dataflow/AddCustomCollectionAttribute) | AddCustomCollectionAttribute (v1) Adds custom attribute to Collection Input(s) : Collection [Intrinsic] - Collection for the custom attribute Output(s): Collection [Passthrough] - Collection for the custom attribute |
| [ClearConvexHulls](/documentation/en-us/unreal-engine/node-reference/Dataflow/ClearConvexHulls) | ClearConvexHulls (v1) Clear convex hulls from a collection Input(s) : TransformSelection - [Optional] selection of transforms to clear convex on, if not set all the transform will be used |
| [CollectionToPoints](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionToPoints) | CollectionToPoints (v1) Get vertices from a collection as a point cloud Input(s) : Collection [Intrinsic] - Collection storing the points Output(s): Collection [Passthrough] - Collection storing the points Points - Points from the collection |
| [CreateLeafConvexHulls](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateLeafConvexHulls) | CreateLeafConvexHulls (v1) Create Leaf Convex Hulls Dataflow Node Input(s) : OptionalSelectionFilter - Optional transform selection to compute leaf hulls on -- if not provided, all leaf hulls will be computed. |
| [CreateNonOverlappingConvexHulls](/documentation/en-us/unreal-engine/node-reference/Dataflow/CreateNonOverlappingConvexHulls) | CreateNonOverlappingConvexHulls (v1) Generates convex hull representation for the bones for simulation Input(s) : CanExceedFraction - Fraction (of geometry volume) by which a cluster's convex hull volume can exceed the actual geometry volume before instead using the hulls of the children. |
| [GenerateClusterConvexHullsFromChildrenHulls](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateClusterConvexHullsFromChildrenHulls) | GenerateClusterConvexHullsFromChildrenHulls (v1) Generates cluster convex hulls for children hulls Input(s) : ConvexCount - Maximum number of convex to generate for a specific cluster. |
| [GenerateClusterConvexHullsFromLeafHulls](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateClusterConvexHullsFromLeafHulls) | GenerateClusterConvexHullsFromLeafHulls (v1) Generates cluster convex hulls for leafs hulls Input(s) : ConvexCount - Maximum number of convex to generate for a specific cluster. |
| [GetBoundingBoxesFromCollection](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetBoundingBoxesFromCollection) | GetBoundingBoxesFromCollection (v1) Gets BoundingBoxes of pieces from a Collection Input(s) : Collection - Input Collection TransformSelection - The BoundingBoxes will be output for the bones selected in the TransformSelection Output(s): BoundingBoxes - Output BoundingBoxes |
| [GetCentroidsFromCollection](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetCentroidsFromCollection) | GetCentroidsFromCollection (v1) Gets centroids of pieces from a Collection Input(s) : Collection - Input Collection TransformSelection - The centroids will be output for the bones selected in the TransformSelection Output(s): Centroids - Output centroids Levels - Hidden output to store computed level values for centroids |
| [GetCollectionAttributeDataTyped](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetCollectionAttributeDataTyped) | GetCollectionAttributeDataTyped (v1) Get attribute data from a Collection Input(s) : Collection [Intrinsic] - Collection for the custom attribute AttributeKey - Input to drive the Attribute and Group name Output(s): BoolAttributeData - Bool type attribute data FloatAttributeData - Float type attribute data DoubleAttributeData - Float type attribute data Int32AttributeData - Int type attribute data StringAttributeData - Int type attribute data Vector3fAttributeData - Vector3f type attribute data Vector3dAttributeData - Vector3d type attribute data LinearColorAttributeData - Vector3d type attribute data |
| [GetConvexHullVolume](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetConvexHullVolume) | GetConvexHullVolume (v1) Get the sum of volumes of the convex hulls on the selected nodes Input(s) : TransformSelection [Intrinsic] - The transforms to consider Output(s): Volume - Sum of convex hull volumes |
| [GetNumElementsInCollectionGroup](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetNumElementsInCollectionGroup) | GetNumElementsInCollectionGroup (v1) Returns number of elements in a group in a Collection Input(s) : Collection [Intrinsic] - Collection for the custom attribute Output(s): NumElements - Number of elements for the attribute |
| [GetRootIndexFromCollection](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetRootIndexFromCollection) | GetRootIndexFromCollection (v1) Get the root node index |
| [GetSchema](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetSchema) | GetSchema (v1) Collects group and attribute information from the Collection and outputs it into a formatted string Input(s) : Collection - GeometryCollection for the information Output(s): String - Formatted string containing the groups and attributes |
| [MakeConvexDecompositionSettings](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeConvexDecompositionSettings) | MakeConvexDecompositionSettings (v1) Provide settings for running convex decomposition of geometry Input(s) : MinSizeToDecompose - If greater than zero, the minimum geometry size (cube root of volume) to consider for convex decomposition MaxGeoToHullVolumeRatioToDecompose - If the geo volume / hull volume ratio is greater than this, do not consider convex decomposition ErrorTolerance - Stop splitting when hulls have error less than this (expressed in cm; will be cubed for volumetric error). |
| [MergeConvexHulls](/documentation/en-us/unreal-engine/node-reference/Dataflow/MergeConvexHulls) | MergeConvexHulls (v1) Merge convex hulls on transforms with multiple hulls Input(s) : MaxConvexCount - Maximum number of convex to generate per transform. |
| [PointsToCollection](/documentation/en-us/unreal-engine/node-reference/Dataflow/PointsToCollection) | PointsToCollection (v1) Add point cloud to a collection as vertices Input(s) : Collection [Intrinsic] - Collection to add the points to Points - Points to add to the collection Output(s): Collection [Passthrough] - Collection to add the points to |
| [Proximity](/documentation/en-us/unreal-engine/node-reference/Dataflow/Proximity) | Proximity (v1) Update the proximity (contact) graph for the bones in a Collection Input(s) : DistanceThreshold - If hull-based proximity detection is enabled, amount to expand hulls when searching for overlapping neighbors ContactThreshold - If greater than zero, proximity will be additionally filtered by a 'contact' threshold, in cm, to exclude grazing / corner proximity Collection [Intrinsic] - GeometryCollection to update the proximity graph on Output(s): Collection [Passthrough] - GeometryCollection to update the proximity graph on |
| [RemoveOnBreak](/documentation/en-us/unreal-engine/node-reference/Dataflow/RemoveOnBreak) | RemoveOnBreak (v1) Remove on Break Dataflow Node Input(s) : Collection [Intrinsic] - Collection to set theremoval data on TransformSelection - selection to apply the data on ( if not specified the entire collection will be set ) bEnabledRemoval - Whether or not to enable the removal on the selection PostBreakTimer - How long after the break the removal will start ( Min / Max ) RemovalTimer - How long removal will last ( Min / Max ) bClusterCrumbling - If applied to a cluster this will cause the cluster to crumble upon removal, otherwise will have no effect Output(s): Collection [Passthrough] - Collection to set theremoval data on |
| [SetAnchorState](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetAnchorState) | SetAnchorState (v1) Sets the anchored state on the selected bones in a Collection Input(s) : Collection [Intrinsic] - GeometryCollection to set anchor state on TransformSelection [Intrinsic] - Bone selection for setting the state on Output(s): Collection [Passthrough] - GeometryCollection to set anchor state on |
| [SetCollectionAttributeDataTyped](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetCollectionAttributeDataTyped) | SetCollectionAttributeDataTyped (v1) Set attribute data in a Collection Input(s) : Collection [Intrinsic] - Collection for the custom attribute AttributeKey - Input to drive the Attribute and Group name BoolAttributeData - Bool type attribute data FloatAttributeData - Float type attribute data DoubleAttributeData - Float type attribute data Int32AttributeData - Int type attribute data StringAttributeData - Int type attribute data Vector3fAttributeData - Vector3f type attribute data Vector3dAttributeData - Vector3d type attribute data LinearColorAttributeData - LinearColor type attribute data Output(s): Collection [Passthrough] - Collection for the custom attribute |
| [SetDynamicState](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetDynamicState) | SetDynamicState (v1) Sets the dynamic state on the selected bones in a Collection Input(s) : Collection [Intrinsic] - GeometryCollection to set anchor state on TransformSelection [Intrinsic] - Bone selection for setting the state on Output(s): Collection [Passthrough] - GeometryCollection to set anchor state on |
| [SetPivot](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetPivot) | SetPivot (v1) Sets pivot for Collection Input(s) : Collection [Intrinsic] - Collection for the pivot change Transform - Pivot transform Output(s): Collection [Passthrough] - Collection for the pivot change |
| [SimplifyConvexHulls](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimplifyConvexHulls) | SimplifyConvexHulls (v1) Simplify Convex Hulls Dataflow Node Input(s) : OptionalSelectionFilter - Optional transform selection to compute leaf hulls on -- if not provided, all leaf hulls will be computed. |
| [SpheresToPoints](/documentation/en-us/unreal-engine/node-reference/Dataflow/SpheresToPoints) | SpheresToPoints (v1) Outputs Spheres as Points and radius values Output(s): Points - Centers of the spheres Radii - Radius values |
| [UpdateVolumeAttributes](/documentation/en-us/unreal-engine/node-reference/Dataflow/UpdateVolumeAttributes) | UpdateVolumeAttributes (v1) Update the Volume and Size attributes on the target Collection (and add them if they were not present) |

### GeometryCollection|UV

| Node | Description |
| --- | --- |
| [AddUVChannel](/documentation/en-us/unreal-engine/node-reference/Dataflow/AddUVChannel) | AddUVChannel (v1)  *Add a new UV channel to the collection*  note that there's a maximum of 8 channels that can be handled by a collection Input(s) : Collection [Intrinsic] - Target Collection Output(s): Collection [Passthrough] - Target Collection UVChannel - Index of the added UV channel |
| [AutoUnwrapUV](/documentation/en-us/unreal-engine/node-reference/Dataflow/AutoUnwrapUV) | AutoUnwrapUV (v1) Auto unwrap UVs for a specific UV channel Input(s) : Collection [Intrinsic] - Target Collection FaceSelection - Faces to auto unwrap, no selection means all faces UVChannel - UV channel to unwrap into ( 0 by default ) GutterSize - Approximate space to leave between UV islands, measured in texels for 512x512 texture Output(s): Collection [Passthrough] - Target Collection UVChannel [Passthrough] - UV channel to unwrap into ( 0 by default ) |
| [BoxProjectUV](/documentation/en-us/unreal-engine/node-reference/Dataflow/BoxProjectUV) | BoxProjectUV (v1) Generates UVs using a box projection Input(s) : Collection [Intrinsic] - Target Collection UVChannel - UV channel to unwrap into ( 0 by default ) GutterSize - Approximate space to leave between UV islands, measured in texels for 512x512 texture Output(s): Collection [Passthrough] - Target Collection UVChannel [Passthrough] - UV channel to unwrap into ( 0 by default ) |
| [MergeUVIslands](/documentation/en-us/unreal-engine/node-reference/Dataflow/MergeUVIslands) | MergeUVIslands (v1) Merge adjacent UV Islands with similar normals for a specific UV channel Input(s) : Collection [Intrinsic] - Target Collection FaceSelection - Faces to auto unwrap, no selection means all faces UVChannel - UV channel to unwrap into ( 0 by default ) AreaDistortionThreshold - Threshold for allowed area distortion from merging islands (when we use ExpMap to compute new UVs for the merged island) MaxNormalDeviationDeg - Threshold for allowed normal deviation between merge-able islands NormalSmoothingRounds - Amount of normal smoothing to apply when computing new UVs for merged islands. |

### Groom

| Node | Description |
| --- | --- |
| [AttachCurveRoots](/documentation/en-us/unreal-engine/node-reference/Dataflow/AttachCurveRoots) | AttachCurveRoots (v1) Experimental Attach the curve roots by setting their kinematic weights to 1.0f Input(s) : Collection - Managed array collection to be used to store datas CurveSelection - Curve selection to focus the geometry transfer spatially Output(s): Collection [Passthrough] - Managed array collection to be used to store datas KinematicWeightsKey - Vertex kinematic weights key to be used in other nodes if necessary |
| [BuildCurveLODs](/documentation/en-us/unreal-engine/node-reference/Dataflow/BuildCurveLODs) | BuildCurveLODs (v1) Experimental Builds the curves LODs Input(s) : Collection - Managed array collection to be used to store data CurveSelection - Curve selection to focus the geometry LODs spatially Output(s): Collection [Passthrough] - Managed array collection to be used to store data CurveParentsKey - Curve parent indices key to be used in other nodes if necessary CurveLodsKey - Curve lods indices key to be used in other nodes if necessary |
| [BuildCurveWeights](/documentation/en-us/unreal-engine/node-reference/Dataflow/BuildCurveWeights) | BuildCurveWeights (v1) Experimental Build a weight map that will be identical on every curves Input(s) : Collection - Managed array collection to be used to store datas CurveSelection - Curve selection to focus the geometry transfer spatially WeightsAttribute - Vertex kinematic weights key to be used in other nodes if necessary Output(s): Collection [Passthrough] - Managed array collection to be used to store datas |
| [BuildSplineSkinWeights](/documentation/en-us/unreal-engine/node-reference/Dataflow/BuildSplineSkinWeights) | BuildSplineSkinWeights (v1) Experimental Build spline skinning data from skeletal mesh Input(s) : Collection - Managed array collection to be used to store datas VertexSelection - Vertex selection to focus the geometry transfer spatially SkeletalMesh - SkeletalMesh used to compute spline skinning weights. |
| [GenerateCurveGeometry](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateCurveGeometry) | GenerateCurveGeometry (v1) Experimental Build the curve geometry from a collection containing curves Input(s) : Collection - Managed array collection to be used to store datas SourceCurves - Managed array collection to be used to store datas CurveSelection - Curve selection to focus the curves generation spatially CurveCount - Max number of guides Output(s): Collection [Passthrough] - Managed array collection to be used to store datas |
| [GetCurveAttributes](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetCurveAttributes) | GetCurveAttributes (v1) Experimental Get the kinematic weights attributes names Output(s): AttributeKey - Attribute key to build |
| [GetGroomAsset](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetGroomAsset) | GetGroomAsset (v2) Experimental Get the groom asset Output(s): GroomAsset - Groom asset that will be used in the dataflow graph |
| [GroomAssetTerminal](/documentation/en-us/unreal-engine/node-reference/Dataflow/GroomAssetTerminal) | GroomAssetTerminal (v2) Experimental Groom Asset Terminal Dataflow Node V 2 |
| [GroomAssetToCollection](/documentation/en-us/unreal-engine/node-reference/Dataflow/GroomAssetToCollection) | GroomAssetToCollection (v1) Experimental Transform a groom asset to a collection Input(s) : GroomAsset - Input asset to read the guides from CurvesType - Type of curves to use to fill the groom collection (guides/strands) CurvesThickness - Curves thickness for geometry generation Output(s): Collection - Managed array collection used to store the curves |
| [LinearToSplineSkinWeights](/documentation/en-us/unreal-engine/node-reference/Dataflow/LinearToSplineSkinWeights) | LinearToSplineSkinWeights (v1) Experimental Convert linear skinning data to spline skinning data Input(s) : Collection - Managed array collection to be used to store datas VertexSelection - Vertex selection to process vertices subset Output(s): Collection [Passthrough] - Managed array collection to be used to store datas SplineParamKey - Spline skinning parameter key SplineBonesKey - Spline bones key. |
| [ResampleCurvePoints](/documentation/en-us/unreal-engine/node-reference/Dataflow/ResampleCurvePoints) | ResampleCurvePoints (v1) Experimental Resample the curves with a fixed number of points Input(s) : Collection - Managed array collection to be used to store datas CurveSelection - Curve selection to focus the guides generation spatially NumPoints - Max number of points (to be able to plug into a variable since enum is not supported in dataflow) Output(s): Collection [Passthrough] - Managed array collection to be used to store datas |
| [SmoothCurvePoints](/documentation/en-us/unreal-engine/node-reference/Dataflow/SmoothCurvePoints) | SmoothCurvePoints (v1) Experimental Smooth the curves for more stable deformation Input(s) : Collection - Managed array collection to be used to store data CurveSelection - Curve selection to focus the guides smoothing spatially SmoothingFactor - Smoothing factor between 0 and 1 Output(s): Collection [Passthrough] - Managed array collection to be used to store data |
| [SplineToLinearSkinWeights](/documentation/en-us/unreal-engine/node-reference/Dataflow/SplineToLinearSkinWeights) | SplineToLinearSkinWeights (v1) Experimental Convert spline skinning data to linear data Input(s) : Collection - Managed array collection to be used to store datas VertexSelection - Vertex selection to process vertices subset SplineParamKey - Spline skinning parameter key SplineBonesKey - Spline bones key. |
| [TransferLinearSkinWeights](/documentation/en-us/unreal-engine/node-reference/Dataflow/TransferLinearSkinWeights) | TransferLinearSkinWeights (v1) Experimental Build the curves skinning by transferring the indices weights from a skelmesh geometry Input(s) : Collection - Managed array collection to be used to store datas VertexSelection - Vertex selection to focus the geometry transfer spatially SkeletalMesh - SkeletalMesh used to transfer the skinning weights. |

### Image

| Node | Description |
| --- | --- |
| [ImageCombineChannels](/documentation/en-us/unreal-engine/node-reference/Dataflow/ImageCombineChannels) | ImageCombineChannels (v1) Combine channels into a single RGBA image Outputs are single channel images Input(s) : Red - Red channel - if not connected, use black color Green - Green channel - if not connected, use black color Blue - Blue channel - if not connected, use black color Alpha - Alpha channel - if not connected, use black color Output(s): Image - Output image recombined from input channels |
| [ImageFromColor](/documentation/en-us/unreal-engine/node-reference/Dataflow/ImageFromColor) | ImageFromColor (v1) Create a RGBA image from a single color at a specific resolution Outputs are single channel images Input(s) : FillColor - color to fill the image with Resolution - resolution of the output image Output(s): Image - Output image |
| [ImageSplitChannels](/documentation/en-us/unreal-engine/node-reference/Dataflow/ImageSplitChannels) | ImageSplitChannels (v1) Split a image in individual channels Outputs are single channel images Input(s) : Image - Input image to split per channel Output(s): Red - Red channel Green - Green channel Blue - Blue channel Alpha - Alpha channel |
| [ImageToTexture](/documentation/en-us/unreal-engine/node-reference/Dataflow/ImageToTexture) | ImageToTexture (v1) Create a transient texture asset from an image |
| [TextureToImage](/documentation/en-us/unreal-engine/node-reference/Dataflow/TextureToImage) | TextureToImage (v1) Experimental Import a texture asset as an image. |

### Materials

| Node | Description |
| --- | --- |
| [AddToMaterialArray](/documentation/en-us/unreal-engine/node-reference/Dataflow/AddToMaterialArray) | AddToMaterialArray (v1) Add material(s) to an array Input(s) : MaterialArray - Material array to add to Output(s): MaterialArray [Passthrough] - Material array to add to |
| [AssignMaterialToCollection](/documentation/en-us/unreal-engine/node-reference/Dataflow/AssignMaterialToCollection) | AssignMaterialToCollection (v1) Assign material to a set of face in a geometry collection Input(s) : Collection [Intrinsic] - Collection to assign material to FaceSelection - Faces that will be set with this material index, if no selection is connected , all faces will be set MaterialArray [Intrinsic] - Array holding the materials objects Material - Material to assign to the selection Output(s): Collection [Passthrough] - Collection to assign material to MaterialArray [Passthrough] - Array holding the materials objects MaterialIndex - Index where the material was set in the array |
| [GetMaterialAsset](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetMaterialAsset) | GetMaterialAsset (v1) Get a material interface from an existing asset Output(s): Material - Material asset to get |
| [MakeMaterialArray](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeMaterialArray) | MakeMaterialArray (v1) Make a array from a user defined list of material objects Output(s): MaterialArray - Material array set by the user |
| [MaterialInterfaceTextureOverride](/documentation/en-us/unreal-engine/node-reference/Dataflow/MaterialInterfaceTextureOverride) | MaterialInterfaceTextureOverride (v1) Experimental Duplicate the given material and replace the target texture with the override texture on the newly-created material |
| [SetIntoMaterialsArray](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetIntoMaterialsArray) | SetIntoMaterialsArray (v1) Set an element into a material array at a specific index (if the index does not match the range of the array, the array will remain unchanged) Input(s) : MaterialArray [Intrinsic] - Material array to modify Material - Material to set at the specific index into the array Index - Index Set the material at (if the index does not match the range of the array, the array will remain unchanged) Output(s): MaterialArray [Passthrough] - Material array to modify |

### Math

| Node | Description |
| --- | --- |
| [MathExpression](/documentation/en-us/unreal-engine/node-reference/Dataflow/MathExpression) | MathExpression (v1) Expression node for floats |

### Math|Boolean

| Node | Description |
| --- | --- |
| [BooleanOperation](/documentation/en-us/unreal-engine/node-reference/Dataflow/BooleanOperation) | BooleanOperation (v1) Boolean operations Input(s) : bBoolA - Boolean input bBoolB - Boolean input Output(s): bResult - Boolean result of the operator |
| [MakeLiteralBool](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeLiteralBool) | MakeLiteralBool (v2) Make a bool value |

### Math|Compare

| Node | Description |
| --- | --- |
| [CompareFloat](/documentation/en-us/unreal-engine/node-reference/Dataflow/CompareFloat) | CompareFloat (v1) Comparison between floats Output(s): Result - Boolean result of the comparison |
| [CompareInt](/documentation/en-us/unreal-engine/node-reference/Dataflow/CompareInt) | CompareInt (v1) Comparison between integers Output(s): Result - Boolean result of the comparison |

### Math|Conversions

| Node | Description |
| --- | --- |
| [FloatArrayToIntArray](/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatArrayToIntArray) | FloatArrayToIntArray (v1) Converts a Float array to Int array using the specified method. |

### Math|Double

| Node | Description |
| --- | --- |
| [MakeLiteralDouble](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeLiteralDouble) | MakeLiteralDouble (v1) Make a double value |

### Math|Float

| Node | Description |
| --- | --- |
| [Division (Whole and Remainder)](/documentation/en-us/unreal-engine/node-reference/Dataflow/DivisionWholeandRemainder) | Division (Whole and Remainder) (v1) Division Dataflow Node |
| [EFit](/documentation/en-us/unreal-engine/node-reference/Dataflow/EFit) | EFit (v1) Fits a value from one range to another Takes the value num from the range (oldmin, oldmax) and shifts it to the corresponding value in the new range (newmin, newmax). |
| [Fit](/documentation/en-us/unreal-engine/node-reference/Dataflow/Fit) | Fit (v1) Fits a value from one range to another Returns a number between newmin and newmax that is relative to num in the range between oldmin and oldmax. |
| [FloatArrayNormalize](/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatArrayNormalize) | FloatArrayNormalize (v1) Normalize the selected float data in a FloatArray Input(s) : InFloatArray [Intrinsic] - Input VectorArray Selection - Selection for the operation |
| [FloatMathExpression](/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatMathExpression) | FloatMathExpression (v1) Expression node for floats |
| [Lerp](/documentation/en-us/unreal-engine/node-reference/Dataflow/Lerp) | Lerp (v1) Linearly interpolates between A and B based on Alpha. |
| [MakeFloatArray](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeFloatArray) | MakeFloatArray (v1) M Input(s) : NumElements - Number of elements of the array Value - Value to initialize the array with Output(s): FloatArray - Output float array |
| [MakeLiteralFloat](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeLiteralFloat) | MakeLiteralFloat (v2) Make a float value |
| [NormalizeToRange](/documentation/en-us/unreal-engine/node-reference/Dataflow/NormalizeToRange) | NormalizeToRange (v1) Returns Float normalized to the given range |
| [Wrap](/documentation/en-us/unreal-engine/node-reference/Dataflow/Wrap) | Wrap (v1) Wrap Dataflow Node |

### Math|Int

| Node | Description |
| --- | --- |
| [MakeLiteralInt](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeLiteralInt) | MakeLiteralInt (v2) Make an integer value |

### Math|Random

| Node | Description |
| --- | --- |
| [RandomFloat](/documentation/en-us/unreal-engine/node-reference/Dataflow/RandomFloat) | RandomFloat (v1) Generates a random float |
| [RandomFloatInRange](/documentation/en-us/unreal-engine/node-reference/Dataflow/RandomFloatInRange) | RandomFloatInRange (v1) Generates a random float between Min and Max |
| [RandomUnitVector](/documentation/en-us/unreal-engine/node-reference/Dataflow/RandomUnitVector) | RandomUnitVector (v1) Returns a random vector with length of 1 |
| [RandomUnitVectorInCone](/documentation/en-us/unreal-engine/node-reference/Dataflow/RandomUnitVectorInCone) | RandomUnitVectorInCone (v1) Returns a random vector with length of 1, within the specified cone, with uniform random distribution Input(s) : ConeDirection - The base "center" direction of the cone ConeHalfAngle - The half-angle of the cone (from ConeDir to edge), in degrees |

### Math|Scalar

| Node | Description |  |  |
| --- | --- | --- | --- |
| [Abs](/documentation/en-us/unreal-engine/node-reference/Dataflow/Abs) | Abs (v1) Absolute value ( | A | ) |
| [Add](/documentation/en-us/unreal-engine/node-reference/Dataflow/Add) | Add (v1) Addition (A + B) |  |  |
| [Ceil](/documentation/en-us/unreal-engine/node-reference/Dataflow/Ceil) | Ceil (v1) Ceil ( 1.4 => 2.0 | 1.9 => 2.0 | -5.3 => -5.0) |
| [Clamp](/documentation/en-us/unreal-engine/node-reference/Dataflow/Clamp) | Clamp (v1) Clamp(A, Min, Max) clamp a value to specific range (inclusive) |  |  |
| [Constants](/documentation/en-us/unreal-engine/node-reference/Dataflow/Constants) | Constants (v1) Math constants ( see EDataflowMathConstantsEnum ) |  |  |
| [Cube](/documentation/en-us/unreal-engine/node-reference/Dataflow/Cube) | Cube (v1) Cube ( A  *A*  A ) |  |  |
| [Divide](/documentation/en-us/unreal-engine/node-reference/Dataflow/Divide) | Divide (v1) Division (A / B) if B is equal to 0, 0 is returned Fallback value |  |  |
| [Exp](/documentation/en-us/unreal-engine/node-reference/Dataflow/Exp) | Exp (v1) Exponential ( Exp(A) ) |  |  |
| [Floor](/documentation/en-us/unreal-engine/node-reference/Dataflow/Floor) | Floor (v1) Floor ( 1.4 => 1.0 | 1.9 => 1.0 | -5.3 => -6.0 ) |
| [Frac](/documentation/en-us/unreal-engine/node-reference/Dataflow/Frac) | Frac (v1) Frac ( 1.4 => 0.4 | 1.9 => 0.9 | -5.3 => 0.3 ) |
| [InverseSquareRoot](/documentation/en-us/unreal-engine/node-reference/Dataflow/InverseSquareRoot) | InverseSquareRoot (v1) Inverse Square Root ( 1 / sqrt(A) ) if A is equal to 0, returns Fallback |  |  |
| [Log](/documentation/en-us/unreal-engine/node-reference/Dataflow/Log) | Log (v1) Natural log ( Log(A) ) |  |  |
| [LogX](/documentation/en-us/unreal-engine/node-reference/Dataflow/LogX) | LogX (v1) Log for a specific base ( Log[Base](A) ) If base is negative or zero returns 0 |  |  |
| [Maximum](/documentation/en-us/unreal-engine/node-reference/Dataflow/Maximum) | Maximum (v2) Maximum ( Max(A, B, C, ... ) ) |  |  |
| [Minimum](/documentation/en-us/unreal-engine/node-reference/Dataflow/Minimum) | Minimum (v2) Minimum ( Min(A, B, C, ... ) ) |  |  |
| [Multiply](/documentation/en-us/unreal-engine/node-reference/Dataflow/Multiply) | Multiply (v1) Multiplication (A \* B) |  |  |
| [Negate](/documentation/en-us/unreal-engine/node-reference/Dataflow/Negate) | Negate (v1) Negate ( -A ) |  |  |
| [OneMinus](/documentation/en-us/unreal-engine/node-reference/Dataflow/OneMinus) | OneMinus (v1) One minus (1 - A) |  |  |
| [Pow](/documentation/en-us/unreal-engine/node-reference/Dataflow/Pow) | Pow (v1) power ( A ^ B) |  |  |
| [Reciprocal](/documentation/en-us/unreal-engine/node-reference/Dataflow/Reciprocal) | Reciprocal (v1) Reciprocal( 1 / A ) if A is equal to 0, returns Fallback |  |  |
| [Round](/documentation/en-us/unreal-engine/node-reference/Dataflow/Round) | Round (v1) Round ( 1.4 => 1.0 | 1.9 => 2.0 | -5.3 => -5.0) |
| [Sign](/documentation/en-us/unreal-engine/node-reference/Dataflow/Sign) | Sign (v1) return -1, 0, +1 whether the input is respectively negative, zero or positive ( Sign(A) ) |  |  |
| [Square](/documentation/en-us/unreal-engine/node-reference/Dataflow/Square) | Square (v1) Square ( A \* A ) |  |  |
| [SquareRoot](/documentation/en-us/unreal-engine/node-reference/Dataflow/SquareRoot) | SquareRoot (v1) Square Root ( sqrt(A) ) |  |  |
| [Subtract](/documentation/en-us/unreal-engine/node-reference/Dataflow/Subtract) | Subtract (v1) Subtraction (A - B) |  |  |
| [Trunc](/documentation/en-us/unreal-engine/node-reference/Dataflow/Trunc) | Trunc (v1) Trunc ( 1.4 => 1.0 | 1.9 => 1.0 | -5.3 => -5.0) |

### Math|Transform

| Node | Description |
| --- | --- |
| [BakeTransformsInCollection](/documentation/en-us/unreal-engine/node-reference/Dataflow/BakeTransformsInCollection) | BakeTransformsInCollection (v1) Bake transforms in Collection Input(s) : Collection [Intrinsic] - Collection to bake transforms in Output(s): Collection [Passthrough] - Collection to bake transforms in |
| [BreakTransform](/documentation/en-us/unreal-engine/node-reference/Dataflow/BreakTransform) | BreakTransform (v1) Break a Transform into Translation, Rotation (Euler, Rotator, Quaternion), Scale Input(s) : Transform - Transform to break into components Output(s): Translation - Translation Rotation - Rotation as Euler Rotator - Rotation as a rotator Quat - Rotation as a quaternion Scale - Scale |
| [InvertTransform](/documentation/en-us/unreal-engine/node-reference/Dataflow/InvertTransform) | InvertTransform (v1) Invert a transform. |
| [MultiplyTransform](/documentation/en-us/unreal-engine/node-reference/Dataflow/MultiplyTransform) | MultiplyTransform (v1) Description for this node |
| [TransformCollection](/documentation/en-us/unreal-engine/node-reference/Dataflow/TransformCollection) | TransformCollection (v1) Transforms a Collection Input(s) : Collection [Intrinsic] - Output mesh TransformSelection - Transform selection for transforming Translate - Translation Rotate - Rotation Scale - Scale Output(s): Collection [Passthrough] - Output mesh |
| [TransformMesh](/documentation/en-us/unreal-engine/node-reference/Dataflow/TransformMesh) | TransformMesh (v1) Transforms a mesh Input(s) : Mesh [Intrinsic] - Output mesh Translate - Translation Rotate - Rotation Scale - Scale UniformScale - Uniform scale ScalePivot - Pivot for the scale bInvertTransformation - Invert the transformation Output(s): Mesh [Passthrough] - Output mesh |

### Math|Trig

| Node | Description |
| --- | --- |
| [ArcCos](/documentation/en-us/unreal-engine/node-reference/Dataflow/ArcCos) | ArcCos (v1) ArcCos(A) returns a value in radians |
| [ArcSin](/documentation/en-us/unreal-engine/node-reference/Dataflow/ArcSin) | ArcSin (v1) ArcSin(A) returns a value in radians |
| [ArcTan](/documentation/en-us/unreal-engine/node-reference/Dataflow/ArcTan) | ArcTan (v1) ArcTan(A) returns a value in radians |
| [ArcTan2](/documentation/en-us/unreal-engine/node-reference/Dataflow/ArcTan2) | ArcTan2 (v1) ArcTan2(A, B) returns a value in radians |
| [Cos](/documentation/en-us/unreal-engine/node-reference/Dataflow/Cos) | Cos (v1) Cos(A) with A in radians |
| [DegToRad](/documentation/en-us/unreal-engine/node-reference/Dataflow/DegToRad) | DegToRad (v1) DegToRad(A) convert degrees to radians |
| [RadToDeg](/documentation/en-us/unreal-engine/node-reference/Dataflow/RadToDeg) | RadToDeg (v1) RadToDeg(A) convert radians to degrees |
| [Sin](/documentation/en-us/unreal-engine/node-reference/Dataflow/Sin) | Sin (v1) Sin(A) with A in radians |
| [Tan](/documentation/en-us/unreal-engine/node-reference/Dataflow/Tan) | Tan (v1) Tan(A) with A in radians |

### Math|Utilities

| Node | Description |
| --- | --- |
| [IsNearlyZero](/documentation/en-us/unreal-engine/node-reference/Dataflow/IsNearlyZero) | IsNearlyZero (v1) Is Nearly Zero Dataflow Node |

### Math|Vector

| Node | Description |
| --- | --- |
| [MakeQuaternion](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeQuaternion) | MakeQuaternion (v1) Make Quaternion Dataflow Node |
| [VectorArrayNormalize](/documentation/en-us/unreal-engine/node-reference/Dataflow/VectorArrayNormalize) | VectorArrayNormalize (v1) Normalize all the selected vectors in a VectorArray Input(s) : InVectorArray [Intrinsic] - Input VectorArray Selection - Selection for the operation |

### Math|Vectors

| Node | Description |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [AddVector](/documentation/en-us/unreal-engine/node-reference/Dataflow/AddVector) | AddVector (v1) Add two vectors component wise : V = (A + B) Input(s) : A - A Vector operand B - B Vector operand Output(s): V - Add result V=A+B |  |  |  |  |  |  |  |  |
| [BreakVector](/documentation/en-us/unreal-engine/node-reference/Dataflow/BreakVector) | BreakVector (v1) Break a vector in 4 components if the input vector is of a lower dimension than 4, the remaining components will be set to zero Input(s) : V - Vector to break into components Output(s): X - X component Y - Y component Z - Z component W - W component |  |  |  |  |  |  |  |  |
| [DivideVector](/documentation/en-us/unreal-engine/node-reference/Dataflow/DivideVector) | DivideVector (v1) Multiply two vectors component wise: V = (A / B) When a component of B is zero, use the falback value as a return value for the specific component Input(s) : A - A Vector operand B - B Vector operand Fallback - Fallback Vector used when components of B are zero Output(s): V - Add result V=A\*B |  |  |  |  |  |  |  |  |
| [MakeVector2](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeVector2) | MakeVector2 (v1) Make a 2D Vector Input(s) : X - X component Y - Y component Output(s): Vector2D - 2D Vector {X, Y} |  |  |  |  |  |  |  |  |
| [MakeVector3](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeVector3) | MakeVector3 (v1) Make a 3D Vector Input(s) : X - X component Y - Y component Z - Z component Output(s): Vector3D - 3D Vector {X, Y, Z} |  |  |  |  |  |  |  |  |
| [MakeVector4](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeVector4) | MakeVector4 (v1) Make a 4D Vector Input(s) : X - X component Y - Y component Z - Z component W - W component Output(s): Vector4D - 4D Vector {X, Y, Z, W} |  |  |  |  |  |  |  |  |
| [MultiplyVector](/documentation/en-us/unreal-engine/node-reference/Dataflow/MultiplyVector) | MultiplyVector (v1) Multiply two vectors component wise: V = (A  *B) Input(s) : A - A Vector operand B - B Vector operand Output(s): V - Add result V=A*B |  |  |  |  |  |  |  |  |
| [NormalizeVector](/documentation/en-us/unreal-engine/node-reference/Dataflow/NormalizeVector) | NormalizeVector (v1) Normalize a vector : Normalized = V/ | V | Input(s) : V - Vector to normalize Output(s): Normalized - Normalized vector : Normalized=V/ | V |  |  |  |  |  |
| [ScaleVector](/documentation/en-us/unreal-engine/node-reference/Dataflow/ScaleVector) | ScaleVector (v1) Scale a vector by a scalar : Scaled = (V  *Scale) Input(s) : V - Vector to scale Scale - Scale factor Output(s): Scaled - Scaled vector : Scaled=(V*  Scale) |  |  |  |  |  |  |  |  |
| [SubtractVector](/documentation/en-us/unreal-engine/node-reference/Dataflow/SubtractVector) | SubtractVector (v1) Subtract two vectors component wise: V = (A - B) Input(s) : A - A Vector operand B - B Vector operand Output(s): V - Add result V=A-B |  |  |  |  |  |  |  |  |
| [VectorCrossProduct](/documentation/en-us/unreal-engine/node-reference/Dataflow/VectorCrossProduct) | VectorCrossProduct (v1) Compute the cross product of two vectors : CrossProduct = B^A This node only operates in 3 dimensions, inputs will be converted to a 3D vector internally and result will be a vector with a zero W component Input(s) : A - A Vector operand B - B Vector operand Output(s): CrossProduct - Resulting cross product of A and B : CrossProduct=B^A |  |  |  |  |  |  |  |  |
| [VectorDistance](/documentation/en-us/unreal-engine/node-reference/Dataflow/VectorDistance) | VectorDistance (v1) Compute the distance between two vectors : Distance = | B-A | Input(s) : A - A Vector operand B - B Vector operand Output(s): Distance - Distance between A and B : Distance= | B-A |  |  |  |  |  |
| [VectorDotProduct](/documentation/en-us/unreal-engine/node-reference/Dataflow/VectorDotProduct) | VectorDotProduct (v1) Compute the dot product between two vectors : DotProduct = A.B Input(s) : A - A Vector operand B - B Vector operand Output(s): DotProduct - Resulting dot product : DotProduct=A.B |  |  |  |  |  |  |  |  |
| [VectorLength](/documentation/en-us/unreal-engine/node-reference/Dataflow/VectorLength) | VectorLength (v1) Compute the Length of a vector : Length = | V | Input(s) : V - Vector to get length from Output(s): Length - Length of the input vector : Length= | V |  |  |  |  |  |
| [VectorSquaredLength](/documentation/en-us/unreal-engine/node-reference/Dataflow/VectorSquaredLength) | VectorSquaredLength (v1) Compute the Squared length of a vector : Length = | V |  | V | Input(s) : V - Vector to get squared length from Output(s): SquaredLength - Length of the input vector : SquaredLength = | V |  | V |  |

### Mesh

| Node | Description |
| --- | --- |
| [GetMeshBoundingBox](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetMeshBoundingBox) | GetMeshBoundingBox (v1) Get the local geometric bounding box a dynamic mesh Input(s) : Mesh - dynamic mesh to compute the bouning box from Output(s): BoundingBox - Geometric bounding box of the input dynamic mesh Center - Center of the resulting bounding box Dimensions - Dimensions of the resulting bounding box in centimers |

### Mesh|Utilities

| Node | Description |
| --- | --- |
| [AppendMeshesToCollection](/documentation/en-us/unreal-engine/node-reference/Dataflow/AppendMeshesToCollection) | AppendMeshesToCollection (v1) Append Array of Meshes to Collection Input(s) : Collection [Intrinsic] - Meshes will be appended to this collection Meshes - Dynamic Meshes to append ParentIndex - Index of parent bone for appended meshes. |
| [ApplyGeometryScriptToCollection](/documentation/en-us/unreal-engine/node-reference/Dataflow/ApplyGeometryScriptToCollection) | ApplyGeometryScriptToCollection (v1) Apply a Geometry Script Mesh Processors to the geometry of selected transforms in a geometry collection Input(s) : Collection [Intrinsic] - Input/Output mesh TransformSelection - Selected bones will have geometry script processing applied (if they have geometry). |
| [ApplyGeometryScriptToMesh](/documentation/en-us/unreal-engine/node-reference/Dataflow/ApplyGeometryScriptToMesh) | ApplyGeometryScriptToMesh (v1) Apply a Geometry Script Mesh Processors to an input UDynamicMesh Input(s) : Mesh [Intrinsic] - Input/Output mesh Output(s): Mesh [Passthrough] - Input/Output mesh |
| [BoxToMesh](/documentation/en-us/unreal-engine/node-reference/Dataflow/BoxToMesh) | BoxToMesh (v1) Converts a BoundingBox into a DynamicMesh Input(s) : Box [Intrinsic] - BoundingBox input Output(s): Mesh - Mesh output TriangleCount - Mesh triangle count |
| [CollectionSelectionToMeshes](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionSelectionToMeshes) | CollectionSelectionToMeshes (v1) Converts a Collection to a set of Dynamic Meshes per selected Transform Input(s) : Collection [Intrinsic] - Collection to convert TransformSelection - Geometry on or under selected bones will be converted to meshes, optionally after filtering the selection to leaves. |
| [CollectionToMesh](/documentation/en-us/unreal-engine/node-reference/Dataflow/CollectionToMesh) | CollectionToMesh (v1) Converts a Collection to a DynamicMesh Input(s) : Collection [Intrinsic] - Collection to convert TransformSelection - Geometry on or under selected bones will be appended to the output mesh. |
| [DataflowMeshAppend](/documentation/en-us/unreal-engine/node-reference/Dataflow/DataflowMeshAppend) | DataflowMeshAppend (v1) Combine two Dataflow meshes Input(s) : Mesh [Intrinsic] - Mesh input/output AppendMesh [Intrinsic] - Mesh to append Output(s): Mesh [Passthrough] - Mesh input/output |
| [DuplicateMeshUVChannelNode](/documentation/en-us/unreal-engine/node-reference/Dataflow/DuplicateMeshUVChannelNode) | DuplicateMeshUVChannelNode (v1) Create a new UV layer/channel in a UDataflowMesh Input(s) : Mesh [Intrinsic] - DataflowMesh input/output Output(s): Mesh [Passthrough] - DataflowMesh input/output NewUVChannel - Index of the added UV channel |
| [GetMeshData](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetMeshData) | GetMeshData (v1) Outputs Mesh data Input(s) : Mesh [Intrinsic] - Mesh for the data Output(s): VertexCount - Number of vertices EdgeCount - Number of edges TriangleCount - Number of triangles |
| [MakeDataflowMesh](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeDataflowMesh) | MakeDataflowMesh (v1) Create a UDataflow mesh from an input UDynamicMesh and material array Input(s) : InMesh [Intrinsic] - DynamicMesh input InMaterials [Intrinsic] - Materials input Output(s): Mesh - DataflowMesh output |
| [MeshAppend](/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshAppend) | MeshAppend (v1) Appends two meshes Input(s) : Mesh1 [Intrinsic] - Mesh input Mesh2 [Intrinsic] - Mesh input Output(s): Mesh - Output mesh |
| [MeshBoolean](/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshBoolean) | MeshBoolean (v1) Compute a Mesh Boolean between Mesh1 and Mesh2 Supported Boolean Operations: Union (Mesh1 + Mesh2) Difference (Mesh1 - Mesh2; removing what's inside of Mesh2 from Mesh1) Intersection (Mesh1 & Mesh2; removing what's outside of Mesh2 from Mesh1) Input(s) : Mesh1 [Intrinsic] - Mesh input Mesh2 [Intrinsic] - Mesh input Output(s): Mesh - Output mesh |
| [MeshInfo](/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshInfo) | MeshInfo (v1) Collects information from the DynamicMesh and outputs it into a formatted string Input(s) : Mesh [Intrinsic] - DynamicMesh for the information Output(s): InfoString - Formatted output string |
| [MeshToCollection](/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshToCollection) | MeshToCollection (v1) Converts a DynamicMesh to a Collection Input(s) : Mesh [Intrinsic] - DynamicMesh to convert bSplitIslands - Whether to split the mesh into multiple bones based on the mesh connectivity bAddClusterRootForSingleMesh - Whether to add a root cluster for the single mesh case. |
| [PointsToMesh](/documentation/en-us/unreal-engine/node-reference/Dataflow/PointsToMesh) | PointsToMesh (v1) Converts points into a DynamicMesh Input(s) : Points [Intrinsic] - Points input Output(s): Mesh - Mesh output TriangleCount - Mesh triangle count |
| [ScatterMeshes](/documentation/en-us/unreal-engine/node-reference/Dataflow/ScatterMeshes) | ScatterMeshes (v1) Copies the same mesh with scale onto points Input(s) : Points [Intrinsic] - Points to copy meshes onto MeshToCopy [Intrinsic] - Mesh to copy onto points Output(s): Mesh - merged result mesh Meshes - Result meshes as individual ones |
| [SkeletalMeshToMesh](/documentation/en-us/unreal-engine/node-reference/Dataflow/SkeletalMeshToMesh) | SkeletalMeshToMesh (v1) Experimental Converts a SkeletalMesh into a DynamicMesh with Imported Vertex information Input(s) : SkeletalMesh - SkeletalMesh to convert Output(s): Mesh - Output mesh MaterialArray - Output materials |
| [SplitDataflowMesh](/documentation/en-us/unreal-engine/node-reference/Dataflow/SplitDataflowMesh) | SplitDataflowMesh (v1) Split a UDataflow mesh into a UDynamicMesh and a material array Input(s) : InMesh [Intrinsic] - DataflowMesh input Output(s): Mesh - DyanmicMesh output MaterialArray - Materials output |
| [SplitMeshIslands](/documentation/en-us/unreal-engine/node-reference/Dataflow/SplitMeshIslands) | SplitMeshIslands (v1) Split a mesh into a connected islands Input(s) : Mesh [Intrinsic] - Mesh input Output(s): Meshes - Meshes output |
| [StaticMeshToMesh](/documentation/en-us/unreal-engine/node-reference/Dataflow/StaticMeshToMesh) | StaticMeshToMesh (v1) Converts a StaticMesh into a DynamicMesh Input(s) : StaticMesh - StaticMesh to convert Output(s): Mesh - Output mesh MaterialArray - Output materials |

### MeshResizing

| Node | Description |
| --- | --- |
| [AlignUVMeshNode](/documentation/en-us/unreal-engine/node-reference/Dataflow/AlignUVMeshNode) | AlignUVMeshNode (v1) Experimental Align UVMesh Node Input(s) : BaseUVChannelIndex - Base UV channel index in case it differs from the ResizingMesh UV channel index, or -1 to use the same channel. |
| [ApplyRBFResizing](/documentation/en-us/unreal-engine/node-reference/Dataflow/ApplyRBFResizing) | ApplyRBFResizing (v1) Experimental Apply the interpolation data calculated by GenerateRBFResizingWeights to resize a mesh. |
| [GenerateInterpolatedProxy](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateInterpolatedProxy) | GenerateInterpolatedProxy (v1) Experimental Generate a pair of Dynamic Meshes with the same topology that can be interpolated. |
| [GenerateRBFResizingWeights](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateRBFResizingWeights) | GenerateRBFResizingWeights (v1) Experimental Sample points and generate RBF Interpolation data for a given Source mesh. |
| [GenerateResizableProxy](/documentation/en-us/unreal-engine/node-reference/Dataflow/GenerateResizableProxy) | GenerateResizableProxy (v1) Experimental Generate a pair of Dynamic Meshes with the same topology that can be interpolated. |
| [GrowTileRegion](/documentation/en-us/unreal-engine/node-reference/Dataflow/GrowTileRegion) | GrowTileRegion (v1) Experimental Finds a square tile within a specified image region and duplicates it over the whole image. |
| [MeshConstrainedDeformationTestPlayground](/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshConstrainedDeformationTestPlayground) | MeshConstrainedDeformationTestPlayground (v1) Experimental Mesh Constrained Deformation Node |
| [MeshWarp](/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshWarp) | MeshWarp (v1) Experimental Mesh Warp Node |
| [MeshWrap](/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshWrap) | MeshWrap (v1) Experimental Dataflow node for wrapping one mesh's topology to another mesh's shape. |
| [MeshWrapLandmarks](/documentation/en-us/unreal-engine/node-reference/Dataflow/MeshWrapLandmarks) | MeshWrapLandmarks (v1) Experimental Node for defining landmarks used by MeshWrapNode. |
| [UVMeshTransformNode](/documentation/en-us/unreal-engine/node-reference/Dataflow/UVMeshTransformNode) | UVMeshTransformNode (v1) Experimental UVMesh Transform Node |
| [UVResizeController](/documentation/en-us/unreal-engine/node-reference/Dataflow/UVResizeController) | UVResizeController (v1) Experimental UV Resizing logic. |
| [UVUnwrapNode](/documentation/en-us/unreal-engine/node-reference/Dataflow/UVUnwrapNode) | UVUnwrapNode (v1) Experimental UVUnwrap Node |

### Outfit

| Node | Description |
| --- | --- |
| [ExtractBodyPartsArrayFromBodySizeParts](/documentation/en-us/unreal-engine/node-reference/Dataflow/ExtractBodyPartsArrayFromBodySizeParts) | ExtractBodyPartsArrayFromBodySizeParts (v1) Experimental Extract the array of BodyParts from a FChaosOutfitBodySizeBodyParts Input(s) : BodySizeParts - The source outfit. |
| [FilterSizedOutfit](/documentation/en-us/unreal-engine/node-reference/Dataflow/FilterSizedOutfit) | FilterSizedOutfit (v1) Experimental Select a single size for the passed Outfit and filter out all non matching sizes. |
| [GetClothAsset](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetClothAsset) | GetClothAsset (v1) Experimental Get a cloth asset object into the graph. |
| [GetOrMakeOutfitFromAsset](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetOrMakeOutfitFromAsset) | GetOrMakeOutfitFromAsset (v1) Experimental Extract the Outfit from an Outfit Asset. |
| [GetOutfitAsset](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetOutfitAsset) | GetOutfitAsset (v1) Experimental Get an outfit asset object into the graph. |
| [GetOutfitBodyParts](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetOutfitBodyParts) | GetOutfitBodyParts (v1) Experimental Extract the Body Part Skeletal Meshes from an Outfit. |
| [GetOutfitClothCollections](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetOutfitClothCollections) | GetOutfitClothCollections (v1) Experimental Extract the cloth collections contained into the specified source outfit. |
| [GetOutfitRBFInterpolationData](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetOutfitRBFInterpolationData) | GetOutfitRBFInterpolationData (v1) Experimental Extract the Body Part RBF Interpolation Data from an outfit. |
| [MakeOutfit](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeOutfit) | MakeOutfit (v1) Experimental Add multiple cloth asset objects to an outfit collection. |
| [MakeSizedOutfit](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeSizedOutfit) | MakeSizedOutfit (v1) Experimental Add multiple cloth asset objects to an outfit collection. |
| [MergeOutfits](/documentation/en-us/unreal-engine/node-reference/Dataflow/MergeOutfits) | MergeOutfits (v1) Experimental Merge multiple outfits into a single outfits. |
| [OutfitAssetTerminal](/documentation/en-us/unreal-engine/node-reference/Dataflow/OutfitAssetTerminal) | OutfitAssetTerminal (v1) Experimental Outfit terminal node to generate an outfit asset from several cloth assets. |
| [OutfitQuery](/documentation/en-us/unreal-engine/node-reference/Dataflow/OutfitQuery) | OutfitQuery (v1) Query an Outfit about its properties. |
| [SetOutfitClothCollection](/documentation/en-us/unreal-engine/node-reference/Dataflow/SetOutfitClothCollection) | SetOutfitClothCollection (v1) Experimental Replace the ClothCollection in an Outfit with a new one. |

### Physics|Common

| Node | Description |
| --- | --- |
| [GetSimulationTime](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetSimulationTime) | GetSimulationTime (v1) Get the context simulation time Output(s): SimulationTime - Simulation time property coming from the context |

### Physics|Proxy

| Node | Description |
| --- | --- |
| [FilterSimulationProxies](/documentation/en-us/unreal-engine/node-reference/Dataflow/FilterSimulationProxies) | FilterSimulationProxies (v1) Filter simulation proxies from context Input(s) : SimulationProxies - Simulation proxies coming from the context and filtered with the groups Output(s): FilteredProxies - Simulation proxies coming from the context and filtered with the groups |

### Physics|Solver

| Node | Description |
| --- | --- |
| [AddSolverDeformer](/documentation/en-us/unreal-engine/node-reference/Dataflow/AddSolverDeformer) | AddSolverDeformer (v1) Add a graph deformer to the groom simulation Input(s) : PhysicsSolvers - Physics solvers to advance in time SimulationTime - Delta time to use to advance the solver Output(s): PhysicsSolvers [Passthrough] - Physics solvers to advance in time |
| [AdvancePhysicsSolvers](/documentation/en-us/unreal-engine/node-reference/Dataflow/AdvancePhysicsSolvers) | AdvancePhysicsSolvers (v1) Advance the simulation physics solver in time Input(s) : SimulationTime - Delta time to use to advance the solver PhysicsSolvers - Physics solvers to advance in time Output(s): PhysicsSolvers [Passthrough] - Physics solvers to advance in time |
| [GetPhysicsSolvers](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetPhysicsSolvers) | GetPhysicsSolvers (v1) Get physics solvers from context Output(s): PhysicsSolvers - Physics solvers coming from the context and filtered with the groups |

### PointSampling

| Node | Description |
| --- | --- |
| [FilterPointsWithMesh](/documentation/en-us/unreal-engine/node-reference/Dataflow/FilterPointsWithMesh) | FilterPointsWithMesh (v1) Filter a point set to only the points inside or outside of a given mesh Input(s) : TargetMesh [Intrinsic] - Mesh to use to filter point set bKeepInside - Whether to keep the points inside or (if false) outside the mesh, when filtering by Winding Number. |
| [NonUniformPointSampling](/documentation/en-us/unreal-engine/node-reference/Dataflow/NonUniformPointSampling) | NonUniformPointSampling (v1) NonUniform Sampling on a DynamicMesh Input(s) : TargetMesh [Intrinsic] - Mesh to sample points on SamplingRadius - Desired "radius" of sample points. |
| [UniformPointSampling](/documentation/en-us/unreal-engine/node-reference/Dataflow/UniformPointSampling) | UniformPointSampling (v1) Uniform Sampling on a DynamicMesh Input(s) : TargetMesh [Intrinsic] - Mesh to sample points on SamplingRadius - Desired "radius" of sample points. |
| [VertexWeightedPointSampling](/documentation/en-us/unreal-engine/node-reference/Dataflow/VertexWeightedPointSampling) | VertexWeightedPointSampling (v1) VertexWeighted Sampling on a DynamicMesh Input(s) : TargetMesh [Intrinsic] - Mesh to sample points on VertexWeights [Intrinsic] - Weight array SamplingRadius - Desired "radius" of sample points. |

### Selection|Utility

| Node | Description |
| --- | --- |
| [SelectionToVertexList](/documentation/en-us/unreal-engine/node-reference/Dataflow/SelectionToVertexList) | SelectionToVertexList (v1) Selection to Vertex List Dataflow Node |

### SphereCovering

| Node | Description |
| --- | --- |
| [Get Sphere Covering Sphere Count](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetSphereCoveringSphereCount) | Get Sphere Covering Sphere Count (v1) Report the number of spheres in a sphere covering Input(s) : SphereCovering [Intrinsic] - The sphere covering to evaluate Output(s): NumSpheres - Number of spheres in the sphere covering |

### Static Mesh

| Node | Description |
| --- | --- |
| [GetStaticMeshBoundingBox](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetStaticMeshBoundingBox) | GetStaticMeshBoundingBox (v1) Get the local geometric bounding box a static mesh Input(s) : StaticMesh - Static Mesh to compute the bouning box from Output(s): BoundingBox - Geometric bounding box of the input Static Mesh Center - Center of the resulting bounding box Dimensions - Dimensions of the resulting bounding box in centimers |

### SubGraph

| Node | Description |
| --- | --- |
| [GetCurrentIndex](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetCurrentIndex) | GetCurrentIndex (v1) Get the current index in a subgraph This is to be used in subgraph when iterating over an array |
| [SubGraphCall](/documentation/en-us/unreal-engine/node-reference/Dataflow/SubGraphCall) | SubGraphCall (v1) Call a subgraph |
| [SubGraphInput](/documentation/en-us/unreal-engine/node-reference/Dataflow/SubGraphInput) | SubGraphInput (v1) This node represent the inputs of a dataflow subgraph |
| [SubGraphOutput](/documentation/en-us/unreal-engine/node-reference/Dataflow/SubGraphOutput) | SubGraphOutput (v1) This node represent the Outputs of a dataflow subgraph |

### Terminal

| Node | Description |
| --- | --- |
| [CurveSamplingAnimationAssetTerminal](/documentation/en-us/unreal-engine/node-reference/Dataflow/CurveSamplingAnimationAssetTerminal) | CurveSamplingAnimationAssetTerminal (v1) \* terminal node to create an animation asset for muscle activation MLD training. |
| [FleshAssetTerminal](/documentation/en-us/unreal-engine/node-reference/Dataflow/FleshAssetTerminal) | FleshAssetTerminal (v1) Flesh Asset Terminal Dataflow Node |
| [GeometryCollectionTerminal](/documentation/en-us/unreal-engine/node-reference/Dataflow/GeometryCollectionTerminal) | GeometryCollectionTerminal (v2) \* Geometry Collection asset terminal node Input(s) : Materials - Materials to set on this asset InstancedMeshes - array of instanced meshes Output(s): Materials [Passthrough] - Materials to set on this asset InstancedMeshes [Passthrough] - array of instanced meshes |
| [SkeletonAssetTerminal](/documentation/en-us/unreal-engine/node-reference/Dataflow/SkeletonAssetTerminal) | SkeletonAssetTerminal (v1) \* Dataflow terminal node to save a skeleton asset Input(s) : SourceSkeleton - Source Skeleton used to override the skeleton asset SkeletonAsset - Skeleton Asset to be saved |
| [TextureTerminal](/documentation/en-us/unreal-engine/node-reference/Dataflow/TextureTerminal) | TextureTerminal (v1) \* terminal node to a save a dependent 2D texture |

### Terminal|Proxy

| Node | Description |
| --- | --- |
| [SimulationProxiesTerminal](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationProxiesTerminal) | SimulationProxiesTerminal (v1) Main terminal node for simulation proxies Input(s) : SimulationProxies - Physics solvers to evaluate |

### Utilities

| Node | Description |
| --- | --- |
| [UnionIntArrays](/documentation/en-us/unreal-engine/node-reference/Dataflow/UnionIntArrays) | UnionIntArrays (v1) Union Int Arrays Dataflow Node |

### Utilities|Array

| Node | Description |
| --- | --- |
| [BoolArrayToFaceSelection](/documentation/en-us/unreal-engine/node-reference/Dataflow/BoolArrayToFaceSelection) | BoolArrayToFaceSelection (v1) Converts a TArray to a FDataflowFaceSelection Input(s) : BoolAttributeData [Intrinsic] - TArray data |
| [ConvertToArray](/documentation/en-us/unreal-engine/node-reference/Dataflow/ConvertToArray) | ConvertToArray (v1) convert a single element to an array Input(s) : Element - Element to convert to an array Output(s): Array - Array to Convert to |
| [FloatArrayComputeStatistics](/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatArrayComputeStatistics) | FloatArrayComputeStatistics (v1) Computes statistics of a float array Input(s) : FloatArray [Intrinsic] - Array to compute values from TransformSelection - TransformSelection describes which values to use, if not connected all the elements will be used Output(s): Value - Computed value Indices - Indices of elements with the computed value |
| [FloatArrayToVertexSelection](/documentation/en-us/unreal-engine/node-reference/Dataflow/FloatArrayToVertexSelection) | FloatArrayToVertexSelection (v1) Converts a TArray to a FDataflowVertexSelection Input(s) : FloatArray [Intrinsic] - TArray array |
| [GetArrayElement](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetArrayElement) | GetArrayElement (v1) Get an element from an array Input(s) : Array [Intrinsic] - Array to get the element from Index - Index to get the element at Output(s): Array [Passthrough] - Array to get the element from Element - Element from the array at the specified index |
| [GetArraySize](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetArraySize) | GetArraySize (v1) Get size of an array Input(s) : Array [Intrinsic] - Array to get size from Output(s): Size - Computed value |
| [MakeManagedArrayCollectionArray](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeManagedArrayCollectionArray) | MakeManagedArrayCollectionArray (v1) Append an element to an array of ManagedArrayCollections. |
| [RandomizeFloatArray](/documentation/en-us/unreal-engine/node-reference/Dataflow/RandomizeFloatArray) | RandomizeFloatArray (v1) Randomize elements in a float array (Random value will be in (RandomRangeMin, RandomRangeMax) Input(s) : FloatArray [Intrinsic] - Array to randomize RandomRangeMin - Random range min RandomRangeMax - Random range max RandomSeed - Seed for random Output(s): FloatArray [Passthrough] - Array to randomize |
| [RemoveFloatArrayElement](/documentation/en-us/unreal-engine/node-reference/Dataflow/RemoveFloatArrayElement) | RemoveFloatArrayElement (v1) Removes the specified element from an array Input(s) : FloatArray [Intrinsic] - Array to remove the element from Output(s): FloatArray [Passthrough] - Array to remove the element from |

### Utilities|Box

| Node | Description |
| --- | --- |
| [BreakBox](/documentation/en-us/unreal-engine/node-reference/Dataflow/BreakBox) | BreakBox (v1) Description for this node |
| [GetBoxLengths](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetBoxLengths) | GetBoxLengths (v1) Create an array of lengths of bounding boxes (measured along an axis, diagonal, or the max/min axes) from an array of bounding boxes |
| [GetCollectionBoundingBox](/documentation/en-us/unreal-engine/node-reference/Dataflow/GetCollectionBoundingBox) | GetCollectionBoundingBox (v1) Get the geometric bounding box a collection in collection space Input(s) : Collection - Collection to compute the bouning box from Output(s): BoundingBox - Geometric bounding box of the input collection Center - Center of the resulting bounding box Dimensions - Dimensions of the resulting bounding box in centimers |

### Utilities|FlowControl

| Node | Description |
| --- | --- |
| [BranchCollection](/documentation/en-us/unreal-engine/node-reference/Dataflow/BranchCollection) | BranchCollection (v1) Branch between two Managed Array Collections based on Boolean condition Input(s) : TrueCollection - Collection input for the 'true' case FalseCollection - Collection input for the 'false' case Output(s): ChosenCollection - Output Collection |
| [BranchFloat](/documentation/en-us/unreal-engine/node-reference/Dataflow/BranchFloat) | BranchFloat (v1) Branch between two float inputs based on boolean condition Input(s) : A - Float input B - Float input Output(s): ReturnValue - Output |
| [BranchInt](/documentation/en-us/unreal-engine/node-reference/Dataflow/BranchInt) | BranchInt (v1) Branch between two int inputs based on boolean condition Input(s) : A - Int input B - Int input Output(s): ReturnValue - Output |
| [BranchMesh](/documentation/en-us/unreal-engine/node-reference/Dataflow/BranchMesh) | BranchMesh (v1) Branch between two mesh inputs based on boolean condition Input(s) : MeshA - Mesh input MeshB - Mesh input Output(s): Mesh - Output mesh |

### Utilities|Sphere

| Node | Description |
| --- | --- |
| [BoundingSphere](/documentation/en-us/unreal-engine/node-reference/Dataflow/BoundingSphere) | BoundingSphere (v1) Description for this node |
| [BreakBoundingSphere](/documentation/en-us/unreal-engine/node-reference/Dataflow/BreakBoundingSphere) | BreakBoundingSphere (v1) Expands data of FSphere |

### Utilities|String

| Node | Description |
| --- | --- |
| [HashString](/documentation/en-us/unreal-engine/node-reference/Dataflow/HashString) | HashString (v1) Generates a hash value from a string Input(s) : String - String to hash Output(s): Hash - Generated hash value |
| [MakeLiteralString](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeLiteralString) | MakeLiteralString (v2) Make a literal string |
| [StringAppend](/documentation/en-us/unreal-engine/node-reference/Dataflow/StringAppend) | StringAppend (v2) Concatenates strings together to make a new string |

### Utilities|Vector

| Node | Description |
| --- | --- |
| [BreakVector](/documentation/en-us/unreal-engine/node-reference/Dataflow/BreakVector) | BreakVector (v1) Expands a Vector into X, Y, Z components |
| [HashVector](/documentation/en-us/unreal-engine/node-reference/Dataflow/HashVector) | HashVector (v1) Generates a hash value from a vector Input(s) : Vector - Vector to hash Output(s): Hash - Generated hash value |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Cloth](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#cloth)
* [Collection](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#collection)
* [Collection|Utilities](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#collection%7Cutilities)
* [Convert](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#convert)
* [Core](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#core)
* [Dataflow](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#dataflow)
* [Fields](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#fields)
* [Flesh](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#flesh)
* [Flesh|Experimental](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#flesh%7Cexperimental)
* [Flesh|Utilities](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#flesh%7Cutilities)
* [FlowControl](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#flowcontrol)
* [General](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#general)
* [Generators|Box](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#generators%7Cbox)
* [Generators|Collection](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#generators%7Ccollection)
* [Generators|Mesh](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#generators%7Cmesh)
* [Generators|Plane](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#generators%7Cplane)
* [Generators|Point](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#generators%7Cpoint)
* [Generators|Sphere](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#generators%7Csphere)
* [Generators|Transform](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#generators%7Ctransform)
* [GeometryCollection](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#geometrycollection)
* [GeometryCollection|Asset](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#geometrycollection%7Casset)
* [GeometryCollection|Cluster](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#geometrycollection%7Ccluster)
* [GeometryCollection|Development](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#geometrycollection%7Cdevelopment)
* [GeometryCollection|Edit](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#geometrycollection%7Cedit)
* [GeometryCollection|Fracture](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#geometrycollection%7Cfracture)
* [GeometryCollection|Fracture|Utilities](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#geometrycollection%7Cfracture%7Cutilities)
* [GeometryCollection|Mesh](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#geometrycollection%7Cmesh)
* [GeometryCollection|Overrides](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#geometrycollection%7Coverrides)
* [GeometryCollection|Selection](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#geometrycollection%7Cselection)
* [GeometryCollection|Selection|All](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#geometrycollection%7Cselection%7Call)
* [GeometryCollection|Selection|Array](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#geometrycollection%7Cselection%7Carray)
* [GeometryCollection|Selection|Face](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#geometrycollection%7Cselection%7Cface)
* [GeometryCollection|Selection|Transform](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#geometrycollection%7Cselection%7Ctransform)
* [GeometryCollection|Selection|Vertex](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#geometrycollection%7Cselection%7Cvertex)
* [GeometryCollection|Texture](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#geometrycollection%7Ctexture)
* [GeometryCollection|Utilities](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#geometrycollection%7Cutilities)
* [GeometryCollection|UV](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#geometrycollection%7Cuv)
* [Groom](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#groom)
* [Image](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#image)
* [Materials](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#materials)
* [Math](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#math)
* [Math|Boolean](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#math%7Cboolean)
* [Math|Compare](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#math%7Ccompare)
* [Math|Conversions](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#math%7Cconversions)
* [Math|Double](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#math%7Cdouble)
* [Math|Float](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#math%7Cfloat)
* [Math|Int](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#math%7Cint)
* [Math|Random](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#math%7Crandom)
* [Math|Scalar](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#math%7Cscalar)
* [Math|Transform](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#math%7Ctransform)
* [Math|Trig](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#math%7Ctrig)
* [Math|Utilities](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#math%7Cutilities)
* [Math|Vector](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#math%7Cvector)
* [Math|Vectors](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#math%7Cvectors)
* [Mesh](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#mesh)
* [Mesh|Utilities](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#mesh%7Cutilities)
* [MeshResizing](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#meshresizing)
* [Outfit](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#outfit)
* [Physics|Common](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#physics%7Ccommon)
* [Physics|Proxy](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#physics%7Cproxy)
* [Physics|Solver](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#physics%7Csolver)
* [PointSampling](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#pointsampling)
* [Selection|Utility](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#selection%7Cutility)
* [SphereCovering](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#spherecovering)
* [Static Mesh](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#staticmesh)
* [SubGraph](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#subgraph)
* [Terminal](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#terminal)
* [Terminal|Proxy](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#terminal%7Cproxy)
* [Utilities](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#utilities)
* [Utilities|Array](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#utilities%7Carray)
* [Utilities|Box](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#utilities%7Cbox)
* [Utilities|FlowControl](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#utilities%7Cflowcontrol)
* [Utilities|Sphere](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#utilities%7Csphere)
* [Utilities|String](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#utilities%7Cstring)
* [Utilities|Vector](/documentation/en-us/unreal-engine/node-reference/Dataflow?application_version=5.7#utilities%7Cvector)
