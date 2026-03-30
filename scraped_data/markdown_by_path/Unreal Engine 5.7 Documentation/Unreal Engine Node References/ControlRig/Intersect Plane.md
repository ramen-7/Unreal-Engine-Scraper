<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/IntersectPlane?application_version=5.7 -->

# Intersect Plane

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
7. Intersect Plane

# Intersect Plane

2 nodes with name Intersect Plane

On this page

## Intersect Plane (FRigVMFunction\_MathRayIntersectPlane)

Returns the closest point intersection of a ray with a plane

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Ray |
| Tags | Closest,Ray,Cross |
| Type | [FRigVMFunction\_MathRayIntersectPlane](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathRayIntersectP-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Ray | The ray to intersect with the plane | [Ray](/documentation/en-us/unreal-engine/API/Runtime/Core) | (Origin=(X=0.000000,Y=0.000000,Z=0.000000),Direction=(X=0.000000,Y=0.000000,Z=1.000000)) |
| PlanePoint | The point on the plane to intersect the ray with | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| PlaneNormal | The normal of the plane to intersect the ray with | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting intersection position | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Distance | The distance of the ray origin to the plane | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |
| Ratio | The ratio along the ray up to the intersection point | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

## Intersect Plane (FRigVMFunction\_MathIntersectPlane)

Intersects a plane with a vector given a start and direction

### Information

|  |  |
| --- | --- |
| Plugin | [RigVM](/documentation/en-us/unreal-engine/API/PluginIndex/RigVM) |
| Category | Math|Vector |
| Tags | Collide,Intersect,Raycast |
| Type | [FRigVMFunction\_MathIntersectPlane](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMFunction_MathIntersectPlan-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Start | The start of the ray to intersect with the plane | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| Direction | The direction of the ray to intersect with the plane | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |
| PlanePoint | The point on the plane to intersect with | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=0.000000) |
| PlaneNormal | The normal of the plane to intersect with | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Result | The resulting position on the plane | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |
| Distance | The distance along the ray to the intersection | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Intersect Plane (FRigVMFunction\_MathRayIntersectPlane)](/documentation/en-us/unreal-engine/node-reference/ControlRig/IntersectPlane?application_version=5.7#intersectplane(frigvmfunction-mathrayintersectplane))
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/IntersectPlane?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/IntersectPlane?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/IntersectPlane?application_version=5.7#outputs)
* [Intersect Plane (FRigVMFunction\_MathIntersectPlane)](/documentation/en-us/unreal-engine/node-reference/ControlRig/IntersectPlane?application_version=5.7#intersectplane(frigvmfunction-mathintersectplane))
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/IntersectPlane?application_version=5.7#information-2)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/IntersectPlane?application_version=5.7#inputs-2)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/IntersectPlane?application_version=5.7#outputs-2)
