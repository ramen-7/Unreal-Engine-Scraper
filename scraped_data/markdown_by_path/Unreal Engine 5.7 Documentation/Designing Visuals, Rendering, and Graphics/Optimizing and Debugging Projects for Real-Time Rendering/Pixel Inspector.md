<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/pixel-inspector-in-unreal-engine?application_version=5.7 -->

# Pixel Inspector

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
6. [Optimizing and Debugging Projects for Real-Time Rendering](/documentation/en-us/unreal-engine/optimizing-and-debugging-projects-for-realtime-rendering-in-unreal-engine "Optimizing and Debugging Projects for Real-Time Rendering")
7. Pixel Inspector

# Pixel Inspector

The Pixel Inspector shows you what is happening in the various parts of the Geometry Buffer at a given pixel.

![Pixel Inspector](https://dev.epicgames.com/community/api/documentation/image/eb7fd3b3-c709-48d1-9d07-bc8ceb0897ff?resizing_type=fill&width=1920&height=335)

 On this page

The **Pixel Inspector** tool is a Developer Tool that
will allow you to diagnose the pixels that make up the colors in your
scene. If you want to know why a pixel is producing an unexpected color
(or maybe what Material input is driving a pixel's color), you can use
the Pixel Inspector's **Inspect Mode** to output information that is driving the pixel's visual result.

## Using the Pixel Inspector

To enable and use the Pixel Inspector:

1. From the Main Editor Window go to the **Tools** menu option under **Debug** and select **Pixel Inspector**.

   [![Pixel Inspector under Debug in the Tools menu.](https://dev.epicgames.com/community/api/documentation/image/871defc2-9f40-4cd3-abe1-b899b585a98d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/871defc2-9f40-4cd3-abe1-b899b585a98d?resizing_type=fit)

   The Pixel Inspector Window will open.

   [![Pixel Inspector window](https://dev.epicgames.com/community/api/documentation/image/bcd7d47a-6b6c-4e03-96aa-d1bae36face7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bcd7d47a-6b6c-4e03-96aa-d1bae36face7?resizing_type=fit)
2. Click the **Search** (magnifying glass) button to start pixel inspection.
3. Move the mouse over any viewport (Level, Material, Blueprint, or other) to populate the Pixel Inspector data fields in realtime.

   [![Using the Pixel Inspector](https://dev.epicgames.com/community/api/documentation/image/c39fb988-f09f-4282-9060-756764647d41?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c39fb988-f09f-4282-9060-756764647d41?resizing_type=fit)
4. Press Escape to stop inspection and populate the Pixel Inspector data fields with the last inspected pixel.

## Pixel Inspector Data Reference

Below are the data fields that will become populated with a pixel's information during inspection:

| Option | Description |
| --- | --- |
| Viewport ID | Displays the ID of which viewport the Pixel Inspector is drawing from. |
| Coordinate | Displays the X/Y coordinates from the current inspection (can be manually set). |
| Final Color |  |
| --- | --- |
| Context Colors | Displays the Context Colors associated with the current inspection. |
| Final Color | Final RGBA 8bits Color after tone mapping (default value is black). |
| Scene Color |  |
| --- | --- |
| Scene Color | The RGB Scene Color applied from the current inspection. |
| Pre-Exposure | Defines the upper bounds for the brightness range of the generated histogram. It remaps the range of SceneColor around camera exposure, limiting the render target required to support HDR lighting values.  You must enable the Project Setting **Apply Pre-Exposure before writing to the scene** color under **Rendering** for this value to become available. |
| HDR |  |
| --- | --- |
| Luminance | HDR Luminance value for current inspection. |
| HDR Color | The HDR RGB Color value being applied. |
| GBuffer A |  |
| --- | --- |
| Normal | The Normal applied from the GBufferA channel. |
| Per Object GBuffer Data | The amount of per object data from the GBufferA Channel. |
| GBuffer B |  |
| --- | --- |
| Metallic | The Metallic value applied from the GBufferB R Channel. |
| Specular | The Specular value applied from the GBufferB G Channel. |
| Roughness | The amount of Roughness applied from the GBufferB B Channel. |
| Material Shading Model | The shading model from the GBufferB A Channel encoded with Selective Output Mask. |
| Selective Output Mask | The value for the Selective Output Mask from the GBufferB A Channel encoded with Shading Model. |
| GBuffer C |  |
| --- | --- |
| Base Color | The base color value applied from the GBufferC RGB Channels. |
| Indirect Irradiance | The value of Indirect Irradiance from the GBufferC A Channel encoded with Ambient Occlusion (AO). |
| Ambient Occlusion | The value of AO from the GBufferC A Channel encoded with Indirect Irradiance.  See [Using GBuffer Properties](https://dev.epicgames.com/documentation/en-us/unreal-engine/post-process-materials-in-unreal-engine#using-g-buffer-properties) and [Buffer Visualization](https://dev.epicgames.com/documentation/en-us/unreal-engine/viewport-modes-in-unreal-engine#buffer-visualization) for more information on GBuffers.  Defines the upper bounds for the brightness range of the generated histogram. It remaps the range of SceneColor around camera exposure, limiting the render target required to support HDR lighting values.  You must enable the Project Setting **Apply Pre-Exposure before writing to the scene** color under **Rendering** for this value to become available. |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Using the Pixel Inspector](/documentation/en-us/unreal-engine/pixel-inspector-in-unreal-engine?application_version=5.7#usingthepixelinspector)
* [Pixel Inspector Data Reference](/documentation/en-us/unreal-engine/pixel-inspector-in-unreal-engine?application_version=5.7#pixelinspectordatareference)
