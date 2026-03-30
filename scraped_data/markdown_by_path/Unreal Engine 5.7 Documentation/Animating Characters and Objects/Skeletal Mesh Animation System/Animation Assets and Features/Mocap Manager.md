<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/mocap-manager-in-unreal-engine?application_version=5.7 -->

# Mocap Manager

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
7. [Animation Assets and Features](/documentation/en-us/unreal-engine/animation-assets-and-features-in-unreal-engine "Animation Assets and Features")
8. Mocap Manager

# Mocap Manager

Learn how to set up and use the Mocap Manager.

On this page

This tutorial provides a complete walkthrough of Mocap Manager, part of the Performance Capture Workflow Plugin in Unreal Engine.

It covers enabling the plugin, setting up your mocap stage representation, managing performers, characters and props, recording, and reviewing takes, all in support of a full performance capture pipeline.

## Set up Mocap Manager

### Enable the Performance Capture Workflow Plugin

1. Go to **Edit** > **Plugins**.
2. Search for and enable the **Performance Capture Workflow** plugin.
3. Restart the editor when prompted.

### Open Mocap Manager

1. Go to **Window** > **Virtual Production** > **Mocap Manager**.

[![Window > Virtual Production > Mocap Manager](https://dev.epicgames.com/community/api/documentation/image/b1c3ed82-4b14-4b4e-b32a-bd8f0be55e47?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b1c3ed82-4b14-4b4e-b32a-bd8f0be55e47?resizing_type=fit)

### Create Required Assets

1. If prompted, click **Create Missing Assets**.

   [![The Create Missing Assets button](https://dev.epicgames.com/community/api/documentation/image/162a686f-c081-4dcd-9327-397de4a1c70f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/162a686f-c081-4dcd-9327-397de4a1c70f?resizing_type=fit)
2. Confirm storing them in the default folder: `Content/Pcap`.

Instead of clicking the Create Missing Assets button, you can also manually create the session and production tables. In the Content Browser, go to **Add** > **Performance Capture** > **PCap Datatable** and create one table with the Session Struct and one with the Production Struct. In **Project Settings** > **Performance Capture,** set a reference to these two new tables.

You only have to add these assets once in each project where you enable the Performance Capture workflow plugin.

[![Performance Capture Project Settings](https://dev.epicgames.com/community/api/documentation/image/7ef9740b-4757-427a-aab9-078062d214e7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7ef9740b-4757-427a-aab9-078062d214e7?resizing_type=fit)

You might also want to create your own session template to define how session folders are created. You can do this by going to **Add** > **Performance Capture** > **PCap Dataset** and choose the session template type. Alternatively you can duplicate the default session template asset and modify it to your needs (`/Plugins/PerformanceCaptureWorkflow/Core/DefaultSessionTemplate`).

## Use Mocap Manager

Mocap Manager is a centralized location for controlling what is needed during a mocap shoot. It is designed to lead you through the process linearly, from start to finish.

### Create a Session

1. In the **Create New Session** section, enter a session name and any optional notes.
2. Click **+Session**.

A folder structure is created and becomes active.

Mocap Manager can only have one active session at a time.

Navigate to your session folder at any time by clicking the **folder** icon in Mocap Manager.

[![Jump to session folder button](https://dev.epicgames.com/community/api/documentation/image/127b5123-ca9d-4924-891f-a2038c500007?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/127b5123-ca9d-4924-891f-a2038c500007?resizing_type=fit)

Productions can be used to organize larger efforts, such as separate games or cinematic deliveries, in one Unreal project. They are optional and if you do not wish to use them, the default production can be used.

Sessions represent individual capture sessions (such as a morning or afternoon shoot). When you create a session, folders and some assets used during a session are created.

Session templates allow for customization of folder structure and naming using dynamic [naming tokens](https://dev.epicgames.com/documentation/en-us/unreal-engine/BlueprintAPI/NamingTokens/GetNamingTokens?application_version=5.6).

[![A session template data asset](https://dev.epicgames.com/community/api/documentation/image/950f13cb-bf55-4f2c-af76-d81ba24c9ce3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/950f13cb-bf55-4f2c-af76-d81ba24c9ce3?resizing_type=fit)

All actors created by Mocap Manager are assigned to a data layer or sub-level for your session. Each session gets a new data layer or sub-level.

Mocap Manager checks if your currently open level is using world partition or level streaming when you create a session. In the `[SessionName]/Scenes` folder, a data layer or sub-level will be created, depending on the context of creation. This data layer or sub-level will be the edit context for your level. This means that all actors will be placed inside this context.

### Set Up the Mocap Stage in Unreal Engine

The Performance Capture workflow plugin comes with a premade default named **BP\_DemoStage**. You can duplicate and edit this BP to your needs.

The stage is spawned on a valid floor in front of the camera. Move and align it to your real-world capture space.

In the **Stage** tab of the **Mocap Manager**, you can toggle grid view and the stage ghost meshes for easier positioning to align your Unreal level to your real-world stage.

[![An example mocap stage actor](https://dev.epicgames.com/community/api/documentation/image/27600ce9-4686-464f-bed8-927ab0f2f0f3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/27600ce9-4686-464f-bed8-927ab0f2f0f3?resizing_type=fit)

When you spawn the stage, it will be added to the **Current Context** for your level.

### Motion Actor setup

In the Motion tab of Mocap Manager, you can configure Live Link subjects and create performers, props, and characters.

#### Live Link Preview

In the **LiveLink** tab, you can toggle which of your incoming Live Link subject data is displayed in the preview. The icons in the list indicate the data type: skeletal mesh, camera, or markers.

You can choose to show individual subjects or all by clicking the **Show/Hide** icon.

[![The LiveLink tab](https://dev.epicgames.com/community/api/documentation/image/1635675f-7734-40a2-a00e-c2f6bd0aa334?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1635675f-7734-40a2-a00e-c2f6bd0aa334?resizing_type=fit)

[![Live Link data in the preview](https://dev.epicgames.com/community/api/documentation/image/8d3e8d8b-48b8-49db-906a-af935f25c7ee?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8d3e8d8b-48b8-49db-906a-af935f25c7ee?resizing_type=fit)

#### Create Performers

In the **Motion** tab of Mocap Manager, click the **Performers** tab to create and spawn performers. Performers are encapsulated in a data asset called a **PCapPerformer**.

[![The Performers tab](https://dev.epicgames.com/community/api/documentation/image/68243271-1b8f-4c2e-a76b-95d4dfee373a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/68243271-1b8f-4c2e-a76b-95d4dfee373a?resizing_type=fit)

To create a performer, follow these steps:

1. In the **Create Proportioned Mesh** section of the **Performers** tab, select a **Live Link Subject**from the dropdown menu. Only subjects with the role type "animation" (skeletal data) will be listed on the dropdown.
2. Click **Launch Workflow** to launch the **Create Proportioned Mesh** viewport.

   [![The Mocap Manager Proportioned Mesh workflow](https://dev.epicgames.com/community/api/documentation/image/4b49d60a-3da4-49cf-a01c-c3abaa5c684d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4b49d60a-3da4-49cf-a01c-c3abaa5c684d?resizing_type=fit)
3. In the viewport, align the skeleton over the origin (the pelvis at (0,0)) by asking the performer to move their position until they line up.
4. Optionally, you can press pause to freeze the animation, allowing your performer to relax from holding their pose over the origin.
5. Click **Create Mess & IKRig**. This closes the **Proportioned Mesh** viewport and takes you back to the **Mocap Manager** panel.
6. Click **Create Performer** to generate the PCapPerformer data asset.

The performer will now be selectable from the **Spawn Performer** section. Click **Spawn** and the newly created skeletal mesh with Live Link data applied will spawn, parented to your Stage Root actor.

#### Create Props

In the **Motion** tab of Mocap Manager, click the **Props** tab to create props for your performers to use.

[![The Props tab](https://dev.epicgames.com/community/api/documentation/image/389ec2d0-a447-4bd3-8e7f-d07c9d4b8222?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/389ec2d0-a447-4bd3-8e7f-d07c9d4b8222?resizing_type=fit)

To create a prop, follow these steps:

1. In the **Props** tab, click **Launch Workflow** to open the **Create Prop** viewport.

   [![](https://dev.epicgames.com/community/api/documentation/image/54901a8c-19a3-4bfc-8f07-c7a13bc1085c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/54901a8c-19a3-4bfc-8f07-c7a13bc1085c?resizing_type=fit)
2. In either the **Static Mesh** or **Skeletal Mesh** dropdown menus, select a mesh for the prop.
3. In the **Subject** dropdown, select a Live Link subject.
4. In the Prop Offset section, make adjustments to align the mesh and the subject.
5. In the **Name Override** field, enter a name for the prop.
6. Click **Finalize**. This closes the **Create Prop** viewport and takes you back to the Mocap Manager panel.
7. Click **Create Prop Asset** to generate the PCapProp data asset.

You can spawn this prop into the level, same as the Performer data asset, by selecting it from the picker and clicking **Spawn Prop**.

#### Optional: Prepare a Metahuman

By default, Metahuman Blueprints are not ideal for mocap retargeting and recording because they do not use a SkeletalMeshComponent as their root component.

To prepare a Metahuman for the Mocap Manager, follow these steps:

1. Create a Blueprint derived from **CaptureCharacter**.
2. Copy the necessary skeletal mesh components and grooms from your Metahuman Blueprint into the new Blueprint.
3. Disable decals on all the components.
4. On all skeletal mesh components attached to the root, apart from the head, add a **Follow Leader Pose** node in the construction script to force these components to get their pose from the root component.
5. In the **Performance Capture** section of your Blueprint, untick **Force All Components to Follow Leader**.

If your character is not a Metahuman or does not use multiple meshes, you can directly use CaptureCharacter and assign a single skeletal mesh.

#### Create a Character

In the **Characters** tab of Mocap Manager, you can create characters for your performers to control.

[![The Character tab in Mocap Manager](https://dev.epicgames.com/community/api/documentation/image/a5a219df-a53f-40c1-b658-c31b2f14d743?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a5a219df-a53f-40c1-b658-c31b2f14d743?resizing_type=fit)

1. In the **Create New Character Asset** section, enter the following information:

   1. **Source Performer Asset**: Select the performer that will control this character.
   2. **Character Class**: Select the default **CaptureCharacter** class, unless you are using a custom Blueprint, such as the one from the Metahuman example above.
   3. Character Mesh: Assign the body skeletal mesh for the character. This is required for retargeting.
   4. **Character Name**: Enter a name for the character.
2. Click **Create Character Asset**. A character data asset is generated, storing references to the performer, retarget asset, IKRig, mesh, and CaptureCharacter class.
3. Click **Spawn Character** to spawn your character in the scene.

When you spawn your character, it will be attached to the Stage Root actor.

#### Tune Retarget

Click the **retarget tuner** button on a character in Mocap Manager to open the **Retarget Settings** window. In this window, you can modify retarget properties on each bone chain. Retarget tuner is designed to work only with Humanoid Bipeds, as its chains are named specifically to match those created by auto IKRig scripts.

[![The retarget tuner button, and the Retarget Settings window.](https://dev.epicgames.com/community/api/documentation/image/2bd252cf-00f3-4fde-9b62-2fae37fcd1de?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2bd252cf-00f3-4fde-9b62-2fae37fcd1de?resizing_type=fit)

#### Mocap Recorder

##### Create Slates

Predefine your recording names using slates with name and metadata. This also provides facility for a checklist to work through during a session.

To open the Slates tab in Mocap Manager, click the **Record** tab, then **Slates**.

[![](https://dev.epicgames.com/community/api/documentation/image/fa32845c-d054-4dcb-8956-1a64fb026897?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fa32845c-d054-4dcb-8956-1a64fb026897?resizing_type=fit)

Slates are stored in a data table. You can import updates using `.csv` files.

Click **Prep** on your chosen slate to use this name for your text recording.

##### Recording

To record mocap in Mocap Manager, follow these steps:

1. Click the Record tab, then click Mocap Recorder.

   [![The Mocap Recorder tab](https://dev.epicgames.com/community/api/documentation/image/2c097c85-88ec-4c26-8019-5e73c861b105?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2c097c85-88ec-4c26-8019-5e73c861b105?resizing_type=fit)
2. Select which actors and data to capture (performers, props, live link, audio).
3. Click **Record** to start recording. The rest of the interface locks down while recording.
4. Click **Stop** to stop recording.

#### Review Panel

Recordings are automatically logged into a **Takes Data** table.

To view your takes, follow these steps:

1. In Mocap Manager, click the **Review** tab, the click **Take View**.
2. Under **Takes Data**, double-click a take to open it.

After opening a take, you can scrub, preview, and inspect the recording. Assign a rating of 1 to 5 stars for sorting and filtering.

[![](https://dev.epicgames.com/community/api/documentation/image/f2038e31-e1c7-4049-bfa9-e5fef6144af5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f2038e31-e1c7-4049-bfa9-e5fef6144af5?resizing_type=fit)

The takes table can be exported to `.csv` for further production tracking.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Set up Mocap Manager](/documentation/en-us/unreal-engine/mocap-manager-in-unreal-engine?application_version=5.7#setupmocapmanager)
* [Enable the Performance Capture Workflow Plugin](/documentation/en-us/unreal-engine/mocap-manager-in-unreal-engine?application_version=5.7#enabletheperformancecaptureworkflowplugin)
* [Open Mocap Manager](/documentation/en-us/unreal-engine/mocap-manager-in-unreal-engine?application_version=5.7#openmocapmanager)
* [Create Required Assets](/documentation/en-us/unreal-engine/mocap-manager-in-unreal-engine?application_version=5.7#createrequiredassets)
* [Use Mocap Manager](/documentation/en-us/unreal-engine/mocap-manager-in-unreal-engine?application_version=5.7#usemocapmanager)
* [Create a Session](/documentation/en-us/unreal-engine/mocap-manager-in-unreal-engine?application_version=5.7#createasession)
* [Set Up the Mocap Stage in Unreal Engine](/documentation/en-us/unreal-engine/mocap-manager-in-unreal-engine?application_version=5.7#setupthemocapstageinunrealengine)
* [Motion Actor setup](/documentation/en-us/unreal-engine/mocap-manager-in-unreal-engine?application_version=5.7#motionactorsetup)
* [Live Link Preview](/documentation/en-us/unreal-engine/mocap-manager-in-unreal-engine?application_version=5.7#livelinkpreview)
* [Create Performers](/documentation/en-us/unreal-engine/mocap-manager-in-unreal-engine?application_version=5.7#createperformers)
* [Create Props](/documentation/en-us/unreal-engine/mocap-manager-in-unreal-engine?application_version=5.7#createprops)
* [Optional: Prepare a Metahuman](/documentation/en-us/unreal-engine/mocap-manager-in-unreal-engine?application_version=5.7#optional:prepareametahuman)
* [Create a Character](/documentation/en-us/unreal-engine/mocap-manager-in-unreal-engine?application_version=5.7#createacharacter)
* [Tune Retarget](/documentation/en-us/unreal-engine/mocap-manager-in-unreal-engine?application_version=5.7#tuneretarget)
* [Mocap Recorder](/documentation/en-us/unreal-engine/mocap-manager-in-unreal-engine?application_version=5.7#mocaprecorder)
* [Create Slates](/documentation/en-us/unreal-engine/mocap-manager-in-unreal-engine?application_version=5.7#createslates)
* [Recording](/documentation/en-us/unreal-engine/mocap-manager-in-unreal-engine?application_version=5.7#recording)
* [Review Panel](/documentation/en-us/unreal-engine/mocap-manager-in-unreal-engine?application_version=5.7#reviewpanel)
