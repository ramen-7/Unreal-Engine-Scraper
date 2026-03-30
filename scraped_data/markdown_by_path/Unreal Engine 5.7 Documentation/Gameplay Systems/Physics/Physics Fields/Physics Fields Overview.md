<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-physics-fields-in-unreal-engine?application_version=5.7 -->

# Physics Fields Overview

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
7. [Physics Fields](/documentation/en-us/unreal-engine/physics-fields-in-unreal-engine "Physics Fields")
8. Physics Fields Overview

# Physics Fields Overview

Overview of Physics Fields in Unreal Engine

![Physics Fields Overview](https://dev.epicgames.com/community/api/documentation/image/0470f448-ff8a-4587-a529-3d383a41e26e?resizing_type=fill&width=1920&height=335)

 On this page

The **Physics Field System** enables users to directly affect **Chaos Physics** simulations at runtime on a specified region of space. These Fields can be configured to influence the physics simulation in a variety of ways, such as exerting force on rigid bodies and cloth, breaking Geometry Collection Clusters, anchoring or disabling fractured rigid bodies, and interacting with rigid body animation nodes.

In addition, the Physics Field System can communicate with other engine systems, such as Niagara and Materials. These systems can sample Physics Fields by using built-in functions that allow the evaluation of a Field at a specific location.

Fields are set up by creating a **Field System Component** Blueprint and specifying which systems are allowed to query your Field. You can configure a Field as a **World Field** to allow **Materials** and **Niagara Systems** to sample the Field. You can also configure it as a Chaos Field to allow Geometry Collections, physics objects, cloth, and rigid body animation nodes to interact with it.

Internally, Physics Fields directly affect **Chaos Particles**. Chaos Particles are defined as a point in space with various properties, such as position, velocity, and mass, that can be affected by the Chaos Physics Solver. Common examples of Chaos Particles include fractured rigid bodies from Geometry Collections, rigid bodies attached to characters, and individual vertices in cloth simulation.

## Adding a Physics Field

Once the Blueprint is created, you can add one of three types of Physics Fields - Transient, Construction, or Persistent.

**Transient Fields** are created, executed, and destroyed at runtime and are used to add a temporary effect to the physics simulation. A common example includes applying external strain or linear velocity to rigid bodies that overlap the field volume.

**Construction Fields** are created in the Construction Script of the Blueprint and store the field after each compilation. The most common example of this type of field is the Anchor Field which is used to hold Geometry Collection fractured pieces in place.

**Persistent Fields** are created and remain active until they are explicitly removed. Persistent fields are evaluated at every tick of the physics simulation. A common example is the Disable Field, which can be used to disable the fractured pieces of Geometry Collections that overlap its volume.

## Applying Physics Types

Each Field type applies to a specific **Physics Type**, such as Linear Force, External Strain, or Disabled Threshold to overlapping Chaos Particles. Each Physics Type is further categorized by type as Integer, Scalar or Vector. These categories are referenced when using the built-in functions in the Material Editor and Niagara Systems.

## Adding Meta Data

Fields can use different types of **Meta Data** to add additional information on how they should be evaluated. This Meta Data can provide filtering of the Chaos Particles according to their State (Dynamic, Static, Kinematic, Sleeping or Disabled) and the Object Type (cloth, rigid body, destruction, and character). It can also be used to set where the Physics Field will be evaluated within a rigid body, such as the center of mass or pivot point.

## Defining the Field

Each Field is defined by a Blueprint graph that connects to the **Field Node** pin of the **Add Transient Field**, **Add Construction Field**, or **Add Persistent Field** nodes. The graph defines the scope and properties of the Field.

The Blueprint graph is composed of **Field Nodes**, which are added as child components of the Field System Component. Common examples of these objects include Box and Radial Falloff, Uniform and Radial Vectors, and Field Operators, which combine overlapping Fields.

## Visualizing the Field

Persistent Physics Fields can be visualized in the level by running the appropriate console command. Click **Show > Visualize > Physics Field** inside the viewport to enable the visualization.

![Click Show - Visualize - Physics Field inside the viewport to enable the visualization](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b66a6525-51ae-4dfc-979e-3249fcd33edc/pf-overview-1.png)

Enter the following commands in the console during simulation:

| **Console Command** | **CVARS Available** | **Description** |
| --- | --- | --- |
| **r.PhysicsField.Rendering.TargetType** | \*\*1: Dynamic State  2: Linear Force  3: External Strain  4: Kill Particles  5: Linear Velocity  6: Angular Velocity  7: Angular Torque  8: Internal Strain  9: Disabled Threshold  10: Sleeping Threshold  15: Collision Group  16: Activate Disabled\*\* | Set which Physics Field target type should be displayed. |
| **r.PhysicsField.Rendering.SystemType** | \*\*0: Chaos Field  1: World Field\*\* | Set which type of Physics Field type should be displayed. |
| **r.PhysicsField.Rendering.EvalType** | \*\*0: Analytical Evaluation (precise, slower)  1: Sample the Clipmap (approximate, faster)\*\* | Set which kind of field evaluation to use. |

Please refer to the [Physics Field Reference Guide](/documentation/en-us/unreal-engine/reference-guide-for-physics-field-in-unreal-engine) for further information about the various elements mentioned on this page.

* [physics](https://dev.epicgames.com/community/search?query=physics)
* [fields](https://dev.epicgames.com/community/search?query=fields)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Adding a Physics Field](/documentation/en-us/unreal-engine/overview-of-physics-fields-in-unreal-engine?application_version=5.7#addingaphysicsfield)
* [Applying Physics Types](/documentation/en-us/unreal-engine/overview-of-physics-fields-in-unreal-engine?application_version=5.7#applyingphysicstypes)
* [Adding Meta Data](/documentation/en-us/unreal-engine/overview-of-physics-fields-in-unreal-engine?application_version=5.7#addingmetadata)
* [Defining the Field](/documentation/en-us/unreal-engine/overview-of-physics-fields-in-unreal-engine?application_version=5.7#definingthefield)
* [Visualizing the Field](/documentation/en-us/unreal-engine/overview-of-physics-fields-in-unreal-engine?application_version=5.7#visualizingthefield)
