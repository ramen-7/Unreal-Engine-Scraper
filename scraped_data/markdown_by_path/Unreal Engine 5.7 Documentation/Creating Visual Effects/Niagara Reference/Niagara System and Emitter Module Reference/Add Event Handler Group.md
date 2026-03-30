<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/add-event-handler-group-reference-for-niagara-effects-in-unreal-engine?application_version=5.7 -->

# Add Event Handler Group

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
7. [Niagara System and Emitter Module Reference](/documentation/en-us/unreal-engine/system-and-emitter-module-reference-for-niagara-effects-in-unreal-engine "Niagara System and Emitter Module Reference")
8. Add Event Handler Group

# Add Event Handler Group

This document provides reference information for modules in the Add Event Handler group.

![Add Event Handler Group](https://dev.epicgames.com/community/api/documentation/image/725593fc-0c39-4b04-8e14-7aa9cf86e072?resizing_type=fill&width=1920&height=335)

 On this page

An **Event Handler** determines how an emitter responds to incoming events. For each event, you create an **Event Handler Properties** item and a **Receive Event** item. There can be multiple events in each emitter.

Events currently do not work with GPU simulation. They can only be used with CPU simulations.

In order to use an Event Handler, you need to first place an [**Event Module**](/documentation/en-us/unreal-engine/particle-update-group-reference-for-niagara-effects-in-unreal-engine#eventsmodules) in the Particle Update group of the emitter that is generating the event. For example, if you want the particles in Emitter B to follow the particles in Emitter A, you would place a **Generate Location Event** module in the Particle Update group of Emitter A. Then you would add an **Event Handler** to Emitter B, along with a **Receive Location Event** item, to listen for that location event.

In order to use events properly, make sure to enable **Requires Persistent IDs** in the **Emitter Properties** item of any emitter that is generating events.

## Event Handler Properties

| Parameter | Description |
| --- | --- |
| **Source** | Click the dropdown to select the source emitter and event. |
| **Execution Mode** | This controls which particles have the event script run on them. Available options are:   * **Spawned Particles**: The event script is run only on particles that were spawned in response to the current event in the emitter. * **Every Particle**: The event script is run on every existing particle in the emitter.    Be careful with this mode, as it can lead to a large amount of runtime work. |
| **Max Events Per Frame** | This sets the number of events that are consumed by this event handler. If the number of events generated is greater than this value, those additional events will be ignored. |
| **Spawn Number** | This controls whether or not particles are spawned as a result of handling this event. If **Random Spawn Number** is checked, this indicates the maximum number of particles spawned. |
| **Min Spawn Number** | If **Random Spawn Number** is checked, this indicates the minimum number of particles spawned. |
| **Random Spawn Number** | Check this box to randomly generate the number of particles that spawn as a result of handling this event. |

## Receive Event Modules

| Module Name | Description |
| --- | --- |
| **Receive Collision Event** | This is required to listen for a generated collision event (created by the **Generate Collision Event** module in the Particle Update group). Optionally, you can enable Inherited Collision Velocity Scale to determine how much of the parent velocity particles will inherit. |
| **Receive Death Event** | This is required to listen for a generated death event (created by the **Generate Death Event** module in the Particle Update group). Optionally, you can enable Inherited Velocity Scale to determine how much of the parent velocity particles will inherit. |
| Receive Location Event | This is required to listen for a generated location event (created by the **Generate Location Event** module in the Particle Update group). The Receive Location Event has the following settings:  ***Inherited Velocity**: This determines how much of the parent velocity the particles inherit.* **Use Acceleration**: Extrapolate from the incoming event's acceleration to determine the new position.  ***Inherit Parent Normalized Age**: This sends the maximum of either the receiving particle lifetime or the parent particle lifetime.* **Spawn Count**: This indicates how many particles are spawning as a result of this event. |

* [effects](https://dev.epicgames.com/community/search?query=effects)
* [module](https://dev.epicgames.com/community/search?query=module)
* [reference](https://dev.epicgames.com/community/search?query=reference)
* [vfx](https://dev.epicgames.com/community/search?query=vfx)
* [event](https://dev.epicgames.com/community/search?query=event)
* [niagara](https://dev.epicgames.com/community/search?query=niagara)
* [visual effects](https://dev.epicgames.com/community/search?query=visual%20effects)
* [particle effects](https://dev.epicgames.com/community/search?query=particle%20effects)
* [emitter](https://dev.epicgames.com/community/search?query=emitter)
* [system](https://dev.epicgames.com/community/search?query=system)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Event Handler Properties](/documentation/en-us/unreal-engine/add-event-handler-group-reference-for-niagara-effects-in-unreal-engine?application_version=5.7#eventhandlerproperties)
* [Receive Event Modules](/documentation/en-us/unreal-engine/add-event-handler-group-reference-for-niagara-effects-in-unreal-engine?application_version=5.7#receiveeventmodules)
