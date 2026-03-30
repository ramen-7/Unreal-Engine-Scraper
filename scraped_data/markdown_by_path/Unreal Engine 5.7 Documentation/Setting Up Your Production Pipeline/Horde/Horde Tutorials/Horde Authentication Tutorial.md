<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/horde-authentication-tutorial-for-unreal-engine?application_version=5.7 -->

# Horde Authentication Tutorial

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
5. [Setting Up Your Production Pipeline](/documentation/en-us/unreal-engine/setting-up-your-production-pipeline-in-unreal-engine "Setting Up Your Production Pipeline")
6. [Horde](/documentation/en-us/unreal-engine/horde-in-unreal-engine "Horde")
7. [Horde Tutorials](/documentation/en-us/unreal-engine/horde-tutorials-for-unreal-engine "Horde Tutorials")
8. Horde Authentication Tutorial

# Horde Authentication Tutorial

A tutorial for authenticating Horde for use with Unreal Engine.

![Horde Authentication Tutorial](https://dev.epicgames.com/community/api/documentation/image/406650ca-f65c-47aa-8910-a74a1559291d?resizing_type=fill&width=1920&height=335)

 On this page

## Introduction

Horde ships with authentication disabled by default to make it easier to demonstrate and experiment with. Most production deployments will probably want users to log in, and restrict the actions they can perform based on their role.

To do this, Horde supports **[OAuth2](https://oauth.net/2/)** and **[OIDC](https://openid.net/developers/how-connect-works/)**, which is supported by most third party identity providers - including Okta, AWS, Azure, and Google. Configuring an external identity provider is out of scope for this documentation, though the relevant configuration points are touched on in the [Deployment > Server](/documentation/en-us/unreal-engine/horde-server-for-unreal-engine#authentication) page.

If you don't have an existing OIDC-compatible identity provider, Horde includes its own - which this guide covers.

## Prerequisites

* Horde Server installation (see the [Horde Installation Tutorial](/documentation/en-us/unreal-engine/horde-installation-tutorial-for-unreal-engine)).
* A valid certificate, and [HTTPS support](/documentation/en-us/unreal-engine/horde-server-for-unreal-engine#https) enabled on your server.

## Steps

1. In your [server.json](/documentation/en-us/unreal-engine/horde-orientation-for-unreal-engine) file set the `AuthMode` property to `Horde`, and restart the server.
2. The first time you launch the server, you'll be prompted to enter an administrator password.
3. After logging in, there will be an `Accounts` menu item in the `Server` menu. From here, you can manage the users allowed to log in to the server, and the [claims](/documentation/en-us/unreal-engine/horde-glossary-for-unreal-engine#authorization) that they have. Horde's account system uses the `http://epicgames.com/ue/horde/group` claim for groups that a user belongs to, and the dashboard will suggest and autocomplete any groups found in the deployment's configuration files.

There are two standard groups defined in the server's `default.globals.json` file, which is included from the standard `globals.json` file by default: `View` and `Run`.

```
"acl": {
    "entries": [
        {
            "claim": {
                "type": "http://epicgames.com/ue/horde/group", 
                "value": "View"
            },
            "profiles": [
                "default-read"
            ]
        },
        {
            "claim": {
                "type": "http://epicgames.com/ue/horde/group", 
                "value": "Run"
            },
            "profiles": [
                "default-run"
            ]
        }
    ]
}
Copy full snippet
```

The `default-read` and `default-run` profiles are defined in code (`AclConfig.cs`). You can define your own profiles within the `profiles` element of each [AclConfig](/documentation/en-us/unreal-engine/horde-schema-for-unreal-engine#aclconfig) object.

* [horde](https://dev.epicgames.com/community/search?query=horde)
* [bronze](https://dev.epicgames.com/community/search?query=bronze)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Introduction](/documentation/en-us/unreal-engine/horde-authentication-tutorial-for-unreal-engine?application_version=5.7#introduction)
* [Prerequisites](/documentation/en-us/unreal-engine/horde-authentication-tutorial-for-unreal-engine?application_version=5.7#prerequisites)
* [Steps](/documentation/en-us/unreal-engine/horde-authentication-tutorial-for-unreal-engine?application_version=5.7#steps)
