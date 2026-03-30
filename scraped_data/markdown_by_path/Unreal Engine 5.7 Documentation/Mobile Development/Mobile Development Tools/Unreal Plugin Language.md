<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/using-the-unreal-plugin-language-for-mobile-projects-in-unreal-engine?application_version=5.7 -->

# Unreal Plugin Language

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
6. [Mobile Development Tools](/documentation/en-us/unreal-engine/development-tools-for-mobile-applications "Mobile Development Tools")
7. Unreal Plugin Language

# Unreal Plugin Language

UPL is a simple XML-based language for manipulating XML and returning strings.

![Unreal Plugin Language](https://dev.epicgames.com/community/api/documentation/image/de9b3ceb-5007-4c0f-b1c7-14a02cd7b2d7?resizing_type=fill&width=1920&height=335)

 On this page

**Unreal Plugin Language** (UPL) is a simple XML-based language for manipulating XML and returning strings. It contains an section which is evaluated once per architecture before any other sections. The state is maintained and carried forward to the next section evaluated so the order the sections are executed matters. While UPL is a general system for modifying and querying XML it is specifically used to allow plug-ins to effect the global configuration of the package that they are a part of. For example, this allows a plug-in to modify an Android APK AndroidManfiest.xml file or an IOS IPA plist file. UBT will also query a plug-in's UPL xml file for strings to be included in files that must be common to the package such as some .java files on Android.

## Enable Tracing

If you need to see the instructions executed in your plugin context add the following to enable tracing:

```
	<trace enable="true"/>
Copy full snippet
```

After this instruction all the nodes actually executed in your context will be written to the log until you do a `<trace enable="false"></trace>`. You can also get a dump of all the variables in your context with this command:

```
	<dumpvars/>
Copy full snippet
```

## Variable Types

Bool, Int, and String variable types are supported. Any attribute can reference a variable and will be replaced with the string equivalent before evaluation using this syntax:

```
	$B(name) = boolean variable "name"'s value
	$I(name) = integer variable "name"'s value
	$S(name) = string variable "name"'s value
	$E(name) = element variable "name"'s value
Copy full snippet
```

The following variables are initialized automatically:

```
	$S(Output) = the output returned for evaluating the section (initialized to Input)
	$S(Architecture) = target architecture (armeabi-armv7a, arm64-v8a, x86, x86_64)
	$S(PluginDir) = directory the XML file was loaded from
	$S(EngineDir) = engine directory
	$S(BuildDir) = project's platform appropriate build directory (within the Intermediate folder)
	$S(Configuration) = configuration type (Debug, DebugGame, Development, Test, Shipping)
	$B(Distribution) = true if distribution build
Copy full snippet
```



With the exception of the above variables, all are in the context of the plugin to prevent namespace collision; trying to set a new value to any of the above, with the exception of Output, will only affect the current context.

## Variable Manipulation

The following nodes allow manipulation of variables:

```
	<setBool result="" value=""/>
	<setInt result="" value=""/>
	<setString result="" value=""/>
	<setElement result="" value=""/>
	<setElement result="" value="" text=""/>
	<setElement result="" xml=""/>
	<setElement> with value creates an empty XML element with the tag set to value.
	<setElement> with value and text creates an XML element with tag set to value of unparsed text.
	<setElement> with xml will parse the XML provided.  Remember to escape any special characters!

Copy full snippet
```

Variables can also be set from a property in an ini file:

```
	<setBoolFromProperty result="" ini="" section="" property="" default=""/>
	<setBoolFromPropertyContains result="" ini="" section="" property="" default="" contains=""/>
	<setIntFromProperty result="" ini="" section="" property="" default=""/>
	<setStringFromProperty result="" ini="" section="" property="" default=""/>
Copy full snippet
```

Strings can also be set from an environment variable using the `<setStringFromEnvVar>` node. The environment variable must be specified as the '**value**' attribute and wrapped in a pair of '**%**' characters.

```
	<setStringFromEnvVar result="" value=""/>
Copy full snippet
```

You can also check if a specific environment variable is defined (again, wrapped in '%' characters):

```
	<setBoolEnvVarDefined result="" value=""/>
Copy full snippet
```

A general example for using environment variable nodes:

```
	<setBoolEnvVarDefined result="bHasNDK" value="%NDKROOT%"/>
	<setStringFromEnvVar result="NDKPath" value="%NDKROOT%"/>
Copy full snippet
```

Boolean variables can also be set to the result of applying operators:

```
	<setBoolNot result="" source=""/>
	<setBoolAnd result="" arg1="" arg2=""/>
	<setBoolOr result="" arg1="" arg2=""/>
	<setBoolIsEqual result="" arg1="" arg2=""/>
	<setBoolIsLess result="" arg1="" arg2=""/>
	<setBoolIsLessEqual result="" arg1="" arg2=""/>
	<setBoolIsGreater result="" arg1="" arg2=""/>
	<setBoolIsGreaterEqual result="" arg1="" arg2=""/>
	<setBoolFromPropertyContains result="" ini="" section="" property="" contains=""/>

Copy full snippet
```

Integer variables can use these arithmetic operations:

```
	<setIntAdd result="" arg1="" arg2=""/>
	<setIntSubtract result="" arg1="" arg2=""/>
	<setIntMultiply result="" arg1="" arg2=""/>
	<setIntDivide result="" arg1="" arg2=""/>

Copy full snippet
```

You can manipulate strings with the following:

```
	<setStringAdd result="" arg1="" arg2=""/>
	<setStringSubstring result="" source="" start="" length=""/>
	<setStringReplace result="" source="" find="" with=""/>
Copy full snippet
```

String length can be retrieved with:

```
	<setIntLength result="" source=""/>

Copy full snippet
```

The index of a search string can be found in source with:

```
	<setIntFindString result="" source="" find=""/>

Copy full snippet
```

The following shortcut string comparisons can also be used instead of using `<setIntFindString>` and checking the result:

```
	<setBoolStartsWith result="" source="" find=""/>
	<setBoolEndsWith result="" source="" find=""/>
	<setBoolContains result="" source="" find=""/>

Copy full snippet
```

## Writing Messages

Messages are written to the log with this node:

```
	<log text=""/>
Copy full snippet
```

## Conditional Execution

Conditional execution uses the following form:

```
	<if condition="">
		<true>
			<-- Executes if boolean variable if the condition is true -->
		</true>
		<false>
			<-- executes if boolean variable in condition is false -->
		</false>
	</if>
Copy full snippet
```

The `<true>` and `<false>` blocks are optional. The condition must be in a boolean variable. The boolean operator nodes may be combined to create a final state for more complex conditions:

```
	<setBoolNot result="notDistribution" source="$B(Distribution)/>
	<setBoolIsEqual result="isX86" arg1="$S(Architecture)" arg2="x86"/>
	<setBoolIsEqual result="isX86_64" arg2="$S(Architecture)" arg2="x86_64/">
	<setBoolOr result="isIntel" arg1="$B(isX86)" arg2="$B(isX86_64)"/>
	<setBoolAnd result="intelAndNotDistribution" arg1="$B(isIntel)" arg2="$B(notDistribution)"/>
	<if condition="intelAndNotDistribution">
		<true>
			<-- do something for Intel if not a distribution build -->
		</true>
	</if>
Copy full snippet
```

The "isIntel" could also be done like this:

```
	<setStringSubstring result="subarch" source="$S(Architecture)" start="0" length="3"/>
	<setBoolEquals result="isIntel" arg1="$S(subarch)" arg2="x86"/>
Copy full snippet
```

Two shortcut nodes are available for conditional execution:
The following code:

```
	<isArch arch="armeabi-armv7">
		<-- do stuff -->
	</isArch>
Copy full snippet
```

Is the equivalent of:

```
	<setBoolEquals result="temp" arg1="$S(Architecture)" arg2="armeabi-armv7">
	<if condition="temp">
		<true>
			<-- do stuff -->
		</true>
	</if>
Copy full snippet
```

The following code:

```
	<isDistribution> blah
		<-- do stuff -->
	</isDistribution>
Copy full snippet
```

Is the equivalent of:

```
	<if condition="Distribution">
		<-- do stuff -->
	</if>
Copy full snippet
```

Execution can be stopped with:

```
	<return/>

Copy full snippet
```

## Loops

Loops can be created using these nodes:

```
	<while condition="">
		<-- do stuff -->
	</while>
	<break/>
	<continue/>
Copy full snippet
```

The `<while>` body will execute until the condition is false or a `<break/>` is hit. The `<continue></continue>` will restart execution of the loop if the condition is still true or exit.

`<break/>` outside a `<while>` body will act the same as `<return></return>`.

Here is an example loop which writes 1 to 5 to the log, skipping 3. Note the update of the while condition should be done before the continue otherwise it may not exit.

```
	<setInt result="index" value="0"/>
	<setBool result="loopRun" value="true"/>
	<while condition="loopRun">
		<setIntAdd result="index" arg1="$I(index)" arg2="1"/>
		<setBoolIsLess result="loopRun" arg1="$I(index)" arg2="5"/>
		<setBoolIsEqual result="indexIs3" arg1="$I(index)" arg2="3"/>
		<if condition="indexIs3">
			<true>
				<continue/>
			</true>
		</if>
		<log text="$I(index)"/>
	</while>
Copy full snippet
```

It is possible to use variable replacement in generating the result variable name as well. This makes the creation of arrays in loops possible:

```
	<setString result="array_$I(index)" value="element $I(index) in array"/>
Copy full snippet
```

This may be retrieved using the following (value is treated as the variable name):

```
	<setStringFrom result="out" value="array_$I(index)"/>
Copy full snippet
```

It is possible to use variable replacement in generating the result variable name as well. This makes the creation of arrays in loops possible:

```
	<setString result="array_$I(index)" value="element $I(index) in array"/>
Copy full snippet
```

This may be retrieved using the following (value is treated as the variable name):

```
	<setStringFrom result="out" value="array_$I(index)"/>
Copy full snippet
```

For boolean and integer types, you can use `<setBoolFrom>` and `<setIntFrom>`.

## Inserting Text

Nodes for inserting text into the section are as follows:

```
	<insert> body </insert>
	<insertNewline/>
	<insertValue value=""/>
	<loadLibrary name="" failmsg=""/>
Copy full snippet
```

The first one will insert either text or nodes into the returned section string. Please note you must use escaped characters for:

```
	< = <
	> = >
	& = &
Copy full snippet
```

`<insertValue value="" /pre>` - Evaluates variables in value before insertion. If value contains double quote ("), you must escape it with quote.
`<loadLibrary name="" failmsg="">` -Is a shortcut to insert a system.LoadLibrary try/catch block with an optional logged message for failure to load case.

## Search and Replace

You can do a search and replace in the Output with:

```
	<replace find="" with=""/>

Copy full snippet
```

You can also manipulate the actual $S(Output) directly, the above are more efficient:

```
	<setStringAdd result="Input" arg1="$S(Output)" arg2="sample\n"/>
	<setStringReplace result="Input" source="$S(Output)" find=".LAUNCH" with=".INFO"/>

Copy full snippet
```

## XML Manipulation

XML manipulation uses the following nodes:

```
	<addElement tag="" name=""/>
	<addElements tag=""> body </addElements>
	<removeElement tag=""/>
	<setStringFromTag result="" tag=""/>
	<setStringFromAttribute result="" tag="" name=""/>
	<setStringFromTagText result="" tag=""/>
	<addAttribute tag="" name="" value=""/>
	<removeAttribute tag="" name=""/>
	<loopElements tag=""> instructions </loopElements>

Copy full snippet
```

The current element is referenced with tag="$". Element variables are referenced with $varname since using $E(varname) will be expanded to the string equivalent of the XML. The **addElement**, **addElements**, and **removeElement** by default are applied to all matching tags. An optional `once="true"` attribute may be added to only apply to first matching tag.

The `<uses-permission>`, `<uses-feature>`, and `<uses-library>` are updated with:

```
	<addPermission android:name="" .. />
	<addFeature android:name="" .. />
	<addLibrary android:name="" .. />
Copy full snippet
```

Any attributes in the above commands are copied to the element added to the manifest so you can do the following, for example:

```
	<addFeature android:name="android.hardware.usb.host" android:required="true"/>
Copy full snippet
```

## Copying of Files

Finally, these nodes allow copying of files useful for staging jar and so files:

```
	<copyFile src="" dst="" force=""/>
	<copyDir src="" dst="" force=""/>
Copy full snippet
```

If force is false the file(s) are replaced only if length or timestamp don't match. The default for this is true.

The following should be used as the base for the src and dst paths:

```
	$S(PluginDir) = directory the XML file was loaded from
		$S(EngineDir) = engine directory
	$S(BuildDir) = project's platform appropriate build directory
Copy full snippet
```

While it is possible to write outside the APK directory, it is not recommended.

## Removing FIles

If you must remove files (like development-only files from distribution builds) you can use this node:

```
	<deleteFiles filespec=""/>
Copy full snippet
```

It is restricted to only removing files from the BuildDir. Here is example usage to remove the Oculus Signature Files (osig) from the assets directory:

```
	<deleteFiles filespec="assets/oculussig_*"/>
Copy full snippet
```

## Packaging or Deploying

The following sections are evaluated during the packaging or deploy stages:

```
	For all platforms
	<-- init section is always evaluated once per architecture -->
		<init> </init>
	Android Specific sections
			<--  optional updates applied to AndroidManifest.xml -->
		<androidManifestUpdates> </androidManifestUpdates>
			<--  optional additions to proguard -->
		<proguardAdditions>    </proguardAdditions>
			<--  optional AAR imports additions -->
		<AARImports> </AARImports>
			<--  optional base build.gradle additions -->
		<baseBuildGradleAdditions>  </baseBuildGradleAdditions>
			<--  optional base build.gradle buildscript additions -->
		<buildscriptGradleAdditions>  </buildscriptGradleAdditions>
			<--  optional app build.gradle additions -->
		<buildGradleAdditions>  </buildGradleAdditions>
			<--  optional additions to generated build.xml before ${sdk.dir}/tools/ant/build.xml import -->
		<buildXmlPropertyAdditions> </buildXmlPropertyAdditions>
			<--  optional files or directories to copy or delete from Intermediate/Android/APK before ndk-build -->
		<prebuildCopies> </prebuildCopies>
			<-- optional files or directories to copy or delete from Intermediate/Android/APK after ndk-build -->
		<resourceCopies> </resourceCopies>
			<-- optional files or directories to copy or delete from Intermediate/Android/APK before Gradle -->
		<gradleCopies> </gradleCopies>
			<-- optional properties to add to gradle.properties -->
		<gradleProperties> </gradleProperties>
			<-- optional parameters to add to Gradle commandline (prefix with a space or will run into previous parameter(s)) -->
		<gradleParameters> </gradleParameters>
			<-- optional minimum SDK API level required -->
		<minimumSDKAPI> </minimumSDKAPI>
			<-- optional additions to the GameActivity imports in GameActivity.java -->
		<gameActivityImportAdditions> </gameActivityImportAdditions>
		<-- optional additions to the GameActivity after imports in GameActivity.java -->
		<gameActivityPostImportAdditions> </gameActivityPostImportAdditions>
			<-- optional additions to the GameActivity class implements in GameActivity.java (end each line with a comma) -->
		<gameActivityImplementsAdditions> </gameActivityImplementsAdditions>
			<-- optional additions to the GameActivity class body in GameActivity.java -->
		<gameActivityClassAdditions> </gameActivityOnClassAdditions>
			<-- optional additions to GameActivity onCreate metadata reading in GameActivity.java -->
		<gameActivityReadMetadata> </gameActivityReadMetadata>
		<-- optional additions to GameActivity onCreate in GameActivity.java -->
		<gameActivityOnCreateAdditions> </gameActivityOnCreateAdditions>
			<-- optional additions to GameActivity onDestroy in GameActivity.java -->
		<gameActivityOnDestroyAdditions> </gameActivityOnDestroyAdditions>
			<-- optional additions to GameActivity onStart in GameActivity.java -->
		<gameActivityOnStartAdditions> </gameActivityOnStartAdditions>
			<-- optional additions to GameActivity onStop in GameActivity.java -->
		<gameActivityOnStopAdditions> </gameActivityOnStopAdditions>
			<-- optional additions to GameActivity onPause in GameActivity.java -->
		<gameActivityOnPauseAdditions> </gameActivityOnPauseAdditions>
			<-- optional additions to GameActivity onResume in GameActivity.java -->
		<gameActivityOnResumeAdditions>    </gameActivityOnResumeAdditions>
			<-- optional additions to GameActivity onNewIntent in GameActivity.java -->
		<gameActivityOnNewIntentAdditions> </gameActivityOnNewIntentAdditions>
			<-- optional additions to GameActivity onActivityResult in GameActivity.java -->
		<gameActivityOnActivityResultAdditions>    </gameActivityOnActivityResultAdditions>
			<-- optional libraries to load in GameActivity.java before libUE4.so -->
		<soLoadLibrary>    </soLoadLibrary>

Copy full snippet
```

## Supported Nodes

Here is the complete list of supported nodes:

```
	<isArch arch="">
	<isDistribution>
	<if> => <true> / <false>
	<while condition="">
	<return/>
	<break/>
	<continue/>
	<log text=""/>
	<insert> </insert>
	<insertValue value=""/>
	<replace find="" with""/>
	<copyFile src="" dst=""/>
	<copyDir src="" dst=""/>
	<loadLibrary name="" failmsg=""/>
	<setBool result="" value=""/>
	<setBoolEnvVarDefined result="" value=""/>
	<setBoolFrom result="" value=""/>
	<setBoolFromProperty result="" ini="" section="" property="" default=""/>
	<setBoolFromPropertyContains result="" ini="" section="" property="" contains=""/>
	<setBoolNot result="" source=""/>
	<setBoolAnd result="" arg1="" arg2=""/>
	<setBoolOr result="" arg1="" arg2=""/>
	<setBoolIsEqual result="" arg1="" arg2=""/>
	<setBoolIsLess result="" arg1="" arg2=""/>
	<setBoolIsLessEqual result="" arg1="" arg2=""/>
	<setBoolIsGreater result="" arg1="" arg2=""/>
	<setBoolIsGreaterEqual result="" arg1="" arg2=""/>
	<setInt result="" value=""/>
	<setIntFrom result="" value=""/>
	<setIntFromProperty result="" ini="" section="" property="" default=""/>
	<setIntAdd result="" arg1="" arg2=""/>
	<setIntSubtract result="" arg1="" arg2=""/>
	<setIntMultiply result="" arg1="" arg2=""/>
	<setIntDivide result="" arg1="" arg2=""/>
	<setIntLength result="" source=""/>
	<setIntFindString result="" source="" find=""/>
	<setString result="" value=""/>
	<setStringFrom result="" value=""/>
	<setStringFromEnvVar result="" value=""/>
	<setStringFromProperty result="" ini="" section="" property="" default=""/>
	<setStringAdd result="" arg1="" arg2=""/>
	<setStringSubstring result="" source="" index="" length=""/>
	<setStringReplace result="" source="" find="" with=""/>
Copy full snippet
```

* [reference](https://dev.epicgames.com/community/search?query=reference)
* [mobile](https://dev.epicgames.com/community/search?query=mobile)
* [android](https://dev.epicgames.com/community/search?query=android)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Enable Tracing](/documentation/en-us/unreal-engine/using-the-unreal-plugin-language-for-mobile-projects-in-unreal-engine?application_version=5.7#enabletracing)
* [Variable Types](/documentation/en-us/unreal-engine/using-the-unreal-plugin-language-for-mobile-projects-in-unreal-engine?application_version=5.7#variabletypes)
* [Variable Manipulation](/documentation/en-us/unreal-engine/using-the-unreal-plugin-language-for-mobile-projects-in-unreal-engine?application_version=5.7#variablemanipulation)
* [Writing Messages](/documentation/en-us/unreal-engine/using-the-unreal-plugin-language-for-mobile-projects-in-unreal-engine?application_version=5.7#writingmessages)
* [Conditional Execution](/documentation/en-us/unreal-engine/using-the-unreal-plugin-language-for-mobile-projects-in-unreal-engine?application_version=5.7#conditionalexecution)
* [Loops](/documentation/en-us/unreal-engine/using-the-unreal-plugin-language-for-mobile-projects-in-unreal-engine?application_version=5.7#loops)
* [Inserting Text](/documentation/en-us/unreal-engine/using-the-unreal-plugin-language-for-mobile-projects-in-unreal-engine?application_version=5.7#insertingtext)
* [Search and Replace](/documentation/en-us/unreal-engine/using-the-unreal-plugin-language-for-mobile-projects-in-unreal-engine?application_version=5.7#searchandreplace)
* [XML Manipulation](/documentation/en-us/unreal-engine/using-the-unreal-plugin-language-for-mobile-projects-in-unreal-engine?application_version=5.7#xmlmanipulation)
* [Copying of Files](/documentation/en-us/unreal-engine/using-the-unreal-plugin-language-for-mobile-projects-in-unreal-engine?application_version=5.7#copyingoffiles)
* [Removing FIles](/documentation/en-us/unreal-engine/using-the-unreal-plugin-language-for-mobile-projects-in-unreal-engine?application_version=5.7#removingfiles)
* [Packaging or Deploying](/documentation/en-us/unreal-engine/using-the-unreal-plugin-language-for-mobile-projects-in-unreal-engine?application_version=5.7#packagingordeploying)
* [Supported Nodes](/documentation/en-us/unreal-engine/using-the-unreal-plugin-language-for-mobile-projects-in-unreal-engine?application_version=5.7#supportednodes)
