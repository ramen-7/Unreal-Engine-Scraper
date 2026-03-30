<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7 -->

# Cloners and Effectors

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
5. [Motion Design](/documentation/en-us/unreal-engine/motion-design-in-unreal-engine "Motion Design")
6. Cloners and Effectors

# Cloners and Effectors

An overview for using Cloners and Effectors in Motion Design.

![Cloners and Effectors](https://dev.epicgames.com/community/api/documentation/image/0423ab9a-6ee4-4edb-bc65-65ebe2018797?resizing_type=fill&width=1920&height=335)

 On this page

## Introduction

Motion Design has its own unique integration of the established Niagara particle system. You can use Motion Design to create lively motion graphics by way of creating clones or multiple instances of existing geometry. You can influence a variety of actor properties either as a group or on a granular level.

The core features are powered by Niagara, but working with Cloners and Effectors simplifies that process significantly through streamlined tooling. You can use cloners and effectors for scaling, rotation, and positioning and for procedural noise, so you can randomize and colorize your actors to create unique visual effects.

This overview assumes readers are familiar with the content of the [Motion Design Quick Start](https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-design-quickstart-guide-in-unreal-engine).

## Where to Find the Tools

First, either enable the **ClonerEffector** plugin, or enable the Motion Design mode (which was covered in the Quick Start guide).

When you enter Motion Design mode, click on **Actors** in the palette to see the two main tools:

* the **Cloner Actor**
* the **Effector Actor**

You can also use the **Place Actors** tab, and search for Motion Design Cloner and Effector.

[![Place a cloner or effector actor](https://dev.epicgames.com/community/api/documentation/image/daafe0aa-4d31-477b-a66c-ed499483c323?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/daafe0aa-4d31-477b-a66c-ed499483c323?resizing_type=fit)

You can find the Cloner and Effector actors in the **Place Actors** panel here:

[![Motion Design actors in the Place Actors panel](https://dev.epicgames.com/community/api/documentation/image/0a8a01c1-375d-45cd-a5e0-ce61bbdc2189?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0a8a01c1-375d-45cd-a5e0-ce61bbdc2189?resizing_type=fit)

## Cloner Actors

Double-clicking on the Cloner Actor from the toolbar in the **Motion Design** mode places the actor in the middle of your level with a default mesh applied to it. You can also click on the Cloner Actor button and click in your viewport to place it. In this case, it uses the DefaultCube, but you can apply any mesh that you want. For example, you can select another shape from the **Motion Design 3D Shapes** palette (also seen in the above screenshot).

Here is an example of mixing and matching the shapes, using sphere and torus meshes instead of the default cube mesh:

[![Mixed sphere and torus clone shapes](https://dev.epicgames.com/community/api/documentation/image/fdcf0457-1d60-4817-aba8-185d74bdbd06?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fdcf0457-1d60-4817-aba8-185d74bdbd06?resizing_type=fit)

Your Details panel has the following categories:

* [General](https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine#general)
* [Cloner](https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine#cloner)
* [Effector](https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine#effector)
* [Emission](https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine#emission)
* [Physics](https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine#physics)
* [Rendering](https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine#rendering)
* [Utilities](https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine#utilities)

### General

The **General** category contains common transforms for positioning your cloner actors. These transforms do not directly affect [layouts](https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine#layouts).

[![Cloner actor General category](https://dev.epicgames.com/community/api/documentation/image/a282327c-11cb-460c-97a7-a04f547a3f03?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a282327c-11cb-460c-97a7-a04f547a3f03?resizing_type=fit)

| General Properties | Description |
| --- | --- |
| Transform |  |
| **Location** | Standard location transform, using X, Y, and Z coordinates. |
| **Rotation** | Standard rotation transform, using X, Y, and Z coordinates. |
| **Scale** | Standard scale transform, using X, Y, and Z coordinates. |

### Cloner

The **Cloner** category handles the majority of how your system sorts and presents your clones. This includes how you assign a **Layout** for your cloner, tint them a specific color, and force the cloner to update if changing your settings isn’t resulting in an instant change. It also contains the ability to disable the cloner completely with the **Enabled** toggle.

[![Cloner actor Cloner category](https://dev.epicgames.com/community/api/documentation/image/9d7d896f-aa73-4e4d-8ce5-1e34c801c502?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9d7d896f-aa73-4e4d-8ce5-1e34c801c502?resizing_type=fit)

#### Force Update Cloner

In the event that your cloner system fails to update, this acts as a fallback to ensure proper generation.

#### Seed

The **Seed** property, when used together with the **Range** property enabled, gives variations when changing the value.

In the example below, we modified the **OffsetMax** property to adjust the position of the shapes. Changing the **Seed** randomizes those positions.

Seed value of 0:

[![OffsetMax with Seed 0](https://dev.epicgames.com/community/api/documentation/image/d97fd27f-e826-404b-8138-99743828ed81?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d97fd27f-e826-404b-8138-99743828ed81?resizing_type=fit)

Seed value of 1:

[![OffsetMax with Seed 1](https://dev.epicgames.com/community/api/documentation/image/26351cac-8bf3-46d4-a1ca-525218688770?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/26351cac-8bf3-46d4-a1ca-525218688770?resizing_type=fit)

#### Color

You can set the color of your clones using an RGBA value. You can use the Color Picker, or just input your values directly.

#### Advanced

In this sub-category you can set how often your tree refreshes using the **Tree Update Interval**. To reduce system overload, the default value of 0.2 means that your tree does not update every tick. Instead, it updates every 5 ticks, approximately.

[![Cloner category Advanced properties](https://dev.epicgames.com/community/api/documentation/image/4b634d20-ec3d-4c96-8d0e-55abebfc8e32?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4b634d20-ec3d-4c96-8d0e-55abebfc8e32?resizing_type=fit)

The **Visualizer Sprite Visible** toggle shows or hides the cloner widget in your viewport:

[![Visualizer sprite visible](https://dev.epicgames.com/community/api/documentation/image/16600b0a-467a-4ffb-b0dd-6cdd1e904e5f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/16600b0a-467a-4ffb-b0dd-6cdd1e904e5f?resizing_type=fit)

| Cloner Properties | Description |
| --- | --- |
| **Force Update Cloner** | Manually forces cloners to update in the event of an error. |
| **Enabled** | Enables using cloners. |
| **Seed** | Used to randomize cloners positions. |
| **Color** | Standard RGBA color selection using the Color Picker |
| Advanced |  |
| --- | --- |
| **Tree Update Interval** | Determines how often your tree refreshes. |
| **Visualizer Sprite Visible** | Makes the cloner widget visible when enabled. |

#### Layouts

The most important option in this category is the **Layout**. Layouts share similar options like range, step, effectors, lifetime, rendering, and progress. They also have specific options depending on the layout selected.

[![Layouts category properties](https://dev.epicgames.com/community/api/documentation/image/1c9300e8-1be0-46bf-84e3-fa6fcb1de49c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1c9300e8-1be0-46bf-84e3-fa6fcb1de49c?resizing_type=fit)

Setting the Layout changes how the clones arrange themselves. By setting the other properties in the image above, you can spread out the clones with **Spacing** and adjust the number of clones with the **Count** properties.

The available options for arranging the clones using the Layout dropdown are:

* [Grid](https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine#grid)
* [Line](https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine#line)
* [Circle](https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine#circle)
* [Cylinder](https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine#cylinder)
* [Sphere Uniform](https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine)
* [Honeycomb](https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine#honeycomb)
* [Mesh](https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine#mesh)
* [Spline](https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine#spline)
* [Sphere Random](https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine)

Each **Layout** has different settings and options.

[![Layout dropdown](https://dev.epicgames.com/community/api/documentation/image/5e86e73e-65df-4a51-9d75-80b312bd1c87?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5e86e73e-65df-4a51-9d75-80b312bd1c87?resizing_type=fit)

##### Grid

The Grid layout sorts the clones into a 3-dimensional grid. You can set parameters for how many clones display on each axis (X, Y, Z), and the clones' spacing. This layout also provides you the option to limit your clones to a constraint, which is a specific shape profile, and to invert the constraint.

[![Constraint options](https://dev.epicgames.com/community/api/documentation/image/ba72cb46-4ec8-4606-b995-5ec3cd63bdfa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ba72cb46-4ec8-4606-b995-5ec3cd63bdfa?resizing_type=fit)

[![Grid layout](https://dev.epicgames.com/community/api/documentation/image/06009226-cd25-4984-a643-f3eb8b0f13ab?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/06009226-cd25-4984-a643-f3eb8b0f13ab?resizing_type=fit)

Here is an example using the **Constraint** to take on the shape of a sphere:

[![Sphere constraint properties](https://dev.epicgames.com/community/api/documentation/image/d9efe91f-d7c2-4fea-a90a-662753c0858b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d9efe91f-d7c2-4fea-a90a-662753c0858b?resizing_type=fit)

[![Grid with sphere constraint](https://dev.epicgames.com/community/api/documentation/image/b65401b5-2bab-410c-b4d0-8aa213ceb2f6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b65401b5-2bab-410c-b4d0-8aa213ceb2f6?resizing_type=fit)

Each of those **Grid Layout** options also gives you the ability to **Invert Constraint**.

[![Invert Constrait option enabled](https://dev.epicgames.com/community/api/documentation/image/1ffab5b9-8fcd-47ff-aeb9-a38a4018b84c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1ffab5b9-8fcd-47ff-aeb9-a38a4018b84c?resizing_type=fit)

[![Grid layout with inverted sphere constraint](https://dev.epicgames.com/community/api/documentation/image/ecbc1584-c5e9-4211-a296-d9d4b38566cc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ecbc1584-c5e9-4211-a296-d9d4b38566cc?resizing_type=fit)

You also have the option to use a texture to constrain your clones:

[![Grid with texture constraint](https://dev.epicgames.com/community/api/documentation/image/76c48400-b274-46f8-9527-c3f360b28014?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/76c48400-b274-46f8-9527-c3f360b28014?resizing_type=fit)

| Grid Layout Properties | Description |
| --- | --- |
| **Count X / Y / Z** | The number of cloners in the grid along the X, Y, or Z axis. |
| **Spacing X / Y / Z** | The space between cloners in the grid along the X, Y, or Z axis. |
| **Constraint** | Options are:   * None (don’t use a constraint) * Cylinder * Sphere * Texture |
| **Invert Constraint** | Enable this option to invert the effects of the selected Constraint. Only available when Constraint is set to an option other than None. |

##### Line

The Line layout arranges the cloner actors into a straight line. You can control the number of clones using the **Count** property, and the space between those clones using the **Spacing** property. You can use the **Axis** property to control which direction the clones flow, and the **Rotation** property to cause the clones to curl along a combination of the X,Y, and Z axes.

[![Line layout](https://dev.epicgames.com/community/api/documentation/image/d0faeadf-2464-4453-b08a-b6cdead5a93e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d0faeadf-2464-4453-b08a-b6cdead5a93e?resizing_type=fit)

| Line Layout Properties | Description |
| --- | --- |
| **Count** | The number of cloners in the line. |
| **Spacing** | The spacing between the cloners in the line. |
| **Axis** | The main axis (X, Y, or Z) along which the line is oriented. |
| **Rotation X / Y / Z** | Rotation of the line in degrees towards the X, Y, or Z axis. Does not directly rotate the cloner actors. |

##### Circle

The **Circle** layout arranges the cloner actors into a circle. You can set the clone count with the **Count** property, and the **Radius** of the circle of clones. You can also use the **Angle Ratio** to determine how spaced out the clones will be along the circle. 0 means no spacing between cloners at all, and 1 means clones are spread out evenly along the shape. You can use the **Plane** dropdown to define the plane (XY, YZ, XZ) on which the clones spawn. The **Orient Mesh** toggle forces all clones to face the center of the circle.

[![Circle layout](https://dev.epicgames.com/community/api/documentation/image/05c59b66-8ca7-4066-9978-3fcf435d639f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/05c59b66-8ca7-4066-9978-3fcf435d639f?resizing_type=fit)

You can set the rotation angle of your circle using the **Angle Start** property.

Adjusting the **Angle Ratio** spreads the clones along the circle. If you want the clones to only spread across half of the circle, then here is what a .5 value would look like:

[![Using Angle Ratio to create a half-circle](https://dev.epicgames.com/community/api/documentation/image/cef99efe-e7aa-4a87-8b70-72d24c30e212?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cef99efe-e7aa-4a87-8b70-72d24c30e212?resizing_type=fit)

Scaling on a single axis property, as opposed to fully linked, results in an oval:

[![Circle scaled on a single axis to produce an oval](https://dev.epicgames.com/community/api/documentation/image/ba9fac01-4eff-48be-af9a-b5596b51f6e0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ba9fac01-4eff-48be-af9a-b5596b51f6e0?resizing_type=fit)

| Circle Layout Properties | Description |
| --- | --- |
| **Count** | The number of clones in the circle. |
| **Radius** | The radius of the circle. |
| **Angle Start** | Sets the rotation angle of the circle. |
| **Angle Ratio** | Determines how spread out on the circle the clones are. Values range from 0 to 1, with 0 meaning no spacing, and 1 meaning completely even spacing around the whole circle. |
| **Orient Mesh** | Forces clones to face the center of the circle. |
| **Plane** | Determines the axes used to define the plane on which the Circle layout clones spawn. Options are:   * XY * YZ * XZ |
| **Scale X / Y / Z** | Scales the layout circle on the X, Y, or Z axis. Does not scale the cloner actors. |

##### Cylinder

The Cylinder layout arranges the cloner actors into a cylinder. It has mostly the same properties as the Circle layout, with the addition of the Height and Height Count properties.

[![Cylinder layout](https://dev.epicgames.com/community/api/documentation/image/e3e610cc-629d-4b1b-96e8-3f3a6e36dda6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e3e610cc-629d-4b1b-96e8-3f3a6e36dda6?resizing_type=fit)

| Cylinder Layout Properties | Description |
| --- | --- |
| **Base Count** | The number of clones in the circle that makes up the base of the cylinder. |
| **Height** | The height of the cylinder from the plane that defines its base. |
| **Height Count** | The number of clones in a line from the base to the top of the cylinder. Each one represents a complete circle of clones. |
| **Radius** | The radius of the cylinder. |
| **Angle Start** | Sets the rotation angle of the cylinder. |
| **Angle Ratio** | Determines how spread out on each circle of the cylinder the clones are. Values range from 0 to 1, with 0 meaning no spacing, and 1 meaning completely even spacing around the whole cylinder. |
| **Orient Mesh** | Forces clones to face the center of the cylinder. |
| **Plane** | Determines the axes used to define the plane on which the cylinder layout clones spawn. Options are:   * XY * YZ * XZ |
| **Scale X / Y / Z** | Scales the layout cylinder on the X, Y, or Z axis. Does not scale the cloner actors. |

##### Sphere Uniform

You can set the total **Count** of the clones in the sphere, and the **Radius** of the sphere, which spreads the clones apart evenly.

[![Sphere Uniform layout](https://dev.epicgames.com/community/api/documentation/image/1d836b79-b567-48dc-bb0b-8e9f88dd1d06?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1d836b79-b567-48dc-bb0b-8e9f88dd1d06?resizing_type=fit)

The **Rotation** property rotates the entire sphere along the X, Y, or Z axis:

[![Rotating a sphere layout](https://dev.epicgames.com/community/api/documentation/image/05513971-4613-4ea4-a11a-69e76af672d8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/05513971-4613-4ea4-a11a-69e76af672d8?resizing_type=fit)

The **Ratio** property sets how much of the sphere will be covered by your clones. A .5 value produces a result like the image below:

[![Using the Ratio property to cover half a sphere](https://dev.epicgames.com/community/api/documentation/image/c5896881-9992-4ac1-823b-3fa86dc322ea?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c5896881-9992-4ac1-823b-3fa86dc322ea?resizing_type=fit)

The **Orient Mesh** toggle forces all clones to face the center of the sphere.

[![Using Orient Mesh to force clone facing](https://dev.epicgames.com/community/api/documentation/image/7e333304-a433-47a1-a34b-047f4f0d6f14?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7e333304-a433-47a1-a34b-047f4f0d6f14?resizing_type=fit)

If you set the **Scale** property unevenly for the X, Y, and Z axes, the result is an elliptical spheroid, like the image below:

[![Using uneven scaling to create an elliptical spheroid](https://dev.epicgames.com/community/api/documentation/image/06ec4578-b930-4a8a-b78f-7e50215812de?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/06ec4578-b930-4a8a-b78f-7e50215812de?resizing_type=fit)

| Sphere Uniform Layout Properties | Description |
| --- | --- |
| **Count** | The number of clones in the sphere. |
| **Radius** | The radius of the sphere, which controls how spread out the clones are. |
| **Ratio** | Sets how much of the sphere is covered by your clones. |
| **Orient Mesh** | Forces clones to face the center of the sphere. |
| **Rotation X / Y / Z** | Rotation of the sphere in degrees towards the X, Y, or Z axis. Does not directly rotate the cloner actors. |
| **Scale X / Y / Z** | Scales the layout sphere on the X, Y, or Z axis. Does not scale the cloner actors. |

##### Honeycomb

You can set the axis that the elements clone along using the **Plane** setting. You can control the number of clones using the **Width Count** and **Height Count**, and use the **Width Offset** and **Height Offset** properties to control the clones' positional offset. To space out the clones, use the **Width Spacing** and **Height Spacing** properties.

[![Honeycomb layout](https://dev.epicgames.com/community/api/documentation/image/0dff21d7-e501-4a16-b278-428499a4be92?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0dff21d7-e501-4a16-b278-428499a4be92?resizing_type=fit)

You can twist your **Honeycomb** using the **Twist Factor** setting, and decide which axis to twist along using the Twist Axis property. The value is measured in percentage, with 100% representing a full 180 degree twist.

Twisting along the Y-axis:

[![Honeycomb layout twisted along Y axis](https://dev.epicgames.com/community/api/documentation/image/088defec-5e77-409b-a30e-33babf7b8e05?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/088defec-5e77-409b-a30e-33babf7b8e05?resizing_type=fit)

Twisting along the Z-axis:

[![Honeycomb layout twisted along Z axis](https://dev.epicgames.com/community/api/documentation/image/332642eb-5c53-4be7-8819-66dfeded0aa2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/332642eb-5c53-4be7-8819-66dfeded0aa2?resizing_type=fit)

Twisting along the X-axis:

[![Honeycomb layout twisted along X axis](https://dev.epicgames.com/community/api/documentation/image/fd316539-faf2-49be-97ac-c03e85aff85a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fd316539-faf2-49be-97ac-c03e85aff85a?resizing_type=fit)

| Honeycomb Layout Properties | Description |
| --- | --- |
| **Plane** | Determines the axes used to define the plane on which the hexagonal layout clones spawn. Options are:   * XY * YZ * XZ |
| **Width Count** | The number of clones in the layout horizontally. |
| **Height Count** | The number of clones in the layout vertically. |
| **Width Offset** | Controls the horizontal position offset. |
| **Height Offset** | Controls the vertical position offset. |
| **Width Spacing** | Controls the spacing between clones horizontally. |
| **Height Spacing** | Controls the spacing between clones vertically. |
| **Twist Factor** | Controls how much twist to apply to the Honeycomb layout, in percentage. 100% is a 180 degree twist. |
| **Twist Axis** | Determines which axis to use to twist the layout (X, Y, or Z). |

##### Mesh

The Mesh layout gives you a way to populate clones along a static mesh or skeletal mesh. You can select these under the **Asset** property. The example below shows the selected number of clones populating evenly over each of the static mesh’s vertices.

[![Mesh layout](https://dev.epicgames.com/community/api/documentation/image/605f2b28-e8df-4520-b0eb-986ebc8321d4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/605f2b28-e8df-4520-b0eb-986ebc8321d4?resizing_type=fit)

You are able to sample the mesh in a variety of ways:

[![Mesh Sample Data options](https://dev.epicgames.com/community/api/documentation/image/4b9d831b-ba0b-43c6-934a-80b33b55ba9d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4b9d831b-ba0b-43c6-934a-80b33b55ba9d?resizing_type=fit)

Here is an example sampling triangles:

[![Mesh sampled using triangles](https://dev.epicgames.com/community/api/documentation/image/65ce7329-f8d4-41ac-ad28-37364b6b368b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/65ce7329-f8d4-41ac-ad28-37364b6b368b?resizing_type=fit)

Here is an example using a skeletal mesh:

[![Using a skeletal mesh](https://dev.epicgames.com/community/api/documentation/image/fa134ab9-cb55-4dae-b660-a2b27dd9df0a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fa134ab9-cb55-4dae-b660-a2b27dd9df0a?resizing_type=fit)

| Mesh Layout Properties | Description |
| --- | --- |
| **Sample Actor** | Identifies the actor used as the mesh source. |
| **Asset** | Determines the type of asset. Options are:   * Static Mesh * Skeletal Mesh |
| **Count** | The number of clones on the mesh. |
| **Sample Data** | Determines how the Motion Design system samples the mesh. Options are:   * Vertices * Triangles * Sockets (skeletal mesh only) * Bones (skeletal mesh only) * Sections |

##### Spline

When using the Spline Layout, you can use a spline actor created using the Motion Design toolbox as the Sample Actor, and clone that actor repeatedly along the path of the spline. You can orient the clones to rotate along with the curve using a combination of the **Orient Mesh** toggle, which causes the clones to follow the spline's tangent, and rotating the individual static mesh 90 degrees on the Y axis. The image below shows the result of using such a combination.

[![Spline layout](https://dev.epicgames.com/community/api/documentation/image/fa1ba742-8888-45f5-a90b-c99cc82a6b48?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fa1ba742-8888-45f5-a90b-c99cc82a6b48?resizing_type=fit)

The image below shows the same actor without the Orient Mesh toggle enabled and default transforms.

[![Spline with Orient Mesh disabled and default transforms](https://dev.epicgames.com/community/api/documentation/image/036becbd-5dad-4057-9a78-e87ffa5ff868?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/036becbd-5dad-4057-9a78-e87ffa5ff868?resizing_type=fit)

| Spline Layout Properties | Description |
| --- | --- |
| **Count** | The number of clones on the spline. |
| **SampleActor** | The spline actor used for the clones. |
| **Orient Mesh** | Forces clones to follow the spline's tangent. |

##### Sphere Random

The Sphere Random layout spreads out your mesh clones around the surface of the sphere in a random, chaotic manner. This is controlled by the **Distribution**, **Latitude**, and **Longitude** settings. Enabling **Orient Mesh** causes all the clones to direct themselves around the surface of the sphere along the forward vector. In the example below, the forward vector comes **from** the center of the sphere.

[![Sphere Random layout](https://dev.epicgames.com/community/api/documentation/image/140a5551-b0f8-4eff-b398-a09bc17936b3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/140a5551-b0f8-4eff-b398-a09bc17936b3?resizing_type=fit)

Without **Orient Mesh** enabled, you will end up with a result like the image below, where all clones will follow the forward vector (the X axis in this example):

[![Sphere Random with clones all following forward vector](https://dev.epicgames.com/community/api/documentation/image/9f16feae-38a5-4993-91a1-cdeaffcd05d8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9f16feae-38a5-4993-91a1-cdeaffcd05d8?resizing_type=fit)

A .5 value for both **Longitude** and **Latitude** forces the clones to cover a quarter of the sphere. You can increase your clone count to a large value (800 in the example shown) to demonstrate this more effectively.

[![Longitude and latitude both halved to quarter the sphere](https://dev.epicgames.com/community/api/documentation/image/635a0d51-4dd2-4d74-ae08-1d0f46d52bed?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/635a0d51-4dd2-4d74-ae08-1d0f46d52bed?resizing_type=fit)

Increasing the **Scale** setting reduces the density of your clones by expanding the total area that they cover.

Small Scale value:

[![Smaller scale, higher clone density](https://dev.epicgames.com/community/api/documentation/image/8f716c82-3938-4b25-a5f2-b7a509eade05?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8f716c82-3938-4b25-a5f2-b7a509eade05?resizing_type=fit)

Larger Scale Value:

[![Larger scale, lower clone density](https://dev.epicgames.com/community/api/documentation/image/81c3ff55-02d5-4d4a-adc6-8b8f0385453c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/81c3ff55-02d5-4d4a-adc6-8b8f0385453c?resizing_type=fit)

Changing the **Rotation** value rotates the group of clones.

| Sphere Random Layout Properties | Description |
| --- | --- |
| **Count** | The number of clones in the sphere. |
| **Radius** | The radius of the sphere, which controls how spread out the clones are. |
| **Distribution** | Determines how evenly spread the clones are. |
| **Longitude** | Determines how much the cloners cover the sphere horizontally in degrees. |
| **Latitude** | Determines how much the cloners cover the sphere vertically in degrees. |
| **Orient Mesh** | Enable this to orient all the clones on the surface of the sphere layout. |
| **Rotation X / Y / Z** | Determines the rotation of the sphere in degrees towards the X, Y, or Z axis. Does not directly rotate the cloner actors. |
| **Scale X / Y / Z** | Scales the layout sphere on the X, Y, or Z axis. Does not scale the cloner actors. |

#### Range

[![Cloner category Range properties](https://dev.epicgames.com/community/api/documentation/image/22a92b0e-2416-4bf2-a900-600948a88498?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/22a92b0e-2416-4bf2-a900-600948a88498?resizing_type=fit)

Since every clone is a particle, you can use the **Offset**, **Rotation**, and **Scale** settings to manipulate the initial transforms for the clone. This manipulation can be uniform or non-uniform. You can also randomize the initial placement from the current layout. The image below shows an example of just modifying the **ScaleMin** and **ScaleMax** properties to scale the sphere clones between 0.001 and 2.613.

[![Sphere with uniformly scaled clones of different sizes](https://dev.epicgames.com/community/api/documentation/image/fe895304-d8f1-4cc3-9848-f2b21afb4f4d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fe895304-d8f1-4cc3-9848-f2b21afb4f4d?resizing_type=fit)

You can disable the ScaleUniformEnabled property to cause the clones to have more random shapes.

[![Sphere with non-uniformly scaled clones of different sizes](https://dev.epicgames.com/community/api/documentation/image/dcd582c9-3906-47fd-b180-3242e5c6d36e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dcd582c9-3906-47fd-b180-3242e5c6d36e?resizing_type=fit)

| Range Properties | Description |
| --- | --- |
| **Enabled** | When enabled, cloners use Range features. |
| **OffsetMin X / Y / Z** | Determines the minimum offset on the X, Y, or Z axis. |
| **OffsetMax X / Y / Z** | Determines the maximum offset on the X, Y, or Z axis. |
| **RotationMin X / Y / Z** | Determines the minimum rotation in degrees on the X, Y, or Z axis. |
| **RotationMax X / Y / Z** | Determines the maximum rotation in degrees on the X, Y, or Z axis. |
| **ScaleUniformEnabled** | When enabled, clones scale uniformly. |
| **ScaleMin X / Y / Z** | Determines the minimum scaling on the X, Y, or Z axis. |
| **ScaleMax X / Y / Z** | Determines the maximum scaling on the X, Y, or Z axis. |

#### Step (Cloner)

[![Offset transforms using the Cloner category Step property](https://dev.epicgames.com/community/api/documentation/image/86378c8b-15c7-4adb-8a6d-06fd96e5cf4a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/86378c8b-15c7-4adb-8a6d-06fd96e5cf4a?resizing_type=fit)

With the **Step** property, you can set the scale and rotation of your clones in an offset manner. To use the effect, the clone count must be higher than 1. The scale and rotation accumulate per clone.

| Step Properties | Description |
| --- | --- |
| **Enabled** | When enabled, cloners use the Step feature. |
| **Rotation X / Y / Z** | Determines the rotation in degrees on the X, Y, or Z axis. |
| **Scale X / Y / Z** | Determines the scaling on the X, Y, or Z axis. |

### Emission

The **Emission** category properties provide ways for you to spawn new clones, and then have them despawn, controlling the clone spawn rate, number, and duration.

[![Emission category properties](https://dev.epicgames.com/community/api/documentation/image/b178e66c-a5ac-476c-a56d-bdde68759b39?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b178e66c-a5ac-476c-a56d-bdde68759b39?resizing_type=fit)

#### Spawn

You can use the **Spawn** feature when you want to create dynamic simulations by having your clones respawn after their lifetime expires. If you want your clones to respawn continuously, change the **Emission Mode** from **Once** to **Infinite**, then enable the [Lifetime](https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine#lifetime) feature. You can edit the aesthetic by changing the **Emission Style** property from **Instant** to **Rate**. The **Emission Rate** property determines how many clones appear per second.

If you only want to spawn a fixed number of clones rather than an unlimited number, you can change the value of the Emission Mode property from **Infinite** to **Multiple** and set the **Emission Count** value to whatever you want.

| Spawn Properties | Description |
| --- | --- |
| **Emission Mode** | Determines whether clones spawn infinitely or a fixed number of times. Options are:   * **Once**: Clones spawn once. * **Infinite**: Clones spawn infinitely. * **Multiple**: Clones spawn a fixed number of times. |
| **Emission Count** | Determines how many spawn loops for cloners will occur when Emission Mode is set to Multiple. |
| **Emission Interval** | Determines the intervals between cloner spawns. |
| **Emission Style** | Determines how quickly clones spawn. Options are:   * **Instant**: All clones spawn immediately at the start of a loop. * **Rate**: Clones spawn over time. |
| **Rate** | Determines how many clones spawn per second. Only used when BehaviorMode is set to Rate. |

#### Lifetime

When enabled, the Lifetime options provide a way for you to despawn clones after a period of time.

The image below depicts the beginning of the clones' lifetime.

[![Lifetime property clones starting state](https://dev.epicgames.com/community/api/documentation/image/07cd75e7-8755-4a54-8145-fc2024e9c9f5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/07cd75e7-8755-4a54-8145-fc2024e9c9f5?resizing_type=fit)

Clones begin to disappear as time passes.

[![Clones disappearing as lifetime ends](https://dev.epicgames.com/community/api/documentation/image/67ae347a-fab4-4e4e-b142-2436c97dd05f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/67ae347a-fab4-4e4e-b142-2436c97dd05f?resizing_type=fit)

[![Example lifetime settings](https://dev.epicgames.com/community/api/documentation/image/ca2b2083-6b4c-4979-bd65-4e21ff8df831?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ca2b2083-6b4c-4979-bd65-4e21ff8df831?resizing_type=fit)

The **Min** and **Max** properties control the minimum and maximum time that a clone is active. Modifying either property restarts the timer.

The **ScaleEnabled** toggle gives you access to the list of prescribed curve **Templates**.

[![Lifetime ScaleEnabled options](https://dev.epicgames.com/community/api/documentation/image/9da8a235-4ad9-438f-8aae-abe6bc8fa25f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9da8a235-4ad9-438f-8aae-abe6bc8fa25f?resizing_type=fit)

| Lifetime Properties | Description |
| --- | --- |
| **Enabled** | Cloners will use Lifetime features when you enable this option. |
| **Min** | The minimum time a cloner will be active. |
| **Max** | The maximum time a cloner will be active. |
| **ScaleEnabled** | When enabled, the curve templates are available. |
| Templates |  |
| --- | --- |
| **Linear Ramp Up** | Lifetime curve template. |
| **Linear Ramp Down** | Lifetime curve template. |
| **Drop Off** | Lifetime curve template. |
| **Ease In** | Lifetime curve template. |
| **Pulse Out** | Lifetime curve template. |
| **Smooth Ramp Up** | Lifetime curve template. |
| **Smooth Ramp Down** | Lifetime curve template. |
| **Ramp Up Ramp Down** | Lifetime curve template. |

#### Progress

You can use the **Progress** settings to hide or reveal clones. It can reveal clones from top to bottom, or bottom to top when the **Invert Progress** option is enabled.

[![Emissions category Progress properties](https://dev.epicgames.com/community/api/documentation/image/89035638-0c02-40c4-9c2b-e1d9f2bf301f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/89035638-0c02-40c4-9c2b-e1d9f2bf301f?resizing_type=fit)

Clones at .5 Progress Value:

[![Progress at half](https://dev.epicgames.com/community/api/documentation/image/61ff888e-7696-4e12-ac1e-f682d13cdec6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/61ff888e-7696-4e12-ac1e-f682d13cdec6?resizing_type=fit)

Clones at .5 Progress Value with **Invert Progress** enabled.

[![Inverted progress at half](https://dev.epicgames.com/community/api/documentation/image/44a22779-f8f2-4c8a-8b85-dabef7aa45d1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/44a22779-f8f2-4c8a-8b85-dabef7aa45d1?resizing_type=fit)

| Progress Properties | Description |
| --- | --- |
| **Invert Progress** | When enabled, clones are revealed from bottom to top instead of top to bottom. |
| **Progress** | Defines the proportion of the clones that are hidden or revealed. |

### Physics

Because each clone is also a particle, particle physics provides a way for you to have your clones collide with both surfaces and each other.

#### Surface Collision Enabled

By enabling the **Surface Collision Enabled** property, you can have your clones collide with surfaces in your level (in the example below, the floor). The images below provide examples of each case.

Before enabling collision:

[![No collision physics](https://dev.epicgames.com/community/api/documentation/image/52d5876a-6ef4-42a4-a7d0-1d3f86f7995e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/52d5876a-6ef4-42a4-a7d0-1d3f86f7995e?resizing_type=fit)

After enabling the **Surface Collision Enabled** checkbox, and moving the position of the cloner actor toward the floor:

[![Surface collision enabled only, clones collided with surface](https://dev.epicgames.com/community/api/documentation/image/990e5625-fc43-47a2-ab4f-550ed88ba49b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/990e5625-fc43-47a2-ab4f-550ed88ba49b?resizing_type=fit)

Because in the example we used only the Surface Collision Enabled property, moving the clones up again does not cause them to change relative position any further, because they don't collide with each other. The image below shows this effect:

[![Surface collision only, clones moved up again](https://dev.epicgames.com/community/api/documentation/image/e07971d8-cb17-4053-a1a5-713024ce9334?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e07971d8-cb17-4053-a1a5-713024ce9334?resizing_type=fit)

#### Particle Collision Enabled

You can also use the **Particle Collision Enabled** property to have your cloners collide with each other:

[![Particle collision enabled, clones colliding with each other](https://dev.epicgames.com/community/api/documentation/image/0e23b329-f288-4284-bdbb-39ff5cb0829b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0e23b329-f288-4284-bdbb-39ff5cb0829b?resizing_type=fit)

You can use the Surface Collision Enabled and Particle Collision Enabled properties together. When you do so, clones react both to colliding with the floor and each other, resulting in a clump like the following image:

[![Surface collision and particle collision enabled](https://dev.epicgames.com/community/api/documentation/image/c1e3ba35-cf06-4395-b64c-a7df68c24eaa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c1e3ba35-cf06-4395-b64c-a7df68c24eaa?resizing_type=fit)

#### Collision Velocity Enabled / Collision Iterations

When you want to calculate the physics after the collision has occurred, you can take particle interaction even further using the **Collision Velocity Enabled** property.

You can enhance the precision of the interaction with the **Collision Iterations** property, which determines how frequently the collision solver process repeats; higher values mean more precise collisions, but impacts system performance.

[![Collision Velocity Enabled and Collision Iterations](https://dev.epicgames.com/community/api/documentation/image/ebde5515-1a95-495c-a06d-7dcfb35dcef4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ebde5515-1a95-495c-a06d-7dcfb35dcef4?resizing_type=fit)

#### Collision Grid Size / Collision Grid Resolution

The **Collision Grid Size** and **Collision Grid Resolution** properties directly impact how many of the clones are affected by the collision. A large value, relative to the size of the area you are trying to cover, will affect a higher number of your clones. A low value produces a result similar to the image below. In this example, any clone that falls outside of a 200, 200, 200 grid volume does not have collision physics:

[![Particle collision with low collision grid size](https://dev.epicgames.com/community/api/documentation/image/52fd379a-a7c4-41cc-b54a-6d4a23b24864?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/52fd379a-a7c4-41cc-b54a-6d4a23b24864?resizing_type=fit)

Adjusting the Collision Grid Size to a higher value provides more volume in which particles collide, resulting in something like the image below:

[![Particle collision with high collision grid size](https://dev.epicgames.com/community/api/documentation/image/234af6af-ca96-4f16-87d8-284ccdc4c0ed?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/234af6af-ca96-4f16-87d8-284ccdc4c0ed?resizing_type=fit)

A low Collision Grid Resolution value results in collision physics applied to large chunks of your clones collectively, rather than as individual particles. A higher Collision Grid Resolution results in collision physics calculations applied properly to individual clones.

#### Collision Radius Mode

The **Collision Radius Mode** property determines how the overall radius is calculated for each attached actor. In the example in the image above, there are two actors - the torus and the sphere.

* **Extent Length**: Calculates from the center of the mesh to the furthest point. This is useful for unevenly sized shapes.
* **Manual**: Provides a way to define the size of each mesh regardless of the *actual* size of the mesh. This is useful when you want some padding, or to reduce the calculated size regardless of its actual size.
* **Min Extent**: Calculates the shortest side of the referenced mesh.
* **Max Extent**: Calculates the longest side of the referenced mesh.

#### Mass Min / Mass Max

**Mass Min** and **Mass Max** define the overall weight of the particle, in kilograms (kg).

| Physics Properties | Description |
| --- | --- |
| **Surface Collision Enabled** | When enabled, clones collide with surfaces in your level. |
| **Particle Collision Enabled** | When enabled, clones collide with each other. |
| **Collision Velocity Enabled** | When enabled, clones bounce away from collisions with added velocity. |
| **Collision Iterations** | Determines how many collisions are calculated for clones. |
| **Collision Grid Resolution** | Determines how precisely collision physics are applied to clones. |
| **Collision Grid Size X / Y / Z** | Defines the volume in which clones collide, using the X / Y / Z axes. |
| **Collision Radius Mode** | Determines how the overall radius is calculated for each attached actor. Options are:   * Extent Length * Manual * Min Extent * Max Extent |
| **Mass Min** | Defines the minimum weight of a particle (clone), in kg. |
| **Mass Max** | Defines the maximum weight of a particle (clone), in kg. |

### Rendering

You can use the cloners’ **Rendering** settings to control the clones' general visibility and orientation after you set all the other details in the other Cloner settings, depending on the values you choose for several additional properties in this category.

#### Mesh Render Mode

There are several different mesh render modes to choose from.

##### Iterate

Iterates through each of the attached meshes.

[![Iterate Mesh Render Mode](https://dev.epicgames.com/community/api/documentation/image/d5f5b37d-fc1e-4b76-b2ff-b4531c32cb13?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d5f5b37d-fc1e-4b76-b2ff-b4531c32cb13?resizing_type=fit)

##### Random

Arranges the attached meshes randomly.

[![Random Mesh Render Mode](https://dev.epicgames.com/community/api/documentation/image/13163ab7-4936-4e98-bd1f-02bd3dd33524?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/13163ab7-4936-4e98-bd1f-02bd3dd33524?resizing_type=fit)

##### Blend

Blends meshes based on the total count and the attached meshes.

[![Blend Mesh Render Mode](https://dev.epicgames.com/community/api/documentation/image/64e0d569-5d82-4915-8e7a-d2897fc2e415?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/64e0d569-5d82-4915-8e7a-d2897fc2e415?resizing_type=fit)

#### Mesh Facing Mode

You can determine the direction the clones face using the **Mesh Facing Mode**.

[![Mesh Facing Mode options](https://dev.epicgames.com/community/api/documentation/image/5d22d1d3-67b7-4015-a827-e3c18fcbb7db?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5d22d1d3-67b7-4015-a827-e3c18fcbb7db?resizing_type=fit)

##### Default

The **Default** option uses the forward vector as seen in the example image below. The arrows are all facing the forward vector and will not rotate.

[![Default Mesh Facing Mode](https://dev.epicgames.com/community/api/documentation/image/5cba6365-f9db-4cc3-bcfc-5cbaea87d1e7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5cba6365-f9db-4cc3-bcfc-5cbaea87d1e7?resizing_type=fit)

##### Velocity

Orients the clones based on their velocity direction. As they rotate around the sphere, they maintain orientation in the direction of their rotation.

[![Velocity Mesh Facing Mode](https://dev.epicgames.com/community/api/documentation/image/8bde13be-0101-43dd-a6bc-de5026bc2691?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8bde13be-0101-43dd-a6bc-de5026bc2691?resizing_type=fit)

##### Camera Position

Orients all clones to face the camera. For example, the arrows in the GIF below only show the front and none of the tail because they fully face the camera at all times.

##### Camera Plane

Orients all clones to point toward the plane where the camera is, rather than directly at the camera itself.

[![Clones oriented towards camera plane](https://dev.epicgames.com/community/api/documentation/image/dd324d9e-1429-431c-8e62-06280b050835?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dd324d9e-1429-431c-8e62-06280b050835?resizing_type=fit)

#### Meshes Cast Shadows

You can make meshes cast shadows by enabling the **Meshes Cast Shadows** property.

#### Default Meshes

If there is no mesh attached below the cloner actor in the Details panel, you can set the default meshes that appear instead. You can do this by using the **Default Meshes** option. In this example, we set it to SM\_Ball\_01.

[![image alt text](https://dev.epicgames.com/community/api/documentation/image/2207ad41-29e0-4dc1-9a2b-797975a8246b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2207ad41-29e0-4dc1-9a2b-797975a8246b?resizing_type=fit)

#### Visualize Effectors

The **Visualize Effectors** property toggles using a default material for all clones, so that you can evaluate the results of using effectors more clearly by temporarily removing any confounding colors and patterns added by your material.

#### Use Override Material

You can define a custom material for all clones by enabling the **User Override Material** property.

##### Override Material

Use this property to select your override material. You can select any material from your Content Browser.

##### Edit with Material Designer

When you have selected an override material, you can edit it by clicking **Edit with Material Designer**. This opens your material in the **Motion Design Material Designer** in a separate panel.

##### Set Translucent Priority

You can enable this property to use the **Set Translucent Priority** feature.

| Rendering Properties | Description |
| --- | --- |
| **Mesh Render Mode** | Determines the render mode for the cloners. Options are:   * Iterate * Random * Blend |
| **Mesh Facing Mode** | When enabled, the clones always face the camera. Options are:   * Default * Velocity * Camera Position * Camera Plane |
| **Mesh Cast Shadows** | When enabled, the clone meshes cast shadows. |
| **Default Meshes** | Use this array to set the default meshes used for the clones when there is no mesh attached below the cloner. |
| **Visualize Effectors** | When enabled, a default material is used for all clones to simplify viewing effectors. |
| **Use Override Material** | When enabled, you can define a custom material used for all clones. Has several sub-properties and options you can use to define your material:   * **Override Material** * **Edit with Material Designer** * **Set Translucent Priority** |

### Utilities

There will be occasions where you don’t want a cloner to remain in a "live" state, and only need it to exist with the settings that you’ve established. Several of the utilities described below are useful in that use-case.

[![Cloner actor Utilities category](https://dev.epicgames.com/community/api/documentation/image/bdba8acc-ac41-459f-9531-545897a2f1d3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bdba8acc-ac41-459f-9531-545897a2f1d3?resizing_type=fit)

For example, if you create something with the cloner and you want actual actors in the scene instead of particles, you can export your cloner creation by converting them into static meshes or dynamic meshes. You can then use those meshes (including instances) like any other mesh, with all the advantages of those asset types. It's like taking a snapshot of the particles, and transforming the results into actors in your level.

#### Create Default Actor Attached

If you deleted the default actor that spawns when you create a cloner, clicking this utility respawns that actor using the actor currently set as the default. If you didn’t change the current default actor, this utility spawns a standard cube static mesh.

If you do not have a mesh attached below the cloner, you can set the default meshes that appear instead, using the **Default Meshes** option under the **Rendering** tab. In the example in the image below, we set it to SM\_Ball\_01.

[![Example Default Mesh settings](https://dev.epicgames.com/community/api/documentation/image/2e321663-852c-4c28-8b0a-dde5fc8c76d0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2e321663-852c-4c28-8b0a-dde5fc8c76d0?resizing_type=fit)

[![Example Default Mesh](https://dev.epicgames.com/community/api/documentation/image/0462bc1c-5379-484f-9671-8189b47f834d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0462bc1c-5379-484f-9671-8189b47f834d?resizing_type=fit)

#### Convert to Static Meshes

Clicking this utility requires you to specify a save location for the static mesh output.

[![Specify save location](https://dev.epicgames.com/community/api/documentation/image/aa3f224d-a629-4d48-ad49-b4401f210abd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/aa3f224d-a629-4d48-ad49-b4401f210abd?resizing_type=fit)

Instances of each clone are saved as a static mesh and placed where they originated.

[![Saved static meshes in the outliner](https://dev.epicgames.com/community/api/documentation/image/80b3187c-031b-4e32-9cd9-01db9bed6098?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/80b3187c-031b-4e32-9cd9-01db9bed6098?resizing_type=fit)

#### Convert to Static Mesh

This utility condenses all clones into a single static mesh.

The image below shows an example of a cloner and clones before converting to a static mesh:

[![Before converting to a static mesh](https://dev.epicgames.com/community/api/documentation/image/ab116492-88fe-4ec2-b63d-5fac69d2bf0a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ab116492-88fe-4ec2-b63d-5fac69d2bf0a?resizing_type=fit)

After using the Convert to Static Mesh utility, this static mesh output appears in your Content Drawer:

[![Static mesh output in the Content Drawer](https://dev.epicgames.com/community/api/documentation/image/d595a76e-386a-402b-bd24-0097363342c2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d595a76e-386a-402b-bd24-0097363342c2?resizing_type=fit)

The newly-created static mesh is given an auto-generated name, using the format `SM_{ClonerName}_{MeshUniqueId}`. You can rename the static mesh in the Content Drawer.

#### Convert to Instanced Static Mesh

Converts all children of the cloner into an **Instanced Static Mesh**. This might result in performance improvements.

#### Convert to Dynamic Mesh / Convert to Dynamic Meshes

These utilities are similar to the utilities for converting to static meshes described previously, but convert the clones to dynamic meshes instead. **Dynamic Meshes** are described in the documentation for **Modifiers**.

#### Create Cloner Sequencer Tracks

You can use this to link a cloner to Sequencer, which helps you to scrub your colliding, cloned animations linearly. To accomplish this, the animation is cached.

The Effector Collision Velocity Physics property is a good way to experiment with this feature. Enable the property first, then set up your clones before creating the track for Sequencer, as shown in the following images:

[![Effector Collision Velocity Physics property settings](https://dev.epicgames.com/community/api/documentation/image/851ad4b5-d2a5-4340-9a12-bf8b1b399701?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/851ad4b5-d2a5-4340-9a12-bf8b1b399701?resizing_type=fit)

[![Create Cloner Sequencer Tracks button](https://dev.epicgames.com/community/api/documentation/image/386f629a-8bcb-4c75-b811-080692ebf044?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/386f629a-8bcb-4c75-b811-080692ebf044?resizing_type=fit)

When you create the Sequencer track, the result should be similar to the following example:

[![Example Sequencer track](https://dev.epicgames.com/community/api/documentation/image/ed7a7e6f-5960-4a6e-bfdf-2739c906f5cf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ed7a7e6f-5960-4a6e-bfdf-2739c906f5cf?resizing_type=fit)

## Effector Actors

You can use **effectors** to modify the various transform values of your clones. You can set this to be done from multiple points of engagement by using multiple effectors all linked to your cloner system. Examples of results you can achieve using effectors include:

* Moving clones in different directions.
* Randomizing clone positions with noise patterns.
* Manipulating clone transforms by offsetting, rotating, and scaling them.

The main requirement is that the clones must be within the effector’s area of influence.

### Creating an Effector

There are two ways to create an effector:

* Select an existing cloner, then click the **Spawn Linked Effector** button in the Details panel.

  [![Spawn Linked Effector on an existing cloner](https://dev.epicgames.com/community/api/documentation/image/852d6abe-3315-4df5-9fbc-401d19679945?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/852d6abe-3315-4df5-9fbc-401d19679945?resizing_type=fit)
* Place an effector directly by double-clicking **Effector Actor** on your **Motion Design** toolbar, or by using the **Place Actors** tab and searching for the Motion Design Effector Actor.

  [![Place an Effector Actor directly](https://dev.epicgames.com/community/api/documentation/image/83a94776-153a-4aeb-9c6a-986abc3b588e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/83a94776-153a-4aeb-9c6a-986abc3b588e?resizing_type=fit)

If you only have a single cloner, we recommend the first method.

If you want to use multiple effectors, then you need to create an **Effector** actor, name it, and add it to the **Effectors** array on your cloner.

[![Creating multiple effectors](https://dev.epicgames.com/community/api/documentation/image/f887c70b-db08-440d-ae5f-06a503606035?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f887c70b-db08-440d-ae5f-06a503606035?resizing_type=fit)

[![Adding effectors to your cloner array](https://dev.epicgames.com/community/api/documentation/image/df5a113c-067c-4df6-b830-52e62f70e55e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/df5a113c-067c-4df6-b830-52e62f70e55e?resizing_type=fit)

After adding and assigning the new effector, you can set up your project to resemble the following example. The red area shows the original effector, and the new effector is blue.

[![Using multiple effectors together](https://dev.epicgames.com/community/api/documentation/image/66963681-0793-412e-85a7-b0856798caec?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/66963681-0793-412e-85a7-b0856798caec?resizing_type=fit)

### General

[![Effector actor General category](https://dev.epicgames.com/community/api/documentation/image/d225bd85-1d34-4a85-9697-97670bc72a82?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d225bd85-1d34-4a85-9697-97670bc72a82?resizing_type=fit)

The General category shows standard settings for transforms applied to the Effector actor.

| General Properties | Description |
| --- | --- |
| Location | Standard location transform, using X, Y, and Z coordinates. |
| Rotation | Standard rotation transform, using X, Y, and Z coordinates. |
| Scale | Standard scale transform, using X, Y, and Z coordinates. |
| Mobility | Determines the [actor mobility](https://dev.epicgames.com/documentation/en-us/unreal-engine/actor-mobility-in-unreal-engine), similar to other UE actors. Options are:   * Static * Stationary * Movable |

### Effector

In the **Effector** category, the **Enabled** checkbox determines whether you want to use the tool. To use effectors, make sure the checkbox has a check.

[![Effector actor Effector category](https://dev.epicgames.com/community/api/documentation/image/2c944905-8d91-42ad-88d6-4349995e2692?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2c944905-8d91-42ad-88d6-4349995e2692?resizing_type=fit)

The **Magnitude** property determines the strength of the effector's impact on the clones within its range.

You can use the **Color** property to colorize the clones your effector is affecting. If you don’t want to colorize them, you can set this property to white. You can use the Unreal Engine color picker to select the color, or just enter RGBA values directly.

Under the **Advanced** section, you can:

* Control the visibility of your effector's inner and outer boundaries in the viewport using the **Visualizer Sprite Visible** property
* Control the visibility of the visualizer component under the Effector actor in the Details panel using the **Visualizer Component Visible** property.

Visualizer Sprite Visible enabled:

[![Visualizer sprite enabled, boundaries showing](https://dev.epicgames.com/community/api/documentation/image/147a7626-f85c-414b-901e-cc51c71c640c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/147a7626-f85c-414b-901e-cc51c71c640c?resizing_type=fit)

Visualizer Sprite Visible disabled:

[![Visualizer sprite disabled, boundaries hidden](https://dev.epicgames.com/community/api/documentation/image/aea44502-296e-4d6e-8f48-1321306e9d48?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/aea44502-296e-4d6e-8f48-1321306e9d48?resizing_type=fit)

The **Channel Data Identifier** property is an advanced feature that provides a way for you to use effectors with custom projects outside Motion Design. For example, advanced users could build their own custom systems using Niagara modules that can be affected by Motion Design effectors using the effector's data channel. The values are transient, and can be different every time the world is reloaded.

| Effector Category Properties | Description |
| --- | --- |
| **Enabled** | Enables using effectors. |
| **Magnitude** | Determines the strength of the effector'simpact on the clones within its range. |
| **Color** | Standard RGBA color selection using the color picker. |
| **Advanced** |  |
| **Visualizer Component Visible** | When enabled, the visualizer component is visible in the Details panel. |
| **Visualizer Sprite Visible** | When enabled, the visualizer sprite is visible in the viewport. |
| **Channel Data Identifier** | Identifies effectors for use with custom systems. |

### Forces

You can use **Forces** to animate your clones without the need for keyframes, instead relying on Niagara physics. There are several methods to animate within the Effector system, which you can combine as desired. The settings for the various Forces options are only accessible when the associated Force is enabled.

[![Effector actor Forces category](https://dev.epicgames.com/community/api/documentation/image/6d89d4a3-3708-419a-8618-bca922b243c9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6d89d4a3-3708-419a-8618-bca922b243c9?resizing_type=fit)

| Forces Properties | Description |
| --- | --- |
| **Forces Enabled** | Enables the Forces effector options. |
| **Orientation Force Enabled** | Enables the Orientation Force and related settings. |
| **Vortex Force Enabled** | Enables the Vortex Force and related settings. |
| **Curl Noise Force Enabled** | Enables the Curl Noise Force and related settings. |
| **Attraction Force Enabled** | Enables the Attraction Force and related settings. |
| **Gravity Force Enabled** | Enables the Gravity Force and related settings. |
| **Drag Force Enabled** | Enables the Drag Force and related settings. |
| **Vector Noise Force Enabled** | Enables the Vector Noise Force and related settings. |

#### Orientation Force

[![Orientation Force properties](https://dev.epicgames.com/community/api/documentation/image/516da96c-89d3-4fad-8a21-528704fe45a9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/516da96c-89d3-4fad-8a21-528704fe45a9?resizing_type=fit)

This Forces option influences the orientation of the clones at a constant rate, and spins them faster depending on how close they are to the center of the **Inner Radius**.

In this example, the darker green area that the effector is reaching is twirling the shapes at a faster rate than the greyer shapes based on their intersection with the inner radius of the effector. If the clones are outside of the inner and outer boundaries, they will not spin at all.

[![Orientation Force ring of toruses example](https://dev.epicgames.com/community/api/documentation/image/b392b1f4-b0e8-4ea7-9a60-17a30eeb9d50?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b392b1f4-b0e8-4ea7-9a60-17a30eeb9d50?resizing_type=fit)

You can combine the **Orientation Force Rate**, **Orientation Force Min**, and **Orientation Force Max** properties to manipulate where the affected clones are facing and how often they cycle. The Orientation Rate changes the speed of rotation, while the Orientation Force Min and Max regulate the cycle speed.

[![Orientation Force spinning example](https://dev.epicgames.com/community/api/documentation/image/7d9a5a06-7497-4370-b9d5-2e33f9e420b6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7d9a5a06-7497-4370-b9d5-2e33f9e420b6?resizing_type=fit)

| Orientation Force Properties | Description |
| --- | --- |
| **Orientation Force Rate** | Determines the rotation speed of the clones. |
| **Orientation Force Min X / Y / Z** | The minimum force applied to clones along the specified axis. |
| **Orientation Force Max X / Y / Z** | The maximum force applied to clones along the specified axis. |

#### Vortex Force

[![Vortex Force properties](https://dev.epicgames.com/community/api/documentation/image/1661e69a-fe13-47ca-a7e9-85088bcc5296?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1661e69a-fe13-47ca-a7e9-85088bcc5296?resizing_type=fit)

Early in the process, the clones will begin to drift after increasing the force along the X axis.

This rotates the clones according to Vortex Force Amount and around a Vortex Force Axis. The values in the GIF above combined with the size of the effector result in a relatively slow reaction that sends the clones offscreen.

| Vortex Force Properties | Description |
| --- | --- |
| **Vortex Force Amount** | Determines the force of rotation applied to the clones. |
| **Vortex Force Axis X / Y / Z** | Determines the axis of rotation. The magnitude of the different axis determines the relative position of the final axis in relation to the cardinal axes, with the result normalized to 1. |

#### Curl Noise Force

The two properties here are **Curl Noise Force Strength** and **Curl Noise Force Frequency**.

* Increasing **Curl Noise Force Strength** increases the acceleration affecting the clones.
* **Curl Noise Force Frequency** sends the clones in different directions. The higher the value, the more time it will take the clones to disperse, because there is more randomness in the direction of the force applied to the clones.

The results are deterministic, not random, and depend on the cloner's seed. When the same seed value repeats for the same arrangement of layout and cloners, it always has the same effect.

The image below shows the effect of a Curl Noise Force Frequency value of 1 after 2 seconds:

[![Curl Noise Frequency value of 1](https://dev.epicgames.com/community/api/documentation/image/2227065e-719a-47e4-8621-d81c9db4123f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2227065e-719a-47e4-8621-d81c9db4123f?resizing_type=fit)

Here is the same setup except with a **Curl Noise Force Frequency** value of 50 after 2 seconds:

[![Curl Noise Frequency value of 50](https://dev.epicgames.com/community/api/documentation/image/fc9dfb7f-6459-4906-9fd1-476715c89f81?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fc9dfb7f-6459-4906-9fd1-476715c89f81?resizing_type=fit)

| Curl Noise Force Properties | Description |
| --- | --- |
| **Curl Noise Force Strength** | Determines the magnitude of the force applied to clones. |
| **Curl Noise Force Frequency** | Determines the randomness of the force's direction. |

#### Attraction Force

Thia Force option causes your clones to flow toward the effector’s location. They will flow faster the closer they are to the inner radius of the effector. In the example below, the green area is the inner radius.

[![Attraction Force example](https://dev.epicgames.com/community/api/documentation/image/867e7943-70f3-4d6e-8d70-bc2e2124dc8d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/867e7943-70f3-4d6e-8d70-bc2e2124dc8d?resizing_type=fit)

The **Attraction Force Falloff** property decreases the speed of the particles as it gets closer to the outer boundary. In the example below, the outer boundary is represented by the red outer area.

| Attraction Force Properties | Description |
| --- | --- |
| **Attraction Force Strength** | Determines how quickly clones flow towards the center. |
| **Attraction Force Falloff** | Decreases particle speed closer to the outer boundary. |

#### Gravity Force

Using this forces clones to fall gradually depending on the inner/outer radius set in the **Shape** property.

The image below shows an example setup of clones before enabling **Gravity Force**.

[![Clones before enabling Gravity Force](https://dev.epicgames.com/community/api/documentation/image/942fd835-922a-4470-8351-aece5374cca2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/942fd835-922a-4470-8351-aece5374cca2?resizing_type=fit)

This image shows the same setup shortly after enabling Gravity Force:

[![Clones just after enabling Gravity Force](https://dev.epicgames.com/community/api/documentation/image/b33b9792-bdcc-4eae-b7ba-ec2b1b393987?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b33b9792-bdcc-4eae-b7ba-ec2b1b393987?resizing_type=fit)

Combining Gravity Force and Orientation Force produces an effect like in the image below:

[![Gravity Force abd Orientation Force combined example](https://dev.epicgames.com/community/api/documentation/image/f9d3ab7a-0456-4329-b462-50cd5327b844?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f9d3ab7a-0456-4329-b462-50cd5327b844?resizing_type=fit)

| Gravity Force Properties | Description |
| --- | --- |
| **Gravity Force Acceleration X / Y / Z** | Determines the magnitude of the acceleration along each axis.  A value of -981 on the Z axis approximates real world gravity (9.81 m/s/s downwards, or -981 in Unreal Units). |

#### Drag Force

You can use this to add drag and decrease the speed of your forces. If you use it in conjunction with another force like Vortex Force, increasing the Drag Force Linear property makes everything move slower.

The GIF below shows an example of what occurs when an effector with drag force moves off to the left, allowing the Vortex Force to take over.

| Drag Force Properties | Description |
| --- | --- |
| **Drag Force Linear** | Determines the magnitude of the linear drag force, which acts to slow down any linear movement of particles. |
| **Drag Force Rotational** | Determines the magnitude of the rotational drag force, which slows down any rotation of the particles. |

#### Vector Noise Force

This Forces option shifts particles in all directions with speed depending on the **Vector Noise Force Amount** property.

The results are deterministic, not random, and depend on the cloner's seed, so the same seed value repeated for the same arrangement of layout and cloners will always have the same effect.

[![Vector Noise Force example](https://dev.epicgames.com/community/api/documentation/image/761ce346-b553-4c98-9e58-f3fc2c26ba00?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/761ce346-b553-4c98-9e58-f3fc2c26ba00?resizing_type=fit)

| Vector Noise Force Properties | Description |
| --- | --- |
| **Vector Noise Force Amount** | Determines the magnitude of the Vector Noise Force. |

### Mode

There are four modes that you can use to influence an individual clone’s transforms. The effects of the Mode you choose depend on the [shape](https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine#shape) of the effector and the proximity of the clone.

| Mode Properties | Description |
| --- | --- |
| **Mode** | Choose which mode to use to affect clone transforms. Options are:   * Offset * Target * Noise Field * Push |

#### Offset

**Offset** applies standard transformation properties like Location, Rotation, and Scale to the clones within range of the effector. The image below shows an offset of the X axis value and a rotation of 80. This affects some effector Shape options more than others depending on their proximity to the Offset effector.

[![Offset Mode example](https://dev.epicgames.com/community/api/documentation/image/160a8207-8665-45b0-9aeb-d36d551a01be?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/160a8207-8665-45b0-9aeb-d36d551a01be?resizing_type=fit)

| Offset Mode Properties | Description |
| --- | --- |
| **Offset X / Y / Z** | Offsets the influence of the effector by the specified distance on the indicated axes. |
| **Rotation X / Y / Z** | Standard rotation transform, using X, Y, and Z coordinates, within the influence of the effector. |
| **Scale X / Y / Z** | Standard scale transform, using X, Y, and Z coordinates, within the influence of the effector. |

#### Target

By default, this mode automatically sets the **TargetActor** to the effector. All clones rotate to face the effector as long as they are within the inner or outer boundary of the effector type used.

[![Target mode example](https://dev.epicgames.com/community/api/documentation/image/b6f540ff-7b86-4361-89e9-8b5f7567b581?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b6f540ff-7b86-4361-89e9-8b5f7567b581?resizing_type=fit)

You can also target a specific actor. In the example below, there is a cube mesh present in the level. As long as the clones are within the inner and outer boundaries of the effector, they will face the static mesh. It does not matter if the target static mesh itself is within the effector range. It only matters that the meshes that you want to face the target are within that range.

[![Clones tracking a target actor](https://dev.epicgames.com/community/api/documentation/image/bbac5de2-04b3-4b46-9c59-00afa3537ccd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bbac5de2-04b3-4b46-9c59-00afa3537ccd?resizing_type=fit)

[![Select a target actor](https://dev.epicgames.com/community/api/documentation/image/dd655f8a-97e9-4fbe-83af-deff0ebc8793?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dd655f8a-97e9-4fbe-83af-deff0ebc8793?resizing_type=fit)

| Target Mode Properties | Description |
| --- | --- |
| **TargetActor** | Defines the target actor all clones face when within the influence of the effector. |

#### Noise Field

The **Noise Field** organizes and animates clones based on a variety of parameters. The example below uses a combination of the various **Strength**, **Pan**, and **Frequency** properties:

[![Noise Field example](https://dev.epicgames.com/community/api/documentation/image/bc8c9929-f898-4799-9296-2203da9bcc1e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bc8c9929-f898-4799-9296-2203da9bcc1e?resizing_type=fit)

##### Scale Strength

**Scale Strength** adjusts the scaling of each clone in the affected area along the selected axes according to the easing curve. In the examples below, the Scale Strength is set to affect the Z axis. The clones rise and fall with the noise field passing through the effector area due to the **Pan** setting value.

This example shows the Scale Strength on the Z axis set to 1.0:

[![Noise Field Scale Strength low Z axis scaling](https://dev.epicgames.com/community/api/documentation/image/1b119442-bce5-4d27-9fbd-ec4a3e0f6130?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1b119442-bce5-4d27-9fbd-ec4a3e0f6130?resizing_type=fit)

The example below shows the same effector set-up, except with the Scale Strength on the z axis set to 25.0:

[![Noise Field Scale Strength high Z axis scaling](https://dev.epicgames.com/community/api/documentation/image/f96fe114-7397-4e6a-9b1a-c6d73d29a7df?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f96fe114-7397-4e6a-9b1a-c6d73d29a7df?resizing_type=fit)

##### Location Strength

**Location Strength** determines how flat the noise field is. The example below uses a relatively low value:

[![Noise Field Location Strength low value](https://dev.epicgames.com/community/api/documentation/image/516a4124-715d-46ca-add6-3003478e8034?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/516a4124-715d-46ca-add6-3003478e8034?resizing_type=fit)

In the example below, the Location Strength is set to a relatively high value.

[![Noise Field Location Strength high value](https://dev.epicgames.com/community/api/documentation/image/6bdcfa96-1466-4f79-a701-a75e48089866?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6bdcfa96-1466-4f79-a701-a75e48089866?resizing_type=fit)

##### Rotation Strength

The **Rotation Strength** property rotates clones according to how close they are to the center of the effector. In the example shown below, the clones most affected are whiter and more acutely rotated.

[![Noise Field Rotation Strength example](https://dev.epicgames.com/community/api/documentation/image/9c375152-138f-42bf-b2a0-d6c03fbe2929?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9c375152-138f-42bf-b2a0-d6c03fbe2929?resizing_type=fit)

##### Pan

The **Pan** value determines how quickly the noise curve passes through the effector. When you use a low value, the result should look similar to the example below.

[![Noise Field Pan value low example](https://dev.epicgames.com/community/api/documentation/image/37d76544-24b2-4b7c-b4a9-d5535f77523f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/37d76544-24b2-4b7c-b4a9-d5535f77523f?resizing_type=fit)

The example below shows Pan set to a high value.

[![Noise Field Pan value high example](https://dev.epicgames.com/community/api/documentation/image/87462b0e-f69f-44b9-bca4-d4a228381725?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/87462b0e-f69f-44b9-bca4-d4a228381725?resizing_type=fit)

##### Frequency

Setting the **Frequency** value determines the overall intensity of the noise, which affects the number of peaks.

The example below shows a relatively low Frequency value.

[![Noise Field Frequency value low example](https://dev.epicgames.com/community/api/documentation/image/5b4350e9-babb-4b98-a2ce-afaf16f769f7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5b4350e9-babb-4b98-a2ce-afaf16f769f7?resizing_type=fit)

Here is the same example, except with a higher Frequency value.

[![Noise Field Frequency value high example](https://dev.epicgames.com/community/api/documentation/image/2f416098-d8b5-49d2-83d9-330f0fcda420?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2f416098-d8b5-49d2-83d9-330f0fcda420?resizing_type=fit)

| Noise Field Mode Properties | Description |
| --- | --- |
| **Location Strength X / Y / Z** | Determines how flat the noise field is. Higher values result in a less flat field. |
| **Rotation Strength X / Y / Z** | Determines how much the affected clones rotate around the indicated axes. |
| **Scale Strength X / Y / Z** | Determines how much the cloners affected will move along the indicated axes. |
| **Pan X / Y / Z** | Determines the rate and axes along which the noise field passes through the effector area. |
| **Frequency** | Determines the intensity of the noise, affecting the number of peaks. |

#### Push

You can use the **Push** mode to push the clones in a variety of directions and with varying levels of **Push Strength**.

[![Push Mode properties](https://dev.epicgames.com/community/api/documentation/image/b26e6e2b-f20d-40fb-90c1-80f2b3df82a9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b26e6e2b-f20d-40fb-90c1-80f2b3df82a9?resizing_type=fit)

##### Push Forward

This push option creates a push effect on your clones parallel to the axes defined for the Push Strength.

[![Push Forward example](https://dev.epicgames.com/community/api/documentation/image/49af2864-e165-4dc0-80d6-cbf82d206f55?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/49af2864-e165-4dc0-80d6-cbf82d206f55?resizing_type=fit)

##### Push Right

This push option creates a push effect on your clones horizontally perpendicular to the axes defined for the Push Strength.

[![Push Right example](https://dev.epicgames.com/community/api/documentation/image/d68b7f26-aa0d-4f90-a20f-2ff5848d6841?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d68b7f26-aa0d-4f90-a20f-2ff5848d6841?resizing_type=fit)

##### Push Up

This push option creates a push effect on your clones vertically perpendicular to the axes defined for the Push Strength.

[![Push Up example](https://dev.epicgames.com/community/api/documentation/image/5690bfd6-a4cd-4a57-b466-e6059636d7bd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5690bfd6-a4cd-4a57-b466-e6059636d7bd?resizing_type=fit)

When using the Push Forward, Push Right, and Push Up mode options, you can push in the opposite direction (back, left, or down) by using negative numbers for the values.

##### Push Effector

This push option creates a unit vector based on the relative locations of the effector and particle, and pushes based on the Push Strength along that vector.

##### Push Random

This push option creates a random unit vector based on the cloner seed, and pushes based on the Push Strength along that vector. This effect is deterministic, the same options with the same cloner seed always produce the same result.

| Push Mode Properties | Description |
| --- | --- |
| **Push Strength X / Y / Z** | Determines the magnitude of the push on the indicated axes. |
| **Push Direction** | Determines the direction of the push. Options are:   * Forward * Right * Up * Effector * Random |

### Step (Effector)

The Step effector provides a method for you to position, scale, and rotate your clones along a strict before-and-after plane, represented by the floating plane as it moves through the system.

| Step Mode Properties | Description |
| --- | --- |
| **Position X / Y / Z** | Determines the position of the Step effector plane on the indicated axes. |
| **Rotation X / Y / Z** | Determines the rotation of the Step effector plane on the indicated axes. |
| **Scaling X / Y / Z** | Determines the scaling of the Step effector plane on the indicated axes. |

### Shape

Using the **Effector** panel, there are several shaped formations you can set up to control the scope of an effector's influence on your clones, for a variety of effects. Their primary function is to restrain the effector's influence within specific bounds. You can begin by using the **Unbound** mode to understand the full extent of the effectors on your design when they aren't limited,, but below you will find descriptions for each Shape option in the order that they appear on the menu.

For all Shape options except Unbound, you can set the **Easing** property, which provides a list of curves you can choose from (linear, sine, cubic, circular, elastic, and so on). These apply an additional intensity effect on the clones in range, based on the shape you selected. See below under [Effector Boundaries](https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine) for more information.

Except when specified otherwise, all examples for demonstrating shapes shown below use the following settings for the **Mode**.

| Property | Value |
| --- | --- |
| **Mode** | Noise Field |
| **Scale Strength X** | 1.0 |
| **Scale Strength Y** | 1.0 |
| **Scale Strength Z** | 25.0 |
| **Frequency** | 1.0 |

Values not listed are 0.

[![Shape example settings](https://dev.epicgames.com/community/api/documentation/image/a7ae0421-a7e2-405d-99a1-f8cba17c5d5b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a7ae0421-a7e2-405d-99a1-f8cba17c5d5b?resizing_type=fit)

| Shape Properties | Description |
| --- | --- |
| **Shape** | Determines the shape applied to the effector. Options are:   * Sphere * Plane * Box * Unbound * Radial * Torus |
| **Easing** | Determines the easing curve applied to the effector's influence as it passes through the boundaries of the shape. Options are listed below. |

#### Effector Boundaries

Most effector shapes have two wireframe boundaries:

* An **inner boundary**, inside which clones are fully affected by whatever effect is generated by the effector. By default, the inner boundary area is shown in **red**.
* An **outer boundary**, inside which clones are partially affected by whatever effect is generated by the effector. By default, the outer boundary area is shown in **blue**.

The exception is any effector with the [Unbound](https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine#unbound) shape. See below for more information.

The outer boundary interpolates the effect on the clones between the full effect within the inner boundary area, and the default clone behavior outside the effector's area. How much the effector affects the clones within the outer boundary area depends on:

* The position of the clones within the outer boundary, with respect to the edge of the inner boundary and the external region.
* The Easing property curve associated with the effector, which determines how the interpolation is calculated.

  + There are many different curves available, mostly based on various mathematical functions. See the list of curves below along with images which demonstrate each curve.

| Curve Name | Image | Curve Name | Image |
| --- | --- | --- | --- |
| **In Expo** | [In Expo curve](https://dev.epicgames.com/community/api/documentation/image/26ad05e0-fadd-41c0-9d98-efd60a38a756?resizing_type=fit) | **In Out Quint** | [In Out Quint curve](https://dev.epicgames.com/community/api/documentation/image/5315ec21-795e-4c7e-aeea-b17b3b633d5f?resizing_type=fit) |
| **In Circ** | [In Circ curve](https://dev.epicgames.com/community/api/documentation/image/046064f9-83cb-4115-9a93-b5f1a2706f07?resizing_type=fit) | **In Out Quart** | [In Out Quart curve](https://dev.epicgames.com/community/api/documentation/image/6165b628-9294-41c9-bcb5-c0e020e4a41c?resizing_type=fit) |
| **In Quint** | [In Quint curve](https://dev.epicgames.com/community/api/documentation/image/2a016974-84c3-4794-a346-5e90667a942c?resizing_type=fit) | **In Out Quad** | [In Out Quad curve](https://dev.epicgames.com/community/api/documentation/image/ce7cb851-e35e-4b72-82f4-e118002d6c3b?resizing_type=fit) |
| **In Quart** | [In Quart curve](https://dev.epicgames.com/community/api/documentation/image/093edea0-1644-4e0e-89aa-6b8a517df2df?resizing_type=fit) | **In Out Cubic** | [In Out Cubic curve](https://dev.epicgames.com/community/api/documentation/image/554cd7e0-68e3-487b-88ab-ef38383de362?resizing_type=fit) |
| **In Quad** | [In Quad curve](https://dev.epicgames.com/community/api/documentation/image/5e72d16a-2a31-442e-9573-0fb1237599e8?resizing_type=fit) | **In Out Sine** | [In Out Sine curve](https://dev.epicgames.com/community/api/documentation/image/2bfbc47a-7436-426e-b825-32989524764b?resizing_type=fit) |
| **In Cubic** | [In Cubic curve](https://dev.epicgames.com/community/api/documentation/image/fd21fb72-793e-4589-9c5b-64f6afaf0797?resizing_type=fit) | **Linear** | [Linear curve](https://dev.epicgames.com/community/api/documentation/image/6653a9a8-1088-40a0-a2e5-f057f8fcf531?resizing_type=fit) |
| **In Sine** | [In Sine curve](https://dev.epicgames.com/community/api/documentation/image/ee8b088e-b77f-4fe9-a9dc-1bf0532d9e98?resizing_type=fit) | **In Bounce** | [In Bounce curve](https://dev.epicgames.com/community/api/documentation/image/0b627b60-91ee-44e5-928d-a602c1f88fe5?resizing_type=fit) |
| **Out Expo** | [Out Expo curve](https://dev.epicgames.com/community/api/documentation/image/7fdfdb40-0af0-4658-b5fb-4d679437f8ee?resizing_type=fit) | **In Back** | [In Back curve](https://dev.epicgames.com/community/api/documentation/image/4ab0eeca-118b-433b-8507-be451ffe9a7f?resizing_type=fit) |
| **Out Circ** | [Out Circ curve](https://dev.epicgames.com/community/api/documentation/image/482f5b91-0fbf-4ebd-893c-f21ce25fe3e9?resizing_type=fit) | **In Elastic** | [In Elastic curve](https://dev.epicgames.com/community/api/documentation/image/4fbcd8ea-880f-4f02-9647-83d7622c1516?resizing_type=fit) |
| **Out Quint** | [Out Quint curve](https://dev.epicgames.com/community/api/documentation/image/e78a79de-0409-421a-b7c7-3777b1257cba?resizing_type=fit) | **Out Bounce** | [Out Bounce curve](https://dev.epicgames.com/community/api/documentation/image/691fac11-18f5-4ace-80e4-ddb8602ef8cb?resizing_type=fit) |
| **Out Quart** | [Out Quart curve](https://dev.epicgames.com/community/api/documentation/image/4fd7d8b0-266c-49c7-9577-47f07afd5824?resizing_type=fit) | **Out Back** | [Out Back curve](https://dev.epicgames.com/community/api/documentation/image/82ff69b5-e1f5-4e4c-8d22-5f16c5376a47?resizing_type=fit) |
| **Out Quad** | [Out Quad curve](https://dev.epicgames.com/community/api/documentation/image/91e4ff56-5502-4a03-9c72-5ec7fed922ca?resizing_type=fit) | **Out Elastic** | [Out Elastic curve](https://dev.epicgames.com/community/api/documentation/image/7ffd5507-8faa-4c96-9ef4-948912606b46?resizing_type=fit) |
| **Out Cubic** | [Out Cubic curve](https://dev.epicgames.com/community/api/documentation/image/9d9763d9-8c36-4382-9673-f098f19a58d5?resizing_type=fit) | **In Out Bounce** | [In Out Bounce curve](https://dev.epicgames.com/community/api/documentation/image/0c45650a-8e2b-4526-9e50-23694060717d?resizing_type=fit) |
| **Out Sine** | [Out Sine curve](https://dev.epicgames.com/community/api/documentation/image/fdd37277-c032-4881-97fc-43cb44756785?resizing_type=fit) | **In Out Back** | [In Out Back curve](https://dev.epicgames.com/community/api/documentation/image/34689649-4972-479c-91b7-6c716e05474b?resizing_type=fit) |
| **In Out Expo** | [In Out Expo curve](https://dev.epicgames.com/community/api/documentation/image/1738a900-d48f-4d9d-a2ba-4acdd8321d4d?resizing_type=fit) | **In Out Elastic** | [In Out Elastic curve](https://dev.epicgames.com/community/api/documentation/image/b06d9eab-cdd2-4289-bfc8-0e30756f9a98?resizing_type=fit) |
| **In Out Circ** | [In Out Circ curve](https://dev.epicgames.com/community/api/documentation/image/ef7abbad-592e-44c8-817b-3f0174236124?resizing_type=fit) | **Random** | [Random curve](https://dev.epicgames.com/community/api/documentation/image/5340a4a7-b51d-4762-96a5-2d3d5f75dfd6?resizing_type=fit) |

Depending on the shape of the effector, the boundary description will differ, either as inner / outer radius, or inner / outer extent. See specific shape options below for details.

You can control the color and transparency of the boundaries in your **Project Settings**, under **Motion Design - Cloner & Effector**. You can set the color with the Color Picker, or manually set the RGBA values. The alpha channel (A) controls the transparency of the wireframes, from 0.1 (most transparent) to 1 (least transparent).

[![Motion Design effector color settings](https://dev.epicgames.com/community/api/documentation/image/b727743d-e794-49f3-91b6-439df2bdeb16?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b727743d-e794-49f3-91b6-439df2bdeb16?resizing_type=fit)

#### Invert Type

An important setting shared across all of the Shape properties is the **Invert Type** option at the bottom of the list. Enabling this property inverts the affected area.

[![Invert Type setting](https://dev.epicgames.com/community/api/documentation/image/a3aed99f-8a64-486b-bfe0-3fff04b893c5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a3aed99f-8a64-486b-bfe0-3fff04b893c5?resizing_type=fit)

The example below shows an effector using a sphere shape before inverting. The effect is contained within the boundaries of the effector, attenuating to nothing at the edge of the outer boundary.

[![Sphere shape example](https://dev.epicgames.com/community/api/documentation/image/9ea1c20f-7abf-4add-9a11-19eb0f612db7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9ea1c20f-7abf-4add-9a11-19eb0f612db7?resizing_type=fit)

After inverting, the example now shows the effects are reversed. The effector's influence is at full strength outside the boundaries, attenuating across the outer boundary volume and having no effect on the inner boundary volume.

[![Sphere shape inverted example](https://dev.epicgames.com/community/api/documentation/image/32d8d317-73d9-4504-b8d2-052f5a824dfa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/32d8d317-73d9-4504-b8d2-052f5a824dfa?resizing_type=fit)

#### Sphere

This shapes the effector into a sphere that has customizable properties for the **Inner / Outer** boundaries. Any clone that falls outside of the **Outer** boundary is not influenced by the effector. You can set the **Easing** property as described previously.

[![Effector Sphere shape example](https://dev.epicgames.com/community/api/documentation/image/c5114785-a44f-4f69-accc-0c8d66d6b393?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c5114785-a44f-4f69-accc-0c8d66d6b393?resizing_type=fit)

Below is a clearer example of the Sphere shape boundary when the mode is changed from **Noise Field** to **Offset**.

[![Effector Sphere shape Offset mode example](https://dev.epicgames.com/community/api/documentation/image/36c36879-f631-4bf9-af27-ec0161f4e81c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/36c36879-f631-4bf9-af27-ec0161f4e81c?resizing_type=fit)

The image below shows the Mode settings we used for this change in the example above.

| Property | Value |
| --- | --- |
| **Mode** | Offset |
| **Offset Z** | -262.70 |
| **Rotation Y** | 90.0 |
| **Scale X** | 1.0 |
| **Scale Y** | 1.0 |
| **Scale Z** | 1.0 |

[![Effector Sphere shape Offset mode settings](https://dev.epicgames.com/community/api/documentation/image/aac28451-e0cf-4eee-a8d7-0603d42f3668?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/aac28451-e0cf-4eee-a8d7-0603d42f3668?resizing_type=fit)

| Sphere Shape Properties | Description |
| --- | --- |
| **Inner Radius** | Defines the boundaries of the inner area of influence for the effector using a sphere shape. |
| **Outer Radius** | Defines the boundaries of the outer area of influence for the effector using a sphere shape. |
| **Invert Type** | Inverts how the shape modifies the effector's influence. |

#### Plane

Passing this effector shape through the cloner will interpolate between minimum and maximum values of the mode selected along the curve selected under the **Easing** setting. The effector has two handles that represent what happens before and after the effector passes through the space.

[![Plane shape Noise field example](https://dev.epicgames.com/community/api/documentation/image/ee160aba-1075-47fd-9ff1-6e60bc21fce2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ee160aba-1075-47fd-9ff1-6e60bc21fce2?resizing_type=fit)

Lowering the value of **Plane Spacing** reduces the space between the two handles, and the effect will have a less gradual curve.

When using the Plane shape, you must select one of the Easing property curve options. The default setting is the Linear curve option.

[![Effector Plane shape default linear curve example](https://dev.epicgames.com/community/api/documentation/image/727870d2-0232-43f6-9a2d-7b9ee60d759a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/727870d2-0232-43f6-9a2d-7b9ee60d759a?resizing_type=fit)

| Plane Shape Properties | Description |
| --- | --- |
| **Plane Spacing** | Determines the space between the two plane handles. |
| **Invert Type** | Inverts how the shape modifies the effector's influence. |

#### Box

This shape restrains the effector's influence using the **Inner Extent** and **Outer Extent** properties, which use the X, Y, and Z axes to define rectangular cuboid volumes. The Box shape draws a bounding box to indicate where the effect is present. Much like the other Effector Shape options, you can set the Easing property.

[![Effector Box shape example](https://dev.epicgames.com/community/api/documentation/image/a3229fa1-5e4f-4c0e-8aaa-9d370a10ebd7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a3229fa1-5e4f-4c0e-8aaa-9d370a10ebd7?resizing_type=fit)

Inverting the previous example results in the image below.

[![Effector Box shape inverted example](https://dev.epicgames.com/community/api/documentation/image/fb5c4793-474d-4989-817c-bcf144141976?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fb5c4793-474d-4989-817c-bcf144141976?resizing_type=fit)

| Box Shape Properties | Description |
| --- | --- |
| **Inner Extent** **X / Y / Z** | Defines the boundaries of the inner area of influence for the effector using a box shape, on the respective axes. |
| **Outer Extent** **X / Y / Z** | Defines the boundaries of the outer area of influence for the effector using a box shape, on the respective axes. |
| **Invert Type** | Inverts how the shape modifies the effector's influence. |

#### Unbound

This option places no shape restraints on the effector. This shape does not have boundaries, nor does it use the Easing property, unlike the other options.

[![Effector Unbound shape example](https://dev.epicgames.com/community/api/documentation/image/a8822b15-7b7c-4233-a55d-d8c2e9a1a0c1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a8822b15-7b7c-4233-a55d-d8c2e9a1a0c1?resizing_type=fit)

#### Radial

When using the Radial shape, you can set the **Radial Angle**, which you can increase up to a full circle with a hollow center. The center is defined by the **Radial Min Radius** and **Radial Max Radius** properties. You can use the standard Easing property options to define how the Radial shape changes.

The example below shows the Radial Angle property using the In Out Back curve Easing option. This option makes the Radial shape start low and curve upward.

[![In Out Back curve setting](https://dev.epicgames.com/community/api/documentation/image/b8456c7c-f581-4f7c-9d39-1ba8a1e8c71e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b8456c7c-f581-4f7c-9d39-1ba8a1e8c71e?resizing_type=fit)

[![Effector Radial shape example](https://dev.epicgames.com/community/api/documentation/image/fc922e83-d309-4ba0-8c6b-b46cc1fc01b8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fc922e83-d309-4ba0-8c6b-b46cc1fc01b8?resizing_type=fit)

The following GIF shows an example of manipulating the Radial Min Radius and Radial Max Radius to customize the inner and outer thickness of the ring.

For this example, the **Invert Type** property instead pushes the shape area down into the floor.

| Radial Shape Properties | Description |
| --- | --- |
| **Radial Angle** | Determines the arc of the radial shape. Can extend to a full circle at 360 degrees. |
| **Radial Min Radius** | Determines the radius of the minimum (inner) boundary of the Radial shape. |
| **Radial Max Radius** | Determines the radius of the maximum (outer) boundary of the Radial shape. |
| **Invert Type** | Inverts how the shape modifies the effector's influence. |

#### Torus

When using the Torus shape option, you can control the radius of the main torus, as well as the radius of both the inner and outer boundaries.

[![Effector Torus shape example](https://dev.epicgames.com/community/api/documentation/image/8c147762-d450-49e5-96d3-4cda9469ca1d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8c147762-d450-49e5-96d3-4cda9469ca1d?resizing_type=fit)

You can use the Torus Radius property to expand the size of the torus while still remaining an equal thickness. Below is an example.

[![Effector Torus shape changing radius example](https://dev.epicgames.com/community/api/documentation/image/4f813ce8-878b-432f-9bec-c919e6744143?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4f813ce8-878b-432f-9bec-c919e6744143?resizing_type=fit)

| Radial Shape Properties | Description |
| --- | --- |
| Torus Radius | Determines the radius of the entire Torus shape. |
| Torus Inner Radius | Determines the radius of the Torus inner boundary. |
| Torus Outer Radius | Determines the radius of the Torus outer boundary. |
| Invert Type | Inverts how the shape modifies the effector's influence. |

* [experimental](https://dev.epicgames.com/community/search?query=experimental)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Introduction](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#introduction)
* [Where to Find the Tools](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#where-to-find-the-tools)
* [Cloner Actors](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#cloner-actors)
* [General](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#general)
* [Cloner](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#cloner)
* [Force Update Cloner](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#force-update-cloner)
* [Seed](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#seed)
* [Color](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#color)
* [Advanced](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#advanced)
* [Layouts](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#layouts)
* [Grid](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#grid)
* [Line](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#line)
* [Circle](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#circle)
* [Cylinder](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#cylinder)
* [Sphere Uniform](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#sphere-uniform)
* [Honeycomb](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#honeycomb)
* [Mesh](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#mesh)
* [Spline](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#spline)
* [Sphere Random](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#sphere-random)
* [Range](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#range)
* [Step (Cloner)](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#step-cloner)
* [Emission](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#emission)
* [Spawn](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#spawn)
* [Lifetime](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#lifetime)
* [Progress](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#progress)
* [Physics](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#physics)
* [Surface Collision Enabled](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#surface-collision-enabled)
* [Particle Collision Enabled](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#particle-collision-enabled)
* [Collision Velocity Enabled / Collision Iterations](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#collision-velocity-enabled-collision-iterations)
* [Collision Grid Size / Collision Grid Resolution](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#collision-grid-size-collision-grid-resolution)
* [Collision Radius Mode](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#collision-radius-mode)
* [Mass Min / Mass Max](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#mass-min-mass-max)
* [Rendering](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#rendering)
* [Mesh Render Mode](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#mesh-render-mode)
* [Iterate](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#iterate)
* [Random](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#random)
* [Blend](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#blend)
* [Mesh Facing Mode](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#mesh-facing-mode)
* [Default](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#default)
* [Velocity](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#velocity)
* [Camera Position](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#camera-position)
* [Camera Plane](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#camera-plane)
* [Meshes Cast Shadows](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#meshes-cast-shadows)
* [Default Meshes](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#default-meshes)
* [Visualize Effectors](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#visualize-effectors)
* [Use Override Material](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#use-override-material)
* [Override Material](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#override-material)
* [Edit with Material Designer](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#edit-with-material-designer)
* [Set Translucent Priority](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#set-translucent-priority)
* [Utilities](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#utilities)
* [Create Default Actor Attached](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#create-default-actor-attached)
* [Convert to Static Meshes](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#convert-to-static-meshes)
* [Convert to Static Mesh](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#convert-to-static-mesh)
* [Convert to Instanced Static Mesh](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#convert-to-instanced-static-mesh)
* [Convert to Dynamic Mesh / Convert to Dynamic Meshes](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#convert-to-dynamic-mesh-convert-to-dynamic-meshes)
* [Create Cloner Sequencer Tracks](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#create-cloner-sequencer-tracks)
* [Effector Actors](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#effector-actors)
* [Creating an Effector](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#creating-an-effector)
* [General](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#general)
* [Effector](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#effector)
* [Forces](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#forces)
* [Orientation Force](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#orientation-force)
* [Vortex Force](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#vortex-force)
* [Curl Noise Force](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#curl-noise-force)
* [Attraction Force](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#attraction-force)
* [Gravity Force](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#gravity-force)
* [Drag Force](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#drag-force)
* [Vector Noise Force](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#vector-noise-force)
* [Mode](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#mode)
* [Offset](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#offset)
* [Target](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#target)
* [Noise Field](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#noise-field)
* [Scale Strength](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#scale-strength)
* [Location Strength](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#location-strength)
* [Rotation Strength](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#rotation-strength)
* [Pan](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#pan)
* [Frequency](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#frequency)
* [Push](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#push)
* [Push Forward](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#push-forward)
* [Push Right](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#push-right)
* [Push Up](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#push-up)
* [Push Effector](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#push-effector)
* [Push Random](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#push-random)
* [Step (Effector)](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#step-effector)
* [Shape](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#shape)
* [Effector Boundaries](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#effector-boundaries)
* [Invert Type](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#invert-type)
* [Sphere](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#sphere)
* [Plane](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#plane)
* [Box](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#box)
* [Unbound](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#unbound)
* [Radial](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#radial)
* [Torus](/documentation/en-us/unreal-engine/motion-design-cloners-and-effectors-in-unreal-engine?application_version=5.7#torus)
