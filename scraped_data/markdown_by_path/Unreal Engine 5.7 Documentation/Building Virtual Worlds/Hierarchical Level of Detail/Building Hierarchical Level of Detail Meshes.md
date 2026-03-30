<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/building-hierarchical-level-of-detail-meshes-in-unreal-engine?application_version=5.7 -->

# Building Hierarchical Level of Detail Meshes

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
5. [Building Virtual Worlds](/documentation/en-us/unreal-engine/building-virtual-worlds-in-unreal-engine "Building Virtual Worlds")
6. [Hierarchical Level of Detail](/documentation/en-us/unreal-engine/hierarchical-level-of-detail-in-unreal-engine "Hierarchical Level of Detail")
7. Building Hierarchical Level of Detail Meshes

# Building Hierarchical Level of Detail Meshes

This how to covers how to generate the HLOD meshes for your HLOD enabled Unreal Engine 5 project.

![Building Hierarchical Level of Detail Meshes](https://dev.epicgames.com/community/api/documentation/image/d15f7833-5041-4c4b-a40e-186cc00bad2a?resizing_type=fill&width=1920&height=335)

 On this page

In order to use **Hierarchical Level of Detail** (HLOD) Meshes, there are two processes you must perform in order to set up HLOD Meshes in your Level. First, you must **Generate Clusters** which groups **Actors** in your level together based on the settings you specify in the **Cluster Generation Settings**.

After Generating Clusters, you can then **Generate Proxy Meshes** out of those clusters. The process of Generating Proxy Meshes can take a long time based on the complexity of your scene or the settings specified in the **Mesh Generation Settings**.

In this how-to, we go through an example of building HLOD Meshes by Generating Clusters and Generating Proxy Meshes.

[![Build HLOD Mesh](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/23a9ad86-bcd4-4bff-9174-392fbe217243/01-build-hlod-mesh-hero.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/23a9ad86-bcd4-4bff-9174-392fbe217243/01-build-hlod-mesh-hero.png)

Click image for full size.

## Steps

1. After you define your [Cluster Generation Settings](building-virtual-worlds/hierarchical-level-of-detail/hierarchical-level-of-detail-reference) for the HLOD levels you need, click the **Generate Clusters** button.

   [![Build HLOD Mesh](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/38729299-32ee-446c-a8cf-992027a69fda/02-build-hlod-mesh-step-01.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/38729299-32ee-446c-a8cf-992027a69fda/02-build-hlod-mesh-step-01.png)

   Click image for full size.

   [![Cluster Generation Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6c468d7e-f48d-4262-8105-48d9a62a844f/03-cluster-generation-settings.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6c468d7e-f48d-4262-8105-48d9a62a844f/03-cluster-generation-settings.png)

   Click image for full size.

   Once the process starts, you will see a progress bar appear that indicates the LOD level being generated.

   [![Building HLOD Clusters](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/704cfba4-8801-4400-a8a9-fcc4199ca7f8/04-building-hlod-clusters-1.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/704cfba4-8801-4400-a8a9-fcc4199ca7f8/04-building-hlod-clusters-1.png)

   Click image for full size.
2. After clustering completes, the clustered **LOD Actors** will be populated inside the [HLOD Outliner](/documentation/en-us/unreal-engine/hierarchical-level-of-detail-outliner-in-unreal-engine) window.

   [![Building HLOD Cluster Actors](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3adb3784-e959-4ade-9ea7-eed7c8d50dea/05-building-hlod-cluster-actors.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3adb3784-e959-4ade-9ea7-eed7c8d50dea/05-building-hlod-cluster-actors.png)

   Click image for full size.

   You can expand an **LOD Actor** to view the clustered Static Meshes by clicking the expand arrow to the left of the name.

   [![Building HLOD Cluster Actors Expanded](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3d1c07be-32e7-45ad-a0cd-0339116b7275/06-building-hlod-cluster-actors-expanded.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3d1c07be-32e7-45ad-a0cd-0339116b7275/06-building-hlod-cluster-actors-expanded.png)

   Click image for full size.

   You can also see  the clusters in the **Viewport** by selecting an **LOD Actor** (and Static Meshes) from the **HLOD Outliner**.

   [![Build HLOD Mesh Visible](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f3f1debf-4782-4936-8493-f3f65f7ef3d4/07-build-hlod-mesh-visible.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f3f1debf-4782-4936-8493-f3f65f7ef3d4/07-build-hlod-mesh-visible.png)

   Click image for full view.

   If you want to make changes to a given cluster, you can adjust the **Cluster Generation Settings** to your desired settings and **Generate Clusters** again. You can also use the [HLOD context menus](/documentation/en-us/unreal-engine/hierarchical-level-of-detail-outliner-in-unreal-engine#lodactorcontextmenu) to define settings for **LOD Actors** or what to do with a Static Mesh Actor in a cluster.
3. Once you are satisfied with the clusters, click the **Generate Proxy Meshes** button.

   [![Build HLOD Mesh Generate Button](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ec12c080-b514-4724-9af2-f282693187f3/08-build-hlod-mesh-generate-button.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ec12c080-b514-4724-9af2-f282693187f3/08-build-hlod-mesh-generate-button.png)

   Click image for full size.

     

   Once the process starts, a progress bar will appear and indicates the **LODActor** and **LOD Level** being worked on out of the total number of Proxy Meshes that will be generated.

   [![Build HLOD Mesh Generate Building](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/808e007a-d62c-478e-93e2-d950ebe3fc4b/09-build-hlod-mesh-generate-building.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/808e007a-d62c-478e-93e2-d950ebe3fc4b/09-build-hlod-mesh-generate-building.png)

   Click image for full size.

   Depending on your HLOD Settings, the complexity of your scene, and your computer specifications, this process can take a long time to complete. As a frame of reference, a system with a 12-core i7 processor, a GTX-980 video card, and 64 GB of RAM took 10 to 12 minutes with default settings on both HLOD Levels, with 100+ LOD Actors per HLOD level.

   [![Build HLOD Mesh Generate](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1e726070-ea2e-4b0e-9938-2b2ef54496d9/10-build-hlod-mesh-generate.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1e726070-ea2e-4b0e-9938-2b2ef54496d9/10-build-hlod-mesh-generate.png)

   Click image for full size.

### Generate Clusters

Cluster generation uses the settings from the individual HLOD Levels to decide how it should group **Static Mesh Actors** in the scene together. This generation process can take some time depending on the settings use, the number of **Actors** being groups, whether materials are generated, and generally on your hardware's specs.

1. Once you've setup your specific settings for the individual HLOD levels you need, click the **Generate Clusters** button.

   [![Generate Clusters Button](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/96e2afb7-0138-4c30-bbcb-588c74ae59b2/11-generate-clusters-button.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/96e2afb7-0138-4c30-bbcb-588c74ae59b2/11-generate-clusters-button.png)

   Click image for full size.

   Once the process starts you'll see a progress bar appear that indicates the LOD level being generated.

   [![LOD Level Being Generated](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2c84fea7-5a0e-48c7-9b93-19a5be853cc1/12-lod-level-being-generated.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2c84fea7-5a0e-48c7-9b93-19a5be853cc1/12-lod-level-being-generated.png)

   Click image for full size.
2. Now that the process has completed you'll see the **HLOD Outliner** populated with all the clustered **Actors**.

   [![HLOD Outliner populated with all the Clustered Actors](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ddbba766-f187-4ea6-a7f9-6064b61bf0fd/13-hlod-outliner-populated-with-all-the-clustered-actors.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ddbba766-f187-4ea6-a7f9-6064b61bf0fd/13-hlod-outliner-populated-with-all-the-clustered-actors.png)

   Click image for full size.
3. You can expand the individual **LODActors** to see what **Static Meshes** make up this cluster by clicking the arrow button to the left of the name.

   [![Static Meshes make up the expand individual Cluster of LODActors](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/72d943b8-08a8-461d-89f1-f52020df66d3/14-static-meshes-make-up-the-expand-individual-cluster-of-lodactors.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/72d943b8-08a8-461d-89f1-f52020df66d3/14-static-meshes-make-up-the-expand-individual-cluster-of-lodactors.png)

   Click image for full size.
4. You can visualize the clusters in the level by selecting a **LODActor** from the **HLOD Outliner** and locating it in the editor viewport.

   [![Selecting a LODActor from the HLOD Outliner and visualize it in the Editor Viewport](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0dd27fb8-0f5d-443a-9132-544e45304871/15-selecting-a-lodactor-in-the-editor-viewport.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0dd27fb8-0f5d-443a-9132-544e45304871/15-selecting-a-lodactor-in-the-editor-viewport.png)

   Click image for full size.

To visualize how the generated clusters work in the editor you can use the **Forced LOD Level** menu to see the HLOD in action without the need to have it transition at a specific screen size. This is helpful for troubleshooting any issues appearing on screen that may be part of the generated cluster.

[![Forced LOD Level](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/03e32116-afb4-4766-88e4-f7298d50a4a8/16-forced-lod-level.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/03e32116-afb4-4766-88e4-f7298d50a4a8/16-forced-lod-level.png)

Click image for full size.

Should you run into any issues you don't like with the generated cluster you can expand the specified cluster and select the offending **Static Mesh Actor**. You can then click and drag it to another cluster, or you have the option to **Remove** or **Exclude** it from the generation of the cluster by right-clicking on the **Actor's** name in the list.

**Actors** can also be excluded on a per-instance basis by selecting them in the level and in their **Details Panel** set the option for **Can be in Cluster** to false.

Further, if you wish to add an **Actor** to a **Cluster** you can click and drag from the **Outliner** to the **Cluster** you wish it to be included in.

[![Can be in Cluster](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f35118f2-8b52-4556-b7c6-94b0d06ad709/17-can-be-in-cluster.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f35118f2-8b52-4556-b7c6-94b0d06ad709/17-can-be-in-cluster.png)

Click image for full size.

Repeat this process while adjusting the values in the HLOD's level **Cluster Generation Settings** until you are happy with the clusters being generated, then continue on to the next section: **Generate Proxy Meshes**.

### Generate Proxy Meshes

After you're happy with the results of the generated cluster you can move on to the option to Build the clusters into a Proxy Mesh. This proxy mesh will be a newly created **Static Mesh Actor** that combines materials (if enabled), has it's own lightmaps, and it's own editable static mesh that can be opened in the static mesh editor.

1. If you're ready to build the proxy meshes you can now click the button "Generate Proxy Mesh" button to start the process.

   [![Generate Proxy Mesh Button](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cc98eb27-de1f-4dd9-9b44-f51f8a781083/18-generate-proxy-mesh-button.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cc98eb27-de1f-4dd9-9b44-f51f8a781083/18-generate-proxy-mesh-button.png)

   Click image for full size.

   Once the process starts you'll see the progress bar appear that indicates the HLOD Level being worked on and the number of Proxy Meshes being generated. This progress bar does not show all the HLOD Levels and total number of proxy meshes being created, only that specific level.

   [![Proxy Meshes being Generated](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/99030e82-01e5-4671-98a2-4733713e94bf/19-proxy-meshes-being-generated.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/99030e82-01e5-4671-98a2-4733713e94bf/19-proxy-meshes-being-generated.png)

   Click image for full size.

   Depending on your HLOD Level settings, the number of proxy meshes being created, and your system specs this process can take a while, even for high-end machines!

As a reference the Proxy Mesh Generation process for my machine (12-core i7 processor, GTX-980, and 64GB of RAM) took ~10-12 minutes with default settings for both HLOD Levels and ~100+ **LODActors** per HLOD level.

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [hlod](https://dev.epicgames.com/community/search?query=hlod)
* [level of detail](https://dev.epicgames.com/community/search?query=level%20of%20detail)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/building-hierarchical-level-of-detail-meshes-in-unreal-engine?application_version=5.7#steps)
* [Generate Clusters](/documentation/en-us/unreal-engine/building-hierarchical-level-of-detail-meshes-in-unreal-engine?application_version=5.7#generateclusters)
* [Generate Proxy Meshes](/documentation/en-us/unreal-engine/building-hierarchical-level-of-detail-meshes-in-unreal-engine?application_version=5.7#generateproxymeshes)
