<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-blueprint-brushes-in-unreal-engine?application_version=5.7 -->

# Landscape Blueprint Brushes

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
7. [Editing Landscapes](/documentation/en-us/unreal-engine/editing-landscapes-in-unreal-engine "Editing Landscapes")
8. [Landscape Sculpt Mode](/documentation/en-us/unreal-engine/landscape-sculpt-mode-in-unreal-engine "Landscape Sculpt Mode")
9. Landscape Blueprint Brushes

# Landscape Blueprint Brushes

Brushes that enable you to create and manipulate arbitrary terrain regions using shapes defined entirely in Blueprint.

![Landscape Blueprint Brushes](https://dev.epicgames.com/community/api/documentation/image/f14c2a68-3969-4279-897c-57be47ad95a9?resizing_type=fill&width=1920&height=335)

 On this page

Landscape Blueprint Brushes provde a stack of user-defined sculting brushes that can be manipulated non-destructively, so that any changes to a brush lower in the stack automatically flow through to the brushes above it in the stack. These brushes can be used to layer multiple terrain manipulations on top of one another while maintaining separation of those manipulations, enabling them to be reordered or moved around the terrain as necessary.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5ac9223e-7c15-42dc-93cd-450f190c1932/non_destructive.gif)


To use Landscape Blueprint Brushes, you must enable the Landmass plugin in the Plugins Browser and check **Enable Edit Layers** when creating your Landscape.

**To enable the Landmass plugin in the Plugins Browser:**

1. From the main menu, open the Plugins Browser.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/aec5d395-a72e-40fe-9d67-2762c243ad7a/pluginsbrowser.png)
2. Search for *Landmass* and click **Enable**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c2f86840-64f0-4eaa-9c8c-89f0a846faae/landmassplugin_enabled.png)

**To enable Edit Layers when creating your Landscape:**

* Check the **Enable Edit Layers** property in the **New Landscape** section.

  ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/baf883ee-2e8a-467f-b49c-470fadfea33a/enableeditlayers.png)

## Adding Landscape Blueprint Brushes to Edit Layers

**To add a new Landscape Blueprint Brush to an existing Edit Layer:**

1. With the Landsape mode selected in the Level Editor Toolbar, select the Sculpt tab and select **Blueprint** from the available sculting tools.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e522338e-64ae-4042-90a4-befb0da3e42c/selectblueprinttool.png)
2. Click the **Blueprint Brush** dropdown and select one of the available types of brushes.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2dac5423-5f61-4c13-80fc-81f5f26a64df/blueprintbrushselect.png)
3. In the viewport, click the Landscape to add the new brush.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7915dc45-3744-4850-81bd-952bec0adf56/newbrush.png)

## Built-In Landscape Blueprint Brush Types

### CustomBrush\_Landmass Brush

The CustomBursh\_Landmass brush generates a landmass shape from a user-defined spline shape and a collection of configurable effects—such as erosion, curl noise, and displacement—and applies the resulting shape to the terrain

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e9ff73ba-4476-42b8-8ef3-afb132004d77/falloff_angle_45.png)

#### Blend Modes

The Blend Mode determines how the shape is added to, or cut into, the terrain—similar to CSG or boolean operations. There are four blend modes available:

| Blend Mode | Description |
| --- | --- |
| Alpha Blend | Raises and lowers the terrain by generating both a regular and inverted version of the landmass shape and applying the inverted shape to the portion that is located below the underlying terrain [undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a7cda7b7-4caa-4d73-b745-f56ac608872f/blend_alpha.png) |
| Min | Lowers the terrain by generating an inverted version of the landmass shape and applying only the portion that is located below the underlying terrain. [undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d7f5b7ce-de3a-44b7-8e62-e331f8c62797/blend_min.png) |
| Max | Raises the terrain by applying only the portion of the landmass shape that is located above the underlying terrain. [undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0b2b12dc-6f23-45cf-8514-d11df16715c3/blend_max.png) |
| Additive | [undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/974d2d79-5569-42c5-8e1b-7ab93807d54d/blend_additive.png) |

#### Shape Capping

The shape generated by a Landmass brush can either be capped or uncapped. If the shape is capped, it resembles a plateau with a flat top. An uncapped shape resembles a mountain or hill with a peak.

|  |  |
| --- | --- |
| Cap Shape enabled | Cap Shape disabled |
| Cap Shape enabled | Cap Shape disabled |

#### Falloff

Falloff determines the slope of the transition from the brush shape to the underlying terrain.

