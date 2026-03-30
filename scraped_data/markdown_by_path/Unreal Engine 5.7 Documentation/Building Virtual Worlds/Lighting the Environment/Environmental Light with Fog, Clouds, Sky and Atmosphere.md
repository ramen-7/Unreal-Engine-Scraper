<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/environmental-light-with-fog-clouds-sky-and-atmosphere-in-unreal-engine?application_version=5.7 -->

# Environmental Light with Fog, Clouds, Sky and Atmosphere

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
6. [Lighting the Environment](/documentation/en-us/unreal-engine/lighting-the-environment-in-unreal-engine "Lighting the Environment")
7. Environmental Light with Fog, Clouds, Sky and Atmosphere

# Environmental Light with Fog, Clouds, Sky and Atmosphere

Components and tools that enable users to build immersive worlds with environment lighting from fog, clouds, sky and atmosphere.

![Environmental Light with Fog, Clouds, Sky and Atmosphere](https://dev.epicgames.com/community/api/documentation/image/3552e785-af9d-489f-a5f5-0d39964a5a2a?resizing_type=fill&width=1920&height=335)

 On this page

Unreal Engine provides a set of components that allow for designers and artists to create immersive worlds with physically based lighting at large — or even small — scale while working efficiently to do so. These environment lighting components for atmosphere, clouds, fog, and lighting all work seamlessly together to create a unified experience that supports fully dynamically lit worlds.

The tools and features in this page will help you get started with creating your own worlds.

## Light Mixer

The **Light Mixer** is a dockable editor window where you can add, edit, and reference properties of Directional, Point, Spot, and Rect Lights in your Level.

For artists and designers, this window simplifies and can speed up your workflow by having them availabl and editable in one location. This includes lights that are components of scene Actors or of Blueprints. You can use Collections to organize them as well.

[![Light Mixer Panel](https://dev.epicgames.com/community/api/documentation/image/c3259e7b-a916-4279-af46-c6fec7f0a48e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c3259e7b-a916-4279-af46-c6fec7f0a48e?resizing_type=fit)

For more information, see [Light Mixer](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-light-mixer-in-unreal-engine).

## Environment Light Mixer

The **Environment Light Mixer** is a dockable editor window where you can add, edit, and reference properties of environment lighting components for sky, clouds, atmosphere lights, and a sky light.

For artists and designers, this window simplifies and can speed up your workflow by having them all available in one location.

[![](https://dev.epicgames.com/community/api/documentation/image/e73797b2-a717-49fd-bc21-8afbe14315bb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e73797b2-a717-49fd-bc21-8afbe14315bb?resizing_type=fit)

For more information, see [Environment Light Mixer](https://dev.epicgames.com/documentation/en-us/unreal-engine/environment-light-mixer-in-unreal-engine).

## Fog Effects

Fog effects are useful for adding ambiance to the world and setting the mood for environments. This includes creating multi-layered fog for high and low-lying areas, and volumetric effects for light shafts.

[![volumetric fog](https://dev.epicgames.com/community/api/documentation/image/f9a59c30-a722-455c-b7b0-bb91b2ef0665?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f9a59c30-a722-455c-b7b0-bb91b2ef0665?resizing_type=fit)

The [Sky Atmosphere](https://dev.epicgames.com/documentation/en-us/unreal-engine/sky-atmosphere-component-in-unreal-engine) includes its own scattering and height fog simulation, but also works well with the Exponential Height Fog to support all types of lights in the scene.

![Sky Atmosphere's Height Fog](https://dev.epicgames.com/community/api/documentation/image/a338f91e-e932-4237-a251-e0980464083f?resizing_type=fit&width=1920&height=1080)

![Sky Atmosphere | with Exponential Height Fog](https://dev.epicgames.com/community/api/documentation/image/3b7181ea-7a4e-4ddd-b76d-e7af6872fbd7?resizing_type=fit&width=1920&height=1080)

Sky Atmosphere's Height Fog

Sky Atmosphere | with Exponential Height Fog

When the Project Setting **Support Sky Atmosphere Affecting Height Fog** is enabled, any contribution from Exponential Height Fog is additive. The Sky Atmosphere's height fog is applied on top of the Exponential Height Fog colors. However, should the **Fog Inscattering Color** and **Directional Inscattering Color** be set to black, the Sky Atmosphere will directly affect and influence the coloring of any Exponential Height Fog in the scene.

Additionally, you can used locally placed fog volumes to create fog effects in large or small areas of your scene. These local fog volumes support all platforms and volumetric fog effects when enabled.

[![Placed Local Fog Volumes in a scene.](https://dev.epicgames.com/community/api/documentation/image/b3d45e87-3219-43da-9944-122cfed8a7df?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b3d45e87-3219-43da-9944-122cfed8a7df?resizing_type=fit)

### Fog Effects Topics

* [![Exponential Height Fog](https://dev.epicgames.com/community/api/documentation/image/9d4a0bf6-f2a3-4f59-a2e0-0fe9ece4d07c?resizing_type=fit&width=640&height=640)

  Exponential Height Fog

  An overview of the height-based, distant fog system.](https://dev.epicgames.com/documentation/en-us/unreal-engine/exponential-height-fog-in-unreal-engine)

* [![Local Fog Volumes](https://dev.epicgames.com/community/api/documentation/image/721ae029-df9b-4053-829d-f7fa30ccbe00?resizing_type=fit&width=640&height=640)

  Local Fog Volumes

  An overview of locally placed volumes to create height-based fog effects.](https://dev.epicgames.com/documentation/en-us/unreal-engine/local-fog-volumes-in-unreal-engine)

* [![Volumetric Fog](https://dev.epicgames.com/community/api/documentation/image/ce84088e-5aa2-4039-b2a9-83dd0d0af6da?resizing_type=fit&width=640&height=640)

  Volumetric Fog

  An overview of the volumetric fog and lighting options available with the Exponential Height Fog Component.](https://dev.epicgames.com/documentation/en-us/unreal-engine/volumetric-fog-in-unreal-engine)

## Atmosphere, Cloud, and World Lighting Effects

The lighting components for Sky Atmosphere, Volumetric Clouds, Directional Lights, and Sky Light make up the majority of your enviornment lighting. These components all work seamlessly together dynamically lit large worlds possible.

[![enviornment lighting components](https://dev.epicgames.com/community/api/documentation/image/96aac395-0ff2-4910-98d5-54c128e1b86d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/96aac395-0ff2-4910-98d5-54c128e1b86d?resizing_type=fit)

In your Levels, you can use the following components:

* Up to two Directional Lights for the sun and moon, two suns, or any combination.
* A single Sky Light with optional real-time capturing.
* A Sky Atmosphere with its own height fog.
* Volumetric Clouds with or without a sky dome mesh.

With **Real Time Capture** enabled on the Sky Light, use the keyboard shortcut **Right Ctrl + L** (first Directional Light) or **Right Ctrl + Right Shift + L** (second Directional Light) in combination with moving the mouse to change lighting dynamically and see the results instantly.

### Atmosphere, Clouds, and World Lighting Topics

* [![Sky Atmosphere Component](https://dev.epicgames.com/community/api/documentation/image/b8387986-89fb-4810-abde-f4b04c381381?resizing_type=fit&width=640&height=640)

  Sky Atmosphere Component

  A physically-based sky and atmosphere rendering system with time-of-day features and ground-to-space view transitions featuring aerial perspective.](https://dev.epicgames.com/documentation/en-us/unreal-engine/sky-atmosphere-component-in-unreal-engine)

* [![Volumetric Cloud Component](https://dev.epicgames.com/community/api/documentation/image/d5d27248-8407-4e94-9ea9-9982ba198b84?resizing_type=fit&width=640&height=640)

  Volumetric Cloud Component

  Real-time cloud rendering using volumetric materials.](https://dev.epicgames.com/documentation/en-us/unreal-engine/volumetric-cloud-component-in-unreal-engine)

* [![Directional Lights](https://dev.epicgames.com/community/api/documentation/image/92ad23d0-3477-4663-956f-93d7da3fbf0b?resizing_type=fit&width=640&height=640)

  Directional Lights

  The basics of undestanding directional lights.](https://dev.epicgames.com/documentation/en-us/unreal-engine/directional-lights-in-unreal-engine)

* [![Sky Lights](https://dev.epicgames.com/community/api/documentation/image/0b03f2e4-d392-438e-950a-bbe79879f766?resizing_type=fit&width=640&height=640)

  Sky Lights

  The basics of undestanding sky lighting.](https://dev.epicgames.com/documentation/en-us/unreal-engine/sky-lights-in-unreal-engine)

* [![Heterogeneous Volumes](https://dev.epicgames.com/community/api/documentation/image/af82dd58-2636-48f7-b27c-0237e343a425?resizing_type=fit&width=640&height=640)

  Heterogeneous Volumes

  Use the Heterogeneous Volume component to render volume-domain materials that sample from Sparse Volume Textures.](https://dev.epicgames.com/documentation/en-us/unreal-engine/heterogeneous-volumes-in-unreal-engine)

### Atmosphere, Clouds, and World Lighting Properties Reference

* [![Sky Atmosphere Component Properties](https://dev.epicgames.com/community/api/documentation/image/9c7d9eff-3e40-486e-902c-391bec050446?resizing_type=fit&width=640&height=640)

  Sky Atmosphere Component Properties

  Settings and property reference for the Sky Atmosphere Component.](https://dev.epicgames.com/documentation/en-us/unreal-engine/sky-atmosphere-component-properties-in-unreal-engine)

* [![Volumetric Cloud Component Properties](https://dev.epicgames.com/community/api/documentation/image/14b65465-f014-4732-a2b2-7c7c60af44bb?resizing_type=fit&width=640&height=640)

  Volumetric Cloud Component Properties

  Settings and property reference for the Volumetric Clouds Component.](https://dev.epicgames.com/documentation/en-us/unreal-engine/volumetric-cloud-component-properties-in-unreal-engine)

## Material and Sparse Volume Texture Assets

* [![Sparse Volume Textures](https://dev.epicgames.com/community/api/documentation/image/265e7889-3102-4e1b-bfc4-dddad349ae85?resizing_type=fit&width=640&height=640)

  Sparse Volume Textures

  An asset that stores baked simulation data representing volumetric media, such as smoke, fire, and water.](https://dev.epicgames.com/documentation/en-us/unreal-engine/sparse-volume-textures-in-unreal-engine)

* [![Volumetric Cloud Material](https://dev.epicgames.com/community/api/documentation/image/d996582d-4d1b-41a1-b02a-f8b20d571521?resizing_type=fit&width=640&height=640)

  Volumetric Cloud Material

  The default volumetric material used to create various types of cloud types, shapes, and effects.](https://dev.epicgames.com/documentation/en-us/unreal-engine/volumetric-cloud-material-in-unreal-engine)

* [environment](https://dev.epicgames.com/community/search?query=environment)
* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [lighting](https://dev.epicgames.com/community/search?query=lighting)
* [fog](https://dev.epicgames.com/community/search?query=fog)
* [clouds](https://dev.epicgames.com/community/search?query=clouds)
* [atmosphere](https://dev.epicgames.com/community/search?query=atmosphere)
* [sky](https://dev.epicgames.com/community/search?query=sky)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Light Mixer](/documentation/en-us/unreal-engine/environmental-light-with-fog-clouds-sky-and-atmosphere-in-unreal-engine?application_version=5.7#light-mixer)
* [Environment Light Mixer](/documentation/en-us/unreal-engine/environmental-light-with-fog-clouds-sky-and-atmosphere-in-unreal-engine?application_version=5.7#environment-light-mixer)
* [Fog Effects](/documentation/en-us/unreal-engine/environmental-light-with-fog-clouds-sky-and-atmosphere-in-unreal-engine?application_version=5.7#fog-effects)
* [Fog Effects Topics](/documentation/en-us/unreal-engine/environmental-light-with-fog-clouds-sky-and-atmosphere-in-unreal-engine?application_version=5.7#fog-effects-topics)
* [Atmosphere, Cloud, and World Lighting Effects](/documentation/en-us/unreal-engine/environmental-light-with-fog-clouds-sky-and-atmosphere-in-unreal-engine?application_version=5.7#atmosphere-cloud-and-world-lighting-effects)
* [Atmosphere, Clouds, and World Lighting Topics](/documentation/en-us/unreal-engine/environmental-light-with-fog-clouds-sky-and-atmosphere-in-unreal-engine?application_version=5.7#atmosphere-clouds-and-world-lighting-topics)
* [Atmosphere, Clouds, and World Lighting Properties Reference](/documentation/en-us/unreal-engine/environmental-light-with-fog-clouds-sky-and-atmosphere-in-unreal-engine?application_version=5.7#atmosphere-clouds-and-world-lighting-properties-reference)
* [Material and Sparse Volume Texture Assets](/documentation/en-us/unreal-engine/environmental-light-with-fog-clouds-sky-and-atmosphere-in-unreal-engine?application_version=5.7#material-and-sparse-volume-texture-assets)
