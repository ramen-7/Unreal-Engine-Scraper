<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-motion-blur?application_version=5.7 -->

# Setting Up Motion Blur

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
5. [Creating Visual Effects](/documentation/en-us/unreal-engine/creating-visual-effects-in-niagara-for-unreal-engine "Creating Visual Effects")
6. [Niagara Tutorials](/documentation/en-us/unreal-engine/tutorials-for-niagara-effects-in-unreal-engine "Niagara Tutorials")
7. [Niagara for Linear Content](/documentation/en-us/unreal-engine/niagara-for-linear-content "Niagara for Linear Content")
8. Setting Up Motion Blur

# Setting Up Motion Blur

Learn how to set up motion blur for your Niagara system render.

![Setting Up Motion Blur](https://dev.epicgames.com/community/api/documentation/image/15502df3-0f36-4854-aba7-5d537d38433a?resizing_type=fill&width=1920&height=335)

 On this page

## Motion Blur

Unreal Engine uses a **Velocity GBuffer** to apply **motion blur** to the rendered image. The technique is very fast for real time applications but the artifacts are often not acceptable for Linear Content.

The Velocity GBuffer stores a single vector per pixel. The technique is not able to blur secondary motion such as shadows and reflections. It can also introduce artifacts when fast moving objects cross paths.

## Movie Render Queue: Temporal Sample Count

As we can usually afford longer render times with Linear Content production, we can improve quality by rendering multiple images per frame. Each render is distributed evenly through the shutter open time. These renders are then combined to produce a final high quality frame.



If you have toggled on the **Lock to Display Rate at Runtime** option for accurate previews, you must switch it OFF for **Temporal Samples** to take effect. This setting will override the effect of Temporal Samples.

Sequencer ticks according to the number of temporal samples you define. As a result the time step passed to your simulation will also change based on the temporal sample count.

An added complication is the fact that Sequencer will add temporal samples only during the part of the frame when the camera shutter is open, typically for half the frame. As a result your simulation will be passed a series of very small time steps during shutter open, followed by one large time step during shutter close. Some simulation types have issues with this kind of irregular stepping and can cause artifacts.

![Time steps during the simulation](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/110a4b40-4989-4cc0-bcdf-757596e549ad/timeline_v2.png)

The diagram above shows the **time steps** (in red) passed to the simulation. Through shutter open the time steps are 8 times smaller than through shutter close.

Grid simulations are especially susceptible to changes in the time steps per frame. If a grid simulation ticks 9 times per frame it will look quite different to the same simulation that ticks once. Having the time step change between shutter open and shutter close only makes these differences more pronounced.

If you are dealing with grid based simulations, set the system's **Fixed Tick Delta Time** to match **Sequencers frame rate** (eg: if Sequencer is set to 30fps, set the Fixed Tick Delta Time to (1.0/30) or 0.33333.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Motion Blur](/documentation/en-us/unreal-engine/setting-up-motion-blur?application_version=5.7#motionblur)
* [Movie Render Queue: Temporal Sample Count](/documentation/en-us/unreal-engine/setting-up-motion-blur?application_version=5.7#movierenderqueue:temporalsamplecount)
