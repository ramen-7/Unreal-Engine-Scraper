<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/dataprep-selection-transform-reference-in-unreal-engine?application_version=5.7 -->

# Dataprep Selection Transform Reference

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
6. [Datasmith](/documentation/en-us/unreal-engine/datasmith-plugins-for-unreal-engine "Datasmith")
7. [Dataprep Import Customization](/documentation/en-us/unreal-engine/dataprep-import-customization-in-unreal-engine "Dataprep Import Customization")
8. Dataprep Selection Transform Reference

# Dataprep Selection Transform Reference

Details on ways you can transform the list of objects you want to modify in the Dataprep system.

![Dataprep Selection Transform Reference](https://dev.epicgames.com/community/api/documentation/image/8be1b072-9973-4ebf-bb13-19df3bfa4ce7?resizing_type=fill&width=1920&height=335)

 On this page

This page describes each of the **Transform** blocks that you can use in the Visual Dataprep system to change the objects selected for an Action.

Each type of **Transform** block encapsulates a specific type of modification that the Unreal Editor can make to the selection of Assets and Actors passed to it. The block then passes the modified selection on to the next block below it within the same Dataprep Action.

Transform blocks are like filters, in that they determine the set of Actors and Assets that other Dataprep blocks in the same Action will operate on. However, a filter block can only cut down the list of objects passed down to it. A **Transform** block, on the other hand, can *add* objects to the current selection.

## Common Controls

All **Transform** blocks offer the **Output Can Include Input** setting.

* When this setting is enabled, the **Transform** block always adds the Actors and Assets passed in to the block to the output selection that it passes on to the next block in the Dataprep Action.
* When this setting is disabled, the **Transform** block *only* adds the Actors and Assets passed in to the block to the output selection *if* those Actors and Assets also pass the other selection criteria built in to the block.

## Reference Selection Transform

This operation checks each Actor and Asset in the input list looking for references to other Assets in the temporary world. It then adds each referenced Static Mesh, Material, and Texture Asset that it finds to the output selection that it passes on to the next block.

![Reference Selection Transform](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/125d117e-a3dc-45d6-a0f6-9e4733ffcf8b/reference-selection-transform.png "Reference Selection Transform")

## Select Hierarchy

For each Actor passed in to this block, this transform looks for other Actors that are children of that input Actor. It then adds all of those child Actors to the output selection that it passes on to the next block.

![Select Hierarchy](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fbbfe045-a985-4b25-953e-b32900f5b23c/select-hierarchy.png "Select Hierarchy")

| Setting | Description |
| --- | --- |
| **Select** | Determines how deeply the selection extends into the descendants of each input Actor.   * Use **Immediate Children** to have the output selection contain only Actors that are direct children of the Actors passed in to the transform block. * Use **All Descendants** to have the output selection recurse to include the complete hierarchies under the Actors passed in to the transform block. |

## Select Actor Components

For each Actor passed into this block, this transform looks for all Components of previously selected Actors. It then adds those Components to the output selection that it passes on to the next block.

![Select Actor Components](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f5e16709-46e7-4c4f-a254-72b4cb11e35a/select-actor-components.png "Select Actor Components")

## Select Owning Actor

This transform looks for the parent Actor of each Component passed in to this block. It then adds the parent Actor to the output selection that it passes on to the next block.

![Select Owning Actor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/87d95764-8225-4bdd-b0a7-5778d3c38ac7/select-owning-actor.png "Select Owning Actor")

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [datasmith](https://dev.epicgames.com/community/search?query=datasmith)
* [enterprise](https://dev.epicgames.com/community/search?query=enterprise)
* [manufacturing](https://dev.epicgames.com/community/search?query=manufacturing)
* [dataprep](https://dev.epicgames.com/community/search?query=dataprep)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Common Controls](/documentation/en-us/unreal-engine/dataprep-selection-transform-reference-in-unreal-engine?application_version=5.7#commoncontrols)
* [Reference Selection Transform](/documentation/en-us/unreal-engine/dataprep-selection-transform-reference-in-unreal-engine?application_version=5.7#referenceselectiontransform)
* [Select Hierarchy](/documentation/en-us/unreal-engine/dataprep-selection-transform-reference-in-unreal-engine?application_version=5.7#selecthierarchy)
* [Select Actor Components](/documentation/en-us/unreal-engine/dataprep-selection-transform-reference-in-unreal-engine?application_version=5.7#selectactorcomponents)
* [Select Owning Actor](/documentation/en-us/unreal-engine/dataprep-selection-transform-reference-in-unreal-engine?application_version=5.7#selectowningactor)
