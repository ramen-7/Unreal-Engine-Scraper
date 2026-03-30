<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/quixel-bridge-plugin-for-unreal-engine?application_version=5.7 -->

# Quixel Bridge Plugin for Unreal Engine

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
5. [Samples and Tutorials](/documentation/en-us/unreal-engine/samples-and-tutorials-for-unreal-engine "Samples and Tutorials")
6. [Free Epic Games Content](/documentation/en-us/unreal-engine/free-epic-games-content-for-unreal-engine "Free Epic Games Content")
7. Quixel Bridge Plugin for Unreal Engine

# Quixel Bridge Plugin for Unreal Engine

Quixel Bridge lets you access the Megascans library to bring environments, materials, and MetaHumans into Unreal Engine.

![Quixel Bridge Plugin for Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/0ddfe868-9964-4395-9c2c-77ff1fbfd1d9?resizing_type=fill&width=1920&height=335)

Learn to use this **Deprecated** feature, but use caution when shipping with it.

 On this page

## Overview

**Quixel Bridge** plugin for **Unreal Engine** gives you full featured access to the **Megascans** library within the Level Editor. You can browse collections, search for specific assets, and add assets to your Unreal Engine projects.

All of the content accessible through Quixel Bridge is now available from [Fab](https://www.fab.com/), including the Fab tab in the Epic Games Launcher, and through the [Fab window in UE](https://dev.epicgames.com/documentation/en-us/unreal-engine/fab-window-in-unreal-engine?application_version=5.3).

All of the functionality of the Quixel Bridge plugin will remain until the application is taken offline, and you retain the rights to any content you have acquired through Quixel. For more information,
see the Quixel section of the [Purchasing and Downloading Assets in Fab](https://dev.epicgames.com/documentation/en-us/fab/purchasing-and-downloading-assets-in-fab) page.

## Get Bridge for Unreal Engine

Bridge for Unreal Engine is a plugin included with your installation of Unreal Engine 5. To ensure that your Quixel Bridge plugin is enabled, select **Edit > Plugins**. Type **bridge** into the search bar and click the checkbox to enable the plugin.

[![Enable the Quixel Bridge Plugin](https://dev.epicgames.com/community/api/documentation/image/ad65879d-972c-4860-9a59-a3505a860a71?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ad65879d-972c-4860-9a59-a3505a860a71?resizing_type=fit)

Click image for full size.

If you don't see the Quixel Bridge plugin here, then you may need to install it from the **Epic Games Launcher**. Open the Epic Games Launcher, click **Library**, then scroll down to the section called **Vault**. Type **Bridge** into the search bar. Select **Install to Engine**. When you relaunch the engine, you should be able to enable the plugin as described above.

[![Install the Quixel Bridge Plugin from the Epic Games Launcher](https://dev.epicgames.com/community/api/documentation/image/98f90c51-efa3-43ec-b66e-091bcdf826e9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/98f90c51-efa3-43ec-b66e-091bcdf826e9?resizing_type=fit)

Click image for full size.

## Launching Bridge in Unreal Engine

Quixel Bridge can be accessed from a number places inside the editor:

1. Click the **Content** dropdown in the toolbar and select **Quixel Bridge**.

   [![Access Quixel Bridge from the Content Menu](https://dev.epicgames.com/community/api/documentation/image/cdeba9bf-c78d-4c03-a980-deca8913820f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cdeba9bf-c78d-4c03-a980-deca8913820f?resizing_type=fit)

   Click image for full size.
2. From the top menu, select **Window > Quixel Bridge**.

   [![Access Quixel Bridge from the Window menu](https://dev.epicgames.com/community/api/documentation/image/05c70cfd-2f3e-4791-a1b3-e6b1d35c4b59?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/05c70cfd-2f3e-4791-a1b3-e6b1d35c4b59?resizing_type=fit)

   Click image for full size.
3. From the **Content Drawer**, right-click and select **Add Quixel Content**.

[![Access Quixel Bridge from the Content Drawer](https://dev.epicgames.com/community/api/documentation/image/3c73bd6e-91db-4210-8fab-a04d27fc469d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3c73bd6e-91db-4210-8fab-a04d27fc469d?resizing_type=fit)

Click image for full size.

If you can't find Quixel Bridge as directed above, select **Edit > Plugins**. Type **Bridge** in the search bar, and click the checkbox to enable the plugin.

You may be prompted to restart Unreal Engine for the changes to take effect.

[![Enable the Quixel Bridge Plugin](https://dev.epicgames.com/community/api/documentation/image/920c7a97-a492-4bec-8ca9-a08324658d1a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/920c7a97-a492-4bec-8ca9-a08324658d1a?resizing_type=fit)

Click image for full size.

## Updating Bridge

When you launch Unreal Engine, and open the Bridge tab, you may see a message indicating that Bridge is out of date.

[![Notification that Quixel Bridge is Out of Date](https://dev.epicgames.com/community/api/documentation/image/fc951b04-e5e6-41da-9b49-d1641ec4b71f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fc951b04-e5e6-41da-9b49-d1641ec4b71f?resizing_type=fit)

Click image for full size.

To update Bridge, close Unreal Engine and return to the Epic Games Launcher. In the **Unreal Engine > Library** tab, locate the version of Unreal Engine that you have installed. Underneath it, you will see **Installed Plugins**. If a new version of an installed plugin is available, you will see an exclamation mark.

[![Engine Version Installed Plugins](https://dev.epicgames.com/community/api/documentation/image/aa45b689-fa8a-416c-8a83-41bf7103d0b0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/aa45b689-fa8a-416c-8a83-41bf7103d0b0?resizing_type=fit)

Click **Installed Plugins**. From the pop-up window, next to **Quixel Bridge** click **Update**.

[![Update the Quixel Bridge Plugin](https://dev.epicgames.com/community/api/documentation/image/22329281-3bdb-453b-a889-ab3a10256260?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/22329281-3bdb-453b-a889-ab3a10256260?resizing_type=fit)

You can now relaunch Unreal Engine.

## Sign up or Log in to Bridge for Unreal Engine

Bridge for Unreal Engine works with your Epic Games account and currently supports the **Unreal Unlimited** plan.

To log in, click the user icon in the top right corner of the Quixel Bridge panel and select **Sign In**.

[![User Sign In](https://dev.epicgames.com/community/api/documentation/image/ffea5021-c54e-46e7-aa34-9dc912932548?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ffea5021-c54e-46e7-aa34-9dc912932548?resizing_type=fit)

Click image for full size.

You can log in using your existing Epic Games account, or sign up for a new account. To get free, unlimited access to the Megascans library, make sure you're on the Unreal Unlimited plan.

### What is the Unreal Unlimited plan?

Megascans is completely free for all users of Unreal Engine. If you have an Unreal Engine license, sign in with your Epic Games account and go to [quixel.com/pricing](https://quixel.com/pricing) to get unlimited access to the Megascans library. You will also have unlimited downloads within Bridge and Mixer.

This unlimited Megascans access is licensed for use with Unreal Engine and Twinmotion only and treats Megascans assets as UE-Only Content under the Unreal Engine End User License Agreement.

You can find more details on [the Quixel Bridge FAQ page](https://help.quixel.com/hc/en-us/sections/360000977797-Unlimited-Access-for-Unreal-Engine).

## Using Bridge for Unreal Engine

### System requirements

Quixel Bridge for Unreal Engine runs on Windows, MacOS, and Linux.

Bridge requires an active internet connection to display and download the content library. When you do not have an internet connection available, you can access local content that is on disk by navigating to the **Local** tab in the left navigation pane.

### Navigation

On the left of the Quixel Bridge panel, there are buttons to navigate to the different tabs:

* Home
* Collections
* MetaHumans
* Favorites
* Local

#### Home

The **Home** tab is split into sections displaying the latest collections, trending assets, and the newest uploads across every category.

[![Quixel Bridge Home Screen](https://dev.epicgames.com/community/api/documentation/image/530cf9f8-9e11-46ea-a33b-66b5886b7186?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/530cf9f8-9e11-46ea-a33b-66b5886b7186?resizing_type=fit)

Click image for full size.

The left navigation is structured as a category tree with different levels of subcategories.

[![Quixel Bridge Left Navigation](https://dev.epicgames.com/community/api/documentation/image/b7cc16d2-f963-4800-a2eb-b04b8f1dabfc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b7cc16d2-f963-4800-a2eb-b04b8f1dabfc?resizing_type=fit)

Click image for full size.

All the available asset types are listed in the **Home** tab. You can filter by category and subcategories.

Atlases, Displacements, and Brushes are not supported in Bridge for Unreal Engine.

#### Collections

The **Collections** section contains curated content with references and renders across different biomes as well as essentials, architectural selections, tutorial assets and community collections.

[![Quixel Bridge Collections](https://dev.epicgames.com/community/api/documentation/image/5cb72948-b8f8-4f87-8e0b-80bafda019f5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5cb72948-b8f8-4f87-8e0b-80bafda019f5?resizing_type=fit)

Click image for full size.

#### MetaHumans

If you're using the MetaHuman Creator app to create characters, you can access them in Quixel Bridge for Unreal from the My Metahumans tab in the left navigation panel.

[![Quixel Bridge MetaHumans](https://dev.epicgames.com/community/api/documentation/image/29ec7cbb-122a-4b88-b45b-3cd19e0743b6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/29ec7cbb-122a-4b88-b45b-3cd19e0743b6?resizing_type=fit)

Click image for full size.

#### Favorites

Any asset in Quixel Bridge can be marked as a **Favorite** for quick access in the future.

[![Quixel Bridge Favorites](https://dev.epicgames.com/community/api/documentation/image/0996939e-cd2b-468e-8b05-b31761c3dc82?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0996939e-cd2b-468e-8b05-b31761c3dc82?resizing_type=fit)

Click image for full size.

To mark an asset as a favorite, hover over the asset and click the **heart** icon.

#### Local

The **Local** section shows all the assets that you have already downloaded and are available on your machine.

[![Quixel Bridge Local Files](https://dev.epicgames.com/community/api/documentation/image/cd9d00b1-26e8-4cc7-8731-0df8f6f20617?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cd9d00b1-26e8-4cc7-8731-0df8f6f20617?resizing_type=fit)

Click image for full size.

### Search & Filter

The Megascans content library contains thousands of assets and is continuously growing.

To search for an asset or a collection, click in the search bar. As you begin typing, suggested results will appear below the search bar.

[![Quixel Bridge Search](https://dev.epicgames.com/community/api/documentation/image/7d7040f4-4dc1-4d33-a61c-6a8a7ef0d01a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7d7040f4-4dc1-4d33-a61c-6a8a7ef0d01a?resizing_type=fit)

Click image for full size.

If one of the suggested results is the item you need, select it to be taken to that asset. To see all the results for your search query, press **Enter/Return**. The search results will list all of the matching content, including suggestions of popular assets, related collections, and matching asset categories.

Additionally, you can use the filter bar to refine any search result with specific filters such as: asset type, color, biome, state, size, and more. To hide or show the filter bar, click the **Filter** icon in top right.

[![Quixel Bridge Search Filters](https://dev.epicgames.com/community/api/documentation/image/20d6fb28-308e-4be0-a84f-9ba2cf4759f8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/20d6fb28-308e-4be0-a84f-9ba2cf4759f8?resizing_type=fit)

Click image for full size.

### Asset Information

To view more information for an asset, select the asset to open its information panel.

[![Asset Information Panel](https://dev.epicgames.com/community/api/documentation/image/58e5224c-6b5a-47b1-bc44-42db5c4ca065?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/58e5224c-6b5a-47b1-bc44-42db5c4ca065?resizing_type=fit)

Click image for full size.

Icons display information about the asset, for example asset size or whether a surface is tileable or not. You also see related assets that are similar to the current asset.

At the bottom of the asset right panel, choose the download resolution before downloading or adding an asset to your project.

Click the **Export Settings** button to adjust how to import the assets into your scene.

## Download Settings

### Preferences

By default, all the assets you download from Bridge for Unreal Engine are placed at the following location on disk:

* **Win:** `C:\Users\user\Documents\Megascans Library`
* **Mac:** `~\Documents\Megascans Library`
* **Linux:** `~\Documents\Megascans Library`

To change this path, click the user icon in the top right corner of the Bridge window and select **Preferences**.

[![Bridge User Preferences](https://dev.epicgames.com/community/api/documentation/image/efd8173d-b339-4311-9394-89332098d841?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/efd8173d-b339-4311-9394-89332098d841?resizing_type=fit)

Click image for full size.

In the **Preferences** dialog enter the **Library Path** that you want to save your assets to and click **Save**.

[![Quixel Bridge Library Path](https://dev.epicgames.com/community/api/documentation/image/e0c8f6b2-daf5-4cb6-85f8-52164a1f27b2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e0c8f6b2-daf5-4cb6-85f8-52164a1f27b2?resizing_type=fit)

Click image for full size.

### Format & Resolution

Download Settings of assets are available in the asset's information panel.

All 3D assets in Bridge for Unreal Engine are downloaded in UAsset format and are available in the following resolutions:

* Nanite
* High
* Medium
* Low

All other asset types, such as Surfaces, 3D plants, Decals and Imperfections are available in the following resolutions:

* Highest
* High
* Medium
* Low

### Nanite

Bridge for Unreal Engine 5 now serves in a fully Nanite-ready tier for 3D assets. These assets are downloaded as pre-converted Nanite meshes which are loaded into the project upon import.

The assets work right out of the box and do not require any project settings to be configured beforehand.

### Export Settings

Export Settings of assets are available in the asset's information panel. Click the **Export Settings** button to open them.

[![Export Settings Button](https://dev.epicgames.com/community/api/documentation/image/900a5a0e-cfcb-4605-9290-a6dff48d5b7a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/900a5a0e-cfcb-4605-9290-a6dff48d5b7a?resizing_type=fit)

Click image for full size.

The Export Settings dialog allows you to specify parameters to control how the assets will be exported or added into your project. They must be configured before adding an asset into the scene.

[![Export Settings Dialog](https://dev.epicgames.com/community/api/documentation/image/d540e82c-0a68-4706-aa42-90b33deb18c1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d540e82c-0a68-4706-aa42-90b33deb18c1?resizing_type=fit)

Click image for full size.

* **Auto-Populate Foliage Painter**: enabling this will automatically populate foliage editor's asset list in the project with the latest imported assets. This setting must be checked before exporting assets and is only applicable to scatter and plant assets.
* **Apply to Selection**: enabling this will apply the exported material to the selected objects in the scene.
* **Master Material Overrides**: This section lets you choose your own custom master materials instead of the default master materials provided by the plugin.
* **Material Blend Settings**: This section allows you to blend materials using already imported materials in the content browser. The plugin comes with a Vertex Blend Shader which is used for material blending.

## Adding Assets to Your Project

There are a couple of ways to download and add assets to your UE project.

1. Drag and Drop.
2. Download and Add to Scene.

These two methods are described further in the following sections.

### Drag & Drop

You can drag and drop a single asset or multiple assets together into your scene.

To add an asset to your scene, select the asset in the Bridge panel. Drag it into the viewport.

[![Drag Asset Into Viewport](https://dev.epicgames.com/community/api/documentation/image/c7dc9e5f-bd8e-442e-8877-1c3a070b2b8a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c7dc9e5f-bd8e-442e-8877-1c3a070b2b8a?resizing_type=fit)

Click image for full size.

If the asset has not previously been downloaded, this will automatically initiate download. It will download the resolution specified in the asset's information panel.

While the asset is downloading, a preview of the asset will appear in your scene. This preview is a placeholder until the full asset finishes downloading.

If this is the first time you are downloading something in Bridge for Unreal Engine, the following new folders are created in your Content browser.

* **Megascans**: this is where the assets are saved inside your UE project.
* **MSPresets**: this contains all the template master materials that are used to render the downloaded assets in your scene.

Once the final asset has been downloaded, it will replace the preview in the scene.

All surfaces, imperfections, and decals appear on a spherical mesh when dragged and dropped into the viewport.

### Download and Add to Scene

You can also download then add assets to your scene in two separate steps.

#### Download to Project

One way to download an asset is to hover over the asset in the grid, then click the green **Quick Download** button.

[![Hover and Download an Asset](https://dev.epicgames.com/community/api/documentation/image/83a3f340-cae7-4adb-a4c4-9df26b49209d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/83a3f340-cae7-4adb-a4c4-9df26b49209d?resizing_type=fit)

Click image for full size.

Alternatively, select the asset to open the **Asset Information** panel and click **Download**. You can choose at which resolution to download the asset.

[![Download Asset from Information Panel](https://dev.epicgames.com/community/api/documentation/image/acb21aa1-af7e-458c-bf0a-770310487d18?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/acb21aa1-af7e-458c-bf0a-770310487d18?resizing_type=fit)

Click image for full size.

Once downloaded, all assets are accessible from the **Local** tab.

[![Bridge Local Assets](https://dev.epicgames.com/community/api/documentation/image/51fa1eb2-e66a-4829-890b-4720f85306b4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/51fa1eb2-e66a-4829-890b-4720f85306b4?resizing_type=fit)

Click image for full size.

To navigate to the asset's location on disk, right-click the downloaded asset and select **Go to Files**.

[![Right-click and select Go to Files](https://dev.epicgames.com/community/api/documentation/image/15dabd93-b9bf-4f92-9c31-84d4a46ed129?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/15dabd93-b9bf-4f92-9c31-84d4a46ed129?resizing_type=fit)

Click image for full size.

Inside the Editor, the downloaded assets appear in the **Content > Megascans** folder in the **Content Drawer**.

[![Megascans folder in the Content Drawer](https://dev.epicgames.com/community/api/documentation/image/021b9602-5cba-4fec-a371-357043bcdcc5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/021b9602-5cba-4fec-a371-357043bcdcc5?resizing_type=fit)

Click image for full size.

#### Add to Scene

After downloading, there are two ways to add to scene. The first way is to hover over the downloaded asset. Click the blue **Quick Add** button.

[![Hover and click the Quick Add button](https://dev.epicgames.com/community/api/documentation/image/f01bc638-84e8-40bf-a259-bcf4f00fe0b0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f01bc638-84e8-40bf-a259-bcf4f00fe0b0?resizing_type=fit)

Click image for full size.

Alternatively, select the asset to open the asset information panel. Then, click the Add button at the bottom of the panel. You can choose at which resolution to export the asset.

[![Add from the Asset Information panel](https://dev.epicgames.com/community/api/documentation/image/df979577-6932-4612-a4a9-54678edaea98?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/df979577-6932-4612-a4a9-54678edaea98?resizing_type=fit)

Click image for full size.

Make sure you have set up your Export Settings before adding assets to your scene. This will ensure that the assets are downloaded and added at the proper resolution for your project.

## Updating to the latest version

New version updates are available often for Quixel Bridge. These include feature improvements and bug fixes.

To check what version you're using or if an update is available, click the **User** button, then **About Bridge**.

[![Click the User Button and select About Bridge](https://dev.epicgames.com/community/api/documentation/image/8c9db989-5423-4c6e-be8e-845dc4e409c7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8c9db989-5423-4c6e-be8e-845dc4e409c7?resizing_type=fit)

Click image for full size.

A dialog displays information about the current version, and whether an update is available.

[![About Bridge dialog](https://dev.epicgames.com/community/api/documentation/image/f766533f-c194-4c0b-b867-2ffbc35b764e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f766533f-c194-4c0b-b867-2ffbc35b764e?resizing_type=fit)

Click image for full size.

If you've installed Unreal Engine using the **Epic Games Launcher**, you can also make sure you have the latest version installed there. From the **Library** tab, locate the installed engine version you are using. Under it, click **Installed Plugins** to see a list of all plugins you have installed to that engine version. If an update is available, click **Update** to install it.

Live changes to source code are available through GitHub. You can access C++ source code [via GitHub](https://www.unrealengine.com/ue4-on-github).

* [editor](https://dev.epicgames.com/community/search?query=editor)
* [quixel bridge](https://dev.epicgames.com/community/search?query=quixel%20bridge)
* [megascans](https://dev.epicgames.com/community/search?query=megascans)
* [free assets](https://dev.epicgames.com/community/search?query=free%20assets)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Overview](/documentation/en-us/unreal-engine/quixel-bridge-plugin-for-unreal-engine?application_version=5.7#overview)
* [Get Bridge for Unreal Engine](/documentation/en-us/unreal-engine/quixel-bridge-plugin-for-unreal-engine?application_version=5.7#get-bridge-for-unreal-engine)
* [Launching Bridge in Unreal Engine](/documentation/en-us/unreal-engine/quixel-bridge-plugin-for-unreal-engine?application_version=5.7#launching-bridge-in-unreal-engine)
* [Updating Bridge](/documentation/en-us/unreal-engine/quixel-bridge-plugin-for-unreal-engine?application_version=5.7#updating-bridge)
* [Sign up or Log in to Bridge for Unreal Engine](/documentation/en-us/unreal-engine/quixel-bridge-plugin-for-unreal-engine?application_version=5.7#sign-up-or-log-in-to-bridge-for-unreal-engine)
* [What is the Unreal Unlimited plan?](/documentation/en-us/unreal-engine/quixel-bridge-plugin-for-unreal-engine?application_version=5.7#what-is-the-unreal-unlimited-plan)
* [Using Bridge for Unreal Engine](/documentation/en-us/unreal-engine/quixel-bridge-plugin-for-unreal-engine?application_version=5.7#using-bridge-for-unreal-engine)
* [System requirements](/documentation/en-us/unreal-engine/quixel-bridge-plugin-for-unreal-engine?application_version=5.7#system-requirements)
* [Navigation](/documentation/en-us/unreal-engine/quixel-bridge-plugin-for-unreal-engine?application_version=5.7#navigation)
* [Home](/documentation/en-us/unreal-engine/quixel-bridge-plugin-for-unreal-engine?application_version=5.7#home)
* [Collections](/documentation/en-us/unreal-engine/quixel-bridge-plugin-for-unreal-engine?application_version=5.7#collections)
* [MetaHumans](/documentation/en-us/unreal-engine/quixel-bridge-plugin-for-unreal-engine?application_version=5.7#meta-humans)
* [Favorites](/documentation/en-us/unreal-engine/quixel-bridge-plugin-for-unreal-engine?application_version=5.7#favorites)
* [Local](/documentation/en-us/unreal-engine/quixel-bridge-plugin-for-unreal-engine?application_version=5.7#local)
* [Search & Filter](/documentation/en-us/unreal-engine/quixel-bridge-plugin-for-unreal-engine?application_version=5.7#search-filter)
* [Asset Information](/documentation/en-us/unreal-engine/quixel-bridge-plugin-for-unreal-engine?application_version=5.7#asset-information)
* [Download Settings](/documentation/en-us/unreal-engine/quixel-bridge-plugin-for-unreal-engine?application_version=5.7#download-settings)
* [Preferences](/documentation/en-us/unreal-engine/quixel-bridge-plugin-for-unreal-engine?application_version=5.7#preferences)
* [Format & Resolution](/documentation/en-us/unreal-engine/quixel-bridge-plugin-for-unreal-engine?application_version=5.7#format-resolution)
* [Nanite](/documentation/en-us/unreal-engine/quixel-bridge-plugin-for-unreal-engine?application_version=5.7#nanite)
* [Export Settings](/documentation/en-us/unreal-engine/quixel-bridge-plugin-for-unreal-engine?application_version=5.7#export-settings)
* [Adding Assets to Your Project](/documentation/en-us/unreal-engine/quixel-bridge-plugin-for-unreal-engine?application_version=5.7#adding-assets-to-your-project)
* [Drag & Drop](/documentation/en-us/unreal-engine/quixel-bridge-plugin-for-unreal-engine?application_version=5.7#drag-drop)
* [Download and Add to Scene](/documentation/en-us/unreal-engine/quixel-bridge-plugin-for-unreal-engine?application_version=5.7#download-and-add-to-scene)
* [Download to Project](/documentation/en-us/unreal-engine/quixel-bridge-plugin-for-unreal-engine?application_version=5.7#download-to-project)
* [Add to Scene](/documentation/en-us/unreal-engine/quixel-bridge-plugin-for-unreal-engine?application_version=5.7#add-to-scene)
* [Updating to the latest version](/documentation/en-us/unreal-engine/quixel-bridge-plugin-for-unreal-engine?application_version=5.7#updating-to-the-latest-version)
