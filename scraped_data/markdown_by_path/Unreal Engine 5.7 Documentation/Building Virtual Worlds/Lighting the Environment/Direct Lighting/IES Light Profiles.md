<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-ies-light-profiles-in-unreal-engine?application_version=5.7 -->

# IES Light Profiles

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
7. [Direct Lighting](/documentation/en-us/unreal-engine/features-and-properties-of-lights-in-unreal-engine "Direct Lighting")
8. IES Light Profiles

# IES Light Profiles

An overview of setting up and using IES textures with lights.

![IES Light Profiles](https://dev.epicgames.com/community/api/documentation/image/e2fbc608-bb2b-4b0a-a5a6-1fe18c4135bf?resizing_type=fill&width=1920&height=335)

 On this page

The Illuminating Engineering Society (IES) has defined a file format which describes a light's distribution from a light source using real world measured data. These IES Photometric files, or **IES Profiles**, are a lighting industry standard method of diagramming the brightness and falloff of light as it exists a particular real world light fixture. It enables them to account for reflective surfaces in the light fixture, the shape of the light bulb, and any lensing effects that happens. This type of photometric lighting is primarily used in Enterprise fields (such as Media and Entertainment or Architecture and Manufacturing), but is often used in games production to achieve realistic lighting effects, too.

IES Light Profiles are a 1D texture (gradient). However, they are not actual texture files. The curve defines light intensity in an arc that "sweeps" around an axis to make Point, Spot, and Rect Lights appear to be casting light realistically based on the provided real-world data. The curve works like a multiplier for the overall brightness of the light, as if you were projecting a texture from a light, but without the overhead of using a texture, or the errors that can occur at some angles.

In the examples below, the IES Profile is assigned to a Point Light and the diagram in the top left of each panel shows the shape of the given IES Profile.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c84caff8-e5aa-4bd6-b779-63842bdd0331/01-ies-light-profiles-examples.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c84caff8-e5aa-4bd6-b779-63842bdd0331/01-ies-light-profiles-examples.png)

Click the image for full size.

If you were to open an IES Profile in a text editor, you would find that it is an ASCII file containing a wide array of metadata, like this example for a Lithonia TE\_150S\_E17\_C:

```
	IESNA:LM-63-2002
	[TEST] 11915
	[TESTDATE] 1/31/2008
	[ISSUEDATE] 1/24/2014
	[TESTLAB] ACUITY BRANDS LIGHTING CONYERS LAB
	[TESTMETHOD] IES LM-46:2004
	[MANUFAC] Lithonia Lighting
	[LUMCAT] TE 150S E17 C (SC=1.0)
	[LUMINAIRE] PREMIUM ENCLOSED HIGHBAY INDUSTRIAL WITH ALUMINUM REFLECTOR, CLEAR TEMPERED GLASS LENS, AND CONCENTRATING DISTRIBUTION
	[LAMPCAT] LU150
	[LAMP] ONE 150-WATT CLEAR ET-23.5 HIGH PRESSURE SODIUM, VERTICAL BASE-UP POSITION
	[BALLAST]
	[BALLASTCAT]
	[DISTRIBUTION] DIRECT, SC-0=1.05, SC-90=1.05
	[_LAMPPOSITION] 0 , 0
	[_LAMPTYPE] HIGH PRESSURE SODIUM
	[_LAMPWATTAGE] 150
	[_LAMPLUMENS] 16000
	[_MOUNTING] Suspended
	[_FAMILY] TE E17
	[_PRODUCTID] 69f8c24f-2e1c-4665-820d-92d61687bd9f
	[_INFOLINK] www.lithonia.com/visual/ies/ies.asp?vfile=
	[_PRODUCTGROUP] INDOOR HID
	[_TERCAT] Highbay, Nonlinear
	[_TER] 41
	TILT=NONE
	1  16000  1  11  1  1  1  -1.4  0  0
	1  1  189
	0  5  15  25  35  45  55  65  75  85  90
	0
	8461  8664  10082  7108  4474  1272  330  106  54  39  35
Copy full snippet
```

## Usage

Use the following steps to use your own IES Profiles:

### Importing and Assigning to Lights

1. Import an IES Profile by using one of the available [import methods for textures](/documentation/en-us/unreal-engine/datasmith-import-options-in-unreal-engine): using the **Add** button, drag-and-drop, or context menu.
2. Select a [Point](/documentation/en-us/unreal-engine/point-lights-in-unreal-engine), [Spot](/documentation/en-us/unreal-engine/spot-lights-in-unreal-engine), or [Rect Light](/documentation/en-us/unreal-engine/rectangular-area-lights-in-unreal-engine) from your scene. Under the **Details** panel, assign the light profile to the **IES Texture** slot under **Light Profiles**.

   ![Assigning the light profile to the IES Texture](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/dddd4033-2b14-4638-8cb1-1c1f87a36ef6/02-ies-light-profiles-assigning-texture.png)

Using a light profile with precomputed **Static** lighting builds can potentially produce poor results due to the light profile's mask and a low lightmap resolution. Increasing the lightmap resolution of the receiving surface or using **Stationary** or **Movable** Lights produce the best result.

### Profile Light Intensity

Optionally, you can choose to use IES Profile's light intensity over the Light's **Intensity**:

