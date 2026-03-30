<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-01-project-setup-and-content-import?application_version=5.7 -->

# Set Up Your Project and Import Content

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
7. [Art Pass for a Puzzle Adventure Game](/documentation/en-us/unreal-engine/art-pass-for-a-puzzle-adventure-game "Art Pass for a Puzzle Adventure Game")
8. Set Up Your Project and Import Content

# Set Up Your Project and Import Content

Setting up your project and importing content.

![Set Up Your Project and Import Content](https://dev.epicgames.com/community/api/documentation/image/0ac26f8f-2b4f-4a18-8d4b-fde8c4236d30?resizing_type=fill&width=1920&height=335)

###### Prerequisite topics

In order to understand and use the content on this page, make sure you are familiar with the following topics:

* [Design a Puzzle Adventure](/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine)

 On this page

As you start to follow this course, you’ll need to know a few things in order to follow along and make sure you have everything you need to complete the tasks. You’ll go over the list of things you’ll need and walk through the steps to import the content you’ll need later in this course as well. Finally, you’ll be reminded of some good practices for keeping your project organized so that it’s easier to quickly locate assets and work with others in a collaborative way.

## Before You Begin

Before you get started with this project, here are some things to keep in mind and be aware of:

* Install the Epic Games Launcher and Unreal Engine.

  + For more information, see [Install Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/install-unreal-engine).
* This project and its content were developed and written using **Unreal Engine 5.6**.

  + This will not prevent you from using the content you download if you’re using a later version of the engine. Also, it shouldn’t prevent you from following the steps in this series, even though some parts (like material nodes) may look a little different.
* Familiarizing yourself with the Unreal Editor’s interface. You can start by checking out these pages:

  + [Unreal Editor Interface](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-editor-interface)
  + [Viewport Controls](https://dev.epicgames.com/documentation/en-us/unreal-engine/viewport-controls-in-unreal-engine)
  + [Viewport Toolbar](https://dev.epicgames.com/documentation/en-us/unreal-engine/viewport-toolbar)

This course picks up where the [Design a Puzzle Adventure Game](https://dev.epicgames.com/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine) left off using the same project. Using the project will be required for some parts of this course. If you did not complete that course or want to start fresh with the project, see the next section where you’ll download the project to use as a starting point for this course.

## Download the Starter Project

This tutorial series is a small part of an ongoing series where you’ll build out a game focusing on different aspects of game development, from coding to design to art and beyond. This part of the series picks up where [Designing a Puzzle Adventure Game](https://dev.epicgames.com/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine) left off.

The Adventure Design project contains the following parts that will be useful for this course as you’ll edit and add to them to bring artistic design together with gameplay design in this course:

* A functional game loop with collection puzzles, player hazards, and non-playable characters (NPCs).
* A player character with a built-in HUD that can take damage from level hazards.
* A blocked out level with multiple rooms, points of interest, and hazards.

You can continue using your project from the previous course, or you can follow the steps below to start with a clean project. If you're made changes to your project to your project different from the original course direction, you may want to start with a clean project below in order to follow along.

Download the following files required to follow along with different parts of this course:

[Adventure Designer Example Project](https://d1iv7db44yhgxn.cloudfront.net/documentation/attachments/76a4e171-318c-4f25-a5ef-992f91ea55a7/adventuredesigner.zip)

(Download size: 73.4 MB)

* This zip file contains the game project from the end of the Design a Puzzle Adventure Game course.

[Artist Track Content Pack](https://d1iv7db44yhgxn.cloudfront.net/documentation/attachments/16c03e7b-0350-4c19-8681-93275bef7fc7/artist-track-content-pack.zip)

(Download size: 1.07 MB) (Last Updated: 11/17/2025)

* This contains the source sound files you’ll use to complete tasks later in this course.

Once downloaded, you can extract their files to a folder location of your choosing.

## Opening the Starter Project

After downloading and extracting the project files, follow these steps:

1. Open the **Epic Games Launcher** and start the Engine.

   The [Designing a Puzzle Adventure Game](https://dev.epicgames.com/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine) was built using Unreal Engine 5.6. You can choose to use 5.6 or a later version of the engine with these project files. You’ll be prompted with the **Convert Project** dialog box. Use the **Open a copy** option to create a copy of the project.

   [![](https://dev.epicgames.com/community/api/documentation/image/c8ba6a8e-565e-4b4e-bc61-c47d1fdb5461?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c8ba6a8e-565e-4b4e-bc61-c47d1fdb5461?resizing_type=fit)
2. In the **Project Browser**, select **Open a Project** and navigate to the location of the root folder where you extracted the project.
3. Select `AdventureDesigner.uproject` and open it.

   [![](https://dev.epicgames.com/community/api/documentation/image/e349316f-e5f0-47a8-8959-4df34894425e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e349316f-e5f0-47a8-8959-4df34894425e?resizing_type=fit)

Once the project loads, you should see something that looks like this:

[![](https://dev.epicgames.com/community/api/documentation/image/ff5ab1ef-d871-415b-9abe-bbffc25de472?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ff5ab1ef-d871-415b-9abe-bbffc25de472?resizing_type=fit)

## Importing the Content Pack Files into Your Project

The **Content Pack zip** file includes source files for sounds you’ll use throughout this course to build specific materials for surfaces and sounds used for character interactions and visual effects.

These files should be imported into your project and placed in folders, so that when the time comes, you can locate them to follow along with the relevant parts of this guide.

Let’s walk through importing these and the options you’re provided when doing so.

### Import the Sound Source Files

To import the sound files, follow these steps:

1. In Unreal Engine, in the **Content Browser** navigate to the **AdventureGame** folder.
2. Inside **AdventureGame**, right-click and select **New Folder**. Name this folder `Artist`.
3. In the **Artist** folder, create another new folder named `Audio`.

   [![](https://dev.epicgames.com/community/api/documentation/image/f100e6ad-efd6-4de4-bbc5-4bc057159b95?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f100e6ad-efd6-4de4-bbc5-4bc057159b95?resizing_type=fit)
4. On your computer, navigate to the folder where you extracted the **Artists Track Content Pack** files you downloaded earlier.
5. Drag and drop the **Audio Sources** folder into the **Artist** folder. This creates three folders named `Default Footsteps`, `Fire Trap`, and `Metal Footsteps` that contain the WAV sound files.

## Project Organization

As you start to add actors and elements to your project and levels, it’s important to keep your project organized so that you can quickly locate where things are.

Let’s look at some ways you can continue this good practice as you continue to develop your project while following this course.

### Content Browser

[![](https://dev.epicgames.com/community/api/documentation/image/6d3a6f7c-3663-4088-ac1f-611456eb13cf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6d3a6f7c-3663-4088-ac1f-611456eb13cf?resizing_type=fit)

Anytime you’re creating assets in the engine or importing them into the **Content Browser**, you should strive to keep them well-organized so that you can locate them easily while working. This also helps anyone you’re working with find the assets they need, whether it’s a large or small project.

We recommend following these guidelines mentioned in our [Recommended Asset Naming Conventions](https://dev.epicgames.com/documentation/en-us/unreal-engine/recommended-asset-naming-conventions-in-unreal-engine-projects) when thinking about how you organize and name content for your projects.

Throughout this series, you’ll be asked to create folders and new assets that you’ll use. We’ll use these naming conventions and organizational methods.

### Level Outliner

[![](https://dev.epicgames.com/community/api/documentation/image/6e5d429d-6080-487c-b160-51d60424314e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6e5d429d-6080-487c-b160-51d60424314e?resizing_type=fit)

Just as the Content Browser contains assets of the project, the **Outliner** contains actors and objects found in a level. It can also include ways to organize them so that they are easily accessible and identifiable with their function or placement. You can create custom named folders and groupings of selected actors to organize them.

Throughout this series, you may notice that the outliner already uses folder groupings that match the design of the level, naming some sections after their room name, or having folders that contain all the blocking volumes of the level. As you add new actors to the scene, you’ll want to add these to the folders in the outliner they correspond to or make your own new named folders to organize assets.

## Additional Art Resources

Throughout a lot of this course, you’ll learn about different aspects of developing your own materials, material instances, lighting and its features. A lot of what you learn in these tutorials will be practical knowledge of how to create and use these features at a basic level. What you’ll also learn is that a lot of the artistic approach to developing a project is very subjective to your game’s needs and what you’d like the look and feel of it to be.

With this in mind, you’ll create something in this course you can use but also know that there are resources available that you can download other assets from to help with the development of your project. These can range from textures, sounds, and materials to entire projects-worth of content for you to explore and integrate into your own.

With each of these resources, there is free and paid content you can explore. To learn how you can migrate content from one project to another, see [Migrating Assets](https://dev.epicgames.com/documentation/en-us/unreal-engine/migrating-assets-in-unreal-engine).



* [![Samples and Tutorials](https://dev.epicgames.com/community/api/documentation/image/f1954fd2-f9a4-4083-bc27-c000b758efb3?resizing_type=fit&width=640&height=640)

  Samples and Tutorials

  Links to various example scenes, sample games, and tutorials.](https://dev.epicgames.com/documentation/en-us/unreal-engine/samples-and-tutorials-for-unreal-engine)

* [![Engine Feature Examples](https://dev.epicgames.com/community/api/documentation/image/38259691-6f58-4ba7-9a2b-bcd0893c0ee2?resizing_type=fit&width=640&height=640)

  Engine Feature Examples

  Full scenes demonstrating particular features or approaches to specific challenges.](https://dev.epicgames.com/documentation/en-us/unreal-engine/engine-feature-examples-for-unreal-engine)

* [![Content Examples](https://dev.epicgames.com/community/api/documentation/image/e308acee-3ece-4571-9feb-4febb6ce7a2c?resizing_type=fit&width=640&height=640)

  Content Examples

  Sample project that demonstrates specific concepts and techniques to use in Unreal Engine.](https://dev.epicgames.com/documentation/en-us/unreal-engine/content-examples-sample-project-for-unreal-engine)

* [![Free Epic Games Content](https://dev.epicgames.com/community/api/documentation/image/5796eb80-337f-45ef-97df-35e4b1778ffa?resizing_type=fit&width=640&height=640)

  Free Epic Games Content

  Companion documentation for free content distributed by Epic in Fab.](https://dev.epicgames.com/documentation/en-us/unreal-engine/free-epic-games-content-for-unreal-engine)

## Next Up

Now that you have a project set up to work from and content you’ll need imported, it’s time to start taking some artistic liberties with where the Designer course left off.

In the next section, you’ll get an introduction to different types of lights and how you can use those with some environment lighting features, like volumetric fog, to create an interesting atmosphere within the scene and how to use these to drive players towards gameplay goals to complete tasks.

If you are comfortable with where you are in setting up the project, you can proceed to the Light a Scene tutorial:

* [![Light a Scene](https://dev.epicgames.com/community/api/documentation/image/554f65ca-c199-4103-9380-850b74958081?resizing_type=fit&width=640&height=640)

  Light a Scene

  Learn to light your level and set the mood with Spot Lights, Point Lights, and Rect Lights.](https://dev.epicgames.com/documentation/en-us/unreal-engine/artist-02-light-a-scene)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Before You Begin](/documentation/en-us/unreal-engine/artist-01-project-setup-and-content-import?application_version=5.7#beforeyoubegin)
* [Download the Starter Project](/documentation/en-us/unreal-engine/artist-01-project-setup-and-content-import?application_version=5.7#downloadthestarterproject)
* [Opening the Starter Project](/documentation/en-us/unreal-engine/artist-01-project-setup-and-content-import?application_version=5.7#openingthestarterproject)
* [Importing the Content Pack Files into Your Project](/documentation/en-us/unreal-engine/artist-01-project-setup-and-content-import?application_version=5.7#importingthecontentpackfilesintoyourproject)
* [Import the Sound Source Files](/documentation/en-us/unreal-engine/artist-01-project-setup-and-content-import?application_version=5.7#importthesoundsourcefiles)
* [Project Organization](/documentation/en-us/unreal-engine/artist-01-project-setup-and-content-import?application_version=5.7#projectorganization)
* [Content Browser](/documentation/en-us/unreal-engine/artist-01-project-setup-and-content-import?application_version=5.7#contentbrowser)
* [Level Outliner](/documentation/en-us/unreal-engine/artist-01-project-setup-and-content-import?application_version=5.7#leveloutliner)
* [Additional Art Resources](/documentation/en-us/unreal-engine/artist-01-project-setup-and-content-import?application_version=5.7#additionalartresources)
* [Next Up](/documentation/en-us/unreal-engine/artist-01-project-setup-and-content-import?application_version=5.7#nextup)

Related documents

[Code a First-Person Adventure Game

![Code a First-Person Adventure Game](https://dev.epicgames.com/community/api/documentation/image/ffc1a8f8-e7e5-42c0-b4ed-32ce6d3adbbc?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/code-a-firstperson-adventure-game-in-unreal-engine)

[Design a Puzzle Adventure

![Design a Puzzle Adventure](https://dev.epicgames.com/community/api/documentation/image/a7b7ff2c-23d0-47a0-8a04-e569209942b0?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/design-a-puzzle-adventure-game-in-unreal-engine)
