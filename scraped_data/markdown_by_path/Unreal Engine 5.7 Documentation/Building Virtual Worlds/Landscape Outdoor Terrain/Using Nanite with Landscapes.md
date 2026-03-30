<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-nanite-with-landscapes-in-unreal-engine?application_version=5.7 -->

# Using Nanite with Landscapes

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
5. [Building Virtual Worlds](/documentation/en-us/unreal-engine/building-virtual-worlds-in-unreal-engine "Building Virtual Worlds")
6. [Landscape Outdoor Terrain](/documentation/en-us/unreal-engine/landscape-outdoor-terrain-in-unreal-engine "Landscape Outdoor Terrain")
7. Using Nanite with Landscapes

# Using Nanite with Landscapes

An overview of how to use Nanite virtualized geometry with the Landscape system.

![Using Nanite with Landscapes](https://dev.epicgames.com/community/api/documentation/image/890d73ed-81c4-4e9a-8583-89d1847f10e3?resizing_type=fill&width=1920&height=335)

 On this page

Nanite is Unreal Engine's virtualized geometry system. Nanite uses an internal mesh format and rendering technology to render pixel scale detail and high object counts. Nanite's compressed data format provides support for high detail meshes and fine-grained streaming with automatic level of detail.

You can use Nanite on your Landscape to improve performance with Nanite rendering, especially with regard to Virtual Shadow Maps. In-editor performance while the non-Nanite Landscape is in use is not representative of the runtime performance of the Nanite-enabled Landscape in your project until Nanite meshes are fully rebuilt. End users of your product should expect no visual improvement or downgrade since the source data is identical.

For more information on Nanite and its advantages, see [Nanite Virtualized Geometry](designing-visuals-rendering-and-graphics/rendering-optimization/nanite).

Sometimes, parts of your landscape may use standard rendering, or Nanite meshes might not be fully updated. This is expected behavior. To make such issues disappear, save or cook your project.

## Technical Considerations

Nanite Landscapes stream on top of the existing Landscape data streaming since both Nanite and non-Nanite data are necessary at runtime. Non-Nanite Landscape data is required for Runtime Virtual Textures, water rendering, and more.

This means twice the amount of data is streamed. One set of data for Nanite streaming and another set for texture streaming. Enabling Nanite causes both sets of data to reside in memory.

Hierarchical Level of Detail (HLOD) and Landscape proxy streaming behaves identically to non-Nanite Landscapes.

## Enable Nanite on a Landscape

To use Nanite with your Landscape terrain, follow these steps:

1. Select your Landscape in the viewport.
2. In the **Details** panel, check the box next to **Enable Nanite**.

[![The Enable Nanite checkbox in the Details panel for a Landscape.](https://dev.epicgames.com/community/api/documentation/image/1ced085c-401e-4a8c-889e-32e67a7ffcb0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1ced085c-401e-4a8c-889e-32e67a7ffcb0?resizing_type=fit)

## Build Nanite Mesh on a Landscape

After you've enabled Nanite on a Landscape, you can build the Nanite mesh representation from Landscape data in any of the following ways:

* In the Landscape's **Details** panel, go to the **Nanite** section, and click **B****uild Data**.

  + If **Build Data** is disabled, you can click **Rebuild Data**. The **Build Data** button is disabled when the Nanite landscape mesh is up to date and currently being rendered in the viewport.
* In the **Build** menu, select **Build Landscape**.

The build time for the Landscape depends on the size of the Landscape and the number of tiles. When complete, you can view the Nanite geometry using the Nanite visualization modes.

If the viewport shows a warning message that says **Nanite meshes need to be rebuilt**, then the Nanite landscape is not up to date (for example, after a sculpt operation).

[![The rebuild warning message in the viewport](https://dev.epicgames.com/community/api/documentation/image/f16dd31f-6865-457a-a351-4a8af2bcd625?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f16dd31f-6865-457a-a351-4a8af2bcd625?resizing_type=fit)

The uncollapsed rebuild warning message in the viewport

[![The collapsed nofication message in the viewport](https://dev.epicgames.com/community/api/documentation/image/24172d6d-8be2-4732-8597-3f6f69d27e9b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/24172d6d-8be2-4732-8597-3f6f69d27e9b?resizing_type=fit)

The collapsed rebuild warning message in the viewport

When you rebuild the Nanite data or save the Landscape proxy mesh, the message disappears.

When Nanite landscape data is out of date, the editor will not render the landscape using Nanite, but the game will build the out-of-date landscape at cook time. This can negatively impact cook times, so keep landscape actors up to date and regularly save updated proxies.

## Nanite Skirts

Nanite Landscape relies on standard Nanite techniques for LODs and vertex decimation. The resulting mesh won't use a regular grid topology unless the camera gets very close to it, but will contain more vertices where necessary to retain shape. Because of this, the borders between Landscape Proxy Actors have vertices that might not be evenly distributed on each side of the border. At large distances this can introduce seam artifacts, which appear as tiny holes through the landscape. These are usually small enough to be corrected by temporal anti-aliasing.

You can use the Nanite Skirt enable option to avoid seams.This functionality expands the Nanite landscape mesh by an additional row/column of vertices at the edges of the mesh and move those new vertices down by an amount specified by the **Nanite Skirt Depth**:

[![Enable Nanite Skirt](https://dev.epicgames.com/community/api/documentation/image/7a8ca065-dccc-462c-b2fe-c6a2ea22f0cf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7a8ca065-dccc-462c-b2fe-c6a2ea22f0cf?resizing_type=fit)

Enable the Nanite Skirt option on your Landscape in the Details panel.

This causes neighboring Nanite Landscape meshes to criss-cross each other and prevent seam artifacts from appearing.

## Nanite Tessellation

Like other Nanite static meshes, the landscape material can specify a displacement, which allows Nanite tessellation to work on the landscape. See [Nanite Tessellation](https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine?application_version=5.5#nanite-tessellation) for more information.

Nanite tessellation only works if the Nanite data is up to date, which means that one or more of the landscape proxies has been sculpted since the last time Nanite data was built for it. If a landscape proxy mesh is not up to date, then the tessellation effect will not be visible on that specific proxy in the editor, though it will be visible in the final build. To see the tessellation effect in the editor, rebuild the Nanite data or save the Landscape proxy mesh.

## Useful Console Commands

The following console variables are useful when you're working with Nanite-enabled Landscapes:

| Console Command | Description |
| --- | --- |
| **Landscape.RenderNanite** | Enables Nanite rendering for Landscapes.  The default value is 1. |
| **Landscape.Nanite.LiveRebuildOnModification** | Triggers a rebuild of the Nanite representation whenever a modification is performed.  This function is Experimental.  The default value is 0. |
| **Landscape.Nanite.MultithreadedBuild** | Enables rebuilding of Nanite-enabled Landscape meshes using multiple processor threads to improve performance when working with several Landscape components.  The default value is 1. |

When you're editing Nanite-enabled Landscapes, we recommend that you keep the live rebuilding of Nanite meshes toggled off (`Landscape.LiveRebuildNaniteOnModification 0`), as this might decrease performance significantly. Landscape rendering relies on non-Nanite Landscapes until the Nanite mesh is rebuilt and up-to-date. Unreal Engine uses that version for rendering until it is fully rebuilt, so the editing experience is identical to working with non-Nanite Landscape actors.

* [landscape](https://dev.epicgames.com/community/search?query=landscape)
* [building virtual worlds](https://dev.epicgames.com/community/search?query=building%20virtual%20worlds)
* [open world](https://dev.epicgames.com/community/search?query=open%20world)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Technical Considerations](/documentation/en-us/unreal-engine/using-nanite-with-landscapes-in-unreal-engine?application_version=5.7#technical-considerations)
* [Enable Nanite on a Landscape](/documentation/en-us/unreal-engine/using-nanite-with-landscapes-in-unreal-engine?application_version=5.7#enable-nanite-on-a-landscape)
* [Build Nanite Mesh on a Landscape](/documentation/en-us/unreal-engine/using-nanite-with-landscapes-in-unreal-engine?application_version=5.7#buildnanitemeshonalandscape)
* [Nanite Skirts](/documentation/en-us/unreal-engine/using-nanite-with-landscapes-in-unreal-engine?application_version=5.7#nanite-skirts)
* [Nanite Tessellation](/documentation/en-us/unreal-engine/using-nanite-with-landscapes-in-unreal-engine?application_version=5.7#nanitetessellation)
* [Useful Console Commands](/documentation/en-us/unreal-engine/using-nanite-with-landscapes-in-unreal-engine?application_version=5.7#useful-console-commands)
