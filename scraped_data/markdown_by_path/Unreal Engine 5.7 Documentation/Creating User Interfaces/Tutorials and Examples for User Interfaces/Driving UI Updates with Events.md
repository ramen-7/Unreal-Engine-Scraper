<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/driving-ui-updates-with-events-in-unreal-engine?application_version=5.7 -->

# Driving UI Updates with Events

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
5. [Creating User Interfaces](/documentation/en-us/unreal-engine/creating-user-interfaces-with-umg-and-slate-in-unreal-engine "Creating User Interfaces")
6. [Tutorials and Examples for User Interfaces](/documentation/en-us/unreal-engine/tutorials-and-examples-for-user-interfaces-in-unreal-engine "Tutorials and Examples for User Interfaces")
7. Driving UI Updates with Events

# Driving UI Updates with Events

Learn how to optimize your UI elements by driving updates through the use of Events.

![Driving UI Updates with Events](https://dev.epicgames.com/community/api/documentation/image/cdc038e2-fbb8-4754-add8-356dd2622ff0?resizing_type=fill&width=1920&height=335)

 On this page

When crafting your UI elements, it's best practice to think of ways you can optimize your content to increase performance and minimize inefficiencies. For example, based on the scope of your project, [Property Binding](/documentation/en-us/unreal-engine/property-binding-for-umg-in-unreal-engine) may be fine for communicating information to your UI. However, if you have a more complex UI setup, or need to optimize your project, you may want to consider updating your UI on a need-to-know basis.

In this reference guide, we will examine three ways of communicating information to a HUD. While all three approaches accomplish the task, the third example presents the most cost effective way by moving the update process away from tick events, and instead manually updates information through the use of [Event Dispatchers](/documentation/en-us/unreal-engine/event-dispatchers-in-unreal-engine).

## Example 1. Function Binding

For this example, we will take a look at updating Health/Energy for a player using **Function Binding**.

Here we have a basic Health/Energy setup.

![Hierarchy structure of the HUD widget](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/223372f0-76b1-43ba-bb38-0e0d173f3571/ue5_1-01-hierarchy.png "Hierarchy structure of the HUD widget")

With display in place, we **Create Bindings** for our progress bars called **GetHealth** and **GetEnergy**. The function bindings cast to the Player Character Blueprint and assign the variables we defined for Health and Energy.

Below is the binding for GetHealth. For debugging purposes, we also added a **Print String** node to print to the screen the value of our Health variable.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c9aa43bb-38bf-4a1a-bbda-7aa47f50ee9a/ue5_1-02-get-health-bind-script.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c9aa43bb-38bf-4a1a-bbda-7aa47f50ee9a/ue5_1-02-get-health-bind-script.png)

Click image for full view.

In the image below, you can see the Health and Energy values from the player character that are passed through and reflected in the HUD. However, you can also see that even when we are not updating the Health Value, the blue debug text illustrates that we are still checking the Health Value every frame.

![Gameplay Example](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3f5d200d-f267-46f4-8076-84d97619b925/ue5_1-03-gameplay-example.png)

Essentially, this approach is asking "What is the player character blueprint? And when I know what it is, "give me the values for health and energy" each frame. For smaller, less complex systems, this approach works well; however, if you are using a more complex system with multiple properties checking for updates every frame, this setup can lead to poor performance.

## Example 2. Property Binding

The second approach is **Property Binding**, which is a bit more cost effective than Function Binding.

Using the same Health/Energy setup, let's examine how Property Bindings work.

![Hierarchy structure of the HUD widget](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c6d1b955-f9c6-424b-9dc6-0aac210d39ed/ue5_1-01-hierarchy.png "Hierarchy structure of the HUD widget")

In the **Event Graph** of our [Widget Blueprint](/documentation/en-us/unreal-engine/widget-blueprints-in-umg-for-unreal-engine), we use the **Event Construct** to get a reference to the Player Character Blueprint.

