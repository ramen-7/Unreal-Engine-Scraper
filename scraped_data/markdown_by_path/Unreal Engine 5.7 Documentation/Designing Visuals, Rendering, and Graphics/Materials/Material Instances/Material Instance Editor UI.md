<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-material-instance-editor-ui?application_version=5.7 -->

# Material Instance Editor UI

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
6. [Materials](/documentation/en-us/unreal-engine/unreal-engine-materials "Materials")
7. [Material Instances](/documentation/en-us/unreal-engine/instanced-materials-in-unreal-engine "Material Instances")
8. Material Instance Editor UI

# Material Instance Editor UI

Guide to using the Material Instance Editor for modifying MaterialInstanceConstants.

![Material Instance Editor UI](https://dev.epicgames.com/community/api/documentation/image/5b73816e-9b68-48e2-b34a-98983a65f024?resizing_type=fill&width=1920&height=335)

 On this page

The Material Instance Editor is used for modifying parameters in Material Instances. If you are unfamiliar with Material parameterization and instancing, read the following pages:

1. [Material Instances Overview](/documentation/en-us/unreal-engine/instanced-materials-in-unreal-engine)
2. [Creating and Using Material Instances](/documentation/en-us/unreal-engine/creating-and-using-material-instances-in-unreal-engine)

## Opening the Material Instance Editor

Double-click a **Material Instance** asset in the Content Browser to open the Material Instance Editor.

![Double-click instance](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cf1bef8c-b3a2-4e69-93c3-75a76642a2d3/click-asset.png)

You can also **Right-click** the Material Instance thumbnail in the Content Browser and choose **Edit** from the context menu.

## Material Instance Editor Interface

The Material Instance Editor is comprised of these regions:

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/db641b1f-22b5-4ff7-bea7-d9f1428b39b7/material-instance-editor-sm.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/db641b1f-22b5-4ff7-bea7-d9f1428b39b7/material-instance-editor-sm.png)

