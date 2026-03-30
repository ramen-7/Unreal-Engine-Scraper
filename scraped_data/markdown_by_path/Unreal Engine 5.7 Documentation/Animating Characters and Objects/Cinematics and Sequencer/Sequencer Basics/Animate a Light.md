<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-animate-lights-in-unreal-engine?application_version=5.7 -->

# Animate a Light

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
8. Animate a Light

# Animate a Light

A beginner's guide at how to animate lights in Sequencer.

![Animate a Light](https://dev.epicgames.com/community/api/documentation/image/8f2b6408-a193-4a91-8b43-242b05ef805e?resizing_type=fill&width=1920&height=335)

 On this page

This page provides a beginner's overview of how to animate lights in Sequencer and is intended for those who are new to Cinematics and Unreal Engine.

#### Prerequisites

* You have read through the [Sequencer Basics](/documentation/en-us/unreal-engine/how-to-make-movies-in-unreal-engine) page and have already created and opened a **Level Sequence** in your level.
* [Lights](/documentation/en-us/unreal-engine/light-types-and-their-mobility-in-unreal-engine) are in your level.

## Adding a Light to Sequencer

Start by adding a light to your sequence. To do this, click **Add Track (+)** and select **Actor to Sequencer > Add 'Light'**. Any type of light Actor can be added as a track in Sequencer.

![add light to sequencer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/b658005b-91be-4b81-aefc-eb7a56f29e47/addlight.png)


Whenever a light is added to Sequencer, it will [automatically add](/documentation/en-us/unreal-engine/cinematic-actor-tracks-in-unreal-engine#automatictrackcreation) some of its commonly used tracks to the sequence. In this example, **Intensity** and **Light Color** tracks were automatically added.

## Animating Intensity

To animate a light's intensity, select the **Intensity** track and press **Enter**. This will set a keyframe with the current intensity value.

![animate light intensity](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4df3300c-153d-4344-bd84-7028d5d90360/intensity1.gif)

Next, move the playhead to a later point in the sequence by dragging it.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/62a79510-d045-4e09-9caa-ee33d30a75ef/scrublater.png)

Finally, set a new intensity value by manipulating the value of the **Intensity** track. You can do this by either dragging it to change the value, or by selecting the textbox and typing the value directly. Either method will result in a new keyframe being created at the playhead. At this point you can drag the playhead along the sequence, or play the sequence to preview your animation.

![animate light intensity](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3a1a9633-007c-4379-9b41-f88c21fb8816/intensity2.gif)

## Animating Color

To change a light's color, select the **Light Color** track and press **Enter**. This will set a keyframe at the current color value. Double-click the keyframe to open the color picker tool, then select a color value and click **OK** to confirm the change.

![animate light color](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/80e736a1-e4cb-4f10-8573-cd238c8b19db/color1.gif)

Next, move the playhead to a later point in the sequence by dragging it.

![](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/af9104ad-467f-4138-94e7-c1dd172b4cde/scrublater2.png)

Set a new color keyframe by selecting the **Light Color** track and pressing **Enter** to create another keyframe. Double-click that keyframe and select a color from the color picker tool. At this point, you can play or scrub the sequence to preview your color animation.

![animate light color](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/2f0897f6-2da7-482a-b582-a95985ed9fe7/color2.gif)

* [animation](https://dev.epicgames.com/community/search?query=animation)
* [lights](https://dev.epicgames.com/community/search?query=lights)
* [sequencer](https://dev.epicgames.com/community/search?query=sequencer)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Prerequisites](/documentation/en-us/unreal-engine/how-to-animate-lights-in-unreal-engine?application_version=5.7#prerequisites)
* [Adding a Light to Sequencer](/documentation/en-us/unreal-engine/how-to-animate-lights-in-unreal-engine?application_version=5.7#addingalighttosequencer)
* [Animating Intensity](/documentation/en-us/unreal-engine/how-to-animate-lights-in-unreal-engine?application_version=5.7#animatingintensity)
* [Animating Color](/documentation/en-us/unreal-engine/how-to-animate-lights-in-unreal-engine?application_version=5.7#animatingcolor)
