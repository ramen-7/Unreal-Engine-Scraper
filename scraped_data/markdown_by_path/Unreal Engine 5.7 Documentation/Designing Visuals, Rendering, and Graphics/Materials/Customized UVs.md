<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/customized-uvs-in-unreal-engine-materials?application_version=5.7 -->

# Customized UVs

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
5. [Designing Visuals, Rendering, and Graphics](/documentation/en-us/unreal-engine/designing-visuals-rendering-and-graphics-with-unreal-engine "Designing Visuals, Rendering, and Graphics")
6. [Materials](/documentation/en-us/unreal-engine/unreal-engine-materials "Materials")
7. Customized UVs

# Customized UVs

Feature that allows running calculations in the vertex shader to increase performance over running them per-pixel.

![Customized UVs](https://dev.epicgames.com/community/api/documentation/image/264ae1b5-d486-4cf9-89df-92526fe12d68?resizing_type=fill&width=1920&height=335)

 On this page

On GPU's, the vertex shader is run for every vertex, and the pixel shader is run for every pixel. Almost all the material nodes in Unreal Engine 4 are run for every pixel. While a **UV Coordinate** node can be either part of the vertex or pixel shader, the **CustomizedUVs** feature is only run in the vertex shader, and offers a performance increase over running the same calculations in the pixel shader. This offers an excellent way to speed up even just tiling a texture. While the system is not limited in the math you run on the UVs, the result will depend on the tessellation of your mesh.

Note: Customized UVs are currently only implemented for certain component types: Static Meshes, Skeletal Meshes, BSP, landscape, and mesh particles. Notably Sprite particles do not support Customized UVs yet.

## Properties

In the **Material Editor**, you can set the number of **CustomizedUVs** input pins by selecting the main material node and editing the **Num Customized UVs** property in the **Material** category. If **Num Customized UVs** is set to a number greater than 0, CustomizedUVs pins will show on the main material node.

![Customized UVs Properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/19979182-c648-45ea-8e8d-2779110023ee/customized-uv-properties.png)

## Non-Linear Math

The general rule is that if the computation you are doing is using constants (camera position, time, vector parameters, etc.) or varies linearly with per-vertex attributes, then doing that work in the vertex shader will give the same results as doing them in the pixel shader. Varying linearly means only operations that will result in straight lines, no curves, such as multiplication and addition. Squaring a variable, using sine, cosine, or operations like `length` will result in a non-linear equation.

Whether or not non-linear math will produce a desirable result will depend on the detail of the mesh it is being applied to:

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0bd30e75-a602-43d3-90d8-2b1022a2ac96/cuvs_highvslowdetailmesh.png)

*The mesh on the left is a 9x9 polygon grid, while the one on the right is a 4x4 polygon grid.*

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9b4023a9-c1ce-43e2-80a6-55240cb84b07/customized-uv-graph-01.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9b4023a9-c1ce-43e2-80a6-55240cb84b07/customized-uv-graph-01.png)

Click to enlarge image.

In contrast, if this same math is directly inputted into a texture, it will be evaluated in the pixel shader producing the same result regardless of mesh detail.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/44ad584b-0e7d-4eb6-b950-df1202d0ff2f/cuvs_perpixel.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/44ad584b-0e7d-4eb6-b950-df1202d0ff2f/cuvs_perpixel.png)

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ea6b9807-d5b9-49c2-972e-1567bb913e29/customized-uv-graph-02.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ea6b9807-d5b9-49c2-972e-1567bb913e29/customized-uv-graph-02.png)

Click to enlarge image.

## Linear Math

Scaling (multiplying) UVs by a parameter will work the same in both. The UVs are per-vertex attributes, and scaling is a linear operation. The images below show when doing linear operations, CustomizedUVs, which are calculated in the vertex shader, produce the same effect as doing the same calculation in the pixel shader.

![In this example the result is the same whether the UV tiling is caluculated in the vertex shader (with customized UVs) or in the pixel shader.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5f161e89-55da-4a68-b52a-01fc49b06cb4/linear-math-01.png)
![In this example the result is the same whether the UV tiling is caluculated in the vertex shader (with customized UVs) or in the pixel shader.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/21fe34e8-699b-4e2d-a2e3-32ac3078f698/linear-math-02.png)

**In this example the result is the same whether the UV tiling is caluculated in the vertex shader (with customized UVs) or in the pixel shader.**

## How it works

The CustomizedUV pins pass through the texture coordinates (UVs) in the mesh by default. Then when you place a Texcoord node in a pixel shader input (like BaseColor), you are still getting the mesh's texture coordinates. However, if you do something in CustomizedUV0 and then use Texcoord 0 in the BaseColor input, you will get the modified UV value. Note that Texture sample nodes use TexCoord 0 by default.

**Shader Model 5** on PC can use 8 custom UVs, while **OpenGL ES2** on mobile can only use 3.

Here is an example, the original material is mapping a texture using world space y and z.

![Texture mapped in world space](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/af88441e-66f4-4b85-b955-9760cd3e970b/customized-uvs-example-01.png)

This material is doing the same thing, the logic in Customized UV 0 is passed through as Texcoord0 to the BaseColor pixel shader input. However, the calculation for Texcoord0 was done in the vertex shader.

![Customized UVs](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d54d47e3-7ed9-410e-8ad6-f540b6674b8e/customized-uvs-example-02.png)

*The Texture Sample node has an implicit TexCoord0 node inside.*

## General Performance

Most of the time, there are substantially fewer vertices than pixels, and moving any math to the vertex shader can be a big performance benefit. Note that if you are making a mesh with a very high poly count, or not making any use of LOD with high poly meshes, the extra vertex shader work can be the bottleneck. This is because the vertex shader work is the same no matter whether the mesh is off in the distance covering 4 pixels or filling up the screen.

## Mobile specific

On mobile, **any texture sample that manipulates the texture coordinates in any way takes a slow path**. These are called *dependent* texture fetches. By using the customized UV inputs, you can still implement tiling or world space texture mapping while keeping all the texture fetches *independent*, which is the fast path.

Additionally, everything in the pixel shader on mobile is evaluated with half precision floats. This causes blocky looking textures and some other artifacts, when pixel shader math is done on texture coordinates. The Customized UV inputs however are done with full precision so they get around this problem.

Here is a cave material setup to use tiling at two different rates, but still only have independent texture samples.

![Customized UVs independent tiling](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8a7fbd0d-2633-4c3e-9e65-17ad0f5df98b/cuvs-independent-tiling.png)

* [materials](https://dev.epicgames.com/community/search?query=materials)
* [shaders](https://dev.epicgames.com/community/search?query=shaders)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Properties](/documentation/en-us/unreal-engine/customized-uvs-in-unreal-engine-materials?application_version=5.7#properties)
* [Non-Linear Math](/documentation/en-us/unreal-engine/customized-uvs-in-unreal-engine-materials?application_version=5.7#non-linearmath)
* [Linear Math](/documentation/en-us/unreal-engine/customized-uvs-in-unreal-engine-materials?application_version=5.7#linearmath)
* [How it works](/documentation/en-us/unreal-engine/customized-uvs-in-unreal-engine-materials?application_version=5.7#howitworks)
* [General Performance](/documentation/en-us/unreal-engine/customized-uvs-in-unreal-engine-materials?application_version=5.7#generalperformance)
* [Mobile specific](/documentation/en-us/unreal-engine/customized-uvs-in-unreal-engine-materials?application_version=5.7#mobilespecific)
