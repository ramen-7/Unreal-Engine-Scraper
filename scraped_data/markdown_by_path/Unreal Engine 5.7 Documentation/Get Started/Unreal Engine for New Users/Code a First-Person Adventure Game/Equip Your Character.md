<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools?application_version=5.7 -->

# Equip Your Character

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
8. Equip Your Character

# Equip Your Character

Learn to use C++ to create custom equippable items and attach them to your character.

On this page

## Before You Begin

Ensure you’ve completed the following objectives in the previous sections of [Code a First-Person Adventure Game](https://dev.epicgames.com/documentation/en-us/unreal-engine/code-a-firstperson-adventure-game-in-unreal-engine):

* Built a C++ first-person player character in [Create a Player Character With Input Actions](https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-02-create-a-player-character-with-input-actions-in-cplusplus).
* Set up data-driven gameplay elements to manage item data in [Manage Items and Data](https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-05-manage-item-and-data-in-an-unreal-engine-game).
* Created a pickup item and added it to your level in [Create a Respawning Pickup Item](https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-06-create-a-respawning-pickup-item-in-unreal-engine).

### Create Reference Items With a New CreateItemCopy Function

Before you start creating a new equippable pickup item, you’ll first need to modify your **ItemDefinition** and **PickupBase** classes to support capturing a reference item from a wider variety of item types.

In the `InitializePickup()` function in your `PickupBase` class, you set a `ReferenceItem` of type `UItemDefinition`. This is too restrictive; setting a reference item this way won’t include the additional properties you’ll add to any new, specialized item classes derived from `UItemDefinition`.

To solve this, you’ll create a new virtual function in `ItemDefinition` that creates and returns a copy of that item. Because it’s a virtual function, you can override it in any classes that inherit from `UItemDefinition`. When `PickupBase` calls the function, the compiler determines the correct function to call based on the class it was called from.

Adding this function to the parent `ItemDefinition` class ensures it’s available if you decide to continue extending your project to include more item types that inherit from `UItemDefinition`.

To define a new `CreateItemCopy()` function for creating reference items, follow these steps:

1. Open `ItemDefinition.h`. In the `public` section, declare a new virtual const function named `CreateItemCopy()` that returns a `UItemDefinition` pointer. The function should take a `UObject` pointer named `Outer` so you can tell Unreal Engine what object owns the copy.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Creates and returns a copy of the item. |
   |  | virtual UItemDefinition* CreateItemCopy(UObject* Outer) const; |
   ```

   // Creates and returns a copy of the item.
   virtual UItemDefinition\* CreateItemCopy(UObject\* Outer) const;

   Copy full snippet(2 lines long)

   In Unreal Engine, every UObject has an **Outer,**which is the object that owns it. The Outer acts like a parent to the UObject; if the parent goes away, UE knows the child object can also be cleaned up. Setting a sensible Outer is important for garbage collection and controlling the lifetime of the object.
2. In `ItemDefinition.cpp`, add a function signature for the `CreateItemCopy()` function.
3. Inside the function, create a new `UItemDefinition` object pointer named `ItemCopy`, passing `Outer` as the owner.

   Inside,

   C++

   ```
   // Copyright Epic Games, Inc. All Rights Reserved.

   #include "ItemDefinition.h"

   // --- New Code Start --- 
   /* Creates and returns a copy of this Item Definition.
   *	@return	a copy of the item. */
   UItemDefinition* UItemDefinition::CreateItemCopy(UObject* Outer) const
   {
   	UItemDefinition* ItemCopy = NewObject<UItemDefinition>(Outer);
   ```

   Expand code  Copy full snippet(12 lines long)

   Visual Studio disambiguates `UItemDefinition::StaticClass()` to `StaticClass()`.
4. Assign each field of `ItemCopy` to this class’s fields and then return `ItemCopy`:

   C++

   ```
   // Copyright Epic Games, Inc. All Rights Reserved.

   #include "ItemDefinition.h"

   /* Creates and returns a copy of this Item Definition.
   *	@return	a copy of the item. */
   UItemDefinition* UItemDefinition::CreateItemCopy(UObject* Outer) const
   {
   	UItemDefinition* ItemCopy = NewObject<UItemDefinition>(Outer);
   ```

   Expand code  Copy full snippet(19 lines long)

Next, refactor your `InitializePickup()` function by removing the code that manually sets up `ReferenceItem` and replace that code with a `CreateItemCopy()` call.

To update `InitializePickup()` with your new `CreateItemCopy()` function, follow these steps:

1. Open `PickupBase.cpp` and go to `InitializePickup()`.
2. Delete these five lines that define and set `ReferenceItem`:

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Delete these 5 lines: |
   |  |  |
   |  | ReferenceItem = NewObject<UItemDefinition>(this, UItemDefinition::StaticClass()); |
   |  |  |
   |  | ReferenceItem->ID = ItemDataRow->ID; |
   |  | ReferenceItem->ItemType = ItemDataRow->ItemType; |
   |  | ReferenceItem->ItemText = ItemDataRow->ItemText; |
   |  | ReferenceItem->WorldMesh = TempItemDefinition->WorldMesh; |
   ```

   // Delete these 5 lines:
   ReferenceItem = NewObject&lt;UItemDefinition&gt;(this, UItemDefinition::StaticClass());
   ReferenceItem-&gt;ID = ItemDataRow-&gt;ID;
   ReferenceItem-&gt;ItemType = ItemDataRow-&gt;ItemType;
   ReferenceItem-&gt;ItemText = ItemDataRow-&gt;ItemText;
   ReferenceItem-&gt;WorldMesh = TempItemDefinition-&gt;WorldMesh;

   Copy full snippet(8 lines long)
3. Set `ReferenceItem` by calling `TempItemDefinition->CreateItemCopy()`:

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Create a copy of the item with this class as the owner |
   |  | ReferenceItem = TempItemDefinition->CreateItemCopy(this); |
   ```

   // Create a copy of the item with this class as the owner
   ReferenceItem = TempItemDefinition-&gt;CreateItemCopy(this);

   Copy full snippet(2 lines long)

Save `PickupBase.cpp`. Your `InitializePickup()` function should now look like the following:

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

Expand code  Copy full snippet(63 lines long)

## Define Equippable Tool Data

In the previous section, you learned how to create interactable pickup objects in your level that are concrete representations of table data. In this section, you’ll learn how to build tools for your character to equip.

To set up a new equippable tool, you’ll create:

* `EquippableToolDefinition`: A Data Asset class derived from `ItemDefinition` that stores the tool’s data.
* `EquippableToolBase`: An Actor class to represent the tool in-game. It gives your character the animations, input mappings, and mesh so the character can hold and operate the tool.

To make your character able to pick up and equip tools, you’ll add:

* A place to store items.
* A way to know the type of each item in their inventory.
* A way to equip tools.

Remember, the `EquippableToolBase` actor represents the tool your character is holding and using, while the `PickupBase` actor represents the pickup item in your level. Your character has to collide with the pickup item before it can equip it, so you’ll also modify `PickupBase` to grant the item to the character after a successful collision.

Then, you’ll combine your new tool class with the pickups and Data Table you’ve already built to create a custom dart launcher and attach it to your character!

First, you’ll define your tool’s data in a new `ItemDefinition` class.

To create a new `EquippableToolDefinition` class, follow these steps:

1. In Unreal Editor, go to **Tools > New C++ Class**. Go to **All Classes**, search for and select **ItemDefinition** as the parent class, and click **Next**.

   [![](https://dev.epicgames.com/community/api/documentation/image/e9057eb5-03ce-440a-a632-e723a9900d6f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e9057eb5-03ce-440a-a632-e723a9900d6f?resizing_type=fit)
2. Name the class `EquippableToolDefinition` and click **Create Class**.
3. In Visual Studio, at the top of `EquippableToolDefinition.h`, ensure there's an include for `”ItemDefinition.h”`, then add the following forward declarations:

   1. `class UInputMappingContext`: Each equippable tool should hold a reference to an Input Mapping Context that you’ll apply to the character wielding that tool.
   2. `class AEquippableToolBase`: The Actor representing your tools in-game. You’ll create this in the next step.

      C++

      ```
      // Copyright Epic Games, Inc. All Rights Reserved.

      #pragma once

      #include "CoreMinimal.h"
      #include "ItemDefinition.h"
      #include "EquippableToolDefinition.generated.h"

      // --- New Code Start --- 
      class AEquippableToolBase;
      ```

      Expand code  Copy full snippet(21 lines long)
4. In the `public` section, add a `TSubclassOf` property of type `AEquippableToolBase` named `ToolAsset`. Give this a `UPROPERTY()` macro with `EditDefaultsOnly` and `BlueprintReadOnly`.

   C++

   ```
   UCLASS(BlueprintType, Blueprintable)
   class ADVENTUREGAME_API UEquippableToolDefinition : public UItemDefinition
   {
   	GENERATED_BODY()

   // --- New Code Start --- 
   public:
   	// The tool actor associated with this item
   	UPROPERTY(EditDefaultsOnly, BlueprintReadOnly)
   	TSubclassOf<AEquippableToolBase> ToolAsset;
   ```

   Expand code  Copy full snippet(13 lines long)

   `TSubclassOf<AEquippableToolBase>` is a template wrapper around `UClass` that enables you to reference Blueprint subclasses of `AEquippableToolBase` while ensuring type safety. It’s useful in gameplay scenarios where you want to spawn different types of actors dynamically.

   You’ll use `ToolAsset` to dynamically spawn a tool actor when it gets equipped to your character.
5. Declare an override for the `CreateItemCopy()` function you declared in `UItemDefinition`. This override creates and returns a copy of the `UEquippableToolDefinition` class.

   Your complete `EquippableToolDefinition.h` file should look like the following:

   C++

   ```
   UCLASS(BlueprintType, Blueprintable)
   class ADVENTUREGAME_API UEquippableToolDefinition : public UItemDefinition
   {
   	GENERATED_BODY()

   public:
   	// The tool actor associated with this item
   	UPROPERTY(EditDefaultsOnly, BlueprintReadOnly)
   	TSubclassOf<AEquippableToolBase> ToolAsset;
   ```

   Expand code  Copy full snippet(16 lines long)
6. In `EquippableToolDefinition.cpp`, add a function definition header for `CreateItemCopy()`.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Copyright Epic Games, Inc. All Rights Reserved. |
   |  |  |
   |  | #include "EquippableToolDefinition.h" |
   |  |  |
   |  | UEquippableToolDefinition* UEquippableToolDefinition::CreateItemCopy(UObject* Outer) const |
   |  | { |
   |  |  |
   |  | } |
   ```

   // Copyright Epic Games, Inc. All Rights Reserved.
   #include &quot;EquippableToolDefinition.h&quot;
   UEquippableToolDefinition\* UEquippableToolDefinition::CreateItemCopy(UObject\* Outer) const
   {
   }

   Copy full snippet(8 lines long)
7. Add an `if` statement to check if the Outer is null. If it is null and a fallback Outer is needed, copy the item with `GetTransientPackage()` as the Outer.

   `GetTransientPackage()` returns an engine-owned UPackage that is never saved to disk and lives for the lifetime of the editor or game session, so it's a good backup Outer for temporary UObjects.

   C++

   ```
   UEquippableToolDefinition* UEquippableToolDefinition::CreateItemCopy(UObject* Outer) const
   {
   	// --- New Code Start --- 
   	// If we need an Outer, use GetTransientPackage
   	if (!Outer)
   	{
   		Outer = GetTransientPackage();
   	}
   	// --- New Code End ---
   ```

   Expand code  Copy full snippet(12 lines long)
8. Return a `DuplicateObject<T>(ExistingObject, Outer)` call to clone the equippable item definition asset and return the copy.

   C++

   ```
   UEquippableToolDefinition* UEquippableToolDefinition::CreateItemCopy(UObject* Outer) const
   {
   	// If we need an Outer, use GetTransientPackage
   	if (!Outer)
   	{
   		Outer = GetTransientPackage();
   	}
   	
   	// --- New Code Start --- 
   	return DuplicateObject<UEquippableToolDefinition>(this, Outer);
   ```

   Expand code  Copy full snippet(13 lines long)

   In `ItemDefinition`, you created runtime item copies using `NewObject` and manual property assignment, but this approach becomes cumbersome and error-prone as items gain more properties. With `DuplicateObject`, you can automatically copy all reflected data (including inherited properties) automatically. Same result, cleaner way to get there.
9. Save both `EquippableToolDefinition` class files. The code won't compile until you create `EquippableToolBase`.

## Set Up an Equippable Tool Actor

Next, start building your equippable tool Actor. This is the in-game representation that adds the tool’s animations, controls, and mesh to the character.

To create and set up a new base equippable tool Actor, follow these steps:

1. In Unreal Editor, go to **Tools > New C++ Class**. Select **Actor** as the parent class and name the class **EquippableToolBase**.
2. Click **Create Class**. Unreal Engine automatically opens your new class’ files in VS.
3. At the top of `EquippableToolBase.h`, forward declare class `AAdventureCharacter`, `UInputAction`, and `UInputMappingContext`. The equippable tool needs to know what Character it's equipped to so it can bind tool-specific Input Actions to that Character.
4. In `EquippableToolBase.h`,  add an `#include` for `EnhancedInputSubsystems.h`, `Animation/AnimBlueprint.h`, and `Components/SkeletalMeshComponent.h`.
5. In the class declaration’s `UCLASS` macro, add the `BlueprintType` and `Blueprintable` specifiers to expose this class to Blueprints.

   C++

   ```
   // Copyright Epic Games, Inc. All Rights Reserved.

   #pragma once

   #include "CoreMinimal.h"
   #include "GameFramework/Actor.h"
   // --- New Code Start ---
   #include "EnhancedInputSubsystems.h"
   #include "Animation/AnimBlueprint.h" 
   #include "Components/SkeletalMeshComponent.h"
   ```

   Expand code  Copy full snippet(39 lines long)
6. In `EquippableToolBase.cpp`, add an `#include` for `AdventureCharacter.h`. and `InputMappingContext.h`.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | #include "EquippableToolBase.h" |
   |  | #include "AdventureCharacter.h" |
   |  | #include "InputMappingContext.h" |
   ```

   #include &quot;EquippableToolBase.h&quot;
   #include &quot;AdventureCharacter.h&quot;
   #include &quot;InputMappingContext.h&quot;

   Copy full snippet(3 lines long)

### Declare Tool Animations

In `EquippableToolBase.h`, in the `public` section, add two `TObjectPtr` to `UAnimBlueprint` properties named `FirstPersonToolAnim` and `ThirdPersonToolAnim`. These are the first-person and third-person animations that the character uses when equipped with this tool.

Give these properties a `UPROPERTY()` macro with `EditAnywhere`and `BlueprintReadOnly`.

C++

```
public:	
	// Sets default values for this actor's properties
	AEquippableToolBase();

	// --- New Code Start --- 
	// First Person animations
	UPROPERTY(EditAnywhere, BlueprintReadOnly)
	TObjectPtr<UAnimBlueprint> FirstPersonToolAnim;

	// Third Person animations
```

Expand code  Copy full snippet(13 lines long)

### Create the Tool’s Mesh

To declare and set up a mesh component for equippable tools, follow these steps:

1. In `EquippableToolBase.h`, in the `public` section, add a `TObjectPtr` to a `USkeletalMeshComponent` named `ToolMeshComponent`. This is the tool’s skeletal mesh that the character sees when equipped. Give it a `UPROPERTY()` macro with `EditAnywhere` and `BlueprintReadOnly`.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Tool Skeletal Mesh |
   |  | UPROPERTY(EditAnywhere, BlueprintReadOnly) |
   |  | TObjectPtr<USkeletalMeshComponent> ToolMeshComponent; |
   ```

   // Tool Skeletal Mesh
   UPROPERTY(EditAnywhere, BlueprintReadOnly)
   TObjectPtr&lt;USkeletalMeshComponent&gt; ToolMeshComponent;

   Copy full snippet(3 lines long)
2. In `EquippableToolBase.cpp`, modify the `AEquippableToolBase()` constructor function to create a default `USkeletalMeshComponent` and assign it to `ToolMeshComponent`. Then check if the `ToolMeshComponent` is not null to make sure your tool has a model when it's loaded.

   C++

   ```
   #include "EquippableToolBase.h"
   #include "InputMappingContext.h"
   #include "AdventureCharacter.h"

   // Sets default values
   AEquippableToolBase::AEquippableToolBase()
   {
    	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
   	PrimaryActorTick.bCanEverTick = true;
   ```

   Expand code  Copy full snippet(17 lines long)

### Declaring the Tool’s Owner

In `EquippableToolBase.h`, in the `public` section, create a `TObjectPtr` to an instance of your Character class named `OwningCharacter`. Give it a `UPROPERTY()` macro with `EditAnywhere` and `BlueprintReadOnly`.

This is the character this tool is currently equipped to.

C++

```
|  |  |
| --- | --- |
|  | // The character holding this tool |
|  | UPROPERTY(EditAnywhere, BlueprintReadOnly) |
|  | TObjectPtr<AAdventureCharacter> OwningCharacter; |
```

// The character holding this tool
UPROPERTY(EditAnywhere, BlueprintReadOnly)
TObjectPtr<AAdventureCharacter> OwningCharacter;

Copy full snippet(3 lines long)

### Declare Input and a Use-Tool Function

Your tool comes with an Input Mapping Context and Input Action that it needs to give the character.

To set up the tool's controls, follow these steps:

1. To add the Input Mapping Context, in the `public` section, declare a `TObjectPtr` to a `UInputMappingContext` named `ToolMappingContext`. Give it a `UPROPERTY()` macro with `EditAnywhere` and `BlueprintReadOnly`.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // The input mapping context associated with this tool |
   |  | UPROPERTY(EditAnywhere, BlueprintReadOnly) |
   |  | TObjectPtr<UInputMappingContext> ToolMappingContext; |
   ```

   // The input mapping context associated with this tool
   UPROPERTY(EditAnywhere, BlueprintReadOnly)
   TObjectPtr&lt;UInputMappingContext&gt; ToolMappingContext;

   Copy full snippet(3 lines long)
2. Similar to when you implemented movement controls, you’ll add a function that implements a use-tool action and a new function that binds an input action to the function.

   In `EquippableToolBase.h`, in the `public` section, declare two virtual void functions named `Use()` and `BindInputAction()`.

   The `BindInputAction()` function takes a const `UInputAction` pointer and binds the given input action to the character’s `Use()` function.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Use the tool |
   |  | UFUNCTION() |
   |  | virtual void Use(); |
   |  |  |
   |  | // Binds the Use function to the owning character |
   |  | UFUNCTION() |
   |  | virtual void BindInputAction(const UInputAction* ActionToBind); |
   ```

   // Use the tool
   UFUNCTION()
   virtual void Use();
   // Binds the Use function to the owning character
   UFUNCTION()
   virtual void BindInputAction(const UInputAction\* ActionToBind);

   Copy full snippet(7 lines long)

   When you implemented character movement controls, you used the InputComponent’s `BindAction()` function that requires you to pass the exact name of the target function. You don’t know the full name of the function yet, so you need a custom `BindInputAction()` function that you can implement in each `EquippableToolBase` subclass to call `BindAction`, passing `[ToolChildClass]::Use`.
3. In `EquippableToolBase.cpp`, add function definition headers for the `Use()` and `BindInputAction()` functions.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | void AEquippableToolBase::Use() |
   |  | { |
   |  | } |
   |  |  |
   |  | void AEquippableToolBase::BindInputAction(const UInputAction* ActionToBind) |
   |  | { |
   |  | } |
   ```

   void AEquippableToolBase::Use()
   {
   }
   void AEquippableToolBase::BindInputAction(const UInputAction\* ActionToBind)
   {
   }

   Copy full snippet(7 lines long)

   These won’t do anything in the parent class, so you can leave them blank for now. You’ll add logic to these when creating `EquippableToolBase` subclasses; for example, the `Use()` function should include tool-specific actions such as launching a projectile or opening a door.
4. Save your code and compile it from VS.

Your `EquippableToolBase.h` file should now look like the following:

C++

```
// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "EnhancedInputSubsystems.h"     
#include "Animation/AnimBlueprint.h"
#include "Components/SkeletalMeshComponent.h"
#include "EquippableToolBase.generated.h"
```

Expand code  Copy full snippet(61 lines long)

`EquippableToolBase.cpp` should now look like the following:

C++

```
// Copyright Epic Games, Inc. All Rights Reserved.

#include "EquippableToolBase.h"
#include "InputMappingContext.h"
#include "AdventureCharacter.h"

// Sets default values
AEquippableToolBase::AEquippableToolBase()
{
 	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
```

Expand code  Copy full snippet(41 lines long)

## Grant Items to a Character

You’ve defined tools your character can use, but they can't equip them yet. Next, you'll add an inventory system so the character can store and equip items when picking them up.

### Build an Inventory Component

Your character’s inventory should add functionality to the character but not exist in the game world, so you’ll use an **Actor Components** class to define an inventory that knows what items a character has, can swap tools, and can prevent the character from obtaining more than one of the same tool.

To create an inventory component for the character, follow these steps:

1. In Unreal Editor, go to **Tools > New C++ Class**. Select **Actor Component** as the parent class and name the class `InventoryComponent`.
   Click **Create Class**.

   [![](https://dev.epicgames.com/community/api/documentation/image/abfd6b28-4096-433a-b82c-1040ff25e0d6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/abfd6b28-4096-433a-b82c-1040ff25e0d6?resizing_type=fit)
2. In VS, at the top of `InventoryComponent.h`, forward declare a `UEquippableToolDefinition`. This is the class you’ll be storing in your inventory.

   C++

   ```
   #include "CoreMinimal.h"
   #include "Components/ActorComponent.h"
   #include "InventoryComponent.generated.h"

   // --- New Code Start --- 
   class UEquippableToolDefinition;
   // --- New Code End --- 

   UCLASS( ClassGroup=(Custom), meta=(BlueprintSpawnableComponent) )
   class ADVENTUREGAME_API UInventoryComponent : public UActorComponent
   ```

   Expand code  Copy full snippet(13 lines long)
3. In the `public` section, declare a new `TArray` of  `UEquippableToolDefinition` pointers named `ToolInventory`. Give this the `UPROPERTY()` macro with `VisibleAnywhere`, `BlueprintReadOnly`, and `Category = "Tools"`.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | public: |
   |  | // Sets default values for this component's properties |
   |  | UInventoryComponent(); |
   |  |  |
   |  | // --- New Code Start --- |
   |  | // The array of tools stored in this inventory. |
   |  | UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Tools") |
   |  | TArray<TObjectPtr<UEquippableToolDefinition>> ToolInventory; |
   |  | // --- New Code End --- |
   ```

   public:
   // Sets default values for this component&#39;s properties
   UInventoryComponent();
   // --- New Code Start ---
   // The array of tools stored in this inventory.
   UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = &quot;Tools&quot;)
   TArray&lt;TObjectPtr&lt;UEquippableToolDefinition&gt;&gt; ToolInventory;
   // --- New Code End --- 

   Copy full snippet(9 lines long)

   This inventory only stores tools, but you can expand this to include any type of item you want. A more generic implementation would store only `UItemDefinition` or `TSubclassOf<UItemDefinition>` values to build a more complex inventory with UI, icons, sound effects, cost, and other item properties.

Your complete `InventoryComponent.h` file should now look like the following:

C++

```
// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "Components/ActorComponent.h"
#include "InventoryComponent.generated.h"

class UEquippableToolDefinition;
```

Expand code  Copy full snippet(33 lines long)

### Add Tool and Inventory Declarations to the Character

Now that you have a place to store your items, you’re ready to upgrade your character with logic that grants them items.

To add tool and inventory forward declarations and `#include` statements to your character class, follow these steps:

1. To start, at the top of your character’s `.h` file, forward declare the `UItemDefinition`, `AEquippableToolBase`, `UEquippableToolDefinition`, and `UInventoryComponent` classes.

   C++

   ```
   #pragma once

   #include "CoreMinimal.h"
   #include "Camera/CameraComponent.h"
   #include "GameFramework/Character.h"
   #include "EnhancedInputComponent.h"
   #include "EnhancedInputSubsystems.h" 
   #include "InputActionValue.h"
   #include "AdventureCharacter.generated.h"
   ```

   Expand code  Copy full snippet(20 lines long)
2. At the top of your character's `.cpp` file, add an `#include` for `EquippableToolDefinition`, `InventoryComponent.h`, and `EquippableToolBase.h`.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | #include "AdventureCharacter.h" |
   |  | #include "Animation/AnimBlueprint.h" |
   |  | // --- New Code Start --- |
   |  | #include "InventoryComponent.h" |
   |  | #include "EquippableToolDefinition.h" |
   |  | #include "EquippableToolBase.h" |
   |  | // --- New Code End --- |
   ```

   #include &quot;AdventureCharacter.h&quot;
   #include &quot;Animation/AnimBlueprint.h&quot;
   // --- New Code Start ---
   #include &quot;InventoryComponent.h&quot;
   #include &quot;EquippableToolDefinition.h&quot;
   #include &quot;EquippableToolBase.h&quot;
   // --- New Code End --- 

   Copy full snippet(7 lines long)

### Create the Character’s Inventory Component

In the character’s `.h` file, in the `public` section, declare a `TObjectPtr` to a `UInventoryComponent` named `InventoryComponent`. Give it a `UPROPERTY()` macro with `VisibleAnywhere` and `Category = "Inventory"`.

C++

```
|  |  |
| --- | --- |
|  | // Inventory Component |
|  | UPROPERTY(VisibleAnywhere, Category = "Inventory") |
|  | TObjectPtr<UInventoryComponent> InventoryComponent; |
```

// Inventory Component
UPROPERTY(VisibleAnywhere, Category = "Inventory")
TObjectPtr<UInventoryComponent> InventoryComponent;

Copy full snippet(3 lines long)

In your character’s `.cpp` file, in the constructor function, after you create the Mesh Component subobject, create a default `UInventoryComponent` subobject named `InventoryComponent`. This ensures your inventory is set up properly when the Character spawns.

C++

```
// Sets default values
AAdventureCharacter::AAdventureCharacter()
{
	// Set this character to call Tick() every frame.  You can turn this off to improve performance if you don't need it
	PrimaryActorTick.bCanEverTick = true;

	// COMPONENT CREATION
		// Create a first-person camera component
		FirstPersonCameraComponent = CreateDefaultSubobject<UCameraComponent>(TEXT("FirstPersonCamera"));
		check(FirstPersonCameraComponent != nullptr);
```

Expand code  Copy full snippet(19 lines long)

### Check Existing Inventory

Before you attach the tool, check if the player already has the tool so you don’t equip it multiple times.

To check if the tool is already owned, follow these steps:

1. In the character’s `.h` file, in the `public` section, declare a function named `IsToolAlreadyOwned()` that takes a `UEquippableToolDefinition` pointer and returns true if that tool already exists in the player’s inventory.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Returns whether or not the player already owns this tool |
   |  | UFUNCTION() |
   |  | bool IsToolAlreadyOwned(UEquippableToolDefinition* ToolDefinition); |
   ```

   // Returns whether or not the player already owns this tool
   UFUNCTION()
   bool IsToolAlreadyOwned(UEquippableToolDefinition\* ToolDefinition);

   Copy full snippet(3 lines long)
2. In your character’s `.cpp` file `AdventureCharacter.cpp`, implement the `IsToolAlreadyOwned()` function. Inside, in a `for` loop, get each tool in the character’s inventory by accessing the `InventoryComponent->ToolInventory` array.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | bool AAdventureCharacter::IsToolAlreadyOwned(UEquippableToolDefinition* ToolDefinition) |
   |  | { |
   |  | // Check that the character does not yet have this particular tool |
   |  | for (UEquippableToolDefinition* InventoryItem : InventoryComponent->ToolInventory) |
   |  | { |
   |  | } |
   |  | } |
   ```

   bool AAdventureCharacter::IsToolAlreadyOwned(UEquippableToolDefinition\* ToolDefinition)
   {
   // Check that the character does not yet have this particular tool
   for (UEquippableToolDefinition\* InventoryItem : InventoryComponent-&gt;ToolInventory)
   {
   }
   }

   Copy full snippet(7 lines long)
3. In an `if` statement, check if the `ToolDefinition->ID` from the tool passed to this function matches the `InventoryItem->ID`. If so, `return true` since the character already owns this tool. Otherwise, after the `for` loop, `return false` because `ToolDefinition` didn’t match any existing inventory items and is therefore a new item.

   C++

   ```
   bool AAdventureCharacter::IsToolAlreadyOwned(UEquippableToolDefinition* ToolDefinition)
   {
   	// Check that the character does not yet have this particular tool
   	for (UEquippableToolDefinition* InventoryItem : InventoryComponent->ToolInventory)
   	{
   		// --- New Code Start --- 
   		if (ToolDefinition->ID == InventoryItem->ID)
   		{
   			return true;
   		}
   ```

   Expand code  Copy full snippet(17 lines long)

### Attach a Tool

To create and call `AttachTool()` to attach a new tool to the character, follow these steps:

1. In your character’s `.h` file, in the `public` section, declare a function named `AttachTool()` that takes a `UEquippableToolDefinition` pointer. This function attempts to equip the tool within the `ToolDefinition` to the player.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Attaches and equips a tool to the player |
   |  | UFUNCTION() |
   |  | void AttachTool(UEquippableToolDefinition* ToolDefinition); |
   ```

   // Attaches and equips a tool to the player
   UFUNCTION()
   void AttachTool(UEquippableToolDefinition\* ToolDefinition);

   Copy full snippet(3 lines long)
2. In the `protected` section, declare a `TObjectPtr` to an `AEquippableToolBase` named `EquippedTool`. Give it `VisibleAnywhere`, `BlueprintReadOnly`, and `Category = Tools UPROPERTY()` specifiers.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // The currently-equipped tool |
   |  | UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Tools") |
   |  | TObjectPtr<AEquippableToolBase> EquippedTool; |
   ```

   // The currently-equipped tool
   UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = &quot;Tools&quot;)
   TObjectPtr&lt;AEquippableToolBase&gt; EquippedTool;

   Copy full snippet(3 lines long)
3. In your character’s `.cpp` file, implement `AttachTool()`. First, in an `if` statement, check if the Character already has the tool by calling `IsToolAlreadyOwned()`.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | void AAdventureCharacter::AttachTool(UEquippableToolDefinition* ToolDefinition) |
   |  | { |
   |  | // Only equip this tool if it isn't already owned |
   |  | if (!IsToolAlreadyOwned(ToolDefinition)) |
   |  | { |
   |  | } |
   |  | } |
   ```

   void AAdventureCharacter::AttachTool(UEquippableToolDefinition\* ToolDefinition)
   {
   // Only equip this tool if it isn&#39;t already owned
   if (!IsToolAlreadyOwned(ToolDefinition))
   {
   }
   }

   Copy full snippet(7 lines long)

#### Spawn a Tool Actor

The `AEquippableToolBase` tool stored inside `ToolDefinition` is an Actor, so it may not be loaded when `AttachTool()` is called. To handle this, you’re going to spawn a new instance of the tool using the `SpawnActor()` function.

`SpawnActor()` is part of the **UWorld** object, which is the core object that represents the map and the actors in it. Access it by calling the `GetWorld()` function from any Actor.

In the `if` statement inside `AttachTool`, declare a new `AEquippableToolBase` pointer named **ToolToEquip**. Set this equal to the result of calling `GetWorld()->SpawnActor()`, passing the `ToolDefinition->ToolAsset` as the Actor to spawn and`this->GetActorTransform()` as the location to spawn it.

C++

```
|  |  |
| --- | --- |
|  | // Only equip this tool if it isn't already owned |
|  | if (!IsToolAlreadyOwned(ToolDefinition)) |
|  | { |
|  | // Spawn a new instance of the tool to equip |
|  | AEquippableToolBase* ToolToEquip = GetWorld()->SpawnActor<AEquippableToolBase>(ToolDefinition->ToolAsset, this->GetActorTransform()); |
|  | } |
```

// Only equip this tool if it isn't already owned
if (!IsToolAlreadyOwned(ToolDefinition))
{
// Spawn a new instance of the tool to equip
AEquippableToolBase\* ToolToEquip = GetWorld()->SpawnActor<AEquippableToolBase>(ToolDefinition->ToolAsset, this->GetActorTransform());
}

Copy full snippet(6 lines long)

When you pass `ToolDefinition->ToolAsset` to `SpawnActor`, UE knows to look at `ToolAsset`’s class type and spawn that type of Actor. (`ToolAsset` is the `EquippableToolBase` Actor associated with that `ToolDefinition`.)

#### Attach an Item to the Character

To attach the spawned tool actor to your character, follow these steps:

1. In `AttachTool`, after the `ToolToEquip` declaration, declare a new `FAttachementTransformRules` named `AttachementRules`.

   C++

   ```
   void AAdventureCharacter::AttachTool(UEquippableToolDefinition* ToolDefinition)
   {
   	// Only equip this tool if it isn't already owned
   	if (!IsToolAlreadyOwned(ToolDefinition))
   	{
   		// Spawn a new instance of the tool to equip
   		AEquippableToolBase* ToolToEquip = GetWorld()->SpawnActor<AEquippableToolBase>(ToolDefinition->ToolAsset, this->GetActorTransform());

   		// --- New Code Start ---
   		FAttachmentTransformRules AttachmentRules();
   ```

   Expand code  Copy full snippet(13 lines long)

   `FAttachementTransformRules` is a struct that defines how to handle location, rotation, and scale when attaching. It takes `EAttachmentRules` and a bool `InWeldSimulatedBodies` at the end to tell UE if physics is involved. When true, UE welds both bodies together so they can interact as one when moving around. Some popular attachment rules include `KeepRelative` (maintain relative transform to parent), `KeepWorld` (maintain world transform), and `SnapToTarget` (snap to parent's transform).
2. In your `AttachmentRules` definition, add `EAttachmentRule::SnapToTarget` and `true`.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Attach the tool to the First Person Character |
   |  | FAttachmentTransformRules AttachmentRules(EAttachmentRule::SnapToTarget, true); |
   ```

   // Attach the tool to the First Person Character
   FAttachmentTransformRules AttachmentRules(EAttachmentRule::SnapToTarget, true);

   Copy full snippet(2 lines long)
3. Call `ToolToEquip->AttachToActor()` to attach the tool to the character, followed by `ToolToEquip->AttachToComponent()` to attach the tool to the right-hand socket of the first-person mesh component.

   `AttachToActor` attaches an Actor to a target parent Actor, and `AttachToComponent` attaches an Actor’s root component to the target component. They have the following syntax:

   `MyActor->AttachToActor(ParentActor, AttachmentRules, OptionalSocketName)`

   C++

   ```
   	// Only equip this tool if it isn't already owned
   	if (!IsToolAlreadyOwned(ToolDefinition))
   	{
   		// Spawn a new instance of the tool to equip
   		AEquippableToolBase* ToolToEquip = GetWorld()->SpawnActor<AEquippableToolBase>(ToolDefinition->ToolAsset, this->GetActorTransform());

   		// Attach the tool to the First Person Character
   		FAttachmentTransformRules AttachmentRules(EAttachmentRule::SnapToTarget, true);

   		// --- New Code Start ---
   ```

   Expand code  Copy full snippet(15 lines long)

#### Add the Item’s Animations to the Character

After attaching `ToolToEquip`, set the animations on the first and third-person meshes using `SetAnimInstanceClass()`, passing the tool’s first-person and third-person animations.

C++

```
|  |  |
| --- | --- |
|  | // Attach the tool to this character, and then the right hand of their first-person mesh |
|  | ToolToEquip->AttachToActor(this, AttachmentRules); |
|  | ToolToEquip->AttachToComponent(FirstPersonMeshComponent, AttachmentRules, FName(TEXT("HandGrip_R"))); |
|  |  |
|  | // --- New Code Start --- |
|  | // Set the animations on the character's meshes. |
|  | FirstPersonMeshComponent->SetAnimInstanceClass(ToolToEquip->FirstPersonToolAnim->GeneratedClass); |
|  | GetMesh()->SetAnimInstanceClass(ToolToEquip->ThirdPersonToolAnim->GeneratedClass); |
|  | // --- New Code End --- |
```

 // Attach the tool to this character, and then the right hand of their first-person mesh
ToolToEquip->AttachToActor(this, AttachmentRules);
ToolToEquip->AttachToComponent(FirstPersonMeshComponent, AttachmentRules, FName(TEXT("HandGrip\_R")));
// --- New Code Start ---
// Set the animations on the character's meshes.
FirstPersonMeshComponent->SetAnimInstanceClass(ToolToEquip->FirstPersonToolAnim->GeneratedClass);
GetMesh()->SetAnimInstanceClass(ToolToEquip->ThirdPersonToolAnim->GeneratedClass);
// --- New Code End ---

Copy full snippet(9 lines long)

`SetAnimInstanceClass` dynamically changes the animation Blueprint at runtime for a skeletal mesh and is commonly used when equipping items and weapons with different sets of animations. `GeneratedClass` gets the actual `AnimInstance` class generated from the Blueprint.

#### Add the Item to Inventory

To make the tool belong to the character, follow these steps:

1. After setting the new animations, add the tool to the character’s inventory using `ToolInventory.Add()`.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Add the tool to this character's inventory |
   |  | InventoryComponent->ToolInventory.Add(ToolDefinition); |
   ```

   // Add the tool to this character&#39;s inventory
   InventoryComponent-&gt;ToolInventory.Add(ToolDefinition);

   Copy full snippet(2 lines long)
2. Now that the tool is attached, set the `ToolToEquip->OwningCharacter` to this character.

   C++

   ```
   ToolToEquip->OwningCharacter = this;
   ```

   ToolToEquip-&gt;OwningCharacter = this;

   Copy full snippet(1 line long)
3. You’ve finished attaching the new tool to the character, so set the `EquippedTool` to `ToolToEquip`.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Set the animations on the character's meshes. |
   |  | FirstPersonMeshComponent->SetAnimInstanceClass(ToolToEquip->FirstPersonToolAnim->GeneratedClass); |
   |  | GetMesh()->SetAnimInstanceClass(ToolToEquip->ThirdPersonToolAnim->GeneratedClass); |
   |  |  |
   |  | // Add the tool to this character's inventory |
   |  | InventoryComponent->ToolInventory.Add(ToolDefinition); |
   |  | ToolToEquip->OwningCharacter = this; |
   |  | // --- New Code Start --- |
   |  | EquippedTool = ToolToEquip; |
   |  | // --- New Code End --- |
   ```

    // Set the animations on the character&#39;s meshes.
   FirstPersonMeshComponent-&gt;SetAnimInstanceClass(ToolToEquip-&gt;FirstPersonToolAnim-&gt;GeneratedClass);
   GetMesh()-&gt;SetAnimInstanceClass(ToolToEquip-&gt;ThirdPersonToolAnim-&gt;GeneratedClass);
   // Add the tool to this character&#39;s inventory
   InventoryComponent-&gt;ToolInventory.Add(ToolDefinition);
   ToolToEquip-&gt;OwningCharacter = this;
   // --- New Code Start ---
   EquippedTool = ToolToEquip;
   // --- New Code End ---

   Copy full snippet(10 lines long)

#### Add an Item’s Controls to the Character

To add the tool’s **Input Action** and **Input Mapping Context** to the character, follow these steps:

1. In your character's .h file, in the `protected` section, declare a `TObjectPtr` to a `UInputAction` named `UseAction`. This is the “use tool” input action that you’ll bind to the tool’s `Use()` function.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Use Input Actions |
   |  | UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "Input") |
   |  | TObjectPtr<UInputAction> UseAction; |
   ```

    // Use Input Actions
   UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = &quot;Input&quot;)
   TObjectPtr&lt;UInputAction&gt; UseAction;

   Copy full snippet(3 lines long)
2. You’ll implement the input action similar to how you set up `AAdventureCharacter::BeginPlay()` in the **Bind the Input Mapping to the Character** section of [Configure Character Movement](https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-03-configure-character-movement-with-cplusplus-in-unreal-engine): getting the `PlayerController`, then the enhanced input local subsystem, using `if` statements to check for null pointers as you go.

   Add this code after `EquippedTool = ToolToEquip;`:

   C++

   ```
   		// Add the tool to this character's inventory
   		InventoryComponent->ToolInventory.Add(ToolDefinition);
   		ToolToEquip->OwningCharacter = this;
   		EquippedTool = ToolToEquip;

   		// --- New Code Start ---
   		// Get the player controller for this character
   		if (APlayerController* PlayerController = Cast<APlayerController>(Controller))
   		{
   			if (UEnhancedInputLocalPlayerSubsystem* Subsystem = ULocalPlayer::GetSubsystem<UEnhancedInputLocalPlayerSubsystem>(PlayerController->GetLocalPlayer()))
   ```

   Expand code  Copy full snippet(15 lines long)

   This time, when you add the tool’s Input Mapping Context to the player subsystem, set the priority to `1`. The priority of the player’s main mapping context (`FirstPersonContext`) is lower (`0`), so when both mapping contexts have the same key binding, the input binding in `ToolToEquip->ToolMappingContext` takes priority over `FirstPersonContext`.
3. After adding the mapping context and between the two new `if` statements, call `ToolToEquip->BindInputAction()`, passing the `UseAction` to bind the character’s input action to the tool’s `Use()` function.

   C++

   ```
   		// Get the player controller for this character
   		if (APlayerController* PlayerController = Cast<APlayerController>(Controller))
   		{
   			if (UEnhancedInputLocalPlayerSubsystem* Subsystem = ULocalPlayer::GetSubsystem<UEnhancedInputLocalPlayerSubsystem>(PlayerController->GetLocalPlayer()))
   			{
   				Subsystem->AddMappingContext(ToolToEquip->ToolMappingContext, 1);
   			}
   			// --- New Code Start ---
   			ToolToEquip->BindInputAction(UseAction);
   			// --- New Code End ---
   ```

   Expand code  Copy full snippet(11 lines long)

Your complete `AttachTool()` function should look like the following:

C++

```
void AAdventureCharacter::AttachTool(UEquippableToolDefinition* ToolDefinition)
{
	// Only equip this tool if it isn't already owned
	if (!IsToolAlreadyOwned(ToolDefinition))
	{
		// Spawn a new instance of the tool to equip
		AEquippableToolBase* ToolToEquip = GetWorld()->SpawnActor<AEquippableToolBase>(ToolDefinition->ToolAsset, this->GetActorTransform());

		// Attach the tool to the First Person Character
		FAttachmentTransformRules AttachmentRules(EAttachmentRule::SnapToTarget, true);
```

Expand code  Copy full snippet(37 lines long)

### Support Different Item Types with GiveItem()

You’ve got a way to attach tools, but because pickups and their item definitions can contain more than just tools, you need a way to know what kind of item your character is interacting with before calling `AttachTool()`.

You'll create a `GiveItem()` function to perform different actions based on the type of `ItemDefinition` passed in. You declared different types of items with the `EItemType enum` in `ItemData.h` and you can use that data now to differentiate between different item definitions.

To create a function that gives an item to the player based on its type, follow these steps:

1. In `AdventureCharacter.h`, in the `public` section, declare a function named `GiveItem()` that takes a `UItemDefinition()` pointer. Other classes call this function when attempting to give an item to the player.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Public function that other classes can call to attempt to give an item to the player |
   |  | UFUNCTION() |
   |  | void GiveItem(UItemDefinition* ItemDefinition); |
   ```

   // Public function that other classes can call to attempt to give an item to the player
   UFUNCTION()
   void GiveItem(UItemDefinition\* ItemDefinition);

   Copy full snippet(3 lines long)
2. In `AdventureCharacter.cpp`, add a function definition header for `GiveItem()`. In the function, start by declaring a `switch` statement that cases based on the `ItemType` of the item passed to this function.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | void AAdventureCharacter::GiveItem(UItemDefinition* ItemDefinition) |
   |  | { |
   |  | // Case based on the type of the item |
   |  | switch (ItemDefinition->ItemType) |
   |  | { |
   |  | } |
   |  | } |
   ```

   void AAdventureCharacter::GiveItem(UItemDefinition\* ItemDefinition)
   {
   // Case based on the type of the item
   switch (ItemDefinition-&gt;ItemType)
   {
   }
   }

   Copy full snippet(7 lines long)
3. Inside the switch statement, declare cases for `EItemType::Tool`, `EItemType::Consumable`, and a default case. In this tutorial, you’re only implementing the Tool-type item, so in the `Consumable` and `default` cases, log the type of item and break out of the switch case.

   C++

   ```
   // Case based on the type of the item
   switch (ItemDefinition->ItemType)
   {
   case EItemType::Tool:
   {
   }
   case EItemType::Consumable:
   {
   	// Not yet implemented
   	break;
   ```

   Expand code  Copy full snippet(14 lines long)
4. Inside the `Tool` case, cast the `ItemDefinition` to a `UEquippableToolDefinition` pointer named `ToolDefinition`.
5. Ensure the cast succeeded by checking if `ToolDefinition` is `null`. If it isn’t `null`, call `AttachTool()` to attach the tool to the character. Otherwise, `print` the error and `break`.

   C++

   ```
   // Case based on the type of the item
   switch (ItemDefinition->ItemType)
   {
   // If the item is a tool, attempt to cast and attach it to the character
   case EItemType::Tool:
   {
   	// --- New Code Start ---
   	UEquippableToolDefinition* ToolDefinition = Cast<UEquippableToolDefinition>(ItemDefinition);

   	if (ToolDefinition != nullptr)
   ```

   Expand code  Copy full snippet(27 lines long)

Your complete `GiveItem()` function should look like the following:

C++

```
void AAdventureCharacter::GiveItem(UItemDefinition* ItemDefinition)
{
	// Case based on the type of the item
	switch (ItemDefinition->ItemType)
	{
	case EItemType::Tool:
	{
		// If the item is a tool, attempt to cast and attach it to the character

		UEquippableToolDefinition* ToolDefinition = Cast<UEquippableToolDefinition>(ItemDefinition);
```

Expand code  Copy full snippet(29 lines long)

Last, you need an in-game trigger to set your item-granting logic in motion. When a character collides with a pickup, the pickup should call the character’s `GiveItem()` function to grant the pickup’s `ReferenceItem` to the character.

To call `GiveItem()` after a collision with the tool pickup, follow these steps:

1. In `PickupBase.cpp`, in `OnSphereBeginOverlap()`, after checking if the Character is valid,  call `Character->GiveItem(ReferenceItem)` to grant the item to your character.

   C++

   ```
   void APickupBase::OnSphereBeginOverlap(UPrimitiveComponent* OverlappedComponent, AActor* OtherActor, UPrimitiveComponent* OtherComp, int32 OtherBodyIndex, bool bFromSweep, const FHitResult& SweepResult)
   {
   	GEngine->AddOnScreenDebugMessage(-1, 5.0f, FColor::Yellow, TEXT("Attempting a pickup collision"));

   	// Checking if it's an AdventureCharacter overlapping
   	AAdventureCharacter* Character = Cast<AAdventureCharacter>(OtherActor);
   	if (Character != nullptr)
   	{
   		// --- New Code Starts ---
   		// Give the item to the character
   ```

   Expand code  Copy full snippet(18 lines long)

Now that you’ve set up your tool data and actor, you can use these to build a real tool for your character to equip in-game!

## Implement a Dart Launcher

For your first equippable tool, you’ll create a dart launcher that can launch projectiles. In this section, you’ll start by creating the tool for your character to hold and use. In the next section of this tutorial, you’ll implement projectile logic.

### Set up a New DartLauncher Class

To derive a new dart launcher class from `EquippableToolBase`, follow these steps:

1. In the Unreal Editor, go to **Tools > New C++ Class**.
2. Go to All Classes, search for **EquippableToolBase**, and select it as the parent class.
3. Name the class `DartLauncher`. Create a new folder named `Tools` in your project's `Public` folder to store the code for your tools. Click **Create Class**.

   [![](https://dev.epicgames.com/community/api/documentation/image/84cba007-f2f4-4363-9b3e-dbd6322fb0aa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/84cba007-f2f4-4363-9b3e-dbd6322fb0aa?resizing_type=fit)
4. In Visual Studio,  at the top of `DartLauncher.h`:

   1. Add the `BlueprintType` and `Blueprintable` specifiers to the `UCLASS()` macro.
   2. Add a `public` section, and declare overrides for both the `Use()` and `BindInputAction()` functions from `AEquippableToolBase`.

   Your complete `DartLauncher.h` class should look like the following:

   C++

   ```
   // Copyright Epic Games, Inc. All Rights Reserved.

   #pragma once

   #include "CoreMinimal.h"
   #include "EquippableToolBase.h"
   #include "DartLauncher.generated.h"

   // --- New Code Start ---
   UCLASS(BlueprintType, Blueprintable)
   ```

   Expand code  Copy full snippet(24 lines long)
5. In `DartLauncher.cpp`, at the top of the file, add an include statement for `”AdventureCharacter.h”`. You’ll need this in the `BindInputAction()` function.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | #include "Tools/DartLauncher.h" |
   |  | #include "AdventureCharacter.h" |
   ```

   #include &quot;Tools/DartLauncher.h&quot;
   #include &quot;AdventureCharacter.h&quot;

   Copy full snippet(2 lines long)

Next, you'll start adding new logic to the dart launcher.

### Implement Tool Controls

Now that you’re working in a specific tool and know what function you’re binding, you can implement `BindInputAction()`.

To bind the tool's Use function, follow these steps:

1. In `DartLauncher.cpp`, add a function definition header for the `Use()` function.
2. Inside `Use()`, add a debug message that notifies when the player triggers the function.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | #include "Tools/DartLauncher.h" |
   |  | #include "AdventureCharacter.h" |
   |  |  |
   |  | void ADartLauncher::Use() |
   |  | { |
   |  | GEngine->AddOnScreenDebugMessage(-1, 5.0f, FColor::Yellow, TEXT("Using the dart launcher!")); |
   |  | } |
   ```

   #include &quot;Tools/DartLauncher.h&quot;
   #include &quot;AdventureCharacter.h&quot;
   void ADartLauncher::Use()
   {
   GEngine-&gt;AddOnScreenDebugMessage(-1, 5.0f, FColor::Yellow, TEXT(&quot;Using the dart launcher!&quot;));
   }

   Copy full snippet(7 lines long)
3. Add a function definition header for `BindInputAction()`. Inside the function, in an `if` statement, get the player controller for the `OwningCharacter` by using `GetController()`, and then cast it to `APlayerController`. This is similar to how you added a mapping context in the `AAdventureCharacter::BeginPlay()` function.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | void ADartLauncher::BindInputAction(const UInputAction* InputToBind) |
   |  | { |
   |  | // Set up action bindings |
   |  | if (APlayerController* PlayerController = Cast<APlayerController>(OwningCharacter->GetController())) |
   |  | { |
   |  |  |
   |  | } |
   |  | } |
   ```

   void ADartLauncher::BindInputAction(const UInputAction\* InputToBind)
   {
   // Set up action bindings
   if (APlayerController\* PlayerController = Cast&lt;APlayerController&gt;(OwningCharacter-&gt;GetController()))
   {
   }
   }

   Copy full snippet(8 lines long)
4. Bind the `Use` function similar to how you bound your movement actions in the **Binding Movement Actions** section of [Configure Character Movement](https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-03-configure-character-movement-with-cplusplus-in-unreal-engine):

   In another `if` statement, declare a new `UEnhancedInputComponent` pointer named `EnhancedInputComponent`. Set this equal to the result of calling `Cast()` on the `PlayerInputComponent` passed to this function while casting it to `UEnhancedInputComponent`.

   C++

   ```
   void ADartLauncher::BindInputAction(const UInputAction* InputToBind)
   {
   	// Set up action bindings
   	if (APlayerController* PlayerController = Cast<APlayerController>(OwningCharacter->GetController()))
   	{
   		// --- New Code Start ---
   		if (UEnhancedInputComponent* EnhancedInputComponent = Cast<UEnhancedInputComponent>(PlayerController->InputComponent))
   		{

   		}
   ```

   Expand code  Copy full snippet(13 lines long)
5. Use `BindAction` to bind the `ADartLauncher::Use` action to the `InputToBind` action that’s passed to this function using `BindAction()`. This binds the InputAction to `Use();` so that when the given action happens, `Use()` is called.

   C++

   ```
   void ADartLauncher::BindInputAction(const UInputAction* InputToBind)
   {
   	// Set up action bindings
   	if (APlayerController* PlayerController = Cast<APlayerController>(OwningCharacter->GetController()))
   	{
   		if (UEnhancedInputComponent* EnhancedInputComponent = Cast<UEnhancedInputComponent>(PlayerController->InputComponent))
   		{
   			// --- New Code Start ---
   			// Fire
   			EnhancedInputComponent->BindAction(InputToBind, ETriggerEvent::Triggered, this, &ADartLauncher::Use);
   ```

   Expand code  Copy full snippet(14 lines long)

   When you set up your character’s movement, you used `CastChecked<>` which crashes the game if it fails. Here, you don’t want to stop the game if the pickup controls don’t get initialized properly, so just use `Cast<>`. Only use `CastChecked<>` when a failed cast would indicate a serious bug.
6. Save your code and compile it.

Your `BindInputAction()` function and your complete `DartLauncher.cpp` class should now look like this:

C++

```
// Copyright Epic Games, Inc. All Rights Reserved.


#include "Tools/DartLauncher.h"
#include "AdventureCharacter.h"


void ADartLauncher::Use()
{
	GEngine->AddOnScreenDebugMessage(-1, 5.0f, FColor::Yellow, TEXT("Using the dart launcher!"));
```

Expand code  Copy full snippet(25 lines long)

### Adapt an Animation Blueprint For Your Character

The first-person template includes a sample Animation Blueprint for weapon-type items, but you’ll need to make a few changes to the Blueprint so it can work with your dart launcher.

To add a tool-holding Animation Blueprint to your character, take the following steps:

1. In the **Content Browser**, go to the **Content > Variant\_Shooter > Anim** folder, right-click the `ABP_FP_Pistol` Animation Blueprint, and select **Duplicate**.
2. Name this copy **ABP\_FP\_DartLauncher**, drag it into the **Content > FirstPerson > Anims** folder, and select **Move Here**.

   [![](https://dev.epicgames.com/community/api/documentation/image/9c3c55e6-1076-4539-b2e6-66fde6f84765?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9c3c55e6-1076-4539-b2e6-66fde6f84765?resizing_type=fit)

   The third-person Animation Blueprint, `ABP_TP_Pistol` , doesn’t use any logic specific to the `BP_FPShooter` character so you can use it as-is and don't need to make a custom copy.
3. Open the new Animation Blueprint.
4. Near the top of the Event Graph, zoom in to the group of nodes that begins with an **Event Blueprint Begin Play** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/1c5d41b9-ab86-42a1-a1e5-54ee6e7eed42?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1c5d41b9-ab86-42a1-a1e5-54ee6e7eed42?resizing_type=fit)

   In the **My Blueprint** panel, in the **Graph** section, expand **EventGraph** and double-click **Event Blueprint Begin Play** to find that node in the graph.

   This Blueprint gets **First Person Mesh** and **First Person Camera** variables from `BP_FPShooter`, so you’ll change this to use your Character Blueprint instead (this tutorial uses `BP_AdventureCharacter`).
5. Click each of these nodes and press **Delete**:

   * **Cast To BP\_FPShooter**
   * **First Person Mesh** variable getter
   * **First Person Camera** variable getter
6. Right-click on the **Event Graph**, then search for and select a **Cast To BP\_AdventureCharacter** node.

   [![](https://dev.epicgames.com/community/api/documentation/image/19440113-fe9d-4f9c-85f0-ef670a32cbe1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/19440113-fe9d-4f9c-85f0-ef670a32cbe1?resizing_type=fit)
7. Connect the execution pins from **Event Blueprint Begin Play** to the new node, and then to the **Set First Person Mesh** node.
8. Connect the **Try Get Pawn Owner** node’s **Return Value** pin to the **Cast To** node’s **Object** pin.

   [![](https://dev.epicgames.com/community/api/documentation/image/cb607252-69c1-4527-86c4-1803d5ec974b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cb607252-69c1-4527-86c4-1803d5ec974b?resizing_type=fit)
9. To create a new node off of **Cast To BP\_AdventureCharacter**, click the **As BP My Adventure Character** pin and drag to an empty spot in the graph.

   [![](https://dev.epicgames.com/community/api/documentation/image/3a8e46b8-5ca0-44a1-ab1a-ff0adb06dcf8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3a8e46b8-5ca0-44a1-ab1a-ff0adb06dcf8?resizing_type=fit)
10. Search for and **Get Mesh** and select it under **Variables > Character**. Connect the new node’s **Mesh** pin to the **Set First Person Mesh** node.
11. For the camera, drag another node from the **As BP My First Person Character** pin, and search for and select **Get Component by Class**.

    Ensure you create a **Get Component by Class** node with “by” in lowercase.
12. On the new node, set the **Component Class** to **Camera Component**. Then, connect the **Return Value** pin to the **Set First Person Camera** node.

    [![](https://dev.epicgames.com/community/api/documentation/image/dbe4e68c-cc5d-4c3e-be99-f1936e7ab307?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dbe4e68c-cc5d-4c3e-be99-f1936e7ab307?resizing_type=fit)
13. Save your `ABP_FP_DartLauncher` Blueprint and compile it.

### Define Dart Launcher Controls

Your dart launcher needs an input action and input mapping context so the character can shoot projectiles from the tool.

To create player controls for your dart launcher tool, follow these steps:

1. In the **Content Browser**, go to the **Input > Actions** folder.
2. Create and set up a “use tool” Input Action:

   1. Click **Add**, go to **Input**, and select **Input Action**. Name it **IA\_UseTool**.

      [![](https://dev.epicgames.com/community/api/documentation/image/275793eb-4060-4f95-9e8a-d3a8f0a6c55f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/275793eb-4060-4f95-9e8a-d3a8f0a6c55f?resizing_type=fit)
   2. Double-click **IA\_UseTool** to open it. In its **Details** panel, ensure its **Value Type** is **Digital (bool)**.
   3. Next to **Triggers**, click the **plus** button (**+**), then select **Pressed** from the list of triggers.

      [![](https://dev.epicgames.com/community/api/documentation/image/23103bc1-f9f9-4ba3-b9ae-d3d76e149792?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/23103bc1-f9f9-4ba3-b9ae-d3d76e149792?resizing_type=fit)
   4. Save and close the Input Action.
3. Back in the **Content Browser**, go to the **Input** **folder**.
4. Create and set up a new Input Mapping Context that maps the left mouse button and gamepad right trigger to the dart launcher's Use action:

   1. Create a new **Input Mapping Context** named **IMC\_DartLauncher**.

      [![](https://dev.epicgames.com/community/api/documentation/image/f628c3f0-22ab-4e76-baab-0f7e1ee52bb3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f628c3f0-22ab-4e76-baab-0f7e1ee52bb3?resizing_type=fit)
   2. Open **IMC\_DartLauncher**. Click the plus button next to **Mappings**.
   3. In the dropdown list, select `IA_UseTool`.
   4. Click the arrow to expand the mapping. Click the keyboard button, then press your left mouse button to bind that button to `IA_UseTool`.
   5. Next to **IA\_UseTool**, click **+** to add another binding. In the dropdown list, expand **Gamepad** and select **Gamepad Right Trigger Axis**.

      [![](https://dev.epicgames.com/community/api/documentation/image/b9baa77a-9643-4513-a1de-f8e1c62da995?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b9baa77a-9643-4513-a1de-f8e1c62da995?resizing_type=fit)
   6. Save and close the Input Mapping Context.

### Assign the Use Input Action

To assign `IA_UseTool` to the character's **Use Action** variable, follow these steps:

1. Open your character's Blueprint.
2. In the **Details** panel, in the **Input** section, set **Use Action** to `IA_UseTool`.

   [![](https://dev.epicgames.com/community/api/documentation/image/d35d6599-e2d7-4005-be92-0a45f29238c9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d35d6599-e2d7-4005-be92-0a45f29238c9?resizing_type=fit)
3. Compile and save your Blueprint.

### Create the DartLauncher Blueprint

Now you can bring everything together in a new DartLauncher Blueprint.

To create the Dart Launcher Blueprint from the DartLauncher class, follow these steps:

1. In the Content Browser, go to your C++ Classes > *ProjectName*> Public > Tools folder, right-click your DartLauncher class, and create a new Blueprint class.
2. Name it `BP_DartLauncher`. Right-click your FirstPerson > Blueprints folder to create a new folder named Tools to store your equippable items, then finish creating the Blueprint.
3. In the Blueprint's **Details** panel, set the following default properties:

   1. Set **First Person Tool Anim** to `ABP_FP_DartLauncher`.
   2. Set **Third Person Tool Anim** to `ABP_TP_Pistol`.
   3. Set **Tool Mapping Context** to `IMC_DartLauncher`.
   4. Leave **Owning Character** empty.

   [![](https://dev.epicgames.com/community/api/documentation/image/e52eff20-5a1c-45d9-bbfd-d196bd466cc6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e52eff20-5a1c-45d9-bbfd-d196bd466cc6?resizing_type=fit)

   If you can only see your Blueprint’s Details panel and not the full Blueprint Editor with Event Graph and Components tab, click **Open Full Blueprint Editor** in the note near the top of the window.

   [![](https://dev.epicgames.com/community/api/documentation/image/3d5693d4-7057-4bb6-bda9-fbcf7c0cf78b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3d5693d4-7057-4bb6-bda9-fbcf7c0cf78b?resizing_type=fit)
4. In the **Components** tab, click the **Tool Mesh Component** and set the **Skeletal Mesh Asset** to `SKM_Pistol`.

   [![](https://dev.epicgames.com/community/api/documentation/image/24dc6e6d-0f1c-4139-9281-58b51b333b77?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/24dc6e6d-0f1c-4139-9281-58b51b333b77?resizing_type=fit)

### Create the Dart Launcher Data Asset

To create a Data Asset to store this Blueprint’s data, follow these steps:

1. In the **Content Browser**, in the **FirstPerson > Data** folder, create a new Data Asset and pick **Equippable Tool Definition** as the Data Asset instance. Name this asset `DA_DartLauncher`.
2. Inside `DA_DartLauncher`, in the **Details** panel, set the following properties:

   * Set **Tool Asset** to `BP_DartLauncher`.
   * Set **ID** to **tool\_001**.
   * Set **Item Type** to **Tool**.
   * Set **World Mesh** to `SM_Pistol`.

   [![](https://dev.epicgames.com/community/api/documentation/image/ae599263-87cd-4417-84ea-a81265b7dc4e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ae599263-87cd-4417-84ea-a81265b7dc4e?resizing_type=fit)
3. Enter a **Name** and **Description**.
4. Save your Data Asset.

### Create a Data Table for Tools

Although this tool could go in your `DT_PickupData` table, it’s helpful to organize your tables to track specific things. For example, you could have different tables for items that specific classes can equip, or tables of items that different enemies drop when defeated. In this tutorial, you’ll have a table for consumables and a table for tools.

To create a new Data Table to track your tool items, follow these steps:

1. In the **Content Browser**, go to the **FirstPerson > Data** folder, and create a new **Data** **Table**.
2. Select **ItemData** as the row structure.
3. Name the table `DT_ToolData`, then open it.

   [![](https://dev.epicgames.com/community/api/documentation/image/60bf2e34-5c78-4207-b39a-fb0fa0716048?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/60bf2e34-5c78-4207-b39a-fb0fa0716048?resizing_type=fit)
4. Inside `DT_ToolData`, click **Add** to create a new row for your dart launcher.
5. With the new row selected, set the following fields:

   * Change the **Row Name** and **ID** to `tool_001`.
   * Set **Item Type** to **Tool**.
   * Enter the same **Name** and **Description** you set in the Data Asset.
   * Set **Item Base** to the `DA_DartLauncher`.

   [![](https://dev.epicgames.com/community/api/documentation/image/0b0d8057-0651-4033-b9c0-fb7b008b2a2b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0b0d8057-0651-4033-b9c0-fb7b008b2a2b?resizing_type=fit)
6. Save and close the Data Table.

## Test a Dart Launcher Pickup In Game

You’ve modified your pickup class to grant an item to the user, created an equippable item class that gives the player a new mesh, animations, and controls, and set up an equippable dart launcher tool.

It’s time to bring it all together and create the in-game pickup that triggers all the equippable item logic you’ve set up in this part of the tutorial. `PickupBase` handles picking up an object, and `EquippableToolBase` handles giving an item to the player.

In the **Content Browser**, go to **Content > FirstPerson > Blueprints** and drag a new `BP_PickupBase` into the level. Set the **Pickup Item ID** to `tool_001`and the **Pickup Data Table** to `DT_ToolData`.

[![](https://dev.epicgames.com/community/api/documentation/image/c1fa4e33-9241-4dc2-8bc9-4de441520804?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c1fa4e33-9241-4dc2-8bc9-4de441520804?resizing_type=fit)

Click **Play** to test out your game. When the game begins, your pickup should initialize to the dart launcher. When you run over your pickup, your character should start holding the tool!

## Next Up

In the final section, you’ll implement projectile physics in your dart launcher and make it launch foam darts!

* [![Implement a Projectile](https://dev.epicgames.com/community/api/documentation/image/25ecf04a-ccd5-4507-80d4-446d937d850c?resizing_type=fit&width=640&height=640)

  Implement a Projectile

  Learn to use C++ to implement projectiles and spawn them during gameplay.](https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-08-implement-a-projectile-in-unreal-engine)

## Complete Code

C++

ItemDefinition.h

```
// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "Engine/DataAsset.h"
#include "Data/ItemData.h"
#include "ItemDefinition.generated.h"

// Defines an item definition built from data table data.
```

Expand code  Copy full snippet(32 lines long)

C++

EquippableToolDefinition.h

```
// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "ItemDefinition.h"
#include "EquippableToolDefinition.generated.h"

class AEquippableToolBase;
class UInputMappingContext;
```

Expand code  Copy full snippet(25 lines long)

C++

EquippableToolDefinition.cpp

```
// Copyright Epic Games, Inc. All Rights Reserved.

#include "EquippableToolDefinition.h"

UEquippableToolDefinition* UEquippableToolDefinition::CreateItemCopy(UObject* Outer) const
{
	// If we need an Outer, use GetTransientPackage
	if (!Outer)
	{
		Outer = GetTransientPackage();
```

Expand code  Copy full snippet(15 lines long)

C++

InventoryComponent.h

```
// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "Components/ActorComponent.h"
#include "InventoryComponent.generated.h"

class UEquippableToolDefinition;
```

Expand code  Copy full snippet(33 lines long)

C++

DartLauncher.h

```
// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "EquippableToolBase.h"
#include "DartLauncher.generated.h"


UCLASS()
```

Expand code  Copy full snippet(21 lines long)

 N 

C++

DartLauncher.cpp

```
// Copyright Epic Games, Inc. All Rights Reserved.


#include "Tools/DartLauncher.h"
#include "AdventureCharacter.h"


void ADartLauncher::Use()
{
	GEngine->AddOnScreenDebugMessage(-1, 5.0f, FColor::Yellow, TEXT("Using the dart launcher!"));
```

Expand code  Copy full snippet(25 lines long)

C++

EquippableToolBase.h

```
// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "EnhancedInputSubsystems.h"      // CHAT GPT SAID NOT NEEDED?
#include "Animation/AnimBlueprint.h"
#include "Components/SkeletalMeshComponent.h"
#include "EquippableToolBase.generated.h"
```

Expand code  Copy full snippet(61 lines long)

C++

EquippableToolBase.cpp

```
// Copyright Epic Games, Inc. All Rights Reserved.


#include "EquippableToolBase.h"
#include "InputMappingContext.h"
#include "AdventureCharacter.h"

// Sets default values
AEquippableToolBase::AEquippableToolBase()
```

Expand code  Copy full snippet(44 lines long)

C++

AdventureCharacter.h

```
// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "Camera/CameraComponent.h"
#include "GameFramework/Character.h"
#include "EnhancedInputComponent.h"
#include "EnhancedInputSubsystems.h" 
#include "InputActionValue.h"
```

Expand code  Copy full snippet(113 lines long)

C++

AdventureCharacter.cpp

```
// Copyright Epic Games, Inc. All Rights Reserved.


#include "AdventureCharacter.h"
#include "InventoryComponent.h"
#include "EquippableToolDefinition.h"
#include "EquippableToolBase.h"

// Sets default values
AAdventureCharacter::AAdventureCharacter()
```

Expand code  Copy full snippet(233 lines long)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Before You Begin](/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools?application_version=5.7#beforeyoubegin)
* [Create Reference Items With a New CreateItemCopy Function](/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools?application_version=5.7#createreferenceitemswithanewcreateitemcopyfunction)
* [Define Equippable Tool Data](/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools?application_version=5.7#defineequippabletooldata)
* [Set Up an Equippable Tool Actor](/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools?application_version=5.7#setupanequippabletoolactor)
* [Declare Tool Animations](/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools?application_version=5.7#declaretoolanimations)
* [Create the Tool’s Mesh](/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools?application_version=5.7#createthetool%E2%80%99smesh)
* [Declaring the Tool’s Owner](/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools?application_version=5.7#declaringthetool%E2%80%99sowner)
* [Declare Input and a Use-Tool Function](/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools?application_version=5.7#declareinputandause-toolfunction)
* [Grant Items to a Character](/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools?application_version=5.7#grantitemstoacharacter)
* [Build an Inventory Component](/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools?application_version=5.7#buildaninventorycomponent)
* [Add Tool and Inventory Declarations to the Character](/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools?application_version=5.7#addtoolandinventorydeclarationstothecharacter)
* [Create the Character’s Inventory Component](/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools?application_version=5.7#createthecharacter%E2%80%99sinventorycomponent)
* [Check Existing Inventory](/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools?application_version=5.7#checkexistinginventory)
* [Attach a Tool](/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools?application_version=5.7#attachatool)
* [Spawn a Tool Actor](/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools?application_version=5.7#spawnatoolactor)
* [Attach an Item to the Character](/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools?application_version=5.7#attachanitemtothecharacter)
* [Add the Item’s Animations to the Character](/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools?application_version=5.7#addtheitem%E2%80%99sanimationstothecharacter)
* [Add the Item to Inventory](/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools?application_version=5.7#addtheitemtoinventory)
* [Add an Item’s Controls to the Character](/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools?application_version=5.7#addanitem%E2%80%99scontrolstothecharacter)
* [Support Different Item Types with GiveItem()](/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools?application_version=5.7#supportdifferentitemtypeswithgiveitem())
* [Implement a Dart Launcher](/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools?application_version=5.7#implementadartlauncher)
* [Set up a New DartLauncher Class](/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools?application_version=5.7#setupanewdartlauncherclass)
* [Implement Tool Controls](/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools?application_version=5.7#implementtoolcontrols)
* [Adapt an Animation Blueprint For Your Character](/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools?application_version=5.7#adaptananimationblueprintforyourcharacter)
* [Define Dart Launcher Controls](/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools?application_version=5.7#definedartlaunchercontrols)
* [Assign the Use Input Action](/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools?application_version=5.7#assigntheuseinputaction)
* [Create the DartLauncher Blueprint](/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools?application_version=5.7#createthedartlauncherblueprint)
* [Create the Dart Launcher Data Asset](/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools?application_version=5.7#createthedartlauncherdataasset)
* [Create a Data Table for Tools](/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools?application_version=5.7#createadatatablefortools)
* [Test a Dart Launcher Pickup In Game](/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools?application_version=5.7#testadartlauncherpickupingame)
* [Next Up](/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools?application_version=5.7#nextup)
* [Complete Code](/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools?application_version=5.7#completecode)

Related documents

[Code a First-Person Adventure Game

![Code a First-Person Adventure Game](https://dev.epicgames.com/community/api/documentation/image/ffc1a8f8-e7e5-42c0-b4ed-32ce6d3adbbc?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/code-a-firstperson-adventure-game-in-unreal-engine)

[Implement a Projectile

![Implement a Projectile](https://dev.epicgames.com/community/api/documentation/image/25ecf04a-ccd5-4507-80d4-446d937d850c?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/coder-08-implement-a-projectile-in-unreal-engine)
