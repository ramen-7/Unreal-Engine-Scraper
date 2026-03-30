<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprint-variables-in-unreal-engine?application_version=5.7 -->

# Blueprint Variables

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
5. [Blueprints Visual Scripting](/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine "Blueprints Visual Scripting")
6. [Specialized Blueprint Node Groups](/documentation/en-us/unreal-engine/specialized-blueprint-visual-scripting-node-groups-in-unreal-engine "Specialized Blueprint Node Groups")
7. Blueprint Variables

# Blueprint Variables

Properties that hold a value or reference an Object or Actor in the world.

![Blueprint Variables](https://dev.epicgames.com/community/api/documentation/image/46f50b7d-5552-49ea-ab0b-c44f16cfd67f?resizing_type=fill&width=1920&height=335)

 On this page

**Variables** are properties that hold a value or reference an Object or Actor in the world. These
properties can be accessible internally to the **Blueprint** containing them, or they can be made
accessible externally so that their values can be modified by designers working with instances
of the Blueprint placed in a level.

Variables are displayed as rounded boxes that contain the name of the variable:

![Variable Nodes](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f8ca85ad-e6fa-41e3-859e-bf6374d53741/k2_node_variables.png)

## Variable Types

Variables can be created in a variety of different types, including data types - such as Boolean, integer, and float - as well as reference types for holding things like Objects, Actors, and particular Classes.
Arrays of each variable type can also be created. Each type is color coded for easy identification:

| Variable Type | Color | Example | Represents |
| --- | --- | --- | --- |
| **Boolean** | Maroon |  | True or false value (`bool`). |
| **Byte** | Sherpa blue |  | Whole number value between 0 and 255 (`unsigned char`). |
| **Integer** | Sea green |  | Whole number value between −2,147,483,648 and 2,147,483,647 (`int`). |
| **Integer64** | Moss green |  | Whole number value between −9,223,372,036,854,775,808 and 9,223,372,036,854,775,807 (`long`). |
| **Float** | Yellow green |  | Number value with a decimal such as 0.0553, 101.2887, and -78.322 (`float`). |
| **Name** | Mauve |  | Piece of text used to identify something in the game. |
| **String** | Magenta |  | Group of alphanumeric characters such as `Hello World` (`string`). |
| **Text** | Pink |  | Text that you display to users. Use this type for text that you want to localize. |
| **Vector** | Gold |  | Set of three numbers (X, Y, and Z). This type is useful for 3D coordinates and RGB color data. |
| **Rotator** | Cornflower blue |  | Group of numbers that define rotation in 3D space. |
| **Transform** | Orange |  | Set of data that combines translation (3D position), rotation, and scale. |
| **Object** | Blue |  | Blueprint objects such as Lights, Actors, StaticMeshes, Cameras, and SoundCues. |

## Variables in the My Blueprint Tab

The **My Blueprint** tab allows custom variables to be added to the Blueprint and lists any existing
variables, including component instance variables added in the [Components List](/documentation/en-us/unreal-engine/components-window-in-unreal-engine)
or variables created by promoting a value to a variable in the graph.

![My BLueprint Pane](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d891edb3-17af-428d-b3ce-53ed05ffc12d/myblueprintpane.png)

### Public Variables

To allow a variable to be modified from outside its Blueprint, make it public.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/65594f5f-1878-45a8-ba37-a3d1b3eae701/ht21.png)

By default the eye is closed (private); select the eye to open it and make it public. You can also select or clear the **Instance Editable** box to make the variable private or public.

After you've made the variable public, you can modify its value from the **Details** panel of the Main Editor window.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4aa6eba5-d064-4154-999e-8920f70f904a/ht23.png)

Above, the variable **LightColor** has been set to Editable and we can now set this value in the **Details** panel of the Level Editor.

### Variable Tooltips

You can also add a **Tooltip** for your variables that will appear when mousing over the variable in the editor.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a9c6f813-8b60-400b-bcb8-534223a2fd07/ht25.png)

You can add the **Tooltip** from the **Details** panel of the variable. When doing so, if the variable is set to **Public**, the Eye Icon will change from yellow to green indicating that a Tooltip has been written for the variable.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a00b7b1a-a539-42d8-b9ff-2b8583dd86c3/ht24.png)

### Expose on Spawn

**Expose on Spawn** enables you to set if the variable should be accessible at the time of spawning the Blueprint it sits in.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a8703e3e-55fd-4b1f-b1dc-154954aa1e70/ht26.png)

