<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/lightmass-portals-in-unreal-engine?application_version=5.7 -->

# Lightmass Portals

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
6. [Lighting the Environment](/documentation/en-us/unreal-engine/lighting-the-environment-in-unreal-engine "Lighting the Environment")
7. [Global Illumination](/documentation/en-us/unreal-engine/global-illumination-in-unreal-engine "Global Illumination")
8. Lightmass Portals

# Lightmass Portals

Help increase the quality of baked interior lighting.

![Lightmass Portals](https://dev.epicgames.com/community/api/documentation/image/6a318adf-a0dd-42e7-a6db-339f8ff9031e?resizing_type=fill&width=1920&height=335)

 On this page

![Banner image](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7612e765-e9b8-475c-a8b3-d52324e40375/lightmass-portals-banner.png)

When gathering lighting, Lightmass can backtrack to Point, Spot and Directional light sources using photons from the Photon Mapping technique.
This means that it can find small windows where light is entering from these light types and resolve the incoming lighting with high-quality.
However, SkyLights and Emissive meshes don't support photon emission efficiently, so Lightmass can only find the small important lighting features with brute force.
This manifests as splotchy artifacts around indoor corners. To help Lightmass better understand where the light should be coming from, you can place **Lightmass Portals** Actors around the areas that are critical to lighting.
In the following document, we will take a look at setting up and using Lightmass Portals in your Unreal Engine projects.

## How It Works

From a high-level, Lightmass Portals work in the following manner:

* Lightmass Portals are most useful when a scene is lit using a [Skylight](/documentation/en-us/unreal-engine/sky-lights-in-unreal-engine), HDR image or a Static Mesh that is set to [Use Emissive for Static Lighting](/documentation/en-us/unreal-engine/using-the-emissive-material-input-in-unreal-engine#usingemissivematerialstolighttheworld) checked.

  [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8a2393d9-5c2e-4108-92f5-ab981f4ee37b/01-lightmass-portals-skylight-setup.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8a2393d9-5c2e-4108-92f5-ab981f4ee37b/01-lightmass-portals-skylight-setup.png)

  Click for full image.
* Lightmass Portals are placed and in the level and scaled to fit any open areas that are important to the final lighting.

  ![Example of the scene with Lightmass Portals](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9c5a1683-e8b4-4ab5-bcd7-4d70390cf80d/02-lightmass-portals-example-scene.png)
* When Lightmass is building the light, the Lightmass Portals tell Lightmass that more light rays should come from this area yielding higher quality light and shadows.

  ![Scene without Portals](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/01c1f189-f679-4821-bd05-6dd9149af2b5/03-lightmass-portals-result-without.png)

  ![Scene with Portals](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/709088ce-36ea-46f4-993f-22f683506e4e/04-lightmass-portals-result-with.png)

  Scene without Portals

  Scene with Portals

## Steps

To use Lightmass Portals in your projects, you will need to do the following.

1. From the **Place Actors** panel, search for **Lightmass Portal** and then drag the **Lightmass Portal Actor** into your **Level** to place it.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/54b6e226-d997-4995-a76d-67e3be13dbbe/05-lightmass-portals-adding-actor.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/54b6e226-d997-4995-a76d-67e3be13dbbe/05-lightmass-portals-adding-actor.png)

   Click for full image.
2. Using the **Move**, **Rotate** and **Scale** tools, position and scale the Lightmass Portal to be about the same size or slightly smaller than the opening or area you want Lightmass to focus more rays towards.

   ![Adjusting position and scaleof the Lightmass Portal Actor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8d53c77f-49ff-4694-8637-2742ba28367f/06-lightmass-portals-adjusting-actor.png)
3. Click the **Build** in the **Main** menu panel, select **Build** and change the **Lighting Quality** to **Production**.

   ![Enable production lighting quality](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d63f843b-89a3-4685-a038-89e132bd04cc/07-lightmass-portals-lighting-quality.png)
4. When that has all been completed, click the **Build** in the **Main** menu panel and select **Build All Levels** to start the Lightmass lighting build.

   ![Build the Lightmass lighting](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ae51a761-5a64-4a89-acda-a563faecd694/08-lightmass-portals-build.png)

## End Result

Once your Lightmass build has completed, you will have something similar to the following image.

![Scene without Portals](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/73ab3150-4a4b-4cf8-b36e-e4b740184ea7/09-lightmass-portals-off.png)

![Scene with Portals](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ba390b6f-6a9d-422d-bc60-912528c3b046/10-lightmass-portals-on.png)

Scene without Portals

Scene with Portals

If you take a close look at the **Without Portals** image, you will notice that there is a lot of noise in the image, especially in the darker areas when compared to the **With Portals** image.

## Known Issues and Limitations

* Lightmass Portals work by forcing Lightmass to send rays toward the portal. Because of this, you should only use Lightmass Portals on small levels and only for lighting that is critical to the scene. Failing to do this (and adding too many Lightmass Portals) can drastically increase your Lightmass build times.
* Only use Lightmass Portals on very small levels as Lightmass Portals are not occluded by anything. Using them in big open world-type levels will result in longer-than-needed light baking times.
* If you are using Static Meshes for Emissive light casters and the results are noisy, place a Lightmass Portal around the area where the Static Meshes' light is supposed to be emitted from.

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [lighting](https://dev.epicgames.com/community/search?query=lighting)
* [global illumination](https://dev.epicgames.com/community/search?query=global%20illumination)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [How It Works](/documentation/en-us/unreal-engine/lightmass-portals-in-unreal-engine?application_version=5.7#howitworks)
* [Steps](/documentation/en-us/unreal-engine/lightmass-portals-in-unreal-engine?application_version=5.7#steps)
* [End Result](/documentation/en-us/unreal-engine/lightmass-portals-in-unreal-engine?application_version=5.7#endresult)
* [Known Issues and Limitations](/documentation/en-us/unreal-engine/lightmass-portals-in-unreal-engine?application_version=5.7#knownissuesandlimitations)
