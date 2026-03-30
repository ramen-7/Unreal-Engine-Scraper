<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/outliner-in-unreal-engine?application_version=5.7 -->

# Outliner

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
5. [Building Virtual Worlds](/documentation/en-us/unreal-engine/building-virtual-worlds-in-unreal-engine "Building Virtual Worlds")
6. [Level Editor](/documentation/en-us/unreal-engine/level-editor-in-unreal-engine "Level Editor")
7. Outliner

# Outliner

Hierarchical tree view of all Actors within the current Level. Used for selection, attachment, and more.

![Outliner](https://dev.epicgames.com/community/api/documentation/image/d4b9937d-3a48-4aac-b76c-19f2b3f3cf43?resizing_type=fill&width=1920&height=335)

 On this page

The **Outliner** panel displays all the Actors within the scene in a hierarchical tree view. Using the Outliner, you can:

* Select and modify Actors.
* Search and filter Actors by name, type, and other characteristics.
* Use advanced search operators to further refine Actor searches.
* Customize which Actor information to display.

[![Outliner panel in context](https://dev.epicgames.com/community/api/documentation/image/2c9a6d59-17ec-425d-9b67-d96ee338550c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2c9a6d59-17ec-425d-9b67-d96ee338550c?resizing_type=fit)

By default, the Outliner panel docks to the right side of the Unreal Editor window. Click the image for full size.

You can have up to four instances of the Outliner and customize the settings for each instance separately. Switch between Outliner instances by right-clicking the Outliner tab and selecting a different Outliner, or go to **Window > Outliner** from Unreal Engine's main menu.

[![Multiple Outliners](https://dev.epicgames.com/community/api/documentation/image/863b379f-a3f6-461d-9bdf-1842e90f396d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/863b379f-a3f6-461d-9bdf-1842e90f396d?resizing_type=fit)

Switching between different Outliner instances.

## Outliner Actions

You can perform the following actions on an Actor in the Outliner:

| Action | Description |
| --- | --- |
| **Left-click** | Selects that Actor. |
| **Right-click** | Displays the same context menu brought up by right-clicking an Actor in the Viewport. Use this to quickly modify an Actor without having to navigate to that Actor in the Viewport. |
| **Left-click and drag** | Attaches the Actor being Dragged to another Actor. |
| **F** keyboard shortcut | With an Actor selected in the Outliner: Focuses that Actor in the Viewport. With an Actor selected in the Viewport: Scrolls the list of Actors in the Outliner to the selected Actor. |

## Searching and Filtering in the Outliner

Use the **Search** box in the Outliner to search and quickly filter the list of Actors in the scene. By default, searching displays all Actors with a partial match to the search term. If you use more than one search term, only Actors that match all the terms will appear.

You can use all of the [advanced search syntax](https://dev.epicgames.com/documentation/en-us/unreal-engine/advanced-search-syntax-in-unreal-engine) operators when searching in the Outliner.

Some of the most common operators are:

| Operator | Action | Example |
| --- | --- | --- |
| `-` | Excludes Actors that match a specific term. | `-Sky` |
| `+` | Forces a term to match exactly, as opposed to a partial match. | `+Sky` will match `Sky` but exclude `Skylight` |

You can save your search as a **custom filter** and access custom filters from the **Custom Filters** category of the **Filter** drop-down. Custom filters are saved globally for each user, which means they are available across all of the streams and projects of the user who created them.

[![Filters in the Outliner](https://dev.epicgames.com/community/api/documentation/image/08786b23-972a-46c4-91c7-669b8e0b8731?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/08786b23-972a-46c4-91c7-669b8e0b8731?resizing_type=fit)

Filters menu in the Outliner.

**Filtering** Actors in the Outliner works in the same way as [Asset filtering](https://dev.epicgames.com/documentation/en-us/unreal-engine/filters-and-collections-in-unreal-engine) in the Content Browser.

## Customizing the Outliner

**Right-click** any column header to bring up a context menu where you can select which columns to show or hide in the Outliner by enabling or disabling the checkbox next to the column name.

[![Show and hide Outliner columns](https://dev.epicgames.com/community/api/documentation/image/62fac773-fec9-4d5f-a444-481e6078265e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/62fac773-fec9-4d5f-a444-481e6078265e?resizing_type=fit)

Showing and hiding Outliner columns.

Searching matches terms in all columns in the Outliner, whether or not they are visible.

**Left-click and drag** the edge of a column header to resize that column.

The Outliner will always scroll to an Actor when you select that Actor in the Viewport. You can disable this behavior by toggling **Always Frame Selection** from the Outliner's **Settings** menu.

Animated demonstration of the Always Frame Selection option when toggled on or off.

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [building virtual worlds](https://dev.epicgames.com/community/search?query=building%20virtual%20worlds)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Outliner Actions](/documentation/en-us/unreal-engine/outliner-in-unreal-engine?application_version=5.7#outliner-actions)
* [Searching and Filtering in the Outliner](/documentation/en-us/unreal-engine/outliner-in-unreal-engine?application_version=5.7#searching-and-filtering-in-the-outliner)
* [Customizing the Outliner](/documentation/en-us/unreal-engine/outliner-in-unreal-engine?application_version=5.7#customizing-the-outliner)
