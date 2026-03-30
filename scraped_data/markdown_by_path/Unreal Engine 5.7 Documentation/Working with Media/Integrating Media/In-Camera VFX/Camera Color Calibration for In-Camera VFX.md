<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/camera-color-calibration-for-in-camera-vfx-in-unreal-engine?application_version=5.7 -->

# Camera Color Calibration for In-Camera VFX

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
6. [Integrating Media](/documentation/en-us/unreal-engine/integrating-media-in-unreal-engine "Integrating Media")
7. [In-Camera VFX](/documentation/en-us/unreal-engine/in-camera-vfx-in-unreal-engine "In-Camera VFX")
8. Camera Color Calibration for In-Camera VFX

# Camera Color Calibration for In-Camera VFX

How to calibrate the display of content on the LED wall for capture with a given camera.

![Camera Color Calibration for In-Camera VFX](https://dev.epicgames.com/community/api/documentation/image/072be2ac-44a3-4758-8179-b947964e9fe7?resizing_type=fill&width=1920&height=335)

 On this page

## Overview

This document covers the steps to calibrate the display of content on the LED wall for capture with a given camera. The steps that are covered in more detail below are:

* Display a chart with known RGB values in UE using emissive unlit texture in the scene.
  + Turn off all camera-related parameters, and ensure OpenColorIO (OCIO) only has PQ encoding.
  + Set Brompton to receive PQ encoded RGB signal and interpret it as PQ Achievable, and also set wall reproduction to Achievable.
* Capture footage of the wall with the camera.
  + During the calibration step, set the white balance of the camera to 6500, and set the exposure to a value that comfortably captures the bright white patch on the wall.
* Linearize camera footage using standard methods, then converted from camera encoding color space to UE camera verification color space (used below).
* Find a matrix from known RGB to linearized verification space RGB. Invert that matrix to produce a **camera calibration matrix**.
* Display the chart again in UE. Note that it is now presumed to be in working color space.
  + Set the OCIO source to a working color space, and set the destination to a space that contains three steps:
    - Matrix conversion from reference to camera verification space.
    - Calculated camera calibration matrix application.
    - Linear to PQ encoding.
* Capture the chart again, and linearize footage to working color space. Compare the chart to the linearized footage. Preferably, this should be done analytically by means of the linear content, but could also be done by eye with the same look lut applied to both.

## Color Pipeline for In-Camera VFX

The outline above sketches the steps used to calibrate for a camera/LED wall combination. This brief preface is provided to describe the proper setup for a color pipeline from UE to LED processor.

The **Working Color Space** of Unreal Engine is not explicit. It is implicitly *Linear Rec709* (also called *Linear sRGB*). This means the encoding is linear, and the color space is Rec709 primaries and white point. It is possible to provide textures and materials in another color space, which implies to the engine that the Working Color Space is something other than Rec709. A common alternative space is *ACEScg*, which is used by many VFX studios.

The important point is that the virtual scene is linear, and that the goal is for those linear values to be represented on the LED wall. To do this, portions of the post-processing chain should be disabled (or set to 0) to ensure that none of the normal UE "camera effects" are applied to the virtual content.

The **Bloom Intensity** and **Vignette Intensity** should be set to **0.0**, as these effects are typically not desirable on the output to the LED wall. Additionally, you should set the **Expand Gamut** amount to **0.0** as well as the **Tone Curve** amount. It should be noted that the Tone Curve amount will automatically be set to zero when OCIO is active, but Expand Gamut is under user control.

The OCIO conversion requires an OCIO Configuration Asset which refers to your local OCIO config file. Additionally, this Asset has an allowlist of colorspaces from the OCIO config that are then available for use by UE. See [this page](/documentation/en-us/unreal-engine/opencolorio-quick-start-for-unreal-engine) for more info on how to associate a particular Source and Destination colorspace with a nDisplay output viewport.

* OCIO conversion from linear to signal value.
  + Source color space: Linear Working Color Space
    - This converts from the Source space to OCIO Reference space.
  + Destination color space: PQ encoded Signal Color Space
    - This converts from the OCIO Reference space to the Destination space.
  + Convert from OCIO Reference to Linear Camera Calibration Color Space.
    - Camera calibration matrix
    - Linear to PQ conversion

While it is possible to use **Post Process Materials (PPMs)** After Tonemapping when OCIO is active, they will be operating on encoded data. This can give unexpected results, because all values that are available to the PPM are in the output signal color space and color encoding.

If you need to alter the scene using a PPM, it is preferable to use it Before Tonemapping. This will ensure that the material is operating on linear values. If, for example, you wanted to provide your own color correction controls, this would be a suitable place for those operations.

## Details of OCIO conversion

The purpose of the OCIO conversion is to convert from the Working Color Space of UE to the Output Signal for the LED processor.

The camera calibration steps below presume a particular color space to determine that the calibration matches the target. We will call this **Camera Calibration Color Space**. It is possible that it is the same as the **Working Color Space**, but for flexibility it is called out separately here.

In the config.ocio file, the target space of PQ Encoded Signal Color Space involves three specific steps:

1. First, there is conversion from the OCIO Reference space to the Linear Camera Calibration Color Space.
2. Second, the camera calibration matrix is applied, which converts from the Linear Camera Calibration Color Space to Linear Signal Color Space. It should be noted that the Signal Color Space is not defined using primaries, but rather through the calibration process.
3. The third step is the encoding from Linear to PQ.

To set up the sequence of steps, a few individual OCIO color spaces need to be defined. One is the Linear Camera Calibration Color Space, which in the example below is Linear sRGB (also called Linear Rec709) and is simply named "Gamut sRGB". Another required conversion is the simple straightforward conversion from Linear to PQ. This conversion assumes that a linear value of 1.0 has a nit value of 100, which is then followed by the standard 0-10000 conversion to a 0-1 encoded value.

```
	 - !<ColorSpace>
		name: Gamut - sRGB
		family: Gamut
		equalitygroup: ""
		bitdepth: 32f
		description: |
		  "BT.709 / sRGB" colorspace primaries and "D65" whitepoint as per "IEC 61966-2-1:1999".
		isdata: false
		allocation: lg2
		allocationvars: [-8, 7, 0.00390625]

	 - !<ColorSpace>
		name: CCTF - PQ
		family: CCTF
		equalitygroup: ""
		bitdepth: 32f
		description: |
		  "PQ" color component transfer function as per "SMPTE ST 2084". Assumes scene value of 1.0 corresponds to 100 nits.
		isdata: false
		allocation: uniform
		allocationvars: [0, 1]
		to_reference: !<GroupTransform>
		  children:
			- !<FileTransform> {src: Dolby_PQ_10000_to_linear.spi1d, interpolation: linear}
			- !<CDLTransform> {slope: [100, 100, 100], direction: inverse}
Copy full snippet
```



The OCIO Linear Reference space is the same as the Linear Camera Calibration space in this example, so there is no color conversion needed in the Gamut sRGB space.

The actual target color space is the conversion to the Encoded Signal Color Space, as shown here. The conversion includes a Color Matrix followed by an encoding from Linear to PQ. The derivation of this Color Matrix is described later. The values in the Matrix Transform below are only shown as an example; these values must be replaced by the calibration done for your particular LEDs and camera.

```
	 - !<ColorSpace>
		name: View - Camera on LED Walls - PQ
		family: View
		equalitygroup: ""
		bitdepth: 32f
		description: |
		  View for content on LED Walls (via camera calibration calcs) assuming input in OCIO Reference, then encoding to PQ "ST 2084" HDR color component \ transfer function. Assumes scene value 1.0 corresponds to 100 nits.
		isdata: false
		allocation: uniform
		allocationvars: [0, 1]
		from_reference: !<GroupTransform>
		  children:
			- !<MatrixTransform> {matrix: [0.80252942, 0.12102891, 0.07644168, 0, 0.05176983, 0.89236679, 0.05488673, 0, 0.01495024, 0.07238952, 0.88267732, 0, 0, 0, 0, 1]}
			- !<ColorSpaceTransform> {src: Gamut - sRGB, dst: CCTF - PQ}
Copy full snippet
```

## Scene Exposure

Because the linear values are encoded as PQ and the values are interpreted in a canonical 0-10000 nit range, the exposure of the scene must be adjusted before the OCIO conversion. This can be done by means of the Exposure control in the CineCamera or PostProcess Volumes. The important note here is to make a correspondence between the virtual scene luminances and the eventual brightness on the LED wall.

Typically, a linear scene contains HDR values. While the majority of scene values will hover around a 100 nits luminance value, portions can be much brighter, with some pixels attempting to be 2000 or 3000 nits. For most LED walls, these brightnesses are beyond the capability of the LED panels. The result on the wall will be the same bright value for pixels that may be different in the scene, because the peak presentable value on the LEDs is likely to be 1500-1800 nits. For example, if the peak brightness of LEDs is 1600 nits, that would correspond to a scene linear value of 16.0 after the exposure compensation.

## Camera Calibration Matrix

The purpose of the camera calibration matrix is to ensure that there is a match between virtual scene linear colors and the colors produced from linearization of the camera footage.

For background, it should be noted that a camera has a unique set of spectral responses, and those differ by brand of camera, and also are different from the human eye. Because LEDs have a rather narrow spectral distribution, the subtle differences in camera responses can cause photographed LEDs to appear different in the resulting footage of different cameras. To reduce this issue, we desire to change the pixels on the LED wall slightly so that the linearized footage from any particular camera will match the values that were represented in the scene.

To create the matrix, a minimum of four color values must be displayed by UE. Those four values are red, green, blue, and white patches, where the resulting pixels on the wall are captured by the camera. For this to work properly, the LED processor should be set up to produce native color on the wall. In the case of Brompton processors, this is called Achievable. Other vendors may call this Native. The goal of using this color space is that the calibration attempts to use the full capability of the wall, without clipping the color values. Additionally, the color encoding should be set to be the same color encoding that will be used for eventual shooting. For our Brompton setup, we used the PQ encoding.

In actual practice, we used more patches to confirm that the overall behavior is as expected. But the calibration calculation only requires four patches.

The following is the basic method to create a camera calibration matrix. Note that there are concerns and possible issues that are discussed later.

### Display a Scene Linear Chart

Display a scene linear chart in UE using a geometric plane object, and a shader that displays the patch values in Unlit mode. The values can be pulled from a known texture file or from math within the plane's shader Material.

The chart should contain a red, green, blue, and white patch that have known scene brightness values. The simplest example would be (1.0, 0.0, 0.0) for red, and similar values for the other patches. By adjusting UE Exposure, the chart should be displayed to have a particular target brightness on the LED wall. The brightness should approach the peak value of the wall, but should be slightly below peak to avoid any color shift that occurs due to clipping.

The chart should be large enough to comfortably allow sampling of each patch in the resulting footage, but should also be centered and small enough to avoid regions of falloff that occur due to lens vignette.

The OCIO conversion should be enabled when the charts are displayed. The conversion used should be similar to the eventual goal conversion, but would only be the conversion from Linear to PQ (without a calibration matrix, since we are creating that with this step).

### Linearize Footage for the Vendor

The footage should be linearized using standard methods for the particular vendor. For example, for a Sony Venice, the footage should be linearized using the Sony XOCN F55 ST codec. The data is SLog3 encoded in the SGamut3-Cine color space. For our simple example, we linearized to Rec709 Gamut using the Read node in Nuke12.

It is important to note which method is used to linearize the footage, and to verify that the result is truly linear. In our example, we linearized to Rec709. This term can be misleading, however, because many users speak about a Rec709 camera output which normally has a look lut applied to the content. For this calibration purpose, our goal is to capture in native camera format with no look applied, and to convert that to linear using standard methods.

The white patch should be mostly neutral, assuming the camera was set to 6500K white balance. If the white patch is heavily tinted there may be issues that need to be resolved before proceeding.

### Matrix Creation Math

The next segment is the math for how the matrix is created from the sample data for R,G,B,W.

First, a 3x3 matrix is made from the red, green, and blue patch samples:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | RR | GR | BR |
| F | = | RG | GG | BG |
|  |  | RB | GB | BB |

I = F-1

Using the inverse of that matrix, multiply it by the white sample, where the highest value has been normalized to 1.0:

S = I × W/max(WRGB)

Use the calculated scale factors to scale the F matrix, then calculate its inverse.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  |  | SR | 0 | 0 |  |  |
| F | = | 0 | SG | 0 | x | F |
|  |  | 0 | 0 | SB |  |  |

CalibrationMX = F-1

### Place Calibration Matrix in OCIO Conversion

The resulting calibration matrix should be placed in the OCIO conversion for the wall/camera combination as was shown earlier. It should be noted that the matrix is presented as nine numbers in order such that the first row of the matrix is given, then the second, then the third row.

In the example above, the OCIO Reference Color Space was Rec709. This matched the color space used for linearization during calibration. If you choose to use a different OCIO Reference Color Space, the Calibration Matrix must include a conversion from the Reference Color Space to the Rec709 space used for linearization of the camera footage. This was noted in the outline above as "Matrix conversion from reference to camera verification space".

## Calibration Verification

It is useful to confirm that the camera calibration matrix is active and behaving properly. To do this, display known patches using the same method as was used for the initial capture, except the color space target should include the newly created calibration matrix.

The goal is that the known patch values in scene linear space match the values found in the footage after linearization back to the same working space.

Earlier, the required patches were simply R, G, B, and W. For verification, it is helpful to include values that are at known locations between 0 and 1. This image shows a 5x5x5 collection of patches that are separated by 0.25, resulting in an even spacing of samples in linear space.

![Calibration patches for full verification](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/91be23c3-0d68-4f23-a56d-cd00a52303f4/camera-calibration-patches.png)

The reason to include more samples than just RGBW is that the linearized footage of this image will help confirm whether you have clipping due to brightness (or other such concerns).

* [virtual production](https://dev.epicgames.com/community/search?query=virtual%20production)
* [in-camera vfx](https://dev.epicgames.com/community/search?query=in-camera%20vfx)
* [opencolorio](https://dev.epicgames.com/community/search?query=opencolorio)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Overview](/documentation/en-us/unreal-engine/camera-color-calibration-for-in-camera-vfx-in-unreal-engine?application_version=5.7#overview)
* [Color Pipeline for In-Camera VFX](/documentation/en-us/unreal-engine/camera-color-calibration-for-in-camera-vfx-in-unreal-engine?application_version=5.7#colorpipelineforin-cameravfx)
* [Details of OCIO conversion](/documentation/en-us/unreal-engine/camera-color-calibration-for-in-camera-vfx-in-unreal-engine?application_version=5.7#detailsofocioconversion)
* [Scene Exposure](/documentation/en-us/unreal-engine/camera-color-calibration-for-in-camera-vfx-in-unreal-engine?application_version=5.7#sceneexposure)
* [Camera Calibration Matrix](/documentation/en-us/unreal-engine/camera-color-calibration-for-in-camera-vfx-in-unreal-engine?application_version=5.7#cameracalibrationmatrix)
* [Display a Scene Linear Chart](/documentation/en-us/unreal-engine/camera-color-calibration-for-in-camera-vfx-in-unreal-engine?application_version=5.7#displayascenelinearchart)
* [Linearize Footage for the Vendor](/documentation/en-us/unreal-engine/camera-color-calibration-for-in-camera-vfx-in-unreal-engine?application_version=5.7#linearizefootageforthevendor)
* [Matrix Creation Math](/documentation/en-us/unreal-engine/camera-color-calibration-for-in-camera-vfx-in-unreal-engine?application_version=5.7#matrixcreationmath)
* [Place Calibration Matrix in OCIO Conversion](/documentation/en-us/unreal-engine/camera-color-calibration-for-in-camera-vfx-in-unreal-engine?application_version=5.7#placecalibrationmatrixinocioconversion)
* [Calibration Verification](/documentation/en-us/unreal-engine/camera-color-calibration-for-in-camera-vfx-in-unreal-engine?application_version=5.7#calibrationverification)
