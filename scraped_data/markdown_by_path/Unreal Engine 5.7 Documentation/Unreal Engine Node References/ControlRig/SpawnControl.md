<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnControl?application_version=5.7 -->

# SpawnControl

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
6. [ControlRig](/documentation/en-us/unreal-engine/node-reference/ControlRig "ControlRig")
7. SpawnControl

# SpawnControl

Adds a new control to the hierarchy Note: This node only runs as part of the construction event.

On this page

### Description

Adds a new control to the hierarchy
Note: This node only runs as part of the construction event.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | DynamicHierarchy |
| Tags | SpawnControl,Spawn Float Control,Construction,Create,New,AddControl,NewControl,CreateControl,Spawn Integer Control,Spawn Vector2D Control,Spawn Vector Control,Spawn Rotator Control,Rotation,Spawn Transform Control |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| InitialValue | The initial value of the new control | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore)   [int32](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Rotator](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core)   [Vector 2D](/documentation/en-us/unreal-engine/API/Runtime/Core) | 0.000000 |
| Settings | The settings for the control | [Rig Unit Hierarchy Add Control Float Settings](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddControlFloa-_2)   [FRigUnit\_HierarchyAddControlInteger\_Settings](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddControlInte-_2)   [FRigUnit\_HierarchyAddControlVector2D\_Settings](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddControlVect-_3)   [FRigUnit\_HierarchyAddControlVector\_Settings](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddControlVect-_5)   [FRigUnit\_HierarchyAddControlRotator\_Settings](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddControlRota-_2)   [FRigUnit\_HierarchyAddControlTransform\_Settings](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_HierarchyAddControlTran-_2) | (PrimaryAxis=X,bIsScale=False,Limits=(Limit=(bMinimum=True,bMaximum=True),MinValue=0.000000,MaxValue=100.000000,bDrawLimits=True),Shape=(bVisible=True,Name="Default",Color=(R=1.000000,G=0.000000,B=0.000000,A=1.000000),Transform=(Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000))),Proxy=(bIsProxy=False,DrivenControls=,ShapeVisibility=BasedOnSelection),DisplayName="",bSelectable=True) |
| OffsetTransform | The offset transform of the new control | [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |
| OffsetSpace | The space the offset is in | [Rig VMTransform Space](/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMTransformSpace) | LocalSpace |
| Parent | The parent of the new element to add | [Rig Element Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Name | The name of the new element to add | [FName](/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | NewControl |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Item | The resulting item | [Rig Element Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnControl?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnControl?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnControl?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnControl?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SpawnControl?application_version=5.7#outputs)
