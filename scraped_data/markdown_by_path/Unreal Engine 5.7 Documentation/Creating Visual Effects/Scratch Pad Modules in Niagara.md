<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7 -->

# Scratch Pad Modules in Niagara

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
5. [Creating Visual Effects](/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine "Creating Visual Effects")
6. Scratch Pad Modules in Niagara

# Scratch Pad Modules in Niagara

Learn about using Scratch Pad Modules, Niagara's visual-scripted local modules.

On this page

This tutorial is an introduction to scratch pad modules in Unreal Engine. It builds upon a single Niagara system to explore the fundamentals of this feature. The tutorial is less about the final result, and more about learning different ways to use the feature.

## Scope

Scratch pad modules are local Niagara modules that can be authored using visual scripting graphs. There are two asset types that support the creation of Scratch Pad Modules: Niagara **emitters** and Niagara **systems**. The modules are limited in scope to the system or emitter they are created within, and don't appear as standalone assets in the Content Browser.

### Emitter-Based Scratch Pad Module

If a scratch pad module is made inside a Niagara emitter asset, it will apply to all uses of that emitter in whatever Niagara systems it’s been added to. In the `NE_Example` emitter asset below, the **ScratchModuleInEmitter** module appears in the modules list, and its stack entry is editable within the emitter.

