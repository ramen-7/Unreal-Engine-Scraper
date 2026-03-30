<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/realtime-compositing-tools-in-unreal-engine?application_version=5.7 -->

# Legacy Real-Time Compositing Tools

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
7. [Real-Time Compositing with Composure](/documentation/en-us/unreal-engine/realtime-compositing-with-composure-in-unreal-engine "Real-Time Compositing with Composure")
8. Legacy Real-Time Compositing Tools

# Legacy Real-Time Compositing Tools

Product documentation including reference and guides for Unreal Engine

![Legacy Real-Time Compositing Tools](https://dev.epicgames.com/community/api/documentation/image/61764d17-d8f2-4e1a-8344-e4416846252d?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

The process of compositing imagery together in Unreal Engine (UE) is handled by using our real-time compositing plugin **Composure**. It enables you to combine visual elements from different sources, such as computer generated (CG) or real-world sources to layer together into a single, seamlessly blended image while working in-Editor or in-game. For Film and Television, the visual effects (VFX) industry, compositing a single frame has primarily been an offline process, up to this point, with each frame taking some time to render.

When you start compositing with previsualization in mind, it's especially helpful in enabling directors—or other creatives working on set—get a sense of what the final render will look like, even helping alter performances or how a shot it set up. For compositors, previsualization can be used as a guide for completing their work in other third-party industry standard software, like Nuke or Fusion.

## Enabling the Composure Plugin

To access the Composure compositing tools, go to the **Edit** menu and open the **Plugins** browser. Under the **Compositing** category, enable **Composure** and restart the Editor for the changes to take effect.

[![Enable the Composure Plugin](https://dev.epicgames.com/community/api/documentation/image/6d2b8854-2a7c-443d-94da-efb7f22604c3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6d2b8854-2a7c-443d-94da-efb7f22604c3?resizing_type=fit)

## Compositing Tree Panel

Once the Composure plugin is enabled, access the **Composure Compositing** panel from the **Window > Virtual Production** menu.

[![Compositing Tree Panel](https://dev.epicgames.com/community/api/documentation/image/102ceab3-d001-4d54-9f2e-00ebdf4b457e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/102ceab3-d001-4d54-9f2e-00ebdf4b457e?resizing_type=fit)

Use the panel to build a hierarchy of compositing **Elements**. These elements are objects responsible for rendering a piece of your composite scene. For example, the hierarchy above is made up of a Composition named "My\_Composite." It has three Elements named "FG\_Element," "BG\_Element," and "Media\_Plate." Each element contains a different part of the scene that is composited together. FG\_Element and BG\_Element are **CG Layer** elements that contain both foreground and background objects from the scene. Media\_Plate is a **Media Plate** layer that is used for video input into the compositing pipeline.

When right-clicking in the Composure Compositing panel, add your own composite by selecting **New Comp Shot**.

[![Add New Comp Shot](https://dev.epicgames.com/community/api/documentation/image/2f7b268d-9017-4434-a4f2-bebd9d1751bd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2f7b268d-9017-4434-a4f2-bebd9d1751bd?resizing_type=fit)

When right-clicking on the Composition Shot, new elements are added by selecting **Add Layer Element** and selecting the type of element you want to add from the **Pick an Element Type** selection window.

[![Add Layer Element](https://dev.epicgames.com/community/api/documentation/image/ac9a6c62-ced3-439c-9207-fe2ac8278186?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ac9a6c62-ced3-439c-9207-fe2ac8278186?resizing_type=fit)

Elements can be nested under one another in a hierarchical structure to determine which Elements are available for cross-Element use in ones found higher in the hierarchy tree. Keep in mind that Elements are just Actors within the Level and can be added like any other Actor. The panel provides a way to nest these Elements for organization and exposes some controls to make them easier to use.

For portability and ease of use within the scene, be sure that your Elements are added to their own sub-Level. Since they are Level Actors, it lets you load your compositing tree in other Levels that you would potentially open.

## Anatomy of the Composure Compositing Panel

[![Composure Anatomy](https://dev.epicgames.com/community/api/documentation/image/a68d1e52-cafb-4320-b871-a60b85a1ff5e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a68d1e52-cafb-4320-b871-a60b85a1ff5e?resizing_type=fit)

Composure Anatomy

*Click image to expand.*

1. The **Element Row** is made up of a Composition Shot composed of Elements composited within the scene. It has a row representing each layer in the currently loaded map.
2. The **Element Name** is a unique name given to each added Layer Element and is used to reference the specific Element found in the Compositing Material Graphs.
3. Each Composition Shot or Layer Element can be toggled on or off using the **Eye** button.
4. The **Alpha** box controls how opaque the selected Composition Shot or Layer Element is. Enter a value in the text box or click the drop-down and use the slider to control its visibility.
5. The **Lock** toggles freeze framing the Element. For animations or video streaming in, it lets you pause the Element's rendering, freezing its position.
6. The **Media Output** toggle lets you turn on/off the selected Composition Shot or Layer Element render result. Toggling this on for the first time prompts you to pick (or create) a **Media Output Definition** Asset. Provide the Asset details of your Target Output (such as a card or port).
7. When selecting a Composition Shot or Layer Element, the properties and attributes of the Element will be available from the Level **Details** panel. Compositing specific settings are found under the **Composure** category.
8. When selecting a Composition Shot or Layer Element, the **Element Preview Pane** appears in the Level Viewport, like a Camera Actors preview pane would. It displays the render for the selected Element and also shows error messages when the Element is in a bad state. For example, it displays "Empty" if there is no information to display.

   Elements are processed in linear color space. By default, the preview is displayed with a linear to sRGB conversion and displays the images without tonemapping, which consequently makes them appear blown out. However, you have the option to change how Elements are previewed, such as adding your own tonemapping through a custom Material.

## Compositing Elements

**Elements** are the individual building blocks used to construct a composited image which can be the Composition Shot or the individual Layer Elements. Each one makes up the composited image made up of layers or Level Actors that are individually responsible for rendering a piece of the composite scene. Layer Actors are individually responsible for rendering a piece of the composited scene.

### Internal Passes

Each Element has a set of internal passes it performs. These are a sequential set of steps unique to that Element type. Each pass is a distinct step in rendering the Element in the composite. An Element without any passes does nothing. There are many different kinds of passes available and there are certain Element archetypes that come with their own predefined passes. For example, the Media Plate Element comes with Chroma Key and Despill passes already built in.

### Anatomy of an Element

When selecting an Element in the Composure Compositing Tree window, the **Details** panel in the Level will display information and properties for this selected Element.

[![Element Anatomy](https://dev.epicgames.com/community/api/documentation/image/9b1e9638-352f-4202-8ae5-26acb9f19eb4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9b1e9638-352f-4202-8ae5-26acb9f19eb4?resizing_type=fit)

Element Anatomy

*Click image to expand.*

1. The **Inputs** attribute enables some elements to access a resource outside of the compositing system, such as using a Media texture for video input. They provide a way to route dependencies to the Element and act as a special kind of pass that can be referenced by other subsequent passes and some Element types that come with predefined inputs.
2. The **Target Camera Actor** enables some Element types that need a point of view for reference to use a Camera Actor in the Level. If left undefined, the Element searches the Level for the first Camera Actor it can find and assigns it. This can be overridden for individual elements, or let it inherit from the root Element.
3. **Transforms** are passes that take an input of some kind and alters it or uses it to generate something new. For example, color transforms take an image from one color space and puts it in another. The last transform in this list produces the Elements final render result.
4. There are many types of **Passes**, such as chroma key, despill, or even custom ones that can be added. They all share some properties but may also contain ones unique to that pass.

   1. The **Enabled** flag toggles a pass on and off. When disabled, the pass behaves as though the pass were not there.
   2. The **Pass Name** feeds in name that can be referenced by subsequent passes.

      A pass must be uniquely named if it's to be referenced in a Material.
   3. The **Intermediate** flag controls whether subsequent passes use it. By default, it is assumed that you only need it for the next pass. After that, its render target is released so that it can be used by another pass. If you need the pass result to be accessible longer, disable this flag.

      Rendering for Elements and passes uses a shared render target pool. Each frame all targets are returned to the pool and redistributed. Unused targets in the pool get flushed.
5. **Outputs** are another form of pass, they don't contribute to the Element's render result. Instead, they route the result of the pass somewhere else, such as a video capture card or to the player viewport.
6. The **Render Resolution** defines the resolution output of the Element. It can be overridden or inherited from a parent and some passes have the option to override or scale this setting.
7. In the **Preview Transforms**, elements are processed in their linear color space. By default, they are previewed without any kind of tonemapping, which can cause their color to appear blown out. The optional transform on the Element enables you to adjust how the image is previewed in the Editor.
8. The **Auto Run** flag toggles the Element, preventing it from running (or rendering). The flag state is reflected by the eye icon in the Composure Compositing panel's tree view as well.

## Compositing Material

The following sections detail how parts of the compositing pipeline work and come together in UE.

For a step-by-step guide to creating a basic composition with composure, see the [Composure Quick Start](working-with-media/integrating-media/Composure/QuickStart).

### Nesting Elements

Elements can be nested under one another and while any kind of Element can be placed in the hierarchy, you should put the final composition at the top with its layer elements listed below it. To add a new nested Element, right click on the desired parent element and select **Add Layer Element** from the context menu. Then, choose the type of Element you want to add from the window.

Nesting elements determines the render order of the Elements used in the composition. The parent element is rendered last and everything under is rendered beforehand. Parent elements can use the render result from their children in their own render passes.

### Compositing Element Material Pass

The **Compositing Element Material Pass** is a transform pass that lets you add a user authored Material to the compositing pipeline. In the Material you can reference sub-elements by name.

[![Compositing Element Material Pass](https://dev.epicgames.com/community/api/documentation/image/b7b71b03-28bc-488d-b290-c4f03a32e7a1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b7b71b03-28bc-488d-b290-c4f03a32e7a1?resizing_type=fit)

Compositing Element Material Pass

*Click image to expand.*

### Referencing Elements in Your Material

In your Material, create a **Texture Parameter** and have it auto-filled with a child Element's render result. Name the parameter the same as the sub-Element found in the compositing tree.

[![Referencing Elements in the Material](https://dev.epicgames.com/community/api/documentation/image/9436c0d8-5606-4758-9cd0-c5da3de5e8c3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9436c0d8-5606-4758-9cd0-c5da3de5e8c3?resizing_type=fit)

Referencing Elements in the Material

*Click image to expand.*

Since only a single color is needed for output, Post Process Materials are used for compositing these materials. Enable the **Output Alpha** for Post Process Materials, if needed.

Use the Details panel to plug this Material into the **Material** slot. If everything is set up correctly, it should start working in the viewport preview.

[![Custom Material Applied](https://dev.epicgames.com/community/api/documentation/image/3de4054f-b4a4-42da-b62f-ccb032241741?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3de4054f-b4a4-42da-b62f-ccb032241741?resizing_type=fit)

If you're not seeing the preview show the child Element, double-check that the name match exactly. Typos or extra spaces can cause this to fail.

If the sub-Element is disabled and not rendering, the Texture Parameter is filled with a transparent black texture. If the named Element cannot be found, the texture will use the default texture from the Material.

#### Making Materials Portable

Referencing your Element by name in the Material is easy enough, but it makes your Material very specialized; it will only work with Element having specific names. Alternatively, give your Material Texture Parameter a generic name and set it to reference a sub-Element in the Pass's properties.

[![Custom Material Pass Inputs](https://dev.epicgames.com/community/api/documentation/image/be88dc1a-6ce0-4c0d-9df9-ad178f4da6ee?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/be88dc1a-6ce0-4c0d-9df9-ad178f4da6ee?resizing_type=fit)

Custom Material Pass Inputs

*Click image to expand.*

Once a Material is set on the pass, it will have a property section called **Input Elements**. It lists all of the Texture Parameters in the Material and let's you set them to reference a specific child Element.

### Referencing Other Passes in Your Material

Like Elements, Materials can reference other passes that have already run and is how you would do progressive transforms within a single Element. For example, with the Media Plate, we do a chroma keying pass and a despill pass that used the keyed result.

[![Custom Material Inputs Parameters](https://dev.epicgames.com/community/api/documentation/image/6d687669-b17c-4efa-9176-a3d5c8888aba?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6d687669-b17c-4efa-9176-a3d5c8888aba?resizing_type=fit)

If you need to reference a pass other than the one that comes right before the current pass, the other pass needs to have its **Intermediate** flad unchecked.

#### PrePass Special Parameter Name

**PrePass** is a special parameter name that can be interpreted as reference whichever pass was run right before this. Using it in your Material makes it more portable without requiring you to set the parameter mapping in the Details panel.

[![PrePass Special Parameter Name](https://dev.epicgames.com/community/api/documentation/image/dc434419-9da9-4a24-9ee9-ba25fd9bd618?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dc434419-9da9-4a24-9ee9-ba25fd9bd618?resizing_type=fit)

### Compositing Two Elements Together

By default, projects are setup to send alpha data through the post process pipeline. For CG Layers to work properly, the Project Setting **Enable alpha channel support in post processing** needs to be set to **Linear color space only**. This setting can be found under the Rendering > PostProcessing category.

To make compositing Elements together simpler in your Material, the following functions are available:

The **Over** node takes the input A and overlays its with input B using A's opacity to blend the two together. The node takes a flaot4 RGBA vector and expects the RGB channels to be pre-multiplied with their alpha value.

[![Compositing Two Materials](https://dev.epicgames.com/community/api/documentation/image/c0d815d4-4957-458e-b452-5891acb4e920?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c0d815d4-4957-458e-b452-5891acb4e920?resizing_type=fit)

Compositing Two Materials

*Click image to expand.*

In this example below, the Over material expression is blending the the `FG_Element` with the `BG_Element`. The alpha of `FG_Element` is used to blend the foreground objects with the background plate.

[![Composure Material Blend](https://dev.epicgames.com/community/api/documentation/image/810ea2a2-9be8-4271-84c0-cc4adfe7a05c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/810ea2a2-9be8-4271-84c0-cc4adfe7a05c?resizing_type=fit)

### Exposing Material Parameters

Scalar and Vector material parameters are automatically exposed to the pass Details panel under the **Material Parameters** category. It makes adjusting, tweaking, and experimenting with your composition simpler to do.

[![Material Parameter Blend](https://dev.epicgames.com/community/api/documentation/image/0eec7b46-b806-4063-baf8-c20d9b19ea16?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0eec7b46-b806-4063-baf8-c20d9b19ea16?resizing_type=fit)

Material Parameter Blend

*Click image to expand.*

In this example material, the **Blend** scalar parameter is automatically exposed to the Element's Details panel. Adjusting it's value can be used here to make quick edits or experiment with settings while working in the Editor.

![Exposed Blend Scalar Value = 0.0](https://dev.epicgames.com/community/api/documentation/image/1c4b140e-5f3a-4c58-8072-15015739901f?resizing_type=fit&width=1920&height=1080)

![Exposed Blend Scalar Value = 0.5](https://dev.epicgames.com/community/api/documentation/image/0b35c7f2-86d9-4828-b763-ff8adf3fb57c?resizing_type=fit&width=1920&height=1080)

Exposed Blend Scalar Value = 0.0

Exposed Blend Scalar Value = 0.5

## Outputting Your Composite

An **Output** pass is responsible for routing the different Elements' final result to some external consumer. Each Element has a place for you to add Output passes.

Clicking the **add** (**+**) button next to **Outputs** gives you the following selectable options:

[![Output Composite Formats](https://dev.epicgames.com/community/api/documentation/image/99f3f4df-8924-474a-937f-3c43c9ca29a0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/99f3f4df-8924-474a-937f-3c43c9ca29a0?resizing_type=fit)

* Compsiting Media Capture Output
* EXRFile Compositing Output
* Player Viewport Compositing Output
* Render Target Compositing Output

The most common (or primary) output is to a capture card using the **Media Capture** pass. To quickly, or conveniently, add a Media Capture pass to your Element, use the tree panel button:

[![Tree Panel Button](https://dev.epicgames.com/community/api/documentation/image/d415ca69-74fc-4bc2-879e-0f1463ee5a43?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d415ca69-74fc-4bc2-879e-0f1463ee5a43?resizing_type=fit)

### Exporting Composition with Sequencer

An alternative workflow is to render out composites and other layers or passes through [Sequencer](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview).

[![Sequencer Output](https://dev.epicgames.com/community/api/documentation/image/816b162e-8d76-48eb-b390-656dcff2ef64?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/816b162e-8d76-48eb-b390-656dcff2ef64?resizing_type=fit)

Sequencer Output

*Click image to expand.*

For further reading, see [Real-Time Compositing with Sequencer](https://dev.epicgames.com/documentation/en-us/unreal-engine/real-time-compositing-with-sequencer-in-unreal-engine).

* [getting started](https://dev.epicgames.com/community/search?query=getting%20started)
* [beta](https://dev.epicgames.com/community/search?query=beta)
* [ar/vr/xr](https://dev.epicgames.com/community/search?query=ar%2Fvr%2Fxr)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Enabling the Composure Plugin](/documentation/en-us/unreal-engine/realtime-compositing-tools-in-unreal-engine?application_version=5.7#enabling-the-composure-plugin)
* [Compositing Tree Panel](/documentation/en-us/unreal-engine/realtime-compositing-tools-in-unreal-engine?application_version=5.7#compositing-tree-panel)
* [Anatomy of the Composure Compositing Panel](/documentation/en-us/unreal-engine/realtime-compositing-tools-in-unreal-engine?application_version=5.7#anatomy-of-the-composure-compositing-panel)
* [Compositing Elements](/documentation/en-us/unreal-engine/realtime-compositing-tools-in-unreal-engine?application_version=5.7#compositing-elements)
* [Internal Passes](/documentation/en-us/unreal-engine/realtime-compositing-tools-in-unreal-engine?application_version=5.7#internal-passes)
* [Anatomy of an Element](/documentation/en-us/unreal-engine/realtime-compositing-tools-in-unreal-engine?application_version=5.7#anatomy-of-an-element)
* [Compositing Material](/documentation/en-us/unreal-engine/realtime-compositing-tools-in-unreal-engine?application_version=5.7#compositing-material)
* [Nesting Elements](/documentation/en-us/unreal-engine/realtime-compositing-tools-in-unreal-engine?application_version=5.7#nesting-elements)
* [Compositing Element Material Pass](/documentation/en-us/unreal-engine/realtime-compositing-tools-in-unreal-engine?application_version=5.7#compositing-element-material-pass)
* [Referencing Elements in Your Material](/documentation/en-us/unreal-engine/realtime-compositing-tools-in-unreal-engine?application_version=5.7#referencing-elements-in-your-material)
* [Making Materials Portable](/documentation/en-us/unreal-engine/realtime-compositing-tools-in-unreal-engine?application_version=5.7#making-materials-portable)
* [Referencing Other Passes in Your Material](/documentation/en-us/unreal-engine/realtime-compositing-tools-in-unreal-engine?application_version=5.7#referencing-other-passes-in-your-material)
* [PrePass Special Parameter Name](/documentation/en-us/unreal-engine/realtime-compositing-tools-in-unreal-engine?application_version=5.7#pre-pass-special-parameter-name)
* [Compositing Two Elements Together](/documentation/en-us/unreal-engine/realtime-compositing-tools-in-unreal-engine?application_version=5.7#compositing-two-elements-together)
* [Exposing Material Parameters](/documentation/en-us/unreal-engine/realtime-compositing-tools-in-unreal-engine?application_version=5.7#exposing-material-parameters)
* [Outputting Your Composite](/documentation/en-us/unreal-engine/realtime-compositing-tools-in-unreal-engine?application_version=5.7#outputting-your-composite)
* [Exporting Composition with Sequencer](/documentation/en-us/unreal-engine/realtime-compositing-tools-in-unreal-engine?application_version=5.7#exporting-composition-with-sequencer)
