<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/title-file-interface-in-unreal-engine?application_version=5.7 -->

# Title File Interface

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
5. [Gameplay Systems](/documentation/en-us/unreal-engine/gameplay-systems-in-unreal-engine "Gameplay Systems")
6. [Online Subsystems and Services](/documentation/en-us/unreal-engine/online-subsystems-and-services-in-unreal-engine "Online Subsystems and Services")
7. [Online Services](/documentation/en-us/unreal-engine/online-services-in-unreal-engine "Online Services")
8. [Online Services Interfaces](/documentation/en-us/unreal-engine/online-services-interfaces-in-unreal-engine "Online Services Interfaces")
9. Title File Interface

# Title File Interface

Read title files from the backend online services.

![Title File Interface](https://dev.epicgames.com/community/api/documentation/image/bc6ee875-844e-4247-bec8-36ddd6ffc68e?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

The **Online Services Title File Interface** provides support for your game to read files from your platform's backend online services at runtime.

Your game might require reading files not packaged with your title. The title file interface provides you with tools to read files that you have uploaded to backend online services. Examples of such information might include configuration files or a message of the day. This interface helps you to access and download these files for use at runtime.

For player-specific file storage, see the [User File Interface](https://dev.epicgames.com/documentation/en-us/unreal-engine/user-file-interface-in-unreal-engine?application_version=5.5).

## API Overview

### Functions

The following table provides a high-level overview of the functions provided by the Title File Interface:

| Function | Description |
| --- | --- |
| [EnumerateFiles](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/ITitleFile/EnumerateFiles?application_version=5.5) | Enumerate all available files. |
| [GetEnumeratedFiles](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/ITitleFile/GetEnumeratedFiles?application_version=5.5) | Retrieve a cached list of files enumerated by a call to `EnumerateFiles`. |
| [ReadFile](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/ITitleFile/ReadFile?application_version=5.5) | Read a file and return its contents. |

## Process Flow

To read a file from the backend online services with the Title File Interface, follow these steps:

1. `EnumerateFiles` asynchronously caches a list of all files available to retrieve from the online services with the interface.
2. `GetEnumeratedFiles` retrieves the list of files cached with the interface by `EnumerateFiles`.
3. For each file in the retrieved list, `ReadFile` reads the file asynchronously and returns its contents for use in your game.

## More Information

### Header File

Consult the `TitleFile.h` header file directly for more information as needed. The Title File Interface header file `TitleFile.h` is located in the directory:

C++

```
Engine\Plugins\Online\OnlineServices\Source\OnlineServicesInterface\Public\Online
```

Engine\Plugins\Online\OnlineServices\Source\OnlineServicesInterface\Public\Online

Copy full snippet(1 line long)

For instructions on how to obtain the UE source code, see our documentation on [Downloading Unreal Engine Source Code](https://dev.epicgames.com/documentation/en-us/unreal-engine/downloading-source-code-in-unreal-engine).

### Function Parameters and Return Types

See the [Functions](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-online-services-in-unreal-engine?application_version=5.5#functions) section of the Online Services Overview page for an explanation of function parameters and return types, including how to pass parameters and processing the results when functions return.

* [beta](https://dev.epicgames.com/community/search?query=beta)
* [programming](https://dev.epicgames.com/community/search?query=programming)
* [online services](https://dev.epicgames.com/community/search?query=online%20services)
* [title](https://dev.epicgames.com/community/search?query=title)
* [file](https://dev.epicgames.com/community/search?query=file)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [API Overview](/documentation/en-us/unreal-engine/title-file-interface-in-unreal-engine?application_version=5.7#api-overview)
* [Functions](/documentation/en-us/unreal-engine/title-file-interface-in-unreal-engine?application_version=5.7#functions)
* [Process Flow](/documentation/en-us/unreal-engine/title-file-interface-in-unreal-engine?application_version=5.7#process-flow)
* [More Information](/documentation/en-us/unreal-engine/title-file-interface-in-unreal-engine?application_version=5.7#more-information)
* [Header File](/documentation/en-us/unreal-engine/title-file-interface-in-unreal-engine?application_version=5.7#header-file)
* [Function Parameters and Return Types](/documentation/en-us/unreal-engine/title-file-interface-in-unreal-engine?application_version=5.7#function-parameters-and-return-types)
