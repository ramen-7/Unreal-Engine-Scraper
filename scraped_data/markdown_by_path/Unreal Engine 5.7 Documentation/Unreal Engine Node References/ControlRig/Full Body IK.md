<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/FullBodyIK?application_version=5.7 -->

# Full Body IK

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
7. Full Body IK

# Full Body IK

Based on a Position Based solver at core, this node can solve multi chains within a root using multi effectors

On this page

### Description

Based on a Position Based solver at core, this node can solve multi chains within a root using multi effectors

### Information

|  |  |
| --- | --- |
| Module | [PBIK](/documentation/en-us/unreal-engine/API/Plugins/PBIK) |
| Category | Hierarchy |
| Tags | FBIK, Position Based, PBIK, IK, Full Body, Multi, Effector, N-Chain, FB, HIK, HumanIK |
| Type | [FRigUnit\_PBIK](/documentation/en-us/unreal-engine/API/Plugins/PBIK/FRigUnit_PBIK) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Root | This is usually the top-most skinned bone; often the "Pelvis" or "Hips", but can be set to any bone. Bones above the root will be ignored by the solver. Bones that are located *between* the Root and the effectors will be included in the solve. | [FName](/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |
| Effectors | An array of effectors. These specify target transforms for different parts of the skeleton. | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FPBIKEffector](/documentation/en-us/unreal-engine/API/Plugins/PBIK/FPBIKEffector)> | () |
| BoneSettings | Per-bone settings to control the resulting pose. Includes limits and preferred angles. | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FPBIKBoneSetting](/documentation/en-us/unreal-engine/API/Plugins/PBIK/FPBIKBoneSetting)> | () |
| ExcludedBones | These bones will be excluded from the solver. They will not bend and will not contribute to the constraint set. Use the ExcludedBones array instead of setting Rotation Stiffness to very high values or Rotation Limits with zero range. | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FName](/documentation/en-us/unreal-engine/API/Runtime/Core/FName)> | () |
| Settings | Global solver settings. | [PBIKSolver Settings](/documentation/en-us/unreal-engine/API/Plugins/PBIK/FPBIKSolverSettings) | (Iterations=20,SubIterations=0,MassMultiplier=1.000000,bAllowStretch=False,RootBehavior=PrePull,PrePullRootSettings=(RotationAlpha=0.000000,RotationAlphaX=1.000000,RotationAlphaY=1.000000,RotationAlphaZ=1.000000,PositionAlpha=1.000000,PositionAlphaX=1.000000,PositionAlphaY=1.000000,PositionAlphaZ=1.000000),GlobalPullChainAlpha=1.000000,MaxAngle=30.000000,OverRelaxation=1.300000) |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/FullBodyIK?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/FullBodyIK?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/FullBodyIK?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/FullBodyIK?application_version=5.7#inputs)
