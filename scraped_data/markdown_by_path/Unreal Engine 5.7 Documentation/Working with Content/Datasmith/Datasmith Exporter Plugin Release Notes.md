<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/datasmith-exporter-plugin-release-notes-for-unreal-engine?application_version=5.7 -->

# Datasmith Exporter Plugin Release Notes

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
5. [Working with Content](/documentation/en-us/unreal-engine/working-with-content-in-unreal-engine "Working with Content")
6. [Datasmith](/documentation/en-us/unreal-engine/datasmith-plugins-for-unreal-engine "Datasmith")
7. Datasmith Exporter Plugin Release Notes

# Datasmith Exporter Plugin Release Notes

Information about the latest updates to the Datasmith Exporter plugins.

![Datasmith Exporter Plugin Release Notes](https://dev.epicgames.com/community/api/documentation/image/2ba85ec6-f155-409e-aa8b-c23659284661?resizing_type=fill&width=1920&height=335)

 On this page

To view the release notes for the Datasmith Exporter Plugins for Twinmotion, see [Datasmith Release Notes for Twinmotion](https://dev.epicgames.com/documentation/en-us/twinmotion/datasmith-explorer-plugin-release-notes-for-twinmotion) in the Twinmotion documentation.

## Datasmith exporter Plugin: SketchUp 5.7.300

**New:**

* Windows:

  + The Datasmith Exporter Plugin is now signed in Sketchupʼs Extension Manager.
  + Mac:

    - The Datasmith Exporter Plugin is now signed in Sketchupʼs Extension Manager.

## Datasmith Exporter Plugin: SketchUp

**New:**

* Provides a way to export the current viewport camera transform information in Datasmith and through Direct Link.

**Bug Fix:**

* You can now install the Datasmith Exporter plugin if a previous install is not found.

## Datasmith Exporter Plugin: Rhino 3D

**New:**

* Provides a way to export the current viewport camera transform information in Datasmith and through Direct Link.
* Provides a way to export Named views camera transform information in Datasmith and through Direct Link.

**Bug Fix:**

* Direct Link for Unreal Engine 5.7 updates lights on settings change in Rhino.
* Fixed UV repetition on objects for Datasmith (.udatasmith files)
* Allow Install of Datasmith Exporter plugin if previous install is not found.
* Material Handling:

  + Custom Materials

    - Exported as expected.
  + Double Sided Materials

    - Currently exports only the front face.

    Rhinoʼs “Double Sided” material actually uses two different materials, one per face. This is not currently supported in UE and TM.
* Emission:

  + Only intensity = 1 is supported.
* Gem and Glass:

  + Partially supported.
  + Generates a material with some opacity, which is not equivalent to true clarity.
  + Refraction values cannot be exported due to a limitation in the Datasmith material, where refraction mode is not exposed or changeable.
* Metal:

  + Exported as expected.
* Paint:

  + No special behavior.
  + Physically-based.
  + Exported as expected.
* Picture

  + Partially supported.
  + Only basic properties are exported.
  + Masking and other advanced attributes are ignored.
* Plaster

  + Exported as expected.
* Plastic

  + Exported as expected.
* Fixed the issue where Rhino Mac force shutdowns when clicking Sync for Direct Link Resolved

## Datasmith Exporter Plugin: ArchiCAD

**New:**

* Now supports ArchiCAD 29.

**Bug Fix:**

* You can now install the Datasmith Exporter plugin if a previous install is not found.

## Datasmith Exporter Plugin: NavisWorks

**Bug Fix:**

* You can now install the Datasmith Exporter plugin if a previous install is not found.

## Datasmith Exporter Plugin: SolidWorks

**Bug Fix:**

* You can now install the Datasmith Exporter plugin if a previous install is not found.

Datasmith Exporter Plugin Release Note

* [datasmith](https://dev.epicgames.com/community/search?query=datasmith)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Datasmith exporter Plugin: SketchUp 5.7.300](/documentation/en-us/unreal-engine/datasmith-exporter-plugin-release-notes-for-unreal-engine?application_version=5.7#datasmithexporterplugin:sketchup57300)
* [Datasmith Exporter Plugin: SketchUp](/documentation/en-us/unreal-engine/datasmith-exporter-plugin-release-notes-for-unreal-engine?application_version=5.7#datasmithexporterplugin:sketchup)
* [Datasmith Exporter Plugin: Rhino 3D](/documentation/en-us/unreal-engine/datasmith-exporter-plugin-release-notes-for-unreal-engine?application_version=5.7#datasmithexporterplugin:rhino3d)
* [Datasmith Exporter Plugin: ArchiCAD](/documentation/en-us/unreal-engine/datasmith-exporter-plugin-release-notes-for-unreal-engine?application_version=5.7#datasmithexporterplugin:archicad)
* [Datasmith Exporter Plugin: NavisWorks](/documentation/en-us/unreal-engine/datasmith-exporter-plugin-release-notes-for-unreal-engine?application_version=5.7#datasmithexporterplugin:navisworks)
* [Datasmith Exporter Plugin: SolidWorks](/documentation/en-us/unreal-engine/datasmith-exporter-plugin-release-notes-for-unreal-engine?application_version=5.7#datasmithexporterplugin:solidworks)
