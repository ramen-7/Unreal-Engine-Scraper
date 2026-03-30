<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/production-considerations?application_version=5.7 -->

# Production Considerations

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
8. Production Considerations

# Production Considerations

Learn about production considerations when rendering your Niagara systems.

![Production Considerations](https://dev.epicgames.com/community/api/documentation/image/9e6fc0a9-1fb1-4c99-b500-fa8e364d64f6?resizing_type=fill&width=1920&height=335)

 On this page

## Production Considerations

In most cases, you will not be working in isolation. Other artists will need to check out the files you are using. This can result in work stoppages as you wait for the files you need to be released back to you.

There are several methodologies you can employ to allow teams to work in parallel:

* Add per discipline level sequences to each shot.
* Add per discipline sub levels to each Persistent/Sequence based level.

Depending on the size of your team you may want to break down even further by adding per artist and/or per shot level sequences and sub levels.

![Separate sequences](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4870c614-955d-4880-834f-a9ff488b88b0/shotsetup1.png)

Another technique you can employ is the use of **Spawnable** actors instead of **Possessable** actors.

A Spawnable actor is created by Sequencer. It does not exist within the level until you open the Level Sequence which spawns it. As a result you do not need access to the persistent level to add or modify an actor.

Spawnable actors can be created by either:

* Converting a Possessable actor to Spawnable.
* Dragging an asset from the Content Browser directly into Sequencer.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Production Considerations](/documentation/en-us/unreal-engine/production-considerations?application_version=5.7#productionconsiderations)
