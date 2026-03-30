<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/mutable-physics-and-clothing-in-unreal-engine?application_version=5.7 -->

# Physics and Clothing

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
6. [Mutable Skeletal Mesh Generation](/documentation/en-us/unreal-engine/mutable-skeletal-mesh-generation-in-unreal-engine "Mutable Skeletal Mesh Generation")
7. [Mutable Development Guides](/documentation/en-us/unreal-engine/mutable-development-guides-in-unreal-engine "Mutable Development Guides")
8. Physics and Clothing

# Physics and Clothing

Learn how to use physics assets and clothing assets with the Mutable plugin.

![Physics and Clothing](https://dev.epicgames.com/community/api/documentation/image/6476ebe0-757b-4f30-88dc-538e2135b081?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

This guide explains how to use physics assets and clothing assets with the Mutable plugin.

## Physics Assets

When a Mutable mesh is assembled, by default the mesh component's reference mesh PhysicsAsset is assigned to it. With simple setups this will suffice, unless the CustomizableObject has parts with very different proportions.

To solve these cases, a more modular approach can be achieved with Mutable support for PhysicsAsset merging. This option that can be enabled in the CutsomizableObject compilation options. Go to the **Object Properties** tab and click **Compile Options** > **Enable Physics Asset Merging**.

![The Enable Physics Asset Merge option](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3128d060-a04d-411d-bd91-4550e8e6f0f1/enable-physics.png)

When enabled, all the PhysicsAssets from the meshes used in the generation of an instance skeletal mesh component will be merged into a single PhysicsAsset. If only one PhysicsAsset is found, and no modification to the body shapes is detected, then nothing is merged, and the original asset is assigned to the generated mesh.

When merging does happen, the generated PhysicsAsset will use the PhysicsAsset in the CustomizableObject components reference SkeletalMesh as a template for the Solver Settings and Solver Type. BodySetups and Constrains will be merged form the constituent PhysicsAssets.

If the PhysicsAssets to merge are complementary and no bone used for one BodySetup in a PhysicsAsset is also used for another PhysicsAsset, then no conflicts can occur and the expected physics asset will be generated.

This might not always be possible, for example, if some customizable parts from different meshes could collide. In that case, some interfacing between the two PhysicsAsset is needed. This can be achieved by adding setups that use the same bone in different physics assets body setups. When merging setups, the shapes of both setups are aggregated and properties are copied from the first body encountered for a given bone. There is no guarantee from which body setup the properties will be copied and, in general, the same properties should be set for possible setups that could be merged.

## Skeletal Mesh Clothing Assets

Mutable supports transfer of clothing simulation data to the generated skeletal meshes.

This feature needs to be enabled per CutomizableObject in its compilation options. Go to the **Object Properties** tab and click **Compile Options** > **Enable Clothing**.

![the Enable Clothing option](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e3266296-9bf4-4c36-8a6b-6532e3cbeac5/enable-clothing.png)

Once enabled, if a skeletal mesh section has clothing assets attached and participates of the final generated mutable mesh, the simulation data will be transferred to it.

If parts of a mesh with clothing simulation attached have been removed, the simulation mesh triangles associated with those parts will be removed as well. When removing mesh triangles, Mutable uses the association between the simulation mesh and the render mesh. The parts of the simulation mesh that don't have this association after the render mesh has been processed by Mutable will be removed.

Clothing assets may have configurations that control some simulation properties, such as iterations or subdivisions shared for all mesh sections with clothing in a skeletal mesh. These are assumed to be the same for all skeletal meshes involved in a CustomizableObject. If multiple shared configurations are found, the first one will be used.

Generated clothing simulation meshes can be visualized using the **Customizable Object** preview. In the **Character** menu, click **Physical Mesh (Wireframe)**.

![the Physical Mesh Wireframe option](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/37c75873-1816-4553-84f8-dd3ff8f7c0ae/enable-physical-mesh-visualization.png)

If a more detailed visualization is needed, use the regular skeletal mesh viewer.

### Current limitations

#### Unsupported operations

One of the main limitations of this feature is that mesh section extensions are not supported. Each mesh part with clothing needs its own mesh section, and merging of clothing assets is not supported.

#### Simulation mesh face removal edge cases

The removal of the simulation mesh parts is done using the association between the render mesh and the simulation mesh. If parts of the original simulation are not associated with any part of the render mesh, these will be removed, even if no remove operations are performed.

#### Multiple influences

Clothing with multiple influences is not supported. In case the asset uses them, the resulting asset will only use the influences with higher weight.

* [beta](https://dev.epicgames.com/community/search?query=beta)
* [working with content](https://dev.epicgames.com/community/search?query=working%20with%20content)
* [skeletal mesh](https://dev.epicgames.com/community/search?query=skeletal%20mesh)
* [mutable](https://dev.epicgames.com/community/search?query=mutable)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Physics Assets](/documentation/en-us/unreal-engine/mutable-physics-and-clothing-in-unreal-engine?application_version=5.7#physicsassets)
* [Skeletal Mesh Clothing Assets](/documentation/en-us/unreal-engine/mutable-physics-and-clothing-in-unreal-engine?application_version=5.7#skeletalmeshclothingassets)
* [Current limitations](/documentation/en-us/unreal-engine/mutable-physics-and-clothing-in-unreal-engine?application_version=5.7#currentlimitations)
* [Unsupported operations](/documentation/en-us/unreal-engine/mutable-physics-and-clothing-in-unreal-engine?application_version=5.7#unsupportedoperations)
* [Simulation mesh face removal edge cases](/documentation/en-us/unreal-engine/mutable-physics-and-clothing-in-unreal-engine?application_version=5.7#simulationmeshfaceremovaledgecases)
* [Multiple influences](/documentation/en-us/unreal-engine/mutable-physics-and-clothing-in-unreal-engine?application_version=5.7#multipleinfluences)
