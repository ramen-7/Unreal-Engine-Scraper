<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/ControlRig/CreateParentRelationship?application_version=5.7 -->

# Create Parent Relationship

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
7. Create Parent Relationship

# Create Parent Relationship

Adds a new parent to an element.

On this page

### Description

Adds a new parent to an element. The weight for the new parent will be 0.0.
You can use the SetParentWeights node to change the parent weights later.

If you just want to add a space to a control you can use the 'Add Spaces' node.

### Information

|  |  |
| --- | --- |
| Plugin | [ControlRig](/documentation/en-us/unreal-engine/API/PluginIndex/ControlRig) |
| Category | DynamicHierarchy |
| Tags | Children,Parent,Constraint,Space,AddParent |
| Type | [FRigUnit\_AddParent](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigUnit_AddParent) |

### IO

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ExecutePin | This property is used to chain multiple mutable units together | [Execute Context](/documentation/en-us/unreal-engine/API/Plugins/RigVM/FRigVMExecuteContext) |  |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Child | The child to be parented under the new parent | [Rig Element Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Control,Name="") |
| Parent | The new parent to be added to the child | [Rig Element Key](/documentation/en-us/unreal-engine/API/Plugins/ControlRig/FRigElementKey) | (Type=Control,Name="") |
| DisplayLabel | The optional display label for the parent constraint / space | [FName](/documentation/en-us/unreal-engine/API/Runtime/Core/FName) | None |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/ControlRig/CreateParentRelationship?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/ControlRig/CreateParentRelationship?application_version=5.7#information)
* [IO](/documentation/en-us/unreal-engine/node-reference/ControlRig/CreateParentRelationship?application_version=5.7#io)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/ControlRig/CreateParentRelationship?application_version=5.7#inputs)
