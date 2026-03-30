<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-proxy-geometry-tool-with-hlods-in-unreal-engine?application_version=5.7 -->

# Using the Proxy Geometry tool with HLODs

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
8. Using the Proxy Geometry tool with HLODs

# Using the Proxy Geometry tool with HLODs

How to use the Proxy Geometry Tool with the Hierarchical Level of Detail (HLOD) system.

![Using the Proxy Geometry tool with HLODs](https://dev.epicgames.com/community/api/documentation/image/8858246f-f1a6-4e2f-b1c2-b8fc0c117c2b?resizing_type=fill&width=1920&height=335)

 On this page

In the following How-To, we will take a look at using the Proxy Geometry Tool in conjunction with the [Hierarchical Level of Detail](/documentation/en-us/unreal-engine/hierarchical-level-of-detail-in-unreal-engine) (HLOD) system. Using these two tools together will help increase your Unreal Engine 4 (UE4) project's rendering performance by reducing both draw calls and number of triangles drawn to the screen per frame.

## Steps

1. Go to your project's [World Settings](/documentation/en-us/unreal-engine/world-settings-in-unreal-engine) and display the **LODSystem** menu option.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a92da9ca-a0d5-4e21-9f04-b9c95c41d9c4/proxy_geo_ht_whlod_01.png)
2. In the LODSystem menu, enable the following two options:

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/48375cfe-48fe-4ee4-9734-cdefb445ca6a/proxy_geo_ht_whlod_02.png)

   | **Property Name** | **Description** |
   | --- | --- |
   | **Enable Hierarchical LOD System** | Enables the HLOD to be used with this level. |
   | **Simplify Mesh** | Enables Proxy Geometry Static Mesh simplification. |
3. Open up the **Hierarchical LOD Outliner** tools by going to **Window > Hierarchical LOD Outliner**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c02313ba-5fee-4697-b32a-56b629cecfc2/proxy_geo_ht_whlod_03.png "Proxy_Geo_HT_WHLOD_03.png")
4. Press the **Generate Clusters** button on the **Hierarchical LOD Outliner** and when that is completed, press the **Generate Proxy Meshes** button to begin the HLOD and Proxy Geometry creation process.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/63523d13-fa00-46c2-9637-957b44f7d95a/proxy_geo_ht_whlod_04.png "Proxy_Geo_HT_WHLOD_04.png")

## End Result

When the Hierachical LOD tool has finished processing, you can see how many triangles were removed and also compare the results against the original by moving the slider back and forth.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0a0c1977-c41b-4f1e-9fb9-528e7f409976/proxy_geo_ht_whlod_05.png "Proxy_Geo_HT_WHLOD_05.png")

The image comparison slider below shows an example of the types of results you can get when using just the default settings with **Simplify Mesh** enabled.

![Before Running HLOD & Proxy Geo](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/89d1a17d-f168-4281-b6b1-b1806bc38e0b/proxy_geo_ht_whlod_before.png)

![After Running HLOD & Proxy Geo](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/307d6ea9-17c8-48b0-a9e2-bdc0ab16e206/proxy_geo_ht_whlod_after.png)

Before Running HLOD & Proxy Geo

After Running HLOD & Proxy Geo

* [hlod](https://dev.epicgames.com/community/search?query=hlod)
* [proxygeometry](https://dev.epicgames.com/community/search?query=proxygeometry)
* [optmization](https://dev.epicgames.com/community/search?query=optmization)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/using-the-proxy-geometry-tool-with-hlods-in-unreal-engine?application_version=5.7#steps)
* [End Result](/documentation/en-us/unreal-engine/using-the-proxy-geometry-tool-with-hlods-in-unreal-engine?application_version=5.7#endresult)
