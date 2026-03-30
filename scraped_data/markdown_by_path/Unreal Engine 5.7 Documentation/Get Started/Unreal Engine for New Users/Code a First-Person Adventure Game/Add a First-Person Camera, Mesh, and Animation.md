<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-04-adding-a-firstperson-camera-mesh-and-animation?application_version=5.7 -->

# Add a First-Person Camera, Mesh, and Animation

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
8. Add a First-Person Camera, Mesh, and Animation

# Add a First-Person Camera, Mesh, and Animation

Learn how to use C++ to attach mesh and camera components on a first-person Character.

On this page

## Before You Start

Ensure you've completed the following objectives in the previous section, [Configure Character Movement](https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-03-configure-character-movement-with-cplusplus-in-unreal-engine):

* Understand how Input Actions and Input Mapping Contexts work.
* Set up a character with forward, backward, left, right, and jump movements.

## First-Person Camera Controls

To change the camera orientation, we change the **Rotation** value of the camera’s **Transform** property. To rotate in a 3D space, objects use **Pitch**, **Roll**, and **Yaw** to control what direction they turn and along what axis.

* **Pitch**: Controls rotation along the horizontal (X) axis. Changing it rotates an object up or down, similar to nodding your head.
* **Yaw**: Controls rotation along the vertical (Y) axis. Changing it rotates an object left or right, similar to rotating right or left.
* **Roll**: Controls rotation along the longitudinal (Z) axis. Changing it rolls an object side to side, similar to leaning your head  right or left.

