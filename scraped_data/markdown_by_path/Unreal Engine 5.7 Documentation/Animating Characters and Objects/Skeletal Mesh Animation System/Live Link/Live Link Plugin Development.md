<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/live-link-plugin-development-in-unreal-engine?application_version=5.7 -->

# Live Link Plugin Development

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
5. [Animating Characters and Objects](/documentation/en-us/unreal-engine/animating-characters-and-objects-in-unreal-engine "Animating Characters and Objects")
6. [Skeletal Mesh Animation System](/documentation/en-us/unreal-engine/skeletal-mesh-animation-system-in-unreal-engine "Skeletal Mesh Animation System")
7. [Live Link](/documentation/en-us/unreal-engine/live-link-in-unreal-engine "Live Link")
8. Live Link Plugin Development

# Live Link Plugin Development

An overview of plugin development and integration with Live Link.

![Live Link Plugin Development](https://dev.epicgames.com/community/api/documentation/image/b3d17519-d70d-46eb-bf6b-8a81e33f8afb?resizing_type=fill&width=1920&height=335)

 On this page

There are two paths for integrating in Live Link:

* Building an Unreal Engine plugin that exposes a new Source to Live Link.

This is the recommended approach for anyone that already has there own streaming protocol.

* Integrating a Message Bus endpoint in third-party software to allow it to act as a data transmitter for the built in Message Bus Source.

This is the approach we have taken for our Maya and Motionbuilder plugins.

If you have more than one Network Adapater in your machine and want to specify which one to recieve data from, you will need to specify the [**Unicast Endpoint**](/documentation/en-us/unreal-engine/live-link-in-unreal-engine#udpmessaging) in your Project Settings.

## Live Link Source

A Live Link source provides animation data to the Live Link client. A source plugin needs to provide the following:

* A Source Factory `Base Class ULiveLinkSourceFactory`

This is how Live Link knows about the sources it can use. The source factory must be a UObject and derive from ULiveLinkSourceFactory. The factory provides functions to create sources and create custom editor UI for source creation. Source factories are automatically picked up by the client (there is no manual registration process).

Your source factory must override the following functions:

* `GetSourceDisplayName` - Returns a localized string for the source name
* `GetSourceTooltip` - Returns a localized string for the source UI tooltip
* `CreateSourceCreationPanel` - Returns a reference to a slate widget to be used to create the source.
* `OnSourceCreationPanelClosed` - Is called when the client is done with the source creation widget. The bCreateSource parameter tells the source factory whether it should use the contents of the UI to create a source or not.
* A Source object (Base Class ILiveLinkSource)

This is the object that manages data transfer into the client from the outside world. A source must derive from ILiveLinkSource. It is created by the source factory and is responsible for passing animation data to the client and managing its data connection lifetime.

Your source must override the following functions:

* `ReceiveClient` - Is called when a source is created
* `IsSourceStillValid`
* `RequestSourceShutdown` - Called to ask the source to close. Usually connection cleanup will happen here. Can return false if more time is needed to clean close the connection

The following are used by the client UI:

* `GetSourceType` - Return localized string representing the source type
* `GetSourceMachineName` - Return string representing source ident (MachineName, IP Address, etc.)
* `GetSourceStatus` - Return a localized string for source status.

## Message Bus source

An example of what is required to create a new source can be found in the editor by looking at the following classes in /Engine/Plugins/Animation/LiveLink/Source/LiveLink:

* `FLiveLinkMessageBusSource`
* `ULiveLinkMessageBusSourceFactory`
* `SLiveLinkMessageBusSourceEditor`

These classes make up the Message Bus Live Link source that is built into the Live Link plugin. The message bus source uses a custom message bus protocol to allow third party apps to transfer animation data to the engine.

### Using the Live Link Message Bus Framework

To make use of the Live Link Message Bus framework (like the Maya and MotionBuilder plugins, the software needs to include the core libraries of Unreal Engine and create a LiveLinkProvider).

```
	TSharedPtr<ILiveLinkProvider> LiveLinkProvider;
	LiveLinkProvider = ILiveLinkProvider::CreateLiveLinkProvider(TEXT("Maya"));

Copy full snippet
```

This automatically handles communication with one or more Unreal Engine instances. All the software then needs to do is use the following two functions to tell the provider about the streamed data:

* `UpdateSubject` - Gives a description of the subject to Live Link (name and joint hierarchy).
* `UpdateSubjectFrame` - Gives a frame of data about the subject to Live Link (current transform, any named float parameters we want to associate and a time/frame number).

An example of this approach can be found in `Engine\Source\Programs\MayaLiveLinkPlugin\`.

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [live link](https://dev.epicgames.com/community/search?query=live%20link)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Live Link Source](/documentation/en-us/unreal-engine/live-link-plugin-development-in-unreal-engine?application_version=5.7#livelinksource)
* [Message Bus source](/documentation/en-us/unreal-engine/live-link-plugin-development-in-unreal-engine?application_version=5.7#messagebussource)
* [Using the Live Link Message Bus Framework](/documentation/en-us/unreal-engine/live-link-plugin-development-in-unreal-engine?application_version=5.7#usingthelivelinkmessagebusframework)
