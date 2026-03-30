<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-08-implement-a-projectile-in-unreal-engine?application_version=5.7 -->

# Implement a Projectile

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
8. Implement a Projectile

# Implement a Projectile

Learn to use C++ to implement projectiles and spawn them during gameplay.

On this page

## Before You Begin

Ensure you’ve completed the following objectives in the previous section, [Equip Your Character](https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-07-equip-your-character-with-cplusplus-tools):

* Created a respawning pickup item and added it to your level
* Created an equippable dart launcher for your character to hold and use

## Basic Projectiles

Your character can hold your dart launcher, and your tool has control bindings to use it, but it’s not quite living up to its name. In this section, you’ll implement projectile logic to make darts launch out from the equipped item.

Unreal Engine has a **Projectile Movement** component class that you can add to an actor to turn it into a projectile. It includes many helpful variables, such as projectile speed, bounciness, and gravity scale.

To handle the math of implementing projectiles, you’ll need to think about several things:

* The initial transform, velocity, and direction of the projectile.
* Whether you want to spawn projectiles from the center of the character or the tool they have equipped.
* What behavior you want the projectile to exhibit when it collides with another object.

## Create a Projectile Base Class

You’ll first create a base projectile class, and then subclass from it to create unique projectiles for your tools.

To start setting up a base projectile class, follow these steps:

1. In the Unreal Editor, go to **Tools > New C++ Class**. Select **Actor** as the parent class and name the class `FirstPersonProjectile`. Click **Create Class**.
2. In VS, go to `FirstPersonProjectile.h`. At the top of the file, forward declare both a `UProjectileMovementComponent` and a `USphereComponent`.

   You’ll use a simple sphere component to simulate collisions between the projectile and other objects.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Copyright Epic Games, Inc. All Rights Reserved. |
   |  |  |
   |  | #pragma once |
   |  |  |
   |  | #include "CoreMinimal.h" |
   |  | #include "GameFramework/Actor.h" |
   |  | #include "FirstPersonProjectile.generated.h" |
   |  |  |
   |  | class UProjectileMovementComponent; |
   |  | class USphereComponent; |
   ```

   // Copyright Epic Games, Inc. All Rights Reserved.
   #pragma once
   #include &quot;CoreMinimal.h&quot;
   #include &quot;GameFramework/Actor.h&quot;
   #include &quot;FirstPersonProjectile.generated.h&quot;
   class UProjectileMovementComponent;
   class USphereComponent;

   Copy full snippet(10 lines long)
3. Add the `BlueprintType` and `Blueprintable` specifiers to expose this class to Blueprints:

   C++

   ```
   |  |  |
   | --- | --- |
   |  | UCLASS(BlueprintType, Blueprintable) |
   |  | class FIRSTPERSON_API AFirstPersonProjectile : public AActor |
   ```

   UCLASS(BlueprintType, Blueprintable)
   class FIRSTPERSON\_API AFirstPersonProjectile : public AActor

   Copy full snippet(2 lines long)
4. Open `FirstPersonProjectile.cpp`, at the top of the file, add an include statement for `"GameFramework/ProjectileMovementComponent.h"` and `"Components/SphereComponent.h"` to include the projectile movement and collision component classes.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | #include "FirstPersonProjectile.h" |
   |  | #include "GameFramework/ProjectileMovementComponent.h" |
   |  | #include "Components/SphereComponent.h" |
   |  |  |
   |  | // Sets default values |
   |  | AFirstPersonProjectile::AFirstPersonProjectile() |
   ```

   #include &quot;FirstPersonProjectile.h&quot;
   #include &quot;GameFramework/ProjectileMovementComponent.h&quot;
   #include &quot;Components/SphereComponent.h&quot;
   // Sets default values
   AFirstPersonProjectile::AFirstPersonProjectile()

   Copy full snippet(6 lines long)

### Implement Projectile Behavior When Hitting Objects

To make your projectile more realistic, you can make it exert some force (an impulse) on objects it hits. For example, if you are shooting at a physics-enabled block, the projectile would nudge the block along the ground. Then, remove the projectile after impact instead of letting it live out its default lifespan. Create an `OnHit()` function to implement this behavior.

To implement projectile on-hit behavior, follow these steps:

1. In `FirstPersonProjectile.h`, in the `public` section, define a `float` property named `PhysicsForce`.

   Give it a `UPROPERTY()` macro with `EditAnywhere`, `BlueprintReadOnly`, and `Category = “Projectile | Physics”`.

   This is the amount of force the projectile imparts when it hits something.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // The amount of force this projectile imparts on objects it collides with |
   |  | UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "Projectile | Physics") |
   |  | float PhysicsForce = 100.0f; |
   ```

   // The amount of force this projectile imparts on objects it collides with
   UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = &quot;Projectile | Physics&quot;)
   float PhysicsForce = 100.0f;

   Copy full snippet(3 lines long)
2. Define a `void` function `OnHit()`. This is a function from AActor that's called when the actor collides with another component or actor. It takes the following arguments:

   * `HitComp`: The component that was hit.
   * `OtherActor`: The actor that was hit.
   * `OtherComp`: The component that created the hit (in this case, the projectile’s CollisionComponent).
   * `NormalImpulse`: The normal impulse of the hit.
   * `Hit`: A `FHitResult` reference that contains more data about the hit event such as time, distance, and location.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Called when the projectile collides with an object |
   |  | UFUNCTION() |
   |  | void OnHit(UPrimitiveComponent* HitComp, AActor* OtherActor, UPrimitiveComponent* OtherComp, FVector NormalImpulse, const FHitResult& Hit); |
   ```

   // Called when the projectile collides with an object
   UFUNCTION()
   void OnHit(UPrimitiveComponent\* HitComp, AActor\* OtherActor, UPrimitiveComponent\* OtherComp, FVector NormalImpulse, const FHitResult&amp; Hit);

   Copy full snippet(3 lines long)
