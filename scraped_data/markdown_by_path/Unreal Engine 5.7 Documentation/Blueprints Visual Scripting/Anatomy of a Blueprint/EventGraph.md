<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/event-graph-in-unreal-engine?application_version=5.7 -->

# EventGraph

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
6. [Anatomy of a Blueprint](/documentation/en-us/unreal-engine/anatomy-of-a-blueprint-in-unreal-engine "Anatomy of a Blueprint")
7. EventGraph

# EventGraph

Uses events and function calls to perform actions in response to Blueprint events.

![EventGraph](https://dev.epicgames.com/community/api/documentation/image/483c2450-cf74-4e87-bd02-ad62ad39f8d8?resizing_type=fill&width=1920&height=335)

 On this page

![Graph Panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/39ae3438-0598-475e-8591-c013f977365a/k2_graphview.png)


The **EventGraph** of a Blueprint contains a node graph that uses events and function calls to perform actions in response to gameplay events associated with the Blueprint. This is used to add functionality that is common to all instances of a Blueprint. This is where interactivity and dynamic responses are setup. For example, a light Blueprint could respond to a damage event by turning off its `LightComponent` and changing the material used by its mesh. This would automatically provide this behavior to all instances of the light Blueprint.

The **EventGraph** of a Level Blueprint contains a node graph that uses events and function calls to perform actions in response
to gameplay events. This is used to handle events for the level as a whole and to add functionality for specific instances of
Actors and Blueprints within the world.

In either case, an **EventGraph** is used by adding one or more events to act as entry points and then connecting Function
Calls, Flow Control nodes, and Variables to perform the desired actions.

## Working with Graphs

The **Graph** tab displays the visual representation of a particular graph of nodes as it shows all of the nodes contained in the graph as well as the connections between them. It provides editing capabilities for adding and removing nodes, arranging nodes, and creating links between nodes. Breakpoints can also be set in the **Graph** tab to aid in debugging Blueprints.

See the [Blueprint Editor Graph Editor](/documentation/en-us/unreal-engine/graph-editor-for-the-blueprints-visual-scripting-editor-in-unreal-engine) for a detailed guide to working with the **EventGraph** and other **Graphs** with Blueprints.

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [blueprint](https://dev.epicgames.com/community/search?query=blueprint)
* [graphs](https://dev.epicgames.com/community/search?query=graphs)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Working with Graphs](/documentation/en-us/unreal-engine/event-graph-in-unreal-engine?application_version=5.7#workingwithgraphs)
