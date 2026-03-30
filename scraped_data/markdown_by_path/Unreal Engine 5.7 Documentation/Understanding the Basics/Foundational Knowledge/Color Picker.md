<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/color-picker-in-unreal-engine?application_version=5.7 -->

# Color Picker

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
7. Color Picker

# Color Picker

Tool for interactively choosing colors to assign to color properties of actors.

![Color Picker](https://dev.epicgames.com/community/api/documentation/image/d5bd8683-e6d4-457e-948f-ddf456b2403a?resizing_type=fill&width=1920&height=335)

 On this page

The **Color Picker** allows you to easily adjust a color value for a color property in the Unreal Editor. You can adjust colors by RGBA (red, green, blue, alpha), HSV (hue, saturation, value), and Hex (ARGB). Alternatively you can select a color by clicking anywhere in the color wheel or by capturing the color under your mouse, anywhere on your monitors.

![ColorPicker](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/133be832-2f5a-4b04-909e-61110329e5a5/colorpicker.png)

| Item | Description |
| --- | --- |
| Themes & sRGB | Allows for [Theme](/documentation/en-us/unreal-engine/color-picker-in-unreal-engine#themes) selection and **sRGB** previews (see note below). |
| Color Wheel | A Color wheel that allows a color to be selected graphically by clicking and dragging with the mouse. Additional adjustments can be made by using the two vertical bars. Instead of Color Wheel, a Color Spectrum may be used if the option is toggled on. |
| Color Swatches | Displays the color currently assigned (Old) to the property and the color currently selected in the Color Picker (New). Colors can be dragged from either the *Old* or *New* sections to the **Themes** bar to save them for reuse later on. |
| Picker Options | Toggles between the Color Wheel or Color Spectrum (left image). The **Eye Dropper** (right image) can be used for selecting a colored pixel from any window inside or outside of Unreal Engine. |
| Red Channel | Drag or type value to set the **Red** channel. |
| Green Channel | Drag or type value to set the **Green** channel. |
| Blue Channel | Drag or type value to set the **Blue** channel. |
| Hue Channel | Drag or type value to set the **Hue**. |
| Saturation Channel | Drag or type value to set the **Saturation**. |
| Value Channel | Drag or type value to set the **Value** (color brightness). |
| Alpha Channel | Drag or type value to set the **Alpha** channel. |
| Hex Values | Enter in Hexadecimal Linear or Hexadecimal sRGB values manually. |

When working with the Color Picker, it does not assume a straight inverse gamma conversion from colors sampled on the screen using the Eye Dropper. Instead, sRGB is the assumed space all colors are sampled in, making sampling colors from Photoshop the identical version of the color converted into linear space. When transformed back into sRGB space, it will be the same color you saw in Photoshop.

`FColor` and `FLinearColor` can also default to the sRGB space using a UPROPERTY meta tag of **sRGB=true** (or **false**), you can force a specific default checking of the sRGB checkbox.

Several places in [Unreal Motion Graphics (UMG)](/documentation/en-us/unreal-engine/creating-user-interfaces-with-umg-and-slate-in-unreal-engine) now force this default since sRGB is the space UMG will be rendered in (on PC). Additional work will be needed on Mac where the final rendering space is gamma 2.2.

## Themes

**Themes** are collections of colors that can be easily reused. These can be used to make commonly used colors available or to restrict the colors used by artists and designers to a specific palette.

![Example Theme](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/93a65e09-6f68-48a9-8a31-ffc234126635/theme_spring.png)

### Creating Themes

New themes can be added by clicking the **Theme Menu** button.  
![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/77a220b8-5f3e-4146-8fce-2577d22944e0/thememenubutton.png)

Click the **New Theme** button to add an empty theme to the list.  
![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/812aab91-baa4-4899-8839-ee6124bdd532/newtheme_2.png)

Click the **Duplicate** button to create a new theme that copies an existing theme.  
![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ad86645d-df0c-4333-92b6-37eee79fb106/theme_duplicate.png)

### Renaming Themes

Themes can be renamed by clicking the **Rename** button.  
![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5d4e8b15-44c1-4c83-a218-6bf431bfd22e/theme_rename.png)

This displays a text field, with the default text "New Theme".  
![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c249b101-62d1-4868-a674-9485e4804133/theme_rename_editbox.png)

Type in a new name for the theme. Then click the **Accept** button.  
![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/317ce134-0305-4599-8a4e-3042114afa91/theme_rename_newname.png)

### Adding and Removing Colors

Colors can be added, removed, or reordered within the theme using drag and drop.

Drag colors from the main swatch to add them to a theme.  
![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f21560ce-421c-4aad-b5f6-eab77baa7c69/theme_add_color.png)

Reorder colors within a theme by dragging them right or left.  
![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/daec98da-7196-4e83-823c-41cf6b0ef55e/theme_edit.png)

Drag colors to the **Trashcan** icon to delete them from the theme.  
![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/29e29abd-cd9e-4313-9882-f572874cdbbe/theme_edit_color_delete.png)

Colors can also be reordered and removed from the **Theme Menu**.

To edit the theme, drag colors left or right.  
![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/30ac2a33-e68d-45c6-b6b1-81b1ef23714c/theme_menu_edit.png)

To delete a color from the theme, drag it to the **Trashcan** icon.  
![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5dfe710f-8009-4a85-86cf-dd5790be2080/theme_menu_delete.png)

### Labeling Saved Colors in a Theme

You can label colors saved in your **Theme Bar** by right-clicking a saved color, and typing a name for the color in the **Color Label** window.  
![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/03a8bcec-b472-421b-b285-7948942ed37b/colorlabel-2.png)

When you hover the mouse cursor over the color that has been labeled, you will see the name listed in the tooltip properties for the color.  
![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/32adf2db-9cc1-4953-a8d7-8cbdfb82a1d5/colorlabel-3.png)

Colors can also be labeled from the **Theme Menu**. Right-click the color, then type a name for the color�into the **Color Label** window.  
![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e5ffaf2d-3d6f-4fc2-b38e-d7fb741c0be2/colorlabel-4.png)

### Using Themes

To change themes, select the theme you want to be active from the **Theme Menu**.

![Select Theme](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f3983f64-c4be-4a6b-8779-8e9140274cad/theme_select.png)

To use a color from the current theme, double-click the color to be applied. This will update the currently selected color in the Color Picker.

![Use Color](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f0f72814-7139-420f-bcbb-bfae620c7655/theme_use_color.png)

Hovering the cursor over a color in the theme will display the color information.

![Color Info](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c0e62b53-774d-42fe-be35-df6a18797fea/theme_color_info.png)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Themes](/documentation/en-us/unreal-engine/color-picker-in-unreal-engine?application_version=5.7#themes)
* [Creating Themes](/documentation/en-us/unreal-engine/color-picker-in-unreal-engine?application_version=5.7#creatingthemes)
* [Renaming Themes](/documentation/en-us/unreal-engine/color-picker-in-unreal-engine?application_version=5.7#renamingthemes)
* [Adding and Removing Colors](/documentation/en-us/unreal-engine/color-picker-in-unreal-engine?application_version=5.7#addingandremovingcolors)
* [Labeling Saved Colors in a Theme](/documentation/en-us/unreal-engine/color-picker-in-unreal-engine?application_version=5.7#labelingsavedcolorsinatheme)
* [Using Themes](/documentation/en-us/unreal-engine/color-picker-in-unreal-engine?application_version=5.7#usingthemes)
