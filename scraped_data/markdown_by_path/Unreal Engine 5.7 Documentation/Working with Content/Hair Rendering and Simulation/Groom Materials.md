<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/groom-materials-in-unreal-engine?application_version=5.7 -->

# Groom Materials

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
6. [Hair Rendering and Simulation](/documentation/en-us/unreal-engine/hair-rendering-and-simulation-in-unreal-engine "Hair Rendering and Simulation")
7. Groom Materials

# Groom Materials

Manage materials for your grooms.

![Groom Materials](https://dev.epicgames.com/community/api/documentation/image/2973e107-5b87-4f14-93ae-22bf7186a584?resizing_type=fill&width=1920&height=335)

The **Material** panel in the [Groom Asset Editor](/documentation/en-us/unreal-engine/groom-asset-editor-user-guide-in-unreal-engine) regroups all the materials a groom uses. You can add material slots with the **Add (+)** icon and remove them with the **Remove (trash bin)** icon. Each material has a unique name, which appears as a dropdown menu in the **Cards**, **Meshes**, and **Strands** panels. On each Groom component, a material slot can override the ones set in the Groom Asset Editor.

![Groom Asset Editor Material Slots](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5c332868-17d9-494e-8710-b2196b555712/groom-asset-editor-material-slots.png)

For a material to be valid for use with a groom, the material must use the **Hair** shading model.

![Material Shader Model Selection set to Hair](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a87627dc-6c0f-4d46-bdfa-c494da124d26/hair-shading-model-setting.png)


The flag **Use with Hair Strands** must also be enabled in the **Usage** section of the Material Editor. This flag is automatically set when you apply the material to a groom for the first time, but if not, you can enable it manually.

In a Material Graph, you can access hair attributes with the **Hair Attributes** expression.

![Hair Attributes material expression](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c95c9421-8562-4480-8c11-892797133e7b/hair-attributes-material-expression.png)

| Property | Description |
| --- | --- |
| **U / V** | The UV coordinates of hair. The U coordinate is always *along* the hair, with 0 being the root and 1 the tip. |
| **Length** | The length of the current curve. |
| **Radius** | Radius of the curve at the current position. |
| **Seed** | Random value in 0 to 1, and uniform along the curve. |
| **Tangent** | Tangent vector aligned in the direction of the curve. |
| **Root UV** | UV of the underlying mesh at the curve's root position. |
| **BaseColor** | Per curve's point color. |
| **Roughness** | Per curve's point roughness. |
| **Depth** | Depth offset. Only used for cards and mesh geometry. |
| **Coverage** | Coverage mask value. Only used for cards and mesh geometry. |
| **AuxiliaryData** | Auxiliary data that is only used for cards and mesh geometry. |
| **AtlasUVs** | Cards UVs that are only used for cards and mesh geometry. |
| **Group Index** | The group index of the curve. |
| **AO** | Per curve's ambient occlusion. |
| **Clump ID** | The clump ID of the curve. |

Below is an example using the Hair Attributes expression used in a "hair" material:

![Example of a material setup to be used for hair.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/941ec2db-6c63-4d3b-9490-86c751093021/hair-material-example.png)

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [physics](https://dev.epicgames.com/community/search?query=physics)
* [hair](https://dev.epicgames.com/community/search?query=hair)
* [metahumans](https://dev.epicgames.com/community/search?query=metahumans)
* [grooms](https://dev.epicgames.com/community/search?query=grooms)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)
