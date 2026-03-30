<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/scene-state-for-unreal-engine?application_version=5.7 -->

# Scene State

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
5. [Motion Design](/documentation/en-us/unreal-engine/motion-design-in-unreal-engine "Motion Design")
6. Scene State

# Scene State

An overview of Motion Design Scene State.

![Scene State](https://dev.epicgames.com/community/api/documentation/image/bbdae9ab-78ac-4f8f-9304-c7802788b51c?resizing_type=fill&width=1920&height=335)

 On this page

## What is Motion Design Scene State?

**Motion Design Scene State** is a state machine plugin designed for broadcast graphics to have behavior encapsulated in states. The main goal of this plugin is to provide a way to isolate different behaviors within a graphic while also defining a relationship between these behaviors and states so that it results in an easier, more maintainable way to build logic.

The plugin itself is built to be usable outside of Motion Design levels. A second plugin, **Motion Design Scene State Integration**, exists to integrate scene state into Motion Design levels, and offer Motion Design-specific tasks.

If you are familiar with state machines in Animation Blueprints, a lot of the elements in Motion Design Scene State will be familiar to you. However, keep in mind that these two systems are completely different and are designed to solve different problems.

## Overview

[![Scene State User Interface](https://dev.epicgames.com/community/api/documentation/image/e4db1730-ffb6-4c03-a367-9f075309c8bc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e4db1730-ffb6-4c03-a367-9f075309c8bc?resizing_type=fit)

1. State Machine List Tab

   * Lists all the state machines present in the Scene State Blueprint.
   * Add new state machines by clicking on the ‘Add’ button.
   * Select a state machine to view and edit its settings in the details view (4).
   * Double-click a state machine to open them in the graph view (7).
   * Drag a state machine to reorder them and categorize them.
2. Debug View Tab

   * Viewpoint of the debugged Scene State object.
   * For a Motion Design Scene State object, the viewpoint is the game viewport.
   * You can change the debugged object from the debug toolbar (3).
3. Play World and Debug Toolbar

   * Play the current world in a specified mode (PIE, Standalone)
   * Set the debugged object to inspect the scene state behavior and data for that object.
   * You can visualize Scene State behavior and data in the graph view (7) and debug controls (8).
4. Details View Tab

   * The Property editor tab for the currently selected editor object.
   * This object can be a state, state machine, transition, task, or a Blueprint node like a variable and function, macro, or similar.
5. Property Binding Extension

   * An extension to the Details view to provide a way for the target property to be bound to a source property or a property function.
   * A source property can be a Blueprint variable, for example.
   * It is only available for properties that are bindable.
6. My Blueprint Tab

   * Like other Blueprints, it holds the variables, functions, events, and other nodes for the Blueprint.
   * You can add new variables, events, functions or other nodes by clicking the Add button.
7. Graph View

   * Shows the currently opened graphs.
   * These graphs can be state machine graphs, transition graphs, or Blueprint graphs like function or event graphs.
   * When in play, it shows the current execution flow for the currently debugged object.
   * You can change the debugged object from the debug toolbar (3).
8. Debug Controls

   * Send events to or change the data of the currently debugged object to inspect behavior changes in play.
   * You can change the debugged object from the debug toolbar (3).

### State

A **state** is the base object in a state machine. Only one state can be active at a time in a state machine. A state can have tasks, transitions to other states (known as exit transitions), child state machines, and event handlers. Each is discussed in its own section.

When a state becomes active, the state stores the event data required by the event handlers (if any) and both the task graph and child state machines start their execution.

[![State node](https://dev.epicgames.com/community/api/documentation/image/2cc238dc-e7f2-4827-a07a-c9bc1c7dba6d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2cc238dc-e7f2-4827-a07a-c9bc1c7dba6d?resizing_type=fit)

### State Machine

A **state machine** is the base starting point of execution in a scene state system. Top-level state machines have a Run Mode property you can set to either Auto or Manual.

* **Auto** means that when the scene state system starts, the state machine will start as well. This is the default option.
* **Manual** means that the state machine will not automatically start, but rather can be started by other means like the Run State Machine task.

[![State machine category and run mode](https://dev.epicgames.com/community/api/documentation/image/6a8fec2d-8d56-4aea-851e-0dc675aab552?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6a8fec2d-8d56-4aea-851e-0dc675aab552?resizing_type=fit)

[![State machine graph](https://dev.epicgames.com/community/api/documentation/image/9f1e8141-8413-49a4-8213-547693fa1ae5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9f1e8141-8413-49a4-8213-547693fa1ae5?resizing_type=fit)

Due to the underlying scene state architecture, the same state machine can be executed multiple times simultaneously, each execution managing its own instance data separately.

State Machines also contain parameters. For more information, see [State Machine Parameters](https://dev.epicgames.com/documentation/en-us/unreal-engine/scene-state-for-unreal-engine#state-machine-parameters).

### Entry

An **entry** indicates to the owning state machine which state to first activate when the state machine starts. Only one entry node is considered in a state machine graph.

[![Entry node](https://dev.epicgames.com/community/api/documentation/image/49ef8402-9847-4e9f-86ba-b678bc93b745?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/49ef8402-9847-4e9f-86ba-b678bc93b745?resizing_type=fit)

### Exit

An **exit** indicates to the state machine to finish execution. It is optional so a state machine can have none or multiple. Exits can be a target to transitions, but cannot be a source, as once a transition to an exit executes, the owning state machine’s execution stops.

[![Exit node](https://dev.epicgames.com/community/api/documentation/image/dbfd8008-aa00-4f61-8df6-b834eeb64571?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dbfd8008-aa00-4f61-8df6-b834eeb64571?resizing_type=fit)

### Task

A **task** is the main implementable object in the scene state system. It holds specific logic to execute at runtime. Built-in examples include Print String, Delay, and similar. You can implement tasks in either C++ or Blueprints, but C++ is preferable as it has a clearer distinction between logic and instance data, which makes it more performant and memory efficient.

A task can only be owned by one state. A task starts execution when both its owning state is active and its prerequisite tasks are complete. These prerequisite tasks are also owned by the same state.

[![State task graph](https://dev.epicgames.com/community/api/documentation/image/d3e52f60-23bb-4211-93c6-b1d4af93f825?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d3e52f60-23bb-4211-93c6-b1d4af93f825?resizing_type=fit)

In the example above, the state owns three tasks: Print Red, Print Blue, and Wait 1s, a delay task. Only Print Blue has a prerequisite task, which is the Wait 1s delay task. This means that once the state becomes active, both the Print Red and the delay task execute in the same frame, and Print Blue executes once the one second wait is over.

A task with more than one prerequisite executes only when all the prerequisite tasks are complete.

### Transition

A **transition** defines a link from a source to a target. The source and targets are typically a state, but can also be conduits or exits (exits can only be targets to a transition).

[![State machine transition](https://dev.epicgames.com/community/api/documentation/image/0b55093e-9bc0-4654-b11d-712b811292ee?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0b55093e-9bc0-4654-b11d-712b811292ee?resizing_type=fit)

[![State machine transition settings](https://dev.epicgames.com/community/api/documentation/image/d84afd0c-b24a-411b-a7a5-dc019c15f712?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d84afd0c-b24a-411b-a7a5-dc019c15f712?resizing_type=fit)

Transitions have a priority value. Transitions exiting from the same state or conduit are evaluated in order from highest to lowest priority. The first transition whose conditions are satisfied is executed. If the transition is to another state, the source state becomes inactive and the target state becomes active. If the transition is to an exit, the owning state machine’s execution stops. If the transition is to a conduit, that conduit is evaluated (its exit transitions are evaluated and the process repeats for these).

A transition has a **Wait for tasks to finish** option. If enabled, the state’s tasks must all complete prior to the transition being considered.

[![State machine transition to an event](https://dev.epicgames.com/community/api/documentation/image/b79745f8-296d-451c-bf7c-da11ee71947e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b79745f8-296d-451c-bf7c-da11ee71947e?resizing_type=fit)

If a transition is to a target state that requires first pushing or broadcasting certain events, the transition also checks that these events are present in the stream. If they are not, the transition is not considered in that evaluation pass. In the above example, the transition from State A to On Event X can only occur if Event X is present in the event stream. For more information about events, see [Event](https://dev.epicgames.com/documentation/en-us/unreal-engine/scene-state-for-unreal-engine#event).

#### Transition Graph

[![Transition graph](https://dev.epicgames.com/community/api/documentation/image/3dbafe3a-5add-459f-871b-06fd8878662e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3dbafe3a-5add-459f-871b-06fd8878662e?resizing_type=fit)

**Transition graphs** are Blueprint graphs that have a boolean as a result that determines whether the transition can occur. Because it goes through the Blueprint system, these graphs are executed last when evaluating a transition. If the other conditions are not met, the transition graph is not executed at all.

In addition, transition graphs with **Can Transition** set to true explicitly get compiled to have no Blueprint overhead. Transition graphs with Can Transition set to false explicitly do not get compiled at all so the transition link does not exist at all in the compiled data.

Transitions have parameters you can use with the transition graphs. For more information, see [Transition Parameters](https://dev.epicgames.com/documentation/en-us/unreal-engine/scene-state-for-unreal-engine#transition-parameters).

### Conduit

**Conduits** are a transition indirection and can hold multiple exit transitions to other targets. A conduit can be connected from multiple states (or other conduits), enabling a reduction of transition links in cases where these same transitions and rules are reusable across multiple states.

A conduit, like a transition, becomes relevant when one of its source states is currently active in the state machine. Conduits have an additional condition graph to determine whether the conduit should be enabled or not.

[![Complex transitions](https://dev.epicgames.com/community/api/documentation/image/cff1bc3b-7f08-465e-a5ef-c6a9b5a63fda?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cff1bc3b-7f08-465e-a5ef-c6a9b5a63fda?resizing_type=fit)

[![Simplified conduit](https://dev.epicgames.com/community/api/documentation/image/583a9ad7-f687-44ab-93d2-3a70f628f3ca?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/583a9ad7-f687-44ab-93d2-3a70f628f3ca?resizing_type=fit)

The example above illustrates the benefits of using a conduit. Both graphs express that each state in the graph can transition to the other. The conduit version reduces the number of transition links from twelve to eight while also increasing clarity. This reduction in transition links improves the more states you add.

### Event

When an interesting thing happens outside of a scene state system, it can push an **event** to the scene state system’s event stream, so that it can be handled.

An event is created from an **event schema** which holds a name and an optional user defined struct. These event schemas are held in an **Event Schema Collection** asset. The example below shows a collection with two event schemas:

* Event X that has no properties.
* Event Y that has two properties.

[![Event schema collection](https://dev.epicgames.com/community/api/documentation/image/76a64c69-9ba9-43e9-867d-2b75a4e4669e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/76a64c69-9ba9-43e9-867d-2b75a4e4669e?resizing_type=fit)

#### Event Stream

An **event stream** is the queue of events for a particular scene state system. An event can either be pushed directly to an event stream, or broadcast to a particular context, where all the event streams in that context push a copy of that event to their own stream.

[![Event stream](https://dev.epicgames.com/community/api/documentation/image/c2335c15-d452-4ee0-9904-55d1d607baa2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c2335c15-d452-4ee0-9904-55d1d607baa2?resizing_type=fit)

One of the principal ways to broadcast or push events is using the Blueprint API that provides both the **Broadcast Event** and **Push Event** nodes. A Broadcast Event only requires a world context object (for example, an actor, component, or similar), whereas a Push Event requires an explicit stream to push the event to.

These event nodes automatically create pins matching the payload struct of the event. In the example above, the Broadcast Event: Event Y node automatically adds Property A and Property B pins to match the Event Y payload struct.

### Event Handler

**Event handlers** are objects that take ownership of particular events pushed in a stream. This is referred to as capturing events. When an event is captured by a handler, it is no longer visible to other handlers in the stream, and only accessible to the handler that captured the event.

Event handlers are composed of a unique ID, and a handle to an event schema, so that any event created with that event schema is prone to be captured by the event handler.

As mentioned above, you can set states to have event handlers. When a state is activated, it signals to all its event handlers to capture their matching events. The data these captured events hold is then forwarded to tasks in the system by the property binding system. For more information about this binding mechanism, see [Property Binding System](https://dev.epicgames.com/documentation/en-us/unreal-engine/scene-state-for-unreal-engine#property-binding-system).

[![State machine event handler](https://dev.epicgames.com/community/api/documentation/image/59316443-e815-45bb-a0d9-5f47dfb366c8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/59316443-e815-45bb-a0d9-5f47dfb366c8?resizing_type=fit)

In the example above, the On Event Y state has a handler to the Event Y schema, and so its tasks like the ‘Print String’ task can bind to the payload data of Event Y, which in this case can be Property B. When Event Y gets pushed to the stream, it contains data in that Property B string and is copied to the Print String Message argument.

### Property Binding System

A simple task like Print String has a Message parameter you can set in the Details panel directly. However in a real scenario, tasks usually require something beyond a fixed value. This value can come from Blueprint variables, events, and other sources.

You can use the **property binding system** to solve this. It binds source data to target data. For a task, the target is the task instance data itself. In the example described above, the target struct in this case is the struct containing the message parameter. The source data for a task can be Blueprint variables, events captured by event handlers in the owning state, state machine parameters (of the owning state machine), or results from property functions.

[![Proeprty binding variable data source](https://dev.epicgames.com/community/api/documentation/image/93ab3251-4fc7-4ad9-9119-1b875591b1d8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/93ab3251-4fc7-4ad9-9119-1b875591b1d8?resizing_type=fit)

[![Property binding in the state machine](https://dev.epicgames.com/community/api/documentation/image/507b6a46-c89a-4e6b-86a1-ce38f0ca909f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/507b6a46-c89a-4e6b-86a1-ce38f0ca909f?resizing_type=fit)

[![Property binding data bound to task](https://dev.epicgames.com/community/api/documentation/image/eabad7e6-9613-4281-940e-420f0521cae9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/eabad7e6-9613-4281-940e-420f0521cae9?resizing_type=fit)

The example above illustrates how to bind the SourceMessage variable in the Scene State Blueprint to the Print String task Message parameter.

These bindings get applied once, just before the task starts execution. The bindings are copy operations, so for Print String dealing with its Message parameter, it’s dealing with a copy of the value SourceMessage had at the time. Print String executes its logic immediately, but for tasks that process data at a later time, the source data they copied might have already changed and the data they then process would be only a copy of the source data at the time the task started. For more information, see Property Functions.

As mentioned in the Event Handler section, if a state has event handlers, it means that the state can only be activated if the necessary events are present in the stream. If an event handler is added to a state, the state knows the event data will be present when the state is activated, and so this event data is available as a source for binding:

[![Event handler property binding](https://dev.epicgames.com/community/api/documentation/image/afa7cc0c-213f-48c2-a46c-484f8b0c50da?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/afa7cc0c-213f-48c2-a46c-484f8b0c50da?resizing_type=fit)

### Property References

**Property references** give the binding system a way to handle a property by reference rather than by copy. This means the tasks can not only save on copy operations for large structs, but tasks can also write back to properties.

At the moment, property references are limited to being usable in C++ tasks only, but support for Blueprint Tasks is planned.

[![State machine print Hello World!](https://dev.epicgames.com/community/api/documentation/image/4dbd6766-0c0f-4d24-b1e4-7f48d715d13d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4dbd6766-0c0f-4d24-b1e4-7f48d715d13d?resizing_type=fit)

The example above shows the Set String tasks, one of multiple setter tasks where the Target parameter is a property reference. In this example, running the task sets the Source Message variable to "Hello World!".

In addition, you can use property references in parameters like State Machine parameters:

[![Setting state machine parameters](https://dev.epicgames.com/community/api/documentation/image/30064944-9439-4f07-8633-e13b6c78fe38?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/30064944-9439-4f07-8633-e13b6c78fe38?resizing_type=fit)

[![State machine parameters](https://dev.epicgames.com/community/api/documentation/image/71c2d210-2869-4117-a1f3-7068d7044230?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/71c2d210-2869-4117-a1f3-7068d7044230?resizing_type=fit)

### Property Functions

Direct binding to properties works well if the source data type is compatible and is in a usable format for the task. In situations where this is not the case, the source data either needs to change to make it usable for the task, or additional custom tasks are needed to address this. Neither option is ideal.

**Property functions** are a layer of logic that execute prior to applying property bindings. The functions mediate between the source data and the target data.

Currently, property functions are only implementable in C++.

For example, a property function like Integer to String gives you a way to feed a source data of type integer into a task’s string parameter. These functions can be found in the same property binding menu, and their availability/visibility depend on the target property type:

[![State machine set property function source data](https://dev.epicgames.com/community/api/documentation/image/408b1180-4257-4543-b0bf-019187c6dffb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/408b1180-4257-4543-b0bf-019187c6dffb?resizing_type=fit)

[![State machine set property function target data](https://dev.epicgames.com/community/api/documentation/image/381c4586-3892-431c-88cb-6eb08e4d883a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/381c4586-3892-431c-88cb-6eb08e4d883a?resizing_type=fit)

[![State machine complete property function](https://dev.epicgames.com/community/api/documentation/image/d5ab53ab-ef90-4977-bf59-dff6c327c670?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d5ab53ab-ef90-4977-bf59-dff6c327c670?resizing_type=fit)

In the above example, only string functions are shown, as the target property Message is a string. The Integer to String function is used to bind to the Count integer variable.

Property functions unlock all sorts of capabilities. As an example, in combination with property references, the Count integer variable can be incremented using the Integer setter task:

[![State machine use property function](https://dev.epicgames.com/community/api/documentation/image/7ccbdeb6-8095-4625-984c-73f868c8db81?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7ccbdeb6-8095-4625-984c-73f868c8db81?resizing_type=fit)

Below you can see the result after activating State A multiple times to rerun its tasks:

[![State machine property function output](https://dev.epicgames.com/community/api/documentation/image/22e871b2-eb3d-4f2b-9110-5095115cc5a9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/22e871b2-eb3d-4f2b-9110-5095115cc5a9?resizing_type=fit)

### State Machine Parameters

A state machine can have **parameters**.

[![State machine parameters](https://dev.epicgames.com/community/api/documentation/image/8b37357e-bc67-4f1a-8b48-ed48f131cdcb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8b37357e-bc67-4f1a-8b48-ed48f131cdcb?resizing_type=fit)

When executing state machines using the **Run State Machine** task, you can edit these parameters. In the example below, the same state machine is run twice, but with different parameters passed to it.

[![State machine parameters version 1](https://dev.epicgames.com/community/api/documentation/image/bbd3a865-fae8-4fc0-898e-9332b178cb7a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bbd3a865-fae8-4fc0-898e-9332b178cb7a?resizing_type=fit)

[![State machine parameters version 2](https://dev.epicgames.com/community/api/documentation/image/e8ba4e28-3633-4eea-9f77-98896b6f6d3c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e8ba4e28-3633-4eea-9f77-98896b6f6d3c?resizing_type=fit)

These state machine parameters are available for binding for tasks and transition parameters:

[![State machine using parameters](https://dev.epicgames.com/community/api/documentation/image/31d14d73-5f47-4da3-98a4-e9ad1530451b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/31d14d73-5f47-4da3-98a4-e9ad1530451b?resizing_type=fit)

### Transition Parameters

Similar to state machine parameters, **transitions** also have **parameters**. The primary reason for transitions to have parameters is to bridge the transition graph with data accessible through the property binding system like state machine parameters, events, and similar.

[![State machine transition parameters](https://dev.epicgames.com/community/api/documentation/image/a2f92344-f970-4764-9cfa-5b06f789e0d2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a2f92344-f970-4764-9cfa-5b06f789e0d2?resizing_type=fit)

These parameters can then be accessed in the transition graph using the Transition Parameters node:

[![Transition graph parameters node](https://dev.epicgames.com/community/api/documentation/image/01cc468d-f167-42af-9677-3105fb55e6c6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/01cc468d-f167-42af-9677-3105fb55e6c6?resizing_type=fit)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [What is Motion Design Scene State?](/documentation/en-us/unreal-engine/scene-state-for-unreal-engine?application_version=5.7#whatismotiondesignscenestate?)
* [Overview](/documentation/en-us/unreal-engine/scene-state-for-unreal-engine?application_version=5.7#overview)
* [State](/documentation/en-us/unreal-engine/scene-state-for-unreal-engine?application_version=5.7#state)
* [State Machine](/documentation/en-us/unreal-engine/scene-state-for-unreal-engine?application_version=5.7#statemachine)
* [Entry](/documentation/en-us/unreal-engine/scene-state-for-unreal-engine?application_version=5.7#entry)
* [Exit](/documentation/en-us/unreal-engine/scene-state-for-unreal-engine?application_version=5.7#exit)
* [Task](/documentation/en-us/unreal-engine/scene-state-for-unreal-engine?application_version=5.7#task)
* [Transition](/documentation/en-us/unreal-engine/scene-state-for-unreal-engine?application_version=5.7#transition)
* [Transition Graph](/documentation/en-us/unreal-engine/scene-state-for-unreal-engine?application_version=5.7#transitiongraph)
* [Conduit](/documentation/en-us/unreal-engine/scene-state-for-unreal-engine?application_version=5.7#conduit)
* [Event](/documentation/en-us/unreal-engine/scene-state-for-unreal-engine?application_version=5.7#event)
* [Event Stream](/documentation/en-us/unreal-engine/scene-state-for-unreal-engine?application_version=5.7#eventstream)
* [Event Handler](/documentation/en-us/unreal-engine/scene-state-for-unreal-engine?application_version=5.7#event-handler)
* [Property Binding System](/documentation/en-us/unreal-engine/scene-state-for-unreal-engine?application_version=5.7#property-binding-system)
* [Property References](/documentation/en-us/unreal-engine/scene-state-for-unreal-engine?application_version=5.7#property-references)
* [Property Functions](/documentation/en-us/unreal-engine/scene-state-for-unreal-engine?application_version=5.7#property-functions)
* [State Machine Parameters](/documentation/en-us/unreal-engine/scene-state-for-unreal-engine?application_version=5.7#state-machine-parameters)
* [Transition Parameters](/documentation/en-us/unreal-engine/scene-state-for-unreal-engine?application_version=5.7#transition-parameters)
