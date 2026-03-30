<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/horde-integrations-for-unreal-engine?application_version=5.7 -->

# Horde Integrations

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
7. [Horde Deployment](/documentation/en-us/unreal-engine/horde-deployment-for-unreal-engine "Horde Deployment")
8. Horde Integrations

# Horde Integrations

How to integrate Horde with Perforce and Slack for use with Unreal Engine.

![Horde Integrations](https://dev.epicgames.com/community/api/documentation/image/13153b3a-9ea7-42c7-9017-d4336f3e1447?resizing_type=fill&width=1920&height=335)

 On this page

## Perforce

### General

Horde uses Perforce primarily for CI functionality but also supports reading configuration data directly from a Perforce server (see [Configuration > Orientation](/documentation/en-us/unreal-engine/horde-orientation-for-unreal-engine)).

The Perforce connection to use for reading configuration files is configured alongside the server deployment via the `perforce` property in the server [Server.json](/documentation/en-us/unreal-engine/horde-settings-for-unreal-engine#serversettings) file.

Support for other version control systems may be added in the future.

### Clusters

Epic's Perforce deployment is quite elaborate, and the desire to scale our CI build infrastructure across multiple regions and data centers has resulted in bolstering Horde with a lot of custom functionality for interacting with Perforce edge servers. Horde implements a load balancer for connecting build agents to Perforce servers, for example, which uses health check data provided by server instances to roll over to new server instances when a server reports a problem.

Horde supports the use of multiple independent Perforce installations and load balancing across multiple mirrors within each installation. A collection of Perforce servers that mirror the same data is called a cluster. If desired, you can configure each stream in the CI system to use a different cluster.

Clusters are configured through the `perforceClusters` property in the [globals.json](/documentation/en-us/unreal-engine/horde-schema-for-unreal-engine#globals) config file.

There are several configurables for each cluster:

* `Name`: Used to reference the cluster from a stream in the CI system.
* `Servers`: Each server supports several settings of its own:
  + `ServerAndPort`: The server part may be a DNS entry with multiple records, in which case it will be actively load balanced.
  + `ResolveDns`: If true, the given DNS name is resolved to find a concrete list of servers to be used. This allows IT/infrastructure teams to add and remove servers to a cluster without reconfiguring Horde.
  + `Properties`: Specifies properties that the agent must have to select this server.
  + `HealthCheck`: If true, the Horde server will periodically poll the server for its health on a well-known endpoint. See [Health Checks](/documentation/en-us/unreal-engine/horde-integrations-for-unreal-engine#health-checks) for more information.
* `Credentials`: A list of usernames/passwords/tickets for different accounts on this server. CI jobs can request these credentials.
* `ServiceAccount`: Sets the account username that Horde should use for internal operations, such as querying commits from a stream, submitting on behalf of another user, and so on.
* `CanImpersonate`: Indicates whether Horde should attempt to impersonate other users when submitting changes after a successful preflight-and-submit operation. Typically requires an administrator account.

### Servers with SSL

When the Perforce server uses SSL and the `ssl:` prefix is specified, it is essential to ensure that the server's fingerprint or certificate is trusted. For more information, refer to the [p4 trust](https://www.perforce.com/manuals/cmdref/Content/CmdRef/p4_trust.html) documentation. Depending on the configuration, it may be necessary to explicitly set the `P4TRUST` environment variable, which should point to a valid `p4trust.txt` file. Again, see the P4 documentation for further details.

For example, on Windows, the Horde server runs as a service by default. In this scenario, the default location of the trust file resolves to `%SystemRoot%\System32\config\systemprofile\p4trust.txt`.

### Health Checks

If enabled, health checks for Perforce servers are performed by performing an HTTP `GET` request to `http://{{ PERFORCE_SERVER_URL }}:5000/healthcheck`. The endpoint is expected to return a JSON document with the following structure:

```
{
    "results": [
        {
            "checker": "edge_traffic_lights"
            "output": "green"
        }
    ]
}
Copy full snippet
```

Where valid values for `output` are:

* `green`: Server is healthy.
* `yellow`: Server peformance is degraded.
* `red`: Server is draining existing connections and should not be used.

This functionality is implemented in `PerforceLoadBalancer.GetServerHealthAsync()`.

### P4CONFIG

Horde creates a file called `p4.ini` in a parent directory of workspaces created for CI use, containing the appropriate Perforce server, port, and username.

Running the following command will allow Perforce to automatically detect the correct settings for the workspace in the current directory:

```
p4 set P4CONFIG=p4.ini
Copy full snippet
```

## Slack

Horde uses Slack to:

* broadcast notifications on configuration errors and CI failures.
* provide avatars for users logged in to Horde.

### Manifest

The Horde Slack app can be configured using the following manifest. Note the `{{ SERVER_URL }}` placeholder below.

```
{
    "display_information": {
        "name": "Horde",
        "description": "Allow for interaction with the Horde build system.",
        "background_color": "#000000"
    },
    "features": {
        "bot_user": {
            "display_name": "Horde",
            "always_online": false
        }
    },
    "oauth_config": {
        "scopes": {
            "user": [
                "admin.conversations:write"
            ],
            "bot": [
                "chat:write",
                "chat:write.public",
                "reactions:read",
                "reactions:write",
                "users.profile:read",
                "users:read",
                "users:read.email",
                "channels:manage"
            ]
        }
    },
    "settings": {
        "interactivity": {
            "is_enabled": true,
            "request_url": "{{ SERVER URL }}/api/v1/slack"
        },
        "org_deploy_enabled": true,
        "socket_mode_enabled": true,
        "token_rotation_enabled": false
    }
}
Copy full snippet
```

You can find a suitable application icon in the source tree under `Horde/Horde.Server/Slack`, along with icons that you can use for build health notification prompts.

Horde requires two tokens to be configured in the server's [Server.json](/documentation/en-us/unreal-engine/horde-settings-for-unreal-engine#serversettings) file to operate fully:

* `SlackToken`: Bot token used to post messages to channels (has an `xoxb-` prefix). The Horde bot user must also be explicitly invited to any channels where it needs to post.
* `SlackSocketToken`: Token used to open a WebSocket connection to Slack and provide interactive functionality (has an `xapp-` prefix), responding to button presses, and so on.

### User Mapping

Horde users are mapped to Slack users by correlating the email address in the user's [OIDC profile](/documentation/en-us/unreal-engine/horde-server-for-unreal-engine) with their Slack user profile. Horde will use avatars configured through Slack in the dashboard for any successfully mapped email address.

* [horde](https://dev.epicgames.com/community/search?query=horde)
* [bronze](https://dev.epicgames.com/community/search?query=bronze)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Perforce](/documentation/en-us/unreal-engine/horde-integrations-for-unreal-engine?application_version=5.7#perforce)
* [General](/documentation/en-us/unreal-engine/horde-integrations-for-unreal-engine?application_version=5.7#general)
* [Clusters](/documentation/en-us/unreal-engine/horde-integrations-for-unreal-engine?application_version=5.7#clusters)
* [Servers with SSL](/documentation/en-us/unreal-engine/horde-integrations-for-unreal-engine?application_version=5.7#serverswithssl)
* [Health Checks](/documentation/en-us/unreal-engine/horde-integrations-for-unreal-engine?application_version=5.7#healthchecks)
* [P4CONFIG](/documentation/en-us/unreal-engine/horde-integrations-for-unreal-engine?application_version=5.7#p4config)
* [Slack](/documentation/en-us/unreal-engine/horde-integrations-for-unreal-engine?application_version=5.7#slack)
* [Manifest](/documentation/en-us/unreal-engine/horde-integrations-for-unreal-engine?application_version=5.7#manifest)
* [User Mapping](/documentation/en-us/unreal-engine/horde-integrations-for-unreal-engine?application_version=5.7#usermapping)
