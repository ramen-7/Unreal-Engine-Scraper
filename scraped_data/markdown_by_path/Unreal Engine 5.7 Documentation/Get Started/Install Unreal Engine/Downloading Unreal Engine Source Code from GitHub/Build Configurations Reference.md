<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/build-configurations-reference-for-unreal-engine?application_version=5.7 -->

# Build Configurations Reference

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
6. [Install Unreal Engine](/documentation/en-us/unreal-engine/install-unreal-engine "Install Unreal Engine")
7. [Downloading Unreal Engine Source Code from GitHub](/documentation/en-us/unreal-engine/downloading-source-code-in-unreal-engine "Downloading Unreal Engine Source Code from GitHub")
8. Build Configurations Reference

# Build Configurations Reference

Reference guide for solution and project build configurations.

![Build Configurations Reference](https://dev.epicgames.com/community/api/documentation/image/4cc1cc43-7570-4412-9db9-499ca0cb7a98?resizing_type=fill&width=1920&height=335)

 On this page

Operating System 

×Windows

Select an option from the dropdown to see content relevant to it.

Google has informed developers of a vulnerability in versions (earlier than M102) of WebRTC. Impacts, workarounds, and updates can be found [here](https://eoshelp.epicgames.com/s/news/eos-news-article-MCVDBTZSVM7VAJHF4ZGJVXZM52I4?language=en_US).

## Build Configuration Descriptions

**Unreal Engine (UE)** uses a custom building method via the **Unreal Build Tool (UBT)**. This tool processes the information necessary to build the engine's reflection system, integrating your C++ code with Blueprints, replication, serialization, and garbage collection.

Every build configuration contains two keywords. The first keyword indicates the state of the engine and your game project. For instance, if you compile using a **Debug** configuration, the build process forgoes optimization making it easer to debug. To be clear, every configuration, even Shipping builds, produce symbols for debugging if built form Visual Studio or if **Project Settings > Project > Packaging > Project > Include Debug Files** is turned on in the Unreal Editor. This means that you can still debug Development and Shipping configurations, they just may not be as easy to debug as the Debug configuration. The second keyword indicates the target you are building for. For example, if you want to open a project in Unreal, you need to build with the **Editor** target keyword.

| Build Configuration - State | Description |
| --- | --- |
| **Debug** | This configuration builds both engine and game code in debug configuration without optimizations. This makes things slower, but is easier to debug. If you compile your project using the **Debug** configuration and want to open the project with the Unreal Editor, you must use the `-debug` flag in order to see your code changes reflected in your project. |
| **DebugGame** | This configuration builds game code without optimizations. This configuration is ideal for debugging only game modules. |
| **Development** | This configuration enables all but the most time-consuming engine and game code optimizations, which makes it ideal for development and performance reasons. Unreal Editor uses the **Development** configuration by default. Compiling your project using the **Development** configuration enables you to see code changes made to your project reflected in the editor. |
| **Shipping** | This is the configuration for optimal performance and shipping your game. This configuration strips out console commands, stats, and profiling tools. |
| **Test** | This configuration is the **Shipping** configuration, but with some console commands, stats, and profiling tools enabled. |

| Build Configuration - Target | Description |
| --- | --- |
| **Game** | This configuration builds a stand-alone executable version of your project, but requires cooked content specific to the platform. Please refer to the  Reference page to learn more about cooked content. |
| **Editor** | To open a project in Unreal Editor and see all code changes reflected, the project must be built in an **Editor** configuration. |
| **Client** | If you are working on a multiplayer project using UE networking features, this target designates the specified project as being a Client in UE's client-server model for multiplayer games. If there is a `<GAME_NAME>Client.Target.cs` file, the **Client** build configurations will be valid. |
| **Server** | If you are working on a multiplayer project using UE networking features, this target designates the specified project as being a Server in UE's client-server model for multiplayer games. If there is a `<GAME_NAME>Server.Target.cs` file, the **Server** build configurations will be valid. |

### Build Configuration for UE Solution

When compiling a UE solution, you are compiling our engine's source code together with your project's source code. The following build configurations are available when building your project this way:

|  | Debug | DebugGame | Development | Shipping | Test |
| --- | --- | --- | --- | --- | --- |
| **Game** | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Editor** | ✓ | ✓ | ✓ |  |  |
| **Client** | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Server** | ✓ | ✓ | ✓ | ✓ | ✓ |

### Build Configuration for UE Project

When compiling a UE project, you are only compiling your project's source code. The following build configurations are available when building your project this way:

|  | Debug | DebugGame | Development | Shipping | Test |
| --- | --- | --- | --- | --- | --- |
| **Game** |  | ✓ | ✓ | ✓ |  |
| **Editor** |  | ✓ | ✓ |  |  |
| **Client** |  |  |  |  |  |
| **Server** |  |  |  |  |  |

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Build Configuration Descriptions](/documentation/en-us/unreal-engine/build-configurations-reference-for-unreal-engine?application_version=5.7#build-configuration-descriptions)
* [Build Configuration for UE Solution](/documentation/en-us/unreal-engine/build-configurations-reference-for-unreal-engine?application_version=5.7#build-configuration-for-ue-solution)
* [Build Configuration for UE Project](/documentation/en-us/unreal-engine/build-configurations-reference-for-unreal-engine?application_version=5.7#build-configuration-for-ue-project)
