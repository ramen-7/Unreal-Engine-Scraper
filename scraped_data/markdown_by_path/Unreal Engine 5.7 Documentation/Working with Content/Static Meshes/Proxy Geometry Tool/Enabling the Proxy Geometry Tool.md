<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/enabling-the-proxy-geometry-tool-in-unreal-engine?application_version=5.7 -->

# Enabling the Proxy Geometry Tool

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
6. [Static Meshes](/documentation/en-us/unreal-engine/static-meshes "Static Meshes")
7. [Proxy Geometry Tool](/documentation/en-us/unreal-engine/proxy-geometry-tool-in-unreal-engine "Proxy Geometry Tool")
8. Enabling the Proxy Geometry Tool

# Enabling the Proxy Geometry Tool

Product documentation including reference and guides for Unreal Engine 5

![Enabling the Proxy Geometry Tool](https://dev.epicgames.com/community/api/documentation/image/4fe14131-9092-47fa-b11d-aba06fec55f5?resizing_type=fill&width=1920&height=335)

 On this page

Before your can use the Proxy Geometry tool you will first need to enable it. In the following How - To we will take a look at how you go about enabling the Proxy Geometry tool in your UE5 projects.

## Steps

1. First launch your UE5 project and once it has opened, open up the Project Settings by going to the main toolbar and selecting **Edit > Project Settings**.

   [![Project Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c5d35469-dac7-4de8-9d94-d95fd5f07e5d/01-project-settings.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c5d35469-dac7-4de8-9d94-d95fd5f07e5d/01-project-settings.png)

   Click image for full size.
2. Once the Project Settings is open, go to **Editor > Hierarchical LOD Mesh Simplification** and under the **General** section click the **Hierarchical LOD Mesh Reduction Plugin** and then select the **ProxyLODMeshReduction** plugin.

   [![ProxyLODMeshReduction plugin](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dd81a59f-3e78-4c39-a4f4-c3296165df37/02-proxy-lod-mesh-reduction-plugin.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dd81a59f-3e78-4c39-a4f4-c3296165df37/02-proxy-lod-mesh-reduction-plugin.png)

   Click image for full size.
3. Then go to **Tools** and then click on the **Merge Actors** option.

   [![Merge Actors option](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/49199c20-ecb0-46f4-b97b-6e60c3b4463a/04-merge-actors-option.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/49199c20-ecb0-46f4-b97b-6e60c3b4463a/04-merge-actors-option.png)

   Click image for full size.

## End Result

When the Merge Actors tools is open, you should see two icons at the top. Click on the second icon to access the options for the Proxy Geometry Tools.

[![Proxy Geometry Tools](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1902394c-f52e-422c-a378-db9318ea26d7/05-proxy-geometry-tools.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1902394c-f52e-422c-a378-db9318ea26d7/05-proxy-geometry-tools.png)

Click image for full size.

Note that all options will be grayed out until a Static Mesh that is placed in a level is selected.

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [proxy geometry tool](https://dev.epicgames.com/community/search?query=proxy%20geometry%20tool)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/enabling-the-proxy-geometry-tool-in-unreal-engine?application_version=5.7#steps)
* [End Result](/documentation/en-us/unreal-engine/enabling-the-proxy-geometry-tool-in-unreal-engine?application_version=5.7#endresult)
