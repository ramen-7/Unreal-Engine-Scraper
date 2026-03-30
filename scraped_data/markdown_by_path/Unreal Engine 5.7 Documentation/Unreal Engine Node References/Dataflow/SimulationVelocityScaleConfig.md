<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationVelocityScaleConfig?application_version=5.7 -->

# SimulationVelocityScaleConfig

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
5. [Unreal Engine Node References](/documentation/en-us/unreal-engine/node-reference "Unreal Engine Node References")
6. [Dataflow](/documentation/en-us/unreal-engine/node-reference/Dataflow "Dataflow")
7. SimulationVelocityScaleConfig

# SimulationVelocityScaleConfig

SimulationVelocityScaleConfig (v1) Velocity scale properties configuration node.

On this page

### Description

SimulationVelocityScaleConfig (v1)

Velocity scale properties configuration node.

### Information

|  |  |
| --- | --- |
| Module | [ChaosClothAssetDataflowNodes](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes) |
| Category | Cloth |
| Tags | Cloth Simulation Velocity Scale Config |
| Type | [FChaosClothAssetSimulationVelocityScaleConfigNode](/documentation/en-us/unreal-engine/API/Plugins/ChaosClothAssetDataflowNodes/FChaosClothAsset-_34) |

### Parameters

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| VelocityScaleSpace | All vector properties on this node (e.g., Linear Velocity Scale, Max Linear Acceleration) will be evaluated in this space. | [EChaosSoftsSimulationSpace](/documentation/en-us/unreal-engine/API/Runtime/Chaos/EChaosSoftsSimulationSpace) | ReferenceBoneSpace |
| LinearVelocityScale | The amount of linear velocities sent to the local cloth space from the reference bone (the closest bone to the root on which the cloth section has been skinned, or the root itself if the cloth isn't skinned). This value will be clamped by "Max Velocity Scale". A velocity scale of > 1 will amplify the velocities from the reference bone. | [FVector3f](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=0.750000,Y=0.750000,Z=0.750000) |
| bEnableLinearVelocityClamping | Enable linear velocity clamping. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| MaxLinearVelocity | The maximum amount of linear velocity sent to the local cloth space from the reference bone (the closest bone to the root on which the cloth section has been skinned, or the root itself if the cloth isn't skinned). | [FVector3f](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=1000.000000,Y=1000.000000,Z=1000.000000) |
| bEnableLinearAccelerationClamping | Enable linear acceleration clamping. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| MaxLinearAcceleration | The maximum amount of linear acceleration sent to the local cloth space from the reference bone (the closest bone to the root on which the cloth section has been skinned, or the root itself if the cloth isn't skinned). | [FVector3f](/documentation/en-us/unreal-engine/API/Runtime/Core) | (X=60000.000000,Y=60000.000000,Z=60000.000000) |
| AngularVelocityScale | The amount of angular velocities sent to the local cloth space from the reference bone (the closest bone to the root on which the cloth section has been skinned, or the root itself if the cloth isn't skinned). This value will be clamped by "Max Velocity Scale". A velocity scale of > 1 will amplify the velocities from the reference bone. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.750000 |
| bEnableAngularVelocityClamping | Enable angular velocity clamping. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| MaxAngularVelocity | The maximum amount of angular velocity sent to the local cloth space from the reference bone (the closest bone to the root on which the cloth section has been skinned, or the root itself if the cloth isn't skinned). | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 200.000000 |
| bEnableAngularAccelerationClamping | Enable angular acceleration clamping. | [bool](/documentation/en-us/unreal-engine/API/Runtime/Core) | False |
| MaxAngularAcceleration | The maximum amount of angular acceleration sent to the local cloth space from the reference bone (the closest bone to the root on which the cloth section has been skinned, or the root itself if the cloth isn't skinned). | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 12000.000000 |
| MaxVelocityScale | Clamp on Linear and Angular Velocity Scale. The final velocity scale (e.g., including contributions from blueprints) will be clamped to this value. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |
| FictitiousAngularScale | The portion of the angular velocity that is used to calculate the strength of all fictitious forces (e.g. centrifugal force). This parameter is only having an effect on the portion of the reference bone's angular velocity that has been removed from the simulation via the Angular Velocity Scale parameter. This means it has no effect when AngularVelocityScale is set to 1 and Angular Velocity and Acceleration clamps are disabled, in which case the cloth is simulated with full world space angular velocities and subjected to the true physical world inertial forces. Values range from 0 to 2, with 0 showing no centrifugal effect, 1 full centrifugal effect, and 2 an overdriven centrifugal effect. | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 1.000000 |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) | () |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Collection |  | [FManagedArrayCollection](/documentation/en-us/unreal-engine/API/Runtime/Chaos/FManagedArrayCollection) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationVelocityScaleConfig?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationVelocityScaleConfig?application_version=5.7#information)
* [Parameters](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationVelocityScaleConfig?application_version=5.7#parameters)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationVelocityScaleConfig?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/SimulationVelocityScaleConfig?application_version=5.7#outputs)
