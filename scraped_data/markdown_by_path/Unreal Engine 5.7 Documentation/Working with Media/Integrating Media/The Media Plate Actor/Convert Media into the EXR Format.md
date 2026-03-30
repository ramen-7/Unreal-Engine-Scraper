<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/convert-media-into-the-exr-format-with-the-process-exr-tool-in-unreal-engine?application_version=5.7 -->

# Convert Media into the EXR Format

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
5. [Working with Media](/documentation/en-us/unreal-engine/working-with-media-in-unreal-engine "Working with Media")
6. [Integrating Media](/documentation/en-us/unreal-engine/integrating-media-in-unreal-engine "Integrating Media")
7. [The Media Plate Actor](/documentation/en-us/unreal-engine/the-media-plate-actor-in-unreal-engine "The Media Plate Actor")
8. Convert Media into the EXR Format

# Convert Media into the EXR Format

Use the Process EXR tool to convert media into the EXR format

![Convert Media into the EXR Format](https://dev.epicgames.com/community/api/documentation/image/cb194009-1dc3-43e5-a1aa-20ebbbadbd17?resizing_type=fill&width=1920&height=335)

 On this page

![The Process EXR window](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9fdeaa1a-44b7-415f-9d6c-c2a4697d558a/process-exr-window.png)

Unreal Engine supports EXR tiles and mips for EXR videos and sequences. When you use the [Media Plate Actor](/documentation/404) to play your EXR sequences, the Actor's sphere and plane meshes automatically optimize performance by only streaming the tiles visible to the camera at any given time and picking the appropriate mip level for those tiles. This technique is compatible with clustered rendering, so the more PCs you have for a given display volume, the better the per-PC performance improvements are.

You can convert existing latlong 360 videos and 2D plates into the EXR format, by using the Process EXR tool. The tool divides EXR images into sub-divisions of tiles with mips in them.

To convert media source to the Unreal Engine EXR format:

* Go to **Content Browser** > **ImgMedia** > **Process EXR**. This opens the Process EXR window, where you configure your `.exr` files.

If you want to convert your media outside of Unreal Engine, you can use the offline tool oiiotool. If you want to use the tool, you must disable compression. The following command line is an example for converting your media:
`oiiotool source.exr --ch R,G,B --compression none --tile 256 256 -otex result.exr`

## The Process EXR Window

The Process EXR window has the following options for you to configure:

### Sequence

| Property | Description |
| --- | --- |
| Input Path | Source folder for the files you want to convert into the EXR format. |
| Output Path | Destination folder you want to store the converted `.exr` files in. |
| Enable Mip Mapping | Enable the computation and processing of the EXR tile mipmap chain. Enabled by default. |

### Tiles

| Property | Description |
| --- | --- |
| Enable Tiling | Enables tile splitting where you can determine the grid subdivision. Enabled by default.  When you are setting the numbers of tiles and mips, there's a potential trade off: if you have too many tiny tiles, your calculation cost increases. If your tiles are too large, your streaming cost increases. The default value is 256. |
| Tile Size X | The size of each tile along the X-axis. |
| Tile Size Y | The size of each tile along the Y-axis. |
| Num Tiles X | The amount of tiles on the X-axis. |
| Num Tiles Y | The amount of tiles on the Y-axis. |

### Processing

| Property | Description |
| --- | --- |
| Num Threads | Specify the number of concurrent process threads to be used in your system. |
| Use Player | Use the Player for decoding. This is capped to 1 image per frame. |

This is a faster option for large images. For smaller images, the cap makes it a slower option.

 |

### Debug

| Property | Description |
| --- | --- |
| Enable Mip Level Tint | Bake mipmap coloring into the `.exr` file, to use for debugging purposes. |
| Mip Level Tints | Select the tints you want to bake into your mips. |

* [exr media](https://dev.epicgames.com/community/search?query=exr%20media)
* [convert images to exr](https://dev.epicgames.com/community/search?query=convert%20images%20to%20exr)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [The Process EXR Window](/documentation/en-us/unreal-engine/convert-media-into-the-exr-format-with-the-process-exr-tool-in-unreal-engine?application_version=5.7#theprocessexrwindow)
* [Sequence](/documentation/en-us/unreal-engine/convert-media-into-the-exr-format-with-the-process-exr-tool-in-unreal-engine?application_version=5.7#sequence)
* [Tiles](/documentation/en-us/unreal-engine/convert-media-into-the-exr-format-with-the-process-exr-tool-in-unreal-engine?application_version=5.7#tiles)
* [Processing](/documentation/en-us/unreal-engine/convert-media-into-the-exr-format-with-the-process-exr-tool-in-unreal-engine?application_version=5.7#processing)
* [Debug](/documentation/en-us/unreal-engine/convert-media-into-the-exr-format-with-the-process-exr-tool-in-unreal-engine?application_version=5.7#debug)