By using Event Construct, we are casting to the Character Blueprint once and storing the information as a reference so the script does not have to call that information every frame.

![BP script of the HUD Widget Blueprint](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f27e0414-f391-4b91-8f5c-c14612f945a8/ue5_1-04-hud-widget-bp-script-1.png "BP script of the HUD Widget Blueprint")

Then, we can bind the values for the progress bars directly to the variables inside the Character Blueprint.

![Set bind for percent value](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d9166ab9-7be8-47c4-8684-c6379c7d42f3/ue5_1-05-set-percent-bind.png "Set bind for percent value")

With this approach, we are no longer casting every frame and checking "what is the player character blueprint?" Instead, we are only querying the values for health and energy each frame.

Based on the scope of your project, this is approach can be efficient; however, if your system is more complex, then an Event Driven approach may be better.

## Example 3. Event Driven

Here we take a look at using Events to update the HUD only when it changes, and we will continue with the same Health/Energy setup.

![Hierarchy structure of the HUD widget](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e8e30643-e600-4819-b46e-5ebbc0b9a067/ue5_1-01-hierarchy.png "Hierarchy structure of the HUD widget")

Inside the Character Blueprint, add an **Event Dispatcher** node to the end of the script that decrements our Health. In this example, the Event Dispatcher node is **Call Update Health**.

For testing purposes, Health is set to decrease whenever the **F** key is pressed.

![BP Script for causing damage of the Character](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c900d09c-b450-436d-b0db-98f3c50ae7f6/ue5_1-06-set-causing-damage.png "BP Script for causing damage of the Character")

Now, whenever we decrease our Health, we also call this Event Dispatcher. In the Event Graph of the HUD Widget Blueprint, we can use the Event Construct again to get and store a reference to the Player Character Blueprint. We can also Bind a Custom Event to the Event Dispatcher inside that Character Blueprint so that the Custom Event is called when the Event Dispatcher is called.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f4913d8f-6a18-4724-94cd-6190594469ec/ue5_1-07-hud-widget-bp-script-2.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f4913d8f-6a18-4724-94cd-6190594469ec/ue5_1-07-hud-widget-bp-script-2.png)

Click image for full view.

The Custom Event inside the HUD Widget Blueprint now only checks and updates the display of player's Health when it changes, rather than always checking the value regardless of whether or not it changed.

The image below shows how you can incorporate Health and Energy into the same Event Construct script.

The Custom Events **UpdateHealth** and **UpdateEnergy** are bound to Event Dispatchers from the Character Blueprint, which are only called when the character's Health/Energy value changes. We can also initialize the display by calling those two Custom Events when the HUD is constructed following the binding process.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9c754eb0-9c3f-41c1-bdbb-3525ef758d95/ue5_1-08-hud-widget-bp-script-3.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9c754eb0-9c3f-41c1-bdbb-3525ef758d95/ue5_1-08-hud-widget-bp-script-3.png)

Click image for full view.

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [blueprint](https://dev.epicgames.com/community/search?query=blueprint)
* [umg ui designer](https://dev.epicgames.com/community/search?query=umg%20ui%20designer)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Example 1. Function Binding](/documentation/en-us/unreal-engine/driving-ui-updates-with-events-in-unreal-engine?application_version=5.7#example1functionbinding)
* [Example 2. Property Binding](/documentation/en-us/unreal-engine/driving-ui-updates-with-events-in-unreal-engine?application_version=5.7#example2propertybinding)
* [Example 3. Event Driven](/documentation/en-us/unreal-engine/driving-ui-updates-with-events-in-unreal-engine?application_version=5.7#example3eventdriven)

Related documents

[Blueprints Visual Scripting

![Blueprints Visual Scripting](https://dev.epicgames.com/community/api/documentation/image/4e3f56de-8371-4c9d-aa32-4bafe6592648?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine)
