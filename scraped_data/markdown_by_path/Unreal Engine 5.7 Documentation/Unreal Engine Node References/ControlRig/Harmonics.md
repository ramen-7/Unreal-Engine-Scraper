<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/Harmonics?application_version=5.7 -->

# Harmonics

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
4. Harmonics

# Harmonics

Drives an array of items through a harmonics spectrum

On this page

### Description

Drives an array of items through a harmonics spectrum

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Simulation |
| Tags | Sin,Wave |
| Type | [FRigUnit\_ItemHarmonics](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_ItemHarmonics) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Targets | The items to drive. | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[FRigUnit\_Harmonics\_TargetItem](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_Harmonics_TargetItem)> | () |
| WaveSpeed | The speed of the wave to use | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=1.000000,Z=1.000000) |
| WaveFrequency | The frequency of the wave to use | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1.000000,Y=0.600000,Z=0.800000) |
| WaveAmplitude | The amplitude in degrees per axis | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=70.000000,Z=0.000000) |
| WaveOffset | The positional offset of the wave | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=1.000000,Z=2.000000) |
| WaveNoise | The amount of noise to apply to the wave | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| WaveEase | The easing function to apply to the wave | [Rig VMAnim Easing Type](/documentation/en-us/unreal-engine/API/Plugins/RigVM/ERigVMAnimEasingType) | Linear |
| WaveMinimum | The minimum value for the wave | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.500000 |
| WaveMaximum | The maximum value for the wave | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| RotationOrder | The rotation order to use when encoding the rotation | [Euler Rotation Order](/documentation/en-us/unreal-engine/API/Runtime/AnimationCore/EEulerRotationOrder) | YZX |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/Harmonics?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/Harmonics?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/Harmonics?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/Harmonics?application_version=5.7#inputs)
