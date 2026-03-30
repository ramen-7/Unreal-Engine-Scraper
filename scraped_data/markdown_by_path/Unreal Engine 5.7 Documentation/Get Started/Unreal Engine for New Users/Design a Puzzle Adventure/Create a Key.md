<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-02-create-a-key-in-unreal-engine?application_version=5.7 -->

# Create a Key

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
7. [Design a Puzzle Adventure](/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine "Design a Puzzle Adventure")
8. Create a Key

# Create a Key

Using blueprints, learn how to create a key that players can pick up.

![Create a Key](https://dev.epicgames.com/community/api/documentation/image/46165b6d-8426-4391-af47-38aef3372c23?resizing_type=fill&width=1920&height=335)

 On this page

In this section, you’ll create your first gameplay object: a Key Blueprint.

To create the functionality for gameplay objects in your level, you’ll use [Blueprint Visual Scripting](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprint-foundations). Blueprints in Unreal Engine are assets with a physical representation and special functionality, like the player being able to pick them up.

The Blueprint Visual Scripting system can be used to create functionality without writing code, as you are using a node-based interface to create a gameplay object’s behavior.

First, you’ll define the key’s in-game actor, adding components that let you configure keys to appear in three different variations: a yellow oval, a blue rectangle, or a red cone. Instead of making separate assets for each variation, Blueprints let you build all of these options into one asset.

Next, you’ll add the key’s behavior — the ability for the player character to pick it up. Picking up objects is one of the most common gameplay mechanics.

Here's an overview of all of the assets you'll make to create a key with three different appearance options and allow a player character to pick up the key:

[![](https://dev.epicgames.com/community/api/documentation/image/9cf334b5-b49e-4dc7-8f56-7412ccfdad1a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9cf334b5-b49e-4dc7-8f56-7412ccfdad1a?resizing_type=fit)

## Before You Begin

Make sure you understand the following topics, covered in previous sections of [Design a Puzzle Adventure](https://dev.epicgames.com/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine):

* Unreal Editor UI, such as the **[Content Browser](https://dev.epicgames.com/documentation/en-us/unreal-engine/BlueprintAPI/ContentBrowser?application_version=5.6)** and **[Viewport](https://dev.epicgames.com/documentation/en-us/unreal-engine/BlueprintAPI/Viewport?application_version=5.6)**.
* An understanding of Blueprints. See the [Blueprint Foundations](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprint-foundations) documentation for more information.

You’ll need the following assets from [Project Setup and Level Blockout](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine):

* A level with blocked-out rooms.

## Define Key Types and Key Attributes

Before you create the key blueprint, you’ll define some key data that the blueprint will use to create the red, yellow, and blue variations.

To represent the different types of keys used in your game, you’ll use both an **Enumeration** and a **Structure**.

| Asset Type | Description |
| --- | --- |
| **Enumerations** | Also known as **enums**, store a list of unique values that you can use across your project. For the key, you will use an enum to define the different key types you can choose from (yellow oval, blue rectangle, red cone). |
| **Structures** | Also known as **structs**, are used to group related information together. For the key, you will use a struct to hold all of the key’s attributes: a mesh (3D model), and material color (red, yellow, blue) to apply to that mesh. |

Each enumerator acts like a label on a container, and the struct is like the contents of each container.

### Define Key Types in an Enum

First, create an Enumeration asset that defines your key variants: Red, Yellow, and Blue.

To create an enum asset, follow these steps:

1. Open the **Content Browser**, or a **Content Drawer**,by using the **Content Drawer** button in the bottom-left corner of Unreal Engine.
2. Create a place to store the blueprints and supporting assets you’ll create in this tutorial. Go to the **Content > AdventureGame > Designer** folder. Right-click in this folder and click **New Folder**.
3. Name the new folder `Blueprints`.
4. In the **Blueprints** folder, create another folder named `Core`.
5. Right-click in the **Core** folder, go to **Blueprint**, and click **Enumeration** from the Create Asset menu. Name the new asset `Enum_KeyType`.

   [![Creating an Enumerator](https://dev.epicgames.com/community/api/documentation/image/f3f55d7f-c2d5-4679-9048-f6e71936f471?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f3f55d7f-c2d5-4679-9048-f6e71936f471?resizing_type=fit)
6. Double-click the asset to open it in a new window.

The Enumeration contains a list of Enumerator options.

To add key types to the enum, follow these steps:

1. Click the **Add Enumerator** button three times to add three new enums to the list.
2. Change the first enumerator’s **Display Name** to `Blue`. Change the second one to `Yellow`, and the third one to `Red`.

   [![Add Enumerator](https://dev.epicgames.com/community/api/documentation/image/96247826-8acd-4a2f-b964-fa44e601ad80?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/96247826-8acd-4a2f-b964-fa44e601ad80?resizing_type=fit)
3. Save the enum asset file by clicking the **Save** button in the top-left corner of the window. Alternatively, use **CTRL + S**.

When you add an enumerator, you are adding an option to the list. Blue, Yellow, and Red are all values you’ll use to distinguish between the different key types.

In comparison to blueprints, you don’t have to compile **data assets** since you are not compiling any functionality.

### Define Key Attributes in a Struct

Next, create a struct that defines the attributes that distinguish each key type: a mesh shape and a color.

To build a Structure (struct) asset, follow these steps:

1. Go to the **Content Browser** again and make sure that you are still in the **Content > AdventureGame > Designer > Core** folder.
2. Right-click anywhere in the **Core** folder, go to **Blueprint**, and click **Structure**. Name this asset `Struct_KeyData`.

   [![Create a Struct](https://dev.epicgames.com/community/api/documentation/image/812b7e71-47b4-4a05-9409-0c8a5b5a24f9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/812b7e71-47b4-4a05-9409-0c8a5b5a24f9?resizing_type=fit)
3. Double-click the new asset to open it in a new window with the struct’s properties.
4. The struct will have a variable by default, named **MemberVar\_0**. Click **Add Variable** to add a second variable.
5. Change the first variable’s name to `Key Material` and the second variable to `Key Mesh`.
6. Each variable has a data **type** assigned to it. This is set to Boolean (a true or false value) by default. You need to change the type of both variables.

   For the **Key Material** variable, click the dropdown that says **Boolean**. Enter `material instance` into the search field, hover over **Material Instance**, and select **Object Reference**.

   [![Material Instance Actor](https://dev.epicgames.com/community/api/documentation/image/97bdf4b4-c478-4c61-b41b-3ef4f3a4210b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/97bdf4b4-c478-4c61-b41b-3ef4f3a4210b?resizing_type=fit)
7. Repeat these steps to change the variable type of **Key Mesh** to **Static Mesh > Object Reference**.

   [![Static Mesh](https://dev.epicgames.com/community/api/documentation/image/192e51fe-21c1-4d24-bb9b-59aa10d483c1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/192e51fe-21c1-4d24-bb9b-59aa10d483c1?resizing_type=fit)
8. **Save** the struct asset file.

[![Struct Key Data](https://dev.epicgames.com/community/api/documentation/image/10555a39-e4f2-4099-a8fe-2fea08c5a665?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/10555a39-e4f2-4099-a8fe-2fea08c5a665?resizing_type=fit)

You have now created two attributes that each key type will use — a Key Material that will set the key color, and a Key Mesh that will set the key shape.

You’ve finished defining what sort of data the key has. Next, you’ll set up the key’s colors and then actually build each key type.

## Create Key Colors

Now that you have the data for blue, yellow, and red key types, you’ll create **Materials** with corresponding colors that you’ll assign to each key type.

In Unreal Engine, a **Material** defines how a surface looks. It controls things like color, texture, shininess, transparency, and more. A **Material Instance** is a copy of a material that uses the material as a foundation, but can override specific settings like colors or textures, without needing to create a brand new material from scratch.

In this example, you will create a base **Material** that defines attributes for all keys in the game. Then, you will create two **Material Instances** of that material to copy all attributes but override the colors.

This section briefly guides you through creating some materials so you can use them throughout this tutorial series; Materials are not explained in detail.

To create a colored Material asset, follow these steps:

1. Go to the **Content Browser**. Navigate to the **Content > AdventureGame > Designer** folder.
2. Right-click in the **Designer** folder and click **New Folder**. Name this folder `Materials`.
3. Go to the **Materials** folder. Right-click in the folder and select **Material** to create a material asset.

   [![Creating a Material](https://dev.epicgames.com/community/api/documentation/image/a6fc5279-b38c-479d-9e30-22bdb86e3e58?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a6fc5279-b38c-479d-9e30-22bdb86e3e58?resizing_type=fit)
4. Change the name of the material asset to `M_BasicColor`.

   The tutorial’s sample level uses the `M_` prefix as a naming convention to identify materials.
5. Double-click the Material to open it. This opens the **Material Editor** in a new window.

The **Material Editor** is a node-based editor, meaning that it’s built with some similarities to Blueprint Visual Scripting. You should see a node called **M\_BasicColor**, which is the main node that you can use to change the properties of this material.

[![Material Window](https://dev.epicgames.com/community/api/documentation/image/89afd88b-55fb-4caa-b7dd-3c8472fcbe9c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/89afd88b-55fb-4caa-b7dd-3c8472fcbe9c?resizing_type=fit)

The **Base Color** property sets the color of this material. You can click the gray color swatch next to **Base Color** to manually set the color.

Instead of using the color picker, you’ll create a **Color** parameter node that you can override in each material instance, therefore making one material that can become many colors. Creating a parameter is like adding a variable — it turns the material color into an editable parameter in a Material Instance.

To create a color parameter node, follow these steps:

1. Next to **Base Color**, you will see a **pin**. Click the pin and drag to an empty area of the graph.

   [![Base Color Material](https://dev.epicgames.com/community/api/documentation/image/b04c8bbc-7bf4-4bae-8f55-8e8fce55c8e1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b04c8bbc-7bf4-4bae-8f55-8e8fce55c8e1?resizing_type=fit)
2. In the dropdown list, type `VectorParameter` into the search field, and select **VectorParameter**.

   This will create a new node that has a color picker. A vector-type variable has three values so you can use it to define the RGB values of a color.
3. The node’s default name, **Param**, is highlighted when you first create the node. Rename the node **Color** to make it easier to identify in your Material Instances.

   If Param isn’t highlighted, click the node, then click the node name to rename it.
4. On the new **Color** node, click the checkered square next to **Default Value** to open a color picker.

   [![Checkered Box on the Color Parameter](https://dev.epicgames.com/community/api/documentation/image/4ba26260-401f-45e5-9875-f0f3c57d47a0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4ba26260-401f-45e5-9875-f0f3c57d47a0?resizing_type=fit)
5. In the Hex sRGB field, change the value to `F7DE0000`, a yellow color, and click OK.

   [![Color Picker](https://dev.epicgames.com/community/api/documentation/image/b7e70bad-fe0b-4779-b808-c269a42d3de5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b7e70bad-fe0b-4779-b808-c269a42d3de5?resizing_type=fit)
6. **Save** and close the Material asset.

Next, you’ll create Material Instances to add more colors without having to recreate the main material.

To create three Material Instances for your key colors, follow these steps:

1. In the **Content Browser**, right-click the `M_BasicColor` asset you created. Near the top of the context menu, click **Create Material Instance**.
2. Name the material instance asset `M_BasicColor_Red`. Double-click the asset to open it.

   [![Material Instance Window](https://dev.epicgames.com/community/api/documentation/image/227df545-5495-4912-94a0-4857f440f9a8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/227df545-5495-4912-94a0-4857f440f9a8?resizing_type=fit)

   You’ll notice this window is different from the Material Editor. This is because a **Material Instance** does not need the full editing suite of a **Material** — instead, it focuses on modifying parameters you defined in the base **Material**.
3. In the **Details** panel, under the **Parameter Groups** at the top, expand **Global Vector Parameter Values**.

   [![Global Vector Parameter Values](https://dev.epicgames.com/community/api/documentation/image/21329db5-5bbd-4bf0-9362-4e12dd6ba07d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/21329db5-5bbd-4bf0-9362-4e12dd6ba07d?resizing_type=fit)
4. You will see a disabled **Color**, which is the VectorParameter node you added to the base material. Click the checkbox next to Color to enable and override it.

   [![Global Vector Parameter Values Color Heading](https://dev.epicgames.com/community/api/documentation/image/cb32223b-1bde-4964-b138-2e4c0af0446c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cb32223b-1bde-4964-b138-2e4c0af0446c?resizing_type=fit)
5. Click on the color swatch next to Color and set the **Hex sRGB** value to `F7005A00`. This changes the material instance to a beautiful, hot-red color!
6. It’s your turn to lead the way! Repeat this process to create two more Material Instances:

   1. Create a Material Instance named `M_BasicColor_Blue`. Override the Color with **Hex sRGB** = `00AFF700` and **Save** the asset.
   2. Create a Material Instance named `M_BasicColor_Yellow`. Keep the base material color, and **Save** the asset.

Material Instance parameters inherited from a Material asset always use the parent material’s values unless you override them. For example, if you open the `M_BasicColor` material and change its color, the `M_BaseColor_Yellow` material instance would also change color; however, the Blue and Red material instances would keep their colors.

## Build the Key Blueprint

Now that you’ve got all the pieces you need, it’s time to create the Key Blueprint. The Key Blueprint is the asset that you can add to a level to create an instanced actor of it, which has the functionality to be picked up by the player.

To create a new blueprint class for your key, follow these steps:

1. Go to the **Content Browser** and navigate to the **Content > AdventureGame > Designer > Blueprints** folder.
2. Create a new folder named `Key`.
3. Go to the **Key** folder. Right-click in the folder and select **Blueprint Class**.
4. Select **Actor** as the parent class.

   [![Pick Parent Class](https://dev.epicgames.com/community/api/documentation/image/d62ad418-6778-4f5e-babc-2f808c1f275d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d62ad418-6778-4f5e-babc-2f808c1f275d?resizing_type=fit)
5. Name this new actor `BP_Key` and double-click to open it.

   The tutorial’s sample level uses the `BP_` prefix as a naming convention to identify blueprint classes.

The **Actor** parent class is commonly used for an object that can be placed in a level — it doesn’t come with additional features like movement, like in the Character parent class, but it can be used to build interactions and logic.

To dock a window in the main editor, drag its tab next to your level’s tab.

Docking Blueprint Editor Window

You need to add a few things to our Key blueprint to make it function properly:

1. A static mesh to visually represent the key in your project.
2. A collision volume that detects when the player is close enough to pick up the key.
3. A way to know what type of key it is.
4. Game logic to determine what happens when the player collides with the key.

Collision is the detection of two objects coming into contact at runtime. Box, capsule, and sphere collisions are shapes used to make these detections.

### Set up the Key’s Components

First, set up the key’s components so you have something to place and interact with in the game world.

To add a collision component and mesh shape to the key, follow these steps:

1. In `BP_Key`, go to the **Viewport** tab.
2. In the **Components** panel in the top-left corner, click **Add** and search for and select **Capsule Collision**.

   [![Capsule Collision Component](https://dev.epicgames.com/community/api/documentation/image/d5586f97-9a34-4203-9d27-2bcc63c68f7d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d5586f97-9a34-4203-9d27-2bcc63c68f7d?resizing_type=fit)

   This is the collision volume that the player can touch to pick up the key. Without this, the player wouldn’t be able to detect the key.

   You could add collision to the key mesh itself, but using a collision shape helps even out complex geometry, improving collision detection and game performance.
3. Select the **Capsule** component and click **Add** again. This time, search for and select a **Sphere** basic shape, and rename it `KeyMesh`.

   By selecting the **Capsule** component and then adding the **Sphere** mesh, the mesh becomes a child of the **Capsule**, and the **Capsule** is the parent of the mesh. The child component inherits all properties from the parent.
4. Set up the **KeyMesh** component:

   1. Select the **KeyMesh** component. In the **Details** panel, go to the **Transform** category. Next to **Scale**, change the values to `0.3` , `0.3`, and `1.0`.

      [![Key Mesh Scale](https://dev.epicgames.com/community/api/documentation/image/69d9f6d2-a477-4083-bfba-f108daba04e6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/69d9f6d2-a477-4083-bfba-f108daba04e6?resizing_type=fit)

      This shrinks the sides of the mesh into an oval shape.
   2. Under the **Collision** category, set **Collision Presets** to **NoCollision**.

      [![Collision Presets](https://dev.epicgames.com/community/api/documentation/image/df9dca7e-bc45-4946-b8e1-a3ec5ff31c5a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/df9dca7e-bc45-4946-b8e1-a3ec5ff31c5a?resizing_type=fit)

      You’ve added collision with the Capsule component, so this turns off collision on the mesh, ensuring the player character can smoothly collect the key without bouncing off the static mesh.
5. Set up the Capsule component:

   * Select the **Capsule** component. In the **Details** panel, under the **Transform** category, set the **Location** to `0.0`, `0.0`, `80.0`.

     This makes the key float above the ground. The mesh moves with the capsule because the mesh is a child component that inherits all properties from its parent component.
   * Under the **Shape** category, set the **Capsule Half** **Height** to `60.0`. This stretches the collision volume to better surround the mesh.
6. In the **Components** panel, select the **DefaultSceneRoot**. Click **Add**, and select **Rotating Movement**. This slowly spins your key to make it more interesting to the player.

   [![Rotating Movement](https://dev.epicgames.com/community/api/documentation/image/f217eef4-332e-4e52-98d6-7356997575ec?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f217eef4-332e-4e52-98d6-7356997575ec?resizing_type=fit)
7. **Save** and **Compile** the blueprint.

### Set Up the Key’s Properties

Your key also needs to store information, like what type of key it is, and what materials and meshes correspond to each type of key.

To set this up, you’ll use the Key Type enum and Key Data struct that you created earlier.

To add a key type variable to the blueprint, follow these steps:

1. Under the **Components** panel, you will see a **My Blueprint** panel. In the **Variables** section, click the plus (**+**) button to add a new variable.
2. Name the variable `KeyType`.
3. By default, its type is **Boolean**. Click the type dropdown, search for **Enum Key Type**, and select it. This variable type is the enum that you created earlier — so it’s time to use it! Here, it means the **KeyType** variable can be set to **Red**, **Yellow**, or **Blue**.

   In blueprints, the variable type is also called the **pin type** because variables appear as pins in nodes.
4. Click the **Eye** next to the **KeyType** variable to make it a public and editable variable. This is important to do so you can edit the value of this variable in the Unreal Editor later and set the type of each key in your level.

   [![Key Type Variable](https://dev.epicgames.com/community/api/documentation/image/c6d234e8-d0b2-4e74-a6ad-5c273bc5e012?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c6d234e8-d0b2-4e74-a6ad-5c273bc5e012?resizing_type=fit)
5. Click **KeyType** to select it. In the **Details** panel, next to the **Category** property, delete **Default** and enter `Setup`.

   This makes the KeyType property appear in the **Details** panel under a category named **Setup**.

   [![Key Type Blue](https://dev.epicgames.com/community/api/documentation/image/dcd0c691-8b8b-490d-a96d-bb1a859173e3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dcd0c691-8b8b-490d-a96d-bb1a859173e3?resizing_type=fit)

Each key type should have a shape and color combination. In the next step, you’ll create a Map variable to define these combinations.

To set up a variable that maps key types to shapes and colors, follow these steps:

1. In the **My Blueprint** panel, add a new variable named **KeyMap**, also of type **Enum Key Type**.
2. With the **KeyMap** variable selected, in the **Details** panel, next to the type dropdown, there’s another menu that sets the variable’s **container type**, or how many values the variable holds. Change the container type to **Map**.

   [![Set Variable Container Type](https://dev.epicgames.com/community/api/documentation/image/942e164f-593d-4a44-a1fa-93c9f59b6369?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/942e164f-593d-4a44-a1fa-93c9f59b6369?resizing_type=fit)
3. When you set the **Map** container, another type dropdown appears next to the container type. This is the type of data stored in each map option. You defined this key data earlier in a struct, so click the dropdown and set the data type to **Struct\_KeyData**.
4. **Compile** the blueprint so you can populate the KeyMap with materials and mesh shapes, setting up a material-mesh pair for each KeyType option.
5. In the **Details** panel, go to the **Default Value** category.
6. Next to **Key Map**, click the **+**button to add a new **element** to the map.
7. Change the **Key Type** from **Blue** to a different color. If you don’t do this, you might not be able to add a new element since an element with the default Key Type already exists.
8. Repeat this two more times to create second and third elements.
9. With your three map elements added, set up your key types with the following values:

   | Key Type | Key Material | Key Mesh |
   | --- | --- | --- |
   | Red | `M_BasicColor_Red` | Cone |
   | Yellow | `M_BasicColor_Yellow` | Sphere |
   | Blue | `M_BasicColor_Blue` | Cube |

   There are multiple meshes named `Cube` and `Sphere` in the project. The correct `Cube` and `Sphere` meshes should appear second in the list when you search for them. When you hover over them, they should have a **Path** of /**Engine/BasicShapes** in their tooltip.

   [![File Path for Cube Static Mesh](https://dev.epicgames.com/community/api/documentation/image/d67d30e0-dd40-4879-92ae-11e87144f925?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d67d30e0-dd40-4879-92ae-11e87144f925?resizing_type=fit)

   Your **KeyMap** should now look like the following:

   [![Key Map Reference](https://dev.epicgames.com/community/api/documentation/image/c5898650-b0d2-4b38-bf39-d853d66aad24?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c5898650-b0d2-4b38-bf39-d853d66aad24?resizing_type=fit)

   Key Map Reference
10. **Save** and **Compile** the blueprint.

Finally, you need a variable that stores a reference to the player character when they touch the key.

To create a variable that stores a reference to another actor, follow these steps:

1. Under the **Variables** section, add a new variable named `OtherActor`.
2. Change its type to **Actor > Object Reference**.
3. In the **Details** panel, change its **Container Type** to **Single**, since you only need to reference one actor who interacts with this key — the player.

Now, the key’s variables should look like the following:

[![Key Variable](https://dev.epicgames.com/community/api/documentation/image/0896a54a-701d-46f9-80a4-8f407077cac9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0896a54a-701d-46f9-80a4-8f407077cac9?resizing_type=fit)

### Test the Key

Give the key a test and see what it looks like so far.

Go back to your level and, in the **Content Browser**, drag `BP_Key` into your level. You’ve created a blueprint that you can add instances of to your game, and that’s worth celebrating! However, it’s still gray.

[![BP_Key Gray](https://dev.epicgames.com/community/api/documentation/image/2fd86697-d780-43a6-9742-7d143301863b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2fd86697-d780-43a6-9742-7d143301863b?resizing_type=fit)

With the key selected, go to the **Details** panel. Look for the **Setup** category you created, and find the **Key Type** property. You can change this from **Blue**, to **Yellow**, to **Red**, but it’s not changing your gray oval key yet.

This is because you’ve added components and data to your key, but those parts are not communicating with each other yet. This is where Blueprint Visual Scripting comes in — you’ll build logic (nodes and wires) to pass information around a blueprint and perform actions with that information.

## Set Key Values With a Blueprint Function

Next, you’ll create a function that connects the KeyMap options to the KeyMesh component, automatically setting the correct mesh shape and material color for a key based on its type.

A **function** is a reusable set of blueprint nodes that performs a specific task. They help keep your node graphs organized and let you execute (or “call”) the same logic multiple times without recreating it. With functions, you can trigger the execution of that part of a blueprint's logic from other blueprints.

Instead of creating the function in the key blueprint, you’ll put it in a new **Blueprint Function Library**, which is a type of Blueprint asset that stores a collection of reusable functions. These functions are not tied to a specific blueprint or actor. Instead, they’re globally accessible across your entire project. Libraries keep useful functions in one place so you don’t have to copy and paste them into multiple blueprints.

To create a Blueprint Function Library with a new function, follow these steps:

1. Go to the **Content Browser** and navigate to **Content > AdventureGame > Designer > Core**.
2. Right-click in the **Core** folder, go to **Blueprint**, and select **Blueprint Function Library**. Name the new asset `BPL_FPGame` and open it.

   [![Create a Blueprint Function Library](https://dev.epicgames.com/community/api/documentation/image/215c72d6-2374-4247-a493-b63cc4994588?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/215c72d6-2374-4247-a493-b63cc4994588?resizing_type=fit)
3. In the **My Blueprint** panel, in the **Functions** section, you start with one new function that’s highlighted. Name it `fnBPLSetKey`.

   [![Adding a New Function](https://dev.epicgames.com/community/api/documentation/image/1e941825-5a53-43a2-97a1-b3ade127454f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1e941825-5a53-43a2-97a1-b3ade127454f?resizing_type=fit)

   The tutorial’s sample project uses a `BPL` label for functions in a blueprint library and an `fn` prefix for functions. This helps identify what SetKey is and where it comes from, and makes it easier to find the function in the node actions list.

Next, set up the function with the inputs and outputs it needs.

**Inputs** are values you pass into a function so it can do its work. They act similarly to variables. The **fnBPLSetKey** function needs to perform actions between the KeyType, KeyMap, and KeyMesh, so these should be inputs.

**Outputs** are information that the function passes back to the blueprint, usually after creating a result. The **fnBPLSetKey** function doesn’t need any outputs.

To add inputs to the **fnBPLSetKey** function, follow these steps:

1. Click the **fnBPLSetKey** function to select it. In the **Details** panel, next to the **Inputs** category, click the **+**button to create a new input.

   Like variables, each input has a name, variable pin type, and container type.
2. Change the input’s name to `Static Mesh Array`.
3. Change its type to a **Static Mesh Component > Object Reference**. In the function’s node graph, notice how the purple function entry node now has a pin with the input you created, and the style of pin reflects the type (static mesh array).
4. Click the **Container Type** dropdown next to the type, and choose **Array**.

   [![BPL Static Mesh Array](https://dev.epicgames.com/community/api/documentation/image/cec7791c-0eff-4f4a-a9f3-d1dfeb582342?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cec7791c-0eff-4f4a-a9f3-d1dfeb582342?resizing_type=fit)

   An **array** is a variable that stores multiple values of the same type in a single container. Each value is stored as an **array element**.
5. Set up another input to match the key’s **KeyMap** property:

   1. Add another input, and name it `KeyMap`.
   2. Click the **Pin Type** dropdown and set it to **Enum Key Type**.
   3. Click the **Container Type** dropdown and select **Map**.
   4. Click the **Value Type** dropdown and set it to **Struct Key Data**.
6. Set up a Key Type input:

   1. Add another input named `Key`.
   2. Set its **Container** to **Single**, and keep its type as **Enum Key Type**.

Your three inputs should now look like this:

[![Final Inputs](https://dev.epicgames.com/community/api/documentation/image/f35339b8-27bb-4b4b-823c-fbfc3f464876?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f35339b8-27bb-4b4b-823c-fbfc3f464876?resizing_type=fit)

Now, you can build the function’s nodes. In the graph panel, you can see the function entry node **fnBPLSetKey** with the inputs you just created — a **Static Mesh Array**, **Key Map**, and **Key**.

Navigating the blueprint graph:

* **Pan:** Right-click and drag.
* **Zoom:** Use the mouse wheel.

To add logic to the function that sets up the keys with a new Key Mesh shape, follow these steps:

1. Drag off the triangle **execution (exec)** pin of this node, search for **For Each Loop**, and select it in the node actions list. This creates a new node connected to the **fnBPLSetKey** node.

   With the **For Each Loop** node, you can perform some actions on each item in an array. Any logic you connect to the Loop Body execution pin runs once per array element. When the loop is done, execution continues through the Completed pin.

   [![EventGraph 01](https://dev.epicgames.com/community/api/documentation/image/79155d28-51ba-47bb-bd3c-7f3d7c38d310?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/79155d28-51ba-47bb-bd3c-7f3d7c38d310?resizing_type=fit)
2. Drag the **Static Mesh Array** pin of the **fnBPLSetKey** node, and connect it to the **Array** pin of the **For Each Loop**.

   [![EventGraph 02](https://dev.epicgames.com/community/api/documentation/image/e02c33cd-2f62-4217-9212-48fb3dd65ba7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e02c33cd-2f62-4217-9212-48fb3dd65ba7?resizing_type=fit)

   The key only has one mesh, but **fnBPLSetKey** uses a static mesh array so you can use it with a variety of level objects. For example, in the next part of this tutorial series, you’ll work with the door blueprint that has two static meshes for the right and left doors.
3. Next, drag the **Key Map** pin of the **fnBPLSetKey** node and search for and select a **Find** node. This node can take a Key Type and pull the corresponding mesh and material from the KeyMap.
4. Right-click the **blue output** pin of the **Find** node, and click **Split Struct Pin**.

   [![Find Node Split Struct Pin](https://dev.epicgames.com/community/api/documentation/image/e0ce61bc-a7e0-4cc5-9708-73e1e9a5af83?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e0ce61bc-a7e0-4cc5-9708-73e1e9a5af83?resizing_type=fit)

   This splits the output into **Key Material** and **Key Mesh**, which are the two variables in `Struct_KeyData`.
5. Connect the **Key** pin of the **fnBPLSetKey** node to the turquoise **Key** pin of the **Find** node.

   [![Connect Key Pin](https://dev.epicgames.com/community/api/documentation/image/d7a04ba6-4cc4-4cfd-831c-2595d7862da9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d7a04ba6-4cc4-4cfd-831c-2595d7862da9?resizing_type=fit)
6. Now, on the **For Each Loop** node, drag from the **Loop Body** pin and search for **Is Valid** under the **Struct** category. Add the **Is Valid** node with a question mark icon (**?**) next to it, since this is the one that you use for struct values.

   [![Connect Loop Body Pin](https://dev.epicgames.com/community/api/documentation/image/d6562f74-29b2-46b4-ae5a-dd75261b022e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d6562f74-29b2-46b4-ae5a-dd75261b022e?resizing_type=fit)

   This node checks if a valid mesh shape was passed into the function. If it is, you’ll set both the static mesh of the object and its material. If not, you’ll only set the material.
7. Connect the **Key Mesh** pin of the **Find** node to the **Input Object** pin of the **Is Valid** node.

   [![Connect Key Mesh Pin](https://dev.epicgames.com/community/api/documentation/image/af9f0091-f510-4d5f-9878-4df0856a1013?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/af9f0091-f510-4d5f-9878-4df0856a1013?resizing_type=fit)
8. In the **Is Valid** node, drag the **Is Valid** pin and toggle the **Context Sensitive** option to false.

   [![Toggle Context Sensitive](https://dev.epicgames.com/community/api/documentation/image/0f954608-e87d-40c1-8a9f-486fb83c0902?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0f954608-e87d-40c1-8a9f-486fb83c0902?resizing_type=fit)
9. Search for and add a **Set Static Mesh** node.
10. From the **For Each Loop** node, drag the **Array Element** pin and connect it to the **Set Static Mesh** node’s **Target** pin.

    The **Target** is the entity the node will act on. You want to execute the Set Static Mesh action on the KeyMesh, so the Static Mesh Array should be the target.
11. From the **Find** node, drag the **Key Mesh** pin and connect it to the **Set Static Mesh** node’s **New Mesh** pin.

The function’s graph should now look like this:

[![EventGraph 03](https://dev.epicgames.com/community/api/documentation/image/025d0984-f6ac-4f6a-98d1-b62f2286cd8d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/025d0984-f6ac-4f6a-98d1-b62f2286cd8d?resizing_type=fit)

You can double-click a wire between two nodes to create an additional connector. Hover over the connector until your cursor turns into four arrows, and then drag the connector to reshape the wires. This can help you position your nodes and lines freely.

[![Blueprint Wire Pivot](https://dev.epicgames.com/community/api/documentation/image/fc9e8d06-03a1-4beb-af44-59399bf46341?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fc9e8d06-03a1-4beb-af44-59399bf46341?resizing_type=fit)

Select a wire and press the **Q** key to straighten the wire.

You’ve set the new mesh shape on the key, now you just need to set the new material as well.

To add logic that sets up the keys with a new Key Material color, follow these steps:

1. Drag the **Set Static Mesh** node’s **Exec** pin and search for the **Set Material** node (in the **Rendering > Material** category) and create it.
2. Drag its **Target** pin to the **Array Element** of the **For Each Loop** node.
3. Drag its **Material** pin to the **Key Material** pin of the **Find** node.

   [![EventGraph 04](https://dev.epicgames.com/community/api/documentation/image/25e3a4b8-2cea-4db8-97e0-e182bcbe4769?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/25e3a4b8-2cea-4db8-97e0-e182bcbe4769?resizing_type=fit)
4. To make sure the material is set when a mesh isn’t provided, connect the **Is Not Valid** pin of the node to the **Set Material** node’s exec pin. Add two connectors to reshape the wire.
5. **Save** and **Compile** the blueprint.

Your complete **fnBPLSetKey** function should now look like this:

Blueprint

Copy full snippet(113 lines long)

To copy this group of nodes into your project, click **Copy Full Snippet**, click a blank area in the corresponding graph in your blueprint, and press **Ctrl** + **V**. Then, connect the function entry node’s pins to the **For Each Loop** and **Find** nodes.

### Initialize the Keys

You are now ready to use the functionality you’ve created inside the key blueprint. First, you will initialize the key based on the KeyType you assign to it.

To **initialize** a Blueprint level object means to set it up when it’s created, either in the viewport or when the game begins.

To initialize the key, follow these steps:

1. Drag the **Exec** pin of the **Construction Script** node and search for the **fnBPLSetKey** function you created earlier.

   [![Add fnBPLSetKey](https://dev.epicgames.com/community/api/documentation/image/efee7f14-f73f-4590-a57f-7828e96ad68f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/efee7f14-f73f-4590-a57f-7828e96ad68f?resizing_type=fit)

   The function node requires a **Static Mesh Array**, **Key Map**, and **Key**, which you will provide from `BP_Key`.
2. In the **My Blueprint** panel, under the **Variables** section, expand the **Setup** category, and drag the **KeyType** variable into the node graph near the function node.

   [![Get Variable Reference Node](https://dev.epicgames.com/community/api/documentation/image/24f04ff5-a973-41f7-bcf5-b62b30848443?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/24f04ff5-a973-41f7-bcf5-b62b30848443?resizing_type=fit)
3. This prompts you if you would like to **Get** or **Set** the value of the variable. In this case, you need to check the type of key this is, so select **Get**.
4. Connect the new **Get Key Type** node’s pin to the **Key** pin of the **Fn BPLSet Key** node.

   [![Connect Get Key Type](https://dev.epicgames.com/community/api/documentation/image/621793d0-b997-400e-b33f-9cfddaa9d753?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/621793d0-b997-400e-b33f-9cfddaa9d753?resizing_type=fit)
5. Repeat the same process for the **KeyMap** variable. Drag it into the node graph and create a **Get** node. Connect the pin of this node to the **KeyMap** pin of the **Fn BPLSet Key** node.

   [![Connect Get Key Map](https://dev.epicgames.com/community/api/documentation/image/94c5c8dc-cf6b-4b61-8be4-5001e7cae9d7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/94c5c8dc-cf6b-4b61-8be4-5001e7cae9d7?resizing_type=fit)
6. Next, from the **Components** panel, drag **KeyMesh** into the graph and create a **Get** node.
7. The **Key Mesh** node contains a single static mesh component reference, but the function node needs an array. Unreal Engine can take care of this for you: connect the **Key Mesh** pin to the **Static Mesh Array** pin of the **Fn BPLSet Key** node.
8. **Save** and **Compile** your blueprint.

  The key’s construction script should now look like this:

Blueprint

Copy full snippet(77 lines long)

If you copy this snippet into your project, you need to connect the **FnBPLSetKey** node to the **Construction Script** node.

### Test the Key’s Functionality

Now, you can test the color-changing functionality you created in your key and new function.

Close down the Blueprint Editor window and go back to the level editor.

Since the default **Key Type** value is **Blue**, your key should be initialized as a blue rectangle.

Select the key actor, and in the **Details** panel, under the **Setup** section, change the **Key Type** between **Yellow** and **Red**. As you change it, you should see your key update its color and shape in the level!

If your rectangle and oval keys appear too large, you may have selected the wrong mesh assets when building the **KeyMap**. Go back to your **KeyMap’s** details and ensure the Sphere and Cube meshes are from the **/Engine/BasicShapes** path.

[![Cube Path](https://dev.epicgames.com/community/api/documentation/image/b8d44eaa-0417-459e-96f4-35505ae0c09e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b8d44eaa-0417-459e-96f4-35505ae0c09e?resizing_type=fit)

## Grant Keys to the Player Character

Your player needs a way to pick up keys, and for other objects to know what keys the player holds. To handle granting and retrieving keys, you’re going to use a **Blueprint Interface**.

### Use a Blueprint Interface to Communicate Between Blueprints

A **Blueprint Interface** stores a list of functions that can be used by each blueprint that has access to the interface. To **implement** an interface means giving your blueprint the ability to respond to a shared set of events (or **messages**).

In a game where player and NPC characters are walking around, the key needs a way to make sure it’s only interacting with the player character. To do this, you'll create a Blueprint Interface to implement in `BP_AdventureCharacter`. This acts like a permission slip that the player blueprint uses to listen to the pick-up-key message.

Blueprint Interfaces are useful when you want different Blueprints to communicate without knowing each other’s details.

To create a Blueprint Interface with two functions, follow these steps:

1. Go to the **Content Browser** and navigate to **Content > AdventureGame > Designer > Blueprints > Core**.
2. Right-click in the **Core** folder, go to **Blueprint**, and create a new **Blueprint Interface**. Name this asset `BPI_PlayerKeys` and open it by double-clicking on it.

   This window looks similar to the Blueprint Editor. On the right side, you have the **My Blueprint** panel that lists all functions in this interface. Below that is the **Details** panel.
3. In the **My Blueprint** panel, there’s already an initial function made for you. Name it `fnBPIAddKey`.
4. Select the function, and in the **Details** panel, under the **Inputs** section, press the **+**button to add a new input.
5. Name the input `KeyType`, and change its type to **Enum Key Type**.

   [![Added Input](https://dev.epicgames.com/community/api/documentation/image/87e5c6d2-5998-4949-8e36-e6fff4104c48?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/87e5c6d2-5998-4949-8e36-e6fff4104c48?resizing_type=fit)
6. Also in the **Details** panel, next to **Category**, enter `Keys`. This makes your function easier to find in the blueprints’ Interfaces list.
7. Next, add a new function in the My Blueprint panel named fnBPIGetKeys, which will handle retrieving keys.

   [![Add New Function](https://dev.epicgames.com/community/api/documentation/image/9925c429-9361-4c7f-9bf2-bf83b52c4b11?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9925c429-9361-4c7f-9bf2-bf83b52c4b11?resizing_type=fit)
8. Select the new **fnBPIGetKeys** function, and in the **Details** panel, under the **Outputs** section, click the **+**button to add a new parameter named **Held Keys**.
9. Change its type to **Enum Key Type**, and the return value to **Array** so it can return the player’s found keys.

   [![Add Input](https://dev.epicgames.com/community/api/documentation/image/4d046a26-906e-4bba-a987-a67cd8d7678a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4d046a26-906e-4bba-a987-a67cd8d7678a?resizing_type=fit)
10. **Save** and **Compile** your interface. You can now close the **BPI\_PlayerKeys** window.

    Since an interface is related to the blueprint system, you need to compile it just like you do with blueprints.

Notice that in the Blueprint Interface, you only created function declarations. Interface functions don’t contain logic themselves, but their setup determines how you can use them in blueprints.

Interface functions without outputs (**fnBPIAddKeys**) act like events, while functions with outputs (**fnBPIGetKeys**) work like regular functions you can add logic to.

### Create a New Player Character

Before adding to the character, you’ll duplicate a default player character that comes with the project to create your own variant. You’ll also need to change your game mode settings to use your new character.

To create a player character to use in your project, follow these steps:

1. Go to the **Content Browser** and navigate to the **Content > AdventureGame > Designer > Blueprints** folder.
2. Create a new folder named `Characters`.
3. Go to the **Content > Variant\_Shooter > Blueprints > FirstPerson** folder.
4. Drag the `BP_ShooterChracter` asset into the **Characters** folder you created, and select **Copy Here**.
5. Right-click the new copy in the **Characters** folder to rename it `BP_AdventureCharacter`.
6. Go to **Edit > Project Settings**. In the left panel, go to **Project > Maps & Modes** settings.
7. Under the **DefaultGameMode** setting, expand **SelectedGameMode**.

   A **Game Mode** asset that defines a set of rules for the world — including the default player character. You will need to change it to use the new character you created. You can change game mode settings here, or by opening the asset itself.
8. Change the **Default Pawn Class** to `BP_AdventureCharacter`.

   [![Default Pawn Class](https://dev.epicgames.com/community/api/documentation/image/160a2579-fee9-4a08-9bc9-02e2427c9147?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/160a2579-fee9-4a08-9bc9-02e2427c9147?resizing_type=fit)
9. Close the **Project Settings** window.

To change game mode settings on a per-level basis instead of for your entire project, use **World Settings**. You can find this tab next to the **Details** panel.

[![World Settings](https://dev.epicgames.com/community/api/documentation/image/43a1de00-013b-4936-ab8e-35a99f6b2076?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/43a1de00-013b-4936-ab8e-35a99f6b2076?resizing_type=fit)

If you can’t see the **World Settings** panel, in the main menu bar, go to **Window**, and select **World Settings**.

### Add the Blueprint Interface to the Player

In this section, you’re going to modify the player character blueprint. This character has many helpful functions and interfaces already set up for you, and you’ll add the **BPI\_PlayerKeys** interface you made earlier to allow them to pick up keys.

Next, you will modify the new `BP_AdventureCharacter` to use keys.

To add the Blueprint Interface functions to the character, follow these steps:

1. Navigate to your new **Characters** folder and open `BP_AdventureCharacter`.
2. You’ll add the **BPI Player Keys** interface to make sure that the player blueprint implements it. In the toolbar at the top of the new window, click the **Class Settings** button.
3. In the **Details** panel on the right-hand side, under the **Interfaces > Implemented Interfaces** section, click **Add**, then select `BPI_PlayerKeys` from the dropdown. This grants your character the ability to implement the **fnBPIGetKeys** and **fnBPIAddKey** functions.

   [![Add Interface](https://dev.epicgames.com/community/api/documentation/image/500dd284-227c-4647-93da-9eedaf64a4f5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/500dd284-227c-4647-93da-9eedaf64a4f5?resizing_type=fit)
4. **Compile** the blueprint so you can use the interface functions. In the Interfaces section of the **My Blueprint** panel, you’ll see a **Keys** category containing **fnBPIAddKey** and **fnBPIGetKey**. It has a yellow icon instead of gray, meaning these functions act like **events**.

### Store Picked Up Keys

The player needs to store the keys they’ve collected, so create a new variable for this. The variable needs to hold up to three keys, so it should be an array.

To create an array variable to store the player’s keys, follow these steps:

1. In the `BP_AdventureCharacter` blueprint, add a new variable to the **Variables** list in the **My Blueprint** panel.
2. Name the variable `Held Keys`.
3. Select the variable, and in the **Details** panel, set the container to an **array** of the type **Enum** **Key Type**. Using an array is important since the player can hold multiple keys simultaneously.

   [![Held Keys Variable](https://dev.epicgames.com/community/api/documentation/image/a67bee95-b18d-4bd6-870b-618f677b770a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a67bee95-b18d-4bd6-870b-618f677b770a?resizing_type=fit)

To add keys to the **Held Keys** array when the player picks up a key, follow these steps:

1. Go to the character’s **Event Graph** tab.
2. Right-click the graph and search for Event **fnBPIAddKey**. This is the event node that executes when the **fnBPIAddKey** function is called.
3. Drag from its execution pin and search for `Array Add`, and select an **Add** node. This node takes a new element and adds it to an array.
4. Add a reference to the **Held Keys** variable by dragging the variable into the Event Graph, and select **Get**.
5. Connect the **Held Keys** node to the **Array Add** node’s **Target Array** input. This pin looks like a square.
6. Connect the Event node’s **Key Type** pin to the Add node’s **New Item** input.

   [![Connect Key Type to Add Node](https://dev.epicgames.com/community/api/documentation/image/73a01d07-475e-459c-9ed2-15bb613d26e7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/73a01d07-475e-459c-9ed2-15bb613d26e7?resizing_type=fit)

Now, when this event function is triggered, the player character adds the provided **Key Type** to their **Held Keys** array.

### Retrieve the Player’s List of Keys

The door you’ll work with in the next part of this tutorial needs to check all of the player’s keys, so add functionality to the player that returns an array of keys they have picked up.

To handle retrieving keys, follow these steps:

1. In the `BP_AdventureCharacter` blueprint, under **My Blueprint > Interfaces**, expand the **Keys** section.

   [![My Blueprint Interfaces](https://dev.epicgames.com/community/api/documentation/image/6c827b92-2082-4900-81bc-c1fdecaa178f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6c827b92-2082-4900-81bc-c1fdecaa178f?resizing_type=fit)

   In the list, **fnBPIGetKeys** has a grey icon, meaning you can use it as a regular function, not just an event.
2. Double-click **fnBPIGetKeys** to open the function’s graph.
3. Add a reference to the **Held Keys** variable by dragging it in and selecting **Get**.
4. Connect the **Get Held Keys** node to the **Return** node’s **Held Keys** pin.

The **fnBPIGetKeys** graph should now look like the following:

[![fnBPIGetKeys](https://dev.epicgames.com/community/api/documentation/image/843a5388-4447-4763-80db-0de42d6689d7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/843a5388-4447-4763-80db-0de42d6689d7?resizing_type=fit)

### Make Keys Detect Collisions With the Player

Next, you will add functionality that triggers the **fnBPIGetKeys** event function when the player picks up a key. This should happen when the player touches the key’s collision volume.

You will add an event that belongs to the **Capsule** collision component. An event triggers when something happens during gameplay. In this case, when the player actor overlaps with the key’s Capsule, the key should perform some actions.

To add an overlap event and check if the overlapping actor is the player, follow these steps:

1. Open your `BP_Key` blueprint and navigate to an empty area of the **EventGraph**.
2. In the **Components** panel, right-click the **Capsule** component and select **Add Event > Add OnComponentBeginOverlap**. The associated node appears in your event graph. This event node triggers if an overlap happens between this and another actor.

   [![Add BeginOverlap](https://dev.epicgames.com/community/api/documentation/image/3b485e58-34fd-4bab-8150-df951aa4b8f3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3b485e58-34fd-4bab-8150-df951aa4b8f3?resizing_type=fit)

   The event node comes with information about that event. For example, the overlapping actor that triggered the event is passed through the **Other Actor** pin.
3. Drag your **OtherActor** variable from the **Variables** list into your graph and select **Set**. A **Set** node saves a new value to that variable.
4. Drag the **Exec** pin of the Event **OnComponentBeginOverlap** node and connect it to the **Exec** input of the **Set Other Actor** node.
5. Drag the **Other Actor** pin of the **Event OnComponentBeginOverlap** node and connect it to the **Other Actor** input of the **Set Other Actor** node.

   [![Adding the Set Other Actor Node](https://dev.epicgames.com/community/api/documentation/image/32bd37e6-4348-4318-b16e-5820338d8999?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/32bd37e6-4348-4318-b16e-5820338d8999?resizing_type=fit)
6. Before you do anything with the key, check if the overlapping actor is the player, since that’s the only character that should be able to collect keys. You know it’s the player if they have the Blueprint Interface.

   Right-click near the **Set** node and add a **Does Object Implement Interface** node.
7. On the **Does Object Implement Interface** node, change the **Interface** pin to **BPI\_PlayerKeys**.
8. Connect the **Test Object** input pin to the **Set Other Actor** node’s blue pin. This pin works like a **Get Other Actor** node.
9. On the **Does Object Implement Interface** node, drag the **Return Value** pin and add a **Branch** node.
10. Connect the **exec** input pin of the **Branch** node to the **Set** node.

    [![Connect to Branch Node](https://dev.epicgames.com/community/api/documentation/image/e361893b-53b0-450b-bad2-0b2b0ab58d75?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e361893b-53b0-450b-bad2-0b2b0ab58d75?resizing_type=fit)

A **Branch** node checks if a condition is true or false so you can execute different actions for each result. Here, you’ll create logic for two scenarios, true and false, based on what happens if the overlapping actor is or isn’t the player.

To call the add-key function when the player has touched the key, follow these steps:

1. If the Branch result is true, the actor can pick up keys, so trigger the interface’s event function. Drag off the **True** pin of the **Branch** node and add an **Fn BPIAdd Key (Message)** node.

   You’re adding a message node instead of a regular function node because when you call a blueprint interface function, you’re sending a message. The **Target** blueprint only responds if it implements that interface.
2. Drag the **Fn BPIAdd Key** node’s **Target** pin and add a **Get Other Actor** node.
3. Drag the **Key Type** pin and add a **Get Key Type** node. This is another way to add variable references.

   [![Add Get Key Type](https://dev.epicgames.com/community/api/documentation/image/9426de8f-9360-4840-b835-e09c75524252?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9426de8f-9360-4840-b835-e09c75524252?resizing_type=fit)
4. When your key is picked up, it should disappear after a short delay so it can’t be picked up again. To handle this, drag the **Fn BPIAdd Key** node’s **exec** pin and add a **Delay** node. Keep the default Duration of `0.2`.
5. When the timer expires your key should disappear, so connect a **Destroy Actor** node to the **Delay** node’s **Completed** pin. Make sure the **Target** is set to **self**, meaning that the key actor should remove itself from the level.

   [![Connecting a Delay Node](https://dev.epicgames.com/community/api/documentation/image/ff8f91fd-ceb3-4db2-8d01-5269229fa263?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ff8f91fd-ceb3-4db2-8d01-5269229fa263?resizing_type=fit)
6. **Save** and **Compile** your blueprint.

You’ll notice you didn’t add any nodes to the **Branch** node’s **False** result. This is because if the overlapping actor doesn’t have the keys interface, they can’t pick up the key, so do nothing.

  The key’s complete event graph should now look like the following:

Blueprint

Copy full snippet(120 lines long)

Here's the asset diagram from the beginning of this page again, but this time it shows a summary of all the assets and functions you've created and how they combine together to create the key's appearance and behavior:

[![](https://dev.epicgames.com/community/api/documentation/image/b3f1046f-d54d-4c63-a76c-3a832dc89322?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b3f1046f-d54d-4c63-a76c-3a832dc89322?resizing_type=fit)

## Test the Final Key

Go back to your level and add a key of each color. You can now try to pick up the keys in-game by walking over them.

To place a key on the floor after dragging it in from the **Content Browser**, press **End**. This snaps the selected level object to the floor.

## Next Up

In the next section, you’ll change the door blueprint to be able to change color like the keys and remain closed unless the player has picked up the corresponding key.

* [![Open Doors with Keys](https://dev.epicgames.com/community/api/documentation/image/a8a6ceb2-292f-4306-9ba4-0121d3fc6dda?resizing_type=fit&width=640&height=640)

  Open Doors with Keys

  Configure the BP\_DoorFrame blueprint so the doors can change color and only open with the matching BP\_Key.](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-03-open-doors-with-keys-in-unreal-engine)

* [types](https://dev.epicgames.com/community/search?query=types)
* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [collision](https://dev.epicgames.com/community/search?query=collision)
* [attributes](https://dev.epicgames.com/community/search?query=attributes)
* [beginner](https://dev.epicgames.com/community/search?query=beginner)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Before You Begin](/documentation/en-us/unreal-engine/designer-02-create-a-key-in-unreal-engine?application_version=5.7#beforeyoubegin)
* [Define Key Types and Key Attributes](/documentation/en-us/unreal-engine/designer-02-create-a-key-in-unreal-engine?application_version=5.7#definekeytypesandkeyattributes)
* [Define Key Types in an Enum](/documentation/en-us/unreal-engine/designer-02-create-a-key-in-unreal-engine?application_version=5.7#definekeytypesinanenum)
* [Define Key Attributes in a Struct](/documentation/en-us/unreal-engine/designer-02-create-a-key-in-unreal-engine?application_version=5.7#definekeyattributesinastruct)
* [Create Key Colors](/documentation/en-us/unreal-engine/designer-02-create-a-key-in-unreal-engine?application_version=5.7#createkeycolors)
* [Build the Key Blueprint](/documentation/en-us/unreal-engine/designer-02-create-a-key-in-unreal-engine?application_version=5.7#buildthekeyblueprint)
* [Set up the Key’s Components](/documentation/en-us/unreal-engine/designer-02-create-a-key-in-unreal-engine?application_version=5.7#setupthekey%E2%80%99scomponents)
* [Set Up the Key’s Properties](/documentation/en-us/unreal-engine/designer-02-create-a-key-in-unreal-engine?application_version=5.7#setupthekey%E2%80%99sproperties)
* [Test the Key](/documentation/en-us/unreal-engine/designer-02-create-a-key-in-unreal-engine?application_version=5.7#testthekey)
* [Set Key Values With a Blueprint Function](/documentation/en-us/unreal-engine/designer-02-create-a-key-in-unreal-engine?application_version=5.7#setkeyvalueswithablueprintfunction)
* [Initialize the Keys](/documentation/en-us/unreal-engine/designer-02-create-a-key-in-unreal-engine?application_version=5.7#initializethekeys)
* [Test the Key’s Functionality](/documentation/en-us/unreal-engine/designer-02-create-a-key-in-unreal-engine?application_version=5.7#testthekey%E2%80%99sfunctionality)
* [Grant Keys to the Player Character](/documentation/en-us/unreal-engine/designer-02-create-a-key-in-unreal-engine?application_version=5.7#grantkeystotheplayercharacter)
* [Use a Blueprint Interface to Communicate Between Blueprints](/documentation/en-us/unreal-engine/designer-02-create-a-key-in-unreal-engine?application_version=5.7#useablueprintinterfacetocommunicatebetweenblueprints)
* [Create a New Player Character](/documentation/en-us/unreal-engine/designer-02-create-a-key-in-unreal-engine?application_version=5.7#createanewplayercharacter)
* [Add the Blueprint Interface to the Player](/documentation/en-us/unreal-engine/designer-02-create-a-key-in-unreal-engine?application_version=5.7#addtheblueprintinterfacetotheplayer)
* [Store Picked Up Keys](/documentation/en-us/unreal-engine/designer-02-create-a-key-in-unreal-engine?application_version=5.7#storepickedupkeys)
* [Retrieve the Player’s List of Keys](/documentation/en-us/unreal-engine/designer-02-create-a-key-in-unreal-engine?application_version=5.7#retrievetheplayer%E2%80%99slistofkeys)
* [Make Keys Detect Collisions With the Player](/documentation/en-us/unreal-engine/designer-02-create-a-key-in-unreal-engine?application_version=5.7#makekeysdetectcollisionswiththeplayer)
* [Test the Final Key](/documentation/en-us/unreal-engine/designer-02-create-a-key-in-unreal-engine?application_version=5.7#testthefinalkey)
* [Next Up](/documentation/en-us/unreal-engine/designer-02-create-a-key-in-unreal-engine?application_version=5.7#nextup)

Related documents

[Code a First-Person Adventure Game

![Code a First-Person Adventure Game](https://dev.epicgames.com/community/api/documentation/image/ffc1a8f8-e7e5-42c0-b4ed-32ce6d3adbbc?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/code-a-firstperson-adventure-game-in-unreal-engine)

[Open Doors with Keys

![Open Doors with Keys](https://dev.epicgames.com/community/api/documentation/image/a8a6ceb2-292f-4306-9ba4-0121d3fc6dda?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/designer-03-open-doors-with-keys-in-unreal-engine)

[Design a Puzzle Adventure

![Design a Puzzle Adventure](https://dev.epicgames.com/community/api/documentation/image/a7b7ff2c-23d0-47a0-8a04-e569209942b0?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine)

[Blueprint Foundations

![Blueprint Foundations](https://dev.epicgames.com/community/api/documentation/image/d5519c66-d202-42af-bd24-b32ac0bbe537?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/blueprint-foundations)
