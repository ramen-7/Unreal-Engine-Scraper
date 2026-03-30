<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/construction-script-in-unreal-engine?application_version=5.7 -->

# Construction Script

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
7. Construction Script

# Construction Script

Executed when instances of a Blueprint are created to perform initialization actions.

![Construction Script](https://dev.epicgames.com/community/api/documentation/image/d0efdcfe-9d57-4f02-9a5d-3557ab9f831c?resizing_type=fill&width=1920&height=335)

 On this page

![User Construction Script](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/196a5ab2-6be8-4556-9445-835bd2dc6230/ucs_banner.png)


The **Construction Script** runs following the Components list when an instance of a Blueprint Class is created. It contains a node graph that is executed allowing the Blueprint Class instance to perform initialization operations. This can be extremely powerful as actions like performing traces into the world, setting meshes and materials, and so on can be used to achieve context-specific setup. For instance, a light Blueprint could determine what type of ground it is placed upon and choose the correct mesh to use from a set of meshes or a fence Blueprint could perform traces extending out in each direction to determine how long of a fence is needed to span the distance.



Only Blueprint Classes contain **Construction Scripts**. Level Blueprints do not have them.

The execution entry point into the **Construction Script** Graph is through a **ConstructionScript** node that is always present.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4f7e4008-2ee9-4fd6-aad8-16e6dfd742df/construction_script.png)

## Working with Graphs

See the [Blueprint Editor Graph Editor](/documentation/en-us/unreal-engine/graph-editor-for-the-blueprints-visual-scripting-editor-in-unreal-engine) for a detailed guide to working with the **ConstructionScript** and other Graphs within Blueprints.

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [graphs](https://dev.epicgames.com/community/search?query=graphs)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Working with Graphs](/documentation/en-us/unreal-engine/construction-script-in-unreal-engine?application_version=5.7#workingwithgraphs)
