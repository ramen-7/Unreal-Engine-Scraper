<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-device-profiles-in-unreal-engine?application_version=5.7 -->

# Setting Device Profiles

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
6. [General Platform Support](/documentation/en-us/unreal-engine/tools-for-general-platform-support-in-unreal-engine "General Platform Support")
7. Setting Device Profiles

# Setting Device Profiles

Set device profiles for platform-specific configurations

![Setting Device Profiles](https://dev.epicgames.com/community/api/documentation/image/14fcf0b3-5477-4aca-afbd-8530e7b2f4f1?resizing_type=fill&width=1920&height=335)

 On this page

The best way to set device-specific configurations is to create a custom `Config/DefaultDeviceProfiles.ini` inside your project. You can set many properties in a device profile, such as a texture pool size; it is the recommended way of handling scalability on different mobile devices or in scalability settings buckets on PC/Mac.

```
|  |  |
| --- | --- |
|  | [iPhone5 DeviceProfile] |
|  | DeviceType=IOS |
|  | BaseProfileName=IOS |
|  | MeshLODSettings= |
|  | TextureLODSettings= |
|  | +CVars=r.RenderTargetSwitchWorkaround=1 |
|  |  |
|  | [iPhone5S DeviceProfile] |
|  | DeviceType=IOS |
|  | BaseProfileName=IOS |
|  | MeshLODSettings= |
|  | TextureLODSettings= |
|  | +CVars=r.MobileContentScaleFactor=2 |
|  | +CVars=r.BloomQuality=1 |
|  | +CVars=r.DepthOfFieldQuality=1 |
|  | +CVars=r.LightShaftQuality=1 |

Copy full snippet
```

For more on setting up configuration files, see the main [Configuration Files](/documentation/en-us/unreal-engine/configuration-files-in-unreal-engine) documentation.

### iOS

Device profiles can be used to set your game's resolution for iOS devices. The `r.MobileContentScaleFactor` property is relative to the 'nominal iOS resolution' for a device. For example, a Retina iPad has actual resolution 2048x1536, but nominal resolution 1024x768, so you would use 2.0 to get native resolution there. You can also use fractional values like 1.5 if you want more resolution but not the full performance hit from running at native resolution.

```
	[iPad3 DeviceProfile]
	+CVars=r.MobileContentScaleFactor=1

	[iPad4 DeviceProfile]
	+CVars=r.MobileContentScaleFactor=2

	[iPadAir DeviceProfile]
	+CVars=r.MobileContentScaleFactor=2
Copy full snippet
```

The iOS device profiles can be seen in `BaseDeviceProfiles` in `Engine/Config`. These categories are set through a plugin system, with the default plugin being **iOSDeviceProfileSelector**. The iOS device categories are simply the name of the device.

### Android

Android has hierarchical device profile categories (see `BaseDeviceProfiles.ini` in `Engine/Config` for examples). These categories are set through a plugin system, with the default plugin being **AndroidDeviceProfileSelector**.

## Memory Buckets

You can specify how different Platforms with different memory capabilities will run your Unreal Engine 4 (UE4) project, and what options they will use by adding **Memory Buckets**. To add this capability you will first need to open up your projects **Engine.ini** file (use **Android/AndroidEngine.ini**, **IOS/IOSEngine.ini,**  or any of the **PlatformNameEngine.ini** files to set on a per platform basis) in a text editing program. Several defaults are already set up for your convenience. For example, the following is already entered in **AndroidEngine.ini**:

```
	[PlatformMemoryBuckets]
	LargestMemoryBucket_MinGB=8
	LargerMemoryBucket_MinGB=6
	DefaultMemoryBucket_MinGB=4
	SmallerMemoryBucket_MinGB=3
	 ; for now, we require 3gb
	SmallestMemoryBucket_MinGB=3
Copy full snippet
```

You can specify which Memory Bucket should be associated with which device setting in **DeviceProfiles.ini**. For example, to adjust how much memory the Texture Streaming Pool should use, you would add the following to your DeviceProfiles.ini file:

```
	[Mobile DeviceProfile]
	+CVars_Default=r.Streaming.PoolSize=180
	+CVars_Smaller=r.Streaming.PoolSize=150
	+CVars_Smallest=r.Streaming.PoolSize=70
	+CVars_Tiniest=r.Streaming.PoolSize=16
Copy full snippet
```

Where "Mobile" is replaced with the name of the specific platform you're adding the Device Profile for. You can also use Memory Buckets to specify the rendering settings that will be used. In the following example, the **TextureLODGroup** for Textures that use the **World setting** have been setup so that if UE4 detects a device using Tiniest Memory Bucket it will adjust the **MaxLODSize** from 1024 to 256, reducing the needed memory for textures that have their LOD group set to World.

```
	[Mobile DeviceProfile]
	+TextureLODGroups=(Group=TEXTUREGROUP_World, MaxLODSize=1024, OptionalMaxLODSize=1024, OptionalLODBias=1, MaxLODSize_Smaller=1024, MaxLODSize_Smallest=1024, MaxLODSize_Tiniest=256, LODBias=0, LODBias_Smaller=0, LODBias_Smallest=1, MinMagFilter=aniso, MipFilter=point)
Copy full snippet
```

* [settings](https://dev.epicgames.com/community/search?query=settings)
* [platforms](https://dev.epicgames.com/community/search?query=platforms)
* [device profiles](https://dev.epicgames.com/community/search?query=device%20profiles)
* [config](https://dev.epicgames.com/community/search?query=config)
* [configs](https://dev.epicgames.com/community/search?query=configs)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [iOS](/documentation/en-us/unreal-engine/setting-up-device-profiles-in-unreal-engine?application_version=5.7#ios)
* [Android](/documentation/en-us/unreal-engine/setting-up-device-profiles-in-unreal-engine?application_version=5.7#android)
* [Memory Buckets](/documentation/en-us/unreal-engine/setting-up-device-profiles-in-unreal-engine?application_version=5.7#memorybuckets)
