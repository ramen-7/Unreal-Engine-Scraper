<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/sequences-folder-structure-in-unreal-engine?application_version=5.7 -->

# Sequences Folder Structure

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
5. [Working with Media](/documentation/en-us/unreal-engine/working-with-media-in-unreal-engine "Working with Media")
6. [Integrating Media](/documentation/en-us/unreal-engine/integrating-media-in-unreal-engine "Integrating Media")
7. [In-Camera VFX](/documentation/en-us/unreal-engine/in-camera-vfx-in-unreal-engine "In-Camera VFX")
8. [In-Camera VFX Project Structure Example](/documentation/en-us/unreal-engine/in-camera-vfx-project-structure-example-in-unreal-engine "In-Camera VFX Project Structure Example")
9. Sequences Folder Structure

# Sequences Folder Structure

A reference guide for organizing your In-Camera VFX project's Sequences files in the Content Browser.

![Sequences Folder Structure](https://dev.epicgames.com/community/api/documentation/image/4073e9af-4434-48b8-beff-dcd7e133bc9b?resizing_type=fill&width=1920&height=335)

![The recommended Media folder structure in the Content Browser](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e1bbcba5-60c4-4d26-ad66-ec8906996db7/cb_sequences.png)

The **Sequences** folder contains all **Level Sequences** and **Animations**, grouped by sequence abbreviation (CE, CP, and SJ in the example shown).

The **Edits** subfolder contains edits that apply to the entire project's sequences taken together. Each individual sequence folder also has an **Edits** subfolder, which applies specifically to that sequence only.

This sample uses the format `(Sequence Code)_(Setup)_(Camera or Anim Pass)_(Take)`. However, this is only an example take-naming convention. Use whatever naming system for your takes that makes sense for your project. The important point is for the naming system to be consistent.

* Edits

  + EDIT\_Origin\_00\_01
  + EDIT\_Origin\_0A\_07
* CE (Sequence Abbreviation)

  + Takes - Sorted by shot name and take number

    - CE\_00\_0A\_01

      * LS\_CE\_00\_0A\_01
      * SNAP\_CE\_00\_0A\_01
      * CE\_00\_0A\_01\_Subscenes

        + LS\_Actor01\_CE\_00\_0A\_01
        + LS\_Actor02\_CE\_00\_0A\_01
      * Animations

        + A\_CE\_00\_0A-01\_Actor02
  + Shots
  + Previs
  + Techvis
  + Edits

    - EDIT\_CE\_00\_01
    - EDIT\_CE\_0G\_99
  + Sublevels

    - CE\_Lighting
    - CE\_Chr

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6e88203f-9e5a-47de-9691-b39806d9f4ab/sequences-chart.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/6e88203f-9e5a-47de-9691-b39806d9f4ab/sequences-chart.png)

A diagram showing the recommended Sequences folder structure for your project in the Content Browser.

* [content browser](https://dev.epicgames.com/community/search?query=content%20browser)
* [animation](https://dev.epicgames.com/community/search?query=animation)
* [sequencer](https://dev.epicgames.com/community/search?query=sequencer)
* [icvfx](https://dev.epicgames.com/community/search?query=icvfx)
* [virtual sets](https://dev.epicgames.com/community/search?query=virtual%20sets)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)
