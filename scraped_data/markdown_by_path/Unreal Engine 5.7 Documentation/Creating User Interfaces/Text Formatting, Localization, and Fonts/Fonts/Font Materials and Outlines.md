<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/font-materials-and-outlines-in-unreal-engine?application_version=5.7 -->

# Font Materials and Outlines

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
5. [Creating User Interfaces](/documentation/en-us/unreal-engine/creating-user-interfaces-with-umg-and-slate-in-unreal-engine "Creating User Interfaces")
6. [Text Formatting, Localization, and Fonts](/documentation/en-us/unreal-engine/text-formatting-localization-and-fonts-in-unreal-engine "Text Formatting, Localization, and Fonts")
7. [Fonts](/documentation/en-us/unreal-engine/using-fonts-in-unreal-engine "Fonts")
8. Font Materials and Outlines

# Font Materials and Outlines

Examples of how you can style your UMG fonts using colors, Materials, and outlines.

![Font Materials and Outlines](https://dev.epicgames.com/community/api/documentation/image/c12e3e70-c7a7-4616-9a2b-21c00581b12f?resizing_type=fill&width=1920&height=335)

 On this page

In addition to being able to set a **Color and Opacity** for your **Font** in UMG, you can also use Materials and font outlines for additional **Font** styling.

## Font Colors

You can set the **Vertex Color** for your **Font** by setting its **Color and Opacity**.

![Set the Font Color and Opacity](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ffd8649b-1851-432d-b765-2adbd07ead6d/ue5_1-01-set-color.png "Set the Font Color and Opacity")

Without a **Font Material** specified, this will apply a solid color to your text.

![Example of the Font Block without a Font Material specified](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bdb47391-a20a-4fed-8fd9-8cff30768e34/ue5_1-02-example-text-block-1.png "Example of the Font Block without a Font Material specified")

## Font Materials

You can specify a **Font Material** for your **Font** in the **Details** panel.

![Set Font Material](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2750c90d-cc73-4762-bb50-cfaaf98f5334/ue5_1-03-set-font-material.png "Set Font Material")

If your **Font Material** doesn't have a **Vertex Color** node, the effect is like a simple multiplication.

|  |  |  |
| --- | --- | --- |
| [undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f03b05f9-98b5-47fa-8aeb-d52fc84dd6fc/ue5_1-04-base-color.png) | Base Color material preview | Example of the Font Block with a Base Color node |
| Font Material Setup | Font Material Preview | Final Font |

However, if you place a **Vertex Color** node in your **Font Material**, you can use its outputs to do math within your shader.

|  |  |  |
| --- | --- | --- |
| [undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/05ac4729-36fd-4eb2-8223-e908fe9a435a/ue5_1-07-vertex-red-color.png) | Vertex Red Color material preview | Example of the Font Block with a Vertex Red Color node |
| Font Material Setup | Font Material Preview | Final Font |

Materials used as font materials must be in the **User Interface** domain.

![Set Material Domain to UI](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/499215a1-3adb-4bed-9618-5bdd20d25749/ue5_1-10-set-domain.png "Set Material Domain to UI")

## Font Outlines

You can specify a different **Outline Color** as well as a different Material to use for a font outline.

![Set the Font Outline Settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dd8bf273-1d73-40ac-8f46-65b0480e854c/ue5_1-11-outline-settings.png "Set the Font Outline Settings")

The size of the outline is specified in Slate units, but when the font's scale is 1.0, 1 Slate unit is equivalent to 1 pixel.

![Example of the Font Block with Outline](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/45fd7ffa-a12e-4891-8c18-1c1a62bb6ce9/ue5_1-12-example-text-block-3.png "Example of the Font Block with Outline")

One interesting note is that you can specify whether or not to use **Separate Fill Alpha**.

![Separate Fill Alpha option](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/23bb7b46-aa4e-434a-a98d-53c33600ddc0/ue5_1-13-separate-fill-alpha.png "Separate Fill Alpha option")

When this is enabled, the outline is translucent
where the filled area will be, allowing you to adjust the alphas of the font and the font outline independently. When it is disabled, the font is overlaid
on the outline, so the alphas are additive and the outline color and Material is visible through a font with an alpha less than 1.

![Font Color Alpha = 0.5, Separate Fill Alpha disabled](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c6ff0d9a-ce4f-48bf-9947-31a13b64acb2/ue5_1-14-separate-fill-alpha-disable.png)

![Font Color Alpha = 0.5, Separate Fill Alpha enable](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1a57d1d5-b9a8-4a3b-882c-b6b9f051a9d5/ue5_1-15-separate-fill-alpha-enable.png)

Font Color Alpha = 0.5, Separate Fill Alpha disabled

Font Color Alpha = 0.5, Separate Fill Alpha enable

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [umg ui designer](https://dev.epicgames.com/community/search?query=umg%20ui%20designer)
* [fonts](https://dev.epicgames.com/community/search?query=fonts)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Font Colors](/documentation/en-us/unreal-engine/font-materials-and-outlines-in-unreal-engine?application_version=5.7#fontcolors)
* [Font Materials](/documentation/en-us/unreal-engine/font-materials-and-outlines-in-unreal-engine?application_version=5.7#fontmaterials)
* [Font Outlines](/documentation/en-us/unreal-engine/font-materials-and-outlines-in-unreal-engine?application_version=5.7#fontoutlines)
