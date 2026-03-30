<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/events-and-event-handlers-in-niagara-effects-for-unreal-engine?application_version=5.7 -->

# Events and Event Handlers Overview

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
6. [Getting Started in Niagara](/documentation/en-us/unreal-engine/getting-started-in-niagara-effects-for-unreal-engine "Getting Started in Niagara")
7. Events and Event Handlers Overview

# Events and Event Handlers Overview

This page gives basic information about using Events and Event Handlers in Niagara.

![Events and Event Handlers Overview](https://dev.epicgames.com/community/api/documentation/image/c20ebc79-24f9-4878-8d93-245e81005d31?resizing_type=fill&width=1920&height=335)

 On this page

In many cases, you will want several emitters in one system to interact with each other to create the effect you want. This usually means that one emitter generates some data, and then other emitters listen for that data, and perform some behavior in reaction to that data. In Niagara, this is done using **Events** and **Event Handlers**. **Events** are the modules that generate specific events that occur in the lifetime of a particle. **Event Handlers** are modules that listen for those generated events, and then initiate a behavior in response to that event.

Currently, events with GPU simulations will not work. Events only work with CPU simulation.

## Events

In order to use events, make sure to enable Requires Persistent IDs in the Emitter Properties of your emitters.

Because events happen dynamically as the particle ages, events are added to the Particle Update group. If you click on the **Plus (+)** next to Particle Update, you will see a section called **Events** in which you can add event modules to the stack.

[![Add Event to Particle Update Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b6d6966a-480b-478e-9fb7-f5c960072b9a/01-add-event-to-particle-update-group.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b6d6966a-480b-478e-9fb7-f5c960072b9a/01-add-event-to-particle-update-group.png)

There are several types of event modules available:

* Location
* Death
* Collision

### Location Events

When you place a **Generate Location Event** module into the Particle Update group of your emitter, each particle spawned in that emitter will generate location data during its lifecycle. You can then set an Event Handler to receive that location data and trigger another behavior.

For example, if you want to create a trail effect for a fireworks rocket, you can place a **Generate Location Event** module into the Particle Update group of your rocket emitter. Then the trail emitter can spawn particles that follow the rocket by using the location data.

[![Generate Location Event](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a4cd3498-23fa-44d3-b438-3e49fcf24b7b/02-generate-location-event.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a4cd3498-23fa-44d3-b438-3e49fcf24b7b/02-generate-location-event.png)

Click image for full size.

### Death Events

When you place a **Generate Death Event** module into the Particle Update group of your emitter, each particle spawned in that emitter will generate an event at the end of its lifetime. There are many ways to use this data. You can trigger another emitter's particle effect when the first emitter's particles die, or you can create chain reactions where each emitter spawns their effect when the previous emitter's particles die. You can also combine Location and Death events to create intricate interactions.

To use our fireworks example, you can generate an explosion effect to spawn at the end of the rocket particle's life. The Location event determines where the rocket particle is, which is where the explosion occurs. The Death event determines when the particle's lifetime ends, which is when the explosion effect is spawned.

[![Generate Death Event](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/14934b38-0d8d-49d0-ada6-8035f413fc54/03-generate-death-event.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/14934b38-0d8d-49d0-ada6-8035f413fc54/03-generate-death-event.png)

Click image for full size.

### Collision Events

When you place a **Generate Collision Event** module into the Particle Update group of your emitter, particles will generate an event when they collide with an Actor, such as a static mesh or skeletal mesh. For example, if you want to change the firework effect into a weapon effect, you could have the explosion spawn when the rocket particles collide with a static or skeletal mesh.

[![Generate Collision Event](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1adf447e-8eda-42ab-86dd-4fbea0af2555/04-generate-collision-event.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1adf447e-8eda-42ab-86dd-4fbea0af2555/04-generate-collision-event.png)

Click image for full size.

You need to add a **Collision** module to an emitter before you can add a **Generate Collision Event** to that emitter. This enables the emitter's particles to collide with objects in the world.

## Event Handlers

Event Handlers consist of two parts: **Event Handler Properties**, and a **Receive Event**. For each event you want the emitter to respond to, you will add an **Event Handler Properties** item, and a **Receive Event** module.

If you click the **Plus (+)** next to Emitter Properties, you will be able to add an **Event Handler** stage to your emitter.

[![Add Stage to Emitter](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1ffaa648-ceb5-4efc-a620-6b444e05b208/05-add-stage-to-emitter.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1ffaa648-ceb5-4efc-a620-6b444e05b208/05-add-stage-to-emitter.png)

Click image for full size.

In **Event Handler Properties**, set the **Source** of the event with a dropdown that lists all of the Generate Event modules that are available. Then you can choose what particles are affected by the event, how many times the event occurs per frame, and if the event spawns particles you can select how many are spawned.

[![Event Handler Properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b9ae5bc5-86ea-4270-b4cf-288dfa5729f6/06-event-handler-properties.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b9ae5bc5-86ea-4270-b4cf-288dfa5729f6/06-event-handler-properties.png)

Click image for full size.

After you set the properties for the Event Handler, click the **Plus (+)** next to **Event Handler** to add a **Receive Event** module. It must match the generated event module you placed in the Particle Update group of the emitter that generates the event.

[![Add Receive Location Event](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1770810a-0338-4af3-afd8-21664f63bd96/07-add-receive-location-event.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1770810a-0338-4af3-afd8-21664f63bd96/07-add-receive-location-event.png)

Click image for full size.

For example, if you placed a **Generate Location Event** in an emitter, you would select the **Receive Location Event** module for your Event Handler.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/353a8e2c-2494-4a09-8e2b-382f9f0337f8/08-generate-and-receive-location-event.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/353a8e2c-2494-4a09-8e2b-382f9f0337f8/08-generate-and-receive-location-event.png)

Click image for full size.

* [events](https://dev.epicgames.com/community/search?query=events)
* [effects](https://dev.epicgames.com/community/search?query=effects)
* [getting started](https://dev.epicgames.com/community/search?query=getting%20started)
* [vfx](https://dev.epicgames.com/community/search?query=vfx)
* [niagara](https://dev.epicgames.com/community/search?query=niagara)
* [visual effects](https://dev.epicgames.com/community/search?query=visual%20effects)
* [particle effects](https://dev.epicgames.com/community/search?query=particle%20effects)
* [event handler](https://dev.epicgames.com/community/search?query=event%20handler)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Events](/documentation/en-us/unreal-engine/events-and-event-handlers-in-niagara-effects-for-unreal-engine?application_version=5.7#events)
* [Location Events](/documentation/en-us/unreal-engine/events-and-event-handlers-in-niagara-effects-for-unreal-engine?application_version=5.7#locationevents)
* [Death Events](/documentation/en-us/unreal-engine/events-and-event-handlers-in-niagara-effects-for-unreal-engine?application_version=5.7#deathevents)
* [Collision Events](/documentation/en-us/unreal-engine/events-and-event-handlers-in-niagara-effects-for-unreal-engine?application_version=5.7#collisionevents)
* [Event Handlers](/documentation/en-us/unreal-engine/events-and-event-handlers-in-niagara-effects-for-unreal-engine?application_version=5.7#eventhandlers)
