<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-06-create-a-respawning-pickup-item-in-unreal-engine?application_version=5.7 -->

# Create a Respawning Pickup Item

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
7. [Code a First-Person Adventure Game](/documentation/en-us/unreal-engine/code-a-firstperson-adventure-game-in-unreal-engine "Code a First-Person Adventure Game")
8. Create a Respawning Pickup Item

# Create a Respawning Pickup Item

Learn how to use C++ to create custom pickups and initialize them in your level.

On this page

## Before You Begin

Ensure you’ve completed the following objectives in the previous section, [Manage Items and Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-05-manage-item-and-data-in-an-unreal-engine-game):

* Set up an Item Data Struct, `UDataAsset` class, a Consumable-type Data Asset instance named `DA_Pickup_001`, and a Data Table.

## Create a New Pickup Class

So far, you've learned to define and store an item's structure and data. In this section, you'll learn how to turn this data into an in-game "pickup", a concrete representation of table data that the player can interact with and gain an effect. A pickup could be an equippable gadget, a box that gives them materials, or a powerup that gives them a temporary boost.

To start setting up a pickup class with initial declarations, follow these steps:

1. In the Unreal Editor, go to **Tools** > **New C++ Class**. Select **Actor** as the parent class and name the class `PickupBase`. Click **Create Class**.
2. In Visual Studio, in `PickupBase.h`, add the following statements to the top of the file:

   * `#include ”Components/SphereComponent.h”`. You’ll add a sphere component to the pickup to detect collisions between player and pickup.
   * `#include ”AdventureCharacter.h”`. Add a reference to your first-person character class so you can check for overlaps between the pickup and characters of this class. (This tutorial uses `AdventureCharacter`.)
   * A forward declaration for `UItemDefinition`. This is the associated Data Asset item that each pickup references.

   C++

   ```
   // Copyright Epic Games, Inc. All Rights Reserved.

   #pragma once

   // --- New Code Start --- 
   #include "Components/SphereComponent.h"
   #include "AdventureCharacter.h"
   // --- New Code End --- 
   #include "CoreMinimal.h"
   #include "GameFramework/Actor.h"
   ```

   Expand code  Copy full snippet(15 lines long)
