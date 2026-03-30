<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/online-services-in-unreal-engine?application_version=5.7 -->

# Online Services

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
6. [Online Subsystems and Services](/documentation/en-us/unreal-engine/online-subsystems-and-services-in-unreal-engine "Online Subsystems and Services")
7. Online Services

# Online Services

Use Unreal Engine's Online Services to extend your project's online experience.

![Online Services](https://dev.epicgames.com/community/api/documentation/image/c02c5e5a-f3f8-4a4b-83ba-daeedb2a6516?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

The **Online Services** plugin and its interfaces provide a common way to access the functionality of various online services. The design of the Online Services plugin ensures that the only changes developers need to make when working on a game that ships on multiple platforms, or supports multiple online services, are configuration adjustments for each supported service.

## Overview



* [![Online Services Overview](https://dev.epicgames.com/community/api/documentation/image/f1dae502-06de-471d-9a45-0afc04eb42a5?resizing_type=fit&width=640&height=640)

  Online Services Overview

  Learn about the Online Services Interfaces and how to configure them for use in Unreal Engine.](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-online-services-in-unreal-engine)

## Interfaces

* [![Online Services Achievements Interface](https://dev.epicgames.com/community/api/documentation/image/a1512a73-a1cd-4883-981a-47321e83b340?resizing_type=fit&width=640&height=640)

  Online Services Achievements Interface

  Read and update player achievements.](https://dev.epicgames.com/documentation/en-us/unreal-engine/achievements-interface-in-unreal-engine)
* [![Auth Interface](https://dev.epicgames.com/community/api/documentation/image/03189535-7955-483c-bdcf-2842120f2d89?resizing_type=fit&width=640&height=640)

  Auth Interface

  Authenticate and verify a local user with online services.](https://dev.epicgames.com/documentation/en-us/unreal-engine/auth-interface-in-unreal-engine)
* [![Commerce Interface](https://dev.epicgames.com/community/api/documentation/image/b9df3117-f83a-48e3-928f-5de072a98cac?resizing_type=fit&width=640&height=640)

  Commerce Interface

  Purchase and redeem game content outside of gameplay.](https://dev.epicgames.com/documentation/en-us/unreal-engine/commerce-interface-in-unreal-engine)
* [![Connectivity Interface](https://dev.epicgames.com/community/api/documentation/image/65b76225-f818-4753-91e4-a95c38a8a58e?resizing_type=fit&width=640&height=640)

  Connectivity Interface

  Determine whether your game is connected to your platform's online services.](https://dev.epicgames.com/documentation/en-us/unreal-engine/connectivity-interface-in-unreal-engine)
* [![Online Services External UI Interface](https://dev.epicgames.com/community/api/documentation/image/da2177ba-e63d-4aa0-8fc8-2ccee1802c1a?resizing_type=fit&width=640&height=640)

  Online Services External UI Interface

  Display your platform's online services external user interface.](https://dev.epicgames.com/documentation/en-us/unreal-engine/external-ui-interface-in-unreal-engine)
* [![Leaderboards Interface](https://dev.epicgames.com/community/api/documentation/image/04a84b3d-454b-4dfa-ab1b-aa5523b86ba5?resizing_type=fit&width=640&height=640)

  Leaderboards Interface

  Display and update leaderboards from within your game.](https://dev.epicgames.com/documentation/en-us/unreal-engine/leaderboards-interface-in-unreal-engine)
* [![Lobbies Interface](https://dev.epicgames.com/community/api/documentation/image/69f72916-1131-4335-a34b-56088168cdaf?resizing_type=fit&width=640&height=640)

  Lobbies Interface

  Create and manage online lobbies.](https://dev.epicgames.com/documentation/en-us/unreal-engine/lobbies-interface-in-unreal-engine)
* [![Online Services Presence Interface](https://dev.epicgames.com/community/api/documentation/image/3fe28257-f92c-4368-a5f7-c1e276724ec1?resizing_type=fit&width=640&height=640)

  Online Services Presence Interface

  Access the presence and joinability status of friends and followers.](https://dev.epicgames.com/documentation/en-us/unreal-engine/presence-interface-in-unreal-engine)
* [![Privileges Interface](https://dev.epicgames.com/community/api/documentation/image/cb1320af-347e-4cb1-8df7-1d1970c80217?resizing_type=fit&width=640&height=640)

  Privileges Interface

  Access player privileges including online and crossplay as well as voice and text chat.](https://dev.epicgames.com/documentation/en-us/unreal-engine/privileges-interface-in-unreal-engine)
* [![Sessions Interface](https://dev.epicgames.com/community/api/documentation/image/6e281343-478c-4b2f-b0a9-123aef73fe5e?resizing_type=fit&width=640&height=640)

  Sessions Interface

  Create and manage online game sessions.](https://dev.epicgames.com/documentation/en-us/unreal-engine/sessions-interface-in-unreal-engine)
* [![Social Interface](https://dev.epicgames.com/community/api/documentation/image/e27ec3a3-4407-4ebc-a8ce-341ac29ccd5a?resizing_type=fit&width=640&height=640)

  Social Interface

  Manage relationships with friends and blocked users.](https://dev.epicgames.com/documentation/en-us/unreal-engine/social-interface-in-unreal-engine)
* [![Stats Interface](https://dev.epicgames.com/community/api/documentation/image/4cc92b93-4660-401d-920d-d2d6b958199e?resizing_type=fit&width=640&height=640)

  Stats Interface

  Upload stats and data to online services and complete stats queries.](https://dev.epicgames.com/documentation/en-us/unreal-engine/stats-interface-in-unreal-engine)
* [![Title File Interface](https://dev.epicgames.com/community/api/documentation/image/e0ad35d0-920f-42a9-91c1-e7999c9727f0?resizing_type=fit&width=640&height=640)

  Title File Interface

  Read title files from the backend online services.](https://dev.epicgames.com/documentation/en-us/unreal-engine/title-file-interface-in-unreal-engine)
* [![User File Interface](https://dev.epicgames.com/community/api/documentation/image/a05687c9-562f-4f2f-a8b3-5d76c9f9d91c?resizing_type=fit&width=640&height=640)

  User File Interface

  Read user files from the backend online services.](https://dev.epicgames.com/documentation/en-us/unreal-engine/user-file-interface-in-unreal-engine)
* [![User Info Interface](https://dev.epicgames.com/community/api/documentation/image/db44cc9e-d03b-4dba-9356-3a2865dec794?resizing_type=fit&width=640&height=640)

  User Info Interface

  Access a player's display name and avatar for use in your game.](https://dev.epicgames.com/documentation/en-us/unreal-engine/user-info-interface-in-unreal-engine)

## Get Started

* [![Setup and Configure the Online Services Plugins](https://dev.epicgames.com/community/api/documentation/image/47d357bc-1731-42a6-af3b-99b1a4cc2c2d?resizing_type=fit&width=640&height=640)

  Setup and Configure the Online Services Plugins

  Setup and configure the Online Services plugins for use in your project.](https://dev.epicgames.com/documentation/en-us/unreal-engine/setup-and-configure-the-online-services-plugins-in-unreal-engine)
* [![Structure and Implement the Online Services Plugins](https://dev.epicgames.com/community/api/documentation/image/36eef5f5-66de-4d2a-a947-6799dfd5c6b3?resizing_type=fit&width=640&height=640)

  Structure and Implement the Online Services Plugins

  Guide to organizing and implementing your Online Services plugin code.](https://dev.epicgames.com/documentation/en-us/unreal-engine/structure-and-implement-the-online-services-plugins-in-unreal-engine)

## Online Services EOS

* [![Enable and Configure Online Services EOS](https://dev.epicgames.com/community/api/documentation/image/1e4d21ac-d005-439e-a9b6-9a7faefd4e16?resizing_type=fit&width=640&height=640)

  Enable and Configure Online Services EOS

  Access EOS Game Services and Epic Account services in your project through the Online Services EOSGS and EOS plugins.](https://dev.epicgames.com/documentation/en-us/unreal-engine/enable-and-configure-online-services-eos-in-unreal-engine)

## Debugging

* [![Online Services Console Commands](https://dev.epicgames.com/community/api/documentation/image/6d8f474c-5ac3-413a-ac5c-6ab083435787?resizing_type=fit&width=640&height=640)

  Online Services Console Commands

  Use console commands to debug and test the Online Services plugin during gameplay.](https://dev.epicgames.com/documentation/en-us/unreal-engine/online-services-console-commands-in-unreal-engine)

* [beta](https://dev.epicgames.com/community/search?query=beta)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Overview](/documentation/en-us/unreal-engine/online-services-in-unreal-engine?application_version=5.7#overview)
* [Interfaces](/documentation/en-us/unreal-engine/online-services-in-unreal-engine?application_version=5.7#interfaces)
* [Get Started](/documentation/en-us/unreal-engine/online-services-in-unreal-engine?application_version=5.7#get-started)
* [Online Services EOS](/documentation/en-us/unreal-engine/online-services-in-unreal-engine?application_version=5.7#online-services-eos)
* [Debugging](/documentation/en-us/unreal-engine/online-services-in-unreal-engine?application_version=5.7#debugging)
