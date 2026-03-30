<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-visual-studio-code-for-unreal-engine?application_version=5.7 -->

# Setting Up VS Code for Unreal Engine

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
6. [Development Setup](/documentation/en-us/unreal-engine/setting-up-your-development-environment-for-cplusplus-in-unreal-engine "Development Setup")
7. Setting Up VS Code for Unreal Engine

# Setting Up VS Code for Unreal Engine

How to set up Visual Studio Code as your IDE for use with Unreal Engine projects.

![Setting Up VS Code for Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/014e42fd-530e-4223-ba81-863764520ad3?resizing_type=fill&width=1920&height=335)

 On this page

While **Unreal Engine (UE)** supports **Microsoft Visual Studio** as its default IDE for C++ projects in Windows, it also supports **Visual Studio Code (VS Code)** as a more lightweight, free, open-source alternative. Although VS Code does not have the same capabilities as Visual Studio out of the box, it is highly extensible, and is available for Windows, MacOS, and Linux, providing a common ground for developers working in multiple platforms.

However, VS Code requires extra manual setup to give it equivalent functionality to Visual Studio for Windows. This guide will walk you through these extra steps so that your VS Code environment is fully equipped for UE development.

You do not need a full Visual Studio installation to use VS Code.

## Required Setup

This guide assumes that you have installed Unreal Engine and created a C++ project with it.

## Installing VS Code and Required Extensions for Your OS

