<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine?application_version=5.7 -->

# Geometry Brush Actors

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
5. [Understanding the Basics](/documentation/en-us/unreal-engine/understanding-the-basics-of-unreal-engine "Understanding the Basics")
6. [Actors and Geometry](/documentation/en-us/unreal-engine/actors-and-geometry-in-unreal-engine "Actors and Geometry")
7. [Actors Reference](/documentation/en-us/unreal-engine/unreal-engine-actors-reference "Actors Reference")
8. Geometry Brush Actors

# Geometry Brush Actors

Guide to using BSP brushes to create level geometry in Unreal Engine.

![Geometry Brush Actors](https://dev.epicgames.com/community/api/documentation/image/a86a7670-2d78-4e90-af5a-649ea23e19ae?resizing_type=fill&width=1920&height=335)

 On this page

Geometry Brushes, also known as Binary Space Partitioning (BSP) brushes, is Unreal Engine's tool for level construction. Conceptually, it is best to think of a Geometry Brush as filling in and carving out volumes of space in your level. You can use the brushes to create basic shapes for your level design process, either as permanent fixtures or as something temporary to test while your artists create the final meshes.

Previously, Geometry Brushes were used as the primary building block in level design. However, that role has been passed on to [Static Meshes](/documentation/en-us/unreal-engine/static-meshes) and in-engine [modeling tools](/documentation/en-us/unreal-engine/getting-started-with-modeling-mode), which are far more efficient. However, Geometry Brushes can still be helpful in the early stages of a product for rapid prototyping of levels and objects. This document goes over the use of Geometry Brushes and how to use them for your level.

Geometry Brushes are not recommended as a final method of level design. It is not required, but can be useful at the early stages of creation.

## Uses for Geometry Brushes

While Static Meshes are now primarily used to populate levels with geometry, Geometry Brushes still have their place, such as blocking out a level and creating filler geometry.

### Blocking Out Levels

A standard workflow for developing a level might go something like:

* Block out and path level
* Playtest flow and gameplay
* Modify layout and repeat testing
* Initial meshing pass
* Initial lighting pass
* Playtest for collision and performance issues
* Polish pass

|  |  |
| --- | --- |
| Level blocking in UE | Final level design in UE |
| Brush Blocking / Rough-In | Final level |

The first step is to block out the level to figure out the layout and flow before putting any time into populating the level with Static Meshes and other finished art assets. You can do this by using Geometry Brushes to create a shell for the level, then, through testing and iterating, the team agrees on the final layout. Geometry Brushes are perfect for this aspect of the level design process because it does not require any time or involvement from the art team. The level designer can use the tools built into the Unreal Editor to create and modify the Geometry Brushes until they are happy with the layout and the way the level plays.

As testing finalizes and meshing begins, the level designer gradually replaces Geometry Brushes with Static Meshes. This replacement process allows for faster initial iterations and provides an excellent reference for the art team.

### Simple Filler Geometry

Often, when a level designer is creating their level, they will come upon a situation where they need a relatively simple piece of geometry to fill in a gap or space. If no existing Static Mesh fills the area, instead of tasking the art team to create a custom mesh, the designer can use Geometry Brushes to fill the space. Even though Static Meshes are better performance-wise, you can occasionally use Geometry Brushes without any serious impact as long as the geometry is simple.

## Creating Brushes

Create a brush using the **Geometry** tab in the **Place Actors** panel:

1. Choose **Place Actors Panel** from the add dropdown.

   ![Geometry brush via Place Actors Panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b633feab-4430-404c-a91b-ba1657eca6bc/add-dropdown-ue-5-1.png)
2. Select the Geometry icon.

   ![Place Actors Panel in UE](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b0fb33c6-3db8-4acb-8057-cf576b6408ad/place-actors-panel-ue-5-1.png)
3. Drag one of the primitive types from the list into a **Viewport**.

   ![Placing geometry brush in Level](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/775881e7-e3d8-4e05-9552-e6828d8ec566/place-geometry-in-level-ue-5-1.png)
4. Choose the [Brush Type](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine#brushtypes) (additive or subtractive) in the **Details** panel.
5. Modify your Brush using the **Brush Settings** in the Details panel, the transform widget, or activate the **Brush Editing Mode**. See [Modifying Brushes](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine#modifyingbrushes) for more details.

## Brush Primitives

| Primitive | Description |  |
| --- | --- | --- |
|  | Creates a Geometry Brush Actor in a Box shape that can then be customized within the **Details** panel. Options include:   * **X**: Set the size in the X-Axis. * **Y**: Set the size in the Y-Axis. * **Z**: Set the size in the Z-Axis. * **Wall Thickness**: If **Hollow** is checked, set the thickness of the inner walls of the Brush. * **Hollow**: Check this box to have a hollow space inside the Brush (which is a fast way to make a room) rather than a solid. If checked, enables the **Wall Thickness** setting. * **Tessellated**: Check this box to tessellate the sides of the box into triangles, rather than remaining as quads. |  |
|  | Creates a Geometry Brush Actor in a Cone shape that can then be customized within the **Details** panel. Options include:   * **Z**: Set the height in the Z-Axis. * **Cap Z**: If **Hollow** is checked, set the height of the inner cap in the Z-Axis. * **Outer Radius**: Set the radius of the base of the cone. * **Inner Radius**: If **Hollow** is checked, set the radius of the inner wall of the cone. * **Sides**: Set the number of sides around the shape of the cone. * **Align to Side**: Check this box to align the rotation of a side along the X-Axis. Disable to let one of the angles point down the axis. * **Hollow**: Check this box to have a hollow space inside the Brush (which is a fast way to make a room), rather than a solid. If checked, enables the **Inner Radius** setting. |  |
|  | Creates a Geometry Brush Actor in a Cylinder shape that can then be customized within the **Details** panel. Options include:   * **Z**: Set the height in the Z-Axis. * **Outer Radius**: Set the radius of the cylinder. * **Inner Radius**: If **Hollow** is checked, set the radius of the hollow space inside the cylinder. * **Sides**: Set the number of sides around the shape of the cylinder. * **Align to Side**: Check this box to align the rotation of a side along the X-Axis. Disable to let one of the angles point down the axis. * **Hollow**: Check this box to have a hollow space inside the Brush (which is a fast way to make a room), rather than a solid. If checked, enables the **Inner Radius** setting. |  |
|  | Creates a Geometry Brush Actor in a Curved Staircase shape, meaning a staircase that bends around at an angle but cannot wrap over itself - for that, you would need a Spiral Staircase. The Curved Staircase extends all the way to the ground. The shape can be customized within the **Details** panel. Options include:   * **Inner Radius**: Set the radius of the inner column around which the steps will wrap. * **Step Height**: Set the height of each stair. * **Step Width**: Set the width of each stair. * **Angle of Curve**: Set the angle of rotation for each stair. * **Num Steps**: Set the number of steps in the staircase. * **Add to First Step**: Set the additional height to the first step, effectively changing the height of the entire staircase. (Enter a negative value to reduce the height of the first step). * **Counter Clockwise**: Check this box to curve the stairs counterclockwise rather than clockwise. |  |
|  | Creates a Geometry Brush Actor in a Linear Staircase shape, meaning a straight staircase that does not bend. The staircase extends all the way to the ground. The shape can then be customized within the **Details** panel. Options include:   * **Step Length**: Set the length of each stair. * **Step Height**: Set the height of each stair. * **Step Width**: Set the width of each stair. * **Num Steps**: Set the number of stairs in the staircase. * **Add to First Step**: Set additional height to the first step, effectively changing the height of the entire staircase. (Enter a negative value to reduce the height of the first step). |  |
|  | Creates a Geometry Brush Actor in a Spiral Staircase shape, meaning a staircase can repeatedly wrap over itself. This staircase does not extend all the way to the ground. The shape can be customized within the **Details** panel. Options include:   * **Inner Radius**: Set the radius of the inner column around which the steps will wrap. * **Step Width**: Set the width of each stair. * **Step Height**: Set the difference in the height of each stair relative to the stair below it. * **Step Thickness**: Set the thickness of the stair. * **Num Steps Per 360**: Set the number of steps required to make one complete revolution. * **Num Steps**: Set the number of steps in the staircase. * **Add to First Step**: Set additional height to the first step, effectively changing the height of the entire staircase. (Enter a negative value to reduce the height of the first step). * **Sloped Ceiling**: Check this box to create a sloped underside for the staircase, rather than tiers. * **Sloped Floor**: Check this box to create a sloped floor, effectively turning it into a spiraling ramp instead of a traditional staircase. * **Counter Clockwise**: Check this box if you want the stairs to curve counterclockwise instead of clockwise. |  |
|  | Creates a Geometry Brush Actor in a Sphere shape that can then be customized within the **Details** panel. Options include:   * **Radius**: Set the radius of the sphere. * **Tessellation**: Set the number of sides used to make the sphere. Due to the method of tessellation, this is capped at 5. |  |

## Modifying Brushes

You can modify Brushes using several methods, each suited to particular situations and how you wish to edit the Brush.

### Brush Editing Mode

The best way to change a Brush's actual shape is to use the **Brush Editing Mode**. This editor mode allows the direct manipulation of the Brush's vertices, edges, and faces. It is very similar to working in a very simplified 3D modeling application.

![BSP Brush Editing Mode](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dd4974a2-adc9-44b0-a2de-3b9f5a1c28a1/brush-editing-mode-ue-5-1.png)


You can have the Brush Editing and Place Actors panels open simultaneously for workflow efficiency.

![BSP Panels](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/193a586e-df56-4d03-b808-a2699055dffe/brush-panels-side-by-side-ue-5-1.png)

For more information about **Brush Editing Mode** and how to use it to modify Brushes, see the [Level Editor Modes](/documentation/en-us/unreal-engine/level-editor-modes-in-unreal-engine) page.

### Transform Widgets

It is possible to modify your Brush using the various editor transform widgets. These allow you to translate, rotate, and scale interactively and are accessible via the widget buttons in the viewport toolbar:

![Adjust BSP Brushes with transform widgets](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c764f163-cc32-4eb7-9341-d11220cd6ea3/transform-widgets-ue-5-1.png)

For more information on the Transform widgets and how to use them, please see [Transforming Actors](/documentation/en-us/unreal-engine/transforming-actors-in-unreal-engine).

## Brush Properties

You can edit existing Brushes by selecting the Brush and using the **Details** panel. If you have the entire Brush selected, you will see the **Brush Settings** category:

![Geometry Brush Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/20292a33-6ff8-4e5a-b436-bf554a614f15/brush-settings-ue-5-1.png)

### Brush Types

The **Brush Type** dropdown includes the following:

| Brush Type Dropdown |  |
| --- | --- |
| **Additive** | Set the Brush to Additive. |
| **Subtractive** | Set the Brush to Subtractive. |

Each Brush Type is particularly suited to specific situations.

#### Additive

**Additive** Brushes are solid, filled-in spaces. The Additive Brush is the type you use for any Brush geometry you wish to add to the level. A good way to visualize an additive Brush is to imagine the four walls, the floor, and the ceiling of a room. Each would be a separate box-like Additive Brush in your map, with corners matching up to form an enclosed space.



#### Subtractive

A **Subtractive** Brush is a hollow, carved-out space. This is the type of Brush you would use to remove solid space to create doors, windows, and so on, from previously created additive Brushes. Subtractive space is the only area that players can freely move around in.



### Advanced Properties

Clicking the ![Advanced](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3ba0de89-8d68-459d-bad2-25c5e7671874/button_advanced.png) button at the bottom of the **Brush Settings** exposes the advanced Brush properties:

![BSP Brush Advance Properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2bc65ee0-027f-44f3-a9f1-09baf2c3c757/advance-properties-ue-5-1.png)

#### Polygons

The **Polygons** dropdown offers the following options:

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a74e3db9-ce88-4f1b-85c0-8ed164baac4c/polygonsdropdown.png)

| Polygons Dropdown |  |
| --- | --- |
| **Merge** | Merge together any planar faces on a Brush. |
| **Separate** | Reverse the effects of a merge. |

#### Solidity

The **Solidity** dropdown includes the following:

Be sure to read the [Brush Solidity section](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine#brushsolidity) for more details.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/64c495c2-4ee0-4efc-a92f-2cbf86c6086c/soliditydropdown.png)

| Solidity Dropdown |  |
| --- | --- |
| **Solid** | Set the Brush solidity to be solid. |
| **Semi Solid** | Set the Brush solidity to be semi-solid. |
| **Non Solid** | Set the Brush solidity to non-solid. |

#### Order

The **Order** dropdown includes the following:

Be sure to read the [Brush Order](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine#brushorder) section for more details:

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9efcb20e-3218-4611-98f5-0a35d5263a7a/oderdropdown.png)

| Order Dropdown |  |
| --- | --- |
| **To First** | Make the selected Brush the first to be calculated. |
| **To Last** | Make the selected Brush the last to be calculated. |

### Align and Static Mesh Buttons

If you expand the properties under the **Brush Settings** Category, the following buttons appear:

| Brush Type Dropdown |  |
| --- | --- |
| **Align Brush Vertices** | Snap the Brush's vertices to the grid. |
| **Create Static Mesh** | Convert the current Brush to a Static Mesh Actor, saved at the location specified. |

## Drag Grid

The drag grid used to snap objects in the world is very important when working with Brushes. If you don't set the edges or corners of Brushes on the grid, errors can occur, causing rendering artifacts or other problems. You should always make sure the drag grid is enabled when working with Brushes and make sure that you keep the vertices of your Brushes on this grid at all times.

## Brush Order

The order in which Brushes are placed is critical, as the addition and subtraction operations are performed according to this order. Placing a subtractive Brush and then an additive Brush will not have the same effect as placing an additive Brush and then a subtractive Brush, even if they are in the exact locations.

If you subtract from empty space and add on top, the subtractive Brush is essentially ignored, as you cannot subtract from anything. However, if you place those same Brushes in the opposite order, you add to empty space, then subtract from the addition, carving space out of it.

Sometimes you may place Brushes out of order or want to add a new Brush that needs to be calculated before an existing Brush. The Brushes' order can be modified, as seen in the [Brush Properties](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine#brushproperties) section.

## Brush Surfaces

If you select a Brush surface (use **Ctrl + Shift + Left Click** to select the surface and not the Brush), you will see the following categories in the **Details** panel:

![Geometry Brush surface](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f61371fa-fbce-41d5-b9c2-dea419cd97b2/brush-surfaces-ue-5-1.png)

### Geometry Category

The **Geometry** category contains a few tools for helping you manage Material application across Brush surfaces.

| Geometry Category Buttons |  |
| --- | --- |
| **Select** | Helps you select Brush surfaces based on various situations. |
| **Alignment** | Realigns the texture coordinates for surfaces based on your desired settings. This is useful, for example, when you need a complex arrangement of Brushes along the floor to align and look like a single surface. |
| **Clean Geometry Materials** | If, through any operations, your Brush surfaces have lost their Material, this will fix the problem. |

### Surface Properties

The **Surface Properties** area contains various tools to help you control how textures are placed across your surfaces, as well as lightmap resolution.

| Surface Property Categories |  |
| --- | --- |
| **Pan** | The buttons in this section allow you to pan the texture of the Material either horizontally or vertically by the given number of units. |
| **Rotate** | Rotates the texture on a Brush surface's Material by the given number of degrees. |
| **Flip** | Allows you to flip the texture on a Brush surface horizontally or vertically. |
| **Scale** | Resizes the texture of a Brush surface by the amount given. |

#### Lighting

The **Lighting** section allows you to change various important light-centric properties for your Brush surfaces.

| Lighting Properties |  |
| --- | --- |
| **Lightmap Resolution** | Essentially allows for adjustment of the shadows across this surface. The lower the number, the tighter the shadows. |
| Lightmass Settings |  |
| **Use Two Sided Lighting** | If checked, this surface will receive light on both the positive and negative sides of each polygon. |
| **Shadow Indirect Only** | Check this box to allow the surface to create shadows from indirect lighting. |
| **Use Emissive for Static Lighting** | Check this box to allow the emissive color of the surface to influence the lighting of static objects. |
| **Use Vertex Normal for Hemisphere Gather** | Check this box to use the vertex normal rather than the default triangle normal that prevents self-shadowing. |
| **Emissive Boost** | Scales the amount of influence emissive color will have on indirect lighting. |
| **Diffuse Boost** | Scales the amount of influence diffuse color will have on indirect lighting. |
| **Fully Occluded Samples Fraction** | Fraction of samples along this surface that must be occluded before it is considered to be occluded from indirect lighting calculations. |

## Brush Solidity

Brushes can be either **Solid**, **Semi-solid**, or **Non-solid**. The solidity of a Brush refers to whether it collides with objects in the world and whether the Brush causes BSP cuts to be created in the surrounding Brushes when building geometry.

The solidity of Brushes can be changed in the **Details** panel after you create a Brush:

![Geometry Brush Solidity](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/26d65d64-7972-4e58-85ab-b671c1d6c53a/brush-solidity-ue-5-1.png)

The three types of solidity are explained below.

### Solid

**Solid** Brushes are the default type of Brush. You get these when you create a new additive or subtractive Brush. They have the following attributes:

* Block players and projectiles in the game.
* Can be additive or subtractive.
* Create cuts in the surrounding Brushes.

### Semi-Solid

**Semi-solid** Brushes are colliding Brushes that can be placed in your level without creating cuts to the surrounding world geometry. You can use it to make pillars and support beams, though such objects should be created using Static Meshes. They have the following attributes:

* Block players and projectiles, just as Solid Brushes do.
* Can only be additive, never subtractive.
* Do not create cuts in the surrounding Brushes.

### Non-Solid

**Non-Solid** Brushes are non-colliding Brushes that also do not create cuts in the surrounding world geometry. These have the effect of being visible but unable to be interacted with in any way. They have the following attributes:

* Do not block players or projectiles.
* Can only be additive, never subtractive.
* Do not create cuts in the surrounding Brushes.

## Next Steps

After learning the essentials of Geometry Brushes, you can familiarize yourself with the geometry tools in [Modeling Mode](/documentation/en-us/unreal-engine/getting-started-with-modeling-mode) to further develop your level. To use the Modeling Mode tools on your current Geometry Brushes, you must convert them using **Create Static Mesh** in the **Advanced** tab.

* [level design](https://dev.epicgames.com/community/search?query=level%20design)
* [geometry brush](https://dev.epicgames.com/community/search?query=geometry%20brush)
* [bsp brush](https://dev.epicgames.com/community/search?query=bsp%20brush)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Uses for Geometry Brushes](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine?application_version=5.7#usesforgeometrybrushes)
* [Blocking Out Levels](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine?application_version=5.7#blockingoutlevels)
* [Simple Filler Geometry](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine?application_version=5.7#simplefillergeometry)
* [Creating Brushes](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine?application_version=5.7#creatingbrushes)
* [Brush Primitives](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine?application_version=5.7#brushprimitives)
* [Modifying Brushes](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine?application_version=5.7#modifyingbrushes)
* [Brush Editing Mode](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine?application_version=5.7#brusheditingmode)
* [Transform Widgets](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine?application_version=5.7#transformwidgets)
* [Brush Properties](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine?application_version=5.7#brushproperties)
* [Brush Types](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine?application_version=5.7#brushtypes)
* [Additive](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine?application_version=5.7#additive)
* [Subtractive](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine?application_version=5.7#subtractive)
* [Advanced Properties](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine?application_version=5.7#advancedproperties)
* [Polygons](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine?application_version=5.7#polygons)
* [Solidity](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine?application_version=5.7#solidity)
* [Order](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine?application_version=5.7#order)
* [Align and Static Mesh Buttons](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine?application_version=5.7#alignandstaticmeshbuttons)
* [Drag Grid](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine?application_version=5.7#draggrid)
* [Brush Order](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine?application_version=5.7#brushorder)
* [Brush Surfaces](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine?application_version=5.7#brushsurfaces)
* [Geometry Category](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine?application_version=5.7#geometrycategory)
* [Surface Properties](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine?application_version=5.7#surfaceproperties)
* [Lighting](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine?application_version=5.7#lighting)
* [Brush Solidity](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine?application_version=5.7#brushsolidity)
* [Solid](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine?application_version=5.7#solid)
* [Semi-Solid](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine?application_version=5.7#semi-solid)
* [Non-Solid](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine?application_version=5.7#non-solid)
* [Next Steps](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine?application_version=5.7#nextsteps)

Related documents

[Modeling Mode Overview

![Modeling Mode Overview](https://dev.epicgames.com/community/api/documentation/image/056cb8c8-a8a2-4ba1-b18c-42a01965bcb1?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/modeling-mode-in-unreal-engine)

[CubeGrid

![CubeGrid](https://dev.epicgames.com/community/api/documentation/image/146717e4-6db2-499a-bd26-cd73e81c8789?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/cubegrid-tool-in-unreal-engine)

[Level Editor

![Level Editor](https://dev.epicgames.com/community/api/documentation/image/71d227f9-244b-4770-ba06-e2f16c49ad56?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/level-editor-in-unreal-engine)
