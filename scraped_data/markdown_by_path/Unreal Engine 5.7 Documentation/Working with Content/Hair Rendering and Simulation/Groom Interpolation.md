<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/groom-interpolation-in-unreal-engine?application_version=5.7 -->

# Groom Interpolation

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
7. Groom Interpolation

# Groom Interpolation

Define how a groom's curves should move with respect to skinned meshes and phyics simulation.

![Groom Interpolation](https://dev.epicgames.com/community/api/documentation/image/bbab7cb4-ab90-4eb7-84b1-05b44b6f43d1?resizing_type=fill&width=1920&height=335)

 On this page

Groom **Interpolation** settings define how the groom curves should move with respect to skinning and physics simulation. Depending on the skinning deformation and length of curves, you may need different settings.

![Groom Interpolation Properties Panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b69b1a4f-d519-4512-aa19-9c7ce26463d4/groom-interpolation.png)

## Visualizing Guide Influences

You can visualize the guides' influences in the Groom Asset Editor and within a level:

|  |  |
| --- | --- |
| Groom Asset Editor Guides Visualization Options | Level Editor Groom Guides Visualization Options |
| Groom Asset Editor Guides Visualization | Level Editor Groom Guides Visualization |

* From the Groom Asset Editor, use the **Show** menu to select **Guides** or **Strands Guides Influences**.
* From a Level, use the **View Modes** menu to select **Groom > Guides** or **Groom > Strands Guides Influences**.

The example below shows the rendering strands and the guides and how the guides influence each rendering strand.

|  |  |
| --- | --- |
| Groom Rendering Strands | Groom Guides |
| Rendering Strands | Guides |

For look or performance reasons, you can use the setting **Use Unique Guide** to reduce the cost of hair interpolation.

## Global Interpolation

The global interpolation option preserves the original groom shape under large skeletal mesh deformations and simulation. The underlying system uses **Radial Basis Function** (RBF) to preserve the original groom's positions despite the deformation. A set of samples is placed on the skinned mesh, and the differences are used between the rest. Skinned positions and the current deformed positions are used to compute the corrective values. This implies that global deformation only works when a groom is bound to a skeletal mesh and skinning is used for deformation (See the **LOD** panel in the **Groom Asset Editor**).

You can visualize the RBF samples of a groom placed in a level by selecting **Lit > Groom > Root Bindings**. Hover over the deformed RBF check box in the viewport.

![Groom Root Binding Visualization](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fb6b2ca1-1b3e-42d1-9d2e-13b7f9ba4c0f/groom-root-bindings-vis.png)

In the **LOD** panel of the Groom Asset Editor, each LOD can opt in or out of **RBF Interpolation**, allowing a high degree of flexibility.

![Groom Interpolation LOD Group](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/463842d8-3581-451d-8502-f868cf29723d/groom-lod-group.png)

## Groom Asset Editor Interpolation Properties

The **Interpolation** panel modifies some of the properties set during the initial import of the groom.

![Groom Asset Editor Interpolation Properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c47b3cd3-a392-4cd8-88c0-1665b404071f/groom-interpolation-properties.png)

| Property | Description |
| --- | --- |
| Hair Group |  |
| **Curve Decimation** | Decimates the groom by reducing the number of strands. The removed strands are chosen randomly from the groom's imported strands. |
| **Vertex Decimation** | Decimates the groom by removing vertices on strands. |
| **Guide Type** | Define which guides are used:   * **Imported:** Uses imported guides. * **Generated:** Generates guides from strands. * **Rigged:** generates rigged guides from strands. |
| **Hair to Guide Density** | Defines the ratio of strands used as guides. |
| **Rigged guide num. curves** | Number of guides that are generated on the groom and the skeletal mesh. |
| **Rigged guide num points** | Number of points / bones allotted per guide. |
| **Interpolation Quality** | Defines the quality of the interpolation when interpolating guides motions onto the strands. For short hair, we recommend using Low settings, as it is faster to compute and has a lower impact on the final quality. For medium-length and long hair, it is beneficial to use the High setting for better deformation.   * **Low:** Build interpolation data based on nearest neighbor search. This results in lower-quality interpolation data but is fast to build. This setting takes only several minutes to complete. * **Medium:** Build interpolation data using curve shape matching search but within a limited spatial range. This option is a tradeoff between Low and High quality settings in terms of quality and build time. This setting can take several dozen minutes to complete. * **High:** Build interpolation data using curve shape matching search. This results in high-quality interpolation data, but is relatively slow to build. This option setting can take several dozen minutes to complete. |
| **Interpolation Distance** | Defines the metric used for pairing guides and strands together. Choose from the following:   * **Parametric:** Build interpolation data based on curve parametric distance. * **Root:** Build interpolation data based on the distance between a guide's root and strand's root. * **Index:** Build interpolation data based on a guide's and strand's vertex indices. * **Distance:** Build interpolation data based on curve euclidean distance. |
| **Randomize Guide** | When enabled, the guides used for interpolation are slightly randomized to break up clumps that can happen. |
| **User Unique Guide** | When enabled, a single guide is used for motion interpolation |
| Hair Interpolation |  |
| **RBF Interpolation** | When enabled, the Radial Bias Function (RBF) is used for interpolation instead of the local skin rigid transform. This value is used for all levels of detail (LOD) whose RBF interpolation property is set to **Auto**. |
| **RBF Type** | Select the type of interpolation to use when the groom is bound to a skeletal mesh:   * **Rigid Transform:** Only the translation of the root closest skin triangle is used during interpolation. * **Offset Transform:** Only the translation of the root closest skin triangle is used during interpolation. * **Smooth Transform:** The translation of the root's closest skin triangle and a smooth rotation computed from the guides are used during interpolation. * The translation of the root's closest triangle is used for smooth rotation computed from the guides being used during interpolation. * **No Skinning:** No skinning will occur. |
| **Enable Guide-Cache Support** | Enable guide-cache support to allow this groom to attach a simulation cache dynamically at runtime. |
| **Hair Interpolation Type** | Select the type of interpolation to use when the groom is bound to a skeletal mesh:   * **Rigid Transform:** Only the translation of the root closest skin triangle is used during interpolation. * **Offset Transform:** Only the translation of the root closest skin triangle is used during interpolation. * **Smooth Transform:** The translation of the root's closest skin triangle and a smooth rotation computed from the guides are used during interpolation. * The translation of the root's closest triangle is used for smooth rotation computed from the guides being used during interpolation. * **No Skinning:** No skinning will occur. |

## Groom Asset Editor LOD Interpolation Properties

The **LOD** panel contains the following properties that relate to groom interpolation:

![Groom Asset Editor LOD Interpolation Properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7fef78dd-9090-4987-8da9-493b4ce03b24/groom-interpolation-lod-properties.png)

| Property | Description |
| --- | --- |
| **RBF Interpolation** | Sets the global interpolation mode to represent this level of detail. This selection overrides the default RBF interpolation value set in the [Interpolation](/documentation/en-us/unreal-engine/groom-interpolation-in-unreal-engine#groomasseteditorinterpolationsettings) panel. The following options are available:   * **Auto:** Uses the set global value. * **Enable:** Force enables RBF interpolation. * **Disable:** Force disables RBF interpolation. |

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [physics](https://dev.epicgames.com/community/search?query=physics)
* [hair](https://dev.epicgames.com/community/search?query=hair)
* [metahumans](https://dev.epicgames.com/community/search?query=metahumans)
* [grooms](https://dev.epicgames.com/community/search?query=grooms)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Visualizing Guide Influences](/documentation/en-us/unreal-engine/groom-interpolation-in-unreal-engine?application_version=5.7#visualizingguideinfluences)
* [Global Interpolation](/documentation/en-us/unreal-engine/groom-interpolation-in-unreal-engine?application_version=5.7#globalinterpolation)
* [Groom Asset Editor Interpolation Properties](/documentation/en-us/unreal-engine/groom-interpolation-in-unreal-engine?application_version=5.7#groomasseteditorinterpolationproperties)
* [Groom Asset Editor LOD Interpolation Properties](/documentation/en-us/unreal-engine/groom-interpolation-in-unreal-engine?application_version=5.7#groomasseteditorlodinterpolationproperties)
