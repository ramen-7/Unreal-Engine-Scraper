<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine?application_version=5.7 -->

# Working with Plugins

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
5. [Understanding the Basics](/documentation/en-us/unreal-engine/understanding-the-basics-of-unreal-engine "Understanding the Basics")
6. [Foundational Knowledge](/documentation/en-us/unreal-engine/foundational-knowledge-in--unreal-engine "Foundational Knowledge")
7. Working with Plugins

# Working with Plugins

Installing, enabling, and disabling plugins in Unreal Engine

![Working with Plugins](https://dev.epicgames.com/community/api/documentation/image/1ada575e-9a96-42c6-b127-97fd8bf42d72?resizing_type=fill&width=1920&height=335)

 On this page

A **plugin** is an optional software component that adds specific functionality to **Unreal Engine**. Plugins can add entirely new features and modify built-in functionality without modifying the Unreal Engine code directly. For example, a plugin might add new menu items and toolbar commands to the editor, or even add entirely new features and editor sub-modes.

You can enable or disable plugins independently for each project, depending on your needs.

There are two types of plugins available in Unreal Engine:

* Unreal Engine plugins.
* Third-party plugins.

## Enabling a Plugin

To enable an Unreal Engine plugin, follow these steps:

1. From the main menu, go to **Edit > Plugins**. This opens the **Plugins** window.

   [![Plugins window in Unreal Engine 5](https://dev.epicgames.com/community/api/documentation/image/1d852bde-ec0b-4473-82c0-f99a112213e3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1d852bde-ec0b-4473-82c0-f99a112213e3?resizing_type=fit)

   Plugins window in Unreal Engine 5.
2. Find the plugin you want to enable using the list on the left of the screen. Alternatively, enter a term in the **Search** box to search for all plugin names and descriptions that contain this term.

   [![Searching for a plugin by name](https://dev.epicgames.com/community/api/documentation/image/6a2bdfae-9bd9-4730-9e3f-8ae9e83d5f65?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6a2bdfae-9bd9-4730-9e3f-8ae9e83d5f65?resizing_type=fit)

   This example shows all search results for the term "xr". Note that the search term is highlighted everywhere it appears.
3. To enable a plugin, click the checkbox next to it.

   [![Enabling a plugin.](https://dev.epicgames.com/community/api/documentation/image/aa635320-6d4b-4da7-8101-60144f577d3a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/aa635320-6d4b-4da7-8101-60144f577d3a?resizing_type=fit)

   Enabling a plugin.

   For plugins that are not production-ready, such as beta plugins, you might see a warning asking you to confirm that you want to enable that plugin.
4. Save your work, then restart Unreal Engine.

Third-party plugins might require additional steps before you can enable them. For more information, refer to the documentation for the third-party plugin you want to install. Note that Epic Games is not responsible for the contents of third-party plugins.

## Disabling a Plugin

To disable a plugin, follow these steps:

1. From the main menu, go to **Edit > Plugins**. This opens the **Plugins** window.

   [![Plugins window in Unreal Engine 5](https://dev.epicgames.com/community/api/documentation/image/148d90b9-3a35-43b0-b618-a98cc9149c0b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/148d90b9-3a35-43b0-b618-a98cc9149c0b?resizing_type=fit)

   Plugins window in Unreal Engine 5.
2. Find the plugin you want to disable using the list on the left of the screen. Alternatively, enter a term in the **Search** box to search for all plugin names and descriptions that contain this term.

   [![Searching for a plugin by name](https://dev.epicgames.com/community/api/documentation/image/69f0ee1a-1f25-4c90-86f2-939cecffcf6e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/69f0ee1a-1f25-4c90-86f2-939cecffcf6e?resizing_type=fit)

   This example shows all search results for the term "xr". Note that the search term is highlighted everywhere it appears.
3. To disable a plugin, clear the checkbox next to it.

   [![Disabling a plugin](https://dev.epicgames.com/community/api/documentation/image/2bdb4946-79db-438d-9208-8a709741f5d0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2bdb4946-79db-438d-9208-8a709741f5d0?resizing_type=fit)

   Disabling a plugin.

   If the plugin you want to disable is a *dependency* for other plugins (that is, other plugins require it to function), you will see a notification asking you if you want to disable those plugins as well. Note that this might break existing functionality in your project if you used any of those plugins to implement it.
4. Save your work, then restart Unreal Engine.

## Installing Plugins from Fab

While Unreal Engine contains plugins that offer many different kinds of functionality, you can also install additional plugins from [Fab](https://www.fab.com), using the methods described below. The examples shown here use the free glTF Exporter plugin by Epic Games.

### Downloading Plugins from Fab

You can browse and download plugins for Unreal Engine directly from the Fab site, or from the Fab tab in the Epic Games Launcher.

To download plugins from the site, follow these steps:

1. Do either of the following:

   1. In the **Epic Games Launcher**, navigate to the **Fab** tab.

      [![Fab in Launcher](https://dev.epicgames.com/community/api/documentation/image/75cfcac9-cb88-424d-a283-ab1e85e90f0b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/75cfcac9-cb88-424d-a283-ab1e85e90f0b?resizing_type=fit)
   2. Go to the [Fab website](https://www.fab.com/).

      [![Fab website](https://dev.epicgames.com/community/api/documentation/image/00a5b3eb-33ea-4dc7-bf9b-768ba3e5e57d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/00a5b3eb-33ea-4dc7-bf9b-768ba3e5e57d?resizing_type=fit)
2. Search for the plugin you want to install and click the thumbnail to open the listing.

   [![Searching for a plugin on Fab](https://dev.epicgames.com/community/api/documentation/image/1a729afb-97ba-4ec0-bdb5-9fb7ea10d0f5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1a729afb-97ba-4ec0-bdb5-9fb7ea10d0f5?resizing_type=fit)

The next step depends on whether you selected a [free plugin](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine) or a [paid plugin](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine).

The following information is adapted from the [Acquiring Products section of the Purchasing and Downloading Products](https://dev.epicgames.com/documentation/en-us/fab/purchasing-and-downloading-assets-in-fab#acquire-products) page in the Fab documentation. Refer to that page for more information.

#### Free Plugin

To download a free plugin, follow these steps:

1. On the plugin's listing click **Add to My Library**.

   [![Adding a plugin to your library](https://dev.epicgames.com/community/api/documentation/image/fef73cd2-4de0-4503-9d52-c62da5cf4473?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fef73cd2-4de0-4503-9d52-c62da5cf4473?resizing_type=fit)
2. Accept the Fab EULA.

   [![Accept the Fab EULA](https://dev.epicgames.com/community/api/documentation/image/ee889a03-5f94-455a-a62d-6b0ec74df8f4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ee889a03-5f94-455a-a62d-6b0ec74df8f4?resizing_type=fit)
3. Your free plugin is now available in your Fab library on the Fab site and in the Epic Games launcher.

   [![Plugin saved in my library notification](https://dev.epicgames.com/community/api/documentation/image/eb56f25a-d9f7-47e9-824f-d2143a00d601?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/eb56f25a-d9f7-47e9-824f-d2143a00d601?resizing_type=fit)

#### Paid Plugin

To download a plugin for sale, follow these steps:

1. Click the **Select a License** dropdown to view the available licenses. Select a license type if applicable. This can vary depending on the size of your organization.

   [![Select a license](https://dev.epicgames.com/community/api/documentation/image/9c7fcc72-80a6-458e-9db4-1f6605f39a46?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9c7fcc72-80a6-458e-9db4-1f6605f39a46?resizing_type=fit)
2. Select either **Buy now** or **Add to cart**.

   1. If you select Buy now, you are shown the checkout screen where you can pay for your selected plugin directly. Go to step 4.
   2. If you select Add to cart, your plugin is added to your cart. Continue to step 3.
3. Click **View in cart**, then click the **Checkout** button to pay for your selections once you have all the plugins (and any other Fab products) you want to buy.

   [![Checking out](https://dev.epicgames.com/community/api/documentation/image/c04a53dd-6549-44b7-a332-674c66ea8cd1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c04a53dd-6549-44b7-a332-674c66ea8cd1?resizing_type=fit)
4. Complete the checkout process, and you will see the same notification as for free plugins.

   [![Plugin saved in my library notification](https://dev.epicgames.com/community/api/documentation/image/4d7a4d21-3f00-43f7-949a-3edcdfa9cb3f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4d7a4d21-3f00-43f7-949a-3edcdfa9cb3f?resizing_type=fit)

#### Install your Plugin

After you have added your new plugin to your Fab library, you need to install it to Unreal Engine.

1. Go to the Library tab in the launcher, then scroll down to the Fab Library section. Search for your new plugin, then click **Install to Engine**.

   [![Install to Engine button for a plugin](https://dev.epicgames.com/community/api/documentation/image/41a013c4-12a9-4a92-96f1-f889f4883e7a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/41a013c4-12a9-4a92-96f1-f889f4883e7a?resizing_type=fit)

   If you can't find your new plugin, refresh the Fab Library.

   [![Refresh the Fab Library](https://dev.epicgames.com/community/api/documentation/image/85bae0b2-6cef-4f60-af3c-08952c85d1dd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/85bae0b2-6cef-4f60-af3c-08952c85d1dd?resizing_type=fit)
2. Select the engine version for the plugin installation, then click **Install**.

   [![Selecting an Unreal Engine version](https://dev.epicgames.com/community/api/documentation/image/0f9cfaea-0a29-4076-8852-7737c7902802?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0f9cfaea-0a29-4076-8852-7737c7902802?resizing_type=fit)

   When installing a plugin or other asset, only supported versions of Unreal Engine are available, even if you have other Unreal Engine versions installed.
3. After the installation completes, open the version of Unreal Engine you installed the plugin for, and **enable** the plugin following the instructions in the [Enabling a Plugin](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine) section on this page.

### Downloading Plugins From Fab Inside Unreal Engine

You can download plugins (and other content) using the Fab plugin while you are working inside Unreal Engine. Before you can install additional plugins from Fab, you must first [enable the Fab plugin](https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine).

[![Fab plugin in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/a4a8c237-07e9-4c45-a6ac-e626317c0f57?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a4a8c237-07e9-4c45-a6ac-e626317c0f57?resizing_type=fit)

After you install the plugin, you can access it from the following options in Unreal Engine:

* In the **Windows** menu, scroll down to the **Get Content** section and click **Fab**.

  [![Fab in the Unreal Engine Windows menu](https://dev.epicgames.com/community/api/documentation/image/00a25c83-c9be-449e-b704-e218ad8b0202?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/00a25c83-c9be-449e-b704-e218ad8b0202?resizing_type=fit)
* In the **Content Drawer**, click the **Fab** button right next to the **+Add** button.

  [![Fab in the Content Drawer](https://dev.epicgames.com/community/api/documentation/image/2b8890f5-bd66-4811-861f-9e60e50dc595?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2b8890f5-bd66-4811-861f-9e60e50dc595?resizing_type=fit)

In the Fab window, you can search for and acquire plugins (both free or paid) in the same way as on the Fab site.

[![Fab window in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/7dcaa163-7667-4f37-95c4-21d61ceef71c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7dcaa163-7667-4f37-95c4-21d61ceef71c?resizing_type=fit)

Only plugins usable with Unreal Engine appear in the Fab window inside Unreal Engine. Content for other platforms is not available.

After you add a plugin to your library, you must download and install it to use it. To install your new plugin, quit out of Unreal Engine, and find the plugin in your Fab Library. Click **Install to Engine**, and proceed as previously described above.

[![Install to Engine button for a plugin](https://dev.epicgames.com/community/api/documentation/image/a25335a6-9329-4bd1-b9a9-d202f9d390d0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a25335a6-9329-4bd1-b9a9-d202f9d390d0?resizing_type=fit)

[![Selecting an Unreal Engine version](https://dev.epicgames.com/community/api/documentation/image/e5dd1153-181e-4973-aa85-834858d65895?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e5dd1153-181e-4973-aa85-834858d65895?resizing_type=fit)

## Plugin Installation Locations

Unreal Engine stores all plugins at the following locations:

* `C:\Program Files\Epic Games\UE_[version]\Engine\Plugins` on Windows
* `/Users/Shared/Epic Games/UE_[version]/Engine/Plugins` on macOS

* [plugins](https://dev.epicgames.com/community/search?query=plugins)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Enabling a Plugin](/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine?application_version=5.7#enabling-a-plugin)
* [Disabling a Plugin](/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine?application_version=5.7#disabling-a-plugin)
* [Installing Plugins from Fab](/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine?application_version=5.7#installing-plugins-from-fab)
* [Downloading Plugins from Fab](/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine?application_version=5.7#downloading-plugins-from-the-fab-website)
* [Free Plugin](/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine?application_version=5.7#free-plugin)
* [Paid Plugin](/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine?application_version=5.7#paid-plugin)
* [Install your Plugin](/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine?application_version=5.7#install-your-plugin)
* [Downloading Plugins From Fab Inside Unreal Engine](/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine?application_version=5.7#downloading-plugins-from-fab-inside-unreal-engine)
* [Plugin Installation Locations](/documentation/en-us/unreal-engine/working-with-plugins-in-unreal-engine?application_version=5.7#plugin-installation-locations)