1. Download and install [VS Code](https://code.visualstudio.com/) as well as the official [C/C++ extension pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools-extension-pack) and [C# extension](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csharp) for VS Code. These are required for reading the source code for both Unreal Engine and its **Build Tools**.
2. Download and install the compiler toolset for your OS.

   * **Windows:** The [Microsoft Visual C++ (MSVC) compiler toolset](https://visualstudio.microsoft.com/downloads/).
   * **Mac:** [LLVM/Clang](https://code.visualstudio.com/docs/cpp/config-clang-mac).
   * **Linux:** [LLVM/Clang](/documentation/en-us/unreal-engine/setting-up-visual-studio-code-for-unreal-engine#compilertoolsetforlinux).

For details about how to set up these components, refer to [Installing the Compiler Toolset](/documentation/en-us/unreal-engine/setting-up-visual-studio-code-for-unreal-engine#installingthecompilertoolset).

1. If you are debugging on Mac or Linux, download and install the [LLDB extension](https://marketplace.visualstudio.com/items?itemName=vadimcn.vscode-lldb).
2. If you need to set VS Code as your default IDE, open **Unreal Editor** and go to **Edit** > **Editor Preferences** > **General** > **Source Code**, then set your **Source Code Editor** to **Visual Studio Code**. Restart the editor for the change to take effect. This is not necessary to generate a VS Code solution (see step 5c), but it becomes the default instead of Visual Studio.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/aa3d2498-ec0f-4bc2-a9cf-4116f9171a98/default_ide.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/aa3d2498-ec0f-4bc2-a9cf-4116f9171a98/default_ide.png)

   Click image to enlarge.
3. Generate your VS Code workspace. There are three ways you can do this:

   1. Open **Unreal Editor** and click **Tools** > **Refresh Visual Studio Code Project**.

      ![Refreshing the VS Code Project in Unreal Editor](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/458eeeab-59a3-4996-a706-af59c7126b65/refreshvscode.png)
   2. On Windows and Mac, right-click your project's `.uproject` file and click **Generate Project Files**. When complete, you should see a `.code-workspace` file in your project's folder.

      ![image alt text](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e975fe78-09d3-4d96-9427-5272eaf6d525/code-workspace.png)
   3. In a command line, run `GenerateProjectFiles.bat -vscode`. Adding the `-vscode` parameter will make a `.vscode` workspace instead of a Visual Studio `.sln`. If you use this method, you do not need to change your default source code editor.

## Installing the Compiler Toolset

Each desktop OS uses a different compiler toolset to compile projects in VS Code. The installation process for each one is straightforward, but each requires you to look in a different place to initiate setup.

### Compiler Toolset for Windows

VS Code uses the Microsoft Visual C++ compiler (MSVC) toolset on Windows.

1. Open the [Microsoft Visual Studio Downloads page](https://visualstudio.microsoft.com/downloads/).
2. Scroll down to the **All Downloads** section, then expand **Tools for Visual Studio**.
3. Click the **Download** button next to **Build Tools for Visual Studio 2022** and install it.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/940ebc16-dca2-4052-a280-3afa0bb3515e/download_vs2022_tools.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/940ebc16-dca2-4052-a280-3afa0bb3515e/download_vs2022_tools.png)

   Click image to enlarge.

### Compiler Toolset for MacOS

Unreal Engine uses LLVM/Clang as its compiler toolset on MacOS. Refer to Microsoft's documentation on [Using Clang for Visual Studio Code](https://code.visualstudio.com/docs/cpp/config-clang-mac) for full instructions on how to install and enable it.

### Compiler Toolset for Linux

Unreal Engine uses the LLVM/Clang toolset for Linux. To set it up, follow these steps:

1. Open a Terminal and run the following command:

   ```
        sudo apt install clang
   Copy full snippet
   ```
2. Run `SetupToolchain.sh`. This is located in your Engine's install directory under `Build/BatchFiles/Linux`.
3. Run `GenerateProjectFiles.sh` to build your VS Code workspace.

## Setting Up IntelliSense for VS Code

VS Code can use **IntelliSense** for code hinting, but using it for Unreal Engine requires extra setup steps to expose your project's code to it.

1. In the **Explorer**, open `.vscode/c_cpp_properties.json`.

   ![cpp properties json file](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e195c080-0012-48c4-9d5c-46e8a10ae930/cpp_props_json.png)
2. Add the `includePath` property as follows:

   ```
        "includePath": [ 
            "${workspaceFolder}\\Intermediate\\**", 
            "${workspaceFolder}\\Plugins\\**", 
            "${workspaceFolder}\\Source\\**" 
        ],
   Copy full snippet
   ```

   This exposes these paths in your project to IntelliSense so it can discover your project's code.

   `${workspaceFolder}` is not placeholder text. It is a shortcut indicating your workspace's current directory, which removes the need for absolute paths when editing these files.
3. Open the **Extensions** panel. Click the gear icon for the **C/C++** extension, then click **Extension Settings**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4947f235-745e-41d2-8587-4c3fbb53e51b/extensionsettings.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4947f235-745e-41d2-8587-4c3fbb53e51b/extensionsettings.png)

   Click image to enlarge.
4. Locate the entry for **C\_Cpp: IntelliSense Engine Fallback**. Click the dropdown and set it to **Enabled**.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b07677a4-22b3-4291-819a-8fd022e22ccf/intellisenseenginefallback.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b07677a4-22b3-4291-819a-8fd022e22ccf/intellisenseenginefallback.png)

   Click image to enlarge.
5. Set your **configuration** in the status tray to match the name of your configuration in `c_cpp_properties.json`.
6. You now see a small database icon in the VSCode status tray (blue bar) located in the lower-right side of the VS Code window. Mouse over this icon to see IntelliSense's progress parsing your project.

   ![Database Icon in the status tray](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5458eb95-52c3-4014-8132-bc3fe5cd33e9/dbicon.png)

### Example C/C++ Configurations File

The following is an example of a working `c_cpp_properties.json` file:

```
{
	"configurations": [ 
		{ 
			"name": "CustomGame Editor Win64 Development", 
			"intelliSenseMode": "msvc-x64", 
			"compileCommands": "", 
			"cStandard": "c17",
			"cppStandard": "c++17", 
			"includePath": [ 
				"${workspaceFolder}\\Intermediate\\**", 
				"${workspaceFolder}\\Plugins\\**", 
				"${workspaceFolder}\\Source\\**" 
			],
			"defines": [ 
				"UNICODE", 
				"_UNICODE", 
				"__UNREAL__", 
				"UBT_COMPILED_PLATFORM=Windows", 
				"WITH_ENGINE=1", 
				"WITH_UNREAL_DEVELOPER_TOOLS=1", 
				"WITH_APPLICATION_CORE=1", 
				"WITH_COREUOBJECT=1" 
			] 
		} 
	],
	"version": 
}
Copy full snippet
```

Once you are finished, IntelliSense provides code hinting for your project, including context-sensitive auto-complete functionality.

## Building and Launching Projects in VS Code

Before you can build your project, make sure VS Code is set to the correct **build configuration**, otherwise it will attempt to build and run a standalone or shipping build of your game instead of the editor.

1. Open the **Run and Debug** panel by clicking the play button tab on the left side of the window, or by pressing **CTRL+SHIFT+D**.
2. Click the dropdown next to **RUN AND DEBUG** at the top of the panel. Choose the Development Editor configuration for your project. For example, if your project is named TestGame, you would choose **Launch TestGameEditor (Development) (TestGame)**.

   ![Setting Build Configuration](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c378939e-88c6-4337-b562-56a89c8bd9ff/vscodebuildconfig.png)

   Refer to the [Build Configuration Reference](/documentation/404) page for more information about these options.
3. Click the **Play** button or press **F5** to start building your project in Editor mode. The project compiles, and when it finishes it opens Unreal Editor. Make sure you do not already have Unreal Editor open.

   After you choose your Build Configuration, you can press F5 or click **Run** > **Start Debugging** in the toolbar to build and debug your project regardless of whether you are using the Run and Debug panel.

* [debugging](https://dev.epicgames.com/community/search?query=debugging)
* [programming](https://dev.epicgames.com/community/search?query=programming)
* [ide](https://dev.epicgames.com/community/search?query=ide)
* [linux](https://dev.epicgames.com/community/search?query=linux)
* [vs code](https://dev.epicgames.com/community/search?query=vs%20code)
* [visual studio code](https://dev.epicgames.com/community/search?query=visual%20studio%20code)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Required Setup](/documentation/en-us/unreal-engine/setting-up-visual-studio-code-for-unreal-engine?application_version=5.7#requiredsetup)
* [Installing VS Code and Required Extensions for Your OS](/documentation/en-us/unreal-engine/setting-up-visual-studio-code-for-unreal-engine?application_version=5.7#installingvscodeandrequiredextensionsforyouros)
* [Installing the Compiler Toolset](/documentation/en-us/unreal-engine/setting-up-visual-studio-code-for-unreal-engine?application_version=5.7#installingthecompilertoolset)
* [Compiler Toolset for Windows](/documentation/en-us/unreal-engine/setting-up-visual-studio-code-for-unreal-engine?application_version=5.7#compilertoolsetforwindows)
* [Compiler Toolset for MacOS](/documentation/en-us/unreal-engine/setting-up-visual-studio-code-for-unreal-engine?application_version=5.7#compilertoolsetformacos)
* [Compiler Toolset for Linux](/documentation/en-us/unreal-engine/setting-up-visual-studio-code-for-unreal-engine?application_version=5.7#compilertoolsetforlinux)
* [Setting Up IntelliSense for VS Code](/documentation/en-us/unreal-engine/setting-up-visual-studio-code-for-unreal-engine?application_version=5.7#settingupintellisenseforvscode)
* [Example C/C++ Configurations File](/documentation/en-us/unreal-engine/setting-up-visual-studio-code-for-unreal-engine?application_version=5.7#examplec/c++configurationsfile)
* [Building and Launching Projects in VS Code](/documentation/en-us/unreal-engine/setting-up-visual-studio-code-for-unreal-engine?application_version=5.7#buildingandlaunchingprojectsinvscode)
