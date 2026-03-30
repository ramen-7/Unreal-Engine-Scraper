<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/ndisplay-actor-replication-in-unreal-engine?application_version=5.7 -->

# nDisplay Actor Replication

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
5. [Working with Media](/documentation/en-us/unreal-engine/working-with-media-in-unreal-engine "Working with Media")
6. [Integrating Media](/documentation/en-us/unreal-engine/integrating-media-in-unreal-engine "Integrating Media")
7. [Rendering to Multiple Displays with nDisplay](/documentation/en-us/unreal-engine/rendering-to-multiple-displays-with-ndisplay-in-unreal-engine "Rendering to Multiple Displays with nDisplay")
8. nDisplay Actor Replication

# nDisplay Actor Replication

An overview of how to control Actor replication across your nDisplay cluster.

![nDisplay Actor Replication](https://dev.epicgames.com/community/api/documentation/image/30dd2e3f-f9fc-4e2f-92dd-e4b447667e68?resizing_type=fill&width=1920&height=335)

 On this page

All inputs to the nDisplay system are handled only by the primary node. Without any replication, only the primary node would see changes in the scene. Therefore, the primary node needs to be able to replicate changes to all other parts of the nDisplay network.

To accomplish this, nDisplay offers two different kinds of Components that you can attach to your Actors:

* The **DisplayClusterSceneComponentSyncParent** Component tracks changes in the 3D transforms of its parent Component, and pushes those changes to the other cluster nodes in the network.  
  The default DisplayClusterPawn used by the nDisplay system uses this Component.
* The **DisplayClusterSceneComponentSyncParent** Component tracks changes to the 3D transforms of its child components, and pushes those changes to the other cluster nodes in the network.

For example, in the Actor shown below, the **DisplayClusterSceneComponentSyncParent\_Scene** Component tracks and replicates changes to the 3D transforms of its parent Actor as the Actor moves around the Level. The **DisplayClusterSceneComponentSyncThis** Component tracks and synchronizes movements of its child Static Mesh component as it moves relative to the scene graph root.

![DisplayClusterSceneComponentSyncParent](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/aadbf4a5-30d0-46b9-a138-fbeff8699a8a/01-bp-actor-sync_ue5.png "DisplayClusterSceneComponentSyncParent")

If you have other Actors in your scene that can be affected during gameplay, you must use one of these two Components to replicate those changes to all nodes. To do this:

1. Select the Actor you need to replicate in the Level viewport or the **World Outliner** panel.
2. In the **Details** panel, click **+ Add Component**. Search for either **DisplayClusterSceneComponentSyncParent** or **DisplayClusterSceneComponentSyncThis**, and select it from the list.

   ![Add an nDisplay sync Component](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8e5cf88a-5105-497e-9a65-200574a5f706/02-add-display-sync-parent_ue5.png "Add an nDisplay sync Component")

These components do not carry out a full replication. Only the transforms of the parent Actor or of child Components are sent to the cluster.

## Replicating Custom Data

If you need to replicate other custom data between your primary node and the rest of your cluster, you can write your own C++ class that implements the `IDisplayClusterClusterSyncObject` interface. nDisplay will automatically invoke the methods in this interface to check whether each instance of this class needs to be synchronized from the primary node to the other cluster nodes.

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [vfx](https://dev.epicgames.com/community/search?query=vfx)
* [graphics](https://dev.epicgames.com/community/search?query=graphics)
* [guide](https://dev.epicgames.com/community/search?query=guide)
* [ndisplay](https://dev.epicgames.com/community/search?query=ndisplay)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Replicating Custom Data](/documentation/en-us/unreal-engine/ndisplay-actor-replication-in-unreal-engine?application_version=5.7#replicatingcustomdata)
