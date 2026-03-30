<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/androidfileserver-settings-in-the-unreal-engine-project-settings?application_version=5.7 -->

# AndroidFileServer

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
6. [Project Settings](/documentation/en-us/unreal-engine/project-settings-in-unreal-engine "Project Settings")
7. [Plugins Settings](/documentation/en-us/unreal-engine/plugins-section-of-the-unreal-engine-project-settings "Plugins Settings")
8. AndroidFileServer

# AndroidFileServer

Reference for the AndroidFileServer section of the Unreal Engine Project Settings.

![AndroidFileServer](https://dev.epicgames.com/community/api/documentation/image/11c60d59-a336-4508-b5a6-85891977e98b?resizing_type=fill&width=1920&height=335)

 On this page

## AndroidFileServer

### Packaging

| **Setting** | **Description** |
| --- | --- |
| **Use AndroidFileServer** | Enable the AndroidFileServer plugin. |
| **Allow Network Connection** | Allow FileServer connection using the network. |
| **Security Token** | Optional security token required to start FileServer (leave empty to disable). |
| **Include in Shipping** | Embed FileServer in Shipping builds. |
| **Allow External Start in Shipping** | Allow FileServer to be started in Shipping builds with UnrealAndroidFileTool. |
| **Compile AFSProject** | Compile standalone AFS project. |

### Deployment

| **Setting** | **Description** |
| --- | --- |
| **Use Compression** | Enable compression during data transfer. |
| **Log Files** | Log transferred files. |
| **Report Stats** | Report transfer rate statistics. |

### Connection

| **Setting** | **Description** |
| --- | --- |
| **Connection Type** | Defines how to connect to the file server. You can choose from the following options:   * **USB Only** * **Network Only** * **USB and Network Combined** |
| **Use Manual IP Address?** | Defines whether to use manual IP address instead of automatic query from device. Use only for single-device deploys. |
| **Manual IP Address** | IP address of the device to use. |

* [ui](https://dev.epicgames.com/community/search?query=ui)
* [basics](https://dev.epicgames.com/community/search?query=basics)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [AndroidFileServer](/documentation/en-us/unreal-engine/androidfileserver-settings-in-the-unreal-engine-project-settings?application_version=5.7#androidfileserver)
* [Packaging](/documentation/en-us/unreal-engine/androidfileserver-settings-in-the-unreal-engine-project-settings?application_version=5.7#packaging)
* [Deployment](/documentation/en-us/unreal-engine/androidfileserver-settings-in-the-unreal-engine-project-settings?application_version=5.7#deployment)
* [Connection](/documentation/en-us/unreal-engine/androidfileserver-settings-in-the-unreal-engine-project-settings?application_version=5.7#connection)
