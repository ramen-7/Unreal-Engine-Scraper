<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-use-android-manifest-control-in-unreal-engine-projects?application_version=5.7 -->

# Android Manifest Control

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
6. [Android Support](/documentation/en-us/unreal-engine/android-support-for-unreal-engine "Android Support")
7. [Android Development Guides](/documentation/en-us/unreal-engine/developing-guides-for-android-in-unreal-engine "Android Development Guides")
8. Android Manifest Control

# Android Manifest Control

Setting up and using the Android Mainfest file.

![Android Manifest Control](https://dev.epicgames.com/community/api/documentation/image/6f4fabc0-bde4-4a9d-98fe-ee92816950a2?resizing_type=fill&width=1920&height=335)

 On this page

The `AndroidManifest.xml` file is used to store various Android system permissions and settings that are set in the **Advanced APK Packaging** section of your **Projects Settings**. The following document shows how you can input commands that will be added to the `AndroidManifest.xml` file to meet the needs of your **Unreal Engine** (UE) project.

## Android Manifest Location

Before you can locate the `AndroidManifest.xml` file for your project, you will first need to either package the project or deploy the project to your Android device. Once the project has been built or deployed you will then find the `AndroidManifest.xml` file in `(YourProjectName)\\Intermediate\Android\arm64`.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a44b76ec-c524-4d26-aefc-22126c66c50b/ue5_1-01-file-location.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/a44b76ec-c524-4d26-aefc-22126c66c50b/ue5_1-01-file-location.png)

Click for full image.

You should **never** edit the `AndroidManifest.xml` file under any circumstances. Any edits that need to be made to the `AndroidManifest.xml` file should be done inside the UE Editor in the Advanced APK Packing section.

## Android Manifest Layout

In a typical `AndroidManifest.xml` file you will find the following three sections.

* **Application Definition**
* **Activity**
* **Requirements**

  ```
            <manifest xmlns:android="http://schemas.android.com/apk/res/android"
                package="com.YourCompany.Project"
                android:versionCode="1"
                android:versionName="1.0.">
  		
                <-- Application Definition -->
                <application android:label="@string/app_name" android:icon="@drawable/icon" android:hasCode="true">
                 <activity android:name="com.epicgames.unreal.GameApplication"
                 </activity>
                </application>
  		
                 <-- Requirements -->
                 <uses-sdk android:minSdkVersions="9"/>
                 <uses-feature android android:glEsVersion="0x00020000" android:required="true" />
                 <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
            </manifest>
  		
  Copy full snippet
  ```

Please note that the above Android Manifest file is not a working manifest file and is only shown for reference purposes.

## Extra Tags for Manifest

Navigate to **Extra Tags for <manifest> node** in the **Advanced APK Packaging** section. You can add additional tags for the Manifest by clicking on the **Plus** sign icon to add a new element to the tags array and then inputting the tag or tags you want to use into the input box. For this example the following tag was used, **android:sharedUserId="Foo"**.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8c9e3848-856a-42ff-8afd-80e636443334/ue5_1-02-extra-man-tags.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/8c9e3848-856a-42ff-8afd-80e636443334/ue5_1-02-extra-man-tags.png)

Click for full image.

Tags that are input into the **Extra Tags for <manifest> node** section will be added to the **manifest** section of the `AndroidManifest.xml` file.

```
	<manifest xmlns:android="http://schemas.android.com/apk/res/android"
		package="com.YourCompany.Project"
		android:sharedUserId="Foo"
		android:versionCode="1"
		android:versionName="1.0">
Copy full snippet
```

## Extra Tags for Application

Navigate to **Extra Tags for <application> node** in the **Advanced APK Packaging** section. You can add additional tags for the Application by clicking on the **Plus** sign icon to add a new element to the Application array and then inputting the tag you want to use. For this example the following tag was used, **android:hardwareAccelerated="True"**.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e50f9925-9946-41eb-9189-510d35e7da25/ue5_1-03-extra-app-tags.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/e50f9925-9946-41eb-9189-510d35e7da25/ue5_1-03-extra-app-tags.png)

Click for full image.

Items that are input into the **Extra Tags for <application> node** section will be added to the **Application Definition** section of the `AndroidManifest.xml` file.

```
	
	<application android:label="@string/app_name"
	 android:icon="@drawable/icon"
	 android:hardwareAccelerated="True"
	 android:hasCode="true">
Copy full snippet
```

## Extra Settings for Application

