<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/system-and-emitter-module-reference-for-niagara-effects-in-unreal-engine?application_version=5.7 -->

# Niagara System and Emitter Module Reference

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
5. [Creating Visual Effects](/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine "Creating Visual Effects")
6. [Niagara Reference](/documentation/en-us/unreal-engine/reference-for-niagara-effects-in-unreal-engine "Niagara Reference")
7. Niagara System and Emitter Module Reference

# Niagara System and Emitter Module Reference

This page links to documents that are part of the Niagara System and Emitter Module Reference.

![Niagara System and Emitter Module Reference](https://dev.epicgames.com/community/api/documentation/image/1f286400-13b5-4dee-a49b-81b4a05eb5ea?resizing_type=fill&width=1920&height=335)

 On this page

This page contains some basic reference information about how modules work in Niagara. Below this reference information, there are links to pages describing each group of items and modules that are included with the Niagara plugin.

## Niagara Selection Stack Model

Particle simulation in Niagara operates as a *stack* simulation flows from the top of the stack to the bottom, executing programmable code blocks called *modules* in order. Crucially, every module is assigned to a *group* that describes when the module is executed.

Modules that are part of the **System** groups execute first, handling behavior that is shared with every emitter. Then, modules and items in the **Emitter** groups execute for each unique emitter. Following this, parameters in the **Particle** groups execute for each unique particle in an individual emitter. Finally, **Render** group items describe how to render each emitter's simulated particle data to the screen.

For more information on the Stack, see the **Niagara Selection Stack and Stack Groups** section in [Niagara Key Concepts](/documentation/en-us/unreal-engine/key-concepts-in-niagara-effects-for-unreal-engine).

**A module is an item, but an item is not a module**. *Modules* are editable assets a user can create. *Items* refer to parts of a system or emitter that the user cannot create. Examples of items are system properties, emitter properties, and renderers.

## Execution State Management

Niagara systems and emitters have a distinct Execution State that defines how their simulation is run. Emitters that are part of a system each have a unique Execution State independent of the owning system, so they can change how they are being executed independent of that owning System. The possible Execution States are:

* **Active**: The System or Emitter simulates and allows spawning.
* **Inactive**: The System or Emitter simulates but does not allow any new spawning.
* **InactiveClear**: The System or Emitter destroys all Particles it owns, and then moves to the Inactive Execution State.
* **Complete**: The System or Emitter does not simulate and does not render.

## Settings, Groups, and Renderers

[![Emitter Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/931b4fce-3597-44c5-a961-11bf22d98cd4/niagara_topic.png)

Emitter Settings

This page contains reference information for the Emitter Settings group in a Niagara emitter.](/documentation/en-us/unreal-engine/emitter-settings-reference-for-niagara-effects-in-unreal-engine)
[![Emitter Spawn Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8431dc58-ee33-4c27-a985-e5638d5eca4b/niagara_topic.png)

Emitter Spawn Group

This document provides reference information for modules in the Emitter Spawn group.](/documentation/en-us/unreal-engine/emitter-spawn-group-reference-for-niagara-effects-in-unreal-engine)
[![Emitter Update Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/359307e7-fe08-4a0b-b48d-1e22e88639ca/niagara_topic.png)

Emitter Update Group

This document provides reference information for Emitter Update modules in a Niagara emitter.](/documentation/en-us/unreal-engine/emitter-update-group-reference-for-niagara-effects-in-unreal-engine)
[![Particle Spawn Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3e20107d-f2ad-4ddc-a030-58e85f51245b/niagara_topic.png)

Particle Spawn Group

This page provides reference information for modules in the Particle Spawn group.](/documentation/en-us/unreal-engine/particle-spawn-group-reference-for-niagara-effects-in-unreal-engine)
[![Particle Update Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9e3573f5-419c-426e-86ca-0e3e94f73970/niagara_topic.png)

Particle Update Group

This page provides reference information for modules in the Particle Update group.](/documentation/en-us/unreal-engine/particle-update-group-reference-for-niagara-effects-in-unreal-engine)
[![Niagara Renderers](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/45556844-a6e2-4365-b426-26b7bb570c11/niagara_topic.png)

Niagara Renderers

This document provides reference information for the Renderer group in a Niagara Emitter.](/documentation/en-us/unreal-engine/render-module-reference-for-niagara-effects-in-unreal-engine)
[![System Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7eba3fd1-5675-46f4-bd07-8abbf4da0290/niagara_topic.png)

System Settings

This page contains reference information for the System Settings group in a Niagara system.](/documentation/en-us/unreal-engine/system-settings-reference-for-niagara-effects-in-unreal-engine)
[![System Spawn Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/23058c93-a3af-4434-8911-0357674fc9e6/niagara_topic.png)

System Spawn Group

This document provides reference information for modules in the System Spawn group.](/documentation/en-us/unreal-engine/system-spawn-group-reference-for-niagara-effects-in-unreal-engine)
[![System Update Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/240e9b03-f437-479f-bbc3-b1d3a2c04605/niagara_topic.png)

System Update Group

This document provides reference information for modules in the System Update group.](/documentation/en-us/unreal-engine/system-update-group-reference-for-niagara-effects-in-unreal-engine)
[![Add Event Handler Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2bbe24ee-0058-4e71-b172-cb4aea4f3c0c/niagara_topic.png)

Add Event Handler Group

This document provides reference information for modules in the Add Event Handler group.](/documentation/en-us/unreal-engine/add-event-handler-group-reference-for-niagara-effects-in-unreal-engine)

* [effects](https://dev.epicgames.com/community/search?query=effects)
* [module](https://dev.epicgames.com/community/search?query=module)
* [reference](https://dev.epicgames.com/community/search?query=reference)
* [vfx](https://dev.epicgames.com/community/search?query=vfx)
* [niagara](https://dev.epicgames.com/community/search?query=niagara)
* [visual effects](https://dev.epicgames.com/community/search?query=visual%20effects)
* [particle effects](https://dev.epicgames.com/community/search?query=particle%20effects)
* [emitter](https://dev.epicgames.com/community/search?query=emitter)
* [system](https://dev.epicgames.com/community/search?query=system)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Niagara Selection Stack Model](/documentation/en-us/unreal-engine/system-and-emitter-module-reference-for-niagara-effects-in-unreal-engine?application_version=5.7#niagaraselectionstackmodel)
* [Execution State Management](/documentation/en-us/unreal-engine/system-and-emitter-module-reference-for-niagara-effects-in-unreal-engine?application_version=5.7#executionstatemanagement)
* [Settings, Groups, and Renderers](/documentation/en-us/unreal-engine/system-and-emitter-module-reference-for-niagara-effects-in-unreal-engine?application_version=5.7#settings,groups,andrenderers)
