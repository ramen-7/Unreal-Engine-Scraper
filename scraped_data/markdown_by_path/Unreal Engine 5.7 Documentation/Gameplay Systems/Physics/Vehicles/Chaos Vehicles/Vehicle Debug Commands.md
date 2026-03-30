<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/vehicle-debug-commands-in-unreal-engine?application_version=5.7 -->

# Vehicle Debug Commands

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
8. [Chaos Vehicles](/documentation/en-us/unreal-engine/chaos-vehicles "Chaos Vehicles")
9. Vehicle Debug Commands

# Vehicle Debug Commands

Reference for Chaos Vehicle debug commands, helping users visualize the vehicle physics simulation.

![Vehicle Debug Commands](https://dev.epicgames.com/community/api/documentation/image/a7cec3da-c28a-4cdb-bcc4-97ff712819fa?resizing_type=fill&width=1920&height=335)

 On this page

**Chaos Vehicles** come with a variety of debug commands to help you visualize what is happening during the vehicle simulation. All the vehicle-specific commands start with `p.vehicle`. The commands are enabled by following them with `1`, and are disabled by following them with `0`. These commands either enable or disable vehicle physics or render debug lines in the scene.

Many of the debug rendering commands are called from the physics thread and need to be enabled with the `p.chaos.debugdraw.enabled 1` command before they can be visualized in the scene.

![Vehicle Console Debug](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/16b84cc8-24d1-492c-8384-ad5862d54e69/vehicle-console-debug.png)

p.Vehicle debug commands display in the editor command console

## Generic Commands

Generic commands apply to all vehicle types and include visualizing forces and locations, and disabling features and forces.

### Visualize Forces and Locations

| Command | Description |
| --- | --- |
| `p.Vehicle.ShowCOM` | Enables or disables the center of mass visualization. |
| `p.Vehicle.ShowModelOrigin` | Enables or disables the origin visualization. |
| `p.Vehicle.ShowAerofoilForces` | Enables or disables the aerofoil visualization. |
| `p.Vehicle.ShowAerofoilSurface` | Enables or disables the surface visualization. |
| `p.Vehicle.ShowAllForces` | Enables or disables the force visualization. |
| `p.Vehicle.SetForceDebugScaling` | Sets scaling for force visualization. If the forces are large and the lines appear too long, lower the scaling of the rendered lines by using a smaller value. |

### Disable Features and Forces

These commands will turn off specific forces in isolation to other force. This can help isolate which system is generating a particular behavior in the vehicle movement.

| Command | Description |
| --- | --- |
| `p.Vehicle.DisableSuspensionForces` | Disables suspension forces in isolation of other forces. |
| `p.Vehicle.DisableFrictionForces` | Disables wheel friction forces in isolation of other forces. |
| `p.Vehicle.DisableRollbarForces` | Disables suspension roll bar forces in isolation of other forces. |
| `p.Vehicle.DisableTorqueControl` | Disables direct torque control. |
| `p.Vehicle.DisableStabilizeControl` | Disables position stabilization control. |
| `p.Vehicle.DisableAerodynamics` | Disables aerodynamic force drag / downforce. |
| `p.Vehicle.DisableAerofoils` | Disables aerofoil forces. |
| `p.Vehicle.DisableThrusters` | Disables thruster forces. |

## Wheeled Vehicle Commands

| Command | Description |
| --- | --- |
| `p.Vehicle.ShowWheelCollisionNormal` | Shows the hit location and normal of the surface that the wheel raycast has hit. |
| `p.Vehicle.ShowSuspensionRaycasts` | Shows the suspension raycast length. The color indicates whether the ray hit something (green), or not (red). |
| `p.Vehicle.ShowSuspensionLimits` | Enables or disables the suspension limits visualization. |
| `p.Vehicle.ShowWheelForces` | Enables or disables the wheel forces visualization. |
| `p.Vehicle.ShowSuspensionForces` | Enables or disables the suspension forces visualization. |
| `p.Vehicle.ShowRaycastComponent` | Displays the name of the component the wheels are in contact with (from the raycast hit). |
| `p.Vehicle.ShowRaycastMaterial` | Displays the name of the physics material that the wheels are in contact with (from the raycast hit). |

## Vehicle Commands Overrides

| Command | Description |
| --- | --- |
| `p.Vehicle.ControlInputWakeTolerance` | Sets the threshold used by the control input to wake up the vehicle if it is sleeping. The default is 0.02. |
| `p.Vehicle.TraceTypeOverride` | Global override of the ray trace type. A value of 1 uses Simple collision, while a value of 2 uses Complex collision. |
| `p.Vehicle.SetMaxMPH` | Set a top speed override in miles per hour(affects all vehicles). Can help debug an issue or can be used in conjunction with the throttle override. |
| `p.Vehicle.ThrottleOverride` | Global override of the throttle control input (range 0 to 1). This is useful for testing the performance of many vehicles driving at once. |
| `p.Vehicle.SteeringOverride` | Global override of the steering value (range -1 to 1). This is useful for testing the performance of many vehicles driving at once, as you can set them to dre in circles over the terrain. |
| `p.Vehicle.BatchQueries` | Enable or disable batching of suspension raycasts. |
| `p.Vehicle.EnableMultithreading` | Enable or disable parallel updates of all vehicles. If a threading crash is suspected, then the vehicle manager can be switched from parallel updates to serial updates. This will simulate vehicles one at a time. |

## Vehicle Stat Commands

| Command | Description |
| --- | --- |
| `stat ChaosVehicle` | Displays timings for the different parts of the vehicle simulation. |
| `stat ChaosVehicleManager` | Displays timings for simulating all the vehicles in the scene. It also displays counters showing the number of vehicles, and the portion of vehicles currently awake or sleeping. |

## Using the Center of Mass

The location of the center of mass has a significant effect on vehicle handling. A high center of mass will cause the vehicle to roll more in corners, or dip more under acceleration and braking.

Pushing the center of mass forward will make steering less reactive since the movement arm will be longer for the rear wheels and shorter for the front wheels. This means that the lateral forces on the rear wheels will have a greater effect on the angular rotation of the vehicle compared to the front wheels.

Visualizing where the center of mass is located is one of the most useful tools for debugging vehicle behavior. A **Center Of Mass Offset** defined on the skeletal mesh can shift the center of mass position relative to the initially calculated location from the collision model. The center of mass visualization command `p.Vehicle.ShowCOM 1` displays the current center of mass position after any offset has been applied.

![Center of mass visualized](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2be628e4-7231-498d-b586-66cd334a2daf/vehicles-center-of-mass-1.png)
![Center of mass visualized](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/939e0e53-3247-4308-84a4-ceb7d7ec6a3c/vehicles-center-of-mass-2.png)

* [physics](https://dev.epicgames.com/community/search?query=physics)
* [chaos](https://dev.epicgames.com/community/search?query=chaos)
* [vehicles](https://dev.epicgames.com/community/search?query=vehicles)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Generic Commands](/documentation/en-us/unreal-engine/vehicle-debug-commands-in-unreal-engine?application_version=5.7#genericcommands)
* [Visualize Forces and Locations](/documentation/en-us/unreal-engine/vehicle-debug-commands-in-unreal-engine?application_version=5.7#visualizeforcesandlocations)
* [Disable Features and Forces](/documentation/en-us/unreal-engine/vehicle-debug-commands-in-unreal-engine?application_version=5.7#disablefeaturesandforces)
* [Wheeled Vehicle Commands](/documentation/en-us/unreal-engine/vehicle-debug-commands-in-unreal-engine?application_version=5.7#wheeledvehiclecommands)
* [Vehicle Commands Overrides](/documentation/en-us/unreal-engine/vehicle-debug-commands-in-unreal-engine?application_version=5.7#vehiclecommandsoverrides)
* [Vehicle Stat Commands](/documentation/en-us/unreal-engine/vehicle-debug-commands-in-unreal-engine?application_version=5.7#vehiclestatcommands)
* [Using the Center of Mass](/documentation/en-us/unreal-engine/vehicle-debug-commands-in-unreal-engine?application_version=5.7#usingthecenterofmass)
