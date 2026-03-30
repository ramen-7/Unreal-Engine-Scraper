<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeRotator?application_version=5.7 -->

# MakeRotator

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
7. MakeRotator

# MakeRotator

MakeRotator (v1)

On this page

### Description

MakeRotator (v1)

Make a Rotator

Input(s) :
Pitch - Rotation around the right axis (around Y axis), Looking up and down (0=Straight Ahead, +Up, -Down)
Yaw - Rotation around the up axis (around Z axis), Turning around (0=Forward, +Right, -Left)
Roll - Rotation around the forward axis (around X axis), Tilting your head, (0=Straight, +Clockwise, -CCW)

Output(s):
Rotator - Rotator output

### Information

|  |  |
| --- | --- |
| Module | [GeometryCollectionNodes](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes) |
| Category | Generators|Transform |
| Type | [FMakeRotatorDataflowNode](/documentation/en-us/unreal-engine/API/Plugins/GeometryCollectionNodes/FMakeRotatorDataflowNode) |

### Inputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Pitch | Rotation around the right axis (around Y axis), Looking up and down (0=Straight Ahead, +Up, -Down) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Yaw | Rotation around the up axis (around Z axis), Turning around (0=Forward, +Right, -Left) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |
| Roll | Rotation around the forward axis (around X axis), Tilting your head, (0=Straight, +Clockwise, -CCW) | [float](/documentation/en-us/unreal-engine/API/Runtime/uLangCore) | 0.000000 |

### Outputs

| Name | Description | Permitted Types | Default Value |
| --- | --- | --- | --- |
| Rotator | Rotator output | [FRotator](/documentation/en-us/unreal-engine/API/Runtime/Core) |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Description](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeRotator?application_version=5.7#description)
* [Information](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeRotator?application_version=5.7#information)
* [Inputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeRotator?application_version=5.7#inputs)
* [Outputs](/documentation/en-us/unreal-engine/node-reference/Dataflow/MakeRotator?application_version=5.7#outputs)
