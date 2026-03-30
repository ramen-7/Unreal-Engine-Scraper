<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/event-dispatchers-in-unreal-engine?application_version=5.7 -->

# Event Dispatchers

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
5. [Blueprints Visual Scripting](/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine "Blueprints Visual Scripting")
6. [Specialized Blueprint Node Groups](/documentation/en-us/unreal-engine/specialized-blueprint-visual-scripting-node-groups-in-unreal-engine "Specialized Blueprint Node Groups")
7. Event Dispatchers

# Event Dispatchers

Allows a Blueprint Class to report on its state to the Level Blueprint.

![Event Dispatchers](https://dev.epicgames.com/community/api/documentation/image/947727cf-ea77-4344-904e-fd168deb1622?resizing_type=fill&width=1920&height=335)

 On this page

An example on [Event Dispatchers](/documentation/en-us/unreal-engine/event-dispatchers-and-delegates-quick-start-guide-in-unreal-engine) from the [Blueprint Actor Communication](/documentation/en-us/unreal-engine/actor-communication-in-unreal-engine) page demonstrates both languages of Blueprint and C++ in a feature-oriented way. This page should be considered a supplemental helper for Blueprint Scripting.



By binding one or more events to an **Event Dispatcher**, you can cause all of those events to fire once the Event Dispatcher is called. These events can be bound within a Blueprint Class, but Event Dispatchers also allow events to be fired within the Level Blueprint.

## Creating Event Dispatchers

Event Dispatchers are created in the Blueprint Editor's [Blueprint Editor My Blueprint Panel](/documentation/en-us/unreal-engine/my-blueprint-panel-in-the-blueprints-visual-scripting-editor-for-unreal-engine) tab.

To create a new Event Dispatcher:

1. In the **My Blueprint** panel click ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/185a937c-313e-427a-b527-c87bab9f9ac8/plus_button.png) on the Event Dispatcher category: ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d6876519-ca7d-4307-87ea-f3b718ad3b95/myblueprint_eventdispatcher.png).
2. Enter a name for the Event Dispatcher in the name field that appears at the end of the list in the **My Blueprint** tab.

   ![](name_event_Dispatcher.png)

### Setting Properties

By selecting the Event Dispatcher in the **My Blueprint** panel, you can edit its properties in the **Details** panel. You can set the tooltip and category for your Event Dispatcher, as well as add inputs.

Adding inputs to your Event Dispatcher allows you to send variables to each event bound to your Event Dispatcher. This allows data flow not only within your Blueprint Class, but also between your Blueprint Class
and the Level Blueprint.

The process to add inputs to your Event Dispatcher is similar to the workflow for adding inputs and outputs to functions, custom events, and macros. If you would like to use the same inputs as another event, you can use the **Copy Signature from** dropdown to indicate the event.
To add your own inputs to the Event Dispatcher:

1. Click **New** in the **Inputs** section of the **Details** pane.

   ![](new_input_Dispatcher.png)
2. Name the new input and set its type using the dropdown menu. In this example, there is a String input parameter named **MyStringParam**.

   ![](named_new_Dispatcher.png)
3. You can also set a default value and indicate whether or not to pass the parameter by reference by expanding the entry for the parameter.

   ![](expanded_input_Dispatcher.png)


   To change the location of the pin for this parameter on the edge of the node, use the up and down arrows in the expanded **Details** pane entry.

## Using Event Dispatchers

After creating the Event Dispatcher, you can add event nodes, bind nodes, and unbind nodes linked to it. Although you can double-click on the Event Dispatcher entry in the **My Blueprint** tab to
open the Event Dispatcher's graph, the graph is locked and you cannot modify the Event Dispatcher directly. The bind, unbind, and assign methods enable you to add events to the Event Dispatcher's
event list, while the call method activates all the events stored in the event list.

Event, bind, and unbind nodes can be added in both the Blueprint Class and the Level Blueprint. Except for the Event node, each node has a **Target** input pin:

* In the Blueprint Class, this pin is automatically set to **Self**. This means that the event list is changed for the class, so every instance of the class will be changed.
* In the Level Blueprint, this pin must be connected to a reference to an instance of the class in the level. This means that the event list will only be changed for that particular instance of the class.
  The [Level Blueprint documentation](/documentation/en-us/unreal-engine/level-blueprint-in-unreal-engine#referencingactors) explains how to create any **Actor** references you might need.

[![Binding and Unbinding Events](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/19d5fc66-2661-4493-9fde-231ba2dbd9a4/placeholder_topic.png)

Binding and Unbinding Events

Adding and removing events from an Event Dispatcher's events list.](/documentation/en-us/unreal-engine/binding-and-unbinding-events-in-unreal-engine)
[![Calling Event Dispatchers](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c0628ec4-8bc1-4090-aa09-2a5e57a905ec/placeholder_topic.png)

Calling Event Dispatchers

Calling the Event Dispatcher executes all of the currently bound events in the events list.](/documentation/en-us/unreal-engine/calling-event-dispatchers-in-unreal-engine)
[![Creating Dispatcher Events](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/eb60d6d8-230a-4c22-b126-95a559d4523e/create_eventdispatcher_topic.png)

Creating Dispatcher Events

Creating events that can be bound and added to the Event Dispatcher's events list.](/documentation/en-us/unreal-engine/creating-dispatcher-events-in-unreal-engine)

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [blueprint](https://dev.epicgames.com/community/search?query=blueprint)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Creating Event Dispatchers](/documentation/en-us/unreal-engine/event-dispatchers-in-unreal-engine?application_version=5.7#creatingeventdispatchers)
* [Setting Properties](/documentation/en-us/unreal-engine/event-dispatchers-in-unreal-engine?application_version=5.7#settingproperties)
* [Using Event Dispatchers](/documentation/en-us/unreal-engine/event-dispatchers-in-unreal-engine?application_version=5.7#usingeventdispatchers)
