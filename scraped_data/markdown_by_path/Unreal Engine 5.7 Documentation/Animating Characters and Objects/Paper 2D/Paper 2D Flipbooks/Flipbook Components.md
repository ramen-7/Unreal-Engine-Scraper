<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/flipbook-components-in-unreal-engine?application_version=5.7 -->

# Flipbook Components

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
6. [Paper 2D](/documentation/en-us/unreal-engine/paper-2d-overview-in-unreal-engine "Paper 2D")
7. [Paper 2D Flipbooks](/documentation/en-us/unreal-engine/paper-2d-flipbooks-in-unreal-engine "Paper 2D Flipbooks")
8. Flipbook Components

# Flipbook Components

Information on working with Flipbook Components in Blueprints or C++.

![Flipbook Components](https://dev.epicgames.com/community/api/documentation/image/199fbb6b-2cd1-4417-8095-6cff78bf6372?resizing_type=fill&width=1920&height=335)

 On this page

**Flipbook Components** are regular primitive components, and can be posed arbitrarily in 3D, attached to other components, or have other components attached to them. Each Flipbook Component instance can specify a custom color that will be passed down to the Flipbook Material as a Vertex Color. They can also have a custom Material specified that will override the default Material defined in the Flipbook.

You can change the current Flipbook asset by calling **SetFlipbook**, but note that this will only work if the **Mobility** property is set to **Moveable** (or if it is called during the construction of the Actor). You can also control play rate, play direction, looping, etc. with various other methods on the component.

While C++ documentation for working with Flipbook Components is still in development, you can refer to [UPaperFlipbookComponent](/documentation/404) for more information on using them in your code until more detailed documentation comes online.

## Setup

To learn more about Flipbook Components using Blueprints, follow the link below:

* [Paper 2D Flipbooks](/documentation/en-us/unreal-engine/paper-2d-flipbooks-in-unreal-engine)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Setup](/documentation/en-us/unreal-engine/flipbook-components-in-unreal-engine?application_version=5.7#setup)
