<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/working-with-ios-input-in-unreal-engine?application_version=5.7 -->

# Working with iOS Input

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
5. [Mobile Development](/documentation/en-us/unreal-engine/getting-started-with-mobile-development-in-unreal-engine "Mobile Development")
6. [iOS, iPadOS, and tvOS](/documentation/en-us/unreal-engine/ios-ipados-and-tvos-support-for-unreal-engine "iOS, iPadOS, and tvOS")
7. [iOS and tvOS Development Guides](/documentation/en-us/unreal-engine/developing-on-ios-tvos-and-ipados-in-unreal-engine "iOS and tvOS Development Guides")
8. Working with iOS Input

# Working with iOS Input

Guidelines for working with external input devices in iOS, tvOS and iPadOS 14 and later

![Working with iOS Input](https://dev.epicgames.com/community/api/documentation/image/a0a09005-f3b1-4677-be38-8ba2049de8a8?resizing_type=fill&width=1920&height=335)

 On this page

In iOS, tvOS, and iPadOS 14 and later, Apple supports a wide variety of input devices, including gamepads, keyboard, mouse, and trackpad. This includes the ability to remap gamepad buttons for Xbox, PlayStation, and MFi gamepad controllers at the OS-level. The OS provides handling for the button glyph displays for these devices, enabling applications to obtain glyphs that are accurate to users' custom mappings. This is required for all apps targeting OS version 14 and later.

Apple requires that your in-game button displays must be accurate to the user's OS-level input bindings. The App Store and Apple Arcade may reject your Apps for distribution if you do not comply with this requirement.

**Unreal Engine** supports input handling, enabling your applications to take full advantage of the expanded range of devices. As long as users correctly connect their input to their Apple device, no additional setup is required to use this functionality. However, functionality is included to assist in complying with Apple's requirements for the UI.

## Obtaining Gamepad Button Glyphs

Use the **Get Gamepad Button Glyph** node in **Blueprint** to retrieve glyphs accurate to your users' mappings.

![The Get Gamepad Button Glyph node in Blueprint](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/01ef4c19-b78c-4d65-b740-dddd4c9fc028/getbuttonglyphbp.png)

The Get Button Glyph node, with the text Gamepad\_Facebutton\_Top provided in the Button Key field.

Its parameters are as follows:

| Parameter | Type | Description |
| --- | --- | --- |
| Button Key | String | The `FKey` name for the intended button, as defined in `InputCoreTypes.h`, converted to a string. |
| Controller Index | Integer | The index of the connected controller that you want to fetch button glyphs for. |
| Return Value | Texture2D | A 2D texture containing the button glyph to use in your UI widgets. |

As an example, if you wanted to obtain the button glyph for the top face button on a controller, you would use the string **Gamepad\_Facebutton\_Top**.

When requesting buttons like this, you should request the button that you expect the user to use based on the default mapping. If the user has remapped the buttons within the OS, the function will automatically return the re-mapped button they're using instead. For instance, if the user swaps the X and Y buttons on an Xbox controller, `Gamepad_Facebutton_Top` would return the X button glyph instead of Y.

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [user interface](https://dev.epicgames.com/community/search?query=user%20interface)
* [input](https://dev.epicgames.com/community/search?query=input)
* [ios](https://dev.epicgames.com/community/search?query=ios)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Obtaining Gamepad Button Glyphs](/documentation/en-us/unreal-engine/working-with-ios-input-in-unreal-engine?application_version=5.7#obtaininggamepadbuttonglyphs)
