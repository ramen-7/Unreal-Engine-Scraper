<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/remote-control-preset-api-http-reference-for-unreal-engine?application_version=5.7 -->

# Remote Control Preset API HTTP Reference

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
6. [Scripting and Automating the Unreal Editor](/documentation/en-us/unreal-engine/scripting-and-automating-the-unreal-editor "Scripting and Automating the Unreal Editor")
7. [Remote Control](/documentation/en-us/unreal-engine/remote-control-for-unreal-engine "Remote Control")
8. Remote Control Preset API HTTP Reference

# Remote Control Preset API HTTP Reference

Details about the HTTP endpoints offered by the Remote Control API for accessing properties and functions exposed in a Remote Control Preset.

![Remote Control Preset API HTTP Reference](https://dev.epicgames.com/community/api/documentation/image/31c1758b-325e-4b65-b9b7-85fc9518b992?resizing_type=fill&width=1920&height=335)

Learn to use this **Beta** feature, but use caution when shipping with it.

 On this page

This page describes the HTTP endpoints offered by the [Remote Control API](/documentation/en-us/unreal-engine/remote-control-for-unreal-engine) for [Remote Control Presets](/documentation/en-us/unreal-engine/remote-control-presets-and-web-application-for-unreal-engine) and details the format of the message body you need to include when you call each endpoint.

The examples in this page are using the **Blueprint Third-Person** Template. To follow along with the examples, add a **Remote Control Preset** to the project, name it MyPreset, and expose the following properties and functions:

* Directional Light's rotation property, renamed as **Directional Light Rotation**
* Print Text function from the Kismet System Library, with **Print to Log** enabled

![Screenshot of Remote Control Preset with a Directional Light's rotation property and Print Text function exposed](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/92a3682b-4b8f-4d60-9006-20ec853af030/01_remotecontrolpreset1.png)

## GET remote/presets

Use this endpoint to get the list of all available presets. The call returns a JSON payload with information on every **Remote Control Preset** in the project.

### Example

Send the request with an empty request body. A successful request returns a 200 status and a response body with the following properties:

```
	{
		"Presets": [
			{
				"Name": "MyPreset",
				"Path": "/Game/Presets/MyPreset.MyPreset"
			}
		]
	}

Copy full snippet
```

## GET remote/preset/insert\_preset\_name

Use this endpoint to get details on specific presets in your project. In the URL, replace `insert_preset_name` with the name of a **Remote Control Preset** in your project. If the preset is found with the name specified, the call returns a JSON payload with information on the preset.

If a preset cannot be found with the specified name, the call returns a JSON payload with an error message:

```
	{
		"errorMessage": "Preset insert_preset_name could not be found."
	}
Copy full snippet
```

### Example

Sending the request GET `http://localhost:30010/remote/preset/MyPreset` with an empty request body returns a successful request with a 200 status and the following response body:

```
	{
		"Preset": {
			"Name": "MyPreset",
			"Path": "/Game/Presets/MyPreset.MyPreset",
			"Groups": [
				{
					"Name": "Lighting",
					"ExposedProperties": [
						{
							"DisplayName": "Directional Light Rotation",
							"UnderlyingProperty": {
								"Name": "RelativeRotation",
								"Description": "Rotation of the component relative to its parent",
								"Type": "FRotator",
								"ContainerType": "",
								"KeyType": "",
								"Metadata": {
									"ToolTip": "Rotation of the component relative to its parent"
								}
							}
						}
					],
					"ExposedFunctions": []
				},
				{
					"Name": "Print",
					"ExposedProperties": [],
					"ExposedFunctions": [
						{
							"DisplayName": "Print Text (KismetSystemLibrary)",
							"UnderlyingFunction": {
								"Name": "PrintText",
								"Description": "Prints text to the log, and optionally, to the screen\nIf Print To Log is true, it will be visible in the Output Log window.  Otherwise it will be logged only as 'Verbose', so it generally won't show up.\n\n@param       InText                  The text to log out\n@param       bPrintToScreen  Whether or not to print the output to the screen\n@param       bPrintToLog             Whether or not to print the output to the log\n@param       bPrintToConsole Whether or not to print the output to the console\n@param       TextColor               Whether or not to print the output to the console\n@param       Duration                The display duration (if Print to Screen is True). Using negative number will result in loading the duration time from the config.",
								"Arguments": [
									{
										"Name": "WorldContextObject",
										"Description": "",
										"Type": "UObject*",
										"ContainerType": "",
										"KeyType": "",
										"Metadata": {}
									},
									{
										"Name": "InText",
										"Description": "",
										"Type": "FText",
										"ContainerType": "",
										"KeyType": "",
										"Metadata": {}
									},
									{
										"Name": "bPrintToScreen",
										"Description": "",
										"Type": "bool",
										"ContainerType": "",
										"KeyType": "",
										"Metadata": {}
									},
									{
										"Name": "bPrintToLog",
										"Description": "",
										"Type": "bool",
										"ContainerType": "",
										"KeyType": "",
										"Metadata": {}
									},
									{
										"Name": "TextColor",
										"Description": "",
										"Type": "FLinearColor",
										"ContainerType": "",
										"KeyType": "",
										"Metadata": {}
									},
									{
										"Name": "Duration",
										"Description": "",
										"Type": "float",
										"ContainerType": "",
										"KeyType": "",
										"Metadata": {}
									}
								]
							}
						}
					]
				}
			]
		}
	}

Copy full snippet
```

## GET remote/preset/insert\_preset\_name/metadata

Use this endpoint to get all metadata associated with the preset. In the URL, replace `insert_preset_name` with the name of a **Remote Control Preset** in your project. The call returns a JSON payload with the metadata entries for that preset.

### Example

Sending the request GET `http://localhost:30010/remote/preset/MyPreset/metadata` with an empty request body returns a successful request with a 200 status and the following response body:

```
	{
		"Metadata": {}
	}

Copy full snippet
```



Once you add Metadata entries with `PUT remote/preset/insert_preset_name/metadata/insert_metadata_key`, calling this endpoint will include those key-value pairs in this result.

## PUT remote/preset/insert\_preset\_name/metadata/insert\_metadata\_key

Use this endpoint to create or update a metadata key-value pair for the preset. The metadata key can be any name but the request body must include the property **"Value"** in the JSON object; any other property will make the value an empty string. The call returns only the status of the request.

### Example

Send the request `PUT http://localhost:30010/remote/preset/MyPreset/metadata/MyKey` with the following request body:

```
	{
		"Value": "MyValue"
	}

Copy full snippet
```

A successful request returns a 200 status. Verify the key-value pair was created by calling `GET http://localhost:30010/remote/preset/MyPreset/metadata`:

```
	{
		"Metadata": {
			"MyKey": "MyValue"
		}
	}

Copy full snippet
```

## GET remote/preset/insert\_preset\_name/metadata/insert\_metadata\_key>

Use this endpoint to read the value associated with a metadata key. The call returns a JSON payload with the information requested.

### Example

Send the request `GET http://localhost:30010/remote/preset/MyPreset/metadata/MyKey` with an empty request body. A successful request gives a 200 status with the following response body:

```
	{
		"Value": "MyValue"
	}

Copy full snippet
```

## DELETE remote/preset/insert\_preset\_name/metadata/insert\_metadata\_key

Use this endpoint to remove a metadata key-value pair associated with the preset. The call returns only the status of the request.

### Example

Sending the request `DELETE http://localhost:30010/remote/preset/MyPreset/metadata/MyKey` returns a successful request with a 200 status. Verify the key-value pair was deleted by calling `GET http://localhost:30010/remote/preset/MyPreset/metadata`:

```
	{
		"Metadata": {}
	}

Copy full snippet
```

## GET remote/preset/insert\_preset\_name/property/insert\_property\_name

Use this endpoint to read a property exposed in the preset. The call returns a JSON payload with the requested information.

### Example

Send the request `GET http://localhost:30010/remote/preset/MyPreset/property/Directional Light Rotation` with an empty request body.

A successful request returns a 200 status with the following response body:

```
	{
		"PropertyValues": [
			{
				"ObjectPath": "/Game/ThirdPerson/Maps/ThirdPersonMap.ThirdPersonMap:PersistentLevel.DirectionalLight_0.LightComponent0",
				"PropertyValue": {
					"Pitch": -60.779161,
					"Yaw": -14.98808,
					"Roll": 25.555014
				}
			}
		]
	}

Copy full snippet
```

## PUT remote/preset/insert\_preset\_name/property/insert\_property\_name

Use this endpoint to update the value of a property exposed in the preset.

### Example

Send the request `PUT http://localhost:30010/remote/preset/MyPreset/property/Directional Rotation Light` with the following request body:

```
	{
		"PropertyValue": {
			"Pitch": -90,
			"Yaw": 0,
			"Roll": 0
		},
		"GenerateTransaction": true
	}

Copy full snippet
```

A successful request returns a 200 status. Verify the change by looking at the property in the preset:

![image alt text](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/f24e1485-8efe-46df-98ec-7a2cac719f46/02_remotecontrolpreset2.png)

## PUT remote/preset/insert\_preset\_name/function/insert\_function\_name

Use this endpoint to call a function exposed in the preset. The call returns a JSON payload with any return values from the function.

## Example

Send the request `PUT http://localhost:30010/remote/preset/MyPreset/function/Print Text (KismetSystemLibrary)` with the following request body:

```
	{
		"Parameters": {
			"InText": "Hello, World"
		},
		"GenerateTransaction": true
	}

Copy full snippet
```

A successful request returns a 200 status with the following response body and "Hello, World" printed to the Output Log:

```
	{
		"ReturnedValues": [
			{}
		]
	}
Copy full snippet
```

* [beta](https://dev.epicgames.com/community/search?query=beta)
* [remote control](https://dev.epicgames.com/community/search?query=remote%20control)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [GET remote/presets](/documentation/en-us/unreal-engine/remote-control-preset-api-http-reference-for-unreal-engine?application_version=5.7#getremote/presets)
* [Example](/documentation/en-us/unreal-engine/remote-control-preset-api-http-reference-for-unreal-engine?application_version=5.7#example)
* [GET remote/preset/insert\_preset\_name](/documentation/en-us/unreal-engine/remote-control-preset-api-http-reference-for-unreal-engine?application_version=5.7#getremote/preset/insert-preset-name)
* [Example](/documentation/en-us/unreal-engine/remote-control-preset-api-http-reference-for-unreal-engine?application_version=5.7#example-2)
* [GET remote/preset/insert\_preset\_name/metadata](/documentation/en-us/unreal-engine/remote-control-preset-api-http-reference-for-unreal-engine?application_version=5.7#getremote/preset/insert-preset-name/metadata)
* [Example](/documentation/en-us/unreal-engine/remote-control-preset-api-http-reference-for-unreal-engine?application_version=5.7#example-3)
* [PUT remote/preset/insert\_preset\_name/metadata/insert\_metadata\_key](/documentation/en-us/unreal-engine/remote-control-preset-api-http-reference-for-unreal-engine?application_version=5.7#putremote/preset/insert-preset-name/metadata/insert-metadata-key)
* [Example](/documentation/en-us/unreal-engine/remote-control-preset-api-http-reference-for-unreal-engine?application_version=5.7#example-4)
* [GET remote/preset/insert\_preset\_name/metadata/insert\_metadata\_key>](/documentation/en-us/unreal-engine/remote-control-preset-api-http-reference-for-unreal-engine?application_version=5.7#getremote/preset/insert-preset-name/metadata/insert-metadata-key%3E)
* [Example](/documentation/en-us/unreal-engine/remote-control-preset-api-http-reference-for-unreal-engine?application_version=5.7#example-5)
* [DELETE remote/preset/insert\_preset\_name/metadata/insert\_metadata\_key](/documentation/en-us/unreal-engine/remote-control-preset-api-http-reference-for-unreal-engine?application_version=5.7#deleteremote/preset/insert-preset-name/metadata/insert-metadata-key)
* [Example](/documentation/en-us/unreal-engine/remote-control-preset-api-http-reference-for-unreal-engine?application_version=5.7#example-6)
* [GET remote/preset/insert\_preset\_name/property/insert\_property\_name](/documentation/en-us/unreal-engine/remote-control-preset-api-http-reference-for-unreal-engine?application_version=5.7#getremote/preset/insert-preset-name/property/insert-property-name)
* [Example](/documentation/en-us/unreal-engine/remote-control-preset-api-http-reference-for-unreal-engine?application_version=5.7#example-7)
* [PUT remote/preset/insert\_preset\_name/property/insert\_property\_name](/documentation/en-us/unreal-engine/remote-control-preset-api-http-reference-for-unreal-engine?application_version=5.7#putremote/preset/insert-preset-name/property/insert-property-name)
* [Example](/documentation/en-us/unreal-engine/remote-control-preset-api-http-reference-for-unreal-engine?application_version=5.7#example-8)
* [PUT remote/preset/insert\_preset\_name/function/insert\_function\_name](/documentation/en-us/unreal-engine/remote-control-preset-api-http-reference-for-unreal-engine?application_version=5.7#putremote/preset/insert-preset-name/function/insert-function-name)
* [Example](/documentation/en-us/unreal-engine/remote-control-preset-api-http-reference-for-unreal-engine?application_version=5.7#example-9)