3. In `FirstPersonProjectile.cpp`, implement the `OnHit()` function you defined in your header file. Inside `OnHit()`, in an `if` statement, check that:

   1. `OtherActor` isn't null and isn't the projectile itself.
   2. `OtherComp` isn't null and is also simulating physics.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | void AFirstPersonProjectile::OnHit(UPrimitiveComponent* HitComp, AActor* OtherActor, UPrimitiveComponent* OtherComp, FVector NormalImpulse, const FHitResult& Hit) |
   |  | { |
   |  | // Only add impulse and destroy projectile if we hit a physics object |
   |  | if ((OtherActor != nullptr) && (OtherActor != this) && (OtherComp != nullptr) && OtherComp->IsSimulatingPhysics()) |
   |  | { |
   |  | } |
   |  | } |
   ```

   void AFirstPersonProjectile::OnHit(UPrimitiveComponent\* HitComp, AActor\* OtherActor, UPrimitiveComponent\* OtherComp, FVector NormalImpulse, const FHitResult&amp; Hit)
   {
   // Only add impulse and destroy projectile if we hit a physics object
   if ((OtherActor != nullptr) &amp;&amp; (OtherActor != this) &amp;&amp; (OtherComp != nullptr) &amp;&amp; OtherComp-&gt;IsSimulatingPhysics())
   {
   }
   }

   Copy full snippet(7 lines long)

   This checks that the projectile hit an object that wasn’t itself and participates in physics.
4. Inside the `if` statement, use `AddImpulseAtLocation()` to add an impulse to the `OtherComp` component.

   Pass this function the velocity of the projectile multiplied by the `PhysicsForce` and apply it at the location of the projectile actor.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | void AFirstPersonProjectile::OnHit(UPrimitiveComponent* HitComp, AActor* OtherActor, UPrimitiveComponent* OtherComp, FVector NormalImpulse, const FHitResult& Hit) |
   |  | { |
   |  | // Only add impulse and destroy projectile if we hit a physics object |
   |  | if ((OtherActor != nullptr) && (OtherActor != this) && (OtherComp != nullptr) && OtherComp->IsSimulatingPhysics()) |
   |  | { |
   |  | // --- New Code Start --- |
   |  | OtherComp->AddImpulseAtLocation(GetVelocity() * PhysicsForce, GetActorLocation()); |
   |  | // --- New Code End --- |
   |  | } |
   |  | } |
   ```

   void AFirstPersonProjectile::OnHit(UPrimitiveComponent\* HitComp, AActor\* OtherActor, UPrimitiveComponent\* OtherComp, FVector NormalImpulse, const FHitResult&amp; Hit)
   {
   // Only add impulse and destroy projectile if we hit a physics object
   if ((OtherActor != nullptr) &amp;&amp; (OtherActor != this) &amp;&amp; (OtherComp != nullptr) &amp;&amp; OtherComp-&gt;IsSimulatingPhysics())
   {
   // --- New Code Start ---
   OtherComp-&gt;AddImpulseAtLocation(GetVelocity() \* PhysicsForce, GetActorLocation());
   // --- New Code End ---
   }
   }

   Copy full snippet(10 lines long)

   `AddImpulseAtLocation()` is a physics function in Unreal Engine that applies an instantaneous force (impulse) to a simulated physics object at a specific world-space location. It’s useful when you want to simulate an impact, like an explosion throwing something, a bullet hitting an object, or a door swinging open.
5. Since this projectile hit another actor, remove the projectile from the scene by calling `Destroy()`.

Your complete `OnHit()` function should look like the following:

C++

```
|  |  |
| --- | --- |
|  | void AFirstPersonProjectile::OnHit(UPrimitiveComponent* HitComp, AActor* OtherActor, UPrimitiveComponent* OtherComp, FVector NormalImpulse, const FHitResult& Hit) |
|  | { |
|  | // Only add impulse and destroy projectile if we hit a physics |
|  | if ((OtherActor != nullptr) && (OtherActor != this) && (OtherComp != nullptr) && OtherComp->IsSimulatingPhysics()) |
|  | { |
|  | OtherComp->AddImpulseAtLocation(GetVelocity() * PhysicsForce, GetActorLocation()); |
|  |  |
|  | Destroy(); |
|  | } |
|  | } |
```

void AFirstPersonProjectile::OnHit(UPrimitiveComponent\* HitComp, AActor\* OtherActor, UPrimitiveComponent\* OtherComp, FVector NormalImpulse, const FHitResult& Hit)
{
// Only add impulse and destroy projectile if we hit a physics
if ((OtherActor != nullptr) && (OtherActor != this) && (OtherComp != nullptr) && OtherComp->IsSimulatingPhysics())
{
OtherComp->AddImpulseAtLocation(GetVelocity() \* PhysicsForce, GetActorLocation());
Destroy();
}
}

Copy full snippet(10 lines long)

### Add the Projectile’s Mesh, Movement, Collision Components

Next, add a static mesh, projectile movement logic, and a collision sphere to your projectile and define how the projectile should move.

To add these components to your projectile, follow these steps:

