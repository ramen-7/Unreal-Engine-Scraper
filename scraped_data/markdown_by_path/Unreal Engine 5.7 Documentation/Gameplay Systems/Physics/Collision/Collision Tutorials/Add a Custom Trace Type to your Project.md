<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/add-a-custom-trace-type-to-your-project-in-unreal-engine?application_version=5.7 -->

# Add a Custom Trace Type to your Project

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
7. [Collision](/documentation/en-us/unreal-engine/collision-in-unreal-engine "Collision")
8. [Collision Tutorials](/documentation/en-us/unreal-engine/collision-tutorials-in-unreal-engine "Collision Tutorials")
9. Add a Custom Trace Type to your Project

# Add a Custom Trace Type to your Project

Content guide to creating and setting up collision geometry.

![Add a Custom Trace Type to your Project](https://dev.epicgames.com/community/api/documentation/image/cabdf0a2-edb2-4864-b15c-741b391f374b?resizing_type=fill&width=1920&height=335)

 On this page

Often you will find a need for more than just the two default **Trace Response** channels (Visibility and Camera), perhaps you have a special laser that needs to pass through a special opaque object that you can't see through or have the camera clip through. When you encounter a situation like this you can add your own custom **Trace Response** channels by following the steps below.

## Steps

1. Open your project settings: **Edit Menu** -> **Project Settings**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e90e5a9d-d939-4664-9569-bb24dc225171/col-project-settings-1.png)
2. Under **Engine** select **Collision**:

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/00d4f1ca-cd62-47bf-b81a-219ed867a01a/col-project-settings-2.png)
3. Click the **New Trace Channel...** button. Name your new **Trace Channel** and set its **Default Response**. Click the **Accept** button.

   The **Default Response** can be **Block**, **Overlap**, or **Ignore**. Depending on your use case you'll want to choose carefully to prevent as much additional work adjusting collision profiles on your Actors.
4. Any **Blueprints** open in the **Blueprint Editor** will have to be closed down and re-opened for the new Trace Channel to appear on any components or nodes.

## Result

You'll now have a new Trace Channel to use anywhere in the editor. Any Actors or Components you want to be able to Trace with your new Channel will have to be set to block the new Channel.

* [collision](https://dev.epicgames.com/community/search?query=collision)
* [physics](https://dev.epicgames.com/community/search?query=physics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/add-a-custom-trace-type-to-your-project-in-unreal-engine?application_version=5.7#steps)
* [Result](/documentation/en-us/unreal-engine/add-a-custom-trace-type-to-your-project-in-unreal-engine?application_version=5.7#result)
