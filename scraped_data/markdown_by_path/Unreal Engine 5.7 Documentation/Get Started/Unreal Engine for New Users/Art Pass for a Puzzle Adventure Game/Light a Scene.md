<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-02-light-a-scene?application_version=5.7 -->

# Light a Scene

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
5. [Get Started](/documentation/en-us/unreal-engine/get-started "Get Started")
6. [Unreal Engine for New Users](/documentation/en-us/unreal-engine/unreal-engine-for-new-users "Unreal Engine for New Users")
7. [Art Pass for a Puzzle Adventure Game](/documentation/en-us/unreal-engine/art-pass-for-a-puzzle-adventure-game "Art Pass for a Puzzle Adventure Game")
8. Light a Scene

# Light a Scene

Learn to light your level and set the mood with Spot Lights, Point Lights, and Rect Lights.

![Light a Scene](https://dev.epicgames.com/community/api/documentation/image/9ea68835-5a28-4762-94db-c5adda01c17a?resizing_type=fill&width=1920&height=335)

 On this page

Unreal Engine’s lighting system simulates how light interacts with objects in the scene. These can be materials applied to surfaces, shadowing of geometry, reflections, atmosphere and clouds, fog, and much more. All of these elements combine to create realistic and stylized visuals for your games to define mood, readability, and visual quality.

In this guide, you’ll start by looking at the following:

* Types of light actors available to choose from.
* How to place and use them in your scene.
* Common properties of lights.

## Before You Begin

Make sure you understand these topics covered in the [Unreal Engine for New Users](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-for-new-users) documentation:

* Unreal Editor basics, including transforming actors and using viewports.
* Adding and editing Blueprint components.

You’ll work with the following assets in the [sample project file](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-01-project-setup-and-content-import):

* `BP_TrapSpikes` Blueprint

## Light Types and Behaviors

Unreal Engine includes five types of lights you can use to light and shadow your scenes. With a range of large to small light sources, you can create a variety of looks that replicate real-world lighting.

Placeable light actors you can use to light the scene can be broken up into two categories:

**Environment Lighting** includes scene-wide, natural light sources that establish the overall mood, time of day, and illumination of the level.

* **Directional Lights** are primarily outdoor lights that appear to cast light from extreme, or near infinite, distances. This light is most often used as a sun or moon.
* **Sky Lights** capture and apply ambient lighting to the scene, helping darkened spaces look more naturally lit in an efficient way. This light captures the environment background and applies it to the level geometry.

**Localized Lighting** includes targeted light sources that represent actual objects in the world, often placed with the intention to guide the player’s eye or reinforce realism.

* **Point Lights** are omnidirectional lights that emit light in all directions from a single point, similar to a light bulb.
* **Spot Lights** are direction-limited lights that emit light from a single point in a direction limited by a cone around the light source. These lights function similarly to a flashlight.
* **Rect Lights** (also called Area Lights) emit light from a rectangular surface in a direction. They also have properties that let you adjust virtual shutters on all sides of the light, softening or sharpening the shape of the light being cast onto surfaces. These lights are generally used for rectangular window or ceiling lights, but can be used to provide some soft bounce light for large areas.

Common light actor adjustments include light intensity, color, light-source size, and temperature (warm or cool light). Additionally, each light type has its own properties specific to its function. For example, you can control the cone angle of a Spot Light or the size and angle of a Rect Light.

With **Lumen Global Illumination**, you can use emissive materials as another type of light source, where supported.

## Lighting for Gameplay

Lighting your scene goes far beyond allowing the player to see — you can use lights to communicate with the player. Adding light to an area of interest or pathway guides the player in that direction by creating contrast and visibility. Making an item pickup glow tells the player it’s important and worth inspecting. You could even create a language in your game with lighting; for example, objects lit up with a green light could always signal a health pickup, while doorways lit in orange could always signal an exit.

Lights also communicate mood and storytelling to the player. Adjusting the intensity of a light, its color, its effect on fog, and volumetric shadowing (beams of light) can change the mood of a space from calm to inspiring to scary without changing any scene geometry.

## Set Up World Lighting

First, adjust the environmental lighting in your level so the localized lighting you’ll add is visible.

To hide blocking volumes in the level editor while you’re working, click the eye button (**Show Flags**) in the viewport toolbar, go to **Volumes**, and disable **Blocking**.

To darken the level to prepare it for localized lighting, follow these steps:

1. Add a Post Process Volume:

   1. Use the **Create** dropdown menu to add a **Post Process Volume** to the scene.
   2. In its **Details** panel, in the **Post Process Volume Settings** category, enable Infinite **Extent (Unbound)**.
   3. In the **Lens > Exposure** category, set the **Min EV100** and **Max EV100** to `1.0`.
   4. Optional: Move the volume out of the way so you don’t accidentally select it while working with other level objects. This volume applies to the entire level, so it doesn’t matter where you place it.
2. Adjust the Directional Light:

   1. In the **Outliner**, search for and select the **DirectionalLight**.

      To find this actor, use the Outliner search box. Or, to view all environmental lighting actors in the level, click Settings (gear icon) in the top-right corner of the Outliner, select Collapse All, and expand the Level folder.
   2. Lower the **Intensity** to `0.75` to make it easier to work with other lighting effects in the scene. Intensity sets how much light should be emitted.
3. Enable Volumetric Fog:

   1. In the **Outliner**, search for and select the **ExponentialHeightFog**.
   2. In the **Details** panel under the **Volumetric Fog** category, enable **Volumetric Fog**. This doesn’t change the look of your scene now, but sets up the environment so you can scatter light through the air, creating beams of light or a soft atmospheric glow.

A Post Process Volume adjusts how the scene is rendered and appears on camera after all other lighting and materials are drawn. By setting a minimum and maximum exposure threshold that is the same value, you stabilize the lighting and prevent the engine’s auto-exposure adjustments from brightening and darkening the scene within this range.

You’ll learn more about volumetric fog, environmental lighting, and post-processing effects in later parts of this tutorial series.

[![Start-room-no-lighting](https://dev.epicgames.com/community/api/documentation/image/fbae4337-515a-44c7-9db3-47adfdb6f0bb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fbae4337-515a-44c7-9db3-47adfdb6f0bb?resizing_type=fit)

Next, you’re going to add three types of lights to the Starting Room to explore how you can use them to achieve different results. While these three examples with three different lights and behaviors are something you can follow, you are not limited to only using these three lights in this scene. You can place multiple lights in this room or others as you see fit.

Throughout this tutorial, you can follow along or adjust each light’s settings to achieve the desired look for your project.

## Add a Spot Light Over the Keys

Spot Lights emit light from a single point and shine directional light in a cone shape. Here’s a demonstration of changing a Spot Light’s properties:

To guide the player’s attention to the key and reinforce its importance, add a Spot Light so it casts down on the key in the Start Room.

To learn more about a light’s properties, hover over the property name in the **Details** panel. A tooltip appears with information about that property.

To add a Spot Light to your level, follow these steps:

1. In the **Level Editor** toolbar, use the **Create > Lights** menu to add a **Spot Light** to the scene.
2. Place this above the column where the first key is located. Try to center it above the pillar and raise it directly above.

   You can use the **Top Orthographic** view to help position your objects, or select the **BP\_Key** blueprint and copy its **Location** into the **Light’s Location** in the **Details** panel.

![Placing-a-light-above-a-column](https://dev.epicgames.com/community/api/documentation/image/9b3623de-1e01-4836-bccd-306f3196dcda?resizing_type=fit)

To configure the light’s settings, follow these steps:

1. With the Spot Light selected, use the **Details** panel to change the following settings:

   1. **Intensity**: 100
   2. **Attenuation Radius**: 500

      This controls how far the light reaches. Adjust this to be large enough that it reaches the top of the pillar or a little beyond where the key sits, but not large enough that it’s reaching the floor below the pillar. Raise or lower the light to adjust how the light hits the key.
   3. **Outer Cone**: 20
   4. **Source Radius**: 50

      This sets the size of the light source itself. It changes how soft or sharp the light and shadows cast from it appear. Increasing the size of the light source causes more scattering of light around the key, adding softness to the key’s shadow. Distance between the object above a surface and where the shadow is also plays a role in how soft the shadow will appear.

      [![Hard-shadow-vs-soft-shadow](https://dev.epicgames.com/community/api/documentation/image/3df49405-dc1b-4d48-a4da-a7050c855afb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3df49405-dc1b-4d48-a4da-a7050c855afb?resizing_type=fit)
   5. **Volumetric Scattering Intensity**: 15 -50

      Set this value to something you’re happy with.

      [![](https://dev.epicgames.com/community/api/documentation/image/792ff83e-8001-4af5-9ab5-5b876bfb97cd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/792ff83e-8001-4af5-9ab5-5b876bfb97cd?resizing_type=fit)

      Examples of volume scattering intensity values of 0, 15, 30, and 50.

## Add a Point Light to the Spike Trap Blueprint

Point Lights emit light in all directions. Here’s a demonstration of changing a Point Light’s properties:

Use a point light to add a fiery glow effect to your spike traps. By adding it to the Blueprint, the light is applied to every spike trap actor in your level automatically.

To add a Point Light to your Spike Trap Blueprint, follow these steps:

1. In the Start Room, select one of the **BP\_TrapSpikes** instances in the pit. In the **Outliner**, select **Edit BP\_TrapSpikes** to open the `BP_TrapSpikes` Blueprint in the Blueprint Editor.

   [![Select-a-trap-spike](https://dev.epicgames.com/community/api/documentation/image/c6bc8466-64d1-4ae1-ae19-2902ed0c2fac?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c6bc8466-64d1-4ae1-ae19-2902ed0c2fac?resizing_type=fit)
2. Select the **Viewport** tab to view the Blueprint’s components.

   [![BP-trap-spikes-viewport-and-components-panel](https://dev.epicgames.com/community/api/documentation/image/2d5c0ee0-7e9c-45c9-a5bc-32dedbb83177?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2d5c0ee0-7e9c-45c9-a5bc-32dedbb83177?resizing_type=fit)
3. In the **Components** panel, click **Add** and select a **Point Light** from the list. This adds a point light to the center point (or world 0 position) of the viewport.
4. With the Point Light selected, move the light up (Z-axis) 30 units so it’s near the top of the spike meshes in the viewport.

   [![Point-light-over-the-trap-spikes](https://dev.epicgames.com/community/api/documentation/image/f47c8ede-33ea-4443-bf55-44c18ca1d2e9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f47c8ede-33ea-4443-bf55-44c18ca1d2e9?resizing_type=fit)

Go back to the Level Editor to see the effect in the scene:

[![Check-the-effect-in-the-level-editor](https://dev.epicgames.com/community/api/documentation/image/493fb5f3-789d-4025-8aa9-f63b626adc23?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/493fb5f3-789d-4025-8aa9-f63b626adc23?resizing_type=fit)

Now, edit the light’s properties to change the mood and create a distinctive look.

To adjust the spike trap’s glow, follow these steps:

1. In the `BP_SpikeTrap`, with the **PointLight** component selected, change the following properties in the **Details** panel:

   1. **Intensity**:  40
   2. **Attenuation Radius**: 300
   3. **Source Radius**: 5
   4. **Use Temperature**: Enabled
   5. **Temperature**: 1700

      This changes the color of the light (warm or cool) based on a Kelvin color temperature scale.
   6. **Volumetric Scattering Intensity**: 40

      This property interacts with the Volumetric Fog you enabled earlier.

      [![Trap-spikes-with-a-more-intense-glow](https://dev.epicgames.com/community/api/documentation/image/01b85d81-521b-4008-a311-55cc6941ef93?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/01b85d81-521b-4008-a311-55cc6941ef93?resizing_type=fit)
   7. **Intensity Units**: Lumens - Luminous Flux, Normalized
2. To make the spike pit look more sinister, select all **Cone** mesh components, click the Scale gizmo, and scale the spikes up on the Z (blue) axis. The sharper spikes produce more contextual shadows that can relay danger or harm in this area.
3. Select the **InvisFloor** mesh component and move it up to match the height of the spikes. This invisible platform prevents the player’s mesh from getting stuck between the spikes.

   To make the floor visible in the viewport, in the **Details** panel, go to the **Rendering** section and enable **Visible**. Remember to disable this when you’re done editing the blueprint.
4. Select the **TrapTrigger** component and adjust its size and position to extend beyond the top of your spikes. This ensures the player triggers the spike’s damage effect when they land on the trap.

   [![Configure-the-trap-trigger](https://dev.epicgames.com/community/api/documentation/image/29fcbd98-a79d-47f2-96c2-81120f61f4f8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/29fcbd98-a79d-47f2-96c2-81120f61f4f8?resizing_type=fit)
5. **Compile** and **Save** the blueprint.

Play your game to test the new spikes. Ensure you have successfully done the following:

* Positioned the invisible floor so that the player doesn't get stuck in the spikes.
* Sized the TrapTrigger collision box so the player still takes damage when standing on the trap.

## Add Spot Lights Over Doorways

Next, illuminate the colored doorways. You’ll create an interesting lighting effect over the door with some volumetric fog combined with the properties you’ve already used in your Spot and Point Lights.

To light the doorways, follow these steps:

1. For the yellow doorway, add a **Spot Light** and move it above the doorway or just under the overhang so it looks like a spotlight attached to the doorframe. Rotate it so it points a couple of meters away from the door.

   [![Add-a-spot-light-to-the-yellow-door](https://dev.epicgames.com/community/api/documentation/image/ec3bffb2-1bd7-44ea-b69b-98d9cabc60aa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ec3bffb2-1bd7-44ea-b69b-98d9cabc60aa?resizing_type=fit)
2. With the Spot Light selected, hold **Alt** and drag the light on the X and Y axis (red and green handles) to duplicate it. Move the copy in front of the blue door and then duplicate again to move a copy in front of the red door.

   [![Duplicate-the-light-for-each-door](https://dev.epicgames.com/community/api/documentation/image/23dd2462-46b2-42b9-a893-96f0df1f2853?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/23dd2462-46b2-42b9-a893-96f0df1f2853?resizing_type=fit)

   [![Final-image-with-all-three-doors-lit](https://dev.epicgames.com/community/api/documentation/image/1e910daa-9f08-4325-a494-43687dacfc82?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1e910daa-9f08-4325-a494-43687dacfc82?resizing_type=fit)
3. In the **Details** panel, set the following properties on the light:

   1. **Source Radius**: 5
   2. **Volumetric Scattering Intensity**: 50

      This property interacts with the Volumetric Fog you enabled earlier.

      Your light should look like this:

      [![Finished-light-on-yellow-door](https://dev.epicgames.com/community/api/documentation/image/021ccae7-91b4-4cf1-ad7b-d54eed92a966?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/021ccae7-91b4-4cf1-ad7b-d54eed92a966?resizing_type=fit)
   3. **Intensity**: 100
4. Select the light in front of the yellow door. In the **Details** panel, click the **Light Color** color swatch. In the **Color Picker** window, change the color to yellow. To use the same color as the sample level, enter `FFFF89FF` into the **Hex sRGB** property. Click **OK** to accept the color changes.

   [![Color-wheel-for-door-lights](https://dev.epicgames.com/community/api/documentation/image/36ec962d-afff-4f1e-9791-a1024ca76e24?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/36ec962d-afff-4f1e-9791-a1024ca76e24?resizing_type=fit)
5. Change the **Light Color** property of the two other Spot Lights to match their doors. To match the sample level, you can use the following **Hex sRGB** values:

   1. Red door light: **FF8989FF**
   2. Blue door light: **8989FFFF**

Now your scene should look like this with colored lights above each doorway, indicating which key will unlock them.

[![Door-light-color-matches-the-door-color](https://dev.epicgames.com/community/api/documentation/image/1b9fbb79-05ff-4c19-937b-ab5240a5d927?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1b9fbb79-05ff-4c19-937b-ab5240a5d927?resizing_type=fit)

## Add a Rect Light to a Window

Rect Lights emit directional light from a rectangular surface. Here’s a demonstration of changing a Rect Light’s properties:

To create a nice effect as well as guide the player’s attention to the platforms they can jump up to reach the first key, add a Rect Light to the nearby window.

To make light stream in through a window, follow these steps:

1. In the Level Editor toolbar, use the **Create > Lights** menu to add a **Rect Light** to the scene.

   The light’s yellow rectangle wireframe represents the light’s dimensions and its **Barn Door Angle** and **Barn Door Length**, which control how the Rect Light’s beam is shaped and projected.
2. Place the Rect Light outside a window. Rotate it and place it so it casts light through the opening in the wall, adding light and shadow in the room.
3. In the **Details** panel, change the **Intensity** to `200`.
4. Change the **Source Width** and **Source Height** to roughly match the size of the window. In the sample level, the Start Room’s Rect Light has a width of `400` and height of `200`.

   [![](https://dev.epicgames.com/community/api/documentation/image/4de90c8f-ea03-4841-99ab-d21b3f51723d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4de90c8f-ea03-4841-99ab-d21b3f51723d?resizing_type=fit)
5. Adjust the light’s position until you’re happy with the angle and intensity of light and shadow it creates in the room.

You should have something that looks similar to this now:

[![Finished-Rect-Light-streaming-into-room](https://dev.epicgames.com/community/api/documentation/image/45e4d3f6-2535-410f-ab95-f51095f25eaf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/45e4d3f6-2535-410f-ab95-f51095f25eaf?resizing_type=fit)

With Rect Lights, you can assign a **Source Texture** to color the light and add a distinctive look to the scene. The closer the light gets to a surface, the less diffuse the assigned source texture becomes.

![Gif-showing-source-texture-at-different-distances](https://dev.epicgames.com/community/api/documentation/image/eddd0995-d012-471b-b1eb-92f5779b9f6c?resizing_type=fit)

To add a source texture to a Rect Light, follow these steps:

1. Select the **Rect Light**. In the **Details** panel, in the **Light** category, go to the **Source Texture** asset assignment slot.
2. Click the dropdown menu and search for and select the **ColorGradingWheelGradient** texture.

   [![Color-grading-wheel-gradient](https://dev.epicgames.com/community/api/documentation/image/a8d940b7-6252-45df-908f-a77010b3f93f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a8d940b7-6252-45df-908f-a77010b3f93f?resizing_type=fit)

   This texture is included with Engine Content and should automatically appear in the dropdown list.

Multicolored light now casts into the room:

[![Multi-colored-light-via-the-wheel-gradient](https://dev.epicgames.com/community/api/documentation/image/1eb1c762-5c44-429d-aefb-c4324559ead3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1eb1c762-5c44-429d-aefb-c4324559ead3?resizing_type=fit)

## Use an Emissive Material as a Light Source

Last, create a material that emits a light using **Lumen Global Illumination** system. You can use your own choice of color for this material.

[![Emissive-material](https://dev.epicgames.com/community/api/documentation/image/e29bc6d0-d020-4fe7-bb5f-497c83dba419?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e29bc6d0-d020-4fe7-bb5f-497c83dba419?resizing_type=fit)

To create an emissive material, follow these steps:

1. In the Content Browser, go to your Content > AdventureGame > Artist folder.
2. In the Artist folder, create another new folder named `Materials`.
3. In the **Content Browser**, in the **AdventureGame > Artist > Materials** folder, right-click an empty area in the folder or click the **Add** button, and select **Material**.

   This tutorial assumes you’re using the asset directory structure used in the tutorial sample level and [Design a Puzzle Adventure](https://dev.epicgames.com/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine).
4. Name the material asset `M_Emissive` and double-click it to open it.

   We recommend naming assets with prefixes to help identify assets at a glance. For example, the tutorial’s sample project uses `M_` with material names as a naming convention.
5. In the **Material Graph**, on the **M\_Emissive** material node, click the color swatch next to the **Emissive Color** input and set a color. To follow along with the sample level, change
   **Hex sRGB** to `00FF0000`.

   [![Emissive-color-gradient-wheel](https://dev.epicgames.com/community/api/documentation/image/14ce25df-22e3-4eb1-be99-cf536518f0cf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/14ce25df-22e3-4eb1-be99-cf536518f0cf?resizing_type=fit)
6. Click **OK** to accept the new color and close the **Color Picker** window.
7. In the Material, click **Apply** and **Save**.

   [![](https://dev.epicgames.com/community/api/documentation/image/31393c77-fd92-47d0-99d0-33adc888a18a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/31393c77-fd92-47d0-99d0-33adc888a18a?resizing_type=fit)

Next, you’ll add some geometry to the scene and apply the material to this geometry.

To use the emissive material in the level, follow these steps:

1. From the **Content Browser**, in **Content > LevelPrototyping > Meshes**, add two `SM_Cylinder` meshes to the room you’ve been working in. Resize and position them to be thin columns in the remaining dark corners of the room.  If you’re using the sample level, duplicate two columns next to the yellow and blue doors and move them to the front corners of the room.

   [![Duplicating-the-emissive-columns](https://dev.epicgames.com/community/api/documentation/image/0c96a9a6-199b-4b92-839a-77f2bafc5b8e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0c96a9a6-199b-4b92-839a-77f2bafc5b8e?resizing_type=fit)
2. Open the **Content Browser** and drag `M_Emissive` onto the two columns to apply that material to the mesh shapes. The changes may take a few seconds to load.

To use a material as a light source, you must have Lumen enabled for the project. Emissive materials as light sources also produce more ghosting effects and don’t work well with small, bright light sources. We recommend using emissive materials subtly, keeping these limitations in mind.

Your room should look similar to this:

[![Finished-start-room](https://dev.epicgames.com/community/api/documentation/image/68f4883b-e6bb-4387-8756-0c3d45f9611c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/68f4883b-e6bb-4387-8756-0c3d45f9611c?resizing_type=fit)

## Next Up

In the next section, you’ll learn about working with materials in more detail, including how to use instancing to make flexible materials that can change color and brightness dynamically at runtime, giving you more power to make changes to the scene.

* [![Create Materials and Material Instances](https://dev.epicgames.com/community/api/documentation/image/8e452b45-4ccc-4be0-af67-f51041daf936?resizing_type=fit&width=640&height=640)

  Create Materials and Material Instances

  Use materials and material instances to surface a level.](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-03-create-materials-and-material-instances)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Before You Begin](/documentation/en-us/unreal-engine/artist-02-light-a-scene?application_version=5.7#beforeyoubegin)
* [Light Types and Behaviors](/documentation/en-us/unreal-engine/artist-02-light-a-scene?application_version=5.7#lighttypesandbehaviors)
* [Lighting for Gameplay](/documentation/en-us/unreal-engine/artist-02-light-a-scene?application_version=5.7#lightingforgameplay)
* [Set Up World Lighting](/documentation/en-us/unreal-engine/artist-02-light-a-scene?application_version=5.7#setupworldlighting)
* [Add a Spot Light Over the Keys](/documentation/en-us/unreal-engine/artist-02-light-a-scene?application_version=5.7#addaspotlightoverthekeys)
* [Add a Point Light to the Spike Trap Blueprint](/documentation/en-us/unreal-engine/artist-02-light-a-scene?application_version=5.7#addapointlighttothespiketrapblueprint)
* [Add Spot Lights Over Doorways](/documentation/en-us/unreal-engine/artist-02-light-a-scene?application_version=5.7#addspotlightsoverdoorways)
* [Add a Rect Light to a Window](/documentation/en-us/unreal-engine/artist-02-light-a-scene?application_version=5.7#addarectlighttoawindow)
* [Use an Emissive Material as a Light Source](/documentation/en-us/unreal-engine/artist-02-light-a-scene?application_version=5.7#useanemissivematerialasalightsource)
* [Next Up](/documentation/en-us/unreal-engine/artist-02-light-a-scene?application_version=5.7#nextup)

Related documents

[Design a Puzzle Adventure

![Design a Puzzle Adventure](https://dev.epicgames.com/community/api/documentation/image/a7b7ff2c-23d0-47a0-8a04-e569209942b0?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine)

[Code a First-Person Adventure Game

![Code a First-Person Adventure Game](https://dev.epicgames.com/community/api/documentation/image/ffc1a8f8-e7e5-42c0-b4ed-32ce6d3adbbc?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/code-a-firstperson-adventure-game-in-unreal-engine)

[Lighting the Environment

![Lighting the Environment](https://dev.epicgames.com/community/api/documentation/image/6ac87c9a-797e-4019-9f8b-d2267a504b71?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/lighting-the-environment-in-unreal-engine)

[Animate a Light

![Animate a Light](https://dev.epicgames.com/community/api/documentation/image/dc8aae74-67c8-4335-8c4b-2ffe445faad9?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/how-to-animate-lights-in-unreal-engine)

[Light Types and Their Mobility

![Light Types and Their Mobility](https://dev.epicgames.com/community/api/documentation/image/359e9f83-7bd2-4412-b87c-daa4e5b109d3?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/light-types-and-their-mobility-in-unreal-engine)
