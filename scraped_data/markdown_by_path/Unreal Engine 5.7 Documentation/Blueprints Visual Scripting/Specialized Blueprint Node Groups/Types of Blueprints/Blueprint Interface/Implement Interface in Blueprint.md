<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/implementing-blueprint-interfaces-in-unreal-engine?application_version=5.7 -->

# Implement Interface in Blueprint

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
7. [Types of Blueprints](/documentation/en-us/unreal-engine/types-of-blueprints-in-unreal-engine "Types of Blueprints")
8. [Blueprint Interface](/documentation/en-us/unreal-engine/blueprint-interface-in-unreal-engine "Blueprint Interface")
9. Implement Interface in Blueprint

# Implement Interface in Blueprint

Implement interface functions in Blueprints that inherit from C++ or Blueprint interfaces.

![Implement Interface in Blueprint](https://dev.epicgames.com/community/api/documentation/image/eae83bca-eaa5-4c7b-b008-13e1701ad94b?resizing_type=fill&width=1920&height=335)

 On this page

Interfaces are a common method of interacting with different types of objects that all share some specific functionality. This means you can enforce different types of objects to implement some of the same functionality, no matter how dissimilar the objects are. Blueprints can implement:

* Blueprint Interfaces
* Unreal C++ Interfaces

## Create an Interface

To create an interface, see the following documentation:

* [Create a Blueprint Interface](/documentation/en-us/unreal-engine/blueprint-interface-in-unreal-engine)
* [Create an Unreal C++ Interface](/documentation/404)

## Content Used on this Page

The content on this page uses an Unreal Engine interface defined in C++ and an actor that implements that interface. The header and source files are provided below:

MyInterface.h

```
#pragma once

#include "CoreMinimal.h"
#include "UObject/Interface.h"
#include "MyInterface.generated.h"

// This class does not need to be modified.
UINTERFACE(MinimalAPI, Blueprintable)
class UMyInterface : public UInterface
{
	GENERATED_BODY()
};


class SAMPLE_API IMyInterface
{
	GENERATED_BODY()

	// Add interface functions to this class. This is the class that will be inherited to implement this interface.
public:

	virtual bool MyInterfaceFunction();

	UFUNCTION(BlueprintCallable, BlueprintImplementableEvent, Category=MyInterface)
	bool MyImplementableFunction();

	UFUNCTION(BlueprintCallable, BlueprintNativeEvent, Category=MyInterface)
	FString MyNativeFunction();

	// Utility Functions
public:
	FString GetInterfaceName();
};
Copy full snippet
```

MyInterface.cpp

```
#include "MyInterface.h"

// Add default functionality here for any IMyInterface functions that are not pure virtual.
bool IMyInterface::MyInterfaceFunction()
{
	return false;
}

FString IMyInterface::GetInterfaceName()
{
	return FString(TEXT("MyInterface"));
}
Copy full snippet
```

MyInterfaceActor.h

```
#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "MyInterface.h"
#include "MyInterfaceActor.generated.h"

UCLASS()
class SAMPLE_API AMyInterfaceActor : public AActor, public IMyInterface
{
	GENERATED_BODY()	

public:	
	// Sets default values for this actor's properties
	AMyInterfaceActor();

	// Interface function implementations
	virtual bool MyInterfaceFunction() override;

	FString MyNativeFunction_Implementation() override;

	// Called every frame
	virtual void Tick(float DeltaTime) override;

protected:
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

};
Copy full snippet
```

MyInterfaceActor.cpp

```
#include "MyInterfaceActor.h"

// Sets default values
AMyInterfaceActor::AMyInterfaceActor()
{
 	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;
}

bool AMyInterfaceActor::MyInterfaceFunction()
{
	return true;
}

FString AMyInterfaceActor::MyNativeFunction_Implementation()
{
	return FString(TEXT("My Native Function C++ Implementation first."));
}

// Called when the game starts or when spawned
void AMyInterfaceActor::BeginPlay()
{
	Super::BeginPlay();
}

// Called every frame
void AMyInterfaceActor::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);
}
Copy full snippet
```

## Add an Interface to an Existing Blueprint

To add an interface to an existing Blueprint class, follow these steps:

1. Open your existing Blueprint class.

   ![Blueprint Actor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a03d26e0-a6c6-41cd-bbab-09f4180d826b/interface-actor.png)

   Existing Blueprint class.
2. In the Blueprint Toolbar, select **Class Settings**.

   ![Select Class Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7e30ee96-dc22-4069-9756-902b4a1bd580/bp-class-settings.png)

   Open Blueprint class settings.
3. Navigate to the **Class Settings Details Panel**. Under **Interfaces > Implemented Interfaces** select your interface from the dropdown that says **Add**.

   ![Add implemented interface](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/72320e42-d888-41eb-bc3f-3cf82d74743b/implemented-interfaces.png)

   Add an interface you want this Blueprint to implement.
4. Search for the interface you want your class to implement.

   This example uses a C++ interface named `MyInterface` defined in `MyInterface.h`.
5. Once you have found the interface, choose the interface, then **Compile** and **Save** your Blueprint.

Your Blueprint should now be configured to implement your interface. The **My Blueprint** tab should now display a category for the interface you selected and all the functions the interface provides for you to implement.

The Inherited Interfaces section in the Interfaces category of the Class Settings automatically populates with any Interfaces that are inherited by this class through its parent Blueprint or C++ class. Below, a Blueprint actor inherits from the `MyInterfaceActor` C++ class thereby inheriting `MyInterface`.

![Show inheritied interfaces](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a5cd1b2b-a6dd-47b4-af46-1f9e37bf0f82/inheritied-interfaces.png)

List the inherited interfaces for this Blueprint.

## Remove an Interface

To remove an interface from a Blueprint class, click the X button located next to the interface you want to remove in the Implemented Interfaces list in the Class Settings.

![Remove an interface from a Blueprint](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f4c16725-fa5c-4aaf-9c7a-5d7a055d64f8/remove-interface.png)

Remove an inherited interface from this Blueprint.

## Implement Interface Functions

To implement an interface function in your Blueprint that inherits from an interface, do one of the following:

* Double-click on the function in **My Blueprint > Interfaces** to open the function’s Blueprint graph.
* Right-click on the function in **My Blueprint > Interfaces** and select **Open Graph**.

![Open function Blueprint graph](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f9b06694-565b-4d66-b54e-f54bc94b8083/open-graph.png)

Open the function's Blueprint graph.

Here you can implement the interface function for your class. See the [Blueprint Functions](/documentation/en-us/unreal-engine/functions-in-unreal-engine) documentation for more information about implementing functions in Blueprint.

![Implementation of interface function](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4f015ed8-7a52-46c9-83bc-da0fe7e009a3/implementable-function.png)

Default implementation of an interface function in Blueprint.

## Override Interface Functions

Blueprint implementations of interface functions override implementations in parent classes by default. To first call the parent class’ implementation inside your Blueprint, see Step 4 in the [Blueprint Native Events](/documentation/en-us/unreal-engine/implementing-blueprint-interfaces-in-unreal-engine#blueprintnativeevents) section.

## Blueprint Native Events

`BlueprintNativeEvent` functions differ from `BlueprintImplementableEvent` functions. `BlueprintImplementableEvent` functions can only be implemented within Blueprint. `BlueprintNativeEvent` functions can be implemented in Blueprint, C++, or both. To implement a `BlueprintNativeEvent`, follow the steps for the context that best suits your needs:

* To implement a `BlueprintNativeEvent` purely in Blueprint, follow the guidance in the [Implement Interface Functions](/documentation/en-us/unreal-engine/implementing-blueprint-interfaces-in-unreal-engine#implementinterfacefunctions) section.
* To implement a `BlueprintNativeEvent` in C++, see the [Unreal Interfaces](/documentation/404) documentation.
* To override a `BlueprintNativeEvent` in Blueprint and have the Blueprint call the C++ implementation contained in its parent class, see the [Override Blueprint Native Event in Blueprint](/documentation/en-us/unreal-engine/implementing-blueprint-interfaces-in-unreal-engine#overrideblueprintnativeeventinblueprint) section.

### Override Blueprint Native Event in Blueprint

To override a Blueprint native event in Blueprint that is defined in C++, follow these steps:

1. Open your Blueprint that inherits from a C++ class implementing an interface.
   * In this case, the C++ class implementation looks like this:

     ```
           FString AMyInterfaceActor::MyNativeFunction_Implementation()
           {
               return FString(TEXT("My Native Function C++ Implementation first."));
           }
     Copy full snippet
     ```
2. Open your `BlueprintNativeEvent` function in the **My Blueprint** panel.

   ![Blueprint native function](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1e384242-8cf8-484e-8185-96600fae5c45/native-function.png)

   Open function implementation.
3. If you have not already implemented this function in Blueprint, you should see a main function node.

   ![Main Blueprint function node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f381f5e7-f5f7-41e9-9c32-86f901a352cc/native-function-node.png)

   Blueprint function definition.
4. Right-click on this node and choose **Add Call to Parent Function**.

   ![Add call to parent function](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3aa09ad0-aae3-4391-88d0-109a761b3f75/call-parent-function.png)

   Add call to parent function in Blueprint.
5. Add your Blueprint functionality after the **Parent** node.

   ![Add Blueprint functionality after parent node](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/592883bc-3601-43a4-88de-66c2f8e3a24e/native-function-impl.png)

   Add additional functionality after call to parent.

## Call Interface Functions

Interface functions are called in different ways depending on the context. When you want to call **My Implementable Function** in Blueprint, you have multiple options:

* My Implementable Function (Object)
* My Implementable Function (Interface)
* My Implementable Function (Message)

![Different Blueprint interface function node types](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/12b088a3-d6f2-4047-bbfb-4aed8c1a1a33/function-types.png)

Blueprint nodes corresponding to the different types of Blueprint interface function calls.

| **Blueprint Function Type** | **Description** |
| --- | --- |
| Object | Call on an object of the specified class that implements the interface. |
| Interface | Call on an object that implements this interface. |
| Message | Call on any object.  If the object does not implement the correct interface, the function fails silently. This method is also slower than the object and interface methods. |

* [interface](https://dev.epicgames.com/community/search?query=interface)
* [blueprint](https://dev.epicgames.com/community/search?query=blueprint)
* [blueprintnativeevent](https://dev.epicgames.com/community/search?query=blueprintnativeevent)
* [blueprintimplementableevent](https://dev.epicgames.com/community/search?query=blueprintimplementableevent)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Create an Interface](/documentation/en-us/unreal-engine/implementing-blueprint-interfaces-in-unreal-engine?application_version=5.7#createaninterface)
* [Content Used on this Page](/documentation/en-us/unreal-engine/implementing-blueprint-interfaces-in-unreal-engine?application_version=5.7#contentusedonthispage)
* [Add an Interface to an Existing Blueprint](/documentation/en-us/unreal-engine/implementing-blueprint-interfaces-in-unreal-engine?application_version=5.7#addaninterfacetoanexistingblueprint)
* [Remove an Interface](/documentation/en-us/unreal-engine/implementing-blueprint-interfaces-in-unreal-engine?application_version=5.7#removeaninterface)
* [Implement Interface Functions](/documentation/en-us/unreal-engine/implementing-blueprint-interfaces-in-unreal-engine?application_version=5.7#implementinterfacefunctions)
* [Override Interface Functions](/documentation/en-us/unreal-engine/implementing-blueprint-interfaces-in-unreal-engine?application_version=5.7#overrideinterfacefunctions)
* [Blueprint Native Events](/documentation/en-us/unreal-engine/implementing-blueprint-interfaces-in-unreal-engine?application_version=5.7#blueprintnativeevents)
* [Override Blueprint Native Event in Blueprint](/documentation/en-us/unreal-engine/implementing-blueprint-interfaces-in-unreal-engine?application_version=5.7#overrideblueprintnativeeventinblueprint)
* [Call Interface Functions](/documentation/en-us/unreal-engine/implementing-blueprint-interfaces-in-unreal-engine?application_version=5.7#callinterfacefunctions)
