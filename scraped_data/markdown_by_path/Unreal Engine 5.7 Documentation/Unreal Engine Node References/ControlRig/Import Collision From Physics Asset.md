<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ImportCollisionFromPhysicsAsset?application_version=5.7 -->

# Import Collision From Physics Asset

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
7. Import Collision From Physics Asset

# Import Collision From Physics Asset

Imports/creates bones from the physics asset and creates collision for them.

On this page

### Description

Imports/creates bones from the physics asset and creates collision for them.
The bones will lose their hierarchy and be placed under the specified parent - ready to be moved around.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigPhysics](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigPhysics) |
| Category | RigPhysics |
| Tags | Construction,Create,New |
| Type | [FRigUnit\_HierarchyImportCollisionFromPhysicsAsset](/documentation/en-us/unreal-engine/API/Plugins/ControlRigPhysics/FRigUnit_HierarchyImportCollisio-) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| PhysicsSolverComponentKey | Note that setting the solver component, if known, has the benefit of avoiding the need to search for an automatic solver. | [Rig Component Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey) | (ElementKey=(Type=Bone,Name=""),Name="PhysicsSolver") |
| bUseAutomaticSolver | If true (and the physics solver is not explicitly set), then this component will be added to any physics solver that exists above it in the hierarchy, if that solver allows automatically adding physics components. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| PhysicsAsset | The physics asset to import collision from | Physics Asset | None |
| BonesToUse | If this is empty, then all bones with bodies in the physics asset will be created. Otherwise only bodies that relate to the specified bones will be created. | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FName](/documentation/en-us/unreal-engine/API/Runtime/Core/FName)> | () |
| NameSpace | Prefix to the bone names | [FName](/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | Physics\_ |
| Owner | Parent/owner for all the new bones | [Rig Element Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=None,Name="") |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| BoneKeys | The element keys of the bones that were created to own the physics bodies | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigElementKey](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey)> |  |
| PhysicsBodyComponentKeys | The Physics Body component keys that were created | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigComponentKey](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigComponentKey)> |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/ImportCollisionFromPhysicsAsset?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/ImportCollisionFromPhysicsAsset?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/ImportCollisionFromPhysicsAsset?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/ImportCollisionFromPhysicsAsset?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/ImportCollisionFromPhysicsAsset?application_version=5.7#outputs)
