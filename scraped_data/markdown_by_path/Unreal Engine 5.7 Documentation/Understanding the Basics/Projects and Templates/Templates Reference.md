<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-templates-reference?application_version=5.7 -->

# Templates Reference

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
5. [Understanding the Basics](/documentation/en-us/unreal-engine/understanding-the-basics-of-unreal-engine "Understanding the Basics")
6. [Projects and Templates](/documentation/en-us/unreal-engine/working-with-projects-and-templates-in-unreal-engine "Projects and Templates")
7. Templates Reference

# Templates Reference

Templates available with Unreal Engine and how to use them.

On this page

When you create a new Unreal Engine project, you have the option to use one of the existing templates as a base for your game or application. Unreal Engine templates contain character controllers, Blueprints, and other features that work without the need for additional configuration.

To learn how to create a new project from a template, see the [Creating New Project](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-a-new-project-in-unreal-engine) page.

When you select a template, you will see a description that tells you more about the template and what it contains. Scroll down to read the full description.

[![Example description of an Unreal Engine template](https://dev.epicgames.com/community/api/documentation/image/bd82350e-2034-4f6f-a40e-ea9f94d10428?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bd82350e-2034-4f6f-a40e-ea9f94d10428?resizing_type=fit)

Example of a template description for the Third Person template.

You can also create custom templates from any one of your existing projects. To learn more, see the [Creating Custom Templates](https://dev.epicgames.com/documentation/en-us/unreal-engine/converting-a-project-to-an-unreal-engine-template) page.

## Configuring Input for Playable Characters

Many templates include a character you can control using your keyboard, mouse, or controller. In Unreal Engine terms, this is called a Pawn.

You can learn more about how you can configure and use these in a template project by checking out [Configuring Input for Playable Characters in Templates](https://dev.epicgames.com/documentation/en-us/unreal-engine/configuring-input-for-your-template-pawns).

## Available Templates in Unreal Engine

The templates in Unreal Engine are split into the following categories:

* Games
* Film, Television, and Live Events
* Architecture, Engineering, and Construction
* Automotive, Product Design, and Manufacturing
* Simulation

Each of these categories also includes a **Blank** template, which consists of an empty project with no additional content and settings. This is the most basic template available.

### Games Templates

[![Unreal Engine's Game Templates with the First Person template in the background.](https://dev.epicgames.com/community/api/documentation/image/f5a37d65-3212-46f7-bfe6-0b00855408d1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f5a37d65-3212-46f7-bfe6-0b00855408d1?resizing_type=fit)

Unreal Engine's Game Templates.

Unreal Engine's **Games** templates offer quick starting points for various kinds of games, such as first and third-person, side-scroller, top-down, virtual reality, and driving.

Although these are tagged as "Game" templates, you can use them as a starting point for any kind of project. For example, you can use the VR Template to create a virtual reality walkthrough of a three-dimensional space. The Third Person template is generally a good starting point for many different kinds of projects, such as a platformer game or walking simulator.

| Template Name | Template Contents | Additional Documentation |
| --- | --- | --- |
| **First Person** | A character with a first-person camera perspective where you'll experience level contents from the character's viewport. This template includes various variants that includes a walking simulator, shooter arena with different weapon types, and a horror-like walking/platformer style game. | [First Person Template Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/first-person-template-in-unreal-engine?application_version=5.5) |
| **Third Person** | A character with a third-person camera perspective and basic scene geometry. The camera is located above and behind the character. | Third Person Template Overview |
| **Top Down** | A character you move by clicking or tapping to a new location. The camera is in a fixed position above the character and follows their movement. |  |
| **Handheld AR** | A starting point for creating AR applications you can deploy to Android or iOS. Includes runtime logic for scanning an environment to gather data for creating interactive planes in the virtual scene, and lighting and scene depth information. | * [Handheld AR Template Quickstart](https://dev.epicgames.com/documentation/en-us/unreal-engine/handheld-ar-template-quickstart-in-unreal-engine) * [Handheld AR Template Technical Reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/handheld-ar-template-technical-reference) |
| **Virtual Reality** | A starting point for all of your virtual reality (VR) projects in Unreal Engine 5. It includes encapsulated logic for teleport locomotion and common input actions, such as grabbing and attaching items to your hand. | * [VR template](https://dev.epicgames.com/documentation/en-us/unreal-engine/vr-template-in-unreal-engine) * [Developing for VR in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/developing-for-xr-experiences-in-unreal-engine) |
| **Vehicle** | A physics-driven vehicle with two different camera views — one inside the vehicle, the other above and behind it — as well as a HUD. |  |

### Film, Video, and Live Events Templates

[![Film, Video, and Live Event Templates.](https://dev.epicgames.com/community/api/documentation/image/67de66dc-7952-4735-a95f-f3227b42bd68?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/67de66dc-7952-4735-a95f-f3227b42bd68?resizing_type=fit)

Film, Video, and Live Event Templates.

The **Film, Video, and Live Events** templates provide a starting point for live production work.

| Template Name | Template Contents | Additional Documentation |
| --- | --- | --- |
| **Virtual Production** | Functionality for VR Scouting, Virtual Camera, SDI Video, Composure, and nDisplay. | * [Virtual Scouting Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/virtual-scouting-in-unreal-engine) * [Controlling Virtual Camera Actors](https://dev.epicgames.com/documentation/en-us/unreal-engine/controlling-a-virtual-camera-actor-using-live-link-in-unreal-engine?application_version=5.5) |
| **DMX** | Examples for addressing, patching, and controlling proxy lighting fixtures, as well as recording and playback of live DMX data streams in and outside Unreal Engine. | [DMX](https://dev.epicgames.com/documentation/en-us/unreal-engine/dmx-in-unreal-engine) |
| **InCamera VFX** | Blueprints, plugins, and example stages for in-camera VFX workflows. Use this as a starting point for Virtual Production shoots with LED volumes. | * [In-Camera VFX Template](https://dev.epicgames.com/documentation/en-us/unreal-engine/in-camera-vfx-template-in-unreal-engine) * [In-Camera VFX Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/in-camera-vfx-in-unreal-engine) |
| **nDisplay** | Display functionality using a cluster of PCs. Use as a starting point for rendering on complex arrangements of physical displays for live performances. | * [nDisplay Template](https://dev.epicgames.com/documentation/en-us/unreal-engine/ndisplay-template-in-unreal-engine) * [Rendering to Multiple Displays with nDisplay](https://dev.epicgames.com/documentation/en-us/unreal-engine/rendering-to-multiple-displays-with-ndisplay-in-unreal-engine) |

### Architecture, Engineering, and Construction Templates

[![Architecture Templates.](https://dev.epicgames.com/community/api/documentation/image/6c24134c-53b2-4c57-8149-8b9d453c1681?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6c24134c-53b2-4c57-8149-8b9d453c1681?resizing_type=fit)

Architecture Templates.

The **Architecture** templates (including engineering and construction) use [Datasmith](https://dev.epicgames.com/documentation/en-us/unreal-engine/datasmith-plugins-for-unreal-engine?application_version=5.5) to import content from various 3D programs into Unreal Engine, where you can further refine that content for desktop and XR applications.

| Template Name | Template Contents | Additional Documentation |
| --- | --- | --- |
| **Archvis** | Example architectural visualisation workflows with sample scenes for sun studies, interior renderings, and non-photorealistic stylized renderings. | * [Architectural Visualization for Design Strategies (video)](https://dev.epicgames.com/community/learning/talks-and-demos/bZdy/unreal-engine-architectural-visualization-for-design-strategies-on-a-120-year-old-building-unreal-fest-2024) * [Designing an Interior Space in Unreal Engine (video)](https://dev.epicgames.com/community/learning/tutorials/q39K/designing-a-interior-space-in-unreal-engine-5) * [The Epic Games Ecosystem for Arch Viz - Part 1 (tutorial)](https://dev.epicgames.com/community/learning/tutorials/nwML/unreal-engine-realityscan-the-epic-games-ecosystem-for-arch-viz-part-1) |
| **Design Configurator** | Uses Variant Manager, UMG, and Blueprint functionality to build a project where you can toggle between different object states such as visibility, initiate animation sequences, switch between views, and toggle between different design options. |  |
| **Collab Viewer** | Navigation and interaction for desktop and VR in collaborative sessions. This template contains some archviz-specific starter content and has several additional plugins enabled by default, including OpenXR and LiveLink. | [Collab Viewer Template](https://dev.epicgames.com/documentation/en-us/unreal-engine/collab-viewer-templates-in-unreal-engine) |
| **Handheld AR** | A starting point for creating AR applications you can deploy to Android or iOS. Includes runtime logic for scanning an environment to gather data for creating interactive planes in the virtual scene, and lighting and scene depth information. | * [Handheld AR Template Quickstart](https://dev.epicgames.com/documentation/en-us/unreal-engine/handheld-ar-template-quickstart-in-unreal-engine) * [Handheld AR Template Technical Reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/handheld-ar-template-technical-reference) |

### Automotive, Product Design, and Manufacturing Templates

[![Automotive, Product Design, and Manufacturing Templates.](https://dev.epicgames.com/community/api/documentation/image/f1245830-5950-4499-8779-63b4dd184466?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f1245830-5950-4499-8779-63b4dd184466?resizing_type=fit)

Automotive, Product Design, and Manufacturing Templates.

The **Automotive, Product Design, and Manufacturing** templates use Datasmith to import content from various 3D programs into Unreal Engine, where you can further refine that content for desktop and XR applications.

| Template Name | Template Contents | Additional Documentation |
| --- | --- | --- |
| **Photo Studio** | A premade photographic studio environment you can use for cinematics and product presentations. |  |
| **Product Configurator** | Uses Variant Manager, UMG, and Blueprint functionality to build a generic product configurator (that is, a program that lets you swap out different parts to test out new looks for a product, such as different colors for a car). | [Product Configurator](https://dev.epicgames.com/documentation/en-us/unreal-engine/product-configurator-template-in-unreal-engine) |
| **Collab Viewer** | Navigation and interaction for desktop and VR in collaborative sessions. This template also contains a sample model car that can be explored in VR. | [Collab Viewer Template](https://dev.epicgames.com/documentation/en-us/unreal-engine/collab-viewer-templates-in-unreal-engine) |
| **Handheld AR** | A starting point for creating AR applications you can deploy to Android or iOS. Includes runtime logic for scanning an environment to gather data for creating interactive planes in the virtual scene, and lighting and scene depth information. | * [Handheld AR Template Quickstart](https://dev.epicgames.com/documentation/en-us/unreal-engine/handheld-ar-template-quickstart-in-unreal-engine) * [Handheld AR Template Technical Reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/handheld-ar-template-technical-reference) |

### Simulation Templates

[![Simulation Templates.](https://dev.epicgames.com/community/api/documentation/image/a2d2cc0b-f5de-4e6e-86ea-801abe8c26f2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a2d2cc0b-f5de-4e6e-86ea-801abe8c26f2?resizing_type=fit)

Simulation Templates.

**Simulation** templates offer a broad range of starting points for various enterprise simulation applications. These templates contain the following functionality:

* Specific settings for outdoor environments.
* Realistic sky and lighting.
* Georeferencing tools.

| Template Name | Template Contents | Additional Documentation |
| --- | --- | --- |
| **Simulation Blank** | A template that consists of an empty project with the required settings and plugins enabled. This template is suitable as a starting point for most simulation applications and contains the following features:   * Earth atmosphere * Atmospheric lighting * Volumetric clouds * Geographical coordinates * [World Geodetic System (WGS84)](https://en.wikipedia.org/wiki/World_Geodetic_System) |  |
| **Handheld AR** | A starting point for creating AR applications you can deploy to Android or iOS. Includes runtime logic for scanning an environment to gather data for creating interactive planes in the virtual scene, and lighting and scene depth information. | * [Handheld AR Template Quickstart](https://dev.epicgames.com/documentation/en-us/unreal-engine/handheld-ar-template-quickstart-in-unreal-engine) * [Handheld AR Template Technical Reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/handheld-ar-template-technical-reference) |
| **Virtual Reality** | A starting point for all of your virtual reality (VR) projects in Unreal Engine 5. It includes encapsulated logic for teleport locomotion and common input actions, such as grabbing and attaching items to your hand. | * [VR template](https://dev.epicgames.com/documentation/en-us/unreal-engine/vr-template-in-unreal-engine) * [Developing for VR in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/developing-for-xr-experiences-in-unreal-engine) |

* [templates](https://dev.epicgames.com/community/search?query=templates)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Configuring Input for Playable Characters](/documentation/en-us/unreal-engine/unreal-engine-templates-reference?application_version=5.7#configuring-input-for-playable-characters)
* [Available Templates in Unreal Engine](/documentation/en-us/unreal-engine/unreal-engine-templates-reference?application_version=5.7#available-templates-in-unreal-engine)
* [Games Templates](/documentation/en-us/unreal-engine/unreal-engine-templates-reference?application_version=5.7#games-templates)
* [Film, Video, and Live Events Templates](/documentation/en-us/unreal-engine/unreal-engine-templates-reference?application_version=5.7#film-television-and-live-events-templates)
* [Architecture, Engineering, and Construction Templates](/documentation/en-us/unreal-engine/unreal-engine-templates-reference?application_version=5.7#architecture-engineering-and-construction-templates)
* [Automotive, Product Design, and Manufacturing Templates](/documentation/en-us/unreal-engine/unreal-engine-templates-reference?application_version=5.7#automotive-product-design-and-manufacturing-templates)
* [Simulation Templates](/documentation/en-us/unreal-engine/unreal-engine-templates-reference?application_version=5.7#simulation-templates)