3. In the `UCLASS()` macro above the `APickupBase` class definition, add the `BlueprintType` and `Blueprintable` specifiers to expose it as a base class for creating Blueprints.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | UCLASS(BlueprintType, Blueprintable) |
   |  | class ADVENTUREGAME_API APickupBase : public AActor |
   |  | { |
   ```

   UCLASS(BlueprintType, Blueprintable)
   class ADVENTUREGAME\_API APickupBase : public AActor
   {

   Copy full snippet(3 lines long)
4. Switch to 
   `PickupBase.cpp`.
5. In `PickupBase.cpp`, add an `#include` for `ItemDefinition.h` and `ItemData.h`.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Copyright Epic Games, Inc. All Rights Reserved. |
   |  |  |
   |  | #include "PickupBase.h" |
   |  | #include "ItemDefinition.h" |
   |  | #include "Data/ItemData.h" |
   ```

   // Copyright Epic Games, Inc. All Rights Reserved.
   #include &quot;PickupBase.h&quot;
   #include &quot;ItemDefinition.h&quot;
   #include &quot;Data/ItemData.h&quot; 

   Copy full snippet(5 lines long)

## Initialize the Pickup with Table Data

Your pickup is just a blank Actor, so when the game begins, you need to give it the data it needs to operate properly. The pickup should pull a row of values from the Data Table and save those values in an ItemDefinition Data Asset (the “reference item”).

### Pull Data from a Data Table

To declare the function and properties you need to pull data from the data table, follow these steps:

1. In `PickupBase.h`, in the `public` section, declare a new void function `InitializePickup()`. You’ll use this function to initialize the pickup with values from the Data Table.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | public: |
   |  | // Sets default values for this actor's properties |
   |  | APickupBase(); |
   |  |  |
   |  | // --- New Code Start --- |
   |  | // Initializes this pickup with values from the data table. |
   |  | void InitializePickup(); |
   |  | // --- New Code End --- |
   ```

   public:
   // Sets default values for this actor&#39;s properties
   APickupBase();
   // --- New Code Start ---
   // Initializes this pickup with values from the data table.
   void InitializePickup();
   // --- New Code End --- 

   Copy full snippet(8 lines long)
2. To pull data from the table, the pickup Blueprint needs two properties: the Data Table asset and the Row Name (which you’ve set up to be the same as the item ID).

   In the `protected` section, declare an `FName` property named `PickupItemID`. Give it the `EditInstanceOnly` and `Category = “Pickup | Item Table”` specifiers. This is the ID of this pickup in the associated Data Table.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | protected: |
   |  | // Called when the game starts or when spawned |
   |  | virtual void BeginPlay() override; |
   |  |  |
   |  | // --- New Code Start --- |
   |  | // The ID of this pickup in the associated data table. |
   |  | UPROPERTY(EditInstanceOnly, Category = "Pickup | Item Table") |
   |  | FName PickupItemID; |
   |  | // --- New Code End --- |
   ```

   protected:
   // Called when the game starts or when spawned
   virtual void BeginPlay() override;
   // --- New Code Start ---
   // The ID of this pickup in the associated data table.
   UPROPERTY(EditInstanceOnly, Category = &quot;Pickup | Item Table&quot;)
   FName PickupItemID;
   // --- New Code End ---

   Copy full snippet(9 lines long)

   Pickups shouldn’t have a default item ID, so the `EditInstanceOnly` specifier lets you edit this property in instances of pickups in the world, but not in the archetype (or class default).

   In the `Category` text, the vertical bar (`|`) creates a nested subsection. So in this example, Unreal Engine creates a **Pickup** section with a subsection named **Item Table** in the asset’s **Details** panel.
3. Also in the `protected` section, declare a `TSoftObjectPtr` to a `UDataTable` named `PickupDataTable`. Give it the same specifiers as the `PickupItemID`. This is the Data Table the pickup uses to get its data.

   The Data Table may not be loaded at runtime, so use a `TSoftObjectPtr` here so you can load it asynchronously.

   C++

   ```
   protected:
   	// Called when the game starts or when spawned
   	virtual void BeginPlay() override;

   	// The ID of this pickup in the associated data table.
   	UPROPERTY(EditInstanceOnly, Category = "Pickup | Item Table")
   	FName PickupItemID;

   	// --- New Code Start --- 
   	// Data table that contains this pickup.
   ```

   Expand code  Copy full snippet(13 lines long)
4. Save the header file and switch to `PickupBase.cpp` to implement `InitializePickup()`.

To initialize a pickup, you first need to retrieve a row of item data from the Data Table using the Pickup Item ID. This lookup should only happen if the ID is set and a valid Data Table asset is assigned. `PickupDataTable` is a soft reference and may not be loaded yet, so to validate the data table, you'll first convert that soft reference to an `FSoftObjectPath`

An `FSoftObjectPath` stores an asset’s path without loading it, making it useful for validating soft references before using them.

 To implement the `InitializePickup()` function, follow these steps:

1. In `PickupBase.cpp`, add the function definition for `InitializePickup()`.
2. Convert `PickupDataTable` to a `const FSoftObjectPath` named `TablePath` to verify that it points to a real asset before attempting to load and use it.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Initializes the pickup with values retrieved from the associated data table. |
   |  | void APickupBase::InitializePickup() |
   |  | { |
   |  | // Only initialize if the pickup has valid inputs |
   |  | const FSoftObjectPath TablePath = PickupDataTable.ToSoftObjectPath(); |
   |  |  |
   |  | } |
   ```

   // Initializes the pickup with values retrieved from the associated data table.
   void APickupBase::InitializePickup()
   {
   // Only initialize if the pickup has valid inputs
   const FSoftObjectPath TablePath = PickupDataTable.ToSoftObjectPath();
   }

   Copy full snippet(7 lines long)
3. Inside the function, in an `if` statement, check if the `TablePath` is valid and that `PickupItemID` has a value.

   C++

   ```
   // Initializes the pickup with values retrieved from the associated data table.
   void APickupBase::InitializePickup()
   {
   	// Only initialize if the pickup has valid inputs 
   	const FSoftObjectPath TablePath = PickupDataTable.ToSoftObjectPath();	
   	// --- New Code Start --- 
   	if (!TablePath.IsNull() && !PickupItemID.IsNone())
   	{
   	}
   	// --- New Code End ---
   ```

   Expand code  Copy full snippet(12 lines long)
4. In the `if` statement, declare a new pointer variable to a 
   `UDataTable` named `LoadedDataTable` and use a ternary operator to test `PickupDataTable.IsValid()`, assigning `PickupDataTable.Get()` if it’s already loaded or `PickupDataTable.LoadSynchronous()` if it isn’t.

   C++

   ```
   // Initializes the pickup with values retrieved from the associated data table.
   void APickupBase::InitializePickup()
   {
   	// Only initialize if the pickup has valid inputs 
   	const FSoftObjectPath TablePath = PickupDataTable.ToSoftObjectPath();
   	if (!TablePath.IsNull() && !PickupItemID.IsNone())
   	{
   		// --- New Code Start --- 
   		/* Resolve the table soft reference into a usable data table.
   		   Use the loaded table if available; otherwise load it now. */
   ```

   Expand code  Copy full snippet(16 lines long)

   Call `LoadSynchronous()` on an object to load and return an asset pointer to that object.
5. Use an `if` statement with a `return;` inside to exit the function if `LoadedDataTable` is null.

   C++

   ```
   // Initializes the pickup with values retrieved from the associated data table.
   void APickupBase::InitializePickup()
   {
   	// Only initialize if the pickup has valid inputs 
   	const FSoftObjectPath TablePath = PickupDataTable.ToSoftObjectPath();
   	if (!TablePath.IsNull() && !PickupItemID.IsNone())
   	{
   		/* Resolve the table soft reference into a usable data table.
   		   Use the loaded table if available; otherwise load it now. */
   		UDataTable* LoadedDataTable = PickupDataTable.IsValid()
   ```

   Expand code  Copy full snippet(23 lines long)

   When working with data-driven systems, never assume that assets or references are immediately usable. We recommend checking a reference is assigned, resolve or load it, and then access its data. This strategy prevents silent failures and makes your code more robust to editor state, loading order, and asset changes.

   Through this tutorial, you'll repeat this pattern of "check, resolve, use" any time you're accessing external data.
6. Retrieve the row of values from the Data Table. Declare a const `FItemData` pointer named `ItemDataRow` and set it to the result of calling `FindRow()` on your `LoadedDataTable`. Specify `FItemData` as the type of row to find.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Continue only if the DataTable was successfully loaded |
   |  | if (!LoadedDataTable) |
   |  | { |
   |  | return; |
   |  | } |
   |  |  |
   |  | // --- New Code Start --- |
   |  | // Use the pickup ID to look up and save the corresponding table row |
   |  | const FItemData* ItemDataRow = LoadedDataTable->FindRow<FItemData>(); |
   |  | // --- New Code End --- |
   ```

    // Continue only if the DataTable was successfully loaded
   if (!LoadedDataTable)
   {
   return;
   }
   // --- New Code Start ---
   // Use the pickup ID to look up and save the corresponding table row
   const FItemData\* ItemDataRow = LoadedDataTable-&gt;FindRow&lt;FItemData&gt;();
   // --- New Code End --- 

   Copy full snippet(10 lines long)
7. Add the following two arguments to the `FindRow()` call:

   * An `FName` row name you want to find. Pass the `PickupItemID` as the row name.
   * An `FString`-type context string that you can use for debugging if the row isn’t found. You can use `Text(“My context here.”)` to add a context string, or use `ToString()` to convert the item ID into a context string.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Use the pickup ID to look up and save the corresponding table row |
   |  | const FItemData* ItemDataRow = LoadedDataTable->FindRow<FItemData>(PickupItemID, PickupItemID.ToString()); |
   ```

    // Use the pickup ID to look up and save the corresponding table row
   const FItemData\* ItemDataRow = LoadedDataTable-&gt;FindRow&lt;FItemData&gt;(PickupItemID, PickupItemID.ToString());

   Copy full snippet(2 lines long)
8. Use an `if` statement with a `return;` inside to exit the function if `ItemDataRow` is null.

   C++

   ```
   // Initializes the pickup with values retrieved from the associated data table.
   void APickupBase::InitializePickup()
   {
   	// Only initialize if the pickup has valid inputs 
   	const FSoftObjectPath TablePath = PickupDataTable.ToSoftObjectPath();
   	if (!TablePath.IsNull() && !PickupItemID.IsNone())
   	{
   		/* Resolve the table soft reference into a usable data table.
   		   Use the loaded table if available; otherwise load it now. */
   		UDataTable* LoadedDataTable = PickupDataTable.IsValid()
   ```

   Expand code  Copy full snippet(33 lines long)
9. Check that the Data Asset referenced in the table row is valid so you can retrieve the item's mesh from the Data Asset later in this section of the tutorial.

   Declare a pointer to a `UItemDefinition` Data Asset named `TempItemDefinition` and use the same ternary operator syntax you used earlier.

   C++

   ```
   // Initializes the pickup with values retrieved from the associated data table.
   void APickupBase::InitializePickup()
   {
   	// Only initialize if the pickup has valid inputs 
   	const FSoftObjectPath TablePath = PickupDataTable.ToSoftObjectPath();
   	if (!TablePath.IsNull() && !PickupItemID.IsNone())
   	{
   		/* Resolve the table soft reference into a usable data table.
   		   Use the loaded table if available; otherwise load it now. */
   		UDataTable* LoadedDataTable = PickupDataTable.IsValid()
   ```

   Expand code  Copy full snippet(38 lines long)
10. Add an `if` statement to check that you have a loaded Data Asset before continuing.

    C++

    ```
    		/* Resolve the Data Asset referenced by this table row.
    		Use the Data Asset if available; otherwise load it now.    */
    		UItemDefinition* TempItemDefinition = ItemDataRow->ItemBase.IsValid()
    			? ItemDataRow->ItemBase.Get()
    			: ItemDataRow->ItemBase.LoadSynchronous();

    		// --- New Code Start --- 
    		// Continue only if the Data Asset was successfully loaded 
    		if (!TempItemDefinition)
    		{
    ```

    Expand code  Copy full snippet(13 lines long)

### Create a Reference Item

Once you’ve retrieved the pickup’s row data, create and initialize a Data Asset-type `ReferenceItem` to hold that information.

By saving the data in a reference item like this, Unreal Engine can easily reference that data when it needs to know about the item instead of performing more table data lookups, which is less efficient.

To save a row of table data in a reference item, follow these steps:

1. In `PickupBase.h`, in the `protected` section, declare a `TObjectPtr` to a `UItemDefinition` named `ReferenceItem`. This is a Data Asset that stores the pickup’s data. Give it the `VisibleAnywhere` and `Category = “Pickup | Reference Item”` specifiers.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Data asset associated with this item. |
   |  | UPROPERTY(VisibleAnywhere, Category = "Pickup | Reference Item") |
   |  | TObjectPtr<UItemDefinition> ReferenceItem; |
   ```

   // Data asset associated with this item.
   UPROPERTY(VisibleAnywhere, Category = &quot;Pickup | Reference Item&quot;)
   TObjectPtr&lt;UItemDefinition&gt; ReferenceItem;

   Copy full snippet(3 lines long)
2. Save the header file and switch back to `PickupBase.cpp`.
3. In `InitializePickup()`, after the `if (!TempItemDefinition)` statement,   set `ReferenceItem` to a `NewObject` of type `UItemDefinition`.

   In Unreal Engine, `NewObject<T>()` is a templated function for dynamically creating `UObject`-derived instances at runtime. It returns a pointer to the new object. It usually has the following syntax:

   `T* Object = NewObject<T>(Outer, Class);`

   Where *T* is the type of `UObject` you're creating, *`Outer`* is who owns this object, and *`Class`* is the class of the object you're creating. The `Class` argument is often `T::StaticClass()`, which gives a `UClass` pointer representing *T*'s class type. However, you can often omit both arguments as UE assumes *`Outer`* is the current class and uses *T* to infer the `UClass`.

   Pass `this` as the outer class and the `UItemDefinition::StaticClass()` as the class type to create a base `UItemDefinition`.

   C++

   ```
   // Initializes the pickup with values retrieved from the associated data table.
   void APickupBase::InitializePickup()
   {
   	// Only initialize if the pickup has valid inputs 
   	const FSoftObjectPath TablePath = PickupDataTable.ToSoftObjectPath();
   	if (!TablePath.IsNull() && !PickupItemID.IsNone())
   	{
   		/* Resolve the table soft reference into a usable data table.
   		   Use the loaded table if available; otherwise load it now. */
   		UDataTable* LoadedDataTable = PickupDataTable.IsValid()
   ```

   Expand code  Copy full snippet(47 lines long)
4. To copy the pickup’s information into `ReferenceItem`, set each field in `ReferenceItem` to the associated field from `ItemDataRow`. For the `WorldMesh`, pull the `WorldMesh` property from `TempItemDefinition`.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Build a runtime ItemDefinition object from the data table row |
   |  | ReferenceItem = NewObject<UItemDefinition>(this); |
   |  | // --- New Code Start --- |
   |  | ReferenceItem->ID = ItemDataRow->ID; |
   |  | ReferenceItem->ItemType = ItemDataRow->ItemType; |
   |  | ReferenceItem->ItemText = ItemDataRow->ItemText; |
   |  | ReferenceItem->WorldMesh = TempItemDefinition->WorldMesh; |
   |  | // --- New Code End --- |
   ```

    // Build a runtime ItemDefinition object from the data table row
   ReferenceItem = NewObject&lt;UItemDefinition&gt;(this);
   // --- New Code Start ---
   ReferenceItem-&gt;ID = ItemDataRow-&gt;ID;
   ReferenceItem-&gt;ItemType = ItemDataRow-&gt;ItemType;
   ReferenceItem-&gt;ItemText = ItemDataRow-&gt;ItemText;
   ReferenceItem-&gt;WorldMesh = TempItemDefinition-&gt;WorldMesh;
   // --- New Code End --- 

   Copy full snippet(8 lines long)

### Call InitializePickup()

In `BeginPlay()`, call `InitializePickup()` to initialize the pickup when the game begins.

C++

```
|  |  |
| --- | --- |
|  | // Called when the game starts or when spawned |
|  | void APickupBase::BeginPlay() |
|  | { |
|  | Super::BeginPlay(); |
|  |  |
|  | // Initialize this pickup with default values |
|  | InitializePickup(); |
|  | } |
```

// Called when the game starts or when spawned
void APickupBase::BeginPlay()
{
Super::BeginPlay();
// Initialize this pickup with default values
InitializePickup();
}

Copy full snippet(8 lines long)

Save and build your code.

`PickupBase.cpp` should now look like this:

C++

```
// Copyright Epic Games, Inc. All Rights Reserved.

#include "PickupBase.h"
#include "ItemDefinition.h"
#include "Data/ItemData.h" 

// Sets default values
APickupBase::APickupBase()
{
```

Expand code  Copy full snippet(82 lines long)

## Create In-Game Functionality

Your pickup has the item data it needs, but it still needs to know how to appear and operate in the game world. It needs a mesh for the player to see, a collision volume to determine when the player touches it, and some logic to make the pickup disappear (as if the player picked it up) and respawn after a certain amount of time.

### Add a Mesh Component

Just like you did when setting up the player character in [Add a First-Person Camera, Mesh, and Animation](https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-04-adding-a-firstperson-camera-mesh-and-animation), you’ll use the `CreateDefaultSubobject` template function to create a static mesh object as a child component of your pickup class and then apply the item’s mesh to this component.

To give the base pickup class a static mesh component, follow these steps:

1. In `PickupBase.h`, in the `protected` section, declare a `TObjectPtr` to a `UStaticMeshComponent` named `PickupMeshComponent`. This is the mesh that will represent the pickup in the world.

   You’ll use code to assign the Data Asset’s mesh to this property, so give it the `VisibleDefaultsOnly` and `Category = “Pickup | Mesh”` specifiers so it’s visible, but not editable, in Unreal Editor.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // The mesh component to represent this pickup in the world. |
   |  | UPROPERTY(VisibleDefaultsOnly, Category = "Pickup | Mesh") |
   |  | TObjectPtr<UStaticMeshComponent> PickupMeshComponent; |
   ```

   // The mesh component to represent this pickup in the world.
   UPROPERTY(VisibleDefaultsOnly, Category = &quot;Pickup | Mesh&quot;)
   TObjectPtr&lt;UStaticMeshComponent&gt; PickupMeshComponent;

   Copy full snippet(3 lines long)
2. Save the header file and return to to `PickupBase.cpp`.
3. In the `APickupBase` construction function, set the `PickupMeshComponent` pointer to the result of calling `CreateDefaultSubobject()` of type `UStaticMeshComponent`. In the `Text` argument, name the object `“PickupMesh”`.

   C++

   ```
   // Sets default values
   APickupBase::APickupBase()
   {
    	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
   	PrimaryActorTick.bCanEverTick = true;

   	// --- New Code Start --- 
   	// Create this pickup's mesh component
   	PickupMeshComponent = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("PickupMesh"));
   	// --- New Code End ---
   ```

   Expand code  Copy full snippet(11 lines long)
4. On the next line, to ensure the mesh was properly instantiated, check that `PickupMeshComponent` isn’t null.

   C++

   ```
   check(PickupMeshComponent != nullptr);
   ```

   check(PickupMeshComponent != nullptr);

   Copy full snippet(1 line long)
5. After creating the mesh component, call `SetRootComponent()` to ensure the mesh is the root component.

   C++

   ```
   // Sets default values
   APickupBase::APickupBase()
   {

   	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
   	PrimaryActorTick.bCanEverTick = true;

   	// Create this pickup's mesh component
   	PickupMeshComponent = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("PickupMesh"));
   	check(PickupMeshComponent != nullptr);
   ```

   Expand code  Copy full snippet(16 lines long)

   If you don’t set a root component in C++, Unreal Engine may choose a different one during recompiles or editor restarts, which can break component attachment, transforms, and collision behavior.

Next, apply the item's mesh to the mesh component. You defined `WorldMesh` with a `TSoftObjectPtr`, so in `InitializePickup()`’s implementation, first check that the mesh is loaded before applying it.

To check the mesh is loaded and then apply it, follow these steps:

1. In `InitializePickup()`, after the `ReferenceItem` setup but inside the larger `if` statement, declare a `UStaticMesh` pointer named `LoadedMesh` and use the same ternary operator syntax to resolve `TempItemDefinition`'s `WorldMesh` soft pointer and ensure the mesh is ready to use.

   C++

   ```
   // Initializes the pickup with values retrieved from the associated data table.
   void APickupBase::InitializePickup()
   {
   	// Only initialize if the pickup has valid inputs 
   	const FSoftObjectPath TablePath = PickupDataTable.ToSoftObjectPath();
   	if (!TablePath.IsNull() && !PickupItemID.IsNone())
   	{
   		/* Resolve the table soft reference into a usable data table.
   		   Use the loaded table if available; otherwise load it now. */
   		UDataTable* LoadedDataTable = PickupDataTable.IsValid()
   ```

   Expand code  Copy full snippet(56 lines long)
2. In a new `if` statement, check if `LoadedMesh` is not null.

   C++

   ```
   		// Build a runtime ItemDefinition object from the data table row     
   		ReferenceItem = NewObject<UItemDefinition>(this);
   		ReferenceItem->ID = ItemDataRow->ID;
   		ReferenceItem->ItemType = ItemDataRow->ItemType;
   		ReferenceItem->ItemText = ItemDataRow->ItemText;
   		ReferenceItem->WorldMesh = TempItemDefinition->WorldMesh;

   		// Resolve the item's world mesh from the item definition.
   		// This uses the mesh if it’s already in memory, or loads it if it isn’t.
   		UStaticMesh* LoadedMesh = TempItemDefinition->WorldMesh.IsValid()
   ```

   Expand code  Copy full snippet(20 lines long)
3. In the new `if` statement, set the `PickupMeshComponent` by calling `SetStaticMesh()`, passing `LoadedMesh`:

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Check the mesh is set and can load before using it |
   |  | if (LoadedMesh) |
   |  | { |
   |  | // --- New Code Start --- |
   |  | // Set the pickup's mesh |
   |  | PickupMeshComponent->SetStaticMesh(LoadedMesh); |
   |  | // --- New Code End --- |
   |  | // |
   |  | } |
   ```

    // Check the mesh is set and can load before using it
   if (LoadedMesh)
   {
   // --- New Code Start ---
   // Set the pickup&#39;s mesh
   PickupMeshComponent-&gt;SetStaticMesh(LoadedMesh);
   // --- New Code End ---
   //
   }

   Copy full snippet(9 lines long)
4. Save and build your code.

`PickupBase.cpp` should look like this:

C++

```
// Copyright Epic Games, Inc. All Rights Reserved.

#include "PickupBase.h"
#include "ItemDefinition.h"
#include "Data/ItemData.h" 

// Sets default values
APickupBase::APickupBase()
{
	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
```

Expand code  Copy full snippet(101 lines long)

### Add a Collision Shape

Add a sphere component to act as a collision volume, then enable collision queries on that component.

To set up collision on the pickup, follow these steps:

1. In `PickupBase.h`, in the `protected` section, declare a `TObjectPtr` to a `USphereComponent` named `SphereComponent`. This is the sphere component used for collision detection. Give it the `EditAnywhere`, `BlueprintReadOnly`, and `Category = “Pickup | Components”` specifiers.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Sphere Component that defines the collision radius of this pickup for interaction purposes. |
   |  | UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "Pickup | Components") |
   |  | TObjectPtr<USphereComponent> SphereComponent; |
   ```

   // Sphere Component that defines the collision radius of this pickup for interaction purposes.
   UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = &quot;Pickup | Components&quot;)
   TObjectPtr&lt;USphereComponent&gt; SphereComponent;

   Copy full snippet(3 lines long)
2. Save the header file and return to `PickupBase.cpp`.
3. In the `APickupBase` construction function, after you set the `PickupMeshComponent`, set `SphereComponent` to the result of calling `CreateDefaultSubobject` with `USphereComponent` as the type and `“SphereComponent”` as the name. Add a null `check` afterwards.

   C++

   ```
   // Sets default values
   APickupBase::APickupBase()
   {
    	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
   	PrimaryActorTick.bCanEverTick = true;

   	// Create this pickup's mesh component
   	PickupMeshComponent = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("PickupMesh"));
   	check(PickupMeshComponent != nullptr);
   	// Make the mesh the root component
   ```

   Expand code  Copy full snippet(18 lines long)
4. Now that you have both components, use `SetupAttachment()` to attach the `PickupMeshComponent` to the `SphereComponent`:

   C++

   ```
   // Sets default values
   APickupBase::APickupBase()
   {
    	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
   	PrimaryActorTick.bCanEverTick = true;

   	// Create this pickup's mesh component
   	PickupMeshComponent = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("PickupMesh"));
   	check(PickupMeshComponent != nullptr);
   	// Make the mesh the root component
   ```

   Expand code  Copy full snippet(21 lines long)
5. After attaching the `SphereComponent`, set the sphere’s size using `SetSphereRadius()`. This value should be large enough for the player to intentionally interact with the pickup, but not so large that the player collects the pickup accidentally when passing nearby.

   C++

   ```
   // Sets default values
   APickupBase::APickupBase()
   {
    	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
   	PrimaryActorTick.bCanEverTick = true;

   	// Create this pickup's mesh component
   	PickupMeshComponent = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("PickupMesh"));
   	check(PickupMeshComponent != nullptr);
   	// Make the mesh the root component
   ```

   Expand code  Copy full snippet(24 lines long)
6. After setting the radius, make the sphere generate overlap events by calling `SetGenerateOverlapEvents(true)`.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Configure the sphere to actually generate overlap events |
   |  | SphereComponent->SetGenerateOverlapEvents(true); |
   ```

    // Configure the sphere to actually generate overlap events
   SphereComponent-&gt;SetGenerateOverlapEvents(true);

   Copy full snippet(2 lines long)
7. Make the `SphereComponent` collidable by calling `SetCollisionEnabled()`.

   This function takes an enum (`ECollisionEnabled`) that tells the engine what type of collision to use. You want the character to be able to collide and trigger collision queries with the pickup, but the pickup shouldn’t have any physics that makes it bounce away when hit, so pass the `ECollisionEnabled::QueryOnly` option.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Enable collision |
   |  | SphereComponent->SetCollisionEnabled(ECollisionEnabled::QueryOnly); |
   ```

    // Enable collision
   SphereComponent-&gt;SetCollisionEnabled(ECollisionEnabled::QueryOnly);

   Copy full snippet(2 lines long)
8. You've turned collision on for the sphere, and you also need to define what types of collisions can occur. Collision channels define what types of objects can interact with each other and collision responses define how those interactions are handled.

   Before setting up the sphere's collision responses, call `SetCollisionResponseToAllChannels()` to set the response to every collision channel to `ECR_Ignore` to ensure no engine defaults or presents affect your collision rules.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Set the sphere's response to every collision channel to Ignore, removing any engine defaults |
   |  | SphereComponent->SetCollisionResponseToAllChannels(ECR_Ignore); |
   ```

    // Set the sphere&#39;s response to every collision channel to Ignore, removing any engine defaults
   SphereComponent-&gt;SetCollisionResponseToAllChannels(ECR\_Ignore);

   Copy full snippet(2 lines long)

   The `ECC` prefix is used by the `ECollisionChannels` enum and the `ECR` prefix is used by the `ECollisionResponses` enum. In Unreal Editor, these channels and responses are displayed without prefixes.
9. Now you can set the collision channel responses. The pickup needs query-only collision and overlap responses, but only with the Pawn channel.

   A collision query is a non-physical check such as an overlap or trace, so the pickup can respond to an overlap with the player while letting the character move through it naturally.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Set the sphere's response to every collision channel to Ignore, removing any engine defaults |
   |  | SphereComponent->SetCollisionResponseToAllChannels(ECR_Ignore); |
   |  | // --- New Code Start --- |
   |  | // Overrides the previous collision rule for the Pawn channel, so encountering anything on that channel generates an overlap |
   |  | SphereComponent->SetCollisionResponseToChannel(ECC_Pawn, ECR_Overlap); |
   |  | // --- New Code End --- |
   ```

    // Set the sphere&#39;s response to every collision channel to Ignore, removing any engine defaults
   SphereComponent-&gt;SetCollisionResponseToAllChannels(ECR\_Ignore);
   // --- New Code Start ---
   // Overrides the previous collision rule for the Pawn channel, so encountering anything on that channel generates an overlap
   SphereComponent-&gt;SetCollisionResponseToChannel(ECC\_Pawn, ECR\_Overlap);
   // --- New Code End --- 

   Copy full snippet(6 lines long)

For more information about Unreal Engine's collision system, see [Collision Response Reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/collision-response-reference-in-unreal-engine).

`PickupBase.cpp` should now look like this:

C++

```
// Copyright Epic Games, Inc. All Rights Reserved.

#include "PickupBase.h"
#include "ItemDefinition.h"
#include "Data/ItemData.h" 

// Sets default values
APickupBase::APickupBase()
{
	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
```

Expand code  Copy full snippet(122 lines long)

### Simulate Pickup Collisions

Now that your pickup has a collision shape, add logic to detect a collision between the pickup and player and make the pickup disappear when collided with.

#### Declare the Overlap Handler

In `PickupBase.h`, in the `protected` section, declare a `void` function named `OnSphereBeginOverlap()`.

Any component that inherits from `UPrimitiveComponent`, like `USphereComponent`, can implement this function to run code when the component overlaps with some other Actor. This function takes several parameters you won’t be using; you’ll only pass the following:

* `UPrimitiveComponent* OverlappedComponent`: The component that was overlapped.
* `AActor* OtherActor`: The Actor overlapping that component.
* `UPrimitiveComponent* OtherComp`: The Actor’s component that overlapped.
* `int32 OtherBodyIndex`: The index of the overlapped component.
* `bool bFromSweep, const FHitResult& SweepResult`: Information about the collision, such as where it happened and at what angle.

C++

```
|  |  |
| --- | --- |
|  | // Code for when something overlaps the SphereComponent. |
|  | UFUNCTION() |
|  | void OnSphereBeginOverlap(UPrimitiveComponent* OverlappedComponent, AActor* OtherActor, UPrimitiveComponent* OtherComp, int32 OtherBodyIndex, bool bFromSweep, const FHitResult& SweepResult); |
```

// Code for when something overlaps the SphereComponent.
UFUNCTION()
void OnSphereBeginOverlap(UPrimitiveComponent\* OverlappedComponent, AActor\* OtherActor, UPrimitiveComponent\* OtherComp, int32 OtherBodyIndex, bool bFromSweep, const FHitResult& SweepResult);

Copy full snippet(3 lines long)

Save the header file and switch to `PickupBase.cpp`.

#### Bind the Function to the Collision Event

Unreal Engine’s collision events are implemented using dynamic multicast delegates. In UE, this delegate system enables one object to call multiple functions at once, sort of like broadcasting a message to a mailing list where your subscribers are these other functions. When we bind functions to the delegate, it’s like we’re subscribing them to our mailing list. The “delegate” is our event; in this case, a collision between the player and the pickup. When the event happens, Unreal Engine calls all functions bound to that event.

Unreal Engine includes a couple of other binding functions, but you’ll want to use `AddDynamic()` because your delegate, `OnComponentBeginOverlap`, is a dynamic delegate. And, you’re binding a `UFUNCTION` in a `UObject`class, requiring `AddDynamic()` for reflection support. For more information about dynamic multicast delegates, see Multicast Delegates[Multi-cast Delegates](https://dev.epicgames.com/documentation/en-us/unreal-engine/multicast-delegates-in-unreal-engine).

In `PickupBase.cpp`, in `BeginPlay()`, before calling `InitializePickup();`, call the `AddDynamic` helper function to bind `OnSphereBeginOverlap()` to the sphere component’s `OnComponentBeginOverlap` event.

C++

```
// Called when the game starts or when spawned
void APickupBase::BeginPlay()
{
	Super::BeginPlay();
	
	// --- New Code Start --- 
	// Register the overlap event so it runs when an overlap happens
	SphereComponent->OnComponentBeginOverlap.AddDynamic(
		this,
		&APickupBase::OnSphereBeginOverlap
```

Expand code  Copy full snippet(17 lines long)

To ensure Unreal Engine only ever creates a single event binding, before the line of code that binds the overlap event, call `RemoveAll(this)` on the delegate before the event binding.

`RemoveAll()` clears any existing delegate bindings associated with the passed actor.

C++

```
// Called when the game starts or when spawned
void APickupBase::BeginPlay()
{
	Super::BeginPlay();

	// --- New Code Start --- 
	// Ensure we don’t bind the overlap event more than once   
	SphereComponent->OnComponentBeginOverlap.RemoveAll(this);
	// --- New Code End --- 
	// Register the overlap event so it runs when an overlap happens
```

Expand code  Copy full snippet(19 lines long)

Bindings like this are usually done in `BeginPlay()` as a part of runtime behavior, and you can  call `RemoveAll(this)` to guarantee the event is bound only once, even across editor during reloads and recompiles.

You could bind the the overlap event in `InitiaizePickup()`, but we recommend performing this step outside of the function so the binding is successful even if loading and using the item data fails.

Save your code.

Now, `OnSphereBeginOverlap()` will run when a character collides with the pickup’s sphere component.

#### Hide the Pickup After a Collision

Next, you'll implement the `OnSphereBeginOverlap()` function so the player can pick up the item.

To make your pickup disappear so it looks like the player picked it up, follow these steps:

1. In `PickupBase.cpp`, add the function signature for `OnSphereBeginOverlap()`.

   C++

   ```
   /**
   *	Broadcasts an event when a character overlaps this pickup's SphereComponent. Sets the pickup to invisible and uninteractable, and respawns it after a set time.
   *	@param OverlappedComponent - the component that was overlapped.
   *	@param OtherActor - the Actor overlapping this component.
   *	@param OtherComp - the Actor's component that overlapped this component.
   *	@param OtherBodyIndex - the index of the overlapped component.
   *	@param bFromSweep - whether the overlap was generated from a sweep.
   *	@param SweepResult - contains info about the overlap such as surface normals and faces.
   */
   void APickupBase::OnSphereBeginOverlap(UPrimitiveComponent* OverlappedComponent, AActor* OtherActor, UPrimitiveComponent* OtherComp, int32 OtherBodyIndex, bool bFromSweep, const FHitResult& SweepResult)
   ```

   Expand code  Copy full snippet(12 lines long)
2. Inside the function, add a debug message to signal the function is triggered properly.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Sets the pickup to invisible and uninteractable, and respawns it after a set time. |
   |  | void APickupBase::OnSphereBeginOverlap(UPrimitiveComponent* OverlappedComponent, AActor* OtherActor, UPrimitiveComponent* OtherComp, int32 OtherBodyIndex, bool bFromSweep, const FHitResult& SweepResult) |
   |  | { |
   |  | GEngine->AddOnScreenDebugMessage(-1, 5.0f, FColor::Yellow, TEXT("Attempting a pickup collision")); |
   |  | } |
   ```

   // Sets the pickup to invisible and uninteractable, and respawns it after a set time.
   void APickupBase::OnSphereBeginOverlap(UPrimitiveComponent\* OverlappedComponent, AActor\* OtherActor, UPrimitiveComponent\* OtherComp, int32 OtherBodyIndex, bool bFromSweep, const FHitResult&amp; SweepResult)
   {
   GEngine-&gt;AddOnScreenDebugMessage(-1, 5.0f, FColor::Yellow, TEXT(&quot;Attempting a pickup collision&quot;));
   }

   Copy full snippet(5 lines long)
3. This function runs whenever another actor collides with the pickup, so you need to make sure it’s your first-person character doing the colliding.

   Declare a new `AAdventureCharacter` pointer named `Character` and set it by casting `OtherActor` to your Character class’ name (this tutorial uses `AAdventureCharacter`).

   C++

   ```
   // Sets the pickup to invisible and uninteractable, and respawns it after a set time.
   void APickupBase::OnSphereBeginOverlap(UPrimitiveComponent* OverlappedComponent, AActor* OtherActor, UPrimitiveComponent* OtherComp, int32 OtherBodyIndex, bool bFromSweep, const FHitResult& SweepResult)
   {
   	GEngine->AddOnScreenDebugMessage(-1, 5.0f, FColor::Yellow, TEXT("Attempting a pickup collision"));

   	// --- New Code Start --- 
   	// Checking if it's an AdventureCharacter overlapping
   	AAdventureCharacter* Character = Cast<AAdventureCharacter>(OtherActor);
   	// --- New Code End ---
   ```

   Expand code  Copy full snippet(11 lines long)
4. In an `if` statement, check if `Character` is not null. Null indicates that the cast failed and that `OtherActor` was not some type of `AAdventureCharacter`.
5. In the `if` statement, hide the mesh and end the collision by:

   * Setting the `PickupMeshComponent` to invisible using `SetVisibility(false)`
   * Setting both the mesh and sphere component to non-collidable using `SetCollisionEnabled()`, passing the `NoCollision` option.

   C++

   ```
   // Sets the pickup to invisible and uninteractable, and respawns it after a set time.
   void APickupBase::OnSphereBeginOverlap(UPrimitiveComponent* OverlappedComponent, AActor* OtherActor, UPrimitiveComponent* OtherComp, int32 OtherBodyIndex, bool bFromSweep, const FHitResult& SweepResult)
   {
   	GEngine->AddOnScreenDebugMessage(-1, 5.0f, FColor::Yellow, TEXT("Attempting a pickup collision"));

   	// Checking if it's an AdventureCharacter overlapping
   	AAdventureCharacter* Character = Cast<AAdventureCharacter>(OtherActor);
   	if (Character != nullptr)
   	{
   		// --- New Code Start ---
   ```

   Expand code  Copy full snippet(19 lines long)
6. Save your code.

### Make the Pickup Respawn

Now that the character can’t interact with the pickup, make it respawn after a certain amount of time.

To implement a respawn timer for pickups, follow these steps:

1. In `PickupBase.h`, in the `protected` section, declare two variables:

   * A bool named `bShouldRespawn`. You can use this to turn respawns on or off.
   * Declare a float named `RespawnTime` initialized to `4.0f`. This is the time to wait until the pickup should respawn.

   Give both properties `EditAnywhere`, `BlueprintReadOnly`, and `Category = “Pickup | Respawn”` specifiers.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Whether this pickup should respawn after being picked up. |
   |  | UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "Pickup | Respawn") |
   |  | bool bShouldRespawn; |
   |  |  |
   |  | // The time in seconds to wait before respawning this pickup. |
   |  | UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "Pickup | Respawn") |
   |  | float RespawnTime = 4.0f; |
   ```

   // Whether this pickup should respawn after being picked up.
   UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = &quot;Pickup | Respawn&quot;)
   bool bShouldRespawn;
   // The time in seconds to wait before respawning this pickup.
   UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = &quot;Pickup | Respawn&quot;)
   float RespawnTime = 4.0f;

   Copy full snippet(7 lines long)
2. Also in the `protected` section, declare an `FTimerHandle` named `RespawnTimerHandle`.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Timer handle to distinguish the respawn timer. |
   |  | FTimerHandle RespawnTimerHandle; |
   ```

   // Timer handle to distinguish the respawn timer.
   FTimerHandle RespawnTimerHandle;

   Copy full snippet(2 lines long)

   In Unreal Engine, gameplay timers are handled by `FTimerManager`. This class includes the `SetTimer()` function, which calls a function or delegate after a set delay. `FTimerManager’s` functions use an `FTimerHandle` to start, pause, resume, or infinitely loop the function. You’ll use `RespawnTimerHandle` to signal when to respawn the pickup. To learn more about using Timer Manager, see [Gameplay Timers](https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-timers-in-unreal-engine).
3. Save the header file and return to `PickupBase.cpp`. Here, you'll use the Timer Manager to set a timer that calls `InitializePickup()` after a short wait.
4. You only want to respawn the pickup if respawns are enabled; so, at the bottom of  `OnSphereBeginOverlap()`, add an `if` statement that checks if `bShouldRespawn` is true.

   C++

   ```
   	// Checking if it's an AdventureCharacter overlapping
   	AAdventureCharacter* Character = Cast<AAdventureCharacter>(OtherActor);
   	if (Character != nullptr)
   	{
   		// Set this pickup to be invisible and disable collision
   		PickupMeshComponent->SetVisibility(false);
   		PickupMeshComponent->SetCollisionEnabled(ECollisionEnabled::NoCollision);
   		SphereComponent->SetCollisionEnabled(ECollisionEnabled::NoCollision);
   	}
   ```

   Expand code  Copy full snippet(17 lines long)
5. In the `if` statement, get the Timer Manager using `GetWorldTimerManager()` and call `SetTimer()` on the timer manager. This function has the following syntax:

   `SetTimer(InOutHandle, Object, InFuncName, InRate, bLoop, InFirstDelay);`

   Where:

   * `InOutHandle` is the `FTimerHandle` that’s controlling the timer (your `RespawnTimerHandle`).
   * `Object` is the `UObject` that owns the function you’re calling. Use this.
   * `InFuncName` is a pointer to the function you want to call (`InitializePickup()` in this case).
   * `InRate` is a float value specifying the time in seconds to wait before calling your function.
   * `bLoop` makes the timer either repeat every `Time` seconds (`true`) or only fire once (`false`).
   * `InFirstDelay` (optional) is an initial time delay before the first function call in a looping timer. If not specified, UE uses `InRate` as the delay.

   You only want to call `InitializePickup()` once to replace the pickup, so set `bLoop` to `false`.

   Set your preferred respawn time; this tutorial makes the pickup respawn after four seconds (`RespawnTime`).

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // If the pickup should respawn, wait an fRespawnTime amount of seconds before calling InitializePickup() to respawn it |
   |  | if (bShouldRespawn) |
   |  | { |
   |  | // --- New Code Start --- |
   |  | GetWorldTimerManager().SetTimer(RespawnTimerHandle, this, &APickupBase::InitializePickup, RespawnTime, false); |
   |  | // --- New Code End --- |
   |  | } |
   ```

    // If the pickup should respawn, wait an fRespawnTime amount of seconds before calling InitializePickup() to respawn it
   if (bShouldRespawn)
   {
   // --- New Code Start ---
   GetWorldTimerManager().SetTimer(RespawnTimerHandle, this, &amp;APickupBase::InitializePickup, RespawnTime, false);
   // --- New Code End ---
   }

   Copy full snippet(7 lines long)
6. You've turned off collision and hidden the mesh in the overlap event, so you need to restore the pickup's active state after it respawns.

   At the end of `InitializePickup()`:

   * Make the `PickupMeshComponent` visible using `SetVisiblity(true)`.
   * Repeat the `SphereComponent->SetCollisionEnabled` line of code that is in the class constructor.

   C++

   ```
   		// Check the mesh is set and can load before using it
   		if (LoadedMesh)
   		{
   			// Set the pickup's mesh
   			PickupMeshComponent->SetStaticMesh(LoadedMesh);
   	
   		}

   		// --- New Code Start --- 
   		// Restore visibility after respawning
   ```

   Expand code  Copy full snippet(14 lines long)
7. Save your code and compile it from Visual Studio.

Your complete `OnSphereBeginOverlap()` function should look like this:

C++

```
// Copyright Epic Games, Inc. All Rights Reserved.

#include "PickupBase.h"
#include "ItemDefinition.h"
#include "Data/ItemData.h" 

// Sets default values
APickupBase::APickupBase()
{
```

Expand code  Copy full snippet(157 lines long)

## Implement Pickups in Your Level

Now that you’ve defined the code that makes up your pickups, it’s time to test them out in your game!

To add pickups to your level, follow these steps:

1. In Unreal Editor, in the **Content Browser** asset tree, go to **Content > FirstPerson > Blueprints**.
2. In the **Blueprints** folder, create a new child folder named **Pickups** to store your pickup classes.
3. In the asset tree, go to your **C++ Classes** folder. Right-click your **PickupBase** class to create a Blueprint from that class.

   [![](https://dev.epicgames.com/community/api/documentation/image/15cbc8c4-541d-4fc2-8826-c05c266bf695?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/15cbc8c4-541d-4fc2-8826-c05c266bf695?resizing_type=fit)
4. Name it `BP_PickupBase`.
5. For the **Path**, select **Content/FirstPerson/Blueprints/Pickups**, and click **Create Pickup Base Class**.

   [![](https://dev.epicgames.com/community/api/documentation/image/f9df2655-bb13-4c98-841a-2b03c151f238?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f9df2655-bb13-4c98-841a-2b03c151f238?resizing_type=fit)
6. Go back to your **Blueprints > Pickups** folder. Drag your `BP_PickupBase` Blueprint into the level. An instance of PickupBase appears in your level and is automatically selected in the **Outliner** panel. However, it doesn’t have a mesh yet.

   [![](https://dev.epicgames.com/community/api/documentation/image/49839627-7c2b-4f40-9439-d69be93ee25a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/49839627-7c2b-4f40-9439-d69be93ee25a?resizing_type=fit)
7. With the `BP_PickupBase` actor still selected, in the **Details** panel, set the following properties:

   1. Set **Pickup Item ID** to `pickup_001`.
   2. Set **Pickup Data Table** to `DT_PickupData`.
   3. Set **Should Respawn** to **true**.

   [![](https://dev.epicgames.com/community/api/documentation/image/99dab706-6813-4627-8570-54efb0c536aa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/99dab706-6813-4627-8570-54efb0c536aa?resizing_type=fit)

   This system relies on manual data entry, so make sure the **Pickup Item ID** in your level object exactly matches the **ID** in the Data Table row, or the item will fail to initialize.

When you click **Play** to test your game, your pickup uses the **Pickup Item ID** to query the Data Table and retrieve data associated with `pickup_001`. The pickup uses table data and the reference to your `DA_Pickup_001` Data Asset to initialize a reference Item and load its static mesh.

[![](https://dev.epicgames.com/community/api/documentation/image/b542012b-991b-4757-b6ba-c1a98ff45789?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b542012b-991b-4757-b6ba-c1a98ff45789?resizing_type=fit)

When you run over the pickup, you should see it disappear, then reappear four seconds later.

### Load a Different Pickup

If you set the **Pickup Item ID** to a different value, your pickup will retrieve data from that row in the table instead.

To experiment with switching the **Pickup Item ID**, follow these steps:

1. Create a new Data Asset named **DA\_Pickup\_002**. Set the following properties in this asset:

   * **ID**: pickup\_002
   * **Item Type**: Consumable
   * **Name**: Test Name 2
   * **Description**: Test Description 2
   * **World** **Mesh**: `SM_ChamferCube`

   [![500](https://dev.epicgames.com/community/api/documentation/image/43c35634-3b5c-4a88-a95c-62e62e7b763c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/43c35634-3b5c-4a88-a95c-62e62e7b763c?resizing_type=fit)
2. Add a new row in the `DT_PickupData` table and enter the Data Asset's information into the new row's fields.

   [![](https://dev.epicgames.com/community/api/documentation/image/41eac8a8-93f3-42c6-a83f-49afd2486558?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/41eac8a8-93f3-42c6-a83f-49afd2486558?resizing_type=fit)
3. In the `BP_PickupBase` actor, change the **Pickup Item ID** to `pickup_002`.

When you click **Play** to test your game, the pickup should spawn with the values from `DA_Pickup_002` instead!

[![](https://dev.epicgames.com/community/api/documentation/image/09ce7a4b-0f06-46cf-b051-1d11cb076cf4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/09ce7a4b-0f06-46cf-b051-1d11cb076cf4?resizing_type=fit)

## Update Pickup Actors in the Editor

Your pickups are working in-game, but it can be difficult to visualize them in the editor since they don’t have a default mesh.

To fix this, use the `PostEditChangeProperty()` function. This is an in-editor function that Unreal Engine calls when the editor changes a property, so you can use it to keep your actors up to date in the Viewport as their properties change. For example, updating a UI element as you change a player’s default health, or scaling a sphere as you bring it closer or further away from the origin.

In this project, you’ll use it to apply the pickup’s new static mesh whenever **Pickup Item ID** changes. This way, you can change your pickup type and see it immediately update in the Viewport without needing to click Play!

To make changes to your pickups immediately in the editor, you'll:

* Declare a new `PostEditChangeProperty` function.
* Use `PropertyChangedEvent` information to get the name of the changed property.
* Apply the new property value to your pickup item.

First, to declare PostEditChangeProperty and retrieve the name of the changed property, follow these steps:

1. In `PickupBase.h`, at the end of the `protected` section, declare an `#if WITH_EDITOR` macro. This macro tells Unreal Header Tool that anything inside it should only be packaged for editor builds and not compiled for release versions of the game. End this macro with an `#endif` statement.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | #if WITH_EDITOR |
   |  |  |
   |  | #endif |
   ```

   #if WITH\_EDITOR
   #endif

   Copy full snippet(3 lines long)
2. Inside the macro, declare a virtual void function override for `PostEditChangeProperty()`. This function takes a reference to the `FPropertyChangedEvent`, which includes info about the property changed, the type of change, and more. Save the header file.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | #if WITH_EDITOR |
   |  |  |
   |  | // Runs whenever a property on this object is changed in the editor |
   |  | virtual void PostEditChangeProperty(FPropertyChangedEvent& PropertyChangedEvent) override; |
   |  |  |
   |  | #endif |
   ```

   #if WITH\_EDITOR
   // Runs whenever a property on this object is changed in the editor
   virtual void PostEditChangeProperty(FPropertyChangedEvent&amp; PropertyChangedEvent) override;
   #endif

   Copy full snippet(6 lines long)
3. In `PickupBase.cpp`, implement the `PostEditChangeProperty()` function. Start by calling the `Super::PostEditChangeProperty()` function to handle any parent class property changes.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | /*	Updates this pickup whenever a property is changed. |
   |  | *	@param PropertyChangedEvent - contains info about the property that was changed. */ |
   |  | void APickupBase::PostEditChangeProperty(FPropertyChangedEvent& PropertyChangedEvent) |
   |  | { |
   |  | // Handle parent class property changes |
   |  | Super::PostEditChangeProperty(PropertyChangedEvent); |
   |  | } |
   ```

   /\* Updates this pickup whenever a property is changed.
   \* @param PropertyChangedEvent - contains info about the property that was changed. \*/
   void APickupBase::PostEditChangeProperty(FPropertyChangedEvent&amp; PropertyChangedEvent)
   {
   // Handle parent class property changes
   Super::PostEditChangeProperty(PropertyChangedEvent);
   }

   Copy full snippet(7 lines long)
4. Create a new `const FName` variable named `ChangedProperty` to store the changed property’s name.

   C++

   ```
   /*	Updates this pickup whenever a property is changed.
   *	@param PropertyChangedEvent - contains info about the property that was changed. */
   void APickupBase::PostEditChangeProperty(FPropertyChangedEvent& PropertyChangedEvent)
   {
   	// Handle parent class property changes
   	Super::PostEditChangeProperty(PropertyChangedEvent);

   	// --- New Code Start --- 
   	const FName ChangedPropertyName;
   	// --- New Code End ---
   ```

   Expand code  Copy full snippet(11 lines long)
5. To verify that the `PropertyChangedEvent` includes a `Property` and save that property, use a ternary operator with `PropertyChangedEvent.Property` as the condition. Set `ChangedPropertyName` to `PropertyChangedEvent.Property->GetFName()` if the condition is true and set it to `NAME_None` if false.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // If a property was changed, get the name of the changed property. Otherwise use none. |
   |  | const FName ChangedPropertyName = PropertyChangedEvent.Property |
   |  | ? PropertyChangedEvent.Property->GetFName() |
   |  | : NAME_None; |
   ```

    // If a property was changed, get the name of the changed property. Otherwise use none.
   const FName ChangedPropertyName = PropertyChangedEvent.Property
   ? PropertyChangedEvent.Property-&gt;GetFName()
   : NAME\_None;

   Copy full snippet(4 lines long)

   `NAME_None` is a global Unreal Engine constant of type `FName` that means "no valid name" or “null name”.

Now that you know the name of the property, you can make Unreal Engine update the mesh if it detected the ID changed. You'll need to check and resolve each soft pointer before using the data, so as a short cut, you can just call `InitializePickup()`.

To update the mesh in the editor preview, follow these steps:

1. In an `if` statement, check that `ChangedPropertyName` is named `PickupItemID` or `PickupDataTable`.

   To do this, call `GET_MEMBER_NAME_CHECKED()`, passing this `APickupBase` class and either `PickupItemID`. or `PickupDataTable`. This macro does a compile-time check to ensure the property you pass exists in the passed class.

   C++

   ```
   /*	Updates this pickup whenever a property is changed.
   *	@param PropertyChangedEvent - contains info about the property that was changed. */
   void APickupBase::PostEditChangeProperty(FPropertyChangedEvent& PropertyChangedEvent)
   {
   	// Handle parent class property changes
   	Super::PostEditChangeProperty(PropertyChangedEvent);

   	// If a property was changed, get the name of the changed property. Otherwise use none.
   	const FName ChangedPropertyName = PropertyChangedEvent.Property 
   		? PropertyChangedEvent.Property->GetFName()
   ```

   Expand code  Copy full snippet(21 lines long)
2. Inside the `if` statement, you need to check and resolve the item data, the data asset, and the item's mesh, and then apply the mesh to the pickup. Since you already built the code for that in `InitializePickup()`, call that function.

   C++

   ```
   /*	Updates this pickup whenever a property is changed.
   *	@param PropertyChangedEvent - contains info about the property that was changed. */
   void APickupBase::PostEditChangeProperty(FPropertyChangedEvent& PropertyChangedEvent)
   {
   	// Handle parent class property changes
   	Super::PostEditChangeProperty(PropertyChangedEvent);

   	// If a property was changed, get the name of the changed property. Otherwise use none.
   	const FName ChangedPropertyName = PropertyChangedEvent.Property 
   		? PropertyChangedEvent.Property->GetFName()
   ```

   Expand code  Copy full snippet(22 lines long)

   `InitializePickup()` includes extra runtime logic that's not necessary for editor preview updates, but reusing it here keeps the example simple. In a production system, you'd have a dedicated validation function or preview-only function instead.
3. Save your code and compile it from Visual Studio.

Your complete `PostEditChangeProperty()` function should look like this:

C++

```
/*	Updates this pickup whenever a property is changed.
*	@param PropertyChangedEvent - contains info about the property that was changed. */
void APickupBase::PostEditChangeProperty(FPropertyChangedEvent& PropertyChangedEvent)
{
	// Handle parent class property changes
	Super::PostEditChangeProperty(PropertyChangedEvent);

	// If a property was changed, get the name of the changed property. Otherwise use none.
	const FName ChangedPropertyName = PropertyChangedEvent.Property 
		? PropertyChangedEvent.Property->GetFName()
```

Expand code  Copy full snippet(20 lines long)

Back in the editor, in the **Outliner**, ensure your **BP\_PickupBase** actor is selected. Change the **Pickup Item ID** from `pickup_001` to `pickup_002`, then change it back. As you change the ID, your pickup’s mesh updates in the Viewport.

[![](https://dev.epicgames.com/community/api/documentation/image/93570ce9-c467-42f7-9d25-672873535b65?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/93570ce9-c467-42f7-9d25-672873535b65?resizing_type=fit)

## Next Up

Next, you’ll extend your pickup class further to create a custom gadget and equip it to your character!

* [![Equip Your Character](https://dev.epicgames.com/community/api/documentation/image/d7ce94e9-285d-4876-b873-3c7728f842fa?resizing_type=fit&width=640&height=640)

  Equip Your Character

  Learn to use C++ to create custom equippable items and attach them to your character.](https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools)

## Complete Code

C++

PickupBase.h

```
// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "Components/SphereComponent.h"
#include "AdventureCharacter.h"
#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "PickupBase.generated.h"
```

Expand code  Copy full snippet(76 lines long)

C++

PickupBase.cpp

```
// Copyright Epic Games, Inc. All Rights Reserved.

#include "PickupBase.h"
#include "ItemDefinition.h"
#include "Data/ItemData.h" 

// Sets default values
APickupBase::APickupBase()
{
```

Expand code  Copy full snippet(178 lines long)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Before You Begin](/documentation/en-us/unreal-engine/coder-06-create-a-respawning-pickup-item-in-unreal-engine?application_version=5.7#beforeyoubegin)
* [Create a New Pickup Class](/documentation/en-us/unreal-engine/coder-06-create-a-respawning-pickup-item-in-unreal-engine?application_version=5.7#createanewpickupclass)
* [Initialize the Pickup with Table Data](/documentation/en-us/unreal-engine/coder-06-create-a-respawning-pickup-item-in-unreal-engine?application_version=5.7#initializethepickupwithtabledata)
* [Pull Data from a Data Table](/documentation/en-us/unreal-engine/coder-06-create-a-respawning-pickup-item-in-unreal-engine?application_version=5.7#pulldatafromadatatable)
* [Create a Reference Item](/documentation/en-us/unreal-engine/coder-06-create-a-respawning-pickup-item-in-unreal-engine?application_version=5.7#createareferenceitem)
* [Call InitializePickup()](/documentation/en-us/unreal-engine/coder-06-create-a-respawning-pickup-item-in-unreal-engine?application_version=5.7#callinitializepickup())
* [Create In-Game Functionality](/documentation/en-us/unreal-engine/coder-06-create-a-respawning-pickup-item-in-unreal-engine?application_version=5.7#createin-gamefunctionality)
* [Add a Mesh Component](/documentation/en-us/unreal-engine/coder-06-create-a-respawning-pickup-item-in-unreal-engine?application_version=5.7#addameshcomponent)
* [Add a Collision Shape](/documentation/en-us/unreal-engine/coder-06-create-a-respawning-pickup-item-in-unreal-engine?application_version=5.7#addacollisionshape)
* [Simulate Pickup Collisions](/documentation/en-us/unreal-engine/coder-06-create-a-respawning-pickup-item-in-unreal-engine?application_version=5.7#simulatepickupcollisions)
* [Declare the Overlap Handler](/documentation/en-us/unreal-engine/coder-06-create-a-respawning-pickup-item-in-unreal-engine?application_version=5.7#declaretheoverlaphandler)
* [Bind the Function to the Collision Event](/documentation/en-us/unreal-engine/coder-06-create-a-respawning-pickup-item-in-unreal-engine?application_version=5.7#bindthefunctiontothecollisionevent)
* [Hide the Pickup After a Collision](/documentation/en-us/unreal-engine/coder-06-create-a-respawning-pickup-item-in-unreal-engine?application_version=5.7#hidethepickupafteracollision)
* [Make the Pickup Respawn](/documentation/en-us/unreal-engine/coder-06-create-a-respawning-pickup-item-in-unreal-engine?application_version=5.7#makethepickuprespawn)
* [Implement Pickups in Your Level](/documentation/en-us/unreal-engine/coder-06-create-a-respawning-pickup-item-in-unreal-engine?application_version=5.7#implementpickupsinyourlevel)
* [Load a Different Pickup](/documentation/en-us/unreal-engine/coder-06-create-a-respawning-pickup-item-in-unreal-engine?application_version=5.7#loadadifferentpickup)
* [Update Pickup Actors in the Editor](/documentation/en-us/unreal-engine/coder-06-create-a-respawning-pickup-item-in-unreal-engine?application_version=5.7#updatepickupactorsintheeditor)
* [Next Up](/documentation/en-us/unreal-engine/coder-06-create-a-respawning-pickup-item-in-unreal-engine?application_version=5.7#nextup)
* [Complete Code](/documentation/en-us/unreal-engine/coder-06-create-a-respawning-pickup-item-in-unreal-engine?application_version=5.7#completecode)

Related documents

[Code a First-Person Adventure Game

![Code a First-Person Adventure Game](https://dev.epicgames.com/community/api/documentation/image/ffc1a8f8-e7e5-42c0-b4ed-32ce6d3adbbc?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/code-a-firstperson-adventure-game-in-unreal-engine)

[Manage Items and Data

![Manage Items and Data](https://dev.epicgames.com/community/api/documentation/image/1db9f4bd-93e0-4ad8-8abf-c7be6ecec5e8?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/coder-05-manage-item-and-data-in-an-unreal-engine-game)

[Equip Your Character

![Equip Your Character](https://dev.epicgames.com/community/api/documentation/image/d7ce94e9-285d-4876-b873-3c7728f842fa?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools)
