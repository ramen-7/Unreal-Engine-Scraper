<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/replicating-actor-components-in-unreal-engine?application_version=5.7 -->

# Actor Component Replication

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
5. [Gameplay Systems](/documentation/en-us/unreal-engine/gameplay-systems-in-unreal-engine "Gameplay Systems")
6. [Networking and Multiplayer](/documentation/en-us/unreal-engine/networking-and-multiplayer-in-unreal-engine "Networking and Multiplayer")
7. [Programming Multiplayer Games](/documentation/en-us/unreal-engine/programming-network-multiplayer-games-for-unreal-engine "Programming Multiplayer Games")
8. Actor Component Replication

# Actor Component Replication

Learn how to replicate actor-owned components.

![Actor Component Replication](https://dev.epicgames.com/community/api/documentation/image/448c4c78-afd7-47f0-8432-a636a1632ab8?resizing_type=fill&width=1920&height=335)

 On this page

An actor component extends an actor's behavior. An actor component is a special type of object that you can attach to an actor as a subobject. Actor components do not replicate by default, but you can configure any actor component to replicate as part of its owning actor. Actor components can replicate their own properties and subobjects, as well as call actor component class-defined remote procedure calls (RPCs) in the same way actors can.

To replicate an actor component as part of your actor, you must make sure that:

* The actor that owns your actor component is set to replicate.
* The actor component is set to replicate.

## Types of Actor Components

### Static Actor Components

A *static actor component* is an actor component spawned when the owning actor is spawned. Static components are created in an actor's C++ constructor as a default subobject or in the Blueprint Editor's [Component Mode](/documentation/en-us/unreal-engine/components-window-in-unreal-engine).

#### Replicate a Static Actor Component

To replicate an actor component created in your actor constructor, follow these steps:

1. In your actor constructor:
   * Set your actor to replicate with `bReplicates = true;`.
   * Create your actor component in your actor constructor with `CreateDefaultSubobject<T>`:

     ```
               AMyActor::AMyActor()
               {
                   bReplicates = true;
                   MyActorComponent = CreateDefaultSubobject<UMyActorComponent>(TEXT("MyActorComponent"));
               }
     Copy full snippet
     ```
2. In you actor component constructor:
   * Set your actor component to replicate with `UActorComponent::SetIsReplicatedByDefault`:

     ```
               UMyActorComponent::UMyActorComponent()
               {
                   SetIsReplicatedByDefault(true);
               }
     Copy full snippet
     ```

### Dynamic Actor Components

A *dynamic actor component* is an actor component spawned on the server at runtime. The creation or deletion of a dynamic actor component replicates to connected clients. Dynamic actor components work similarly to actors.

Clients can spawn their own, local, non-replicating dynamic actor components.

#### Replicate a Dynamic Actor Component

To replicate an actor component created dynamically at runtime, follow these steps:

1. In your actor constructor:
   * Set your actor to replicate with `bReplicates = true;`.
   * Create your actor component in your gameplay code with `NewObject<T>`:

     ```
               MyActorComponent = NewObject<UMyActorComponent>();
     Copy full snippet
     ```
2. When you want to replicate your new actor component:
   * Set your actor component to replicate with `UActorComponent::SetIsReplicated`:

     ```
               if (MyActorComponent)
               {
                   MyActorComponent->SetIsReplicated(true);
               }
     Copy full snippet
     ```

### Blueprint Actor Components

You can spawn both static and dynamic actor components in Blueprint.

#### Replicate a Static Blueprint Actor Component

To replicate a static actor component in Blueprint, toggle the **Replicates** boolean field in your actor component's **Details Panel**. You only need to replicate an actor component if the component has properties or events that you need to replicate.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5f5ff454-a2cf-47b2-91f4-dd12088b0cbc/component-replicates.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5f5ff454-a2cf-47b2-91f4-dd12088b0cbc/component-replicates.png)

You can set an actor component to replicate by default in the Component Replication section of the Details Panel.

The **Component Replication** section only appears on components that support some form of replication.

#### Replicate a Dynamic Blueprint Actor Component

To replicate a dynamic actor component in Blueprint, call the **Set Is Replicated** function with the **Should Replicate** field toggled on.

Copy code

Begin Object Class=/Script/BlueprintGraph.K2Node\_CustomEvent Name="K2Node\_CustomEvent\_0" ExportPath="/Script/BlueprintGraph.K2Node\_CustomEvent'/Game/MyBlueprints/BP\_MyActor.BP\_MyActor:EventGraph.K2Node\_CustomEvent\_0'"
CustomFunctionName="Event ReplicateComponent"
NodePosY=681
NodeGuid=818B4FBA4AB8D2434CFAECA23B4FA1A1
CustomProperties Pin (PinId=421A30E3469187EF6B5740AE931D3780,PinName="OutputDelegate",Direction="EGPD\_Output",PinType.PinCategory="delegate",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(MemberParent="/Script/Engine.BlueprintGeneratedClass'/Game/MyBlueprints/BP\_MyActor.BP\_MyActor\_C'",MemberName="Event ReplicateComponent",MemberGuid=818B4FBA4AB8D2434CFAECA23B4FA1A1),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=62D2FC444CA20DB5E9B3A8955CAC3E2E,PinName="then",Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_0 06F6405B4C0EAC380F0686AAB61C9142,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_CallFunction Name="K2Node\_CallFunction\_0" ExportPath="/Script/BlueprintGraph.K2Node\_CallFunction'/Game/MyBlueprints/BP\_MyActor.BP\_MyActor:EventGraph.K2Node\_CallFunction\_0'"
FunctionReference=(MemberParent="/Script/CoreUObject.Class'/Script/Engine.ActorComponent'",MemberName="SetIsReplicated")
NodePosX=416
NodePosY=681
NodeGuid=BF0399784595F2FE6960EB96EC2720C3
CustomProperties Pin (PinId=06F6405B4C0EAC380F0686AAB61C9142,PinName="execute",PinToolTip="\nExec",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CustomEvent\_0 62D2FC444CA20DB5E9B3A8955CAC3E2E,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=B9CD644C4D6D4BA1C0974A9E6587E6C6,PinName="then",PinToolTip="\nExec",Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=B3041B214B81F199F983ACB72C6313B4,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinToolTip="Target\nActor Component Object Reference",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Engine.ActorComponent'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableGet\_0 148F62B441C32524EE4B75A258C6EDA3,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=63B137774CD10EC982E1EB9977EDDB2A,PinName="ShouldReplicate",PinToolTip="Should Replicate\nBoolean",PinType.PinCategory="bool",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="true",AutogeneratedDefaultValue="false",PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_VariableGet Name="K2Node\_VariableGet\_0" ExportPath="/Script/BlueprintGraph.K2Node\_VariableGet'/Game/MyBlueprints/BP\_MyActor.BP\_MyActor:EventGraph.K2Node\_VariableGet\_0'"
VariableReference=(MemberName="BP\_MyActorComponent",bSelfContext=True)
NodePosX=128
NodePosY=784
NodeGuid=77ABE40B46D72F9B9E5F3CAF2525B65C
CustomProperties Pin (PinId=148F62B441C32524EE4B75A258C6EDA3,PinName="BP\_MyActorComponent",Direction="EGPD\_Output",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/Engine.BlueprintGeneratedClass'/Game/MyBlueprints/BP\_MyActorComponent.BP\_MyActorComponent\_C'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_0 B3041B214B81F199F983ACB72C6313B4,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=2E0192B34CCBEC99A1F485B839A7E62D,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/Engine.BlueprintGeneratedClass'/Game/MyBlueprints/BP\_MyActor.BP\_MyActor\_C'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object

Begin Object Class=/Script/BlueprintGraph.K2Node\_CustomEvent Name="K2Node\_CustomEvent\_0" ExportPath="/Script/BlueprintGraph.K2Node\_CustomEvent'/Game/MyBlueprints/BP\_MyActor.BP\_MyActor:EventGraph.K2Node\_CustomEvent\_0'"
CustomFunctionName="Event ReplicateComponent"
NodePosY=681
NodeGuid=818B4FBA4AB8D2434CFAECA23B4FA1A1
CustomProperties Pin (PinId=421A30E3469187EF6B5740AE931D3780,PinName="OutputDelegate",Direction="EGPD\_Output",PinType.PinCategory="delegate",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(MemberParent="/Script/Engine.BlueprintGeneratedClass'/Game/MyBlueprints/BP\_MyActor.BP\_MyActor\_C'",MemberName="Event ReplicateComponent",MemberGuid=818B4FBA4AB8D2434CFAECA23B4FA1A1),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=62D2FC444CA20DB5E9B3A8955CAC3E2E,PinName="then",Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_0 06F6405B4C0EAC380F0686AAB61C9142,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_CallFunction Name="K2Node\_CallFunction\_0" ExportPath="/Script/BlueprintGraph.K2Node\_CallFunction'/Game/MyBlueprints/BP\_MyActor.BP\_MyActor:EventGraph.K2Node\_CallFunction\_0'"
FunctionReference=(MemberParent="/Script/CoreUObject.Class'/Script/Engine.ActorComponent'",MemberName="SetIsReplicated")
NodePosX=416
NodePosY=681
NodeGuid=BF0399784595F2FE6960EB96EC2720C3
CustomProperties Pin (PinId=06F6405B4C0EAC380F0686AAB61C9142,PinName="execute",PinToolTip="\nExec",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CustomEvent\_0 62D2FC444CA20DB5E9B3A8955CAC3E2E,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=B9CD644C4D6D4BA1C0974A9E6587E6C6,PinName="then",PinToolTip="\nExec",Direction="EGPD\_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=B3041B214B81F199F983ACB72C6313B4,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinToolTip="Target\nActor Component Object Reference",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/CoreUObject.Class'/Script/Engine.ActorComponent'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_VariableGet\_0 148F62B441C32524EE4B75A258C6EDA3,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=63B137774CD10EC982E1EB9977EDDB2A,PinName="ShouldReplicate",PinToolTip="Should Replicate\nBoolean",PinType.PinCategory="bool",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,DefaultValue="true",AutogeneratedDefaultValue="false",PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object
Begin Object Class=/Script/BlueprintGraph.K2Node\_VariableGet Name="K2Node\_VariableGet\_0" ExportPath="/Script/BlueprintGraph.K2Node\_VariableGet'/Game/MyBlueprints/BP\_MyActor.BP\_MyActor:EventGraph.K2Node\_VariableGet\_0'"
VariableReference=(MemberName="BP\_MyActorComponent",bSelfContext=True)
NodePosX=128
NodePosY=784
NodeGuid=77ABE40B46D72F9B9E5F3CAF2525B65C
CustomProperties Pin (PinId=148F62B441C32524EE4B75A258C6EDA3,PinName="BP\_MyActorComponent",Direction="EGPD\_Output",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/Engine.BlueprintGeneratedClass'/Game/MyBlueprints/BP\_MyActorComponent.BP\_MyActorComponent\_C'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,LinkedTo=(K2Node\_CallFunction\_0 B3041B214B81F199F983ACB72C6313B4,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
CustomProperties Pin (PinId=2E0192B34CCBEC99A1F485B839A7E62D,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject="/Script/Engine.BlueprintGeneratedClass'/Game/MyBlueprints/BP\_MyActor.BP\_MyActor\_C'",PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PinType.bIsUObjectWrapper=False,PinType.bSerializeAsSinglePrecisionFloat=False,PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPin=False,)
End Object

## Replicate Actor Component Properties

You can replicate actor component properties the same way that you replicate actor properties. For more information about how to replicate actor properties, see the [Replicate Actor Properties](/documentation/en-us/unreal-engine/replicate-actor-properties-in-unreal-engine) documentation.

## Actor Component Remote Procedure Calls

You can define remote procedure calls (RPCs) within your actor component class and call them the same way that you call actor RPCs. For more information about how to define, implement, and call RPCs, see the [Remote Procedure Calls](/documentation/404) documentation.

## Replicate Actor Component Subobjects

Actor Components can have their own replicated subobjects list in the same way as actors. They use the same API as actors for registering and unregistering their subobjects. Subobjects within an actor component can have replication conditions as well.

The owning component must be replicated to a connection before the conditions of its replicated subobjects are checked. For example, if a subobject has the `COND_OwnerOnly` condition, but is registered to a component that uses the `COND_SkipOwner` condition, the subobject never replicates, because the owner is skipped..

For more information on how to replicate subobjects, see the [Replicate Actor Subobjects](/documentation/en-us/unreal-engine/replicating-uobjects-in-unreal-engine) documentation.

## Bandwidth Overhead

Each replicating actor component within an actor adds:

* A Network Globally Unique Identifier (NetGUID) header consisting of 4 bytes.
* All replicated properties and the space required.
* A footer consisting of approximately 1 byte.

When considering bandwidth overhead, there are three areas to be aware of:

* *Replication*: Compared to replicating an entire actor, the impact of replicating a property on an actor component is relatively low.
* *Calling an RPC*: Calling an RPC from an actor component has more overhead than calling from directly within an actor. To mitigate this, consider routing your actor component RPCs through your actor. For an example of this, see the [character movement component](/documentation/404).
* *Amount of actor components*: Actor components are relatively small. However, if you use a high number of components and component subobjects, your performance might be lower.

* [components](https://dev.epicgames.com/community/search?query=components)
* [programming](https://dev.epicgames.com/community/search?query=programming)
* [networking](https://dev.epicgames.com/community/search?query=networking)
* [replication](https://dev.epicgames.com/community/search?query=replication)
* [actor](https://dev.epicgames.com/community/search?query=actor)
* [properties](https://dev.epicgames.com/community/search?query=properties)
* [actor component](https://dev.epicgames.com/community/search?query=actor%20component)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Types of Actor Components](/documentation/en-us/unreal-engine/replicating-actor-components-in-unreal-engine?application_version=5.7#typesofactorcomponents)
* [Static Actor Components](/documentation/en-us/unreal-engine/replicating-actor-components-in-unreal-engine?application_version=5.7#staticactorcomponents)
* [Replicate a Static Actor Component](/documentation/en-us/unreal-engine/replicating-actor-components-in-unreal-engine?application_version=5.7#replicateastaticactorcomponent)
* [Dynamic Actor Components](/documentation/en-us/unreal-engine/replicating-actor-components-in-unreal-engine?application_version=5.7#dynamicactorcomponents)
* [Replicate a Dynamic Actor Component](/documentation/en-us/unreal-engine/replicating-actor-components-in-unreal-engine?application_version=5.7#replicateadynamicactorcomponent)
* [Blueprint Actor Components](/documentation/en-us/unreal-engine/replicating-actor-components-in-unreal-engine?application_version=5.7#blueprintactorcomponents)
* [Replicate a Static Blueprint Actor Component](/documentation/en-us/unreal-engine/replicating-actor-components-in-unreal-engine?application_version=5.7#replicateastaticblueprintactorcomponent)
* [Replicate a Dynamic Blueprint Actor Component](/documentation/en-us/unreal-engine/replicating-actor-components-in-unreal-engine?application_version=5.7#replicateadynamicblueprintactorcomponent)
* [Replicate Actor Component Properties](/documentation/en-us/unreal-engine/replicating-actor-components-in-unreal-engine?application_version=5.7#replicateactorcomponentproperties)
* [Actor Component Remote Procedure Calls](/documentation/en-us/unreal-engine/replicating-actor-components-in-unreal-engine?application_version=5.7#actorcomponentremoteprocedurecalls)
* [Replicate Actor Component Subobjects](/documentation/en-us/unreal-engine/replicating-actor-components-in-unreal-engine?application_version=5.7#replicateactorcomponentsubobjects)
* [Bandwidth Overhead](/documentation/en-us/unreal-engine/replicating-actor-components-in-unreal-engine?application_version=5.7#bandwidthoverhead)

Related documents

[Object Replication

![Object Replication](https://dev.epicgames.com/community/api/documentation/image/89fd5c0f-64b1-4d26-a324-7f59cb82b770?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/replicating-uobjects-in-unreal-engine)
