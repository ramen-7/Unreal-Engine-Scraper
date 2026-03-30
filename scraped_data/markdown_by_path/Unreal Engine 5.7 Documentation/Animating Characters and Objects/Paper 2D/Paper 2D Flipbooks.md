<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/paper-2d-flipbooks-in-unreal-engine?application_version=5.7 -->

# Paper 2D Flipbooks

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
5. [Animating Characters and Objects](/documentation/en-us/unreal-engine/animating-characters-and-objects-in-unreal-engine "Animating Characters and Objects")
6. [Paper 2D](/documentation/en-us/unreal-engine/paper-2d-overview-in-unreal-engine "Paper 2D")
7. Paper 2D Flipbooks

# Paper 2D Flipbooks

Description of Paper 2D Flipbooks and how to create them.

![Paper 2D Flipbooks](https://dev.epicgames.com/community/api/documentation/image/5443f0d8-9119-49ca-8e10-35c57d95bdcd?resizing_type=fill&width=1920&height=335)

 On this page

![The best way to think of Paper 2D Flipbooks is in the form of hand-drawn animation](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d009820d-98dc-42f8-9963-169de93cffed/flipbook-banner-2.png)


The best way to think of **Paper 2D Flipbooks** (or **Flipbooks** for short) is in the form of hand-drawn animation, where a series of images that are slightly different are "flipped" through to produce what appears to be motion. In Unreal Engine, Flipbooks consist of a series of keyframes, each of which contains a [Sprite](/documentation/en-us/unreal-engine/how-to-import-and-use-paper-2d-sprites-in-unreal-engine) to be displayed and a duration (in frames) to display it.
A **Frames Per Second** option determines how fast the frames will be displayed, indicating how many animation "beats" will occur in a second and the keyframes themselves can be edited in the **Details** panel or by using a **Timeline** which can be found at the bottom of the **Flipbook Editor**.

## Creating a Flipbook

There are a couple of ways you can go about creating a Flipbook. You can either create a blank Flipbook that you populate with sprites yourself or you can auto-generate a Flipbook based off a series of selected sprites.

You can import a JSON-formatted sprite sheet description, which will import associated textures and create sprites and a Flipbook for the described frames as well. See [Paper 2D Import Options](/documentation/en-us/unreal-engine/import-sprites-in-unreal-engine) for more information.

### Blank Flipbooks

Creating a blank Flipbook can be achieved by following the steps below.

**From the Content Drawer**:

1. Click the **+Add** button, then in the context menu under *Animation*, select the **Paper Flipbook** option.

   ![In the context menu under Animation select the Paper Flipbook option](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2b6acf07-a9b3-4ba6-892d-56e7b9384f25/flipbook-create-1.png)


   You can also **Right-click** inside the **Content Drawer** to open the context menu instead of clicking **Add New**.
2. You will then be prompted to enter a name for your new Flipbook.

   ![New Flipbook](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/90695073-73a0-438a-95f2-1531c519e588/flipbook-create-2.png)
3. After you select a name, your Flipbook asset has been created.

   ![Your Flipbook asset has been created](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/22e7e433-fbc9-44f7-b1d3-b76e6478db61/flipbook-create-3.png)

   The asterisk symbol in the lower-left corner indicates that the asset has not been saved yet and will go away when you save it.

### Auto-Generated Flipbooks

To create an automatically generated Flipbook, follow the steps below.

**From the Content Drawer**:

1. Locate and select each of the sprites you would like to include in the Flipbook in the **Content Drawer**.

   ![Locate and select each of the sprites you would like to include in the Flipbook in the Content Drawer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6638d6c0-62a4-4e81-bd08-47f405b72835/autocreate-1.png)
2. **Right-click** on any of the sprites, then select the **Create Flipbook** option from the context menu.

   ![Select the Create Flipbook option from the context menu](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9b5a71e9-e0e2-42b4-89d8-9b8000c51058/autocreate-2.png)
3. You will then be prompted to enter a name for your new Flipbook.

   ![You will then be prompted to enter a name for your new Flipbook](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d25c9055-b1ca-42f0-911f-573add3a104b/autocreate-3.png)
4. After you select a name, your Flipbook asset has been created.

   ![Your Flipbook asset has been created](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a5445379-8f15-4090-a9a7-b73be5023062/autocreate-4.png)

   When you mouse over the Flipbook in the **Content Drawer**, you will also be able to preview the Flipbook animation.

When auto-generating a Flipbook, the naming convention you use for the sprites included is **very important** as the sprites will be added to the Flipbook in alphabetical order. In the example above, we've named each of our sprites for creating an Idle to **Idle\_x** where X is the order in which we want the sequence to appear.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Creating a Flipbook](/documentation/en-us/unreal-engine/paper-2d-flipbooks-in-unreal-engine?application_version=5.7#creatingaflipbook)
* [Blank Flipbooks](/documentation/en-us/unreal-engine/paper-2d-flipbooks-in-unreal-engine?application_version=5.7#blankflipbooks)
* [Auto-Generated Flipbooks](/documentation/en-us/unreal-engine/paper-2d-flipbooks-in-unreal-engine?application_version=5.7#auto-generatedflipbooks)
