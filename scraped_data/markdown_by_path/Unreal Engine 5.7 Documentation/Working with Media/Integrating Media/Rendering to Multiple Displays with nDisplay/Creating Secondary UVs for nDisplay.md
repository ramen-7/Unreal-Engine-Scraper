<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-secondary-uvs-for-ndisplay-for-unreal-engine?application_version=5.7 -->

# Creating Secondary UVs for nDisplay

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
8. Creating Secondary UVs for nDisplay

# Creating Secondary UVs for nDisplay

Guide for creating a second UV channel for the nDisplay projection meshes so that the In-Camera VFX editor can take full advantage of all of its features.

![Creating Secondary UVs for nDisplay](https://dev.epicgames.com/community/api/documentation/image/c2e06a5a-a3ea-43a0-8d42-c346f8aba543?resizing_type=fill&width=1920&height=335)

This guide is meant for UV1 of the projection meshes. [The UV channel 0 is used for warp mapping with a mesh projection policy in nDisplay.](/documentation/en-us/unreal-engine/projection-policies-in-ndisplay-in-unreal-engine)

Because of how **nDisplay** applies ‘2D style’ effects to the projection meshes, we utilize the second UV channel and expect all UV shells across meshes to have been given the same texel density, and for each UV shell to have no overlap.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f27d60bb-e1d4-4c2e-97db-8d8a08e15c3a/seconduvs-1.png)

Consideration also needs to be given to the shape of the stage. For example, a very wide continuous LED wall, though likely made of separate meshes, should always be one continuous set of UVs as the wall would stand in reality. We will use the stage mesh from the **ICVFXExample Project**. If you wish to follow along, go to `/Content/nDisplayConfigs/Meshes` to export the relevant static mesh actors to **FBX** and follow along in your DCC of choice.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/41e6e904-20ab-4d42-8e1e-957a8b070233/seconduvs-2.png)

Though this may seem like a poor use of UV space, it is more important for the shells in this second UV set to be representative of their real-life counterpart’s construction. In this example, the seam of these two meshes is in the center of the curved wall. In this configuration, the checkerboard texture flows correctly. This is important for the **Chroma Key mode** of **nDisplay**, as incorrect layout and uneven texel density can cause markers to be cut off and have different sizes across the Volume.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f7ab81d5-5cc8-4229-8835-70276f69ac65/seconduvs-3.png)

The example above makes better use of UV space but is unsuitable for the needs of the In-Camera VFX Editor. You can see the checkerboard no longer flows correctly. **UV Light Cards** passing through the middle seam will look incorrect.

For **common-plane sets of panels**, such as the ceiling, it’s a good idea to do a **plane projection** if they have any standout characteristics, such as the gap. The gap must be proportional to how it is in reality, otherwise, **UV space effects** won’t translate across correctly. In the example below you can see how the **UV Light Card** is able to maintain its correct proportions in the Editor viewport nDisplay preview.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c1e6ed88-3042-4f91-bcae-6b567ee5bbe7/seconduvs-4.gif)

Before: The UV Light Card does not maintain correct proportions when moved in the viewport nDisplay preview.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/41baf749-039d-4e7c-a181-292b1d0ecef9/seconduvs-5.gif)

After: The UV Light Card maintains the correct proportions when moved in the viewport nDisplay preview.

It’s also important to consider how the layout and orientation of the UV shells will be. Having shells flipped in UV can cause unintuitive feedback, such as the controls feeling “backward”.

See above how where the light card “comes out” of the top of the curved wall, it shows up partially on the ceiling. It would be better to move the UV1 shell of the ceiling further away from the walls in UV1 so there is space for the UV Light Card to become ‘hidden’ when it’s hanging off the edges of the wall UV shell.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/1be30032-2086-48db-9cca-a139ef9deee0/seconduvs-6.png)

These meshes should remain separate, so do not combine them when exporting. You can work on them simultaneously by selecting each mesh when opening your DCC’s UV layout editor.

* [getting started](https://dev.epicgames.com/community/search?query=getting%20started)
* [virtual production](https://dev.epicgames.com/community/search?query=virtual%20production)
* [ndisplay](https://dev.epicgames.com/community/search?query=ndisplay)
* [icvfx](https://dev.epicgames.com/community/search?query=icvfx)
* [virtual sets](https://dev.epicgames.com/community/search?query=virtual%20sets)
* [bronze](https://dev.epicgames.com/community/search?query=bronze)
* [uvs](https://dev.epicgames.com/community/search?query=uvs)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)
