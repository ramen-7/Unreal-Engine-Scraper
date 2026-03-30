<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/SphereTraceByObjectTypes?application_version=5.7 -->

# Sphere Trace By Object Types

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
7. Sphere Trace By Object Types

# Sphere Trace By Object Types

Sweeps a sphere against the world and return the first blocking hit.

On this page

### Description

Sweeps a sphere against the world and return the first blocking hit. The trace is filtered by object types only, the collision response settings are ignored.
You can create custom object types in Project Setting - Collision

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | Collision |
| Tags | Sweep,Raytrace,Collision,Collide,Trace |
| Type | [FRigUnit\_SphereTraceByObjectTypes](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_SphereTraceByObjectType-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Start | Start of the trace in rig / global space | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| End | End of the trace in rig / global space | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| ObjectTypes | The types of objects that this trace can hit | [TArray](/documentation/en-us/unreal-engine/API/Runtime/Core/TArray)<[TEnumAsByte](/documentation/en-us/unreal-engine/API/Runtime/Core/TEnumAsByte)<[EObjectTypeQuery](/documentation/en-us/unreal-engine/API/Runtime/Engine/EObjectTypeQuery)>> | () |
| Radius | Radius of the sphere to use for sweeping / tracing | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 5.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| bHit | Returns true if there was a hit | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| HitLocation | Hit location in rig / global Space | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| HitNormal | Hit normal in rig / global Space | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/SphereTraceByObjectTypes?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/SphereTraceByObjectTypes?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SphereTraceByObjectTypes?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/SphereTraceByObjectTypes?application_version=5.7#outputs)