1. In `FirstPersonProjectile.h`, in the
   `public` section, declare a `TObjectPtr` to a `UStaticMeshComponent` named
   `ProjectileMesh`. This is the static mesh of the projectile in the world.

   Give it a `UPROPERTY()` macro with `EditAnywhere`, `BlueprintReadOnly`, and `Category = “Projectile | Mesh“`.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Mesh of the projectile in the world |
   |  | UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "Projectile | Mesh") |
   |  | TObjectPtr<UStaticMeshComponent> ProjectileMesh; |
   ```

   // Mesh of the projectile in the world
   UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = &quot;Projectile | Mesh&quot;)
   TObjectPtr&lt;UStaticMeshComponent&gt; ProjectileMesh;

   Copy full snippet(3 lines long)
2. In the `protected` section, declare:

   * A `TObjectPtr` to a `USphereComponent` named `CollisionComponent`.
   * A `TObjectPtr` to a `UProjectileMovementComponent` named `ProjectileMovement`.

   Give both of these a `UPROPERTY()` macro with `VisibleAnywhere`, `BlueprintReadOnly`, and `Category = “Projectile | Components”`.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Sphere collision component |
   |  | UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Projectile | Components") |
   |  | TObjectPtr<USphereComponent> CollisionComponent; |
   |  |  |
   |  | // Projectile movement component |
   |  | UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Projectile | Components") |
   |  | TObjectPtr<UProjectileMovementComponent> ProjectileMovement; |
   ```

   // Sphere collision component
   UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = &quot;Projectile | Components&quot;)
   TObjectPtr&lt;USphereComponent&gt; CollisionComponent;
   // Projectile movement component
   UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = &quot;Projectile | Components&quot;)
   TObjectPtr&lt;UProjectileMovementComponent&gt; ProjectileMovement;

   Copy full snippet(7 lines long)

   The `ProjectileMovementComponent` handles movement logic for you. It calculates where its parent Actor should go based on velocity, gravity, and other variables. Then, during `tick`, it applies the movement to the projectile.
3. In `FirstPersonProjectile.cpp`, in the `AFirstPersonProjectile()` constructor function, create default subobjects for the projectile’s mesh, collision, and projectile movement components. Then, attach the projectile mesh to the collision component.

   C++

   ```
   // Sets default values
   AFirstPersonProjectile::AFirstPersonProjectile()
   {
    	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
   	PrimaryActorTick.bCanEverTick = true;

   	// --- New Code Start ---
   	// Use a simple sphere as the collision representation
   	CollisionComponent = CreateDefaultSubobject<USphereComponent>(TEXT("CollisionComponent"));
   	check(CollisionComponent != nullptr);
   ```

   Expand code  Copy full snippet(23 lines long)
4. Call `InitSphereRadius()` to initialize the `CollisionComponent` size.

   C++

   ```
   // Sets default values
   AFirstPersonProjectile::AFirstPersonProjectile()
   {
    	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
   	PrimaryActorTick.bCanEverTick = true;

   	// Use a simple sphere as the collision representation
   	CollisionComponent = CreateDefaultSubobject<USphereComponent>(TEXT("CollisionComponent"));
   	check(CollisionComponent != nullptr);
   ```

   Expand code  Copy full snippet(25 lines long)
5. Set the name of the collision component’s collision profile to `”Projectile”` using `BodyInstance.SetCollisionProfileName()`.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | CollisionComponent->InitSphereRadius(5.0f); |
   |  |  |
   |  | // --- New Code Start --- |
   |  | // Set the collision profile to the "Projectile" collision preset |
   |  | CollisionComponent->BodyInstance.SetCollisionProfileName("Projectile"); |
   |  | // --- New Code End --- |
   ```

    CollisionComponent-&gt;InitSphereRadius(5.0f);
   // --- New Code Start ---
   // Set the collision profile to the &quot;Projectile&quot; collision preset
   CollisionComponent-&gt;BodyInstance.SetCollisionProfileName(&quot;Projectile&quot;);
   // --- New Code End ---

   Copy full snippet(6 lines long)

   In Unreal Editor, your collision profiles are stored under **Project Settings** > **Engine** > **Collision**, and you can define up to 18 custom collision profiles to use in code. The default behavior of this ”Projectile” collision profile is **Block**, and this creates collisions on any object it collides with.
6. You defined an `OnHit()` function earlier to activate when the projectile hits something, but you need a way to notify when that collision occurs. To do this, use the `AddDynamic()` macro to subscribe a function to `OnComponentHitEvent` in `CollisionComponent`. Pass this macro the `OnHit()` function.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | CollisionComponent->InitSphereRadius(5.0f); |
   |  |  |
   |  | // Set the collision profile to the "Projectile" collision preset |
   |  | CollisionComponent->BodyInstance.SetCollisionProfileName("Projectile"); |
   |  |  |
   |  | // --- New Code Start --- |
   |  | // Set up a notification for when this component hits something blocking |
   |  | CollisionComponent->OnComponentHit.AddDynamic(this, &AFirstPersonProjectile::OnHit); |
   |  | // --- New Code End --- |
   ```

    CollisionComponent-&gt;InitSphereRadius(5.0f);
   // Set the collision profile to the &quot;Projectile&quot; collision preset
   CollisionComponent-&gt;BodyInstance.SetCollisionProfileName(&quot;Projectile&quot;);
   // --- New Code Start ---
   // Set up a notification for when this component hits something blocking
   CollisionComponent-&gt;OnComponentHit.AddDynamic(this, &amp;AFirstPersonProjectile::OnHit);
   // --- New Code End ---

   Copy full snippet(9 lines long)
7. Set the `CollisionComponent` as the projectile’s `RootComponent` and as the `UpdatedComponent` for the movement component to track.

   C++

   ```
   	CollisionComponent->InitSphereRadius(5.0f);

   	// Set the collision profile to the "Projectile" collision preset
   	CollisionComponent->BodyInstance.SetCollisionProfileName("Projectile");


   	// Set up a notification for when this component hits something blocking
   	CollisionComponent->OnComponentHit.AddDynamic(this, &AFirstPersonProjectile::OnHit);

   	// --- New Code Start ---
   ```

   Expand code  Copy full snippet(15 lines long)
