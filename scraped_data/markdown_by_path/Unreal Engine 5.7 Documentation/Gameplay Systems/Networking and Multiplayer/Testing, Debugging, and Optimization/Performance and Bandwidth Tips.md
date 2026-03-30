<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/performance-and-bandwidth-tips-for-unreal-engine?application_version=5.7 -->

# Performance and Bandwidth Tips

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
7. [Testing, Debugging, and Optimization](/documentation/en-us/unreal-engine/network-debugging-for-unreal-engine "Testing, Debugging, and Optimization")
8. Performance and Bandwidth Tips

# Performance and Bandwidth Tips

Some tips for optimizing the performance and bandwidth usage of Actor replication.

![Performance and Bandwidth Tips](https://dev.epicgames.com/community/api/documentation/image/cc5e8342-be37-4e74-a5dc-0ff218fc465e?resizing_type=fill&width=1920&height=335)

**Replicating Actors** can take time. **Unreal Engine (UE)** does its best to make this as efficient as possible, but there are a few things you can do to make this job easier.

When gathering actors for replication, the server will check a few things like relevancy, update frequency, dormancy, etc. You can tweak any of these checks to affect performance. When thinking about making this process as efficient as possible, it is best to prioritize in this order:

* Turning off replication (`AActor::SetReplicates(false)`)
  + When an actor is not replicating, it is not on the list in the first place, so this is the biggest win, to make sure actors that do not need to replicate are marked as such.
* Lower `NetUpdateFrequency` value
  + The less an actor updates, the less time it takes to update. It is best to make this number as low as possible. This number represents how often per second this actor will replicate to clients.
* Dormancy
* Relevancy
* `NetClientTicksPerSecond`

Do not mark properties to replicate if they are not absolutely necessary. It is best to try and derive state from existing replicated properties when possible.

Try to take advantage of the quantization functionality that already exists. e.g. `FVector_NetQuantize`. These will greatly reduce the size needed to replicate this state over to clients, and if used properly, should not cause any noticeable artifacts.

`FName` variables are not generally compressed, so when you are using them as parameters to RPCs, keep in mind that they will generally send the string each call. This can be a lot of overhead.

* [gameplay](https://dev.epicgames.com/community/search?query=gameplay)
* [performance](https://dev.epicgames.com/community/search?query=performance)
* [performance and profiling](https://dev.epicgames.com/community/search?query=performance%20and%20profiling)
* [blueprint](https://dev.epicgames.com/community/search?query=blueprint)
* [multiplayer](https://dev.epicgames.com/community/search?query=multiplayer)
* [network](https://dev.epicgames.com/community/search?query=network)
* [fundamentals](https://dev.epicgames.com/community/search?query=fundamentals)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)
