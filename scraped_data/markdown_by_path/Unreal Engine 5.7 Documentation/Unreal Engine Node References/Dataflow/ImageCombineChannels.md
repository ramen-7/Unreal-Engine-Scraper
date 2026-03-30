<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/ImageCombineChannels?application_version=5.7 -->

# ImageCombineChannels

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
7. ImageCombineChannels

# ImageCombineChannels

ImageCombineChannels (v1)

On this page

### Description

ImageCombineChannels (v1)

Combine channels into a single RGBA image
Outputs are single channel images

Input(s) :
Red - Red channel - if not connected, use black color
Green - Green channel - if not connected, use black color
Blue - Blue channel - if not connected, use black color
Alpha - Alpha channel - if not connected, use black color

Output(s):
Image - Output image recombined from input channels

### Information

|  |  |
| --- | --- |
| Module | [DataflowCore](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore) |
| Category | Image |
| Type | [FDataflowImageCombineChannelsNode](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImageCombineChannelsNod-) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| ResolutionOptions | resolution option | [EDataflowImageCombineResolutionOption](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/EDataflowImageCombineResolutionO-) | Highest |
| Resolution | resolution of the output image if the resolution option is set to user defined | [EDataflowImageResolution](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/EDataflowImageResolution) | Resolution512 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Red | Red channel - if not connected, use black color | [FDataflowImage](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) | () |
| Green | Green channel - if not connected, use black color | [FDataflowImage](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) | () |
| Blue | Blue channel - if not connected, use black color | [FDataflowImage](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) | () |
| Alpha | Alpha channel - if not connected, use black color | [FDataflowImage](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Image | Output image recombined from input channels | [FDataflowImage](/documentation/en-us/unreal-engine/API/Runtime/DataflowCore/FDataflowImage) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/ImageCombineChannels?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/ImageCombineChannels?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/ImageCombineChannels?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ImageCombineChannels?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/ImageCombineChannels?application_version=5.7#outputs)
