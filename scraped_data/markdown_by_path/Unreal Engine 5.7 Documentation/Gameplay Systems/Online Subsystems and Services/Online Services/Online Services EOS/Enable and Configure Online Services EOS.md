<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/enable-and-configure-online-services-eos-in-unreal-engine?application_version=5.7 -->

# Enable and Configure Online Services EOS

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
6. [Online Subsystems and Services](/documentation/en-us/unreal-engine/online-subsystems-and-services-in-unreal-engine "Online Subsystems and Services")
7. [Online Services](/documentation/en-us/unreal-engine/online-services-in-unreal-engine "Online Services")
8. [Online Services EOS](/documentation/en-us/unreal-engine/online-services-eos-plugins-in-unreal-engine "Online Services EOS")
9. Enable and Configure Online Services EOS

# Enable and Configure Online Services EOS

Access EOS Game Services and Epic Account services in your project through the Online Services EOSGS and EOS plugins.

![Enable and Configure Online Services EOS](https://dev.epicgames.com/community/api/documentation/image/79893b69-4454-4f96-b503-52b5062f90f1?resizing_type=fill&width=1920&height=335)

 On this page

The Online Services plugins and their interfaces provide a common way to access the functionality of various online services, in particular, Epic Online Services (EOS). To take advantage of EOS through the Online Services plugins, you can use the Online Services EOSGS and Online Services EOS plugins. In addition to outlining the differences between these plugins and the interfaces each supports, this page describes how to enable and configure these plugins for use in your Unreal Engine project.

## Plugin Structure

The EOS implementation of the Online Services plugins is split into separate plugins:

* Online Services EOSGS
* Online Services EOS

The Epic Online Services Game Services (EOSGS) plugin handles [EOS Game Services](https://dev.epicgames.com/docs/game-services) functionality. The Online Services Epic Online Services (EOS) plugin supplements the EOSGS plugin and handles [EOS Epic Account Services](https://dev.epicgames.com/docs/epic-account-services) functionality. To take advantage of EOS Game Services and EOS Epic Account Services, you can use both plugins simultaneously in your project.

### Implemented Interfaces

The following table shows which interfaces these plugins implement:

| **Interface** | **Online Services EOSGS** | **Online Services EOS** |
| --- | --- | --- |
| [Achievements](/documentation/404) | ✓ |  |
| [Auth](/documentation/404) | ✓ | ✓ |
| [Commerce](/documentation/404) |  | ✓ |
| [External UI](/documentation/404) |  | ✓ |
| [Leaderboards](/documentation/404) | ✓ |  |
| [Lobbies](/documentation/404) | ✓ |  |
| [Presence](/documentation/404) |  | ✓ |
| [Sessions](/documentation/404) | ✓ |  |
| [Social](/documentation/404) |  | ✓ |
| [Stats](/documentation/404) | ✓ |  |
| [Title File](/documentation/404) | ✓ |  |
| [User File](/documentation/404) | ✓ |  |
| [User Info](/documentation/404) |  | ✓ |

## Choosing Online Services or Online Subsystem

Online Services EOSGS and EOS plugins are an improved version of the Online Subsystem plugins, and implement the EOS SDK for Online Services similar to the way Online Subsystem EOS implements the Epic Online Services Software Developer Kit (EOS SDK) for the Online Subsystem. For more information about which is right for your project, see the [Using Online Services or Online Subsystem](/documentation/404) section of the [Online Services Overview](/documentation/404) documentation.

## Enable Online Services EOS Plugins

To enable either Online Services EOSGS or Online Services EOS in your Unreal Engine project, follow these steps:

1. Create or open an Unreal Engine C++ project.
2. From the Unreal Editor menu bar, navigate to **Edit > Plugins**. This opens a new window or tab titled **Plugins**.
3. In this new window, search for "Online Services" or select the **Online Platform** category from the navigation bar on the left-side.
   * A number of plugins should appear. The **Online Services** base plugin should be enabled by default.
4. Enable the plugins you want to use:
   * **Online Services EOS**
   * **Online Services EOSGS**

A warning message should appear stating "You must restart Unreal Editor for your changes to take effect." If you have enabled all the plugins you want and you are ready to restart the Unreal Editor, click **Restart Now**.

The Online Services EOS plugins you previously enabled should now be ready for use in your Unreal Engine project.

## Developer Portal

To take advantage of the Online Services EOS plugins, you must have an organization and product registered and configured with Epic Online Services. Your EOS product is what the Online Services EOS plugins connect with to communicate information between your game and Epic Online Services. Read about the [Developer Portal](https://dev.epicgames.com/docs/dev-portal) in the Epic Developer Documentation to register your organization and product with Epic Online Services.

## Configure Unreal Engine

### Default Services

To use Epic Online Services in your project, you need to configure the Online Services base plugins to use the EOS implementation. To specify EOS as the default platform services, add or edit the following section of your project’s `DefaultEngine.ini` file located in your project’s Config directory:

```
[OnlineServices]
DefaultServices=Epic
Copy full snippet
```

### Network Drivers

Network driver configuration is independent of the online systems, so the same configuration should be valid for Online Services plugins as for the Online Subsystem plugins.

To configure the network drivers for online systems, add the following to your project’s `DefaultEngine.ini` file:

```
[/Script/Engine.Engine]
!NetDriverDefinitions=ClearArray
+NetDriverDefinitions=(DefName="GameNetDriver",DriverClassName="SocketSubsystemEOS.NetDriverEOSBase",DriverClassNameFallback="OnlineSubsystemUtils.IpNetDriver")
+NetDriverDefinitions=(DefName="DemoNetDriver",DriverClassName="/Script/Engine.DemoNetDriver",DriverClassNameFallback="/Script/Engine.DemoNetDriver")

[/Script/Engine.GameEngine]
!NetDriverDefinitions=ClearArray
+NetDriverDefinitions=(DefName="GameNetDriver",DriverClassName="SocketSubsystemEOS.NetDriverEOSBase",DriverClassNameFallback="OnlineSubsystemUtils.IpNetDriver")
+NetDriverDefinitions=(DefName="DemoNetDriver",DriverClassName="/Script/Engine.DemoNetDriver",DriverClassNameFallback="/Script/Engine.DemoNetDriver")
Copy full snippet
```

### Epic Online Services

The Online Services EOSGS and EOS plugins use the EOS SDK to communicate with the Epic Online Services backend. In order for your project to communicate directly with your EOS product as configured in the [Epic Developer Portal](https://dev.epicgames.com/portal/), you must configure the Online Services plugins.

To connect your EOS product with your Unreal Engine project, add the following to your project’s `DefaultEngine.ini` file:

```
[OnlineServices.EOS]
ProductId=PRODUCT_ID
SandboxId=SANDBOX_ID
DeploymentId=DEPLOYTMENT_ID
ClientId=CLIENT_ID
ClientSecret=CLIENT_SECRET
ClientEncryptionKey=CLIENT_ENCRYPTION_KEY
Copy full snippet
```

where you need to replace `PRODUCT_ID`, `SANDBOX_ID`, `DEPLOYMENT_ID`, `CLIENT_ID`, and `CLIENT_SECRET` with the values found on your product’s Product Settings page in the [Epic Developer Portal](https://dev.epicgames.com/portal/).

The following table describes each of these settings:

| **Setting** | **Description** |
| --- | --- |
| Product ID | The EOS SDK uses this ID to identify your product. |
| Sandbox ID | The product belongs to the sandbox with this ID value. |
| Deployment ID | The deployment ID you are targeting. |
| Client ID | The client ID for your product. This ID starts with the first three characters xyz. |
| Client Secret | The client secret used to verify your client ID. |
| Client Encryption Key | A 64-byte hexadecimal string that encrypts data uploaded to an EOS service. Unlike other settings, EOS does not manage this encryption key and it is not stored in your product settings. This key is specific to your game and not known to Epic Games to protect users' data privacy. It is used to encrypt data for Player and Title data storage.  If you are not using Player or Title File storage, you can use the following as the default encryption key (64 ones): `1111111111111111111111111111111111111111111111111111111111111111`. If you are using Player or Title File storage, choose your own key different from this default key and keep it secret. |

## Next Steps

Your project should now be configured to use Online Services EOS. The next step is to implement Epic Online Services in your game, with the first step being sign-in.

## Additional Information

For more information, see the following documentation pages:

* Documentation on the Epic Developer Portal site:
  + [Epic Online Services](https://dev.epicgames.com/docs/)
  + [EOS Game Services](https://dev.epicgames.com/docs/game-services/)
  + [EOS Epic Account Services](https://dev.epicgames.com/docs/epic-account-services/)
  + [Epic Developer Portal](https://dev.epicgames.com/portal/)
* Documentation on the Unreal Engine Documentation site:
  + [Online Services Plugins](/documentation/en-us/unreal-engine/online-services-in-unreal-engine)
  + [Online Services Overview](/documentation/404)
  + [Use Online Services Plugins](/documentation/en-us/unreal-engine/use-the-online-services-plugins-in-unreal-engine)

* [programming](https://dev.epicgames.com/community/search?query=programming)
* [online](https://dev.epicgames.com/community/search?query=online)
* [eos](https://dev.epicgames.com/community/search?query=eos)
* [eas](https://dev.epicgames.com/community/search?query=eas)
* [egs](https://dev.epicgames.com/community/search?query=egs)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Plugin Structure](/documentation/en-us/unreal-engine/enable-and-configure-online-services-eos-in-unreal-engine?application_version=5.7#pluginstructure)
* [Implemented Interfaces](/documentation/en-us/unreal-engine/enable-and-configure-online-services-eos-in-unreal-engine?application_version=5.7#implementedinterfaces)
* [Choosing Online Services or Online Subsystem](/documentation/en-us/unreal-engine/enable-and-configure-online-services-eos-in-unreal-engine?application_version=5.7#choosingonlineservicesoronlinesubsystem)
* [Enable Online Services EOS Plugins](/documentation/en-us/unreal-engine/enable-and-configure-online-services-eos-in-unreal-engine?application_version=5.7#enableonlineserviceseosplugins)
* [Developer Portal](/documentation/en-us/unreal-engine/enable-and-configure-online-services-eos-in-unreal-engine?application_version=5.7#developerportal)
* [Configure Unreal Engine](/documentation/en-us/unreal-engine/enable-and-configure-online-services-eos-in-unreal-engine?application_version=5.7#configureunrealengine)
* [Default Services](/documentation/en-us/unreal-engine/enable-and-configure-online-services-eos-in-unreal-engine?application_version=5.7#defaultservices)
* [Network Drivers](/documentation/en-us/unreal-engine/enable-and-configure-online-services-eos-in-unreal-engine?application_version=5.7#networkdrivers)
* [Epic Online Services](/documentation/en-us/unreal-engine/enable-and-configure-online-services-eos-in-unreal-engine?application_version=5.7#epiconlineservices)
* [Next Steps](/documentation/en-us/unreal-engine/enable-and-configure-online-services-eos-in-unreal-engine?application_version=5.7#nextsteps)
* [Additional Information](/documentation/en-us/unreal-engine/enable-and-configure-online-services-eos-in-unreal-engine?application_version=5.7#additionalinformation)
