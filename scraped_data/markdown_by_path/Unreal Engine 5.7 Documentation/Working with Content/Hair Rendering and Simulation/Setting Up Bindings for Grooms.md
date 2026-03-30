<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-bindings-for-grooms-in-unreal-engine?application_version=5.7 -->

# Setting Up Bindings for Grooms

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
7. Setting Up Bindings for Grooms

# Setting Up Bindings for Grooms

Learn how to bind groom components to skeletal meshes.

![Setting Up Bindings for Grooms](https://dev.epicgames.com/community/api/documentation/image/4cede464-b3c5-47ed-84cc-02c75434640c?resizing_type=fill&width=1920&height=335)

 On this page

**Groom Binding** assets are used to attach and skin a Groom component to a Skeletal Mesh component. No binding is needed if a groom asset only needs to be “rigidly” attached to a skeletal mesh.

## Creating a Binding Asset

To create a Binding asset:

1. Locate a **Groom** asset in the **Content Browser**.
2. Right-click on the groom and select **Create Binding** from the context menu.
3. In the **Groom Binding Options** dialog window, set the following:

   ![Groom Binding Options](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0c45470c-d312-46b8-bdfc-32fcf0df4987/groom-binding-options-example.png)
   * Set **Groom Binding Type** to **Skeletal Mesh** or **Geometry Cache** to bind the groom to.

     Selecting **Geometry Cache** as the Groom Binding Type requires the **Geometry Cache** plugin to be enabled.
   * Set **Target Skeletal Mesh / Target Geometry Cache** to select which skeletal mesh or geometry cache asset this groom should be bound to. You must select a skeletal mesh or geometry cache to create a binding asset.

### Advanced Options for Creating a Binding Asset

The Groom Binding Options dialog contains some advanced options you can use when creating a binding asset:

* Use **Num Interpolation Points** to define the number of samples used for the hair global interpolation, which is optionally enabled within the Groom Asset Editor under the **Interpolation** panel with the setting **RBF Interpolation** under the **Hair Interpolation** section. Global interpolation preserves the original groom shape under large skeletal mesh deformations. Using more samples means more accurate deformation but also implies additional cost. In general, a 100 samples or less should be good enough.
* **Source Skeletal Mesh** optionally defines the mesh on which the groom was authored on. The mesh could be different from the Target Skeletal Mesh assigned, and the topology could also be different. The system assumes both the Source and Target meshes share the same UV mapping to transfer the hair curves and positions. The **Matching Section** constrains the transfer to use only a particular mesh section.

## Setup

To use a groom binding asset to bind a groom to a skinned mesh:

1. Create a **Groom** component and make it a child component of a skeletal mesh. You can do this directly on a Skeletal Mesh in a level or in a Blueprint.

   |  |  |
   | --- | --- |
   | A Groom component on a level actor. | A groom component in a Blueprint. |
   | A Groom component on a level actor. | A Groom component in a Blueprint. |
2. With the **Groom** component selected, perform the following actions in the **Details** panel:

   * Assign a groom asset to the **Groom Asset** assignment slot.
   * Assign a groom binding asset to the **Binding Asset** assignment slot.

Your groom should look attached similarly to how the one pictured below is:

![Groom Attached to a Skeletal Mesh](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fa874164-20a8-4b89-bd05-88ef37d9cc79/groom-skel-mesh.png)


The binding data is only used if the current level of detail (LOD) **Binding Type** is set to **Skinning**. This can be set up separately for each LOD in the [Groom Asset Editor](/documentation/en-us/unreal-engine/groom-asset-editor-user-guide-in-unreal-engine) under the **LOD** panel settings. You can verify the current active binding type in the level by selecting **Lit > Instances** in the viewport menus and visualizing the Binding Type for each.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/11885894-865e-44de-96b6-2984e608439d/groom-instances-stats.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/11885894-865e-44de-96b6-2984e608439d/groom-instances-stats.png)

Click image for full size.

## Previewing Groom Bindings in Groom Asset Editor

The **Binding** panel in the Groom Asset Editor is where you'll manage any binding asset assigned to this groom. It lists all the groom binding assets compatible with the current groom asset.

![Previewing Groom Bindings in the Groom Asset Editor.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e8e50c27-e542-47b3-a79f-beb05012fdf5/groom-preview-bindings.png)

You can use the **Eye** icon below the binding asset assignment slot to preview the binding asset within the preview window.

![Groom Binding Visibility Toggle.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/39bb87e6-dea9-41d1-8bf2-14a35b17d386/groom-binding-visibility.png)

You can use the animation assignment slot above the preview window to select an available animation to preview the hair deformation for the current groom. Use the play and stop buttons to start and stop the animation in the preview window.

![Groom Binding Preview with Animation](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/61fa8876-9a56-4d61-97ba-f1bb22fcd84c/groom-binding-animation.png)

You can visualize a groom's **Root** data in a level by selecting **Lit > Groom > Root Bindings**. The root binding data for each rendered strand is shown by a colored white line at the root of the hair, along with the corresponding triangle on which the root is bound.

