<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/getting-started-with-parametric-clothing?application_version=5.7 -->

# Getting Started

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
7. [Cloth Simulation](/documentation/en-us/unreal-engine/cloth-simulation-in-unreal-engine "Cloth Simulation")
8. [Creating Parametric Clothing for Fab](/documentation/en-us/unreal-engine/creating-parametric-clothing-for-fab "Creating Parametric Clothing for Fab")
9. Getting Started

# Getting Started

Getting started creating parametric clothing for Fab.

![Getting Started](https://dev.epicgames.com/community/api/documentation/image/a8623db9-6ba2-4435-9b53-02930050df6e?resizing_type=fill&width=1920&height=335)

 On this page

## Essential Terminology

**Parametric and Fixed**

* **Parametric**: Refers clothing assets that can resize with the character.
* **Fixed**: Clothing that is made for one specific body shape (as in legacy assets).

The word **resizable** is also occasionally used interchangeably with parametric in the context of clothing.

**Skeletal Meshes and Outfit Assets**

* **Skeletal Mesh Clothing** (fixed, non resizable): This is previously how clothing creators have been making clothing; creating a clothing model and skinning it to the body.
* **Outfit Asset**: A new asset type. Outfit assets are made to be able to handle complex combinations of separate pieces of clothing. They were also created with resizing capabilities in mind. If you’ve played around with chaos cloth, then you may be familiar with cloth assets — an outfit asset is like a cloth asset but with many additional capabilities, and must contain one or more cloth assets.

**Render Meshes and Sim Meshes**

* **Render Meshes**: These are what you generally think of when you think of the model for your clothing asset.
* **Sim Meshes****:** A sim mesh is a simplified, single-sided mesh. It is used for cloth simulation, which drives the deformation of the more complex render mesh. It may also be lower resolution than a render mesh.

| Render Mesh | Sim Mesh |
| --- | --- |
| A render mesh:   * Is what gets rendered * Can have thickness * Can have detail * Always exists | A sim mesh:   * Drives render mesh * Does not get rendered * Is used for simulation but also can be used for resizing and skinning functionality which is the context we will be discussing in this talk * Is not required and does not have to exist in every asset |

**Presets**

* Presets are how we share information about MetaHumans with each other. **MetaHuman Creator** (MHC) comes with built-in presets, but you can create and share (or sell) your own.

  + Any MetaHuman Character can be used as a preset —  you just need to drag that character or folder into the presets window.
  + Presets can be used to copy all settings, such as facial features, skin tone, hair, etc.
  + They can also be used to transfer body shape only. This allows you to make your own MetaHuman and just transfer info about the body shape from a preset.
  + The body shape of a preset, without the head info, and skin color can be transferred from any preset by double clicking on the image of any preset inside the **All Assets** section of **Body > Blend**.

    [![Body > Blend](https://dev.epicgames.com/community/api/documentation/image/1146beb2-d58d-4aae-8a35-c82fb09f3a3d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1146beb2-d58d-4aae-8a35-c82fb09f3a3d?resizing_type=fit)

## Before You Begin

It’s especially important to note whether your asset has a sim mesh or not. Unless you have created one, or done a USD export from [Clo](https://www.clo3d.com/en/) or [Marvelous Designer](https://www.marvelousdesigner.com/), you will be working with a render mesh only.

Depending on how complex your asset is, you might still prefer to create skeletal mesh clothing instead of parametric clothing. In **Unreal Engine** (UE) 5.6, resizable clothing does not support custom skinning, control rig, or **Rigid Body Animation Notes** (RBAN) on your clothing. You can have all of that on your clothing, but when it resizes, the clothing does a simple skin weight transfer from the body, and overwrites all of it.

Skeletal mesh clothing does not resize, but one important distinction from the previous version of MetaHuman is that now, because of parametric bodies, you can create that clothing for any body shape you want — as opposed to the base 18 archetypes. You can now distribute that body shape via preset, even as a part of the package you sell.

This also means that you do not have to skin your parametric clothing. All you need is the model, and it will function exactly the same.

### Parametric Outfit Asset

As this workflow only covers the process inside of UE, but does not cover asset creation in your DCC of choice, you’ll learn about the new parametric outfit asset.

The outfit asset is a new chaos cloth asset type, which is capable of containing parametric clothing. The outfit asset associates your clothing with the body it was made for (source body). It then warps the clothing based on the difference between the source body and a new body with different measurements (target body).

In some cases, the source body and target body are too different, which can cause warping. This is especially the case with more realistic and detailed (not stylized or simplified) clothing. Due to this, we encourage you to create multiple outfits for multiple source bodies. The closer an original source body is to a target body, the less warping and subsequent artifacts will occur.

You can choose to put in as little or as much additional effort as you feel is necessary for the clothing to meet your needs. You can also start with one, test it, and see if you need to add more. Our system automatically detects which source body is the best match for each new target body and selects the appropriate source clothing to resize from.

## Next Step

* [![Parametric Asset Setup](https://dev.epicgames.com/community/api/documentation/image/822d72e7-722a-4223-9bb9-b6123408839c?resizing_type=fit&width=640&height=640)

  Parametric Asset Setup

  Preliminary steps for creating your parametric outfit asset.](https://dev.epicgames.com/documentation/en-us/unreal-engine/parametric-asset-setup)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Essential Terminology](/documentation/en-us/unreal-engine/getting-started-with-parametric-clothing?application_version=5.7#essentialterminology)
* [Before You Begin](/documentation/en-us/unreal-engine/getting-started-with-parametric-clothing?application_version=5.7#beforeyoubegin)
* [Parametric Outfit Asset](/documentation/en-us/unreal-engine/getting-started-with-parametric-clothing?application_version=5.7#parametricoutfitasset)
* [Next Step](/documentation/en-us/unreal-engine/getting-started-with-parametric-clothing?application_version=5.7#nextstep)
