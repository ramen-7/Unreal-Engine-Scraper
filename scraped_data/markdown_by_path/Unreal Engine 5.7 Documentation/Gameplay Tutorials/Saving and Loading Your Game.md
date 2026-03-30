<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/saving-and-loading-your-game-in-unreal-engine?application_version=5.7 -->

# Saving and Loading Your Game

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
5. [Gameplay Tutorials](/documentation/en-us/unreal-engine/gameplay-tutorials-for-unreal-engine "Gameplay Tutorials")
6. Saving and Loading Your Game

# Saving and Loading Your Game

Overview of how to save and load your game

![Saving and Loading Your Game](https://dev.epicgames.com/community/api/documentation/image/135327c4-52c3-4524-9d2b-2f25d8ca173e?resizing_type=fill&width=1920&height=335)

 On this page

Programming Language 

×C++

Select an option from the dropdown to see content relevant to it.

The meaning of "saving the game" can vary considerably from one game to the next, but the general idea of enabling players to quit the game and then resume where they left off at a later time is a part of most modern games. Depending on what type of game you're making, you may only need a few basic pieces of information, such as the last checkpoint the player reached and maybe which items the player has found. Or you may need much more detailed information, possibly involving things like a long list of the player's social interactions with other in-game characters, or the current status of a variety of quests, mission objectives, or subplots.

Unreal Engine (UE) features a saving and loading system that revolves around one or more custom **SaveGame** classes that you create to meet your game's specific needs, including all of the information that you need to preserve across multiple play sessions. The system supports the ability to have multiple saved game files, and to save different SaveGame classes to those files. This is useful for separating globally-unlocked features from playthrough-specific game data.

## Creating a SaveGame Object

The `USaveGame` class sets up an object that can be used as a target for the saving and loading functions declared in `Kismet/GameplayStatics.h`.

You can create a new class based on `USaveGame` using the [C++ Class Wizard](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-cplusplus-class-wizard-in-unreal-engine).

[![](https://dev.epicgames.com/community/api/documentation/image/266ea198-39aa-40a5-b099-9e37109e465f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/266ea198-39aa-40a5-b099-9e37109e465f?resizing_type=fit)

In this example, the new `USaveGame` class is called `UMySaveGame`. In order to use it, add the following lines to your game module's header file, after any other `#include` directives:

C++

MyProject.h

```
|  |  |
| --- | --- |
|  | #include "MySaveGame.h" |
|  | #include "Kismet/GameplayStatics.h" |
```

#include &quot;MySaveGame.h&quot;
#include &quot;Kismet/GameplayStatics.h&quot;

Copy full snippet(2 lines long)

### Header

In the header file for your `SaveGame` object, you can declare any variables you want your `SaveGame` to store.

C++

```
|  |  |
| --- | --- |
|  | UPROPERTY(VisibleAnywhere, Category = Basic) |
|  | FString PlayerName; |
```

UPROPERTY(VisibleAnywhere, Category = Basic)
FString PlayerName;

Copy full snippet(2 lines long)

In this example, there are also variables declared that will be used to store default values for the `SaveSlotName` and the `UserIndex`, so that each class that saves to this
`SaveGame` object will not have to independently set those variables. This step is optional, and will cause there to be one save slot that gets overwritten if the default values are not changed.

C++

MySaveGame.h

```
#pragma once

	#include "GameFramework/SaveGame.h"
	#include "MySaveGame.generated.h"

	/**
	 *
	 */
	UCLASS()
	class [PROJECTNAME]_API UMySaveGame : public USaveGame
```

Expand code  Copy full snippet(26 lines long)

### Source

Generally, the `SaveGame` object's source file does not need any particular code to function, unless your particular save system has additional functionality you would like to set up
here.

This example does define the values of `SaveSlotName` and `UserIndex` in the class constructor, so they can be read out and used by other gameplay classes.

C++

MySaveGame.cpp

```
|  |  |
| --- | --- |
|  | // Copyright 1998-2018 Epic Games, Inc. All Rights Reserved. |
|  |  |
|  | #include "[ProjectName].h" |
|  | #include "MySaveGame.h" |
|  |  |
|  | UMySaveGame::UMySaveGame() |
|  | { |
|  | SaveSlotName = TEXT("TestSaveSlot"); |
|  | UserIndex = 0; |
|  | } |
```

// Copyright 1998-2018 Epic Games, Inc. All Rights Reserved.
#include &quot;[ProjectName].h&quot;
#include &quot;MySaveGame.h&quot;
UMySaveGame::UMySaveGame()
{
SaveSlotName = TEXT(&quot;TestSaveSlot&quot;);
UserIndex = 0;
}

Copy full snippet(10 lines long)

## Saving A Game

Once you have created a SaveGame class, you can populate it with variables to store your game's data. For example, you might create an integer variable to store the player's score, or a string variable for the player's name. When you save the game, you will transfer that information from the current game world into a SaveGame object, and when loading a game, you will copy it from the SaveGame object to game object like Characters, the Player Controller, or the Game Mode.

First, call `CreateSaveGameObject` (from the `UGameplayStatics` library) to get a new `UMySaveGame` object. Once you have the object, you can populate it with the data you want to save. Finally, call `SaveGameToSlot` or `AsyncSaveGameToSlot` to write the data out to your device.

### Asynchronous Saving

`AsyncSaveGameToSlot` is the recommended method for saving the game. Running asynchronously prevents a sudden framerate hitch, making it less noticeable to players and avoiding a possible certification issue on some platforms. When the save process is complete, the delegate (of type `FAsyncSaveGameToSlotDelegate`) will be called with the slot name, the user index, and a `bool` indicating success or failure.

C++

```
if (UMySaveGame* SaveGameInstance = Cast<UMySaveGame>(UGameplayStatics::CreateSaveGameObject(UMySaveGame::StaticClass())))
	{
		// Set up the (optional) delegate.
		FAsyncSaveGameToSlotDelegate SavedDelegate;
		// USomeUObjectClass::SaveGameDelegateFunction is a void function that takes the following parameters: const FString& SlotName, const int32 UserIndex, bool bSuccess
		SavedDelegate.BindUObject(SomeUObjectPointer, &USomeUObjectClass::SaveGameDelegateFunction);

		// Set data on the savegame object.
		SaveGameInstance->PlayerName = TEXT("PlayerOne");
```

Expand code  Copy full snippet(13 lines long)

### Synchronous Saving

`SaveGameToSlot` is sufficient for small SaveGame formats, and for saving the game while paused or in a menu. It's also easy to use, as it simply saves the game immediately and returns a `bool` indicating success or failure. For larger amounts of data, or for auto-saving game while the player is still actively interacting with your game world, `AsyncSaveGameToSlot` is a better choice.

C++

```
if (UMySaveGame* SaveGameInstance = Cast<UMySaveGame>(UGameplayStatics::CreateSaveGameObject(UMySaveGame::StaticClass())))
	{
		// Set data on the savegame object.
		SaveGameInstance->PlayerName = TEXT("PlayerOne");

		// Save the data immediately.
		if (UGameplayStatics::SaveGameToSlot(SaveGameInstance, SlotNameString, UserIndexInt32))
		{
			// Save succeeded.
		}
```

Expand code  Copy full snippet(11 lines long)

### Binary Saving

You can transfer a SaveGame object to memory with the `SaveGameToMemory` function. This function only offers synchronous operation, but is faster than saving to a drive. The caller provides a reference to a buffer (a `TArray<uint8>&`) where the data will be stored. On success, the function returns true.

C++

```
|  |  |
| --- | --- |
|  | TArray<uint8> OutSaveData; |
|  | if (UGameplayStatics::SaveGameToMemory(SaveGameObject, OutSaveData)) |
|  | { |
|  | // The operation succeeded, and OutSaveData now contains a binary represenation of the SaveGame object. |
|  | } |
```

TArray&lt;uint8&gt; OutSaveData;
if (UGameplayStatics::SaveGameToMemory(SaveGameObject, OutSaveData))
{
// The operation succeeded, and OutSaveData now contains a binary represenation of the SaveGame object.
}

Copy full snippet(5 lines long)

You can also save binary data directly to a file, similar to the `SaveGameToSlot` function, by calling `SaveDataToSlot` with the buffer (a `const TArray<uint8>&`) and the slot name and user ID information. As with `SaveGameToMemory`, this function only offers synchronous operation, and returns a `bool` to indicate success or failure.

C++

```
|  |  |
| --- | --- |
|  | if (UGameplayStatics::SaveDataToSlot(InSaveData, SlotNameString, UserIndexInt32)) |
|  | { |
|  | // The operation succeeded, and InSaveData has been written to the save file defined by the slot name and user ID we provided. |
|  | } |
```

if (UGameplayStatics::SaveDataToSlot(InSaveData, SlotNameString, UserIndexInt32))
{
// The operation succeeded, and InSaveData has been written to the save file defined by the slot name and user ID we provided.
}

Copy full snippet(4 lines long)

On development platforms, saved game files use the `.sav` extension and appear in the project's `Saved\SaveGames` folder. On other platforms, particularly consoles, this varies to accommodate the specific file system.

## Loading A Game

To load a saved game, you must provide the save slot name and user ID that you used when you saved it. If the SaveGame you specified exists, the Engine will populate your SaveGame object with the data it contains and return it as a base SaveGame (class `USaveGame`) object. You can then cast that object back to your custom SaveGame class and access the data. Depending on what kind of data your SaveGame type contains, you may want to keep a copy of it, or simply use the data and discard the object.

As with saving, you can load synchronously or asynchronously. If you have a large amount of data, or wish to use a loading screen or animation during load time, we recommend the asychronous method. For small amounts of data that load quickly, a synchronous method exists.

### Asynchronous Loading

When loading asynchronously with `AsyncLoadGameFromSlot`, you must provide a callback delegate in order to receive the data that the system loads.

C++

```
|  |  |
| --- | --- |
|  | // Set up the delegate. |
|  | FAsyncLoadGameFromSlotDelegate LoadedDelegate; |
|  | // USomeUObjectClass::LoadGameDelegateFunction is a void function that takes the following parameters: const FString& SlotName, const int32 UserIndex, USaveGame* LoadedGameData |
|  | LoadedDelegate.BindUObject(SomeUObjectPointer, &USomeUObjectClass::LoadGameDelegateFunction); |
|  | UGameplayStatics::AsyncLoadGameFromSlot(SlotName, 0, LoadedDelegate); |
```

// Set up the delegate.
FAsyncLoadGameFromSlotDelegate LoadedDelegate;
// USomeUObjectClass::LoadGameDelegateFunction is a void function that takes the following parameters: const FString&amp; SlotName, const int32 UserIndex, USaveGame\* LoadedGameData
LoadedDelegate.BindUObject(SomeUObjectPointer, &amp;USomeUObjectClass::LoadGameDelegateFunction);
UGameplayStatics::AsyncLoadGameFromSlot(SlotName, 0, LoadedDelegate);

Copy full snippet(5 lines long)

### Synchronous Loading

The `LoadGameFromSlot` function will create and return a `USaveGame` object if it succeeds.

C++

```
|  |  |
| --- | --- |
|  | // Retrieve and cast the USaveGame object to UMySaveGame. |
|  | if (UMySaveGame* LoadedGame = Cast<UMySaveGame>(UGameplayStatics::LoadGameFromSlot(SlotName, 0))) |
|  | { |
|  | // The operation was successful, so LoadedGame now contains the data we saved earlier. |
|  | UE_LOG(LogTemp, Warning, TEXT("LOADED: %s"), *LoadedGame->PlayerName); |
|  | } |
```

// Retrieve and cast the USaveGame object to UMySaveGame.
if (UMySaveGame\* LoadedGame = Cast&lt;UMySaveGame&gt;(UGameplayStatics::LoadGameFromSlot(SlotName, 0)))
{
// The operation was successful, so LoadedGame now contains the data we saved earlier.
UE\_LOG(LogTemp, Warning, TEXT(&quot;LOADED: %s&quot;), \*LoadedGame-&gt;PlayerName);
}

Copy full snippet(6 lines long)

### Binary Loading

You can load SaveGame data from a file in raw, binary form with `LoadDataFromSlot`. This function is very similar to `LoadGameFromSlot`, except that it does not create a SaveGame object. Only synchronous operation is available for this type of loading.

C++

```
|  |  |
| --- | --- |
|  | TArray<uint8> OutSaveData; |
|  | if (UGameplayStatics::LoadDataFromSlot(OutSaveData, SlotNameString, UserIndexInt32)) |
|  | { |
|  | // The operation succeeded, and OutSaveData now contains a binary represenation of the SaveGame object. |
|  | } |
```

TArray&lt;uint8&gt; OutSaveData;
if (UGameplayStatics::LoadDataFromSlot(OutSaveData, SlotNameString, UserIndexInt32))
{
// The operation succeeded, and OutSaveData now contains a binary represenation of the SaveGame object.
}

Copy full snippet(5 lines long)

You can also convert this binary data to a SaveGame object by calling `LoadGameFromMemory`. This is a synchronous call, and returns a new `USaveGame` object upon success, or a null pointer on failure.

C++

```
|  |  |
| --- | --- |
|  | if (UMySaveGame* SaveGameInstance = Cast<UMySaveGame>(LoadGameFromMemory(InSaveData))) |
|  | { |
|  | // The operation succeeded, and SaveGameInstance was able to cast to type we expected (UMySaveGame). |
|  | } |
```

if (UMySaveGame\* SaveGameInstance = Cast&lt;UMySaveGame&gt;(LoadGameFromMemory(InSaveData)))
{
// The operation succeeded, and SaveGameInstance was able to cast to type we expected (UMySaveGame).
}

Copy full snippet(4 lines long)

* [gameplay](https://dev.epicgames.com/community/search?query=gameplay)
* [programming](https://dev.epicgames.com/community/search?query=programming)
* [save game](https://dev.epicgames.com/community/search?query=save%20game)
* [load game](https://dev.epicgames.com/community/search?query=load%20game)
* [savegame](https://dev.epicgames.com/community/search?query=savegame)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Creating a SaveGame Object](/documentation/en-us/unreal-engine/saving-and-loading-your-game-in-unreal-engine?application_version=5.7#creatingasavegameobject)
* [Header](/documentation/en-us/unreal-engine/saving-and-loading-your-game-in-unreal-engine?application_version=5.7#header)
* [Source](/documentation/en-us/unreal-engine/saving-and-loading-your-game-in-unreal-engine?application_version=5.7#source)
* [Saving A Game](/documentation/en-us/unreal-engine/saving-and-loading-your-game-in-unreal-engine?application_version=5.7#saving-a-game)
* [Asynchronous Saving](/documentation/en-us/unreal-engine/saving-and-loading-your-game-in-unreal-engine?application_version=5.7#asynchronoussaving)
* [Synchronous Saving](/documentation/en-us/unreal-engine/saving-and-loading-your-game-in-unreal-engine?application_version=5.7#synchronoussaving)
* [Binary Saving](/documentation/en-us/unreal-engine/saving-and-loading-your-game-in-unreal-engine?application_version=5.7#binarysaving)
* [Loading A Game](/documentation/en-us/unreal-engine/saving-and-loading-your-game-in-unreal-engine?application_version=5.7#loading-a-game)
* [Asynchronous Loading](/documentation/en-us/unreal-engine/saving-and-loading-your-game-in-unreal-engine?application_version=5.7#asynchronousloading)
* [Synchronous Loading](/documentation/en-us/unreal-engine/saving-and-loading-your-game-in-unreal-engine?application_version=5.7#synchronousloading)
* [Binary Loading](/documentation/en-us/unreal-engine/saving-and-loading-your-game-in-unreal-engine?application_version=5.7#binaryloading)
