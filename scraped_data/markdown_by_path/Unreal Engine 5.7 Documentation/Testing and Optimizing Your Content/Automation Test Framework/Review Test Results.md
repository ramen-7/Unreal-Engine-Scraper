<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/review-test-results-in-unreal-engine?application_version=5.7 -->

# Review Test Results

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
5. [Testing and Optimizing Your Content](/documentation/en-us/unreal-engine/testing-and-optimizing-your-content "Testing and Optimizing Your Content")
6. [Automation Test Framework](/documentation/en-us/unreal-engine/automation-test-framework-in-unreal-engine "Automation Test Framework")
7. Review Test Results

# Review Test Results

Learn how to read test reports.

![Review Test Results](https://dev.epicgames.com/community/api/documentation/image/d349ce82-1943-4faa-9c43-5e53f3b722f0?resizing_type=fill&width=1920&height=335)

 On this page

There are three different test report formats you can review:

* Log File
* JSON
* HTML

## Log File

By default, the Automation Test Framework will log events and the status of tests.

The patterns are:

* `Test Started. Name={<short name>} Path={<full name>}`
* `Test Completed. Result={<status>}. Name={<short name>} Path={<full name>}`
* `BeginEvents: <test full name> (... events caught during the test) EndEvents: <test full name>`
* `**** TEST COMPLETE. EXIT CODE: <exit code number> ****`

An exit code of 0 means no test failure.

## JSON

The command line argument `-ReportExportPath="<output path>"` stores the report in a `.json` file at the target path.

The file includes the test run's details, including:

* all events raised,
* durations of each test,
* device details.

### Example

```
{
  "devices": [
    {
      "deviceName": "00-00-000-00",
      "instance": "878B6A854613D3B6A69CDEAFBA1C5DBA",
      "platform": "WindowsEditor",
      "oSVersion": "Windows Server 2022 (21H2) [10.0.20348.524] ",
      "model": "Default",
      "gPU": "Microsoft Basic Display Adapter",
      "cPUModel": "Intel(R) Xeon(R) Platinum 8259CL CPU @ 2.50GHz",
      "rAMInGB": 127,
      "renderMode": "D3D11_SM5",
      "rHI": "DirectX 11",
      "appInstanceLog": ""
    }
  ],
  "reportCreatedOn": "2000.01.01-12.00.00",
  "succeeded": 1,
  "succeededWithWarnings": 0,
  "failed": 0,
  "notRun": 0,
  "inProcess": 0,
  "totalDuration": 0.3,
  "comparisonExported": false,
  "comparisonExportDirectory": "",
  "tests": [
    {
      "testDisplayName": "Test1",
      "fullTestPath": "Project.Functional Tests.SomeGroup.Test1",
      "state": "Skipped",
      "deviceInstance": [
        "878B6A854613D3B6A69CDEAFBA1C5DBA"
      ],
      "duration": 0,
      "dateTime": "2000.01.01-12.00.00",
      "entries": [
        {
          "event": {
            "type": "Info",
            "message": "Skipping test: Tests for review [config]",
            "context": "",
            "artifact": "00000000000000000000000000000000"
          },
          "filename": "",
          "lineNumber": -1,
          "timestamp": "2000.01.01-12.00.00"
        }
      ],
      "warnings": 0,
      "errors": 0,
      "artifacts": []
    },
    {
      "testDisplayName": "Test2",
      "fullTestPath": "Project.Functional Tests.SomeGroup.Test2",
      "state": "Success",
      "deviceInstance": [
        "878B6A854613D3B6A69CDEAFBA1C5DBA"
      ],
      "duration": 0.3,
      "dateTime": "2000.01.01-12.00.00",
      "entries": [],
      "warnings": 0,
      "errors": 0,
      "artifacts": []
    }
  ]
}
Copy full snippet
```

## HTML

See [Setting Up an Automation Test Report Server](/documentation/en-us/unreal-engine/setting-up-an-automation-test-report-server) for more information on HTML reports.

* [testing](https://dev.epicgames.com/community/search?query=testing)
* [automation test framework](https://dev.epicgames.com/community/search?query=automation%20test%20framework)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Log File](/documentation/en-us/unreal-engine/review-test-results-in-unreal-engine?application_version=5.7#logfile)
* [JSON](/documentation/en-us/unreal-engine/review-test-results-in-unreal-engine?application_version=5.7#json)
* [Example](/documentation/en-us/unreal-engine/review-test-results-in-unreal-engine?application_version=5.7#example)
* [HTML](/documentation/en-us/unreal-engine/review-test-results-in-unreal-engine?application_version=5.7#html)
