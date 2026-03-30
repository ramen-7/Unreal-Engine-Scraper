<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/pain-causing-volume-actor-in-unreal-engine?application_version=5.7 -->

# Pain-Causing Volume Actor

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
8. Pain-Causing Volume Actor

# Pain-Causing Volume Actor

Pain-Causing Volume reference details

![Pain-Causing Volume Actor](https://dev.epicgames.com/community/api/documentation/image/6ce7af47-c7a8-4245-8ee6-88ecee943d44?resizing_type=fill&width=1920&height=335)

In addition to the properties that can be assigned from a Physics Volume, the Pain Causing Volume also has its own set of specific properties outlined below.

| Property | Description |
| --- | --- |
| **Pain Causing** | Whether the volume currently causes damage or not. |
| **Damage Per Sec** | Damage done per second to the Actors in the volume when Pain Causing is enabled. |
| **Damage Type** | This determines the type of damage done to the Actor. |
| **Pain Interval** | This is the amount of time, in seconds, between applied damage when Pain Causing is enabled. |
| **Entry Pain** | Determines whether or not damage will be applied immediately upon entering the volume, assuming that **Pain Causing** is enabled. This damage is in addition to the recurring damage applied based on the **Pain Interval**. |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)
