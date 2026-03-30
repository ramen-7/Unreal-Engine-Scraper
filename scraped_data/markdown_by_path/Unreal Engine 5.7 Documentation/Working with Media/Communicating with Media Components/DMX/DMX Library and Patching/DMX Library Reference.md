<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/dmx-library-reference-in-unreal-engine?application_version=5.7 -->

# DMX Library Reference

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
5. [Working with Media](/documentation/en-us/unreal-engine/working-with-media-in-unreal-engine "Working with Media")
6. [Communicating with Media Components](/documentation/en-us/unreal-engine/communicating-with-media-components-from-unreal-engine "Communicating with Media Components")
7. [DMX](/documentation/en-us/unreal-engine/dmx-in-unreal-engine "DMX")
8. [DMX Library and Patching](/documentation/en-us/unreal-engine/create-a-dmx-library-and-add-fixture-patches-in-unreal-engine "DMX Library and Patching")
9. DMX Library Reference

# DMX Library Reference

Describes the DMX library and patching interfaces.

![DMX Library Reference](https://dev.epicgames.com/community/api/documentation/image/0af2f7a6-a41b-47d7-9840-dd97f0de577a?resizing_type=fill&width=1920&height=335)

 On this page

To use the DMX Library asset, you must first [enable the DMX plugins](/documentation/en-us/unreal-engine/dmx-quick-start-in-unreal-engine#enablingthedmxplugins).

The DMX Library asset is the main DMX plugin data structure that holds the following information:

* Controllers
* Fixture Types
* Fixture Patches

The DMX Library asset is under **DMX** > **DMX Library** when navigating the asset creation menu.

When you open a DMX Library from the Content Drawer, a window appears with a navigation bar and three tabs: the Library Settings tab, the Fixture Types tab, and the Fixture Patch tab.

![The navigation bar and the three tabs for a DMX Library.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6a91df24-15fc-4f17-8d41-7ee0ee36f21d/library-top.png)

## Navigation bar

The **Navigation Bar** contains controls for saving, browsing assets, and importing and exporting MVR files.

![The 3 sections of the navigation bar.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5a90716e-7756-4a69-a7a0-437e529d6fcb/navigation-bar.png)

| Number | Name | Description |
| --- | --- | --- |
| 1 | **Save** | Saves changes made to the DMX library. |
| 2 | **Browse** | Opens the **Content Browser** and selects the DMX Library asset. |
| 3 | **Import** and **Export** | These buttons have the following functionality:   * **Import**: Imports a DMX Library from an MVR file. * **Export**: Exports the DMX Library to an MVR file. |

## Library Settings

In the library settings, you can enable or disable input and output ports. To update other DMX port settings, select **Open DMX Project Settings**.

![The library settings.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0b6d2e4e-3586-4429-a88c-0bea3becd9bb/library-settings.png)

## Fixture Types

In the Fixture Types tab, you can create and update Fixture Types, including their modes and functions.

![The six areas of the Fixture Types tab.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/932869b0-4cbe-4b3c-9d9f-f5f23abcbee0/fixture-types.png)

| Number | Name | Description |
| --- | --- | --- |
| 1 | **Fixture Type** list | A list for creating and organizing Fixture Types. |
| 2 | **Fixture Settings** | Fixture settings and imported Fixture data from GDTF. |
| 3 | **Mode** list | A list for creating and organizing Modes. |
| 4 | **Mode Settings** | Properties and settings for the selected Mode. |
| 5 | **Function** list | A list of attributes and functions. |
| 6 | **Function Settings** | Protocol settings for the selected Function, such as bit depth and channel assignment. |

## Fixture Patch

The Fixture Patch tab is divided into the following areas:

![The three areas of the Fixture Patch tab.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0eacd258-1032-4f29-9cf1-3e1ff3d2843e/fixture-patch.png)

| Number | Name | Description |
| --- | --- | --- |
| 1 | **Fixture List** | A list of all Fixture Patches. |
| 2 | **Patcher Tool** | A visual representation of Patch locations per Universe. |
| 3 | **Fixture Patch** panel | Details about the selected Fixture Patch. |

### Fixture List

The Fixture List has the following columns:

![The Fixture List columns.]](fixture-list.png)

* **Fixture Patch**: The name of the Patch.
* **FID**: The Fixture ID. Each fixture should use its own FID.
* **Fixture Type**: The fixture type the Patch is based on.
* **Mode**: The mode of the fixture type the Patch uses.
* **Patch**: The Universe and first channel of the Patch. (For example, 2.1 \* means Universe 2, Channel 1.)

The Fixture List has a context menu with the following options.

![The context menu for the Fixture List.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9770da66-6db7-4d59-b5f3-1e572da9803b/fixture-list-menu.png)

|  |  |
| --- | --- |
| Action | Description |
| **Cut** | Cuts the selected Patch. |
| **Copy** | Copies the selected Patch. |
| **Paste** | Pastes the cut or copied Patch in the first free channel, starting in the select Universe. |
| **Duplicate** | Creates a copy of the selected Patch in the first free channel, starting in the selected Universe. |
| **Auto-assign in selected universe** | Assigns selected Patches to the first free channels, starting in the selected Universe. |

### Patch Window

The Patch Window includes the following options.

![The options for the Patch Window.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c43749a5-8f6d-45fc-86fa-23f3548376f8/patch-window.png)

* **Local Universe**: The currently selected Universe.
* **Show all patches in Universes**: When this option is enabled, the Patcher displays all Patches in the library instead of showing a specific selection.
* **Monitor DMX inputs**: When this option is enabled, the Patcher monitors inbound DMX.

The Patch Window has a context menu with the following options.

![The context menu for the Patch Window.](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bc358936-ecec-47eb-bdde-3e5dad182e06/patch-window-menu.png)

|  |  |
| --- | --- |
| Action | Description |
| **Auto-assign in selected universe** | Assigns a Patch to the first free channels, starting from the selected Universe. |
| **Auto-assign at [Universe.Channel]** | Assigns a Patch to the first free channels, starting from the right-clicked channel. |
| **Assign at [Universe.Channel]** | Assigns a Patch to the right-clicked channel, regardless if the channel range is already occupied. |
| **Align** (multi-selection only) | Aligns all selected Patches one after another. |
| **Stack** (multi-selection only) | Stacks all selected Patches on top of each other. |
| **Spread over Universes** (multi-selection only) | Puts each Patch into its own Universe. |

* [reference](https://dev.epicgames.com/community/search?query=reference)
* [dmx](https://dev.epicgames.com/community/search?query=dmx)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Navigation bar](/documentation/en-us/unreal-engine/dmx-library-reference-in-unreal-engine?application_version=5.7#navigationbar)
* [Library Settings](/documentation/en-us/unreal-engine/dmx-library-reference-in-unreal-engine?application_version=5.7#librarysettings)
* [Fixture Types](/documentation/en-us/unreal-engine/dmx-library-reference-in-unreal-engine?application_version=5.7#fixturetypes)
* [Fixture Patch](/documentation/en-us/unreal-engine/dmx-library-reference-in-unreal-engine?application_version=5.7#fixturepatch)
* [Fixture List](/documentation/en-us/unreal-engine/dmx-library-reference-in-unreal-engine?application_version=5.7#fixturelist)
* [Patch Window](/documentation/en-us/unreal-engine/dmx-library-reference-in-unreal-engine?application_version=5.7#patchwindow)
