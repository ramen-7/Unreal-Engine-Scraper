<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/accessing-logs-and-crash-reports-on-ios-and-tvos-in-unreal-engine?application_version=5.7 -->

# Accessing Logs and Crash Reports on iOS and tvOS

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
5. [Mobile Development](/documentation/en-us/unreal-engine/getting-started-with-mobile-development-in-unreal-engine "Mobile Development")
6. [Debugging and Optimization for Mobile](/documentation/en-us/unreal-engine/debugging-and-optimization-for-mobile-in-unreal-engine "Debugging and Optimization for Mobile")
7. [iOS and tvOS Debugging and Optimization](/documentation/en-us/unreal-engine/ios-and-tvos-debugging-and-optimization-in-unreal-engine "iOS and tvOS Debugging and Optimization")
8. Accessing Logs and Crash Reports on iOS and tvOS

# Accessing Logs and Crash Reports on iOS and tvOS

Download and read iOS and tvOS logs and crash reports either directly from device or from TestFlight.

![Accessing Logs and Crash Reports on iOS and tvOS](https://dev.epicgames.com/community/api/documentation/image/e52e48f1-540d-4860-8868-3da7902bf6ce?resizing_type=fill&width=1920&height=335)

 On this page

### Accessing iOS and tvOS Logs and Crash Reports

iOS applications built with Unreal Engine produce crash logs that developers can use to debug their projects and fix code issues. However, for security reasons, the debug symbols are not available with the crash logs themselves. You will see keys and numbers, but to see names of functions or information about variables in a human-readable format, you need to match your logs to a database of symbols for your project.

There are several processes for re-symbolicating your logs and reading them, depending on how you delivered your debug builds to devices. **TestFlight** is Apple's application for delivering test builds to a large number of possible devices, and it provides logs from those builds to developers. You can also obtain logs directly through USB debugging.

You need a Mac and Xcode to read logs for iOS projects. Other operating systems and IDEs will not work with the workflows on this page.

## 1. Accessing Logs Directly from Device

If you are debugging directly through USB or Ethernet, follow these steps to view a symbolicated crash log:

1. In Xcode, from the main menu, select **Window** > **Devices and Simulators**.
2. Click the iPhone you want to obtain crash data from, then click **View Device Logs**.
3. Control-click the log you want to read, then click **Re-Symbolicate and export Log**.

This will provide a human-readable log with debug symbols.

## 2. Accessing Logs from TestFlight

When an application delivered through TestFlight crashes, it produces an **XCrashPoint** file containing crash information. To read these files, you need a `.dSYM` file with debug symbols for your project, then you need to extract the crash report and re-symbolicate it.

For specific information about deploying applications through TestFlight and accessing logs, refer to [Apple's documentation on TestFlight](https://developer.apple.com/testflight/). This section will provide information about how to symbolicate them once you have obtained them.

### Generating a .dSYM File During Packaging

To generate a `.dSYM` file when you package your project, follow these steps:

1. Open **Unreal Editor**.
2. Open your **Project Settings**, then navigate to **Platforms** > **iOS** > **Build**.
3. Enable **Generate dSYM file for code debugging and profiling**.

   [![Check the Generate dySM file option](https://dev.epicgames.com/community/api/documentation/image/5501bf54-d2fa-4d31-a78a-7adc2502402d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5501bf54-d2fa-4d31-a78a-7adc2502402d?resizing_type=fit)
4. Package your project.

The `.dSYM` file for your project will appear in your project folder, under `/Binaries/iOS`.

`.dSYM` files have a timestamp showing when they were packaged. Take note of this information so you can match `.dSYM` files to the correct build.

### Generating a .dSYSM File From a Command Line

To generate .dSYM file using UAT, execute the RunUAT script in a command line with the **GenerateDYSM** command. Specify the following parameters:

| Parameter | Optional | Valid Values | Description |
| --- | --- | --- | --- |
| -Platform=[Target Platform] | Yes | IOS, TVOS, Mac | Specifies target platform. Defaults to current platform if unspecified. |
| -Target=[Project Name] | Yes | The name of your project. | Specifies which project you want to use. Defaults to current project if unspecified. |
| -Config=[Build Configuration] | Yes | Debug, DebugGame, Development, Test, Shipping | Target build configuration. Defaults to Development if unspecified. |
| -Architecture=[Architecture Type] | No | x64, arm64, x64+arm64] | Target device architecture. |
| -flat | Yes | Does not take inputs. | If specified, the .dSYMs will be flat files that are easier to copy between computers or servers. |

For example, the following command will generate .dSYM files for iOS devices using the arm64 architecture:

C++

```
```RunUAT.command GenerateDYSM -project=MyProject -platform=Mac -target=EngineTestEditor -config=Test -architecutre=arm64```
```

```RunUAT.command GenerateDYSM -project=MyProject -platform=Mac -target=EngineTestEditor -config=Test -architecutre=arm64```

Copy full snippet(1 line long)

### Extracting the Crash Report and Re-Symbolicating

To obtain your crash report and re-symbolicate it so that you can read it, follow these steps:

1. Obtain an `XCrashPoint`file from TestFlight. You can use the following command line input to do this.

   C++

   ```
   export PATH="/Applications/Xcode.app/Contents/SharedFrameworks/DVTFoundation.framework/Versions/A/Resources:$PATH"
   ```

   export PATH=&quot;/Applications/Xcode.app/Contents/SharedFrameworks/DVTFoundation.framework/Versions/A/Resources:$PATH&quot;

   Copy full snippet(1 line long)
2. Control-click on the `.XCrashPoint` file, then click **Extract `.crash` file**. You can also export this information using the following command line input:

   C++

   ```
   export PATH="/Applications/Xcode.app/Contents/SharedFrameworks/DVTFoundation.framework/Versions/A/Resources:$PATH"
   ```

   export PATH=&quot;/Applications/Xcode.app/Contents/SharedFrameworks/DVTFoundation.framework/Versions/A/Resources:$PATH&quot;

   Copy full snippet(1 line long)
3. Open XCode, then look at the **terminal**. Use it to navigate to your Xcode `.package`.
4. Use the symbolicatecrash tool by running the following command line:

   C++

   ```
   export DEVELOPER_DIR="/Applications/Xcode.app/Contents/Developer" cp -i /Applications/Xcode.app/Contents/SharedFrameworks/DVTFoundation.framework/Versions/A/Resources/symbolicatecrash ././symbolicatecrash unsymbolicated.crash symbols.dSYM > symbolicated.crash
   ```

   export DEVELOPER\_DIR=&quot;/Applications/Xcode.app/Contents/Developer&quot; cp -i /Applications/Xcode.app/Contents/SharedFrameworks/DVTFoundation.framework/Versions/A/Resources/symbolicatecrash ././symbolicatecrash unsymbolicated.crash symbols.dSYM &gt; symbolicated.crash

   Copy full snippet(1 line long)

The above instructions use default directories. Use the locations of your `.crash` and `.dSYM` files when you run these command lines.

Xcode will then provide a crash log with function names and variables visible.

* [testing](https://dev.epicgames.com/community/search?query=testing)
* [debugging](https://dev.epicgames.com/community/search?query=debugging)
* [ios](https://dev.epicgames.com/community/search?query=ios)
* [tvos](https://dev.epicgames.com/community/search?query=tvos)
* [xcode](https://dev.epicgames.com/community/search?query=xcode)
* [testflight](https://dev.epicgames.com/community/search?query=testflight)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Accessing iOS and tvOS Logs and Crash Reports](/documentation/en-us/unreal-engine/accessing-logs-and-crash-reports-on-ios-and-tvos-in-unreal-engine?application_version=5.7#accessing-i-os-and-tv-os-logs-and-crash-reports)
* [1. Accessing Logs Directly from Device](/documentation/en-us/unreal-engine/accessing-logs-and-crash-reports-on-ios-and-tvos-in-unreal-engine?application_version=5.7#1-accessing-logs-directly-from-device)
* [2. Accessing Logs from TestFlight](/documentation/en-us/unreal-engine/accessing-logs-and-crash-reports-on-ios-and-tvos-in-unreal-engine?application_version=5.7#2-accessing-logs-from-test-flight)
* [Generating a .dSYM File During Packaging](/documentation/en-us/unreal-engine/accessing-logs-and-crash-reports-on-ios-and-tvos-in-unreal-engine?application_version=5.7#generating-a-d-sym-file-during-packaging)
* [Generating a .dSYSM File From a Command Line](/documentation/en-us/unreal-engine/accessing-logs-and-crash-reports-on-ios-and-tvos-in-unreal-engine?application_version=5.7#generating-a-d-sysm-file-from-a-command-line)
* [Extracting the Crash Report and Re-Symbolicating](/documentation/en-us/unreal-engine/accessing-logs-and-crash-reports-on-ios-and-tvos-in-unreal-engine?application_version=5.7#extracting-the-crash-report-and-re-symbolicating)
