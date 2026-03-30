<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/audio-modulation-quick-start-guide?application_version=5.7 -->

# Audio Modulation Quick Start Guide

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
5. [Working with Audio](/documentation/en-us/unreal-engine/working-with-audio-in-unreal-engine "Working with Audio")
6. [Audio Mixing](/documentation/en-us/unreal-engine/audio-mixing-in-unreal-engine "Audio Mixing")
7. [Audio Modulation](/documentation/en-us/unreal-engine/audio-modulation-in-unreal-engine "Audio Modulation")
8. Audio Modulation Quick Start Guide

# Audio Modulation Quick Start Guide

Quickstart guide on using audio parameter modulation in Unreal Engine.

![Audio Modulation Quick Start Guide](https://dev.epicgames.com/community/api/documentation/image/6d258d38-8e9f-4251-9d85-38382b9c56ce?resizing_type=fill&width=1920&height=335)

 On this page

## Overview

The **Audio Modulation** system provides control over common floating-point audio parameters from the **Blueprint** and **Component** systems. The system includes a better, more intuitive and dynamic subset of features for mixing audio sources, and for dynamically controlling and parameterizing audio properties than Unreal Engine had in prior versions.

In this guide, you will learn how to build a basic volume-based **Control Bus** structure for your game audio.

## Goals

Use the **Audio Modulation Plugin** to build a basic volume-based Control Bus structure for your game audio.

## Objectives

* Create a collection of Control Buses and Control Bus **Mix objects** to apply volume mixing to sound assets .
* Assign Control Buses to **MetaSound Sources** and **Sound Classes**.
* Use the **Mix Matrix Debugger** to see the current values of the Control Bus.
* Adjust a Control Bus from Blueprints.

## 1 - Required Setup

1. Create a new project and select the **Games** category and the **Third Person** template. Enter your project's location and name. Click **Create**.

   [![Create a new First Person project](https://dev.epicgames.com/community/api/documentation/image/03e1c499-5a2f-46a2-ad25-4efa0db14107?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/03e1c499-5a2f-46a2-ad25-4efa0db14107?resizing_type=fit)
2. Click **Settings > Plugins** to open the **Plugins** window.

   [![Open the Plugins window](https://dev.epicgames.com/community/api/documentation/image/067c8bcd-86bd-405f-a990-85bd964b7c06?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/067c8bcd-86bd-405f-a990-85bd964b7c06?resizing_type=fit)
3. Search for and **enable** the **Audio Modulation** and **MetaSound** plugins. Restart Unreal Engine.

   [![Open the Plugins window](https://dev.epicgames.com/community/api/documentation/image/3a6fbb29-d853-4b5e-b73e-c69ca3e1680e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3a6fbb29-d853-4b5e-b73e-c69ca3e1680e?resizing_type=fit)

### Section Results

In this section, you created a new project and enabled the Audio Modulation and MetaSound plugins. You are now ready to create the Control Buses.

## 2 - Create the Control Buses

1. In the **Content Browser**, right click and select **Audio > Modulation > Control Bus**. Name the asset `CB_Main`.

   [![Name the asset CB_Main](https://dev.epicgames.com/community/api/documentation/image/19eb5325-f0f4-4397-bb46-b40c2f20530d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/19eb5325-f0f4-4397-bb46-b40c2f20530d?resizing_type=fit)
2. Open `CB_Main` and click the **Parameter** dropdown. Click the **Gear** icon and enable the **Show Plugin Content** checkbox. You may have to select **Show Engine Content,** as the Modulation plugin is an Engine plugin.

   [![Click the Gear icon and enable the Show Plugin Content checkbox](https://dev.epicgames.com/community/api/documentation/image/711dd3ae-5afd-4777-b514-49fc54ef1600?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/711dd3ae-5afd-4777-b514-49fc54ef1600?resizing_type=fit)
3. Search for and select the **Volume** parameter (other parameters are available, e.g. frequency, pan, pitch, etc.)

   [![Search for and select the Volume parameter](https://dev.epicgames.com/community/api/documentation/image/74167a69-3e18-4c77-8e9a-12ef30923af7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/74167a69-3e18-4c77-8e9a-12ef30923af7?resizing_type=fit)

   You can create a custom parameter by right clicking in the Content Browser and selecting **Audio > Modulation > Modulation Parameter**. Then, select the `SoundModulationParameterVolume` class from the list.

   [![Image-of-options-in-the-select-parameter-class-modal](https://dev.epicgames.com/community/api/documentation/image/3d0224d9-ed3b-450f-993a-58eaa9071273?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3d0224d9-ed3b-450f-993a-58eaa9071273?resizing_type=fit)
4. Create two folders in the **Content Browser** that will contain several Control Buses meant for designers and users. In the example below, the folders are named `Buses_Designer`and `Buses_User`.

   [![Create two folders in the Content Browser](https://dev.epicgames.com/community/api/documentation/image/95a88b11-b696-46dc-9800-543a3379d99e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/95a88b11-b696-46dc-9800-543a3379d99e?resizing_type=fit)
5. Right-click on `CB_Main`and select **Duplicate**. Name the new asset `CB_Ambience`.

   [![Right-click on CB_Main and select Duplicate](https://dev.epicgames.com/community/api/documentation/image/abeb155f-e58c-4f4f-8e7b-cc6d67df53c2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/abeb155f-e58c-4f4f-8e7b-cc6d67df53c2?resizing_type=fit)
6. Repeat this process two more times and create `CB_Foley`and `CB_Footsteps`. Select all three assets and move them to the `Buses_Designer`folder.

   [![Repeat this process two more times and create CB_Foley and CB_Footsteps](https://dev.epicgames.com/community/api/documentation/image/b3e3f983-f6f9-4c63-a116-3fd15ae317a9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b3e3f983-f6f9-4c63-a116-3fd15ae317a9?resizing_type=fit)
7. Repeat the previous step and create `CB_Dialogue`, `CB_Music`, and `CB_SFX`. Move them to the `Buses_User`folder.

   [![Repeat the previous step and create CB_Dialogue, CB_Music, and CB_SFX](https://dev.epicgames.com/community/api/documentation/image/b15de332-1eda-46f7-8f67-0586162cc06d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b15de332-1eda-46f7-8f67-0586162cc06d?resizing_type=fit)

Best Practice: Do not to put the Control Bus on the sound directly, but rather give those sounds an appropriate Sound Class (e.g. an “SFX” Sound class, a “Music” sound class, etc.), and put the Control Buses on the class instead.

### Section Results

In this section, you created the main Control Bus that will modulate the volume for all assigned audio in your project. In addition, you created several Control Buses meant for the user and designer. You are now ready to assign the main Control Bus to the Master sound class in your project.

## 3 - Assign the Control Buses to Sound Assets

1. Click **Settings > Project Settings** to open the **Project Settings**.

   [![Click Settings - Project Settings to open the Project Settings](https://dev.epicgames.com/community/api/documentation/image/ec6a974d-0538-4474-9fcd-08290a20dd2c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ec6a974d-0538-4474-9fcd-08290a20dd2c?resizing_type=fit)
2. Scroll down to the **Engine** section and select the **Audio** category. Go to the **Audio** section and double click the **Master Default Sound Class** to open it.

   [![Scroll down to the Engine section and select the Audio category](https://dev.epicgames.com/community/api/documentation/image/dc0c7db7-66d7-420b-bee3-b6fa0c5e1bdc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dc0c7db7-66d7-420b-bee3-b6fa0c5e1bdc?resizing_type=fit)

   [![Double click the Master Default Sound Class to open it](https://dev.epicgames.com/community/api/documentation/image/6c61b515-ca58-4172-9c32-4c17d936365a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6c61b515-ca58-4172-9c32-4c17d936365a?resizing_type=fit)
3. In the **Details** panel, go to the **Modulation** section and enable the **Modulate** checkbox next to **Volume**.

   1. Click **+** next to **Volume Modulators** and add `CB_Main`to **Index[0]**.

   [![Go to the Modulation section and enable the Modulate checkbox next to Volume](https://dev.epicgames.com/community/api/documentation/image/58067a6a-4163-4ebe-bbd7-5e7948461e02?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/58067a6a-4163-4ebe-bbd7-5e7948461e02?resizing_type=fit)

   Add the `CB_Main` Control Bus to any additional sound classes in your project, so all sounds are mixed using the same Control Bus. The Sound Class reference hierarchy is not observed by modulation and the mix structure. Each Sound Class must list all Control Buses that are to be applied to Sound Assets referencing said Sound Class.

### Section Results

In this section, you assigned the `CB_Main` Control Bus to the Master sound class. You are now ready to create a sample MetaSound to test the mix during gameplay.

## 4 - Create a Sample MetaSound

1. In the **Content Browser**, right-click and select **Audio > MetaSound Source**. Name the asset `MS_Sample`.

   [![Name the asset MS_Sample](https://dev.epicgames.com/community/api/documentation/image/01ac246d-b562-4832-ba12-82bb50b1c615?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/01ac246d-b562-4832-ba12-82bb50b1c615?resizing_type=fit)
2. Open `MS_Sample`by double-clicking it in the **Content Browser**.

   1. Go to the **Interfaces** panel on the left and click the **remove** icon next to **UE.Source.OneShot** to remove it.
   2. Right-click in the **Event Graph** and search for then select **Wave Player (Mono)**.
   3. Connect the **Input** node to the **Play** pin of the **Wave Player** node.
   4. Connect the **Out Mono** pin of the **Wave Player** node to the **Output** node.

   [![Click the remove icon next to UE.Source.OneShot)](https://dev.epicgames.com/community/api/documentation/image/7f38a979-8808-4e85-8b60-47be392c570c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7f38a979-8808-4e85-8b60-47be392c570c?resizing_type=fit)

   [![Right-click in the Event Graph and search for then select Wave Player (Mono)](https://dev.epicgames.com/community/api/documentation/image/b0e74f68-75f2-41ff-ab62-bf05f81a1da7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b0e74f68-75f2-41ff-ab62-bf05f81a1da7?resizing_type=fit)

   [![Connect the Out Mono pin of the Wave Player node to the Output node](https://dev.epicgames.com/community/api/documentation/image/68796a85-1c61-477b-aa27-f61c7b7e9b28?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/68796a85-1c61-477b-aa27-f61c7b7e9b28?resizing_type=fit)
3. Click the **Wave Asset** dropdown and select a sound asset. In this example, **EndPlayInEditor** was selected.

   1. Enable the **Loop** checkbox.

   [![Click the Wave Asset dropdown and select a sound asset](https://dev.epicgames.com/community/api/documentation/image/59c37946-392e-44fb-9ae0-23d7df207c3d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/59c37946-392e-44fb-9ae0-23d7df207c3d?resizing_type=fit)
4. Click **Source** on the toolbar and scroll down to the **Details** panel.

   1. Expand the **Modulation** category.
   2. Click the **Volume Routing** dropdown and select **Union**.
   3. Enable the **Modulate** checkbox next to **Volume**.
   4. Click **+** next to **Volume Modulators** and add `CB_SFX`to **Index[0]**.

   [![Click Source on the toolbar and scroll down to the Details panel](https://dev.epicgames.com/community/api/documentation/image/80715a61-203b-4436-b474-62d09386a92d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/80715a61-203b-4436-b474-62d09386a92d?resizing_type=fit)

   [![Click the Volume Routing dropdown and select Union](https://dev.epicgames.com/community/api/documentation/image/010377fd-1a7c-43ce-b979-9c61aefbac13?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/010377fd-1a7c-43ce-b979-9c61aefbac13?resizing_type=fit)
5. Drag `MS_Sample`to your level.

   [![Drag MS_Sample to your level](https://dev.epicgames.com/community/api/documentation/image/572a1bd0-af43-472a-8122-6ddfa2d4567d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/572a1bd0-af43-472a-8122-6ddfa2d4567d?resizing_type=fit)

### Section Results

In this section, you create a simple MetaSound that will play a sound asset continuously. You are now ready to apply the Control Bus Mix to the Control Buses.

## 5 - Apply a Mix

In this section, you will create a **Control Bus Mix** and apply it to all **Control Buses** in the `Buses_User`folder. You can follow these steps to create a Control Bus Mix for all Control Buses in the `Buses_Designer` folder as well. In addition, there is no strict rule as to what can be included in a mix.

Multiple mixes can be activated and applied to a single or group of Control Buses. However, only a single instance of a given mix can be active at a time.

1. In the **Content Browser**, right-click and select **Audio > Modulation > Control Bus Mix**. Name the asset `CM_User`.

   [![Name the asset CM_User](https://dev.epicgames.com/community/api/documentation/image/4d91b00a-d4b8-4146-b097-28912ed14466?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4d91b00a-d4b8-4146-b097-28912ed14466?resizing_type=fit)
2. Open CM\_User and go to the Mix Stages section.

   1. Click **+** next to **Mix Stages** to add a new mix.
   2. Click the **Bus** dropdown and select `CB_Dialogue`.

   [![Click the Bus dropdown and select CB_Dialogue](https://dev.epicgames.com/community/api/documentation/image/d54b3c52-3211-4ff6-a9a1-df72b0c6484c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d54b3c52-3211-4ff6-a9a1-df72b0c6484c?resizing_type=fit)
3. Repeat the previous step and add `CB_Music`and `CB_SFX`to the **Mix Stages**.

   [![Repeat the previous step and add CB_Music and CB_SFX to the Mix Stages](https://dev.epicgames.com/community/api/documentation/image/13475a73-7474-437f-bf4f-aa38147c9ca9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/13475a73-7474-437f-bf4f-aa38147c9ca9?resizing_type=fit)
4. Press **Play** to enter runtime.

   1. Press **Shift-F1** to regain control of your mouse.
   2. Go to `CM_User`and click **Activate Mix**.
   3. Change the value of `CB_SFX`to see the changes applied in real time.

   [![Go to CM_User and click Activate Mix](https://dev.epicgames.com/community/api/documentation/image/93f79d3c-d15a-4eac-b1a2-7a482e7d94b7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/93f79d3c-d15a-4eac-b1a2-7a482e7d94b7?resizing_type=fit)

   [![Change the value of CB_SFX to see the changes applied in real time](https://dev.epicgames.com/community/api/documentation/image/308ebf46-119c-4d26-b9e6-863d4ad8d434?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/308ebf46-119c-4d26-b9e6-863d4ad8d434?resizing_type=fit)

### Section Results

In this section, you created and applied the `CM_User` **Control Mix** to the Control Buses in your project. You also activated the mix during gameplay and changed the volume of sounds using the `CB_SFX`Control Bus.

## 6 - Debug a Mix

1. During gameplay, press **~** to open the **console** window.

   1. Enter the following command: `au.Debug.Modulation.Enable.Matrix 1` to enable Sound Modulation debugging.

   [![Enter the following command: au.Debug.Modulation.Enable.Matrix 1](https://dev.epicgames.com/community/api/documentation/image/d1d56478-8376-4e9a-8d53-4ef7c4fc501f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d1d56478-8376-4e9a-8d53-4ef7c4fc501f?resizing_type=fit)
2. You can filter the list of Control Buses and Control Mixes displayed by entering the commands: `au.Debug.Modulation.Filter.Buses [substring]` and `au.Debug.Modulation.Filter.Mixes [substring]`.

   [![You can filter the list of Control Buses and Control Mixes displayed by entering the appropriate commands](https://dev.epicgames.com/community/api/documentation/image/b688e5c0-bb71-41d9-98d3-d003d04bc231?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b688e5c0-bb71-41d9-98d3-d003d04bc231?resizing_type=fit)

   [![The Bus Mix Matrix is showing CB_SFX](https://dev.epicgames.com/community/api/documentation/image/f5477d32-e67d-48ab-a59b-c054bb97ff7e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f5477d32-e67d-48ab-a59b-c054bb97ff7e?resizing_type=fit)

### Section Results

In this section, you activated the Sound Modulation debugger and filtered the matrix to only show the `CB_SFX` Control Bus.

## 7 - Adjust Control Buses from Blueprints

In this section, you will activate a Control Mix from Blueprints at runtime.

1. Click the **Blueprint** button in the **Level Editor** toolbar and select **Open Level Blueprint**.

   [![Select Open Level Blueprint](https://dev.epicgames.com/community/api/documentation/image/5862d6d1-ff49-4e56-aaec-551dcdc49c29?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5862d6d1-ff49-4e56-aaec-551dcdc49c29?resizing_type=fit)
2. In the **Event Graph**, right-click and search for then select **Event Begin Play**.

   [![Right-click and search for then select Event Begin Play](https://dev.epicgames.com/community/api/documentation/image/201a75e4-64a3-4a5d-9c4b-a42ccd2ec3ef?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/201a75e4-64a3-4a5d-9c4b-a42ccd2ec3ef?resizing_type=fit)
3. Drag from the **Event Begin Play** node and search for then select **Activate Control Bus Mix**.

   1. Click the **Mix** dropdown and select `CM_User`.

   [![Drag from the Event Begin Play node and search for then select Activate Control Bus Mix](https://dev.epicgames.com/community/api/documentation/image/8efaad0d-9a1a-4b5c-a6a3-17064664e8e2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8efaad0d-9a1a-4b5c-a6a3-17064664e8e2?resizing_type=fit)
4. Drag from the **Activate Control Bus Mix** node and search for then select **Delay**.

   1. Set the **Duration** to **3.0**.

   [![Drag from the Activate Control Bus Mix node and search for then select Delay](https://dev.epicgames.com/community/api/documentation/image/9a088bd3-4791-4dfc-94cb-3c2bd4525e63?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9a088bd3-4791-4dfc-94cb-3c2bd4525e63?resizing_type=fit)
5. Drag from the **Delay** node and search for then select **Set Control Bus Mix By Filter**.

   1. Click the **Mix** dropdown and select `CM_User`.
   2. Add `CB_SFX`to the **Address Filter**.
   3. Enter a **Value** of **0.25**.

   [![Drag from the Delay node and search for then select Set Control Bus Mix By Filter](https://dev.epicgames.com/community/api/documentation/image/1494519f-be0d-4bf5-b809-f791ac72e7a1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1494519f-be0d-4bf5-b809-f791ac72e7a1?resizing_type=fit)
6. Press **Play** and verify that the `CM_User` **Control Bus** is activated and the volume of `MS_Sample` is lowered after 3 seconds.

### Section Results

In this section, you activated the `CM_User` Control Bus and changed the volume of audio using the `CB_SFX` Control Bus.

* [audio](https://dev.epicgames.com/community/search?query=audio)
* [unreal audio engine](https://dev.epicgames.com/community/search?query=unreal%20audio%20engine)
* [modulation](https://dev.epicgames.com/community/search?query=modulation)
* [audio bus](https://dev.epicgames.com/community/search?query=audio%20bus)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Overview](/documentation/en-us/unreal-engine/audio-modulation-quick-start-guide?application_version=5.7#overview)
* [Goals](/documentation/en-us/unreal-engine/audio-modulation-quick-start-guide?application_version=5.7#goals)
* [Objectives](/documentation/en-us/unreal-engine/audio-modulation-quick-start-guide?application_version=5.7#objectives)
* [1 - Required Setup](/documentation/en-us/unreal-engine/audio-modulation-quick-start-guide?application_version=5.7#1-required-setup)
* [Section Results](/documentation/en-us/unreal-engine/audio-modulation-quick-start-guide?application_version=5.7#section-results)
* [2 - Create the Control Buses](/documentation/en-us/unreal-engine/audio-modulation-quick-start-guide?application_version=5.7#2-create-the-control-buses)
* [Section Results](/documentation/en-us/unreal-engine/audio-modulation-quick-start-guide?application_version=5.7#section-results)
* [3 - Assign the Control Buses to Sound Assets](/documentation/en-us/unreal-engine/audio-modulation-quick-start-guide?application_version=5.7#3-assign-the-control-buses-to-sound-assets)
* [Section Results](/documentation/en-us/unreal-engine/audio-modulation-quick-start-guide?application_version=5.7#section-results)
* [4 - Create a Sample MetaSound](/documentation/en-us/unreal-engine/audio-modulation-quick-start-guide?application_version=5.7#4-create-a-sample-meta-sound)
* [Section Results](/documentation/en-us/unreal-engine/audio-modulation-quick-start-guide?application_version=5.7#section-results)
* [5 - Apply a Mix](/documentation/en-us/unreal-engine/audio-modulation-quick-start-guide?application_version=5.7#5-apply-a-mix)
* [Section Results](/documentation/en-us/unreal-engine/audio-modulation-quick-start-guide?application_version=5.7#section-results)
* [6 - Debug a Mix](/documentation/en-us/unreal-engine/audio-modulation-quick-start-guide?application_version=5.7#6-debug-a-mix)
* [Section Results](/documentation/en-us/unreal-engine/audio-modulation-quick-start-guide?application_version=5.7#section-results)
* [7 - Adjust Control Buses from Blueprints](/documentation/en-us/unreal-engine/audio-modulation-quick-start-guide?application_version=5.7#7-adjust-control-buses-from-blueprints)
* [Section Results](/documentation/en-us/unreal-engine/audio-modulation-quick-start-guide?application_version=5.7#section-results)
