<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/change-material-in-unreal-engine-cinematic-movie?application_version=5.7 -->

# Switching Actor Materials in Sequencer

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
6. [Cinematics and Sequencer](/documentation/en-us/unreal-engine/cinematics-and-movie-making-in-unreal-engine "Cinematics and Sequencer")
7. [Cinematic Workflow Guides and Examples](/documentation/en-us/unreal-engine/cinematic-workflow-guides-and-examples-in-unreal-engine "Cinematic Workflow Guides and Examples")
8. Switching Actor Materials in Sequencer

# Switching Actor Materials in Sequencer

How to change materials for an Actor in a Sequence.

![Switching Actor Materials in Sequencer](https://dev.epicgames.com/community/api/documentation/image/28d2a9b8-9d84-4706-937e-f1028982ceda?resizing_type=fill&width=1920&height=335)

 On this page

The **Material Element Switcher** track is a Sequencer track that you can use to animate Materials on an Actor. This enables you to change materials on an Actor by adding keys for specific materials on the track.

For this how to, we can use the Paragon Phase and Fey materials from the Epic Marketplace. You can see that we already have a Material Element Switcher for Phase's Skirt. This is so we can easily see the change in materials in contrast with the jacket.

1. Navigate to **Cinematics** > **Add Level Sequence**. Name and save the sequence, such as "MaterialAnim", and then open it from the **Content Browser**.
2. Add the Skeletal Mesh for your actor to the Viewport. Then add the mesh as a track to your sequence.
3. Under **Skeletal Mesh** Component, add a new **Track** and select a **Material Element Switcher**. You can find which material number corresponds to the element you want to change on the actor in the Skeletal Mesh animation Blueprint.

   ![selecting a specific material switcher](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/376897b2-498b-4dc1-961c-1bec9488fb32/binding1.png)

In this example, I want to change the jacket material, which is Material Element 10.

1. In the dropdown labeled **None**, select the first material for the sequence. Then, add a key for this material in the Sequence.

   ![selecting material switcher dropdown](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9d86fed4-1ae3-452e-a36a-4b54a943432f/binding7.png)
   ![choosing material](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/db899139-a58d-4387-b465-4b3631525b28/binding2.png)

In this example, we will start with **MIC\_Phase\_jacket**, which is Phase's jacket material.

1. Move the slider along the **Timeline** to where you want to change materials. Using the dropdown, select a new material and add a new key to the sequence.

   ![using M_Fey_Armor material](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c3615e21-8fba-4114-827c-c2672524699b/binding3.png)

In this example, we changed the material to the **M\_Fey\_Armours** material.

1. Repeat the previous step to add a third material.

   ![using M_Fey_Plantseed material](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0cc5913e-c0f1-42c6-88ee-48f6efb96553/binding5.png)

In this example, we change the material to the **M\_Fey\_Plantseed** material.

1. The last material change is back to Phase's original jacket material, MIC\_Phase\_jacket. Move the slider and add a key to change the material again. In this example, I change the jacket material before the skirt material changes at the end of the sequence.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/99f737de-6e05-4c6d-b14c-c96986fd32a4/binding6.png)

You can now playback the sequence and watch the materials change.

## End Result

* [materials](https://dev.epicgames.com/community/search?query=materials)
* [animation](https://dev.epicgames.com/community/search?query=animation)
* [sequencer](https://dev.epicgames.com/community/search?query=sequencer)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [End Result](/documentation/en-us/unreal-engine/change-material-in-unreal-engine-cinematic-movie?application_version=5.7#endresult)
