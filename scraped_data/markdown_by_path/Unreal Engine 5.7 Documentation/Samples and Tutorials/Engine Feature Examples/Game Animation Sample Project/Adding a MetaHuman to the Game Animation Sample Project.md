<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/adding-a-metahuman-to-the-game-animation-sample-project-in-unreal-engine?application_version=5.7 -->

# Adding a MetaHuman to the Game Animation Sample Project

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
5. [Samples and Tutorials](/documentation/en-us/unreal-engine/samples-and-tutorials-for-unreal-engine "Samples and Tutorials")
6. [Engine Feature Examples](/documentation/en-us/unreal-engine/engine-feature-examples-for-unreal-engine "Engine Feature Examples")
7. [Game Animation Sample Project](/documentation/en-us/unreal-engine/game-animation-sample-project-in-unreal-engine "Game Animation Sample Project")
8. Adding a MetaHuman to the Game Animation Sample Project

# Adding a MetaHuman to the Game Animation Sample Project

How to add a MetaHuman to the Game Animation Sample project.

On this page

The [Game Animation Sample Project](https://dev.epicgames.com/documentation/en-us/unreal-engine/game-animation-sample-project-in-unreal-engine) is an example project that you can download to access a suite of motion capture animations, and learn how to use Motion Matching in Unreal Engine. The project contains a sample MetaHuman, with preview meshes for all MetaHuman body types, that you can enable in the Game Utility Widget, to observe how the system functions when using a MetaHuman character. This example project exemplifies the premiere example for using a MetaHuman as the player character, with a high-fidelity animation system.

We also recommend you try adding and implementing your own MetaHuman character to observe how the system functions for your own character. You can use the following documentation to learn how to add and implement your own MetaHuman character to the Game Animation Sample Project.

#### Prerequisites

* You have downloaded and created a new project using the Game Animation Sample Project template. For more information about setting up the Game Animation Sample project for the first time, see the [Game Animation Sample Project](https://dev.epicgames.com/documentation/en-us/unreal-engine/game-animation-sample-project-in-unreal-engine) documentation.
* You have a MetaHuman character you would like to implement in the Game Animation Sample Project. For more information about creating and adding a MetaHuman to an Unreal Engine project, see the following documentation:

  + [MetaHuman Creator](https://dev.epicgames.com/documentation/en-us/metahuman/metahuman-creator?application_version=5.6)
  + [MetaHuman Animator](https://dev.epicgames.com/documentation/en-us/metahuman/metahuman-animator?application_version=5.6)
  + [Animation](https://dev.epicgames.com/documentation/en-us/metahuman/animation?application_version=5.6)

## Implementing your MetaHuman

1. Navigate in the Content Browser to `Content/Blueprints/RetargetedCharacters`.

[![ImageAltText](https://dev.epicgames.com/community/api/documentation/image/382bc4ee-7c0b-40c7-a9d1-51fed069567a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/382bc4ee-7c0b-40c7-a9d1-51fed069567a?resizing_type=fit)

1. Locate the `CBP_SandboxCharacter_Metahuman_Kellan` Character Blueprint, and duplicate the asset by right-clicking the asset and navigate to the Duplicate option in the Context Menu.

[![ImageAltText](https://dev.epicgames.com/community/api/documentation/image/10cc903d-3453-4319-bc3f-80a739997467?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/10cc903d-3453-4319-bc3f-80a739997467?resizing_type=fit)

1. Open your new duplicated Character Blueprint.
2. In the Blueprint Editor’s components panel, select the **Body** Skeletal Mesh Component and all of its Child Components, and the **LODSync** component, and delete them using the delete key, or by right-clicking the selected components and selecting **Delete** from the context menu.

[![ImageAltText](https://dev.epicgames.com/community/api/documentation/image/b0290523-c8d1-4989-b353-eec94c9acf50?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b0290523-c8d1-4989-b353-eec94c9acf50?resizing_type=fit)

1. Open the MetaHuman Blueprint that you would like to add as a player in the Game Animation Sample Project. In this example workflow Danielle is used.
2. Select the Body including the child components and the LODSync component again, right-click the selected components, and select **Copy** from the context menu.

[![ImageAltText](https://dev.epicgames.com/community/api/documentation/image/e11f9735-2d59-45b9-a52f-001c7f4358cb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e11f9735-2d59-45b9-a52f-001c7f4358cb?resizing_type=fit)

1. Back in the Character Blueprint and paste the components onto the existing Mesh component, by selecting and right-clicking the Mesh Component, and selecting the **Paste** option in the context menu.

[![ImageAltText](https://dev.epicgames.com/community/api/documentation/image/1520d4b5-9349-4c62-baec-b88411065ed5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1520d4b5-9349-4c62-baec-b88411065ed5?resizing_type=fit)

1. Reparent the Body Mesh Component to the Blueprint Mesh Component, by selecting and dragging the Body onto the Mesh in the **Components** panel.

[![ImageAltText](https://dev.epicgames.com/community/api/documentation/image/d9e21cee-c902-49d4-9c08-5838e71f6b34?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d9e21cee-c902-49d4-9c08-5838e71f6b34?resizing_type=fit)

1. Select the Body component to open its **Details** panel, and then navigate to the **Anim Class** property and select the `ABP_GenericRetarget AnimBP` animation blueprint.

[![ImageAltText](https://dev.epicgames.com/community/api/documentation/image/339116d7-9108-4d4a-88c2-56ac310fc64b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/339116d7-9108-4d4a-88c2-56ac310fc64b?resizing_type=fit)

1. Additionally, you will need to let the Retarget AnimBP know about the new body type, by adding a tag to the Body Mesh Component. In the **Details** panel, navigate to the Component tags property, and add a new element to the array using (**+**) **Add**. Then using the array’s text field, input the following tag:

`RTG_UEFN_to_Metahuman_nrw`

[![ImageAltText](https://dev.epicgames.com/community/api/documentation/image/32cfa873-c638-4c9c-a4c1-09b6a98ebf6f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/32cfa873-c638-4c9c-a4c1-09b6a98ebf6f?resizing_type=fit)

1. Open the **Viewport** panel within the Blueprint Editor.

[![ImageAltText](https://dev.epicgames.com/community/api/documentation/image/1eee781e-960b-49fe-8a46-732ab043ced2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1eee781e-960b-49fe-8a46-732ab043ced2?resizing_type=fit)

1. Align the MetaHumans Mesh with the capsule component, by selecting the Body component, and transforming the mesh down so their feet match with the Capsule’s button, and Rotate the MetaHuman so it faces the arrow in forward direction.

[![ImageAltText](https://dev.epicgames.com/community/api/documentation/image/c9c06506-226f-4a3d-8271-2f4fcb45d68d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c9c06506-226f-4a3d-8271-2f4fcb45d68d?resizing_type=fit)

1. Next you will need to repair the Construction Script. Open the Construction Script by selecting it in the **My Blueprint** panel, then re-add the Feet, Legs, and Torso get reference variables, by dragging each component into the graph, so that each Enable Master Pose node has a definition.

[![ImageAltText](https://dev.epicgames.com/community/api/documentation/image/deeb6872-183a-46d7-8786-8a7089669a82?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/deeb6872-183a-46d7-8786-8a7089669a82?resizing_type=fit)

1. Then open the `EnableMasterPose` function in the **My Blueprint** panel in order to rebind the Body reference variable. Drag the **Body** Mesh Component into the graph, and connect its output pin to the **Ne****w Leader Bone Component** pin of the existing **Set Leader Pose Component** node.

[![ImageAltText](https://dev.epicgames.com/community/api/documentation/image/16a0c503-06e4-4212-b3ef-05e045b0123e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/16a0c503-06e4-4212-b3ef-05e045b0123e?resizing_type=fit)

1. After setting and connecting your Skeletal Mesh Component reference variables, **Save** and **Compile** your Character Blueprint.

## Add Your Character to the Game Animation Widget

1. Open the Game Animation Widget asset, which can be found in the **Content** > **Widgets** folder path.
2. In the Widget Editor’s **Designer** panel, copy one of the character tiles and paste it right next to the last one on the right.

[![ImageAltText](https://dev.epicgames.com/community/api/documentation/image/713de9b1-c13f-4c21-8c78-02f42b63cf55?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/713de9b1-c13f-4c21-8c78-02f42b63cf55?resizing_type=fit)

1. Select your new Tile to open its **Details** panel, and then in the Object property, select the **Character Blueprint** that you created using the asset selection menu.

[![ImageAltText](https://dev.epicgames.com/community/api/documentation/image/098662e6-a4ad-418a-af3d-4edeb1c048c4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/098662e6-a4ad-418a-af3d-4edeb1c048c4?resizing_type=fit)

1. Finally **Save** and **Compile** the Game Animation Widget.

You can now play the project using PIE and use your new button in the Game Animation Widget to swap the player to be your new MetaHuman character, using the project’s animation system.

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [motion matching](https://dev.epicgames.com/community/search?query=motion%20matching)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisites](/documentation/en-us/unreal-engine/adding-a-metahuman-to-the-game-animation-sample-project-in-unreal-engine?application_version=5.7#prerequisites)
* [Implementing your MetaHuman](/documentation/en-us/unreal-engine/adding-a-metahuman-to-the-game-animation-sample-project-in-unreal-engine?application_version=5.7#implementing-your-meta-human)
* [Add Your Character to the Game Animation Widget](/documentation/en-us/unreal-engine/adding-a-metahuman-to-the-game-animation-sample-project-in-unreal-engine?application_version=5.7#add-your-character-to-the-game-animation-widget)
