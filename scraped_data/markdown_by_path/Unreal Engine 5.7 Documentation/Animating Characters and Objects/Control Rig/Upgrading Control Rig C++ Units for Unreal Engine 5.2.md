<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/upgrading-control-rig-cplusplus-units-for-unreal-engine-5.2?application_version=5.7 -->

# Upgrading Control Rig C++ Units for Unreal Engine 5.2

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
5. [Animating Characters and Objects](/documentation/en-us/unreal-engine/animating-characters-and-objects-in-unreal-engine "Animating Characters and Objects")
6. [Control Rig](/documentation/en-us/unreal-engine/control-rig-in-unreal-engine "Control Rig")
7. Upgrading Control Rig C++ Units for Unreal Engine 5.2

# Upgrading Control Rig C++ Units for Unreal Engine 5.2

Upgrading your Control Rig's C++ units from unreal engine 5.0 and 5.1 to 5.2.

![Upgrading Control Rig C++ Units for Unreal Engine 5.2](https://dev.epicgames.com/community/api/documentation/image/7d8716ef-f1ab-4296-8ce6-6ec766abdd70?resizing_type=fill&width=1920&height=335)

 On this page

In **Unreal Engine** 5.2, significant changes have been made to the way a [Control Rig](/documentation/en-us/unreal-engine/control-rig-in-unreal-engine) `FRigVMStruct` and `FRigUnit` are implemented in your project's **C++** code base. The terminology and the extended use of the notion of a **Context** inside of custom `FRigVMStruct` structures have required these structs to be refactored.

You can use this document to learn more about migrating your Control Rig code to be compatible in Unreal Engine 5.2.

## Execute signature changes

In previous versions of Unreal Engine, `FRigVMExecuteContext` members were treated as parameters to each RigVM method. In Unreal Engine 5.2 the execute context members are no longer passed. Instead a single parameter called `ExecuteContext` is passed to any RigVM method. The parameter will be a **Constant** (**const**) or **Mutable** depending on its use in the structure.

To see changes related to the `FRigUnitContext`, see the [Opaque Arguments and FRigUnitContext](/documentation/en-us/unreal-engine/upgrading-control-rig-cplusplus-units-for-unreal-engine-5.2#opaqueargumentsandfrigunitcontext) section.

Here you can reference an example signature change from Unreal Engine 5.1 to 5.2, where a `FRigUnit` such as `FRigUnit_SendEvent` is the signature for `FRigUnit_SendEvent::Execute`:

| 5.1 Signature | 5.2 Signature |
| --- | --- |
| ``` void FRigUnit_SendEvent::StaticExecute( 	const FRigVMExecuteContext& RigVMExecuteContext, 	const ERigEvent Event, 	const FRigElementKey& Item, 	const float OffsetInSeconds, 	const bool bEnable, 	const bool bOnlyDuringInteraction, 	FControlRigExecuteContext& ExecuteContext, 	const FRigUnitContext & Context ) Copy full snippet ``` | ``` void FRigUnit_SendEvent::StaticExecute( 	FControlRigExecuteContext& ExecuteContext, 	const ERigEvent Event, 	const FRigElementKey& Item, 	const float OffsetInSeconds, 	const bool bEnable, 	const bool bOnlyDuringInteraction ) Copy full snippet ``` |

Since the new `ExecuteContext` parameter provides access to a **const** or **mutable** context already we've removed the `RigVMExecuteContext` parameter.

### Opaque Arguments and FRigUnitContext

Formerly domain specific `RIGVM_METHOD` implementations had the option of passing additional **opaque arguments**. In Unreal Engine 5.2, the support for opaque arguments in 5.2 has been removed. The only former usage of this mechanism is the `FRigUnitContext` for Control Rig nodes. Code which relies on accessing the `FRigUnitContext` **Context** parameter must be updated to use the `ExecuteContext.UnitContext` to ensure compatibility.

Members moved from FRigUnitContext to FRigExecuteContext

Here you can reference a list of the members that have moved from the `FRigUnitContext` to the `FRigExecuteContext`:

| Removed 5.1 Argument | Refactored 5.2 Argument |
| --- | --- |
| `FRigUnitContext::DrawInterface` | `FRigVMExecuteContext::GetDrawInterface();` |
| `FRigUnitContext::DrawContainer` | `FRigVMExecuteContext::GetDrawContainer();` |
| `FRigUnitContext::DeltaTime` | `FRigVMExecuteContext::GetDeltaTime();` |
| `FRigUnitContext::AbsoluteTime` | `FRigVMExecuteContext::GetAbsoluteTime();` |
| `FRigUnitContext::FramesPerSecond |` FRigVMExecuteContext::GetFramesPerSecond();` |

|  |  |
| --- | --- |
| `FRigUnitContext::Hierarchy` | `FControlRigExecuteContext::Hierarchy;` |
| `FRigUnitContext::ToWorldSpaceTransform` | `FRigUnitContext::GetToWorldSpaceTransform();` |
| `FRigUnitContext::OwningComponent` | `FRigUnitContext::GetOwningComponent();` |
| `FRigUnitContext::OwningActor` | `FRigUnitContext::GetOwningActor();` |
| `FRigUnitContext::World` | `FRigUnitContext::GetWorld();` |
| `FRigUnitContext::Log` | `FRigVMExecuteContext::GetLog();` |
| `FRigUnitContext::NameCache` | `FRigVMExecuteContext::GetNameCache();` |

All transform conversion related helper functions also have moved to the `FRigVMExecuteContext`.

## FRigUnitContext.State Removal

Control Rig and RigVM no longer calls into RIGVM\_METHOD callbacks multiple times with the **Init** or **Update** state. Instead, it resets the memory to the default during **Init**, and then always runs what used to be considered the **Update** state. This means that you may have to change your code from something that used to rely on the **Init** state for initialization to something which uses an **uninitialized flag** or a similar method to determine if initialization is necessary.

### Example

Here you can reference an example of the refactored code from the Unreal Engine source tree. You can also use the [Unreal Engine GitHub source tree](https://www.unrealengine.com/en-US/ue-on-github) to compare additional refactors, such as with Control Rig nodes, between releases.

| 5.1 FRigUnit\_SendEvent::Execute() | 5.2 FRigUnit\_SendEvent::Execute() |
| --- | --- |
| ~~~ FRigUnit\_SendEvent\_Execute() { DECLARE\_SCOPE\_HIERARCHICAL\_COUNTER\_RIGUNIT()  if(!bEnable) { return; }  if (bOnlyDuringInteraction && !Context.IsInteracting()) { return; }  URigHierarchy *Hierarchy = ExecuteContext.Hierarchy; if (Hierarchy) { switch (Context.State) { case EControlRigState::Init: { break; } case EControlRigState::Update: { FRigEventContext EventContext; EventContext.Key = Item; EventContext.Event = Event; EventContext.SourceEventName = ExecuteContext.GetEventName(); EventContext.LocalTime = Context.AbsoluteTime + OffsetInSeconds; Hierarchy->SendEvent(EventContext, false /* async \*/); break; } default: { break; } } } }   ``` Copy full snippet ```   FRigUnit\_SendEvent\_Execute() { DECLARE\_SCOPE\_HIERARCHICAL\_COUNTER\_RIGUNIT()  if(!bEnable) { return; }  if (bOnlyDuringInteraction && !ExecuteContext.UnitContext.IsInteracting()) { return; }  URigHierarchy *Hierarchy = ExecuteContext.Hierarchy; if (Hierarchy) { FRigEventContext EventContext; EventContext.Key = Item; EventContext.Event = Event; EventContext.SourceEventName = ExecuteContext.GetEventName(); EventContext.LocalTime = ExecuteContext.GetAbsoluteTime() + OffsetInSeconds; Hierarchy->SendEvent(EventContext, false /* async \*/); } } ~~~ |  |

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [control rig](https://dev.epicgames.com/community/search?query=control%20rig)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Execute signature changes](/documentation/en-us/unreal-engine/upgrading-control-rig-cplusplus-units-for-unreal-engine-5.2?application_version=5.7#executesignaturechanges)
* [Opaque Arguments and FRigUnitContext](/documentation/en-us/unreal-engine/upgrading-control-rig-cplusplus-units-for-unreal-engine-5.2?application_version=5.7#opaqueargumentsandfrigunitcontext)
* [FRigUnitContext.State Removal](/documentation/en-us/unreal-engine/upgrading-control-rig-cplusplus-units-for-unreal-engine-5.2?application_version=5.7#frigunitcontextstateremoval)
* [Example](/documentation/en-us/unreal-engine/upgrading-control-rig-cplusplus-units-for-unreal-engine-5.2?application_version=5.7#example)
