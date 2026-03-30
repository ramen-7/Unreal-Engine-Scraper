<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/day-sequence-time-of-day-plugin-for-unreal-engine?application_version=5.7 -->

# Setting Up A Time Of Day With Day Sequence

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
6. [Lighting the Environment](/documentation/en-us/unreal-engine/lighting-the-environment-in-unreal-engine "Lighting the Environment")
7. [Lighting Tools and Plugins](/documentation/en-us/unreal-engine/lighting-tools-and-plugins-in-unreal-engine "Lighting Tools and Plugins")
8. Setting Up A Time Of Day With Day Sequence

# Setting Up A Time Of Day With Day Sequence

A plugin to implement a time of day system with preconfigured or fully customizable components.

![Setting Up A Time Of Day With Day Sequence](https://dev.epicgames.com/community/api/documentation/image/d83b8ca9-eb1c-4520-aac2-5924f25d58de?resizing_type=fill&width=1920&height=335)

Learn to use this **Experimental** feature, but use caution when shipping with it.

 On this page

The **Day Sequence** plugin is a collection of actors and assets you can use and create to automatically generate a 24-hour day cycle. These components make it simpler to set up a time of day system while having more artistic control over sun, moon, stars, atmosphere, and clouds from within Sequenc[er’s](https://dev.epicgames.com/documentation/en-us/unreal-engine/cinematics-and-movie-making-in-unreal-engine) tools. Day Sequences make it easier to reuse and share assets over bespoke day cycle implementation using Blueprint, keyframe structs, and custom triggers.

Day Sequences are designed with modularity, compatibility, and versatility in mind with their emphasis being on reuse and recombination of assets, integration into existing projects, and its overall usefulness across multiple industries and varying team sizes. Day Sequences also handle network synchronization for multiplayer games, point of interest creation using volumes to override other day sequences, and data-oriented approaches to lighting with procedural sequence creation.

## Enabling Day Sequence in a Project

To start using the Day Sequence time of day actor in your scene, you must first enable the **Day Sequence** plugin for your project. You can find it in the **Plugins** browser located in the **Edit** menu.

[![](https://dev.epicgames.com/community/api/documentation/image/fb60c21e-bf16-4246-8719-632da697f42d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fb60c21e-bf16-4246-8719-632da697f42d?resizing_type=fit)

## Setting Up a Day Sequence

The Day Sequence plugin includes all the components necessary to set up a time of day system from scratch, including a preconfigured time of day cycle you can drag and drop into your level.

There are several primary ways you can configure a time of day cycle:

* Editing Day Sequence Actors by adding and removing hand-crafted Day Sequence Collection assets.
* Creating a Day Sequence Actor to customize the set of lighting components, and their parameters, like how long a day is, intervals at which time progresses, and more.
* Customize a Day Sequence Actor with a set of lighting components and parameters, such as specifying how long a day is, the time intervals between updates, and more.

You can use the sections below to explore the different ways you can set up and use Day Sequences to create a time of day system. They are listed in order from simplest to advance in how complex they are to set up and use.

### Setting Up a Preconfigured Time of Day System

The **Sun Moon Day Sequence Actor** is a preconfigured complete day and night cycle that you can drag-and-drop into your level. It requires no additional setup to have a fully functioning time of day system, and it is built using the same components and assets used in later sections of this page to build a custom time of day system.

Follow these steps to get started:

1. Create a new blank level, or open an existing level. If you already have environment lighting components — Directional lights, Sky Light, Sky Atmosphere, and Volumetric Clouds — in your level, these should be removed.
2. From the main toolbar of the level editor, click **Create** and drag a **Sun Moon Day Sequence Actor** into the scene from the **All** rollout category.

   [![](https://dev.epicgames.com/community/api/documentation/image/1f04c870-3805-4400-9cc6-718d1985c8eb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1f04c870-3805-4400-9cc6-718d1985c8eb?resizing_type=fit)

You will see a fully lit environment with sun, atmosphere, and clouds once the **Sun Moon Day Sequence Actor** is placed in the level. The Day Sequence Actor’s presence also includes a new viewport toolbar called **Time of Day**. You can use the **Time** slider in this menu to manually scrub through the current time of day to move the sun’s position in the editor.

To learn more about the Day Sequence Actor’s settings and how you can configure them for your project, see the [Day Sequence Actor](https://dev.epicgames.com/documentation/en-us/unreal-engine/day-sequence-time-of-day-plugin-for-unreal-engine) section of this page.

### Setting up a Simplified Time of Day System

The **Base Day Sequence Actor** is useful for creating a simplified time of day system as a starting point. Similar to the Sun Moon Day Sequence Actor, this actor includes necessary lighting components, but requires you to set up the other assets to allow for customization to fit the needs of your project.

The two primary elements you’ll use to build a simplified time of day system are the **Base Day Sequence Actor** and a **Day Sequence Collection Asset**. The Base Day Sequence Actor is a Day Sequence Actor that includes a set of lighting components. The Day Sequence Collection is an asset used to set a Day Sequence Asset, which specifies how the sun moves across the sky.

Follow these steps to get started:

1. Use the **Create** menu to add a **Base Day Sequence Actor** to your level.

   [![](https://dev.epicgames.com/community/api/documentation/image/d9474487-db58-488c-8215-a78d85125637?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d9474487-db58-488c-8215-a78d85125637?resizing_type=fit)
2. In the **Content Browser**, create a new **Day Sequence Collection** asset.
3. Open your **Day Sequence Collection** asset.
4. Under the “Day Sequence” section, click **add (+)** to create a new entry, and expand its properties.
5. In the **Sequence** slot, assign the **DS\_24hr** Day Sequence asset provided by the Day Sequence plugin.

   If you prefer, you can create your own Day Sequence asset to have something more custom for your project, but for this setup, we’d recommend you use this one when first building a time of day system.
6. Under the “Procedural Day Sequences” section, click **add (+)** to create a new entry. Next to **Index[0]**, use the dropdown to select **Sun Position Sequence**.
7. **Save** and **Close** the Day Sequence Collection.
8. Return to the level and select your **Base Day Sequence Actor** in the Outliner. Then, navigate to its **Details** panel.
9. Locate the **Day Sequence Collection** assignment slot under the “Sequence” category. Assign your **Day Sequence Collection**.

Once complete, you should see a scene lit by a sun with atmosphere and clouds — all things needed for a time of day cycle. If the Day Sequence asset is set up correctly in the Day Sequence Collection, the **Time** slider in the level viewport’s **Time of Day** menu can be used to scrub through the time of day to move the sun’s position in the sky. Alternatively, when you use PIE, the time of day automatically moves according to the default settings of the Day Sequence Actor.

### Setting Up a Custom Time of Day System

You can use the **Day Sequence Actor** to build a time of day system from scratch. This is a generic actor that has no default lighting components, like the Sun Moon Day Sequence Actor and Base Day Sequence Actor have.

Creating a time of day system from scratch using the Day Sequence Actor can provide the most flexibility and customization to your project.

Follow these steps to start building a time of day system from scratch:

1. In the **Content Browser**, click **Add (+)** and select **Blueprint Class**.
2. In the **Pick Parent Class** window that pops up, use the search field under **All Classes** to select **DaySequenceActor** as the class.
3. In the Content Browser, give the Blueprint a name.
4. Open the Day Sequence Blueprint.
5. In the **Components** panel, add any environment lighting components needed for your time of day system. You will be able to preview this in the Blueprint viewport window.

   [![](https://dev.epicgames.com/community/api/documentation/image/e27ea3b3-084c-4a22-8d80-bebde5686746?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e27ea3b3-084c-4a22-8d80-bebde5686746?resizing_type=fit)

   This can include components such as:

   * Two Directional Lights (for the Sun and Moon)
   * Sky Atmosphere
   * Volumetric Clouds
   * Sky Light
   * Exponential Height Fog
   * Post Process Volumes
6. In the **Event Graph**, you’ll add logic that registers the Day Sequence Actor with the **Day Sequence Subsystem**. This enables the Day Sequence Actor for editor preview. You’ll set this up by calling Day Sequence Subsystem > Set Day Sequence Actor (this) on Construction and BeginPlay.

   [![](https://dev.epicgames.com/community/api/documentation/image/a3252a17-a795-446e-87ad-4083845190a9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a3252a17-a795-446e-87ad-4083845190a9?resizing_type=fit)
7. In the **Content Browser**, create a **Day Sequence Collection** asset and a **Day Sequence** asset.
8. Open the **Day Sequence Collection** asset.
9. Click the **Add (+)** icon next to **Day Sequence** and expand the **Index [0]** settings.
10. Assign the **Day Sequence** asset you created in the previous step to the **Sequence** assignment slot.
11. Save and close the **Day Sequence Collection**.
12. In your custom **Day Sequence Actor Blueprint** you created in Step 1, use the **Details** panel to assign your **Day Sequence Collection** asset to the **Day Sequence Collection** assignment slot.
13. **Compile** and **Save** the Blueprint.

## Time of Day Viewport Toolbar

Once a Day is added to a level, the **Time of Day** toolbar menu is automatically added to the viewport toolbar. This toolbar provides quick access to some settings for the time of day system, such as a slider to manually preview changes in the level viewport, settings to override the time, and quick actions for Day Sequences.

[![](https://dev.epicgames.com/community/api/documentation/image/3129d5e7-faba-4a4d-8723-984386836c9e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3129d5e7-faba-4a4d-8723-984386836c9e?resizing_type=fit)

The Time of Day toolbar contains the following:

[![](https://dev.epicgames.com/community/api/documentation/image/9fafb928-903e-404d-b8ba-f647b98065cd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9fafb928-903e-404d-b8ba-f647b98065cd?resizing_type=fit)

| Property | Description |
| --- | --- |
| Preview |  |
| **Time** | This setting is useful for previewing the position of the directional light source according to the assigned Day Sequence Collection asset while working in the level editor. You can manually enter in time values or drag the slider to scrub through the time of day. |
| PIE Settings |  |
| --- | --- |
| **Override Initial Time of Day** | When the box is checked, the current preview set in the Time slider is used as the initial time of day when using Play in Editor (PIE). |
| **Freeze Time in PIE** | Pauses the day cycle when starting PIE at that time. |
| Actions |  |
| --- | --- |
| **Open Root Sequence** | Opens the Root Sequence on the Day Sequence Actor. |
| **Select Day Sequence Actor** | Selects the Day Sequence Actor in the current level. |
| **Refresh Day Sequence Actor** | Refreshes the Main Sequence in the Day Sequence Actor. |
| **Open Day Sequence Actor** | Opens the Day Sequence Actor Blueprint. |

You can use the **Time** slider to manually scrub through the time of day when a Day Sequence Actor has been set up to do so, like with the preconfigured Sun Moon Day Sequence Actor.

If the you’re not able to use the **Time** slider in the Time of Day toolbar, you should check the following to ensure the time slider is enabled:

* The Day Sequence Subsystem is aware of the Day Sequence Actor in the level (see “Setting Up a Custom Time of Day System” below).
* The Day Sequence Actor has a valid Root Sequence, meaning that it exists and has at least 1 subsection / subsequence. Usually, this means the Day Sequence Actor has a valid collection asset.

In the majority of cases, when the Time slider is disabled, it is because there is no Day Sequence Actor, there is a Day Sequence Actor that has no collection, or that the Day Sequence Collection is empty.

## Day Sequence Actors, Components, and Assets

The Day Sequence plugin provides a set of runtime actors, components, and assets to build a time of day system from scratch, to modify ones in your level, and a complete preconfigured one to use without minimal setup.

Below is a complete list of these actors, components, and assets you can use:

| Name | Description |
| --- | --- |
| Level Actors |  |
| **Day Sequence Actor** | This is a placeable actor responsible for playback Day Sequence assets in a level. This actor defines:   * The list of Day Sequence assets for playback indirectly from a Day Sequence Collection asset. * Duration of a day cycle in game time (with Day Length). * Duration of a day cycle in real time (with Time Per Cycle). * Initial time of day in game time (with Initial Time of Day). * Whether the day cycle is running in game (with Run Day Cycle).   A Day Sequence Actor dynamically builds a root sequence consisting of multiple subsequences corresponding to an input list of Day Sequence assets, like Directional Lights, Sky Atmosphere, Volumetric Clouds, and fog. The Day Sequence is responsible for constructing and managing playback of the root sequence. |
| **Base Day Sequence Actor** | This is a self-registering Day Sequence Actor with a simple set of lighting components, with some being optional. This actor can be used as-is or extended by derived classes. You can see the `ASunPositionDaySequenceActor` class. |
| **Sun Moon Day Sequence Actor** | This is a self-registered Day Sequence Actor that contains all necessary lighting components to represent a physically accurate 24 hour day / night cycle. This actor can be dragged-and-dropped into a level to have a complete time of day system. |
| **Day Sequence Modifier Volume** | This volume can inject procedurally generated sequences, or user-created sequences into a Day Sequence Actor at runtime. These sequences can be enabled, disabled, and weighted (to blend with other sub-sequences) dynamically during gameplay. |
| Assets |  |
| --- | --- |
| **Day Sequence Collection** | This is a custom data asset that has an array of collection entries. A collection entry is composed of a Day Sequence, a bias offset, and a condition set. This asset is intended to facilitate working with groups of sequences that are tailored to particular situations and use cases. |
| **Day Sequence** | This is a custom sequence asset with a playback range that can represent a full day / night cycle. |
| **Root Sequence** | This sequence is the name of a specific Day Sequence that is created and managed by a Day Sequence Actor. This sequence is accessible by clicking **Open Root Sequence** in the Time of Day viewport toolbar. |
| Asset Types |  |
| --- | --- |
| **Day Sequence Condition Tag** | These are an abstraction of a boolean condition which can be associated with a Day Sequence, and which facilitate the reuse of logic used to dynamically enable and disable Day Sequences based on arbitrary conditions (usually scalability settings). |
| **Day Sequence Condition Set** | These are an associative container that maps condition tags to a boolean value (the condition’s “expected value”). A condition set may be *evaluated*, which is the process of evaluating each condition tag in the condition set and returning true if every condition tag evaluates to its associated expected value and is false otherwise. |
| **Procedural Day Sequence** | This is a simple type that is an abstract representation of an arbitrary Procedural Day Sequence. These allow user-defined logic to create a Day Sequence based on a set of exposed parameters. There are three procedural sequences included that you can use as examples. These are: Sun Angle Sequence, Sun Position Sequence, and Sine Sequence.  Procedural Day Sequences can only be created in C++. |

### Day Sequence Actor

The **Day Sequence Actor** is the basis for any time of day system you create. This is where you’ll assign Day Sequences and configure parameters for how the time of day system should behave in your level. When setting a Day Sequence up from scratch, you’ll use this actor to add other environment lighting components to, such as Directional Lights, Sky Atmosphere, Volumetric Clouds, fog, and more.

The Sun Moon Day Sequence Actor and Base Day Sequence Actor are two examples built with the Day Sequence Actor already preconfigured with their lighting components that you can use in your project or explore how they are set up.

You can add a **Day Sequence Actor** to the level using the **Create** dropdown menu in the level editor toolbar, and use the **Details** panel to add lighting components to it.

The Day Sequence Actor has the following settings:

[![](https://dev.epicgames.com/community/api/documentation/image/2c3ce4c8-f0aa-4c91-827f-b59afd73a562?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2c3ce4c8-f0aa-4c91-827f-b59afd73a562?resizing_type=fit)

| Property | Description |
| --- | --- |
| Sequence |  |
| **Day Sequence Collection** | This is a custom data asset that has an array of collection entries. A collection entry is composed of a Day Sequence, a bias offset, and a condition set. This asset is intended to facilitate working with groups of sequences that are tailored to particular situations and use cases. |
| **Collection Bias** | User-defined bias to apply to sequences in an assigned Day Sequence Collection. |
| Preview |  |
| --- | --- |
| **Time of Day Preview** | This sets the time of day to preview in the level editor. This includes a sequence playback slider that feeds in the timeline from a Day Sequence asset. You can use this slider to scrub through the time of day cycle based on its configured settings in the “Runtime Day Cycle” category of this panel.  This setting does not affect the start time of this time of day cycle at runtime, but it can be used as the initial time that the day cycle starts when the game starts if **Override Initial Time of Day** is checked in the **Time of Day** menu in the level viewport. |
| Runtime Day Cycle |  |
| --- | --- |
| **Sequence Update Interval** | This is how often the day cycle visuals get applied. The Day Sequence uses time sliced / budgeted evaluation for performance reasons. The higher this number is, the cheaper it is to play back the day / night cycle. However, the tradeoff is that you can get choppy visuals. When this value is higher, like around 2, you would see shadows jumping around every two seconds. The update interval is usually best when set to something in the range of 0 to 0.5. |
| **Run Day Cycle** | Sets whether or not to run a day cycle at runtime. If unchecked, the day cycle remains fixed at the time specified by the **Initial Time of Day** settings. |
| **Day Interp Curve** | User-provided interpolation curve that maps day cycle times to desired cycle times (usually from 0 to 24 hours). When disabled, the cycle interpolates linearly. |
| **Day Length** | How long a single day cycle is in game time. This is purely for setting up some logic like making some event happen at a specified time in game time. The default length of a day is 24 hrs in game time. |
| **Time Per Cycle** | How long it takes for a day cycle to complete in world time. If this is the same value as the day’s duration, that means real world time is used (24 hours). The default time is set for a day cycle to complete in five minutes. |
| **Initial Time of Day** | Sets the initial time that the day cycle will start at. By default, the day cycle starts at 6 o’clock AM. |

### Day Sequence Modifier Volume

A **Day Sequence Modifier Volume** is useful to override a Day Sequence in the level. You can use these volumes to inject different Day Sequences into the Root sequence of the scene to override the look of various things at any point in time. Additionally, these volumes can control the time of day or other components in the Day Sequence when entering and exiting the volume.

Below is an example of a modifier volume changing the time of day and the amount of cloud coverage with a separately assigned Day Sequence asset.

You can add a **Day Sequence Modifier Volume** to the level using the **Create** dropdown menu in the level editor toolbar. Scale the volume to fit areas you want it to affect.

A Day Sequence Modifier Volume contains the following:

[![](https://dev.epicgames.com/community/api/documentation/image/a63e2a8c-fd50-4409-944a-55369ba9a407?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a63e2a8c-fd50-4409-944a-55369ba9a407?resizing_type=fit)

| Property | Description |
| --- | --- |
| Day Sequence |  |
| **Volume Shape Component** | When set, the shape components will be used for the modifier volume. Otherwise, the default Box component is used. |
| **Bias** | User-defined bias for this post process volume. |
| **Mode** | Determines how the modifier computes the internal blend weight. You can choose between volume and global.   * **Volume** blends the weight smoothly between 0.0 and 1.0 as the blend target crosses the volume boundary. * **Global** uses a blend weight that is always 1.0. |
| **Blend Amount** | This option only appears when Mode is set to **Volume**.  Defines the region in which the effective blend weight is in the range of 0.0 to 1.0 (not inclusive). |
| **Blend Policy** | Determines how the modifier uses User Blend Weight to compute the effective blend weight. Choose between:   * **Ignored** disregards user-specified weights. The effective weight is the internally computed weight. This option removes the User Blend Weight setting. * **Minimum** (default) is the effective minimum internally computed and user-specified weight to blend. * **Maximum** is the effective maximum internally computed and user-specified weight to blend. * **Override** is the effective user-specified weight. |
| **User Blend Weight** | This setting is removed when Blend Policy is set to Ignored.  This is a user-specified blend weight. The final blend weight is determined by the Blend Policy. |
| **Preview** | When enabled, you can preview this day sequence modifier in the editor by moving the camera position within its bounds. |
| **Use Collection** | If unchecked, you can assign a Day Sequence to User Day Sequence. If checked, you can assign a Day Sequence Collection to the Day Sequence Collection slot. |
| **User Day Sequence** | Requires **Use Collection** to be unchecked.  User-provided Day Sequence asset. |
| **Day Sequence Collection** | Requires **Use Collection** to be checked.  User-provided Day Sequence Collection asset. |
| **Smooth Blending** | When checked, the evaluation of a Day Sequence is smoothed while within a blending region of this volume. This is related to Sequence Update Interval because this temporarily overrides the update interval to be a lower value, which can be overridden with the console variable `DaySequence.UpdateIntervalOverride`.  This can be an expensive option. Use with caution. |
| Time |  |
| --- | --- |
| **Day / Night Cycle** | Changes the way the modifier controls the day / night cycle time when enabled. You can choose from the following options:   * **Default** makes no changes to the day / night cycle time. * **Fixed Time** forces the day / night cycle to be fixed at a specified constant time. * **Start at Specified Time** sets an initial time for the day / night cycle when the modifier is enabled. * **Random Fixed Time** uses a random fixed time for the day / night cycle. * **Random Start Time** starts the day / night cycle at a random time and allows it to continue from there. |

### Day Sequence Collection Asset

A **Day Sequence Collection** asset is used to fine-tune any time of day system you set up. The collection adds references to sequences, and allows for configuration of sequence conditions and procedural day sequence parameters.

When setting up a Day Sequence Collection, you’ll need a **Day Sequence** asset for this collection to reference. You’ll also need to select a procedural day sequence type that uses parameters to determine how the Directional Lights (Sun and Moon) move across the sky as time passes.

You can create this asset type in the **Content Browser** by clicking the **Add (+)** icon and selecting **Day Sequence Collection** from the **Miscellaneous** rollout menu.

The Day Sequence plugin contains an example of a Day Sequence Collection that you can explore. You can locate it in the Content Browser under **Engine > Plugins > DaySequence Content** named **DSCA\_24hr**. This collection is used with the Sun Moon Day Sequence Actor.

A Day Sequence Collection asset contains the following:

[![](https://dev.epicgames.com/community/api/documentation/image/6e76e9ea-d80f-48f4-a660-774d5f8f9c98?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6e76e9ea-d80f-48f4-a660-774d5f8f9c98?resizing_type=fit)

| Property | Description |
| --- | --- |
| Day Sequences |  |
| **Sequence** | The Day Sequence asset for this collection entry. |
| **Bias Offset** | The offset hierarchical bias assigned to this collection entry. |
| **Conditions** | The set of conditions which must evaluate to their expected values for this entry to be active. |
| Procedural Day Sequence |  |
| --- | --- |
| **Index** | Provides a selection of abstract representations of an arbitrary procedural day sequence. (See below for more information.) |

#### Procedural Day Sequences

A **Procedural Day Sequence** is a selection type that is an abstract representation of an arbitrary procedural day sequence. These types can be created by anyone to expose definable logic to create a DaySequene based on a set of exposed parameters.

There are three types of procedural day sequences provided with the Day Sequence plugin. These are:

[![](https://dev.epicgames.com/community/api/documentation/image/561de3ec-50ab-4250-86e4-13f2c7041429?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/561de3ec-50ab-4250-86e4-13f2c7041429?resizing_type=fit)

* **Sine Sequence** animates a user-specified property according to a sine wave.
* **Sun Angle Sequence** linearly animates the sun.
* **Sun Position Sequence** animates a sun in a physically accurate way based on geographic data.

Each of these procedural day sequences include their own user-definable parameters:

|  |  |  |
| --- | --- | --- |
|  |  |  |
| Sine Sequence Settings | Sun Angle Sequence Settings | Sun Position Sequence Settings |

Currently, a procedural day sequence can only be added using C++. In time, you will be able to create these types using Blueprint.

### Day Sequence Assets

A **Day Sequence** asset is a primary building block of any time of day cycle. These are similar to a Level Sequence using [Sequencer](animating-characters-and-objects\Sequencer) with the difference being that its playback range is always exactly one day, and it automatically binds channels to the active Day Sequence Actor in the level.

A Day Sequence is not tied to any particular actor. Instead, they animate components and properties owned by a generic **Root Day Sequence** actor — which is automatically bound to the Day Sequence Actor.

You can create this type of asset in the **Content Browser** by clicking the **Add (+)** icon and selecting **Day Sequence** from the **Miscellaneous** rollout menu.

The Day Sequence plugin contains an example of a Day Sequence that you can explore. You can locate it in the Content Browser under **Engine > Plugins > DaySequence Content** named **DS\_24hr**. This collection is used with the Sun Moon Day Sequence Actor.

Below is an example of a Day Sequence setup to reference some of the lighting components and materials used to animate them within the time of day cycle range. These components are set up and added to the Day Sequence Actor in the level.

[![](https://dev.epicgames.com/community/api/documentation/image/524df135-9020-4551-aebe-6002bf88a0ad?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/524df135-9020-4551-aebe-6002bf88a0ad?resizing_type=fit)

The Sun Moon Day Sequence Actor provides an example of a Day Sequence (DS\_24hr) that animates lighting components and properties used by the Day Sequence Actor.

#### Root Day Sequence

The **Root Day Sequence** is a transient day sequence that constitutes the entirety of the day / night cycle and consists of sub-sequences. The number of subsequences displayed is dependent on the Day Sequences and Procedural Day Sequences that have been added to the Day Sequence Collection asset.

You can use the **Time of Day** viewport toolbar to directly open the Root Sequence by clicking on **Open Root Sequence**.

The Day Sequence Actor in your level is responsible for playback of these sequences.

[![](https://dev.epicgames.com/community/api/documentation/image/749df5f0-7cc7-4c2d-971f-d2c93faa7300?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/749df5f0-7cc7-4c2d-971f-d2c93faa7300?resizing_type=fit)

The Root Day Sequence with two tracks, one that animates the procedural day sequence for sun movement and the other that animates the components of the Day Sequence Actor for things like the volumetric clouds and sky sphere along with their materials.

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [lighting](https://dev.epicgames.com/community/search?query=lighting)
* [experimental](https://dev.epicgames.com/community/search?query=experimental)
* [sequencer](https://dev.epicgames.com/community/search?query=sequencer)
* [blueprint](https://dev.epicgames.com/community/search?query=blueprint)
* [time of day](https://dev.epicgames.com/community/search?query=time%20of%20day)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Enabling Day Sequence in a Project](/documentation/en-us/unreal-engine/day-sequence-time-of-day-plugin-for-unreal-engine?application_version=5.7#enabling-day-sequence-in-a-project)
* [Setting Up a Day Sequence](/documentation/en-us/unreal-engine/day-sequence-time-of-day-plugin-for-unreal-engine?application_version=5.7#setting-up-a-day-sequence)
* [Setting Up a Preconfigured Time of Day System](/documentation/en-us/unreal-engine/day-sequence-time-of-day-plugin-for-unreal-engine?application_version=5.7#setting-up-a-preconfigured-time-of-day-system)
* [Setting up a Simplified Time of Day System](/documentation/en-us/unreal-engine/day-sequence-time-of-day-plugin-for-unreal-engine?application_version=5.7#setting-up-a-simplified-time-of-day-system)
* [Setting Up a Custom Time of Day System](/documentation/en-us/unreal-engine/day-sequence-time-of-day-plugin-for-unreal-engine?application_version=5.7#setting-up-a-custom-time-of-day-system)
* [Time of Day Viewport Toolbar](/documentation/en-us/unreal-engine/day-sequence-time-of-day-plugin-for-unreal-engine?application_version=5.7#time-of-day-viewport-toolbar)
* [Day Sequence Actors, Components, and Assets](/documentation/en-us/unreal-engine/day-sequence-time-of-day-plugin-for-unreal-engine?application_version=5.7#day-sequence-actors-components-and-assets)
* [Day Sequence Actor](/documentation/en-us/unreal-engine/day-sequence-time-of-day-plugin-for-unreal-engine?application_version=5.7#day-sequence-actor)
* [Day Sequence Modifier Volume](/documentation/en-us/unreal-engine/day-sequence-time-of-day-plugin-for-unreal-engine?application_version=5.7#day-sequence-modifier-volume)
* [Day Sequence Collection Asset](/documentation/en-us/unreal-engine/day-sequence-time-of-day-plugin-for-unreal-engine?application_version=5.7#day-sequence-collection-asset)
* [Procedural Day Sequences](/documentation/en-us/unreal-engine/day-sequence-time-of-day-plugin-for-unreal-engine?application_version=5.7#procedural-day-sequences)
* [Day Sequence Assets](/documentation/en-us/unreal-engine/day-sequence-time-of-day-plugin-for-unreal-engine?application_version=5.7#day-sequence-assets)
* [Root Day Sequence](/documentation/en-us/unreal-engine/day-sequence-time-of-day-plugin-for-unreal-engine?application_version=5.7#root-day-sequence)
