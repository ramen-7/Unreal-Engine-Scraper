<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/actors-and-geometry-in-unreal-engine?application_version=5.7 -->

# Actors and Geometry

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
6. Actors and Geometry

# Actors and Geometry

Defines Actors and describes how to use them in level design. Also includes a rundown of the most common types of Actors.

![Actors and Geometry](https://dev.epicgames.com/community/api/documentation/image/84c23ed1-6a6a-403a-ac6f-61fd713c9fbb?resizing_type=fill&width=1920&height=335)

 On this page

An **Actor** is any object that can be placed into a Level, such as a camera, Static Mesh, or player start location. Actors support 3D transformations such as translation, rotation, and scaling. They can be created (spawned) and destroyed through gameplay code (C++ or Blueprints).

In C++, `AActor` is the base class of all Actors.

To create a Level, you place Actors into a Level (map), then move and scale them to create an environment, and add script to make them behave the way you want. This section covers the basic techniques of working with Actors, such as placing, selecting, and transforming Actors. It also covers some of the most commonly used Actor types.

## Working with Actors

[![Placing Actors](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cc559c2a-2d85-4bd0-bd44-be7f676c8d0e/placeholder_topic.png)

Placing Actors

Shows how you can place Actors such as props, lights, and cameras into your Level.](/documentation/en-us/unreal-engine/placing-actors-in-unreal-engine)
[![Selecting Actors](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1e7dc513-0737-460d-9c31-ab849738c7c2/placeholder_topic.png)

Selecting Actors

Overview of methods available for selecting Actors in the Level Editor viewport.](/documentation/en-us/unreal-engine/selecting-actors-in-unreal-engine)
[![Transforming Actors](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/298ef1aa-b2e8-493b-9a4b-aa156e2fab71/placeholder_topic.png)

Transforming Actors

How to modify the location, rotation, and scale of Actors in a Level.](/documentation/en-us/unreal-engine/transforming-actors-in-unreal-engine)
[![Actor Snapping](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ea33013f-4d72-4356-a700-8885b1178cfd/topic-image.png)

Actor Snapping

Overview of Actor snapping in Unreal Engine.](/documentation/en-us/unreal-engine/actor-snapping-in-unreal-engine)
[![Actor Mobility](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a6183e7e-d7aa-4921-9f3e-b3384f5b4e96/placeholder_topic.png)

Actor Mobility

Setting that controls whether an Actor can move or change in some way during gameplay.](/documentation/en-us/unreal-engine/actor-mobility-in-unreal-engine)
[![Grouping Actors](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fa5743f1-b0e7-49d4-bbff-dc3137908573/actorgrouping_topic.png)

Grouping Actors

How to create and work with groups of Actors in Unreal Engine.](/documentation/en-us/unreal-engine/grouping-actors-in-unreal-engine)
[![Merging Actors](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2861f29e-994f-4e18-b6a8-816f609d8a36/placeholder_topic.png)

Merging Actors

How to merge two or more Static Mesh Actors into a single Actor in Unreal Engine.](/documentation/en-us/unreal-engine/merging-actors-in-unreal-engine)

## Common Actor Types

This is not a comprehensive list of every Actor type available in Unreal Engine. Some plugins and project templates add their own Actors, and certain Actors may not be available for all projects.

[![Physics Volume Actor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/feecb00f-fe2b-4251-a8e1-1547c3a69e96/placeholder_topic.png)

Physics Volume Actor

Describes the properties of Physics Volumes in Unreal Engine.](/documentation/en-us/unreal-engine/physics-volume-actor-in-unreal-engine)
[![Static Mesh Actors](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cc768f4e-d5f8-44a1-b767-1aa70fe98cb5/topic-static-mesh-actors.png)

Static Mesh Actors

Place Static Mesh Actors in your Level to create your game world.](/documentation/en-us/unreal-engine/static-mesh-actors-in-unreal-engine)
[![Skeletal Mesh Actors](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3d6178dd-d5c4-44c8-b7d6-387f6b4df9df/topic-skeletal-mesh-actors.png)

Skeletal Mesh Actors

Use Skeletal Mesh Actors to create player avatars and populate your game world.](/documentation/en-us/unreal-engine/skeletal-mesh-actors-in-unreal-engine)
[![Geometry Brush Actors](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e8ec2dd9-b545-444e-ad9c-817690de78ca/topic-image.png)

Geometry Brush Actors

Guide to using BSP brushes to create level geometry in Unreal Engine.](/documentation/en-us/unreal-engine/geometry-brush-actors-in-unreal-engine)
[![Camera Actors](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7b8183db-920e-4257-814f-c127baebb687/placeholder_topic.png)

Camera Actors

Understanding the fundamentals of Cameras in Unreal Engine.](/documentation/en-us/unreal-engine/camera-actors-in-unreal-engine)
[![Audio Volume Actor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9427ba22-fbe1-47b4-b451-4685a2f444c8/placeholder_topic.png)

Audio Volume Actor

Audio Volume reference details](/documentation/en-us/unreal-engine/audio-volume-actor-in-unreal-engine)
[![Player Start Actor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9d9fb872-b5ac-41bb-9b15-a5a82371b52f/topic-player-start-actor.png)

Player Start Actor

Use Player Start Actors to set up starting locations for players.](/documentation/en-us/unreal-engine/player-start-actor-in-unreal-engine)
[![Trigger Volume Actors](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9358cb9c-92ee-4bfe-a370-bed1d16502b2/placeholder_topic.png)

Trigger Volume Actors

Actor that can be activated and cause events to occur in the Level.](/documentation/en-us/unreal-engine/trigger-volume-actors-in-unreal-engine)
[![Volume Actors](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9bac2e6b-db01-4f69-a781-97aadc0b9343/placeholder_topic.png)

Volume Actors

Reference for the different kinds of Volume Actors in Unreal Engine.](/documentation/en-us/unreal-engine/volume-actors-in-unreal-engine)
[![Pain-Causing Volume Actor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fadb6d6b-205d-477a-accd-4588ade51897/placeholder_topic.png)

Pain-Causing Volume Actor

Pain-Causing Volume reference details](/documentation/en-us/unreal-engine/pain-causing-volume-actor-in-unreal-engine)
[![Decal Actors](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/70e45340-f8e5-45e9-bf9e-fd4562a2c6c4/decal_topic.png)

Decal Actors

A guide to using the Deferred Decal actor.](/documentation/en-us/unreal-engine/decal-actors-in-unreal-engine)
[![3D Text Actor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e985d5c9-e2fa-402b-a5d2-19bb35713dc0/text3d-topic.png)

3D Text Actor

Guide to placing 3D Text and using it to create motion graphics.](/documentation/en-us/unreal-engine/3d-text-actor-in-unreal-engine)
[![Target Point Actors](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9d93c79a-f721-4ba7-8ba8-abc132b23f0b/placeholder_topic.png)

Target Point Actors

Guide to creating and using Target Actors.](/documentation/en-us/unreal-engine/target-point-actors-in-unreal-engine)

* [actors](https://dev.epicgames.com/community/search?query=actors)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Working with Actors](/documentation/en-us/unreal-engine/actors-and-geometry-in-unreal-engine?application_version=5.7#workingwithactors)
* [Common Actor Types](/documentation/en-us/unreal-engine/actors-and-geometry-in-unreal-engine?application_version=5.7#commonactortypes)
