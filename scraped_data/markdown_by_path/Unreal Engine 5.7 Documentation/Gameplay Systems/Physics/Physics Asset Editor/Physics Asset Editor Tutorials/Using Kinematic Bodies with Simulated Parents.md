<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-kinematic-bodies-with-simulated-parents-in-unreal-engine?application_version=5.7 -->

# Using Kinematic Bodies with Simulated Parents

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
9. Using Kinematic Bodies with Simulated Parents

# Using Kinematic Bodies with Simulated Parents

This tutorial covers setting up kinematic physics bodies with simulated parents.

![Using Kinematic Bodies with Simulated Parents](https://dev.epicgames.com/community/api/documentation/image/043b06e1-3c41-4436-bcfd-d951dddd89bb?resizing_type=fill&width=1920&height=335)

 On this page

The [Physics Asset Editor](/documentation/en-us/unreal-engine/physics-asset-editor-in-unreal-engine) provides several different ways in which you can simulate physics bodies including the ability to have kinematic physics bodies with simulated parents.
This enables you to define child bodies that can be driven by animation data while the parents of those bodies are driven by physics simulation data.
This can be useful if you have a character that you want to perform a physics-based reaction while playing a hanging idle or hanging traversal animation.

In this How-to, we use kinematic bodies with simulated parents to generate the effect of a character hanging from a ledge while the rest of the body is simulated with physics.

![We use kinematic bodies with simulated parents to generate the effect of a character hanging from a ledge while the rest of the body is simulated with physics](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/45ecd040-6d3f-4732-94be-73fadfe8c01a/end-result-image.png)

## Steps

For this guide, we are using the **Blueprint Third Person Template** project with **Starter Content** enabled.

1. In your project in the **Content/Mannequin/Character/Mesh** folder, open the **SK\_Mannequin\_PhysicsAsset**.

   ![Open the SKMannequinPhysicsAsset](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/eab6fa89-eccd-447e-a403-fd96d0c7b7f0/kinematic-how-to-01.png)
2. In the **Skeleton Tree** panel, hold **Ctrl** and select both the **hand\_l** and **hand\_r** bodies, then in the **Details** panel, change the **Physics Type** to **Kinematic**.

   ![Change the Physics Type to Kinematic](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f9dec76f-d853-4c90-a277-cab641cea0fd/kinematic-how-to-03.png)

   By setting these bones to Kinematic, they will not simulate physics and will follow any animation data.

   Alternatively, you can right-click bones in the hierarchy list and expand **Physics Type** in the Context Menu, then set their **Body Physics Type** to **Kinematic**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1edc5e00-cc48-4ebf-9bc1-45255daa0ff3/kinematic-how-to-04.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1edc5e00-cc48-4ebf-9bc1-45255daa0ff3/kinematic-how-to-04.png)

   This option enables you to set the **Physics Type** property for children's bodies below the current bone.
3. Click on a space within the viewport to deselect all bones, then in the **Details** panel, change the **Physics Update Mode** to **Component Transform is Kinematic**.

   ![Change the Physics Update Mode to Component Transform is Kinematic](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f6abeedc-8181-450f-b4d9-b147848529e2/kinematic-how-to-05.png)

   This option determines whether the simulation of the root body updates component transform or is kinematic.
4. From the toolbar, open the dropdown menu under the **arrow icon**, and select **Simulate**.

   ![Select Simulate](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7b6a3acb-a6af-4d1b-a1e5-cd94e8c2cc1c/kinematic-how-to-06.png)

   The character in the viewport will slump over and appear to be hanging by their hands.

   ![The character in the viewport will slump over and appear to be hanging by their hands](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/273052d6-2349-47c6-b4f8-d8e3cb3b5d04/kinematic-how-to-07.png)
5. From the toolbar, open the **Animation** dropdown menu, then select the **ThirdPersonJump\_Loop** animation.

   ![Select the ThirdPersonJumpLoop animation](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5f2ceff2-0f3c-414b-be91-37fd14375b34/kinematic-how-to-08.png)

   The hands (because they are set to kinematic) will follow the animation data contained within the **ThirdPersonJump\_Loop** motion.

   ![The hands will follow the animation data contained within the ThirdPersonJumpLoop motion](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3413766c-3458-4913-bbdf-dc4e83c84ea8/kinematic-how-to-09.png)
6. From the **Main Editor** window, drag the **SK\_Mannequin\_PhysicsAsset** into the level and then, in the **Details** panel, set **Physics Transform Update Mode** to **Component Transform is Kinematic**.

   ![Set Physics Transform Update Mode to Component Transform is Kinematic](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/51f31253-b5c3-4099-8a1f-e04ce2b47454/kinematic-how-to-10.png)
7. Select the **SkeletalMeshComponent**, then change **Animation Mode** to **Use Animation Asset** and **Anim to Play** to **ThirdPersonJump\_Loop**.

   ![Change Animation Mode to Use Animation Asset and Anim to Play to ThirdPersonJumpLoop](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d9d9b300-e089-4198-b105-83549cd7e0f5/kinematic-how-to-11.png)
8. Click the **Play** button from the toolbar to play in the editor.

## End Result

Below we've placed the character near a ledge when we run and bump into it, it reacts to physics while the hands appear slightly fixed.

While the animation we used above is not ideal, below we apply the same concept to an animation of a character hanging and traversing a ledge.

The arms and head are set to Kinematic (denoted below with Gold Boxes) while the rest is being simulated.

![The arms and head are set to Kinematic while the rest is being simulated](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2b57eadb-88a7-4fed-9736-de71e64970d9/example-setup.png)

* [physics](https://dev.epicgames.com/community/search?query=physics)
* [kinematic](https://dev.epicgames.com/community/search?query=kinematic)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/using-kinematic-bodies-with-simulated-parents-in-unreal-engine?application_version=5.7#steps)
* [End Result](/documentation/en-us/unreal-engine/using-kinematic-bodies-with-simulated-parents-in-unreal-engine?application_version=5.7#endresult)
