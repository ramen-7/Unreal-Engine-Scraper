<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/calling-event-dispatchers-in-unreal-engine?application_version=5.7 -->

# Calling Event Dispatchers

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
7. [Event Dispatchers](/documentation/en-us/unreal-engine/event-dispatchers-in-unreal-engine "Event Dispatchers")
8. Calling Event Dispatchers

# Calling Event Dispatchers

Calling the Event Dispatcher executes all of the currently bound events in the events list.

![Calling Event Dispatchers](https://dev.epicgames.com/community/api/documentation/image/6b12fb50-82d1-4855-a5b5-da912e5322ab?resizing_type=fill&width=1920&height=335)

 On this page

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5e622ac7-36e9-42c9-97b3-d85493c9c53b/event_dispatcher_call_node.png)


Calling an Event Dispatcher with a **Call** node causes all of the events bound to the Event Dispatcher to fire. You can have more than one **Call** node for each Event Dispatcher, and you can also
call the Event Dispatcher in both Blueprint Classes and Level Blueprints.

## Calling in Blueprint Classes

1. Drag off of the Event Dispatcher's name in the **My Blueprint** tab, and drop into the graph you are working in.
2. Select **Call** in the menu that appears.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/900da6dc-7cf4-4486-ad99-b2689350cd90/dispatcher_call_menu.png)

**Alternatively:**

1. **Right-click** in the graph.
2. Expand **Event Dispatcher** in the context menu that appears.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1ac35c2e-a6d2-4489-82a8-fce9363957cd/event_dispatcher_context.png)
3. Select **Call [EventDispatcherName]** under **Event Dispatcher**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/42ddd18c-238f-4e28-9ae3-ef9d2c774abf/event_dispatcher_context_name.png)

## Calling in Level Blueprints

1. [Add a reference](/documentation/en-us/unreal-engine/level-blueprint-in-unreal-engine#referencingactors) to the Actor in your level you would like to call the Event Dispatcher for.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/650738cb-fef5-4cb1-b728-70006287d461/target_step1.png)
2. Drag off of the output pin of the reference node and release to show the context menu.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/24e85d48-137e-4ee0-b2d1-7e5909792a81/empty_context_menu.png)
3. Navigate to **Event Dispatcher > Call [EventDispatcherName]** in the context menu. Searching for "Event Call" should quickly bring up the correct entry.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e915a778-b13b-43d2-ba7b-966dcff3776e/call_node_level.png)

   The **Call** node will appear, with the Actor reference already wired to the **Target** pin.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6b547732-9883-460e-a41b-919cada5c0f0/call_dispatcher_wired_level.png)

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Calling in Blueprint Classes](/documentation/en-us/unreal-engine/calling-event-dispatchers-in-unreal-engine?application_version=5.7#callinginblueprintclasses)
* [Calling in Level Blueprints](/documentation/en-us/unreal-engine/calling-event-dispatchers-in-unreal-engine?application_version=5.7#callinginlevelblueprints)
