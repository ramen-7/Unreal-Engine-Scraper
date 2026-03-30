<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/testing-physics-assets-in-unreal-engine?application_version=5.7 -->

# Testing Physics Assets

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
7. [Physics Asset Editor](/documentation/en-us/unreal-engine/physics-asset-editor-in-unreal-engine "Physics Asset Editor")
8. [Physics Asset Editor Tutorials](/documentation/en-us/unreal-engine/physics-asset-editor-tutorial-directory-for-unreal-engine "Physics Asset Editor Tutorials")
9. Testing Physics Assets

# Testing Physics Assets

This tutorial covers the basics for testing your Physics Assets in the Physics Asset Editor.

![Testing Physics Assets](https://dev.epicgames.com/community/api/documentation/image/cdc05d79-3397-442a-839d-8cfde8197319?resizing_type=fill&width=1920&height=335)

 On this page

This page covers the basics of testing a **Physics Asset** in the **Physics Asset Tool**.

## Testing

![Testing](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4a3d1ba6-e983-4fdf-8805-9bc38de91d60/simulate-options.png)

Selecting **Simulation** from the dropdown menu under the toolbar **arrow icon** will allow you to test your Physics Asset.

![Selecting Simulation from the dropdown menu under the toolbar arrow icon will allow you to test your Physics Asset](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1a8d59bc-894f-4b9a-a92c-3fd942607027/simulation-physics-asset.png)

* When the **No Gravity** option is enabled, the entire Physics Asset is simulated but gravity is not turned on, enabling you to ctrl+click to poke the **Physics Bodies** in a zero gravity environment. This is useful for finding any interpenetrating Physics Bodies or **Limited Physics Constraints** already outside of their limits.
* You can also simulate a chain of joints by toggling on **Selected Simulation**. This option only simulates the Physics Bodies you have selected (you can select more than one) and those down the hierarchy from the selected Physics Bodies. For example, if you select the shoulder, the entire arm will be simulated.

* [physics](https://dev.epicgames.com/community/search?query=physics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Testing](/documentation/en-us/unreal-engine/testing-physics-assets-in-unreal-engine?application_version=5.7#testing)
