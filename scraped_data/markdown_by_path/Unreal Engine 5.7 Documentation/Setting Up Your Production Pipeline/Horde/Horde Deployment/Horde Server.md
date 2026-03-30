<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/horde-server-for-unreal-engine?application_version=5.7 -->

# Horde Server

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
8. Horde Server

# Horde Server

An overview of Horde Server for use with Unreal Engine.

![Horde Server](https://dev.epicgames.com/community/api/documentation/image/8703e507-b207-48aa-8d00-098e3f8117ca?resizing_type=fill&width=1920&height=335)

 On this page

## Installation

### MSI Installer (Windows)

Windows builds of MongoDB and Redis are included in the installer and launched by Horde at startup (Horde will also close them when it terminates). This installation is fine for small-scale installations and testing Horde, though hosting databases separately would be preferred in production scenarios.

### Docker (Linux)

Images for hosting Horde through Docker are available through the Epic Games organization on [GitHub](https://www.unrealengine.com/en-US/ue-on-github). Note that you must be signed into GitHub with an account associated with an Epic Games account to follow these links.

* [Horde Server](https://github.com/orgs/EpicGames/packages/container/package/horde-server)

To download an image, first create a GitHub personal access token (PAT) from the developer section of your account settings page and pass it as the password to:

```
docker login ghcr.io
Copy full snippet
```

To download the image:

```
docker pull ghcr.io/epicgames/horde-server:latest 
Copy full snippet
```

Note that in this form, an external MongoDB and Redis instance must be configured through a configuration file or environment variable (see below).

Running multiple Horde servers behind a load balancer does not require explicit configuration as long as each server points to the same MongoDB and Redis instance.

Using Docker containers on Linux is [Epic's preferred way of running Horde](/documentation/en-us/unreal-engine/horde-deployment-for-unreal-engine).

### Docker Compose (Linux)

[Docker Compose](https://docs.docker.com/compose/) simplifies the setup of a Docker-based installation by providing a preconfigured group of Docker containers, which includes instances of MongoDB and Redis.

Similar to the MSI installer, this method is suitable for testing Horde or deploying it in small-scale environments. To access the prebuilt images, refer to the Docker section above. The necessary Docker Compose configuration can be found within the `Engine/Source/Programs/Horde.Server/docker-compose.yml` file.

From the same directory, start the containers with:

```
docker compose up
Copy full snippet
```

For additional guidance, see the comments within the YAML file.

### Homebrew (Mac)

We don't provide any prebuilt binaries for running the server on Mac, though it's relatively straightforward to install all the prerequisites using [Homebrew](https://brew.sh/).

1. Install the .NET 8 SDK.

   ```
        brew install dotnet-sdk
   Copy full snippet
   ```
2. Install MongoDB.

   ```
        brew tap mongodb/brew
        brew update
        brew install mongodb-community
        brew services start mongodb-community
   Copy full snippet
   ```
3. Install Redis.

   ```
        brew install redis
        brew services start redis
   Copy full snippet
   ```
4. Launch Horde. The environment variables below use standard ASP.NET syntax; you can modify values in `server.json` instead if you prefer.

   ```
        export Horde__MongoConnectionString=mongodb://localhost:27017
        export Horde__HttpPort=37107
        export Horde__Http2Port=37109
   		
        cd Engine/Source/Programs/Horde/Horde.Server
        dotnet run
   Copy full snippet
   ```

### Building from Source

The source code for the Horde server is located under `Engine/Source/Programs/Horde/Horde.Server/...`.

You can build and run the server from Visual Studio using the solution at `Engine/Source/Programs/Horde/Horde.sln`, or from the command line via the `dotnet build` or `dotnet publish` commands.

Docker images can be built through the BuildGraph script at `Engine/Source/Programs/Horde/BuildHorde.xml`, using the Dockerfile in `Engine/Source/Programs/Horde.Server/Dockerfile`.

Using the BuildGraph script is recommended over running the Dockerfile directly because it stages the relevant files to a temporary directory before running `docker build`, which prevents the Docker daemon from copying the entire UE source tree to the containerized environment before building.

The command line for building Docker images using BuildGraph is:

```
RunUAT.bat BuildGraph -Script=Engine/Source/Programs/Horde/BuildHorde.xml -Target="Build HordeServer"
Copy full snippet
```

The Windows installer can be built from the same BuildGraph script with a similar command line:

```
RunUAT.bat BuildGraph -Script=Engine/Source/Programs/Horde/BuildHorde.xml -Target="Build Horde Installer"
Copy full snippet
```

## Settings

### General

Server settings are configured through the [`Server.json`](/documentation/en-us/unreal-engine/horde-settings-for-unreal-engine#serversettings) file. On Windows, this file is stored at `C:\ProgramData\Epic\Horde\Server\Server.json`. On other platforms, it is stored in the `Data` folder under the application directory by default. Settings in this file are applied on top of the `appsettings.json` file distributed alongside the server executable.

All Horde-specific settings are stored under the `Horde` top-level key, with middleware and standard .NET settings under other root keys.

As an ASP.NET application, Horde's application configuration supports the following features:

* Individual properties can be overridden through **environment variables** using standard ASP.NET syntax (see [MSDN](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-7.0#naming-of-environment-variables)). For example, the database connection string can be passed in using the `Horde__MongoConnectionString` environment variable.
* The deployment environment can be configured using the ASPNETCORE\_ENVIRONMENT environment variable. Standard values for Horde are `Production`, `Development`, and `Local`.
* A deployment-specific configuration file can be created called `appsettings.{Environment}.json` (e.g. `appsettings.Local.json`), which will be merged with other settings.

Note that the server configuration files (`Server.json`, `appsettings.json`, etc.) differ from the global configuration file (`globals.json`). The server configuration file is deployed alongside the server. It contains deployment/infrastructure settings, whereas the global configuration file can be stored in revision control and updated dynamically during the server's lifetime. See [Config > Orientation](/documentation/en-us/unreal-engine/horde-orientation-for-unreal-engine) for more information.

### MongoDB

The MongoDB connection string can be specified via the `MongoConnectionString` property in the [Server.json](/documentation/en-us/unreal-engine/horde-settings-for-unreal-engine#serversettings) file or the `Horde__MongoConnectionString` environment variable. The connection string should be in standard [MongoDB syntax](https://www.mongodb.com/docs/manual/reference/connection-string/), e.g.:

```
mongodb://username:password@host:27017?replicaSet=rs0&readPreference=primary
Copy full snippet
```

Horde implements many operations as compare-and-swap operations, so it is important that all reads are configured to use the primary database instance using the `readPreference=primary` argument when using a replica set. Using a secondary instance for reads can cause deadlocks because the server gets out-of-date documents in a read-modify-write cycle.

The MongoDB connection can be configured to use a trusted set of certificates via the `MongoPublicCertificate` property. For example, when running on AWS using DocumentDB, this property can be set to use Amazon's [combined certificate bundle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html) by placing the `global-bundle.pem` file into the server's application directory.

### Redis

The Redis server is configured through the RedisConnectionConfig property in the [Server.json](/documentation/en-us/unreal-engine/horde-settings-for-unreal-engine#serversettings) file or via the `Horde__MongoConnectionString` environment variable. This string is formatted as a plain server and port, e.g.:

```
127.0.0.1:6379
Copy full snippet
```

### Ports

By default, Horde is configured to serve data over unencrypted HTTP using port 5000. Agents communicate with the Horde server using gRPC over unencrypted HTTP/2 on port 5002 by default. These settings are echoed to the console during server startup.

A separate port is used for gRPC since Kestrel (the .NET web server) does not support unencrypted HTTP/2 traffic over the same port as HTTP/1 traffic. This separate port for non-TLS HTTP/2 traffic can be useful when putting Horde behind a reverse proxy. If an HTTPS port is configured, all traffic can use that port.

Settings for port usage are defined in [Server.json](/documentation/en-us/unreal-engine/horde-settings-for-unreal-engine#serversettings):

* To disable serving data over HTTP, set the `HttpPort` property to zero.
* To configure the secondary HTTP/2 port used, set the `Http2Port` property (or set it to zero to disable it).

### HTTPS

To serve data over HTTPS, set the `HttpsPort` property in the [Server.json](/documentation/en-us/unreal-engine/horde-settings-for-unreal-engine#serversettings) file.

Configure the certificate for [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-8.0) (the NET Core web server) by setting the default certificate in the same file.

Cross-platform:

```
"Kestrel": {
    "Certificates": {
        "Default": {
            "Path": "C:\\cert\\test.pfx",
            "Password": "my-password"
        }
    }
}
Copy full snippet
```

Windows (using the system certificate store):

```
"Kestrel": {
    "Certificates": {
        "Default":
        {
            "Subject": "my-domain.com",

            // Use the 'Personal' certificate store on the local machine
            "Store": "My",
            "Location": "LocalMachine"
        }
    }
}
Copy full snippet
```



The `Kestrel` object must be added at the root scope of the file, not within the `Horde` object.

Other ways to configure certificates for Kestrel are listed on [MSDN](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel/endpoints?view=aspnetcore-8.0#configure-https).

Both HTTP/1.1 and HTTP/2.0 traffic can be served over the `HttpsPort`. Unencrypted traffic can be disabled by setting `HttpPort` and `Http2Port` to zero.

There are occasions where the server provides links back to itself (the OIDC discovery document used when using Horde's internal account system, for example), and it's important that these URLs match the HTTPS certificate. By default, this URL is derived from the server's reported DNS name, but this can be overridden through the `ServerUrl` property.

To set up a self-signed certificate for testing see [Tutorials > Self Signed Certs](/documentation/en-us/unreal-engine/horde-self-signed-certs-tutorial-for-unreal-engine).

### Monitoring

Horde uses [Serilog](https://serilog.net/) for logging and is configured to generate plain text and JSON log files to the application directory on Linux and the `C:\ProgramData\HordeServer` folder on Windows. Plain text output is written to stdout by default, though Json output can be enabled using the `LogJsonToStdOut` property in [Server.json](/documentation/en-us/unreal-engine/horde-settings-for-unreal-engine#serversettings).

Profiling and telemetry data for the server is routed through [OpenTelemetry](https://opentelemetry.io/). Settings for telemetry capture are [listed here](/documentation/en-us/unreal-engine/horde-settings-for-unreal-engine#opentelemetrysettings).

### RunModes

In order to separate lighter request traffic from heavier background operations, the Horde server can be configured to run in different RunModes. You can configure these via the [RunMode](/documentation/en-us/unreal-engine/horde-settings-for-unreal-engine#serversettings) setting.

### Authentication

Horde supports [OpenID Connect (OIDC)](https://openid.net/developers/how-connect-works/) for authentication using an external identity provider. OIDC is a widely used auth standard, and Okta, AWS, Azure, Google, Facebook, and many others implement identity providers compatible with it.

The [Getting Started > Authentication](/documentation/en-us/unreal-engine/horde-authentication-tutorial-for-unreal-engine) page explains how to configure Horde's internal account system and OIDC provider.

The following settings in [Server.json](/documentation/en-us/unreal-engine/horde-settings-for-unreal-engine#serversettings) are required to configure an external OIDC provider:

* `AuthMethod`: Set this to `OpenIdConnect`.
* `OidcAuthority`: URL of the OIDC authority. You can check the URL specified here is correct by navigating to `{{Url}}/.well-known/openid-configuration` in a browser, which should return the OIDC discovery document.
* `OidcClientId`: Identifies the application (Horde) to the OIDC provider. This is generated by the OIDC provider.
* `OidcClientSecret`: A secret value provided by the OIDC provider to identify the application requesting authorization.

In addition, the following settings can be specified:

* `OidcRequestedScopes`: Specifies the scopes requested from the OIDC provider. Scopes determine the access that Horde requests from the OIDC provider and the claims that will be returned and available for checking against in Horde ACLs. The meaning of these values is specific to your OIDC provider configuration.
* `OidcClaimNameMapping`: Specifies a list of claims to check, in order of preference, when trying to show a user's real name.
* `OidcClaimEmailMapping`: Specifies a list of claims to check, in order of preference, when trying to show a user's email address.
* `OidcClaimHordePerforceUserMapping`: Specifies a list of claims to check, in order of preference, when trying to determine a user's Perforce username.

See [Config > Permissions](/documentation/en-us/unreal-engine/horde-permissions-for-unreal-engine) for other authentication options.

### Reference

For a full list of valid properties in the server configuration file, see [Server.json (Server)](/documentation/en-us/unreal-engine/horde-settings-for-unreal-engine#serversettings).

* [horde](https://dev.epicgames.com/community/search?query=horde)
* [bronze](https://dev.epicgames.com/community/search?query=bronze)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Installation](/documentation/en-us/unreal-engine/horde-server-for-unreal-engine?application_version=5.7#installation)
* [MSI Installer (Windows)](/documentation/en-us/unreal-engine/horde-server-for-unreal-engine?application_version=5.7#msiinstaller(windows))
* [Docker (Linux)](/documentation/en-us/unreal-engine/horde-server-for-unreal-engine?application_version=5.7#docker(linux))
* [Docker Compose (Linux)](/documentation/en-us/unreal-engine/horde-server-for-unreal-engine?application_version=5.7#dockercompose(linux))
* [Homebrew (Mac)](/documentation/en-us/unreal-engine/horde-server-for-unreal-engine?application_version=5.7#homebrew(mac))
* [Building from Source](/documentation/en-us/unreal-engine/horde-server-for-unreal-engine?application_version=5.7#buildingfromsource)
* [Settings](/documentation/en-us/unreal-engine/horde-server-for-unreal-engine?application_version=5.7#settings)
* [General](/documentation/en-us/unreal-engine/horde-server-for-unreal-engine?application_version=5.7#general)
* [MongoDB](/documentation/en-us/unreal-engine/horde-server-for-unreal-engine?application_version=5.7#mongodb)
* [Redis](/documentation/en-us/unreal-engine/horde-server-for-unreal-engine?application_version=5.7#redis)
* [Ports](/documentation/en-us/unreal-engine/horde-server-for-unreal-engine?application_version=5.7#ports)
* [HTTPS](/documentation/en-us/unreal-engine/horde-server-for-unreal-engine?application_version=5.7#https)
* [Monitoring](/documentation/en-us/unreal-engine/horde-server-for-unreal-engine?application_version=5.7#monitoring)
* [RunModes](/documentation/en-us/unreal-engine/horde-server-for-unreal-engine?application_version=5.7#runmodes)
* [Authentication](/documentation/en-us/unreal-engine/horde-server-for-unreal-engine?application_version=5.7#authentication)
* [Reference](/documentation/en-us/unreal-engine/horde-server-for-unreal-engine?application_version=5.7#reference)