Above we have a variable called **LightColor** which is a Linear Color property that is set to **Expose on Spawn**. This variable is implemented in a Blueprint for a Point Light that uses the **Set Light Color** node and the **LightColor** variable to determine the color the light should be.

Below, inside a different Blueprint, a script is used to spawn the Point Light Blueprint and since the **LightColor** variable was set to Expose on Spawn, the option to set the value is made available on the **Spawn Actor from Class** node, allowing us to set its color when the light spawns in the game world.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dc1277e8-726f-4e74-87b4-ba79dc2e4246/ht27.png)

### Private Variables

With the **Private** option checked on a variable, this prevents the variable from being modified from external Blueprints.

For example, we have a variable below that is not set to private:

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d9d5ec30-838f-48ec-9ff3-c251294302e2/ht42.png)

Inside another Blueprint, we spawn the Blueprint that contains the variable, then off the **Return Value** we can access our variable.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6cc5505a-73d4-4210-ba35-917a4fa04627/ht43.png)

If we were to set it Private however:

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3b5254ca-90f3-4827-a005-306302e6e0ef/ht41.png)

And spawn the Blueprint again and try to access that variable, we cannot.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/db084e84-2cf1-4a3a-a22b-46ee542f54cf/ht44.png)

### Expose to Cinematics

If you want the value of your variable to be affected by **Sequencer**, select **Expose to Cinematics**.

To learn more about the sequencer, see [Real-Time Compositing with Sequencer](/documentation/en-us/unreal-engine/real-time-compositing-with-sequencer-in-unreal-engine).

## Promoting to Variable

You can also create variables by using **Promote to Variable**.

Right-click any input or output data pins on a Blueprint node and select **Promote to Variable**.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e0522186-18ed-4c7b-9684-78127ca71b3c/ht38.png)

By right-clicking the **New Light Color** pin and selecting **Promote to Variable**, we can assign a variable as the **New Light Color** value.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d8ebdce8-c600-4194-921d-fc234400a347/ht40.png)

Alternatively, you can drag off an input or output pin and select **Promote to Variable**.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/152ef092-0115-4120-b10f-0c4b212ed3bb/ht39.png)

## Accessing Variables in Blueprints

When working with variables in Blueprints, you will access them in one of two ways: by using the **Get** node (referred to as a Getter) to get the value of the variable or by using the **Set** node (referred to as a Setter) to set the value of the variable.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1382b62f-8a52-4f16-b4b3-cbf812cb2064/ht45.png)

You can create a **Set** node (1 above) or **Get** node (2 above) for a variable by right-clicking in the graph and typing either **Set (variable name)** or **Get (variable name)**. Another method you can use is to hold down the **Ctrl** key and drag in the variable from the **MyBlueprint** window to create a **Get** node or hold down the **Alt** key and drag in the variable from **MyBlueprint** window to create a **Set** node.

## Editing Variables

Variable values can be set either as a part of the Blueprint node network or as a default value prior to execution. To set variable default values:

1. Click **Class Defaults** on the Blueprint Editor Toolbar to open the Defaults in the **Details** panel.
2. In the **Details** panel, enter the desired default values to the right of your variable name.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1a1c94bb-ee27-48da-a1fa-0e58d6e2aaaf/blueprint_details_variable_callout.png)

   Above, we highlight our Color variable in which we can set its default color.

If you do not see your variable listed in the defaults, make sure to click **Compile**.

### Renaming Variables

To rename a variable:

1. Right-click the variable name in the **My Blueprint** tab and select **Rename** in the menu that appears.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b1d1e67d-cfce-4a11-9b94-391666fd067e/rename_variable_menu.png)
2. Type the new variable name in the text box and then press **Enter**.

   ![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bfed105f-febc-4fa6-a145-be20fb44e3fd/rename_variable.png)

### Variable Properties

You can set all the properties for a variable in the **Details** panel. Some variables may have more properties than those shown here, such as **Expose to Cinematics** for Vectors or a **Slider Range** for numeric variables like Integers or Floats.

| Property | Description |
| --- | --- |
| **Variable Type** | Set the variable type in the dropdown menu and determine whether or not the variable is an array. |
| **Instance Editable** | Set whether or not it is possible to edit the value of the variable in the **Class Defaults** and the Blueprint's **Details** tab. |
| **Tooltip** | Set the tooltip for the variable. |
| **Private** | Set whether or not this variable should be private and not modified by derived Blueprints. |
| **Category** | Choose from an existing category or type a new Category name. Setting the Category determines where the variable appears in the **Class Defaults**, the **My Blueprint** tab, and the Blueprint's **Details** tab. |
| **Replication** | Choose if the variable's value should or should not be replicated across clients, and if the value is replicated, if there should be a notification by way of a callback function. |

