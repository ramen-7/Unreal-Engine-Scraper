<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/testing-and-setup-in-metahuman-creator?application_version=5.7 -->

# Testing and Setup in MetaHuman Creator

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
5. [Gameplay Systems](/documentation/en-us/unreal-engine/gameplay-systems-in-unreal-engine "Gameplay Systems")
6. [Physics](/documentation/en-us/unreal-engine/physics-in-unreal-engine "Physics")
7. [Cloth Simulation](/documentation/en-us/unreal-engine/cloth-simulation-in-unreal-engine "Cloth Simulation")
8. [Creating Parametric Clothing for Fab](/documentation/en-us/unreal-engine/creating-parametric-clothing-for-fab "Creating Parametric Clothing for Fab")
9. Testing and Setup in MetaHuman Creator

# Testing and Setup in MetaHuman Creator

Test your outfit asset in MetaHuman Creator.

![Testing and Setup in MetaHuman Creator](https://dev.epicgames.com/community/api/documentation/image/0857c289-1bc9-47dc-a4e7-20bb89e5dc74?resizing_type=fill&width=1920&height=335)

 On this page

Now that you’ve created your outfit, it's time to test it. To test your outfit asset in **MetaHuman Creator** (MHC), follow these steps:

1. In the **Unreal Editor,** right-click in the **Content Browser**. Select **MetaHuman > MetaHuman Character**to create a new character. Give it a name and press Enter to save it.
2. Double-click the character to open up **MetaHuman Creator**.

   [![](https://dev.epicgames.com/community/api/documentation/image/7510d291-1b6d-4cad-a2bb-e06aadf59bb1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7510d291-1b6d-4cad-a2bb-e06aadf59bb1?resizing_type=fit)
3. Click on the **Hair & Clothing** tool, and scroll down to the bottom. Here you will see a section called **Outfit Clothing**. Drag your outfit asset from the **Content Browser** into this section.

   Once your outfit asset is transferred, double-click it or click the **Wear** button to apply it to your character. You will see it resize automatically.

   To remove an item, double-click it again or click the **Remove** button.

   There may be a short delay in wearing an item for the first time while the underlying assets are prepared for use.

   A character can wear more than one clothing item in each slot at a time. To avoid this, remove items you no longer want your character to wear by double-clicking them or clicking the **Remove** button.
4. Select the **Body** tool and adjust the sliders or apply body presets to see how your outfit resizes. If the outfit doesn’t fit accurately to a certain body type, export that body type and create a new size for it.

   As you are changing body shapes, your outfit asset should be switching between source assets, selecting the best possible fit for the body.
5. Navigate back to the **Content Browser**. A new wardrobe asset called `WI_[yourAssetName]` has been added.

   This asset allows you to change the colors of your clothing within MHC, if the asset materials have already been set up to have their colors changed.

   Double-click the asset to open the details. The **Principal Asset** should already have the outfit asset selected.

   [![Principle Asset](https://dev.epicgames.com/community/api/documentation/image/ee171fb3-7194-4227-ad8c-8b4e3cb2fd7c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ee171fb3-7194-4227-ad8c-8b4e3cb2fd7c?resizing_type=fit)
6. Next, for the **Pipeline**, select **MetaHuman Outfit Pipeline** from the dropdown menu.

   The Pipeline sub-menus is where you add your material parameters. For each color you want to be customizable, click the **+** button next to **Runtime Material Parameters**.

   [![](https://dev.epicgames.com/community/api/documentation/image/aaec3a92-ae60-4a7a-91d5-d3873129f2bb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/aaec3a92-ae60-4a7a-91d5-d3873129f2bb?resizing_type=fit)
7. Expand the **Runtime Material Parameters** section. For each addition you make with the **+** button, an index item will be added. In this example, the techwear outfit has 9.

   [![Techwear Indices](https://dev.epicgames.com/community/api/documentation/image/46dc8b34-c462-4d0d-a309-7af6164be33b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/46dc8b34-c462-4d0d-a309-7af6164be33b?resizing_type=fit)

   Each of these indexes corresponds to one color section. Expanding an Index menu gives you the ability to type in a description to help identify which areas on the clothing the color affects. For example, one index changes the color of the cuffs of the jacket, so it is given the name `JacketCuffsColor`.
8. (Optional) If you have more than one size for your outfit asset, or if the meshes share the same material, open up your outfit asset again. Otherwise, skip this step.

   Verify in your outfit asset which size corresponds to which index, and how many indexes you have. This is how many sizes you made. The techwear outfit example has two.

   [![Number Of Indices](https://dev.epicgames.com/community/api/documentation/image/9bee8280-73f1-48dd-a5ad-d7fdcc980420?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9bee8280-73f1-48dd-a5ad-d7fdcc980420?resizing_type=fit)
9. Next, you need to define the **Slot Names**. Click the **+** button next to Slot Names as many times as you have sizes (or indexes in your outfit asset).

   [![Slot Names](https://dev.epicgames.com/community/api/documentation/image/ccaaa14c-530f-423d-bac4-580bd0869923?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ccaaa14c-530f-423d-bac4-580bd0869923?resizing_type=fit)
10. Expand the **Material Parameter** section.

    Find the parameter in your materials which is associated with the color you are looking to control, and type that in the **Name** field.

    This parameter must match in all materials across all sizes. Set up your first material and then copy it to the other sizes, changing the maps or other attributes accordingly.

    For the jacket cuffs example, that parameter was named `B_diffuse_color_1`.

    [![Parameter Type](https://dev.epicgames.com/community/api/documentation/image/111d6e72-b90a-4365-ac39-6d14c16aebe2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/111d6e72-b90a-4365-ac39-6d14c16aebe2?resizing_type=fit)
11. Next, set **Parameter Type** to **Vector**. Repeat this process for as many different colors as you have.
12. Under **Editor Pipeline > Outfit**, add the **Body Hidden Face Map**.

    This map tells MHC which faces of the body are always hidden by the clothing, and removes them in the assembly process.  This makes the garment look better by reducing clipping, and also makes the MetaHuman more efficient.

    You must first create this map by obtaining the uv map from the MetaHuman body in your DCC of choice.  Then, paint parts of the body that should be shown in White and parts to be hidden in Black.

    Below is an example of the map used for the `techwearOutfit`. The techwear outfit covers most of the body which is why it’s mostly black.

    [![](https://dev.epicgames.com/community/api/documentation/image/14e7855b-2965-47ef-827e-8db6ce41611c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/14e7855b-2965-47ef-827e-8db6ce41611c?resizing_type=fit)

    Though we are using the combined Head & Body to create the clothing, actual MetaHumans have separate head and body meshes. We are unable to hide faces on the head mesh at this time.

    Add this map by first dragging it into the Content Browser, then add it to the **Body Hidden Face Map**.

    [![](https://dev.epicgames.com/community/api/documentation/image/395d68dd-ffa4-4a04-b4d7-8a3ba497411c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/395d68dd-ffa4-4a04-b4d7-8a3ba497411c?resizing_type=fit)
13. Once you’re happy with the result, save it.
14. Finally, to add the item to your wardrobe, drag the Wardrobe Item (`WI_`) into the **Outfit Clothing** section of the **Hair & Clothing** tool.

Be sure to drag the **Wardrobe Item****Asset** instead of the Outfit Asset, as dragging in the Outfit Asset will cause MHC to overwrite your existing Wardrobe Item Asset.

Now, in MHC, you (or the person who purchases your garment) can use the Details panel of the Hair & Clothing tool to customize the colors of your outfit.

[![Hair And Clothing](https://dev.epicgames.com/community/api/documentation/image/cd132236-3fd0-419e-af70-6eb0acdae5bc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cd132236-3fd0-419e-af70-6eb0acdae5bc?resizing_type=fit)

## Next Step

* [![Packaging Your Outfit Asset](https://dev.epicgames.com/community/api/documentation/image/d89e5f10-5199-4521-8477-5c967c519917?resizing_type=fit&width=640&height=640)

  Packaging Your Outfit Asset

  Packaging a MetaHuman Outfit Asset in Unreal Engine.](https://dev.epicgames.com/documentation/en-us/unreal-engine/packaging-your-outfit-asset)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Next Step](/documentation/en-us/unreal-engine/testing-and-setup-in-metahuman-creator?application_version=5.7#nextstep)