[![](https://dev.epicgames.com/community/api/documentation/image/138faa69-ba6c-4e01-bad4-48cc2df677be?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/138faa69-ba6c-4e01-bad4-48cc2df677be?resizing_type=fit)

An emitter asset (NE\_Example).

However, a scratch pad module made in an emitter cannot be used by any other system or emitter assets, and will not appear in a Niagara system's modules list. The example below shows the `NE_Example` emitter asset used within the `NS_Example` Niagara system. Just like other modules, the scratch pad module is locked (can be disabled but not deleted) when the emitter is instanced in a Niagara system.

[![](https://dev.epicgames.com/community/api/documentation/image/260b6f50-6ff1-4220-9cae-34d9cba5e9f2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/260b6f50-6ff1-4220-9cae-34d9cba5e9f2?resizing_type=fit)

An emitter (NE\_Example) instanced inside a Niagara system asset (NS\_Example).

### System-Based Scratch Pad Module

If the Scratch Pad Module is made inside a Niagara System asset, it can be used on any Emitters inside that system. As is the case for all Scratch Pad Modules, they are unavailable to Emitters in other Niagara Systems.

[![](https://dev.epicgames.com/community/api/documentation/image/d99a5d35-9b15-41e9-8dc2-8b75fb35c050?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d99a5d35-9b15-41e9-8dc2-8b75fb35c050?resizing_type=fit)

A Niagara system with a scratch module applied to multiple emitters.

### Niagara Module Script

A scratch pad module can be exported as a Niagara module script asset. This export process is covered more in-depth in the [Share Scratch Modules](https://dev.epicgames.com/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine#share-scratch-modules) section of this tutorial. Niagara module scripts are entirely separate assets that appear in the Content Browser, and can be used by any Niagara emitter and in any Niagara system within your project. This is comparable to how material nodes can be converted into material functions, which then can be used by separate material assets throughout a project.

[![](https://dev.epicgames.com/community/api/documentation/image/e09c422d-2169-49eb-8a1e-0abadaa5e37c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e09c422d-2169-49eb-8a1e-0abadaa5e37c?resizing_type=fit)

A Niagara module script asset in the Content Browser.

## Getting Started

To create a Scratch Pad Module, you'll need to work within a Niagara System asset or Niagara Emitter asset. This tutorial uses a simple grid-spawned Niagara System as the basis for working with Scratch Pad Modules.

### Create a Niagara System

This section explains how to create a Niagara system for new users and those who want to follow this tutorial from beginning to end. If you already have created a Niagara system, you can use that to follow the rest of the tutorial.

To create a new Niagara system, follow these steps:

1. In the **Content Browser**, right-click, then click Niagara System.

   [![The Niagara System option in the right-click menu.](https://dev.epicgames.com/community/api/documentation/image/2c1ad9a5-d40f-4192-9ce8-8c33a5ce97ac?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2c1ad9a5-d40f-4192-9ce8-8c33a5ce97ac?resizing_type=fit)
2. In the **Template** menu, select **Minimal**, and then click **Create**.

   [![The template menu with Minimal emitter type selected.](https://dev.epicgames.com/community/api/documentation/image/ab588b57-7add-4b2c-916b-10cfa6a0437c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ab588b57-7add-4b2c-916b-10cfa6a0437c?resizing_type=fit)
3. Name the new Niagara system (for example, **NS\_Minimal**). Open the asset by double-clicking or pressing **Enter**.

   [![The Niagara System asset in the Content Browser.](https://dev.epicgames.com/community/api/documentation/image/239d3108-15f4-490a-a1d4-7b3b934e37f4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/239d3108-15f4-490a-a1d4-7b3b934e37f4?resizing_type=fit)

By default, the system will have a system node (blue) and a single **Minimal** emitter (orange).

[![The Niagara system with a Minimal default emitter.](https://dev.epicgames.com/community/api/documentation/image/8e00e8ca-043f-4d4a-b829-106a50e5c1de?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8e00e8ca-043f-4d4a-b829-106a50e5c1de?resizing_type=fit)

### Spawn Particles

To make the emitter spawn particles, follow these steps:

1. Navigate to the Minimal emitter.
2. In the Emitter Update section, click Add (+).
3. Search for and click Spawn Particles in Grid option.

[![](https://dev.epicgames.com/community/api/documentation/image/aaec6a8e-d285-4b8c-9b52-0768ef8e453b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/aaec6a8e-d285-4b8c-9b52-0768ef8e453b?resizing_type=fit)

The Spawn Particles in Grid option

You can add often-used modules to the top of the **Add New Module** menu. Hover over the module's name and click on the ****star** (⭐)** icon. The icon will change from an outline to a filled-in star. Close and reopen the menu to see your module listed in the **Suggested** section. To remove it, click the **star** icon again.

#### Fix Dependency Issue

The new module will have a red dot next to its name, indicating an error. In this case, the **Spawn Particles in Grid** module also needs a **Grid Location** module to work correctly.

To fix this issue, click on the module. Review the issue in the **Details** panel, and then click **Fix Issue**.

[![Module with dependency error and Fix Issue button](https://dev.epicgames.com/community/api/documentation/image/b712bf37-cc72-4d3e-b7aa-a568ef8c189d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b712bf37-cc72-4d3e-b7aa-a568ef8c189d?resizing_type=fit)

A **Grid Location** module will be added to the **Particle Spawn** section of the emitter. After that happens, the dependency will be met, and the error icon in the **Spawn Particles in Grid** module will be removed.

[![The Grid Location module.](https://dev.epicgames.com/community/api/documentation/image/d2ff52d9-89b8-4413-b8df-0626149672ad?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d2ff52d9-89b8-4413-b8df-0626149672ad?resizing_type=fit)

### Emitter Settings

To configure the emitter for this tutorial, follow these steps:

1. On the **Minimal** emitter, select **Spawn Particles in Grid**.
2. In the **Details** panel, do the following:

   1. Set X Count to 10.
   2. Set Y Count to 1.
   3. Set Z Count to 1.
   4. Set Spawn Time to 0.
3. On the Minimal emitter, select Initialize Particle.
4. In the **Details** panel, set the following:

   1. Set **Lifetime Mode** to **Direct Set**.
   2. Set **Lifetime** to 5.
   3. Set **Color Mode** to **Direct Set**.
   4. Set **Color** to 1, 0, 0.
   5. Set **Position Mode** to **Simulation Position**.
   6. Set **Position Offset** to 0, 0, 0.
   7. Set **Mass Mode** to ****Unset** / (Mass of 1)**.
   8. Set **Sprite Size Mode** to **Uniform**.
   9. Set **Uniform Sprite Size** to 10.
   10. Set **Sprite Rotation Mode** to **Unset**.
   11. Set **Sprite UV Mode** to **Unset**.
   12. Set all other mesh and ribbon attributes to **Unset**.

In this example, the **Grid Location** module is left with its default values.

## Create a Scratch Pad Module

On the Minimal emitter, click **Add (+)** next to the **Particle Spawn** header. Search for and select the **New Scratch Pad Module** option.

[![Adding a New Scratch Pad Module.](https://dev.epicgames.com/community/api/documentation/image/c477c896-4b11-4697-82ff-361222fe441a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c477c896-4b11-4697-82ff-361222fe441a?resizing_type=fit)

The scratch module graph opens automatically as a tab next to the original **System Overview** tab. A **Local Modules** tab appears below the **Preview** window, next to the **Parameters** and **User Parameters** tabs.

[![The Local Modules tab.](https://dev.epicgames.com/community/api/documentation/image/8a978221-bb66-471e-a66f-f56708b776fe?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8a978221-bb66-471e-a66f-f56708b776fe?resizing_type=fit)

Rename your scratch module to something descriptive (for example, **ApplyOffset**).

While module names will appear as one word (**ApplyOffset**) in the **Modules** list, they are displayed with spaces based on letter capitalization (**Apply Offset**) in search menus and for stack entries.

In the **System Overview** graph, the **Apply Offset** module is now listed as a module in the Minimal Emitter. The new scratch module will also appear in the search menus and be labeled as a scratch pad (rather than Niagara) item.

[![The ApplyOffset module on the Minimal emitter.](https://dev.epicgames.com/community/api/documentation/image/b1aae69f-f921-4cec-8c34-b0ab5b7a017a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b1aae69f-f921-4cec-8c34-b0ab5b7a017a?resizing_type=fit)

### Navigation

To open the scratch pad module's graph, you can do any of the following:

* Click the scratch module's tab, located next to the **System Overview** tab.
* Select the scratch module in the emitter, then click the scratch pad button in the **Details** panel.
* Double-click the scratch module stack entry in the emitter.
* Double-click the scratch module in the **Local Modules** > **Modules** list.

### Data Flow

Like other graphs in Unreal Engine, the data in a module flows from left to right. The data starts at the red **Input Map** node, flows through the white **Niagara Parameter Map** line, and ends at the green **Output Module** node.

You can use **Map Get** nodes to extract data from this **Niagara Parameter Map** line, and use **Map Set** nodes to set data into it.

[![Data flowing from left to right in the scratch pad module graph.](https://dev.epicgames.com/community/api/documentation/image/c0dbf054-eef0-400b-a686-e619fcf7aef3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c0dbf054-eef0-400b-a686-e619fcf7aef3?resizing_type=fit)

## Add Location Offset

Next, add some functionality to the scratch pad module, starting with a location offset.

### Get Position Attribute from Particles

On the **Map Get** node, click the **Add +** pin, then search for and click the **PARTICLES Position** parameter. This is data that is held on each individual particle.

These parameters are written as one word, with a period between the namespace and the name (
NAMESPACE.Name). If you are accessing parameters (especially user parameters) using code or Blueprints, use the version with the period, not spaces.

[![The Position parameter.](https://dev.epicgames.com/community/api/documentation/image/9d522583-f633-4b0a-ba3c-953cab23e74d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9d522583-f633-4b0a-ba3c-953cab23e74d?resizing_type=fit)

[![The PARTICLES Position parameter in the Map Get node.](https://dev.epicgames.com/community/api/documentation/image/3a3cf4f3-b716-4606-8d5e-bb55f9936044?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3a3cf4f3-b716-4606-8d5e-bb55f9936044?resizing_type=fit)

### Add a Vector Input

On the **Map Get** node, click the **Add (+)** pin, then search for and click the **Vector** (INPUT.Vector) option.

[![The Vector parameter.](https://dev.epicgames.com/community/api/documentation/image/4f8e0b51-22ca-41de-83b4-e3f577db0283?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4f8e0b51-22ca-41de-83b4-e3f577db0283?resizing_type=fit)

[![The Vector parameter on the Map Get node.](https://dev.epicgames.com/community/api/documentation/image/be1ddf8b-1a3f-48bb-aa65-436b9b455065?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/be1ddf8b-1a3f-48bb-aa65-436b9b455065?resizing_type=fit)

### Data Namespaces

The text inside the colored blocks in parameter names specifies which namespace the data is coming from.

The **Position** comes from the **PARTICLES** namespace, meaning the data is held on the particles. This data is persistent from frame to frame throughout the particle's lifetime.

The **INPUT** namespace, used for the **Vector**, indicates that its data comes from the module, which a user can modify directly.

## Calculate Location Offset

Drag from the **PARTICLES.Position** pin, then search for and click the **Add** node.

[![PARTICLES.Position to Add node](https://dev.epicgames.com/community/api/documentation/image/76945c49-cdea-49d3-80e5-d3dcbdc38cb4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/76945c49-cdea-49d3-80e5-d3dcbdc38cb4?resizing_type=fit)

By default, the inputs of the **Add** node will be dark blue, showing that it is a type of wildcard called the Niagara Numeric. It accepts positions, vectors, floats, and integers. When connected to other nodes with specific types, the pin and connection wire change to reflect the data type used in those pins.

Drag from the **INPUT.Vector** pin to the second pin of the Add node. It will turn yellow to show that it is a vector type.

[![INPUT.Vector to Add node](https://dev.epicgames.com/community/api/documentation/image/1b38044a-45c7-4295-bd4b-476b88311805?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1b38044a-45c7-4295-bd4b-476b88311805?resizing_type=fit)

### Update Data

After adding the offset amount (**INPUT.Vector**) to the **PARTICLES.Position**, the particle data needs to be updated using a **Map Set** node.

In the existing **Map Set** node, click the **Add (+)** pin, then search for and click **PARTICLES.Position**.

[![PARTICLES.Position in Map Set node](https://dev.epicgames.com/community/api/documentation/image/a253dc28-45c1-45ff-b155-f7fdb07cc257?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a253dc28-45c1-45ff-b155-f7fdb07cc257?resizing_type=fit)

Connect the output of the Add node to the Map Set node's PARTICLES Position pin. This will update (overwrite) the PARTICLES.Position value (accessed in the Map Get node) with the new value.

[![Add node to PARTICLES.Position in Map Set](https://dev.epicgames.com/community/api/documentation/image/e4187e61-9ec6-4131-88c2-e64648a16d56?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e4187e61-9ec6-4131-88c2-e64648a16d56?resizing_type=fit)

## Apply Graph Changes

Click either the **Apply** or **Apply & Save** button to commit the changes in the graph to the scratch module and its stack entries in the Niagara system.

[![The Apply and Apply & Save buttons](https://dev.epicgames.com/community/api/documentation/image/e5bb0821-b6df-4173-82a8-9c4340868aed?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e5bb0821-b6df-4173-82a8-9c4340868aed?resizing_type=fit)

In the **System Overview** graph, select the **Apply Offset** scratch module stack entry on the Minimal emitter. The **Vector** input created in the prior steps is now a valid module input.

[![The Vector input in the scratch module.](https://dev.epicgames.com/community/api/documentation/image/f9817915-2e40-4cd9-9cb5-b1cf882b447a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f9817915-2e40-4cd9-9cb5-b1cf882b447a?resizing_type=fit)

To test the module's functionality, enter a value into the **Vector** input and note how it changes the system's visual output in the Niagara system viewport. In this example, changing the Z value from 0 to 200 moves the red particles up 200 units (centimeters).

[![The Z value set to 0](https://dev.epicgames.com/community/api/documentation/image/9c83c6e2-1d7d-4ba2-a849-8f4d024a5dc9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9c83c6e2-1d7d-4ba2-a849-8f4d024a5dc9?resizing_type=fit)

[![The Z value set to 200](https://dev.epicgames.com/community/api/documentation/image/e25e911d-9286-45fc-b6f7-7580822a1df7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e25e911d-9286-45fc-b6f7-7580822a1df7?resizing_type=fit)

## Module Context

You can set up modules to be visible and usable only in specific emitter contexts.

### Set Module Usage Bitmask

In the **Apply Offset** module graph, click anywhere in the background of the graph. This brings up the module settings in the **Details** panel. The first setting in the list is the **Module Usage Bitmask**, which defines where the module can be created and moved to. Click the dropdown menu to check, search, and set the various context options.

The following contexts are available:

* Function
* Module (enabled by default)
* Dynamic Input
* Particle Spawn Script (enabled by default)
* Particle Update Script (enabled by default)
* Particle Event Script (enabled by default)
* Particle Simulation Stage Script (enabled by default)
* Emitter Spawn Script
* Emitter Update Script
* System Spawn Script
* System Update Script

You can limit where and how the module can be used by checking or unchecking the items in the dropdown menu.

[![The Module Usage Bitmask options.](https://dev.epicgames.com/community/api/documentation/image/a886fde7-d466-410a-839d-f167962b808e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a886fde7-d466-410a-839d-f167962b808e?resizing_type=fit)

To try this out, disable the **Particle Update Script** option, then press the **Apply** button.

[![Disabling the Particle Update Script option.](https://dev.epicgames.com/community/api/documentation/image/6948c1dd-e735-488a-828d-c81998af1a6c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6948c1dd-e735-488a-828d-c81998af1a6c?resizing_type=fit)

Go to the **System Overview** graph view, and try to drag the **Apply Offset** module stack entry into the **Particle Update** section. The bright blue drop line will not appear between the entries of the emitter, and a warning tooltip will appear that says: "This module can't be moved to this section of the stack because it's not valid for this usage context."

[![The warning tooltip](https://dev.epicgames.com/community/api/documentation/image/c4197eb6-d5ef-4d6f-8947-817b3b9d6ad4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c4197eb6-d5ef-4d6f-8947-817b3b9d6ad4?resizing_type=fit)

Additionally, this context limitation applies to the search results of that restricted section. In this case, the **Apply Offset** module doesn't appear in the **Particle Update** section's search.

[![Apply Offset not valid in Particle Update search](https://dev.epicgames.com/community/api/documentation/image/55198a08-836d-4115-9d94-af04c6f1a1d2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/55198a08-836d-4115-9d94-af04c6f1a1d2?resizing_type=fit)

The Apply Offset module is still available in the Particle Spawn search results.

[![ApplyOffset valid in Particle Spawn search](https://dev.epicgames.com/community/api/documentation/image/97f83615-2d34-4549-b1d0-6fdf0cfd0f52?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/97f83615-2d34-4549-b1d0-6fdf0cfd0f52?resizing_type=fit)

Enable the **Particle Update Script** context to continue following this tutorial.

### Particle Spawn and Particle Update

Modules located in the **Particle Spawn** section of the emitter only execute when the particle is created (spawned).

Modules located in the **Particle Update** section of the emitter execute every tick.

To demonstrate, drag the **Apply Offset** stack entry from **Particle Spawn** to a spot under the **Particle Update** section. Change the Vector input Z value to 1. In the viewport, the red dots will move upward, as the 1cm offset is applied to the particles every tick.

[![Apply Offset moved to Particle Spawn section and Vector Z set to 1](https://dev.epicgames.com/community/api/documentation/image/bb6983eb-9dd4-48ab-8360-0e4043d63585?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bb6983eb-9dd4-48ab-8360-0e4043d63585?resizing_type=fit)

When you're done, drag it back into the **Particle Spawn** section to continue following the tutorial.

## Rotation Offset

There are a few ways to let the user (in this case, a VFX artist) rotate the offset around an axis. In this section, you will add rotation inside the module. Later in the tutorial you will learn how to leverage dynamic inputs for user-entered data.

### Add Node

Right-click on the graph background, search for "rotation", and then click XYZRotationToQuaternion.

[![The XYZ Rotation to Quaterion node.](https://dev.epicgames.com/community/api/documentation/image/f0691686-ae93-4485-8be8-bbdc40368cb1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f0691686-ae93-4485-8be8-bbdc40368cb1?resizing_type=fit)

### Create Inputs

The next step is creating inputs that the user can access and enter values into. The easiest way is to drag a line from the desired pin (in this example, X, Y, and Z) onto the **Add (+)** icon in the **Map Get** node. This creates a corresponding INPUT parameter of the same name and correct type. Do this for all three float values (green pins, XYZ) in the **Rotation to Quaternion** node.

[![The XYZRotationToQuaterion node connected to Map Get.](https://dev.epicgames.com/community/api/documentation/image/d663c840-9655-4957-8c41-c8224277b42e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d663c840-9655-4957-8c41-c8224277b42e?resizing_type=fit)

### Calculate Rotation Offset

Drag from the **Map Get**'s **INPUT.Vector** pin, then search for and click the **Multiply Vector With Quaternion** node. Drag the output pin of the **XYZRotation to Quaternion** node to the **Quaternion** input pin in the **Multiply Vector with Quaternion** node.

[![The INPUT.Vector connected to Multiply Vector with Quaternion.](https://dev.epicgames.com/community/api/documentation/image/050ec435-8658-4ef6-abcb-be09598f43bc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/050ec435-8658-4ef6-abcb-be09598f43bc?resizing_type=fit)

Connect the output pin of the **Multiply Vector with Quaternion** node to the second pin of the **Add** node, replacing the plain **INPUT.Vector** value with the new multiplied **Vector** and **Quaternion** value.

[![Rearrange nodes to put Multiply Quaternion node between the INPUT.Vector and Add node.](https://dev.epicgames.com/community/api/documentation/image/1d06d63d-cecf-40a3-9587-d19119dde409?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1d06d63d-cecf-40a3-9587-d19119dde409?resizing_type=fit)

### Apply Rotation Offset Changes

Click **Apply & Save**, then open the **System Overview** graph.

Select the **Apply Offset** stack entry (located in the **Particle Update** section of the emitter), and set the Y value to 30. This causes the red particles to move upward and to the right.

[![Vector Y set to 30, particle trajectory changed.](https://dev.epicgames.com/community/api/documentation/image/266fb64c-913c-4b85-b16d-e805284c2c0f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/266fb64c-913c-4b85-b16d-e805284c2c0f?resizing_type=fit)

## Parameters Tabs

There are two tabs under the viewport in a Niagara system with different data and interaction options.

### Parameters

The Parameters tab lists all the parameters included within a Niagara system. This includes:

* **System Attributes** (such as  SYSTEM.Age, SYSTEM.LoopCount)
* **Emitter Attributes** (such as EMITTER.Age, EMITTER.DistanceTraveled)
* **Particle Attributes** (such as PARTICLES.Position, PARTICLES.SpriteSize)
* **Module Outputs** (such as OUTPUT.GRIDLOCATION.GridSpacing, OUTPUT.PARTICLESTATE.FirstFrame)
* **Engine Provided** (such as ENGINE.DeltaTime, ENGINE.EMITTER.NumParticles, ENGINE.OWNER.Velocity)
* **Stage Transients** (such as TRANSIENT.FirstFrame, TRANSIENT.ScalabilityExecutionState)

There are also headings in this tab that will be empty by default:

* **User Exposed** (same as in the User Parameters tab)
* **Stack Context Sensitive**
* **Niagara Parameter Collection**

[![The Parameters tab.](https://dev.epicgames.com/community/api/documentation/image/1ffc50ef-a4b6-4e48-b2b0-aeaa761ba4ca?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1ffc50ef-a4b6-4e48-b2b0-aeaa761ba4ca?resizing_type=fit)

## User Parameters

The **User Parameters** tab lists all the user parameters created in a Niagara system. It is empty by default. The user parameters here are the same as in the **User Exposed** section of the **Parameters** tab.

[![The User Parameters tab with an example USER.test parameter.](https://dev.epicgames.com/community/api/documentation/image/a76efe08-6a64-435c-b042-bc576de9c74a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a76efe08-6a64-435c-b042-bc576de9c74a?resizing_type=fit)

### View-Dependent Changes & Renaming

When you're viewing the graph for a specific module, like **Apply Offset**, the **Parameters** list is filtered down to the inputs that you currently have available to you.

[![The same inputs in Map Get and the Parameters tab.](https://dev.epicgames.com/community/api/documentation/image/7d730776-5136-45b3-a8d8-21eb4f349bd1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7d730776-5136-45b3-a8d8-21eb4f349bd1?resizing_type=fit)

In these tabs, you can rename your inputs (like INPUT.RotationAngleX). As with other parts of Unreal Engine, click twice on the input name or press **F2**.

[![Renamed inputs in the Parameters tab.](https://dev.epicgames.com/community/api/documentation/image/350c3e93-77c9-4a55-a4b1-0e5668686d25?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/350c3e93-77c9-4a55-a4b1-0e5668686d25?resizing_type=fit)

When you click **Apply & Save**, the new names are visible in the module's stack entry.

[![Renamed inputs in the Details Panel.](https://dev.epicgames.com/community/api/documentation/image/2f5086f1-dec6-4225-932b-4eb4343b39df?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2f5086f1-dec6-4225-932b-4eb4343b39df?resizing_type=fit)

## Edit Hierarchy Tool

In the **Edit Hierarchy** window, you can order the inputs, add tooltips, and manage dependencies.

To access the **Edit Hierarchy** interface, open the scratch pad module you want to edit (in this case, the **Apply Offset** module).

In the **Parameters** tab, click **Edit Input Hierarchies**.

[![The Edit Input Hierarchy button in the Parameters tab.](https://dev.epicgames.com/community/api/documentation/image/97de05d3-5364-46fa-9525-06ff55da6243?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/97de05d3-5364-46fa-9525-06ff55da6243?resizing_type=fit)

This opens the **Edit Hierarchy** window.

[![The Edit Hierarchy window.](https://dev.epicgames.com/community/api/documentation/image/082c4e85-8117-46da-beab-e429f9715896?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/082c4e85-8117-46da-beab-e429f9715896?resizing_type=fit)

From the left column, drag the relevant inputs into the center column, where the blue highlight appears.

[![The INPUT.Vector added to the Hierarchy list](https://dev.epicgames.com/community/api/documentation/image/b3485998-03d6-48ca-9097-24e1a66b7d59?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b3485998-03d6-48ca-9097-24e1a66b7d59?resizing_type=fit)

Drag the inputs in the center column to reorder them.

### Defaults

As in the Details panel, you can access the item's Default Value and Variable settings.

* **Default Mode**: Options include **Binding**, **Custom**, **Fail if Previously Not Set**, and the default value**.**
* **Default Value**: Based on type, such as float or vector.
* **Tooltip (and localization options)**: Add helpful implementation details, units, caveats, or other notes that are valuable to users.
* **Display Unit**: Options include **Centimeters**, **Lumens**, **Hours**, **Gigabytes**, **Grams**, **Degrees**, and the default **Unspecified**.
* **Advanced Display**: False by default.
* **Display in Overview Stack**: False by default.
* **Inline Parameter Sort Priority and Color Override**: Disabled by default.
* **Edit Condition and Visible Condition** (Input Name and Target Values): None and 0 elements by default.
* **Property Metadata**: 0 elements by default.
* **Alternate Aliases for Variable**: 0 elements by default.
* **Widget Type**: Default.
* **Min Value**: 0 by default.
* **Max Value**: 1 by default.
* **Step Width**: 1 by default.
* **Broadcast Value Change On Commit Only**: False (set to true if you only want values to be updated when committed, not when typing).

[![Default Value and Variable sections of the Rotation Angle X input](https://dev.epicgames.com/community/api/documentation/image/b0f4c9d4-5e7c-4927-9df7-d4b376b72540?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b0f4c9d4-5e7c-4927-9df7-d4b376b72540?resizing_type=fit)

### Tooltips

Add text into the **Tooltip** field of the **Rotation Angle X** input, then click **Apply** or **Apply & Save**.

[![The Tooltip field](https://dev.epicgames.com/community/api/documentation/image/fee38ab6-847b-4d53-a976-a6adcb5882ce?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fee38ab6-847b-4d53-a976-a6adcb5882ce?resizing_type=fit)

Then, go to the **System Overview** graph, select the **Apply Offset** module, and hover over the **Rotate Angle X** option in the **Details** panel. Your tooltip will be the first line in the popup, followed by the **Name** and **Type** information of the input you're hovering over.

[![The Tooltip in the Details panel.](https://dev.epicgames.com/community/api/documentation/image/2e30286c-479a-4ffe-a413-5c139cf2db6e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2e30286c-479a-4ffe-a413-5c139cf2db6e?resizing_type=fit)

### Display Unit

In the **Edit Hierarchy** window (or the **Details** panel), change the **Display Unit** of the value. Select the **Rotation Angle X** input, and change the **Display Unit** from **Unspecified** to **Degrees**.

[![Display Unit set to Degrees](https://dev.epicgames.com/community/api/documentation/image/fa79084c-6a31-403c-b156-cf4cadc536a9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fa79084c-6a31-403c-b156-cf4cadc536a9?resizing_type=fit)

Then, change the **Vector** input's **Display Unit** to **Centimeters**.

[![Display Unit set to Centimeters](https://dev.epicgames.com/community/api/documentation/image/31bac2fa-4bbb-4678-a6dc-eccf26e0d84e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/31bac2fa-4bbb-4678-a6dc-eccf26e0d84e?resizing_type=fit)

## Local Parameters

When making complex modules, you can leverage local parameters to help keep your module graph organized and easy to read. Separating the graph by operations is a common and generally recommended approach.

Local parameters only exist in the module, and are not persistent from frame to frame. They are often used for temporary value storage within a graph.

### Split Inputs Between Different Map Gets and Map Sets

Right-click the **PARTICLES.Position** pin from the **Map Get** and click **Remove**. Disconnect the node (**Alt + click**).

Near the **Multiply Vector with Quaternion** node, add a **Map Set** node (listed as **Parameter Map Set** in the right-click menu). Connect it to the **Niagara Parameter Map** line, between the **Input node** and the **Map Set** node.

[![The Map Set node](https://dev.epicgames.com/community/api/documentation/image/2e330fda-d8a2-4b1e-8d78-1b342b20c796?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2e330fda-d8a2-4b1e-8d78-1b342b20c796?resizing_type=fit)

Drag the **Multiply Vector with Quaternion** output pin to the **Add (+)** icon on **Map Set**. This creates a local parameter of the same name and type as the pin you pulled from. In this case, it creates **LOCAL.Vector**. Rename this to something more descriptive (for example, **LOCAL.Offset**).

[![LOCAL.Offset in Map Set node](https://dev.epicgames.com/community/api/documentation/image/14bbeb1a-d223-4444-93f3-d6095ca79c15?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/14bbeb1a-d223-4444-93f3-d6095ca79c15?resizing_type=fit)

On the right side of the **Map Set** node, drag from the white **Dest** pin, then search for and click the **Map Get** option.

[![The Map Get node connected to the Map Set node](https://dev.epicgames.com/community/api/documentation/image/6d83f1da-296f-4b63-bd30-b43511c23a48?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6d83f1da-296f-4b63-bd30-b43511c23a48?resizing_type=fit)

Click **Add (+)**, then search for and select the **LOCAL.Offset** created in the previous step.

[![LOCAL.Offset in new Map Get node](https://dev.epicgames.com/community/api/documentation/image/7ef57c4d-17fe-4fb3-92e3-a2950e7dbf80?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7ef57c4d-17fe-4fb3-92e3-a2950e7dbf80?resizing_type=fit)

Now you can use that cached Offset value in another organized section of the graph.

### Break & Rearrange

When rearranging or adding nodes in any Unreal Engine graph, you might need to disconnect the wires connecting specific nodes. Use **Alt + Left Click** on a pin or wire to disconnect it.

To grab and move a pin connection instead, hold **Ctrl + Left Click** to pick up the wire. Release over a valid pin. The connection will be deleted if you release over empty graph space.

To remove, rename, reorder, or perform other actions on a pin, right-click to bring up a menu and click the desired action.

[![The Remove Pin option in the right-click menu.](https://dev.epicgames.com/community/api/documentation/image/0beab98c-ad4d-49c7-885e-b8ca0954d6b6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0beab98c-ad4d-49c7-885e-b8ca0954d6b6?resizing_type=fit)

## Transformation Space & Position Offset

There are three different types of **Transformation Spaces**:

* **Simulation**: Calculations are done in whatever context (local or world) that is set in the emitter's **Properties** section, where **Local Space** is set to either true or false.
* **World**: Calculations are done in the context of the world values.
* **Local**: Calculations are done in the context of the system itself, regardless of where it is in the world.

### User-Set Transform Space

For this example, let’s give the user an option to choose which **Transformation Space** to use in this module.

Create a **Transform Vector** node. Drag the **Map Get**'s Offset pin to the **InVector** pin of the **Transform Vector** node.

[![The Transform Vector node](https://dev.epicgames.com/community/api/documentation/image/cd0a861a-ca11-4ea3-b8d9-d401fd5a357d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cd0a861a-ca11-4ea3-b8d9-d401fd5a357d?resizing_type=fit)

To let the user set the **Source Space** as an input, drag the **Transform Vector**'s **Source Space** pin back to the **Map Get** node's **Add (+)** icon. This creates an input of the same name and type.

[![The Source Space input](https://dev.epicgames.com/community/api/documentation/image/dfa24143-ae0c-415c-81ea-72886fee7ab4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dfa24143-ae0c-415c-81ea-72886fee7ab4?resizing_type=fit)

Add another **Map Set** node, and connect it between the previous Map Set and the final Map Set. Create a **LOCAL.Offset** entry on the **Map Set** node, and drag it to the **Transform Vector**’s **OutVector** pin.

[![Set LOCAL.Offset](https://dev.epicgames.com/community/api/documentation/image/f55716d1-bc08-44e8-8056-abd1aacf5255?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f55716d1-bc08-44e8-8056-abd1aacf5255?resizing_type=fit)

### Re-Implement Position Offset

From the new **Map Set** node, create a **Map Get** node, and click the **Add (+)** button to access the **LOCAL.Offset** variable.

[![The Map Get node](https://dev.epicgames.com/community/api/documentation/image/041297a1-2ccc-4b10-beb8-4e94f4763b18?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/041297a1-2ccc-4b10-beb8-4e94f4763b18?resizing_type=fit)

Next, click the **Add (+)** button to access the **PARTICLES.Position** parameter.

[![PARTICLES.Position in Map Get](https://dev.epicgames.com/community/api/documentation/image/8a34fdf6-1b9a-4e1f-9ccd-785241240b4f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8a34fdf6-1b9a-4e1f-9ccd-785241240b4f?resizing_type=fit)

Add the **LOCAL.Offset** to the **PARTICLES.Position** using the **Add** node from before.

[![Using the add node to add LOCAL.Offset](https://dev.epicgames.com/community/api/documentation/image/c22f6b2d-f253-473c-b49c-eedb6ed7d85e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c22f6b2d-f253-473c-b49c-eedb6ed7d85e?resizing_type=fit)

If you want to change the order of the elements in a node, right-click on one of the items and click **Move pin up**.

Connect the **Add** node to the **Map Set** node using the **PARTICLES.Position** pin, and drag the **Dest** to the final **Output Module**.

[![Connecting Add, Map Set, and Output Module.](https://dev.epicgames.com/community/api/documentation/image/583a9351-9c98-4bf4-9452-699f7c453b57?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/583a9351-9c98-4bf4-9452-699f7c453b57?resizing_type=fit)

### Apply Changes

[![](https://dev.epicgames.com/community/api/documentation/image/4782f0b0-9a25-404b-bef6-3af203b0a890?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4782f0b0-9a25-404b-bef6-3af203b0a890?resizing_type=fit)

The scratch pad module graph so far

Click **Apply** or **Apply & Save**, then open the **System Overview** graph. Select the **Minimal** emitter, then select the **Apply Offset** stack entry on it. In the **Details** panel, there's now a **Source Space** input option.

[![Source Space in the Details Panel](https://dev.epicgames.com/community/api/documentation/image/acc68c27-f7ac-439e-a787-bc173c7da610?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/acc68c27-f7ac-439e-a787-bc173c7da610?resizing_type=fit)

## Add Comments

Comments visually group nodes together, and often include text to describe that portion of the graph or any other notes pertinent to that section. Like with text-based code, leaving comments throughout your work is considered a best practice. Comments make it easier for other developers to understand your decisions.

Open the **Scratch Module** graph. Select nodes in the graph, and press the **C** key to create a comment. Rename it to be descriptive (for example, **Initial Offset Vector**).

[![Initial Offset Vector comment](https://dev.epicgames.com/community/api/documentation/image/ca30e568-b577-42ce-9bd7-af273f62c44b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ca30e568-b577-42ce-9bd7-af273f62c44b?resizing_type=fit)

With the comment box selected, the **Detail** panel displays the available settings: **Color**, **Font Size**, **Show Bubble When Zoomed**, **Color Bubble**, **Move Mode**, and the **Details** field.

[![The comment Details panel](https://dev.epicgames.com/community/api/documentation/image/1c10cbac-18e4-4c33-b95a-6cdd7b6ba398?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1c10cbac-18e4-4c33-b95a-6cdd7b6ba398?resizing_type=fit)

Commenting provides visual and textual information about what's happening in each section of the graph. Comments on this example graph could include: **Initial Offset Vector**, **Transform Into Space**, and **Set Position**. Each comment box here includes the initial **Map Get** and the subsequent **Map Set** node, where the next **Map Get** starts the next section.

[![The scratch pad module graph with comment boxes throughout](https://dev.epicgames.com/community/api/documentation/image/8e53bb5a-3b57-4e04-a2d8-909174941e91?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8e53bb5a-3b57-4e04-a2d8-909174941e91?resizing_type=fit)

## Module Outputs

Module outputs can supply extra data to the user without having to fill in particle data. Since emitter stack entries are executed from top to bottom, module output data is available only to stack entries below it. Knowing the outputs and other parameters written to them can be helpful when figuring out how to work with the data in your particle system.

### Show Parameter Writes

Select any module in the Minimal emitter. In the **Details** panel, select the **gear (⚙️)** icon, and enable **Show Parameter Writes**. The **Parameter Writes** section is collapsed by default. Click the **arrow (🔽)** to expand the list and see all the outputs the stack entry writes to.

In the **Apply Offset** scratch pad module stack entry below, the **Parameter Writes** section only includes **PARTICLES.Position**.

[![The Show Parameter Writes option](https://dev.epicgames.com/community/api/documentation/image/fab2fb62-3ea1-40b6-bd8e-c4b1fed49670?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fab2fb62-3ea1-40b6-bd8e-c4b1fed49670?resizing_type=fit)

### Use Module Outputs

Select the **Grid Location** module stack entry, and expand the **Parameter Writes** section. It writes to **PARTICLES.Position**, as well as other **OUTPUT** parameters.

[![](https://dev.epicgames.com/community/api/documentation/image/ecdf46bb-1609-4eb7-b2c2-f7d3c5fa7dfc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ecdf46bb-1609-4eb7-b2c2-f7d3c5fa7dfc?resizing_type=fit)

The Parameter Writes section for the Grid Location module

As an example, let’s use **OUTPUT.GRIDLOCATION.GridUVW** to change the color of our particles.

To demonstrate this, open the **Spawn Particles in Grid** stack entry, then change the X, Y, and Z values to 10. You'll see a cube-shaped group of particles, rather than a line of them.

[![Spawn Particles in Grid XYZ set to 10](https://dev.epicgames.com/community/api/documentation/image/d1f39a3e-a528-4de3-96e8-a5eac8f05d64?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d1f39a3e-a528-4de3-96e8-a5eac8f05d64?resizing_type=fit)

Then, in the **Particle Spawn** section of the emitter, click the **Add (+)** button to create a **Color** module.

[![Color module with default Color setting](https://dev.epicgames.com/community/api/documentation/image/c867508b-1672-4bb1-911b-2664ce386dea?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c867508b-1672-4bb1-911b-2664ce386dea?resizing_type=fit)

Using the drop-down menu next to the **Color** swatch, search for and click both **Make Linear Color from Vector** and **Float.**

[![Make Linear Color from Vector and Float](https://dev.epicgames.com/community/api/documentation/image/bbcec2d7-3975-4f72-9d56-25b846ddd8c0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bbcec2d7-3975-4f72-9d56-25b846ddd8c0?resizing_type=fit)

Using the dropdown menu next to the new **Vector (RGB)** field, search for and click **OUTPUT.GRIDLOCATION.GridUVW**.

[![Vector RGB set to OUTPUT.GRIDLOCATION.GridUVW](https://dev.epicgames.com/community/api/documentation/image/34f33a67-b4f0-4db2-8606-f7586ccb16e2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/34f33a67-b4f0-4db2-8606-f7586ccb16e2?resizing_type=fit)

Now, the RGB values are determined by the **OUTPUT.GRIDLOCATION.GridUVW** information.

[![Colors from OUTPUT.GRIDLOCATION.GridUVW](https://dev.epicgames.com/community/api/documentation/image/10794d3b-1c12-4918-95ac-9a23f63b93c7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/10794d3b-1c12-4918-95ac-9a23f63b93c7?resizing_type=fit)

### Create Module Outputs

Open the **Apply Offset** scratch pad module graph. In the **Set Position** comment section (the last Map Get and Map Set), drag the Map Get's LOCAL.Offset pin to the **Add (+)** pin of the **Map Set** node.

[![Set Position LOCAL.Offset to Map Set](https://dev.epicgames.com/community/api/documentation/image/9761d78e-061d-47c1-96e9-a02f956515f8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9761d78e-061d-47c1-96e9-a02f956515f8?resizing_type=fit)

Double-click a connection wire to create a reroute node, then move it as needed to reduce overlap and increase visibility in the graph. You can also manually create reroute nodes through the graph's right-click menu.

Right-click the new **LOCAL.Offset** pin in the **Map Set** node. Click **Change Namespace** > **OUTPUT**.

[![Changing the namespace to OUTPUT](https://dev.epicgames.com/community/api/documentation/image/dddfbc9c-f577-4fa5-b3f3-684e0709ed69?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dddfbc9c-f577-4fa5-b3f3-684e0709ed69?resizing_type=fit)

This changes the **LOCAL** namespace to **OUTPUT**. It also adds a namespace modifier (for example, **MODULE**) and appends the module name (**Apply Offset**). The result is **OUTPUT.MODULE.Offset** in the **Map Set** node.

[![LOCAL.Offset changed to OUTPUT.MODULE.Offset](https://dev.epicgames.com/community/api/documentation/image/15d5d0ee-2fb5-4448-8c47-06326a0bb369?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/15d5d0ee-2fb5-4448-8c47-06326a0bb369?resizing_type=fit)

Click **Apply**, then open the **System Overview** graph. Select the **Minimal** emitter's **Apply Offset** stack entry, and expand the **Parameter Writes** section in the **Details** panel. The **OUTPUT.APPLYOFFSET.Offset** parameter will be in the list and available for use by any module stack entries below it.

### Set Parameter Directly

For example, let's query the offset. Click the **Add (+)** button to create a **Set Parameters** stack entry underneath the **Apply Offset** stack entry. This module appears as **Set new or existing parameter directly** in the search menu.

[![Set new or existing parameter directly](https://dev.epicgames.com/community/api/documentation/image/1e182f8c-6b48-457f-a532-362280286bf3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1e182f8c-6b48-457f-a532-362280286bf3?resizing_type=fit)

In the **Details** panel, click the **Add (+)** button to create a **Vector** (PARTICLES.Vector) item in the list.

[![Add Vector parameter](https://dev.epicgames.com/community/api/documentation/image/ddef90b3-fe0f-4ef6-bfaf-a1f00355b464?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ddef90b3-fe0f-4ef6-bfaf-a1f00355b464?resizing_type=fit)

In the new entry, click the **arrow** to open the type menu, then search for and click **OUTPUT.APPLYOFFSET.Offset**.

[![PARTICLES Vector set to OUTPUT.APPLYOFFSET.Offset](https://dev.epicgames.com/community/api/documentation/image/89eecc0e-aa3e-4caa-97c4-d53d93a7dd1e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/89eecc0e-aa3e-4caa-97c4-d53d93a7dd1e?resizing_type=fit)

## Dynamic Module Inputs

When writing a module script, there are a few options for where the functionality can be set up. Many dynamic inputs are available, which can give the user more options and power when implemented.

For example, you can rework the **Quaternion** in the **Apply Offset** module. Open the **Apply Offset** graph, and navigate to the first **Map Get** in the graph (the one with the separate X, Y, and Z Map Get inputs connected to the **Quaternion** node).

[![Initial Offset Vector section](https://dev.epicgames.com/community/api/documentation/image/c5ac43d5-a4d7-4a09-8258-9ce46dc68eb7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c5ac43d5-a4d7-4a09-8258-9ce46dc68eb7?resizing_type=fit)

Handling the **Quaternion** in this way has some limitations. The rotation angle is exposed separately as X, Y, and Z, and it assumes the angle type is in degrees. These are the only options provided to the user.

It could be more powerful for the user to expose the quaternion as an input, and then let the pre-existing dynamic inputs do the work for us. In this case, you can use the quaternion directly, instead of the rotation angles in the first **Map Get**.

### Set Up Dynamic Inputs

Right-click and remove each of the X, Y, and Z pins from the first **Map Get** node. Also, delete the **XYZRotation to Quaternion** node.

[![Map Get with INPUT.Vector, Multiply Vector with Quaternion, Map Set](https://dev.epicgames.com/community/api/documentation/image/19457409-f9ca-4dc8-a1f1-59968b19bf6b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/19457409-f9ca-4dc8-a1f1-59968b19bf6b?resizing_type=fit)

In Map Get, click the **Add (+)** pin to search for and click **INPUT.Quaternion** (Quat). Rename it to something descriptive (for example, **INPUT.RotationQuaternion**). Drag that pin to the **Quaternion** pin of the **Multiply Vector With Quaternion** node.

[![INPUT.RotationQuaternion added to Map Get](https://dev.epicgames.com/community/api/documentation/image/1c929d6a-8433-4e52-9b38-977d75671e32?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1c929d6a-8433-4e52-9b38-977d75671e32?resizing_type=fit)

Click **Apply**, then open the **System Overview** graph. The **Rotation Quaternion** is now available in the **Apply Offset** module's **Details** panel, and the separate X, Y, and Z options have been removed.

[![The Rotation Quaternion in the Details panel](https://dev.epicgames.com/community/api/documentation/image/14f9764e-efb9-4775-af46-6e5f5d0f5fa5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/14f9764e-efb9-4775-af46-6e5f5d0f5fa5?resizing_type=fit)

### Use Dynamic Inputs

In the emitter’s **Apply Offset** stack entry, open the drop-down for the **Rotation Quaternion** item, then search for and click **Make Quaternion**.

[![Make Quaternion](https://dev.epicgames.com/community/api/documentation/image/b5318885-78b4-4869-b4bc-4fd934549d67?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b5318885-78b4-4869-b4bc-4fd934549d67?resizing_type=fit)

A user can now choose any of the options predefined by the dynamic input. They can change the **Angle Type**, select **XYZ Rotations** as the **Quaternion From**, and specify a different **Coordinate Space**. These are all built-in options that Niagara provides.

[![Make Quaternion applied](https://dev.epicgames.com/community/api/documentation/image/76e2ffa1-a044-4eb6-8eac-66dd478333f0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/76e2ffa1-a044-4eb6-8eac-66dd478333f0?resizing_type=fit)

### Considerations

When figuring out how to author and present the modules, consider what's easiest for you to manage and what's most powerful and usable for the user. Try to find a balance between what’s flexible for your end user without being too open-ended.

In this case, the drawback is that a "Rotation Quaternion” might be a bit esoteric or unclear for the user.

To address such potential roadblocks, add tooltips to your inputs. Select the input from the **Parameters** list, and enter a tooltip in the **Details** panel **Tooltip** field. For this input, you can enter something like, "Use the Make Quaternion Dynamic Input." This gives the user a clear next step.

[![INPUT.RotationQuaternion tooltip](https://dev.epicgames.com/community/api/documentation/image/57656933-2dd0-4458-8237-4f00a5e49be0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/57656933-2dd0-4458-8237-4f00a5e49be0?resizing_type=fit)

Click **Apply**. Open the **System Overview** graph, select the **Apply Offset** module, and hover over the **Rotation Quaternion** item in the **Details** Panel. The custom text will appear as the first line in the tooltip.

[![The Tooltip in the Details Panel](https://dev.epicgames.com/community/api/documentation/image/b2865d79-6d3e-4596-b8ba-1cdb8da2f789?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b2865d79-6d3e-4596-b8ba-1cdb8da2f789?resizing_type=fit)

## Module Notes

Every module, including scratch pad modules, has a **Note** field available. These **Module Usage Notes** appear at the top of the **Details** panel when a module's stack entry is selected in an emitter. You can put information here about how the module works, including any quirks about its usage, and dependency notes.

[![Module Usage Note in the Details panel](https://dev.epicgames.com/community/api/documentation/image/de8c97da-baa7-4056-a57f-a0d1dcbe7452?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/de8c97da-baa7-4056-a57f-a0d1dcbe7452?resizing_type=fit)

### Add Module Notes

To find and edit this option, click the graph background to deselect any nodes. This populates the Details panel with information about the module as a whole, rather than a specific part of it. Enter information about the module to the **Note Message** field.

For the **Apply Offset** scratch module, a helpful tooltip could be: "This module applies an offset to the particle position. Use the Make Quaternion Dynamic Input as a utility to provide the Quaternion."

[![The Note Message field](https://dev.epicgames.com/community/api/documentation/image/53343806-0b10-4385-aa18-bc8772c0344f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/53343806-0b10-4385-aa18-bc8772c0344f?resizing_type=fit)

### View Module Notes

Click Apply, then open the **System Overview** graph. Select the **Apply Offset** scratch module stack entry, and the **Module Usage Note** will be at the top of the Details panel.

[![The Module Usage Note in the Details panel](https://dev.epicgames.com/community/api/documentation/image/400b6830-1bfe-4b51-9b29-764c9389e3af?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/400b6830-1bfe-4b51-9b29-764c9389e3af?resizing_type=fit)

### Dismiss and Show Notes

Notes (and other issues or warnings) at the top of the **Details** panel can be hidden by clicking **Dismiss**.

[![The Dismiss button](https://dev.epicgames.com/community/api/documentation/image/2d05bc29-f464-4bf0-a026-2e9e4c5b07ca?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2d05bc29-f464-4bf0-a026-2e9e4c5b07ca?resizing_type=fit)

Notes can be made visible again by clicking the **gear (⚙️)** icon at the top of the module, and clicking U**ndismiss All Stack Issues**.

[![Undismiss All Stack Issues](https://dev.epicgames.com/community/api/documentation/image/a2293b2a-bae1-4688-b8a6-df3ceb22945f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a2293b2a-bae1-4688-b8a6-df3ceb22945f?resizing_type=fit)

When dismissed on one stack entry, the **Notes** section will appear on newly added stack entries of the same module type.

## Managing Parameters

All the parameters and inputs are listed in the **Parameters** tab.

[![The Parameters tab](https://dev.epicgames.com/community/api/documentation/image/c6de4716-3a89-4c6a-98dc-e2fd9167be95?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c6de4716-3a89-4c6a-98dc-e2fd9167be95?resizing_type=fit)

The list might include parameters and inputs that are no longer in use in your module.

### Parameter Usage Stats

The easiest way to identify what parameters and inputs need to be cleaned up is to check the field on the right of each input. This shows the references for the reads and writes for each input. In this case, all three of the **INPUT.RotationAngle** parameters (X, Y, and Z) are not in use, because those entries are all listed as having 0 reads and 0 writes (**0|0**).

[![Highlighted inputs have 0 reads and 0 writes (no usages)](https://dev.epicgames.com/community/api/documentation/image/dd1d7c63-63a9-4ce9-9045-42908d6432b3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dd1d7c63-63a9-4ce9-9045-42908d6432b3?resizing_type=fit)

### Remove Unused Parameters

Even when its usages are deleted in a module graph, parameters will remain in the **Parameters** list. You’ll need to manually delete them when you no longer need them.

To remove unused parameters like these, select them in the Parameters list and press the **Delete** key, or right-click on the parameter and click **Delete**.

## Data Interfaces

These special data types take information from the general editor and pass it into Niagara, so you can use it to direct your particles or influence your simulation.

### Access Data Interfaces

To access data interfaces, open your scratch module graph. On a **Map Ge**t node, click the **Add (+)** pin to open the **Make New** drop-down. Click **Data Interface** to show a list of options.

[![Data Interface options](https://dev.epicgames.com/community/api/documentation/image/97235cee-f1e3-400f-a9ea-c7cfbea12a72?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/97235cee-f1e3-400f-a9ea-c7cfbea12a72?resizing_type=fit)

Most of these data interfaces have modules already written for them in the engine. Sometimes, you might want to add that functionality directly into your scratch module instead.

### Work With Data Interfaces

For this example, create space between the Transform Into Space and Set Position sections on the graph.

[![Space created in the graph](https://dev.epicgames.com/community/api/documentation/image/8f9839bf-2ec1-4efc-bd27-6c756c605002?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8f9839bf-2ec1-4efc-bd27-6c756c605002?resizing_type=fit)

Add a **Map Set** node before the **Set Position** section, and reroute the pins. Connect the **Map Set** from **Transform Into Space** into the new **Map Set** node, and drag the **Dest** pin on the Map Set into the **Map Get** in **Set Position** and subsequent **Map Set**.

[![New Map Set](https://dev.epicgames.com/community/api/documentation/image/55c882b1-672e-497a-bf45-26c93f238e08?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/55c882b1-672e-497a-bf45-26c93f238e08?resizing_type=fit)

Create a **Map Get** node, and add an **INPUT.CameraQuery** input.

Drag the **INPUT.CameraQuery** pin to an empty space on the graph to open the **Source Filtering** menu. The first entry is specific to the data interface selected, and when expanded, lists all the methods that are available on that data interface.

[![New Map Get with Camera Query input](https://dev.epicgames.com/community/api/documentation/image/29615f0a-649a-421f-aa84-f4834dffaeda?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/29615f0a-649a-421f-aa84-f4834dffaeda?resizing_type=fit)

For this example, click **Get Camera Properties CPU/GPU**. This provides the **Camera Position**, **Forward Vector**, **Up Vector**, and **Right Vector** (all in World context). You can use this data to apply an offset towards or away from the camera.

[![Get Camera Properties CPU/GPU](https://dev.epicgames.com/community/api/documentation/image/1465ee5e-b2be-4245-94aa-10a3141fcb64?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1465ee5e-b2be-4245-94aa-10a3141fcb64?resizing_type=fit)

Add an **INPUT.Float** to the **Map Get**, and name it something descriptive (for example, **CameraOffsetScale**).

[![INPUT.Float connected to INPUT.CameraOffsetScale](https://dev.epicgames.com/community/api/documentation/image/7590f0c0-c22e-471e-b99d-bcb189e08ce3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7590f0c0-c22e-471e-b99d-bcb189e08ce3?resizing_type=fit)

Use a **Multiply** node to multiply the**Forward Vector World** by the new **INPUT.CameraOffsetScale** float.

[![Multiply Camera Properties by Camera Offset Scale float](https://dev.epicgames.com/community/api/documentation/image/95359a87-8497-4633-b551-1aad3024fec9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/95359a87-8497-4633-b551-1aad3024fec9?resizing_type=fit)

Add the **LOCAL.Offset** to the **Map Get** node. Add it to the **Multiply** node's result.

[![Add Local Offset to Multiplication result](https://dev.epicgames.com/community/api/documentation/image/e77d1ad8-5292-4cc3-9e43-7af380424d2e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e77d1ad8-5292-4cc3-9e43-7af380424d2e?resizing_type=fit)

In the Map Set node n this new section, add **LOCAL.Offset**. Then, connect the result of the **Add** node to that **LOCAL.Offset** pin.

[![Addition result connected to Map Set LOCAL.Offset](https://dev.epicgames.com/community/api/documentation/image/dcab4a5a-8082-47c5-8d94-769b4b811f24?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dcab4a5a-8082-47c5-8d94-769b4b811f24?resizing_type=fit)

### Use Data Interface

Click **Apply**, then open the **System Overview** graph. Select the **Apply Offset** scratch module stack entry. The **Details** panel now has a **Camera Query** section with additional options for the user, including the **Camera Offset Scale** float input.

[![Camera Query in Details panel](https://dev.epicgames.com/community/api/documentation/image/a3f28f9d-fca9-4f60-b34f-eca6ec9f7cdc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a3f28f9d-fca9-4f60-b34f-eca6ec9f7cdc?resizing_type=fit)

Change the Camera Offset scale to -200, to see the offset in action.

[![](https://dev.epicgames.com/community/api/documentation/image/796fa08d-a23e-402c-b27b-3dea8c836dd2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/796fa08d-a23e-402c-b27b-3dea8c836dd2?resizing_type=fit)

Camera Offset Scale set to 0

[![](https://dev.epicgames.com/community/api/documentation/image/cb574e5c-d538-4ce4-8c62-a13a46b775a1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cb574e5c-d538-4ce4-8c62-a13a46b775a1?resizing_type=fit)

Camera Offset Scale set to 200

## Hide Fields

As a module author, you can hide fields you don't expect or want the user to change.

In this example, you can expect that the user won’t need to edit the **Player Controller Index** or **Require Current Frame Data** fields. Therefore, you can hide these options.

Open the **Apply Offset** scratch pad module graph. In the **Details** panel (or the **Edit Hierarchy** view), enable the **Advanced Display** option. This determines whether this input should be visible if the user has expanded the **Advanced** section.

[![Advanced Display](https://dev.epicgames.com/community/api/documentation/image/038f3fa6-224a-4a4d-acff-c3029a9bc8c4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/038f3fa6-224a-4a4d-acff-c3029a9bc8c4?resizing_type=fit)

In the **System Overview** graph, select the **Apply Offset** stack entry. In the **Details** panel, the extra data interface information is now hidden inside the Advanced options section. The information can be viewed by opening up the Advanced section of the panel. Click the **arrow**button to expand this section, and click again to collapse it.

[![Advanced panel, Camera Query hidden](https://dev.epicgames.com/community/api/documentation/image/96e0b49a-0692-4be3-996d-2b8f5a8e41b1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/96e0b49a-0692-4be3-996d-2b8f5a8e41b1?resizing_type=fit)

This setup allows more advanced users to change these settings, like if they're working with a split-screen game and want to manually set the camera, while removing clutter for most users that won't need to change those settings.

[![Advanced panel, Camera Query shown](https://dev.epicgames.com/community/api/documentation/image/9be6f19b-03b6-487b-9acb-4abdee30746a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9be6f19b-03b6-487b-9acb-4abdee30746a?resizing_type=fit)

You can use the **Edit Hierarchy** interface to make the **Camera Offset Scale** input available in the **Details** panel even when your **Camera Query** is set to be in the **Advanced** section.

In the scratch pad module graph, open the **Parameters** tab, then open the **Edit Hierarchies** panel. Drag **INPUT.CameraOffsetScale** from the left column into the center column to rearrange the order.

[![Camera Offset Scale in hierarchy](https://dev.epicgames.com/community/api/documentation/image/d7086574-46bc-42b1-a342-a511d0470418?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d7086574-46bc-42b1-a342-a511d0470418?resizing_type=fit)

Click **Apply**. In the **System Overview** graph, select the **Apply Offset** module stack entry. In the **Details** panel, the **Camera Offset Scale** input will be included in the main list of inputs, even with the **Advanced** panel collapsed.

[![Camera Offset Scale in Details panel without Camera Query settings](https://dev.epicgames.com/community/api/documentation/image/bad63322-a533-4e50-9b19-3796e11ef659?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bad63322-a533-4e50-9b19-3796e11ef659?resizing_type=fit)

## User Parameters

User parameters let you change Niagara settings without repeatedly opening and editing the Niagara System or module graph. When a Niagara system is added to a level, the user parameters are available in the asset’s **Details** Panel. This can speed up workflows since users can adjust those parameters directly within the scene’s context.

There is a cost associated with user parameters. Every time a user parameter is adjusted, the parameters get pushed to the corresponding execution context, and all parameters within that same context are updated:

* System & Emitter Spawn
* System & Emitter Update
* Particles Spawn & Particle Updates (per Emitter)
* Simulation Stages

Using a data interface as a user parameter is generally discouraged due to performance concerns. The engine makes a copy of the data interface per instance, and because they are UObjects, they get garbage collected. The main cost of a data interface is when you create an instance. After it’s created, it has the same overhead as if it were elsewhere in the stack.

### Promote Module Input

Module inputs can be promoted to user parameters. To promote a module input, follow these steps:

1. In the System Overview graph's Minimal emitter, select the Apply Offset stack entry.
2. Click the Dynamic Input dropdown next to the Camera Offset Scale input.
3. Search for and click Read from new User parameter.

[![The Read from new User parameter](https://dev.epicgames.com/community/api/documentation/image/d180b7d0-9ba7-41be-bc99-50773967df0f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d180b7d0-9ba7-41be-bc99-50773967df0f?resizing_type=fit)

A new user parameter is created with the same name and value as the **Details** panel field. The display name for this parameter is **USER Camera Offset Scale**. If you want to access this or other user parameters in code or Blueprints, it must be formatted as `USER.CameraOffsetScale` or `User.CameraOffsetScale.`

[![The USER Camera Offset Scale user parameter in the Details panel.](https://dev.epicgames.com/community/api/documentation/image/8a2152ae-e905-4a98-b00c-2aee859dd17d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8a2152ae-e905-4a98-b00c-2aee859dd17d?resizing_type=fit)

### Edit User Parameters

The **Parameters** tab shows user parameters, but they are not editable in that interface. The **User Parameters** tab provides a field for editing values. For this tutorial, change the **USER Camera Offset Scale** back to 0.

[![The USER Camera Offset Scale set to 0 in the User Parameter tab.](https://dev.epicgames.com/community/api/documentation/image/32026322-a42b-49dd-a6a8-20524db1afb2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/32026322-a42b-49dd-a6a8-20524db1afb2?resizing_type=fit)

### Use User Parameters

Open a level, and drag the Niagara system (in this example, **NS\_Minimal**) into the scene. Select the Niagara system in the **Outliner**. In the **Details** panel, expand the **User Parameters** section. The **Camera Offset Scale** user parameter is included in the list. This means a user can set these parameters interactively, in the context of the world, rather than while in the Niagara viewport.

[![The Niagara system in level, and the Camera Offset Scale is available for editing in Details Panel.](https://dev.epicgames.com/community/api/documentation/image/9fde0e93-15dc-4a03-9855-53e2a2dc4919?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9fde0e93-15dc-4a03-9855-53e2a2dc4919?resizing_type=fit)

## Static Switches

Static switches control the flow of the script. They are helpful when you want certain parts of your graph compiled out of your module except under certain circumstances.

### Implement Static Switch

For this example, make a switch for the USER.CameraOffsetScale parameter. It might be something that an end user would rarely use, so the code wouldn’t need to be available in the emitter most of the time.

Open the **Apply Offset** scratch module graph, and go to the section that has the **USER.CameraOffsetScale**.

[![The USER.CameraOffsetScale section of the Apply Offset graph](https://dev.epicgames.com/community/api/documentation/image/52998e02-3d13-4679-88c3-cd5133c5e527?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/52998e02-3d13-4679-88c3-cd5133c5e527?resizing_type=fit)

In this section, right-click and create a **Static Switch** node.

[![The Static Switch node](https://dev.epicgames.com/community/api/documentation/image/ae69dfe6-e7d5-472c-a8a1-9d74ba18be38?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ae69dfe6-e7d5-472c-a8a1-9d74ba18be38?resizing_type=fit)

Rename the Static Switch to something descriptive (for example, **Use Camera Offset**).

The Static Switch expects a type (often numeric, but not always). Add a type by clicking the **Add (+)** pin, then search for and select the **Niagara Parameter Map** type for this example.

[![The Niagara Parameter Map type on the Static Switch node.](https://dev.epicgames.com/community/api/documentation/image/ab39475e-bb51-4728-a06a-4b484f5c561a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ab39475e-bb51-4728-a06a-4b484f5c561a?resizing_type=fit)

Drag the Camera Offset **Map Set** output to the Static Switch node, then drag the Static Switch output to both the**Map Get** and **Map Set** in the Set Position section.

[![](https://dev.epicgames.com/community/api/documentation/image/a811b5e9-d948-4eec-a855-31a8cd23c6a4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a811b5e9-d948-4eec-a855-31a8cd23c6a4?resizing_type=fit)

Use **Ctrl** + **Click** to pick up connection wires and move them to a different pin.

[![](https://dev.epicgames.com/community/api/documentation/image/9cc5fd27-e10d-4fe3-98fd-66da23e15678?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9cc5fd27-e10d-4fe3-98fd-66da23e15678?resizing_type=fit)

Then, connect the **Map Set** of the Transform Into Space section to the **False** pin of the **Static Switch** node.

[![](https://dev.epicgames.com/community/api/documentation/image/dd628a95-2b01-4c9c-a8ff-ea800417c1ad?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dd628a95-2b01-4c9c-a8ff-ea800417c1ad?resizing_type=fit)

If the **Static Switch** is false, it will skip (compile out) the **Camera Offset** section, and go right from the **Transform Into Space** section to the switch and the following **Set Position** section. If it's true, the Camera Offset nodes will be used.

### Static Switch Settings

By default, the **Static Switch** type is a Boolean. Other options are available, but use the default Boolean for this example. The **Default Value** can be set to true or false, but leave it false for this example. The **Expose as** pin can also be left false for this tutorial. Setting it to true will expose a pin for the setting on the node in the graph, creating a way to set that value using data in the graph.

[![The Details panel for the Static Switch.](https://dev.epicgames.com/community/api/documentation/image/0737aee0-5946-44e1-ac9f-e9d24389d3eb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0737aee0-5946-44e1-ac9f-e9d24389d3eb?resizing_type=fit)

### Use the Static Switch

Open the **System Overview** graph, and select the **Apply Offset** scratch module stack entry. The **Details** panel will now have a **Use Camera Offset** option. While set to false, no other camera offset options will appear in the list, and the skipped nodes will not affect the Emitter. The **Camera Data Interface** information has also been removed from the **Advanced** options section.

[![Use Camera Offset static switch in Details panel](https://dev.epicgames.com/community/api/documentation/image/ea708e48-ce24-47d0-adfb-72473e723243?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ea708e48-ce24-47d0-adfb-72473e723243?resizing_type=fit)

While set to true, the **Camera Offset** nodes are compiled, and all the relevant options (both outside and inside the **Advanced** section) are available in the **Details** panel.

[![Use Camera Offset set to true](https://dev.epicgames.com/community/api/documentation/image/5230b6ff-de81-481c-ae74-f6d2900235ea?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5230b6ff-de81-481c-ae74-f6d2900235ea?resizing_type=fit)

## Share Scratch Modules

To share your scratch module with other Niagara systems or with the rest of your team, you need to export your scratch module as a Niagara nodule script asset.

Open the **Apply Offset** graph, and click the **Local Modules** tab. Right-click the listed module's name, then click **Create Asset**.

[![Create asset from scratch module](https://dev.epicgames.com/community/api/documentation/image/22bb8fb6-afdb-4ce3-8ae2-b242b8222b81?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/22bb8fb6-afdb-4ce3-8ae2-b242b8222b81?resizing_type=fit)

This opens the **Create Script As** window. Name your module (for example, **NMS\_ApplyOffset**), and select the folder where you would like this asset to be located. Then, click **Save**.

[![Name and save the script asset](https://dev.epicgames.com/community/api/documentation/image/48f92573-ddeb-40f0-bf3a-8270dae53895?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/48f92573-ddeb-40f0-bf3a-8270dae53895?resizing_type=fit)

  The asset is created, and can be accessed from the Content Browser.

[![NMS_ApplyOffset asset in Content Browser](https://dev.epicgames.com/community/api/documentation/image/a4a9b7da-7a66-4243-bf45-92c61541a761?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a4a9b7da-7a66-4243-bf45-92c61541a761?resizing_type=fit)

  The engine then automatically opens the new Niagara module script asset.

[![Niagara module script asset window](https://dev.epicgames.com/community/api/documentation/image/6edbe7ce-f5a3-4134-8def-64607f0be951?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6edbe7ce-f5a3-4134-8def-64607f0be951?resizing_type=fit)

### Library Exposure

The first thing you'll likely want to change in the Niagara module script asset is the **Library Visibility** flag in the **Script Details** panel.

By default, it's set to Unexposed, which means it does not appear in menus and searches with the **Library Only** option enabled (which is the case by default).

[![Library Visibility set to Unexposed](https://dev.epicgames.com/community/api/documentation/image/c24e5edc-4698-46de-981b-bab9979ebcdc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c24e5edc-4698-46de-981b-bab9979ebcdc?resizing_type=fit)

To demonstrate this, open your Niagara System, and use the Add + button to search for ApplyOffset. The only result will be the Scratch Pad, not the NMS asset we just created (which would be listed as Game).

[![Unexposed NMS asset not visible with Library Only set to true](https://dev.epicgames.com/community/api/documentation/image/33db8117-a571-4c31-b237-566954f61f77?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/33db8117-a571-4c31-b237-566954f61f77?resizing_type=fit)

There are two different ways to handle this, depending on how discoverable you want that Niagara module script asset to be.

#### Unexposed and Library Only Off

One option is to leave the module set to **Unexposed**, and turn the **Library Only** filter option to false on your workstation. This might be preferred if you don't want or need the module to be easily accessible by users with default filter settings. If anyone else wanted to use this module, they would need to know to uncheck the **Library Only** option in their **Add New Module** window as well.

[![Unexposed NMS asset visible with Library Only set to false](https://dev.epicgames.com/community/api/documentation/image/5306b1d0-c8b7-4580-9578-6bd4a084eba6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5306b1d0-c8b7-4580-9578-6bd4a084eba6?resizing_type=fit)

#### Exposed and Library Only On

The other option is to change the Niagara module script asset's **Library Visibility** to **Exposed**. This would make the module much more discoverable, as it would appear in the **Add New Module** menu with the default filtering options in place (**Library Only** set to true). This is ideal for modules that you want to be readily accessible to your team or other end users.

Open the Niagara module script asset, change the **Library Visibility** to **Exposed**, then click **Compile** and **Save**.

[![Library Visibility set to Exposed](https://dev.epicgames.com/community/api/documentation/image/4d57c98b-4e26-4e4d-8848-2695bf91f171?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4d57c98b-4e26-4e4d-8848-2695bf91f171?resizing_type=fit)

To see this in action, open any Niagara system, and click the **Add (+)** button to search for **Apply Offset**. Unlike before, the Niagara module script asset (labeled **Game**) is included in the search results while the **Library Only** option is set to true.

[![Exposed NMS asset visible with Library Only set to true](https://dev.epicgames.com/community/api/documentation/image/26466c31-fb88-4d0c-a5f0-44a902d0d150?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/26466c31-fb88-4d0c-a5f0-44a902d0d150?resizing_type=fit)

### Module Usage Bitmask

Check the new Niagara module script asset's **Module Usage Bitmask** to ensure the visibility settings are appropriate for this module's intended functionality.

### Description Field

Text in the Niagara module script's **Description** field is included in the tooltip that appears when hovering over the module in the **Add New Module** menu. Include any information here that would help a user decide whether or not to use this module. For example, explain what it's meant to do, what circumstances are more or less ideal for this module to be used, and what other factors might make this more or less relevant to your user’s creative or technical goals.

[![Module tooltip with description](https://dev.epicgames.com/community/api/documentation/image/a41d4d89-9329-4b63-b55a-f1506464780a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a41d4d89-9329-4b63-b55a-f1506464780a?resizing_type=fit)

### Note Message

If a Niagara script module is created from a scratch module, the **Note** field is automatically filled with whatever text was included in the scratch module. If your scratch module didn't include any **Note** text, this will be blank. This message appears at the top of the **Details** panel when the module's stack entry is selected within an emitter.

[![The Note Message field](https://dev.epicgames.com/community/api/documentation/image/2c5630c6-7583-47f0-ab68-74d5c57e40bf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2c5630c6-7583-47f0-ab68-74d5c57e40bf?resizing_type=fit)

### Keywords

Keywords help make the Niagara module script more discoverable during menu searches. Keywords should be separated by spaces. The **Keywords** field for the **Apply Offset** Niagara module script could include "offset position camera", which would allow an end user to search for "camera offset" and have **Apply Offset** pop up as an option in the menu.

[![NMS Apply Offset appearing when searching for "camera offset".](https://dev.epicgames.com/community/api/documentation/image/0be32c8c-b997-4f73-ac67-ec37083b563b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0be32c8c-b997-4f73-ac67-ec37083b563b?resizing_type=fit)

## Conclusion

You can use scratch pad modules to directly add new functionality to your emitters and Niagara systems using visual scripting.

For more information about using Niagara, see [Creating Visual Effects](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine) and [Niagara Script Editor Reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/script-editor-reference-for-niagara-effects-in-unreal-engine).

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Scope](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#scope)
* [Emitter-Based Scratch Pad Module](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#emitter-basedscratchpadmodule)
* [System-Based Scratch Pad Module](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#system-basedscratchpadmodule)
* [Niagara Module Script](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#niagaramodulescript)
* [Getting Started](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#gettingstarted)
* [Create a Niagara System](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#createaniagarasystem)
* [Spawn Particles](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#spawnparticles)
* [Fix Dependency Issue](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#fixdependencyissue)
* [Emitter Settings](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#emittersettings)
* [Create a Scratch Pad Module](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#createascratchpadmodule)
* [Navigation](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#navigation)
* [Data Flow](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#dataflow)
* [Add Location Offset](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#addlocationoffset)
* [Get Position Attribute from Particles](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#getpositionattributefromparticles)
* [Add a Vector Input](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#addavectorinput)
* [Data Namespaces](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#datanamespaces)
* [Calculate Location Offset](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#calculatelocationoffset)
* [Update Data](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#updatedata)
* [Apply Graph Changes](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#applygraphchanges)
* [Module Context](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#modulecontext)
* [Set Module Usage Bitmask](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#setmoduleusagebitmask)
* [Particle Spawn and Particle Update](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#particlespawnandparticleupdate)
* [Rotation Offset](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#rotationoffset)
* [Add Node](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#addnode)
* [Create Inputs](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#createinputs)
* [Calculate Rotation Offset](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#calculaterotationoffset)
* [Apply Rotation Offset Changes](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#applyrotationoffsetchanges)
* [Parameters Tabs](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#parameterstabs)
* [Parameters](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#parameters)
* [User Parameters](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#userparameters)
* [View-Dependent Changes & Renaming](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#view-dependentchanges&renaming)
* [Edit Hierarchy Tool](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#edithierarchytool)
* [Defaults](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#defaults)
* [Tooltips](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#tooltips)
* [Display Unit](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#displayunit)
* [Local Parameters](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#localparameters)
* [Split Inputs Between Different Map Gets and Map Sets](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#splitinputsbetweendifferentmapgetsandmapsets)
* [Break & Rearrange](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#break&rearrange)
* [Transformation Space & Position Offset](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#transformationspace&positionoffset)
* [User-Set Transform Space](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#user-settransformspace)
* [Re-Implement Position Offset](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#re-implementpositionoffset)
* [Apply Changes](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#applychanges)
* [Add Comments](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#addcomments)
* [Module Outputs](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#moduleoutputs)
* [Show Parameter Writes](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#showparameterwrites)
* [Use Module Outputs](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#usemoduleoutputs)
* [Create Module Outputs](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#createmoduleoutputs)
* [Set Parameter Directly](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#setparameterdirectly)
* [Dynamic Module Inputs](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#dynamicmoduleinputs)
* [Set Up Dynamic Inputs](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#setupdynamicinputs)
* [Use Dynamic Inputs](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#usedynamicinputs)
* [Considerations](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#considerations)
* [Module Notes](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#modulenotes)
* [Add Module Notes](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#addmodulenotes)
* [View Module Notes](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#viewmodulenotes)
* [Dismiss and Show Notes](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#dismissandshownotes)
* [Managing Parameters](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#managingparameters)
* [Parameter Usage Stats](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#parameterusagestats)
* [Remove Unused Parameters](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#removeunusedparameters)
* [Data Interfaces](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#datainterfaces)
* [Access Data Interfaces](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#accessdatainterfaces)
* [Work With Data Interfaces](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#workwithdatainterfaces)
* [Use Data Interface](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#usedatainterface)
* [Hide Fields](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#hidefields)
* [User Parameters](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#userparameters-2)
* [Promote Module Input](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#promotemoduleinput)
* [Edit User Parameters](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#edituserparameters)
* [Use User Parameters](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#useuserparameters)
* [Static Switches](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#staticswitches)
* [Implement Static Switch](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#implementstaticswitch)
* [Static Switch Settings](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#staticswitchsettings)
* [Use the Static Switch](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#usethestaticswitch)
* [Share Scratch Modules](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#share-scratch-modules)
* [Library Exposure](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#libraryexposure)
* [Unexposed and Library Only Off](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#unexposedandlibraryonlyoff)
* [Exposed and Library Only On](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#exposedandlibraryonlyon)
* [Module Usage Bitmask](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#moduleusagebitmask)
* [Description Field](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#descriptionfield)
* [Note Message](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#notemessage)
* [Keywords](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#keywords)
* [Conclusion](/documentation/en-us/unreal-engine/niagara-scratch-pad-modules-in-unreal-engine?application_version=5.7#conclusion)