### Advanced Variable Properties

| Property | Description |
| --- | --- |
| **Config Variable** | Read its default value from a config file if it is present? Use this option to customize variable default values and behavior between different projects and configurations. |
| **Transient** | Not serialize and be zero-filled at load. |
| **SaveGame** | Be serialized for saved games. |
| **Advanced Display** | Be hidden in Class Defaults windows by default. |
| **Multi line** | Be capable of displaying multiple lines. To add a new line while editing the variable, press Shift+Enter.  This option applies only to **String** and **Text** variables. |
| **Deprecated**  **Deprecation Message** | Be deprecated. Any nodes that reference the variable will produce a compiler warning indicating that it should be removed or replaced.  (Optional) You can specify a message to include with the warning. For example: `X is no longer supported. Please use Y instead.` |

### Getting and Setting Variable Values

Variables can also be edited as a part of your Blueprint network by way of Get and Set nodes. The easiest way to create these is by dragging a variable from the Variables tab directly into the Event Graph. A small menu will appear asking if you would like to create a Get or Set node.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/de4538e6-0d42-46fd-8793-abfb75eeb5ff/variablegetset.png)

#### Get Nodes

Get nodes supply portions of the network with a variable value. Once created, these nodes can be plugged into any node that takes the appropriate type.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b434ff6d-758e-4d90-8948-858f44451ad4/getvariable.png)

#### Set Nodes

Set nodes enable you to change the value of a variable. Note that these must be called by an execution wire in order to execute.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7aae90b4-6b4c-41a5-a6de-c04da58f511e/setvariable.png)

| **Shortcuts when dragging from the My Blueprint tab** |  |
| --- | --- |
| **Ctrl-drag** | Creates a Get node. |
| **Alt-drag** | Creates a Set node. |

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [blueprint](https://dev.epicgames.com/community/search?query=blueprint)
* [data types](https://dev.epicgames.com/community/search?query=data%20types)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Variable Types](/documentation/en-us/unreal-engine/blueprint-variables-in-unreal-engine?application_version=5.7#variabletypes)
* [Variables in the My Blueprint Tab](/documentation/en-us/unreal-engine/blueprint-variables-in-unreal-engine?application_version=5.7#variablesinthemyblueprinttab)
* [Public Variables](/documentation/en-us/unreal-engine/blueprint-variables-in-unreal-engine?application_version=5.7#publicvariables)
* [Variable Tooltips](/documentation/en-us/unreal-engine/blueprint-variables-in-unreal-engine?application_version=5.7#variabletooltips)
* [Expose on Spawn](/documentation/en-us/unreal-engine/blueprint-variables-in-unreal-engine?application_version=5.7#exposeonspawn)
* [Private Variables](/documentation/en-us/unreal-engine/blueprint-variables-in-unreal-engine?application_version=5.7#privatevariables)
* [Expose to Cinematics](/documentation/en-us/unreal-engine/blueprint-variables-in-unreal-engine?application_version=5.7#exposetocinematics)
* [Promoting to Variable](/documentation/en-us/unreal-engine/blueprint-variables-in-unreal-engine?application_version=5.7#promotingtovariable)
* [Accessing Variables in Blueprints](/documentation/en-us/unreal-engine/blueprint-variables-in-unreal-engine?application_version=5.7#accessingvariablesinblueprints)
* [Editing Variables](/documentation/en-us/unreal-engine/blueprint-variables-in-unreal-engine?application_version=5.7#editingvariables)
* [Renaming Variables](/documentation/en-us/unreal-engine/blueprint-variables-in-unreal-engine?application_version=5.7#renamingvariables)
* [Variable Properties](/documentation/en-us/unreal-engine/blueprint-variables-in-unreal-engine?application_version=5.7#variableproperties)
* [Advanced Variable Properties](/documentation/en-us/unreal-engine/blueprint-variables-in-unreal-engine?application_version=5.7#advancedvariableproperties)
* [Getting and Setting Variable Values](/documentation/en-us/unreal-engine/blueprint-variables-in-unreal-engine?application_version=5.7#gettingandsettingvariablevalues)
* [Get Nodes](/documentation/en-us/unreal-engine/blueprint-variables-in-unreal-engine?application_version=5.7#getnodes)
* [Set Nodes](/documentation/en-us/unreal-engine/blueprint-variables-in-unreal-engine?application_version=5.7#setnodes)
