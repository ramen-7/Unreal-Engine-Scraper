<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/stationary-light-mobility-in-unreal-engine?application_version=5.7 -->

# Stationary Light Mobility

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
7. [Light Types and Their Mobility](/documentation/en-us/unreal-engine/light-types-and-their-mobility-in-unreal-engine "Light Types and Their Mobility")
8. Stationary Light Mobility

# Stationary Light Mobility

Partially dynamic and precomputed lighting capable of changing some of its properties during runtime.

![Stationary Light Mobility](https://dev.epicgames.com/community/api/documentation/image/a58b1a39-4e60-497a-a038-59692771a842?resizing_type=fill&width=1920&height=335)

 On this page

Lights that have their Mobility set to **Stationary** are lights that are intended to stay in one position, but are able to change in other ways, such as their brightness and color. This is the primary way they differ from [Static Lights](https://dev.epicgames.com/documentation/en-us/unreal-engine/static-light-mobility-in-unreal-engine), which cannot change in any way during gameplay.

Of the three light mobilities to choose from, Stationary lights have the highest quality, medium mutability, and medium performance cost.

Stationary Lights use both dynamic and static lighting to achieve its result, with indirect lighting and shadowing being stored within lightmaps for the Level. Direct shadows are stored within shadow maps. These lights make use of Distance Field Shadows, meaning that their shadows can remain crisp even with fairly low lightmap resolutions on lit objects.

## Stationary Direct Lighting

Stationary Lights use both dynamic direct lighting and static indirect lighting to achieve its result. The indirect lighting and shadowing is stored in lightmaps, while direct shadowing is stored in shadow maps. Because Stationary Lights are rendered dynamically using deferred shading, their brightness and color is able to change at runtime, and also support [Light Functions](building-virtual-worlds\lighting-and-shadows\features-of-lights\light-functions) and [IES Profiles](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-ies-light-profiles-in-unreal-engine) in the same way.

Stationary Lights also have high quality analytical specular, like [Movable Lights](https://dev.epicgames.com/documentation/en-us/unreal-engine/movable-light-mobility-in-unreal-engine).

![Stationary Directional Light | with Movable objects](https://dev.epicgames.com/community/api/documentation/image/67a935b0-b0c3-4d86-bab5-5f0b0fe3c44c?resizing_type=fit&width=1920&height=1080)

![Static Directional Light | with Movable objects](https://dev.epicgames.com/community/api/documentation/image/b8f26347-8479-4606-8f56-ef3f5cdd7631?resizing_type=fit&width=1920&height=1080)

Stationary Directional Light | with Movable objects

Static Directional Light | with Movable objects

## Stationary Light Shadowing

Only four or fewer Stationary Lights can overlap one another or any single piece of geometry in the Level, meaning that in some cases you will have fewer Stationary lights that can overlap in some parts of your Level. Shadowing cannot affect the overlap test, so the Directional Light typically requires a channel from the entire Level it is in, even areas that may be underground or hidden by other geometry. Once the channel limit is reached, only dynamic (or whole scene shadows) are used, which brings with it considerable performance cost.

When the limit of up to four Stationary Lights overlap at any time within a Level, the light icon will change to one with a **Red X** over the offending light until the overlap limit is resolved. There is a **Stationary Light Overlap** visualization mode that highlights offending lights in red until the overlap is resolved.

Enable the **Stationary Light Overlap** visualization from the Level Editor **View Mode > Optimization Viewmodes** dropdown selection.

[![level editor menu stationary light overlap visualization](https://dev.epicgames.com/community/api/documentation/image/2ae1dbf7-38e9-4a61-b925-42eb9f85690e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2ae1dbf7-38e9-4a61-b925-42eb9f85690e?resizing_type=fit)

### Stationary Indirect Lighting on Opaque Materials

[Lightmass](https://dev.epicgames.com/documentation/en-us/unreal-engine/global-illumination-in-unreal-engine) generates distance field shadow maps for Stationary Lights on Static objects during the lighting build process. Distance field shadow maps provide accurate shadow transitions, even at lower resolutions, and incur very little runtime cost. For example, lightmaps require uniquely unwrapped UVs on all meshes that have their mobility set to Static and have indirect lighting from a Static or Stationary light source.

[![](https://dev.epicgames.com/community/api/documentation/image/859c313d-a205-4641-82e6-6c190ac1e42d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/859c313d-a205-4641-82e6-6c190ac1e42d?resizing_type=fit)

Accurate shadowing of a Static Mesh Actor onto opaque surfaces.

Lighting must be built to display shadows from Stationary or Static light sources, otherwise dynamic shadows are used.

### Stationary Indirect Lighting on Translucent Materials

Translucency recieves shadowing at low cost with Stationary Lights since Lightmass precomputes a shadow depth map from Static geometry in the Level. That shadow depth is applied to translucency at runtime. This form of shadowing is fairly coarse and only captures shadowing in meters.

![Unshadowed Translucency](https://dev.epicgames.com/community/api/documentation/image/eba60a97-eb68-479c-a119-8203e04bddde?resizing_type=fit&width=1920&height=1080)

![Translucency receiving static shadowing | from a Directional Light](https://dev.epicgames.com/community/api/documentation/image/de84506b-5cd5-4f87-ba2b-ab93ef5889d3?resizing_type=fit&width=1920&height=1080)

Unshadowed Translucency

Translucency receiving static shadowing | from a Directional Light

The resolution of the static shadow depth map is controlled with `StaticShadowDepthMapTransitionSampleDistanceX` and `StaticShadowDepthMapTransitionSampleDistanceY` in the `BaseLightmass.ini` configuration file. It has a default value of 100, meaning one texel every meter.

### Stationary Light Dynamic Shadowing

Dynamic objects, such as Static Meshes with their Mobility set to Movable and Skeletal Meshes, must integrate into the world from shadow maps, which is accomplished with per object shadows. Each Movable object creates two dynamic shadows from a given Stationary Light: a shadow to handle the static world *onto the movable object*, and a shadow to handle the movable object *casting onto the world*.

With this setup, the only shadowing cost for Stationary Lights comes from the Movable objects it affects. It also means the cost can vary from very little to a large amount depending on how many Movable objects there are. With enough Movable objects being affected, it's actually more efficient to use a light with its Mobility set to Movable.

In the example scene below, the spheres have their Mobility set to **Movable**.

In the example scene below, a Stationary Directional Light is used to light the scene. The spheres have their Mobility set to **Movable** with the rest of the scene set to **Static**. Lighting has been built for the scene. The per object shadow frustums of each Movable sphere integrates seamlessly with the scene by receiving shadows from the objects behind and casting their own shadows that blend with the ones on the ground.

[![](https://dev.epicgames.com/community/api/documentation/image/bb0ba755-fbdd-4bea-ab8d-ecbee3516b55?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bb0ba755-fbdd-4bea-ab8d-ecbee3516b55?resizing_type=fit)

Per object shadows used by Movable components apply a shadow map to the object's bounds, therefore the bounds of the object must be accurate. For Skeletal Meshes, this means they should have a Physics Asset. For Particle Systems, a fixed bounding box must be large enough to contain all particles it generates.

#### Stationary Directional Light Dynamic Shadowing

Directional Stationary Lights are special in that they support whole scene shadows through **Cascaded Shadow Maps** at the same time as precomputed static shadowing. This is useful in scenes with lots of animating foliage where you want to have moving shadows around the player but do not want to pay the cost of having many levels of cascaded shadow maps covering a large view range at a larger cost.

A Directional Stationary Light uses Cascaded Shadow Maps for direct shadowing near the player within a specified range with **Dynamic Shadow Distance Stationary Light**. Any shadows beyond this distance fades into precomputed static shadows stored in lightmaps. By default, all Directional Stationary Lights start with a value of 0, meaning there is no dynamic shadowing taking place.

To save performance when you have a lot of Movable objects in the scene but want to use a smaller dynamic shadow distance, enable **Inset Shadows for Movable Objects**. It allows for movable objects to have a shadow even when they are outside of the cascaded shadow maps range and reduces shadowing cost significantly if there are many movable objects in the scene.

### Stationary Light Indirect Shadowing

Stationary Lights store their indirect lighting in lightmaps when lighting is built for the Level, just like Static Lights do. Indirect Lighting cannot be modified without invalidating lighting and needing to be rebuilt with exception to changing the Light's **Intensity** and **Light Color**. However, this does not affect the intensity or colors of the baked shadows.

A **Post Process Volume** does enable indirect shadows intensity and color to be changed using the **Global Illumination** category properties for **Indirect Lighting Color** and **Indirect Lighting Intensity**.

#### Use Area Shadows for Stationary Lights

whether to use area shadows for stationary light precomputed shadow maps.
area shadows get softer the further they are from shadow casters, but require higher lightmap resolution to get the same quality where the shadow is sharp.

By default, Static Lights automatically use area shadows — crisp, hard shadowing near surface contacts with softer shadows the farther surfaces are apart from one another — when building lighting. For Stationary Lights, the property **Use Area Shadows for Stationary Lights** enables soft area shadowing for any Static geometry in the scene affected by this light.

This property is enabled on Stationary Lights under the **Lightmass** section in the Light's **Details** panel.

![Default Stationary Shadows | for Static Geometry](https://dev.epicgames.com/community/api/documentation/image/81094718-73eb-4950-8548-15304094d587?resizing_type=fit&width=1920&height=1080)

![Area Shadows Enabled | for Static Geometry](https://dev.epicgames.com/community/api/documentation/image/74bca25a-d215-4fcc-939a-f32758baea4b?resizing_type=fit&width=1920&height=1080)

Default Stationary Shadows | for Static Geometry

Area Shadows Enabled | for Static Geometry

**Use Area Shadows for Stationary Lights** is only available on Stationary Lights and require higher lightmap resolutions for good results.

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [lighting](https://dev.epicgames.com/community/search?query=lighting)
* [mobility](https://dev.epicgames.com/community/search?query=mobility)
* [light type](https://dev.epicgames.com/community/search?query=light%20type)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Stationary Direct Lighting](/documentation/en-us/unreal-engine/stationary-light-mobility-in-unreal-engine?application_version=5.7#stationary-direct-lighting)
* [Stationary Light Shadowing](/documentation/en-us/unreal-engine/stationary-light-mobility-in-unreal-engine?application_version=5.7#stationary-light-shadowing)
* [Stationary Indirect Lighting on Opaque Materials](/documentation/en-us/unreal-engine/stationary-light-mobility-in-unreal-engine?application_version=5.7#stationary-indirect-lighting-on-opaque-materials)
* [Stationary Indirect Lighting on Translucent Materials](/documentation/en-us/unreal-engine/stationary-light-mobility-in-unreal-engine?application_version=5.7#stationary-indirect-lighting-on-translucent-materials)
* [Stationary Light Dynamic Shadowing](/documentation/en-us/unreal-engine/stationary-light-mobility-in-unreal-engine?application_version=5.7#stationary-light-dynamic-shadowing)
* [Stationary Directional Light Dynamic Shadowing](/documentation/en-us/unreal-engine/stationary-light-mobility-in-unreal-engine?application_version=5.7#stationary-directional-light-dynamic-shadowing)
* [Stationary Light Indirect Shadowing](/documentation/en-us/unreal-engine/stationary-light-mobility-in-unreal-engine?application_version=5.7#stationary-light-indirect-shadowing)
* [Use Area Shadows for Stationary Lights](/documentation/en-us/unreal-engine/stationary-light-mobility-in-unreal-engine?application_version=5.7#use-area-shadows-for-stationary-lights)
