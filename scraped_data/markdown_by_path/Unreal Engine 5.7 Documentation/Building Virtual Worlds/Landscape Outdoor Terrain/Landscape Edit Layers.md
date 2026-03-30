<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-edit-layers-in-unreal-engine?application_version=5.7 -->

# Landscape Edit Layers

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
7. Landscape Edit Layers

# Landscape Edit Layers

Explains the Landscape Edit Layers system that enables non-destructive landscape editing workflows.

![Landscape Edit Layers](https://dev.epicgames.com/community/api/documentation/image/85ea9f57-15bf-46f6-8cc7-5ae1294e0a38?resizing_type=fill&width=1920&height=335)

 On this page

**Landscape Edit Layers** enable you to edit Landscape Heightmap and Weightmap data using non-destructive layers. Edit layers exist in a stack-based workflow and act as independent, non-destructive containers to separate editing data. Each layer represents a separate level of terrain information – such as height, paint, or visibility data that can be independently edited, reordered or hidden. This allows artists to experiment freely with terrain changes, combine procedural and manual edits, and integrate specialized deformation systems such as **Landscape Patches** and **Splines**, without permanently altering the underlying Landscape data.

Edit layers are automatically enabled while creating new landscapes.

[![Enable edit layers when creating a new landscape](https://dev.epicgames.com/community/api/documentation/image/c07ec336-4462-4d5d-8423-79d57fd9a6e8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c07ec336-4462-4d5d-8423-79d57fd9a6e8?resizing_type=fit)

Enable edit layers when creating a new landscape. Click image for full size.

## Adding Layers to Your Landscape

Instead of maintaining all landscape data from a single location you can now add multiple edit layers to separate data. These new layers function as a foundation for sculpting and painting a landscape, which allows you to manipulate and maintain landscapes more efficiently.

By default, you will always have one layer (Layer), which is the initial base layer. To add a new layer, select the **+ Icon** on the right side of the Layers property. A unique name is automatically generated. We recommend naming your layer with a meaningful name relevant to the type of data it holds. For example, a Landscape may have the following layer hierarchy: Base Layer, Sculpting Details, Paint Details, Splines Layer, Patch Layer. In this case the bulk of heightmap sculpting is stored in the Base Layer, with smaller sculpting details being stored in a separate Sculpting Details Layer. Storing Paint weightmap data in a separate layer also allows you to easily hide/show paint data while editing. To Rename an Edit Layer, **Right-Click** on the layer and select **Rename**.

The maximum number of edit layers added to Landscape actors can be configured in the Project Settings under **Landscape: Max Number of Layers**. By default, the editor sets a limit of **8** edit layers.

[![The layer context menu with create and rename highlighted](https://dev.epicgames.com/community/api/documentation/image/69da21eb-7856-4d12-9ce7-c3e3b6bca4f3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/69da21eb-7856-4d12-9ce7-c3e3b6bca4f3?resizing_type=fit)

The layer context menu with create and rename highlighted. Click image for full size.

## Managing Layers

There are several options for managing your layers, which include setting the layer’s lock status, visibility, and alpha.

### Toggling Lock Status

You can lock layers by selecting the **Lock icon**. The closed lock indicates the layer cannot be edited, and the open lock indicates the layer can be edited. Locked edit layers cannot be modified in any way. This includes actions like sculpting, painting, collapsing, and managing Blueprint brushes.

[![Locked layer message](https://dev.epicgames.com/community/api/documentation/image/c2c6fc8b-bfdf-44d6-bf2c-33684c85739f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c2c6fc8b-bfdf-44d6-bf2c-33684c85739f?resizing_type=fit)

Locked layer message. Click image for full size.

### Toggling Visibility

If you want to exclude a layer from blending, you can select the eye icon to **Hide** the layer.

[![Hidden and unhidden eye icons](https://dev.epicgames.com/community/api/documentation/image/941b33a6-73d6-473f-b626-154d95e56a2c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/941b33a6-73d6-473f-b626-154d95e56a2c?resizing_type=fit)

Hidden and unhidden eye icons. Click image for full size.

### Layer Alpha

You can change the blending for each layer by adding or subtracting from the **Alpha** value. The viewport displays changes to the values in real time.

Each layer has two Alpha values, one to control heightmap blending and the other to control paint layers blending.

In **Sculpt** mode, the alpha value represents the edit layer’s heightmap alpha. A negative heightmap alpha applies the data in a subtractive blend. A heightmap alpha of zero means the edit layer’s heightmap data has no effect on the final blended landscape heightmap.

In **Paint** mode, the alpha value represents the edit layer’s weightmap alpha. A weightmap alpha of zero means the weightmap information of the edit layer will have no effect on the final blended landscape weightmap.

[![Layer-4-with-alpha-set-at-zero-point-four-six](https://dev.epicgames.com/community/api/documentation/image/31d3d303-66d8-4886-93bb-5c48f5ddd434?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/31d3d303-66d8-4886-93bb-5c48f5ddd434?resizing_type=fit)

### Removing Layers

Edit layers can be removed using the **Trash** icon. All edit layer data including heightmap, weightmap, visibility, and Blueprint brushes will be deleted. All Landscapes are required to have at least one edit layer. To reset a landscape's data, add a new empty layer and delete the remaining edit layers.

### Edit Layer Inspector

Edit layer features have continued to increase over time. As a result, a new **Edit Layer inspector panel** has been added. Click the **Cog icon** next to the Trash button. A new details panel will open showing all configurable settings for the edit layer type. Plugins that define custom edit layer classes may expose specific UI functionality by overriding the [details customization](https://dev.epicgames.com/documentation/en-us/unreal-engine/details-panel-customizations-in-unreal-engine) class for the new edit layer.

[![Edit-layer-inspector-panel-with-tabs](https://dev.epicgames.com/community/api/documentation/image/56708f22-4735-4a3c-8b3b-8b6f5e2ab0ce?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/56708f22-4735-4a3c-8b3b-8b6f5e2ab0ce?resizing_type=fit)

## Editing Layers

There are several ways you can edit your layer, which include: ordering layers, adjusting the alpha layer blending, and using the Erase tool.

### Ordering Layers

You can drag and drop layers in any order. When you move layers, the order in which those layers display in the viewport changes.

[![Dragging and dropping a layer](https://dev.epicgames.com/community/api/documentation/image/f1235054-da23-4eb8-8893-9fa6859336ca?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f1235054-da23-4eb8-8893-9fa6859336ca?resizing_type=fit)

Dragging and dropping a layer. Click image for full size.

### Edit Layer Context Menu

Right-Click on a Landscape Edit Layer to reveal a context menu. The context menu provides options to manage and update existing layers.

[![Edit-layer-context-menu](https://dev.epicgames.com/community/api/documentation/image/52deddb8-b263-456a-a258-1fbdfcc455c4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/52deddb8-b263-456a-a258-1fbdfcc455c4?resizing_type=fit)

Options:

1. **Rename**: Rename the edit layer.
2. **Delete**: Delete the edit layer, including all of its data and Blueprint Brushes. Edit Layers above the deleted layer in the Edit Layer Stack slide down one position.
3. **Collapse**: Merge the edit layer into the layer below. Merges the final data of both layers into the bottom layer.
4. **Collapse All Layers**: Collapse all edit layers into the base edit layer. Destructive collapse, removing all Blueprint Brushes. Merged data of all layers is flattened into the base layer.
5. **Clear Sculpt Layer**: Available in Sculpt mode. Removes all heightmap data on the edit layer.
6. **Clear Visibility Layer**: Available in Sculpt - Visibility Mode. Removes all visibility data on the edit layer (Removes all Landscape holes).
7. **Clear All Target Layers**: Available in Paint mode. Removes all weightmap data on the edit layer.
8. **Hide Selected**: Disables visibility of selected edit layer.
9. **Show Only Selected**: Disables visibility of all edit layers besides selected layer.
10. **Show All Layers**: Enables visibility of all Layers.
11. **Assign Existing Brush**: Only available when an existing Blueprint brush actor is in the level hierarchy but not assigned to any edit layer. Re-assign the brush to an edit layer or the landscape will not be affected.

### Erasing Height in Layers

If you use the **Erase Tool** on the layer, the sculpting reverts to the default layer height. Layer Contribution can be helpful when using the Erase Tool because the layer is easy to identify (see the highlighted layer below with a symbol of its data (i.e., the mountain).

[![Erase tool in the modes toolbar](https://dev.epicgames.com/community/api/documentation/image/4d8934b1-c131-43bf-86a0-67ac60a7289a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4d8934b1-c131-43bf-86a0-67ac60a7289a?resizing_type=fit)

Erase tool in the modes toolbar. Click image for full size.

### Highlighting Layers

To highlight your layer, you can turn on **Layer Contribution**. By highlighting your layer, you can see the entirety of your sculpted layer. The highlight will remain on your layer until you turn it off. To turn on Layer Contribution, navigate to **Lit > Visualizers > Layer Contribution**. To see the layer's contribution to a heightmap, select the layer in Sculpt mode. To see the layer's contribution to a paint layer, select the layer in Paint mode.

## Special Edit Layers

Edit layers are designed to be multifunctional. Certain Landscape systems use specialized edit layers to apply procedural, feature specific modifications to the terrain. These layers are automatically managed and provide structured, non-destructive control over specific features.

**Splines Edit Layer**: Landscape splines data can now be created and managed in a separate, non destructive layer. After adding a Spline Edit Layer you can edit, change, and move splines non-destructively with the landscape terraforming automatically. The Landscape Spline edit layer only supports procedural data. It cannot be sculpted or painted by hand. See [Landscape Splines](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-splines-in-unreal-engine) for more information on using landscape splines.

**Patches Edit Layer**: Landscape patch data can now be created and managed in a separate, non destructive layer. After adding a Patch Edit Layer you can edit, change, and move patches non-destructively with the landscape terraforming automatically. The Landscape Patches edit layer only supports procedural data. It cannot be sculpted or painted by hand. See [Landscape Patch](https://dev.epicgames.com/documentation/en-us/unreal-engine/BlueprintAPI/LandscapePatch) for more information on using landscape patches.

## Additional Information

There are additional features to Landscape Edit Layers that enable you to build on your landscape easily and non-destructively. See the following features for additional information:

* [Landscape Blueprint Brushes](https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-blueprint-brushes-in-unreal-engine)

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [landscape](https://dev.epicgames.com/community/search?query=landscape)
* [layers](https://dev.epicgames.com/community/search?query=layers)
* [spline](https://dev.epicgames.com/community/search?query=spline)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Adding Layers to Your Landscape](/documentation/en-us/unreal-engine/landscape-edit-layers-in-unreal-engine?application_version=5.7#adding-layers-to-your-landscape)
* [Managing Layers](/documentation/en-us/unreal-engine/landscape-edit-layers-in-unreal-engine?application_version=5.7#managing-layers)
* [Toggling Lock Status](/documentation/en-us/unreal-engine/landscape-edit-layers-in-unreal-engine?application_version=5.7#locking-and-unlocking-layers)
* [Toggling Visibility](/documentation/en-us/unreal-engine/landscape-edit-layers-in-unreal-engine?application_version=5.7#hiding-and-unhiding-layers)
* [Layer Alpha](/documentation/en-us/unreal-engine/landscape-edit-layers-in-unreal-engine?application_version=5.7#layeralpha)
* [Removing Layers](/documentation/en-us/unreal-engine/landscape-edit-layers-in-unreal-engine?application_version=5.7#removinglayers)
* [Edit Layer Inspector](/documentation/en-us/unreal-engine/landscape-edit-layers-in-unreal-engine?application_version=5.7#editlayerinspector)
* [Editing Layers](/documentation/en-us/unreal-engine/landscape-edit-layers-in-unreal-engine?application_version=5.7#editing-layers)
* [Ordering Layers](/documentation/en-us/unreal-engine/landscape-edit-layers-in-unreal-engine?application_version=5.7#ordering-layers)
* [Edit Layer Context Menu](/documentation/en-us/unreal-engine/landscape-edit-layers-in-unreal-engine?application_version=5.7#editlayercontextmenu)
* [Erasing Height in Layers](/documentation/en-us/unreal-engine/landscape-edit-layers-in-unreal-engine?application_version=5.7#erasing-height-in-layers)
* [Highlighting Layers](/documentation/en-us/unreal-engine/landscape-edit-layers-in-unreal-engine?application_version=5.7#highlightinglayers)
* [Special Edit Layers](/documentation/en-us/unreal-engine/landscape-edit-layers-in-unreal-engine?application_version=5.7#specialeditlayers)
* [Additional Information](/documentation/en-us/unreal-engine/landscape-edit-layers-in-unreal-engine?application_version=5.7#additional-information)
