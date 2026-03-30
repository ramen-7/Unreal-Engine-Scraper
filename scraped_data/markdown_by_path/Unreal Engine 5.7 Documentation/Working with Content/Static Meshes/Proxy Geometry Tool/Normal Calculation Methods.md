<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/normal-calculation-methods-with-the-proxy-geometry-tool-in-unreal-engine?application_version=5.7 -->

# Normal Calculation Methods

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
8. Normal Calculation Methods

# Normal Calculation Methods

Adjusting the Normal Calculation Method for the simplified geometry.

![Normal Calculation Methods](https://dev.epicgames.com/community/api/documentation/image/ac30086e-8d6c-49a8-b656-b6959949fbfc?resizing_type=fill&width=1920&height=335)

 On this page

The Proxy Geometry tool will allow you to specify which method should be used when computing the Vertex Normals of a given Static Mesh. In the following How-To we will take a look at how you can change the Vertex Normal calculation method and the effect that will have on your generated Static Meshes.

## Steps

In the following section, we will take a look at how you can adjust the method that is used to calculate the Normals that are used for a Static Mesh.

1. First, locate a Static Mesh or group of Static Meshes that you want to generate new geometry for and select the Mesh or Meshes inside the Viewport.  
   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5230fc54-8d11-4cc2-8f03-80f43512e3ad/normalcalculationmethod_02.png "NormalCalculationMethod_02.png")
2. Next, open the **Merge Actor** tool by going to **Window > Developer Tools > Merge Actors**.  
   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/de0d6991-8878-4a30-807f-3a477fe233c3/gapfilling_02.png "GapFilling_02.png")
3. In the Merge Actor tool, click the **second icon** to access the **Proxy Geometry** tool and then expand the **Proxy Settings**.  
   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c6f8fe1b-927a-4e7b-a8ce-b844c47b3373/normalcalculationmethod_03.png "NormalCalculationMethod_03.png")
4. Set the **Screen Size** value to **50** and make sure that the **Normal Calculation Method** is set to **Angle Weighted**.  
   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2c7624d2-9637-4af5-903c-2dd20dd5f016/normalcalculationmethod_04.png "NormalCalculationMethod_04.png")

   By setting the Screen Size to a value of 50 we are telling the Proxy Geometry tool to reduce the amount of triangles used in the selected Static Mesh.
5. Next, click the **Merge Actors** button and input a name and location in the **Content Browser** for the newly created Static Mesh. Then click the **Save** button to start the merging process.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bf45069c-ab14-4965-9aae-df0fa6226b26/gapfilling_06.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bf45069c-ab14-4965-9aae-df0fa6226b26/gapfilling_06.png)
6. Once that has completed, double-click the Static Mesh to open it in the **Static Mesh Editor**, where you can see the results.

[![NormalCalculationMethod_05.png](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2a2a2b77-d8e1-4b9f-8004-ddbafab2c30d/normalcalculationmethod_05.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2a2a2b77-d8e1-4b9f-8004-ddbafab2c30d/normalcalculationmethod_05.png)

## End Results

Getting the best results is going to take some time and iteration as each object could require a different Normal Calculation Method to achieve the desired results. The results can also be very subtle depending on the type of object that you are using. The following image comparison shows how the Static Mesh used in this example looks when the Normal Calculation Method is set to Angle Weighted, Area Weighted and Equal Weighted.

![The following image slider shows the results that each of the three Normal Calculation Methods can achieve. First you will see  Angle Weighted then Area Weighted and finally Equal Weighted.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7ecc3f82-a7a0-422b-b76e-f7c95aa44976/angleweighted.png)
![The following image slider shows the results that each of the three Normal Calculation Methods can achieve. First you will see  Angle Weighted then Area Weighted and finally Equal Weighted.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bdd8c9b8-94fa-4dce-bfc4-bef374435502/areaweighted.png)
![The following image slider shows the results that each of the three Normal Calculation Methods can achieve. First you will see  Angle Weighted then Area Weighted and finally Equal Weighted.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/27b3f0e6-600d-42ed-8875-891faced811a/equalweighted.png)

The following image slider shows the results that each of the three Normal Calculation Methods can achieve. First you will see  Angle Weighted then Area Weighted and finally Equal Weighted.



---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/normal-calculation-methods-with-the-proxy-geometry-tool-in-unreal-engine?application_version=5.7#steps)
* [End Results](/documentation/en-us/unreal-engine/normal-calculation-methods-with-the-proxy-geometry-tool-in-unreal-engine?application_version=5.7#endresults)