| Property | Description |
| --- | --- |
| Angle | [See below](/documentation/en-us/unreal-engine/landscape-blueprint-brushes-in-unreal-engine#angle) |
| Width | [See below](/documentation/en-us/unreal-engine/landscape-blueprint-brushes-in-unreal-engine#width) |

##### Angle

The falloff slope is determined by a specified angle. Larger falloff angles result in steeper slopes. For uncapped shapes, the falloff continues inside the shape as well to form a peak.

|  |  |  |
| --- | --- | --- |
|  |  |  |
| 30 degrees | 45 degrees | 60 degrees |

###### Width

The falloff slope is determined by specifying a distance in Unreal Units. Smaller falloff distances result in steeper slopes.

|  |  |  |
| --- | --- | --- |
|  |  |  |
| 100 units | 200 units | 400 units |

#### Noise

Noise applies up to two octaves of curl noise to the generated landmass shape.

| Property | Description |
| --- | --- |
| Curl [1/2] Strength | [See below](/documentation/en-us/unreal-engine/landscape-blueprint-brushes-in-unreal-engine#curlstrength) |
| Curl [1/2] Tiling | [See below](/documentation/en-us/unreal-engine/landscape-blueprint-brushes-in-unreal-engine#curltiling) |

##### Curl Strength

Sets the amplitude of the noise applied to the landmass shape.

|  |  |  |
| --- | --- | --- |
|  |  |  |
| Strength 0 | Strength 1 | Strength 2 |

##### Curl Tiling

Sets the frequency of the noise applied to the landmass shape.

|  |  |  |
| --- | --- | --- |
|  |  |  |
| Tiling 0 | Tiling 5 | Tiling 15 |

### CustomBrush\_LandmassRiver Brush

The CustomBrush\_LandmassRiver brush extrudes a Static Mesh along a user-defined spline and raises or lowers the terrain to match the extruded mesh. This brush is useful for laying out roads or rivers where the terrain automatically adjusts to match up.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a1707eb7-2e53-45c9-b5fb-efb11086c8a7/landmass_river.png)

### CustomBrush\_MaterialOnly Brush

The CustomBrush\_MaterialOnly brush uses a Material to apply procedural noise to the whole terrain to form a base.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8a6ee65f-ab6d-4de8-96c9-79151e378d17/materialonly_noise.png)

* [landscape](https://dev.epicgames.com/community/search?query=landscape)
* [sculpting](https://dev.epicgames.com/community/search?query=sculpting)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Adding Landscape Blueprint Brushes to Edit Layers](/documentation/en-us/unreal-engine/landscape-blueprint-brushes-in-unreal-engine?application_version=5.7#addinglandscapeblueprintbrushestoeditlayers)
* [Built-In Landscape Blueprint Brush Types](/documentation/en-us/unreal-engine/landscape-blueprint-brushes-in-unreal-engine?application_version=5.7#built-inlandscapeblueprintbrushtypes)
* [CustomBrush\_Landmass Brush](/documentation/en-us/unreal-engine/landscape-blueprint-brushes-in-unreal-engine?application_version=5.7#custombrush-landmassbrush)
* [Blend Modes](/documentation/en-us/unreal-engine/landscape-blueprint-brushes-in-unreal-engine?application_version=5.7#blendmodes)
* [Shape Capping](/documentation/en-us/unreal-engine/landscape-blueprint-brushes-in-unreal-engine?application_version=5.7#shapecapping)
* [Falloff](/documentation/en-us/unreal-engine/landscape-blueprint-brushes-in-unreal-engine?application_version=5.7#falloff)
* [Angle](/documentation/en-us/unreal-engine/landscape-blueprint-brushes-in-unreal-engine?application_version=5.7#angle)
* [Width](/documentation/en-us/unreal-engine/landscape-blueprint-brushes-in-unreal-engine?application_version=5.7#width)
* [Noise](/documentation/en-us/unreal-engine/landscape-blueprint-brushes-in-unreal-engine?application_version=5.7#noise)
* [Curl Strength](/documentation/en-us/unreal-engine/landscape-blueprint-brushes-in-unreal-engine?application_version=5.7#curlstrength)
* [Curl Tiling](/documentation/en-us/unreal-engine/landscape-blueprint-brushes-in-unreal-engine?application_version=5.7#curltiling)
* [CustomBrush\_LandmassRiver Brush](/documentation/en-us/unreal-engine/landscape-blueprint-brushes-in-unreal-engine?application_version=5.7#custombrush-landmassriverbrush)
* [CustomBrush\_MaterialOnly Brush](/documentation/en-us/unreal-engine/landscape-blueprint-brushes-in-unreal-engine?application_version=5.7#custombrush-materialonlybrush)
