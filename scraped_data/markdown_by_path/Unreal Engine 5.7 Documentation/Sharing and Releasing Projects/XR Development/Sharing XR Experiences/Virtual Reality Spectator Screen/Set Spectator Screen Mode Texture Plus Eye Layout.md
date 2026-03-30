<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/set-spectator-screen-mode-texture-plus-eye-layout-in-unreal-engine?application_version=5.7 -->

# Set Spectator Screen Mode Texture Plus Eye Layout

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
5. [Sharing and Releasing Projects](/documentation/en-us/unreal-engine/sharing-and-releasing-projects-for-unreal-engine "Sharing and Releasing Projects")
6. [XR Development](/documentation/en-us/unreal-engine/developing-for-xr-experiences-in-unreal-engine "XR Development")
7. [Sharing XR Experiences](/documentation/en-us/unreal-engine/sharing-xr-experiences-in-unreal-engine "Sharing XR Experiences")
8. [Virtual Reality Spectator Screen](/documentation/en-us/unreal-engine/virtual-reality-spectator-screen-in-unreal-engine "Virtual Reality Spectator Screen")
9. Set Spectator Screen Mode Texture Plus Eye Layout

# Set Spectator Screen Mode Texture Plus Eye Layout

This node sets up the layout for the TexturePlusEye function in ESpectatorScreenMode.

![Set Spectator Screen Mode Texture Plus Eye Layout](https://dev.epicgames.com/community/api/documentation/image/ec99f5ab-c86f-4b3a-a020-0b5852d2518a?resizing_type=fill&width=1920&height=335)

[![](https://dev.epicgames.com/community/api/documentation/image/f9613dbd-e740-454a-8207-16568e8247ce?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f9613dbd-e740-454a-8207-16568e8247ce?resizing_type=fit)

This node sets up the layout for the `TexturePlusEye` function in `ESpectatorScreenMode`.

**Inputs**

| Pin Location | Name | Description |
| --- | --- | --- |
|  | (In) Exec | Input execution pin. |
|  | Eye Rect Min | A Vector 2D Structure, setting the minimum position of the screen rectangle that the Eye will be drawn in.  Values are normalized between `0.0` and `1.0`. |
|  | Eye Rect Max | A Vector 2D Structure, setting the maximum position of the screen rectangle that the Eye will be drawn in.  Values are normalized between `0.0` and `1.0`. |
|  | Texture Rect Min | A Vector 2D Structure, setting the minimum position of the screen rectangle that the Texture will be drawn in.  Values are normalized between `0.0` and `1.0`. |
|  | Texture Rect Max | A Vector 2D Structure, setting the maximum position of the screen rectangle that the Texture will be drawn in.  Values are normalized between `0.0` and `1.0`. |
|  | Draw Eye First | If this flag is set to `True`, the Eye is drawn before the Texture; however, if this flag is set to false, the Texture will be drawn before the Eye. |
|  | Clear Black | If this flag is set to `True`, the Render Target will be drawn black before either rectangle is drawn. |

**Output**

| Pin Location | Name | Description |
| --- | --- | --- |
|  | (Out) Exec | Output execution pin. |

* [vr](https://dev.epicgames.com/community/search?query=vr)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)
