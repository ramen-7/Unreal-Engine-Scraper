<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-switch-actor-within-scene-variants?application_version=5.7 -->

# Using the Switch Actor

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
7. Using the Switch Actor

# Using the Switch Actor

Use the Switch Actor to quickly toggle visibility between mutually exclusive child Actors.

![Using the Switch Actor](https://dev.epicgames.com/community/api/documentation/image/aaf4b757-76cb-4b5e-8fb7-9e93f185b9ac?resizing_type=fill&width=1920&height=335)

 On this page

The Switch Actor provides a quick way to toggle the visibility of Actors or entire hierarchies of Actors in your Level.

Only one child of the Switch Actor can be visible at any time. When you choose a child Actor that you want to be visible, the Switch Actor automatically hides all other child Actors, along with all their descendants. It then makes the one child Actor you chose visible, along with all of the descendants of that selected child Actor.

This behavior is most convenient when you have mutually exclusive Level Actors or hierarchies of Actors, where only one of those Actors or hierarchies should ever be visible at any given time. For example, a car configurator might offer several different trims, each of which is represented by a different set of Static Mesh Actors that have different geometry, as shown below:

[![Multiple mutually exclusive Actor hierarchies](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dd67e23e-b162-4001-a356-7b74656c1414/01-actor-hierarchies.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dd67e23e-b162-4001-a356-7b74656c1414/01-actor-hierarchies.png)

Click image for full size.

To switch the visible model of the car from one trim option to another would require showing and hiding multiple Actors. You could do this using Blueprint, the Variant Manager, or even manually in the Unreal Editor. However, changing visibility on dozens or potentially hundreds of different Actors at the same time can be cumbersome. If you use a Switch Actor as the parent for all the different trim options, you can easily switch between the different trims by setting a single option on the Switch Actor parent.

The Switch Actor is contained in the **Editor > Variant Manager Content** Plugin. This Plugin is typically enabled by default. However, if you don't see the Switch Actor in your **Modes** panel, you may need to enable this Plugin for your project.

## Adding the Switch Actor to a Level

The **Switch Actor** is listed in the **All Classes** tab of the **Place Actors** panel. Drag it from the **Place Actors** panel into your Level Viewport.

[![Add the Switch Actor to your Level](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d5a19ca9-8010-4335-8404-f579fb1c9f48/02-add-the-switch-actor-to-your-level.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d5a19ca9-8010-4335-8404-f579fb1c9f48/02-add-the-switch-actor-to-your-level.png)

Click image for full size.

## Selecting the Child Actor to Show

The following sections describe the different ways you can choose which child of the Switch Actor you want to show.

### In the Unreal Editor

Select the Switch Actor in your **World Outliner**. In the **Details** panel, find the **Switch Actor > Selected Option** setting. This dropdown lists the names of all the child Actors parented by your Switch Actor.

[![Selected Option setting](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/05f3d390-1b6c-447d-b071-bca5be7ea4ac/03-selected-option-setting.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/05f3d390-1b6c-447d-b071-bca5be7ea4ac/03-selected-option-setting.png)

Click image for full size.

Select the option that you want to be visible.

### In Blueprint

The Switch Actor offers a Blueprint API that you can use to work with its selected child. If you drag right from a reference to a Switch Actor in a Blueprint graph, you'll find these nodes listed under the **Switch Actor** category:

[![Switch Actor Blueprint API](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d43dd831-befa-4c56-af38-aab8bb1e0f3c/04-switch-actor-blueprint-api.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d43dd831-befa-4c56-af38-aab8bb1e0f3c/04-switch-actor-blueprint-api.png)

Click image for full size.

| Node | Name | Description |
| --- | --- | --- |
| Get Options | **Get Options** | Returns an array of references to all the child Actors currently parented by this Switch Actor. |
| Get Selected Option | **Get Selected Option** | Returns the index of the child Actor that is currently shown. |
| Select Option | **Select Option** | Changes the Switch Actor to select the child with the index you specify. |

The array returned by **Get Options** is not guaranteed to be in the same order as the child Actors that you see in the **World Outliner** or in the **Details** panel for the Switch Actor. In addition, the index number that is returned by **Get Selected Option** and that you specify when you call **Select Option** both identify elements within this array.

### In the Variant Manager

When you bind a Switch Actor to a Variant in the Variant Manager, capture its **Selected Option** property. The **Values** column shows a dropdown that lists the names of all the child Actors parented by your Switch Actor.

[![Selected Option in the Variant Manager](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c46f3d20-71b7-4d6b-b913-31c6ef8a6991/08-capturing-the-selected-option-in-the-variant-manager.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c46f3d20-71b7-4d6b-b913-31c6ef8a6991/08-capturing-the-selected-option-in-the-variant-manager.png)

Click image for full size.

Select the option that you want to be visible when this Variant is switched on.

* [enterprise](https://dev.epicgames.com/community/search?query=enterprise)
* [manufacturing](https://dev.epicgames.com/community/search?query=manufacturing)
* [variants](https://dev.epicgames.com/community/search?query=variants)
* [variant manager](https://dev.epicgames.com/community/search?query=variant%20manager)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Adding the Switch Actor to a Level](/documentation/en-us/unreal-engine/using-the-switch-actor-within-scene-variants?application_version=5.7#addingtheswitchactortoalevel)
* [Selecting the Child Actor to Show](/documentation/en-us/unreal-engine/using-the-switch-actor-within-scene-variants?application_version=5.7#selectingthechildactortoshow)
* [In the Unreal Editor](/documentation/en-us/unreal-engine/using-the-switch-actor-within-scene-variants?application_version=5.7#intheunrealeditor)
* [In Blueprint](/documentation/en-us/unreal-engine/using-the-switch-actor-within-scene-variants?application_version=5.7#inblueprint)
* [In the Variant Manager](/documentation/en-us/unreal-engine/using-the-switch-actor-within-scene-variants?application_version=5.7#inthevariantmanager)
