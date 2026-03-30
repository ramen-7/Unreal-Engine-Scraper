<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-levels-of-detail-in-mutable-in-unreal-engine?application_version=5.7 -->

# Using Levels of Detail

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
6. [Mutable Skeletal Mesh Generation](/documentation/en-us/unreal-engine/mutable-skeletal-mesh-generation-in-unreal-engine "Mutable Skeletal Mesh Generation")
7. [Mutable Optimizing and Debugging](/documentation/en-us/unreal-engine/mutable-optimizing-and-debugging-in-unreal-engine "Mutable Optimizing and Debugging")
8. Using Levels of Detail

# Using Levels of Detail

An overview of the Levels of Detail (LOD) tools in Mutable.

![Using Levels of Detail](https://dev.epicgames.com/community/api/documentation/image/a85677bf-62c9-41db-9913-a916634d310d?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

There are many reasons to use Levels of Detail (LODs) in Mutable:

* Memory usage
* Processor performance
* Loading time

In Mutable you can take advantage of the procedural construction of characters to optimize even further by creating specific diagrams for each LOD. In this way, you can have objects such as the base character body follow the usual LOD optimization by simply lowering the polycount and texture sizes on each LOD. You can also go beyond this and define different construction processes for each LOD using cheaper operations as the object is further away.

As an example, imagine a character bracelet. In the top LOD used during close-ups, the bracelet has its own mesh and complex materials with physics animation. For the second LOD, the bracelet may be simplified by replacing it with a rigid mesh with a single material directly skinned to the arm bone. The third LOD may be just a texture patch on the arm (if the bracelet is big enough). In the fourth LOD it may disappear completely. You can define all these cases in different diagrams using the same parameters, so if the bracelet color was customizable, you could see it change on every LOD.

## Defining the Levels of Detail of a Component

You can define the LODs using several different nodes in the graph. The most important node is the [Mesh Component](https://github.com/anticto/Mutable-Documentation/wiki/Node-Mesh-Component) node. The number of LODs defined in this node limits the maximum LODs that can be defined in the component.

For example, the [Add To Mesh Component](https://github.com/anticto/Mutable-Documentation/wiki/Node-Add-To-Mesh-Component) node only generate as many LODs as its parent [Mesh Component](https://github.com/anticto/Mutable-Documentation/wiki/Node-Mesh-Component) node. If an LOD pin has no connections, the LOD will not have geometry unless automatic LODs are used.

LOD properties that control how LODs are selected are standard Unreal Engine properties. They are copied from the Reference SkeletalMesh object and you can set them up there. Please note that this means that the Reference SkeletalMesh object must have LODs.

You can also find more LOD settings in the **Object Properties** tab.

## Automatic Levels of Detail

Since customizable objects may become very large, you can use the Auto LOD Strategy field in the Mesh Component node to simplify the generation of LODs without having to multiply all the nodes. See the [Mesh Component](https://github.com/anticto/Mutable-Documentation/wiki/Node-Mesh-Component) node reference for more information.

* [landscape](https://dev.epicgames.com/community/search?query=landscape)
* [beta](https://dev.epicgames.com/community/search?query=beta)
* [working with content](https://dev.epicgames.com/community/search?query=working%20with%20content)
* [skeletal mesh](https://dev.epicgames.com/community/search?query=skeletal%20mesh)
* [mutable](https://dev.epicgames.com/community/search?query=mutable)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Defining the Levels of Detail of a Component](/documentation/en-us/unreal-engine/using-levels-of-detail-in-mutable-in-unreal-engine?application_version=5.7#definingthelevelsofdetailofacomponent)
* [Automatic Levels of Detail](/documentation/en-us/unreal-engine/using-levels-of-detail-in-mutable-in-unreal-engine?application_version=5.7#automaticlevelsofdetail)
