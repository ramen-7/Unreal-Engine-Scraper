<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/destruction-overview?application_version=5.7 -->

# Destruction Overview

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
7. [Chaos Destruction](/documentation/en-us/unreal-engine/chaos-destruction-in-unreal-engine "Chaos Destruction")
8. Destruction Overview

# Destruction Overview

Overview of Unreal Engine's Destruction system.

![Destruction Overview](https://dev.epicgames.com/community/api/documentation/image/422aa5ac-5f60-4984-a12c-9700388522e6?resizing_type=fill&width=1920&height=335)

![alt text](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f642f6c4-3984-49a5-ae00-c0886f62e54c/city-chaos-destruction-small.gif)

The **Chaos Destruction** system is a collection of tools that can be used to achieve cinematic-quality levels of destruction in real time. In addition to great-looking visuals, the system is optimized for performance, and grants artists and designers more control over content creation and the fracturing process by using an intuitive nonlinear workflow.

The system allows artists to define exactly how geometry will break during the simulation. Artists construct the simulation assets using pre-fractured geometry and utilize dynamically-generated rigid constraints to model the structural connections during the simulation. The resulting objects within the simulation can separate from connected structures based on interactions with environmental elements, like [Physics Field](/documentation/en-us/unreal-engine/physics-fields-in-unreal-engine) and collisions.

The destruction system relies on an internal clustering model which controls how the rigidly attached geometry is simulated. Clustering allows artists to initialize sets of geometry as a single rigid body, then dynamically break the objects during the simulation. At its core, the clustering system will simply join the mass and inertia of each connected element into one larger single rigid body.

The destruction system uses on a new type of asset called a **Geometry Collection** as the base container for its geometry and simulation properties. A Geometry Collection can be created from static and skeletal mesh sources, and then fractured and clustered using UE5's **Fracture Mode**.

At the beginning of the simulation a connection graph is initialized based on each fractured rigid body's nearest neighbors. Each connection between the bodies represents a rigid constraint within the cluster and is given initial strain values. During the simulation, the strains within the connection graph are evaluated. These connections can be broken when collision constraints or field evaluations apply an impulse on the rigid body that exceeds the connections limit. Physics Fields can also be used to decrease the internal strain values of the connections, resulting in a weakening of the internal structure.

For large-scale destruction simulations, Chaos Destruction comes with a new **Cache System** that allows for smooth replay of complex destruction at runtime with minimal impact on performance.

Chaos Destruction easily integrates with other Unreal Engine systems, such as [Niagara](/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine) and [Audio Mixer](/documentation/404), to spawn particles or play specific sounds during the simulation.

* [physics](https://dev.epicgames.com/community/search?query=physics)
* [chaos](https://dev.epicgames.com/community/search?query=chaos)
* [destruction](https://dev.epicgames.com/community/search?query=destruction)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)
