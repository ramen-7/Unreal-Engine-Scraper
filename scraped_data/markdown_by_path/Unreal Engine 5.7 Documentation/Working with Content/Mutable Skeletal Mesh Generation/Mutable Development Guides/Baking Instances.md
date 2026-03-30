<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/baking-instances-using-mutable-in-unreal-engine?application_version=5.7 -->

# Baking Instances

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
8. Baking Instances

# Baking Instances

A guide to baking instances of your skeletal meshes using Mutable.

![Baking Instances](https://dev.epicgames.com/community/api/documentation/image/bc142bcc-8684-408a-b5c5-35b1c0658782?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

The main goal of Mutable is to build dynamic objects at runtime. It is also useful to be able to build these objects in the editor, and convert them to standard Unreal Engine assets (skeletal meshes, materials and textures). Some use cases for this are:

* Production of marketing materials in other tools. From Unreal you can export these assets and import them into other content creation tools for the creation of cinematic videos and offline renders.
* Debugging your object. You can examine a baked instance in standard Unreal Editor tools to better understand the effect of Mutable and try to pinpoint inefficiencies in your object.
* Mutable as a production tool. Some projects use Mutable purely offline at game content creation time, generating final characters for their games.

## Baking an Instance

Instances can be baked using the **Bake Instance** button in any Mutable preview panel. These currently include the Customizable Object Editor and the Customizable Instance Editor.

[![Bake Instance Button](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3b21fd27-23ab-4eb4-8841-c9145ccea329/baking-button.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3b21fd27-23ab-4eb4-8841-c9145ccea329/baking-button.png)

The Bake Instance button is available in any Mutable Preview panel.

A window will pop up to select the target content folder for the generated resources, and a prefix for the asset names:

[![Baking Save Target](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/92b2af0c-19ec-44db-8af3-4c24002d391d/bakin-target.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/92b2af0c-19ec-44db-8af3-4c24002d391d/bakin-target.png)

Select the target content folder to save your baked assets.

There are two additional checkboxes in this window:

* **Export all used resources**: If checked, all the materials and textures used by the object will be baked in the target folder. Otherwise, only the assets that Mutable modifies are baked, and the original references to non-Mutable assets are used instead (i.e. textures used by object materials, but have no nodes connected to them). In other words, checking this box generates a fully self-contained object that doesn't use any shared resources from your project.
* **Generate Constant Material Instances**: If checked, all the material instances in the baked skeletal meshes are constant instead of dynamic. They cannot be changed at runtime but they are lighter and required for UEFN.

The result is a set of Unreal assets in the target folder, including all levels of detail.

[![Baking Result](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dfb05207-10af-4b85-91af-6f2f5e568894/baking-result.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dfb05207-10af-4b85-91af-6f2f5e568894/baking-result.png)

The results of baking out a character skeletal mesh.

* [landscape](https://dev.epicgames.com/community/search?query=landscape)
* [beta](https://dev.epicgames.com/community/search?query=beta)
* [working with content](https://dev.epicgames.com/community/search?query=working%20with%20content)
* [skeletal mesh](https://dev.epicgames.com/community/search?query=skeletal%20mesh)
* [mutable](https://dev.epicgames.com/community/search?query=mutable)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Baking an Instance](/documentation/en-us/unreal-engine/baking-instances-using-mutable-in-unreal-engine?application_version=5.7#bakinganinstance)
