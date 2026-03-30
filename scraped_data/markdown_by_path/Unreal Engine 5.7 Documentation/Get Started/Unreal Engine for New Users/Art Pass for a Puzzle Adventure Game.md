<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/art-pass-for-a-puzzle-adventure-game?application_version=5.7 -->

# Art Pass for a Puzzle Adventure Game

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
5. [Get Started](/documentation/en-us/unreal-engine/get-started "Get Started")
6. [Unreal Engine for New Users](/documentation/en-us/unreal-engine/unreal-engine-for-new-users "Unreal Engine for New Users")
7. Art Pass for a Puzzle Adventure Game

# Art Pass for a Puzzle Adventure Game

Learn how you can apply art workflows with materials, sounds, and visual effects to the Puzzle Adventure game.

![Art Pass for a Puzzle Adventure Game](https://dev.epicgames.com/community/api/documentation/image/7a997a0f-bae4-4504-acd0-b5c30e647e47?resizing_type=fill&width=1920&height=335)

 On this page

Unreal Engine includes a suite of tools designed to empower designers and artists to bring their projects to life in intuitive and creative ways. Its tools enable you — as an artist, designer, or tech artist — to create highly detailed and fully realized game worlds right inside of the editor, and for real-time experiences.

This series of guides will walk you through the process of learning in-editor workflows and tools you can use to perform an art-pass on the worlds you build. The artistic choices you make for your games are subjective. This series builds on things you may have learned in the Designer Track, or you may be starting from scratch with this track. In either case, you’ll learn foundational workflows through practical examples and how you can tie some art-focused tools to gameplay.

### Artist Track Overview

This series provides a starting point for learning beginner-friendly artist-driven workflows through practical game and gameplay-oriented examples. These can help you better understand how the various systems and tools of Unreal Engine work together to bring your games to life.

Through this series you’ll learn how to:

* Import content that you’ll use to build materials and audio for this game.

* Use localized light sources to create atmosphere while highlighting design elements using the built-in properties of lights.
* Create materials and material instances that use parent/child relationships to design and edit surface properties of scene geometry.
* Expand your learnings of material instancing through an interactive gameplay example.
* Add post-processing to set the look and feel of the scene in a non-destructive way.
* Combine post processing with materials to create a damage effect during gameplay.
* Creating original music using the built-in MetaSounds synthesizer for ambient background music.
* Combine gameplay-driven sounds with materials so that your character uses different sounds while walking on different surfaces.
* Create a visual effect using the built-in visual effects system Niagara.

### Before you Begin

This is the third series in a beginner set of courses designed to get new users started with Unreal Engine. While the course is designed to be usable without having completed the previous courses, you will get the most out of this series  after having followed along [Code a First Person Adventure Game](https://dev.epicgames.com/documentation/en-us/unreal-engine/code-a-firstperson-adventure-game-in-unreal-engine) and [Design a Puzzle Adventure Game](https://dev.epicgames.com/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine). The things you’ll learn in these courses will reinforce what you continue to learn in this one.

The level featured in this course picks up where the Design a Puzzle Adventure Game finished. While you do not specifically need to use that project’s level and design for some aspects to get value out of this course, some elements will require this project to complete the steps.

Below you will find the project in two states:

* A clean copy that picks up where the Design a Puzzle Adventure Game finished.
* A version completed using concepts and workflow examples created using the content in this course.

## Example Project

Below is a link to download the final sample project that you can build using this tutorial series. You can use this example project to see what your final project might look like, or as a reference to see how we built and designed the project.

Art direction is its own design choice for any project. While many things will be demonstrated throughout this series of guides, you are encouraged to experiment and make your own choices when they make sense to do so. Lighting, post-processing, some parts of material development, sounds, and so on, all offer room for experimentation as you learn how to work with them. In many respects, the choices you make that differ from this course’s example will not limit or stop you from being able to complete it.

[Download the Artist Track Example Project here](https://d1iv7db44yhgxn.cloudfront.net/documentation/attachments/af343c86-db02-4b00-aef0-efb7e0e54998/adventureartist.zip)

* [![Set Up Your Project and Import Content](https://dev.epicgames.com/community/api/documentation/image/4bf727d1-7354-471e-ad05-6a3a7d570699?resizing_type=fit&width=640&height=640)

  Set Up Your Project and Import Content

  Setting up your project and importing content.](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-01-project-setup-and-content-import)
* [![Light a Scene](https://dev.epicgames.com/community/api/documentation/image/554f65ca-c199-4103-9380-850b74958081?resizing_type=fit&width=640&height=640)

  Light a Scene

  Learn to light your level and set the mood with Spot Lights, Point Lights, and Rect Lights.](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-02-light-a-scene)
* [![Create Materials and Material Instances](https://dev.epicgames.com/community/api/documentation/image/8e452b45-4ccc-4be0-af67-f51041daf936?resizing_type=fit&width=640&height=640)

  Create Materials and Material Instances

  Use materials and material instances to surface a level.](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-03-create-materials-and-material-instances)
* [![Expanded Material Instances](https://dev.epicgames.com/community/api/documentation/image/5c65ff06-ef34-4979-b59c-affce510d5b7?resizing_type=fit&width=640&height=640)

  Expanded Material Instances

  Use dynamic material instances to create an interactive tech demo.](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-04-expanded-material-instances)
* [![Add Post Process Volumes](https://dev.epicgames.com/community/api/documentation/image/77b586de-baf5-45f8-bc6b-125bcd355f18?resizing_type=fit&width=640&height=640)

  Add Post Process Volumes

  Create post process volumes to control the look and performance of a level.](https://dev.epicgames.com/documentation/en-us/unreal-engine/add-post-process-volumes)
* [![Post Process Materials on the UI](https://dev.epicgames.com/community/api/documentation/image/5cd78a95-6add-4a47-bad1-41ab6f2f7f32?resizing_type=fit&width=640&height=640)

  Post Process Materials on the UI

  Learn how to use Materials to create gameplay-driven, on-screen post-process effects.](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-06-post-process-materials-on-the-ui-in-unreal-engine)
* [![Adjust Environment Lighting Features](https://dev.epicgames.com/community/api/documentation/image/dec29683-7a6c-4230-bee7-ed15fd14d1b8?resizing_type=fit&width=640&height=640)

  Adjust Environment Lighting Features

  Learn to enhance your level's atmospheric elements by adding denser fog in low-lying areas and adding storm clouds in the sky.](https://dev.epicgames.com/documentation/en-us/unreal-engine/07-adjust-environment-lighting-features)
* [![Add Sounds to Fire Traps](https://dev.epicgames.com/community/api/documentation/image/7a433b5e-267f-48e8-a8b3-7f0cffdf736e?resizing_type=fit&width=640&height=640)

  Add Sounds to Fire Traps

  Learn how to add a sound effect to a Blueprint.](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-09-adding-sounds-to-fire-traps-artist-track-unreal-engine)
* [![Create Procedural Music](https://dev.epicgames.com/community/api/documentation/image/ee725e45-9ab6-484f-b4c8-969dbba1fb80?resizing_type=fit&width=640&height=640)

  Create Procedural Music

  Create Procedural Music with MetaSounds.](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-10-create-procedural-music-with-metasounds)
* [![Add Footstep Sounds to a Character](https://dev.epicgames.com/community/api/documentation/image/e85f58fa-4b9d-413d-87f2-9baacc3848e4?resizing_type=fit&width=640&height=640)

  Add Footstep Sounds to a Character

  Make a character produce different step sounds as they move across different surfaces.](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-11-add-footstep-sounds-to-a-character)
* [![Add Visual Effects to Your Game](https://dev.epicgames.com/community/api/documentation/image/97f8e7ce-a1bb-4489-8a34-6ea0d7884299?resizing_type=fit&width=640&height=640)

  Add Visual Effects to Your Game

  Add visual effects to your game!](https://dev.epicgames.com/documentation/en-us/unreal-engine/at12-adding-visual-effects-to-your-game)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Artist Track Overview](/documentation/en-us/unreal-engine/art-pass-for-a-puzzle-adventure-game?application_version=5.7#artisttrackoverview)
* [Before you Begin](/documentation/en-us/unreal-engine/art-pass-for-a-puzzle-adventure-game?application_version=5.7#beforeyoubegin)
* [Example Project](/documentation/en-us/unreal-engine/art-pass-for-a-puzzle-adventure-game?application_version=5.7#exampleproject)

Related documents

[Your First Hour in Unreal Engine

![Your First Hour in Unreal Engine](https://dev.epicgames.com/community/api/documentation/image/b68b5e7a-09df-4354-acb4-2fb8b3291793?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/first-hour-in-unreal-engine)

[Design a Puzzle Adventure

![Design a Puzzle Adventure](https://dev.epicgames.com/community/api/documentation/image/a7b7ff2c-23d0-47a0-8a04-e569209942b0?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine)

[Unreal Engine for New Users](/documentation/en-us/unreal-engine/unreal-engine-for-new-users)