8. Initialize the `ProjectileMovement` component with the following values:

   * `InitialSpeed`: The initial speed of the projectile when it spawns. Set this to `3000.0f`.
   * `MaxSpeed`: The maximum speed of the projectile. Set this to `3000.0f`.
   * `bRotationFollowVelocity`: Whether the object should rotate to make the direction of its velocity. For example, how a paper airplane dips up and down as it rises and falls. Set this to `true`.
   * `bShouldBounce`: Whether the projectile should bounce off obstacles. Set this to `true`.
   * `Bounciness`: How much velocity is preserved after a collision, where lower values cause the projectile to lose more energy. Set this to `0.4f`.
   * Friction: How much tangential (sideways) velocity is preserved after impact. Set this to `0.8f`.

   C++

   ```
   	// Set as root component and UpdatedComponent
   	RootComponent = CollisionComponent;

   	ProjectileMovement->UpdatedComponent = CollisionComponent;
   	// --- New Code Start ---
   	ProjectileMovement->InitialSpeed = 3000.f;
   	ProjectileMovement->MaxSpeed = 3000.f;
   	ProjectileMovement->bRotationFollowsVelocity = true;
   	ProjectileMovement->bShouldBounce = true;
   	ProjectileMovement->Bounciness = 0.2f;
   ```

   Expand code  Copy full snippet(12 lines long)

### Set the Projectile’s Lifespan

By default, you’ll make the projectile disappear a few seconds after firing it. However, once you derive your projectile Blueprints in the editor, you can experiment with changing or removing this default time to try filling your level up with foam darts!

To make the projectile disappear after a number of seconds, follow these steps:

1. In `FirstPersonProjectile.h`, in the `public` section, declare a float named `ProjectileLifespan`.

   Give it a `UPROPERTY()` macro with `EditAnywhere`, `BlueprintReadOnly`, and `Category = “Projectile | Lifespan”`.

   This is the lifespan of the projectile in seconds.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Despawn after 5 seconds by default |
   |  | UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "Projectile | Lifespan") |
   |  | float ProjectileLifespan = 5.0f; |
   ```

   // Despawn after 5 seconds by default
   UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = &quot;Projectile | Lifespan&quot;)
   float ProjectileLifespan = 5.0f;

   Copy full snippet(3 lines long)
2. In `FirstPersonProjectile.cpp`, at the end of the `AFirstPersonProjectile()` constructor function, set the `InitialLifeSpan` of the projectile to `ProjectileLifespan` to make it disappear after five seconds.

   C++

   ```
   	ProjectileMovement->UpdatedComponent = CollisionComponent;
   	ProjectileMovement->InitialSpeed = 3000.f;
   	ProjectileMovement->MaxSpeed = 3000.f;
   	ProjectileMovement->bRotationFollowsVelocity = true;
   	ProjectileMovement->bShouldBounce = true;
   	ProjectileMovement->Bounciness = 0.2f;  
   	ProjectileMovement->Friction = 0.8f;  

   	// --- New Code Start ---
   	// Disappear after 5.0 seconds by default.
   ```

   Expand code  Copy full snippet(12 lines long)

   `InitialLifeSpan` is a property inherited from AActor. It’s a float that sets how long the Actor lives before dying. A value of `0` means the Actor lives until the game stops.

  Your complete `FirstPersonProjectile.h` should look like the following:

C++

```
// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "FirstPersonProjectile.generated.h"

class UProjectileMovementComponent;
class USphereComponent;
```

Expand code  Copy full snippet(53 lines long)

Your complete `AFirstPersonProjectile.cpp` should look like the following:

C++

```
// Copyright Epic Games, Inc. All Rights Reserved.

#include "FirstPersonProjectile.h"
#include "GameFramework/ProjectileMovementComponent.h"
#include "Components/SphereComponent.h"

