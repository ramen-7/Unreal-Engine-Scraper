<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/trigger-volume-actors-in-unreal-engine?application_version=5.7 -->

# Trigger Volume Actors

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
5. [Understanding the Basics](/documentation/en-us/unreal-engine/understanding-the-basics-of-unreal-engine "Understanding the Basics")
6. [Actors and Geometry](/documentation/en-us/unreal-engine/actors-and-geometry-in-unreal-engine "Actors and Geometry")
7. [Actors Reference](/documentation/en-us/unreal-engine/unreal-engine-actors-reference "Actors Reference")
8. Trigger Volume Actors

# Trigger Volume Actors

Actor that can be activated and cause events to occur in the Level.

![Trigger Volume Actors](https://dev.epicgames.com/community/api/documentation/image/a138f584-49ce-4055-b7cd-4d31da54af97?resizing_type=fill&width=1920&height=335)

 On this page

**Triggers** are Actors that are used to cause an event to occur when they are interacted with by some other object in the level. In other words, they are used to trigger events in response to some other action in the level. All of the default Triggers are generally the same, differing only in the shape of the area of influence - box, capsule, and sphere - used by the Trigger to detect if another object has activated it.

|  |  |  |
| --- | --- | --- |
| box trigger | capsule trigger | sphere trigger |
| Box Trigger | Capsule Trigger | Sphere Trigger |

## Placing Triggers

Triggers can be placed in the level by dragging and dropping one of the Trigger types. In **Select** mode, you can drag a Trigger type from the **Place Actors** panel **Basic** tab.

![Placing a trigger](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e8bcfaa1-3a62-4b94-842d-ede45f442560/trigger_place.png)

## Triggering Events

Triggers are used to activate events placed inside of the [Level Blueprint](/documentation/en-us/unreal-engine/level-blueprint-in-unreal-engine). There are several different types of events that a Trigger can activate. The main ones happen in response to some type of collision with another object, such as something hitting or overlapping with the Trigger, or in response to input from the player.

With the Trigger selected in the **Viewport**:

* **Right-click** in the **Level Blueprint Event Graph** and choose one of the events under **Add Event for [Trigger Actor Name]**.

  ![Trigger events context menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/346f6152-ca5d-47c7-b819-95b5282e1ade/trigger_event_context.png)

Choosing an event via either of these methods results in an [Event node](/documentation/en-us/unreal-engine/events-in-unreal-engine) being added to the Level Blueprint for the current level:

![Trigger event in Blueprint](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ac32992e-a8b6-4f97-9da8-ba2a5c5354b5/trigger_event.png)

The exec pin of the new event node will fire each time the particular event occurs - in the example above, any time an Actor overlaps (or runs through) the Trigger:

* [actors](https://dev.epicgames.com/community/search?query=actors)
* [trigger](https://dev.epicgames.com/community/search?query=trigger)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Placing Triggers](/documentation/en-us/unreal-engine/trigger-volume-actors-in-unreal-engine?application_version=5.7#placingtriggers)
* [Triggering Events](/documentation/en-us/unreal-engine/trigger-volume-actors-in-unreal-engine?application_version=5.7#triggeringevents)
