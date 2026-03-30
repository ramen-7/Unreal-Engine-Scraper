<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/07-adjust-environment-lighting-features?application_version=5.7 -->

# Adjust Environment Lighting Features

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
8. Adjust Environment Lighting Features

# Adjust Environment Lighting Features

Learn to enhance your level's atmospheric elements by adding denser fog in low-lying areas and adding storm clouds in the sky.

![Adjust Environment Lighting Features](https://dev.epicgames.com/community/api/documentation/image/bed29c66-e098-4f93-9180-ace984c6d4d7?resizing_type=fill&width=1920&height=335)

 On this page

In this section, you’ll take a closer look at environmental lighting. In [Light a Scene](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-02-light-a-scene), you learned to adjust the lighting that’s applied across the entire level. Now, you’ll learn to deepen the atmospheric elements in targeted parts of your level by:

* Adding a second layer of fog in low-lying areas, boosting the realism and atmosphere in your level.
* Adjusting the Volumetric Cloud actor's material to create stormy clouds with lightning effects.

As you complete this tutorial, you can choose to follow along with the example property values or experiment with different values to achieve the look and feel you want in your level.

## Before You Begin

Make sure you understand these topics covered in previous sections of the [Art Pass for a Puzzle Adventure Game](https://dev.epicgames.com/documentation/en-us/unreal-engine/art-pass-for-a-puzzle-adventure-game) tutorial series:

* Unreal Editor basics, including transforming actors and using viewports.

  You’ll work with the following assets in the [sample project file](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-01-project-setup-and-content-import):

* ExponentialHeightFog actor
* VolumetricCloud actor

## Add Exponential Height Fog to Low-Lying Areas

Creating thinner and thicker areas of fog in your level enhances the richness and realism of those spaces, immersing the player in realistic environments.

To create this effect, you’ll use the Exponential Height Fog actor's Second Fog Data properties to add an additional layer of fog to the level. You can use these properties to customize the height (on the Z axis) and density of the secondary fog layer.

The combination of Exponential Height Fog layers creates a consistent amount of fog across the level for very far distances and a secondary layer of fog that can independently increase fog density in low-lying areas like the valley in the example below. You can see in the first image that there is a fog layer and then see how a second layer of dense fog covering the valley changes the scene.

![Exponential Height Fog: Single Fog Layer](https://dev.epicgames.com/community/api/documentation/image/f4c83ee1-b0c3-4b70-bfd3-3a19f63bbb07?resizing_type=fit&width=1920&height=1080)

![Exponential Height Fog: Added Second Fog Layer](https://dev.epicgames.com/community/api/documentation/image/99170a70-7879-420b-b4c0-e8b20502de65?resizing_type=fit&width=1920&height=1080)

Exponential Height Fog: Single Fog Layer

Exponential Height Fog: Added Second Fog Layer

### Add a Second Fog Layer

In the sample level, you’ll use the Exponential Height Fog actor to apply a denser layer of fog in the lower pit areas with traps in Room 1. The secondary fog layer also applies to any other low areas of the level, such as the spike pit in Start Room.

You could create this effect in several ways, such as with materials or local fog volumes, but for the scale of the sample level, you’ll use only the Exponential Height Fog.

To add a second layer of fog to low areas in your level, follow these steps:

1. In the **Outliner**, select the **Exponential Height Fog** actor.

   [![](https://dev.epicgames.com/community/api/documentation/image/24ee1f7e-72b9-4550-b70c-312e48ab67ad?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/24ee1f7e-72b9-4550-b70c-312e48ab67ad?resizing_type=fit)

   To find this actor, use the **Outliner** search box. Or, click **Settings** (gear icon) in the top-right corner of the **Outliner**, select **Collapse All**, and expand the **Level** folder.
2. In the **Details** panel, under **Exponential Height Fog Component > Second Fog Data**, change the following values:

   1. **Fog Density**: `0.3`
   2. **Fog Height Falloff**: `1.8`
   3. **Fog Height Offset**: `7500`

      The **Fog Height Falloff** is how quickly the fog fades as it moves upwards, and the **Fog Height Offset** is where the fog layer sits vertically in the world.

After adjusting the secondary fog properties, the pit should look similar to this:

[![](https://dev.epicgames.com/community/api/documentation/image/c3a16850-1f22-44ab-9685-a97d3f1219d5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c3a16850-1f22-44ab-9685-a97d3f1219d5?resizing_type=fit)

[![](https://dev.epicgames.com/community/api/documentation/image/98fb15c8-0eed-427e-9bbd-fcfc206f3201?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/98fb15c8-0eed-427e-9bbd-fcfc206f3201?resizing_type=fit)

From a higher viewpoint, here’s a demonstration of the level before and after:

[![](https://dev.epicgames.com/community/api/documentation/image/9b881db8-df6b-4914-96ad-ca4597655fdd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9b881db8-df6b-4914-96ad-ca4597655fdd?resizing_type=fit)

### Add Colored Light to the Fog

The secondary volumetric fog adds some atmosphere to Room 1’s pit, but is visually flat. By adding additional lighting that interacts with the fog, you can create a more dramatic and ominous feeling in this area of the room.

In this section, you’ll add a non-shadow-casting light to boost the glow within the pit and make the fog more prominent in a darker environment.

[![](https://dev.epicgames.com/community/api/documentation/image/2dc96f1b-e544-4b21-a209-54bb69f184f2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2dc96f1b-e544-4b21-a209-54bb69f184f2?resizing_type=fit)

To light and color the fog, follow these steps:

1. In the main toolbar, open the **Create** menu and select **Lights > Point Light**.
2. Drag and place the light within or just below the pillar in the middle of the room.

   [![](https://dev.epicgames.com/community/api/documentation/image/e110062f-9c98-44d3-ac8a-99b320f0f5cb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e110062f-9c98-44d3-ac8a-99b320f0f5cb?resizing_type=fit)

   The height you place the light at affects how visible it is as the player walks into the room. Find a placement that works best for the look and feel of your level.
3. With the **Point Light** selected, in the **Details** panel, change the following properties:

   |  |  |  |
   | --- | --- | --- |
   | **Property** | **Value** | **Notes** |
   | Intensity | 10 |  |
   | Light Color | HEX RGB = FF6E36FF (light orange) | If you use a different color, you may need to adjust the light Intensity depending on the color's wavelength (blues require a higher light intensity than reds and greens). |
   | Attenuation Radius | 1300 | This value makes the light illuminate all of Room 1. |
   | Cast Shadows | Off | The Point Light should act as a “fill” light to only light the fog and not cast shadows. |
   | Advanced > Use Inverse Squared Falloff | Off | Disable this property when you want to use a light to uniformly fill an area. Turning this off removes the bright, reflective spot near the center of the light source. |
   | Advanced > Light Falloff Exponent | 3.0 | Lowering the default value makes the light fill more of the area within the **Attenuation Radius**, but can make the light look less realistic (in real life, light sources can only cast light a certain distance). |
4. Optional: Adjust **Volumetric Scattering Intensity** to increase or decrease the amount of light contribution added to the volumetric fog. (The default value is 1.0.)

   [![](https://dev.epicgames.com/community/api/documentation/image/bb93fc7f-3197-4c20-96bf-da2fdc11bd5e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bb93fc7f-3197-4c20-96bf-da2fdc11bd5e?resizing_type=fit)

### Fix Volumetric Intensity of Spot Lights

In [Light a Scene](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-02-light-a-scene), you placed Spot Lights over the key and each door in the Start Room and increased the Volumetric Scattering Intensity of those lights. Increasing their volumetric intensity made the cones of light brighter and more defined without increasing the density of fog throughout the level.

[![](https://dev.epicgames.com/community/api/documentation/image/be245dc2-047d-4185-81ca-21ed92997eb1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/be245dc2-047d-4185-81ca-21ed92997eb1?resizing_type=fit)

If you return to the Start Room, you’ll see that the Spot Lights are now contributing too much light to the volumetric fog, making the cones of light too bright.

[![](https://dev.epicgames.com/community/api/documentation/image/0b19e9cd-60fb-42a8-a98e-5ae6958ad3bf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0b19e9cd-60fb-42a8-a98e-5ae6958ad3bf?resizing_type=fit)

To correct the Spot Lights in the Start Room and restore their softer look, follow these steps:

1. Use the **Viewport** or **Outliner** to select the four **Spot Light** actors.
2. In the **Details** panel, change the **Volumetric Intensity** from `50` to `4` (or other value as desired).

Using the suggested values above, the lights should look something like this:

[![](https://dev.epicgames.com/community/api/documentation/image/02562a71-6cbd-4475-9ad4-05b2af142ddb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/02562a71-6cbd-4475-9ad4-05b2af142ddb?resizing_type=fit)

To add fog to specific sections of a level instead, try using [Local Fog Volumes](https://dev.epicgames.com/documentation/en-us/unreal-engine/local-fog-volumes-in-unreal-engine).

## Create Stormy Clouds with the Volumetric Cloud Component

The sample level was created from the **Basic** level template which includes a set of lighting actors, including a Volumetric Cloud actor. This actor is controlled by its assigned Volumetric Cloud Material Instance. You can use this material to create different cloud formations and effects, including stormy clouds with lightning appearing behind the cloud layers.

In this section, you’ll create a copy of the existing Volumetric Cloud Material Instance and modify the copy to create a stormy cloud that matches the dark, atmospheric look of the level you’ve already created with environmental lighting and exponential height fog.

### Copy the Volumetric Cloud Material Instance

Because the Volumetric Cloud Material is contained in the Engine Content, make a copy of it within your own project first. This way, the original remains unchanged in the **Engine > Content** folder as a backup.

Always make a copy of assets in **Engine > Content** before working with them. Assets in this folder are shared across all of your Unreal Engine projects, so any changes to assets in this folder will affect your other projects and levels.

To create and use a copy of the Volumetric Cloud Material Instance, follow these steps:

1. In the **Outliner**, select the **Volumetric Cloud** actor.
2. In the **Details** panel, in the **Cloud Material** category, next to the **Material**, click the **Browse to Asset** button.

   [![](https://dev.epicgames.com/community/api/documentation/image/36c5b811-6dc2-4226-9d8b-74c6449804c2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/36c5b811-6dc2-4226-9d8b-74c6449804c2?resizing_type=fit)
3. In the **Content Browser**, drag `m_SimpleVolumetricCloud_Inst` to the **Content > AdventureGame > Artist > Materials** folder.
4. Select **Copy Here** to make a copy of the original file.
5. Go to the **AdventureGame > Artist > Materials** folder, and rename the material copy to `MI_MyVolumetricCloud`.
6. In the **Details** panel, use the **Material** asset slot to assign `MI_MyVolumetricCloud` to your level’s Volumetric Cloud actor.

   [![](https://dev.epicgames.com/community/api/documentation/image/3db156ba-214f-44e1-a06e-7bba626962c1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3db156ba-214f-44e1-a06e-7bba626962c1?resizing_type=fit)

### Customize the Volumetric Cloud

Now that you have your own Volumetric Cloud Material Instance applied to your level, you can use the parameters in the Material Instance to work on the storm clouds.

To create storm clouds in the Volumetric Cloud Material, follow these steps:

1. In the **Content Browser**, open `MI_MyVolumetricCloud`. The Material Instance’s parameters are divided into **Cloud Layout**, **Shape**, **Storm**, and **Multiscatter** groups.

   [![](https://dev.epicgames.com/community/api/documentation/image/b8ad05c4-6aea-4b74-9bb9-33abb18f49fa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b8ad05c4-6aea-4b74-9bb9-33abb18f49fa?resizing_type=fit)

   Work with the Material Instance undocked in its own window so you can observe how changing the parameter values affects the level in the viewport.
2. Expand the **02 - Storm** category, enable **StormClouds**, and set its value to a number between `0.3` and `0.5` to start. You can increase or decrease this value to adjust the amount of cloud coverage in the sky.

   In the viewport, position the camera where the player stands so you can test the clouds’ appearance from the player’s point of view.
3. Under **02-Storm**, enable **Storm\_LightningMasks** and expand its parameters.
4. Under **Storm\_LightningMasks**, adjust the **LightingMaskBias**to a value between `1` and `0` (for example, try `0.5` to start). As the value gets closer to 0, you’ll see the lightning become more visible behind the clouds.

   If you’re having trouble seeing the lightning effect in the viewport, ensure **Realtime Viewport** is enabled and move the camera to point a little above the horizon as the effect tends to appear lower in the sky.

   [![](https://dev.epicgames.com/community/api/documentation/image/f692206d-a69f-4317-b5b8-ab93af1a7f0b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f692206d-a69f-4317-b5b8-ab93af1a7f0b?resizing_type=fit)

These parameter values give you a starting point for creating storm-like clouds with lightning effects behind the clouds. You can match the material parameters to the values suggested in this tutorial, or experiment with different values to create the look you want in your level.

If you’d like to keep working on your storm clouds, try adjusting the following settings:

|  |  |  |
| --- | --- | --- |
| **Category** | **Parameter** | **Description** |
| 02 - Storm > Storm\_LightningAnim | All | These parameters change the lightning-flicker animation. Be conservative when changing these parameters, and remember the default values so you can revert if needed. |
| 02 - Storm > Storm\_LightningClouds | FillScatterIntensity | Increase or decrease this value to adjust the intensity of the lighting flashes in the clouds. |
| 02 - Storm > Storm\_LightningMasks | LightningMaskStrength | Lower values dim the lightning effect, making it less pronounced in the clouds. Use this in combination with the CloudTextureWeight for soft, rolling lightning effects in the clouds. |
| 02 - Storm > Storm\_LightningMasks | Cloud TextureWeight | Lower values reduce how much the lighting illuminates the clouds and makes the flashes more subdued. |

Here’s an example of the results you can expect after changing the Volumetric Cloud Material parameters:

For more examples and information on using the Volumetric Cloud Material to create various types of cloud formations, see [Volumetric Cloud Material](https://dev.epicgames.com/documentation/en-us/unreal-engine/volumetric-cloud-material-in-unreal-engine).

## Adjust Light Properties with Light Mixers

Unreal Engine has two editor panels where you can adjust scene light or atmospheric light properties in one convenient place.

In the **Light Mixer** panel, you can manage localized light sources in your level. This panel is like an **Outliner** that only shows actors that contain lights.

Open the **Light Mixer** from Unreal Editor’s main menu by selecting **Window > Light Mixer**.

In the sample level's **Light Mixer**, you can see it includes standalone light actors like Spot Lights, and the Jump Pad and Fire Trap actors since their blueprints contain lights.

[![](https://dev.epicgames.com/community/api/documentation/image/c2b784e0-e0dc-4936-af2f-a46f7a5c2293?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c2b784e0-e0dc-4936-af2f-a46f7a5c2293?resizing_type=fit)

In the **Environmental Light Mixer** window, you can create and edit the properties of your level's environment lighting components.

Open the **Environment Light Mixer** from the main menu by selecting **Window > Env. Light Mixer**.

[![](https://dev.epicgames.com/community/api/documentation/image/d1b7795c-41a0-48bb-999a-8bff790b3f97?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d1b7795c-41a0-48bb-999a-8bff790b3f97?resizing_type=fit)

To learn more about working with these editor windows, see [Light Mixer](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-light-mixer-in-unreal-engine) and [Environment Light Mixer](https://dev.epicgames.com/documentation/en-us/unreal-engine/environment-light-mixer-in-unreal-engine).

## Next Up

In the next section, you’ll start adding sound to your game. You’ll learn to create a Sound Cue and make the sample level’s fire traps play a looping sound effect.

* [![Add Sounds to Fire Traps](https://dev.epicgames.com/community/api/documentation/image/7a433b5e-267f-48e8-a8b3-7f0cffdf736e?resizing_type=fit&width=640&height=640)

  Add Sounds to Fire Traps

  Learn how to add a sound effect to a Blueprint.](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-09-adding-sounds-to-fire-traps-artist-track-unreal-engine)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Before You Begin](/documentation/en-us/unreal-engine/07-adjust-environment-lighting-features?application_version=5.7#beforeyoubegin)
* [Add Exponential Height Fog to Low-Lying Areas](/documentation/en-us/unreal-engine/07-adjust-environment-lighting-features?application_version=5.7#addexponentialheightfogtolow-lyingareas)
* [Add a Second Fog Layer](/documentation/en-us/unreal-engine/07-adjust-environment-lighting-features?application_version=5.7#addasecondfoglayer)
* [Add Colored Light to the Fog](/documentation/en-us/unreal-engine/07-adjust-environment-lighting-features?application_version=5.7#addcoloredlighttothefog)
* [Fix Volumetric Intensity of Spot Lights](/documentation/en-us/unreal-engine/07-adjust-environment-lighting-features?application_version=5.7#fixvolumetricintensityofspotlights)
* [Create Stormy Clouds with the Volumetric Cloud Component](/documentation/en-us/unreal-engine/07-adjust-environment-lighting-features?application_version=5.7#createstormycloudswiththevolumetriccloudcomponent)
* [Copy the Volumetric Cloud Material Instance](/documentation/en-us/unreal-engine/07-adjust-environment-lighting-features?application_version=5.7#copythevolumetriccloudmaterialinstance)
* [Customize the Volumetric Cloud](/documentation/en-us/unreal-engine/07-adjust-environment-lighting-features?application_version=5.7#customizethevolumetriccloud)
* [Adjust Light Properties with Light Mixers](/documentation/en-us/unreal-engine/07-adjust-environment-lighting-features?application_version=5.7#adjustlightpropertieswithlightmixers)
* [Next Up](/documentation/en-us/unreal-engine/07-adjust-environment-lighting-features?application_version=5.7#nextup)

Related documents

[Art Pass for a Puzzle Adventure Game](/documentation/en-us/unreal-engine/art-pass-for-a-puzzle-adventure-game)

[Design a Puzzle Adventure

![Design a Puzzle Adventure](https://dev.epicgames.com/community/api/documentation/image/a7b7ff2c-23d0-47a0-8a04-e569209942b0?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine)

[Environmental Light with Fog, Clouds, Sky and Atmosphere

![Environmental Light with Fog, Clouds, Sky and Atmosphere](https://dev.epicgames.com/community/api/documentation/image/892ee6c7-0143-485c-8d5c-12691ef75515?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/environmental-light-with-fog-clouds-sky-and-atmosphere-in-unreal-engine)

[Exponential Height Fog

![Exponential Height Fog](https://dev.epicgames.com/community/api/documentation/image/fd0dfd25-c262-4271-9738-e187145bb31c?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/exponential-height-fog-in-unreal-engine)

[Volumetric Cloud Material

![Volumetric Cloud Material](https://dev.epicgames.com/community/api/documentation/image/d996582d-4d1b-41a1-b02a-f8b20d571521?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/volumetric-cloud-material-in-unreal-engine)

[Environment Light Mixer

![Environment Light Mixer](https://dev.epicgames.com/community/api/documentation/image/40ad241c-481e-4c43-9b2c-3b742c404383?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/environment-light-mixer-in-unreal-engine)

[Light Mixer](/documentation/en-us/unreal-engine/using-the-light-mixer-in-unreal-engine)
