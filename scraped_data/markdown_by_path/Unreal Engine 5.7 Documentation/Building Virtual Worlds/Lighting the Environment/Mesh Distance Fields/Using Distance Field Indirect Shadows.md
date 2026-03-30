<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-distance-field-indirect-shadows-in-unreal-engine?application_version=5.7 -->

# Using Distance Field Indirect Shadows

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
7. [Mesh Distance Fields](/documentation/en-us/unreal-engine/mesh-distance-fields-in-unreal-engine "Mesh Distance Fields")
8. Using Distance Field Indirect Shadows

# Using Distance Field Indirect Shadows

How to setup and use Distance Field Indirect Shadows.

![Using Distance Field Indirect Shadows](https://dev.epicgames.com/community/api/documentation/image/412d3c72-a9d0-476a-9c96-7d4395aa698f?resizing_type=fill&width=1920&height=335)

 On this page

When your game relies on precomputed lighting with indirectly lit areas, it can be a challenge to blend movable objects because they will not have soft area shadowing. Sometimes you would need to fake this type of effect to blend dynamic objects with the rest of the scene by using complex material setups or even decals. **Distance Field Indirect Shadows** (DFIS) enables you to generate a [Mesh Distance Fields](/documentation/en-us/unreal-engine/mesh-distance-fields-in-unreal-engine) for single Static Meshes for area shadowing in these indirectly lit areas where traditional shadow mapping techniques wouldn't work well.

Distance Field Indirect Shadowing works similarly to [Capsule Shadows](/documentation/en-us/unreal-engine/capsule-shadows-in-unreal-engine) for Skeletal Meshes by using precomputed lighting samples generated during a lighting build. The lighting samples use [Volumetric Lightmaps](/documentation/en-us/unreal-engine/volumetric-lightmaps-in-unreal-engine) to determine the directionality and intensity of the indirect lighting.

In this guide, you'll learn how to enable Distance Fields for individual meshes that can then be used in your levels for area shadowing in areas lit with static indirect lighting so that you see results similar to this:

![Final result example animation](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c43d73e5-de3b-4367-878e-35538c1cd26b/using-dfis-animation.gif)

## Steps

Unlike other [Mesh Distance Fields](/documentation/en-us/unreal-engine/mesh-distance-fields-in-unreal-engine) features, DFIS does not require **Generate Mesh Distance Fields** to be enabled for the entire project. It can be enabled per-mesh, as explained in the steps below.

1. In the **Content Browser**, start by selecting any **Static Mesh** asset and double-clicking to open the **Static Mesh Editor**.

   ![Open Static Mesh asset in the Static Mesh Editor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c589fa4d-fa9e-4aec-ba73-4e0dea237b16/01-using-dfis-open-static-asset.png)
2. In the Static Mesh Editor, navigate to the **Details** panel. In the **Static Mesh Settings** section, set **Generate Mesh Distance Fields** to enabled. After enabling this, you can **save** and **close** the Static Mesh Editor.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c0178b9e-8f6f-4d15-ad3d-dd522b5b4010/02-using-dfis-enable-generating-mdf.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c0178b9e-8f6f-4d15-ad3d-dd522b5b4010/02-using-dfis-enable-generating-mdf.png)

   Click for full image.
3. From the **Content Browser** select the **SM\_MatPreviewMesh\_01** mesh and drag it into the Level **Viewport**.

   ![Drag Static Mesh asset into the Level Viewport](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f0b30a59-8fb3-4cc8-b80b-8125b9758db1/03-using-dfis-drag-to-viewport.png)
4. With the Actor selected in the Level, go to the **Details** panel and set its **Mobility** to **Movable**.

   ![Set Mobility of the Static Mesh asset to Movable](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/79ca58f8-24f9-4208-b1ce-dc7df3d68f85/04-using-dfis-setting-mobility-option.png)
5. Then, under the **Lighting** tab, enable **Distance Field Indirect Shadow**.

   ![Enable Distance Field Indirect Shadow of the Static Mesh asset](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a86fe1e5-4ebf-4b89-9772-8172383aef02/05-using-dfis-enable-dfis.png)
6. If your scene has not already had it's lighting built, click the **Build** on the **Main** menu and select **Build Lighting Only** to build your lighting for the scene.

   ![Build lighting for the scene](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/adfddb32-02b7-4fd4-909d-b7e5f20ad860/06-using-dfis-build-lighting-only.png)

## End Result

In your indirectly lit areas that get a good amount of bounce light, you should see that your movable Static Mesh can cast a soft shadow in indirectly lit areas whereas before there would be no shadow cast.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a5ada1af-6077-4ced-beb5-208389df744b/07-using-dfis-final-result.png)

Keep in mind, that indirect shadows will be practically non-existent in areas that are directly lit or areas that are brightly lit.

## Additional Settings

Use the [Distance Fields Reference](/documentation/en-us/unreal-engine/mesh-distance-fields-properties-in-unreal-engine#actorcomponents) to learn about settings specific to Distance Field Indirect Shadows for Static Mesh Actors.

* [static mesh](https://dev.epicgames.com/community/search?query=static%20mesh)
* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [lighting](https://dev.epicgames.com/community/search?query=lighting)
* [shadows](https://dev.epicgames.com/community/search?query=shadows)
* [distance fields](https://dev.epicgames.com/community/search?query=distance%20fields)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/using-distance-field-indirect-shadows-in-unreal-engine?application_version=5.7#steps)
* [End Result](/documentation/en-us/unreal-engine/using-distance-field-indirect-shadows-in-unreal-engine?application_version=5.7#endresult)
* [Additional Settings](/documentation/en-us/unreal-engine/using-distance-field-indirect-shadows-in-unreal-engine?application_version=5.7#additionalsettings)
