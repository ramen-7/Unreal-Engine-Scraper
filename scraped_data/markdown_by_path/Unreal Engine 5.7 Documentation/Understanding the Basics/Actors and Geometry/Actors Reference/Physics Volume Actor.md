<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/physics-volume-actor-in-unreal-engine?application_version=5.7 -->

# Physics Volume Actor

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
6. [Actors and Geometry](/documentation/en-us/unreal-engine/actors-and-geometry-in-unreal-engine "Actors and Geometry")
7. [Actors Reference](/documentation/en-us/unreal-engine/unreal-engine-actors-reference "Actors Reference")
8. Physics Volume Actor

# Physics Volume Actor

Describes the properties of Physics Volumes in Unreal Engine.

![Physics Volume Actor](https://dev.epicgames.com/community/api/documentation/image/d66afc21-baa7-4c3d-bace-a0176ce39924?resizing_type=fill&width=1920&height=335)

There are some properties that are designated for this volume which can be adjusted from the **Details** panel.

| Property | Description |
| --- | --- |
| **Terminal Velocity** | Determines the Terminal Velocity of Pawns using CharacterMovement when falling. |
| **Priority** | Determines which PhysicsVolume takes precedence if they overlap. |
| **Fluid Friction** | Determines the amount of friction applied by the volume as Pawns using CharacterMovement move through it. The higher this value, the harder it will feel to move through the volume. |
| **Water Volume** | Determines if the volume contains a fluid, like water. |
| **Physics on Contact** | Determines if the Actor is affected by the volume by touching it (by Default, an Actor must be inside the volume for it to affect them). |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)