![Groom Root Bindings Visualization](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/65b8810d-8a67-43b2-bab6-0d811102e434/groom-root-bindings-vis.png)

## Groom Binding Properties

### Groom Binding Options Properties

The following properties are found in the Groom Binding Options dialog when creating a groom binding asset:

![Groom Binding Options](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ed545bb1-f266-449b-a4af-343addaf66d7/groom-binding-options.png)

| Property | Description |
| --- | --- |
| Build Settings |  |
| **Groom Binding Type** | Select the type of mesh to create a groom binding for: **Skeletal Mesh** or **Geometry Cache**. |
| **Target Skeletal Mesh / Target Geometry Cache** | Select the Skeletal Mesh / Geometry Cache asset on which this groom is attached to. |
| Hair Interpolation Points |  |
| **Num Interpolation Points** | The number of points used for the RBF interpolation. |
| Conversion |  |
| **Source Skeletal Mesh / Source Geometry Cache** | The Skeletal Mesh / Geometry Cache on which the groom has been authored. This is optional and used only if the hair binding is done on a different mesh than the one which it has been authored. For instance, only if the curve's roots and the surface geometry don't align and need to be wrapped / transformed. |
| **Matching Section** | Section to pick to transfer the position. |

### Groom Binding Asset Editor Properties

The following properties are found in the Groom Asset Editor when opening a groom asset:

| Property | Description |
| --- | --- |
| Build Settings |  |
| **Groom Binding Type** | Select the type of mesh to create a groom binding for: **Skeletal Mesh** or **Geometry Cache**. |
| **Groom** | The groom this binding asset uses. |
| **Source Skeletal Mesh / Source Geometry Cache** | The Skeletal Mesh / Geometry Cache on which the groom has been authored. This is optional and used only if the hair binding is done on a different mesh than the one which it has been authored. For instance, only if the curve's roots and the surface geometry don't align and need to be wrapped / transformed. |
| **Target Skeletal Mesh / Target Geometry Cache** | Select the Skeletal Mesh / Geometry Cache asset on which this groom is attached to. |
| **Num Interpolation Points** | The number of points used for the radial bias function (RBF) interpolation. |
| **Matching Section** | Section to pick to transfer the position. |
| Hair Groups |  |
| **Curve Count** | Number of curves this hair group has. |
| **Curve LOD** | Number of curve LOD this hair group has. |
| **Guide Count** | Number of guides this hair group has. |
| **Guide LOD** | Number of guide LODs this hair group has. |

### Groom Asset Editor Binding Properties

The following properties are found in the **Groom Asset Editor** under the **LOD** panel:

![Groom Asset Editor Binding Properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c887c499-f698-49e2-95b8-b4e4feed7873/groom-asset-editor-binding-properties.png)

| Property | Description |
| --- | --- |
| Groom |  |
| **Binding Type** | Sets the groom simulation mode to represent this level of detail. Each level of detail group can choose between the following binding types:   * **Rigid:** The hair follows the provided attachment name of a skeletal mesh. * **Skinning:** The hair follows a skin surface of a skeletal mesh. |

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [physics](https://dev.epicgames.com/community/search?query=physics)
* [hair](https://dev.epicgames.com/community/search?query=hair)
* [metahumans](https://dev.epicgames.com/community/search?query=metahumans)
* [grooms](https://dev.epicgames.com/community/search?query=grooms)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Creating a Binding Asset](/documentation/en-us/unreal-engine/setting-up-bindings-for-grooms-in-unreal-engine?application_version=5.7#creatingabindingasset)
* [Advanced Options for Creating a Binding Asset](/documentation/en-us/unreal-engine/setting-up-bindings-for-grooms-in-unreal-engine?application_version=5.7#advancedoptionsforcreatingabindingasset)
* [Setup](/documentation/en-us/unreal-engine/setting-up-bindings-for-grooms-in-unreal-engine?application_version=5.7#setup)
* [Previewing Groom Bindings in Groom Asset Editor](/documentation/en-us/unreal-engine/setting-up-bindings-for-grooms-in-unreal-engine?application_version=5.7#previewinggroombindingsingroomasseteditor)
* [Groom Binding Properties](/documentation/en-us/unreal-engine/setting-up-bindings-for-grooms-in-unreal-engine?application_version=5.7#groombindingproperties)
* [Groom Binding Options Properties](/documentation/en-us/unreal-engine/setting-up-bindings-for-grooms-in-unreal-engine?application_version=5.7#groombindingoptionsproperties)
* [Groom Binding Asset Editor Properties](/documentation/en-us/unreal-engine/setting-up-bindings-for-grooms-in-unreal-engine?application_version=5.7#groombindingasseteditorproperties)
* [Groom Asset Editor Binding Properties](/documentation/en-us/unreal-engine/setting-up-bindings-for-grooms-in-unreal-engine?application_version=5.7#groomasseteditorbindingproperties)
