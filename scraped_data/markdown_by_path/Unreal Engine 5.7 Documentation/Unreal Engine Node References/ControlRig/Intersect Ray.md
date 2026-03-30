<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IntersectRay?application_version=5.7 -->

# Intersect Ray

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
7. Intersect Ray

# Intersect Ray

Returns the closest point intersection of a ray with another ray

On this page

### Description

Returns the closest point intersection of a ray with another ray

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Ray |
| Tags | Closest,Ray,Cross |
| Type | [FRigVMFunction\_MathRayIntersectRay](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathRayIntersectR-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| A | The first ray to intersect | [Ray](/documentation/en-us/unreal-engine/API/Runtime/Core) | (Origin=(X=0.000000,Y=0.000000,Z=0.000000),Direction=(X=0.000000,Y=0.000000,Z=1.000000)) |
| B | The second ray to intersect | [Ray](/documentation/en-us/unreal-engine/API/Runtime/Core) | (Origin=(X=0.000000,Y=0.000000,Z=0.000000),Direction=(X=0.000000,Y=0.000000,Z=1.000000)) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting intersection position. This is either on the rays themselves or at the closest position between the two. | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Distance | The distance between the two rays (or 0 if they touch) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| RatioA | The ratio on the first ray at the intersection | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| RatioB | The ratio on the second ray at the intersection | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/IntersectRay?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/IntersectRay?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/IntersectRay?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/IntersectRay?application_version=5.7#outputs)
