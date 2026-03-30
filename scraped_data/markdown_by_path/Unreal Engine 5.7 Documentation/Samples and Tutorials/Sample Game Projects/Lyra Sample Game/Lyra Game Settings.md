<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/lyra-sample-game-settings-in-unreal-engine?application_version=5.7 -->

# Lyra Game Settings

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
6. [Sample Game Projects](/documentation/en-us/unreal-engine/sample-game-projects-for-unreal-engine "Sample Game Projects")
7. [Lyra Sample Game](/documentation/en-us/unreal-engine/lyra-sample-game-in-unreal-engine "Lyra Sample Game")
8. Lyra Game Settings

# Lyra Game Settings

An overview of Game Settings for the Lyra Game Sample.

![Lyra Game Settings](https://dev.epicgames.com/community/api/documentation/image/22d27aff-dc73-447a-962f-e1b9d82f5990?resizing_type=fill&width=1920&height=335)

 On this page

## Lyra Game Settings

Lyra features a **GameSettings** plugin that is used to simplify the process of creating a User Interface (UI) and its underlying data. The plugin is responsible for managing the data that you may want to store in a configuration file or server.

As an example: Your player is a Photographer exploring a Forest, and you have been tasked with documenting rare wildlife. When your character enters a certain portion of the level, the Game Settings plugin can manage data located on a server to communicate with the level to determine which rare wildlife should appear in the area your character is currently in.

There are several key parts of the framework,

* **UGameSettingRegistry** - The Game Setting Registry is a set of settings. A single registry can be exposed partially or in its entirety to the user, however, you will be required to register at least one of your Game's Settings. If there are other systems in your game that require settings that do not have primary game settings, then we recommend you use another registry.
* **UGameSetting** - Defines the base class of all settings. Any setting in the list of the UI is considered a Game Setting. This class handles core concepts like name, description, dependencies, and edit conditions.
* **UGameSettingValue** - Implements the base class of any setting that has a value that needs to be get and set. A few settings will directly inherit from this class, instead, they'll use:

  ```
            UGameSettingValueScalarDynamic,
            UGameSettingValueDiscreteDynamic_Bool,
            UGameSettingValueDiscreteDynamic_Number,
            UGameSettingValueDiscreteDynamic_Enum.
  Copy full snippet
  ```
* **UGameSettingCollection** - Defines organization settings. A Game Setting Collection is used to group settings together. For example, if you wanted a collection to generate headers in a list, then that collection represents that headered group.
* **FGameSettingEditCondition** - Each setting has a set of attached edit conditions. These edit conditions provide you with the ability to encode logic that queries if a setting is disabled, hidden, or destroyed.

### Making a Setting

Most of the setting's methods you write in code will look like the following,

```
	UGameSettingValueScalarDynamic* Setting = NewObject<UGameSettingValueScalarDynamic>();
	Setting->SetDevName(TEXT("OverallVolume"));
	Setting->SetDisplayName(LOCTEXT("OverallVolume_Name", "Overall"));
	Setting->SetDescriptionRichText(LOCTEXT("OverallVolume_Description", "Adjusts the volume of everything."));
	Setting->SetDynamicGetter(GET_LOCAL_SETTINGS_FUNCTION_PATH(GetOverallVolume));
	Setting->SetDynamicSetter(GET_LOCAL_SETTINGS_FUNCTION_PATH(SetOverallVolume));
	Setting->SetDefaultValue(GetDefault<ULyraSettingsLocal>()->GetOverallVolume());
	Setting->SetDisplayFormat(UGameSettingValueScalarDynamic::ZeroToOnePercent);
	Setting->AddEditCondition(FWhenPlayingAsPrimaryPlayer::Get());

Copy full snippet
```

All settings must have a `DevName` that is unique across the registry and require a `DisplayName`.

`DescriptionRichText` is required for most settings and is checked to ensure every setting where it is required. Rich text is the standard for UMG Rich text widget formatting because the plain text is parsed out when indexing the search. The DynamicGetter and DynamicSetter provide access to settings at runtime. To continually access data using:

```
	LocalPlayer->GetLocalSettings()->GetOverallVolume()

Copy full snippet
```

would be redundant to declare for each setting, instead, the dynamic getters and setters take an `FGameSettingDataSourceDynamic` which is built using the provided macros.

The DynamicSetter and DynamicGetter require that you can access the data from the LocalPlayer using [Metadata Property Specifiers](/documentation/en-us/unreal-engine/metadata-specifiers-in-unreal-engine) (UFUNCTION/UPROPERTY). Using specifiers ensures these conditions on initialization.

### Custom Settings

Using the built-in classes for your settings accommodates most needs. However, there may be instances where you require more complex logic for your settings. For example, you may need to retrieve all the available languages packaged with your game.

```
	UGameSettingValueDiscrete_Language* Setting = NewObject<UGameSettingValueDiscrete_Language>();
	Setting->SetDevName(TEXT("Language"));
	Setting->SetDisplayName(LOCTEXT("LanguageSetting_Name", "Language"));
	Setting->SetDescriptionRichText(LOCTEXT("LanguageSetting_Description", "The language of the game."));
	Matchmaking->AddSetting(Setting);

Copy full snippet
```

`UGameSettingValueDiscrete_Language` directly mutates the language and culture settings we have stored.

### Edit Conditions

All edit conditions subclasses from FGameSettingEditCondition handle one responsibility to disable, hide, prevent resetting, or remove a setting from analytics if any of the following conditions should apply:

* **FWhenCondition** - Provides the ability to write your condition as inline lambda.
* **FWhenPlatformHasTrait** - Used for hiding or disabling settings based on platform traits. Example traits such as:

  + Does the platform support keyboard and mouse?
  + Does the platform support changes in screen resolution?

    You will notice after looking at several source code examples, we do not use checks such as `#if PLATFORM_FEATURE` when eliminating settings or other general areas of Lyra, instead we rely on platform traits, because we can use the option to test other platforms when testing in PIE, and everything can be dynamically re-evaluated. We therefore encourage you to use `FWhenPlatformHasTrait`, when possible.
* **FWhenPlayingAsPrimaryPlayer** - When you do not want other local players to have access to certain settings, you can use these instances to edit certain conditions that will make it exclusively available to the first player.

For example, the Resolution setting located in the class `LyraGameSettingRegistry_Video.cpp`:

```
	Setting->AddEditDependency(WindowModeSetting);
	Setting->AddEditCondition(MakeShared<FWhenCondition>([WindowModeSetting](const ULocalPlayer*, FGameSettingEditableState& InOutEditState) {

		if (WindowModeSetting->GetValue<EWindowMode::Type>() == EWindowMode::Windowed)

		{

			InOutEditState.Disable(LOCTEXT("ResolutionWindowed_Disabled", "When the Window Mode is set to <strong>Windowed</>, the resolution is freely resized with the window."));

		}

		else if (WindowModeSetting->GetValue<EWindowMode::Type>() == EWindowMode::WindowedFullscreen)

		{

			InOutEditState.Disable(LOCTEXT("ResolutionWindowedFullscreen_Disabled", "When the Window Mode is set to <strong>Windowed Fullscreen</>, the resolution must match the native desktop resolution."));

		}
	}));

Copy full snippet
```

Edit conditions track whether settings are toggled to `enabled`, `disabled`, or `hidden`. They are designed to ensure that if the user is attempting to change your project settings during runtime, then you can provide an explanation that can be traced back to the debugger. In the image below, the edit condition for Window Mode has been toggled to Disabled. As a result, the engine reports a message back to the user, so they understand why a setting can't be changed.

![LyraWarningWindow](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f6076fc2-3d24-4390-9150-a97dd891d52c/lyrawarningwindow.png)

### User Interface

The User interface consists of the classes `UGameSettingVisualData`, and `UGameSettingPanel`. The Game Setting Panel is responsible for processing the display, which you can provide with a registry and a filter to have the panel show your settings. To determine how those settings are defined, the Game Setting Visual Data contains the rules your settings will use for connecting a `UGameSettingListEntryBase` to the `UGameSetting` class.

![LyraGameSettingRegistry](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ee46da9d-1413-4219-88ae-a04263482d3e/lyragamesettingregistry.png)

The Game Settings Registry Visual Data contains details on how the panel should display.

### Data Sources

```
	`FGameSettingDataSource`
	`FGameSettingDataSourceDynamic`

	`GET_SHARED_SETTINGS_FUNCTION_PATH`
	`GET_LOCAL_SETTINGS_FUNCTION_PATH`
Copy full snippet
```

* [blueprints](https://dev.epicgames.com/community/search?query=blueprints)
* [programming](https://dev.epicgames.com/community/search?query=programming)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Lyra Game Settings](/documentation/en-us/unreal-engine/lyra-sample-game-settings-in-unreal-engine?application_version=5.7#lyragamesettings)
* [Making a Setting](/documentation/en-us/unreal-engine/lyra-sample-game-settings-in-unreal-engine?application_version=5.7#makingasetting)
* [Custom Settings](/documentation/en-us/unreal-engine/lyra-sample-game-settings-in-unreal-engine?application_version=5.7#customsettings)
* [Edit Conditions](/documentation/en-us/unreal-engine/lyra-sample-game-settings-in-unreal-engine?application_version=5.7#editconditions)
* [User Interface](/documentation/en-us/unreal-engine/lyra-sample-game-settings-in-unreal-engine?application_version=5.7#userinterface)
* [Data Sources](/documentation/en-us/unreal-engine/lyra-sample-game-settings-in-unreal-engine?application_version=5.7#datasources)
