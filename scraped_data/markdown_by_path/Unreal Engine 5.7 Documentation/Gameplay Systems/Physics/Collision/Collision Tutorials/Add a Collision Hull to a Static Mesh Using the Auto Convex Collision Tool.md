<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/add-a-collision-hull-to-a-static-mesh-using-the-auto-convex-collision-tool-in-unreal-engine?application_version=5.7 -->

# Add a Collision Hull to a Static Mesh Using the Auto Convex Collision Tool

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
7. [Collision](/documentation/en-us/unreal-engine/collision-in-unreal-engine "Collision")
8. [Collision Tutorials](/documentation/en-us/unreal-engine/collision-tutorials-in-unreal-engine "Collision Tutorials")
9. Add a Collision Hull to a Static Mesh Using the Auto Convex Collision Tool

# Add a Collision Hull to a Static Mesh Using the Auto Convex Collision Tool

Product documentation including reference and guides for Unreal Engine

![Add a Collision Hull to a Static Mesh Using the Auto Convex Collision Tool](https://dev.epicgames.com/community/api/documentation/image/cbec9d6a-bd1f-4fd2-858d-ee7bfccf6380?resizing_type=fill&width=1920&height=335)

 On this page

In the following How-To we will take a look at using the Auto Convex Collision tool to automatically create collision for Static Meshes.

The Auto Convex Tool also uses a newer version of [V-HACD library](https://github.com/kmammou/v-hacd) that should give more accurate results.

## Steps

1. First open up the Static Mesh you want to add collision to in the Static Meshes Editor. For this example, we will be using the **SM\_Rock Mesh** that comes with the Starter Content.   
   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/436db27a-ccb4-4e7b-9e26-eb7bed1c7a68/ht_addconvexhulls_01.png "HT_AddConvexHulls_01.png")
2. Next, open up the Auto Convex Collision tool by going to **Collision > Auto Convex Collision**. This will open up the Auto Convex Collision in the lower right-hand corner of the Static Mesh Editor.  
   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c7c9abae-fb05-4e48-ab05-7abce94fd08f/ht_addconvexhulls_02.png "HT_AddConvexHulls_02.png")
3. Inside of the Auto Convex Collision tool set the following parameters with the following settings:  
   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c19fec7d-4055-49bb-b6f2-1247b3bd4feb/ht_addconvexhulls_03.png "HT_AddConvexHulls_03.png")

   | Property Name | Value |
   | --- | --- |
   | **Hull Count** | 32 |
   | **Max Hull Verts** | 16 |
   | **Hull Precision** | 50,000 |
4. When all of the above settings have been input, click the **Apply** button to begin the collision creation process.  
   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9fdab84c-8688-4ab4-85b8-aca8acfde746/ht_addconvexhulls_07.png "HT_AddConvexHulls_07.png")

   Computation of the collision will now run as background task in the Static Mesh Editor. The progress of the collision creation will be shown in the following progress window.  
   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cc836d27-7ec1-448e-9bd5-d81935a05273/ht_addconvexhulls_06.png "HT_AddConvexHulls_06.png")

## End Result

When completed you can view the new collision, if not already enabled, by clicking on the Collision icon and then selecting the Simple Collision option from the drop-down list.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ca9a861d-af2c-4d84-9b9c-4e7eb1e77d02/ht_addconvexhulls_05.png "HT_AddConvexHulls_05.png")
![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7e02d088-f020-44c7-925d-231bb9aa22f3/ht_addconvexhulls_04.png "HT_AddConvexHulls_04.png")

The following image sequence shows what type of results you get when increasing the values of the Auto Convex Collision from the default settings to the maximum settings allowed.

![Auto Convex Collision Settings Results](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/522dc1d9-1f48-496f-98ec-6216da111726/ht_addconvexhulls_default.png)
![Auto Convex Collision Settings Results](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/66e942c1-1749-4a50-a0c5-c9e9d0dd8731/ht_addconvexhulls_medium.png)
![Auto Convex Collision Settings Results](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/40e336dd-ecb1-4db0-b6aa-e8abd12e1851/ht_addconvexhulls_high.png)

Auto Convex Collision Settings Results

* [collision](https://dev.epicgames.com/community/search?query=collision)
* [physics](https://dev.epicgames.com/community/search?query=physics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/add-a-collision-hull-to-a-static-mesh-using-the-auto-convex-collision-tool-in-unreal-engine?application_version=5.7#steps)
* [End Result](/documentation/en-us/unreal-engine/add-a-collision-hull-to-a-static-mesh-using-the-auto-convex-collision-tool-in-unreal-engine?application_version=5.7#endresult)
