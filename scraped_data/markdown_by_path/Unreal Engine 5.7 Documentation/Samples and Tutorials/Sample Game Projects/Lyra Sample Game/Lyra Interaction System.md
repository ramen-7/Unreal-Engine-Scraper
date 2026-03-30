<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/lyra-sample-game-interaction-system-in-unreal-engine?application_version=5.7 -->

# Lyra Interaction System

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
5. [Samples and Tutorials](/documentation/en-us/unreal-engine/samples-and-tutorials-for-unreal-engine "Samples and Tutorials")
6. [Sample Game Projects](/documentation/en-us/unreal-engine/sample-game-projects-for-unreal-engine "Sample Game Projects")
7. [Lyra Sample Game](/documentation/en-us/unreal-engine/lyra-sample-game-in-unreal-engine "Lyra Sample Game")
8. Lyra Interaction System

# Lyra Interaction System

An overview of the Lyra Interaction System for the Lyra Game sample.

![Lyra Interaction System](https://dev.epicgames.com/community/api/documentation/image/e7ac277c-00de-4bac-b32f-467c0ef226cd?resizing_type=fill&width=1920&height=335)

 On this page

## Lyra Interaction System

Lyra uses its interaction [Interface](https://dev.epicgames.com/documentation/en-us/unreal-engine/interfaces-in-unreal-engine?application_version=5.5)/[IInterface](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject/IInterface?application_version=5.5) through its own [Gameplay Ability](https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-ability-system-for-unreal-engine)/[UGameplayAbility](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/GameplayAbilities/Abilities/UGameplayAbility?application_version=5.5) (ULyraGameplayAbility\_Interact) which establishes a cause and effect relationship between how the player Interacts with objects in Lyra, and how those objects interact with the player.

Using the `LyraGameplayAbility_Interact` class, you can manage the logic of how your interactions are called.

**ULyraGameplayAbility\_Interact.h**

C++

```
#pragma once
		#include "CoreMinimal.h"
		#include "AbilitySystem/Abilities/LyraGameplayAbility.h"
		#include "Interaction/InteractionQuery.h"
		#include "Interaction/IInteractableTarget.h"
		#include "LyraGameplayAbility_Interact.generated.h"

		class FIndicatorDescriptor;
		/**
```

Expand code  Copy full snippet(48 lines long)

`AbilityTask_WaitForInteractableTargets_SingleLineTrace` is a Gameplay [Ability Task](https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-ability-tasks-in-unreal-engine), which performs a line trace and waits in a looped timer until it hits an Actor that implements the interface.

As an example:

A player controlling a LyraPawnActor is low on health, the player directs the Pawn towards a collectible health item pickup. Upon aligning the player's crosshair with the Collectible, and pressing the "Use/Interact" key, a Line Trace is fired from the Pawn. When the trace hits the Collectible, the interaction interface implemented on the Collectible will handle the logic to restore the Player's health to its full amount.

## Interaction Ability Tasks

`UAbilityTask_WaitForInteractableTargets` is used to make a new method of tracing for interactable targets.

As an example:

A player controlling a LyraPawnActor approaches a door that they want to open. Upon aligning the player's crosshair with the door and pressing the "Use" key, a radial menu appears with the options to "Unlock/Lock" the door, or attempt to open the door.

For additional information on Line Traces in Unreal, See [Tracing](https://dev.epicgames.com/documentation/en-us/unreal-engine/traces-tutorials-in-unreal-engine)

**UAbilityTask\_WaitForInteractableTargets.h**

C++

```
#pragma once
		#include "CoreMinimal.h"
		#include "UObject/ObjectMacros.h"
		#include "Abilities/Tasks/AbilityTask.h"
		#include "Engine/EngineTypes.h"
		#include "CollisionQueryParams.h"
		#include "WorldCollision.h"
		#include "Engine/CollisionProfile.h"
		#include "Abilities/GameplayAbilityTargetDataFilter.h"
		#include "Interaction/InteractionOption.h"
```

Expand code  Copy full snippet(44 lines long)

Your chosen AbilityTask for tracing delivers a set of Interactable targets from the `FInteractionQuery` struct.

**struct FInteractionQuery**

C++

```
#pragma once
		#include "CoreMinimal.h"
		#include "Abilities/GameplayAbility.h"
		#include "InteractionQuery.generated.h"

		/**  */
		USTRUCT(BlueprintType)
		struct FInteractionQuery
		{
```

Expand code  Copy full snippet(25 lines long)

to the method `UAbilityTask_WaitForInteractableTargets::UpdateInteractableOptions`:

C++

```
void UAbilityTask_WaitForInteractableTargets::UpdateInteractableOptions(const FInteractionQuery& InteractQuery, const TArray<TScriptInterface<IInteractableTarget>>& InteractableTargets)
		{

			TArray<FInteractionOption> NewOptions;

			for (const TScriptInterface<IInteractableTarget>& InteractiveTarget : InteractableTargets)

			{

				TArray<FInteractionOption> TempOptions;
```

Expand code  Copy full snippet(126 lines long)

which will call `IInteractableTarget::GatherInteractionOptions` on each interactable target.

C++

```
virtual void GatherInteractionOptions(const FInteractionQuery& InteractQuery, FInteractionOptionBuilder& OptionBuilder) = 0;
```

virtual void GatherInteractionOptions(const FInteractionQuery& InteractQuery, FInteractionOptionBuilder& OptionBuilder) = 0;

Copy full snippet(1 line long)

Once you update the set of interactable objects, the interaction ability (GA\_Interact) calls the `TriggerInteraction` function when the player focuses on an object to interact with and receives input from the player that they want to interact with that particular object.

Once you invoke the current Option, there are two methods by which interactions can occur. The first method grants an ability to the player's Ability System Component through the function `FInteractionOption::InteractionAbilityToGrant`, using this function is recommended for simple logic such as the Weapon Pickup Actor.

Alternatively, if you're interacting with an object that contains its own Ability System Component to handle complex logic, then you can invoke the `FInteractionOption::TargetAbilitySystem` and the `FInteractionOption::TargetInteractionHandle` functions, this invokes the ability on the interactable object, instead of invoking the ability on the Lyra Character's (Avatar) Ability System Component.

The interaction function `FInteractionOption::InteractionAbilityToGrant` is inherited from the base class of your `ULyraGameplayAbility_Interact` interaction ability, which runs the task function `AbilityTask_GrantNearbyInteraction`, as a ranged loop and timer that collects nearby abilities and grants them to your character before you attempt to interact with them. You can increase the `InteractionScanRate` float to be at a larger radius than your `InteractionRange`, otherwise, replication will not deliver the ability to the client soon enough.

The ability is invoked through the event [Gameplay Tag](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-gameplay-tags-in-unreal-engine?application_version=5.5), `FInteractionOption::InteractionEventTag`. This tag needs to match up to a trigger in your ability. For example, the `GA_Collect_Interaction` is triggered when the `Ability.Type.Interact.Collect` event is sent, which is set in the interaction option.

[![](https://dev.epicgames.com/community/api/documentation/image/e9a930d2-0c77-4053-9634-4b342fd2a5ad?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e9a930d2-0c77-4053-9634-4b342fd2a5ad?resizing_type=fit)

`GA_Collect_Interaction` represents only one kind of interaction, it is an ability that provides you the capability to pick up objects on the ground and add them to your inventory. There is no limit to your imagination, you can make an ability to eat Apples on the ground that will refill your player's health, or you could make an ability to open doors, get into a vehicle, or open a chest.

This decoupling behavior provides you with all kinds of different interactions from the central passive interaction scanner.

#### Important Lyra Interaction Terminology

**InteractableTarget** - An Actor or Component that implements the IInteractableTarget interface, this determines what objects in the world can be interacted with.

**InteractionOption** - The "Affordance" or "Option", for example, an apple might provide both a "Collect" and a "Consume".

**InteractionInstigator** - The Pawn (LyraPawnActor) that initiates the interaction. They may or may not implement the `IInteractionInstigator` interface, which allows further customization of options and how they are presented.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Lyra Interaction System](/documentation/en-us/unreal-engine/lyra-sample-game-interaction-system-in-unreal-engine?application_version=5.7#lyra-interaction-system)
* [Interaction Ability Tasks](/documentation/en-us/unreal-engine/lyra-sample-game-interaction-system-in-unreal-engine?application_version=5.7#interaction-ability-tasks)
* [Important Lyra Interaction Terminology](/documentation/en-us/unreal-engine/lyra-sample-game-interaction-system-in-unreal-engine?application_version=5.7#important-lyra-interaction-terminology)
