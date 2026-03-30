<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-patch-system?application_version=5.7 -->

# Landscape Patch System

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
6. [Landscape Outdoor Terrain](/documentation/en-us/unreal-engine/landscape-outdoor-terrain-in-unreal-engine "Landscape Outdoor Terrain")
7. [Editing Landscapes](/documentation/en-us/unreal-engine/editing-landscapes-in-unreal-engine "Editing Landscapes")
8. Landscape Patch System

# Landscape Patch System

Use the Landscape Patch plugin to procedurally change landscape heightmaps and weightmaps.

On this page

Landscape Patch is an editor plugin you can use to procedurally change landscape heightmaps and weightmaps using texture patch components called landscape patches. These patches can be attached to any actor and automatically apply a texture-based modification to a patch edit layer of a given landscape. Patches can read from a texture or render target and apply the results to the landscape in the editor. The results are baked into the final landscape. Any data they require is editor-only, so there is no impact on memory or performance.

## Landscape Patch Edit Layer

Landscape patches apply to a landscape using one or more dedicated **patch edit layers**. This edit layer type is entirely procedural, so you cannot sculpt or paint on a layer using conventional landscape tools. The only way to manipulate patches is through the standard viewport and the scene outliner.

[![Patch edit layers cannot be edited using landscape tools](https://dev.epicgames.com/community/api/documentation/image/021d2986-198f-480c-9591-3db5fdb83525?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/021d2986-198f-480c-9591-3db5fdb83525?resizing_type=fit)

To create a patch edit layer, follow these steps:

1. In the main toolbar, select **Landscape** from the **Selection Mode** dropdown.

   [![The Selection Mode dropdown](https://dev.epicgames.com/community/api/documentation/image/fa063de9-bd8a-481e-9b79-5f80415adb2b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fa063de9-bd8a-481e-9b79-5f80415adb2b?resizing_type=fit)
2. In the **Edit Layers** section, Click the **add (+)** button.
3. Select the landscape patch edit layer type and click **Select**.

   [![The Pick Landscape Edit Layer Class dropdown](https://dev.epicgames.com/community/api/documentation/image/9e5a221f-51fc-468c-8627-88bdae5064e8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9e5a221f-51fc-468c-8627-88bdae5064e8?resizing_type=fit)

Optionally, you can create a patch edit layer by adding a patch component to an existing actor in the world or dropping a blueprint actor with a patch component in the world. After either action, a dialog box appears and you can choose where to add a new patch edit layer in the edit layer stack.

You can use several patch edit layers in the same landscape. The patch edit layers are applied in order from top to bottom. After creating a patch edit layer, the layer can be dragged in the edit layer stack to change when the layer is applied.

## Landscape Texture Patch

The texture patch component is the main component to interact with a patch edit layer. To create one, add a **Landscape Texture Patch** component to an actor, either in the **Actor Details** view or in the **Blueprint Editor**.

[![Landscape Texture Patch](https://dev.epicgames.com/community/api/documentation/image/a1c1ab01-aec3-4107-82f4-ac60e2489050?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a1c1ab01-aec3-4107-82f4-ac60e2489050?resizing_type=fit)

When first dropped into a world, patches attach themselves to the first patch edit layer on the first landscape they find. If the patch doesn't find a patch edit layer, it creates one and prompts you to insert it in the edit layer stack.

When a patch is selected, you can see the landscape and edit layer that it is attached to in the **Details** panel.

[![The Landscape and Edit Layer settings](https://dev.epicgames.com/community/api/documentation/image/25774edf-86f4-4f7a-b363-776c9d2bd07e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/25774edf-86f4-4f7a-b363-776c9d2bd07e?resizing_type=fit)

When you change either of these settings, the other one automatically change to match. If you change the landscape actor, the patch will attach itself to the first patch edit layer it finds in the new landscape.

The following video shows a typical patch setup process.

## Patch Details

### Height Patch

The **Height Patch** section defines whether the patch affects heightmaps. You can set the patch to only affect heightmaps, only affect visibility, only affect a given target layer, or affect any combination of these.

[![The Height Patch section](https://dev.epicgames.com/community/api/documentation/image/11999564-71c7-4d88-8f64-5e2156da4739?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/11999564-71c7-4d88-8f64-5e2156da4739?resizing_type=fit)

This section includes the following properties:

* **Source mode**: Sets where the source texture data should be taken from, based on the following options:

  + **None**: The patch doesn’t affect heightmaps.
  + **Internal Texture**: The patch data is read from an internally-stored texture. In this mode, the patch can't be written to using Blueprints, but it avoids storing the extra render target needed for **Texture Backed Render Target**. This is generally only used with the Reinitialize commands.
  + **Texture Backed Render Target**: The patch data is read from an internally-stored render target, which can be written to using Blueprints and which gets serialized to an internally-stored texture when needed. Uses double the memory of **Internal Texture**. Allows Blueprints to render the texture.
  + **Texture Asset**: The patch data is read from a UTexture asset, which can be a render target. Allows multiple patches to share the same texture.
* **Height Encoding**: Defines how the values stored in the patch represent the height. Not customizable for Internal Texture source mode, which always uses native packed height. Has the following options:

  + **ZeroToOne**: Values in the texture should be interpreted as being floats in the range [0,1]. The Zero In Encoding parameter sets what value corresponds to zero height (when the landscape is cleared). The World Space Encoding parameter sets the size of the range in world units.
  + **World Units**: Values in the texture are direct world-space heights.
  + **Native Packed Height**: Values in the texture are stored as as 16 bit integers packed into two bytes, mapping to [-256, 256 - 1/128] before applying landscape scale.
* **Zero In Encoding**: The value in the patch data that corresponds to zero height, relative to the starting point specified by Zero Height Meaning.
* **World Space Encoding Scale**: The scale in world coordinates to apply to the data stored in the patch, relative to the zero in the encoding. For example, if the encoding is [0,1], 0.5 corresponds to 0, and the World Space Encoding Scale is 100, then the resulting values will lie in the range [-50, 50] in world space. Those coordinates would be [-0.5, 0.5] in the landscape local heights if the Z scale is 100.
* **Zero Height Meaning**: Defines how zero height is interpreted, based on the following options:

  + **Patch Z**: Zero height corresponds to the patch vertical position relative to the landscape. This moves the results up and down as the patch moves up and down.
  + **Landscape Z**: Zero height corresponds to the Z coordinate of 0 in the local space of the landscape, regardless of the patch vertical position. For instance, if the landscape transform has a Z coordinate of -100 in world coordinates, then writing height 0 will correspond to a Z coordinate or -100 in world coordinates, regardless of Patch Z.
  + **World Zero**: Zero height corresponds to the height of the world origin relative to landscape. In other words, writing height 0 will correspond to Z=0 in world coordinates, regardless of Patch Z or landscape transform (as long as the landscape transform still has Z up in world coordinates).

### Weight Patches

Weight patches need to be added one by one (one per target layer) by adding a **Landscape Weight Patch Texture Info** element to the **Weight Patches** property.

[![The Weight Patches section](https://dev.epicgames.com/community/api/documentation/image/ed1e6397-8832-4fb6-ad74-d52972c77b81?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ed1e6397-8832-4fb6-ad74-d52972c77b81?resizing_type=fit)

This section includes the following properties:

* **Weightmap Layer Name**: The name of the weightmap layer (target layer) declared in the landscape that this weight patch should apply to. The name is not case-sensitive but otherwise has to match exactly with the target layer name declared in the targeted landscape for the patch to work.

* **Edit Visibility Layer**: Whether to apply this weight patch to the Visibility layer. When enabled, **Weightmap Layer Name** is ignored. The landscape material has to support visibility for this option to affect visibility.

* **Source Mode**: Sets where the source texture data should be taken from, based on the following options:

  + **None**: The patch doesn’t affect weightmaps.
  + **Internal Texture**: The patch data is read from an internally-stored texture. In this mode, the patch can't be written to using Blueprints, but it avoids storing the extra render target needed for **Texture Backed Render Target**. This is generally only used with the Reinitialize commands.
  + **Texture Backed Render Target**: The patch data is read from an internally-stored render target, which can be written to using Blueprints and which gets serialized to an internally-stored texture when needed. Uses double the memory of **Internal Texture**. Allows Blueprints to render the texture.
  + **Texture Asset**: The patch data is read from a UTexture asset, which can be a render target. Allows multiple patches to share the same texture.

### Reinitialize Height and Weight

The **Reinitialize Heights** and **Reinitialize Weights** buttons capture the current landscape heights and weights at the patch’s current location and bake them into the patch’s textures, so that they can be moved somewhere else. Sculpt and paint the landscape, position a patch above it, and press those buttons to transfer that data over to an internal texture inside the patch, so that those edits can be moved with the patch.

The following video shows an example of how to use these buttons.

### Debug Data

Use the **Debug Data** section for debugging when your source mode is **Internal Texture** or **Texture Backed Render Target**. You can open the debug data in the texture viewer, and see if something is visible.

[![The Debug Data section](https://dev.epicgames.com/community/api/documentation/image/3e91897a-0168-4119-8b0e-6806b3a1e86c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3e91897a-0168-4119-8b0e-6806b3a1e86c?resizing_type=fit)

### Settings

The **Settings** section contains properties that control how the patch applies to the landscape.

[![The Settings section](https://dev.epicgames.com/community/api/documentation/image/ded94202-3205-499e-8a9d-5443f4f90977?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ded94202-3205-499e-8a9d-5443f4f90977?resizing_type=fit)

This section includes the following properties:

* **Unscaled Patch Coverage**: The size of the patch. At scale 1.0, the X and Y of the region are affected by the height patch. This corresponds to the distance from the center of the first pixel to the center of the last pixel in the patch texture in the X and Y directions.
* **Blend Mode**: How this patch should apply to the landscape with respect to the layers underneath, based on the following options:

  + **Alpha Blend**: The patch specifies the actual target height and weight, and then blends that with the existing height and weight using falloff and alpha. For example: with no falloff and alpha set to 1, the landscape will be set directly to the height and weight sampled from the patch. With alpha set to 0.5, the landscape height and weight will be averaged evenly with patch height and weight.
  + **Additive**: Interprets the landscape mid value as 0, and uses the texture patch as an offset to apply to the landscape in the height case. For weight, this is just a standard additive behavior. Falloff and alpha just affect the degree to which the offset is applied (for example,  an alpha of 0.5 will apply just half the offset).
  + **Min**: Like **Alpha Blend** mode, but limited to only lowering the existing landscape values.
  + **Max**: Like **Alpha Blend** mode, but limited to only raising the existing landscape values.
* **Falloff Mode**: How the patch behavior gets attenuated on the sides of the patch, based on the following options:

  + **Circle**: Affects the landscape in a circle defined by the patch, and falls off starting at the edge of the circle and moving inward.
  + **Rounded Rectangle**: Affects the entire rectangle of the patch (except for circular corners), and falls off starting from the edge of the rectangle and moving inward.

## Patch Ordering

In the **Alpha Blend**, **Min**, and **Max** blend modes, each patch gets applied in a certain order controlled by the Priority property. In the Additive blend mode case, the ordering is irrelevant.

The **Priority** property, which determines the patch ordering relative to other patches. The lower the priority value, the earlier the patch is applied. For example, a patch with a Priority of 1000 will apply before a patch with a Priority of 1001.

The Priority value gets automatically assigned to patches when they get added to an actor. This can be controlled using the **Priority Initialization** property in the **Advanced** panel. This property has the following options:

* **Acquire Highest**: Assigns a priority 1 higher than the highest existing priority patch, so that the new patch is on top of any existing patches. Note that the current highest priority could be out of date in between landscape updates.
* **Keep Original**: Assigns the default priority value. This is useful when using custom priority values as categories.
* **Small Increment**: Assigns a priority 0.01 higher than the highest existing priority patch. This can be useful when copying a patch around multiple times, as it allows the new patches to be roughly in the same place in the priority hierarchy while still being higher priority than the copied patch.

## Using Patches in Blueprints

If you want your patches to use the same texture or render target, use a texture asset for the source mode. If you want each patch to have its own render target, you can set the source mode to **Texture Backed Render Target**. Texture backed means that these internal render targets get copied to an internal texture as well for serialization, so they take extra memory when you are in the editor, but don’t get cleared the next time you reload the map. Then, you can write to the render target using **GetHeightRenderTarget** or **GetWeightPatchRenderTarget**.

[![GetHeightRenderTarget and GetWeightPatchRenderTarget](https://dev.epicgames.com/community/api/documentation/image/f1a4e571-23a3-4292-9f91-d967eed7cae5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f1a4e571-23a3-4292-9f91-d967eed7cae5?resizing_type=fit)

An example of a blueprint setting up a bunch of weight patches on the actor’s landscape texture patch component (using the Texture Backed Render Target mode) in the construction script.

[![](https://dev.epicgames.com/community/api/documentation/image/4966b829-ebd5-49db-b3aa-4bc60f6b3f66?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4966b829-ebd5-49db-b3aa-4bc60f6b3f66?resizing_type=fit)

The Render Patch node in the construction script.

Writing to the render target should be done at explicit points using a call-in-editor method, rather than rewriting constantly when not necessary. After writing or making changes, you might want to call **RequestLandscapeUpdate** on the patch to make sure that it is applied, though many function calls will trigger the update anyway. This request is safe to do multiple times in one tick, as the actual update will only happen once in a later tick after it has been requested. Moving the patch will automatically trigger the update as long as the patch is enabled and its source mode is not set to **None**.

Trying to read from the landscape while modifying a patch can result in lag when the landscape is being updated. For example, if you try to disable the patch and then immediately read from the landscape (using a landscape **RenderHeightmap** call, or a scene capture, or some other way), the removal of the patch might not yet be applied. If you are trying to read from landscape in order to write to the patch, you should use one action to disable the patch, and then a separate action to read or write.

### Determinism

When generating landscape data, all expressions must be deterministic, meaning that they always return the same result using the same input data. Two subsequent updates of the same landscape area must have the exact same output, where every computed pixel has the same final height and weight value. For example, do not use time-based material expressions in a material graph that affects a landscape patch texture.

## Troubleshooting

If your patches do nothing, check the following:

* Is the patch enabled? Check the **Is Enabled** flag.
* Is the source mode set to something other than **None**?
* Is there an associated landscape and patch edit layer?
* Are there complaints in the console log?
* Look at the texture that your patch is using. If your patch is set to use the texture alpha, open the texture in the viewer and select the alpha channel to see whether it has some data set.
* Does the patch work if you reinitialize it from landscape and move it around? If not, there is something wrong with the attachment. It might be attached to the wrong landscape, or to a landscape that does not have edit layers enabled.

If the patch affects the landscape, but the landscape is always flat in the patch region, then most likely something is wrong with the data given to the patch. Try to examine the values somehow, and make sure that the height encoding settings match your data. For example, you might be writing 0-1 units, but interpreting them as world units. You can increase the scale of the units to see if the effect is more visible.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Landscape Patch Edit Layer](/documentation/en-us/unreal-engine/landscape-patch-system?application_version=5.7#landscapepatcheditlayer)
* [Landscape Texture Patch](/documentation/en-us/unreal-engine/landscape-patch-system?application_version=5.7#landscapetexturepatch)
* [Patch Details](/documentation/en-us/unreal-engine/landscape-patch-system?application_version=5.7#patchdetails)
* [Height Patch](/documentation/en-us/unreal-engine/landscape-patch-system?application_version=5.7#heightpatch)
* [Weight Patches](/documentation/en-us/unreal-engine/landscape-patch-system?application_version=5.7#weightpatches)
* [Reinitialize Height and Weight](/documentation/en-us/unreal-engine/landscape-patch-system?application_version=5.7#reinitializeheightandweight)
* [Debug Data](/documentation/en-us/unreal-engine/landscape-patch-system?application_version=5.7#debugdata)
* [Settings](/documentation/en-us/unreal-engine/landscape-patch-system?application_version=5.7#settings)
* [Patch Ordering](/documentation/en-us/unreal-engine/landscape-patch-system?application_version=5.7#patchordering)
* [Using Patches in Blueprints](/documentation/en-us/unreal-engine/landscape-patch-system?application_version=5.7#usingpatchesinblueprints)
* [Determinism](/documentation/en-us/unreal-engine/landscape-patch-system?application_version=5.7#determinism)
* [Troubleshooting](/documentation/en-us/unreal-engine/landscape-patch-system?application_version=5.7#troubleshooting)
