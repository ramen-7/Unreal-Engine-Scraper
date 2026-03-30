<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-ability-system-for-unreal-engine?application_version=5.7 -->

# Gameplay Ability System

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
6. Gameplay Ability System

# Gameplay Ability System

High-level view of the Gameplay Ability System

![Gameplay Ability System](https://dev.epicgames.com/community/api/documentation/image/5d6d1641-c70c-488a-b4eb-3ea5071ef96d?resizing_type=fill&width=1920&height=335)

 On this page

The **Gameplay Ability System** is a framework for building attributes, abilities, and interactions that an [Actor](/documentation/en-us/unreal-engine/actors-in-unreal-engine) can own and trigger. The system is designed to be adapted to a wide variety of [Gameplay-Driven](/documentation/en-us/unreal-engine/data-driven-gameplay-elements-in-unreal-engine) projects such as **Role-Playing Games**(RPGs), **Action-Adventure** games, and **Multiplayer Online Battle Arenas** games(MOBA).

With the Gameplay Ability System, you can:

* Use the [Ability System Component](/documentation/en-us/unreal-engine/gameplay-ability-system-component-and-gameplay-attributes-in-unreal-engine). The Ability System Component includes all the base functionality that an [Actor Component](/documentation/en-us/unreal-engine/components-in-unreal-engine) implements.
* The Ability System Component implements its own [Interface](/documentation/404) to access and interact with the framework of the Gameplay Ability System.
* Create active or passive [Gameplay Abilities](/documentation/en-us/unreal-engine/gameplay-ability-system-for-unreal-engine), for Actors that coordinate with your project's gameplay mechanics, [visual effects](/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine),[animations](/documentation/en-us/unreal-engine/animating-characters-and-objects-in-unreal-engine), [sounds](/documentation/en-us/unreal-engine/working-with-audio-in-unreal-engine), and other data-driven elements.
* Use [Attributes and Attribute Sets](/documentation/en-us/unreal-engine/gameplay-attributes-and-attribute-sets-for-the-gameplay-ability-system-in-unreal-engine) that store, calculate, and modify your gameplay-related values as they interact with the Gameplay Ability System.
* Change Attributes with [Gameplay Effects](/documentation/en-us/unreal-engine/gameplay-systems-in-unreal-engine) that provide a method to directly modify attribute values with your project's design. Gameplay Effects contain Gameplay Effect Components that determine how a Gameplay Effect behaves.
* [Ability Tasks](/documentation/en-us/unreal-engine/gameplay-ability-tasks-in-unreal-engine)(`UAbilityTask`) are a specialized form of a Gameplay Task class that work with Gameplay Abilities. Games that use the Gameplay Ability System usually include a variety of custom Ability Tasks which implement their unique gameplay features. They perform asynchronous work during a Gameplay Ability's execution, and have the capability to affect execution flow by calling Delegates in native C++ code or moving through one or more output execution pins like [Blueprints](/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine).

Using this system, you can create abilities like a single attack, or add more complexity like a spell that triggers many status effects depending on data from the user and the targets.

## Valley of the Ancient Sample

Echo's charge and attack animation and their walking animation are examples of a Gameplay Ability.

See the [Valley of the Ancient Sample](/documentation/en-us/unreal-engine/valley-of-the-ancient-sample-game-for-unreal-engine) for additional features.

### Walking Animation Example

### Charge Attack Example

## Topic Directory

[![Ability System Component And Attributes](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ad948610-6af5-4dfa-ae9d-6166ceeee72c/placeholder_topic.png)

Ability System Component And Attributes

Using the Ability System Component with Gameplay Attributes and Attribute Sets](/documentation/en-us/unreal-engine/gameplay-ability-system-component-and-gameplay-attributes-in-unreal-engine)
[![Gameplay Ability](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8b4cc8a5-adc1-471c-926b-f8f4b81476ef/placeholder_topic.png)

Gameplay Ability

Overview of the Gameplay Ability class.](/documentation/en-us/unreal-engine/using-gameplay-abilities-in-unreal-engine)
[![Gameplay Attributes and Attribute Sets](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d975dfc0-c60b-4671-937d-3808617430ac/placeholder_topic.png)

Gameplay Attributes and Attribute Sets

Using Gameplay Attributes and Attribute Sets](/documentation/en-us/unreal-engine/gameplay-attributes-and-attribute-sets-for-the-gameplay-ability-system-in-unreal-engine)
[![Gameplay Ability System Overview](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e9366280-92d0-441d-a0ae-7e9045dc1a94/placeholder_topic.png)

Gameplay Ability System Overview

A breakdown of the Gameplay Ability System and how each of its component classes contribute to abilities.](/documentation/en-us/unreal-engine/understanding-the-unreal-engine-gameplay-ability-system)
[![Gameplay Effects](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d4b7bf4b-6279-4293-b5db-c51f58f82dcb/placeholder_topic.png)

Gameplay Effects

Overview of Gameplay Effects within the Gameplay Ability System.](/documentation/en-us/unreal-engine/gameplay-effects-for-the-gameplay-ability-system-in-unreal-engine)
[![Ability Tasks](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2c8381fb-55db-4d4f-b840-9461cd69bacb/placeholder_topic.png)

Ability Tasks

Overview of the Ability Task class.](/documentation/en-us/unreal-engine/gameplay-ability-tasks-in-unreal-engine)

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [programming](https://dev.epicgames.com/community/search?query=programming)
* [gameplay ability system](https://dev.epicgames.com/community/search?query=gameplay%20ability%20system)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Valley of the Ancient Sample](/documentation/en-us/unreal-engine/gameplay-ability-system-for-unreal-engine?application_version=5.7#valleyoftheancientsample)
* [Walking Animation Example](/documentation/en-us/unreal-engine/gameplay-ability-system-for-unreal-engine?application_version=5.7#walkinganimationexample)
* [Charge Attack Example](/documentation/en-us/unreal-engine/gameplay-ability-system-for-unreal-engine?application_version=5.7#chargeattackexample)
* [Topic Directory](/documentation/en-us/unreal-engine/gameplay-ability-system-for-unreal-engine?application_version=5.7#topicdirectory)
