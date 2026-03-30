<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/light-types-and-their-mobility-in-unreal-engine?application_version=5.7 -->

# Light Types and Their Mobility

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
4. Light Types and Their Mobility

# Light Types and Their Mobility

The available types of lights to choose from and how their mobility settings affect lighting in the scene.

![Light Types and Their Mobility](https://dev.epicgames.com/community/api/documentation/image/13067b7f-64ce-4c01-91fc-9abe333fbfd2?resizing_type=fill&width=1920&height=335)

 On this page

Unreal Engine provides several types of light to create nearly any type of lighting scenario and to work with small to large scale worlds. Each of these types of lights also has its own mobility option to define how it interacts with the other Actors in the scene and how the lighting system will utilize the light.

## Types of Lights

The types of lights available in the Editor make it possible to light your world in various styles and configurations to achieve the look you want for your project. With these light types, you can light any size scenes from large sprawling worlds to small localized interiors.

Unreal Engine provides the following types of lights:

* **Directional Lights** are the primary outdoor light, or any light that needs to appear as if it's casting light from extreme, or near infinite, distances.
* **Sky Light** captures the background of the scene and applies it to the Level's geometry.
* **Point Lights** act as a light bulb, casting light in all directions from a single point.
* **Spot Lights** emit light from a single point in a direction limited by a set of cones.
* **Rect Lights** emit light from a rectangular surface in a direction.

**Directional** and **Sky Lights** are useful for large exteriors or to provide lighting and shadowing through interior openings. For large exteriors, Directional Lights are most effective for lighting dense foliage and other geometry more efficiently.

|  |  |
| --- | --- |
| directional light | sky light |
| Directional Light | Sky Light |

**Point**, **Spot**, and **Rect Lights** are useful for lighting smaller localized areas. Their type and properties can help define their shape and look within a given scene. These types of lights also share a lot of the same properties.

|  |  |  |
| --- | --- | --- |
| point light | spot light | rectangular area light |
| Point Light | Spot Light | Rectangular Area Light |

### Overview of Light Types

%building-virtual-worlds/lighting-and-shadows/light-types-and-mobility/Directional:Topic%
[![Sky Lights](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0b03f2e4-d392-438e-950a-bbe79879f766/skylight_topic.png)

Sky Lights

The basics of undestanding sky lighting.](/documentation/en-us/unreal-engine/sky-lights-in-unreal-engine)
[![Point Lights](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/63483740-8f84-4ecb-9080-5c6391743247/pointlight_topic.png)

Point Lights

The basics of undestanding point lights.](/documentation/en-us/unreal-engine/point-lights-in-unreal-engine)
%building-virtual-worlds/lighting-and-shadows/light-types-and-mobility/Spot:Topic%
[![Rectangular Area Lights](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2a313be6-d5bf-4326-bf54-1dad845b96d3/rectlight_topic.png)

Rectangular Area Lights

The basics of undestanding rectangular area lights.](/documentation/en-us/unreal-engine/rectangular-area-lights-in-unreal-engine)

## Light Mobility

Each type of Actor in a scene has its own **Mobility** setting that controls whether it is allowed to move or change in some way during gameplay. For Light Actors, the mobility selection defines how the light will be treated in the scene when a light build is taking place.

It's important to choose the type of light mobility that makes the most sense for your project as they will impact performance, look, and design choice. Some features of lights are limited in their functionality or not entirely supported for some platforms or machines. For example, dynamic shadowing is not supported for all types of lights on mobile platforms.

Each Light Actor has three mobility states:

![light mobility selection](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e54c4a57-0431-4ff1-a502-7e41585bfb48/il_mobility.png)

| Mobility State | Description |
| --- | --- |
| **Static** | This mobility is reserved for Light Actors that are not intended to move or update in any way during gameplay.  Static lights will contribute to pre-calculated lightmaps using [Lightmass](/documentation/en-us/unreal-engine/global-illumination-in-unreal-engine). These lights will illuminate the scene and generate lighting data for any Actors set to Static and Stationary, but for Movable ones, they will be lit by lighting data stored in the [Indirect Lighting Cache](/documentation/en-us/unreal-engine/indirect-lighting-cache-in-unreal-engine) or [Volumetric Lightmaps](/documentation/en-us/unreal-engine/volumetric-lightmaps-in-unreal-engine) to light them. |
| **Stationary** | This mobility is reserved for Actors that can during gameplay, but not move.  These lights can change in some way during gameplay, such as having their color or intensity changed, or turned completely off. Stationary Lights contribute to pre-calculated lightmaps using [Lightmass](/documentation/en-us/unreal-engine/global-illumination-in-unreal-engine), but they can also cast dynamic shadows for movable objects. Stationary lights come with added cost and are limited by the number of lights that can affect a single object at any given time. For example, A single object can only be affected by up to four Stationary Lights at any time. |
| **Movable** | This mobility is reserved for Light Actors that need to be added, removed, or moved during gameplay.  These lights only cast dynamic shadows. In addition to being able to move them during gameplay, they can also change their color, intensity, and other light properties as needed.  Care must be taken when using lights with this mobility since their shadowing cost is the most costly. However, non-shadowing Movable lights are very inexpensive to calculate, and carry a lower cost than lights that are set to Static since there is no lighting data that needs to be saved to disk. |

### Overview of Light Mobility

%building-virtual-worlds/lighting-and-shadows/light-types-and-mobility/movable-lights:Topic%
%building-virtual-worlds/lighting-and-shadows/light-types-and-mobility/StationaryLights:Topic%
[![Static Light Mobility](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/51a12235-1f00-46dc-aced-088a410bf7a4/sl_topic.png)

Static Light Mobility

Precomputed lighting baked into textures that cannot change and has no lighting cost during runtime.](/documentation/en-us/unreal-engine/static-light-mobility-in-unreal-engine)

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [lights](https://dev.epicgames.com/community/search?query=lights)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Types of Lights](/documentation/en-us/unreal-engine/light-types-and-their-mobility-in-unreal-engine?application_version=5.7#typesoflights)
* [Overview of Light Types](/documentation/en-us/unreal-engine/light-types-and-their-mobility-in-unreal-engine?application_version=5.7#overviewoflighttypes)
* [Light Mobility](/documentation/en-us/unreal-engine/light-types-and-their-mobility-in-unreal-engine?application_version=5.7#lightmobility)
* [Overview of Light Mobility](/documentation/en-us/unreal-engine/light-types-and-their-mobility-in-unreal-engine?application_version=5.7#overviewoflightmobility)
