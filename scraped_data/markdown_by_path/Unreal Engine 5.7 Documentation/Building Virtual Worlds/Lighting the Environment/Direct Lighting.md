<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/features-and-properties-of-lights-in-unreal-engine?application_version=5.7 -->

# Direct Lighting

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
7. Direct Lighting

# Direct Lighting

An overview of the various properties and features that lights support.

![Direct Lighting](https://dev.epicgames.com/community/api/documentation/image/3f5b319f-3a8c-462a-9d9a-f96fd2b88a42?resizing_type=fill&width=1920&height=335)

 On this page

Lights in Unreal Engine contain a large set of properties to work with, which are partly dependent on the [Light's mobility and type](/documentation/en-us/unreal-engine/light-types-and-their-mobility-in-unreal-engine).

Light properties are found in the **Details** panel when a light is selected in the Level. Depending on the set **Mobility** of **Static**, **Stationary**, or **Movable** determines what features and properties of the light are supported for the selected light.

![directional light properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5f7074f5-1c67-44c8-9e1a-cab962a4bac0/light-properties.png)

Light properties of a Directional Light.

## Things to Consider for Lights and their Properties

Before diving into the specific features and properties of Lights, you'll want to consider the following:

* What types of lights does your scene require to light it?
* What Mobility should your lights have?
* Lights with different mobilities can be mixed and matched as needed to light a scene. However, considerations must be considered for what that means for the lighting, shadows, and assets it affects within the Level. Not all properties support every mobility or light type.
* [Shadowing](/documentation/en-us/unreal-engine/shadowing-in-unreal-engine) is a broad subject with lighting. Mobilities, type of light, or even enabled lighting features in the Project Settings can affect how lighting works within the project.
* Some types of lights complement other standalone features, such as one for [Environmental Lighting](/documentation/en-us/unreal-engine/environmental-light-with-fog-clouds-sky-and-atmosphere-in-unreal-engine).

## Setting Properties for Lights

The properties and features of lights can be found in the **Details** panel when a light is selected in the Level.

Each light must have its **Mobility** set to **Static**, **Stationary**, or **Movable**.

![light mobility selection](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b42ebff6-b79f-474f-9aca-36ec233b1510/il_mobility.png)

All properties of lights are listed no matter what selection is made, but the mobility affects some properties that are supported. For example, Lightmass settings only affect mobilities set to Static or Stationary.

Explore the topics below to learn about some of the features and properties you can use with the Lights in your scenes and projects.

### General Light Features and Properties Topics

A listing of general concepts and features related to all, or most, types of lights you can use. These can be individual features of lights you can use, or properties of lights that work with larger features, like Global Illumination.

%building-virtual-worlds/lighting-and-shadows/features-of-lights/mega-lights:Topic%
[![Physical Lighting Units](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/db9995a6-67c5-4622-b51b-82e5624bb200/physical-light-units-topic.png)

Physical Lighting Units

An overview of using physically based lighting units with light sources.](/documentation/en-us/unreal-engine/using-physical-lighting-units-in-unreal-engine)
[![Global Illumination](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4adeabb1-f7f8-456e-9709-90784c974c21/randg_topicsmall.png)

Global Illumination

A collection of topics on the global illumination options available to choose from.](/documentation/en-us/unreal-engine/global-illumination-in-unreal-engine)
[![Shadowing](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8be3f00c-3e17-4565-bb9a-fc5ffa40fb43/source-radius-example.png)

Shadowing

An overview of available shadowing methods and the properties they support.](/documentation/en-us/unreal-engine/shadowing-in-unreal-engine)
[![Reflections Environment](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/864b7d89-2140-47f5-9a2c-462ef7f85a7c/rtr_multiplebounces.png)

Reflections Environment

Systems for how reflections are captured and displayed on reflective surfaces.](/documentation/en-us/unreal-engine/reflections-environment-in-unreal-engine)
[![Light Types and Their Mobility](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f98e2063-beaa-4815-9038-26910b1b7994/lm_topic.png)

Light Types and Their Mobility

The available types of lights to choose from and how their mobility settings affect lighting in the scene.](/documentation/en-us/unreal-engine/light-types-and-their-mobility-in-unreal-engine)
[![Mesh Distance Fields](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8e467246-5eb4-4c7a-ad26-055395864c9c/distance-field-topic.png)

Mesh Distance Fields

An overview of Mesh Distance Fields and its available features that you can use when developing your games.](/documentation/en-us/unreal-engine/mesh-distance-fields-in-unreal-engine)
[![Lighting Channels](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9eea4eb4-6244-434c-8d0b-4ac0108740b4/using-lightning-channels-topic.png)

Lighting Channels

An overview of using channels of a light source to light specific surfaces.](/documentation/en-us/unreal-engine/using-lighting-channels-in-unreal-engine)
[![IES Light Profiles](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/61af8f0d-ea37-4873-bb6f-f26db5b2e896/ies-light-profiles-topic.png)

IES Light Profiles

An overview of setting up and using IES textures with lights.](/documentation/en-us/unreal-engine/using-ies-light-profiles-in-unreal-engine)
%building-virtual-worlds/lighting-and-shadows/features-of-lights/light-functions:Topic%

## Directional Light Features and Properties Topics

The following features work with [Directional Lights](/documentation/en-us/unreal-engine/directional-lights-in-unreal-engine).

%building-virtual-worlds/lighting-and-shadows/features-of-lights/light-shafts:Topic%
[![Sky Atmosphere Component](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b8387986-89fb-4810-abde-f4b04c381381/sky-atmosphere-topic-image.png)

Sky Atmosphere Component

A physically-based sky and atmosphere rendering system with time-of-day features and ground-to-space view transitions featuring aerial perspective.](/documentation/en-us/unreal-engine/sky-atmosphere-component-in-unreal-engine)
[![Volumetric Cloud Component](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d5d27248-8407-4e94-9ea9-9982ba198b84/volumetric-cloud-topic-image.png)

Volumetric Cloud Component

Real-time cloud rendering using volumetric materials.](/documentation/en-us/unreal-engine/volumetric-cloud-component-in-unreal-engine)

## Sky Light Features and Properties Topics

The following features work with a [Sky Light](/documentation/en-us/unreal-engine/sky-lights-in-unreal-engine).

%building-virtual-worlds/lighting-and-shadows/environmental-lighting:Topic%

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [lighting](https://dev.epicgames.com/community/search?query=lighting)
* [lights](https://dev.epicgames.com/community/search?query=lights)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Things to Consider for Lights and their Properties](/documentation/en-us/unreal-engine/features-and-properties-of-lights-in-unreal-engine?application_version=5.7#thingstoconsiderforlightsandtheirproperties)
* [Setting Properties for Lights](/documentation/en-us/unreal-engine/features-and-properties-of-lights-in-unreal-engine?application_version=5.7#settingpropertiesforlights)
* [General Light Features and Properties Topics](/documentation/en-us/unreal-engine/features-and-properties-of-lights-in-unreal-engine?application_version=5.7#generallightfeaturesandpropertiestopics)
* [Directional Light Features and Properties Topics](/documentation/en-us/unreal-engine/features-and-properties-of-lights-in-unreal-engine?application_version=5.7#directionallightfeaturesandpropertiestopics)
* [Sky Light Features and Properties Topics](/documentation/en-us/unreal-engine/features-and-properties-of-lights-in-unreal-engine?application_version=5.7#skylightfeaturesandpropertiestopics)
