<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/data-assets-in-unreal-engine?application_version=5.7 -->

# Data Assets

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
5. [Programming with C++](/documentation/en-us/unreal-engine/programming-with-cplusplus-in-unreal-engine "Programming with C++")
6. [Unreal Architecture](/documentation/en-us/unreal-engine/programming-in-the-unreal-engine-architecture "Unreal Architecture")
7. Data Assets

# Data Assets

Information on Data Assets in Unreal Engine.

![Data Assets](https://dev.epicgames.com/community/api/documentation/image/b1324805-7a2b-44d7-b218-f1f8dc5bd2c2?resizing_type=fill&width=1920&height=335)

 On this page

A **Data Asset** is an asset that stores data related to a particular system in an instance of its class.

* **Assets** can be made in the [Content Browser](https://dev.epicgames.com/documentation/en-us/unreal-engine/content-browser-in-unreal-engine) using native classes that inherit from [UDataAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/Engine/UDataAsset?application_version=5.5). If you want data inheritance or a more complex hierarchy, we recommend creating Data Only Blueprint Classes.
* Inheriting from a [Primary Data Asset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/Engine/UPrimaryDataAsset?application_version=5.5) implements a **Primary Asset Id** and has asset bundle support, which allows it to be manually loaded and unloaded from the [Asset Manager](https://dev.epicgames.com/documentation/en-us/unreal-engine/asset-management-in-unreal-engine?application_version=5.5).
* Instances of native subclasses can be created directly as Data Assets in the Unreal editor and will use the name of the native class as the **PrimaryAssetType**.

  [![](https://dev.epicgames.com/community/api/documentation/image/7e903289-c475-4a9e-aa3f-d9d8db215072?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7e903289-c475-4a9e-aa3f-d9d8db215072?resizing_type=fit)

  In the image above, when creating a new data asset in the editor, you will be prompted to choose from a list of native subclasses.
* [Blueprint](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine)
  subclasses can be created to add variables and then subclassed again by
  Data Only Blueprint that sets those variables. With Blueprint
  subclasses, we recommend using Data Only Blueprints instead of the Data
  Asset instance to handle data inheritance and update the parent class.

## Creating a Data Asset

To inherit or create your own **Data Asset**, follow the steps below:

1. Navigate to **Tools** > **New C++ Class** then create a new class based on a **DataAsset**.

   [![](https://dev.epicgames.com/community/api/documentation/image/465aac96-b6b5-47ca-935b-adafea5c06a8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/465aac96-b6b5-47ca-935b-adafea5c06a8?resizing_type=fit)
2. Add your class data members.

   C++

   ```
   USTRUCT()
           struct FMyAssetInfo {
               GENERATED_BODY()
   				 
               UPROPERTY(EditAnywhere)
               FString AssetName;
   				 
               UPROPERTY(EditAnywhere)
               UTexture2D* AssetThumbnail;
   				
   ```

   Expand code  Copy full snippet(22 lines long)
3. Build your project.
4. In the Unreal editor, right-click on the **Content Browser**, then select **Miscellaneous** > **Data Asset**.

   [![](https://dev.epicgames.com/community/api/documentation/image/89d1a0c3-02b5-4da2-9711-052dbf182dfe?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/89d1a0c3-02b5-4da2-9711-052dbf182dfe?resizing_type=fit)
5. When prompted to choose your class for the data asset instance, your asset should be populated in the list.

   [![](https://dev.epicgames.com/community/api/documentation/image/a35ee545-4b23-49f9-8179-5ab906d469d7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a35ee545-4b23-49f9-8179-5ab906d469d7?resizing_type=fit)
6. Open your **Data Asset Blueprint** to observe the member variables.

   [![](https://dev.epicgames.com/community/api/documentation/image/d6f221dc-a125-43f5-b78a-ca2ab5170605?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d6f221dc-a125-43f5-b78a-ca2ab5170605?resizing_type=fit)

When using [Property Specifiers](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-uproperties), you can observe all of your member variables in an asset so designers can modify the data directly from the editor.

## Primary Data Asset

A **Primary Data Asset** is a Data Asset that implements a `GetPrimaryAssetId` function and has asset bundle support, which allows it to be manually loaded/unloaded from the Asset Manager.

The **PrimaryAssetType** is equal to the name of the first native class going up the hierarchy or the highest-level Blueprint class. For example, if you have a `UPrimaryDataAsset` **->** `UParentNativeClass` **->** `UChildNativeClass` **->** `DataOnlyBlueprintClass`, then the type will be a `ChildNativeClass`.

Alternatively, if you have a `UPrimaryDataAsset` **->** `ParentBlueprintClass` **->** `DataOnlyBlueprintClass`, then the type will be a `ParentBlueprintClass`.

To change this behavior, you can override the `GetPrimaryAssetId` function in your native class or copy those functions into a different native base class.

### Creating a Primary Data Asset

To inherit or create your own Primary Data Asset, follow the steps below:

1. Navigate to **Tools** > **New C++ Class,** then create a new class based on a PrimaryDataAsset.
2. Add your class members and override the **GetPrimaryAssetID** function.

   C++

   ```
   UCLASS()
            class PROJECTExample_API UExampleDataAsset : public UPrimaryDataAsset {
                GENERATED_BODY()
   			 
                UPROPERTY(EditAnywhere)
                FString AssetName;
   			 
                UPROPERTY(EditAnywhere)
                UTexture2D* AssetThumbnail;
   			
   ```

   Expand code  Copy full snippet(15 lines long)

## Loading and Unloading Assets

**Unreal Engine** automatically handles [Asset](https://dev.epicgames.com/documentation/en-us/unreal-engine/assets-and-content-packs-in-unreal-engine) loading and unloading to provide developers a method to communicate with the Engine when each asset is needed. However, you may want precise control over when assets are discovered, loaded, and audited. For these cases, we recommend using the [Asset Manager](https://dev.epicgames.com/documentation/en-us/unreal-engine/asset-management-in-unreal-engine?application_version=5.5).

### Asynchronous Asset Loading

Unreal Engine simplifies the process of asynchronously loading asset data. These methods work identically in development and with cooked data on devices, so you do not need to maintain two code paths for loading data on demand.

See [Asynchronous Asset Loading](https://dev.epicgames.com/documentation/en-us/unreal-engine/asynchronous-asset-loading-in-unreal-engine) for documentation.

* [programming](https://dev.epicgames.com/community/search?query=programming)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Creating a Data Asset](/documentation/en-us/unreal-engine/data-assets-in-unreal-engine?application_version=5.7#creating-a-data-asset)
* [Primary Data Asset](/documentation/en-us/unreal-engine/data-assets-in-unreal-engine?application_version=5.7#primary-data-asset)
* [Creating a Primary Data Asset](/documentation/en-us/unreal-engine/data-assets-in-unreal-engine?application_version=5.7#creating-a-primary-data-asset)
* [Loading and Unloading Assets](/documentation/en-us/unreal-engine/data-assets-in-unreal-engine?application_version=5.7#loading-and-unloading-assets)
* [Asynchronous Asset Loading](/documentation/en-us/unreal-engine/data-assets-in-unreal-engine?application_version=5.7#asynchronous-asset-loading)
