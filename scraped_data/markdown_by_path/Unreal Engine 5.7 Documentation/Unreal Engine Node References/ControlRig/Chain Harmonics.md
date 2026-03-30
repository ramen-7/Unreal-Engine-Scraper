<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/ChainHarmonics?application_version=5.7 -->

# Chain Harmonics

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
7. Chain Harmonics

# Chain Harmonics

Given a root will drive all items underneath in a chain based harmonics spectrum

On this page

### Description

Given a root will drive all items underneath in a chain based harmonics spectrum

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Simulation |
| Type | [FRigUnit\_ChainHarmonicsPerItem](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ChainHarmonicsPerItem) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ChainRoot | The root of the chain to apply the harmonics to | [Rig Element Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Bone,Name="") |
| Speed | The speed of the harmonics effects | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000,Z=1.000000) |
| Reach | The reach settings Reach lets the chain "lean" towards the target trying to reach it. | [Rig Unit Chain Harmonics Reach](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ChainHarmonics_Reach) | (bEnabled=False,ReachTarget=(X=0.000000,Y=0.000000,Z=0.000000),ReachAxis=(X=1.000000,Y=0.000000,Z=0.000000),ReachMinimum=0.000000,ReachMaximum=0.000000,ReachEase=Linear) |
| Wave | The wave settings A wave is a rocking back and forth motion to be applied to all / some axes. | [Rig Unit Chain Harmonics Wave](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ChainHarmonics_Wave) | (bEnabled=True,WaveFrequency=(X=1.000000,Y=0.600000,Z=0.800000),WaveAmplitude=(X=0.000000,Y=1.000000,Z=0.000000),WaveOffset=(X=0.000000,Y=1.000000,Z=2.000000),WaveNoise=(X=0.000000,Y=0.000000,Z=0.000000),WaveMinimum=0.000000,WaveMaximum=1.000000,WaveEase=Linear) |
| WaveCurve | The curve to use when evaluating the wave | [Runtime Float Curve](/documentation/en-us/unreal-engine/API/Runtime/Engine/FRuntimeFloatCurve) | (EditorCurveData=(Keys=((),(Time=1.000000,Value=1.000000)),DefaultValue=340282346638528859811704183484516925440.000000,PreInfinityExtrap=RCCE\_Constant,PostInfinityExtrap=RCCE\_Constant),ExternalCurve=None) |
| Pendulum | The pendulum settings The harmonic pendulum uses a simple spring interpolation to allow to follow secondary motion. | [Rig Unit Chain Harmonics Pendulum](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ChainHarmonics_Pendulum) | (bEnabled=False,PendulumStiffness=2.000000,PendulumGravity=(X=0.000000,Y=0.000000,Z=0.000000),PendulumBlend=0.750000,PendulumDrag=0.980000,PendulumMinimum=0.000000,PendulumMaximum=0.100000,PendulumEase=Linear,UnwindAxis=(X=0.000000,Y=1.000000,Z=0.000000),UnwindMinimum=0.200000,UnwindMaximum=0.050000) |
| bDrawDebug | if True the debug drawing will be enabled | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | True |
| DrawWorldOffset | The world offset to be used when debug drawing | [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core) | (Rotation=(X=0.000000,Y=0.000000,Z=0.000000,W=1.000000),Translation=(X=0.000000,Y=0.000000,Z=0.000000),Scale3D=(X=1.000000,Y=1.000000,Z=1.000000)) |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/ChainHarmonics?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/ChainHarmonics?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/ChainHarmonics?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/ChainHarmonics?application_version=5.7#inputs)
