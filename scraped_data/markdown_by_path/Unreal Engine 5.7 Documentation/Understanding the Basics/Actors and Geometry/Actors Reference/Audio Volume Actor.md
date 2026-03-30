<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/audio-volume-actor-in-unreal-engine?application_version=5.7 -->

# Audio Volume Actor

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
8. Audio Volume Actor

# Audio Volume Actor

Audio Volume reference details

![Audio Volume Actor](https://dev.epicgames.com/community/api/documentation/image/5fff0a7f-fb5c-4f74-b44c-b6ffe233678a?resizing_type=fill&width=1920&height=335)

Several properties can be adjusted from the **Details** panel on this volume to allow for more control over its effects as seen below.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/27a57d29-946c-4210-9ff9-9062419139eb/audiovolume.png)

| Property | Description |
| --- | --- |
| **Priority** | In the event of overlapping volumes, the highest priority volume will be used. The order is undefined if two or more overlapping volumes have the same priority. |
| **Apply Reverb** | Determines if the reverb settings should be used. |
| **Reverb Effect** | This is the reverb asset to use for the volume. |
| **Volume** | This is the overall volume level of the reverb effect. |
| **Fade Time** | This is the time (in seconds) to fade from the current reverb settings into the volumes setting. |
| **Enabled** | Determines whether the volume is currently enabled and is able to affect sounds. |

**Ambient Zone Settings** define how Sound Actors located inside the associated Audio Volume will be altered by the Player's location. The Ambient Zone Settings can be adjusted from the **Details** panel.

| Property | Description |
| --- | --- |
| **Exterior Volume** | The final volume of exterior sounds when the player is inside the volume. |
| **Exterior Time** | Time to fade to new exterior volume in seconds. |
| **Exterior LPF** | Lowpass Filter multiplier applied to exterior sounds when inside (1.0 to apply the maximum LPF). |
| **Exterior LPFTime** | Time to fade to new Lowpass Filter level in seconds. |
| **Interior Volume** | The final volume of interior sounds when the player is outside the volume. |
| **Interior Time** | Time to fade to new interior volume in seconds. |
| **Interior LPF** | Lowpass Filter multiplier applied to interior sounds when outside (1.0 to apply the maximum LPF). |
| **Interior LPFTime** | Time to fade to new Lowpass Filter level in seconds. |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)
