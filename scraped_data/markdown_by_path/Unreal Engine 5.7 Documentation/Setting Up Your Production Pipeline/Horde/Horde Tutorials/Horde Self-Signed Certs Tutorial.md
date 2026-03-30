<!-- source: https://dev.epicgames.com/documentation/en-us/unreal-engine/horde-self-signed-certs-tutorial-for-unreal-engine?application_version=5.7 -->

# Horde Self-Signed Certs Tutorial

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
8. Horde Self-Signed Certs Tutorial

# Horde Self-Signed Certs Tutorial

A tutorial on using self-signed certs with Horde for Unreal Engine.

![Horde Self-Signed Certs Tutorial](https://dev.epicgames.com/community/api/documentation/image/3240ca25-4557-4d56-8053-ff6a7085332e?resizing_type=fill&width=1920&height=335)

 On this page

## Introduction

When deploying Horde in production environments, it is recommended to use a verified signing certificate.

For testing scenarios, if can be useful to install a self-signed certificate.

Using self-signed certificates circumvents basic security measures. Do not use this technique in production environments.

## Server

1. From an administrator PowerShell prompt, add a certificate to the "Personal" store for the local machine by running:

   ```
        New-SelfSignedCertificate -CertStoreLocation 'Cert:\LocalMachine\My' -DnsName 'my-domain.com'
   Copy full snippet
   ```
2. Open the Certificate Manager MMC snap-in by running `certmgr.msc` from the Windows 'Run' menu. You should see the certificate created above in the `Personal\Certificates` section.

   Select the certificate and press Ctrl+C. Navigate to the 'Trusted Root Authorities\Certificates' section, and press Ctrl+V to create a copy.
3. Open the [server.json](/documentation/en-us/unreal-engine/horde-orientation-for-unreal-engine) file, and uncomment the `HttpsPort` line:

   ```
        "HttpsPort": 13341,
   Copy full snippet
   ```

   ...as well as the certificate section at the bottom of the file - updating the subject name to the DNS name on the certificate created above.

   ```
    "Kestrel":
    {
        "Certificates":
        {
            "Default":
            {
                "Subject": "my-domain.com",
                "Store": "My",
                "Location": "LocalMachine"
            }
        }
    }
   Copy full snippet
   ```
4. Restart the server. You should be able to connect over HTTPS from a browser on the same machine on port 13341.

## Clients

1. Browse to the server specified above on the HTTPS URL. On the warning dialog about the server having an invalid certificate, choose to export it to a file.

   On **Google Chrome**, this can be accessed by clicking on the "Not Secure" button in the address bar, selecting "Certificate is not valid", switching to the "Details" tab in the certificate browse, and chosing "Export". Select 'Base-64 Encoded ASCII' as the file type, and save the file.

   The certificate may also be exported directly from the Certificate Manager MMC snap-in.
2. Locate the exported certificate file in Windows Explorer, right click on it, and choose "Install Certificate". When prompted, choose to import the certificate in to the "Trusted Root Certificates" store.

* [horde](https://dev.epicgames.com/community/search?query=horde)
* [bronze](https://dev.epicgames.com/community/search?query=bronze)

---

Ask questions and help your peers [Developer Forums](https://forums.unrealengine.com/categories?tag=unreal-engine)

Write your own tutorials or read those from others [Learning Library](https://dev.epicgames.com/community/unreal-engine/learning)

On this page

* [Introduction](/documentation/en-us/unreal-engine/horde-self-signed-certs-tutorial-for-unreal-engine?application_version=5.7#introduction)
* [Server](/documentation/en-us/unreal-engine/horde-self-signed-certs-tutorial-for-unreal-engine?application_version=5.7#server)
* [Clients](/documentation/en-us/unreal-engine/horde-self-signed-certs-tutorial-for-unreal-engine?application_version=5.7#clients)
