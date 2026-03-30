<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/open-world-tools-tips-in-unreal-engine?application_version=5.7 -->

# Open World Tools Tips

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
6. [Open World Tools](/documentation/en-us/unreal-engine/open-world-tools-in-unreal-engine "Open World Tools")
7. Open World Tools Tips

# Open World Tools Tips

A collection of tips and tricks about how to get the most out of the Open World Tools.

![Open World Tools Tips](https://dev.epicgames.com/community/api/documentation/image/815f71aa-34f5-4aea-85c9-7e787e4fbc69?resizing_type=fill&width=1920&height=335)

 On this page

![Tip-Trick Header](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/be31e97f-7337-4c39-ba4d-db4df808c110/01-t-tip-trick-header.png "Tip-Trick Header")

In the following section we will be taking a look at some tips and tricks that you can use to push the Open World tools to their limits.
The following tips and tricks come right from the Epic developers that used the Open World Tools to create the Kite Demo that was debuted at the 2015 Game Developers conference.
Please keep in mind that the following is not meant to be a step by step tutorial but more of a high level look at what was done and how you could apply these techniques to your projects.

If you are looking for more basic information on how to use the Open World Tools check out the [Procedural Foliage Quick Start](/documentation/en-us/unreal-engine/procedural-foliage-tool-in-unreal-engine) or the [Grass Tools Quick Start](/documentation/en-us/unreal-engine/grass-quick-start-in-unreal-engine) for more basic information on how to use these tools.

## Grass Tool Foliage Mesh Culling

While you can adjust the culling of the Grass Tool to render Static Meshes extremely far in the distance be careful setting the options too high as you could run the risk of crashing your video card and/or UE5 editor session.

When using the Grass Tools in your projects you might notice that past a certain distance the Static Meshes that are used stop being displayed.
This is called culling and it is an optimization method that can be used to help lessen the rendering demand for your project by stopping objects from being rendered past a certain distance from the camera.
Inside of UE5 you can adjust the distance at which the Grass Tool stops rendering Static Meshes a number of different ways.
The first way you can effect the distance at which the Grass Tool culls Static Meshes is to set the **Start** and **End** Cull Distance setting that can be found in the **Landscape Grass Type** Actor under the **Grass Varieties** section.

[![Grass Tool Cull Distance](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0e26348f-3ab0-42e6-b1f7-fe0078998277/02-grass-tool-cull-distanc.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/0e26348f-3ab0-42e6-b1f7-fe0078998277/02-grass-tool-cull-distanc.png)

Click image for full size.

The image above shows the Culling settings used for the Field Grass Static Mesh that was used for some of the grass in the Kite demo.
In the image below we compare the original settings of 6,500 with the new setting of 30,000 making the Static Mesh used for the Grass being rendered further out in the distance.

![Default of 6,500](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/885da94c-aed7-4660-94e9-b29521fc4180/03-original-settings-of-6-500.png "Default of 6,500")

![Set to 30,000](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/60129c01-60b7-4ea8-a382-5c9d607b9cc8/04-new-setting-of-30-000.png "Set to 30,000")

Default of 6,500

Set to 30,000

If you look closely at the comparison screen shots above you will notice that no matter how big you set the End Cull Distance number the Static Mesh that is used will still stop being rendered past a certain point.
To make the Static Meshes render even further out you will need to input the following command into the UE5 Console followed by a decimal number.

```
	Foliage.MinimumScreenSize 0.0001

Copy full snippet
```

The **Foliage.MinimumScreenSize** command will increase or decrease the size, in screen space, at which the Static Meshes will be culled.
The reason size in screen space is used in conjunction with distance from the camera is to ensure that you do not accidentally render objects that are very small and very far away from the camera.
You can consider this setting more of a catch all to ensure that your projects performance does not suffer in case someone accidently missed setting a certain meshes cull distance.
To enter the command press the Tilde(~) or Back tick(`) key on the keyboard to open up the Unreal Console with in the UE5 Editor.
When the Unreal Console is opened you should see something that looks like the image below open up at the bottom of the UE5 editor.

[![Console](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a23e5564-c90e-4717-a024-1e6c71387638/05-ue5-console.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a23e5564-c90e-4717-a024-1e6c71387638/05-ue5-console.png)

Click image for full size.

Input the following command into the console, **Foliage.MinimumScreenSize 0.0001**, and then press the **Enter** key to apply the command.
After the Grass Maps rebuild, inside of the viewport you should now see the Static Meshes being used rendered further in the distance than before.

[![Foliage Command](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/39fad67c-efa1-4a50-aeec-400673612fdc/06-ue5-foliage-command.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/39fad67c-efa1-4a50-aeec-400673612fdc/06-ue5-foliage-command.png)

Click image for full size.

Here is a comparison image that shows the difference culling distance between the default setting of **0.0001** and a setting of **0.00000001**.

![Original Settings of 0.0001](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6e7228a3-4cac-4aec-b7f9-11c4b2e7dfb8/07-setting-of-0-0001.png "Original Settings of 0.0001")

![Max Settings of 0.00000001](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/095398f7-8aab-4d64-afad-6ff6eedc5b08/08-setting-of-0-00000001.png "Max Settings of 0.00000001")

Original Settings of 0.0001

Max Settings of 0.00000001

Keep in mind that using values bigger than the default of 0.0001 could cause performance problems.
If you do decide to increase the Foliage.MinimumScreenSize make sure you perform performance testing to ensure that your changes to culling do not have a huge impact on your projects overall performance.

## Procedural Foliage Volume Based Masking

Having the ability to procedurally spawn an entire forest of trees can be a huge time saver, but what if you want to restrict certain trees to only spawn in certain areas?
To accomplish this you could do a number of things like use multiple Procedural Foliage Volumes or use the Foliage tool to place the trees where you want. However, that adds a lot of complexity and upkeep to your project.
Luckily, the **Foliage Types** have the option to restrict the placement of the Static Mesh that is assigned to them to a certain layer in the Landscape Material by allowing only that Foliage Type to spawn when that layer is exposed while painting.

No matter which method you use, you will always need to select the **Procedural Foliage Volume** in the level and click on the **Resimulate** button to update and see your changes.

[![Resim Button](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6a0f367e-8504-4575-8748-8e7196753d94/09-t-resim-button.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6a0f367e-8504-4575-8748-8e7196753d94/09-t-resim-button.png)

Click image for full size.

The image below shows a very simple Landscape Material setup that will allow for three different Foliage Types to be used with three different Textures.
Notice how each input in the **Layer Blend** is uniquely named.
This is important because this name is how we associate which Landscape terrain layer the Foliage Type should be restricted to.

[![Landscape Material](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/301c1367-fcf4-4482-bc5d-3dddc8b5dbd2/10-t-landscape-material.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/301c1367-fcf4-4482-bc5d-3dddc8b5dbd2/10-t-landscape-material.png)

Click image for full size.

Once the Landscape Material has been setup, we now need to setup the Foliage Type so that it can be associated with the correct Landscape layer.
In the image below you can see an example of how a Foliage Type needs to be setup to restrict the placement of the assigned Static Mesh to a specific layer in the Landscape Material.

[![Restrict To Landscape Layers](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/92a89c60-eac9-4622-8a34-92849cc668fa/11-t-restrict-to-landscape-layers.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/92a89c60-eac9-4622-8a34-92849cc668fa/11-t-restrict-to-landscape-layers.png)

Click image for full size.

To set this up for yourself, you will need to do the following inside of the Foliage Type:

1. Expand the **Show Advanced** arrow icon to expose the **Landscape Layers** option.
2. Press the plus sign icon that is to the right of the word **elements** to add a new entry in the array.
3. Input the name of the layer in the Landscape Material that you want to restrict this Foliage Type to.

Once you have the Material and Foliage Types setup, make sure to assign the Material to the Landscape terrain and then start to paint the Landscape as usual.
When you are done painting, or if you just want to see what you have so far, select the Procedural Foliage Volume in the level and then press the **Resimulate** button to update and apply any changes.
When completed, the foliage that was spawned will be confined to the Landscape Texture it is associated with like in the following image.

[![Content Breakdown](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bcf85800-25ab-4369-be8a-2e7caefcda29/12-t-content-breakdown.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bcf85800-25ab-4369-be8a-2e7caefcda29/12-t-content-breakdown.png)

Click image for full size.

If we take a closer look at the image above, we can see that everything has been procedurally placed as expected but none of the spawned meshes intermix with one another.
For example, the leaved trees only spawn where the grass Texture is applied to the Landscape.
If you look closely, you will see that the same occurs with the bush and pine trees.

## Texture Based Masking for the Grass Tool

One of the other methods for controlling where Foliage meshes can or cannot spawn is to use a Texture that acts as a mask telling the Open World Tools to either spawn or not to spawn a Foliage mesh in a specific area.
The following image shows a very simple Material that demonstrates Texture based masking.

[![Texture Based Masking](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bb9e31f4-3c5d-4a0e-b1d0-5833bbff03e8/13-t-texture-based-masking.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bb9e31f4-3c5d-4a0e-b1d0-5833bbff03e8/13-t-texture-based-masking.png)

Click image for full size.

Starting at the far left of this image we have the World Position Scaling section.
This is scaling the Mask Texture in world space so that it can be scaled big enough to fit the Landscape terrain.
Moving to the left, we have the Mask Texture that is used to define where the foliage should be placed, as well as the blending of the two Landscape Textures.
Here is a breakdown of what the different channels of the Mask Texture are used for:

* **Red Channel**: This channel is used to define where the grass meshes should be spawned on the Landscape as well as to define how the Landscape base Textures should be blended.
* **Green Channel**: This channel is used to define where the rock meshes should be spawned on the Landscape.

Finally, on the far right of the image we have the Main Material node and the Grass Output.
The Main Material node is setup in the same way as any other standard Material.
The Grass Output, however, is setup in a similar manner to how you would do Texture based masking, the key difference being that you are going to use the portion of the Material that is masked or unmasked to spawn or not spawn Static Meshes (instead of just showing a different Texture.)
When this Material is applied to a Landscape in UE5 you should get results that look similar to the following image minus the mask Texture that was placed in the corner to show which mask color was doing what to the Landscape.

[![Masking In Action](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f56508f8-eb41-42a5-baf2-e6d86db2dd3b/14-t-masking-in-action.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f56508f8-eb41-42a5-baf2-e6d86db2dd3b/14-t-masking-in-action.png)

Click image for full size.

In the image above, the grass Static Mesh, for the most part, are spawned only in areas that use the red channel of the mask Texture, while the rocks use the green channel of the mask Texture to spawn.
As you might have noticed, the grass and rocks are not entirely contained within the area of the mask Texture that spawns them.
This is expected behavior as the placement of the Static Meshes can be jittered and offset to make things look more natural.

## Math Based Masking for the Grass Tool

While using a Texture for masking can be convenient and quick, there could be times where you can not afford the extra Texture data due to performance concerns or you just do not need that much control over the placement.
In cases like this you can power the placement using Math functions created in the Material Editor in place of Textures.

[![Math Based Masking](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5b050e72-f6b7-42cb-bdd9-10f743e188f0/15-t-math-based-masking.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/5b050e72-f6b7-42cb-bdd9-10f743e188f0/15-t-math-based-masking.png)

Click image for full size.

In the image above, we have taken the Material from the last example but changed how the grass and rocks are spawned.
For this example the grass and rocks are spawned in a checkerboard pattern by using the **Checker Pattern** Material Function to control placement.
The **One Minus** was added to the rocks so that the rocks will spawn in the parts that the grass does not spawn in.
When applied to the Landscape, you will see something that looks like the following:

[![Check Pattern](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/100babc1-a6f7-460a-abfe-a91c9b130ef7/16-t-check-pattern.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/100babc1-a6f7-460a-abfe-a91c9b130ef7/16-t-check-pattern.png)

Click image for full size.

## Non Random Placement for the Grass Tool

With the right adjustments, the Grass tool can also be used to simulate things like crops growing in a field.
In the image below you can see an example of this type of behavior:

[![Spawing In Row](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a1f8d4fc-6191-4ffc-b5bd-f008facc2b9b/17-t-spawing-in-row.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a1f8d4fc-6191-4ffc-b5bd-f008facc2b9b/17-t-spawing-in-row.png)

Click image for full size.

To get the Grass tool to function like this, make sure that **Use Grid** is checked, that **Placement Jitter** is set to **0**, and **Grass Density** is set to something under 100.
The following image shows how the Landscape Grass Type was set up to achieve the results you saw in the first image.

[![LGT Crops Setup](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/10a923dc-b611-4ded-b3a9-a55099b27aa1/18-t-lgt-crops-setup.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/10a923dc-b611-4ded-b3a9-a55099b27aa1/18-t-lgt-crops-setup.png)

Click image for full size.

* [landscape](https://dev.epicgames.com/community/search?query=landscape)
* [building virtual worlds](https://dev.epicgames.com/community/search?query=building%20virtual%20worlds)
* [open world](https://dev.epicgames.com/community/search?query=open%20world)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Grass Tool Foliage Mesh Culling](/documentation/en-us/unreal-engine/open-world-tools-tips-in-unreal-engine?application_version=5.7#grasstoolfoliagemeshculling)
* [Procedural Foliage Volume Based Masking](/documentation/en-us/unreal-engine/open-world-tools-tips-in-unreal-engine?application_version=5.7#proceduralfoliagevolumebasedmasking)
* [Texture Based Masking for the Grass Tool](/documentation/en-us/unreal-engine/open-world-tools-tips-in-unreal-engine?application_version=5.7#texturebasedmaskingforthegrasstool)
* [Math Based Masking for the Grass Tool](/documentation/en-us/unreal-engine/open-world-tools-tips-in-unreal-engine?application_version=5.7#mathbasedmaskingforthegrasstool)
* [Non Random Placement for the Grass Tool](/documentation/en-us/unreal-engine/open-world-tools-tips-in-unreal-engine?application_version=5.7#nonrandomplacementforthegrasstool)
