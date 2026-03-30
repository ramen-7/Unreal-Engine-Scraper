<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/graphs-in-unreal-engine?application_version=5.7 -->

# Graphs

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
7. Graphs

# Graphs

Node graph that uses events and function calls to perform actions in response to events associated with the Blueprint.

![Graphs](https://dev.epicgames.com/community/api/documentation/image/391068ed-321d-4ce1-a434-b0cc9fec0cbc?resizing_type=fill&width=1920&height=335)

 On this page

A **Graph** is a network of nodes that can be connected to one another in order to define the flow of execution for the network. Graphs are the basis for implementing functionality in Blueprints.
Each Blueprint can contain one or more graphs, depending on the type of Blueprint, that define the implementation of a particular aspect of the Blueprint. Each graph within a Blueprint can also
contain sub-graphs, which are essentially collections of nodes collapsed into their own separate graph, mainly for organizational purposes. There are specialized types of Graphs that have unique
properties, but the key principles of adding variable references, adding and connecting Nodes, and debugging will apply throughout.

## Graph Types

### Event Graphs

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/55127ee4-b164-4700-92c2-23ef3701f1fe/eventgraph.png)

**Event Graphs** are the most general type of Blueprint graph. Each new Blueprint Class will contain one Event Graph when it is created, although more can be added. These additional Event Graphs can
help to organize your Blueprint networks. Event Graphs generally contain the networks for the gameplay behavior of the Blueprint, with [Events](/documentation/en-us/unreal-engine/events-in-unreal-engine),
[CustomEvents](/documentation/en-us/unreal-engine/custom-events-in-unreal-engine), and **Input** nodes serving to initiate the flow of execution through the Event Graph.

For more information about this section, see the [Event Graph](/documentation/en-us/unreal-engine/event-graph-in-unreal-engine) documentation.

### Construction Script

![Construction Script](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2f7e5376-e75f-4fd5-8926-1bdfccc4576f/constructionscript.png)

**Construction Scripts** are unique to Blueprint Classes, with only one ConstructionScript graph present in each Blueprint Class. Construction Scripts are useful for Blueprint Class initialization,
as they run right after the **Components** list is set up for the Blueprint Class.

For more information about this section, see the [Construction Script](/documentation/en-us/unreal-engine/construction-script-in-unreal-engine) documentation.

### Functions

![Functions](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6846c06f-261f-4ad7-b30f-499cb006bee9/functions.png)

**Functions** are node graphs belonging to a particular **Blueprint** that can be executed, or called, from another
graph within the Blueprint. Functions have a single entry point designated by a node with the name of the Function
containing a single exec output pin. When the Function is called from another graph, the output exec pin is activated
causing the connected network to execute.

For more information about this section, see the [Functions](/documentation/en-us/unreal-engine/functions-in-unreal-engine) documentation.

### Macros

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5aed6d11-31b4-466c-a034-f28b25df6168/macro.png)

**Blueprint Macros**, or **Macros**, are essentially the same as collapsed graphs of nodes. They have an entry point and exit point designated by
tunnel nodes. Each tunnel can have any number of execution or data pins which are visible on the macro node when used in other
Blueprints and graphs.

For more information about this section, see the [Macros](/documentation/en-us/unreal-engine/macros-in-unreal-engine) documentation.

## Working with Graphs

Whether your Graph is a Construction Script, EventGraph, Function, or Macro, you will edit it in the [Graph](/documentation/en-us/unreal-engine/blueprints-visual-scripting-user-interface-for-blueprint-classes-in-unreal-engine) mode of the [Editor](/documentation/en-us/unreal-engine/user-interface-reference-for-the-blueprints-visual-scripting-editor-in-unreal-engine). Fundamentally,
all Graphs contain networks of Nodes connected by Wires.

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [graphs](https://dev.epicgames.com/community/search?query=graphs)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Graph Types](/documentation/en-us/unreal-engine/graphs-in-unreal-engine?application_version=5.7#graphtypes)
* [Event Graphs](/documentation/en-us/unreal-engine/graphs-in-unreal-engine?application_version=5.7#eventgraphs)
* [Construction Script](/documentation/en-us/unreal-engine/graphs-in-unreal-engine?application_version=5.7#constructionscript)
* [Functions](/documentation/en-us/unreal-engine/graphs-in-unreal-engine?application_version=5.7#functions)
* [Macros](/documentation/en-us/unreal-engine/graphs-in-unreal-engine?application_version=5.7#macros)
* [Working with Graphs](/documentation/en-us/unreal-engine/graphs-in-unreal-engine?application_version=5.7#workingwithgraphs)
