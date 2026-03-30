<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-add-cinematic-animation-to-a-character-in-unreal-engine?application_version=5.7 -->

# Apply Animation to a Character

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
6. [Cinematics and Sequencer](/documentation/en-us/unreal-engine/cinematics-and-movie-making-in-unreal-engine "Cinematics and Sequencer")
7. [Sequencer Basics](/documentation/en-us/unreal-engine/how-to-make-movies-in-unreal-engine "Sequencer Basics")
8. Apply Animation to a Character

# Apply Animation to a Character

A beginner's guide at how to add character animation in Sequencer.

![Apply Animation to a Character](https://dev.epicgames.com/community/api/documentation/image/0e343161-bd09-4ec7-ada6-e6638485da94?resizing_type=fill&width=1920&height=335)

 On this page

This page provides a beginner's overview of how to animate Skeletal Meshes in Sequencer, and is intended for those who are new to Sequencer and Unreal Engine.

#### Prerequisites

* You have read through the [Sequencer Basics](/documentation/en-us/unreal-engine/how-to-make-movies-in-unreal-engine) page and have already created and opened a **Level Sequence** in your Level.
* Your project contains a [Skeletal Mesh](/documentation/en-us/unreal-engine/skeletal-mesh-assets-in-unreal-engine) and [Animation Sequence](/documentation/en-us/unreal-engine/animation-sequences-in-unreal-engine). If not, you can create a project using the [Third Person template](/documentation/404), which provides sample Skeletal Meshes and animations.

## Adding a Character to Sequencer

Start by adding a character to your Level. Do this from the [Content Browser](/documentation/en-us/unreal-engine/content-browser-in-unreal-engine) by navigating to your asset and dragging it into your Level.

![add skeletal mesh](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/24ecb7e8-c4bb-40fc-ad1a-35e96e4b2940/addchar1.png)

Next, with your sequence open and the character selected, click **Add Track (+)** and select **Actor to Sequencer > Add 'SKM\_Manny2'**. This will add a track referencing the character into your sequence.

![character add sequencer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7174834d-7c6b-4baa-8bf9-82d17b7ef9e2/addchar2.png)


When the Skeletal Mesh track is added to the sequence, it [automatically adds](/documentation/en-us/unreal-engine/cinematic-actor-tracks-in-unreal-engine#automatictrackcreation) commonly used tracks for this Actor. In this example, [Animation](/documentation/en-us/unreal-engine/cinematic-animation-track-in-unreal-engine) and [Transform](/documentation/en-us/unreal-engine/cinematic-transform-and-property-tracks-in-unreal-engine) tracks are automatically created.

## Applying Animation to a Character

Click **Add Animation (+)** on the Animation track. This will list all available animations that are compatible with your character's skeleton. Select one of these animations to add it to your sequence.

![add animation sequencer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a25d3666-78b7-40a7-ad6b-ca210b110074/addanim.png)

Once the animation is added, click **Play** to preview the sequence. If the animation is intended to continue past the current endpoint, you can drag the edge of the clip to extend it.

![play character animation sequencer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/55d8e9d4-35c7-4d5d-937d-26019a937bc2/play.gif)

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [sequencer](https://dev.epicgames.com/community/search?query=sequencer)
* [character](https://dev.epicgames.com/community/search?query=character)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisites](/documentation/en-us/unreal-engine/how-to-add-cinematic-animation-to-a-character-in-unreal-engine?application_version=5.7#prerequisites)
* [Adding a Character to Sequencer](/documentation/en-us/unreal-engine/how-to-add-cinematic-animation-to-a-character-in-unreal-engine?application_version=5.7#addingacharactertosequencer)
* [Applying Animation to a Character](/documentation/en-us/unreal-engine/how-to-add-cinematic-animation-to-a-character-in-unreal-engine?application_version=5.7#applyinganimationtoacharacter)
