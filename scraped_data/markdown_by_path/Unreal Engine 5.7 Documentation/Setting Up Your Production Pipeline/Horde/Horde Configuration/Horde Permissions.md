<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/horde-permissions-for-unreal-engine?application_version=5.7 -->

# Horde Permissions

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
7. [Horde Configuration](/documentation/en-us/unreal-engine/horde-configuration-for-unreal-engine "Horde Configuration")
8. Horde Permissions

# Horde Permissions

An overview of Horde Permissions.

![Horde Permissions](https://dev.epicgames.com/community/api/documentation/image/2cf862b9-c1ad-4e4e-b618-9b3d72bda23b?resizing_type=fill&width=1920&height=335)

 On this page

## Authentication

Horde offers three modes of authentication and authorization of users:

* Anonymous
* OpenID Connect
* Built-in user accounts

You can configure the mode via the `AuthMethod` setting.

### Anonymous

Horde ships with authorization disabled by default for demonstration purposes and to get started.

For production deployment, proper authentication must be configured using either OpenID Connect or built-in user accounts.

### OpenID Connect

Horde can use an external OpenID Connect (OIDC) provider for authorization.
See the [server deployment](/documentation/en-us/unreal-engine/horde-server-for-unreal-engine) documentation for information about configuring an OIDC provider.
OIDC is recommended for studios where a central authentication provider is already in use, such as Google Workspaces, Okta, or Azure AD/Entra ID.

After an OIDC provider is configured, a user's claims may be viewed by navigating to `http://{{ server_url }}/account` page in a browser.

### Built-in User Accounts

If you are a smaller studio or don't see the need to use the OpenID Connect method, Horde's built-in user accounts are an option. These accounts are managed by Horde itself and stored in the local database. With the server in anonymous mode, you can set up user accounts via the web UI (Server dropdown in the top right). Configure these with at least one administrator user and set `AuthMethod` to `Horde`.

## Access Control Lists

**Access control lists (ACLs)** control access to entities in Horde. Each item in the list grants the ability to perform certain actions to any users with specific OIDC claims. Each claim is a key/value pair returned by the OIDC provider or synthesized by Horde at login.
See [ACL Actions](/documentation/en-us/unreal-engine/horde-schema-for-unreal-engine#aclactions) for a complete list of actions available.

Many objects that users can query or manipulate have an attached ACL within a hierarchy of other ACL-controlled objects. A stream is part of a project, for example. Users can be granted entitlements to view that specific Perforce stream (via the ACL on that stream's configuration), for all streams within the project (via the ACL on the project's configuration), or for all streams on the server (via the ACL on the global configuration).

### Administrators

Admin users are permitted to perform any operations regardless of any configured ACLs. Users are granted admin status if they contain a particular claim configured in the server's [Server.json](/documentation/en-us/unreal-engine/horde-settings-for-unreal-engine#serversettings) file via the `AdminClaimType` and `AdminClaimValue` properties.

### Synthesized Claims

Horde adds several claims to the configured claims returned through the OIDC provider:

| Name | Description |
| --- | --- |
| `http://epicgames.com/ue/horde/user` | Real name of the user. This is extracted from claims returned by the OIDC provider according to the `OidcClaimNameMapping` [server setting](/documentation/en-us/unreal-engine/horde-server-for-unreal-engine). |
| `http://epicgames.com/ue/horde/user-id-v3` | Identifier for the user. This is a 24-character unique ID assigned by Horde. |
| `http://epicgames.com/ue/horde/agent` | Identifies a particular agent (with the value being the agent ID). |
| `http://epicgames.com/ue/horde/perforce-user` | Gives the Perforce username corresponding to the user |

### Example

The following config fragment declares an ACL which:

* Grants the `ViewJob` and `CreateJob` entitlement to a user by the name of `Tim Sweeney`.
* Grants the `ViewJob` entitlement to any users with the role claim of `app-horde-users`.

  ```
        "acl":
        {
            "entries": [
                {
                    "claim": {
                        "type": "http://epicgames.com/ue/horde/user",
                        "value": "Tim Sweeney"
                    },
                    "actions": [
                        "ViewJob",
                        "CreateJob"
                    ]
                },
                {
                    "claim": {
                        "type": "http://schemas.microsoft.com/ws/2008/06/identity/claims/role",
                        "value": "app-horde-viewers"
                    },
                    "actions": [
                        "ViewJob"
                    ]
                }
            ],
            "inherit": true
        }
  Copy full snippet
  ```

* [horde](https://dev.epicgames.com/community/search?query=horde)
* [bronze](https://dev.epicgames.com/community/search?query=bronze)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Authentication](/documentation/en-us/unreal-engine/horde-permissions-for-unreal-engine?application_version=5.7#authentication)
* [Anonymous](/documentation/en-us/unreal-engine/horde-permissions-for-unreal-engine?application_version=5.7#anonymous)
* [OpenID Connect](/documentation/en-us/unreal-engine/horde-permissions-for-unreal-engine?application_version=5.7#openidconnect)
* [Built-in User Accounts](/documentation/en-us/unreal-engine/horde-permissions-for-unreal-engine?application_version=5.7#built-inuseraccounts)
* [Access Control Lists](/documentation/en-us/unreal-engine/horde-permissions-for-unreal-engine?application_version=5.7#accesscontrollists)
* [Administrators](/documentation/en-us/unreal-engine/horde-permissions-for-unreal-engine?application_version=5.7#administrators)
* [Synthesized Claims](/documentation/en-us/unreal-engine/horde-permissions-for-unreal-engine?application_version=5.7#synthesizedclaims)
* [Example](/documentation/en-us/unreal-engine/horde-permissions-for-unreal-engine?application_version=5.7#example)
