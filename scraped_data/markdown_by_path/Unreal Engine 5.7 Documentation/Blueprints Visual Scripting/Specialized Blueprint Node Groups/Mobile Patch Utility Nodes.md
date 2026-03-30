<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/mobile-patch-utility-nodes-in-unreal-engine?application_version=5.7 -->

# Mobile Patch Utility Nodes

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
7. Mobile Patch Utility Nodes

# Mobile Patch Utility Nodes

Describes the different kinds of Mobile Patch Utility Blueprint nodes.

![Mobile Patch Utility Nodes](https://dev.epicgames.com/community/api/documentation/image/5c586463-bfe2-45c3-90c5-cdb87bcfefbf?resizing_type=fill&width=1920&height=335)

 On this page

After using the  to create a small initial download for your mobile project, you also need to be able to provide the rest of your project in downloadable chunks to the user.
The new Mobile Patch Utilities Blueprint library contains all the functionality required to allow a mobile game to download and install game content and patches from a cloud website instead of being
distributed as part of the initial download from the App Store. There is functionality to determine if updated game content is available, initiate the download, track progress, handle any errors, and
finally install the content paks that are downloaded successfully. Functionality to check for sufficient storage space and WiFi connectivity is also available, so you can warn the user in such cases.
Both Android and iOS are supported.

To show these functions in context with each other, example setups are presented here.
If a function or event in the Blueprint graph examples isn't listed in a table below, then it is a custom node you would need to create in your own project as well.

## Working with Pending Content

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/05fa2b00-da89-465f-8073-33912e4ff196/patching_1.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/05fa2b00-da89-465f-8073-33912e4ff196/patching_1.png)

This is the first stage of the patching process. When patching is initiated, either from a level load or a user action, content needs to be requested from the remote server using the **Request Content** node.
In this example, the install directory is saved off in a variable, but it could also be passed through as function inputs. The **Content To Install** is also saved into a variable for reuse later.
When the content request is complete, different events will be executed depending on whether the request succeeded or failed. Custom events are used as inputs for the **Request Content** function.
The **Check Download Space** function shown here is calling a custom event that starts off the next set of patching logic.

| Node | Description |
| --- | --- |
| Request Content | Attempts to download a manifest file using the specified manifest URL. On success, it will return an object that represents the remote content. This object can be queried for additional information, like total content size, download size, etc. The user can choose to download and install remote content. |

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4ed8c9f8-cf93-49ea-a598-7c6788883323/patching_2.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4ed8c9f8-cf93-49ea-a598-7c6788883323/patching_2.png)

After requesting the remote content succeeds, the next step is to verify that there is enough space for the download using the **Get Required Disk Space** node and comparing the result to the result from **Get Disk Free Space**.
If the required disk space is less than the disk free space, then a custom event is called to start the download.

| Node | Description |
| --- | --- |
| Get Disk Free Space | Gets the disk free space in megabytes where content is installed (or will be installed). |
| Get Required Disk Space | Gets the required disk space in megabytes for this content installation. |

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1d446364-6172-4478-b48f-0569d7dceb8e/patching_3.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1d446364-6172-4478-b48f-0569d7dceb8e/patching_3.png)

Although there is a lot going on in this graph, the only Mobile Patch Utility function is **Start Install**, which attempts to download and install the remote content. Just like **Request Content**, **Start Install** has
event parameters for success and failure. If the install succeeds, the **Mount Content** custom event is used to trigger the final stage of the patching process. Another custom event, **Display Download State** is fired off here
with a timer. Using the timer and the **Update Download State** function, the download state can be shown to the user at regular intervals. More on that logic is in the next Blueprint graph.

| Node | Description |
| --- | --- |
| Start Install | Attempts to download and install remote content. The user can choose to mount the installed content into the game. |

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c3a1c61e-f2e9-4650-854d-bc44a3c8e185/patching_4.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c3a1c61e-f2e9-4650-854d-bc44a3c8e185/patching_4.png)

While the **Display Download State** custom event is connected to a **Format Text** node here, this could also be the stage of the patching process where you fill a progress bar on the UI (User Interface), or other methods of
displaying progress to the user. Here, the outputs of **Get Download Size**, **Get Download Speed**, **Get Download Status Text**, **Get Install Progress**, and **Get Total Downloaded Size** nodes are
combined into a simple text block to present to the user. This script is called at regular intervals with the timer, but does not call back to any of the other example graphs.

| Node | Description |
| --- | --- |
| Get Download Size | Gets the total download size for this content installation. |
| Get Download Speed | Gets the current download speed in megabytes per second. Valid during installation. |
| Get Download Status Text | Gets the current installation status text. Valid during installation. |
| Get Install Progress | Gets the current installation progress. The result is between 0 and 1 for known progress, or less than 0 for unknown progress. |
| Get Total Downloaded Size | Gets the total downloaded size in megabytes. Valid during installation. |

## Working with Installed Content

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/483c3944-4992-4167-9c24-1aff87fa1c56/patching_5.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/483c3944-4992-4167-9c24-1aff87fa1c56/patching_5.png)

The last stage of the patching process is to mount the content. We are using the stored **Install Directory** variable from the first Blueprint graph, but this could again be passed through as a function input.
The **Get Installed Content** node is used to look up the content from that directory, and then the **Mount** function mounts it into the game. Unlike **Request Content** and **Start Install**, **Mount**
does not have success and failure event callbacks.

| Node | Description |
| --- | --- |
| Get Installed Content | Gets the installed content. This will return a non-null object if there is installed content in the specified directory. The user can choose to mount installed content into the game. |
| Mount | Mounts installed content. |

## Other Mobile Patching Functions

The above graphs are a simple example of how to set up patching on a mobile device, but there are other, more complex, behaviors you could set up as well. For example, you could have your game warn users when they don't have
an active WiFi connection, or provide different content for iOS and Android devices. For these use cases and others, the below functions would be useful additions to your Blueprints.

| Node | Description |
| --- | --- |
| Get Active Device Profile Name | Gets the name of the currently selected device profile name. |
| Get Installed Content Size | Gets the installed content size in megabytes |
| Get Supported Platform Names | Gets the list of supported platform names on this device. Example: Android\_ETC2, Android\_ASTC |
| Has Active WiFi Connection | Returns whether or not a WiFi connection is currently available. |

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [blueprint](https://dev.epicgames.com/community/search?query=blueprint)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Working with Pending Content](/documentation/en-us/unreal-engine/mobile-patch-utility-nodes-in-unreal-engine?application_version=5.7#workingwithpendingcontent)
* [Working with Installed Content](/documentation/en-us/unreal-engine/mobile-patch-utility-nodes-in-unreal-engine?application_version=5.7#workingwithinstalledcontent)
* [Other Mobile Patching Functions](/documentation/en-us/unreal-engine/mobile-patch-utility-nodes-in-unreal-engine?application_version=5.7#othermobilepatchingfunctions)

Related documents

[Blueprints Visual Scripting

![Blueprints Visual Scripting](https://dev.epicgames.com/community/api/documentation/image/4e3f56de-8371-4c9d-aa32-4bafe6592648?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine)