// Sets default values
AFirstPersonProjectile::AFirstPersonProjectile()
{
 	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
```

Expand code  Copy full snippet(75 lines long)

## Get the Character Camera Direction

Projectiles should spawn from the dart launcher itself, so you’ll need to do some math to know where the dart launcher is and where it’s pointing. Since the launcher is attached to the player character, these values are going to change based on where the character is and where they’re looking.

Your first-person character contains some of the positional information you need to launch a dart, so start by modifying your Character class to capture that information with a line trace and return the result.

To use a trace to get the information you need from your character, follow these steps:

1. In VS, open your Character’s `.h` and `.cpp` files.
2. In the `.h` file, in the `public` section, declare a new function named `GetCameraTargetLocation()`  that returns an `FVector`. This function will return the location in the world that the character is looking at.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | // Returns the location in the world the character is looking at |
   |  | UFUNCTION() |
   |  | FVector GetCameraTargetLocation(); |
   ```

   // Returns the location in the world the character is looking at
   UFUNCTION()
   FVector GetCameraTargetLocation();

   Copy full snippet(3 lines long)
3. In your character's `.cpp` file, implement the `GetCameraTargetLocation()` function. Start by declaring an `FVector` named `TargetPosition` to return.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | FVector AAdventureCharacter::GetCameraTargetLocation() |
   |  | { |
   |  | // The target position to return |
   |  | FVector TargetPosition; |
   |  | } |
   ```

   FVector AAdventureCharacter::GetCameraTargetLocation()
   {
   // The target position to return
   FVector TargetPosition;
   }

   Copy full snippet(5 lines long)
4. Create a pointer to `UWorld` by calling `GetWorld()`.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | FVector AAdventureCharacter::GetCameraTargetLocation() |
   |  | { |
   |  | // The target position to return |
   |  | FVector TargetPosition; |
   |  |  |
   |  | // --- New Code Start --- |
   |  | UWorld* const World = GetWorld(); |
   |  | // --- New Code End --- |
   |  | } |
   ```

   FVector AAdventureCharacter::GetCameraTargetLocation()
   {
   // The target position to return
   FVector TargetPosition;
   // --- New Code Start ---
   UWorld\* const World = GetWorld();
   // --- New Code End ---
   }

   Copy full snippet(9 lines long)
5. Add an `if` statement to check that `World` isn’t null. In the `if` statement, declare a `FHitResult` named `Hit`.

   C++

   ```
   FVector AAdventureCharacter::GetCameraTargetLocation()
   {
   	// The target position to return
   	FVector TargetPosition;

   	UWorld* const World = GetWorld();

   	// --- New Code Start ---
   	if (World != nullptr)
   	{
   ```

   Expand code  Copy full snippet(15 lines long)

   `FHitResult` is a struct in UE that stores information about the result of a collision query, including the Actor or component that was hit and where you hit it.
6. To find the point that your character is looking at, you’re going to simulate a line trace along the vector the character is looking down to some distant point. If the line trace collides with an object, you know where in the world your character is looking.

   In the if statement, declare two `const FVector` values named `TraceStart` and `TraceEnd`:

   1. Set `TraceStart` to the location of the `FirstPersonCameraComponent`.
   2. Set `TraceEnd` to `TraceStart` plus the forward vector of the camera component multiplied by a very large number. This ensures that the trace will go far enough to collide with most objects in your world as long as your character isn’t staring at the sky. (If the character is looking at the sky, `TraceEnd` is the terminal point of the line trace.)

      C++

      ```
      	if (World != nullptr)
      	{
      		// The result of the line trace
      		FHitResult Hit;

      		// --- New Code Start ---
      		// Simulate a line trace from the character along the vector they're looking down
      		const FVector TraceStart = FirstPersonCameraComponent->GetComponentLocation();
      		const FVector TraceEnd = TraceStart + FirstPersonCameraComponent->GetForwardVector() * 10000.0;
      		// --- New Code End ---
      ```

      Expand code  Copy full snippet(12 lines long)
7. Call `LineTraceSingleByChannel()` from the `UWorld` to simulate the trace. Pass it `Hit`, `TraceStart`, `TraceEnd`, and an `ECollisionChannel::ECC_Visibility`.

   This simulates a line trace from `TraceStart` to `TraceEnd`, colliding with any visible objects and storing the result of the trace in `Hit`. `ECollisionChannel::ECC_Visibility` is the channel to use for tracing, and these channels define what types of objects your trace should try to hit. Use `ECC_Visibility` for line-of-sight camera checks.

   C++

   ```
   	if (World != nullptr)
   	{
   		// The result of the line trace
   		FHitResult Hit;

   		// Simulate a line trace from the character along the vector they're looking down
   		const FVector TraceStart = FirstPersonCameraComponent->GetComponentLocation();
   		const FVector TraceEnd = TraceStart + FirstPersonCameraComponent->GetForwardVector() * 10000.0;

   		// --- New Code Start ---
   ```

   Expand code  Copy full snippet(15 lines long)

   The `Hit` value now contains information about the hit result, such as the location and normal of the impact. It also knows if the hit was a result of an object collision. The location of impact (or the end point of the trace line) is the camera target location to return.
8. Use a ternary operator to set `TargetPosition` to either the `Hit.ImpactPoint` if the hit was a blocking hit and `Hit.TraceEnd` if not. Then, return the `TargetPosition`.

   C++

   ```
   	if (World != nullptr)
   	{
   		// The result of the line trace
   		FHitResult Hit;

   		// Simulate a line trace from the character along the vector they're looking down
   		const FVector TraceStart = FirstPersonCameraComponent->GetComponentLocation();
   		const FVector TraceEnd = TraceStart + FirstPersonCameraComponent->GetForwardVector() * 10000.0;

   		// Simulate a line trace and save result in Hit
   ```

   Expand code  Copy full snippet(20 lines long)

Your complete `GetCameraTargetLocation()` function should look like the following:

C++

```
FVector AAdventureCharacter::GetCameraTargetLocation()
{
	// The target position to return
	FVector TargetPosition;

	UWorld* const World = GetWorld();

	if (World != nullptr)
	{
		// The result of the line trace
```

Expand code  Copy full snippet(25 lines long)

## Spawn Projectiles with DartLauncher::Use()

Now that you have a way to know where the character is looking, you can implement the rest of the projectile logic in your dart launcher’s `Use()` function. You’ll get the location and direction to launch the projectile, then spawn the projectile.

To get the location and rotation the projectile should spawn at, follow these steps:

1. In `DartLauncher.h`, at the top of the file, add a forward declaration for `AFirstPersonProjectile`.
2. In the `public` section, declare a `TSubclassOf<AFirstPersonProjectile>` property named `ProjectileClass`. This will be the projectile that the dart launcher spawns. Give this the `UPROPERTY()` macro with `EditAnywhere` and `Category = "Projectile"`.

   `DartLauncher.h` should now look like the following:

   C++

   ```
   // Copyright Epic Games, Inc. All Rights Reserved.

   #pragma once

   #include "CoreMinimal.h"
   #include "EquippableToolBase.h"
   #include "DartLauncher.generated.h"

   class AFirstPersonProjectile;
   ```

   Expand code  Copy full snippet(26 lines long)
3. `DartLauncher.cpp`, add include statements for:

   * `”Kismet/KismetMathLibrary.h”`. Projectile math can be complicated, and this file includes several functions you’ll use for launching projectiles.
   * `"FirstPersonProjectile.h"`
   * `"EnhancedInputComponent.h"`

   C++

   ```
   |  |  |
   | --- | --- |
   |  | #include "Tools/DartLauncher.h" |
   |  | #include "FirstPersonProjectile.h" |
   |  | #include "Kismet/KismetMathLibrary.h" |
   |  | #include "EnhancedInputComponent.h" |
   |  | #include "AdventureCharacter.h" |
   ```

   #include &quot;Tools/DartLauncher.h&quot;
   #include &quot;FirstPersonProjectile.h&quot;
   #include &quot;Kismet/KismetMathLibrary.h&quot;
   #include &quot;EnhancedInputComponent.h&quot;
   #include &quot;AdventureCharacter.h&quot;

   Copy full snippet(5 lines long)
4. In the DartLauncher’s `Use()` implementation, after the debug message:

   1. Get the `UWorld` by calling `GetWorld()`.
   2. Add an `if` statement to check that `World` and the `ProjectileClass` are not null.
   3. In the `if` statement, get the position the character is looking at by calling `OwningCharacter->GetCameraTargetLocation()`.

   C++

   ```
   void ADartLauncher::Use()
   {
   	GEngine->AddOnScreenDebugMessage(-1, 5.0f, FColor::Yellow, TEXT("Using the dart launcher!"));

     UWorld* const World = GetWorld();
     if (World != nullptr && ProjectileClass != nullptr)
     {
       FVector TargetPosition = OwningCharacter->GetCameraTargetLocation();
     }
   ```

   Expand code  Copy full snippet(11 lines long)
5. Projectiles should spawn from the tool the character is holding, but not from the center of the equipped object. The dart launcher’s `SKM_Pistol` mesh has a ”Muzzle” socket you can use to set a precise spawn point for your darts.

   In the `if` statement, declare a new `FVector` named `SocketLocation` and set it to the result of calling `GetSocketLocation(“Muzzle”)` on the `ToolMeshComponent`.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | if (World != nullptr && ProjectileClass != nullptr) |
   |  | { |
   |  | // Get the direction of the player camera |
   |  | FVector TargetPosition = OwningCharacter->GetCameraTargetLocation(); |
   |  |  |
   |  | // --- New Code Start --- |
   |  | // Get the correct socket to spawn the projectile from |
   |  | FVector SocketLocation = ToolMeshComponent->GetSocketLocation("Muzzle"); |
   |  | // --- New Code End --- |
   |  | } |
   ```

    if (World != nullptr &amp;&amp; ProjectileClass != nullptr)
   {
   // Get the direction of the player camera
   FVector TargetPosition = OwningCharacter-&gt;GetCameraTargetLocation();
   // --- New Code Start ---
   // Get the correct socket to spawn the projectile from
   FVector SocketLocation = ToolMeshComponent-&gt;GetSocketLocation(&quot;Muzzle&quot;);
   // --- New Code End ---
   }

   Copy full snippet(10 lines long)
6. Declare an `FRotator` named `SpawnRotation`. This is the rotation (pitch, yaw, and roll values) of the projectile as it spawns.

   Set this to the result of calling `FindLookAtRotation()` from the kismet math library, passing the `SocketLocation` and `TargetPosition` you got from the player character.

   C++

   ```
   	if (World != nullptr && ProjectileClass != nullptr)
   	{
   		// Get the direction of the player camera
   		FVector TargetPosition = OwningCharacter->GetCameraTargetLocation();

   		// Get the correct socket to spawn the projectile from
   		FVector SocketLocation = ToolMeshComponent->GetSocketLocation("Muzzle");

   		// --- New Code Start ---
   		// Get projectile's rotation as it spawns so we know in what direction to apply an offset
   ```

   Expand code  Copy full snippet(13 lines long)

   `FindLookAtRotation` calculates and returns the rotation you’d need at `SocketLocation` to face `TargetPosition`.
7. Declare an `FVector` named `SpawnLocation`, and set it to the result of adding the `SocketLocation` and the forward vector of the `SpawnRotation` multiplied by `10.0`.

   The muzzle socket isn’t quite at the front of the launcher, so you’ll need to multiply the vector by an offset to get the projectile firing from the right location.

   C++

   ```
   	if (World != nullptr && ProjectileClass != nullptr)
   	{
   		// Get the direction of the player camera
   		FVector TargetPosition = OwningCharacter->GetCameraTargetLocation();

   		// Get the correct socket to spawn the projectile from
   		FVector SocketLocation = ToolMeshComponent->GetSocketLocation("Muzzle");

   		// Get the rotation of the projectile as it spawns so we know in what direction to apply an offset 
   		FRotator SpawnRotation = UKismetMathLibrary::FindLookAtRotation(SocketLocation, TargetPosition);
   ```

   Expand code  Copy full snippet(15 lines long)

Now that you’ve got a location and rotation, you’re ready to spawn the projectile.

To spawn a projectile, follow these steps:

1. Still in the `Use()` function, in the `if` statement, declare a `FActorSpawnParameters` named `ActorSpawnParams`. This class includes information about where and how to spawn the actor.

   C++

   ```
   void ADartLauncher::Use()
   {
   	GEngine->AddOnScreenDebugMessage(-1, 5.0f, FColor::Yellow, TEXT("Using the dart launcher!"));

   	UWorld* const World = GetWorld();
   	if (World != nullptr && ProjectileClass != nullptr)
   	{
   		// Get the direction of the player camera
   		FVector TargetPosition = OwningCharacter->GetCameraTargetLocation();
   ```

   Expand code  Copy full snippet(24 lines long)
2. Set the `SpawnCollisionHandlingOverride` value in `ActorSpawnParams` to `ESpawnActorCollisionHandlingMethod::AdjustIfPossibleButDontSpawnIfColliding`.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | //Set Spawn Collision Handling Override |
   |  | FActorSpawnParameters ActorSpawnParams; |
   |  |  |
   |  | // --- New Code Start --- |
   |  | ActorSpawnParams.SpawnCollisionHandlingOverride = ESpawnActorCollisionHandlingMethod::AdjustIfPossibleButDontSpawnIfColliding; |
   |  | // --- New Code End --- |
   ```

    //Set Spawn Collision Handling Override
   FActorSpawnParameters ActorSpawnParams;
   // --- New Code Start ---
   ActorSpawnParams.SpawnCollisionHandlingOverride = ESpawnActorCollisionHandlingMethod::AdjustIfPossibleButDontSpawnIfColliding;
   // --- New Code End ---

   Copy full snippet(6 lines long)

   This line of code tries to find a place to spawn the projectile where it isn’t colliding with another Actor (such as inside a wall) and won’t spawn it if a suitable location isn’t found.
3. Use `SpawnActor()` to spawn the projectile at the muzzle of the dart launcher, passing `ProjectileClass`, `SpawnLocation`, `SpawnRotation`, and `ActorSpawnParams`.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | ActorSpawnParams.SpawnCollisionHandlingOverride = ESpawnActorCollisionHandlingMethod::AdjustIfPossibleButDontSpawnIfColliding; |
   |  |  |
   |  | // --- New Code Start --- |
   |  | // Spawn the projectile at the muzzle |
   |  | World->SpawnActor<AFirstPersonProjectile>(ProjectileClass, SpawnLocation, SpawnRotation, ActorSpawnParams); |
   |  | // --- New Code End --- |
   ```

    ActorSpawnParams.SpawnCollisionHandlingOverride = ESpawnActorCollisionHandlingMethod::AdjustIfPossibleButDontSpawnIfColliding;
   // --- New Code Start ---
   // Spawn the projectile at the muzzle
   World-&gt;SpawnActor&lt;AFirstPersonProjectile&gt;(ProjectileClass, SpawnLocation, SpawnRotation, ActorSpawnParams);
   // --- New Code End ---

   Copy full snippet(6 lines long)

Your complete `Use()` function should now look like the following:

C++

```
void ADartLauncher::Use()
{
	GEngine->AddOnScreenDebugMessage(-1, 5.0f, FColor::Yellow, TEXT("Using the dart launcher!"));

	UWorld* const World = GetWorld();
	if (World != nullptr && ProjectileClass != nullptr)
	{
		FVector TargetPosition = OwningCharacter->GetCameraTargetLocation();
			
		// Get the correct socket to spawn the projectile from
```

Expand code  Copy full snippet(22 lines long)

## Derive a Foam Dart Class and Blueprint

Now that all the spawning logic is done, it’s time to build a real projectile! Your dart launcher class needs a subclass of `AFirstPersonProjectile` to launch, so you’ll need to build one in code to use in your level.

To derive a foam dart projectile class to use in-game, follow these steps:

1. In Unreal Editor, go to **Tools > New C++ Class**.
2. Go to **All Classes**, search for and select **First Person Projectile** as the parent class, and name the class `FoamDart`. Click **Create Class**.

   [![](https://dev.epicgames.com/community/api/documentation/image/ae41edfd-1522-4175-a05c-0594e642e7a2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ae41edfd-1522-4175-a05c-0594e642e7a2?resizing_type=fit)
3. In VS, leave these files as-is, save your code, and compile it.

In this tutorial, you won’t be implementing any custom projectile code beyond what you defined in `FirstPersonProjectile`, but you can modify the `FoamDart` class on your own to suit the needs of your project. For example, you could try making the dart projectiles stick to objects instead of disappearing or bouncing around.

To create a foam dart Blueprint, follow these steps:

1. In Unreal Editor, create a Blueprint class based on **FoamDart** and name it `BP_FoamDart`. Save this in your `FirstPerson/Blueprints/Tools` folder.

   [![](https://dev.epicgames.com/community/api/documentation/image/5f6c7328-0a6e-4e60-9559-94d290f92506?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5f6c7328-0a6e-4e60-9559-94d290f92506?resizing_type=fit)
2. With the Blueprint open, select the **Projectile Mesh** component and set the **Static Mesh** to `SM_FoamBullet`.

   [![](https://dev.epicgames.com/community/api/documentation/image/9f2f6022-fc58-427d-aca4-248c455c0cb2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9f2f6022-fc58-427d-aca4-248c455c0cb2?resizing_type=fit)
3. The foam dart mesh appears in the **Viewport**. Zoom in or press **F** to look at the orientation of the mesh. The rounded end is the front of the dart, and it should be pointing up the X axis so your darts fire in the correct orientation (`ProjectileMovement` assumes +X is forward).

   Rotate the dart on the Z (blue) axis +90 degrees.
4. Compile and save your Blueprint.
5. In the **Content Browser**, open **`BP_DartLauncher`**.
6. In its **Details** panel, in the new **Projectile** section, set the **Projectile Class**to `BP_FoamDart`.

   [![](https://dev.epicgames.com/community/api/documentation/image/8de5f4e5-4d59-408c-aff3-064c2efcbaf2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8de5f4e5-4d59-408c-aff3-064c2efcbaf2?resizing_type=fit)

   If you don't see `BP_FoamDart` in the list, go to the Content Browser, select `BP_FoamDart`, then go back to the **Projectile Class** property and click **Use Selected Asset from Content Browser**.
7. Click **Compile** and **Save**.

It’s time for the big reveal. Save your assets and click **Play**. When the game begins, you can run to the dart launcher to pick it up. Pressing the left mouse button spawns a projectile from the muzzle of the dart launcher and bounces it around the level! These projectiles should disappear after five seconds and impart a small physics force on objects they collide with (including you!).

If the dart launcher doesn't fire and you don't see the "Using the dart launcher!" debug message, ensure you've assigned `IA_UseTool` to the **Use Action** property in your character's Blueprint.

## Bonus: Adjust Projectiles and Tools

Optionally implement these final adjustments to make your dart launcher and darts look their best.

#### Make Fallen Projectiles Lie Flat

In `FirstPersonProjectile.cpp`, when the projectile hits something, check if the projectile has hit the ground (a flat horizontal surface) and if it has, make it lie flat.

At the top of `OnHit()`, add this code:

C++

```
|  |  |
| --- | --- |
|  | // If we hit the ground (mostly-up surface normal), lay the dart flat. |
|  | if (FVector::DotProduct(Hit.ImpactNormal, FVector::UpVector) > 0.7f) |
|  | { |
|  | FRotator Flat = GetActorRotation(); |
|  | Flat.Pitch = 0.f; |
|  | Flat.Roll = 0.f; |
|  | SetActorRotation(Flat); |
|  |  |
|  | return; |
|  | } |
```

// If we hit the ground (mostly-up surface normal), lay the dart flat.
if (FVector::DotProduct(Hit.ImpactNormal, FVector::UpVector) > 0.7f)
{
FRotator Flat = GetActorRotation();
Flat.Pitch = 0.f;
Flat.Roll = 0.f;
SetActorRotation(Flat);
return;
}

Copy full snippet(10 lines long)

## Next Up

Congratulations! You’ve completed the First-Person Programmer Track tutorial and learned a lot along the way!

You’ve implemented custom characters and movement, created pickups and data assets, and even made equippable tools with their own projectiles. You’ve got everything you need to take this project and turn it into something all your own.

Here are a few suggestions:

* Can you expand the player’s inventory with different types of items? What about stacks of items?
* Can you combine pickups and projectiles to create pickupable ammo? How about implementing this ammo system in the dart launcher?
* Can you develop the idea of consumables into equippable consumables? How about a health pack the player holds, or a ball they can pick up and throw?

## Complete Code

C++

FirstPersonProjectile.h

```
// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "FirstPersonProjectile.generated.h"

class UProjectileMovementComponent;
class USphereComponent;
```

Expand code  Copy full snippet(53 lines long)

C++

FirstPersonProjectile.cpp

```
// Copyright Epic Games, Inc. All Rights Reserved.

#include "FirstPersonProjectile.h"
#include "GameFramework/ProjectileMovementComponent.h"
#include "Components/SphereComponent.h"

// Sets default values
AFirstPersonProjectile::AFirstPersonProjectile()
{
 	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
```

Expand code  Copy full snippet(86 lines long)

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

Expand code  Copy full snippet(118 lines long)

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

Expand code  Copy full snippet(260 lines long)

C++

DartLauncher.h

```
// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "EquippableToolBase.h"
#include "DartLauncher.generated.h"

class AFirstPersonProjectile;
```

Expand code  Copy full snippet(26 lines long)

C++

DartLauncher.cpp

```
// Copyright Epic Games, Inc. All Rights Reserved.


#include "Tools/DartLauncher.h"
#include "FirstPersonProjectile.h"  
#include "Kismet/KismetMathLibrary.h"
#include "EnhancedInputComponent.h" 
#include "AdventureCharacter.h"
```

Expand code  Copy full snippet(51 lines long)

C++

EquippableToolBase.h

```
// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "EnhancedInputSubsystems.h"    //
#include "Animation/AnimBlueprint.h"
#include "Components/SkeletalMeshComponent.h"
#include "EquippableToolBase.generated.h"
```

Expand code  Copy full snippet(62 lines long)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Before You Begin](/documentation/en-us/unreal-engine/coder-08-implement-a-projectile-in-unreal-engine?application_version=5.7#beforeyoubegin)
* [Basic Projectiles](/documentation/en-us/unreal-engine/coder-08-implement-a-projectile-in-unreal-engine?application_version=5.7#basicprojectiles)
* [Create a Projectile Base Class](/documentation/en-us/unreal-engine/coder-08-implement-a-projectile-in-unreal-engine?application_version=5.7#createaprojectilebaseclass)
* [Implement Projectile Behavior When Hitting Objects](/documentation/en-us/unreal-engine/coder-08-implement-a-projectile-in-unreal-engine?application_version=5.7#implementprojectilebehaviorwhenhittingobjects)
* [Add the Projectile’s Mesh, Movement, Collision Components](/documentation/en-us/unreal-engine/coder-08-implement-a-projectile-in-unreal-engine?application_version=5.7#addtheprojectile%E2%80%99smesh,movement,collisioncomponents)
* [Set the Projectile’s Lifespan](/documentation/en-us/unreal-engine/coder-08-implement-a-projectile-in-unreal-engine?application_version=5.7#settheprojectile%E2%80%99slifespan)
* [Get the Character Camera Direction](/documentation/en-us/unreal-engine/coder-08-implement-a-projectile-in-unreal-engine?application_version=5.7#getthecharactercameradirection)
* [Spawn Projectiles with DartLauncher::Use()](/documentation/en-us/unreal-engine/coder-08-implement-a-projectile-in-unreal-engine?application_version=5.7#spawnprojectileswithdartlauncher::use())
* [Derive a Foam Dart Class and Blueprint](/documentation/en-us/unreal-engine/coder-08-implement-a-projectile-in-unreal-engine?application_version=5.7#deriveafoamdartclassandblueprint)
* [Bonus: Adjust Projectiles and Tools](/documentation/en-us/unreal-engine/coder-08-implement-a-projectile-in-unreal-engine?application_version=5.7#bonus:adjustprojectilesandtools)
* [Make Fallen Projectiles Lie Flat](/documentation/en-us/unreal-engine/coder-08-implement-a-projectile-in-unreal-engine?application_version=5.7#makefallenprojectileslieflat)
* [Next Up](/documentation/en-us/unreal-engine/coder-08-implement-a-projectile-in-unreal-engine?application_version=5.7#nextup)
* [Complete Code](/documentation/en-us/unreal-engine/coder-08-implement-a-projectile-in-unreal-engine?application_version=5.7#completecode)

Related documents

[Code a First-Person Adventure Game

![Code a First-Person Adventure Game](https://dev.epicgames.com/community/api/documentation/image/ffc1a8f8-e7e5-42c0-b4ed-32ce6d3adbbc?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/code-a-firstperson-adventure-game-in-unreal-engine)
