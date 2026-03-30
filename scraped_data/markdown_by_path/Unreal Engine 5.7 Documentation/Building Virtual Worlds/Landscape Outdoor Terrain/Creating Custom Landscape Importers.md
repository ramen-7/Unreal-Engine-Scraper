<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-custom-landscape-importers-in-unreal-engine?application_version=5.7 -->

# Creating Custom Landscape Importers

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
5. [Building Virtual Worlds](/documentation/en-us/unreal-engine/building-virtual-worlds-in-unreal-engine "Building Virtual Worlds")
6. [Landscape Outdoor Terrain](/documentation/en-us/unreal-engine/landscape-outdoor-terrain-in-unreal-engine "Landscape Outdoor Terrain")
7. Creating Custom Landscape Importers

# Creating Custom Landscape Importers

Guide to creating new Landscape import formats via plugin.

![Creating Custom Landscape Importers](https://dev.epicgames.com/community/api/documentation/image/7e78da3f-7a53-4545-b9b2-4c5dba88d124?resizing_type=fill&width=1920&height=335)

 On this page

Creating your own heightmap and weightmap formats for importing landscape data is accomplished by writing a plugin. The plugin will add your new format to the engine, as well as importing the data from your files.

### Writing A Custom Importer

* In order to create new importers, your plugin should create instances of objects implementing `ILandscapeHeightmapFileFormat` and `ILandscapeWeightmapFileFormat`, and register those objects with `ILandscapeEditorModulemodule::RegisterHeightmapFileFormat` and `ILandscapeEditorModulemodule::RegisterWeightmapFileFormat`, respectively.
* Implementing the `ILandscapeHeightmapFileFormat` interface in a plugin requires overriding the following functions:

  1. `const FLandscapeFileTypeInfo& GetInfo() const`: Returns type information indicating which file types this class handles, and whether or not exporting is supported.
  2. `FLandscapeHeightmapInfo Validate(const TCHAR* HeightmapFilename) const` - Validates the named file, or rejects it and returns an error code and message.
  3. `FLandscapeHeightmapImportData Import(const TCHAR* HeightmapFilename, FLandscapeFileResolution ExpectedResolution) const` - Actually imports the file.
  4. `void Export(const TCHAR* HeightmapFilename, TArrayView<const uint16> Data, FLandscapeFileResolution DataResolution, FVector Scale) const` - Exports the file, if this format supports exporting (see the return value from `GetInfo`). This is the only function that doesn't need to be overridden in order to compile. However, if it is called without being overridden, it will call `check`.
  5. `(Destructor)` - Classes that implement this interface should use a virtual destructor, as they will be deleted via a pointer to the interface class.
* Implementing the `ILandscapeWeightmapFileFormat` interface is nearly identical, with only minor differences in some return types:

  1. `const FLandscapeFileTypeInfo& GetInfo() const` - Returns type information indicating which file types this class handles, and whether or not exporting is supported.
  2. `FLandscapeWeightmapInfo Validate(const TCHAR* WeightmapFilename, FName LayerName) const` - Validates the named file, or rejects it and returns an error code and message. LayerName represents the target layer name of the weightmap being validated.
  3. `FLandscapeWeightmapImportData Import(const TCHAR* WeightmapFilename,FName LayerName, FLandscapeFileResolution ExpectedResolution) const` - Actually imports the file.
  4. `void Export(const TCHAR* WeightmapFilename, FName LayerName, TArrayView<const uint8> Data, FLandscapeFileResolution DataResolution, FVector Scale) const` - Exports the file, if this format supports exporting (see the return value from `GetInfo`). This is the only function that doesn't need to be overridden in order to compile. However, if it is called without being overridden, it will call `check`.
  5. `(Destructor)` - Classes that implement this interface should use a virtual destructor, as they will be deleted via a pointer to the interface class.
* For further information and examples, you can see the interfaces in `LandscapeFileFormatInterfaces.h`, the .PNG implementations in `LandscapeFileFormatPng.cpp` and `LandscapeFileFormatPng.h` , and the .RAW implementations in `LandscapeFileFormatRaw.cpp` and `LandscapeFileFormatRaw.h`. All of this code is in the LandscapeEditor module in the engine.

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Writing A Custom Importer](/documentation/en-us/unreal-engine/creating-custom-landscape-importers-in-unreal-engine?application_version=5.7#writing-a-custom-importer)
