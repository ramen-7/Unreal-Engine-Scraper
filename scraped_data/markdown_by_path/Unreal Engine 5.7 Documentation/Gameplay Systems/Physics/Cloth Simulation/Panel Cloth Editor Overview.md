<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/panel-cloth-editor-overview?application_version=5.7 -->

# Panel Cloth Editor Overview

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
8. Panel Cloth Editor Overview

# Panel Cloth Editor Overview

Overview of the Panel Cloth Editor in Unreal Engine

![Panel Cloth Editor Overview](https://dev.epicgames.com/community/api/documentation/image/f99648d3-b024-4525-99de-3598501ec345?resizing_type=fill&width=1920&height=335)

 On this page

## Introduction

Unreal Engine 5.3 introduces a new way of authoring cloth by using the **Chaos Cloth Panel** node editor. This new workflow focuses on improving iteration times and providing a more flexible, non-destructive way of authoring Chaos Cloth in-engine.

This system uses a **cloth asset** that holds all the information needed to generate and simulate the asset at runtime. You build the asset via the Chaos Cloth Panel node editor and use a Dataflow graph to generate realistic cloth physics from various sources.

When building your clothing asset, you can import static meshes from external panel-based Digital Content Creation (DCC) packages, and transfer skin weights and masks. You can also add XPBD cloth constraints and use LSV (Level Set Volume) collision for the simulation.

Once you create the asset, you can use it with any skeletal or static mesh via the Chaos Cloth component.

This workflow separates the clothing assets from their respective skeletal meshes and provides artists with the ability to generate clothing assets that a variety of characters can use. In addition, it improves iteration times by removing the need to make adjustments to the clothing assets outside of Unreal Engine.

## Legacy vs. New Panel Editor

### Physical Simulation

The Chaos Cloth Panel node editor and the legacy cloth editor use the same Chaos solver for the physical simulation. However, the panel node editor has expanded functionality with optional (XPBD) constraint types.

Long-term, the Chaos Cloth Panel node editor will continue to expand in functionality and aims to support a real-time workflow, as well as a VFX-oriented workflow (by using caching). The setup with the Dataflow graph determines how fast or how precise the simulation will be.

### Clothing Asset Rendering

The Chaos Cloth Panel node editor provides finer control over the clothing asset setup and does not bake the clothing metrics to the draped pose. This, in turn, provides a better-looking simulation with the right setup, even with the old constraints.

The Cloth Asset workflow uses a separate clothing asset that does not depend on a Skeletal Mesh. This provides more flexibility to the artist and the ability to use as many materials as desired in the cloth render Mesh.

However, it comes at a slightly higher rendering cost compared to the legacy system. This is because the clothing assets are being rendered separately by a component, which has more overhead with object management and draw calls.

## Workflow Overview

Authoring cloth with the Chaos Cloth Panel node editor has the following overall workflow:

**External DCC Package**

* Import your character's skeletal mesh into the external DCC package.
* Create the clothing assets and make sure they fit correctly. Make sure to create separate render and simulation meshes.
* Export both of the static meshes in FBX format.

**Unreal Engine**

* Import the static meshes into Unreal Engine.
* Create a new cloth asset from each static mesh with a new Dataflow graph.
* Build the node graph to generate the cloth asset in a non-destructive way.
* Transfer skin weights from the skeletal mesh into the cloth static mesh.
* Configure the cloth settings - similar to the legacy system.
* Add weight maps to the cloth mesh.
* Set a Physics Asset for collision.
* Add a Chaos Cloth Component to your character Blueprint and add the cloth asset.
* Test the clothing simulation in-game.

To learn more about this workflow follow the [Panel Cloth Editor tutorial](https://dev.epicgames.com/community/learning/tutorials/pv7x/unreal-engine-cloth-panel-editor).

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Introduction](/documentation/en-us/unreal-engine/panel-cloth-editor-overview?application_version=5.7#introduction)
* [Legacy vs. New Panel Editor](/documentation/en-us/unreal-engine/panel-cloth-editor-overview?application_version=5.7#legacyvsnewpaneleditor)
* [Physical Simulation](/documentation/en-us/unreal-engine/panel-cloth-editor-overview?application_version=5.7#physicalsimulation)
* [Clothing Asset Rendering](/documentation/en-us/unreal-engine/panel-cloth-editor-overview?application_version=5.7#clothingassetrendering)
* [Workflow Overview](/documentation/en-us/unreal-engine/panel-cloth-editor-overview?application_version=5.7#workflowoverview)
