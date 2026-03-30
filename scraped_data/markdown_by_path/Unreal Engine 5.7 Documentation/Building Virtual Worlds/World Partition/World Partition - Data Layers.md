<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/world-partition---data-layers-in-unreal-engine?application_version=5.7 -->

# World Partition - Data Layers

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
5. [Building Virtual Worlds](/documentation/en-us/unreal-engine/building-virtual-worlds-in-unreal-engine "Building Virtual Worlds")
6. [World Partition](/documentation/en-us/unreal-engine/world-partition-in-unreal-engine "World Partition")
7. World Partition - Data Layers

# World Partition - Data Layers

An introduction to Data Layers and how they can be used in your projects.

![World Partition - Data Layers](https://dev.epicgames.com/community/api/documentation/image/d7edca3d-35d6-4954-85da-1073861a14dc?resizing_type=fill&width=1920&height=335)

 On this page

**Data Layers** is a system within [World Partition](/documentation/en-us/unreal-engine/world-partition-in-unreal-engine) you can use to organize your Actors both in the Editor and at runtime.

[![Sample Level with Data Layers](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bdeaede8-42fe-44c7-97f8-12975839e29c/data-layer-sample-finished.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bdeaede8-42fe-44c7-97f8-12975839e29c/data-layer-sample-finished.png)

A sample level completed using Data Layers.

Using Data Layer Assets and Data Layer Instances, you can dynamically load and unload layers in the Editor to help manage complex worlds. This system serves as a replacement to the previous Layers system found in older versions of Unreal Engine.

With Data Layers, you can separate gameplay elements and environment assets in the Editor. Artists can work on specific elements without interacting with gameplay triggers or objects. Designers can use dynamically loaded layers to design intriguing gameplay and elaborate level transitions.

At runtime, you can toggle Data Layers using Blueprints or C++ code to drive gameplay (such as quests, progression, and in-game events). They are an important tool for managing asset streaming in a World Partition workflow.

## Creating Data Layers

Data Layers are split into two types of assets: Data Layer Assets and Data Layer Instances. Data Layer Assets contain cross world data and are created using the Data Layers Outliner or in the **Content Browser**. Data Layer Instances contain world specific data and are created in the **Data Layers Outliner**.

the Data Layers system requires you to enable **World Partition** in your map. A map can be converted to World Partition by using **Tools > Convert Level** or by using the commandlet. For more information on converting existing levels to World Partition, see [World Partition](/documentation/en-us/unreal-engine/world-partition-in-unreal-engine).

### Data Layer Assets

Data Layer Assets are Unreal Engine assets you can create and view in the Content Browser. They exist at the project level and are not world specific. They contain the following data:

* **Data Layer Name**
* **Data Layer Type**
* **Debug Color**

#### Data Layer Type

Data Layer Assets are set to one of two different types, **Editor** or **Runtime**. You can use **Editor Data Layers** to keep your assets organized within your project. You can load and unload Editor Data Layers from memory, and toggle visibility using the Data Layer Outliner.

[![Data Layer Asset Options](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/52f1af15-d41c-4cc7-8513-de723f34ba2b/data-layers-editor-options.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/52f1af15-d41c-4cc7-8513-de723f34ba2b/data-layers-editor-options.png)

Setting the options for a Data Layer Asset.

Editor and Runtime Data Layers have identical properties when open in the Content Browser.

**Runtime Data Layers** are similar to Editor Data Layers but you can manipulate them at runtime using Blueprints or C++. You can use in-game events to load or unload the assets assigned to them, opening up a variety of options for complex gameplay or level transitions. For example, we used Runtime Data Layers in the [Valley of the Ancient](/documentation/en-us/unreal-engine/valley-of-the-ancient-sample-game-for-unreal-engine) sample to create the transition between the Light World and the Dark World.

![The Light World](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2ae30aae-d92c-461f-9558-9c885081f6de/light-world.png "The Light World")

![The Dark World](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bbae2bb8-bb56-4db7-9cc9-72ee79a544e8/dark-world.png "The Dark World")

The Light World

The Dark World

### Data Layer Instances

**Data Layer Instances** are world-specific instances of a Data Layer Asset. Using instances, a Data Layer Asset can exist in two or more worlds and reference the same assets but specify different instance properties.

For example, you create a neighborhood point of interest (POI) in a world and assign those assets to an Editor Data Layer to keep them organized. You then decorate the POI using holiday-specific assets and assign those to a Runtime Data Layer to enable them to be loaded and unloaded during runtime. In the standard version of your world, you set a Data Layer Instance of the Runtime Data Layer to not be loaded by default and to toggle on a specific date to celebrate an in-game holiday. In the same project, you can then use a separate instance of the Runtime Data Layer that is always enabled to create a holiday-themed version of the POI separate from your standard world.

### Data Layers Outliner

The **Data Layers Outliner** is used to view all of your existing Data Layer Instances and create new Data Layer Assets and Data Layer Instances. To open the Data Layers Outliner, select **Window > World Partition > Data Layer Outliner**.

[![The Data Layer Outliner](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d5b19513-35a7-4377-a1bb-b0514db2de7b/data-layers-outliner.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d5b19513-35a7-4377-a1bb-b0514db2de7b/data-layers-outliner.png)

The Data Layer Outliner.

| **Number** | **Description** |
| --- | --- |
| **1** | Visibility |
| **2** | Data Layer Loaded In Editor |
| **3** | Data Layer Type |
| **4** | Data Layer Name |
| **5** | Data Layer Validation |
| **6** | Data Layer Outliner Options |
| **7** | Data Layer Asset |
| **8** | Is Initially Visible |
| **9** | Is Initially Loaded |
| **10** | Initial Runtime State |

Right-clicking in the Data Layer Outliner opens the context menu:

[![Data Layer Outliner context menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bdbe1cbb-029d-42b1-9d41-88578e8845dd/data-layers-context-menu.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bdbe1cbb-029d-42b1-9d41-88578e8845dd/data-layers-context-menu.png)

The Data Layer Outliner context menu.

| **Selection** | **Description** |
| --- | --- |
| **Create New Data Layer** | Creates a new, empty Data Layer Instance. |
| **Create New Data Layer under "DL\_Sample"** | Creates a new, empty Data Layer Instance as a child of the selected Data Layer. |
| **Add Selected Actors to Selected Data Layer** | Adds the selected Actors to the selected Data Layer Instance. |
| **Move Data Layers To** | Makes an existing Data Layer Instance a child of another Data Layer. |
| **Remove Selected Actors from Selected Data Layers** | Removes the selected Actors from the selected Data Layer Instance. |
| **Delete Selected Data Layers** | Deletes the selected Data Layer. |
| **Rename Selected Data Layers** | Renames the selected Data Layer. Only works with legacy Data Layers. |
| **Select Actors in Data Layer** | Selects all the Actors assigned to the selected Data Layer Instance. |
| **Append Actors in Data Layer to Selection** | Adds the contents of the selected Data Layer Instance to your selection. |
| **Deselect Actors in Data Layer** | Removes the contents of the selected Data Layer from your selection. |
| **Collapse All Data Layers** | Collapse the Data Layer hierarchy. |
| **Expand All Data Layers** | Expands the Data Layer hierarchy. |
| **Make Current Data Layer** | Sets the selected Data Layer as the current Actor Editor Context. For more information on Actor Editor Context, see the [Actor Editor Context](/documentation/en-us/unreal-engine/actor-editor-context-in-unreal-engine) documentation. |
| **Remove Current Data Layer(s)** | Removes the selected Data Layer from the current Actor Editor Context. |
| **Clear Current Data Layers** | Clears all Data Layers from the current Actor Editor Context. |
| **Make All Data Layers Visible** | Sets the visibility of all Data Layer Instances to visible. |

Clicking the gear icon displays the Data Layer Outliner options:

[![Data Layer Outliner oprions](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e1ea1cb9-7056-4c6c-a598-393df4b96689/data-layers-options.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e1ea1cb9-7056-4c6c-a598-393df4b96689/data-layers-options.png)

Data Layer Outliner oprions.

| **Selection** | **Description** |
| --- | --- |
| **Expand All** | Expands the Data Layer hierarchy. |
| **Collapse All** | Collapse the Data Layer hierarchy. |
| **Stack Hierarchy Headers** | Pins the hierarchy items to the top of the outliner. |
| **Only Selection** | Displays only selected Actors in the Outliner. |
| **Hide Editor Data Layers** | Hides Editor Data Layers In the Outliner. |
| **Hide Runtime Data Layers** | Hides Runtime Data Layers in the Outliner. |
| **Hide Actors** | Hides the list of Actors assigned to Data Layers in the Outliner. |
| **Hide Unloaded Actors** | Hides all Actors from Unloaded World Partition cells in the Outliner. |
| **Hide Level Instance Content** | Hides all assets contained inside Level Instances. |
| **Highlight Selected** | Highlights Data Layer Instances that contain the selected Actors. |
| **Allow Runtime Data Layer Editing** | Allows the editing of Runtime Data Layer Instances. |
| **Reset User Settings** | Resets the Data Layer Outliner settings to their default values. |
| **Choose World** | Determines which world's Data Layer instances are being displayed. |

### Updating Legacy Projects using the Data Layers Commandlet

To update an existing project to use Data Layer Assets and Data Layer Instances, use the Data Layer To Asset commandlet:

[![The Data Layer to Asset commandlet](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1d502e97-7b97-435b-8760-a694d73b8333/commandlet-format-data-layer.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1d502e97-7b97-435b-8760-a694d73b8333/commandlet-format-data-layer.png)

The format of the Data Layer to Asset commandlet.

Follow the steps below to use the commandlet:

1. Open a command prompt window.

[![Open a command prompt](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6b42cbb5-0c5b-42d7-9220-2f061be74825/commandlet1.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6b42cbb5-0c5b-42d7-9220-2f061be74825/commandlet1.png)

Open a command prompt.

1. At the prompt, navigate to the location of the `UnrealEditor.exe` file. For example: `C:\Program Files\UE_5.1\Engine\Binaries\Win64`.

[![Navigate to the location of your engine executable](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7e81b308-83be-4123-b941-2f0644733510/commandlet2.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7e81b308-83be-4123-b941-2f0644733510/commandlet2.png)

Navigate to the location of your engine executable.

1. Begin typing the command. Start with the name of the `.exe` file that will run the commandlet, `UnrealEditor.exe`.

[![Begin the commandlet with UnrealEditor.exe](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8a590f49-ba48-4131-8fe5-c556cbe3738c/commandlet3.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8a590f49-ba48-4131-8fe5-c556cbe3738c/commandlet3.png)

Begin the commandlet with UnrealEditor.exe.

1. Add the name of the project.

[![Add the Project Name](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e4440618-f61e-4dc4-9206-58b72b1c7d43/commandlet4.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e4440618-f61e-4dc4-9206-58b72b1c7d43/commandlet4.png)

Add the Project Name, such as UnrealEditor.exe CitySample.

1. Next, add the name of the commandlet to run.

[![Add the commandlet name](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f60c0c45-0ca0-48ba-8434-728c924a6bf7/commandlet5.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f60c0c45-0ca0-48ba-8434-728c924a6bf7/commandlet5.png)

Add the commandlet name. In this example UnrealEditor.exe CitySample -run=DataLayerToAssetCommandlet.

1. Finally, add the name of the level you want to convert and the destination folder.

[![Add the Level name and destination folder](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7ff79d08-7fde-4695-bf23-3e25d930b6f4/commandlet6.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7ff79d08-7fde-4695-bf23-3e25d930b6f4/commandlet6.png)

Finish by add ng the Level name and destination folder. UnrealEditor.exe CitySample -run=DataLayerToAssetCommandlet Small\_CITY\_LVL -DestinationFolder=/Game/DataLayerConversion.

1. Press **Enter** and run the commandlet.

All previous Data Layers are converted to Data Layer Instances and Data Layer Assets. All Actors that were referencing Data Layers previously now reference Data Layer Assets.

This commandlet has the following optional arguments:

| **Optional Argument** | **Description** |
| --- | --- |
| **-Verbose** | Logs additional context when converting. This outputs the conversion information for every Actor with a Data Layer. |
| **-NoSave** | Runs the commandlet without saving changes. |
| **-IgnoreActorLoadingErrors** | Ignores errors when an Actor fails to load during conversion. |

## Using Data Layers

### Creating New Data Layers

To use the Data Layers system in your project, start by creating a Data Layers Asset:

[![Creating a Data Layer Asset](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f3f72378-b7ec-4b31-a12a-815b4197765e/data-layers-content-browser.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f3f72378-b7ec-4b31-a12a-815b4197765e/data-layers-content-browser.png)

Creating a Data Layer Asset.

1. In the **Content Browser**, navigate to the folder where you want to store your Data Layers Asset, right click and select **Miscellaneous > Data Layer** to create the Data Layers Asset.
2. In the **Data Layers Outliner**, right click and select **Create New Data Layer**. This creates a blank Data Layer Instance named **Unknown** in the outliner.
3. Assign your Data Layers Asset to the new instance by opening the drop down menu next to **Data Layers Asset** and selecting your Data Layers Asset.

Alternatively, dragging and dropping a Data Layer Asset into the Data Layer Outliner creates a new Data Layer Instance with the selected Data Layer Asset assigned. Doing this on an existing Data Layer Instance creates a new child Data Layer Instance with the selected Data Layer Asset assigned.

[![Assigning a Data Layer Asset to a Data Layer Instance](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cec21dc9-7578-479b-a808-b68473169850/data-layers-assign-instance.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cec21dc9-7578-479b-a808-b68473169850/data-layers-assign-instance.png)

Assigning a Data Layer Asset to a Data Layer Instance.

### Assigning Actors to Data Layers

You can assign an Actor to a Data Layer by using the following options:

* Add an asset using the context menu in the Data Layers Outliner.
* Add an asset using the **Data Layers** section in the **Details** Panel.

#### Using the Data Layers Outliner

[![Assigning Actors to a Data Layer Instance with the Data Layer Outliner](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fbad1d72-7617-4124-a4f2-1ea5fe69c6ff/data-layers-assigning-selection.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fbad1d72-7617-4124-a4f2-1ea5fe69c6ff/data-layers-assigning-selection.png)

Assigning Actors to a Data Layer Instance using the Data Layer Outliner.

To add assets to a Data Layer Instance using the Data Layers Outliner:

1. Select the assets you want to add to the Data Layer Instance in the **Viewport**.
2. Right click on the Data Layer Instance in the **Data Layers Outliner** that you want to add to and select **Add Selected Actors to Selected Data Layers**.

#### Using the Details Panel

[![Assigning Actors to a Data Layer Instance with the Details Panel](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9803a6e2-6a76-4dd4-89af-a028f9e15433/data-layers-assigning-details.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9803a6e2-6a76-4dd4-89af-a028f9e15433/data-layers-assigning-details.png)

Assigning Actors to a Data Layer Instance using the Details Panel.

To add assets to a Data Layer Instance using the Details panel:

1. Select the assets you want to add to the Data Layer Instance in the **Viewport**.
2. Navigate to the **Data Layers** section of the **Details** and open **Data Layers** Assets.
3. Click the drop down menu for the **Index** you want to change and select the Data Layers Asset you want to assign. This will assign it to the instance of that Data Layers asset.

This method only works when an instance of the selected Data Layers Asset exists in the world.



Using Actor Editor Context in the level editor, you can set any number of Data Layer Instances as Current. All Actors added with this context active are automatically assigned to the Data Layer Instance set as Current. For more information on Actor Editor Context, see A[ctor Editor Context](/documentation/en-us/unreal-engine/actor-editor-context-in-unreal-engine).

### Performance Concerns

Loading too many assets at once using Data Layers can lead to performance issues.

You should monitor Runtime Data Layer Instance usage closely. Widely used assets assigned to too many Runtime Data Layer Instances can degrade World Partition streaming performance.

### Using Data Layers with Blueprints

You can use Blueprints to change the runtime state of Data Layer Assets and Data Layer Instances.

In the example below, pressing and holding the F key will deactivate the **GreyBox** Data Layer and activate the **Ruins** Data Layer.

[![A Blueprint using Data Layers](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/052e1135-0f75-4e78-b48e-371ca5d7f0fe/data-layers-blueprint.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/052e1135-0f75-4e78-b48e-371ca5d7f0fe/data-layers-blueprint.png)

A Blueprint using Data Layers.

The above Blueprint works by doing the following:

1. Pressing and holding the **F** key accesses the **Data Layer Subsystem**.
2. Using the **Set Data Layer Instance Runtime State** node, the state of the **DL\_GreyBox** Data Layer Instance changes to **Loaded**. This makes it loaded but not visible in the level.
3. The second **Set Data Layer Instance Runtime State** node changes the state of the **DL\_Ruins** Data Layer Instance to **Activated**. This makes it loaded and visible.
4. Releasing the **F** key reverses the process and sets both Data Layer Instances back to their original states.

![Sample Level grey box](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/866705ac-f8c6-4adf-9a98-479f335e3004/data-layer-sample-greybox.png)

![Sample Level with content](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e90758a6-de86-48cd-a647-b69504655a07/data-layer-sample-finished.png)

Sample Level grey box

Sample Level with content

### Using Data Layers with C++

Similar to the Blueprint example above, you can access your project's Data Layers using C++. The example code shown below creates an Actor named **ADataLayerActivator**.

```
	UCLASS()
	class ENGINE_API ADataLayerActivator : public AActor
	{
		GENERATED_BODY()
	public:
	virtual void BeginPlay() override
	{
		// In client/server only the server can activate a DataLayer
		if (HasAuthority())
		{
			if (UDataLayerSubsystem* DataLayerSubsystem = UWorld::GetSubsystem<UDataLayerSubsystem>(GetWorld()))
			{
				DataLayerSubsystem->SetDataLayerInstanceRuntimeState(DataLayerToActivate, EDataLayerRuntimeState::Activated);
			}
		}
	}
	private:
		UPROPERTY(EditAnywhere, Category = "DataLayer")
		TObjectPtr<const UDataLayerAsset> DataLayerToActivate;
	};
Copy full snippet
```

When **ADataLayerActivator** calls **BeginPlay**, it references a specific data layer and sets its runtime state to **Active**.

### Using Data Layers with Level Instancing

[Level Instances](/documentation/en-us/unreal-engine/level-instancing-in-unreal-engine) and **Packed Level Blueprints** support Data Layers.

The Actors contained within the Level Instance inherit the Data Layer assigned to its Level Instance Actor by default. Actors within the Level Instance also support additional Data Layers.

Level Instances that contain a reference to a Data Layer Instance not present in the world will not have their Data Layer references carried over.

For example, you can assign a Level Instance that contains the assets to create a house point of interest to a Neighborhood data layer. The Level Instance can also contain holiday-themed items assigned to different holiday data layers only visible when that data layer is enabled.

## Managing Files

Keeping with the World Partition system's goal of minimizing file overlap between users, Data Layers reduce the need for users to check out important files, such as the world map file or Actor files, when changes are made.

Each Data Layer has a display label and an internal unique identifier. Unreal Engine stores this information in a list of Data Layers in the WorldDataLayer file which provides the following benefits:

* Assigning Data Layers to an Actor only affects that Actor's file In a World Partition world using One File Per Actor.
* Renaming a Data Layer only affects its associated label. There is no need to update any Actors associated with the layer.
* Deleting a Data Layer only affects the WorldDataLayer file. Actors previously associated with the deleted Data Layer are automatically cleaned up with no need to modify or save the Actor.

## Debugging and Runtime Overrides

There are several useful console commands for debugging Data Layers during runtime.

| **Console Command** | **Description** |
| --- | --- |
| **wp.DumpDatalayers** | Outputs a list of Data Layers and their runtime state in the log. |
| **wp.Runtime.DebugFilerByDatalayer** | Filters which Data Layer is visible in the runtime hash 2d debug display. |
| **wp.Runtime.SetDataLayerRuntimeState [state] [layer]** | Forces a Data Layer to a specific runtime state. |
| **wp.Runtime.ToggleDataLayerActivation [layer]** | Toggles a specific runtime data layer. |
| **wp.Runtime.ToggleDrawDataLayers** | Displays a list of Data Layers and their states in the main view. |

* [landscape](https://dev.epicgames.com/community/search?query=landscape)
* [data layers](https://dev.epicgames.com/community/search?query=data%20layers)
* [world partition](https://dev.epicgames.com/community/search?query=world%20partition)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Creating Data Layers](/documentation/en-us/unreal-engine/world-partition---data-layers-in-unreal-engine?application_version=5.7#creatingdatalayers)
* [Data Layer Assets](/documentation/en-us/unreal-engine/world-partition---data-layers-in-unreal-engine?application_version=5.7#datalayerassets)
* [Data Layer Type](/documentation/en-us/unreal-engine/world-partition---data-layers-in-unreal-engine?application_version=5.7#datalayertype)
* [Data Layer Instances](/documentation/en-us/unreal-engine/world-partition---data-layers-in-unreal-engine?application_version=5.7#datalayerinstances)
* [Data Layers Outliner](/documentation/en-us/unreal-engine/world-partition---data-layers-in-unreal-engine?application_version=5.7#datalayersoutliner)
* [Updating Legacy Projects using the Data Layers Commandlet](/documentation/en-us/unreal-engine/world-partition---data-layers-in-unreal-engine?application_version=5.7#updatinglegacyprojectsusingthedatalayerscommandlet)
* [Using Data Layers](/documentation/en-us/unreal-engine/world-partition---data-layers-in-unreal-engine?application_version=5.7#usingdatalayers)
* [Creating New Data Layers](/documentation/en-us/unreal-engine/world-partition---data-layers-in-unreal-engine?application_version=5.7#creatingnewdatalayers)
* [Assigning Actors to Data Layers](/documentation/en-us/unreal-engine/world-partition---data-layers-in-unreal-engine?application_version=5.7#assigningactorstodatalayers)
* [Using the Data Layers Outliner](/documentation/en-us/unreal-engine/world-partition---data-layers-in-unreal-engine?application_version=5.7#usingthedatalayersoutliner)
* [Using the Details Panel](/documentation/en-us/unreal-engine/world-partition---data-layers-in-unreal-engine?application_version=5.7#usingthedetailspanel)
* [Performance Concerns](/documentation/en-us/unreal-engine/world-partition---data-layers-in-unreal-engine?application_version=5.7#performanceconcerns)
* [Using Data Layers with Blueprints](/documentation/en-us/unreal-engine/world-partition---data-layers-in-unreal-engine?application_version=5.7#usingdatalayerswithblueprints)
* [Using Data Layers with C++](/documentation/en-us/unreal-engine/world-partition---data-layers-in-unreal-engine?application_version=5.7#usingdatalayerswithc++)
* [Using Data Layers with Level Instancing](/documentation/en-us/unreal-engine/world-partition---data-layers-in-unreal-engine?application_version=5.7#usingdatalayerswithlevelinstancing)
* [Managing Files](/documentation/en-us/unreal-engine/world-partition---data-layers-in-unreal-engine?application_version=5.7#managingfiles)
* [Debugging and Runtime Overrides](/documentation/en-us/unreal-engine/world-partition---data-layers-in-unreal-engine?application_version=5.7#debuggingandruntimeoverrides)
