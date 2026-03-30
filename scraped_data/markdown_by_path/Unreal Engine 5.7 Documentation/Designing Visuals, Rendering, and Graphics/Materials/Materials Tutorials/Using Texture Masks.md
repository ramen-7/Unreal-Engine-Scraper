<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-texture-masks-in-unreal-engine?application_version=5.7 -->

# Using Texture Masks

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
5. [Designing Visuals, Rendering, and Graphics](/documentation/en-us/unreal-engine/designing-visuals-rendering-and-graphics-with-unreal-engine "Designing Visuals, Rendering, and Graphics")
6. [Materials](/documentation/en-us/unreal-engine/unreal-engine-materials "Materials")
7. [Materials Tutorials](/documentation/en-us/unreal-engine/unreal-engine-materials-tutorials "Materials Tutorials")
8. Using Texture Masks

# Using Texture Masks

This page describes how to use Texture Masking in your Materials.

![Using Texture Masks](https://dev.epicgames.com/community/api/documentation/image/4b9a0b54-2fe5-4311-9084-5bb953312b3c?resizing_type=fill&width=1920&height=335)

 On this page

When creating 3D assets, you might find that you need the ability to define different surface types within the same Material.
A simple and cheap way to achieve this is to use a **Texture Mask** that defines which parts of a surface should be affected by which section of the Material.

This tutorial covers how you can use texture masking inside your Unreal Engine Materials.

## Texture Masks

A **Texture Mask** is a grayscale texture, or a single channel (R, G, B, or A) of a texture, used to limit the area of an effect inside a **Material**.

Masks are frequently contained within a single channel of another texture, such as the **Alpha Channel** of the Diffuse or Normal map. In other cases, a single image file often contains the Roughness, Metallic, and Ambient Occlusion masks, each one occupying a single channel.

This is called channel packing, and is a good way to improve Material performance by reducing the number of texture samples required by the Material.
Technically, any channel of any texture can be thought of and used as a texture mask.

Here is an example of what the Texture Mask for the **SM\_Chair** Static Mesh from the Starter Content looks like.

[![RGB chair masks](https://dev.epicgames.com/community/api/documentation/image/910dbecf-ac11-49e8-84dc-7d705cef13df?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/910dbecf-ac11-49e8-84dc-7d705cef13df?resizing_type=fit)

In fact, this image file contains a different black and white mask in each of the four color channels (RGBA).

[![RGBA Masks separated](https://dev.epicgames.com/community/api/documentation/image/fb0398c9-20c9-483c-b094-682140e82f17?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fb0398c9-20c9-483c-b094-682140e82f17?resizing_type=fit)

## Creating a Texture Mask

You can create a texture mask in any 2D image manipulation program. You can also bake masks directly from geometry in your primary content creation program, or with a dedicated texturing tool like Marmoset Toolbag, Xnormal, or Substance Painter/Designer.

When creating masks by hand, you will generally start with an image that shows the UV layout of your mesh. In this example, the intent is to mask the seat cushions. The corresponding UVs are highlighted in the image below. To mask a specific part of the model, you need to paint that region of the image pure white, while leaving all the other areas black.

[![Starter chair UVs](https://dev.epicgames.com/community/api/documentation/image/f514e1d0-b85b-485f-88db-54dad746f8be?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f514e1d0-b85b-485f-88db-54dad746f8be?resizing_type=fit)

As shown above, this allows you to apply specific surface properties to the masked region. In this case, the mask is used to give the cushions an orange color.

[![Cushions mask breakdown](https://dev.epicgames.com/community/api/documentation/image/9f67bac2-592e-4853-9356-f5dcbd1c5af1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9f67bac2-592e-4853-9356-f5dcbd1c5af1?resizing_type=fit)

When creating a Texture Mask you should always use either pure black or white and never color information. Using any other type of color could result in strange artifacts when using the mask inside Unreal.

## Exporting a Texture Mask

When you are done painting your mask texture, you can either export it as a single image or you can pack multiple masks together into the R, G, B, and A channels of a single image and export that.
This is commonly referred to as RGB channel packing and is the preferred method when creating masks, as it offers considerable performance and memory savings with very little extra work.

If do you pack something into the alpha channel of a texture, make sure that you remember to enable alpha exporting in whatever 2D image manipulation software you use.
If not, you run the risk of the alpha channel not being exported with the texture.

## Using Texture Masks

You can use mask textures a number of different ways inside the Unreal Material Editor. Common uses include defining an emissive light source, defining which parts of a mesh are metal and non-metal, or mapping different colors to different portions of a model as shown in the chair example.

The following section demonstrates some of the most common ways to use texture masking in Unreal Engine.

### Emissive Mask

One of the most common uses for a mask texture, is to control the emissive sections of a Material. This is usually done by first creating an emissive mask texture, which uses pure white to define the sections of the Material that should emit light. Two parameters usually accompany an emissive mask:

* To change the color of the light emission, you can multiply the emissive mask by a color defined by a **Vector Parameter**.
* To change the intensity of the emissive light, you can multiply it by a **Scalar Parameter**. Increase the value in the Scalar parameter to increase the brightness of the emission.

The four nodes highlighted in the graph below show an emissive mask multiplied by parameters that control the color and brightness of the light. The sphere only emits light in regions that correspond to the white parts of the emissive mask. The rest of the sphere displays the base color texture.

[![Emissive node graph](https://dev.epicgames.com/community/api/documentation/image/801c578d-47f8-413a-aa46-e8159a20fd21?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/801c578d-47f8-413a-aa46-e8159a20fd21?resizing_type=fit)

### Material Masking

A second common use for texture masks is to store different kinds of texture information within the individual R, G, B, and Alpha channels of the. The Material on the SM\_Chair Static Mesh that comes with the Starter Content is a perfect example of this technique.

You can find SM\_Chair and all the content that goes with it by first selecting the **Starter Content** folder in the **Content Browser** and then entering "chair" into the search box.
This will display all the content that is related to the chair. If you do not see the chair, it probably means that you did not include the Starter Content with your project.
To fix this, you will need to either create a new project or try the [Migrating Assets Tool](https://dev.epicgames.com/documentation/en-us/unreal-engine/migrating-assets-in-unreal-engine) to move the chair content from another project
into this one.

Opening up the chair Material, M\_Chair, we can see a perfect example of Texture Mapping in action.

[![Starter content chair Material](https://dev.epicgames.com/community/api/documentation/image/8de23a96-7846-4c10-81b8-d53c2405be64?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8de23a96-7846-4c10-81b8-d53c2405be64?resizing_type=fit)

In this Material, the mask texture, **T\_Chair\_M** is used to map specific surface properties to different regions on the mesh. The texture mask helps define which sections are metal or non-metal, and is also used to assign different roughness and color values to different parts of the chair.

In the following image, you can see a breakdown of how each channel in the mask texture is used. On the left side is the composite RGB image, or what the image looks like if you view it as a texture. The middle column shows the black and white masks contained in each color channel (R, G, B, A from top to bottom.) The images on the far right show which part of the chair the mask targets; the white parts of the chair correspond to the white section in the mask.

[![Chair regions masked](https://dev.epicgames.com/community/api/documentation/image/b84c2b09-007e-43ce-8d54-2f23abb9d368?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b84c2b09-007e-43ce-8d54-2f23abb9d368?resizing_type=fit)

Here is a breakdown of what type of information is stored inside each channel of the chair mask texture.

* **Red Channel**: Ambient Occlusion information. In the Material, this is used to help add subtle contact shadows where two surfaces are close together.

  [![Red channel - Ambient occlusion](https://dev.epicgames.com/community/api/documentation/image/b577618b-aba2-4e65-aade-c1d3623c4a6d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b577618b-aba2-4e65-aade-c1d3623c4a6d?resizing_type=fit)
* **Green Channel**: Metallic Mask. In the Material, this is used to define which parts are supposed to be metal. This is also used to help define what color the metal should be.

  [![Green channel - metalness mask](https://dev.epicgames.com/community/api/documentation/image/fb0eb670-c251-437f-944b-45439da7d925?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fb0eb670-c251-437f-944b-45439da7d925?resizing_type=fit)
* **Blue Channel**: Non-Metallic Mask. In the Material, this is used to define which parts are non-metal. This mask also helps to define the color of the non-metal parts.

  [![Blue Channel - Nonmetal Mask](https://dev.epicgames.com/community/api/documentation/image/d188c91c-ae2a-460d-9af3-7727d77fbf31?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d188c91c-ae2a-460d-9af3-7727d77fbf31?resizing_type=fit)
* **Alpha Channel**: Whole object Mask. This is not currently used by the Material.

All put together, the chair looks like this in an Unreal level:

[![Chair in level](https://dev.epicgames.com/community/api/documentation/image/edadf865-0358-43e6-aa89-67b4b9f83bd2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/edadf865-0358-43e6-aa89-67b4b9f83bd2?resizing_type=fit)

## Masking Tips & Tricks

Texture masking is a very powerful tool, especially when combined with other tools in Unreal Engine. The following section presents some tips and tricks for making the most of texture masking in your work.

### Texture Masking and Material separate

Using texture masking and Material Instances together is a great way to add an almost endless amount of variety to any assets.
For example, you can use a texture mask to define which areas should have certain properties, like color, and then use different Material Instances to customize these properties in the Instance Editor. Read more about [Material Instancing here](https://dev.epicgames.com/documentation/en-us/unreal-engine/instanced-materials-in-unreal-engine).

[![Multiple color instances of the Starter Content chair.](https://dev.epicgames.com/community/api/documentation/image/5e822393-b144-45e6-84f2-deb3bff4baf3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5e822393-b144-45e6-84f2-deb3bff4baf3?resizing_type=fit)

When Material masks are used along with Material Instancing, you can allow artists to quickly and easily change color and other values within the Material. This approach produces highly customizable assets, as seen with the SM\_Chair in the image above.

### Masking and Channel Artifacts

Because of a quirk with DirectX, the **green channel** of a texture will often offer the best compression. If any of your masks suffer greatly from compression artifacts, first try placing the information into the green channel of the image to see if that helps. If that does not fix the issue, then try using the Alpha channel to store the mask.

Be careful when trying to use the Alpha channel of a texture to store Mask information. Adding an Alpha channel to a texture will greatly increase the memory footprint of that texture and if
you do this enough, you could lose all the saving you gained by packing different masks in to the RGB channels of the texture.

### sRGB and Mask Textures

When packing multiple Mask Textures into a single texture, you should uncheck sRGB in the Texture Editor, as masks should not be gamma corrected.

[![Disable SRGB](https://dev.epicgames.com/community/api/documentation/image/16863b6f-7c37-4b39-a71d-f3aa066bf506?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/16863b6f-7c37-4b39-a71d-f3aa066bf506?resizing_type=fit)

If you disable sRGB for a texture that was previously sampled in a Material, the sample type is not automatically updated in existing 2D Texture Sampler nodes. You need to make sure that you adjust the node type in any existing 2D Texture Sampler Nodes. If you do not change the **Sampler Type**, your Material will fail to compile and the following message is displayed in the Stats log.

[![Incorrect sampler type](https://dev.epicgames.com/community/api/documentation/image/05ffd544-3a1a-4da5-948d-83e381458f5e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/05ffd544-3a1a-4da5-948d-83e381458f5e?resizing_type=fit)

To fix this error, all you need to do is to change the Sampler Type from the default of Color to Linear Color and the warning will go away.
For good measure, you should re-compile the Material to make sure that the changes were successful. Once completed, the warning will go away.

## Conclusion

Texture Masking is a very powerful concept that once mastered allows you to create an almost endless amount of variation with very little source content.
Remember that you only have four available channels in any image file to use for texture masks, so use each channel wisely.
Do not forget to disable sRGB on your mask textures, as it can greatly help to increase the mask's sharpness.

* [materials](https://dev.epicgames.com/community/search?query=materials)
* [uv mapping](https://dev.epicgames.com/community/search?query=uv%20mapping)
* [texturing](https://dev.epicgames.com/community/search?query=texturing)
* [shaders](https://dev.epicgames.com/community/search?query=shaders)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Texture Masks](/documentation/en-us/unreal-engine/using-texture-masks-in-unreal-engine?application_version=5.7#texture-masks)
* [Creating a Texture Mask](/documentation/en-us/unreal-engine/using-texture-masks-in-unreal-engine?application_version=5.7#creating-a-texture-mask)
* [Exporting a Texture Mask](/documentation/en-us/unreal-engine/using-texture-masks-in-unreal-engine?application_version=5.7#exporting-a-texture-mask)
* [Using Texture Masks](/documentation/en-us/unreal-engine/using-texture-masks-in-unreal-engine?application_version=5.7#using-texture-masks)
* [Emissive Mask](/documentation/en-us/unreal-engine/using-texture-masks-in-unreal-engine?application_version=5.7#emissive-mask)
* [Material Masking](/documentation/en-us/unreal-engine/using-texture-masks-in-unreal-engine?application_version=5.7#material-masking)
* [Masking Tips & Tricks](/documentation/en-us/unreal-engine/using-texture-masks-in-unreal-engine?application_version=5.7#masking-tips-tricks)
* [Texture Masking and Material separate](/documentation/en-us/unreal-engine/using-texture-masks-in-unreal-engine?application_version=5.7#texture-masking-and-material-separate)
* [Masking and Channel Artifacts](/documentation/en-us/unreal-engine/using-texture-masks-in-unreal-engine?application_version=5.7#masking-and-channel-artifacts)
* [sRGB and Mask Textures](/documentation/en-us/unreal-engine/using-texture-masks-in-unreal-engine?application_version=5.7#s-rgb-and-mask-textures)
* [Conclusion](/documentation/en-us/unreal-engine/using-texture-masks-in-unreal-engine?application_version=5.7#conclusion)

Related documents

[Textures

![Textures](https://dev.epicgames.com/community/api/documentation/image/1a688349-5489-4742-baae-fa7f6e769910?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/textures-in-unreal-engine)

[Texture Format Support and Settings

![Texture Format Support and Settings](https://dev.epicgames.com/community/api/documentation/image/95a3f52e-cd90-49de-9b00-6a49d15c2f43?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/texture-format-support-and-settings-in-unreal-engine)

[Texture Asset Editor

![Texture Asset Editor](https://dev.epicgames.com/community/api/documentation/image/7db6e329-3178-4c4c-aedb-b929e7a4da85?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/texture-asset-editor-in-unreal-engine)

[Texture Material Expressions

![Texture Material Expressions](https://dev.epicgames.com/community/api/documentation/image/b6723d4d-747b-4209-a447-c4f6e6dd1135?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/texture-material-expressions-in-unreal-engine)

[Using the Emissive Material Input

![Using the Emissive Material Input](https://dev.epicgames.com/community/api/documentation/image/4ddd2c56-6a57-4996-a657-e08a26f2c1f5?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/using-the-emissive-material-input-in-unreal-engine)

[Material Instances

![Material Instances](https://dev.epicgames.com/community/api/documentation/image/8500d1c4-e247-465e-befe-bd71fa4b563d?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/instanced-materials-in-unreal-engine)
