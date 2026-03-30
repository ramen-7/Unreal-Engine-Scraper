<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/user-file-interface-in-unreal-engine?application_version=5.7 -->

# User File Interface

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
9. User File Interface

# User File Interface

Read user files from the backend online services.

![User File Interface](https://dev.epicgames.com/community/api/documentation/image/9069ed49-206c-4b5a-95d4-a59032736a14?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

The **Online Services User File Interface** provides support for your game to read user-specific files from your platform's backend online services at runtime.

Your game might require you to read user files that are not packaged with your title. Examples may include configuration files or user-specific game save files. This interface helps you to access and download these files for use at runtime.

For title-specific file storage, see the [Title File Interface](https://dev.epicgames.com/documentation/en-us/unreal-engine/title-file-interface-in-unreal-engine?application_version=5.5).

## API Overview

### Functions

The following table provides a high-level overview of the functions provided by the User File Interface:

| Function | Description |
| --- | --- |
| [EnumerateFiles](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IUserFile/EnumerateFiles?application_version=5.5) | Enumerate all available files. |
| [GetEnumeratedFiles](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IUserFile/GetEnumeratedFiles?application_version=5.5) | Retrieve a cached list of files enumerated by a call to `EnumerateFiles`. |
| [ReadFile](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IUserFile/ReadFile?application_version=5.5) | Read a file and return its contents. |
| [WriteFile](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IUserFile/WriteFile?application_version=5.5) | Write the file contents to a file with the provided name. |
| [CopyFile](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IUserFile/CopyFile?application_version=5.5) | Copy the file contents to another file. |
| [DeleteFile](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/OnlineServicesInterface/Online/IUserFile/DeleteFile?application_version=5.5) | Delete a file. |

## Process Flow for Reading Files

To read, copy, or delete a file from the backend online services with the User File Interface, follow these steps:

1. `EnumerateFiles` caches a list of all files available to retrieve from the online services with the interface.
2. `GetEnumeratedFiles` retrieves the list of files cached with the interface by `EnumerateFiles`.
3. For each file in the retrieved list, `ReadFile` reads the file and returns its contents.

## Modifying Files

The User File Interface also supports operations for modifying files:

* `WriteFile` creates new files or overwrites existing ones.
* `CopyFile` copies the contents of a user file to a different user file.
* `DeleteFile` deletes the user file with the provided name from the backend online services.

## More Information

### Header File

Consult the `UserFile.h` header file directly for more information as needed. The User File Interface header file `UserFile.h` is located in the directory:

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
* [file](https://dev.epicgames.com/community/search?query=file)
* [user](https://dev.epicgames.com/community/search?query=user)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [API Overview](/documentation/en-us/unreal-engine/user-file-interface-in-unreal-engine?application_version=5.7#api-overview)
* [Functions](/documentation/en-us/unreal-engine/user-file-interface-in-unreal-engine?application_version=5.7#functions)
* [Process Flow for Reading Files](/documentation/en-us/unreal-engine/user-file-interface-in-unreal-engine?application_version=5.7#process-flow-for-reading-files)
* [Modifying Files](/documentation/en-us/unreal-engine/user-file-interface-in-unreal-engine?application_version=5.7#modifying-files)
* [More Information](/documentation/en-us/unreal-engine/user-file-interface-in-unreal-engine?application_version=5.7#more-information)
* [Header File](/documentation/en-us/unreal-engine/user-file-interface-in-unreal-engine?application_version=5.7#header-file)
* [Function Parameters and Return Types](/documentation/en-us/unreal-engine/user-file-interface-in-unreal-engine?application_version=5.7#function-parameters-and-return-types)
