<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/module-3-create-a-coin-pickup-with-modeling-tools-and-blueprints?application_version=5.7 -->

# Module 3: Create a Coin Pickup with Blueprints

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
6. [Your First Hour in Unreal Engine](/documentation/en-us/unreal-engine/first-hour-in-unreal-engine "Your First Hour in Unreal Engine")
7. Module 3: Create a Coin Pickup with Blueprints

# Module 3: Create a Coin Pickup with Blueprints

Create a coin pickup for the player to collect using the in-editor modeling tools, material editor, and blueprints.

###### Prerequisite topics

In order to understand and use the content on this page, make sure you are familiar with the following topics:

* [Module 2: Create a Flashlight with Enhanced Input](/documentation/en-us/unreal-engine/module-2-create-a-flashlight-with-enhanced-input)

 On this page

Create a coin pickup for the player to collect using the in-editor modeling tools, material editor, and blueprints.

Module 3 Overview

In this third module, we begin to create a coin pickup that players are able to collect throughout the level. You will learn to create the visual elements for the pickup using the in-engine Transform tools and Material Editor. You will also add an on screen coin counter to keep track of the number of coins collected and a game end state for when all the coins have been collected.

[![Building The Coin Pickup](https://dev.epicgames.com/community/api/documentation/image/2edc7c1c-893f-41db-b7b4-ab9dac464627?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2edc7c1c-893f-41db-b7b4-ab9dac464627?resizing_type=fit)

Building the coin pickup

### Creating a Coin

Creating the visuals for the coin pickup

### Adding a Coin Material

Creating a gold material and adding it to the coin mesh

### Building a Coin Counter

Setting up the coin counter in the player blueprint

### Creating a Coin Counter

Creating the coin counter functionality

### Creating the End State Screen

Creating the End State

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Creating a Coin](/documentation/en-us/unreal-engine/module-3-create-a-coin-pickup-with-modeling-tools-and-blueprints?application_version=5.7#creatingacoin)
* [Adding a Coin Material](/documentation/en-us/unreal-engine/module-3-create-a-coin-pickup-with-modeling-tools-and-blueprints?application_version=5.7#addingacoinmaterial)
* [Building a Coin Counter](/documentation/en-us/unreal-engine/module-3-create-a-coin-pickup-with-modeling-tools-and-blueprints?application_version=5.7#buildingacoincounter)
* [Creating a Coin Counter](/documentation/en-us/unreal-engine/module-3-create-a-coin-pickup-with-modeling-tools-and-blueprints?application_version=5.7#creatingacoincounter)
* [Creating the End State Screen](/documentation/en-us/unreal-engine/module-3-create-a-coin-pickup-with-modeling-tools-and-blueprints?application_version=5.7#creatingtheendstatescreen)

Related documents

[Blueprint Visual Scripting

![Blueprint Visual Scripting](https://dev.epicgames.com/community/api/documentation/image/2b4d887d-89a1-48b1-9510-70eb6ef48527?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/blueprint-visual-scripting)

[Material Editor Guide

![Material Editor Guide](https://dev.epicgames.com/community/api/documentation/image/f244afee-e66a-41fd-bacf-cd3fd44d3d9e?resizing_type=fit&width=160&height=92)](/documentation/en-us/unreal-engine/unreal-engine-material-editor-user-guide)
