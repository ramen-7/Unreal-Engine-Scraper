<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/edit-tools-user-guide-in-unreal-engine?application_version=5.7 -->

# Edit Tools User Guide

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
5. [Gameplay Systems](/documentation/en-us/unreal-engine/gameplay-systems-in-unreal-engine "Gameplay Systems")
6. [Physics](/documentation/en-us/unreal-engine/physics-in-unreal-engine "Physics")
7. [Chaos Destruction](/documentation/en-us/unreal-engine/chaos-destruction-in-unreal-engine "Chaos Destruction")
8. [Chaos Destruction Key Concepts](/documentation/en-us/unreal-engine/chaos-destruction-key-concepts-in-unreal-engine "Chaos Destruction Key Concepts")
9. Edit Tools User Guide

# Edit Tools User Guide

Overview of the Edit Panel included with the Fracture Mode.

![Edit Tools User Guide](https://dev.epicgames.com/community/api/documentation/image/2e33008a-a63f-42f8-b184-dbd9e8cd56e5?resizing_type=fill&width=1920&height=335)

 On this page

You can find similar information in video format in the Epic Developer Community site by watching the [Fracture and Clustering](https://dev.epicgames.com/community/learning/tutorials/k84m/chaos-destruction-fracture-and-clustering) tutorials.

The **Fracture Mode** comes with editing tools that provide the ability to remove unwanted bones (fractured pieces) from the Geometry Collection hierarchy, as well as hide and unhide specific bones. These tools present a workflow improvement when working with complex fracturing of Geometry Collections.

In this guide you will learn how to use the available tools in the **Edit** panel.

Before learning about the Edit Tools, you should know how to create Geometry Collections and fracture them. If you are not familiar with the process, refer to the [Geometry Collections User Guide](/documentation/en-us/unreal-engine/chaos-destruction-key-concepts-in-unreal-engine) and the [Fracturing User Guide](/documentation/en-us/unreal-engine/fracturing-geometry-collections-user-guide).

## Fracture a Geometry Collection

In this section, you will create and fracture a Geometry Collection so you can learn about the Edit tools included with the **Fracture Mode**.

1. Create a Geometry Collection from a Static Mesh Actor in your Level.

   ![Create a Geometry Collection from a Static Mesh Actor in your Level](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d7223aa0-3341-461c-8190-b01fa1aef667/destruction-cluster-6.png)
2. Fracture the Geometry Collection by using one of the available methods included. In the example below, we used the **Slice** tool to fracture the Geometry Collection into 8 pieces.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/288d1a83-e1ed-4b30-a133-ddb3f61c412b/destruction-cluster-7.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/288d1a83-e1ed-4b30-a133-ddb3f61c412b/destruction-cluster-7.png)

   Click the image for full size.

## Use the Edit Tools

### The Prune tool

The **Prune** tool is used to remove any selected bones (fractured pieces) from the fracture hierarchy.

Select one or more bones in the viewport or the hierarchy.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/227a6d41-20a5-4139-849d-7deafce9af25/destruction-edit-1.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/227a6d41-20a5-4139-849d-7deafce9af25/destruction-edit-1.png)

Click the image for full size.

Click **Prune** to remove selected bones.

![Click Prune to remove the selected bones](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/66da74df-a27a-4f4d-af04-5d837942fb9f/destruction-edit-2.png)

This tool is commonly used to remove intersecting geometry or unwanted Bones after fracturing the Geometry Collection.

![The selected bone has been removed](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c039df25-5754-41b2-a469-e5d0ccbd3bc2/destruction-edit-3.png)

## The Visibility tools

The **Visibility** tools are used to temporarily hide selected bones from the viewport. This can be useful when trying to focus on a specific set of Bones in the hierarchy.

Click **Hide** in the **Edit** category to hide all selected Bones.

![Click Hide in the Edit category to hide all selected Bones](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d9c22d7d-d663-49ad-afd0-00ce7a9fd41a/destruction-edit-7.png)


![Showing all bones](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/48437433-a85b-4e57-92e6-304721b6766c/destruction-edit-4a.png)

![Hiding the selected bones](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ffe63ad3-e531-4ed7-8076-f4f28afe35d1/destruction-edit-4b.png)

Showing all bones

Hiding the selected bones

To show the hidden Bones, select them in the **Fracture Hierarchy** and click **Unhide**.

![Select the Bones in the Fracture Hierarchy](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/98caec67-9ea3-4972-97e2-6a340f61c8cc/destruction-edit-5.png)
![Click Unhide to show the Bones in the viewport](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e7f294b4-3e54-4116-9c9f-375b5a78e614/destruction-edit-6.png)

* [physics](https://dev.epicgames.com/community/search?query=physics)
* [chaos](https://dev.epicgames.com/community/search?query=chaos)
* [destruction](https://dev.epicgames.com/community/search?query=destruction)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Fracture a Geometry Collection](/documentation/en-us/unreal-engine/edit-tools-user-guide-in-unreal-engine?application_version=5.7#fractureageometrycollection)
* [Use the Edit Tools](/documentation/en-us/unreal-engine/edit-tools-user-guide-in-unreal-engine?application_version=5.7#usetheedittools)
* [The Prune tool](/documentation/en-us/unreal-engine/edit-tools-user-guide-in-unreal-engine?application_version=5.7#theprunetool)
* [The Visibility tools](/documentation/en-us/unreal-engine/edit-tools-user-guide-in-unreal-engine?application_version=5.7#thevisibilitytools)
