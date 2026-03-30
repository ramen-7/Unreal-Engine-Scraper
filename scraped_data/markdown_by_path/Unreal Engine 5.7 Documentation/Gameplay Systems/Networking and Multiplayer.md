<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/networking-and-multiplayer-in-unreal-engine?application_version=5.7 -->

# Networking and Multiplayer

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
6. Networking and Multiplayer

# Networking and Multiplayer

Setting up networked games for multiplayer.

![Networking and Multiplayer](https://dev.epicgames.com/community/api/documentation/image/59ed1b0e-5849-45d3-ae26-2893b939dc2c?resizing_type=fill&width=1920&height=335)

 On this page

Modern multiplayer experiences require synchronizing vast amounts of data between large numbers of clients spread around the world. What data you send and how you send it is extremely important to providing a compelling experience to users since it can drastically affect how your project performs and feels. In **Unreal Engine (UE)**, **Replication** is the name for the process of synchronizing data and procedure calls between clients and servers. The Replication system provides a higher-level abstraction along with low-level customization to make it easier to deal with all the various situations you might encounter when creating a project designed for multiple simultaneous users.

## Basics

[![Networking Overview](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9bf04a37-5ece-44a4-9ed1-35f44298d4b4/placeholder_topic.png)

Networking Overview

Learn about networking in Unreal Engine including fundamental concepts and the available replication systems.](/documentation/en-us/unreal-engine/networking-overview-for-unreal-engine)
[![Multiplayer Programming Quick Start](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3f4df5bd-1ced-48a8-8022-7877eef149bd/preview.png)

Multiplayer Programming Quick Start

Create a simple multiplayer game in C++.](/documentation/en-us/unreal-engine/multiplayer-programming-quick-start-for-unreal-engine)

## Managing Sessions

[![Travelling in Multiplayer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4a2f19fd-ee1c-4a12-b819-348c72dff656/placeholder_topic.png)

Travelling in Multiplayer

An overview of how travelling works in multiplayer.](/documentation/en-us/unreal-engine/travelling-in-multiplayer-in-unreal-engine)

## Network Multiplayer Programming

[![Actor Network Dormancy](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bf1b9a30-a217-4a13-beb5-102cf1ff8ca3/placeholder_topic.png)

Actor Network Dormancy

Optimize your multiplayer game by effectively using dormancy.](/documentation/en-us/unreal-engine/actor-network-dormancy-in-unreal-engine)
[![Replicate Actor Properties](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ffc4e9fe-25ca-45a1-9572-5234710ac2c0/placeholder_topic.png)

Replicate Actor Properties

Property replication, conditional replication, custom conditions, and object references.](/documentation/en-us/unreal-engine/replicate-actor-properties-in-unreal-engine)
[![Actor Component Replication](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a25d35e6-6a7e-42c4-985b-ca1a7a232205/placeholder_topic.png)

Actor Component Replication

Learn how to replicate actor-owned components.](/documentation/en-us/unreal-engine/replicating-actor-components-in-unreal-engine)
[![Object Replication](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/89fd5c0f-64b1-4d26-a324-7f59cb82b770/placeholder_topic.png)

Object Replication

Learn how to replicate UObjects.](/documentation/en-us/unreal-engine/replicating-uobjects-in-unreal-engine)
[![Online Beacons](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e90aff48-8d76-4455-920b-84daaf9c403e/placeholder_topic.png)

Online Beacons

Mechanism for lightweight interactions between servers and clients.](/documentation/en-us/unreal-engine/using-online-beacons-in-unreal-engine)

## Iris Replication System

[![Introduction to Iris](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9ea5c765-e3f7-4b8d-9261-3b1e6b7a2d4b/placeholder_topic.png)

Introduction to Iris

Learn about the design and components of Iris as well as how to configure your project to use Iris.](/documentation/en-us/unreal-engine/introduction-to-iris-in-unreal-engine)
[![Migrate to Iris](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d0938636-2e40-4fdd-90c6-652e781f1ec1/placeholder_topic.png)

Migrate to Iris

Learn what has changed between the existing replication systems and Iris.](/documentation/en-us/unreal-engine/migrate-to-iris-in-unreal-engine)
[![Components of Iris](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/925aaeb3-a56c-4b24-b463-b38f1eda4dff/placeholder_topic.png)

Components of Iris

Learn more about the primary components of the Iris replication system and how to use them.](/documentation/en-us/unreal-engine/components-of-iris-in-unreal-engine)
[![Glossary of Iris Terms](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/be877f30-33a9-4db6-9748-38eabf0bbfdf/placeholder_topic.png)

Glossary of Iris Terms

Glossary page for Iris terminology.](/documentation/en-us/unreal-engine/glossary-of-iris-terms-in-unreal-engine)

## Replication Graph

[![Replication Graph](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a583b882-92b3-46aa-9d12-d2f0afe6c02a/placeholder_topic.png)

Replication Graph

Overview of the Replication Graph feature and Replication Graph Nodes.](/documentation/en-us/unreal-engine/replication-graph-in-unreal-engine)

## Replay System

[![Replay System](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/79e4d114-61b1-4668-8cc2-63899d8650fd/placeholder_topic.png)

Replay System

Overview of the Replay system for recording and playback of gameplay](/documentation/en-us/unreal-engine/using-the-replay-system-in-unreal-engine)

## Deploying Multiplayer Games

[![Using Steam Sockets](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4da07abd-2faa-478b-bfc8-e0b515c98423/placeholder_topic.png)

Using Steam Sockets

How to enable the Steam network protocol layer for Unreal Engine projects.](/documentation/en-us/unreal-engine/using-steam-sockets-in-unreal-engine)

## Debugging and Optimization

[![Logging](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a2fce70e-3d91-4442-96a1-8d473106fd2b/placeholder_topic.png)

Logging

An overview of Logging for Network Games.](/documentation/en-us/unreal-engine/logging-for-networked-games-in-unreal-engine)
[![Console Commands](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/12619811-a7e5-4891-9e72-c2b7e9439b7b/placeholder_topic.png)

Console Commands

Specify networking settings and obtain valuable debug information at runtime.](/documentation/en-us/unreal-engine/console-commands-for-network-debugging-in-unreal-engine)
[![Testing Multiplayer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/c0f8759e-c798-44d7-b99e-91ed4ea3b2b1/placeholder_topic.png)

Testing Multiplayer

Set up the Unreal Editor for testing multiplayer games.](/documentation/en-us/unreal-engine/testing-multiplayer-in-unreal-engine)
[![Debugging Guide](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/d537188e-e0e1-4cea-948e-e759108f3440/placeholder_topic.png)

Debugging Guide

Testing and Debugging Networked Games in Unreal.](/documentation/en-us/unreal-engine/testing-and-debugging-networked-games-in-unreal-engine)
[![Network Emulation](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a147083f-7627-4e95-8ab5-08d326b25a8d/placeholder_topic.png)

Network Emulation

Emulate network packet lag and loss in Unreal Engine.](/documentation/en-us/unreal-engine/using-network-emulation-in-unreal-engine)
[![Network Profiler](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/93885194-3163-42b8-96b8-bc2a39f38a37/placeholder_topic.png)

Network Profiler

Analyze network traffic and performance information captured at runtime.](/documentation/en-us/unreal-engine/using-the-network-profiler-in-unreal-engine)
[![Performance and Bandwidth Tips](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f396d939-d769-4747-b296-3edaa37270e7/placeholder_topic.png)

Performance and Bandwidth Tips

Some tips for optimizing the performance and bandwidth usage of Actor replication.](/documentation/en-us/unreal-engine/performance-and-bandwidth-tips-for-unreal-engine)

[![Oodle Network](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/baaf9e11-90a9-4713-9fa6-6384ac256fa3/oodle-topic.png)

Oodle Network

An overview of using Oodle Network to improve streaming performance for your project.](/documentation/en-us/unreal-engine/oodle-network)

## Tutorials and Examples

[![Setting Up Dedicated Servers](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/9cd54dfa-742e-4121-b19c-0fd25efccf6f/placeholder_topic.png)

Setting Up Dedicated Servers

Set up and run a dedicated server for your project.](/documentation/en-us/unreal-engine/setting-up-dedicated-servers-in-unreal-engine)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Basics](/documentation/en-us/unreal-engine/networking-and-multiplayer-in-unreal-engine?application_version=5.7#basics)
* [Managing Sessions](/documentation/en-us/unreal-engine/networking-and-multiplayer-in-unreal-engine?application_version=5.7#managingsessions)
* [Network Multiplayer Programming](/documentation/en-us/unreal-engine/networking-and-multiplayer-in-unreal-engine?application_version=5.7#networkmultiplayerprogramming)
* [Iris Replication System](/documentation/en-us/unreal-engine/networking-and-multiplayer-in-unreal-engine?application_version=5.7#irisreplicationsystem)
* [Replication Graph](/documentation/en-us/unreal-engine/networking-and-multiplayer-in-unreal-engine?application_version=5.7#replicationgraph)
* [Replay System](/documentation/en-us/unreal-engine/networking-and-multiplayer-in-unreal-engine?application_version=5.7#replaysystem)
* [Deploying Multiplayer Games](/documentation/en-us/unreal-engine/networking-and-multiplayer-in-unreal-engine?application_version=5.7#deployingmultiplayergames)
* [Debugging and Optimization](/documentation/en-us/unreal-engine/networking-and-multiplayer-in-unreal-engine?application_version=5.7#debuggingandoptimization)
* [Tutorials and Examples](/documentation/en-us/unreal-engine/networking-and-multiplayer-in-unreal-engine?application_version=5.7#tutorialsandexamples)
