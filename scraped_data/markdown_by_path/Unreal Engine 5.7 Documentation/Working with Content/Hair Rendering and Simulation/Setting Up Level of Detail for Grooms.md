<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-level-of-detail-for-grooms-in-unreal-engine?application_version=5.7 -->

# Setting Up Level of Detail for Grooms

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
7. Setting Up Level of Detail for Grooms

# Setting Up Level of Detail for Grooms

Learn how you can set up and manage level of detail groups for your grooms.

On this page

Like many other types of geometry in Unreal Engine, it's just as important to set up levels of detail (LOD) for your grooms. Simplifying your grooms the farther they are from the camera decreases their rendering cost while improving performance.

You can set up and manage LODs for your groom in the [Groom Asset Editor](/documentation/en-us/unreal-engine/groom-asset-editor-user-guide-in-unreal-engine) from the **LOD** panel. This is where you can define how the various hair groups behave according to their screen coverage.

![Groom Asset Editor LOD Panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/272953d9-12c5-4ff1-8807-dccc0a9184ea/groom-editor-lod-panel.png)

1. Current LOD visualization stats
2. LOD Mode
3. Manual Decimation and Screen Size Properties

## Setting Up Level of Detail

At the top of the **LOD** panel, you can select the **LOD Mode** you want to use for this groom. This mode affects how the strand geometry handles switching between levels of detail.

Choose one of the following options:

![Groom LOD Mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/186077db-a85b-458e-bd65-081353d2e07f/groom-lod-mode.png)

* **Default:** Uses the LOD mode defined in the project settings.
* **Auto:** Automatically adapts the number of curves of the strands based on the groom's screen size, meaning there is no need to create manual LOD entries. This overrides the default LOD mode.
* **Manual:** Adapts the number of curves and points of strand geometry based on information in the LOD entries. This overrides the default LOD mode.

You can use **Auto LOD Bias** to increase the distance at which the groom starts to reduce the number of curves. This can be useful when the automatic curve reduction is too visible.

For each colored hair group, you can create up to 8 LOD entries. Each LOD entry primarily defines the screen size at which it becomes active, the type of geometry used, the type of binding to use, and more. You can add additional LODs to each group by clicking on the **Add (+)** next to the first group in the LOD panel.

![Add a LOD to the groom.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ee123757-c92f-4859-b449-05cbe6a77b69/groom-add-lod.png)

For each hair group, you can decide which type of geometry to use:

* **Strands:** Uses strand geometry and supports skinning, RBF, and simulation.
* **Cards:** Uses card (or flat sheets) geometry and supports skinning, RBF, and simulation.
* **Meshes:** Uses mesh geometry, such as a hair helmet. Only RBF is supported.

To learn more about setting up cards and mesh geometry, see [Setting up Cards and Meshes for Grooms](/documentation/en-us/unreal-engine/setting-up-cards-and-meshes-for-grooms-in-unreal-engine).

These are examples of each geometry type on a MetaHuman character created in [MetaHuman Creator](https://www.unrealengine.com/metahuman).

|  |  |  |
| --- | --- | --- |
| Strands Geometry | Cards Geometry | Hair Helmet Mesh |
| Strands | Cards | Mesh |

When specifying a geometry type, the settings change to reflect the selected type. Strands include its own decimation settings, while cards and meshes only use screen size.

|  |  |
| --- | --- |
| Strands LOD Settings | Cards and Meshes LOD Settings |
| Strands LOD Settings | Cards and Meshes LOD Settings |

When you set the **LOD Mode** to **Manual**, the hair group settings for decimation and screen size become editable for any of the three groom geometry types. The topmost portion of the panel, under the colored hair group ID, is the number of **Curves** and **Points** this LOD group has.

![LOD number of curves and points](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4ac0885c-073a-4ea7-a7f3-f9b883f5cd2f/groom-lod-curves-points.png)

## Visualizing Groom LODs

In the Groom Asset Editor preview window, you can visualize the level of detail automatically or by specifying a particular level when using the **LOD** selection menu.

![Viewport LOD Visualization Selection](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3a3c526a-4358-4993-935d-e3bb3bd245be/groom-lod-visualizer.png)

When set to **LOD Auto**, LODs switch between levels automatically based on their screen size. Alternatively, you can use the dropdown to view the available levels of detail regardless of screen size.

The following stats for each LOD type displays its:

* Geometry type
* LOD Index
* Screen Size
* Number of curves
* Number of points
* Hair thickness scale

![Groom LOD Stats](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6099aaf9-821e-4e00-a3f0-3822019fcfb6/groom-lod-stats.png)

Examples of LOD stats for Strands, Cards, and Meshes geometries.

## Groom Asset Editor LOD Properties

The following properties are available in the **LOD** panel:

| Property | Description |
| --- | --- |
| **LOD Mode** | Defines how LOD adapts curves and points for strand geometry. **Auto** adapts the curve count based on screen coverage. **Manual** uses the discrete LOD created for each group. |
| **Auto LOD Bias** | When Auto LOD is selected, it decreases the screen size at which the curve's reduction occurs. |
| Hair Groups |  |
| **Curve Decimation** | Reduces the number of hair strands in a uniform manner. |
| **Vertex Decimation** | Reduces the number of points for each hair strand. |
| **Angular Threshold** | Max angular difference between adjacent vertices to remove vertices during simplification, in degrees. |
| **Screen Size** | Screen size at which this LOD should be enabled. |
| **Thickness Scale** | Scales the hair strands radius. This can only be used for manually compensating the reduction of curves. |
| **Visible** | Defines whether this hair group's LODs are visible. |
| **Geometry Type** | Defines the type of geometry used by this LOD: Strands, Cards, or Meshes. |
| **Binding Type** | Defines the type of attachment:   * **Rigid:** When attached to a skeletal mesh, the groom uses the provided attachment name on the groom component. * **Skinning:** When attached to a skeletal mesh, the groom is deformed by the skeletal mesh's skinned surface. |
| **Simulation** | Sets whether this groom simulates physics interactions. This overrides the global **Simulation Enable** settings in the **Physics** panel of the Groom Asset Editor. |
| **RBF Interpolation** | Sets whether this groom uses RBF Interpolation. This overrides the global **RBF Interpolation** setting in the **Interpolation** panel of the Groom Asset Editor. |

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [physics](https://dev.epicgames.com/community/search?query=physics)
* [hair](https://dev.epicgames.com/community/search?query=hair)
* [metahumans](https://dev.epicgames.com/community/search?query=metahumans)
* [grooms](https://dev.epicgames.com/community/search?query=grooms)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Setting Up Level of Detail](/documentation/en-us/unreal-engine/setting-up-level-of-detail-for-grooms-in-unreal-engine?application_version=5.7#settinguplevelofdetail)
* [Visualizing Groom LODs](/documentation/en-us/unreal-engine/setting-up-level-of-detail-for-grooms-in-unreal-engine?application_version=5.7#visualizinggroomlods)
* [Groom Asset Editor LOD Properties](/documentation/en-us/unreal-engine/setting-up-level-of-detail-for-grooms-in-unreal-engine?application_version=5.7#groomasseteditorlodproperties)
