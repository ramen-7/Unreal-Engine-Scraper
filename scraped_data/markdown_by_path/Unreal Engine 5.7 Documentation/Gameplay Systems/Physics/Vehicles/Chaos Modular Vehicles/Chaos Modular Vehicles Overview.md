<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/chaos-modular-vehicles-overview?application_version=5.7 -->

# Chaos Modular Vehicles Overview

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
5. [Gameplay Systems](/documentation/en-us/unreal-engine/gameplay-systems-in-unreal-engine "Gameplay Systems")
6. [Physics](/documentation/en-us/unreal-engine/physics-in-unreal-engine "Physics")
7. [Vehicles](/documentation/en-us/unreal-engine/vehicles-in-unreal-engine "Vehicles")
8. [Chaos Modular Vehicles](/documentation/en-us/unreal-engine/chaos-modular-vehicles "Chaos Modular Vehicles")
9. Chaos Modular Vehicles Overview

# Chaos Modular Vehicles Overview

Overview of the Chaos Modular Vehicle system in Unreal Engine.

![Chaos Modular Vehicles Overview](https://dev.epicgames.com/community/api/documentation/image/b64842fa-553e-42d5-bdf4-78318ac5824b?resizing_type=fill&width=1920&height=335)

 On this page

## Introduction

![Modular Vehicles](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/201b8b42-6fe3-4293-be04-9e8ef45b0a12/lego-vehicles.gif)

The **Chaos Modular Vehicle System** is a vehicle simulation plugin that supports real time vehicle construction and destruction. This means that vehicle components can be added or removed at runtime to accommodate gameplay conditions.

An assembled vehicle can be broken up by manually detaching components with code, or by using the physics simulation to break off certain pieces during physics collisions.

This system was designed from the ground up to support the [resimulation network physics model](/documentation/en-us/unreal-engine/networked-physics-overview) and to be more flexible than the vehicle system, but with certain limitations. For this reason, both systems exist in tandem and can be used in the same project.

## Vehicle System vs. Modular Vehicle System

### Vehicle Composition

Vehicles created with the vehicle system are based on a skeletal mesh, and as a result have a fixed topology once the asset is created. These vehicles set up their collision with the [Physics Asset Editor](/documentation/en-us/unreal-engine/physics-asset-editor-in-unreal-engine) and can be animated using skeletal mesh animation.

In contrast, vehicles created with the Modular Vehicle system are built by creating a hierarchy of Geometry Collection components connected under a Cluster Union vehicle component. In addition, each Geometry Collection component can have its own simulation component to drive its behavior at runtime.

### Replication Support

The Modular Vehicle system comes with native support for the Network Physics component and resimulation replication mode, which provides client predicted server authoritative physics (with rewind resimulation). In addition, developers can create their own custom modules with interfaces for dealing with any additional network serialization that is required for a resimulation.

### Simulation Representation

The Vehicle system uses one component to drive the entire vehicle simulation. This component is used to configure the different aspects of the vehicle simulation, such as the engine, transmission, chassis, and wheels.

The Modular Vehicle system is based on a collection of separate simulation components that get assigned to a simulation tree when the Geometry Collections are added to the Cluster Union component. The system includes engine, chassis, transmission, clutch, suspension, wheel, thruster and aerofoil simulation components.

The modules operate independent of each other, simulating their assigned Geometry Collection component and applying forces to the combined Cluster Union rigid body.

Any number of simulation components can be added or removed from a vehicle, allowing for a wider variety of vehicle types.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Introduction](/documentation/en-us/unreal-engine/chaos-modular-vehicles-overview?application_version=5.7#introduction)
* [Vehicle System vs. Modular Vehicle System](/documentation/en-us/unreal-engine/chaos-modular-vehicles-overview?application_version=5.7#vehiclesystemvsmodularvehiclesystem)
* [Vehicle Composition](/documentation/en-us/unreal-engine/chaos-modular-vehicles-overview?application_version=5.7#vehiclecomposition)
* [Replication Support](/documentation/en-us/unreal-engine/chaos-modular-vehicles-overview?application_version=5.7#replicationsupport)
* [Simulation Representation](/documentation/en-us/unreal-engine/chaos-modular-vehicles-overview?application_version=5.7#simulationrepresentation)
