<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/local-fog-volumes-in-unreal-engine?application_version=5.7 -->

# Local Fog Volumes

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
6. [Lighting the Environment](/documentation/en-us/unreal-engine/lighting-the-environment-in-unreal-engine "Lighting the Environment")
7. [Environmental Light with Fog, Clouds, Sky and Atmosphere](/documentation/en-us/unreal-engine/environmental-light-with-fog-clouds-sky-and-atmosphere-in-unreal-engine "Environmental Light with Fog, Clouds, Sky and Atmosphere")
8. Local Fog Volumes

# Local Fog Volumes

An overview of locally placed volumes to create height-based fog effects.

![Local Fog Volumes](https://dev.epicgames.com/community/api/documentation/image/95532b93-97d3-4954-a888-f09c462e775a?resizing_type=fill&width=1920&height=335)

 On this page

After applying [Sky Atmosphere](https://dev.epicgames.com/documentation/en-us/unreal-engine/sky-atmosphere-component-in-unreal-engine) or [Exponential Height Fog](https://dev.epicgames.com/documentation/en-us/unreal-engine/exponential-height-fog-in-unreal-engine) to a world, you can add local variations to the fog using **Local Fog Volumes**. A local fog volume is a placeable actor containing a spherical area of fog that fades out radially.

![A scene with placed local fog volumes with | atmosphere and height fog.](https://dev.epicgames.com/community/api/documentation/image/24e7786b-b513-41c4-beb3-603c42f68206?resizing_type=fit&width=1920&height=1080)

![A scene using only atmosphere and height fog.](https://dev.epicgames.com/community/api/documentation/image/e500f7ee-0a26-4a2d-a7f2-11ec0eb887e1?resizing_type=fit&width=1920&height=1080)

A scene with placed local fog volumes with | atmosphere and height fog.

A scene using only atmosphere and height fog.

[Volumetric Fog](https://dev.epicgames.com/documentation/en-us/unreal-engine/volumetric-fog-in-unreal-engine) can also be used to create local variation in fog, using meshes and materials instead of local fog volumes. Volumetric fog provides shadowing and lighting effects, as well as different shapes of fog, but it requires a higher performance cost and does not work on some low-end platforms. Local fog volumes work across low-end and high-end platforms with multiple scalability levels, and provide consistent visuals with other fog and lighting systems. You can also use both features together. The following table compares the two features.

| Local Fog Volumes | Volumetric Fog |
| --- | --- |
| Sphere shape, radial falloff | Any mesh shape, any fallout shape |
| Visible at any distance, voxelised when close to the camera | Visible only in a set range, voxelised anywhere in that range |
| No volumetric shadowing and lighting | Volumetric shadowing and lighting |
| Works on all platforms | Does not work on all platforms |

The order of composition when using local fog volumes with other volumetric elements is:

1. Sky Atmosphere Aerial Perspective
2. Exponential Height Fog
3. Other Local Fog Volumes
4. Volumetric Fog (when enabled)

## Using Local Fog Volumes

You can place local fog volumes anywhere in your game world. It is a sphere of participating media representing a mixture of exponential height fog combined with a radially faded out fog. Each local fog volume can be independently translated, rotated, and uniformly scaled to fit your scene.

You can add a local fog volume to your scene using the **Create** menu from the **Visual Effects** category, or you can use the **Place Actors** panel.

*A local fog volume is added to the scene and scaled, translated, and rotated. Non-uniform scaling is not supported.*

### Using Local Fog Volumes with Volumetric Fog

You can use local fog volumes with [Volumetric Fog](building-virtual-worlds\lighting-and-shadows\environmental-lighting\volumetric-fog), which provides volumetric shadowing and lighting within these volumes but at a higher performance cost.

To use volumetric fog with local fog volumes, check the box for the **Volumetric Fog** property in the **Exponential Height Fog** details panel. Below is an example scene with and without volumetric fog enabled.

|  |  |
| --- | --- |
| [Local fog volume only](https://dev.epicgames.com/community/api/documentation/image/f6654d62-16b6-414a-b7a2-bcfd7a1ec713?resizing_type=fit) | [Local fog volume with volumetric fog enabled.](https://dev.epicgames.com/community/api/documentation/image/35a9da1c-9fda-45cf-881e-0de526d275de?resizing_type=fit) |
| Local Fog Volume only | Local Fog Volume with Volumetric Fog enabled |

## Local Fog Volume Properties and Project Settings

Local Fog Volumes contain the following properties:

[![Local Fog Volume Details Panel Settings](https://dev.epicgames.com/community/api/documentation/image/82c52a9d-2861-4b27-83ed-4704dd37f8ab?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/82c52a9d-2861-4b27-83ed-4704dd37f8ab?resizing_type=fit)

| Property | Description |
| --- | --- |
| Radial Fog Distribution |  |
| **Radial Fog Density** | The density of the radial fog represents its coefficient at the center of the sphere. The final look of the volume is determined by combining the “Coverage = 1 - Transmittance” of both radial and height fog in order to achieve both soft edges and height fog. |
| Height Fog Distribution |  |
| --- | --- |
| **Height Fog Density** | The density of radial fog represents its extinction coefficient at height 0 in the unit sphere. The final look of the volume is determined by combining the “Coverage = 1 - Transmittance” of both radial and height fog in order to achieve both soft edges and height fog. |
| **Height Fog Falloff** | Controls how the density decreases as height increases. Smaller values make the visible transition larger. 1.0 is the lowest value before visual artifacts are visible at the horizon. |
| **Height Fog Offset** | Height offset relative to the actor’s Z position. |
| Shading |  |
| --- | --- |
| **Scattering Distribution** | Controls the phase “G” parameter, describing the scattering within this fog volume. |
| **Fog Albedo** | Sets the albedo color of this fog volume. The albedo is the base color before any lighting has been applied. |
| **Fog Emissive** | Controls the emissive color of this fog volume. |
| Sorting |  |
| --- | --- |
| **Fog Sort Priority** | The priority can be used as a way to override the sorting by distance. A lower value means the volume is considered further away. For example, it will draw behind volumes with higher priorities.  This setting is not used when Volumetric Fog is enabled in the Exponential Height Fog settings. |

The Project Settings contains the following properties for local fog volumes found in the **Engine > Rendering** section:

[![Local Fog Volume project settings.](https://dev.epicgames.com/community/api/documentation/image/3c2ef9b0-7c6f-4631-aec7-5a75cb165521?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3c2ef9b0-7c6f-4631-aec7-5a75cb165521?resizing_type=fit)

| Project Setting | Description |
| --- | --- |
| Translucency |  |
| **Local Fog Volume Apply on Translucent** | Enables sampling of local fog volumes on translucent elements. |
| Optimizations |  |
| --- | --- |
| **Support Local Fog Volumes** | Local fog volumes components can be applied on translucent and opaque surfaces in Forward shading, so resources need to be bound to apply aerial perspective on transparent surfaces (and all surfaces on mobile via per vertex evaluations). Requires `r.SupportLocalFogVolumes` to be true. |

### Fog Shading

You can use the **Shading** properties to define the artistic look of fog with the albedo color, emissive color, and scattering distribution.

The **Fog Albedo** defines the color of the fog when interacting with light sources, such as the sun and sky. You can use the color picker to select a color for the fog.

|  |  |  |
| --- | --- | --- |
| [Albedo Color White](https://dev.epicgames.com/community/api/documentation/image/c37aefeb-3b2b-4d9d-bf00-204d6a485be1?resizing_type=fit) | [Albedo Color Green](https://dev.epicgames.com/community/api/documentation/image/82f66dac-7de2-469f-9baa-d6eb13cec640?resizing_type=fit) | [Albedo Color Brown](https://dev.epicgames.com/community/api/documentation/image/46844f80-eaf2-4d1a-b9f8-4689551ba52f?resizing_type=fit) |
| Albedo Color: White (Default) | Albedo Color: Green | Albedo Color: Brown |

The **Fog Emissive** defines the color of the light emitted by the fog. The emitted light follows the same density as the local fog volume. You can use the color picker to select an emissive color for the fog.

|  |  |  |
| --- | --- | --- |
| [No emissive applied](https://dev.epicgames.com/community/api/documentation/image/15b8888c-6e5b-4af0-b9fe-8629cf66ec93?resizing_type=fit) | [Emissive color green](https://dev.epicgames.com/community/api/documentation/image/1054e87e-ceb9-4cb8-8da3-a77be78f3089?resizing_type=fit) | [Emissive color red](https://dev.epicgames.com/community/api/documentation/image/d303621e-9725-4939-8f3c-629db80c434e?resizing_type=fit) |
| Emissive Color: None (Default) | Emissive Color: Green | Emissive Color: Red |

The **Scattering Distribution** controls how much the incoming light scatters in various directions. Zero scatters light equally in all directions while something closer to a value of 1 scatters predominantly in the direction of the light.

![Drag the slider to see Local Fog Scattering Distribution changes from low to high starting with 0, 0.25 , 0.5, 0.75, 0.98, and 0.99](https://dev.epicgames.com/community/api/documentation/image/19108324-8257-4e9f-95f4-0a0246a1e4ff?resizing_type=fit&width=1920&height=1080)![Drag the slider to see Local Fog Scattering Distribution changes from low to high starting with 0, 0.25 , 0.5, 0.75, 0.98, and 0.99](https://dev.epicgames.com/community/api/documentation/image/b7275ea8-3cd0-419a-b36a-c4515d899275?resizing_type=fit&width=1920&height=1080)![Drag the slider to see Local Fog Scattering Distribution changes from low to high starting with 0, 0.25 , 0.5, 0.75, 0.98, and 0.99](https://dev.epicgames.com/community/api/documentation/image/4baa516f-035d-4291-822f-ec6669e3c9df?resizing_type=fit&width=1920&height=1080)![Drag the slider to see Local Fog Scattering Distribution changes from low to high starting with 0, 0.25 , 0.5, 0.75, 0.98, and 0.99](https://dev.epicgames.com/community/api/documentation/image/e8f94f56-ad79-4dfa-89a9-2be6111f3f9b?resizing_type=fit&width=1920&height=1080)![Drag the slider to see Local Fog Scattering Distribution changes from low to high starting with 0, 0.25 , 0.5, 0.75, 0.98, and 0.99](https://dev.epicgames.com/community/api/documentation/image/85ee8d7f-9a56-4653-b386-025534928e01?resizing_type=fit&width=1920&height=1080)![Drag the slider to see Local Fog Scattering Distribution changes from low to high starting with 0, 0.25 , 0.5, 0.75, 0.98, and 0.99](https://dev.epicgames.com/community/api/documentation/image/bd1f84db-1129-4623-b90b-3477688b1051?resizing_type=fit&width=1920&height=1080)

**Drag the slider to see Local Fog Scattering Distribution changes from low to high starting with 0, 0.25 , 0.5, 0.75, 0.98, and 0.99**

To have volumetric fog light shafts, volumetric fog must be enabled and the scattering distribution needs to be closer to zero. The default scattering distribution of 0.2 is a good starting point.

### Fog Distribution

The distribution of fog controls how much light passes through the fog volume with properties for density, falloff, and height offset. These properties are similar to those found in the Exponential Height Fog component.

The **Radial Fog Density** and **Height Fog Density** control the look of the volume to achieve both soft edges and height fog.

[![Radial Fog and Height Fog Densities](https://dev.epicgames.com/community/api/documentation/image/0ecec9e2-4fc8-4d00-855e-5ae3e343ec21?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0ecec9e2-4fc8-4d00-855e-5ae3e343ec21?resizing_type=fit)

*Examples of local fog volumes. (Left to Right) Fog with radial density, fog with height density, and fog with a combination of radial and height densities.*

The phase function of a local fog volume controls the uniformity of the light within the volume. Shadows and light functions are ignored because the lighting is evaluated using fast analytical integrals.

The **Height Fog Falloff** controls how the density of the fog decreases as the height increases. Smaller values make larger visible transitions, whereas larger values have smaller transitions.

|  |  |  |
| --- | --- | --- |
| [Height Fog Falloff: 500](https://dev.epicgames.com/community/api/documentation/image/bd5bd83c-d912-4c35-8532-a249ab0210ee?resizing_type=fit) | [Height Fog Falloff: 1000](https://dev.epicgames.com/community/api/documentation/image/9f808549-60b1-4a10-b889-6d98470d04ff?resizing_type=fit) | [Height Fog Falloff: 2500](https://dev.epicgames.com/community/api/documentation/image/654eaa89-05d0-4eca-895a-ef9c274050a4?resizing_type=fit) |
| Height Fog Falloff: 500 | Height Fog Falloff: 1000 (Default) | Height Fog Falloff: 2500 |

The **Height Fog Offset** moves the center of the height fog relative to the actor’s Z (up) position within the local fog volume. Using a lower offset moves the fog down within the radial volume, whereas higher values move it vertically.

|  |  |  |
| --- | --- | --- |
| [Height Fog Offset: -0.12](https://dev.epicgames.com/community/api/documentation/image/65ab0b9d-26da-4207-ad63-95694a5014ab?resizing_type=fit) | [Height Fog Offset: 0](https://dev.epicgames.com/community/api/documentation/image/39f5e0c2-cf91-4a23-9f6c-049ba118c164?resizing_type=fit) | [Height Fog Offset: 0.12](https://dev.epicgames.com/community/api/documentation/image/92c0543b-cb0f-4dc2-ad07-7d4516e37015?resizing_type=fit) |
| Height Fog Offset: -0.12 | Height Fog Offset: 0 (Default) | Height Fog Offset: 0.12 |

### Fog Sort Priority

Local fog volumes are composited on screen according to the distance of their center to the camera view. This allows you to control their sort order by applying a priority for them when they happen to overlap. When volumetric fog is enabled in the exponential height fog settings, local fog volumes are voxelized into volumetric representation — local fog volumes are not sorted, instead they are voxelized as overlapping participating media. Lighting can also cause fog when shadow casting is enabled for volumetric fog.

Below are two examples showing overlapping local fog volumes without and with volumetric fog enabled.

|  |  |
| --- | --- |
| [Two local fog volumes with different color composited.](https://dev.epicgames.com/community/api/documentation/image/3669dd5a-8cf5-47c9-a642-563ba215cabb?resizing_type=fit) | [Two local fog volumes with different color composited with volumetric fog enabled.](https://dev.epicgames.com/community/api/documentation/image/437e42dc-3591-430a-9dbe-a06dc6b86617?resizing_type=fit) |
| Two local Fog Volumes of different color composited. | Two Local Fog Volumes with different color composited with Volumetric Fog enabled. |

Because volumetric fog is voxelized as participating media, and not sorted, it can result in visuals that look different. For example if the scattering distribution (Phase function) is different from that of the volumetric fog’s, the result could look different.

When volumetric fog is enabled, fog is voxelized to sort appropriately. However, when local fog volumes are used without volumetric fog, you can use the **Fog Sort Priority** setting to override sorting by distance. Lower values means the volume is considered farther away — the volume will draw behind others. Larger values will consider the volume closer to the camera and thus should render on top of others.

Because you can have multiple overlapping local fog volumes, sorting is useful when you want larger ambient local fog to always be behind smaller, more intense volumes. In these situations, local fog will always mix well when viewed close up, even without volumetric fog enabled, like in the example scene below.

|  |  |
| --- | --- |
| [Two overlapping local fog volumes viewed from ground level.](https://dev.epicgames.com/community/api/documentation/image/a018dd4e-dc5b-451e-859c-f3cf161b805a?resizing_type=fit) | [two overlapping local fog volumes viewed from above.](https://dev.epicgames.com/community/api/documentation/image/a7eae770-0462-4112-b1a0-5f64b03af5d1?resizing_type=fit) |
| Two overlapping local fog volumes viewed at ground level. | Two overlapping local fog volumes viewed from above. |

## Performance and Debugging

The following are some suggestions for improving performance and debugging content related to local fog volumes:

* Local fog volumes are culled using screen tiles — where the screen is divided into small squares called tiles — making their cost similar to dynamic lights added to the scene since their cost is related to the extent of the space on screen they use.

  + You can visualize the extent of the cost in screen space using the console command `r.LocalFogVolume.TileDebug`.

    - **1** shows the local fog volume count as a color per tile.
    - **2** shows the local fog volume count as a color per tile and the effect of the pixel discard/clipping.
* On lower-end hardware, a good practice to have is to limit multiple volumes from overlapping one another. This reduces the number of volumes to process per pixel when the camera is completely inside of them.

### Local Fog Volume Tile Debug

You can visualize local fog volumes culling per screen tile using the console command `r.LocalFogVolume.TileDebug`.

Use one of the following values:

* **1** shows the local fog volume count as a color per screen tile.
* **2** shows the local fog volume count as a color per screen tile and the effect of the pixel discard/clipping.

The examples in the scene below demonstrate multiple local fog volumes, some close together and some overlapping.

[![Local fog volume examples with overlapping for debugging purposes.](https://dev.epicgames.com/community/api/documentation/image/608813ad-e2e9-4b97-82e6-c7a9cd81ba25?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/608813ad-e2e9-4b97-82e6-c7a9cd81ba25?resizing_type=fit)

Below shows what the tile debug views look like when enabled using the example scene above.

|  |  |
| --- | --- |
| [Tile Debug View 1](https://dev.epicgames.com/community/api/documentation/image/8c9d3995-0e6c-4d4f-864d-2bf4aa7ab4a5?resizing_type=fit) | [Tile Debug View 2](https://dev.epicgames.com/community/api/documentation/image/458ebf58-eda8-4c56-842e-b44b83b9b7b5?resizing_type=fit) |
| r.LocalFogVolume.TileDebug 1 | r.LocalFogVolume.TileDebug 2 |

The tile debug views do not work when volumetric fog is enabled.

## Useful Console Variables

| Console Variable | Description | Default Value |
| --- | --- | --- |
| `r.LocalFogVolume.ApplyOnTranslucent` | Project settings enabling the sampling of local fog volumes on translucent elements. Set this to 1 in order to have local fog volumes applied on translucent meshes. | 0 |
| `r.LocalFogVolume.RenderIntoVolumetricFog` | Sets whether to voxelize local fog volumes into the volumetric fog rendering system. Otherwise, local fog volumes will remain isolated. This is enabled by default. | 1 |
| `r.LocalFogVolume.TilePixelSize` | The pixel size of tiles on screen at which point local fog volumes are culled. | 128 |
| `r.LocalFogVolume.TileMaxInstanceCount` | Maximum number of local fog volumes to account for per view (and per tile for consistency). | 32 |
| `r.LocalFogVolume.TileDebug` | Debug the tiled rendering data complexity. 0 is disabled. 1 shows per-tile LFV count as color. 2 shows the same as one but also shows the effect of pixel discard / clipping. | 0 |
| `r.LocalFogVolume.GlobalStartDistance` | Sets the start distance (in centimeters) from the camera in which local fog volumes start to appear. | 2000 |
| `r.LocalFogVolume.HalfResolution` | This renders local fog volumes at half resolution with upsampling to full resolution later on. This only works for mobile rendering paths, when enabled. | 0 |
| `r.LocalFogVolume.MaxDensityIntoVolumetricFog` | LocalFogVolume Height fog mode can become exponentially dense in the bottom part. Volumetric fog temporal reprojection then can leak due to high density. Clamping density is a way to get that visual artifact under control. | 0.01 |

* [environment](https://dev.epicgames.com/community/search?query=environment)
* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [lighting](https://dev.epicgames.com/community/search?query=lighting)
* [volume](https://dev.epicgames.com/community/search?query=volume)
* [fog](https://dev.epicgames.com/community/search?query=fog)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Using Local Fog Volumes](/documentation/en-us/unreal-engine/local-fog-volumes-in-unreal-engine?application_version=5.7#using-local-fog-volumes)
* [Using Local Fog Volumes with Volumetric Fog](/documentation/en-us/unreal-engine/local-fog-volumes-in-unreal-engine?application_version=5.7#using-local-fog-volumes-with-volumetric-fog)
* [Local Fog Volume Properties and Project Settings](/documentation/en-us/unreal-engine/local-fog-volumes-in-unreal-engine?application_version=5.7#local-fog-volume-properties-and-project-settings)
* [Fog Shading](/documentation/en-us/unreal-engine/local-fog-volumes-in-unreal-engine?application_version=5.7#fog-shading)
* [Fog Distribution](/documentation/en-us/unreal-engine/local-fog-volumes-in-unreal-engine?application_version=5.7#fog-distribution)
* [Fog Sort Priority](/documentation/en-us/unreal-engine/local-fog-volumes-in-unreal-engine?application_version=5.7#fog-sort-priority)
* [Performance and Debugging](/documentation/en-us/unreal-engine/local-fog-volumes-in-unreal-engine?application_version=5.7#performance-and-debugging)
* [Local Fog Volume Tile Debug](/documentation/en-us/unreal-engine/local-fog-volumes-in-unreal-engine?application_version=5.7#local-fog-volume-tile-debug)
* [Useful Console Variables](/documentation/en-us/unreal-engine/local-fog-volumes-in-unreal-engine?application_version=5.7#useful-console-variables)