![Setting up IES intensity options](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/912e21c5-509d-4a92-a583-0c71e9c6924e/03-ies-light-profiles-intensity-options.png)

* **Use IES Intensity** uses the light brightness from the profile, and when disabled will use the selected light's intensity value.
* **IES Intensity Scale** globally scales the profile's brightness contribution. This value can only be set when **Ues IES Intensity** is enabled.

### Texture Properties

When opening an IES Profile, the [Texture Editor](/documentation/en-us/unreal-engine/texture-asset-editor-in-unreal-engine) provides a couple of options under **Texture Light Profiles** that you can set:

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/88de62dc-3001-4617-9d4a-b92101e11c18/04-ies-light-profiles-texture-editor-properties.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/88de62dc-3001-4617-9d4a-b92101e11c18/04-ies-light-profiles-texture-editor-properties.png)

Click the image for full size.

| Property | Description |
| --- | --- |
| **Brightness** | The light brightness in candelas imported from the IES Profile. When enabling **Use IES Intensity** on the light and this value is less than or equal to 0, the profile will be used for masking only, causing the light to be completely masked by the profile. Also, this should be used in conjunction with the light's setting for **Inverse Squared Falloff**. |
| **Texture Multiplier** | This uneditable value is the multiplier used to map texture value to a result that is integrated over a sphere to 1.0f. |

### 3D Light Profile Visualization

When selecting a light that has an IES Texture assigned, a visualization of the light's representation will be shown.

![Without Light Selected](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ff1a4e83-733c-4e14-b78d-c5bc8673a676/05-ies-light-profiles-visualization-1.png)

![With Light Selected](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2623ca38-1def-4a6f-8efc-238770e1f70d/06-ies-light-profiles-visualization-2.png)

Without Light Selected

With Light Selected

## Additional Notes

### Performance

IES Profiles render very fast and do not have a significant effect on performance, making them a more ideal option for shaping your light than a [Light Function](/documentation/en-us/unreal-engine/using-light-functions-in-unreal-engine).

### Spot Lights

Using IES Profiles on any Point or Rect Lights turns them—visually speaking—into Spot Lights and using them on a Spot Light will operate the same way except the Spot Light's cones will mask the IES Profile effect. However, since the projection area of a Spot Light is a 179 degree arc (at its maximum), any IES data past that point is lost.

![Lights Selected](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cc2979fc-892d-4d06-baa3-66a5381e5298/07-ies-light-profiles-spot-light-visual-1.png)

![Lights Unselected](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b7d9bd4f-40e4-42f8-8ef9-9643b4cc1d06/08-ies-light-profiles-spot-light-visual-2.png)

Lights Selected

Lights Unselected

In this comparison, the IES profile emits light in all directions. When used by a Spot Light, the IES data is clipped to the Spot Light's **Cone Angle**. When used by a Point Light, the IES profile is unclipped.

### Acquiring and Previewing Light Profiles

The easiest way to acquire IES Profiles is to visit the manufacturer's website and download them, as almost all major lighting manufacturers provide them free of charge. A couple of links are provided below:

* [Lithonia Lighting](https://lithonia.acuitybrands.com/photometricdownloads)
* [Philips](http://www.usa.lighting.philips.com/support/support/literature/photometric-data)

To visualize the light's IES Profile, you can use photometric viewers, such as IESviewer, which is freely available. With it, you can select a light profile, visualize the profile and preview what it would look like before you decide to import it.

![IESviewer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/49f22471-83b6-4125-ad6a-10be09e57ef0/09-ies-light-profiles-iesviewer.png)

Image credit to Andrey Legotin.

Some manufacturer sites, such as Lithonia's site, have a built-in profile viewer that can be used in your web broswer without needing to download the profile to preview it.

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [lighting](https://dev.epicgames.com/community/search?query=lighting)
* [shadows](https://dev.epicgames.com/community/search?query=shadows)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Usage](/documentation/en-us/unreal-engine/using-ies-light-profiles-in-unreal-engine?application_version=5.7#usage)
* [Importing and Assigning to Lights](/documentation/en-us/unreal-engine/using-ies-light-profiles-in-unreal-engine?application_version=5.7#importingandassigningtolights)
* [Profile Light Intensity](/documentation/en-us/unreal-engine/using-ies-light-profiles-in-unreal-engine?application_version=5.7#profilelightintensity)
* [Texture Properties](/documentation/en-us/unreal-engine/using-ies-light-profiles-in-unreal-engine?application_version=5.7#textureproperties)
* [3D Light Profile Visualization](/documentation/en-us/unreal-engine/using-ies-light-profiles-in-unreal-engine?application_version=5.7#3dlightprofilevisualization)
* [Additional Notes](/documentation/en-us/unreal-engine/using-ies-light-profiles-in-unreal-engine?application_version=5.7#additionalnotes)
* [Performance](/documentation/en-us/unreal-engine/using-ies-light-profiles-in-unreal-engine?application_version=5.7#performance)
* [Spot Lights](/documentation/en-us/unreal-engine/using-ies-light-profiles-in-unreal-engine?application_version=5.7#spotlights)
* [Acquiring and Previewing Light Profiles](/documentation/en-us/unreal-engine/using-ies-light-profiles-in-unreal-engine?application_version=5.7#acquiringandpreviewinglightprofiles)
