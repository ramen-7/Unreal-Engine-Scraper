<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-11-add-footstep-sounds-to-a-character?application_version=5.7 -->

# Add Footstep Sounds to a Character

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
5. [Get Started](/documentation/en-us/unreal-engine/get-started "Get Started")
6. [Unreal Engine for New Users](/documentation/en-us/unreal-engine/unreal-engine-for-new-users "Unreal Engine for New Users")
7. [Art Pass for a Puzzle Adventure Game](/documentation/en-us/unreal-engine/art-pass-for-a-puzzle-adventure-game "Art Pass for a Puzzle Adventure Game")
8. Add Footstep Sounds to a Character

# Add Footstep Sounds to a Character

Make a character produce different step sounds as they move across different surfaces.

![Add Footstep Sounds to a Character](https://dev.epicgames.com/community/api/documentation/image/6256176b-6ff9-4e3c-9cfb-f52a6ec56044?resizing_type=fill&width=1920&height=335)

 On this page

In this section, you’ll add footstep sounds to the player character to add to the realism of running around the level. You will use **Sound Cues** to create different sounds based on the type of surface that the player walks on.

You’ll create **Physical Materials** to represent the surface types. For instance, walking on metal should sound different from walking on stone. You will also create a custom Data Asset that holds the surface and sound information. Using a Data Asset makes it easier to add more surface types and sounds in the future, without modifying the Blueprint code.

Lastly, you’ll create a **Function** in the **Blueprint Function Library** that you already have in the game – **BPL\_FPGame**. 
This function will, in turn, call a function inside the Data Asset that returns the correct sound effect based on the surface type detected.

## Before You Begin

Make sure you understand these topics covered in the previous sections of the **[Art Pass for a Puzzle Adventure Game](https://dev.epicgames.com/documentation/en-us/unreal-engine/art-pass-for-a-puzzle-adventure-game)** and [Unreal Engine for New Users](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-for-new-users):

* Creating Sound Cue and Sound Attenuation assets.
* Blueprint basics, including creating variables and functions, and creating and connecting nodes.

You’ll work with the following assets in the [sample project and content pack](https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-your-project-in-unreal-engine?application_version=5.5):

* **S\_Metal-1** Sound Wave
* **S\_Metal-2** Sound Wave
* **S\_Metal-3** Sound Wave
* **S\_Stone-1** Sound Wave
* **S\_Stone-2** Sound Wave
* **S\_Stone-3** Sound Wave
* **S\_DefaultStep-1** Sound Wave
* **S\_DefaultStep-2** Sound Wave
* **S\_DefaultStep-3** Sound Wave
* **BPL\_FPGame** Blueprint Function Library
* **BP\_AdventureCharacter** Blueprint
* **ABP\_Unarmed** Animation Blueprint

## Create Sound Cues with Footstep Sounds

First, you’ll create two Sound Cues, one for footsteps on metal and one for footsteps on stone.

To create a Sound Cue, follow these steps:

1. Go to the **Content Browser** and navigate to the **AdventureGame > Artist > Audio.**
2. Right-click in the **Audio**folder, select **New Folder**, and name it **Footsteps**.
3. In the **Footsteps** folder, right-click and go to **Audio > Sound Cue**. Name this **SC\_Footsteps\_Metal** and open it. There is already an Output node in this asset, which plays the sound based on the nodes that are connected to it.
4. Right-click anywhere in the graph and add a **Wave Player** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/b4a7a43a-e4f8-4fa1-80c7-1827aab8ae90?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b4a7a43a-e4f8-4fa1-80c7-1827aab8ae90?resizing_type=fit)
5. Select the **Wave Player** node and use the panel on the left side to change the **Sound Wave** to **S\_Metal-1**.

   [![](https://dev.epicgames.com/community/api/documentation/image/22e4e34a-cfce-40f7-af4d-8dfdf0d7a1fa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/22e4e34a-cfce-40f7-af4d-8dfdf0d7a1fa?resizing_type=fit)
6. Add two more **Wave Player** nodes and repeat the steps for them to select the **S\_Metal-2** and **S\_Metal-3** Sound Wave files you imported in [Set Up Your Project and Import Content](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-01-project-setup-and-content-import).
7. Right-click in the graph and add a **Random** node. Click **Add input** in the **Random node** once to add a third input.
8. Connect each **Wave Player** node to a pin on the **Random** node.
9. Connect the **Random** node to the **Output** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/20d5e89d-765a-443a-92d0-339b06a05a93?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/20d5e89d-765a-443a-92d0-339b06a05a93?resizing_type=fit)
10. Save the Sound Cue.

Next, create two **Sound Cue** assets, one that randomizes the stone footstep sounds, and one for the default footstep sounds:

1. Create a **Sound Cue** asset named **SC\_Footsteps\_Stone**.
2. For the **Wave Player** nodes, use the 
   **S\_Stone**-******1** , **S\_Stone-2**, and 
   **S\_Stone**-3**** audio assets you imported in [Set Up Your Project and Import Content](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-01-project-setup-and-content-import).

   [![](https://dev.epicgames.com/community/api/documentation/image/aaca62cd-3ee2-47a8-af75-d3f22b387ac6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/aaca62cd-3ee2-47a8-af75-d3f22b387ac6?resizing_type=fit)
3. Create a **Sound Cue** asset named **SC\_Footsteps\_Default**.
4. For the **Wave Player** nodes, use the **S\_Default-1, S\_Default-2,** and **S\_Default-3** audio assets.

   [![](https://dev.epicgames.com/community/api/documentation/image/7c2ad45e-ccb8-4b31-8da2-7f30d7cf92cd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7c2ad45e-ccb8-4b31-8da2-7f30d7cf92cd?resizing_type=fit)

## Create Physical Materials

Now that you have created your Sound Cues, you will create two [Physical Materials](https://dev.epicgames.com/documentation/en-us/unreal-engine/physical-materials-in-unreal-engine)to represent each surface type. You’ll later match the footstep sounds to these physical materials.

A **Physical Material** is used to define the response of a physical object when interacting dynamically with the world. These material can also be used to identify different types of surfaces during gameplay.

For example, in this tutorial, you’ll create Physical Materials named **PM\_Metal** and **PM\_Stone** to represent metal and stone surfaces. You’ll then check which surface the player is walking on, and play a Sound Cue based on that information.

To create a Physical Material, follow these steps:

1. Go to the **Content Browser** and navigate to the **AdventureGame > Artist > Materials** folder.
2. In the **Materials** folder, right-click, go to **Physics**, and select **Physical Material**.
3. In the **Pick Physical Material Class** window, select **PhysicalMaterial**, and click Select.
4. Name this asset **PM\_Metal**.
5. Create one more Physical Material named **PM\_Stone**.

A Physical Material is a **data asset** that you can use to change various settings for a surface, like friction. For these Physical Materials, you don’t have to edit the properties in the assets themselves. Instead, you’ll assign these assets to different materials to change their individual surface types.

## Assign Footstep Sounds With a Data Asset Blueprint Class

Next, you’ll create a new **Blueprint Data Asset** class to hold the footstep sounds and create a function that returns the correct footstep sound based on the Physical Material assigned to the material of an object.

To set up a Blueprint Data Asset to control your footstep sounds, follow these steps:

1. In the **Content Browser**, navigate to the **AdventureGame > Artist > Audio > Footsteps** folder.
2. Right-click and create a **Blueprint Class**.
3. In the **Pick Parent Class** window, expand the **All Classes** dropdown and search for, then select **PrimaryDataAsset**.
4. Name this asset **BP\_DA\_FootSteps** and open it.
5. In the **My Blueprint** panel, add a new variable:

   1. Name it **FootStepSounds**.
   2. Select it, and in the **Details** panel:

      1. Change the **Variable Type** to **Physical Material (Object Reference)**.
      2. Change the **Container** to **Map**.
      3. Change the **Map Value Type** to **Sound Cue (Object Reference)**.

         The default Variable Type is boolean. Since you can’t map booleans, the **Map** container will not be available if you don't change the Variable Type first.

         [![](https://dev.epicgames.com/community/api/documentation/image/f699fa2b-58f3-435d-8418-a0656b45ad71?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f699fa2b-58f3-435d-8418-a0656b45ad71?resizing_type=fit)
6. Add another variable:

   1. Name it **DefaultFootSteps**.
   2. Change its type to **Sound Cue**.

      Since there is only one Sound Cue for the default footstep sound, and it’ll only play if there is no Physical Material assigned to the object's material, you can change its container type to a single variable.

      [![](https://dev.epicgames.com/community/api/documentation/image/84358840-335b-4c94-b345-f3eef986f056?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/84358840-335b-4c94-b345-f3eef986f056?resizing_type=fit)

A map variable is a data-pair list that links one type of asset to another. The FootStepSounds variable maps each Physical Material to its corresponding Sound Cue.

To set up FootStepSounds to link materials with sounds, follow these steps:

1. **Compile** the blueprint so you can edit your variables’ default values.
2. Select the **FootStepSounds** variable. In the **Details** panel, under **Default Value**, add a new element.
3. In the Physical Material field, select the **PM\_Stone** asset.
4. In the Sound Cue field, select the **SC\_Footsteps\_Default** asset.
5. Repeat the steps above to add an element with **PM\_Metal** and **SC\_Footsteps\_Metal** assigned.

   [![](https://dev.epicgames.com/community/api/documentation/image/1911d32c-2a95-47ec-a462-fa60eca06136?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1911d32c-2a95-47ec-a462-fa60eca06136?resizing_type=fit)
6. Select the **FootStepSounds** variable. In the **Details** panel, under **Default Value**, add **SC\_Footsteps\_Default**.

To build the blueprint logic, follow these steps:

1. In the **My Blueprint** panel, add a new **Function** named **fnGetFootStepSounds**. It opens in a new tab with its own graph.
2. Select the function and, using the **Details** panel, do the following:

   1. Add a new **Input** named **PhysicalMaterial** with the type **Physical Material**.
   2. Add a new **Output** named **SoundCue** with the type set to **Sound Cue**.

      [![](https://dev.epicgames.com/community/api/documentation/image/706ba9e9-95d1-4639-b606-a58dd23057a5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/706ba9e9-95d1-4639-b606-a58dd23057a5?resizing_type=fit)
   3. In the graph, disconnect the wire between the function entry node (**fnGetFootStepSounds**) and **Return Node**.
3. In the function graph, drag the **FootStepSounds** variable into the function graph and select **Get**.
4. Drag the **Foot Step Sounds** node’s pin and add a **Find** node.
5. From the **Find** node, connect the second input pin to the **fnGetFootStepSounds** node’s **Physical Material** pin. This is the parameter for the input you added earlier.

   [![](https://dev.epicgames.com/community/api/documentation/image/6e2760d5-c75f-40f9-b086-aa6ec704cc38?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6e2760d5-c75f-40f9-b086-aa6ec704cc38?resizing_type=fit)
6. On the **fnGetFootStepSounds** node, drag its **exec** pin and add a **Branch** node. Connect the **Condition** pin to the **Find** node’s bottom (red) output pin.

   [![](https://dev.epicgames.com/community/api/documentation/image/59814042-6b79-4f0a-8d5e-2b5d43cff3b3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/59814042-6b79-4f0a-8d5e-2b5d43cff3b3?resizing_type=fit)
7. From the **Branch** node, connect the **True** pin to the **Return** **Node**.
8. From the **Return** node, drag the **Sound Cue** pin and connect it to the **Find** node’s top (blue) output pin.

   [![](https://dev.epicgames.com/community/api/documentation/image/847b17d7-0d58-480b-b5f1-28e7385e65b5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/847b17d7-0d58-480b-b5f1-28e7385e65b5?resizing_type=fit)
9. From the **Branch** node, drag the **False** pin and add another **Return** **Node**.
10. On the new **Return Node**, drag off the **Sound** **Cue** pin and add a **Get Default** **Foot Steps** node.

    [![](https://dev.epicgames.com/community/api/documentation/image/5cead15d-ac65-4835-b552-05569e0faee3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5cead15d-ac65-4835-b552-05569e0faee3?resizing_type=fit)
11. **Compile** and **Save** the blueprint.

This function checks if a Physical Material (function input) is found in the FootStepSounds Map. If the Physical Material is found, it returns the Sound Cue associated with that Physical Material as the function's output variable.

If no Physical Material is found, the DefautlFootSteps Sound Cue is returned instead.

## Set the Default Footstep Sounds

Next, you’ll create a Data Asset to manage the values used by your Blueprint. This asset acts as a configuration layer, allowing you to add, remove, or update the Physical Materials and Sound Cues without modifying or recompiling the Blueprint. Follow these steps:

1. In the **Content Browser**, navigate to the **AdventureGame > Artist > Audio > Footsteps** folder.
2. Right-click and go to **Miscellaneous > Data Asset**. (Select the Data Asset type with a circular icon.)

   [![](https://dev.epicgames.com/community/api/documentation/image/5ea815d3-57ac-4ab5-9dca-4b53d120e545?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5ea815d3-57ac-4ab5-9dca-4b53d120e545?resizing_type=fit)
3. Select the **BP\_DA\_FootSteps** data class as the data asset instance.
4. Name this asset **DA\_FootSteps** and open it.
5. For **Default Foot Steps**, select **SC\_Footsteps\_Default**.
6. Expand **Foot Step Sounds** and ensure the list is populated with both **FootStepSounds** map elements.

   [![](https://dev.epicgames.com/community/api/documentation/image/0f087745-1b8d-4fa9-9c89-65769718d426?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0f087745-1b8d-4fa9-9c89-65769718d426?resizing_type=fit)
7. Save the Data Asset.

## Build a Function to Play Footstep Sounds

Next, you’ll create a function in the function library to play the footstep sound. Any blueprint class in your project can use functions in a blueprint function library.

To create and set up a new function, follow these steps:

1. In the **Content** **Browser**, go to **AdventureGame > Designer > Blueprints > Core**, and open the **BPL\_FPGame** blueprint function library.
2. In the **My Blueprint** panel, add a new function and name it **fnBPLPlayFootStepSound**.
3. Select the new function and in the **Details** panel, add a new **Input** named **PlayerReference** of the type **Pawn**.

   [![](https://dev.epicgames.com/community/api/documentation/image/7213067a-59a8-4129-a0ec-7be9fc5fc28c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7213067a-59a8-4129-a0ec-7be9fc5fc28c?resizing_type=fit)

To set up a line trace between the player and the ground, follow these steps:

1. Drag off the **fnBPLPlayFootStepSound** node’s **exec** pin and add a **Line** **Trace By Channel** node.
2. From the **Line Trace By Channel** node, drag the **Start** pin and add a **Get Actor Location** node.

   In the Node Actions list, remember to disable **Context Sensitive** if you have trouble finding a node.
3. Drag the **Get Actor Location** node’s **Target** pin and add a **Get Player** **Reference** node.
4. Drag the **Get Player Reference** node’s output pin and add a **Make Array** node.
5. Connect the **Make Array** node’s array output pin to the **Line Trace By Channel** node’s **Actors to Ignore** pin.

   [![](https://dev.epicgames.com/community/api/documentation/image/4f1d3bd6-9b5d-412f-aa7e-ae1b96f28a83?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4f1d3bd6-9b5d-412f-aa7e-ae1b96f28a83?resizing_type=fit)
6. From the **Get Actor Location** node, drag the **Return Value** pin and add a **Subtract** node.
7. Connect the **Subtract** node’s output pin to the **Line Trace By Channel** node’s **End** pin.
8. In the **Subtract** node, set the **Z** value to **500**.

[![](https://dev.epicgames.com/community/api/documentation/image/8ddef844-5883-47dd-831d-9c2015cae78d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8ddef844-5883-47dd-831d-9c2015cae78d?resizing_type=fit)

This traces a line starting from the player’s position downwards by 500 units, ignoring the player character. In the next part, you will assign the correct footstep sound based on the surface type reported by the line trace.

Follow these steps to use the Data Asset you created earlier to assign the right footstep sound:

1. From the **Line Trace By Channel** node, drag the **Out Hit** pin and select **Break Hit Results**.
2. Create a local variable, name it **FootStepsAsset** and set its type to **BP\_DA\_FootSteps (Object Reference)**. Set its **Default Value** to **DA\_FootSteps**.

   [![](https://dev.epicgames.com/community/api/documentation/image/2e991b09-951c-4825-8b2f-27fdbe1fcc3b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2e991b09-951c-4825-8b2f-27fdbe1fcc3b?resizing_type=fit)
3. Drag the **FootStepsAsset** variable to the **Event Graph** and selected **Get FootStepAsset**.
4. Drag from the FootStepsAsset node and search for then select **fnGetFootStepSounds**.
5. Connect the **Exec** pin of the **LineTraceByChannel** node to the **FnGetFootStepSounds** node. Expand the **Break Hit Results** node and connect the **Phys Ma**t pin to the **Physical Material** pin of the **FnGetFootStepSounds** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/d35c680f-9eb4-4497-bc65-f5ef5f1d0d5a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d35c680f-9eb4-4497-bc65-f5ef5f1d0d5a?resizing_type=fit)
6. Drag from the **FnGetFootStepSounds** node and search for then select **Play Sound At Location**.
7. Connect the PlaySoundAtLocation node’s **Sound** pin to the **Sound Cue** pin of the **FnGetFootStepSounds** node.
8. Drag the **Location** pin of the **PlaySoundAtLocation** node and search for then select **Get Actor Location**. Drag its **Target** pin and add a **Get Player Reference** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/56ce0b26-9f45-433e-b4c7-f3ba15938a80?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/56ce0b26-9f45-433e-b4c7-f3ba15938a80?resizing_type=fit)
9. **Save** and **Compile** the function.

This uses the Data Asset function **fnGetFootStepSounds** to pass in a Physical Material and get a Sound Cue to play.

## Update the Animation Blueprint with Step Sounds

The next step is to modify your player character’s **Animation Blueprint** to call the **FnBPLPlayFootStepSound**function  when each foot of the character touches on the ground.

Most **Manny** characters, like the one used in this project, use animations that include **Notifications** by default. **Animation Notifications** (also known as **Animation Notifies** or just **Notifies**) provide a way for you to create repeatable events synchronized with **Animation Sequences**. These events can be sounds (such as footsteps for walk or run animations), spawning particles, and more.

While Notifies can be added to an Animation Sequence, most locomotion animations that comes with the Unreal Engine templates, come with default Animation Notifies that match when the character's feet touch the ground (FootPlant).

Follow these steps to see the default Animation Notifies:

1. In the **Content** **Browser**, open the animation blueprint that your player character uses. For **BP\_AdventureCharacter** in the sample project, go to **Content > Characters > Mannequins > Anims > Unarmed**, and open **ABP\_Unarmed**.
2. In the top-right corner, click the **Animation** button (green running human icon). This opens one of the blueprint’s animations in a new tab in Unreal Editor.
3. To change the animation that’s playing, click the three dots next to the Animation button, and select any walk or run animation. For example, **MF\_Unarmed\_Jog\_Fwd**.

   Tip: You can also open the jog animation directly from the **Content Browser**.

In the timeline, you’ll see the footplant Notifies:

[![](https://dev.epicgames.com/community/api/documentation/image/aca301e4-e96e-45e4-9ec1-b1f95e9c6cb6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/aca301e4-e96e-45e4-9ec1-b1f95e9c6cb6?resizing_type=fit)

You can add new Notifies and change existing ones to craft your own system where you would like to execute a chain of events. For this tutorial, you’ll use the **default Notifies** that come with the character’s animations. They are called **AN\_FootPlant\_Right** and **AN\_FootPlant\_Left**.

To add the animation’s Notifies to the blueprint and play the footstep sounds, follow these steps:

1. Go back to **ABP\_Unarmed.**
2. Right-click in the **Event Graph** and add an **AnimNotify\_AN\_FootPlant\_Left** node.
3. Drag from the **Notify** node’s pin and search for then select **FnBPLPlayFootStepSound**.
4. Add an **AnimNotify\_AN\_FootPlant\_Right** node and connect it to the **FnBPLPlayFootStepSound** node’s **exec** input pin.
5. From the **FnBPLPlayFootStepSound** node, drag the **Player Reference** pin and add a **Get Player Pawn** node.
6. **Compile** and **Save** the animation blueprint.

[![](https://dev.epicgames.com/community/api/documentation/image/f0e731d2-2d2c-48c3-81a6-dc040dc57e0e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f0e731d2-2d2c-48c3-81a6-dc040dc57e0e?resizing_type=fit)

This will play the footstep sound each time the foot plant notify triggers from the animation blueprint.

If your character uses additional animation blueprints, then you have to add the code to those animation BPs as well.

[![](https://dev.epicgames.com/community/api/documentation/image/91eb6c75-adae-4304-a88b-fbaf744c1011?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/91eb6c75-adae-4304-a88b-fbaf744c1011?resizing_type=fit)

## Update the Player Character Blueprint to Play Footstep Sounds

Next, you’ll modify the player blueprint and add logic to play the sound when the player lands on the ground, such as landing after falling or jumping. Since you created the FnBPLPlayFootStepSound function in the blueprint function library, you can reuse that function in the player character’s blueprint.

To modify the player blueprint, follow these steps:

1. Open the **Content Browser** and navigate to the **AdventureGame > Designer > Blueprints > Characters** folder.
2. Open the **BP\_AdventureCharacter**blueprint and go to the **EventGraph** tab.
3. Right-click an empty area of the graph and add an **Event On Landed** node.
4. Drag the 
   EventOnLanded node’s **exec** pin and search for then select **FnBPLPlayFootStepSound**.
5. From the **FnBPLPla FootStepSound** node, drag the **Player Reference** pin and add a **Self** node.
6. **Compile** and **Save** the blueprint.

[![](https://dev.epicgames.com/community/api/documentation/image/60046619-256b-4cc3-8272-169389376620?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/60046619-256b-4cc3-8272-169389376620?resizing_type=fit)

## Assign Floors a Physical Material

Next, you’ll assign a Physical Material to multiple surfaces. Follow these steps:

1. Select a surface in the level, like a **Floor** object.
2. In the **Details** panel, under the **Collision** section, change the **Phys Material** **Override** to one of the Physical Materials that you created earlier.

   [![](https://dev.epicgames.com/community/api/documentation/image/b3d54c1f-1d9a-47dc-8bcf-c36e339503e3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b3d54c1f-1d9a-47dc-8bcf-c36e339503e3?resizing_type=fit)
3. Repeat these steps to add both Physical Material types to some of your level’s floors.

Alternatively, you can add a Physical Material to a Material Instance by doing the following:

1. Open the Material Instance and go to the **Details** panel.
2. Scroll down to the **General** section, click the **Phys Material** dropdown and select your desired Physical Material.
3. Save your Material Instance.

   [![](https://dev.epicgames.com/community/api/documentation/image/d4a8e675-00b1-4537-b3fe-94652a0c2852?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d4a8e675-00b1-4537-b3fe-94652a0c2852?resizing_type=fit)

## Test Your Footsteps

Play the game and walk over the surfaces with physical materials and jump to hear the correct footstep sounds.

If the surface has a Physical Material assigned, you will hear the corresponding foot step sound. If no Physical Material is found, you will hear the default foot step sound.

## Next Up

In the next module you will learn how to create a fire effect visual effect and apply it to your fire traps by using the Niagara VFX system.

* [![Add Visual Effects to Your Game](https://dev.epicgames.com/community/api/documentation/image/97f8e7ce-a1bb-4489-8a34-6ea0d7884299?resizing_type=fit&width=640&height=640)

  Add Visual Effects to Your Game

  Add visual effects to your game!](https://dev.epicgames.com/documentation/en-us/unreal-engine/at12-adding-visual-effects-to-your-game)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Before You Begin](/documentation/en-us/unreal-engine/artist-11-add-footstep-sounds-to-a-character?application_version=5.7#beforeyoubegin)
* [Create Sound Cues with Footstep Sounds](/documentation/en-us/unreal-engine/artist-11-add-footstep-sounds-to-a-character?application_version=5.7#createsoundcueswithfootstepsounds)
* [Create Physical Materials](/documentation/en-us/unreal-engine/artist-11-add-footstep-sounds-to-a-character?application_version=5.7#createphysicalmaterials)
* [Assign Footstep Sounds With a Data Asset Blueprint Class](/documentation/en-us/unreal-engine/artist-11-add-footstep-sounds-to-a-character?application_version=5.7#assignfootstepsoundswithadataassetblueprintclass)
* [Set the Default Footstep Sounds](/documentation/en-us/unreal-engine/artist-11-add-footstep-sounds-to-a-character?application_version=5.7#setthedefaultfootstepsounds)
* [Build a Function to Play Footstep Sounds](/documentation/en-us/unreal-engine/artist-11-add-footstep-sounds-to-a-character?application_version=5.7#buildafunctiontoplayfootstepsounds)
* [Update the Animation Blueprint with Step Sounds](/documentation/en-us/unreal-engine/artist-11-add-footstep-sounds-to-a-character?application_version=5.7#updatetheanimationblueprintwithstepsounds)
* [Update the Player Character Blueprint to Play Footstep Sounds](/documentation/en-us/unreal-engine/artist-11-add-footstep-sounds-to-a-character?application_version=5.7#updatetheplayercharacterblueprinttoplayfootstepsounds)
* [Assign Floors a Physical Material](/documentation/en-us/unreal-engine/artist-11-add-footstep-sounds-to-a-character?application_version=5.7#assignfloorsaphysicalmaterial)
* [Test Your Footsteps](/documentation/en-us/unreal-engine/artist-11-add-footstep-sounds-to-a-character?application_version=5.7#testyourfootsteps)
* [Next Up](/documentation/en-us/unreal-engine/artist-11-add-footstep-sounds-to-a-character?application_version=5.7#nextup)

Related documents

[Sound Sources

![Sound Sources](https://dev.epicgames.com/community/api/documentation/image/49e98eb3-8208-45d6-9b3b-39d305efdc4d?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/sound-sources-in-unreal-engine)

[Art Pass for a Puzzle Adventure Game](/documentation/en-us/unreal-engine/art-pass-for-a-puzzle-adventure-game)

[Design a Puzzle Adventure

![Design a Puzzle Adventure](https://dev.epicgames.com/community/api/documentation/image/a7b7ff2c-23d0-47a0-8a04-e569209942b0?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine)
