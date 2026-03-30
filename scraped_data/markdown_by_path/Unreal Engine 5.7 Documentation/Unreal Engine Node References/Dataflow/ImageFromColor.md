<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ImageFromColor?application_version=5.7 -->

# ImageFromColor

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
5. [Unreal Engine Node References](/documentation/en-us/unreal-engine/node-reference "Unreal Engine Node References")
6. [Dataflow](/documentation/en-us/unreal-engine/node-reference/Dataflow "Dataflow")
7. ImageFromColor

# ImageFromColor

ImageFromColor (v1)

On this page

### Description

ImageFromColor (v1)

Create a RGBA image from a single color at a specific resolution
Outputs are single channel images

Input(s) :
FillColor - color to fill the image with
Resolution - resolution of the output image

Output(s):
Image - Output image

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Image |
| Type | [FDataflowImageFromColorNode](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImageFromColorNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| FillColor | color to fill the image with | [FLinearColor](/documentation/en-us/unreal-engine/API/Runtime/Core/FLinearColor) | (R=0.000000,G=0.000000,B=0.000000,A=1.000000) |
| Resolution | resolution of the output image | [EDataflowImageResolution](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/EDataflowImageResolution) | Resolution16 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Image | Output image | [FDataflowImage](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/ImageFromColor?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/ImageFromColor?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ImageFromColor?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ImageFromColor?application_version=5.7#outputs)
