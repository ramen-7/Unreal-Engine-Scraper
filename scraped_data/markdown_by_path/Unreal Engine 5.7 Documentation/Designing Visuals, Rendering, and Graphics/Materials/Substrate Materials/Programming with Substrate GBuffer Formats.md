<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/programming-with-substrate-gbuffer-formats?application_version=5.7 -->

# Programming with Substrate GBuffer Formats

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
7. [Substrate Materials](/documentation/en-us/unreal-engine/substrate-materials-in-unreal-engine "Substrate Materials")
8. Programming with Substrate GBuffer Formats

# Programming with Substrate GBuffer Formats

An overview for programmers using Substrates GBuffer formats in their shader code.

On this page

Substrate introduces changes on how material data are gathered, processed, stored, and used for lighting. This page provides a quick overview of how the system works for programmers.

From an authoring point of view, a material can continue to use the existing root node’s inputs, or use [Substrate Material Nodes](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine#substrate-material-nodes) (Slabs, Operators) and plug them into the root node’s **Front Material** input. Inside a material shader, this is translated by `TEMPLATE_USES_SUBSTRATE==0` in the former case, `TEMPLATE_USES_SUBSTRATE==1` in the latter case.

When using deferred lighting, the material data is stored into an intermediate storage, called **GBuffer**. Substrate comes with two GBuffer storage modes:

* **Blendable GBuffer:** This is similar to the existing GBuffer storage format.
* **Adaptive GBuffer:** This storage is changed into a bitstream of data, whose format changes from pixel to pixel.

This GBuffer format is configured in the project settings and depends on whether the intended target platform supports Adaptive GBuffer or not.

For more information on GBuffer and its usage with Substrate, see the “GBuffer” section of the [Substrate Materials Overview.](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-substrate-materials-in-unreal-engine)

## Scene Texture Data

Scene texture data continues to be queried with `SceneTextureLookup()` for both **Blendable GBuffer** and **Adaptive GBuffer** formats. When using Adaptive GBuffer, this function will only return the first closure data.

## Global Shader

When data needs to be accessed in a global shader, in deferred rendering (for example, for lighting purposes), you need to declare and bind the Substrate global parameter like this:

C++

Declaration

```
class FMyGlobasShaderCS : public FGlobalShader
{
  DECLARE_SHADER_TYPE(FMyGlobasShaderCS, Global)
  SHADER_USE_PARAMETER_STRUCT(FMyGlobasShaderCS, FGlobalShader);
  using FPermutationDomain = TShaderPermutationDomain<>;
  BEGIN_SHADER_PARAMETER_STRUCT(FParameters, )
   ...
   SHADER_PARAMETER_RDG_UNIFORM_BUFFER(FSubstrateGlobalUniformParameters, Substrate)
   ...
  END_SHADER_PARAMETER_STRUCT()
```

Expand code  Copy full snippet(11 lines long)

C++

Shader Parameter Binding

```
|  |  |
| --- | --- |
|  | FMyGlobasShaderCS::FParameters PassParameters; |
|  | PassParameters.Substrate = Substrate::BindSubstrateGlobalUniformParameters(View); |
```

FMyGlobasShaderCS::FParameters PassParameters;
PassParameters.Substrate = Substrate::BindSubstrateGlobalUniformParameters(View);

Copy full snippet(2 lines long)

  In the shader, both Blendable and Adaptive GBuffer formats need to be handled.

A better abstraction is planned for a future release to ease maintenance.

C++

```
#if SUBSTRATE_LOAD_FROM_MATERIALCONTAINER
// For Adaptive GBuffer
FSubstrateAddressing Addressing = GetSubstratePixelDataByteOffset(PixelPos, uint2(View.BufferSizeAndInvSize.xy), Substrate.MaxBytesPerPixel);
FSubstratePixelHeader Header = UnpackSubstrateHeaderIn(Substrate.MaterialTextureArray, Addressing, Substrate.TopLayerTexture);
#else
// For Blendable GBuffer
FSubstrateGBufferBSDF Data = SubstrateReadGBufferBSDF(GetScreenSpaceDataUint(PixelPos));
#endif
```

Expand code  Copy full snippet(22 lines long)

## Material Shader

In a material shader, if the material has its **Front Material** input plugged in, `TEMPLATE_USES_SUBSTRATE==1` will be defined, and the closure data can be processed and retrieved like this:

C++

```
// Initialise a Substrate header with normal in registers
FSubstrateData SubstrateData = PixelMaterialInputs.GetFrontSubstrateData();
FSubstratePixelHeader Header = MaterialParameters.GetFrontSubstrateHeader();
Header.IrradianceAO.MaterialAO = GetMaterialAmbientOcclusion(PixelMaterialInputs);

if (Header.SubstrateTree.BSDFCount > 0)
{
   FSubstrateIntegrationSettings Settings = InitSubstrateIntegrationSettings(false, true, 0, false);
   float3 TotalTransmittancePreCoverage = 0;
   Header.SubstrateUpdateTree(SubstrateData, V, Settings, TotalCoverage, TotalTransmittancePreCoverage);
```

Expand code  Copy full snippet(23 lines long)

For materials not using Substrate nodes, such as the legacy root node inputs, TEMPLATE\_USES\_SUBSTRATE==0 will be defined and the data can be retrieved as usual like this:

C++

```
|  |  |
| --- | --- |
|  | float3 BaseColor = GetMaterialBaseColor(PixelMaterialInputs); |
|  | float Metallic = GetMaterialMetallic(PixelMaterialInputs); |
|  | ... |
```

float3 BaseColor = GetMaterialBaseColor(PixelMaterialInputs);
float Metallic = GetMaterialMetallic(PixelMaterialInputs);
...

Copy full snippet(3 lines long)

## Material Properties

Once a BSDFContext has been retrieved (see code above), you can access the closure data like this:

C++

```
|  |  |
| --- | --- |
|  | SLAB_DIFFUSEALBEDO(BSDFContext.BSDF) |
|  | SLAB_F0(BSDFContext.BSDF); |
|  | SLAB_ROUGHNESS(BSDFContext.BSDF) |
```

SLAB\_DIFFUSEALBEDO(BSDFContext.BSDF)
SLAB\_F0(BSDFContext.BSDF);
SLAB\_ROUGHNESS(BSDFContext.BSDF)

Copy full snippet(3 lines long)

## Lighting Evaluation

For evaluating a particular light with **deferred lighting**, the following function can be used, located in `Substrate\SubstrateDeferredLighting.ush`:

C++

```
FSubstrateDeferredLighting SubstrateDeferredLighting(...)
```

FSubstrateDeferredLighting SubstrateDeferredLighting(...)

Copy full snippet(1 line long)

For evaluating the entire lighting in **forward rendering**, the following function can be used located in `Substrate\SubstrateForwardLighting.ush`:

C++

```
float3 SubstrateForwardLighting(...)
```

float3 SubstrateForwardLighting(...)

Copy full snippet(1 line long)

Additionally, two useful functions for evaluation respectively analytical lights and environment lighting, located in `Substrate/SubstrateEvaluation.ush`:

C++

```
|  |  |
| --- | --- |
|  | // Analytical lighting |
|  | FSubstrateEvaluateResult SubstrateEvaluateBSDFCommon(...); |
|  |  |
|  | // Environment lighting |
|  | FSubstrateEnvLightResult SubstrateEvaluateForEnvLight(...); |
```

// Analytical lighting
FSubstrateEvaluateResult SubstrateEvaluateBSDFCommon(...);
// Environment lighting
FSubstrateEnvLightResult SubstrateEvaluateForEnvLight(...);

Copy full snippet(5 lines long)

## Shader Files

Here is a list of commonly used shader files:

The current shader API is subject to change in future releases.

| Shader Files | Description |
| --- | --- |
| `Substrate/Substrate.ush` | Contains Substrate’s core data structs, data accessors, as well as data reading for Adaptive GBuffer. |
| `Substrate/SubstrateRead.ush` | Contains reading / unpacking logic for Blendable GBuffer data. |
| `Substrate/SubstrateEvaluation.ush` | Contains main shading evaluation logic for analytical light and environment light. |
| `Substrate/SubstrateDeferredLighting.ush` | Contains shading evaluation for the deferred lighting path. |
| `Substrate/SubstrateForwardLighting.ush` | Contains the shading evaluation for forward lighting path. |

## Additional Resources

* Technical presentation of Substrate: [Siggraph 2023 - Unreal Engine Substrate: Authoring Materials That Matter](https://advances.realtimerendering.com/s2023/2023%20Siggraph%20-%20Substrate.pdf)
* Authoring presentation of Substrate: Unreal Fest 2025 Stockholm - Everything You Wanted to Know About Substrate

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Scene Texture Data](/documentation/en-us/unreal-engine/programming-with-substrate-gbuffer-formats?application_version=5.7#scenetexturedata)
* [Global Shader](/documentation/en-us/unreal-engine/programming-with-substrate-gbuffer-formats?application_version=5.7#globalshader)
* [Material Shader](/documentation/en-us/unreal-engine/programming-with-substrate-gbuffer-formats?application_version=5.7#materialshader)
* [Material Properties](/documentation/en-us/unreal-engine/programming-with-substrate-gbuffer-formats?application_version=5.7#materialproperties)
* [Lighting Evaluation](/documentation/en-us/unreal-engine/programming-with-substrate-gbuffer-formats?application_version=5.7#lightingevaluation)
* [Shader Files](/documentation/en-us/unreal-engine/programming-with-substrate-gbuffer-formats?application_version=5.7#shaderfiles)
* [Additional Resources](/documentation/en-us/unreal-engine/programming-with-substrate-gbuffer-formats?application_version=5.7#additionalresources)
