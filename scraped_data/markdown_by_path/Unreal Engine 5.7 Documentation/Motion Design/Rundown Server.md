<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-rundown-server-for-motion-design-in-unreal-engine?application_version=5.7 -->

# Rundown Server

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
5. [Motion Design](/documentation/en-us/unreal-engine/motion-design-in-unreal-engine "Motion Design")
6. Rundown Server

# Rundown Server

See how the Rundown Server loads the rundown assets and page templates for Motion Design.

![Rundown Server](https://dev.epicgames.com/community/api/documentation/image/bde64ed6-b45a-4c8a-bdb6-2e20c6a32a21?resizing_type=fill&width=1920&height=335)

 On this page

Controlling the Motion Design playout can be accomplished by combining two APIs. The **Rundown Server API** is used to load the rundown assets and the page’s templates, and contains an embedded [Remote Control](https://dev.epicgames.com/documentation/en-us/unreal-engine/remote-control-for-unreal-engine) Preset (RCP).

The RCP for the corresponding page can be accessed and modified via the Remote Control API, then saved back in the rundown page for immediate or later playout.

## Architecture Overview

[![Unreal Editor Rundown and Remote Control API process](https://dev.epicgames.com/community/api/documentation/image/3012258b-3c73-40f0-be5f-24ab2ca2c9a7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3012258b-3c73-40f0-be5f-24ab2ca2c9a7?resizing_type=fit)

## Project Configuration

### 1. Set Up WebSocket Messaging Plugin in Server Mode

The Rundown Server API is exposed to WebSocket through the **WebSocket Messaging** bridge plugin. This plugin allows any internal message bus end points to be exposed through a WebSocket.

It can be enabled in the plugin browser by searching for **web socket**:

[![web socket messaging](https://dev.epicgames.com/community/api/documentation/image/e8ad69e7-9890-4df2-88d8-79f50c7f26d8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e8ad69e7-9890-4df2-88d8-79f50c7f26d8?resizing_type=fit)

Once enabled, the plugin can be configured in **Project Settings > Json**.

[![web socket plugin](https://dev.epicgames.com/community/api/documentation/image/ee9ddfa1-7c95-40b2-824b-d93f796b0b91?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ee9ddfa1-7c95-40b2-824b-d93f796b0b91?resizing_type=fit)

Enter the desired listen port and configure the serialization to JSON.

### 2. Enable Rundown Server

In the Editor settings:

[![Motion Design Rundown settings](https://dev.epicgames.com/community/api/documentation/image/27cec298-fe39-4f48-acb3-4be2cf3f4cc1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/27cec298-fe39-4f48-acb3-4be2cf3f4cc1?resizing_type=fit)

Enable the auto start for the Rundown server on the next editor restart. Leaving the server name blank will use the computer’s name instead.

Alternatively, there is a console command to start the rundown server immediately: "MotionDesignRundownServer.Start [ServerName]". The server name is an optional argument.

Finally, the UE process can be launched with a command line argument: `-MotionDesignRundownServerStart[=ServerName]`.

If the server is running, the console command `MotionDesignRundownServer.Status` should provide some information about the status of the server.

### 3. Set Up Remote Control

Follow the instructions on the [Remote Control API WebSocket Reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/remote-control-api-websocket-reference-for-unreal-engine) page.

[![Remote Control Web Server plugin settings](https://dev.epicgames.com/community/api/documentation/image/c36cf42d-6eb5-40be-982e-65e5cccb604c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c36cf42d-6eb5-40be-982e-65e5cccb604c?resizing_type=fit)

**If using the http server**, it is binding to `localhost` by default, which may not be the adapter you need. To let it bind to any adapter, add the following lines to `DefaultEngine.ini`:

[HTTPServer.Listeners]

DefaultBindAddress=any

## Using WebSocket Messaging

The WebSocket Messaging plugin exposes all messages going through the [UE message bus](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Messaging/IMessageBus?application_version=5.5). Each internal message-bus message is wrapped in a .json message with additional routing information.

Anatomy of the a WebSocket Messaging bridge `message`:

| Field Name | Description |
| --- | --- |
| **`Sender`** | UUID of the sender. This identifies the sending endpoint in the messaging bus. |
| **`Recipients`** | List of UUID of the recipients. If empty, this is equivalent to a `broadcast` to all endpoints listening to the given message type. |
| **`MessageType`** | Corresponds to the UE structure of the message content. |
| **`Expiration`** | Unix time at which the message gets discarded. |
| **`Scope`** | Specifies the scope of propagation of the message (thread, process, network) in the message bus system. For the WebSocket, this is always `Network`. |
| **`Annotations`** | Optional message annotations. |
| **`Message`** | Content of the message. The structure of this content is determined by the `Message Type`. |

Example of a request `GetRundowns` and the response from the server:

| Client request | Server response |
| --- | --- |
| C++  ``` {   "Sender": "F2DCD99C267C4F84B50CF091AA4ED608",   "Recipients": [     "139696A842C8861F52E756BB60AA8661"   ],   "MessageType": "/Script/AvalancheMediaEditor.AvaRundownGetRundowns",   "Expiration": 253402300799,   "Scope": "Network",   "Annotations": {},   "Message": {} ```  Expand code  Copy full snippet(11 lines long) | C++  ``` {   "Sender": "139696A842C8861F52E756BB60AA8661",   "Recipients": [     "F2DCD99C267C4F84B50CF091AA4ED608"   ],   "MessageType": "/Script/AvalancheMediaEditor.AvaRundown**Rundowns**",   "Expiration": 253402300799,   "TimeSent": 1660878367,   "Scope": "Network",   "Annotations": {}, ```  Expand code  Copy full snippet(18 lines long) |

The `message type` specifies the content of `Message`. In API terms, for the client, the `message type` is the command and the content of `Message` is the arguments of the command.

### Message Bus Handshake with Rundown Server

In order to get the UUID of the Rundown server on the message bus, which is then used as `Recipient` for the messages, a WebSocket client must broadcast a `ping` message to the WebSocket and listen for the pong reply to get the UUID of the server. In the message bus, the Rundown server is subscribed to the `AvaRundownPing` message and will reply to its sender with a `AvaRundownPong` message.

| Client request | Server response |
| --- | --- |
| C++  ``` {   "Sender": "F2DCD99C267C4F84B50CF091AA4ED608",   "Recipients": [],   "MessageType": "/Script/AvalancheMediaEditor.AvaRundownPing",   "Expiration": 253402300799,   "Scope": "Network",   "Annotations": {},   "Message":     {         "bAuto": false ```  Expand code  Copy full snippet(12 lines long) | C++  ``` {         "Sender": "**69C67BCB4B61795764D1E596D9F01214**",         "Recipients": [ "F2DCD99C267C4F84B50CF091AA4ED608 ],         "MessageType": "/Script/AvalancheMediaEditor.AvaRundownPong",         "Expiration": 253402300799,         "TimeSent": 1661023146,         "Scope": "Network",         "Annotations": { },         "Message":         { ```  Expand code  Copy full snippet(14 lines long) |

The Pong message `Sender` field is the UUID of the Rundown server’s endpoint in the message bus system. This is then used as the `Recipients` field for all other messages from the Websocket client.

## Rundown Server API

Existing commands and response messages can be found in the source code here:

C++

```
Engine\Plugins\Experimental\Avalanche\Source\AvalancheMediaEditor\Private\Rundown\AvaRundownMessages.h
```

Engine\Plugins\Experimental\Avalanche\Source\AvalancheMediaEditor\Private\Rundown\AvaRundownMessages.h

Copy full snippet(1 line long)

The path of the USTRUCT is the `MessageType` field of the WebSocket message, while the content is serialized in the `Message` field as previously shown.

The JSON serializer uses UStructToJsonObject, which will change the case of field names from the native struct definitions. see StandardizeCase in native code for details. As a general rule, in the JSON format, the first character of the field name will be lowercase. This is only true for JSON format, the concise Binary Object Representation (CBOR) keeps the field name’s case untouched.

### Editing the Page RCP with Remote Control API

[![Remote Control API flowchart](https://dev.epicgames.com/community/api/documentation/image/1ee064c2-13d3-47db-966a-5fc0384a8368?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1ee064c2-13d3-47db-966a-5fc0384a8368?resizing_type=fit)

The `GetPageDetails` is used with `bLoadRemoteControlPreset` set to **true** to inject the page’s RC values into the managed RCP for that asset. The server response will include the following fields:

'remoteControlPresetName': '/Temp/Managed/ESPYS/Blueprint/Avalanche/9021',

'remoteControlPresetId': '984A4E0146010512D839538C0AF265FA',

These can be used with Remote Control API as the `PresetName` field.

The RC values are saved back in the page with the `UpdatePageFromRCP` request.

There is no API to modify the Page RC values directly. Doing that might break the RC controllers so it is not allowed by design. The only path to modify RC values is through the Remote Control API, which runs the controllers and all associated logic.

* [build operations](https://dev.epicgames.com/community/search?query=build%20operations)
* [ddc](https://dev.epicgames.com/community/search?query=ddc)
* [bronze](https://dev.epicgames.com/community/search?query=bronze)
* [motion design](https://dev.epicgames.com/community/search?query=motion%20design)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Architecture Overview](/documentation/en-us/unreal-engine/setting-up-rundown-server-for-motion-design-in-unreal-engine?application_version=5.7#architecture-overview)
* [Project Configuration](/documentation/en-us/unreal-engine/setting-up-rundown-server-for-motion-design-in-unreal-engine?application_version=5.7#project-configuration)
* [1. Set Up WebSocket Messaging Plugin in Server Mode](/documentation/en-us/unreal-engine/setting-up-rundown-server-for-motion-design-in-unreal-engine?application_version=5.7#1-set-up-web-socket-messaging-plugin-in-server-mode)
* [2. Enable Rundown Server](/documentation/en-us/unreal-engine/setting-up-rundown-server-for-motion-design-in-unreal-engine?application_version=5.7#2-enable-rundown-server)
* [3. Set Up Remote Control](/documentation/en-us/unreal-engine/setting-up-rundown-server-for-motion-design-in-unreal-engine?application_version=5.7#3-set-up-remote-control)
* [Using WebSocket Messaging](/documentation/en-us/unreal-engine/setting-up-rundown-server-for-motion-design-in-unreal-engine?application_version=5.7#using-web-socket-messaging)
* [Message Bus Handshake with Rundown Server](/documentation/en-us/unreal-engine/setting-up-rundown-server-for-motion-design-in-unreal-engine?application_version=5.7#message-bus-handshake-with-rundown-server)
* [Rundown Server API](/documentation/en-us/unreal-engine/setting-up-rundown-server-for-motion-design-in-unreal-engine?application_version=5.7#rundown-server-api)
* [Editing the Page RCP with Remote Control API](/documentation/en-us/unreal-engine/setting-up-rundown-server-for-motion-design-in-unreal-engine?application_version=5.7#editing-the-page-rcp-with-remote-control-api)
