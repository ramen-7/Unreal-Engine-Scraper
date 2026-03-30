<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/online-subsystem-types-in-unreal-engine?application_version=5.7 -->

# Online Subsystem Types

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
7. [Online Subsystem](/documentation/en-us/unreal-engine/online-subsystem-in-unreal-engine "Online Subsystem")
8. Online Subsystem Types

# Online Subsystem Types

Description of the major types defined in the online subsystem

![Online Subsystem Types](https://dev.epicgames.com/community/api/documentation/image/6176eace-9082-4fb8-a16a-d8fc7e67bd4c?resizing_type=fill&width=1920&height=335)

 On this page

This document serves to define the different data structures that are used throughout the online subsystem.

### IOnlinePlatformData

**IOnlinePlatformData** is the base class for anything meant to be opaque so that the data can be passed around without consideration for the data it contains.
A human-readable version of the data is available via the **ToString()** function; otherwise, nothing but platform code should try to operate directly on the data.

There are often platform-specific representations of various constructs that, while they need to be handled by the game, do not need their details exposed. This allows the game to hold onto the data and replicate it to other machines without understanding the details.

Classes deriving from IOnlinePlatformData:

* [FUniqueNetId](/documentation/en-us/unreal-engine/online-subsystem-types-in-unreal-engine#funiquenetid)
* [FSharedContentHandle](/documentation/en-us/unreal-engine/online-subsystem-types-in-unreal-engine#fsharedcontenthandle)
* [FSessionInfo](/documentation/en-us/unreal-engine/online-subsystem-types-in-unreal-engine#fsessioninfo)

#### Functions

```
	/**
	 * Get the raw byte representation of this opaque data
	 * This data is platform dependent and shouldn't be manipulated directly
	 * @return byte array of size GetSize()
	 */
	virtual const uint8* GetBytes() const = 0;

	/**
	 * Get the size of the opaque data
	 * @return size in bytes of the data representation
	 */
	virtual int32 GetSize() const = 0;

	/**
	 * Check the validity of the opaque data
	 * @return true if this is well formed data, false otherwise
	 */
	virtual bool IsValid() const = 0;

	/**
	 * Get a human readable representation of the opaque data
	 * Shouldn't be used for anything other than logging/debugging
	 * @return data in string form
	 */
	virtual FString ToString() const = 0;
Copy full snippet
```

### FUniqueNetId

**FUniqueNetId** contains a profile service online ID and can represent anything from an individual player, friend or a session.

### FSharedContentHandle

**FSharedContentHandle** contains a profile service shared file handle. This handle can be passed around and used to access shared content from anywhere, given proper permissions.

### FSessionInfo

**FSessionInfo** contains a session's platform-specific info. In most cases, this would be information such as a session identifier, host address, or other means of identifying and connecting to a created session.

See: [Session Interface](/documentation/en-us/unreal-engine/online-subsystem-session-interface-in-unreal-engine)

### FEmsFile

**FEmsFile** is metadata about a given downloadable file. This structure is used when enumerating available data from a given service.

Contains the following elements:

* Hash - the hash value of the given file contents.
* Filename - the filename as downloaded.
* Logical name - the name that maps to the downloaded filename.
* File size - size of the file.

### FTitleFile

**FTitleFile** is the internal structure that holds the data used in downloading a file asynchronously from the online service.

Contains the following elements:

* Filename - the filename as downloaded.
* Async state - the state of the downloaded file. (see: [Async States](/documentation/en-us/unreal-engine/online-subsystem-types-in-unreal-engine#eonlineasynctaskstate) )
* Data - a buffer containing the file contents.

### EOnlineAsyncTaskState

**EOnlineAsyncTaskState** is a simple enum representing the possible states for an asynchronous operation.

```
		/** The task has not been started */
		NotStarted,
		/** The task is currently being processed */
		InProgress,
		/** The task has completed successfully */
		Done,
		/** The task failed to complete */
		Failed
Copy full snippet
```

* [programming](https://dev.epicgames.com/community/search?query=programming)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [IOnlinePlatformData](/documentation/en-us/unreal-engine/online-subsystem-types-in-unreal-engine?application_version=5.7#ionlineplatformdata)
* [Functions](/documentation/en-us/unreal-engine/online-subsystem-types-in-unreal-engine?application_version=5.7#functions)
* [FUniqueNetId](/documentation/en-us/unreal-engine/online-subsystem-types-in-unreal-engine?application_version=5.7#funiquenetid)
* [FSharedContentHandle](/documentation/en-us/unreal-engine/online-subsystem-types-in-unreal-engine?application_version=5.7#fsharedcontenthandle)
* [FSessionInfo](/documentation/en-us/unreal-engine/online-subsystem-types-in-unreal-engine?application_version=5.7#fsessioninfo)
* [FEmsFile](/documentation/en-us/unreal-engine/online-subsystem-types-in-unreal-engine?application_version=5.7#femsfile)
* [FTitleFile](/documentation/en-us/unreal-engine/online-subsystem-types-in-unreal-engine?application_version=5.7#ftitlefile)
* [EOnlineAsyncTaskState](/documentation/en-us/unreal-engine/online-subsystem-types-in-unreal-engine?application_version=5.7#eonlineasynctaskstate)