1. [Toolbar](/documentation/en-us/unreal-engine/unreal-engine-material-instance-editor-ui#toolbar) - Save your asset, locate it in the Content Browser, show hidden parameters, display inheritance hierarchy and platform stats.
2. [Viewport](/documentation/en-us/unreal-engine/unreal-engine-material-instance-editor-ui#viewport) - A realtime viewport showing a preview of the Material instance.
3. [Viewport display options](/documentation/en-us/unreal-engine/unreal-engine-material-instance-editor-ui#viewportdisplayoptions) - Allows you to edit the camera and display settings in the viewport, and change the mesh used for the Material preview.
4. [Details Panel](/documentation/en-us/unreal-engine/unreal-engine-material-instance-editor-ui#detailspanel) - All exposed Material parameters and properties are found here.

### Toolbar

| **Icon** | **Description** |
| --- | --- |
| Save icon | Saves the current asset. |
| Content Browser | Finds and selects the Material instance in the **Content Browser**. |
| Show hidden | Displays inactive parameters that are hidden behind static swtiches. |
| Hierarchy | Shows the inheritance hierarchy of the Material instance. [See below](/documentation/en-us/unreal-engine/unreal-engine-material-instance-editor-ui#hierarchymenu). |
| Platform Stats | Opens a window displaying render statistcs for different target platforms. |

#### Hierarchy Menu

The **Hierarchy menu** displays the inheritance chain for the current Material instance. Since Material instances can be used as the parent for other Material instances, both parents and children are listed in the Hierarchy menu.

![Hierarchy](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3dc0163e-8427-4bcf-be51-89dc2ac26d4c/hierarchy.png)

* **Parents** of the current Material Instance are listed under Parent Chain. If there are multiple parents, the first one listed is at the top of the inheritance hierarchy.
* **Children** of the current Material Instances are listed under Material Instances.

Selecting a parent Material or Material instance from the Hierarchy menu opens that asset in a **new tab** of the Material Instance Editor window.

![Material parent tab](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a1792f4d-1607-469b-a10e-2a7459995bb3/parent-tab.png)

### Viewport

![Preview Viewport](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bb85ec1c-2236-4c4b-81f7-32fb8977c7ac/viewport-window.png)

The viewport shows a preview of your Material instance applied to a Static Mesh. The Material preview updates in real time as you make changes to the parameters in your Material Instance.

You can interact with the viewport using these controls:

* Click and drag the **left mouse button** to rotate the preview mesh.
* Click and drag the **middle mouse button** to pan the camera.
* Click and drag the **right mouse button** to zoom in an out, or use your scroll wheel.
* Rotate the light direction by holding down the **L** key and dragging with the **left mouse button**.

### Viewport Display Options

| **Icon** | **Description** |
| --- | --- |
| Viewport options | Contains toggle to enable real time preview, display FPS, and change FOV of the preview window. |
| Camera options | Switch between Perspective and Orthographic viewport cameras. |
| View mode options | lContains standard view modes like Lit, Unlit, Wireframe and others. Also contains an exposure override. |
| Show options | Enable or disable rendering stats, the grid and the background. |
| Cylinder preview | Preview the Material instance on a cylinder. |
| Sphere preview | Preview the Material instance on a sphere. |
| Plane preview | Preview the Material instance on a plane. |
| Cube preview | Preview the Material instance on a cube. |
| Custom static mesh | Preview the Material instance on a custom Static Mesh. |

You can change the Material preview mesh by clicking one of the shape icons at the bottom of the Viewport.

![Preview Mesh options](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/46ce7f71-f7c6-4a2c-b826-917db8145160/preview-mesh-options.png)

To preview your Material instance on a custom mesh, select a **Static Mesh** asset in the Content Browser, and then click the **brick icon**. The preview mesh is saved with the Material instance so that the next time it is opened it will appear on the same preview mesh.

![Custom mesh preview](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ae993b0d-05e3-4990-87d7-fe21ee943b49/custom-mesh-example.png)

The Viewport also displays statistics about the Material, such as instruction counts for the various shader types as well as the number of Texture
samples used by the Material.

![Viewport statistics](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/577f4512-a0a8-48b4-8475-5e066157b678/viewport-stats.png)

To preview any sort of movement or animation in your Material Instance, you must enable the **Realtime** Viewport option. Click the hambuerger menu to open Viewport options and make sure Realtime is checked. This option is enabled by default.

![Toggle Realtime](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/19a57647-c481-4078-9c3b-b1f72c004e56/toggle-realtime.png)

You can also press **Ctrl+R** to toggle real-time rendering.

### Details Panel

The Details panel is where you can override the parameters and settings in your Material Instance. All of the changes you make to your Material instance will occur in this interface.

![Details Panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/990457fc-5f41-4d37-87b4-ce7abf387b7c/details-panel.png)

There are three main subsections in the Details Panel:

#### Parameter Groups

Material attributes that you have exposed through parameters in your parent Material are listed here. To override the value in a parameter, check the box to the left of the parameter name and modify the value in the field. [See here](/documentation/en-us/unreal-engine/unreal-engine-material-instance-editor-ui#overridingmaterialinstanceparameters) for more information about overriding parameters.

#### General

The General section allows you to select a different Parent Material, or Physical Material. You can also adjust how this Material Instance will influence the Lightmass build and override some of the properties inherited from the parent Material. Read more about [these settings here](/documentation/en-us/unreal-engine/unreal-engine-material-instance-editor-ui#overridingmaterialinstancelightmasssettings).

#### Previewing

This section provides another input to change the static mesh used for the Material Instance preview.

## Overriding Material Instance Parameters

Parameters are listed under the **Parameter Groups** section in the Details panel. To override a Material parameter:

1. Place a check in the box to the left of the parameter name.
2. Type a new value into the field or use the color picker to set a new value.

![Override parameters](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/219987ae-1099-4783-b0fa-749cda6c7281/override-params.png)

Any parameter that is checked is currently overridden in the Material Instance. Unchecked parameters use the value from the parent Material, even if there is a different value in the field:

![Unchecked parameter](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4584b195-55ce-46c7-b876-27a90af2d192/not-overridden.png)

Remember to **Save** your Material instance when you are finished editing parameters so that your work is not lost. For memory conservation, values in unchecked fields will be lost when the Material Instance Editor window is closed.

To reset a parameter to its default value, click the **Reset** button to the right of the parameter.

![Reset parameter](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3812a799-b130-4229-b664-05a1d1e0bc68/reset-parameter.png)

### Overriding Material Instance Lightmass Settings

You can override the way your Material interacts with Lightmass under the **General > Lightmass Settings** section.

For example, if you increase the Emissive Boost attribute of an emissive Material, the Material will contribute more emissive light to the static lighting solution produced by Lightmass. This makes the result brighter.

![Override Emissive Boost](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/93f002ff-3341-4058-a432-8cfdd2eeb43a/emissive-boost.png)

### Overriding Parent Material Properties

The Material Property Overrides section allows you to override some of the Material Properties in the parent Material of your instance.

For example, if you need an instance of your Material to render on both the front and back side of a surface, you can enable the Two Sided option.

![Override Two Sided](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6830edbe-3495-4f72-bc0d-d4b529d35c6a/two-sided.png)

The advantage of overriding these properties in the Material Instance Editor instead of editing the parent is that it only affects a single instance of the Material. Every other instance will inherit settings from the parent.

* [materials](https://dev.epicgames.com/community/search?query=materials)
* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [shaders](https://dev.epicgames.com/community/search?query=shaders)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Opening the Material Instance Editor](/documentation/en-us/unreal-engine/unreal-engine-material-instance-editor-ui?application_version=5.7#openingthematerialinstanceeditor)
* [Material Instance Editor Interface](/documentation/en-us/unreal-engine/unreal-engine-material-instance-editor-ui?application_version=5.7#materialinstanceeditorinterface)
* [Toolbar](/documentation/en-us/unreal-engine/unreal-engine-material-instance-editor-ui?application_version=5.7#toolbar)
* [Hierarchy Menu](/documentation/en-us/unreal-engine/unreal-engine-material-instance-editor-ui?application_version=5.7#hierarchymenu)
* [Viewport](/documentation/en-us/unreal-engine/unreal-engine-material-instance-editor-ui?application_version=5.7#viewport)
* [Viewport Display Options](/documentation/en-us/unreal-engine/unreal-engine-material-instance-editor-ui?application_version=5.7#viewportdisplayoptions)
* [Details Panel](/documentation/en-us/unreal-engine/unreal-engine-material-instance-editor-ui?application_version=5.7#detailspanel)
* [Parameter Groups](/documentation/en-us/unreal-engine/unreal-engine-material-instance-editor-ui?application_version=5.7#parametergroups)
* [General](/documentation/en-us/unreal-engine/unreal-engine-material-instance-editor-ui?application_version=5.7#general)
* [Previewing](/documentation/en-us/unreal-engine/unreal-engine-material-instance-editor-ui?application_version=5.7#previewing)
* [Overriding Material Instance Parameters](/documentation/en-us/unreal-engine/unreal-engine-material-instance-editor-ui?application_version=5.7#overridingmaterialinstanceparameters)
* [Overriding Material Instance Lightmass Settings](/documentation/en-us/unreal-engine/unreal-engine-material-instance-editor-ui?application_version=5.7#overridingmaterialinstancelightmasssettings)
* [Overriding Parent Material Properties](/documentation/en-us/unreal-engine/unreal-engine-material-instance-editor-ui?application_version=5.7#overridingparentmaterialproperties)