Navigate to **Extra Settings for <application> section (\n to separate lines)** in the **Advanced APK Packaging** section. You can add additional settings for the Application to use by inputting the settings you want to use into the **Extra Settings for**  section. If you have more than one setting you want to use, separate each setting by adding **\n**. For this example the the following two items were added, **android:banner="Foo"** and **android:vmSafeMode="True"**.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/87bf596b-d305-4110-a722-d075873826c8/ue5_1-04-extra-app-settings.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/87bf596b-d305-4110-a722-d075873826c8/ue5_1-04-extra-app-settings.png)

Click for full image.

Items that are input into the **Extra Settings for <application>** section will be added to the **Activity** section of the `AndroidManifest.xml` file.

```
		</activity>
		<activity android:name=".DownloaderActivity" android:screenOrientation="sensorLandscape" android:configChanges="mcc|mnc|uiMode|density|screenSize|orientation|keyboardHidden|keyboard" android:theme="@style/UnrealSplashTheme" />
		<meta-data android:name="com.epicgames.unreal.GameActivity.DepthBufferPreference" android:value="0" />
		<meta-data android:name="com.epicgames.unreal.GameActivity.bPackageDataInsideApk" android:value="false" />
		<meta-data android:name="com.epicgames.unreal.GameActivity.bVerifyOBBOnStartUp" android:value="false" />
		<meta-data android:name="com.epicgames.unreal.GameActivity.bShouldHideUI" android:value="true" />
		<meta-data android:name="com.epicgames.unreal.GameActivity.ProjectName" android:value="AndroidProject" />
		<meta-data android:name="com.epicgames.unreal.GameActivity.bHasOBBFiles" android:value="true" />
		<meta-data android:name="com.epicgames.unreal.GameActivity.bSupportsVulkan" android:value="true" />
		<meta-data android:name="com.google.android.gms.games.APP_ID" android:value="@string/app_id" />
		<meta-data android:name="com.google.android.gms.version" android:value="@integer/google_play_services_version" />
		<activity android:name="com.google.android.gms.ads.AdActivity" android:configChanges="keyboard|keyboardHidden|orientation|screenLayout|uiMode|screenSize|smallestScreenSize" />
				android:banner="Foo"
				 android:vmSafeMode="True"
				<service android:name="OBBDownloaderService" /><receiver android:name="AlarmReceiver" /></application>
Copy full snippet
```

## Extra Tags for com.epicgames.unreal Game Activity

You can add additional tags for the **Extra Tags for com.epicgames.unreal.GameActivity activity node** by clicking on the **Plus** sign icon to add a new element to the **Extra Tags for com.epicgames.unreal.GameActivity  node** array and then inputting the tag you want to use.

[![undefined](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7a21a0a4-aa56-48ca-b4f6-92cb4e236cab/ue5_1-05-extra-ue-tags.png)](https://d1iv7db44yhgxn.cloudfront.net/documentation/images/7a21a0a4-aa56-48ca-b4f6-92cb4e236cab/ue5_1-05-extra-ue-tags.png)

Click for full image.

* [development](https://dev.epicgames.com/community/search?query=development)
* [mobile](https://dev.epicgames.com/community/search?query=mobile)
* [android](https://dev.epicgames.com/community/search?query=android)
* [manifest](https://dev.epicgames.com/community/search?query=manifest)
* [distribution](https://dev.epicgames.com/community/search?query=distribution)
* [platform delivery](https://dev.epicgames.com/community/search?query=platform%20delivery)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Android Manifest Location](/documentation/en-us/unreal-engine/how-to-use-android-manifest-control-in-unreal-engine-projects?application_version=5.7#androidmanifestlocation)
* [Android Manifest Layout](/documentation/en-us/unreal-engine/how-to-use-android-manifest-control-in-unreal-engine-projects?application_version=5.7#androidmanifestlayout)
* [Extra Tags for Manifest](/documentation/en-us/unreal-engine/how-to-use-android-manifest-control-in-unreal-engine-projects?application_version=5.7#extratagsformanifest)
* [Extra Tags for Application](/documentation/en-us/unreal-engine/how-to-use-android-manifest-control-in-unreal-engine-projects?application_version=5.7#extratagsforapplication)
* [Extra Settings for Application](/documentation/en-us/unreal-engine/how-to-use-android-manifest-control-in-unreal-engine-projects?application_version=5.7#extrasettingsforapplication)
* [Extra Tags for com.epicgames.unreal Game Activity](/documentation/en-us/unreal-engine/how-to-use-android-manifest-control-in-unreal-engine-projects?application_version=5.7#extratagsforcomepicgamesunrealgameactivity)
