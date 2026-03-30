<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/calling-functions-on-variant-activation?application_version=5.7 -->

# Calling Functions on Variant Activation

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
5. [Working with Content](/documentation/en-us/unreal-engine/working-with-content-in-unreal-engine "Working with Content")
6. [Working with Scene Variants](/documentation/en-us/unreal-engine/working-with-scene-variants-in-unreal-engine "Working with Scene Variants")
7. Calling Functions on Variant Activation

# Calling Functions on Variant Activation

When you activate a Variant, call a function instead of changing a property value.

![Calling Functions on Variant Activation](https://dev.epicgames.com/community/api/documentation/image/009adaf1-789b-4480-a20f-feb86fbc785b?resizing_type=fill&width=1920&height=335)

 On this page

Whenever you bind an Actor to a Variant, the Variant Manager prompts you to choose the properties of that Actor that you want to change when the current Variant is switched on. However, in addition to or instead of changing a bound Actor's property values, you can also specify one or more functions that you want the Variant Manager to invoke on that Actor.

You can set up the Variant Manager to call any function that is already exposed by the Actor you've bound. You can also create your own new Blueprint function from scratch that accepts the bound Actor as an input. The steps on this page show how to do both.

## Steps

To call a Blueprint function when a Variant is activated:

1. Double-click your **Level Variant Sets** Asset in the **Content Browser** to open it in the Variant Manager UI.

   [![Open your Level Variant Sets Asset](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0397bf80-e527-466a-889d-505ef770709e/01-open-your-level-variant-sets-asset.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0397bf80-e527-466a-889d-505ef770709e/01-open-your-level-variant-sets-asset.png)

   Click image for full size.
2. Select the Variant you want to set up in the left-hand column of the Variant Manager UI.

   [![Select the Variant you want to change](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5f62c628-daee-407c-b72c-d62963dccb0e/02-select-the-variant-you-want-to-change.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5f62c628-daee-407c-b72c-d62963dccb0e/02-select-the-variant-you-want-to-change.png)

   Click image for full size.
3. If you haven't already bound the Actor whose function you want to call to the Variant, drag it from the **World Outliner** panel into the **Actors** column of the Variant Manager.

   [![Bind a new Actor, if needed](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/74216260-4f4a-4983-a8ba-e91e1da3ab5b/03-bind-a-new-actor.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/74216260-4f4a-4983-a8ba-e91e1da3ab5b/03-bind-a-new-actor.png)

   Click image for full size.

   When the Variant Manager prompts you to select which properties you want to capture, you can leave all the properties unchecked. Click **Select** to continue.
4. Right-click your Actor in the list of bound Actors on the Variant, and select **Add function caller** from the context menu.

   [![Add Function Caller](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/20c8581e-cf6e-4182-a04f-f3a84a2dcf0c/04-add-function-caller.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/20c8581e-cf6e-4182-a04f-f3a84a2dcf0c/04-add-function-caller.png)

   Click image for full size.
5. Find the new **Function caller** item at the bottom of the **Properties** column, and use the dropdown list in the **Values** column to choose the function you want to call.

   [![Select the function to call](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/68167f0b-7875-4b84-b47b-7217d55a88ec/05-select-the-function-to-call.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/68167f0b-7875-4b84-b47b-7217d55a88ec/05-select-the-function-to-call.png)

   Click image for full size.

   Choose **Create New Function** to create a totally new Blueprint function, or choose an existing function from the **Create Quick Binding** list if your Actor is already set up with the function you want to call.
6. The Variant Manager opens a special Blueprint class for you to edit, called the **LevelVariantSetDirector**. This Blueprint is owned by the Level Variant Sets Asset. Its role to store all logic that you need to run in respose to your Variants being activated.

   The Variant Manager automatically creates a new function for you in the **LevelVariantSetDirector** Blueprint. Whenever your Variant is activated, the Variant Manager automatically calls this function. If you need to further customize the Blueprint logic that gets triggered when the Variant is activated, you can do it in this graph.

   If you chose to create a new function in the previous step, you get a new empty function with a default name. You can fill out this function with any Blueprint logic you need to carry out.

   [![Result of creating a new function](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/81a8f352-8435-41b1-893d-84b5e6942739/06-result-of-creating-a-new-function.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/81a8f352-8435-41b1-893d-84b5e6942739/06-result-of-creating-a-new-function.png)

   Click image for full size.

   The Variant Manager passes your new function some information that you might find useful in creating your Blueprint graph:

   | Parameter | Description |
   | --- | --- |
   | **Target** | A reference to the bound Actor that you set up with the Function Caller in the previous step. |
   | **Level Variant Sets** | A reference to the Level Variant Sets Asset that this **LevelVariantSetDirector** Blueprint controls. You can use this to retrieve information about all the other Variants and Variant Sets that you've configured for the same Asset. |
   | **Variant Set** | A reference to the Variant Set that contains the current Variant: that is, the Variant that has just been activated. |
   | **Variant** | A reference to the Variant that has just been activated: that is, the Variant that contains the bound Actor that you set up with the Function Caller. |

   If you chose to create a quick binding to an existing function exposed by the Actor, the Variant Manager automatically adds a call to that function and hooks it up to the new function it creates in the **LevelVariantSetDirector** Blueprint. If the function being called on the Actor requires any other input values, such as the **New Actor Enable Collision** option in the image below, you can set them up in this graph.

   [![Set Actor Enable Collision Function](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d8f80693-a0a9-44ef-b62b-fcdc27675000/07-set-actor-enable-collision-function.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d8f80693-a0a9-44ef-b62b-fcdc27675000/07-set-actor-enable-collision-function.png)

   Click image for full size.

   [![Result of creating a quick binding](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7f39d91a-0c7e-491d-ba65-1fa3eef02ae0/08-result-of-creating-a-quick-binding.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7f39d91a-0c7e-491d-ba65-1fa3eef02ae0/08-result-of-creating-a-quick-binding.png)

   Click image for full size.

   By default, the Variant Manager only calls your function when the Variant is activated at runtime. If you want your function to also run when the Variant is switched on in the editor, select your function node in the **LevelVariantSetDirector** Blueprint and enable the **Call in Editor** setting in the **Details** panel.

   [![Call in Editor setting](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c26e757d-dcef-45fa-a02b-dbacc4a5d46b/09-call-in-editor-setting.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c26e757d-dcef-45fa-a02b-dbacc4a5d46b/09-call-in-editor-setting.png)

   Click image for full size.
7. When you are done setting up your new function or quick binding in the **LevelVariantSetDirector** Blueprint, **Compile** and **Save** the Blueprint. You can then close the Blueprint Editor and the Variant Manager window.

## End Result

Whenever you switch on the Variant that you set up with a function caller at runtime, the Variant Manager automatically invokes the function you defined in the **LevelVariantSetDirector** Blueprint.

If you've enabled the **Call in Editor** option for the function in the **LevelVariantSetDirector** Blueprint, the Variant Manager will also automatically invoke your function when you switch on that Variant in the Unreal Editor.

You can add multiple function callers to a single bound Actor if you need to call multiple functions on that Actor when a Variant is activated.

* [datasmith](https://dev.epicgames.com/community/search?query=datasmith)
* [enterprise](https://dev.epicgames.com/community/search?query=enterprise)
* [manufacturing](https://dev.epicgames.com/community/search?query=manufacturing)
* [variants](https://dev.epicgames.com/community/search?query=variants)
* [variant manager](https://dev.epicgames.com/community/search?query=variant%20manager)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/calling-functions-on-variant-activation?application_version=5.7#steps)
* [End Result](/documentation/en-us/unreal-engine/calling-functions-on-variant-activation?application_version=5.7#endresult)
