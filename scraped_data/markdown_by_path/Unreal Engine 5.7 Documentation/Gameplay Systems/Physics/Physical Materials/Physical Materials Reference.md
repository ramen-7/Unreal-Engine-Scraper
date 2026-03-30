<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/physical-materials-reference-for-unreal-engine?application_version=5.7 -->

# Physical Materials Reference

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
7. [Physical Materials](/documentation/en-us/unreal-engine/physical-materials-in-unreal-engine "Physical Materials")
8. Physical Materials Reference

# Physical Materials Reference

Assets applied to physically simulated primitives directly or via materials used to configure and control physical properties used by the simulation.

![Physical Materials Reference](https://dev.epicgames.com/community/api/documentation/image/d9472bfc-0f0b-4d11-ab53-8021d3c5b0f2?resizing_type=fill&width=1920&height=335)

 On this page

**Physical Materials** are used to define the response of a physical object when interacting dynamically with the world. Physical Materials are fairly easy to use. Creating one will give you a set of default values, identical to the default physical material that is applied to all physics objects. Examples of this would be a character's dead body (ragdoll), a movable crate, and so on.

## Properties

Below are the properties for Physical Materials separated by major category.

## Physical Material

This category contains the core properties of the Physics Material: Friction, Restitution, and Density.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cb901a97-b93d-43f9-9034-5532ef6d94ff/p1.png)

| Property | Description |
| --- | --- |
| **Friction** | This is the friction value of the surface, which controls how easily things can slide on this surface. |
| **Friction Combine Mode** | This property enables you to adjust how Physical Material frictions are combined. This is set to Average by default, but can be overriden using the **Override Friction Combine Mode** property.   * **Average**: Uses the average value of the touching materials: (a+b)/2 * **Min**: Uses the smaller value of the touching materials: min(a,b) * **Multiply**: Multiplies the values of the touching materials: a\*b * **Max**: Uses the larger value of the touching materials: max(a,b) |
| **Override Friction Combine Mode** | By default, the Friction Combine Mode is set to **Average**, by enabling this property you can change how Frictions are combined between touching Physical Materials. |
| **Restitution** | This is how "bouncy" the surface is, or how much energy it retains when it collides with another surface. |
| **Restitution Combine Mode** | This property enables you to adjust how Physical Material restitutions are combined. This is set to Average by default, but can be overriden using the **Override Restitution Combine Mode** property.   * **Average**: Uses the average value of the touching materials: (a+b)/2 * **Min**: Uses the smaller value of the touching materials: min(a,b) * **Multiply**: Multiplies the values of the touching materials: a\*b * **Max**: Uses the larger value of the touching materials: max(a,b) |
| **Override Restitution Combine Mode** | By default, the Restitution Combine Mode is set to **Average**, by enabling this property you can change how Restitutions are combined between touching Physical Materials. |
| **Density** | Used with the shape of the object to calculate its mass properties. The higher the number, the heavier the object. Measured as **g** per cubic **cm**. |

### Advanced

This category contains a property to change how scale affects the mass of the Actor with the Physical Material applied to it.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f3826e63-ba4c-44c1-82db-86fed404b1fb/p2.png)

| Property | Description |
| --- | --- |
| **Raise Mass To Power** | Used to adjust the way that mass increases as objects get larger. This is applied to the mass as calculated based on a "solid" object. In actuality, larger objects do not tend to be solid, and become more like "shells" (e.g. a car is not a solid piece of metal). Values are clamped to 1 or less. |

## Destruction

Properties that are specific to the Destruction system in Unreal Engine 4.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c1072603-c1a7-4b75-a374-ef1d2ad92fe1/p3.png)

| Property | Description |
| --- | --- |
| **Destructible Damage Threshold Scale** | How much to scale the damage threshold by on any destructible this Physics Material is applied to. |

## Physical Properties

Gameplay related properties for the Physical Material.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f6e9e918-27f6-4abe-8572-4c241b77036c/p4.png)

| Property | Description |
| --- | --- |
| **Surface Type** | Surface Types are set in the `DefaultEngine.ini` file for your project. They define an enum to be used in the engine for defining any number of things, from what sound plays as a character walks across a surface, to the type of decal an explosion should leave on different surfaces.  You can use ProjectSetting/Physics/Physical Surfaces  This data can be pulled in code or Blueprint:  By default, without editing the source code, you are limited to 30 Surface Types, labeled SurfaceType1 through SurfaceType30. |

## Vehicles

These properties are specific to Vehicles in Unreal Engine 4. While they may say they deal with Tires, they only do so when applied to a Vehicle (as Tire Data Types, and Wheel Blueprints, don't directly reference a Physical Material).

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/92397ba5-0120-4599-9fe6-178727a8e660/p5.png)

| Property | Description |
| --- | --- |
| **Tire Friction Scale** | Overall tire friction scalar when this Physical Material is applied to a Vehicle. This value is multiplied against the Vehicle's Wheels' specific Friction Scale values. |
| **Tire Friction Scales** | Tire friction scales for specific Wheels when this Physical Material is applied to a Vehicle. These values are multiplied against the Vehicle's Wheels' specific Friction Scale values. |

* [physics](https://dev.epicgames.com/community/search?query=physics)
* [physical materials](https://dev.epicgames.com/community/search?query=physical%20materials)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Properties](/documentation/en-us/unreal-engine/physical-materials-reference-for-unreal-engine?application_version=5.7#properties)
* [Physical Material](/documentation/en-us/unreal-engine/physical-materials-reference-for-unreal-engine?application_version=5.7#physicalmaterial)
* [Advanced](/documentation/en-us/unreal-engine/physical-materials-reference-for-unreal-engine?application_version=5.7#advanced)
* [Destruction](/documentation/en-us/unreal-engine/physical-materials-reference-for-unreal-engine?application_version=5.7#destruction)
* [Physical Properties](/documentation/en-us/unreal-engine/physical-materials-reference-for-unreal-engine?application_version=5.7#physicalproperties)
* [Vehicles](/documentation/en-us/unreal-engine/physical-materials-reference-for-unreal-engine?application_version=5.7#vehicles)
