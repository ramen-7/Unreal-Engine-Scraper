<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/network-debugging-for-unreal-engine?application_version=5.7 -->

# Testing, Debugging, and Optimization

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
6. [Networking and Multiplayer](/documentation/en-us/unreal-engine/networking-and-multiplayer-in-unreal-engine "Networking and Multiplayer")
7. Testing, Debugging, and Optimization

# Testing, Debugging, and Optimization

An Overview for Network Debugging in Unreal.

![Testing, Debugging, and Optimization](https://dev.epicgames.com/community/api/documentation/image/42605043-3478-4524-be10-4239326f33d7?resizing_type=fill&width=1920&height=335)

 On this page

When creating a multiplayer game or networked project in **Unreal Engine (UE)**, there are several unique challenges in the process of debugging, profiling, and testing your project. These challenges include:

* Debugging multiple instances of your project
* Accounting for the general unreliability and instability that comes with networked communication
* Examining the different functionality that exists on **Clients** as opposed to **Servers**.

UE multiplayer is based around the Client-Server model. This means that there will be a single server that will be Authoritative over the [GameState](/documentation/en-us/unreal-engine/game-mode-and-game-state-in-unreal-engine), while connected clients will maintain a close approximation. See [Client-Server Model](/documentation/en-us/unreal-engine/setting-up-dedicated-servers-in-unreal-engine) for additional documentation.

Unreal Engine features specialized tools and workflows for debugging networked applications. The guides below will show you how to use these tools, as well as tips and best practices for troubleshooting common networking issues.

## Index

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

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Index](/documentation/en-us/unreal-engine/network-debugging-for-unreal-engine?application_version=5.7#index)
