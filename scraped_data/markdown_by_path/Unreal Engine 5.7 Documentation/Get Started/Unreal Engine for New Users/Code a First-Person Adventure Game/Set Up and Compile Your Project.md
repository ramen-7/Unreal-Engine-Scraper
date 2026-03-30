<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-01-set-up-and-compile-a-cplusplus-project-in-unreal-engine?application_version=5.7 -->

# Set Up and Compile Your Project

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
8. Set Up and Compile Your Project

# Set Up and Compile Your Project

Learn how to set up and compile a new C++ game project from a template.

On this page

## Before You Begin

Ensure you've done the following:

* [Installed Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/install-unreal-engine)  and set up [Visual Studio](https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-visual-studio-development-environment-for-cplusplus-projects-in-unreal-engine?application_version=5.5) for Unreal Engine
* Learned about Projects and Actors and how to navigate Unreal Editor
* Read [Code a First-Person Adventure Game](https://dev.epicgames.com/documentation/en-us/unreal-engine/code-a-firstperson-adventure-game-in-unreal-engine)

## Start From a Template

This tutorial starts you off with a Blueprint-based project containing sample assets. You'll gradually add code that replicates and expands on the existing Blueprint functionality. This way, you can learn to build new classes in a fresh C++ project while also having the equivalent Blueprints available as a reference.

To create a new game project from a template, follow these steps:

1. Open Unreal Engine. In the **Unreal Project Browser**, go to the **Games** project category, and select the **First Person** template.

   [![](https://dev.epicgames.com/community/api/documentation/image/73b65128-97f9-4d0e-9660-bdbc27ab951d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/73b65128-97f9-4d0e-9660-bdbc27ab951d?resizing_type=fit)
2. In the **Project Defaults**, keep the project type set to **Blueprint**. This means Unreal Engine creates a project with Blueprint-type default assets instead of C++ assets.
3. For the **Variant**, select **Arena Shooter**.
4. Name your project. This tutorial uses `AdventureGame` as the project name.
5. Click **Create** to open your new project in the editor.

## Verify Enhanced Input

With the **Enhanced Input system**, you can control character movement by building custom Input Actions that define the actions your character can do, such as jumping or crouching. Each Input Action exists as a data asset that you can reference in code to communicate between your code and your character.

Later in this tutorial, you’ll combine Input Actions and code to enable your character to move and look around.

The Enhanced Input system should already be enabled in your project. To verify this, follow these steps:

1. In Unreal Editor’s main menu, go to the **Edit** menu, and select **Plugins**.
2. Search for **Enhanced Input**. You should see the plugin installed and enabled.

   [![](https://dev.epicgames.com/community/api/documentation/image/05b4ce2b-0bb0-494f-8008-f9ab40d5325e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/05b4ce2b-0bb0-494f-8008-f9ab40d5325e?resizing_type=fit)

To learn more about the Enhanced Input system and Input Actions, see [Enhanced Input](https://dev.epicgames.com/documentation/en-us/unreal-engine/enhanced-input-in-unreal-engine).

## Create a C++ Game Mode Class

Your Blueprint-based project doesn’t have any C++ files or a Visual Studio (VS) project to work with. Next, you'll create your first C++ class, which tells Unreal Engine to generate the Visual Studio project and files you need to get coding.

You'll start with a Game Mode class. **Game Mode** assets define a game's rules, win conditions, and what characters are used. The Game Mode also sets the default gameplay framework classes your project uses, including the Pawn, PlayerController, and HUD. Later in this tutorial, you’ll use your Game Mode to change the default player character.

To create a new Game Mode C++ class, follow these steps:

1. In Unreal Editor’s main menu, go to **Tools > New C++ Class**.
2. In the **Choose Parent Class** window, find and select **Game Mode Base**, and click **Next**.

   [![](https://dev.epicgames.com/community/api/documentation/image/f25d4a94-1509-47ab-b79b-90a88bdeddd1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f25d4a94-1509-47ab-b79b-90a88bdeddd1?resizing_type=fit)

   This means your custom class is derived from the parent `AGameModeBase` class.
3. In the **Name Your New Game Mode Base** step, next to **Class Type**, click **Public**, which places the class header in your game module's Public folder so it can be included by other code.

   Modern Unreal projects use a `Public/Private` module layout to control header visibilty. To avoid include issues and follow current best practices, always select **Public** when creating new C++ class in this tutorial series.
4. Enter a name for the new class, then click **Create Class**. This tutorial uses `AdventureGameMode`.

   [![](https://dev.epicgames.com/community/api/documentation/image/b3473dbe-5429-487b-a954-72245b6d562a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b3473dbe-5429-487b-a954-72245b6d562a?resizing_type=fit)
5. Adding code to your project may take a minute or two. During this process, two warning prompts appear, stating that you’ll need to build or compile your project from VS at least once before the C++ classes appear in the Content Browser. Click **OK**, and then click **Yes** on the second warning to open your code.

## Build Your Project

Before you start adding code, finish preparing your environment by building your project in VS and refreshing Unreal Editor.

### Open the Project in Visual Studio

If the engine didn’t automatically prompt you to open your project in VS after you created the Game Mode class, in Unreal Editor’s main menu, go to **Tools** and select **Open Visual Studio**.

You can also find your project’s `.sln` file in `/Documents/Unreal Projects/[ProjectName]` by default.

Unreal Engine tracks changes you make to your project, like adding new classes, modules, plugins, or modifying build settings. However, the VS project files may not automatically reflect these updates. Use **Refresh Visual Studio Project** (also in the **Tools** menu) to regenerate the solution and project files based on the current project state so everything is up-to-date.

When you open Visual Studio, you'll see your project files organized in the **Solution Explorer**.

[![](https://dev.epicgames.com/community/api/documentation/image/0889e6d1-2a98-4897-89f5-9a08439920c4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0889e6d1-2a98-4897-89f5-9a08439920c4?resizing_type=fit)

When you open your first Unreal Engine C++ project in VS, you might see a warning about missing components in the **Solution Explorer**. Click **Install** to allow VS to install any additional components that may be necessary for your project.

[![](https://dev.epicgames.com/community/api/documentation/image/55a7a504-66a6-44fc-b992-31a946018e96?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/55a7a504-66a6-44fc-b992-31a946018e96?resizing_type=fit)

In the **Solution Explorer**, expand **Games > [*ProjectName*] > Source > [*ProjectName*]**. This is where the main files for your game are located, including two files corresponding to your new Game Mode, `[GameModeName].cpp` and `[GameModeName].h`.

[![](https://dev.epicgames.com/community/api/documentation/image/28254003-0850-4232-ad9a-3feca7532b5c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/28254003-0850-4232-ad9a-3feca7532b5c?resizing_type=fit)

### Build the Project and Refresh Unreal Editor

To make Unreal Editor recognize your code project and include your C++ classes in the Content Browser, build your project from VS and restart the editor.

To build your project so its classes appear in Unreal Editor, follow these steps:

1. In the **Solution Explorer**, under the **Games** folder, right-click your project, and select **Build**.

   [![](https://dev.epicgames.com/community/api/documentation/image/0498c05c-f716-4ee8-8785-4927fd7d841f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0498c05c-f716-4ee8-8785-4927fd7d841f?resizing_type=fit)
2. When the build is complete, go back to Unreal Editor and check if the **Compile**button has appeared in the bottom toolbar and if a new C++ Classes folder has appeared in the Content Browser.

   [![](https://dev.epicgames.com/community/api/documentation/image/5a2bbed7-4c2a-472c-afba-dfb4f2f6e072?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5a2bbed7-4c2a-472c-afba-dfb4f2f6e072?resizing_type=fit)
3. If they haven’t appeared, close the editor and open your project again. Opening the editor recompiles your project, telling UE that your C++ classes exist. If Unreal Engine asks to rebuild your project, click **Yes**.

### Disable Live Coding

Before compiling your code again, turn off **Live Coding** in Unreal Editor. With Live Coding, you can change and rebuild C++ code in implementation (`.cpp`) files while the engine is running; however, it follows a different compilation workflow and may produce errors when editing header (`.h`) files or trying to compile from Visual Studio. Live Coding is useful when iterating on a developed code base, but we recommend disabling it when starting a new project.

To turn off Live Coding, in the editor’s bottom toolbar, click the three dots next to the **Compile** button and disable **Enable Live Coding**.

[![](https://dev.epicgames.com/community/api/documentation/image/651891b3-d23b-4c51-9803-27220f146152?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/651891b3-d23b-4c51-9803-27220f146152?resizing_type=fit)

## Extend a C++ Class to Blueprints

Now that you've made your own custom Game Mode, extend it to Blueprints to expose its properties to the editor, then set that new Blueprint as your project’s default Game Mode.

Extending your Game Mode class to Blueprints exposes class values directly to the editor instead of doing everything through code. The Blueprint acts as a child of the C++ class, inheriting all functionality of the class.

To derive a Blueprint asset from your GameMode class, follow these steps:

1. In the **Content Browser** asset tree, go to **C++ Classes > [*ProjectName*]** **> Public** to find the C++ classes you’ve created.
2. Right-click your **Game Mode Base** class and select **Create Blueprint class based on [*GameModeBaseName*]**.

   [![](https://dev.epicgames.com/community/api/documentation/image/db1b8c6e-bf40-47d9-b0a1-a646905ff32d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/db1b8c6e-bf40-47d9-b0a1-a646905ff32d?resizing_type=fit)
3. In the **Add Blueprint Class** window, name your Blueprint with a `BP_` prefix so you can identify it later. This tutorial uses `BP_AdventureGameMode`.
4. For the **Path**, select **All** > **Content** > **FirstPerson** > **Blueprints,** and click **Create Class**.

   [![](https://dev.epicgames.com/community/api/documentation/image/4ffd1c6f-39c1-43da-a829-cd32cf930018?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4ffd1c6f-39c1-43da-a829-cd32cf930018?resizing_type=fit)

   Unreal Engine automatically opens the Blueprint in a new Blueprint Editor window.
5. In the Game Mode Blueprint's tab, click **Save**.

You can dock the new window within the main editor window by dragging the Blueprint’s tab next to the map tab (**Lvl\_FirstPerson**) in the main editor window.

[![](https://dev.epicgames.com/community/api/documentation/image/72e879e9-d48a-49bf-b967-f03082f5419b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/72e879e9-d48a-49bf-b967-f03082f5419b?resizing_type=fit)

## Change the Project’s Game Mode

By default, new Unreal Engine projects use a sample Game Mode. To change this to your custom Game Mode, edit your project’s settings.

To change the default Game Mode, follow these steps:

1. In the editor’s main menu, go to **Edit > Project Settings**.
2. In the **Project** section in the left panel, select **Maps & Modes**.
3. At the top of the settings table, change the **Default GameMode** to your Game Mode Blueprint.

   [![](https://dev.epicgames.com/community/api/documentation/image/49737a24-0a00-45dd-9141-c65a05bf3e1c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/49737a24-0a00-45dd-9141-c65a05bf3e1c?resizing_type=fit)
4. Close **Project Settings**.
5. Return to the level editor tab. Next to the **Details** panel tab, click the **World Settings** tab. The **World Settings** panel contains settings control how the current level behaves.

   If you can't find the World Settings panel, in the main menu, go to the **Window** menu and ensure **World Settings** has a check mark next to it.
6. In the **Game Mode** section, set **GameMode Override** to your new Game Mode Blueprint (ensure the asset you select has the `BP_` prefix).

   Or, click the arrow icon to remove the override so the level uses the default Game Mode set in the project settings.

   [![](https://dev.epicgames.com/community/api/documentation/image/20f5b7c2-ca49-432a-ae2a-311d9b8a1973?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/20f5b7c2-ca49-432a-ae2a-311d9b8a1973?resizing_type=fit)

   You only need to change the **GameMode Override** for any sample levels. If you create a new, blank level, the **GameMode Override** is set to **None** by default.
7. In the level editor, click **Save**.

## Add an On-Screen Debug Message

A great way to start adding code to your project is by adding a “Hello World!” message on screen.

Add a debug message to verify that you are using your new Game Mode rather than the default Game Mode provided by Unreal Engine. Log messages and debug messages are useful for verifying and debugging code during development.

### Override the Default StartPlay() Function

`AGameModeBase` includes a `StartPlay()` function that UE calls when the game is ready to start gameplay. You'll typically override this function in your custom GameMode classes to add global game start logic. Here, you'll override it to make a debug message appear when the game starts.

To override `StartPlay()` in your custom GameMode class, follow these steps:

1. In VS, open your Game Mode class’ `.h` header file. The code samples in this tutorial use a class named `AdventureGameMode.`

   The default code should look like this:

   C++

   ```
   |  |  |
   | --- | --- |
   |  | UCLASS() |
   |  | class ADVENTUREGAME_API AAdventureGameMode : public AGameModeBase |
   |  | { |
   |  | GENERATED_BODY() |
   |  |  |
   |  | }; |
   ```

   UCLASS()
   class ADVENTUREGAME\_API AAdventureGameMode : public AGameModeBase
   {
   GENERATED\_BODY()
   };

   Copy full snippet(6 lines long)

   `GENERATED_BODY()` is a macro used by Unreal Header Tool that automatically generates code required for this class and other UObjects to work with Unreal Engine. To learn more about Unreal Header Tool, see the [UHT documentation](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-header-tool-for-unreal-engine).

   The `AAdventureGameMode` class exposes different Game Mode states to your code, such as a game starting or ending, entering a map, or a game being in progress. When each state is triggered, it runs an associated function such as `StartPlay()` or `ResetLevel()`.
2. Add an override declaration for the `StartPlay()` function to your `AAdventureGameModeBase` class.

   C++

   ```
   UCLASS()
   class ADVENTUREGAME_API AAdventureGameMode : public AGameModeBase
   {
   	GENERATED_BODY()
           
   	// --- New Code Start --- 

   	virtual void StartPlay() override;

   	// --- New Code End --- 	
   ```

   Expand code  Copy full snippet(11 lines long)

   Place this override after the `GENERATED_BODY()` line.
3. Save the `.h` file.

Unreal Engine classes and functions have prefixes tell the Unreal Header Tool about the class type. For example, an `A` prefix for Actors, `U` for UObjects, and `F` for Structs. To learn more about Unreal Engine C++ Class Prefixes, see [Epic C++ Coding Standards: Naming Conventions](https://dev.epicgames.com/documentation/en-us/unreal-engine/epic-cplusplus-coding-standard-for-unreal-engine).

### Add a Debug Message to StartPlay()

Implement your `StartPlay()` override with some custom code that prints a debug message.

To print a debug message on screen when gameplay starts, follow these steps:

1. Open your Game Mode’s `.cpp` file to implement the function you just declared.
2. Add a new function definition for `StartPlay()`. This function is declared in `AAdventureGameMode`, so define it using `AAdventureGameMode::StartPlay()`.

   C++

   ```
   |  |  |
   | --- | --- |
   |  | void AAdventureGameMode::StartPlay() |
   |  | { |
   |  |  |
   |  | } |
   ```

   void AAdventureGameMode::StartPlay()
   {
   }

   Copy full snippet(4 lines long)

   Place this code after the `#include` line.
3. Inside `AMyGameModeBase::StartPlay()`, add `Super::StartPlay()` to call the `StartPlay()` function from the `AAdventureGameMode` parent class. This is necessary to handle the other logic that should run when the game starts.
4. After `Super::StartPlay()`, add a `check` for `GEngine != nullptr` to ensure the global engine pointer is valid.

   C++

   ```
   void AAdventureGameMode::StartPlay()
   {
   	// --- New Code Start --- 

   	Super::StartPlay();

   	check(GEngine != nullptr);

   	// --- New Code End ---
   ```

   Expand code  Copy full snippet(11 lines long)

   This is a pointer to the UEngine class that Unreal Engine itself uses, and checking that it's valid ensures your game is running properly before your code continues. If the global engine pointer isn’t valid, your game will crash.
5. Use `GEngine` to access UEngine's `AddOnScreenDebugMessage()` member function, which prints a message on-screen when the game is running.

   This function takes four values:

   * A unique int key that identifies the message and prevents the same message from being added multiple times. Use `-1` if the uniqueness doesn’t matter.
   * A float number of seconds to display the message.
   * An `FColor` that sets the text color.
   * An `FString` message to print.

   Calling this function with the following values displays a “Hello World!” message in yellow text on the screen for five seconds when the game begins:

   C++

   ```
   GEngine->AddOnScreenDebugMessage(-1, 5.0f, FColor::Yellow, TEXT("Hello World, this is AdventureGameMode!"));
   ```

   GEngine-&gt;AddOnScreenDebugMessage(-1, 5.0f, FColor::Yellow, TEXT(&quot;Hello World, this is AdventureGameMode!&quot;));

   Copy full snippet(1 line long)

   Place this code after the `check` line.
6. Save the `.cpp` file.

  Now, `AAdventureGameMode::StartPlay()` should look like this:

C++

```
|  |  |
| --- | --- |
|  | #include "AdventureGameMode.h" |
|  |  |
|  | void AAdventureGameMode::StartPlay() |
|  | { |
|  | Super::StartPlay(); |
|  |  |
|  | check(GEngine != nullptr); |
|  |  |
|  | GEngine->AddOnScreenDebugMessage(-1, 5.0f, FColor::Yellow, TEXT("Hello World!")); |
|  | } |
```

#include "AdventureGameMode.h"
void AAdventureGameMode::StartPlay()
{
Super::StartPlay();
check(GEngine != nullptr);
GEngine->AddOnScreenDebugMessage(-1, 5.0f, FColor::Yellow, TEXT("Hello World!"));
}

Copy full snippet(10 lines long)

`UE_LOG` is another helpful function for printing debug messages. Instead of printing a message on-screen, it logs messages to Unreal Engine’s output log or console during runtime. It’s useful for logging or tracking detailed information about what’s happening in your game. You can categorize logs into different channels and define the message type (such as informational, error, or warning messages). For example:  
  
`UE_LOG(LogTemp, Warning, TEXT("This is a warning message!"));`

## Compile and Test Your Code

You can click the **Compile** button in Unreal Editor to rebuild your project; however, we recommend rebuilding from VS. Once compiled, you can see your code changes reflected in the editor and in-game.

To see your changes in game, click **Play** in the main toolbar to start **Play in Editor** (**PIE**) mode. Your debug message appears in the top-left corner.

[![](https://dev.epicgames.com/community/api/documentation/image/bf9d8417-1a6c-4f0c-8190-b3ba349a7b1d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bf9d8417-1a6c-4f0c-8190-b3ba349a7b1d?resizing_type=fit)

[![](https://dev.epicgames.com/community/api/documentation/image/6ab7bb86-c2ab-445e-ad58-58399b633cfd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6ab7bb86-c2ab-445e-ad58-58399b633cfd?resizing_type=fit)

To exit PIE mode, press **Shift + Escape** or click **Stop** in the Level Editor toolbar.

## Next Up

Now that you have a basic project with a new Game Mode, you can start creating your player character! In the next section, you’ll build a new Character class and learn how to use Input Actions to add movement controls to your character.

* [![Create a Player Character With Input Actions](https://dev.epicgames.com/community/api/documentation/image/b7155dfc-b014-4288-ae6d-d4620dc7420d?resizing_type=fit&width=640&height=640)

  Create a Player Character With Input Actions

  Learn how to start building a C++ character with Input Actions.](https://dev.epicgames.com/documentation/en-us/unreal-engine/coder-02-create-a-player-character-with-input-actions-in-cplusplus)

## Complete Code

Here is the complete code built in this section:

C++

AdventureGameMode.h

```
#pragma once

#include "CoreMinimal.h"
#include "GameFramework/GameModeBase.h"
#include "AdventureGameMode.generated.h"

UCLASS()
class ADVENTUREGAME_API AAdventureGameMode : public AGameModeBase
{
	GENERATED_BODY()
```

Expand code  Copy full snippet(13 lines long)

C++

AdventureGameMode.cpp

```
|  |  |
| --- | --- |
|  | #include "AdventureGameMode.h" |
|  |  |
|  | void AAdventureGameMode::StartPlay() |
|  | { |
|  | Super::StartPlay(); |
|  |  |
|  | check(GEngine != nullptr); |
|  |  |
|  | GEngine->AddOnScreenDebugMessage(-1, 5.0f, FColor::Yellow, TEXT("Hello World!")); |
|  | } |
```

#include "AdventureGameMode.h"
void AAdventureGameMode::StartPlay()
{
Super::StartPlay();
check(GEngine != nullptr);
GEngine->AddOnScreenDebugMessage(-1, 5.0f, FColor::Yellow, TEXT("Hello World!"));
}

Copy full snippet(10 lines long)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Before You Begin](/documentation/en-us/unreal-engine/coder-01-set-up-and-compile-a-cplusplus-project-in-unreal-engine?application_version=5.7#beforeyoubegin)
* [Start From a Template](/documentation/en-us/unreal-engine/coder-01-set-up-and-compile-a-cplusplus-project-in-unreal-engine?application_version=5.7#startfromatemplate)
* [Verify Enhanced Input](/documentation/en-us/unreal-engine/coder-01-set-up-and-compile-a-cplusplus-project-in-unreal-engine?application_version=5.7#verifyenhancedinput)
* [Create a C++ Game Mode Class](/documentation/en-us/unreal-engine/coder-01-set-up-and-compile-a-cplusplus-project-in-unreal-engine?application_version=5.7#createac++gamemodeclass)
* [Build Your Project](/documentation/en-us/unreal-engine/coder-01-set-up-and-compile-a-cplusplus-project-in-unreal-engine?application_version=5.7#buildyourproject)
* [Open the Project in Visual Studio](/documentation/en-us/unreal-engine/coder-01-set-up-and-compile-a-cplusplus-project-in-unreal-engine?application_version=5.7#opentheprojectinvisualstudio)
* [Build the Project and Refresh Unreal Editor](/documentation/en-us/unreal-engine/coder-01-set-up-and-compile-a-cplusplus-project-in-unreal-engine?application_version=5.7#buildtheprojectandrefreshunrealeditor)
* [Disable Live Coding](/documentation/en-us/unreal-engine/coder-01-set-up-and-compile-a-cplusplus-project-in-unreal-engine?application_version=5.7#disablelivecoding)
* [Extend a C++ Class to Blueprints](/documentation/en-us/unreal-engine/coder-01-set-up-and-compile-a-cplusplus-project-in-unreal-engine?application_version=5.7#extendac++classtoblueprints)
* [Change the Project’s Game Mode](/documentation/en-us/unreal-engine/coder-01-set-up-and-compile-a-cplusplus-project-in-unreal-engine?application_version=5.7#changetheproject%E2%80%99sgamemode)
* [Add an On-Screen Debug Message](/documentation/en-us/unreal-engine/coder-01-set-up-and-compile-a-cplusplus-project-in-unreal-engine?application_version=5.7#addanon-screendebugmessage)
* [Override the Default StartPlay() Function](/documentation/en-us/unreal-engine/coder-01-set-up-and-compile-a-cplusplus-project-in-unreal-engine?application_version=5.7#overridethedefaultstartplay()function)
* [Add a Debug Message to StartPlay()](/documentation/en-us/unreal-engine/coder-01-set-up-and-compile-a-cplusplus-project-in-unreal-engine?application_version=5.7#addadebugmessagetostartplay())
* [Compile and Test Your Code](/documentation/en-us/unreal-engine/coder-01-set-up-and-compile-a-cplusplus-project-in-unreal-engine?application_version=5.7#compileandtestyourcode)
* [Next Up](/documentation/en-us/unreal-engine/coder-01-set-up-and-compile-a-cplusplus-project-in-unreal-engine?application_version=5.7#nextup)
* [Complete Code](/documentation/en-us/unreal-engine/coder-01-set-up-and-compile-a-cplusplus-project-in-unreal-engine?application_version=5.7#completecode)

Related documents

[Code a First-Person Adventure Game

![Code a First-Person Adventure Game](https://dev.epicgames.com/community/api/documentation/image/ffc1a8f8-e7e5-42c0-b4ed-32ce6d3adbbc?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/code-a-firstperson-adventure-game-in-unreal-engine)

[Create a Player Character With Input Actions

![Create a Player Character With Input Actions](https://dev.epicgames.com/community/api/documentation/image/b7155dfc-b014-4288-ae6d-d4620dc7420d?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/coder-02-create-a-player-character-with-input-actions-in-cplusplus)
