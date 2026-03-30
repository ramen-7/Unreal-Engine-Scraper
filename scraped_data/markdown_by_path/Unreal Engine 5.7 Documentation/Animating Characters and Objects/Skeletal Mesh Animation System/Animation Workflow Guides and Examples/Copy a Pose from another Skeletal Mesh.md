<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/copy-a-pose-in-unreal-engine?application_version=5.7 -->

# Copy a Pose from another Skeletal Mesh

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
5. [Animating Characters and Objects](/documentation/en-us/unreal-engine/animating-characters-and-objects-in-unreal-engine "Animating Characters and Objects")
6. [Skeletal Mesh Animation System](/documentation/en-us/unreal-engine/skeletal-mesh-animation-system-in-unreal-engine "Skeletal Mesh Animation System")
7. [Animation Workflow Guides and Examples](/documentation/en-us/unreal-engine/animation-workflow-guides-and-examples-in-unreal-engine "Animation Workflow Guides and Examples")
8. Copy a Pose from another Skeletal Mesh

# Copy a Pose from another Skeletal Mesh

Shows how you can copy the pose from one Skeletal Mesh to another Skeletal Mesh using the Copy Pose From Mesh Animation Blueprint node.

![Copy a Pose from another Skeletal Mesh](https://dev.epicgames.com/community/api/documentation/image/48720b6b-44ac-4039-a97c-48c5c180c485?resizing_type=fill&width=1920&height=335)

 On this page

When working with animated characters, there may be times when you want to apply the same animation data to an entirely different character. Using the **Copy Pose From Mesh** Animation Blueprint node and a little bit of Blueprint Visual Scripting, you can reference a Skeletal Mesh Component and copy whatever pose is being used to another Animation Blueprint for a different Skeletal Mesh.

In this how-to, we use the Copy Pose From Mesh node to copy the player's animations onto another Skeletal Mesh.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/680da96e-d841-44fb-8d94-1e48e2cd96c5/copyposefrommesh.png)

## Steps

1. In the **Content/ThirdPersonBP/Blueprints** folder, duplicate the **ThirdPersonCharacter** Blueprint using the default name.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b6f0a562-a1bc-4159-bcaf-570d887f4193/copypose_1.png)
2. In the **Content/Mannequin/Character/Mesh** folder, right-click the **SK\_Mannequin** and under **Create**, select **Anim Blueprint** and use the default naming convention.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0da1d292-bf96-42fc-810b-6daef30df6a8/copypose_2.png)
3. Open the **ThirdPersonCharacter1** Blueprint from Step 1 and delete all the nodes in the **Event Graph**.
4. Select the **Mesh** in the **Components** window, and then in the **Details** panel, set the **Anim Class** to **UE4\_Mannequin\_Skeleton\_AnimBlueprint**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fd0ce9e7-0ac3-489e-a764-6ddf6b537d94/copypose_3-1.png)
5. Open the **UE4\_Mannequin\_Skeleton\_AnimBlueprint**, and in the **Anim Graph**, add the **Copy Pose From Mesh** node and connect it to the **Final Animation Pose**, then promote the **Source Mesh Component** to a variable called **Character Reference**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dc5aadf0-6ee3-4db5-8c1c-4e5b401dd790/copypose_5.png)

   The Character Reference variable will refer to the Skeletal Mesh Component of the character we specify.
6. Inside **ThirdPersonCharacter1** Blueprint, create a variable called **Character Reference** and set the **Variable Type** to **Third Person Character**, then enable **Instance Editable**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e16e1ccb-0b2c-4e63-9aa2-99c740f04648/copypose_6.png)
7. Drag the **ThirdPersonCharacter1** Blueprint into the level, then in its **Details** panel, assign the **ThirdPersonCharacter** from the level as the **Character Reference** variable.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fc22aa25-8e9a-4094-a25f-8ff24ede2c62/copypose_7.png)

   By assigning the value here, we will have a reference to the character whose Skeletal Mesh Component we want to copy (in this case, the Player).
8. Open the **UE4\_Mannequin\_Skeleton\_AnimBlueprint** and on the **Event Graph** use a **Try Get Pawn Owner** node to **Cast to ThirdPersonCharacter1**, then off the **As Third Person Character 1** pin, get the **Character Reference** variable.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8467920d-a2d3-4455-9704-7da5b28705d2/copypose_8.png)
9. Off the **Character Reference** node, add the **Get Mesh** node and set the **Character Reference** variable inside the Animation Blueprint.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d00a6fc2-46d0-4506-9014-15a6c1a94964/copypose_9.png)

   The Skeletal Mesh from the Player will now be copied and assigned to the Character Reference inside this Animation Blueprint, driving the character's pose.
10. From the Main Toolbar, **Play** in the Editor.

## End Result

When you play in the Editor, the non-playable character will play the same animations as your player character.

As you move around, the other character in the level will copy your animation pose even though that character has no logic or State Machine driving the different poses. While this example copies the player, it is possible to set up a non-playable character (NPC) with AI and a State Machine driving animations, then have another NPC that has no logic copy the pose through the Copy Pose From Mesh node to mimic the same behavior and logic.

When using the Copy Pose From Mesh node, in the **Details** panel, you can enable **Use Attached Parent** which will look for an attached parent and use it as the source if the Source Mesh Component is not valid.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c47fb3da-82cc-48af-b2be-32d7c7cebe81/copyposedetails.png)

Also, you can **Copy Curves** in addition to Bone Transforms, which will copy the curves that exist in the current Skeleton. If the curve list has changed, it will require the animation system to be reinitialized.

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [animation blueprint](https://dev.epicgames.com/community/search?query=animation%20blueprint)
* [copy pose](https://dev.epicgames.com/community/search?query=copy%20pose)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Steps](/documentation/en-us/unreal-engine/copy-a-pose-in-unreal-engine?application_version=5.7#steps)
* [End Result](/documentation/en-us/unreal-engine/copy-a-pose-in-unreal-engine?application_version=5.7#endresult)
