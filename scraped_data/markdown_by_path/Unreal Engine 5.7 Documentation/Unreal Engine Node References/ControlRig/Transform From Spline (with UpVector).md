<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/TransformFromSplinewithUpVector?application_version=5.7 -->

# Transform From Spline (with UpVector)

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
7. Transform From Spline (with UpVector)

# Transform From Spline (with UpVector)

Retrieves the transform from a given Spline and U value based on the given Up Vector and Roll

On this page

### Description

Retrieves the transform from a given Spline and U value based on the given Up Vector and Roll

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRigSpline](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRigSpline) |
| Category | Splines |
| Type | [FRigUnit\_TransformFromControlRigSpline](/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FRigUnit_TransformFromControlRig-) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Spline | The spline to evaluate | [Control Rig Spline](/documentation/en-us/unreal-engine/API/Plugins/ControlRigSpline/FControlRigSpline) | () |
| UpVector | The up-vector to use to build the transform's rotation | [Vector](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.000000,Y=0.000000,Z=1.000000) |
| Roll | The roll to apply to the resulting rotation | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| U | The U value along the spline to evaluate | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Transform | The resulting composed transform | [Transform](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/TransformFromSplinewithUpVector?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/TransformFromSplinewithUpVector?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/TransformFromSplinewithUpVector?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/TransformFromSplinewithUpVector?application_version=5.7#outputs)
