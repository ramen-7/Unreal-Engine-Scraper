<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/projection-policies-in-ndisplay-in-unreal-engine?application_version=5.7 -->

# Projection Policies in nDisplay

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
7. [Rendering to Multiple Displays with nDisplay](/documentation/en-us/unreal-engine/rendering-to-multiple-displays-with-ndisplay-in-unreal-engine "Rendering to Multiple Displays with nDisplay")
8. Projection Policies in nDisplay

# Projection Policies in nDisplay

Reference for policies supported in Unreal Engine for multiple screen displays

![Projection Policies in nDisplay](https://dev.epicgames.com/community/api/documentation/image/7e6e3b4a-fafb-4f4e-977d-7dc809abd261?resizing_type=fill&width=1920&height=335)

 On this page

## Projection Policies in nDisplay

As part of the development strategy for new features, Epic Games is constantly evaluating existing tools that could add functionality to Unreal Engine. After much research, we found the following technologies to help us achieve our goals for scaled displays.

## Simple

*Simple* refers to the standard policy used to render on regular 2D flat displays. This policy requires a rectangle in 3D space to be used to build camera frustum. The rectangle (*screen*) must be defined in the Components panel, then referenced in the simple projection policy section on the viewport's Details panel.

Follow the steps below to use the Simple policy in your project.

1. Open your nDisplay Config Asset in the [nDisplay 3D Config Editor](/documentation/en-us/unreal-engine/ndisplay-3d-config-editor-in-unreal-engine).
2. In the **Components** panel, select **Add Component** and choose **NDisplay Screen**.

   ![Add nDisplay Screen component](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/605d19a9-8658-4f69-8be7-828d879807fd/01-ndis-scr.png)
3. In the **Cluster** panel, select **Add New Viewport**.
4. In the Add New Viewport window under **Configuration > Projection Policy**, modify the following fields:
   * Set **Type** to **simple**.
   * Set **Screen** to the screen component that you created in Step 2. In this example, the screen was named nDisplayScreen.

     ![Configuration Projection Policy settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0afe54a5-e707-407c-9e37-981b4acba5a5/02-ndisplay-sim.png)
5. Verify the screen is rendering the Viewport correctly. You may need to set the **View Origin** in the Viewport's **Details** panel to see the test scene.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f7aca1fd-34ce-492a-9e26-6d05770d1dbd/03-ndisplay-det.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f7aca1fd-34ce-492a-9e26-6d05770d1dbd/03-ndisplay-det.png)

   Click image to expand

## Camera

Since it is impossible to get a view from a regular Unreal Engine camera or cine camera with nDisplay, the camera policy was introduced. This policy allows you to map a view of any UE4 camera to the nDisplay viewport.

Follow the steps below to use the Camera policy in your project.

1. Open your nDisplay Config Asset in the [nDisplay 3D Config Editor](/documentation/en-us/unreal-engine/ndisplay-3d-config-editor-in-unreal-engine).
2. In the **Components** panel, select **Add Component** and choose one of the Camera components: **ICVFX Camera**, **Camera**, or **Cine Camera**.

   ![Add a Camera component](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/05799a0c-81b7-4dd6-a17e-62103df9e293/04-camera-fold.png)
3. In the **Cluster** panel, select **Add New Viewport**.
4. In the Add New Viewport window under **Configuration > Projection Policy**, modify the following fields:
   * Set **Type** to **camera**.
   * Set **Camera** to the camera that you created in Step 2. In this example, the camera was named ICVFXCamera.
   * Choose the setting for Use nDisplay Renderer. By default, this enables the nDisplay render path for clustered rendering. When disabled, the nDisplay renderer is bypassed and displays native UE pixels for this specific camera. Disable this for debugging purposes or to compare native camera rendering vs nDisplay cluster rendering.

     ![Configure the Projection Policy for your camera](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/078d4cbe-06d3-4623-96fd-597c378431d4/05-icvfxcam.png)
5. Verify the camera is rendering the viewport correctly.

   ![Camera rendering the Viewport](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3556e4d2-5fce-477f-bb37-044fac96fabd/15-cam-projection.gif)

## Manual

As a generic solution for those systems that are not yet supported by nDisplay, a new *manual projection policy* was introduced. The key idea is that the user explicitly sets a view frustum for a particular viewport.
For stereo rendering, two frustums are required. This can be done either via projection matrix or frustum angles. For more details on the difference between Mono and Stereo Rendering in nDisplay, see [Stereoscoping Rendering in nDisplay](/documentation/en-us/unreal-engine/stereoscopic-rendering-with-ndisplay-in-unreal-engine).

Follow the steps below to use the Manual policy in your project.

1. Open your nDisplay Config Asset in the [nDisplay 3D Config Editor](/documentation/en-us/unreal-engine/ndisplay-3d-config-editor-in-unreal-engine).
2. In the **Cluster** panel, select **Add New Viewport**.
3. In the **Add New Viewport** window under **Configuration > Projection Policy**, modify the following fields:
   * Set **Type** to **Manual**.
   * Set **Rendering** to **Mono**, **Stereo**, or **Mono&Stereo**.
   * Set **Frustum** to **Matrix** or **Angles**
     + For **Frustum Matrix**: Set the **Rotation** and **Matrix** fields (or **MatrixLeft** and **MatrixRight** if you picked **Stereo** instead of **Mono**).

       ![Frustrum Matrix settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2d024dfb-ade3-4e2a-b1b5-5b43edf1ee4c/06-man-mon-mat.png)
     + For **Frustum Angles**: Set the **Rotation** and **Frustum** fields (or **FrustumLeft** and **FrustumRight** if you picked **Stereo** instead of **Mono**).

       ![Frustrum Angles settings](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0825b432-2b11-4104-9837-157630a5fdce/07-man-mon-angl.png)
4. Verify the viewport is rendering correctly.

## Mesh

This projection policy simplifies warp-rendering workflows. Instead of a *PFM (portable float map) workflow*, it is now possible to simply assign a mesh to effectively warp the rendered output. You can use either an **NDisplayScreen**, which creates a 2D display regardless of ratio and pixel density, or a **StaticMesh** Component, which can be a screen of an arbitrary shape and form, to specify the shape of the rendered output. The UV channel 0 is used for warp mapping.

Follow the steps below to use the Mesh policy in your project.

1. Open your nDisplay Config Asset in the [nDisplay 3D Config Editor](/documentation/en-us/unreal-engine/ndisplay-3d-config-editor-in-unreal-engine).
2. In the **Components** panel, select **Add Component** and choose either **NDisplayScreen** or **StaticMesh**.
3. In the **Cluster** panel, select **Add New Viewport**.
4. In the **Add New Viewport** window under **Configuration > Projection Policy**, modify the following fields:
   * Set **Type** to **Mesh**
   * Set **Mesh** to the Component you created in Step 2. In this example, it's assigned to a StaticMesh with the name SM\_Screen\_0.

     ![Configure the Projection Policy for your mesh](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d730e607-8541-4708-ae86-02cf29d47138/08-mesh-sm-screen.png)
5. Verify the viewport is rendering correctly on the mesh. You may need to set the **View Origin** in the Viewport's **Details** panel to see the test scene.

   [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/27d7722b-9849-4f51-9188-e7aa02200682/09-mesh-sm-screen-det.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/27d7722b-9849-4f51-9188-e7aa02200682/09-mesh-sm-screen-det.png)

   Click image to expand

## MPCDI

An integration of the MPCDI standard is used for complex projects that rely on this industry protocol.

The *MPCDI (Multiple Projection Common Data Interchange)* standard was developed by the VESA Multi-Projector Automatic Calibration (MPAC) Task Group. This is a standard data format for projection calibration systems to communicate with devices in a multi-display configuration.

The standard provides a way for multi-projector systems to generate the data needed to combine individual display components into a single, seamless image by a variety of devices. Any new hardware introduced into a system can be easily integrated with the standard.

MPCDI is used throughout the industry by content producers and vendors such as:

* Scalable Display Technologies
* VIOSO
* Dataton Watchout
* 7thSense Design

Support for the MPCDI standard enables nDisplay to read and store data describing a complex projector system in a standardized and formalized fashion, so that we can easily communicate and interface with various other tools from within the industry. MPDCI is supported in the Editor Preview and Overscan.

There are two ways to use mpcdi projection policy. The first is a native approach where the user has to specify the .mpcdi file, buffer, and region to use. The second is where the user explicitly specifies files stored in .mpcdi (which is basically a file archive).

### Using the .mpcdi File

Follow the steps below to use a native approach for the MPCDI policy in your project.

1. Open your nDisplay Config Asset in the [nDisplay 3D Config Editor](/documentation/en-us/unreal-engine/ndisplay-3d-config-editor-in-unreal-engine).
2. In the **Cluster** panel, select **Add New Viewport**.
3. In the **Add New Viewport** window under **Configuration > Projection Policy**, modify the following fields:
   * Set **Type** to **MPCDI**.
   * Set **MPCDI Type** to **MPCDI**.
   * Next to **File**, browse to the `.mpcdi` file on your computer.
   * Set **Buffer** to the name of the buffer in the `.mpcdi` file.
   * Set **Region** to the name of a region within the `.mpcdi` file's buffer.

     ![Configure the Projection Policy for MPCDI](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ac22fe0a-e17d-4713-9c77-5e11228116c0/10-mpcdi-mpcdi.png)
4. Verify the viewport is rendering correctly.

### Explicit Specification

Follow the steps below to explicitly specify how to use the MPCDI policy in your project.

1. Open your nDisplay Config Asset in the [nDisplay 3D Config Editor](/documentation/en-us/unreal-engine/ndisplay-3d-config-editor-in-unreal-engine).
2. In the **Cluster** panel, select **Add New Viewport**.
3. In the **Add New Viewport** window under **Configuration > Projection Policy**, modify the following fields:
   * Set **Type** to **MPCDI**.
   * Set **MPCDI Type** to **Explicit PFM**.
   * Next to **File**, browse to the `.pfm` file that represents warp geometry on your computer.
   * Next to **Alpha Mask**, browse to the `.png` file that represents the alpha mask on your computer.
   * Set the **Alpha Gamma** field to the associated alpha masks's gamma value. Alpha masks with no gamma can use a value of 1.0, which would be equivalent to linear.
   * Next to **Beta Mask**, browse to the `.png` file that represents the beta mask on your computer.
   * Set the **Scale** field to the geometry scale used in the `.pfm` file.
   * Enable **Use Unreal Axis** if you want to use Unreal's axis.

     ![Configure the Projection Policy for Explicit MPCDI](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/691d2441-cfc6-4570-a4e1-18923757ea46/11-mpcdi-explicit.png)
4. Verify the viewport is rendering correctly.

## EasyBlend (Scalable Display)

Integration of *EasyBlend* calibration data is done with a *Scalable SDK* that enables warp, blend, and keystoning features. This meets the requirement to display on non-planar and complex display surfaces, such as curved or dome-shaped surfaces, using multi-projectors.

*Scalable Display Technologies* is a company that focuses on software and SDKs for complex projection systems. Their SDK is designed to provide a solution for large displays of a single image through warping and blending. Since Scalable Display Technologies already had the EasyBlend solution in place to handle warping and blending of large images, we chose to integrate it with Unreal Engine.

The Unreal Engine nDisplay supports warp and blend through the integration of the industry-standard middlewares Scalable SDK and EasyBlend for all supported modes, native warp and blend with MPCDI, and custom implementations.

We implemented the integration of EasyBlend to provide a seamless experience in configuring a complex projective system. Once calibration is completed using the third-party tool or software, the user only needs to specify a few parameters in the nDisplay configuration file to get it running.

Follow the steps below to use the EasyBlend policy in your project.

1. Open your nDisplay Config Asset in the [nDisplay 3D Config Editor](/documentation/en-us/unreal-engine/ndisplay-3d-config-editor-in-unreal-engine).
2. In the **Cluster** panel, select **Add New Viewport**.
3. In the **Add New Viewport** window under **Configuration > Projection Policy**, modify the following fields:
   * Set **Type** to **EasyBlend**.
   * Next to **File**, browse to the `.pol` file on your computer.
   * Set the **Origin** and **Scale** fields.

     ![Configure your Projection Policy for EasyBlend](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/fb905489-86c2-4697-b9d0-85df0da79957/12-easyblend.png)
4. Verify that the viewport rendering is properly deformed in regards to the provided EasyBlend calibration files. The render result should match the reference images from the vendor.

## VIOSO

Native SDK integration of VIOSO calibration data is available for projector warping and soft edge blending on complex surfaces.

Once calibration is completed using VIOSO's tools and software, follow the steps below to use the VIOSO policy in your project.

1. Open your nDisplay Config Asset in the [nDisplay 3D Config Editor](/documentation/en-us/unreal-engine/ndisplay-3d-config-editor-in-unreal-engine).
2. In the **Cluster** panel, select **Add New Viewport**.
3. In the **Add New Viewport** window under **Configuration > Projection Policy**, modify the following fields:
   * Set **Type** to **VIOSO**.
   * Next to **File**, browse to the `.vwf` file on your computer.
   * Set the **Origin** and **Matrix** fields.

     ![Configure the Projection Policy for VIOSO](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ac0e947f-b14e-4735-bc52-5c12452c2821/13-vioso.png)
4. Verify that the viewport rendering is properly deformed in regards to the provided VIOSO calibration files. The render result should match the reference images from the vendor.

## DomeProjection

Native SDK integration of *DomeProjection* calibration data is available for projector warping and soft edge blending on massive dome surfaces. Once calibration is completed using DomeProjection's tools and software, add a couple parameters to the nDisplay configuration file to use it in your project.

1. Open your nDisplay Config Asset in the nDisplay 3D Config Editor.
2. In the **Cluster** panel, select **Add New Viewport**.
3. In the **Add New Viewport** window under **Configuration > Projection Policy**, modify the following fields:
   * Set **Type** to **DomeProjection**.
   * Next to **File**, browse to the `.xml` file exported from DomeProjection's software on your computer.
   * Set the **Origin** and **Channel** fields.

     ![Configure the Projection Policy for DomeProjection](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/60fac368-1fa8-4ca3-b36e-4a2d4325d424/14-domeprojection.png)
4. Verify that the viewport rendering is properly deformed in regards to the provided DomeProjection calibration files. The render result should match the reference images from the vendor.

* [rendering](https://dev.epicgames.com/community/search?query=rendering)
* [vfx](https://dev.epicgames.com/community/search?query=vfx)
* [graphics](https://dev.epicgames.com/community/search?query=graphics)
* [ndisplay](https://dev.epicgames.com/community/search?query=ndisplay)
* [projection policies](https://dev.epicgames.com/community/search?query=projection%20policies)
* [multiple screen projection](https://dev.epicgames.com/community/search?query=multiple%20screen%20projection)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Projection Policies in nDisplay](/documentation/en-us/unreal-engine/projection-policies-in-ndisplay-in-unreal-engine?application_version=5.7#projectionpoliciesinndisplay)
* [Simple](/documentation/en-us/unreal-engine/projection-policies-in-ndisplay-in-unreal-engine?application_version=5.7#simple)
* [Camera](/documentation/en-us/unreal-engine/projection-policies-in-ndisplay-in-unreal-engine?application_version=5.7#camera)
* [Manual](/documentation/en-us/unreal-engine/projection-policies-in-ndisplay-in-unreal-engine?application_version=5.7#manual)
* [Mesh](/documentation/en-us/unreal-engine/projection-policies-in-ndisplay-in-unreal-engine?application_version=5.7#mesh)
* [MPCDI](/documentation/en-us/unreal-engine/projection-policies-in-ndisplay-in-unreal-engine?application_version=5.7#mpcdi)
* [Using the .mpcdi File](/documentation/en-us/unreal-engine/projection-policies-in-ndisplay-in-unreal-engine?application_version=5.7#usingthempcdifile)
* [Explicit Specification](/documentation/en-us/unreal-engine/projection-policies-in-ndisplay-in-unreal-engine?application_version=5.7#explicitspecification)
* [EasyBlend (Scalable Display)](/documentation/en-us/unreal-engine/projection-policies-in-ndisplay-in-unreal-engine?application_version=5.7#easyblend(scalabledisplay))
* [VIOSO](/documentation/en-us/unreal-engine/projection-policies-in-ndisplay-in-unreal-engine?application_version=5.7#vioso)
* [DomeProjection](/documentation/en-us/unreal-engine/projection-policies-in-ndisplay-in-unreal-engine?application_version=5.7#domeprojection)
