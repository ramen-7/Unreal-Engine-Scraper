<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/horde-secrets-for-unreal-engine?application_version=5.7 -->

# Horde Secrets

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
8. Horde Secrets

# Horde Secrets

An overview of Horde Secrets.

![Horde Secrets](https://dev.epicgames.com/community/api/documentation/image/0a821363-f753-4ffe-807b-41ea64e9b4d6?resizing_type=fill&width=1920&height=335)

 On this page

Horde implements an API for retrieving secrets that can be stored in its own configuration file or obtained from an external source. Marshalling data through Horde allows access to be controlled using Horde's permissions model, and for automated processes to impersonate the user that requested them.

At the moment, Horde only supports the AWS Parameter Store as an external secret provider out of the box, though other implementations can be added through the `ISecretProvider` interface.

## Configuring Secrets

Secrets are defined in the `secrets` list of the [`globals.json`](/documentation/en-us/unreal-engine/horde-schema-for-unreal-engine#globals) file. Each [entry](/documentation/en-us/unreal-engine/horde-schema-for-unreal-engine#secretconfig) includes an identifier for the secret (`id`), a set of key valuepairs (`data`) and an [ACL](/documentation/en-us/unreal-engine/horde-permissions-for-unreal-engine) controlling who can access it.

Additional keys and values may be merged from external providers by adding entries to the `sources` array. Each entry here contains the `name` of the provider to obtain the secret from, and a `path` used to locate the secret in a provider-specific syntax.

Secrets from external providers may take two forms, determined by the `format` property.

* `text` secrets are simple string values which are added to the secret's set of key/value pairs using the specified `key` property.
* `json` secrets are parsed as JSON objects and merged into the secret's key/value pairs using property names as keys.

An example secret may be configured as follows:

```
"secrets": [
    {
        "id": "horde-secrets",

        // Some hard-coded property values        
        "data": {
            "aws-region": "us-east-1"
        },

        // Some values read from the AWS parameter store
        "sources": [

            // Read a single secret from the AWS parameter store and assign it to "aws-secret-access-key"
            {
                "provider": "AwsParameterStore",
                "key": "aws-secret-access-key",
                "path": "name-of-secret-in-parameter-store"
            },

            // Read a JSON object from the AWS parameter store and merge all the key/value pairs into this secret.
            {
                "provider": "AwsParameterStore",
                "format": "json",
                "path": "name-of-secret-in-parameter-store"
            },
        ],

        // Only allow Horde agents to access this
        "acl": {
            "entries": [
                {
                    "claim": {
                        "type": "http://epicgames.com/ue/horde/role",
                        "value": "agent"
                    },
                    "actions": [
                        "ViewSecret"
                    ]
                }
            ]
        }
    }
]
Copy full snippet
```

Secrets are queried from the external provider when requested by a user, and are not cached by Horde.

## Using Secrets

The most common use case for secrets is during build automation pipelines. In this scenario, the Horde Server URL and credentials are taken from environment variables injected automatically by the Horde Agent, and allow the pipeline to request secrets on behalf of the user starting the job with little additional configuration.

There are three common ways to use secrets:

### 1. Using the Horde-GetSecrets BuildGraph Task

This task takes a file as a parameter, and will read it in, expand any secrets in the form {{ secret-name.property }} with their values from Horde, and write it back out again. Rather than updating an existing file, you can also put the template in a BuildGraph property and expand that instead, as follows:

```
<Property Name="AwsEnvironmentText" Multiline="true">
    AWS_REGION={{horde-secrets.aws-region}}
    AWS_ACCESS_KEY_ID={{horde-secrets.aws-access-key-id}}
    AWS_SECRET_ACCESS_KEY={{horde-secrets.aws-secret-access-key}}
</Property>
<Horde-GetSecrets File="credentials.txt" Text="$(AwsEnvironmentText)"/>
Copy full snippet
```

### 2. Using the Horde-SetSecretEnvVar BuildGraph Task

This task sets an environment variable to the value of a secret at runtime. Environment variables are inherited by child processes but not set at the system level, so the environment variable will contain that secret until the end of the current step.

```
<Horde-SetSecretEnvVar Name="AWS_SECRET_ACCESS_KEY" Secret="horde-secrets.aws-secret-access-key"/>
Copy full snippet
```

### 3. Using the Horde API

The HTTP secrets endpoint is listed in Horde's API documentation, and `AutomationTool` includes the following utility methods for querying them at runtime:

```
IReadOnlyDictionary<string, string> secret = await CommandUtils.GetHordeSecretAsync(new SecretId("my-secret-name"));
Copy full snippet
```

```
string propertyValue = await CommandUtils.GetHordeSecretAsync(new SecretId("my-secret-name"), "propertyName")
Copy full snippet
```

* [horde](https://dev.epicgames.com/community/search?query=horde)
* [bronze](https://dev.epicgames.com/community/search?query=bronze)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Configuring Secrets](/documentation/en-us/unreal-engine/horde-secrets-for-unreal-engine?application_version=5.7#configuringsecrets)
* [Using Secrets](/documentation/en-us/unreal-engine/horde-secrets-for-unreal-engine?application_version=5.7#usingsecrets)
* [1. Using the Horde-GetSecrets BuildGraph Task](/documentation/en-us/unreal-engine/horde-secrets-for-unreal-engine?application_version=5.7#1usingthehorde-getsecretsbuildgraphtask)
* [2. Using the Horde-SetSecretEnvVar BuildGraph Task](/documentation/en-us/unreal-engine/horde-secrets-for-unreal-engine?application_version=5.7#2usingthehorde-setsecretenvvarbuildgraphtask)
* [3. Using the Horde API](/documentation/en-us/unreal-engine/horde-secrets-for-unreal-engine?application_version=5.7#3usingthehordeapi)
