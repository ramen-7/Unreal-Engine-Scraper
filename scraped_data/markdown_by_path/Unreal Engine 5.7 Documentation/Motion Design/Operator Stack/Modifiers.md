<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7 -->

# Modifiers

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
6. [Operator Stack](/documentation/en-us/unreal-engine/operator-stack-in-unreal-engine "Operator Stack")
7. Modifiers

# Modifiers

All about Modifiers for use in your Motion Design projects.

![Modifiers](https://dev.epicgames.com/community/api/documentation/image/64f0c321-870c-49d5-9f86-0337e8a61231?resizing_type=fill&width=1920&height=335)

 On this page

Modifiers provide you with a variety of tools to assist you as a designer for both 2D and 3D layouts. With modifiers you can:

* Rig your designs’ layouts using the [Layout](https://dev.epicgames.com/documentation/en-us/unreal-engine/modifiers-in-unreal-engine#layout) tools.
* Edit your 2D and 3D Motion Design primitives with the [Geometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/modifiers-in-unreal-engine#geometry) tools.
* Manipulate how your designs render using the [Rendering](https://dev.epicgames.com/documentation/en-us/unreal-engine/modifiers-in-unreal-engine#rendering) tools.
* Use the [Transition Logic](https://dev.epicgames.com/documentation/en-us/unreal-engine/modifiers-in-unreal-engine#transition-logic) modifier to simplify setting up a system for many use-cases, so you won't need to inspect the transition tree.

You can access modifiers from the [Operator Stack](https://dev.epicgames.com/documentation/en-us/unreal-engine/operator-stack-in-unreal-engine), along with [animators](https://dev.epicgames.com/documentation/en-us/unreal-engine/animators-in-unreal-engine).

## Adding Modifiers

You can add modifiers by clicking **+Add Modifiers** in the Operator Stack window, which displays the palette of modifiers available for you to use on your selected shape.

Some modifiers can only be added to 2D shapes, others can be added to both 2D and 3D shapes. Modifiers that are not compatible with your selected actor are hidden. You can't add a modifier to your shape if it isn’t compatible with your selected actor type.

[![Modifiers menu in the Operator Stack window.](https://dev.epicgames.com/community/api/documentation/image/b63d862d-9f5c-42a5-afc1-6c267dceb99d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b63d862d-9f5c-42a5-afc1-6c267dceb99d?resizing_type=fit)

You can click any of these modifiers to add it to an actor you select in your **Motion Design Outliner**. If you already know the name of the modifier that you want to use, you can search for it by name in the search bar near the top.

The example below shows a case where a modifier type won’t appear. In this example, you can't add a Geometry modifier to a null actor that parents geometry actors, so Geometry modifiers do not appear in the +Add Modifiers menu:

[![Adding a modifier to a null actor.](https://dev.epicgames.com/community/api/documentation/image/75c1b229-1eec-4015-8418-70e0e1e86703?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/75c1b229-1eec-4015-8418-70e0e1e86703?resizing_type=fit)

### Filtering Modifiers

If you have multiple modifiers of different types added to the same shape, you can filter which modifiers are visible by type using the buttons at the top of the Modifiers panel. By default, the panel shows all the modifiers. When you click a filter button, only modifiers of that category appear. You can click multiple buttons to show more than one category of modifiers.

[![Filtering modifiers](https://dev.epicgames.com/community/api/documentation/image/118b4d48-5b3c-40c3-90bb-dc50482b3bc1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/118b4d48-5b3c-40c3-90bb-dc50482b3bc1?resizing_type=fit)

## Layout

Layout modifiers provide a way for you to adjust the placement of actors on screen using straightforward tools that can achieve results without a lot of minute manual adjustments.

### Align Between

You can use the **Align Between** modifier to maintain the position of a collection of actors between two other actors. You can use this when expanding or contracting a region in your level to ensure other actors shift horizontally to stay centered within the region.

The example below shows a group of three characters, nested inside of a null actor that has the Align Between modifier assigned to it:

[![The Align Between modifier](https://dev.epicgames.com/community/api/documentation/image/bc689511-ec38-467f-b7ef-a4a31faa44f4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bc689511-ec38-467f-b7ef-a4a31faa44f4?resizing_type=fit)

#### Reference Actors Array

Setting up involves adding a modifier to a null actor. When you first add the modifier to a null actor, you will be presented with an empty **Reference Actors** array property:

[![Align Between empty array](https://dev.epicgames.com/community/api/documentation/image/ef017d49-2434-45f5-839a-7a018bfb3f9a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ef017d49-2434-45f5-839a-7a018bfb3f9a?resizing_type=fit)

Click the **Add (+)** button to create a new array entry:

[![Align Between new array entry](https://dev.epicgames.com/community/api/documentation/image/b3ad6730-36ef-4621-8fcb-7b96560bfcdb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b3ad6730-36ef-4621-8fcb-7b96560bfcdb?resizing_type=fit)

Click the **Add (+)** button again to create a second array entry. The properties summarized below apply to both reference actors in the array, which function as handles. You need two for the Align Between modifier to function.

#### Actor Weak

The **Actor Weak** property provides a way to choose the reference actors in the array used for the boundaries. Expanding the drop-down menu presents you with a list of all actors in the level. Select actors to act as your boundary for both reference actors in the array.

In the example shown below, setting the values in the array as shown in the image and table provides two purple rectangle actors named "Left" and "Right" to use as bounds:

[![Setting the boundary actors using the Actor Weak property](https://dev.epicgames.com/community/api/documentation/image/3c989cca-1f6c-47e1-a5c5-dc2b0c3d1271?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3c989cca-1f6c-47e1-a5c5-dc2b0c3d1271?resizing_type=fit)

| Index | Actor Weak | Weight |
| --- | --- | --- |
| 1 | Left | 1.0 |
| 2 | Right | 1.0 |

In the example below, when you move the two purple rectangle handles, it shifts the group of characters around to center between the handles.

[![Moving the boundary actors to use the Align Between modifier to reposition the image actors.](https://dev.epicgames.com/community/api/documentation/image/3a59e9d3-1cfa-4f44-b16f-25c450a7d680?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3a59e9d3-1cfa-4f44-b16f-25c450a7d680?resizing_type=fit)

#### Weight

The **Weight** property determines how much interpolation takes place. If the value is higher for one handle, the alignment shifts towards that handle. A value of 0 results in no effect.

#### Enabled

When your actors are positioned to your liking, you can deselect the **Enabled** property checkbox to hide the handle actors.

| Align Between Properties | Description |
| --- | --- |
| **Actor Weak** | Provides a list of available actors to use as the interaction handle. |
| **Weight** | Determines the interpolation between the handle actors. |
| **Enabled** | Disable this checkbox to hide the handle actor. |

### Auto Follow

You can use the **Auto Follow** modifier when you have an actor that needs to follow the position of another actor. In the example below, the UE logo is following the text so that as the text becomes longer or shorter, the logo shifts along with it.

[![auto follow logo follows long text](https://dev.epicgames.com/community/api/documentation/image/93fcbc58-2a63-4876-9bca-c5831d18fa49?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/93fcbc58-2a63-4876-9bca-c5831d18fa49?resizing_type=fit)

Here it is with shorter text:

[![auto follow logo follows short text](https://dev.epicgames.com/community/api/documentation/image/642cd657-5533-47ef-a3ab-8bf8df511567?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/642cd657-5533-47ef-a3ab-8bf8df511567?resizing_type=fit)

To accomplish this using the Auto Follow modifier, place the modifier on the actor that is following another actor. In this example, it’s the UE logo.

[![auto follow set up](https://dev.epicgames.com/community/api/documentation/image/5578862d-3461-465a-b3fc-441999cc9dc5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5578862d-3461-465a-b3fc-441999cc9dc5?resizing_type=fit)

There are some key properties that you will need to define carefully.

#### Reference Container

This property provides a way to define how the auto follow functions. You can select a specific actor to follow using the Other option, or you can set it to follow based on the order of where the actor exists in the Motion Design Outliner hierarchy.

[![reference container options](https://dev.epicgames.com/community/api/documentation/image/02e3c728-c239-4b0c-b995-5221bbf72a1c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/02e3c728-c239-4b0c-b995-5221bbf72a1c?resizing_type=fit)

* **Previous**: follows the previous actor in the Motion Design Outliner.
* **Next**: follows the next actor in the Motion Design Outliner.
* **First**: follows the first actor in the Motion Design Outliner.
* **Last**: follows the last actor in the Motion Design Outliner.
* **Other**: Define a specific actor to follow, regardless of its position in the Motion Design Outliner.

#### Reference Actor

When the Reference Container property is set to Other, the **Reference Actor** property determines which actor the group will follow. In the example at the beginning of this section using the UE Logo actor,  the group follows the 3Dtext actor.

#### Skip Hidden

When the Reference Container property is not set to Other, enabling the **Skip Hidden** property causes the modified actor to ignore hidden actors when determining the reference actor.

#### Followed Axis

The **Followed Axis** property determines the axes on which the actor follows. The most common use case is the **Y | Z** option, but you can expand the dropdown to customize the axes.

[![followed axis options](https://dev.epicgames.com/community/api/documentation/image/25d2b6f0-44fc-4dc0-97fe-76507bb82b54?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/25d2b6f0-44fc-4dc0-97fe-76507bb82b54?resizing_type=fit)

#### Offset Axis

The **Offset Axis** property calculates the width of the following actor (in the example above, the logo) and offsets it to the right with a value of 1.0 for the Y value. If you set the value to 0.0 for X, Y, and Z, the following actor will overlap the followed actor.

#### Followed Alignment and Local Alignment

**Followed Alignment** and **Local Alignment** function similarly, with the difference between them being that Followed Alignment determines the alignment of the reference actor, and Local Alignment determines the alignment of the modified actor.

For the auto follow to calculate correctly, set the vertical and horizontal alignment to match the actors involved in the calculation. You can select any combination of options for your own work, but in this example, both actors are centered both vertically and horizontally.

* Alignment for the text actor:

  [![auto follow text actor alignment](https://dev.epicgames.com/community/api/documentation/image/8744000d-f4f8-4a0e-8498-bc7134836a7e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8744000d-f4f8-4a0e-8498-bc7134836a7e?resizing_type=fit)
* Alignment for the rectangle:

  [![auto follow rectangle alignment](https://dev.epicgames.com/community/api/documentation/image/eebb804b-f6a4-4465-918b-41f2ac39e23f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/eebb804b-f6a4-4465-918b-41f2ac39e23f?resizing_type=fit)

#### Start Padding

This property provides you a way to set a preset gap to prevent your layout from being too densely clustered.

* Start Padding set to 0.0:

  [![auto follow start padding set to 0](https://dev.epicgames.com/community/api/documentation/image/2116838a-6438-4b86-b2cb-bcdf6dcf6353?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2116838a-6438-4b86-b2cb-bcdf6dcf6353?resizing_type=fit)
* Start Padding set to 30.0:

  [![auto follow start padding set to 30](https://dev.epicgames.com/community/api/documentation/image/51538657-b0c9-4cc7-b42e-2dd75ebe81d8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/51538657-b0c9-4cc7-b42e-2dd75ebe81d8?resizing_type=fit)

#### End Padding

You can use End Padding in conjunction with Padding Progress to animate your distance across a fixed 0% - 100% translation, where the Start Padding value defines the 0% position, and the End Padding value defines the 100% position. The image below shows an example:

[![auto follow end padding](https://dev.epicgames.com/community/api/documentation/image/7605b3f4-a82b-48a6-b0c6-4f11e3b9a9fb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7605b3f4-a82b-48a6-b0c6-4f11e3b9a9fb?resizing_type=fit)

#### Padding Progress

You can set the Padding Progress value to show a specific point in the translation from Start Padding to End Padding. If you set the Start Padding value to zero on all three axes (0, 0, 0) then use the End Padding and Padding Progress properties to handle the translation, a Padding Progress value of 50 produces a result like the following image:

[![auto follow padding progress](https://dev.epicgames.com/community/api/documentation/image/cc156261-62a0-4528-a3c1-a003566a9215?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cc156261-62a0-4528-a3c1-a003566a9215?resizing_type=fit)

| Auto Follow Properties | Description |
| --- | --- |
| **Reference Container** | Determines which actor to follow. Options are:   * Previous * Next * First * Last * Other |
| **Reference Actor** | Defines a specific actor to follow. Only available if Reference Container is set to Other. |
| **Skip Hidden** | Enable to ignore hidden actors when picking the reference actor to follow. Only available if Reference Container is not set to Other. |
| **Followed Axis X / Y / Z** | Determines on which axes the actors follow. |
| **Offset Axis X / Y / Z** | Determines on a per-axis basis the offset between the followed and following actors. Setting all values to 0 overlaps the actors. |
| **Followed Alignment** | Determines the alignment for the reference actor. Alignment should match that of the modified actor. |
| **Local Alignment** | Determines the alignment for the modified actor. Alignment should match that of the reference actor. |
| **Start Padding** | Determines a preset distance between actors to prevent layout cluttering. |
| **End Padding** | Determines a maximum distance when animating the following actor layout. |
| **Padding Progress** | Determines the progress towards reaching the maximum distance when animating the following layout. Requires a valid End Padding property value. |

### Grid Arrange

This modifier provides a way for you to spread out a few actors evenly according to the row and/or column count, and the spread between actors. To use the Grid Arrange modifier, you apply it to a parent null actor which has the actors you want to arrange in a grid as children.

[![grid arrange](https://dev.epicgames.com/community/api/documentation/image/3711ec89-0e5c-49e3-a7ed-b52a21104243?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3711ec89-0e5c-49e3-a7ed-b52a21104243?resizing_type=fit)

#### Count

The **Count** property handles the horizontal and vertical number of actors you want to arrange. In the example above, there are three characters spread across a single row.

#### Spread

The **Spread** property controls the distance between the actors, which are evenly distributed. A zero (0.0) value results in the actors overlapping.

#### Start Corner

The **Start Corner** property determines whether the actors spread from the left or from the right.

#### Start Direction

The **Start Direction** property determines whether the actors are spaced vertically or horizontally.

| Grid Arrange Properties | Description |
| --- | --- |
| **Count** | Determines number of actors in the grid horizontally and vertically. |
| **Spread** | Determines the distance between actors. A 0 value results in overlapping actors. |
| **Start Corner** | Determines whether the actors spread from the left or from the right. |
| **Start Direction** | Determines whether the actors are spaced vertically or horizontally. |

### Justify

You can use the **Justify** modifier to force the alignment of a group of actors. To use it, multi-select a group of actors and group them using **Ctrl+G**. Add the **Justify** modifier on the null actor that represents the group, and the modifier will calculate the total area of all the actors’ bounding boxes. If you select **Center** under **Horizontal Alignment**, the modifier centers them in your viewport. Selecting all three helps to visualize this.

[![justify](https://dev.epicgames.com/community/api/documentation/image/0d9177c1-34d9-4d02-9a3a-b9cca7f3ded9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0d9177c1-34d9-4d02-9a3a-b9cca7f3ded9?resizing_type=fit)

Shifting over the purple rectangle with the bounding boxes visible demonstrates that the Justify is centering as expected.

[![justify move box](https://dev.epicgames.com/community/api/documentation/image/dc269af6-3b7c-4b66-9773-073499b156ac?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dc269af6-3b7c-4b66-9773-073499b156ac?resizing_type=fit)

#### Alignment Properties

All three of the **Alignment** properties (Horizontal, Vertical, and Depth) function in the same way. You select an option to define how the group of actors are justified, defaulting to none, with options for either boundary edge or the center of your selected alignment.

#### Anchor Properties

The **Anchor** properties (Horizontal, Vertical, and Depth) are only available if the corresponding alignment property is set to a value other than None, and also all function in the same way. They provide a way to shift the anchor point for how the group of actors is justified away from the default position along the related alignment.

| Justify Properties | Description |
| --- | --- |
| **Horizontal Alignment** | Options are:   * None * Left * Center * Right |
| **Vertical Alignment** | Options are:   * None * Top * Center * Bottom |
| **Depth Alignment** | Options are:   * None * Front * Center * Back |
| **Horizontal Anchor** | Only available if Horizontal Alignment has a value other than None. Provides a way to shift the horizontal anchor point for the justify effect on the modified group of actors. |
| **Vertical Anchor** | Only available if Vertical Alignment has a value other than None. Provides a way to shift the vertical anchor point for the justify effect on the modified group of actors. |
| **Depth Anchor** | Only available if Depth Alignment has a value other than None. Provides a way to shift the depth anchor point for the justify effect on the modified group of actors. |

### Look At

You can use the **Look At** modifier to cause one of your actors to rotate automatically to always face another actor. In the example shown below, we added the modifier to the **Torus** actor, set the **Reference Container** to **Other**, and then set the **Green Sphere** as the **Reference Actor**. The modifier scans the level for the reference actor and turns the modified actor to face it.

[![look at modifier set up](https://dev.epicgames.com/community/api/documentation/image/b568891e-d576-437e-bbf6-2cf917fcf957?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b568891e-d576-437e-bbf6-2cf917fcf957?resizing_type=fit)

In the image below, when we move the Torus to the left, it continues to face the Green Sphere.

[![look at modifier in action](https://dev.epicgames.com/community/api/documentation/image/88c90a7b-59cf-4ef7-a994-758fee532a9a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/88c90a7b-59cf-4ef7-a994-758fee532a9a?resizing_type=fit)

#### Reference Container

The **Reference Container** property provides a way to define the actor the modified actor orients towards. You can select a specific actor to look at using the **Other** option, or you can set it to orient according to the order of where the actor exists in the **Motion Design Outline**r hierarchy.

* **Previous**: orient towards the previous actor in the Motion Design Outliner.
* **Next**: orient towards the next actor in the Motion Design Outliner.
* **First**: orient towards the first actor in the Motion Design Outliner.
* **Last**: orient towards the last actor in the Motion Design Outliner.
* **Other**: Define a specific actor to orient towards, regardless of its position in the Motion Design Outliner.

#### Reference Actor

When the Reference Container property is set to Other, the **Reference Actor** property determines which actor the modified actor looks at.

#### Skip Hidden

When the Reference Container property is not set to Other, enabling the **Skip Hidden** property causes the modified actor to ignore hidden actors when determining the reference actor.

#### Axis Properties

You can use the **Axis** property to define which axis (X, Y, or Z) of your modified actor faces towards the reference actor, the default is the X axis. You can also enable the **Flip Axis** property to cause the modified actor to face the opposite direction along the selected axis.

| Look At Properties | Description |
| --- | --- |
| **Reference Container** | Determines which actor to look at. Options are:   * Previous * Next * First * Last * Other |
| **Reference Actor** | Defines a specific actor to look at. Only available if Reference Container is set to Other. |
| **Skip Hidden** | Enable to ignore hidden actors when picking the reference actor to look at. Only available if Reference Container is not set to Other. |
| **Axis** | Defines the axis of the modified actor along which it faces the reference actor. Options are:   * X * Y * Z |
| **Flip Axis** | Reverses the facing of the modified actor towards the reference actor along the selected axis. |

### Radial Arrange

You can apply a Radial Arrange modifier to the null parent of a set of grouped actors. You can adjust the radial arrangement this generates using a variety of properties, as shown in the example below.

[![radial arrange modifier](https://dev.epicgames.com/community/api/documentation/image/dddae645-ffce-4272-85a9-c9150a428eee?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dddae645-ffce-4272-85a9-c9150a428eee?resizing_type=fit)

#### Count

You can use the **Count** property to set the number of items you want to arrange. Setting the value to -1 automatically uses all available actors in the group.

#### Rings

You can use the **Rings** property to set the number of rings you want to arrange. In the above example, we set the value to 2, which creates 2 rings.

#### Inner Radius and Outer Radius

The **Inner Radius** and **Outer Radius** properties define the size (radius) of the innermost ring and outermost ring created, respectively. The actors will spread out or contract within the two constraints accordingly.

#### Start Angle and End Angle

The **Start Angle** and **End Angle** properties combine to define the shape of the arc arrangement of your actors. The range for each setting is -180 through 180, in degrees. For a complete circle, set the Start Angle value to -180 and the End Angle value to 180.

#### Start from Outer Radius

The **Start from Outer Radius** property constructs the arrangement from the outer radius moving inwards, rather than from the inner radius moving outwards. In the example, this causes the outer spheres to move to the middle of the group:

* Standard:

  [![radial arrange start from outer radius initial state](https://dev.epicgames.com/community/api/documentation/image/708ecf88-c8bd-497a-b294-04d142657b18?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/708ecf88-c8bd-497a-b294-04d142657b18?resizing_type=fit)
* Start from Outer Radius:

  [![radial arrange enable start from outer radius](https://dev.epicgames.com/community/api/documentation/image/c9b110b3-3799-4417-b767-bb6f09fa5232?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c9b110b3-3799-4417-b767-bb6f09fa5232?resizing_type=fit)
* Increasing the values of the Outer Radius and Inner Radius properties reveals what’s happening more effectively:

  [![radial arrange start from outer radius increased radius](https://dev.epicgames.com/community/api/documentation/image/876a49d7-cf23-4d57-8daa-92839f1746a3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/876a49d7-cf23-4d57-8daa-92839f1746a3?resizing_type=fit)

#### Orient Properties

Enabling the **Orient** property gives you control over how the radial arrangement appears in 3 dimensions, by means of 3 additional properties that only become available when you enable Orient.

* **Orientation Axis:** You can define the axis (X, Y, Z) your radial arrangement is oriented around. By default, your radial arrangement is oriented around the X axis.
* **Base Orientation:** You can apply additional rotation, in degrees along one or more axes (X, Y, Z), to the arrangement in addition to the default axis.
* **Flip Axis:** Reverses the facing of the arrangement along the selected axis.

| Radial Arrange Properties | Description |
| --- | --- |
| **Count** | Defines the number of items you want to arrange. Setting the value to -1 automatically uses all available actors in the group. |
| **Rings** | Defines the number of rings you want to arrange. |
| **Inner Radius** | Defines the radius of the inner ring. |
| **Outer Radius** | Defines the radius of the outer ring. |
| **Start Angle** | Defines the start angle for the ring. Range is -180 through 180, in degrees. |
| **End Angle** | Defines the end angle for the ring. Range is -180 through 180, in degrees. |
| **Arrangement** | Defines how the radial arrangement elements are organized. Options are:   * **Equal:** All elements in all radial rings have the same spacing between them. The number of elements in the outer rings will be greater than the inner rings. * **Monospace:** Each radial ring will contain the same number of elements. The spacing between elements in the outer rings will be greater than the inner rings. |
| **Start from Outer Radius** | Enable this property to cause the radial arrangement to start from the outer radius and move inwards, instead of starting from the inner radius and moving outwards. |
| **Orient** | When enabled, the arrangement is oriented with the selected axis towards the center. |
| **Orientation Axis** | Selects the axis of orientation. Only available when Orient is enabled. Options are:   * X * Y * Z |
| **Base Orientation** | Applies additional rotation, in degrees, to the arrangement in addition to the default axis. Only available when Orient is enabled. Options are:   * X (degrees) * Y (degrees) * Z (degrees) |
| **Flip Axis** | Reverses the facing of the arrangement along the selected axis. Only available when Orient is enabled. |

### Spline Path

You can use the **Spline Path** modifier to have your modified shape follow a spline you create using the [Draw Spline](https://dev.epicgames.com/documentation/en-us/unreal-engine/draw-spline-tool-in-unreal-engine) tool.

[![Spline Path modifier](https://dev.epicgames.com/community/api/documentation/image/a0d47a27-48bc-4385-9c2b-49a96826573b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a0d47a27-48bc-4385-9c2b-49a96826573b?resizing_type=fit)

#### Spline Actor Weak

A prerequisite for using this modifier is to already have a spline actor you can select in the Spline Actor Weak property's drop-down menu. If you have multiple splines, you can choose which of them you want your modified shape to use as a path.

#### Sample Mode

You have multiple options for how you track your shape's progress along the spline path, available in the **Sample Mode** property's drop-down menu.

* **Percentage**: Tracks progress as a percentage of the spline path. This is the default option. This option renames the context slider property to **Progress**.
* **Distance**: Tracks progress in terms of the distance along the length of the spline. The values will vary according to how long your spline is. This option renames the context slider property to **Distance**.
* **Time**: Tracks your progress in terms of how long it takes to progress along the spline. The time it takes to fully progress along a spline is determined by a property on the Spline actor; the default is a 1-second transit time. This option renames the context slider property to **Time**.
* **Point**: Tracks your progress along the spline in discrete hops, from point to point used to describe the spline. The values will vary according to how many points you used to create your spline. This option renames the context slider property to **Point**.

#### Context Slider

The context slider property is how you control the specific point where your shape is along the spline. The name of this property varies depending on the value of the Sample Mode property.

In all cases, you can type a valid value in the field to see the shape at that point on the spline. You can also drag inside the field to move your shape on the spline dynamically. The values shown vary depending on what version of the context slider (and thus which Sample Mode) you are using.

* **Progress**: Displays the value as a percentage from 0 - 100.
* **Distance**: Displays the value in cm. Values longer than the full length of the spline place the shape at the end of the spline.
* **Time**: Displays the value in seconds, down to hundredths of a second. Values larger than the time taken to progress the full length of the spline place the shape at the end of the spline.
* **Point**: Displays which point of the spline the shape is on.

![Spline Path](https://dev.epicgames.com/community/api/documentation/image/9e872fc7-758f-4096-bc1b-66937285c0a4?resizing_type=fit)

#### Orient

When you enable the **Orient** property, your shape is oriented along the spline's tangent.

#### Base Orientation

When the Orient property is enabled, you can use the **Base Orientation** properties to apply a rotation on your shape's default orientation. You can apply the rotation separately on each axis, X, Y, and Z.

#### Scale

When you enable the **Scale** property, the scale of your shape is modified according to the scaling of the spline points. If you increase or decrease the scale property of the spline actor points, you increase or decrease the scale of the modified shape accordingly.

| Spline Path Properties | Description |
| --- | --- |
| **Spline Actor Weak** | Determines which spline actor to use as a path. |
| **Sample Mode** | Determines how to track the modified shape along the spline path. Also determines the name and functionality of the context slider property. Options are:   * Percentage * Distance * Time * Point |
| **Context Slider** | Controls where the shape is on the spline path. The property name changes depending on the value of the Sample Mode property. |
| **Orient** | When enabled, your shape orients along the spline's tangent. |
| **Base Orientation** | Adds rotation to your shape's orientation. Only available when Orient is enabled. |
| **Scale** | When enabled, your shape is scaled based on the spline point scaling. |

## Geometry

You can use Geometry modifiers to build 3D designs without relying on a dedicated modeling program. There are several modifiers created for use with multiple design tasks.

[![geometry modifiers](https://dev.epicgames.com/community/api/documentation/image/3ecaaa96-28aa-40e8-b857-b020900ea643?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3ecaaa96-28aa-40e8-b857-b020900ea643?resizing_type=fit)

Using these tools requires you to use the built-in **Motion Design 2D/3D primitives**, or to convert a static mesh for use by Motion Design using the **Dynamic Mesh Converter**.

[![2D shapes for use with geometry modifiers](https://dev.epicgames.com/community/api/documentation/image/d158682a-ecaf-41ae-bcc6-44025a562754?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d158682a-ecaf-41ae-bcc6-44025a562754?resizing_type=fit)

[![3D shapes for use with geometry modifiers](https://dev.epicgames.com/community/api/documentation/image/759f00e0-b0df-48f4-a472-3cc366f22ce1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/759f00e0-b0df-48f4-a472-3cc366f22ce1?resizing_type=fit)

### Auto Size

The **Auto Size** modifier provides a way for you to automatically resize a modified 2D shape, to act as a background for a selected reference actor.

#### Reference Container

The Reference Container property provides a way to define how the auto size functions. You can select a specific actor to resize to match using the Other option, or you can set it to resize with respect to another actor, depending on the other's position in the Motion Design Outliner hierarchy.

* **Previous**: Resizes to match the previous actor in the Motion Design Outliner.
* **Next**: Resizes to match the next actor in the Motion Design Outliner.
* **First**: Resizes to match the first actor in the Motion Design Outliner.
* **Last**: Resizes to match the last actor in the Motion Design Outliner.
* **Other**: Define a specific actor to resize to match, regardless of its position in the Motion Design Outliner.

#### Reference Actor

When the Reference Container property is set to Other, the **Reference Actor** property determines which actor the modified actor references to resize.

#### Padding Vertical

The **Padding Vertical** property provides a way to make the modified actor vertically taller or shorter than the reference actor. Positive values make the modified actor larger, negative values make the modified actor shorter.

#### Padding Horizontal

The **Padding Horizontal** property provides a way to make the modified actor horizontally wider or thinner than the reference actor. Positive values make the modified actor wider, negative values make the modified actor thinner.

#### Fit Mode

You can use the **Fit Mode** property to determine how your modified actor is resized with respect to the reference actor.

* **Width and Height**: By default, your modified actor resize based on both width and height of the reference actor.
* **Width Only:** Your modified actor only resizes its width to match the reference actor.
* **Height Only**: Your modified actor only resizes its height to match the reference actor.

#### Include Children

When enabled, the **Include Children** property causes your modified actor to resize to account for any children of the reference actor as well.

| Auto Size Properties | Description |
| --- | --- |
| **Reference Container** | Determines the reference actor to compare with for resizing. Options are:   * Previous * Next * First * Last * Other |
| **Reference** **Actor** | Defines a specific actor to compare with for resizing. Only available if the reference container is set to Other. |
| **Padding Vertical** | Adds or removes padding to height when resizing. |
| **Padding Horizontal** | Adds or removes padding to width when resizing. |
| **Fit Mode** | Determines how the modified actor is resized in comparison to the reference actor. Options are:   * Width and Height * Width Only * Height Only |
| **Include Children** | When enabled, include children of the reference actor when resizing. |

### Bend

This modifier provides a way for you to take a Motion Design shape like a cube and bend it using a variety of properties.

The Bend modifier is dependent on an associated Subdivide modifier, which is automatically added and can't be removed.

|  |  |
| --- | --- |
| [Bend modifier, simple bend on a shape](https://dev.epicgames.com/community/api/documentation/image/fa8f8a27-ca98-46e0-abe4-43631fdaf153?resizing_type=fit) | [Bend modifier properties, simple bend](https://dev.epicgames.com/community/api/documentation/image/7a395be8-82c6-457a-a5fe-4f9efa918043?resizing_type=fit) |

There are several properties for manipulating your bend.

#### Bend Position and Bend Rotation

The **Bend Position** and **Bend Rotation** properties give you control over the direction and location of your modified shape's bend. Bend Position provides a way for you to adjust the location of your bend relative to the origin point for your shape. Bend Rotation provides a way to twist your bend along any axis.

The example below demonstrates how you can combine Bend Position and Bend Rotation to create a twist, when you center where the bend is occurring in the shape, then add rotation along the Z axis.

|  |  |
| --- | --- |
| [Bend modifier, complex twist on a shape](https://dev.epicgames.com/community/api/documentation/image/36b71992-44e2-47d3-bfd5-c665d353d380?resizing_type=fit) | [Bend modifier properties, complex twist](https://dev.epicgames.com/community/api/documentation/image/4ee1651e-1d42-4d51-a84f-89fbe0803754?resizing_type=fit) |

#### Angle

The **Angle** property determines how much your shape bends, with a larger value meaning a larger bend, up to a maximum of 180 degrees, which represents a complete fold. You can remove your bend completely by setting the Angle property to 0.0.

#### Extent

The **Extent** property controls how much of your shape is affected by the bend. An extent of 1.0 meaning the entire shape is affected, while smaller values mean a proportionally smaller amount of the shape is affected, centered around the point defined by the Bend Position and Bend Rotation properties.

#### Symmetric Extents

When manipulating the value of the Extent property, enabling the **Symmetric Extents** property causes the upper and lower bounds to be affected identically, otherwise only the upper bound will be affected by changing the value of the Extent property.

#### Bidirectional

When enabled, the **Bidirectional** property causes changes to the value of the Extent property to transform (rotate) the mesh, so both the upper and lower bounds are affected the same way, creating a plane of mirrored symmetry.

Playing with Symmetric Extents and Bidirectional properties.

| Bend Properties | Description |
| --- | --- |
| **Bend Position** | Defines the bend position relative to the shape origin on the various axes. Default value is 0. Options are:   * X position * Y position * Z position |
| **Bend Rotation** | Defines the bend rotation relative to the shape origin on the various axes. Default value is 0 degrees. Options are:   * X degrees * Y degrees * Z degrees |
| **Angle** | Defines how much the shape bends. Default is 25 degrees, range is from 0 to 180. |
| **Extent** | Defines the proportion of the shape bent, with 0 meaning the shape is not bent at all, and 1 meaning the entire shape is bent. |
| **Symmetric Extents** | Enable to cause upper and lower extents to be affected in the same way. |
| **Bidirectional** | Enable to create a plane of symmetry when bending the modified shape. |

### Bevel

You can use the **Bevel** modifier to add a bevel to your shape, and control how deeply beveled your shape is.

#### Inset

You can control how much your shape is bevelled with the **Inset** property. The value of the property is clamped between 0 and half the size of your shape's shortest boundary, that is, the maximum bevel you can add is half the shortest dimension of your shape.

#### Iterations

The **Iterations** property will set the number of subdivisions, but this can be costly when set too high on too many shapes. If you want sharp, angular bevels, you can leave this value at 1. Higher values are useful when you want to have a smooth curve for your bevel.

#### Roundness

The **Roundness** property uses iterations to smooth the shape. The property has a range of values from 2 to -2, with 0 representing no roundness, a straight, angular bevel. A value of 2 means your bevel will have a concave curve that is close to an arc of a circle, while a value of -2 is an inset bevel with the opposite convex curve.

Example with Roundness set to 0.0:

[![Bevel, roundness set to 0](https://dev.epicgames.com/community/api/documentation/image/4296ee7d-cd2d-4e3c-bd3a-db9ef0c1fcd5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4296ee7d-cd2d-4e3c-bd3a-db9ef0c1fcd5?resizing_type=fit)

Example with Roundness set to 2:

[![Bevel, roundness set to 2](https://dev.epicgames.com/community/api/documentation/image/76d88df6-3f93-4d8e-b252-0a20d2e241a7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/76d88df6-3f93-4d8e-b252-0a20d2e241a7?resizing_type=fit)

Roundness, positive 2 (concave) compared to negative 2 (convex):

[![Bevel, comparing roundness 2 to roundness -2](https://dev.epicgames.com/community/api/documentation/image/7c84c7b5-4db2-41ee-bf01-4d4cf611b32a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7c84c7b5-4db2-41ee-bf01-4d4cf611b32a?resizing_type=fit)

| Bevel Properties | Description |
| --- | --- |
| **Inset** | How deeply beveled your shape is, ranging from 0 (no bevel) to half the shortest dimension of your shape |
| **Iterations** | Determines how many sections your bevel is made up of. Used mainly to create a smooth curve in combination with Roundness. |
| **Roundness** | Determines how curved your bevel is and whether the curve is concave (positive values) or convex (negative values). The range is from 2 to -2, with 0 (no curve) as the default. |

### Boolean

The **Boolean** modifier provides a way for you to use Motion Design primitives to modify other shapes. There are several modes:

* **Target**
* **Subtract**
* **Union**
* **Intersect**

These modes are also color-coded, where red (as seen in the image below) is Subtract, blue is Intersect, and green is Union.

[![Boolean, subtract mode](https://dev.epicgames.com/community/api/documentation/image/bbf1b826-46b0-4437-9caa-9eeb92e9cddd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bbf1b826-46b0-4437-9caa-9eeb92e9cddd?resizing_type=fit)

#### Mode

The **Mode** property determines what function of the Boolean modifier you are using. Each is a specific version of the Boolean modifier, and they interact with each other according to specific rules, each described below.

##### Target

Use the **Target** modifier on the shape you are modifying. In the example in the image above, this is the chopped-up sphere.

##### Subtract

When you add the **Subtract** modifier to a shape, it checks where the Target shape's geometry is intersecting with the Subtract shape's geometry, and removes it. The remainder of the shape's geometry is retained, as shown in the image above.

##### Intersect

When you add the **Intersect** modifier to a shape, it checks where the Target shape's geometry is intersecting the Intersect shape's geometry, and retains it. The remainder of the shape's geometry is removed.

[![Boolean, intersect mode](https://dev.epicgames.com/community/api/documentation/image/9a1dd599-aa71-4dbb-9fa7-8765431bbb1d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9a1dd599-aa71-4dbb-9fa7-8765431bbb1d?resizing_type=fit)

##### Union

When applied to a shape, the **Union** modifier combines all shapes that intersect with it and are in the same channel.

[![Boolean, union mode](https://dev.epicgames.com/community/api/documentation/image/eda54eb7-3890-4c78-b487-afea828cc496?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/eda54eb7-3890-4c78-b487-afea828cc496?resizing_type=fit)

#### Channel

For boolean modifiers to interact correctly, they must be assigned to the same **Channel**. In the case of these examples, all the Boolean modifiers are set to channel 0. You can use Boolean modifiers assigned to different channels to create different interactions that don't affect each other.

Using the Channel property to control Boolean interactions.

| Boolean Properties | Description |
| --- | --- |
| **Mode** | Determines how the Boolean modifier functions affect the shape it is attached to. Options are:   * **Target**: The Target mode identifies a shape to be affected by the other Boolean mode options. * **Subtract**: Checks where the Target shape's geometry overlaps with the Subtract shape's geometry, and removes it. * **Intersect**: Checks where the Target shape's geometry overlaps the Intersect shape's geometry, and retains it. * **Union**: Combines all overlapping shapes. |
| **Channel** | Determines the channel. Only Boolean modifiers using the same channel can interact. |

### Extrude

You can use the **Extrude** modifier to thicken a 2D object into 3D space along its depth (by default, the Z-axis). Any rotations you apply to the object affect the extrude direction, which is linked to the Z- axis of the object, not of the level.

#### Extrude Depth

The **Extrude Depth** property controls how much your 2D shape extrudes into 3D, measured in centimeters (cm). The default value is 30 cm.

#### Close Back

Enabled by default, the **Close Back** property causes your extruded shape to close, which creates a solid 3D shape. If you disable it, the extruded section remains open.

|  |  |
| --- | --- |
| [Extrude modifier closed](https://dev.epicgames.com/community/api/documentation/image/1053348d-3f39-4e02-bf9e-ac36ce8096d4?resizing_type=fit) | [Extrude modifier open](https://dev.epicgames.com/community/api/documentation/image/a39a2048-00d9-4eaa-a428-3d84bfb35299?resizing_type=fit) |

#### Extrude Mode

The **Extrude Mode** property controls which side of your 2D shape is extruded into 3D.

* **Opposite**: The side of the shape facing away from you when you initially placed it is extruded. This is the default option.
* **Front**: The side of the shape facing towards you when you initially placed it is extruded.
* **Symmetrical**: Both sides of the shape are extruded.

| Extrude Properties | Description |
| --- | --- |
| **Extrude Depth** | Determines how far your shape extrudes. |
| **Close Back** | Determines whether your extruded shape is closed solid or not. |
| **Extrude Mode** | Determines the direction your shape extrudes. Options are:   * Opposite (default) * Front * Symmetrical |

### Mirror

You can use the **Mirror** modifier to create a mirrored clone of your geometry, and control how the mirroring happens in various ways.

#### Mirror Frame Position and Mirror Frame Rotation

You can use the **Mirror Frame Position** property to offset the mirrored clone by a specified amount, controlling how far apart your original shape and the mirror clone are.

[![Mirror Frame Position](https://dev.epicgames.com/community/api/documentation/image/f0663470-3d96-46cc-96c1-e14c20772de2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f0663470-3d96-46cc-96c1-e14c20772de2?resizing_type=fit)

You can also rotate the mirrored geometry using the **Mirror Frame Rotation** property. In combination, these two properties provide you with the means to control exactly where and how your geometry is reflected by the clone.

#### Apply Plane Cut

You can further modify your geometry by setting up your mirrored geometry to cut into the original actor. To do this, enable the **Apply Plane Cut** property and rotate your geometry with the Mirror Frame Rotation until it collides. You should get a result similar to the image below:

[![Mirror modifier, Apply Plane Cut](https://dev.epicgames.com/community/api/documentation/image/503c0318-bad9-4f07-9d0e-6ac24d52e591?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/503c0318-bad9-4f07-9d0e-6ac24d52e591?resizing_type=fit)

#### Flip Cut Side

You can invert the Apply Plane Cut effect by enabling the **Flip Cut Side** property, which angles and cuts the geometry along the flipped axis at the intersection.

[![Mirror modifier, Flip Cut Side](https://dev.epicgames.com/community/api/documentation/image/8226346b-d3f9-47e5-949d-f29147a7404e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8226346b-d3f9-47e5-949d-f29147a7404e?resizing_type=fit)

| Mirror Properties | Description |
| --- | --- |
| **Mirror Frame Position** | Defines the position of the mirrored geometry relative to the original. |
| **Mirror Frame Rotation** | Defines the rotation of the mirrored geometry relative to the original. |
| **Apply Plane Cut** | Defines a plane intersecting the geometry, mirroring the geometry at the plane. |
| **Flip Cut Side** | Inverts the mirroring at the plane cut. Only available when using Apply Plane Cut. |

### Normal

You can use the **Normal** modifier to regenerate the normal map after converting or modifying the geometry with other modifiers.

### Outline

You can use the **Outline** modifier to give your 2D shape an outline, and control whether the outline is outset or inset.

[![Outline modifier](https://dev.epicgames.com/community/api/documentation/image/34155a86-b4a1-4f03-87a5-a69b1fc06d3b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/34155a86-b4a1-4f03-87a5-a69b1fc06d3b?resizing_type=fit)

#### Mode

The **Mode** property determines whether your outline is Outset (outside the edge of your shape) or Inset (inside the edge of your shape).

#### Distance

The **Distance** property determines how far your outline extends. You can type a specific value, or drag inside the field to dynamically adjust the outline distance.

#### Remove Inside

The **Remove Inside** property hides the part of your shape inside the outline. Enabled by default.

If you disable Remove Inside while using Inset Mode, the shape does not appear to change, but the polygons that make up the underlying geometry do change.

### Pattern

You can use the **Pattern** modifier when you want to create multiple copies of your shapes arranged in a variety of ways.

The **Layout** property allows you to arrange your shapes in the formation of a **Line**, **Grid**, and **Circle**. There are many properties for each of those Layouts, several of which are shared between layout options. Those shared properties are described below.

| Pattern Properties | Description |
| --- | --- |
| **Layout** | Determines the layout arrangement for your actors. Options are:   * Line * Grid * Circle |
| Shared Layout Properties |  |
| --- | --- |
| **Centered** | When enabled, the interaction widget for your layout is placed at the center of the layout's bounding box. |
| **Accumulate Transform** | Recursively apply your specified transforms for every actor added by the Repeat Count property. |
| **Rotation X / Y / Z** | Standard rotation transforms on the specified axes, in addition to the default transform values in the Details panel. |
| **Scale X / Y / Z** | Standard scale transforms on the specified axes, in addition to the default transform values in the Details panel. |

#### Line

The **Line** Pattern Layout provides a way for you to arrange copies of your actor in a straight line along an individual axis.

* You can choose which axis using the **Axis** property, which lines them up along X, Y, or Z.
* The **Axis Inverted** property is useful when you have the Centered property disabled; when enabled, the layout line extends in the opposite direction from the default along the specified axis.
* The **Repeat Count** property determines how many instances of your actor are added along the line you define.
* The **Spacing** property determines how much of a gap there is between actors in your line.

The example below shows a line with the Centered property disabled:

[![Line Pattern, Centered disabled](https://dev.epicgames.com/community/api/documentation/image/aaf1d12a-133b-4134-8444-83bfbe77e2f7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/aaf1d12a-133b-4134-8444-83bfbe77e2f7?resizing_type=fit)

Here's the same example with the Centered property enabled:

[![Line Pattern, Centered enabled](https://dev.epicgames.com/community/api/documentation/image/3f48a1e6-25fe-46b5-83c9-342151a13f59?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3f48a1e6-25fe-46b5-83c9-342151a13f59?resizing_type=fit)

The example below shows the effects of the Accumulate Transform property for a Line pattern. The transform applied is to scale down the sphere to 0.4, which is then applied again recursively at each repetition:

[![Line Pattern, accumulate transforms](https://dev.epicgames.com/community/api/documentation/image/70ca83ee-954b-4312-855b-7607cfbb5250?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/70ca83ee-954b-4312-855b-7607cfbb5250?resizing_type=fit)

By adding rotation transforms along with scaling, you can create patterns like the following image:

[![Line Pattern, accumulate transforms with rotation](https://dev.epicgames.com/community/api/documentation/image/925e490e-bb13-483e-8523-1994069a9014?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/925e490e-bb13-483e-8523-1994069a9014?resizing_type=fit)

| Additional Line Pattern Properties | Description |
| --- | --- |
| **Axis** | Determines the axis of the line layout before any rotation transforms. Standard X / Y / Z options. |
| **Axis Inverted** | Inverts the direction your line layout extends along the selected axis. Only functions when the Centered property is not enabled. |
| **Repeat Count** | The number of instances of the actor in your line layout. |
| **Spacing** | The spacing between actors in your line layout. |

#### Grid

[![Grid Pattern Layout](https://dev.epicgames.com/community/api/documentation/image/0eab1624-2ff5-4199-b95a-18d56c6d67b8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0eab1624-2ff5-4199-b95a-18d56c6d67b8?resizing_type=fit)

The **Grid** Pattern Layout provides a way for you to arrange copies of your actor into a grid.

* You can use the **Plane** property to arrange your grid on the XY, XZ, or YZ planes. The example in the image above shows a grid arranged on the YZ plane.
* The **Axis Inverted** property is useful when you have the Centered property disabled. When it is enabled, it will force your grid to center itself based on its own bounding box.
* The **Repeat Count** property determines how many instances of your actor are added along the axes that define your grid, with separate values for each axis.
* The **Spacing** property determines how much of a gap there is between actors in your grid.

Much like the other Pattern modifiers, enabling the Accumulate Transform property creates effects similar to the image below, always perpendicular to the grid's plane:

[![Grid Pattern Layout accumulate transforms](https://dev.epicgames.com/community/api/documentation/image/7ab902a4-142f-48ff-bcaa-ef46135218a0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7ab902a4-142f-48ff-bcaa-ef46135218a0?resizing_type=fit)

| Layout Grid Pattern Properties | Description |
| --- | --- |
| **Plane** | Determines the plane for your grid layout before any rotation transforms. Options are:   * XY * XZ * YZ |
| **Axis Inverted** | Inverts the direction your grid layout extends along the selected axis. You can invert each axis separately. Only functions when the Centered property is not enabled. |
| **Repeat Count** | The number of instances of the actor in your grid layout. Each axis of the grid has a separate value for this property. |
| **Spacing** | The spacing between actors in your grid layout. Each axis of the grid has a separate value for this property. |

#### Circle

[![Circle Pattern Layout](https://dev.epicgames.com/community/api/documentation/image/0240be90-5e69-4bda-9c97-2172c348b663?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0240be90-5e69-4bda-9c97-2172c348b663?resizing_type=fit)

The **Circle Pattern Layout** provides a way to arrange copies of your actor in a circle.

* You can use the **Plane** property to arrange your circle on the XY, XZ, or YZ plane. The example in the image above shows a circle arranged on the YZ plane.
* The **Radius** property determines the size of the circle layout, and so determines how spread out your pattern elements are.
* You can arrange the total angle that your circle group covers by setting the **Start Angle** and **Full Angle** properties. For example, to achieve a 90 degree angle, set your Start Angle to 0.0 and your Full Angle to 90 to create a result similar to the following image:

  [![Circle Pattern Layout, Start Angle and Full Angle](https://dev.epicgames.com/community/api/documentation/image/461ac06f-101a-4e72-add2-7ac7f7409815?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/461ac06f-101a-4e72-add2-7ac7f7409815?resizing_type=fit)

  You can set  the values to create a complete circle by using a combination of Start Angle = 0 and Full Angle = 360.
* The **Repeat Count** property determines how many instances of your actor are added to your circle.

Disabling the **Centered** property aligns all content to the right of the initial actor as shown below.

Using the Centered property with the Circle Pattern Layout.

Enabling the Accumulate Transform property applies changes to the rotation and scale for every repeated actor. Here is an example of increasing the scale of the X value between 1 and 1.5:

![](https://dev.epicgames.com/community/api/documentation/image/d6ee40dd-d0a2-4d3d-b8b3-6f2f26c65d8b?resizing_type=fit)

Accumulate transform using the Scale property for the Circle Pattern Layout.

| Additional Circle Layout Properties | Description |
| --- | --- |
| **Plane** | Determines the plane for your circle layout before any rotation transforms. Options are:   * XY * XZ * YZ |
| **Radius** | The radius of your circle layout. A larger radius value means a bigger circle, which also controls the spacing between actors. |
| **Start Angle** | The starting angle for your circle layout. The value range is from 0 to 360, in degrees. |
| **Full Angle** | The ending angle for your circle layout. The value range is from 0 to 360, in degrees. |
| **Repeat Count** | The number of instances of the actor in your circle layout. |

### Plane Cut

[![Plane Cut modifier](https://dev.epicgames.com/community/api/documentation/image/865075d1-4b13-4b0e-bd73-9584ec007316?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/865075d1-4b13-4b0e-bd73-9584ec007316?resizing_type=fit)

The **Plane Cut** modifier provides a way for you to cut through Motion Design geometry using just a few properties.

#### Plane Origin and Plane Rotation

The **Plane Origin** property provides a way to position the cut relative to the origin point of the modified geometry on the Z-axis, positive values move up, negative values move down. The **Plane Rotation** property provides a way to rotate the cut along any of the 3 axes (X, Y, Z).

Using a combination of Plane Origin and Plane Rotation to situate the cut, you can produce results like the following example.

A geometry example before using Plane Cut:

[![Plane Cut initial shape](https://dev.epicgames.com/community/api/documentation/image/3bf984b5-b0da-4b59-b40e-6a0c886a8dd6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3bf984b5-b0da-4b59-b40e-6a0c886a8dd6?resizing_type=fit)

A geometry example after using Plane Cut:

[![Plane Cut modifier applied](https://dev.epicgames.com/community/api/documentation/image/2e019618-2e2e-4c20-8518-0ef934d2b692?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2e019618-2e2e-4c20-8518-0ef934d2b692?resizing_type=fit)

#### Invert Cut

Enabling the **Invert Cut** property reverses the existing cut. Inverting the cut in the preceding example has the following result:

[![Plane Cut invert cut enabled](https://dev.epicgames.com/community/api/documentation/image/6d9e42a3-0b00-45bf-beca-1473ff56c073?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6d9e42a3-0b00-45bf-beca-1473ff56c073?resizing_type=fit)

#### Fill Holes

If you want to fill in the area that the cut created, you can use the **Fill Holes** property. Using this property with the preceding example produces a result like the following image:

[![Plane Cut fill holes enabled](https://dev.epicgames.com/community/api/documentation/image/b46d6be2-5e34-47b9-b2af-2f5b0ced834a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b46d6be2-5e34-47b9-b2af-2f5b0ced834a?resizing_type=fit)

#### Use Preview

Enabling the **Use Preview** property provides a way for you to visualize the cut you are making, using a green plane.

| Plane Cut Properties | Description |
| --- | --- |
| **Plane Origin** | Defines the origin of the cut, relative to the origin of the geometry on the Z-axis. The default value is 0. |
| **Plane Rotation** | Defines the rotation of the cut, on all 3 axes (X, Y, Z). The default values are 90, 0, 0 (a vertical cut on the X axis). |
| **Invert Cut** | Enable this property to reverse the cut section of the geometry. |
| **Fill Holes** | Enable this property to fill the hole in the cut geometry. |
| **Use Preview** | Enable to show the preview plane of the cut relative to the geometry. |

### Size to Texture

### Size to Texture

You can use the **Size to Texture** modifier to make sure that your shape matches the proportions on the texture applied to it, this avoids distortions in how the texture appears on-screen.

Usually, you use this modifier alongside a remote control setup where you can swap between textures mapped to the shape at the touch of a button, so that your shape adjusts automatically to accommodate textures of different sizes.

#### Texture

The **Texture** property provides a way to select the texture your shape resizes to match. By setting up this property with a remote control preset and multiple textures of different sizes, you can swap which of those textures is assigned to your modified shape.

#### Rule

The Rule property gives you the choice between either:

* **Adaptive Height**, where your shape adapts its height to match the texture.
* **Adaptive Width**, where its width matches the texture.

In both cases, the texture ratio is maintained.

The Size to Texture modifier is intended for use with rectangular shapes. Using it with other shapes will result in unintended behavior. Use at your own risk.

| Size to Texture Properties | Description |
| --- | --- |
| **Texture** | Determines the texture your shape resizes to match. |
| **Rule** | Determines how your texture resizes, to maintain the texture ratio. Options are:   * Adaptive Height * Adaptive Width |

### Spline Sweep

The **Spline Sweep** modifier provides a way to sweep a 2D shape along the length of a spline, creating a 3D shape that fills space while following the spline path. The spline actor does not need to be anywhere near the modified shape. As long as your spline actor is present anywhere on the level, the modified shape will create a 3D shape following the spline's path from the modified shape's initial position.

[![Spline Sweep modifier](https://dev.epicgames.com/community/api/documentation/image/145e1350-abea-407b-a592-fbc804a44e81?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/145e1350-abea-407b-a592-fbc804a44e81?resizing_type=fit)

#### Spline Actor Weak

A prerequisite for using this modifier is to already have a spline actor you can select in the **Spline Actor Weak** property's drop-down menu. If you have multiple splines, you can choose which of them you want your modified shape to use to create the sweep.

#### Sample Mode

The **Sample Mode** property determines how often you sample the spline when generating the sweep. The options are:

* **Full Distance**: The sweep is generated by sampling the spline a number of times equal to the value of the Steps property, regardless of the length of the spline. When using the Full Distance Sample Mode, increasing the length of the spline decreases the precision of the sampling, as the samples are spread further apart along the spline.
* **Custom Distance**: The sweep is generated by sampling the spline a number of times equal to the Steps value for every multiple of the value of the Sample Distance property. When using the Custom Distance Sample Mode, increasing the length of the spline does not decrease the precision of the sampling, as the sampling is repeated for every multiple (or fraction thereof) of the Sample Distance value.

  For example, if the Sample Distance is 2000 Unreal Units, the value of the Steps property is 10, and the spline is 3000 units long, the spline is sampled 15 times. If you then lengthen the spline to 4000 units long, the spline is instead sampled 20 times.

#### Sample Distance

The **Sample Distance** property determines how frequently your modified shape samples the spline when you are using the Custom Distance Sample Mode option. Smaller values cause the  shape to sample the spline more frequently, which results in a smooth sweep.

[![Spline Sweep with small sample distance](https://dev.epicgames.com/community/api/documentation/image/41661484-f513-45fd-aa3e-7a3d4c8872b0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/41661484-f513-45fd-aa3e-7a3d4c8872b0?resizing_type=fit)

#### Steps

The **Steps** property determines how often your modified shape samples the spline within the distance specified by the Sample Mode and Sample Distance properties, either over the full length of the spline with the Full Distance Sample Mode, or over every iteration of the value of the Sample Distance when using the Custom Distance Sample Mode.

#### Progress Properties

The three **Progress** properties provide a way to control how much of the spline is used to generate your sweep. The effects of all three properties are additive.

##### Progress Offset

The **Progress Offset** property provides a way for you to start your sweep further along the length of the spline actor. When you enable the Looped property, the spline sweep connects back to the offset position you selected, and you can use a Progress Offset value greater than 1. Changing the default values of the Progress Start or Progress End properties changes the Progress Offset behavior, see Progress Start and Progress End below for more information.

The value of this property is a proportion, so a value of 0 represents the start of the spline, and a value of 1 represents the end of the spline.

Working with the Spline Sweep modifier.

##### Progress Start

The **Progress Start** property provides a way for you to start your sweep further along the length of the spline actor. If you enabled the Looped property (see below), the spline sweep does not connect back to the start position you selected.  The value of this property is a proportion, so a value of 0 represents the start of the spline, and a value of 1 represents the end of the spline.

##### Progress End

The **Progress End** property provides a way for you to end your sweep before it reaches the end of the spline actor. If your spline is a loop, the sweep ends when it reaches the point along the length of the spline that matches the value of the property, so that the skipped part of the spline at the end is not included in the sweep. The value of this property is a proportion, so a value of 0 represents the start of the spline, and a value of 1 represents the end of the spline.

[![Spline Sweep Progress Start and Progress End](https://dev.epicgames.com/community/api/documentation/image/56632bbf-03c1-41dd-8f29-32375c71ff76?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/56632bbf-03c1-41dd-8f29-32375c71ff76?resizing_type=fit)

#### Scale Start and Scale End

The Scale Start and Scale End properties control the scaling of your modified shape along the length of the sweep. The values of these properties are proportions, the relative scaling of the shape at the start and end of the sweep compared to its unmodified size, respectively. The default values of 1.0 for both properties means the shape remains unmodified.

Changing the values causes the scaling of the shape to be interpolated from the value of the Scale Start at the beginning of the sweep, to the value of the Scale End and at the end of the sweep.

For example, changing the value of the Scale Start property to 0.5 and the value of the Scale End property to 2.0 would mean the shape begins at half its unmodified size then grows along the length of the spline sweep until it reaches twice its unmodified size at the end.

[![Spline Sweep Scale Start and Scale End](https://dev.epicgames.com/community/api/documentation/image/4a84a18e-fd6a-4700-890f-1680f467d740?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4a84a18e-fd6a-4700-890f-1680f467d740?resizing_type=fit)

#### Capped

The **Capped** property is enabled by default, and closes the ends of the sweep to create a solid shape. You can disable the property if you want the ends of the sweep to remain open.

#### Looped

By enabling the **Looped** property you connect the ends of your sweep into a closed loop.

If Progress Start, Progress End, or both are enabled, they will override the Looped property and break the loop.

[![Spline Sweep Looped](https://dev.epicgames.com/community/api/documentation/image/68e5c249-9484-45f2-8b7b-08586f635d68?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/68e5c249-9484-45f2-8b7b-08586f635d68?resizing_type=fit)

| Spline Sweep Properties | Description |
| --- | --- |
| **Spline Actor Weak** | Determines which spline actor to use to create your sweep. |
| **Sample Mode** | Determines how the spline length is sampled. Options are:   * Full Distance * Custom Distance |
| **Sample Distance** | Determines the sample distance. Only available when Sample Mode is set to Custom Distance. The default value is 1000. |
| **Steps** | Determines how many times the spline is sampled within the distance defined by the Sample Mode property. The default value is 10. |
| **Progress** **Offset** | Determines how much offset to add to the start of the sweep, as a proportion of the spline length. Connects back when the Looped property is enabled. The default value is 0. |
| **Progress Start** | Determines where along the length of the spline to start the sweep, as a proportion of the spline length. The default value is 0. |
| **Progress End** | Determines where along the length of the spline to end the sweep, as a proportion of the spline length. The default value is 1. |
| **Scale Start** | Determines the relative scaling of the modified shape at the start of the sweep. |
| **Scale End** | Determines the relative scaling of the modified shape at the end of the sweep. |
| **Capped** | When enabled, the ends of the sweep are capped. Not functional on a looped sweep. |
| **Looped** | When enabled, the end of the sweep connects back to the start to form a closed loop. |

### Subdivide

![Subdivide modifier](https://dev.epicgames.com/community/api/documentation/image/444aeac1-423a-42ad-9cd9-0a8d4fbc95d2?resizing_type=fit)

The **Subdivide** modifier takes your dynamic mesh and subdivides the mesh to increase or decrease the number of polygons. This modifier is automatically added as a required dependency when you add a modifier like Bend or Taper.

#### Cuts

The **Cuts** property determines how much the target shape gets subdivided. Increasing the value increases the number of cuts and therefore polygons, which produces a smoother effect but requires more resources to render.

#### Type

The **Type** property determines how the polygons are subdivided. There are several different algorithms available to calculate this, the options are:

* **Selective**: The polygons created can be different proportions, arranged in patterns.
* **Uniform**: All polygons are proportionally the same . This is the default.
* **PN**: Smooths the polygons. For the best results, enable the **Regenerate Normals** property, which is only available when you select this Type option.

Type options for the Subdivide modifier.

| Subdivide Properties | Description |
| --- | --- |
| **Cuts** | Determines the number of cuts. The default value is 2. |
| **Type** | Options are:   * Selective * Uniform (default) * PN |
| **Regenerate Normals** | Enable to regenerate normals. Only available when Type is set to PN. |

### Taper

The **Taper** modifier provides a way for you to narrow your shape, at multiple points along the surface.

The Taper modifier is dependent on an associated Subdivide modifier, which is automatically added and can't be removed.

To create a smoother shape, you can use the Cuts property of the Subdivide modifier associated with the Taper modifier. Setting the Cuts count to 9 produces a relatively smooth curve. If you reduce the Cuts count to 3, you get a blocky curve instead of a smooth curve.

#### Amount

The **Amount** property determines how much tapering to apply to your shape. The range is a proportion, where 0 means no taper, and 1 means taper to a point.

#### Extent

The **Extent** property determines how much of the shape is tapered. The example below is a simple taper with the Extent value set to the default Whole Shape option.

[![Taper modifier extent property](https://dev.epicgames.com/community/api/documentation/image/662d8a5c-72a0-4ee9-9aca-959e1094edb0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/662d8a5c-72a0-4ee9-9aca-959e1094edb0?resizing_type=fit)

Setting the value to **Custom** provides the option to control the **Upper Extent** (starting from the top and extending downwards) and **Lower Extent** (starting from the bottom and extending upwards) properties separately, in both cases with a range from 0 to 100%. You can use these to create more complex tapers.

#### Interpolation Type

The Interpolation Type property determines the curve applied to your shape by the modifier. The default value is **Linear**, shown in the image above. Other options change the curve, as shown below:

* **Quadratic**

  [![Taper modifier quadratic interpolation](https://dev.epicgames.com/community/api/documentation/image/e17340ec-3fd2-4d1a-900d-b40c0c2c516d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e17340ec-3fd2-4d1a-900d-b40c0c2c516d?resizing_type=fit)
* **Cubic**

  [![Taper modifier cubic interpolation](https://dev.epicgames.com/community/api/documentation/image/596614e1-04bf-4af4-a7db-69929aa3ea01?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/596614e1-04bf-4af4-a7db-69929aa3ea01?resizing_type=fit)
* **Quadratic Inverse**

  [![Taper modifier quadratic inverse interpolation](https://dev.epicgames.com/community/api/documentation/image/2dee5576-9419-4d09-8363-6762515f979d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2dee5576-9419-4d09-8363-6762515f979d?resizing_type=fit)
* **Cubic Inverse**

  [![Taper modifier cubic inverse interpolation](https://dev.epicgames.com/community/api/documentation/image/592784da-fb8a-417a-b202-8d3c0447f39f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/592784da-fb8a-417a-b202-8d3c0447f39f?resizing_type=fit)

#### Reference Frame

The **Reference Frame** property controls how the taper is applied with reference to the position of the shape. By default, the taper references the **Mesh Center**, but you can set the property to **Custom**, and apply an offset to the X and Y values. This will cause the taper to lean towards the direction of the offset.

| Taper Properties | Description |
| --- | --- |
| **Amount** | Determines how much tapering, as a proportion. 0 is no taper, 1 is taper to a point. |
| **Extent** | Determines how much of the shape is tapered. Options are:   * Whole Shape * Custom - use the Upper Extent and Lower Extent properties to control the custom extent. |
| **Upper Extent** | Only available when Extent is set to Custom. Determines the upper extent affected by the taper. Range is 0 - 100%. |
| **Lower Extent** | Only available when Extent is set to Custom. Determines the lower extent affected by the taper. Range is 0 -  100%. |
| **Interpolation Type** | Determines the curve of the taper. Options are:   * Linear (default) * Quadratic * Cubic * Quadratic Inverse * Cubic Inverse |
| **Resolution** | Deprecated. Use the Cuts function of the associated Subdivided modifier. |
| **Reference Frame** | Determines the reference frame. Options are:   * Mesh Center * Custom - uses the Offset property to control the reference frame. |
| **Offset** | Only available when the Reference Frame is set to Custom. Determines the offset applied to the reference frame on the X and Y axis. |

### Dynamic Mesh Converter

The shapes that you create using Motion Design's procedural shape tools aren’t the same as a static mesh, and therefore static meshes aren’t fully compatible with geometry modifiers. For full compatibility with all geometry modifiers, you must first convert your static mesh into a **dynamic mesh**.

Static meshes are functional with some modifiers like Grid Arrange, because the geometry has several actors present. However, if you want to use a static mesh with tools such as Patterns and Mirror, you first need to convert it.

Only geometry modifiers require dynamic meshes. All other modifiers are functional when used with static meshes.

[![Dynamic Mesh Converter modifier](https://dev.epicgames.com/community/api/documentation/image/39b009f2-be4e-4220-a9cb-19fe70f24c81?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/39b009f2-be4e-4220-a9cb-19fe70f24c81?resizing_type=fit)

To convert your static mesh, select your static mesh actor and add a **Dynamic Mesh Converter**.

[![Selecting the Dynamic Mesh Converter modifier](https://dev.epicgames.com/community/api/documentation/image/5ea48d1c-53a7-47bf-a7f5-aac195a79c37?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5ea48d1c-53a7-47bf-a7f5-aac195a79c37?resizing_type=fit)

[![Dynamic Mesh Converter properties](https://dev.epicgames.com/community/api/documentation/image/b581c5bf-f213-4a5c-a428-e590123079ec?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b581c5bf-f213-4a5c-a428-e590123079ec?resizing_type=fit)

The default property settings are sufficient for the majority of use cases, especially when you aren’t dealing with meshes attached to a skeleton or other similarly complex use cases.

[![Adding a modifier to a newly-converted dynamic mesh](https://dev.epicgames.com/community/api/documentation/image/c94c16f6-a4db-4f57-93cc-5fe169bff0a8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c94c16f6-a4db-4f57-93cc-5fe169bff0a8?resizing_type=fit)

You now have the complete list of modifiers at your disposal. Here is an example of applying the Pattern Circle Layout and adjusting some settings:

[![Pattern Circle Layout applied to a converterd Dynamic Mesh](https://dev.epicgames.com/community/api/documentation/image/6c178578-59b1-4094-a503-f5d349135995?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6c178578-59b1-4094-a503-f5d349135995?resizing_type=fit)

For more complex use cases, refer to the property descriptions below.

#### SourceActor

You can change the target actor for your Dynamic Mesh converter using the **SourceActor** property drop-down menu, which gives you access to all the actors in your level, and tools to search for and select the actor you want.

#### Component Type

If your selected actor has multiple components, you can decide which to account for in the conversion using the **Component Type** property, which has a drop-down menu of selectable components types:

* Static Mesh Component
* Dynamic Mesh Component
* Skeletal Mesh Component
* Brush Component
* Procedural Mesh Component

By default, all are selected. Deselect any you don't want included in the conversion to a dynamic mesh.

[![Dynamic Mesh Converter component types](https://dev.epicgames.com/community/api/documentation/image/96900e96-0e07-49f0-ba4e-883d510932e4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/96900e96-0e07-49f0-ba4e-883d510932e4?resizing_type=fit)

#### Filter Actor Mode

You can filter out actors to convert using the **Filter Actor Mode** property, either by including specific actors, or excluding specific actors. You can define the actors to include or exclude using the **Filter Actor Classes** array property.

#### Include Attached Actors

If your selected actor has other actors attached to it, the **Include Attached Actors** property means that by default, they are also converted. If you want to exclude them from the conversion, you can disable the property.

#### Hide Converted Mesh

When you add the modifier, by default it automatically converts your static mesh into a dynamic mesh and hides the original, due to the **Hide Converted Mesh** property. You can disable this property if you also want to see the original static mesh alongside the  dynamic mesh.

#### Update Interval

You can determine how often your converted dynamic mesh checks the source mesh for changes using the **Update Interval** property. The default value is 1 (every second), but you can choose larger or smaller values. A value of 0 or less disables checking for updates.

| Dynamic Mesh Converter Properties | Description |
| --- | --- |
| **SourceActor** | Identifies the target actor. You can use the drop-down menu to select the actor. |
| **Component Type** | Determines which component types are tracked using a selectable list in a drop-down menu. |
| **Filter Actor Mode** | Enables actor filtering. Options are:   * None (default) * Include: only actors matching the filter are converted. * Exclude: actors matching the filter are not converted. |
| **Filter Actor Classes** | Use this array property to define actors affected by the Filter Actor Mode property when it is set to Include or Exclude. |
| **Include Attached Actors** | When enabled, children of the modified mesh are also converted. |
| **Hide Converted Mesh** | When enabled, hides the original mesh, showing only the dynamic mesh |
| **Update Interval** | Defines how often the dynamic mesh checks the original mesh for changes. Values of 0 or less mean no updates. |

## Rendering

### Material Parameter

The **Material Parameter** modifier gives you a way to set parameter values on dynamic material instances. This means if you create a dynamic material instance from a material, you can adjust the parameters using this modifier.

Because parameters cannot be changed on regular material assets, you first need to create a dynamic material instance using a Blueprint, the Material Designer, or C++, and assign it to your geometry. Only then can you add this modifier to your shape and use it to adjust your material instance's values.

#### Parameter Properties

The Material Parameter modifier has 3 properties that function as Map containers:

* **Scalar Parameters** (for example, opacity)
* **Vector Parameters** (for example, color)
* **Texture Parameters** (for example, roughness)

All 3 function similarly. You can add one or more variables from your dynamic material instance to the appropriate parameter properties. You can then manually control the value of the variable from the modifier parameter, as a slider. You can add as many variables to the parameter properties as you want.

[![Material Parameter modifier map properties](https://dev.epicgames.com/community/api/documentation/image/93f8f949-f71a-46e0-bcaf-bff599f67460?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/93f8f949-f71a-46e0-bcaf-bff599f67460?resizing_type=fit)

#### Update Children

The **Update Children** property is enabled by default. Any children of the shape you attached the Material Parameter modifier to are also affected by the changes you make to your dynamic material instance. By disabling the property, only the shape you attached the modifier to is affected by your changes to the dynamic material instance's variables.

| Material Parameter Properties | Description |
| --- | --- |
| **Scalar Parameters** | A map container for scalar variables from your dynamic material instance where you can modify their values. Can contain multiple variables.  Example: opacity |
| **Vector Parameters** | A map container for scalar variables from your dynamic material instance where you can modify their values. Can contain multiple variables.  Example: color |
| **Texture Parameters** | A map container for scalar variables from your dynamic material instance where you can modify their values. Can contain multiple variables.  Example: roughness |
| **Update Children** | When enabled, children of the modified shape are also affected by changes to the dynamic material instance variables. |

### Global Opacity

You can change the opacity on one or several nested actors using the **Global Opacity** modifier. In the example below, we built every texture under the “Translucent Textures” folder in **Material Designer** and set them to “Translucent.” This ensures they function appropriately with the Global Opacity modifier.

[![Global settings Blend Mode Translucent](https://dev.epicgames.com/community/api/documentation/image/222128c6-97cc-4954-811d-1e08f8306cfe?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/222128c6-97cc-4954-811d-1e08f8306cfe?resizing_type=fit)

The Global Opacity property itself has a proportion value from 0 to 1, with 0 representing completely transparent (invisible) and 1 representing completely opaque (the default).

#### Update Children

When you enable the **Update Children** property, changing the Global Opacity setting on the modifier applied to the null actor parent updates all the children (like the Image4, Image3, Image2, and Image1 actors in the example image below) as well.

[![Global Opacity modifier, initial](https://dev.epicgames.com/community/api/documentation/image/f7cb4d05-5c67-41de-a8b3-f6ae3b78b906?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f7cb4d05-5c67-41de-a8b3-f6ae3b78b906?resizing_type=fit)

With this setup, you can change your Global Opacity value to less than 1.0 to fade your images. Here is an example with the value set to .2:

[![Global Opacity modifier, opacity lowered](https://dev.epicgames.com/community/api/documentation/image/60d7a7d8-1b0d-4a48-9617-e56ba26bfae8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/60d7a7d8-1b0d-4a48-9617-e56ba26bfae8?resizing_type=fit)

| Global Opacity Properties | Description |
| --- | --- |
| **Global Opacity** | Determine the opacity of the modified actors, with a range from 0 to 1, where 0 is fully transparent and 1 is fully opaque. |
| **Update Children** | When enabled, any change to the opacity of the parent updates the opacity of any children accordingly. |

### Translucent Priority

Sorting the visibility of your elements based on where they are in the outliner using the Translucent Priority modifier is a core feature of Motion Design. To accomplish this, you need to make sure your material setting for each actor that needs sorting is set to **Translucent**.

#### Sort Mode

Using the **Sort Mode** property, you have multiple ways to sort your actors using Translucent Priority.

* You can use the **Outliner Top First** or **Outliner Bottom First** options to sort them based on their position in the **Outliner**.
* You can use the **Camera Distance** option to sort them based on their distance from the camera.
* You can use the **Manual** option then set the value of the **Sort Priority** property to a higher or lower number to sort them yourself directly.

##### Outliner Top First and Outliner Bottom First

The image below shows an example using the Outliner Top First option to determine which character sits at the front. We placed the Translucent Priority modifier at the top of the level, and because the Sort Mode is set to Outliner Top First, it automatically assessed the child image actors’ priority based on the order we placed them in the Outliner panel:

[![Translucent Priority - Outliner Top First](https://dev.epicgames.com/community/api/documentation/image/0c2eeac5-79b2-4469-be02-a5e27497199c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0c2eeac5-79b2-4469-be02-a5e27497199c?resizing_type=fit)

Note how the Blend Mode is set to “Translucent.”

[![Translucent Priority - Blend Mode set to Translucent](https://dev.epicgames.com/community/api/documentation/image/9b4f1139-a40c-4a3e-a7ce-5b90c37e2755?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9b4f1139-a40c-4a3e-a7ce-5b90c37e2755?resizing_type=fit)

In this example, to make the middle character appear in the foreground, you move the character's actor (Character2 in the image) above the other actor (Character1) in the Outliner.

[![Translucent Priority, changing Outliner order to change priority](https://dev.epicgames.com/community/api/documentation/image/1eee0afd-2092-4cac-b98f-6f1bfab12bcf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1eee0afd-2092-4cac-b98f-6f1bfab12bcf?resizing_type=fit)

##### Camera Distance

The **Camera Distance** option functions similarly to the Outliner Top First and Outliner Bottom First options, but instead of operating based on the Outliner position, it uses the relative position of the modified actors with respect to the camera in your level. You can adjust the translucent priority by translating the actors inside your level to be closer or further away from the camera.

###### Camera Actor

When using the Camera Distance option, you can use the **Camera Actor** property to select which camera is the reference for determining translucent priority, using a variety of methods including selecting it in the level editor, the viewport, or the scene.

##### Manual

When you use the **Manual** option to set translucent priorities, you should set them on each actor, as opposed to using the automatic sorting seen in the above example image. Any manual assignment has priority over the automatic assignment at the top of the group, as shown in the image below:

[![Translucent Priority, manual option](https://dev.epicgames.com/community/api/documentation/image/b245967c-b206-428e-9ea8-30c8bec6c5e0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b245967c-b206-428e-9ea8-30c8bec6c5e0?resizing_type=fit)

Setting the manual sort priority of Character3 (the character with the ponytails) to 3 forces it to the foreground. Setting the manual sort priority of Character2 (the character with the ski mask) to 1 forces the character to the back.

#### Sort Priority Offset

The value of the **Sort Priority Offset** property is shared across all the Translucent Priority modifiers in your level. It applies an offset to the sorting priority of all modifiers in the level. The default value is 0, no offset.

#### Sort Priority Step

The value of the **Sort Priority Step** property is shared across all the Translucent Priority modifiers in your level. It determines the incremental steps for all the Translucent Priority modifiers in your level. The default value is 1.

#### Include Children

You can enable the **Include Children** property to automatically include any children of an actor you are sorting using Translucent Priority

| Translucent Priority Properties | Description |
| --- | --- |
| **Sort Mode** | Determines the method for calculating translucent priority. Options are:   * Outliner Top First * Outliner Bottom First * Camera Distance * Manual |
| **Camera Actor** | Only available when the Sort Mode is set to Camera Distance. Provides a way to select the camera actor used to orient your translucent priority sorting. |
| **Sort Priority** | Only available when the Sort Mode is set to Manual. Determines the manual translucent sort priority. |
| **Sort Priority Offset** | Adds an offset to the translucent sort priority. The value of the property is shared for all Translucent Priority modifiers in your level. |
| **Sort Priority Step** | Determines the incremental steps for setting Translucent Priority. The default value is 1. |
| **Include Children** | When enabled, children of the actor modified by the Translucent Priority modifier are also affected. |

### Visibility

The **Visibility** modifier provides a way for you to select a group of actors and control their visibility, showing or hiding them as you choose.

[![Visibility modifier](https://dev.epicgames.com/community/api/documentation/image/1202d5b0-9ba1-4277-87b0-ea06af66ff50?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1202d5b0-9ba1-4277-87b0-ea06af66ff50?resizing_type=fit)

#### Index

The value of the **Index** property is the main method by which you control the visibility of your actors. The index ordering starts at zero (0), and is assigned automatically to the actors in the order they are added to the parent. If you want your index value to line up with a 1, 2, 3 actor count setup, you need to add a “dummy” null actor to occupy the 0 value position in the index.

For this example, the Visibility modifier's Index property is set to 3, so all three actors are visible.

#### Treat as Range

The default behavior of the Visibility modifier is to treat the Index as a range, showing all the actors with an index position equal to or less than the value of the Index property. If instead you only want to see actor 2 when the value in the Index is 2, then you need to disable the **Treat as Range** property. If you do so, and select 2 as your Index, you will only see the actor with the index position of 2, similar to the example below:

[![Visibility modifier, treat as range disabled](https://dev.epicgames.com/community/api/documentation/image/ed21affa-3a29-4c4c-9529-52599f088811?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ed21affa-3a29-4c4c-9529-52599f088811?resizing_type=fit)

#### Invert Visibility

Conversely, if you want to show everything except the 2nd actor, then you can also enable the **Invert Visibility** property, which produces a result similar to the image below:

[![Visibility modifier, invert visibility](https://dev.epicgames.com/community/api/documentation/image/c55c0ae6-f7b9-4f2e-873a-13fdf40aaa10?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c55c0ae6-f7b9-4f2e-873a-13fdf40aaa10?resizing_type=fit)

You can also combine Treat as Range and Invert Visibility to produce a result like the following image. With the Index value set to 1, the modifier hides the first actor due to the inversion, and reveals the two remaining actors due to the Treat as Range property.

[![Visibility modifier, combining properties to hide specific actors](https://dev.epicgames.com/community/api/documentation/image/f1bd7a12-c610-46ff-ba99-6025e4f4d204?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f1bd7a12-c610-46ff-ba99-6025e4f4d204?resizing_type=fit)

These visibility states are all represented in your Motion Design Outliner on the left side, as shown in this close-up image of the example:

[![Visibility indicated in the Outliner](https://dev.epicgames.com/community/api/documentation/image/e7a676dd-526f-416d-a024-ec7c24c4f4b2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e7a676dd-526f-416d-a024-ec7c24c4f4b2?resizing_type=fit)

#### Skip when Hidden

The **Skip when Hidden** property ensures that hiding the parent actor will hide the children as well. So, if you hide the null actor with the Visibility modifier attached to it, you hide everything. This is the default value, as it is likely to be a common use case.

| Visibility Properties | Description |
| --- | --- |
| **Index** | Defines which actors are shown by the Visibility modifier. Each actor is associated with an Index entry based on Outliner order, beginning with 0. |
| **Treat as Range** | When enabled, the value of the Index property is treated as a range from 0 to the value. |
| **Invert Visibility** | When enabled, it reverses the functioning of the Visibility modifier, hiding the actors instead of showing them. |
| Skip when Hidden | When enabled, the children of any hidden actors are skipped by the Visibility modifier. |

### Masking

You can apply Masks to your shapes using a combination of two modifiers: **Mask Layer (Input)** and **Masked Layer (Output)**. The former is how you create a mask to apply, and the latter is how you apply the mask you created.

You use the Mask Layer (Input) modifier to establish the shape you want to use as a mask. In this example, we use a simple ellipse from the Motion Design shape palette.

This modifier can only mask shapes that have either a Translucent or Masked material type.

#### Mask Set Up

To set up a masking example, proceed as follows:

* Double-click the **ellipse** in the shape palette to place it at the center of your canvas.
* Shift the ellipse to the left of what you are trying to mask.
* Add the **Mask Layer (Input)** modifier from your palette, as shown in the image below.

[![Select Mask Layer (Input) modifier](https://dev.epicgames.com/community/api/documentation/image/fd7a1783-de5e-4e28-9737-d20eb3d78a60?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fd7a1783-de5e-4e28-9737-d20eb3d78a60?resizing_type=fit)

The Mask Layer (Input) and Masked Layer (Output) modifiers share properties you can use to define your mask:

[![Shared mask properties](https://dev.epicgames.com/community/api/documentation/image/9be5d942-b7fe-4219-a2f7-0c57a6439ebc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9be5d942-b7fe-4219-a2f7-0c57a6439ebc?resizing_type=fit)

#### Visualize Mask

Clicking the **Visualize Mask** button shows you a new window that displays your mask in isolation, helping you better understand the mask and how it will look in your level. The new window provides a summary of all the pertinent information about your mask.

[![Visualize mask](https://dev.epicgames.com/community/api/documentation/image/a19da9a4-2b54-468b-94e3-92fa112af71a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a19da9a4-2b54-468b-94e3-92fa112af71a?resizing_type=fit)

#### Write Operation (Add and Subtract)

You can use the Write Operation property to determine whether your masks Add or Subtract from other masks. You can use as many masks as you need to achieve the desired effect.

#### Inverted

You can enable the **Inverted** property to reverse the function of your mask. Visible sections will become invisible, and vice versa.

#### Channel Properties

You can assign your Mask to a channel using the **Channel** property. This is useful when you have several masks in your level and need for them to only interact with specific actors that have different mask assignments.

When nesting your masks, you can enable the **Use Parent Channel** property to cause nested child masks in the Motion Design Outliner to use the same channel as their parent mask, but this disables manually assigning channels yourself using the Channel property.

#### Apply Blur and Apply Feather

You can also blur and feather your mask using the Apply Blur and Apply Feather properties:

[![Mask Apply Blue and Apply Feather](https://dev.epicgames.com/community/api/documentation/image/d91124fa-c50b-454e-a75d-8a88304682d1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d91124fa-c50b-454e-a75d-8a88304682d1?resizing_type=fit)

##### Blur Strength

When you enable Apply Blur, you can use the **Blur Strength** property to control how much blur is applied.

##### Outer Feather Radius and Inner Feather Radius

When you enable Apply Feather, you can use the **Outer Feather Radius** and **Inner Feather Radius** properties to control the size of the effect.

#### Applying your Mask

Now that you have a shape dedicated to act as the Mask Layer (Input), you need to select some actors to mask using the Masked Layer (Output) modifier. You can do this on individual actors or on a null actor acting as a parent. When you apply the Masked Layer (Output) modifier to your actors, the mask(s) defined by your Mask Layer (Input) modifiers with the same channel are automatically applied.

| Mask Modifier Properties | Description |
| --- | --- |
| **Write Operation** | Determines whether masks add or subtract from other masks. Options are:   * Add * Subtract |
| **Use Parent Channel** | When enabled, nested masks use the channel of their parent. |
| **Channel** | Defines the channel used for the associated mask. |
| **Inverted** | Inverts mask visibility, so hidden areas are visible, and visible areas are hidden. |
| **Apply Blur** | Enable to apply a blur effect. |
| **Blur Strength** | Determines the strength of the blur effect. The default value is 16. |
| **Apply Feather** | Enable to apply a feather effect. |
| **Outer Feather Radius** | Determines the outer radius of the feather effect. The default value is 16. |
| **Inner Feather Radius** | Determines the inner radius of the feather effect. The default value is 16. |

## Transition Logic

You can use the **Sub Layer** modifier to identify the groups in your level to associate with a specific Transition Logic Sub Layer.

[![Transition Logic Sub Layer modifier](https://dev.epicgames.com/community/api/documentation/image/f54dbd16-a809-49df-80d1-b1f10e712396?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f54dbd16-a809-49df-80d1-b1f10e712396?resizing_type=fit)

### Sub Layer

After adding a Sub Layer modifier to your actor, you can select animations for the **Change In** and **Change Out** properties. Your selection options populate based on the animations you create and add to [Sequencer](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematics-and-movie-making-in-unreal-engine).

[![Sub Layer selection options](https://dev.epicgames.com/community/api/documentation/image/8a1c22c6-7d0f-40b4-a8ef-11d48589c5f2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8a1c22c6-7d0f-40b4-a8ef-11d48589c5f2?resizing_type=fit)

To use the Transition Logic Sub Layer modifier, you must first create animations in Sequencer. The sequences in the previous image's modifier dropdown list match those in the image below:

[![Sequencer animations for Sub Layer example](https://dev.epicgames.com/community/api/documentation/image/bd2c2901-faa4-48a5-a964-00fede932910?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bd2c2901-faa4-48a5-a964-00fede932910?resizing_type=fit)

#### Change In and Change Out

The **Change In** and **Change Out** properties function similarly. Change In determines the animation used to transition to your modified actor, and Change Out determines the animation used to transition away from your modified actor.

| Sub Layer Properties | Description |
| --- | --- |
| **Change In** | Determines the animation used to transition to your modified actor. |
| **Change Out** | Determines the animation used to transition away from your modified actor. |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Adding Modifiers](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#addingmodifiers)
* [Filtering Modifiers](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#filteringmodifiers)
* [Layout](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#layout)
* [Align Between](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#alignbetween)
* [Reference Actors Array](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#referenceactorsarray)
* [Actor Weak](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#actorweak)
* [Weight](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#weight)
* [Enabled](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#enabled)
* [Auto Follow](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#autofollow)
* [Reference Container](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#referencecontainer)
* [Reference Actor](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#referenceactor)
* [Skip Hidden](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#skiphidden)
* [Followed Axis](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#followedaxis)
* [Offset Axis](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#offsetaxis)
* [Followed Alignment and Local Alignment](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#followedalignmentandlocalalignment)
* [Start Padding](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#startpadding)
* [End Padding](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#endpadding)
* [Padding Progress](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#paddingprogress)
* [Grid Arrange](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#gridarrange)
* [Count](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#count)
* [Spread](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#spread)
* [Start Corner](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#startcorner)
* [Start Direction](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#startdirection)
* [Justify](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#justify)
* [Alignment Properties](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#alignmentproperties)
* [Anchor Properties](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#anchorproperties)
* [Look At](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#lookat)
* [Reference Container](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#referencecontainer-2)
* [Reference Actor](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#referenceactor-2)
* [Skip Hidden](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#skiphidden-2)
* [Axis Properties](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#axisproperties)
* [Radial Arrange](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#radialarrange)
* [Count](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#count-2)
* [Rings](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#rings)
* [Inner Radius and Outer Radius](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#innerradiusandouterradius)
* [Start Angle and End Angle](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#startangleandendangle)
* [Start from Outer Radius](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#startfromouterradius)
* [Orient Properties](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#orientproperties)
* [Spline Path](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#splinepath)
* [Spline Actor Weak](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#splineactorweak)
* [Sample Mode](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#samplemode)
* [Context Slider](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#contextslider)
* [Orient](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#orient)
* [Base Orientation](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#baseorientation)
* [Scale](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#scale)
* [Geometry](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#geometry)
* [Auto Size](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#autosize)
* [Reference Container](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#referencecontainer-3)
* [Reference Actor](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#referenceactor-3)
* [Padding Vertical](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#paddingvertical)
* [Padding Horizontal](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#paddinghorizontal)
* [Fit Mode](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#fitmode)
* [Include Children](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#includechildren)
* [Bend](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#bend)
* [Bend Position and Bend Rotation](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#bendpositionandbendrotation)
* [Angle](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#angle)
* [Extent](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#extent)
* [Symmetric Extents](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#symmetricextents)
* [Bidirectional](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#bidirectional)
* [Bevel](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#bevel)
* [Inset](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#inset)
* [Iterations](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#iterations)
* [Roundness](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#roundness)
* [Boolean](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#boolean)
* [Mode](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#mode)
* [Target](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#target)
* [Subtract](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#subtract)
* [Intersect](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#intersect)
* [Union](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#union)
* [Channel](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#channel)
* [Extrude](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#extrude)
* [Extrude Depth](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#extrudedepth)
* [Close Back](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#closeback)
* [Extrude Mode](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#extrudemode)
* [Mirror](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#mirror)
* [Mirror Frame Position and Mirror Frame Rotation](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#mirrorframepositionandmirrorframerotation)
* [Apply Plane Cut](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#applyplanecut)
* [Flip Cut Side](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#flipcutside)
* [Normal](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#normal)
* [Outline](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#outline)
* [Mode](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#mode-2)
* [Distance](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#distance)
* [Remove Inside](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#removeinside)
* [Pattern](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#pattern)
* [Line](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#line)
* [Grid](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#grid)
* [Circle](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#circle)
* [Plane Cut](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#planecut)
* [Plane Origin and Plane Rotation](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#planeoriginandplanerotation)
* [Invert Cut](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#invertcut)
* [Fill Holes](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#fillholes)
* [Use Preview](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#usepreview)
* [Size to Texture](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#sizetotexture)
* [Size to Texture](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#sizetotexture-2)
* [Texture](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#texture)
* [Rule](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#rule)
* [Spline Sweep](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#splinesweep)
* [Spline Actor Weak](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#splineactorweak-2)
* [Sample Mode](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#samplemode-2)
* [Sample Distance](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#sampledistance)
* [Steps](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#steps)
* [Progress Properties](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#progressproperties)
* [Progress Offset](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#progressoffset)
* [Progress Start](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#progressstart)
* [Progress End](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#progressend)
* [Scale Start and Scale End](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#scalestartandscaleend)
* [Capped](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#capped)
* [Looped](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#looped)
* [Subdivide](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#subdivide)
* [Cuts](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#cuts)
* [Type](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#type)
* [Taper](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#taper)
* [Amount](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#amount)
* [Extent](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#extent-2)
* [Interpolation Type](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#interpolationtype)
* [Reference Frame](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#referenceframe)
* [Dynamic Mesh Converter](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#dynamicmeshconverter)
* [SourceActor](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#sourceactor)
* [Component Type](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#componenttype)
* [Filter Actor Mode](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#filteractormode)
* [Include Attached Actors](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#includeattachedactors)
* [Hide Converted Mesh](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#hideconvertedmesh)
* [Update Interval](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#updateinterval)
* [Rendering](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#rendering)
* [Material Parameter](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#materialparameter)
* [Parameter Properties](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#parameterproperties)
* [Update Children](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#updatechildren)
* [Global Opacity](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#globalopacity)
* [Update Children](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#updatechildren-2)
* [Translucent Priority](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#translucentpriority)
* [Sort Mode](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#sortmode)
* [Outliner Top First and Outliner Bottom First](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#outlinertopfirstandoutlinerbottomfirst)
* [Camera Distance](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#cameradistance)
* [Camera Actor](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#cameraactor)
* [Manual](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#manual)
* [Sort Priority Offset](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#sortpriorityoffset)
* [Sort Priority Step](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#sortprioritystep)
* [Include Children](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#includechildren-2)
* [Visibility](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#visibility)
* [Index](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#index)
* [Treat as Range](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#treatasrange)
* [Invert Visibility](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#invertvisibility)
* [Skip when Hidden](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#skipwhenhidden)
* [Masking](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#masking)
* [Mask Set Up](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#masksetup)
* [Visualize Mask](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#visualizemask)
* [Write Operation (Add and Subtract)](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#writeoperation(addandsubtract))
* [Inverted](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#inverted)
* [Channel Properties](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#channelproperties)
* [Apply Blur and Apply Feather](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#applyblurandapplyfeather)
* [Blur Strength](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#blurstrength)
* [Outer Feather Radius and Inner Feather Radius](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#outerfeatherradiusandinnerfeatherradius)
* [Applying your Mask](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#applyingyourmask)
* [Transition Logic](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#transition-logic)
* [Sub Layer](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#sublayer)
* [Change In and Change Out](/documentation/en-us/unreal-engine/modifiers-in-unreal-engine?application_version=5.7#changeinandchangeout)