[![](https://dev.epicgames.com/community/api/documentation/image/b9ab7e88-76a2-46a5-9986-74516d90c03b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b9ab7e88-76a2-46a5-9986-74516d90c03b?resizing_type=fit)

Cameras in first-person games usually use Yaw and Pitch to control movement. Roll may become relevant if you’re programming a game where you need to rotate an airplane or spaceship or if you need to simulate peeking around corners.

### Explore Camera Movement in Blueprints

Open `BP_FirstPersonCharacter` to view the default character’s camera control logic in the **Blueprint Editor**. In the **EventGraph**, look at two nodes in the top-left corner of the **Camera Input** node group.

[![](https://dev.epicgames.com/community/api/documentation/image/c540ea4d-b631-417f-b45f-de84844d1ba1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c540ea4d-b631-417f-b45f-de84844d1ba1?resizing_type=fit)

Just like with `IA_Move`, the `IA_Look` input action has an **Axis2D Value Type**, so it splits movement into both **X** and **Y** values. This time, X and Y become the custom **Aim** function's **Yaw** and **Pitch** inputs.

Double-click the **Aim** function node to see the logic inside. The **Add Controller Yaw Input** and **Pitch Input** function nodes add the values to the character.

[![](https://dev.epicgames.com/community/api/documentation/image/d190be74-4e4f-4d03-b6c9-d6c8b4b0b556?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d190be74-4e4f-4d03-b6c9-d6c8b4b0b556?resizing_type=fit)

### Explore First-Person Character Components

Go to `BP_FirstPersonCharacter`‘s **Viewport** tab to view a 3D preview of the Actor and its components.

In the **Components** tab, you’ll see a structured hierarchy of attached components that define the character in the world.

Character Blueprints are automatically instantiated with:

* a **Capsule Component** that makes the character collide with objects in the world.
* a **Skeletal Mesh** component that enables animations and visualizes the character. In the **Details** panel, you’ll see this character uses `SKM_Manny_Simple` as its **Skeletal Mesh Asset**.
* A **Character Movement Component** that allows the character to move around.

[![](https://dev.epicgames.com/community/api/documentation/image/b2e2edf0-692b-4888-b3a9-a83167cd123e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b2e2edf0-692b-4888-b3a9-a83167cd123e?resizing_type=fit)

This character also has a second **Skeletal Mesh** named **FirstPersonMesh** (also using `SKM_Manny_Simple`) that is a child of the main mesh component. In first-person games, characters usually have separate meshes for both third-person and first-person contexts:

* The third-person mesh is only visible to other players or when the player is in a third-person view.
* The first-person mesh is visible to the player when they are in first-person view.

The **FirstPersonMesh** has a child **Camera Component** named **FirstPersonCamera**. This camera determines the player’s first-person view and rotates with the character as they look around. In this part of the tutorial, you’ll use C++ to instantiate a camera on your character at runtime and position it to match this camera’s position.

For more information about Character components, see the [Characters Gameplay Framework documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/characters-in-unreal-engine).

## Implement Look Input in Code

To implement this camera functionality in code, just like the movement you implemented in the previous step, you’ll bind the `IA_Look` input action to a function and then bind that function to your character.

### Declare the Look() Function and Variables

To declare the function and variables you need to implement and control the camera-look input action, follow these steps:

1. In Visual Studio, open your character’s `.h` file.

   The code samples in this tutorial use a Character class named `AdventureCharacter`.
2. When your character is built at runtime, you’ll tell UE to add a camera component to it and position the camera dynamically. To enable this functionality, add a new `#include` for `”Camera/CameraComponent.h”`:

   C++

   ```
   |  |  |
   | --- | --- |
   |  | #include "CoreMinimal.h" |
   |  | // --- New Code Start --- |
   |  | #include "Camera/CameraComponent.h" |
   |  | // --- New Code End --- |
   |  | #include "GameFramework/Character.h" |
   |  | #include "EnhancedInputComponent.h" |
   |  | #include "EnhancedInputSubsystems.h" |
   |  | #include "InputActionValue.h" |
   |  | #include "AdventureCharacter.generated.h" |
   ```

   #include &quot;CoreMinimal.h&quot;
   // --- New Code Start ---
   #include &quot;Camera/CameraComponent.h&quot;
   // --- New Code End ---
   #include &quot;GameFramework/Character.h&quot;
   #include &quot;EnhancedInputComponent.h&quot;
   #include &quot;EnhancedInputSubsystems.h&quot;
   #include &quot;InputActionValue.h&quot;
   #include &quot;AdventureCharacter.generated.h&quot;

   Copy full snippet(9 lines long)
3. In the header’s `protected` section, declare a `TObjectPtr` to a `UInputAction` named `LookAction`. Give this pointer the same `UPROPERTY()` macro as `MoveAction` and `JumpAction`.

   C++

   ```
   protected:
   	// Called when the game starts or when spawned
   	virtual void BeginPlay() override;

   	UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = Input)
   	TObjectPtr<UInputMappingContext> FirstPersonContext;

   	// Move Input Actions
   	UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = Input)
   	TObjectPtr<UInputAction> MoveAction;
   ```

   Expand code  Copy full snippet(22 lines long)

   This will point to the `IA_Look` Input Action.
4. In the `public` section, declare a new function named `Look()` that takes a const `FInputActionValue` reference named `Value`. Ensure you add a `UFUNCTION()` macro to the function.

   C++

   ```
   public:	
   	// Called every frame
   	virtual void Tick(float DeltaTime) override;

   	// Called to bind functionality to input
   	virtual void SetupPlayerInputComponent(class UInputComponent* PlayerInputComponent) override;

   	// Handles 2D Movement Input
   	UFUNCTION()
   	void Move(const FInputActionValue& Value);
   ```

   Expand code  Copy full snippet(18 lines long)
5. After the `Look()` function declaration, declare a `TObjectPtr` to a `UCameraComponent` named `FirstPersonCameraComponent`. To expose this property to Unreal Editor, add a `UPROPERTY()` macro with `VisibleAnywhere` and `Category = Camera` arguments so it appears in the **Camera**section of the **Details**panel.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // First Person camera |
   |  | UPROPERTY(VisibleAnywhere, Category = Camera) |
   |  | TObjectPtr<UCameraComponent> FirstPersonCameraComponent; |
   ```

   // First Person camera
   UPROPERTY(VisibleAnywhere, Category = Camera)
   TObjectPtr&lt;UCameraComponent&gt; FirstPersonCameraComponent;

   Copy full snippet(3 lines long)
6. Also in the `public` section, declare an `FVector` named `FirstPersonCameraOffset`. Initialize it to an `FVector` with the default values in the code block below. Include `EditAnywhere` and `Category = Camera` in its `UPROPERTY` macro so you can adjust it in Unreal Editor if needed.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Offset for the first-person camera |
   |  | UPROPERTY(EditAnywhere, Category = Camera) |
   |  | FVector FirstPersonCameraOffset = FVector(2.8f, 5.9f, 0.0f); |
   ```

   // Offset for the first-person camera
   UPROPERTY(EditAnywhere, Category = Camera)
   FVector FirstPersonCameraOffset = FVector(2.8f, 5.9f, 0.0f);

   Copy full snippet(3 lines long)

   This offset positions the camera when the character spawns.
7. You need two more properties to adjust how close-up objects (like the character's body) appear in the camera's view. Declare the following `float` variables:

   * `FirstPersonFieldOfView`: The horizontal field of view (in degrees) that this camera should use when rendering `FirstPerson`-tagged primitive components. Set to `70.0f`.
   * `FirstPersonScale`: The scale this camera should apply to `FirstPerson`-tagged primitive components. Set to `0.6f`.

   Give these properties a `UPROPERTY` macro with `EditAnywhere` and `Category = Camera` specifiers.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // First-person primitives field of view |
   |  | UPROPERTY(EditAnywhere, Category = Camera) |
   |  | float FirstPersonFieldOfView = 70.0f; |
   |  |  |
   |  | // First-person primitives view scale |
   |  | UPROPERTY(EditAnywhere, Category = Camera) |
   |  | float FirstPersonScale = 0.6f; |
   ```

   // First-person primitives field of view
   UPROPERTY(EditAnywhere, Category = Camera)
   float FirstPersonFieldOfView = 70.0f;
   // First-person primitives view scale
   UPROPERTY(EditAnywhere, Category = Camera)
   float FirstPersonScale = 0.6f;

   Copy full snippet(7 lines long)

   Primitive components are components that have a physical presence in the world, such as player arms or held items.

   These camera settings render those tagged components differently so they don't appear too large or stretched. Narrowing the FOV can reduce this distortion and reducing the scale prevents those objects from protruding into walls.

   For more information about controlling how first-person and third-person objects appear to the player, see the[First Person Rendering](https://dev.epicgames.com/documentation/en-us/unreal-engine/first-person-rendering) documentation.
8. Declare a new `TObjectPtr` to a `USkeletalMeshComponent` named `FirstPersonMeshComponent`. Give it a `UPROPERTY()` macro with `VisibleAnywhere` and `Category = Mesh` arguments.

   C++

   ```
   public:	
   	// Called every frame
   	virtual void Tick(float DeltaTime) override;

   	// Called to bind functionality to input
   	virtual void SetupPlayerInputComponent(class UInputComponent* PlayerInputComponent) override;

   	// Handles 2D Movement Input
   	UFUNCTION()
   	void Move(const FInputActionValue& Value);
   ```

   Expand code  Copy full snippet(38 lines long)
9. Save the file.

You’ve now set up declarations for the following:

* First-person mesh (which correlates to the child **FirstPersonMesh** you saw in the Blueprint)
* Camera component
* `Look()` function
* `IA_Look` Input Action

Your character’s `.h` file should look like this:

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

Expand code  Copy full snippet(79 lines long)

### Add Look Input with Look()

Now you can implement the Look() function so it applies the Look input action to the player camera position. Just as with `IA_Move`, `IA_Look` returns an FVector2D value when triggered.

To implement the camera input logic, follow these steps:

1. Open your Character Blueprint’s `.cpp` file.
2. Below the `Move()` function, add a new function definition for `Look()`.

   C++

   ```
   void AAdventureCharacter::Move(const FInputActionValue& Value)
   {
   	// 2D Vector of movement values returned from the input action
   	const FVector2D MovementValue = Value.Get<FVector2D>();

   	// Check if the controller possessing this Actor is valid
   	if (Controller)
   	{
   		// Add left and right movement
   		const FVector Right = GetActorRightVector();
   ```

   Expand code  Copy full snippet(27 lines long)
3. Inside the function, get the value of the `FInputActionValue` inside a new `FVector2D` named `LookAxisValue`.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | void AAdventureCharacter::Look(const FInputActionValue& Value) |
   |  | { |
   |  | // --- New Code Start --- |
   |  |  |
   |  | const FVector2D LookAxisValue = Value.Get<FVector2D>(); |
   |  |  |
   |  | // --- New Code End --- |
   |  | } |
   ```

   void AAdventureCharacter::Look(const FInputActionValue&amp; Value)
   {
   // --- New Code Start ---
   const FVector2D LookAxisValue = Value.Get&lt;FVector2D&gt;();
   // --- New Code End ---
   }

   Copy full snippet(8 lines long)
4. In an `if` statement, check if the Controller is valid.

   If it is, call `AddControllerYawInput()` and `AddControllerPitchInput()`, passing the `LookAxisValue.X` and `LookAxisValue.Y` values, respectively.

   C++

   ```
   void AAdventureCharacter::Look(const FInputActionValue& Value)
   {
   	const FVector2D LookAxisValue = Value.Get<FVector2D>();

   	// --- New Code Start --- 
   	if (Controller)
   	{
   		AddControllerYawInput(LookAxisValue.X);
   		AddControllerPitchInput(LookAxisValue.Y);
   	}
   ```

   Expand code  Copy full snippet(12 lines long)

Your complete `Look()` function should look like the following:

C++

```
|  |  |
| --- | --- |
|  | void AAdventureCharacter::Look(const FInputActionValue& Value) |
|  | { |
|  | const FVector2D LookAxisValue = Value.Get<FVector2D>(); |
|  |  |
|  | if (Controller) |
|  | { |
|  | AddControllerYawInput(LookAxisValue.X); |
|  | AddControllerPitchInput(LookAxisValue.Y); |
|  | } |
|  | } |
```

void AAdventureCharacter::Look(const FInputActionValue& Value)
{
const FVector2D LookAxisValue = Value.Get<FVector2D>();
if (Controller)
{
AddControllerYawInput(LookAxisValue.X);
AddControllerPitchInput(LookAxisValue.Y);
}
}

Copy full snippet(10 lines long)

### Bind Look Functionality to Input with SetupPlayerInputComponent

Inside `SetupPlayerInputComponent()`, similar to the movement actions, you’ll bind the `Look()` function to the `LookAction` Input Action.

C++

```
// Called to bind functionality to input
void AAdventureCharacter::SetupPlayerInputComponent(UInputComponent* PlayerInputComponent)
{

	if (UEnhancedInputComponent* EnhancedInputComponent = CastChecked<UEnhancedInputComponent>(PlayerInputComponent))
	{
		// Bind Movement Actions
		EnhancedInputComponent->BindAction(MoveAction, ETriggerEvent::Triggered, this, &AAdventureCharacter::Move);
		
		// Bind Jump Actions
```

Expand code  Copy full snippet(22 lines long)

Save your code and compile it by clicking **Build** in Visual Studio.

### Assign a Look Input Action in the Blueprint

Last, assign an Input Action to the Character Blueprint’s new **Look Action** property.

To assign look controls to your character, follow these steps:

1. In Unreal Editor, open your Character Blueprint. Click **Compile** in the main editor if the blueprint didn't update with its new properties.
2. In the **Details** panel, in the **Input** section, set **Look Action** to `IA_Look`.

   [![](https://dev.epicgames.com/community/api/documentation/image/96cc4d51-d545-4dcb-a71d-64ef60e7ad93?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/96cc4d51-d545-4dcb-a71d-64ef60e7ad93?resizing_type=fit)
3. Compile and save your Blueprint.

### Test Look Movements

If you press **Play** to test out your game, you’ll be able to look around and move your character in any direction you want!

[![](https://dev.epicgames.com/community/api/documentation/image/08d7cd36-87fb-46ba-b5fd-e40827683874?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/08d7cd36-87fb-46ba-b5fd-e40827683874?resizing_type=fit)

Note that while your in-game view appears to come from a first-person camera, you don’t actually have a camera component on your character yet. Instead, Unreal Engine simulates a view from the center of your character’s capsule component. In the next step, you’ll learn to change this by adding a camera to your Character class.

## Create Components at Runtime

Next, you’ll finish creating your character’s first-person mesh and camera by instantiating the `FirstPersonCameraComponent` and `FirstPersonMeshComponent` pointers you declared in the header file.

To get started, return to your character’s `.cpp` file.

At the top of the file, you’ll see the **class constructor** (`AAdventureCharacter()` in this tutorial). This class runs when the object is allocated in memory and it sets the default values for your character. This is where you’ll add additional components.

When adding code to the class constructor or `BeginPlay()`, consider when each is executed in the Actor's lifecycle and if other objects are initialized yet.

When the class constructor runs, other components or actors may not exist yet. `BeginPlay()` runs when when gameplay starts or when the Actor is spawned, so the Actor and all its components are fully initialized and registered, and it's safe to reference other Actors here.

Also, because of the way Unreal Engine handles timing of attachment, physics, networking, or parent-child relationships behind the scenes, some operations behave more reliably when done in `BeginPlay()`, even if they technically could be done earlier.

### Create a Camera Component

To add components to the Character class, you’ll use the `CreateDefaultSubobject()` template function. It returns a pointer to the new component and takes the following arguments:

`CreateDefaultSubobject<type>(TEXT(“Name”));`

Where *type* is the type of subobject you’re creating and *Name* is the internal name Unreal Engine uses to identify the subobject and display it in the editor.

To add a camera component to the character, follow these steps:

1. In the class constructor, set the `FirstPersonCameraComponent` pointer to the result of calling `CreateDefaultSubobject()` of type `UCameraComponent`. In the `TEXT` argument, name the object ”FirstPersonCamera”.

   C++

   ```
   // Sets default values
   AAdventureCharacter::AAdventureCharacter()
   {
    	// Set this character to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
   	PrimaryActorTick.bCanEverTick = true;

   	// --- New Code Start --- 
   	// Create a first-person camera component
   	FirstPersonCameraComponent = CreateDefaultSubobject<UCameraComponent>(TEXT("FirstPersonCamera"));
   	// --- New Code End ---
   ```

   Expand code  Copy full snippet(11 lines long)

   This creates a default camera component as a child component of the Character class.
2. To ensure the camera was properly instantiated, check that `FirstPersonCameraComponent` isn’t null.

   C++

   ```
   // Sets default values
   AAdventureCharacter::AAdventureCharacter()
   {
    	// Set this character to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
   	PrimaryActorTick.bCanEverTick = true;
    
   	// Create a first-person camera component
   	FirstPersonCameraComponent = CreateDefaultSubobject<UCameraComponent>(TEXT("FirstPersonCamera"));
   	// --- New Code Start ---
   	check(FirstPersonCameraComponent != nullptr);
   ```

   Expand code  Copy full snippet(12 lines long)

### Create a Mesh Component

Set `FirstPersonMeshComponent` to another `CreateDefaultSubobject` function call. This time, use `USkeletalMeshComponent` as the type and “FirstPersonMesh” as the name. Remember to add a `check` afterwards.

C++

```
// Sets default values
AAdventureCharacter::AAdventureCharacter()
{
 	// Set this character to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;
 
	FirstPersonCameraComponent = CreateDefaultSubobject<UCameraComponent>(TEXT("FirstPersonCamera"));
	check(FirstPersonCameraComponent != nullptr);

	// --- New Code Start ---
```

Expand code  Copy full snippet(17 lines long)

### Attach and Configure the Mesh

Now that your mesh is created, attach it to the character and enable first-person rendering on it.

In these steps, you'll use the `SetupAttachment()` function, which attaches one scene component to another, establishing a parent-child relationship in the component hierarchy.

To set up the player mesh, follow these steps:

1. In the class constructor, call the `SetupAttachment()` function on the object that `FirstPersonMeshComponent` points to and pass it the parent component. In this case, the parent should be the character’s default skeletal mesh, which you can get using `GetMesh()`.

   C++

   ```
   // Sets default values
   AAdventureCharacter::AAdventureCharacter()
   {
    	// Set this character to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
   	PrimaryActorTick.bCanEverTick = true;
    
   	FirstPersonCameraComponent = CreateDefaultSubobject<UCameraComponent>(TEXT("FirstPersonCamera"));
   	check(FirstPersonCameraComponent != nullptr);
   	
   	// Create a first person mesh component for the owning player.
   ```

   Expand code  Copy full snippet(20 lines long)
2. In the character's header file, you declared a camera field of view and scale to use for components close to the camera. To make these camera properties apply to the first-person mesh, set the mesh's `FirstPersonPrimitiveType` property to `FirstPerson`.

   C++

   ```
   // Sets default values
   AAdventureCharacter::AAdventureCharacter()
   {
    	// Set this character to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
   	PrimaryActorTick.bCanEverTick = true;
    
   	FirstPersonCameraComponent = CreateDefaultSubobject<UCameraComponent>(TEXT("FirstPersonCamera"));
   	check(FirstPersonCameraComponent != nullptr);
   	
   	// Create a first person mesh component for the owning player.
   ```

   Expand code  Copy full snippet(23 lines long)

   `FirstPerson`-type primitives are rendered in a separate render pass, often with different camera parameters, so they don't cast a shadow. Player shadows perform best when cast from the third-person mesh, and you'll set this up next.
3. Set the first-person mesh collision profile name to `NoCollision` to prevent the first-person mesh from colliding with the environment.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Set the first person mesh to not collide with other objects |
   |  | FirstPersonMeshComponent->SetCollisionProfileName(FName("NoCollision")); |
   ```

   // Set the first person mesh to not collide with other objects
   FirstPersonMeshComponent-&gt;SetCollisionProfileName(FName(&quot;NoCollision&quot;));

   Copy full snippet(2 lines long)

   The first-person mesh should only provide camera-space visuals for the owning player. The Character Blueprint's Capsule Component provides a simpler collision shape.
4. Your first-person camera settings shouldn't apply to the third-person mesh, so set the third-person mesh component's `FirstPersonPrimitiveType` to `WorldSpaceRepresentation`.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Treat the 3rd-person mesh as a regular world object |
   |  | GetMesh()->FirstPersonPrimitiveType = EFirstPersonPrimitiveType::WorldSpaceRepresentation; |
   ```

   // Treat the 3rd-person mesh as a regular world object
   GetMesh()-&gt;FirstPersonPrimitiveType = EFirstPersonPrimitiveType::WorldSpaceRepresentation;

   Copy full snippet(2 lines long)

   This primitive type tells the first-person rendering pass to treat the third-person mesh as normal world geometry. The mesh uses the standard world FOV and world-space rendering rules even when hidden from the owning player.

### Set Mesh and Shadow Visibility

So far, your character has a first and third-person skeletal mesh that overlap during gameplay. However, the first-person mesh should be invisible to other players and the third-person mesh should be invisible to you, the player.

To configure first-person and third-person mesh visibility, follow these steps:

1. In `BeginPlay()`, after the global engine pointer check, call `SetOnlyOwnerSee()` on `FirstPersonMeshComponent`, passing `true` to make the first-person mesh visible only to the owning player.

   C++

   ```
   // Called when the game starts or when spawned
   void AAdventureCharacter::BeginPlay()
   {
   	Super::BeginPlay();

   	check(GEngine != nullptr);

   	// --- New Code Start ---

   	// Only the owning player sees the first-person mesh
   ```

   Expand code  Copy full snippet(27 lines long)
2. For the third-person mesh, use `SetOwnerNoSee()` to hide the mesh from the owning player.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Hide the 3rd-person mesh from the owning player |
   |  | GetMesh()->SetOwnerNoSee(true); |
   ```

   // Hide the 3rd-person mesh from the owning player
   GetMesh()-&gt;SetOwnerNoSee(true);

   Copy full snippet(2 lines long)
3. You've set up the character's first-person mesh as a first-person primitive, which is rendered in the camera-space first-person rendering pass and therefore doesn't contribute to world shadows.

   To give the character a shadow, enable the `CastShadow` and `bCastHiddenShadow` properties on the third-person mesh, since that mesh is a regular world object and participates in world shadow rendering.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Make the 3rd-person mesh cast a shadow |
   |  | GetMesh()->CastShadow = true; |
   |  | GetMesh()->bCastHiddenShadow = true; |
   ```

   // Make the 3rd-person mesh cast a shadow
   GetMesh()-&gt;CastShadow = true;
   GetMesh()-&gt;bCastHiddenShadow = true;

   Copy full snippet(3 lines long)

In general, initialization belongs in the constructor, but these actions work more reliably in `BeginPlay()`.

### Attach the Camera Component

The `SKM_Manny_Simple` skeletal mesh used in this tutorial has a collection of preset **sockets** (or bones) used for animation. To attach components to the character mesh, you'll use a socket as an attachment point. 
Each socket has a name, so you can reference sockets in code using an `FName` string.

`FName` is a special string-like type used in Unreal Engine to store unique, immutable names in a memory-efficient way.

It’s best to position the camera near the character’s head, so you’ll pass the `Head` socket name to `SetupAttachment()` to attach the camera to that socket. You’ll move the camera closer to the character’s eyes next.

In the character's constructor, use another `SetupAttachment()` call to attach the camera component to the first-person mesh.

C++

```
// Sets default values
AAdventureCharacter::AAdventureCharacter()
{
 	// Set this character to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;
 
	FirstPersonCameraComponent = CreateDefaultSubobject<UCameraComponent>(TEXT("FirstPersonCamera"));
	check(FirstPersonCameraComponent != nullptr);
	
	// Create a first person mesh component for the owning player.
```

Expand code  Copy full snippet(27 lines long)

For more information about what sockets are and how they’re created, see [Skeletal Mesh Sockets](https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-sockets-in-unreal-engine).

### Configure the Camera

When you initialized your camera component, you attached it to the character’s Head socket. However, the camera looks more accurate when it’s positioned at the character’s eyes. The camera is also pointing down by default, so you'll need to rotate it behind the character's head.

To finish setting up the player camera, follow these steps:

1. To move and rotate the camera into position, after the camera's `SetupAttachment` line in the class constructor, call `SetRelativeLocationAndRotation()`, passing the `FirstPersonCameraOffset` and a new `FRotator` set to `(0.0f, 90.0f, -90.0f)`.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Attach the camera component to the first-person Skeletal Mesh. |
   |  | FirstPersonCameraComponent->SetupAttachment(FirstPersonMeshComponent, FName("head")); |
   |  |  |
   |  | // --- New Code Start --- |
   |  | // Position the camera slightly above the eyes and rotate it to behind the player's head |
   |  | FirstPersonCameraComponent->SetRelativeLocationAndRotation(FirstPersonCameraOffset, FRotator(0.0f, 90.0f, -90.0f)); |
   |  | // --- New Code End --- |
   ```

    // Attach the camera component to the first-person Skeletal Mesh.
   FirstPersonCameraComponent-&gt;SetupAttachment(FirstPersonMeshComponent, FName(&quot;head&quot;));
   // --- New Code Start ---
   // Position the camera slightly above the eyes and rotate it to behind the player&#39;s head
   FirstPersonCameraComponent-&gt;SetRelativeLocationAndRotation(FirstPersonCameraOffset, FRotator(0.0f, 90.0f, -90.0f));
   // --- New Code End --- 

   Copy full snippet(7 lines long)
2. To make the camera rotate with the character during gameplay, set `FirstPersonCameraComponent`'s `bUsePawnControlRotation` property to `true`. This makes the camera inherit rotation from its parent Pawn so when the character turns, the camera follows.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Enable the pawn to control camera rotation. |
   |  | FirstPersonCameraComponent->bUsePawnControlRotation = true; |
   ```

   // Enable the pawn to control camera rotation.
   FirstPersonCameraComponent-&gt;bUsePawnControlRotation = true;

   Copy full snippet(2 lines long)
3. Apply your First Person Field of View and First Person Scale rendering values to the camera component's corresponding settings.

   Set the component's  `bEnableFirstPersonFieldOfView` and `bEnableFirstPersonScale` properties to `true`. Then, assign the default FOV and scale values you declared earlier.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Enable first-person rendering and set default FOV and scale values |
   |  | FirstPersonCameraComponent->bEnableFirstPersonFieldOfView = true; |
   |  | FirstPersonCameraComponent->bEnableFirstPersonScale = true; |
   |  | FirstPersonCameraComponent->FirstPersonFieldOfView = FirstPersonFieldOfView; |
   |  | FirstPersonCameraComponent->FirstPersonScale = FirstPersonScale; |
   ```

   // Enable first-person rendering and set default FOV and scale values
   FirstPersonCameraComponent-&gt;bEnableFirstPersonFieldOfView = true;
   FirstPersonCameraComponent-&gt;bEnableFirstPersonScale = true;
   FirstPersonCameraComponent-&gt;FirstPersonFieldOfView = FirstPersonFieldOfView;
   FirstPersonCameraComponent-&gt;FirstPersonScale = FirstPersonScale;

   Copy full snippet(5 lines long)
4. Save and compile your code.

Your character’s constructor should look like the following:

C++

```
// Sets default values
AAdventureCharacter::AAdventureCharacter()
{
	// Set this character to call Tick() every frame.  You can turn this off to improve performance if you don't need it
	PrimaryActorTick.bCanEverTick = true;

	// Create a first person camera component
	FirstPersonCameraComponent = CreateDefaultSubobject<UCameraComponent>(TEXT("FirstPersonCamera"));
	check(FirstPersonCameraComponent != nullptr);
```

Expand code  Copy full snippet(38 lines long)

## Assign Meshes in Unreal Editor

Your camera controls are set up, but you still have one step left — use the editor to add the Skeletal Mesh assets to the variables you declared in code.

To add a Skeletal Mesh to a Character Blueprint, follow these steps:

1. In Unreal Editor, if it’s not open already, open your Character Blueprint.

   You may need to click **Compile** in Unreal Editor to update the Character Blueprint with your new code changes.
2. So far, Unreal Engine has likely categorized your Blueprint as a Data-Only Blueprint Class and only displays a list of properties in the Blueprint Editor. To convert the asset to a regular Blueprint Class, click the **Open Full Blueprint Editor** link in the **NOTE** above the list of properties.

   [![](https://dev.epicgames.com/community/api/documentation/image/4e7b986f-9170-4fb3-a8b9-cd72347d20ce?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4e7b986f-9170-4fb3-a8b9-cd72347d20ce?resizing_type=fit)
3. Click the **Viewport** tab so you can see a preview of the character and its components.
4. In the **Components** panel, ensure the root **BP\_*[CharacterName]*** is selected.
5. In the Blueprint Editor, click **Compile** to make your character's new components appear in the **Components** panel.

   [![](https://dev.epicgames.com/community/api/documentation/image/1c81a7b2-8267-4346-b4e0-dc38604cf39a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1c81a7b2-8267-4346-b4e0-dc38604cf39a?resizing_type=fit)
6. In the **Details** panel, in the **Mesh** section, your character has two **Skeletal Mesh Asset** slots instead of one because you created `FirstPersonMeshComponent` in code. Click the arrow in each property’s dropdown menu and select `SKM_Manny_Simple` for both meshes.

   [![](https://dev.epicgames.com/community/api/documentation/image/6c5113a8-b280-4fe1-8fbc-f29972de6a3f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6c5113a8-b280-4fe1-8fbc-f29972de6a3f?resizing_type=fit)

   When you set the **FirstPersonMeshComponent**, your camera should move into position behind the character’s head.
7. As a final adjustment, use the Blueprint Editor to transform the character's mesh so it's inside the Capsule Component and facing the same direction as the Arrow Component:

   1. In the **Components** panel, select the root.
   2. In the **Details** panel, In the **Transform > Mesh** section, change the **Rotation**'s **Z** value to `-90`.
   3. Change the **Location**'s Z value to `-95`.

   [![](https://dev.epicgames.com/community/api/documentation/image/50a75665-c900-4851-ab45-0bdab8f6bc10?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/50a75665-c900-4851-ab45-0bdab8f6bc10?resizing_type=fit)

   * Final mesh alignment is best done in the editor rather than code for faster iteration and easier visual alignment.
   * The Arrow Component indicates the actor's forward direction in the editor.
8. Save your Blueprint and click **Compile**.

If you play your game and look down, you should see the first-person mesh on your character! The mesh rotates as you look around, and your camera matches that movement. The third-person mesh is hidden at runtime and only other players can see it.

However, your character is still in a static T-pose, so next you'll use an Animation Blueprint to add animations to your character and finish bringing it to life!

## Add Animations to Your Character

In code, you can access animation logic through instances of the **UAnimInstance** class, which is a controller that determines what animations are blended and played on a Skeletal Mesh based on state and other variables. Animation Blueprints also derive from `UAnimInstance`, and you can reference them in C++ with the `UAnimBlueprint` type.

Building an Anim Instance class is outside the scope of this tutorial; instead, you’ll add the First Person template’s prebuilt Animation Blueprint to your character. This Blueprint includes the animations and logic your character needs to play different movement and idle animations.

Animations in Unreal Engine are set on a per-mesh basis, so you’ll need separate animations for both your first and third-person meshes. Because your third-person mesh is hidden when the game begins, you only need to set animations on the first-person mesh.

To add an animation property and Animation Blueprint to your character, follow these steps:

1. At the top of your character's `.h` file, forward-declare the `UAnimBlueprint` class. This class represents the Animation Blueprints in your project.

   C++

   ```
   #include "CoreMinimal.h"
   #include "Camera/CameraComponent.h"
   #include "GameFramework/Character.h"
   #include "EnhancedInputComponent.h"
   #include "EnhancedInputSubsystems.h" 
   #include "InputActionValue.h"
   #include "AdventureCharacter.generated.h"

   // --- New Code Start --- 
   class UAnimBlueprint;
   ```

   Expand code  Copy full snippet(14 lines long)
2. In the `public` section, declare a `TObjectPtr` to a `UAnimBlueprint` named `FirstPersonDefaultAnim`. Give it the `UCLASS()` macro with `EditAnywhere` and `Category = Animation`.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | public: |
   |  | // Sets default values for this character's properties |
   |  | AAdventureCharacter(); |
   |  |  |
   |  | // --- New Code Start --- |
   |  | // First Person animations |
   |  | UPROPERTY(EditAnywhere, Category = Animation) |
   |  | TObjectPtr<UAnimBlueprint> FirstPersonDefaultAnim; |
   |  | // --- New Code End --- |
   ```

   public:
   // Sets default values for this character&#39;s properties
   AAdventureCharacter();
   // --- New Code Start ---
   // First Person animations
   UPROPERTY(EditAnywhere, Category = Animation)
   TObjectPtr&lt;UAnimBlueprint&gt; FirstPersonDefaultAnim;
   // --- New Code End --- 

   Copy full snippet(9 lines long)
3. In your character's `.cpp` file, in `BeginPlay()` after the `check` line, call `FirstPersonMeshComponent->SetAnimInstanceClass()`. Even though you haven’t defined an Anim Instance class in code, you can generate a class from the Animation Blueprint using `GeneratedClass`.

   C++

   ```
   // Called when the game starts or when spawned
   void AAdventureCharacter::BeginPlay()
   {
   	Super::BeginPlay();

   	check(GEngine != nullptr);

   	// --- New Code Start --- 
   	// Set the animations on the first person mesh.
   	FirstPersonMeshComponent->SetAnimInstanceClass(FirstPersonDefaultAnim->GeneratedClass);
   ```

   Expand code  Copy full snippet(11 lines long)
4. On the next line, call `SetAnimInstanceClass()` again to assign the AnimInstance to the third-person mesh so if you create a multi-player game, other players will see your character animating.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Set the animations on the first person mesh. |
   |  | FirstPersonMeshComponent->SetAnimInstanceClass(FirstPersonDefaultAnim->GeneratedClass); |
   |  |  |
   |  | // --- New Code Start --- |
   |  | // Set the animations on the third-person mesh. |
   |  | GetMesh()->SetAnimInstanceClass(FirstPersonDefaultAnim->GeneratedClass); |
   |  | // --- New Code End --- |
   ```

    // Set the animations on the first person mesh.
   FirstPersonMeshComponent-&gt;SetAnimInstanceClass(FirstPersonDefaultAnim-&gt;GeneratedClass);
   // --- New Code Start ---
   // Set the animations on the third-person mesh.
   GetMesh()-&gt;SetAnimInstanceClass(FirstPersonDefaultAnim-&gt;GeneratedClass);
   // --- New Code End ---

   Copy full snippet(7 lines long)
5. Save your code and compile it from Visual Studio.
6. In Unreal Editor, return to your Character Blueprint, compile it, and select the root **BP\_*[CharacterName]***component.
7. In the **Details** panel, under **Animation**, set the **First Person Default Anim** to `ABP_Unarmed`.

   [![](https://dev.epicgames.com/community/api/documentation/image/9efb584b-d6c4-4bf8-b759-6d64804bff27?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9efb584b-d6c4-4bf8-b759-6d64804bff27?resizing_type=fit)
8. Save your Blueprint and compile it.

## Test Your Character

Press **Play** to test out your game. If you look down, you'll see the first-person mesh animate as you move! Try moving around and jumping to see the different animations controlled by this Blueprint.

[![](https://dev.epicgames.com/community/api/documentation/image/1aa18e06-e960-4c7d-92eb-8a9a34635932?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1aa18e06-e960-4c7d-92eb-8a9a34635932?resizing_type=fit)

## Next Up

In the next section, you’ll learn how to create an item for your character to pick up and use!

* [![Manage Items and Data](https://dev.epicgames.com/community/api/documentation/image/1db9f4bd-93e0-4ad8-8abf-c7be6ecec5e8?resizing_type=fit&width=640&height=640)

  Manage Items and Data

  Learn to use Item Data Structs, Data Assets, and Data Tables to define items and store and organize item data for scalability.](https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-05-manage-item-and-data-in-an-unreal-engine-game)

## Complete Code

Here is the complete code built in this section:

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

Expand code  Copy full snippet(85 lines long)

C++

AdventureCharacter.cpp

```
// Copyright Epic Games, Inc. All Rights Reserved.


#include "AdventureCharacter.h"

// Sets default values
AAdventureCharacter::AAdventureCharacter()
{
	// Set this character to call Tick() every frame.  You can turn this off to improve performance if you don't need it
	PrimaryActorTick.bCanEverTick = true;
```

Expand code  Copy full snippet(143 lines long)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Before You Start](/documentation/en-us/unreal-engine/coder-04-adding-a-firstperson-camera-mesh-and-animation?application_version=5.7#beforeyoustart)
* [First-Person Camera Controls](/documentation/en-us/unreal-engine/coder-04-adding-a-firstperson-camera-mesh-and-animation?application_version=5.7#first-personcameracontrols)
* [Explore Camera Movement in Blueprints](/documentation/en-us/unreal-engine/coder-04-adding-a-firstperson-camera-mesh-and-animation?application_version=5.7#explorecameramovementinblueprints)
* [Explore First-Person Character Components](/documentation/en-us/unreal-engine/coder-04-adding-a-firstperson-camera-mesh-and-animation?application_version=5.7#explorefirst-personcharactercomponents)
* [Implement Look Input in Code](/documentation/en-us/unreal-engine/coder-04-adding-a-firstperson-camera-mesh-and-animation?application_version=5.7#implementlookinputincode)
* [Declare the Look() Function and Variables](/documentation/en-us/unreal-engine/coder-04-adding-a-firstperson-camera-mesh-and-animation?application_version=5.7#declarethelook()functionandvariables)
* [Add Look Input with Look()](/documentation/en-us/unreal-engine/coder-04-adding-a-firstperson-camera-mesh-and-animation?application_version=5.7#addlookinputwithlook())
* [Bind Look Functionality to Input with SetupPlayerInputComponent](/documentation/en-us/unreal-engine/coder-04-adding-a-firstperson-camera-mesh-and-animation?application_version=5.7#bindlookfunctionalitytoinputwithsetupplayerinputcomponent)
* [Assign a Look Input Action in the Blueprint](/documentation/en-us/unreal-engine/coder-04-adding-a-firstperson-camera-mesh-and-animation?application_version=5.7#assignalookinputactionintheblueprint)
* [Test Look Movements](/documentation/en-us/unreal-engine/coder-04-adding-a-firstperson-camera-mesh-and-animation?application_version=5.7#testlookmovements)
* [Create Components at Runtime](/documentation/en-us/unreal-engine/coder-04-adding-a-firstperson-camera-mesh-and-animation?application_version=5.7#createcomponentsatruntime)
* [Create a Camera Component](/documentation/en-us/unreal-engine/coder-04-adding-a-firstperson-camera-mesh-and-animation?application_version=5.7#createacameracomponent)
* [Create a Mesh Component](/documentation/en-us/unreal-engine/coder-04-adding-a-firstperson-camera-mesh-and-animation?application_version=5.7#createameshcomponent)
* [Attach and Configure the Mesh](/documentation/en-us/unreal-engine/coder-04-adding-a-firstperson-camera-mesh-and-animation?application_version=5.7#attachandconfigurethemesh)
* [Set Mesh and Shadow Visibility](/documentation/en-us/unreal-engine/coder-04-adding-a-firstperson-camera-mesh-and-animation?application_version=5.7#setmeshandshadowvisibility)
* [Attach the Camera Component](/documentation/en-us/unreal-engine/coder-04-adding-a-firstperson-camera-mesh-and-animation?application_version=5.7#attachthecameracomponent)
* [Configure the Camera](/documentation/en-us/unreal-engine/coder-04-adding-a-firstperson-camera-mesh-and-animation?application_version=5.7#configurethecamera)
* [Assign Meshes in Unreal Editor](/documentation/en-us/unreal-engine/coder-04-adding-a-firstperson-camera-mesh-and-animation?application_version=5.7#assignmeshesinunrealeditor)
* [Add Animations to Your Character](/documentation/en-us/unreal-engine/coder-04-adding-a-firstperson-camera-mesh-and-animation?application_version=5.7#addanimationstoyourcharacter)
* [Test Your Character](/documentation/en-us/unreal-engine/coder-04-adding-a-firstperson-camera-mesh-and-animation?application_version=5.7#testyourcharacter)
* [Next Up](/documentation/en-us/unreal-engine/coder-04-adding-a-firstperson-camera-mesh-and-animation?application_version=5.7#nextup)
* [Complete Code](/documentation/en-us/unreal-engine/coder-04-adding-a-firstperson-camera-mesh-and-animation?application_version=5.7#completecode)

Related documents

[Code a First-Person Adventure Game

![Code a First-Person Adventure Game](https://dev.epicgames.com/community/api/documentation/image/ffc1a8f8-e7e5-42c0-b4ed-32ce6d3adbbc?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/code-a-firstperson-adventure-game-in-unreal-engine)

[Create a Player Character With Input Actions

![Create a Player Character With Input Actions](https://dev.epicgames.com/community/api/documentation/image/b7155dfc-b014-4288-ae6d-d4620dc7420d?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/coder-02-create-a-player-character-with-input-actions-in-cplusplus)

[Configure Character Movement

![Configure Character Movement](https://dev.epicgames.com/community/api/documentation/image/63cf4ce2-6faa-4f79-a8d2-f476a7a6adf2?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/coder-03-configure-character-movement-with-cplusplus-in-unreal-engine)

[Manage Items and Data

![Manage Items and Data](https://dev.epicgames.com/community/api/documentation/image/1db9f4bd-93e0-4ad8-8abf-c7be6ecec5e8?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/coder-05-manage-item-and-data-in-an-unreal-engine-game)
