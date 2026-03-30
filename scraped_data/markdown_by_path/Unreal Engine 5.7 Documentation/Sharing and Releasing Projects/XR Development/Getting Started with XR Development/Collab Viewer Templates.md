<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/collab-viewer-templates-in-unreal-engine?application_version=5.7 -->

# Collab Viewer Templates

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
5. [Sharing and Releasing Projects](/documentation/en-us/unreal-engine/sharing-and-releasing-projects-for-unreal-engine "Sharing and Releasing Projects")
6. [XR Development](/documentation/en-us/unreal-engine/developing-for-xr-experiences-in-unreal-engine "XR Development")
7. [Getting Started with XR Development](/documentation/en-us/unreal-engine/getting-started-with-xr-development-in-unreal-engine "Getting Started with XR Development")
8. Collab Viewer Templates

# Collab Viewer Templates

Describes how to get started doing collaborative VR and desktop design reviews with the Collab Viewer Templates.

![Collab Viewer Templates](https://dev.epicgames.com/community/api/documentation/image/bd3c58f8-c384-452b-ac94-a56428a41b5c?resizing_type=fill&width=1920&height=335)

 On this page

The Collab Viewer Templates join multiple people together in a shared experience of the same 3D content. They are intended to make it easier and quicker for your team to review and communicate about designs in realtime, so that you can identify problems and iterate on the content more efficiently.

## Industry-Specific Templates

Unreal Engine offers two Collab Viewer Templates to work with, that are customized for specific user needs.

* OEM/Manufacturing: This template has custom content intended for automotive design. It includes different types of lights present in the scene to demonstrate effects on car surfaces under different conditions.

  [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/48d55d8a-7511-4026-bc2f-ecd45b34854d/oem-manufacturing-template.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/48d55d8a-7511-4026-bc2f-ecd45b34854d/oem-manufacturing-template.png)

  Click image to expand.
* AEC: This template has custom content intended for architecture, engineering, and construction, including a sample building to demonstrate how to set up an architectural mockup.

  [![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/47ff2a25-2718-447a-9db7-99eb0d624aa1/aec-template.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/47ff2a25-2718-447a-9db7-99eb0d624aa1/aec-template.png)

  Click image to expand.

Every participant in a Collab Viewer session can use a computer set up with a standard mouse and keyboard, or with a VR headset and motion controllers. The Templates offer a variety of built-in tools for interacting with the scene content at runtime. Every participant can move objects around, change objects to a see-through X-Ray material, play animations that "explode" content into different spatial arrangements, and more. Everyone sees an avatar of each other person in the session, and can use a laser pointer tool to point out features of the environment:

[![Review with multiple simulataneous users](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ee5139d8-d331-4cff-8de0-41046ac5e736/collabviewer-overview.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/ee5139d8-d331-4cff-8de0-41046ac5e736/collabviewer-overview.png)

Click image to expand.

The Collab Viewer Templates handle most of the difficult problems inherent in multi-viewer experiences, including setting up connections and replicating presence information between multiple computers. Use one as a starting point for your design review experiences, so that you can spend less time setting up networking and more time thinking about your designs. And, while they are most useful for evaluating and communicating your designs in a team environment, they offer enough interaction and navigation controls to be a good a starting point even for single-person experiences around your 3D content.

All of the interaction and navigation controls are provided by Blueprint classes in the Project, so you can customize them, learn from them, or even copy them into your own Projects. For more about working with Blueprint, see [Blueprint Visual Scripting](/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine).

The pages in this section describe everything you need to know to get started with the Collab Viewer Templates, and to use them for your own content.

For a video walkthrough of the Collab Viewer Templates that demonstrates many of the concepts and procedures described in this documentation, see the recorded webinar:

## Workflow

The typical usage pattern for a Collab Viewer Template is:

1. Create a new Project from the Template, or bring the Template content into your own existing Project.
2. Set up the Project with the content you want to share with others.
   This typically involves the same kinds of data import and look development tasks that you would do in any Unreal Engine Project. For details on specific considerations that you'll need to keep in mind when setting up your content, such as collisions and navigation meshes, see [Adding Your Own Content to the Collab Viewer](/documentation/en-us/unreal-engine/adding-your-own-content-to-the-collab-viewer-in-unreal-engine).
3. Use the tools built in to the Unreal Editor to package your Project to an executable file.
4. Share that file with the people who need to be part of the collaborative review.
5. One person launches the packaged Unreal Engine application and starts it up in server mode.
6. Each other person who wants to be part of the same viewing session launches their copy of the application on a separate computer and joins the server session.

For a detailed tutorial that walks you through the steps above using the default content in the Template, see the [Quick Start](/documentation/en-us/unreal-engine/collab-viewer-template-quick-start-in-unreal-engine).

## VR Support

The Collab Viewer Templates use the OpenXR plugin by default to support VR headset interactions. The custom plugins for individual platforms such as Oculus VR and Steam VR are still supported and can be re-enabled if necessary.

## Getting Started

[![Collab Viewer Template Quick Start](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/4af952d9-e3a4-460f-9144-d161d04a5d7a/topic-image.png)

Collab Viewer Template Quick Start

A complete, step-by-step guide to getting up and running with the Collab Viewer Template.](/documentation/en-us/unreal-engine/collab-viewer-template-quick-start-in-unreal-engine)

## How-To Guides

[![Annotating in the Collab Viewer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/44c146a1-a68a-40c4-897a-7872c04d12f6/annotating-banner.png)

Annotating in the Collab Viewer

Describes how to take quick notes at runtime in the Collab Viewer Template.](/documentation/en-us/unreal-engine/annotating-in-the-collab-viewer-in-unreal-engine)
[![Measuring in the Collab Viewer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/3654034e-e4dc-48b7-960d-17a2fa7486e7/adding-measurements-banner.png)

Measuring in the Collab Viewer

Describes how to add measurements at runtime in the Collab Viewer Template.](/documentation/en-us/unreal-engine/measuring-in-the-collab-viewer-in-unreal-engine)
[![Saving and Loading a Session](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f1893823-7b65-4698-b7ee-bf5bbe2c003e/topic-image.png)

Saving and Loading a Session

Describes how to save (and then later reload) a session, including Annotations, Measurements, and transparency](/documentation/en-us/unreal-engine/saving-and-loading-a-session-in-unreal-engine)
[![Adding Your Own Content to the Collab Viewer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/89cb9688-5d44-4d68-b9e9-0364caea0f2a/00-topic-image.png)

Adding Your Own Content to the Collab Viewer

Describes how to get your own models into the Collab Viewer Template.](/documentation/en-us/unreal-engine/adding-your-own-content-to-the-collab-viewer-in-unreal-engine)
[![Working with Bookmarks in the Collab Viewer Template](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6f3fe648-4da0-40be-a68d-402920e68c4e/00-topic-image_ue5.png)

Working with Bookmarks in the Collab Viewer Template

Describes how to place Bookmarks in your Level to provide pre-set points of view, and how to assign those Bookmarks to hotkeys.](/documentation/en-us/unreal-engine/working-with-bookmark-in-the-collab-viewer-template-in-unreal-engine)
[![Setting Up Explode Animations](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/cc3c2870-e125-4721-9aa6-f9cc54c73f1e/00-topic-image_ue5.png)

Setting Up Explode Animations

Describes how to set up an](/documentation/en-us/unreal-engine/setting-up-xr-explode-animations-in-unreal-engine)

## Reference

[![Interacting with the Collab Viewer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/bf6aeb9c-2c6c-46c9-a17d-2647a9e125d7/collabviewer-controls-topic.png)

Interacting with the Collab Viewer

Describes how to control the camera and interact with content at runtime in the Collab Viewer Templates.](/documentation/en-us/unreal-engine/interacting-with-the-collab-viewer-in-unreal-engine)
[![Networking Requirements for the Collab Viewer](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a6e3a25a-93ae-450c-9df5-d172a110c707/collabviewer-networking-topic.png)

Networking Requirements for the Collab Viewer

Describes requirements and considerations that apply when you connect multiple computers together into a design review experience.](/documentation/en-us/unreal-engine/networking-requirements-for-the-collab-viewer-in-unreal-engine)

* [collaboration](https://dev.epicgames.com/community/search?query=collaboration)
* [templates](https://dev.epicgames.com/community/search?query=templates)
* [collab viewer](https://dev.epicgames.com/community/search?query=collab%20viewer)
* [design review](https://dev.epicgames.com/community/search?query=design%20review)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Industry-Specific Templates](/documentation/en-us/unreal-engine/collab-viewer-templates-in-unreal-engine?application_version=5.7#industry-specifictemplates)
* [Workflow](/documentation/en-us/unreal-engine/collab-viewer-templates-in-unreal-engine?application_version=5.7#workflow)
* [VR Support](/documentation/en-us/unreal-engine/collab-viewer-templates-in-unreal-engine?application_version=5.7#vrsupport)
* [Getting Started](/documentation/en-us/unreal-engine/collab-viewer-templates-in-unreal-engine?application_version=5.7#gettingstarted)
* [How-To Guides](/documentation/en-us/unreal-engine/collab-viewer-templates-in-unreal-engine?application_version=5.7#how-toguides)
* [Reference](/documentation/en-us/unreal-engine/collab-viewer-templates-in-unreal-engine?application_version=5.7#reference)
